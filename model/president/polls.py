"""Polling averages as of a date (D = Democrat, R = Republican, K = named third-party candidate).

  1. Static poll weight from sample size, pollster rating, firm crowding, tracking flag          [FIT]
  2. Likely-voter adjustment from polls publishing both versions, zero prior                    [SB]
     Third-party adjustment: where a poll omits the named third-party candidate, impute him       [SB]
  3. Iterate trendline (national + de-leaned state polls) <-> per-firm house effects             [SB]
  4. Trend adjustment scaled by elasticity; convention-bounce deflation by field date            [SB]
     (applied after the trendline, as in Silver's model, so a fading bounce lingers in older polls)
  5. Average with influence = weight x recency (window stretches where polling is thin)          [FIT]
  6. Landmark events: for ~2 weeks after a convention, blend in the pre-convention average        [SB]
     Political time: landmark events are leaps ahead in time for recency and the trendline         [SB]
     kamala_mode: only Harris-Trump polls fielded from June 28, 2024                               [SB]
"""
import numpy as np
import pandas as pd

from . import config as C

CANDS = ("D", "R")


def _days(ts, ref):
    return (ts - ref).dt.total_seconds().to_numpy() / 86400.0


def political_days(dates, cycle, ref="2000-01-01"):
    """Calendar days since `ref` plus the jumps of landmark events on or before each date  [SB]."""
    d = pd.to_datetime(pd.Series(dates))
    out = _days(d, pd.Timestamp(ref))
    for day, kind in C.CYCLES[cycle].get("events", []):
        out = out + C.EVENT_JUMP_DAYS[kind] * (d >= pd.Timestamp(day)).to_numpy()
    return out


def political_days_left(asof, cycle):
    eday = pd.Timestamp(C.ELECTION_DAYS[cycle])
    a, e = political_days([pd.Timestamp(asof), eday], cycle)
    return float(e - a)


def local_linear(grid, t, y, w, h):
    """Gaussian-kernel local linear regression on a grid (slope lightly penalised)."""
    d = t[None, :] - grid[:, None]
    k = w[None, :] * np.exp(-0.5 * (d / h) ** 2)
    s0, s1, s2 = k.sum(1), (k * d).sum(1), (k * d * d).sum(1)
    t0, t1 = (k * y).sum(1), (k * d * y).sum(1)
    s2r = s2 + 0.25 * s0 * h * h
    det = s0 * s2r - s1 * s1
    with np.errstate(invalid="ignore", divide="ignore"):
        a = (s2r * t0 - s1 * t1) / det
        a = np.where(np.isfinite(a) & (s0 > 1e-9), a, t0 / np.maximum(s0, 1e-12))
    return a


def static_weights(p):
    W = C.WEIGHT
    p["nfirm"] = p.groupby(["geo", "pollster"]).poll_id.transform("count")
    ppm = p.ppm.fillna(W["ppm_unrated"])
    p["weight"] = np.exp(W["intercept"] + W["log_n"] * np.log(p.n.clip(lower=100)) + W["ppm"] * ppm
                         + W["log_nfirm"] * np.log(p.nfirm) + W["tracking"] * p.tracking.astype(float))
    return p


def lv_adjustment(lv_pairs, asof):
    pairs = lv_pairs[lv_pairs.created < asof]
    k = C.LV_PRIOR_POLLS
    return {"D": pairs.dD.sum() / (len(pairs) + k), "R": pairs.dR.sum() / (len(pairs) + k), "pairs": len(pairs)}


def bounce(mid, cycle):
    """Convention-bounce inflation of the D-minus-R margin for polls fielded at `mid`."""
    cfg = C.CYCLES[cycle]
    b = np.zeros(len(mid))
    for start, end, party in cfg["conventions"]:
        d_after = (mid - pd.Timestamp(end)).dt.days.to_numpy()
        on = (mid >= pd.Timestamp(start)).to_numpy()
        size = cfg["bounce_peak"] * np.clip(1 - np.maximum(d_after, 0) / C.BOUNCE_DAYS, 0, 1) * on
        b += np.where(party == "D", size, -size)
    return b


