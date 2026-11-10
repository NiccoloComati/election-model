"""Fundamentals: the incumbent party's national margin from the economy and incumbency  [538 2020]/[SB 2024].

  margin = d(P) x [ a + b*economy + c_tier + e*previous margin + f*(rematch x previous margin) ]
  tiers: elected incumbent president / unelected incumbent / sitting vice president / none
  d(P) = exp(-gamma (P - mean P)): more polarization -> closer margins, smaller effects   [538 2020]
  fit on elections 1880 to the previous cycle, recent elections weighted more [SB 2024]; damping and
  recency half-life chosen by leave-one-out error on post-1948 elections [FIT]
"""
import numpy as np
import pandas as pd

from . import config as C
from . import economy as E
from .history import elections

TIERS = ["elected", "unelected", "vp"]


def design(e, econ):
    X = pd.DataFrame(index=e.index)
    X["const"] = 1.0
    X["economy"] = econ.reindex(e.index)
    for t in TIERS:
        X[t] = (e.tier == t).astype(float)
    X["prev_margin"] = e.prev_inc_margin
    X["rematch_x_prev"] = e.rematch * e.prev_inc_margin
    return X


def _fit(X, y, w, damp, ridge=1.0):
    Xd = X.mul(damp, axis=0).to_numpy()
    pen = ridge * np.eye(X.shape[1])
    pen[0, 0] = 0.0
    beta = np.linalg.solve(Xd.T @ (Xd * w[:, None]) + pen, Xd.T @ (w * y))
    return beta


def training_data(last=2020):
    e = elections(C.FUNDAMENTALS["first_year"], last)
    econ = E.election_day_index()["index"]
    X = design(e, econ)
    ok = X.notna().all(1) & e.inc_margin.notna()
    return e[ok], X[ok]


def reported_targets():
    """Silver's reported 2024 fundamentals as extra observations (design rows, D margins).  [SB]"""
    from .history import elections as _el
    p24 = _el(2024, 2024).loc[2024, "polarization"]
    rows, ys = [], []
    for k, v in C.FUNDAMENTALS_REPORTED.items():
        d, who = k.split()
        tier, rem = ("elected", 1) if who == "Biden" else ("vp", 0)
        rows.append({"const": 1.0, "economy": E.index_asof(d, 2024)["index_projected"],
                     **{t: float(tier == t) for t in TIERS}, "prev_margin": 4.45, "rematch_x_prev": rem * 4.45})
        ys.append(v)
    return pd.DataFrame(rows), np.array(ys), p24


def fit(last=2020, gammas=(0, 2, 4, 6, 8), half_lives=(24, 48, 96), ridge=1.0, target_weight=None):
    """Fit the regression. Polarization damping (gamma) and the recency half-life are chosen by
    leave-one-out error on post-1948 elections [FIT]. For the 2024 model (last >= 2020), Silver's reported
    2024 fundamentals enter as extra observations, each weighted like ~2 recent elections [FIT]: history alone
    cannot pin down his incumbency tiers (only five sitting vice presidents ran since 1880)."""
    e, X = training_data(last)
    y = e.inc_margin.to_numpy()
    pbar = e.polarization.mean()
    modern = (e.index >= 1948)
    tw = C.FUNDAMENTALS["target_weight"] if target_weight is None else target_weight
    use_t = last >= 2020 and tw > 0
    if use_t:
        Xt, yt, pt = reported_targets()
        Xt = Xt[X.columns]
    best = None
    for hl in half_lives:
        w = 0.5 ** ((2024 - e.index.to_numpy()) / hl)
        for g in gammas:
            damp = np.exp(-g * (e.polarization - pbar)).to_numpy()
            XA, yA, wA, dA = X, y, w, damp
            if use_t:
                XA = pd.concat([X, Xt], ignore_index=True)
                yA = np.concatenate([y, yt])
                wA = np.concatenate([w, np.full(len(yt), tw)])
                dA = np.concatenate([damp, np.full(len(yt), np.exp(-g * (pt - pbar)))])
            loo = []
            for i in range(len(y)):
                m = np.ones(len(yA), bool)
                m[i] = False
                b = _fit(XA[m], yA[m], wA[m], dA[m], ridge)
                loo.append(float(damp[i] * X.iloc[i].to_numpy() @ b))
            loo = np.array(loo)
            rmse = float(np.sqrt(np.mean((loo - y)[modern] ** 2)))
            if best is None or rmse < best["loo_rmse_post1948"]:
                best = {"gamma": g, "half_life": hl, "loo_rmse_post1948": rmse, "loo": pd.Series(loo, index=e.index)}
    w = 0.5 ** ((2024 - e.index.to_numpy()) / best["half_life"])
    damp = np.exp(-best["gamma"] * (e.polarization - pbar)).to_numpy()
    if use_t:
        beta = _fit(pd.concat([X, Xt], ignore_index=True), np.concatenate([y, yt]),
                    np.concatenate([w, np.full(len(yt), tw)]),
                    np.concatenate([damp, np.full(len(yt), np.exp(-best["gamma"] * (pt - pbar)))]), ridge)
    else:
        beta = _fit(X, y, w, damp, ridge)
    best["used_reported_targets"] = use_t
    best.update({"beta": pd.Series(beta, index=X.columns), "pbar": pbar, "actual": e.inc_margin,
                 "fitted": pd.Series(damp * (X.to_numpy() @ beta), index=e.index), "economy": X.economy})
    return best


_MODEL = {}


def model(last=2020):
    if last not in _MODEL:
        _MODEL[last] = fit(last)
    return _MODEL[last]


def predict(year, economy, tier, prev_margin, rematch, polarization, m=None):
    m = m or model(year - 4)
    x = pd.Series({"const": 1.0, "economy": economy, **{t: float(tier == t) for t in TIERS},
                   "prev_margin": prev_margin, "rematch_x_prev": rematch * prev_margin})
    damp = np.exp(-m["gamma"] * (polarization - m["pbar"]))
    return float(damp * (x[m["beta"].index] @ m["beta"]))


def national_margin(cycle, asof, tier=None, rematch=None):
    """Fundamentals D-minus-R national margin for a cycle as of a date (economy projected to Election Day)."""
    e = elections(1880, cycle).loc[cycle]
    econ = E.index_asof(asof, cycle)["index_projected"]
    inc = predict(cycle, econ, tier or e.tier, e.prev_inc_margin, e.rematch if rematch is None else rematch,
                  e.polarization)
    sign = 1 if e.inc_party == "D" else -1
    return sign * inc, econ
