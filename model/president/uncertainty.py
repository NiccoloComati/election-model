"""Uncertainty index [538 2020]/[SB 2024] and calibration of drift and Election Day error on 1968-2024.

Factors (higher = more uncertain after signing):
  undecided, undecided + third party, polarization (-), volatility of the national average so far,
  volume of national polling (log, -), gap between polls and fundamentals, spread of economic components,
  repeat candidates (-). [NOT IMPLEMENTED] news volume (config.NOT_IMPLEMENTED["news_volume"]).
Each factor is standardized against history at the same distance from Election Day; index = mean z.
Drift SD = const x days^(1/3) x exp(kappa x index), fitted by maximum likelihood on how far national
averages moved between each date and Election Day.
"""
import json

import numpy as np
import pandas as pd
from scipy.optimize import minimize

from . import config as C
from . import economy as E
from . import fundamentals as F
from .history import elections, national_averages

FACTORS = {"undecided": 1, "undecided_third": 1, "polarization": -1, "volatility": 1, "volume": -1,
           "gap": 1, "econ_spread": 1, "repeat_candidates": -1}
HORIZONS = list(range(0, 211, 7))


def factor_rows(nat, cycle, fund_margin, econ_spread, polarization, repeat):
    """Factor values on each date of one cycle's daily national table (date, D, R, total, volume, days_left)."""
    nat = nat.sort_values("date").reset_index(drop=True)
    m = nat.D - nat.R
    rows = []
    for i, r in nat.iterrows():
        win = m[(nat.date <= r.date) & (nat.date > r.date - pd.Timedelta(days=90))]
        rows.append({"cycle": cycle, "date": r.date, "days_left": r.days_left, "margin": m[i],
                     "undecided": 100 - r.total, "undecided_third": 100 - r.D - r.R, "polarization": polarization,
                     "volatility": float(win.std()) if len(win) > 5 else np.nan, "volume": np.log1p(r.volume),
                     "gap": abs(m[i] - fund_margin), "econ_spread": econ_spread, "repeat_candidates": repeat})
    return pd.DataFrame(rows)


def historical_factors():
    nat = national_averages()
    e = elections(1880, 2024)
    econ = E.election_day_index()
    fm = F.model(2020)
    out = []
    for cyc, g in nat.groupby("cycle"):
        if cyc in fm["loo"].index:
            inc_fund = fm["loo"][cyc]
        else:
            inc_fund = F.predict(cyc, econ.loc[cyc, "index"], e.loc[cyc, "tier"], e.loc[cyc, "prev_inc_margin"],
                                 e.loc[cyc, "rematch"], e.loc[cyc, "polarization"])
        fund = inc_fund * (1 if e.loc[cyc, "inc_party"] == "D" else -1)
        spread = float(econ.loc[cyc, E.INDICATORS].std())
        f = factor_rows(g, cyc, fund, spread, e.loc[cyc, "polarization"], e.loc[cyc, "repeat_candidates"])
        f["final_margin"] = g.sort_values("date").margin.iloc[-1]
        f["actual_margin"] = e.loc[cyc, "dem_margin"]
        f["fund_margin"] = fund
        out.append(f)
    return pd.concat(out, ignore_index=True)


def standardization(h):
    """Per factor: linear fit on log(days_left + 1) across history, and residual SD."""
    params = {}
    x = np.log(h.days_left.clip(lower=0) + 1)
    for k in FACTORS:
        y = h[k]
        ok = y.notna()
        if ok.sum() < 10 or y[ok].std() == 0:
            params[k] = (float(y[ok].mean()) if ok.any() else 0.0, 0.0, 1.0)
            continue
        b, a = np.polyfit(x[ok], y[ok], 1)
        sd = float(np.std(y[ok] - (a + b * x[ok]))) or 1.0
        params[k] = (float(a), float(b), sd)
    return params


