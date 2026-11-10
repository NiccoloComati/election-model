"""Monte Carlo simulation of Election Day outcomes (Silver's step 10).

Error components on the D-minus-R margin, all fat-tailed (t, 10 df)                 [SB]/[538]
  national drift      const x days^(1/3) x index multiplier, scaled by elasticity   [538]/[FIT]
  national error      Election Day polling miss, moves only slightly with the index  [SB]
  correlated error    random swings by demographic group and by region              [538]
  state error         larger with less polling and in small states                  [538]
Named third-party candidate: right-skewed share (national x state draws), probabilistic ballot access;
he can win contests and electoral votes                                              [SB]/[538 2016]
"""
import numpy as np
import pandas as pd

from . import config as C
from .data import REGION
from .demographics import FEATURES, profiles


def demographic_loadings(g):
    prof = profiles().reindex(g.index)[FEATURES]
    st = ~g.is_district.to_numpy()
    nat = np.average(prof[st].to_numpy(), axis=0, weights=g.turnout.to_numpy()[st])
    regions = sorted(set(REGION.values()))
    reg = np.array([[1.0 if REGION[g.loc[x, "parent"]] == r else 0.0 for r in regions] for x in g.index])
    return prof.to_numpy() - nat, reg


def _t(rng, df, size):
    return rng.standard_t(df, size) * np.sqrt((df - 2) / df)


def run(g, days_left, cycle, uncertainty_index=0.0, sims=C.SIMS, seed=C.SEED):
    E = C.ERROR
    cfg = C.CYCLES[cycle]
    rng = np.random.default_rng(seed)
    geos = list(g.index)
    n = len(geos)
    df = E["t_df"]
    mult = cfg["error_multiplier"]
    u = np.exp(E["index_kappa"] * uncertainty_index)
    elast = g.elasticity.to_numpy()
    mean = g.margin.to_numpy()
    ev = g.ev.to_numpy()

    sd_drift = E["drift_const"] * max(days_left, 0) ** (1 / 3) * u
    sd_nat = E["national"] * mult * u ** E["error_index_power"]
    national = sd_drift * _t(rng, df, sims) + sd_nat * _t(rng, df, sims)
    demo, reg = demographic_loadings(g)
    corr = (E["group_swing"] * mult * _t(rng, df, (sims, demo.shape[1]))) @ demo.T \
        + (E["region_swing"] * mult * _t(rng, df, (sims, reg.shape[1]))) @ reg.T
    sd_state = mult * np.sqrt(E["state_floor"] ** 2 + (E["state_poll_term"] / np.sqrt(1 + g.n_eff.to_numpy())) ** 2
                              + (E["small_state_extra"] ** 2) * (g.turnout.to_numpy() < 1e6))
    m = mean[None, :] + elast[None, :] * national[:, None] + corr + sd_state * _t(rng, df, (sims, n))

    other = g.other.to_numpy()
    kp = g.K_proj.to_numpy()
    if kp.max() > 0:
        N = C.N3PC
        zn = rng.standard_normal(sims)[:, None]
        zs = rng.standard_normal((sims, n))
        k = kp[None, :] * np.exp(N["national_sd"] * zn - N["national_sd"] ** 2 / 2 + N["state_sd"] * zs - N["state_sd"] ** 2 / 2)
        parent_idx = np.array([geos.index(x) for x in g.parent])
        on = rng.random((sims, n)) < N["ballot_access"]
        k *= on[:, parent_idx]
    else:
        k = np.zeros((sims, n))
    dsh = (100 - other - k + m) / 2
    rsh = (100 - other - k - m) / 2
    kwin = k > np.maximum(dsh, rsh)
    dwin = (m > 0) & ~kwin
    rwin = (m <= 0) & ~kwin
    dev, rev, kev = (dwin * ev).sum(1), (rwin * ev).sum(1), (kwin * ev).sum(1)
    d_ec, r_ec = dev >= 270, rev >= 270

    sign = np.where(d_ec, 1.0, -1.0)
    decided = d_ec | r_ec
    score = np.where(kwin, -1e9, m * sign[:, None])
    order = np.argsort(-score, axis=1)
    cum = np.cumsum(ev[order], axis=1)
    tip = order[np.arange(sims), np.argmax(cum >= 270, axis=1)]
    tipping = np.bincount(tip[decided], minlength=n) / sims

    st = ~g.is_district.to_numpy()
    tw = g.turnout.to_numpy() * st
    pop_d = (dsh * tw).sum(1) / tw.sum()
    pop_r = (rsh * tw).sum(1) / tw.sum()
    pop_k = (k * tw).sum(1) / tw.sum()
    per_geo = pd.DataFrame({
        "label": g.label, "ev": ev, "margin": mean, "margin_p10": np.percentile(m, 10, axis=0),
        "margin_p90": np.percentile(m, 90, axis=0), "win_D": dwin.mean(0), "win_K": kwin.mean(0),
        "tipping": tipping, "D_share": dsh.mean(0), "R_share": rsh.mean(0), "K_share": k.mean(0),
        "sd_state_error": sd_state}, index=geos)
    summary = {
        "sims": sims, "days_left": days_left,
        "win_D": float(d_ec.mean()), "win_R": float(r_ec.mean()), "no_majority": float((~decided).mean()),
        "tie": float(((dev == 269) & (rev == 269)).mean()),
        "ev_D_mean": float(dev.mean()), "ev_D_p10": float(np.percentile(dev, 10)), "ev_D_p90": float(np.percentile(dev, 90)),
        "ev_K_mean": float(kev.mean()), "win_any_ev_K": float((kev > 0).mean()),
        "popvote_D": float(pop_d.mean()), "popvote_R": float(pop_r.mean()), "popvote_K": float(pop_k.mean()),
        "popvote_margin_mean": float((pop_d - pop_r).mean()), "popvote_margin_sd": float((pop_d - pop_r).std()),
        "popvote_win_D": float((pop_d > pop_r).mean()),
        "sd_drift": float(sd_drift), "sd_national_error": float(sd_nat), "uncertainty_multiplier": float(u),
    }
    ev_dist = pd.Series(np.bincount(dev.astype(int), minlength=539) / sims, name="prob")
    return summary, per_geo, ev_dist, {"margins": m, "dev": dev}