def _recency(p, asof, days_left, cycle):
    R = C.RECENCY
    age = political_days([asof], cycle)[0] - political_days(p.end, cycle)      # age in political time  [SB]
    n30 = p[age <= 30].groupby("geo").size()
    base = R["window_days"] + R["early_stretch"] * max(0, days_left - 10)
    window = np.clip(base * np.sqrt(R["sparse_ref_polls"] / np.maximum(p.geo.map(n30).fillna(0).to_numpy(), 1)),
                     base, max(base, R["max_window_days"]))
    return np.clip(1 - age / window, 0, None) ** R["power"]


def build(polls, lv_pairs, geo, asof, cycle, landmarks=True):
    asof = pd.Timestamp(asof)
    cfg = C.CYCLES[cycle]
    if landmarks:
        for start, end, days in cfg["landmarks"]:
            since = (asof - pd.Timestamp(end)).days
            if 0 < since <= days:
                b = build(polls, lv_pairs, geo, asof, cycle, landmarks=False)
                a = build(polls, lv_pairs, geo, start, cycle, landmarks=False)
                wb = since / days
                cols = [c for c in ("D", "R", "K") if c in b["avg"]]
                aa = a["avg"].reindex(b["avg"].index)
                for c in cols:
                    b["avg"][c] = np.where(aa[c].notna(), wb * b["avg"][c] + (1 - wb) * aa[c], b["avg"][c])
                b["landmark_weight_current"] = wb
                return b
    days_left = (pd.Timestamp(C.ELECTION_DAYS[cycle]) - asof).days
    p = polls[(polls.created < asof) & (polls.end < asof)].copy()
    if cfg.get("poll_start_min"):
        p = p[p.start >= pd.Timestamp(cfg["poll_start_min"])]
    p = p.reset_index(drop=True)
    p = static_weights(p)
    elast = p.geo.map(geo.elasticity).fillna(1.0).to_numpy().copy()
    elast[p.geo.to_numpy() == "US"] = 1.0
    p["recency"] = _recency(p, asof, days_left, cycle)
    p["influence"] = p.weight * p.recency

    # 2. likely voters; named third-party candidate
    lv = lv_adjustment(lv_pairs, asof)
    needs = p.population.isin(["rv", "a"]).to_numpy()
    for c in CANDS:
        p[f"lv_{c}"] = p[c] + np.where(needs, lv[c], 0.0)
    n3 = cfg["n3pc"]
    k_avg = None
    if n3 and asof < pd.Timestamp(n3["until"]) and p.K.notna().any():
        has = p.K.notna()
        inf = p.influence.where(has, 0.0)
        k_nat = np.average(p.K[has], weights=np.maximum(inf[has], 1e-6))
        num = (inf * p.K.fillna(0)).groupby(p.geo).sum()
        den = inf.groupby(p.geo).sum()
        k_avg = (num + 2.0 * k_nat) / (den + 2.0)
        k_hat = p.geo.map(k_avg).fillna(k_nat).to_numpy()
        share = C.N3PC["draw_share_from_major"]
        for c in CANDS:
            p[f"lv_{c}"] -= np.where(has, 0.0, share * k_hat / 2)
        p["K_imputed"] = np.where(has, p.K, k_hat)

    # 3. trendline <-> house effects
    origin = p.mid.min().normalize()
    cal_grid = origin + pd.to_timedelta(np.arange(0, (asof - origin).days + 1), "D")
    t = political_days(p.mid, cycle)                    # trendline runs on political time  [SB]
    grid = political_days(cal_grid, cycle)
    is_nat = (p.geo == "US").to_numpy()
    w = p.weight.to_numpy()
    T = C.TREND
    ramp = np.clip((30 - days_left) / 30, 0, 1)
    a_share = T["aggressive_share_early"] + (T["aggressive_share_late"] - T["aggressive_share_early"]) * ramp
    prior = {"D": np.select([p.partisan == "DEM", p.partisan == "REP"], [0.5, -0.5], 0.0),
             "R": np.select([p.partisan == "DEM", p.partisan == "REP"], [-0.5, 0.5], 0.0)}
    H = C.HOUSE
    he = {c: pd.Series(0.0, index=p.pollster.unique()) for c in CANDS}
    trend, lean = {}, {}
    rec_long = np.exp(-(political_days([asof], cycle)[0] - political_days(p.end, cycle)) / 60.0)
    firm = p.groupby("pollster").agg(ppm=("ppm", "first"), partisan=("partisan", lambda s: s.notna().mean()))
    for it in range(H["iterations"]):
        for c in CANDS:
            adj = p[f"lv_{c}"].to_numpy() - p.pollster.map(he[c]).to_numpy()
            if it == 0:
                m = is_nat if is_nat.sum() >= 3 else np.ones(len(p), bool)
                yv, wv = adj[m], w[m]
            else:
                ln = p.geo.map(lean[c]).fillna(0).to_numpy()
                m = np.ones(len(p), bool)
                yv = np.where(is_nat, adj, adj - ln)
                wv = np.where(is_nat, w, w * T["state_poll_discount"])
            tc = local_linear(grid, t[m], yv, wv, T["bandwidth_conservative"])
            ta = local_linear(grid, t[m], yv, wv, T["bandwidth_aggressive"])
            trend[c] = (1 - a_share) * tc + a_share * ta
            tr_at = np.interp(t, grid, trend[c])
            r = pd.Series(adj - tr_at, index=p.index)
            wl = pd.Series(w * rec_long, index=p.index)
            lean[c] = (r * wl).groupby(p.geo).sum() / wl.groupby(p.geo).sum()
            lean[c]["US"] = 0.0
            expected = tr_at + p.geo.map(lean[c]).to_numpy()
            res = p[f"lv_{c}"].to_numpy() - expected
            g = pd.DataFrame({"pollster": p.pollster, "r": res, "w": w, "prior": prior[c] * H["partisan_prior_margin"]})
            stats = g.groupby("pollster").apply(lambda x: pd.Series({
                "n": len(x), "rbar": np.average(x.r, weights=x.w), "prior": x.prior.mean()}), include_groups=False)
            k = H["shrink_polls"]
            est = (stats.n * stats.rbar + k * stats.prior) / (stats.n + k)
            core = firm[(firm.ppm.fillna(9) <= H["center_ppm_max"]) & (firm.partisan < 0.5)].index.intersection(est.index)
            if len(core):
                est = est - np.average(est[core], weights=stats.n[core])
            he[c] = est

    # 4. trend adjustment, then bounce deflation by field date
    p["bounce_adj"] = bounce(p.mid, cycle)
    for c in CANDS:
        p[f"he_{c}"] = p.pollster.map(he[c]).to_numpy()
        p[f"adj_{c}"] = p[f"lv_{c}"] - p[f"he_{c}"]
        shift = trend[c][-1] - np.interp(t, grid, trend[c])
        sign = 1 if c == "D" else -1
        p[f"ta_{c}"] = p[f"adj_{c}"] + elast * shift - sign * p.bounce_adj / 2

    # 5. averages
    g = p.groupby("geo")
    wavg = lambda col: g.apply(lambda x: np.average(x[col], weights=x.influence) if x.influence.sum() > 0 else np.nan,
                               include_groups=False)
    avg = pd.DataFrame({"D": wavg("ta_D"), "R": wavg("ta_R"), "n_eff": g.influence.sum(), "n_polls": g.size(),
                        "n_firms": g.pollster.nunique(), "bounce": wavg("bounce_adj")})
    if k_avg is not None:
        avg["K"] = k_avg.reindex(avg.index)
    trend_df = pd.DataFrame({"date": cal_grid, "D": trend["D"], "R": trend["R"]})
    house = pd.DataFrame({"D": he["D"], "R": he["R"]})
    house["margin"] = house["D"] - house["R"]
    house["polls"] = p.groupby("pollster").size()
    return {"polls": p, "avg": avg, "trend": trend_df, "house": house, "lv": lv, "asof": asof, "days_left": days_left,
            "us_volume": float(p.loc[is_nat, "influence"].sum()), "n3pc_active": k_avg is not None,
            "landmark_weight_current": 1.0}
