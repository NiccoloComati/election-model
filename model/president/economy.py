"""Economic index [538 2020]/[SB 2024]: six indicators, each a z-score from the incumbent party's standpoint.

  jobs (nonfarm payrolls), manufacturing (industrial production), income (real disposable personal income),
  spending (real personal consumption), inflation (CPI, sign flipped), stock market (S&P 500)

Each indicator: annualized six-month log growth, averaged over the past year with more weight on the final
three months (so it spans ~18 months of data), standardized against all months since 1946. Index = mean of the available z-scores.
Projection to Election Day: recent growth reverts toward its long-run mean. [NOT IMPLEMENTED: Silver also
uses professional forecasters' GDP projections and recent stock returns; see config.NOT_IMPLEMENTED.]

Point in time: payrolls, industrial production, real disposable income and real consumption are read as
published on the as-of date (ALFRED vintages, from 1972; income and consumption from 1984). CPI and stocks
are essentially unrevised. Standardization (means, SDs) uses today's revised history.
"""
import time

import requests
import numpy as np
import pandas as pd

from . import config as C

FRED = C.ROOT / "sources" / "economy" / "fred"
SHILLER = C.ROOT / "sources" / "economy" / "shiller" / "ie_data.xls"
INDICATORS = ["income", "inflation", "jobs", "manufacturing", "spending", "stocks"]
LABELS = {"income": "Real disposable personal income", "inflation": "Consumer price index", "jobs": "Nonfarm payrolls",
          "manufacturing": "Industrial production", "spending": "Personal consumption expenditures", "stocks": "S&P 500"}
SIGN = {"inflation": -1}
LAG = {"income": 2, "spending": 2}      # months until a month's data is published (others: 1); revised data only
VINTAGE = {"jobs": "PAYEMS", "manufacturing": "INDPRO", "income": "DSPIC96", "spending": "PCEC96"}
ALFRED = C.ROOT / "sources" / "economy" / "alfred"
PIT_FROM = 1972                           # first election whose index uses archived releases

# Election Day values Silver reported [538 2020 article; SB 2024], for calibration and checks
REPORTED = {1880: 1.37, 1920: -1.52, 1932: -2.34, 1936: 1.55, 1964: 0.70, 1980: -1.71, 1984: 0.86,
            2008: -1.34, 2012: -0.10, 2016: 0.08, 2024: 0.18}
REPORTED_2024 = {"income": -0.21, "inflation": 0.48, "jobs": 0.07, "manufacturing": -0.43, "spending": 0.24, "stocks": 0.91}


def _fred(sid):
    d = pd.read_csv(FRED / f"{sid}.csv")
    d.columns = ["date", "v"]
    d["date"] = pd.to_datetime(d.date)
    d["v"] = pd.to_numeric(d.v, errors="coerce")
    return d.dropna().set_index("date").v


def _annual_to_monthly(s):
    s = s.copy()
    s.index = s.index + pd.offsets.DateOffset(months=6)          # annual value sits mid-year
    m = np.exp(np.log(s).resample("MS").interpolate("linear"))
    return m


def _splice(old, new):
    """Join two series, rescaling the old one so they agree where they first overlap."""
    start = new.index[0]
    o = old[old.index <= start]
    if o.empty:
        return new
    ratio = new.iloc[0] / o.iloc[-1]
    return pd.concat([o[o.index < start] * ratio, new])


def monthly_levels():
    cache = C.CACHE / "econ_levels.csv"
    if cache.exists():
        return pd.read_csv(cache, index_col=0, parse_dates=True)
    sh = pd.read_excel(SHILLER, sheet_name="Data", header=7)
    sh = sh[pd.to_numeric(sh.Date, errors="coerce").notna()].copy()
    yr = sh.Date.astype(float)
    sh["date"] = pd.to_datetime([f"{int(y)}-{int(round((y - int(y)) * 100)):02d}-01" for y in yr])
    sh = sh.set_index("date")
    sp_sh = pd.to_numeric(sh.P, errors="coerce").dropna()
    cpi_sh = pd.to_numeric(sh.CPI, errors="coerce").dropna()
    sp_fred = _fred("SP500").resample("MS").mean()
    lv = pd.DataFrame({
        "jobs": _fred("PAYEMS"),
        "manufacturing": _fred("INDPRO"),
        "inflation": _splice(cpi_sh, _fred("CPIAUCNS")),
        "income": _splice(_annual_to_monthly(_fred("A067RX1A020NBEA")), _fred("DSPIC96")),
        "spending": _splice(_annual_to_monthly(_fred("PCECCA")), _fred("DPCERA3M086SBEA")),
        "stocks": _splice(sp_sh, sp_fred),
    })
    lv = lv[lv.index >= "1870-01-01"]
    cache.parent.mkdir(parents=True, exist_ok=True)
    lv.to_csv(cache)
    return lv


