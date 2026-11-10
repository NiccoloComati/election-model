"""Fit parameters from Silver's published outputs (per cycle) and from history; writes calibration.json.

  python -m model.president.calibrate

Per cycle (2024 Silver Bulletin, 2020 FiveThirtyEight):
  poll weight formula  log(weight) ~ log sample size + rating + log polls by the firm in the race + tracking + unrated
  regression blend     Election Day weight on the regression vs summed poll influence in the state
Across history: uncertainty-index standardization and drift (uncertainty.calibrate).
"""
import json

import numpy as np
import pandas as pd

from . import config as C
from . import data as D
from . import uncertainty as U


def _pollist(cycle):
    kind, ref = C.CYCLES[cycle]["pollist"]
    return D.cached_excel(ref) if kind == "hosted" else pd.read_csv(C.ARCHIVE / ref)


def _steps(cycle):
    if cycle == 2024:
        return D.cached_excel("2024-11-05_forecast-steps")
    return pd.read_csv(C.ARCHIVE / "2020-general-data" / "presidential_forecast_steps.csv")


def fit_weights(cycle):
    p, _ = D.load_polls(cycle)
    x = p[p.silver_weight > 0].copy()
    x["nfirm"] = x.groupby(["geo", "pollster"]).poll_id.transform("count")
    X = np.column_stack([np.ones(len(x)), np.log(x.n.clip(lower=100)), x.ppm.fillna(0), np.log(x.nfirm),
                         x.tracking.astype(float), (~x.rated).astype(float)])
    y = np.log(x.silver_weight.astype(float))
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    r2 = 1 - ((y - X @ b) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    return {"intercept": b[0], "log_n": b[1], "ppm": b[2], "log_nfirm": b[3], "tracking": b[4],
            "ppm_unrated": b[5] / b[2] if b[2] != 0 else 0.6}, float(r2)


def fit_blend(cycle):
    pl = _pollist(cycle)
    pl = pl[pl.candidate_name == C.CYCLES[cycle]["dem"]]
    n_eff = pl.groupby("state").influence.sum()
    fs = _steps(cycle)
    w = fs[fs.step_description.str.contains("regression", case=False)].set_index("state").weight
    d = pd.DataFrame({"N": n_eff, "w": w}).dropna()
    d = d[(d.w < 1) & (d.w > 0)]
    coef = np.polyfit(np.log(d.N), np.log(1 / d.w - 1), 2)
    fit = 1 / (1 + np.exp(np.polyval(coef, np.log(d.N))))
    return [float(c) for c in coef], float(np.abs(fit - d.w).max())


def main():
    cal = json.loads(C.CALIBRATION.read_text()) if C.CALIBRATION.exists() else {}
    cal = {k: v for k, v in cal.items() if not k.isdigit() and k != "weight" and k != "blend_curve" and k != "fit_quality"}
    for cycle in C.CYCLES:
        w, r2 = fit_weights(cycle)
        blend, err = fit_blend(cycle)
        cal[str(cycle)] = {"weight": {k: round(float(v), 4) for k, v in w.items()}, "blend_curve": [round(c, 5) for c in blend],
                           "fit_quality": {"weight_r2": round(r2, 3), "blend_max_abs_error": round(err, 3)}}
        print(cycle, cal[str(cycle)])
    C.CALIBRATION.write_text(json.dumps(cal, indent=2))
    out = U.calibrate(save=True)[0]
    print("uncertainty", {k: v for k, v in out.items() if k != "standardization"})


if __name__ == "__main__":
    main()
