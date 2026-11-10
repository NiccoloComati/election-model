"""Run the presidential model for a cycle and date; compare with Silver's published forecast and the result.

  python -m model.president.run --cycle 2024                     # Election Day
  python -m model.president.run --cycle 2020 --date 2020-09-01
  python -m model.president.run --cycle 2024 --timeseries        # weekly runs + Election Day, for the notebook

Outputs: output/president/<cycle>/<date>/ and output/president/<cycle>/timeseries*.csv
"""
import argparse
import json

import numpy as np
import pandas as pd

from . import config as C
from . import data as D
from . import forecast as F
from . import polls as P
from . import simulate as S

SWING = ["PA", "MI", "WI", "GA", "NC", "AZ", "NV"]
_CACHE = {}


def silver_outputs(cycle):
    """Silver's published daily toplines, re-expressed as Democrat/Republican."""
    if cycle == 2024:
        nt, st = D.cached_excel("2024-11-05_national-topline"), D.cached_excel("2024-11-05_state-topline")
    else:
        nt = pd.read_csv(C.ARCHIVE / "2020-general-data" / "presidential_national_toplines_2020.csv")
        st = pd.read_csv(C.ARCHIVE / "2020-general-data" / "presidential_state_toplines_2020.csv")
    d_is_inc = C.CYCLES[cycle]["inc_party"] == "D"
    a, b = ("inc", "chal") if d_is_inc else ("chal", "inc")
    for df in (nt, st):
        df["date"] = pd.to_datetime(df.modeldate, format="mixed")
    nat = pd.DataFrame({"date": nt.date, "win_D": nt[f"ecwin_{a}"], "win_R": nt[f"ecwin_{b}"], "ev_D": nt[f"ev_{a}"],
                        "popvote_D": nt[f"national_voteshare_{a}"], "popvote_R": nt[f"national_voteshare_{b}"],
                        "popwin_D": nt[f"popwin_{a}"]}).sort_values("date")
    nat["popvote_margin"] = nat.popvote_D - nat.popvote_R
    nat = nat.drop_duplicates("date", keep="last")          # some days have two published runs
    sgn = 1 if d_is_inc else -1
    sta = pd.DataFrame({"date": st.date, "geo": st.state.map(D.LABEL_TO_GEO), "win_D": st[f"winstate_{a}"],
                        "margin": sgn * st.margin, "margin_hi": np.where(d_is_inc, st.margin_hi, -st.margin_lo),
                        "margin_lo": np.where(d_is_inc, st.margin_lo, -st.margin_hi), "tipping": st.tipping})
    sta = sta.drop_duplicates(["date", "geo"], keep="last")
    return nat, sta


def _inputs(cycle):
    if cycle not in _CACHE:
        C.load_calibration(cycle)
        _CACHE[cycle] = (D.geo_table(cycle), *D.load_polls(cycle))
    C.load_calibration(cycle)
    return _CACHE[cycle]


def run_once(cycle, date=None, sims=C.SIMS, save=True, quiet=False):
    date = date or C.ELECTION_DAYS[cycle]
    geo, polls, lv = _inputs(cycle)
    avg = P.build(polls, lv, geo, date, cycle)
    g, info = F.project(avg, geo, cycle)
    summary, per_geo, ev_dist, _ = S.run(g, P.political_days_left(date, cycle), cycle, info["uncertainty_index"], sims=sims)
    summary.update({k: v for k, v in info.items()})
    summary.update({"cycle": cycle, "date": str(pd.Timestamp(date).date()),
                    "lv_adjustment": {k: float(v) for k, v in avg["lv"].items()}})
    actual, actual_nat = D.actual_results(cycle)
    comp = per_geo.join(g[["poll_margin", "reg_margin", "w_reg", "snapshot_margin", "fund_margin", "n_eff",
                           "lean", "home_effect"]])
    comp["actual_margin"] = actual.reindex(comp.index)
    nat_sb, st_sb = silver_outputs(cycle)
    sb_dates = nat_sb.date[nat_sb.date <= pd.Timestamp(date)]
    if len(sb_dates):
        d0 = sb_dates.max()
        n0 = nat_sb[nat_sb.date == d0].iloc[0]
        s0 = st_sb[st_sb.date == d0].set_index("geo")
        comp["silver_margin"] = s0.margin.reindex(comp.index)
        comp["silver_win_D"] = s0.win_D.reindex(comp.index)
        comp["silver_tipping"] = s0.tipping.reindex(comp.index)
        summary["silver"] = {"date": str(d0.date()), **{k: float(n0[k]) for k in
                             ("win_D", "win_R", "ev_D", "popvote_D", "popvote_R", "popwin_D", "popvote_margin")}}
        summary["replication_vs_silver_margin_rmse_swing"] = float(np.sqrt(((comp.margin - comp.silver_margin).loc[SWING] ** 2).mean()))
    ev = D.ev_table(cycle)
    summary["actual"] = {"popvote_margin": float(actual_nat),
                         "ev_D": int(sum(ev[k] for k, v in actual.items() if k in ev and v > 0))}
    ok = comp.actual_margin.notna()
    err = (comp.margin - comp.actual_margin)[ok]
    summary["error_vs_actual"] = {"rmse_all": float(np.sqrt((err ** 2).mean())), "mean_miss_swing": float(err.loc[SWING].mean()),
                                  "called_wrong": [k for k in err.index if np.sign(comp.margin[k]) != np.sign(comp.actual_margin[k])]}
    if "silver_margin" in comp:
        e2 = (comp.silver_margin - comp.actual_margin)[ok]
        summary["error_vs_actual"]["silver_rmse_all"] = float(np.sqrt((e2 ** 2).mean()))
    if save:
        out = C.OUT / str(cycle) / summary["date"]
        out.mkdir(parents=True, exist_ok=True)
        (out / "summary.json").write_text(json.dumps(summary, indent=2, default=float))
        comp.round(4).to_csv(out / "states.csv")
        ev_dist.to_csv(out / "ev_distribution.csv", index_label="dem_ev")
        avg["polls"].to_csv(out / "polls.csv", index=False)
        avg["house"].round(3).sort_values("polls", ascending=False).to_csv(out / "house_effects.csv", index_label="pollster")
        avg["trend"].round(3).to_csv(out / "national_trend.csv", index=False)
    if not quiet:
        report(summary, comp)
    return summary, comp