def growth(h=None):
    """Annualized h-month log growth (percent)."""
    h = h or C.ECON["growth_horizon"]
    lv = np.log(monthly_levels())
    return (lv - lv.shift(h)) * 1200 / h


def _weights(p):
    w = np.ones(p["window_months"])
    w[p["recent_months"]:] = p["older_weight"]
    return w / w.sum()


def _measure_from_log(loglevel, p):
    """Weighted window of h-month growth ending at the last point of a log-level array (newest last)."""
    h, n = p["growth_horizon"], p["window_months"]
    g = (loglevel[h:] - loglevel[:-h]) * 1200 / h
    g = g[-n:][::-1]
    w = _weights(p)[:len(g)]
    return float(np.dot(g, w) / w.sum())


def measures(params=None):
    """Weighted growth measure for every month and indicator (unstandardized)."""
    p = {**C.ECON, **(params or {})}
    g = growth(p["growth_horizon"])
    w = _weights(p)
    return g.rolling(p["window_months"]).apply(lambda x: np.dot(x[::-1], w), raw=True)


def standardization(params=None):
    p = {**C.ECON, **(params or {})}
    m = measures(p)
    ref = m[(m.index >= f"{p['standardize_from']}-01-01") & (m.index < "2024-01-01")]
    return ref.mean(), ref.std()


def zscores(params=None):
    p = {**C.ECON, **(params or {})}
    mu, sd = standardization(p)
    z = (measures(p) - mu) / sd
    for k, s in SIGN.items():
        z[k] *= s
    return z


def vintage(sid, asof):
    """A series exactly as published on `asof` (ALFRED), last four years; cached. Empty if not archived."""
    asof = pd.Timestamp(asof).normalize()
    f = ALFRED / f"{sid}_{asof.date()}.csv"
    if not f.exists():
        ALFRED.mkdir(parents=True, exist_ok=True)
        url = (f"https://alfred.stlouisfed.org/graph/alfredgraph.csv?id={sid}&vintage_date={asof.date()}"
               f"&cosd={asof.year - 4}-01-01")
        for attempt in range(3):
            try:
                r = requests.get(url, headers={"User-Agent": "election-model-research/0.1"}, timeout=60)
                if r.ok:
                    f.write_text(r.text)
                    break
            except requests.RequestException:
                time.sleep(3 * (attempt + 1))
        time.sleep(0.2)
        if not f.exists():
            return pd.Series(dtype=float)
    d = pd.read_csv(f)
    if d.shape[1] < 2:
        return pd.Series(dtype=float)
    d.columns = ["date", "v"]
    d["v"] = pd.to_numeric(d.v, errors="coerce")
    return d.dropna().assign(date=lambda x: pd.to_datetime(x.date)).set_index("date").v


def election_day_index(params=None, pit=True):
    """Each election's 'Election Day' index. From 1972 (pit=True): data as published on Nov 1 of the election
    year, projected to October like a live run. Earlier, or pit=False: revised data for October."""
    p = {**C.ECON, **(params or {})}
    z = zscores(p)
    rows = {}
    for y in range(1880, 2025, 4):
        if pit and y >= PIT_FROM:
            r = index_asof(f"{y}-11-01", y, p)
            rows[y] = {**r["projected"].to_dict(), "index": r["index_projected"], "n_indicators": int(r["projected"].notna().sum()),
                       "pit_indicators": r["pit_indicators"]}
            continue
        t = pd.Timestamp(f"{y}-{p['month']:02d}-01")
        if t in z.index:
            r = z.loc[t]
            rows[y] = {**r.to_dict(), "index": r.mean(skipna=True), "n_indicators": int(r.notna().sum()), "pit_indicators": 0}
    return pd.DataFrame(rows).T


