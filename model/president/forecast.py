"""From polling averages to projected vote shares (Silver's steps 4-9), plus the run's uncertainty index.

  4-5  reserve the named third-party candidate (projected) and 'other' (lower in battlegrounds); split
       undecideds evenly                                                                       [SB]
  6    blend each state's average with a regression estimate; regression weight falls with polling   [SB]/[FIT]
       regression = rigid uniform swing + demographic regression + regional regression           [538]
                    + similar-states estimate (borrows from demographically similar polled states) [ASSUMED form]
       national margin = mostly bottom-up from state polls                                     [SB]
  7    snapshot;  8  blend with fundamentals by days left [538];  9 projected shares
"""
import numpy as np
import pandas as pd

from . import config as C
from . import economy as E
from . import fundamentals as FUND
from . import uncertainty as U
from .demographics import FEATURES, profiles


def _ridge(X, y, w, lam):
    return np.linalg.solve(X.T @ (X * w[:, None]) + lam * np.eye(X.shape[1]), X.T @ (w * y))


def regression_weight(n_eff):
    n = np.asarray(n_eff, float)
    x = np.log(np.clip(n, 0.2, None))
    w = 1 / (1 + np.exp(np.polyval(C.BLEND_CURVE, x)))
    return np.where(n <= 0, 1.0, np.clip(w, 0.0, 1.0))


def fundamentals_weight(days_left):
    d, w = zip(*C.FUNDAMENTALS_SCHEDULE)
    return float(np.interp(days_left, d, w))