def report(s, comp):
    sb = s.get("silver", {})
    print(f"\n=== {s['cycle']} presidential model, as of {s['date']} ({s['days_left']} days out, {s['sims']:,} sims) ===")
    f = lambda x, fmt: (fmt.format(x) if x is not None and not (isinstance(x, float) and np.isnan(x)) else "-")
    rows = [("Dem EC win", f(s["win_D"], "{:.1%}"), f(sb.get("win_D"), "{:.1%}")),
            ("Dem EV (mean)", f(s["ev_D_mean"], "{:.0f}"), f(sb.get("ev_D"), "{:.0f}")),
            ("Pop. vote margin", f(s["popvote_margin_mean"], "{:+.1f}"), f(sb.get("popvote_margin"), "{:+.1f}")),
            ("Dem pop-vote win", f(s["popvote_win_D"], "{:.1%}"), f(sb.get("popwin_D"), "{:.1%}"))]
    print(f"{'':20}{'Replication':>12}{'Silver':>12}")
    for r in rows:
        print(f"{r[0]:20}{r[1]:>12}{r[2]:>12}")
    print(f"fundamentals {s['fundamentals_margin']:+.1f} (economy {s['economic_index_projected']:+.2f}) at weight "
          f"{s['fundamentals_weight']:.2f}; uncertainty index {s['uncertainty_index']:+.2f}; drift SD {s['sd_drift']:.1f}")
    cols = [c for c in ["poll_margin", "margin", "silver_margin", "actual_margin", "win_D", "silver_win_D"] if c in comp]
    print(comp.loc[SWING, cols].round(2).to_string())
    e = s["error_vs_actual"]
    print(f"RMSE vs actual: replication {e['rmse_all']:.2f}" + (f", Silver {e['silver_rmse_all']:.2f}" if "silver_rmse_all" in e else ""))


def timeseries(cycle, sims=20000, step_days=3):
    eday = pd.Timestamp(C.ELECTION_DAYS[cycle])
    nat_sb, _ = silver_outputs(cycle)
    start = max(nat_sb.date.min(), eday - pd.Timedelta(days=120)) + pd.Timedelta(days=1)
    dates = list(pd.date_range(start, eday, freq=f"{step_days}D")) + [eday]
    dates = sorted(set(d.normalize() for d in dates))
    rows, srows = [], []
    for d in dates:
        s, comp = run_once(cycle, d, sims=sims, save=False, quiet=True)
        sb = s.get("silver", {})
        rows.append({"date": d, "win_D": s["win_D"], "ev_D": s["ev_D_mean"], "ev_D_p10": s["ev_D_p10"], "ev_D_p90": s["ev_D_p90"],
                     "popvote_margin": s["popvote_margin_mean"], "popvote_margin_sd": s["popvote_margin_sd"],
                     "fundamentals_margin": s["fundamentals_margin"], "fundamentals_weight": s["fundamentals_weight"],
                     "economic_index": s["economic_index_projected"], "uncertainty_index": s["uncertainty_index"],
                     "sd_drift": s["sd_drift"], "national_margin_polls": s["national_margin_polls"],
                     "national_margin_polls_raw": s["national_margin_polls_raw"],
                     "economic_index_current": s.get("economic_index_current"),
                     "silver_win_D": sb.get("win_D"), "silver_ev_D": sb.get("ev_D"), "silver_popvote_margin": sb.get("popvote_margin"),
                     **{f"uz_{k}": v for k, v in s["uncertainty_factors_z"].items()}})
        c = comp.reset_index().rename(columns={"index": "geo"})
        c["date"] = d
        srows.append(c)
        print(cycle, d.date(), f"replication {s['win_D']:.3f}", f"Silver {sb.get('win_D', float('nan')):.3f}", flush=True)
    out = C.OUT / str(cycle)
    out.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out / "timeseries.csv", index=False)
    pd.concat(srows).to_csv(out / "timeseries_states.csv", index=False)
    run_once(cycle, eday, sims=C.SIMS, save=True, quiet=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--cycle", type=int, default=2024, choices=list(C.CYCLES))
    ap.add_argument("--date", default=None)
    ap.add_argument("--sims", type=int, default=C.SIMS)
    ap.add_argument("--timeseries", action="store_true")
    a = ap.parse_args()
    if a.timeseries:
        timeseries(a.cycle, sims=min(a.sims, 20000))
    else:
        run_once(a.cycle, a.date, sims=a.sims)