def index_asof(asof, election_year, params=None, pit=True):
    """Current and projected index as of a date, using only data published by then (vintages where archived).

    After the last published month, monthly growth reverts toward its long-run mean by a fixed factor
    per month [ASSUMED]. [NOT IMPLEMENTED] professional forecasts and stock-return signal (config.NOT_IMPLEMENTED).
    """
    p = {**C.ECON, **(params or {})}
    asof = pd.Timestamp(asof)
    lv = np.log(monthly_levels())
    g1 = lv.diff() * 1200
    mu_g = g1[(g1.index >= "1946-01-01") & (g1.index < "2024-01-01")].mean()
    mu, sd = standardization(p)
    target = pd.Timestamp(f"{election_year}-{p['month']:02d}-01")
    cur, proj, n_pit = {}, {}, 0
    for k in INDICATORS:
        s = pd.Series(dtype=float)
        if pit and k in VINTAGE:
            v = vintage(VINTAGE[k], asof)
            if len(v) > p["growth_horizon"] + p["window_months"]:
                s = np.log(v[v.index <= target])
                n_pit += 1
        if s.empty:
            last = pd.Timestamp(asof.year, asof.month, 1) - pd.DateOffset(months=LAG.get(k, 1))
            s = lv[k][lv.index <= min(last, target)].dropna()
        if len(s) < p["growth_horizon"] + 1:
            continue
        sign = SIGN.get(k, 1)
        cur[k] = sign * (_measure_from_log(s.to_numpy(), p) - mu[k]) / sd[k]
        months_ahead = max(0, (target.year - s.index[-1].year) * 12 + target.month - s.index[-1].month)
        recent = float(np.diff(s.to_numpy()[-7:]).mean() * 1200)
        path = [mu_g[k] + (recent - mu_g[k]) * p["reversion_per_month"] ** (i + 1) for i in range(months_ahead)]
        ext = np.concatenate([s.to_numpy(), s.iloc[-1] + np.cumsum(path) / 1200]) if path else s.to_numpy()
        proj[k] = sign * (_measure_from_log(ext, p) - mu[k]) / sd[k]
    cur, proj = pd.Series(cur), pd.Series(proj)
    return {"current": cur, "projected": proj, "index_current": float(cur.mean()),
            "index_projected": float(proj.mean()), "component_sd": float(proj.std()), "pit_indicators": n_pit}


def silver_2020_daily():
    """FiveThirtyEight's published daily 2020 index components (current and projected z-scores)."""
    e = pd.read_csv(C.ARCHIVE / "2020-general-data" / "economic_index.csv")
    e["date"] = pd.to_datetime(e.modeldate, format="mixed")
    return e


def calibrate(grid_h=(1, 3, 6, 12), grid_window=(12, 24), grid_recent=(3, 6, 12), grid_older=(0.1, 0.33, 0.6, 1.0), pit=True):
    """Pick the growth horizon and weighting that best reproduce Silver's reported values."""
    e20 = silver_2020_daily()
    e20 = e20[e20.date == e20.date.max()]
    key = {v: k for k, v in LABELS.items()}
    t20 = {key[r.indicator]: r.current_zscore for _, r in e20.iterrows() if r.indicator in key}
    rows = []
    import itertools
    for h, win, rm, ow in itertools.product(grid_h, grid_window, grid_recent, grid_older):
        if rm >= win:
            continue
        if True:
            p = {"growth_horizon": h, "window_months": win, "older_weight": ow, "recent_months": rm}
            ed = election_day_index(p, pit=pit)
            err = [ed.loc[y, "index"] - v for y, v in REPORTED.items() if y in ed.index and y >= 1946]
            err += [ed.loc[2024, k] - v for k, v in REPORTED_2024.items()]
            err += [ed.loc[2020, k] - v for k, v in t20.items()]
            rows.append({**p, "rmse": float(np.sqrt(np.mean(np.square(err))))})
    return pd.DataFrame(rows).sort_values("rmse")