def project(avg_result, geo, cycle):
    cfg = C.CYCLES[cycle]
    avg = avg_result["avg"]
    days_left = avg_result["days_left"]
    asof = avg_result["asof"]
    g = geo.join(avg, how="left")
    g["n_eff"] = g.n_eff.fillna(0.0)
    st_mask = ~g.is_district

    # named third-party candidate: projected share (fades toward Election Day)
    if avg_result["n3pc_active"]:
        k_nat = float(avg.loc["US", "K"]) if "US" in avg.index and pd.notna(avg.loc["US", "K"]) else float(np.nanmean(avg.K))
        g["K_proj"] = g.K.fillna(g.parent.map(g.K)).fillna(k_nat) * C.N3PC["projection_factor"]
    else:
        g["K_proj"] = 0.0

    # first-pass national margin (needed for the battleground discount on 'other')
    st = g[st_mask & (g.n_eff > 0)]
    m0 = np.average((st.D - st.R) - st.lean, weights=st.n_eff)
    close = np.clip(1 - np.abs(m0 + g.lean) / 10, 0, 1)
    g["other"] = g.other_prev * C.OTHER_SCALE * (1 - C.OTHER_BATTLEGROUND_DISCOUNT * close)

    # 4-5 reallocate undecided evenly
    reserve = g.other + g.K_proj
    und = 100 - g.D - g.R - reserve
    tot = g.D + g.R
    g["poll_D"] = np.where(und >= 0, g.D + und / 2, g.D * (100 - reserve) / tot)
    g["poll_R"] = np.where(und >= 0, g.R + und / 2, g.R * (100 - reserve) / tot)
    g["poll_margin"] = g.poll_D - g.poll_R

    st = g[st_mask & (g.n_eff > 0)]
    bottom_up = np.average(st.poll_margin - st.lean, weights=st.n_eff)
    if "US" in avg.index:
        nat = avg.loc["US"]
        tw = g.loc[st_mask, "turnout"]
        nat_reserve = np.average(reserve[st_mask], weights=tw)
        u = 100 - nat.D - nat.R - nat_reserve
        nat_margin = (nat.D + u / 2) - (nat.R + u / 2)
        M = C.NATIONAL_BOTTOM_UP_SHARE * bottom_up + (1 - C.NATIONAL_BOTTOM_UP_SHARE) * nat_margin
    else:
        nat_margin, M = np.nan, bottom_up

    # 6 regression estimate
    rigid = M + g.lean
    resid = (st.poll_margin - (M + st.lean)).to_numpy()
    wts = np.minimum(st.n_eff, 10.0).to_numpy()
    regions = sorted(g.region.unique())
    X = pd.get_dummies(st.region).reindex(columns=regions, fill_value=0).to_numpy(float)
    breg = _ridge(X, resid, wts, C.REGIONAL_RIDGE)
    regional = rigid + g.region.map(dict(zip(regions, breg)))
    prof = profiles().reindex(g.index)[FEATURES]
    mu = np.average(prof[st_mask], axis=0, weights=g.loc[st_mask, "turnout"])
    sd = prof[st_mask].std().to_numpy()
    Z = (prof.to_numpy() - mu) / sd
    idx = [list(g.index).index(x) for x in st.index]
    Zs = Z[idx]
    bdem = _ridge(Zs, resid, wts, C.DEMO_RIDGE)
    demographic = rigid + Z @ bdem
    # similar states: kernel in demographic space (+ region), excluding the contest itself
    S = C.SIMILAR
    d2 = ((Z[:, None, :] - Zs[None, :, :]) ** 2).mean(2)
    d2 += 0.5 * (g.region.to_numpy()[:, None] != st.region.to_numpy()[None, :])
    k = np.exp(-d2 / (2 * S["bandwidth"] ** 2)) * wts[None, :]
    for i, gi in enumerate(g.index):
        if gi in st.index:
            k[i, list(st.index).index(gi)] = 0.0
    similar = rigid + (k @ resid) / (k.sum(1) + S["ridge"])
    mix = C.REG_MIX
    g["reg_rigid"], g["reg_demographic"], g["reg_regional"], g["reg_similar"] = rigid, demographic, regional, similar
    g["reg_margin"] = (mix["rigid"] * rigid + mix["demographic"] * demographic + mix["regional"] * regional
                       + mix["similar"] * similar)

    # 6-7 snapshot
    g["w_reg"] = regression_weight(g.n_eff)
    g["snapshot_margin"] = g.w_reg * g.reg_margin + (1 - g.w_reg) * g.poll_margin.fillna(g.reg_margin)

    # 8-9 fundamentals
    F, econ = FUND.national_margin(cycle, asof)
    g["fund_margin"] = F + g.lean
    g["w_fund"] = fundamentals_weight(days_left)
    g["margin"] = (1 - g.w_fund) * g.snapshot_margin + g.w_fund * g.fund_margin
    g["D_share"] = (100 - g.other - g.K_proj + g.margin) / 2
    g["R_share"] = (100 - g.other - g.K_proj - g.margin) / 2

    # uncertainty index for this run
    ei = E.index_asof(asof, cycle)
    us = avg.loc["US"] if "US" in avg.index else pd.Series({"D": np.nan, "R": np.nan})
    k_us = float(avg.loc["US", "K"]) if avg_result["n3pc_active"] and "US" in avg.index else 0.0
    uidx, uz, urow = U.live_index(cycle, asof, avg_result["trend"], us, avg_result["us_volume"], F,
                                  ei["component_sd"], k_us)
    nat_raw = float(avg.loc["US", "D"] - avg.loc["US", "R"] + avg.loc["US", "bounce"]) if "US" in avg.index else np.nan
    info = {"national_margin_bottom_up": bottom_up, "national_margin_polls": nat_margin, "national_margin_used": M,
            "national_margin_polls_raw": nat_raw,
            "fundamentals_margin": F, "economic_index_projected": econ, "economic_index_current": ei["index_current"],
            "fundamentals_weight": g.w_fund.iloc[0],
            "uncertainty_index": uidx, "uncertainty_factors_z": uz, "uncertainty_factors": urow,
            "regional_effects": dict(zip(regions, np.round(breg, 2))),
            "demographic_effects": dict(zip(FEATURES, np.round(bdem, 2))),
            "n3pc_active": avg_result["n3pc_active"], "landmark_weight_current": avg_result["landmark_weight_current"]}
    return g, info