def index_value(row, params):
    x = np.log(max(row["days_left"], 0) + 1)
    zs = {}
    for k, sign in FACTORS.items():
        v = row.get(k, np.nan)
        if v is None or pd.isna(v):
            continue
        a, b, sd = params[k]
        zs[k] = sign * (v - (a + b * x)) / sd
    return float(np.mean(list(zs.values()))) if zs else 0.0, zs


def calibrate(save=True):
    h = historical_factors()
    params = standardization(h)
    h["index"] = [index_value(r, params)[0] for _, r in h.iterrows()]
    d = h[h.days_left.isin(HORIZONS[1:])].copy()
    d["change"] = d.final_margin - d.margin

    def nll(theta):
        c, kappa = np.exp(theta[0]), theta[1]
        sd = c * d.days_left ** (1 / 3) * np.exp(kappa * d["index"])
        return float(np.sum(np.log(sd) + 0.5 * (d.change / sd) ** 2))

    res = minimize(nll, x0=[np.log(0.75), 0.3], method="Nelder-Mead")
    c, kappa = float(np.exp(res.x[0])), float(res.x[1])
    final = h[h.days_left == h.groupby("cycle").days_left.transform("min")].drop_duplicates("cycle").copy()
    final["ed_error"] = final.actual_margin - final.margin
    out = {"drift_const": round(c, 4), "index_kappa": round(kappa, 4),
           "ed_error_rmse_1968_2024": round(float(np.sqrt((final.ed_error ** 2).mean())), 3),
           "standardization": params}
    if save:
        cal = json.loads(C.CALIBRATION.read_text()) if C.CALIBRATION.exists() else {}
        cal["uncertainty"] = {k: out[k] for k in ("drift_const", "index_kappa")}
        cal["uncertainty_standardization"] = params
        cal["uncertainty_ed_error_rmse_1968_2024"] = out["ed_error_rmse_1968_2024"]
        C.CALIBRATION.write_text(json.dumps(cal, indent=2))
    return out, h, d, final


def standardization_params():
    cal = json.loads(C.CALIBRATION.read_text()) if C.CALIBRATION.exists() else {}
    if "uncertainty_standardization" not in cal:
        return calibrate()[0]["standardization"]
    return {k: tuple(v) for k, v in cal["uncertainty_standardization"].items()}


def live_index(cycle, asof, trend, us_avg, us_volume, fund_margin, econ_spread, third_share=0.0):
    """Index for a model run: factors from our own national trendline and average."""
    e = elections(1880, cycle).loc[cycle]
    days_left = (pd.Timestamp(C.ELECTION_DAYS[cycle]) - pd.Timestamp(asof)).days
    t = trend[trend.date <= pd.Timestamp(asof)]
    m = (t.D - t.R)
    win = m[t.date > pd.Timestamp(asof) - pd.Timedelta(days=90)]
    margin = float(us_avg["D"] - us_avg["R"])
    row = {"days_left": days_left, "undecided": 100 - us_avg["D"] - us_avg["R"] - third_share,
           "undecided_third": 100 - us_avg["D"] - us_avg["R"], "polarization": e.polarization,
           "volatility": float(win.std()) if len(win) > 5 else np.nan, "volume": np.log1p(us_volume),
           "gap": abs(margin - fund_margin), "econ_spread": econ_spread, "repeat_candidates": e.repeat_candidates}
    idx, zs = index_value(row, standardization_params())
    fud = C.CYCLES[cycle].get("volume_fudge")
    if fud and "volume" in zs:      # kamala_mode: poll-volume factor temporarily higher, gone by Sept 12  [SB]
        a, b = pd.Timestamp(fud["start"]), pd.Timestamp(fud["until"])
        frac = float(np.clip((b - pd.Timestamp(asof)).days / max((b - a).days, 1), 0, 1))
        zs["volume"] += fud["z"] * frac
        idx = float(np.mean(list(zs.values())))
    return idx, zs, row
