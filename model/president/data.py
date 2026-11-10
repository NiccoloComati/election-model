"""Inputs for one cycle: geography, past results, partisan lean, elasticity, pollster ratings, polls."""
import numpy as np
import pandas as pd

from . import config as C

STATES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado",
    "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia", "FL": "Florida", "GA": "Georgia",
    "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts",
    "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana",
    "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico",
    "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
    "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington",
    "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming",
}
ABBR = {v: k for k, v in STATES.items()}
EV_2024 = {
    "AL": 9, "AK": 3, "AZ": 11, "AR": 6, "CA": 54, "CO": 10, "CT": 7, "DE": 3, "DC": 3, "FL": 30, "GA": 16,
    "HI": 4, "ID": 4, "IL": 19, "IN": 11, "IA": 6, "KS": 6, "KY": 8, "LA": 8, "ME": 2, "MD": 10, "MA": 11,
    "MI": 15, "MN": 10, "MS": 6, "MO": 10, "MT": 4, "NE": 2, "NV": 6, "NH": 4, "NJ": 14, "NM": 5, "NY": 28,
    "NC": 16, "ND": 3, "OH": 17, "OK": 7, "OR": 8, "PA": 19, "RI": 4, "SC": 9, "SD": 3, "TN": 11, "TX": 40,
    "UT": 6, "VT": 3, "VA": 13, "WA": 12, "WV": 4, "WI": 10, "WY": 3,
    "ME-1": 1, "ME-2": 1, "NE-1": 1, "NE-2": 1, "NE-3": 1,
}
# 2010 apportionment (2012-2020 elections)
EV_2012 = {**EV_2024, "CA": 55, "CO": 9, "FL": 29, "IL": 20, "MI": 16, "MT": 3, "NY": 29, "NC": 15, "OH": 18,
           "OR": 7, "PA": 20, "TX": 38, "WV": 5}
REGION = {}
for _r, _m in {"Northeast": "CT ME MA NH RI VT NJ NY PA", "Midwest": "IL IN MI OH WI IA KS MN MO NE ND SD",
               "South": "DE DC FL GA MD NC SC VA WV AL KY MS TN AR LA OK TX",
               "West": "AZ CO ID MT NV NM UT WY AK CA HI OR WA"}.items():
    for _s in _m.split():
        REGION[_s] = _r
DISTRICTS = {"ME-1": "ME", "ME-2": "ME", "NE-1": "NE", "NE-2": "NE", "NE-3": "NE"}
# Presidential results by congressional district (D%, R%), entered by hand from published district-level
# tabulations (Daily Kos Elections). VERIFY before relying on them. 2024 comes from the Silver Bulletin rawpolls file.
DISTRICT_RESULTS = {
    2012: {"ME-1": (59.57, 38.18), "ME-2": (52.94, 44.38), "NE-1": (40.83, 57.43),
           "NE-2": (45.70, 52.85), "NE-3": (27.82, 70.12)},
    2016: {"ME-1": (53.96, 39.15), "ME-2": (40.98, 51.26), "NE-1": (35.46, 56.18),
           "NE-2": (44.92, 47.16), "NE-3": (19.73, 73.92)},
    2020: {"ME-1": (60.11, 37.02), "ME-2": (44.82, 52.26), "NE-1": (41.09, 56.01),
           "NE-2": (52.24, 45.81), "NE-3": (22.34, 75.61)},
}
GEO_NAME = {**STATES, **{d: d for d in DISTRICTS}}
LABEL_TO_GEO = {**{v: k for k, v in GEO_NAME.items()}, "Maine CD-1": "ME-1", "Maine CD-2": "ME-2",
                "Nebraska CD-1": "NE-1", "Nebraska CD-2": "NE-2", "Nebraska CD-3": "NE-3"}
MAJOR = {1968: ("Hubert Humphrey, Jr.", "Richard M. Nixon"), 1972: ("George S. McGovern", "Richard M. Nixon"),
         1976: ("Jimmy Carter", "Gerald R. Ford"), 1980: ("Jimmy Carter", "Ronald Reagan"),
         1984: ("Walter F. Mondale", "Ronald Reagan"), 1988: ("Michael S. Dukakis", "George Bush"),
         1992: ("Bill Clinton", "George Bush"), 1996: ("Bill Clinton", "Bob Dole"), 2000: ("Al Gore", "George W. Bush"),
         2004: ("John Kerry", "George W. Bush"), 2008: ("Barack Obama", "John McCain"),
         2012: ("Barack Obama", "Mitt Romney"), 2016: ("Hillary Rodham Clinton", "Donald Trump")}


def major_candidates(year):
    if year in C.CYCLES:
        return C.CYCLES[year]["dem"], C.CYCLES[year]["rep"]
    return MAJOR[year]


def cached_excel(stem, sheet=0):
    cache = C.CACHE / f"{stem}.csv"
    if cache.exists():
        return pd.read_csv(cache, low_memory=False)
    d = pd.read_excel(next(C.HOSTED.glob(f"*{stem}*.xlsx")), sheet_name=sheet)
    cache.parent.mkdir(parents=True, exist_ok=True)
    d.to_csv(cache, index=False)
    return d


def geographies():
    return list(STATES) + list(DISTRICTS)


def ev_table(cycle):
    return EV_2024 if cycle >= 2024 else EV_2012


def state_results():
    """D, R, other share (%) and total votes by state and year, from the MIT Election Lab."""
    r = pd.read_csv(C.RESULTS)
    tot = r.groupby(["year", "state_po"]).totalvotes.first()
    by = r.groupby(["year", "state_po", "party_simplified"]).candidatevotes.sum().unstack(fill_value=0)
    out = pd.DataFrame({"D": by["DEMOCRAT"] / tot * 100, "R": by["REPUBLICAN"] / tot * 100, "votes": tot})
    out["O"] = 100 - out.D - out.R
    return out


def national_margin(year):
    t = state_results().loc[year]
    return (t.D * t.votes).sum() / t.votes.sum() - (t.R * t.votes).sum() / t.votes.sum()


def home_effect(year, geo):
    """Home-state boost to the D-minus-R margin in a contest (districts take their state's)."""
    h = C.HOME.get(year)
    if not h:
        return 0.0
    s = DISTRICTS.get(geo, geo)
    b = C.HOME_BONUS
    eff = 0.0
    eff += b["pres"] * (s == h["D"][0]) + b["vp"] * (s == h["D"][1])
    eff -= b["pres"] * (s == h["R"][0]) + b["vp"] * (s == h["R"][1])
    return eff


def geo_table(cycle):
    """One row per contest with everything known before the cycle's election."""
    cfg = C.CYCLES[cycle]
    res = state_results()
    ev = ev_table(cycle)
    years = list(cfg["lean_years"])
    nat = {y: national_margin(y) for y in years}
    prev = max(years)
    rows = []
    for g in geographies():
        parent = DISTRICTS.get(g, g)
        row = {"geo": g, "label": GEO_NAME[g], "parent": parent, "ev": ev[g], "region": REGION[parent],
               "is_district": g in DISTRICTS}
        lean = 0.0
        for y, w in cfg["lean_years"].items():
            d, r = DISTRICT_RESULTS[y][g] if g in DISTRICTS else res.loc[(y, g), ["D", "R"]]
            row[f"rel_{y}"] = d - r - nat[y]
            lean += w * (row[f"rel_{y}"] - home_effect(y, g))
        row["home_effect"] = home_effect(cycle, g)
        row["lean"] = lean + row["home_effect"]
        row["other_prev"] = res.loc[(prev, parent), "O"]
        n_dist = sum(1 for p in DISTRICTS.values() if p == parent) if g in DISTRICTS else 1
        row["turnout"] = res.loc[(prev, parent), "votes"] / n_dist
        rows.append(row)
    geo = pd.DataFrame(rows).set_index("geo")
    el = pd.read_csv(C.GITHUB_538 / "political-elasticity-scores" / "elasticity-by-state.csv").set_index("state").elasticity
    eld = pd.read_csv(C.GITHUB_538 / "political-elasticity-scores" / "elasticity-by-district.csv").set_index("district").elasticity
    geo["elasticity"] = [eld.get(g, el.get(DISTRICTS[g], 1.0)) if g in DISTRICTS else el.get(g, 1.0) for g in geo.index]
    return geo


def actual_results(cycle):
    """Actual D-minus-R margins by contest and nationally (evaluation only)."""
    res = state_results().loc[cycle]
    m = (res.D - res.R).to_dict()
    if cycle in DISTRICT_RESULTS:
        for g, (d, r) in DISTRICT_RESULTS[cycle].items():
            m[g] = d - r
    else:
        rp = cached_excel("2026-01-14_rawpolls-040626")
        rp = rp[(rp.type_simple == "Pres-G") & (rp.year == cycle) & rp.location.isin(list(DISTRICTS))]
        for _, r in rp.groupby("location")[["cand1_actual", "cand2_actual"]].first().iterrows():
            m[r.name] = r.cand1_actual - r.cand2_actual
    return pd.Series(m), national_margin(cycle)


def pollster_ratings(cycle):
    kind, ref = C.CYCLES[cycle]["ratings"]
    if kind == "sb":
        st = cached_excel(ref)
        st = st.rename(columns={"Pollster Rating ID": "rid", "Predictive    Plus-Minus": "ppm", "SB Grade": "grade",
                                "Banned by 538": "banned"})
    else:
        st = pd.read_csv(C.GITHUB_538 / "pollster-ratings" / ref / "pollster-ratings.csv", encoding="utf-8-sig")
        st = st.rename(columns={"Pollster Rating ID": "rid", "Predictive    Plus-Minus": "ppm", "538 Grade": "grade",
                                "Banned by 538": "banned"})
    st = st[pd.to_numeric(st.rid, errors="coerce").notna()].copy()
    st["rid"] = st.rid.astype(int)
    st["ppm"] = pd.to_numeric(st.ppm, errors="coerce")
    return st.drop_duplicates("rid").set_index("rid")[["ppm", "grade", "banned"]]


def _geo_from_label(s):
    if pd.isna(s) or s == "National":
        return "US"
    return LABEL_TO_GEO.get(s)


def load_polls(cycle, source="silver"):
    """Polls for the cycle, one row per poll with D and R shares, plus likely-voter pairs.

    source="silver": the poll universe is Silver's final poll list for the cycle (2024 Silver Bulletin,
        2020 FiveThirtyEight). The FiveThirtyEight feed adds partisan sponsor, release time, LV/RV pairs and
        the named third-party candidate's share. Polls missing from the feed get release = end + 1 day.
    source="538": the FiveThirtyEight feed alone.
    """
    cfg = C.CYCLES[cycle]
    feed, lv_pairs = _load_feed(cycle)
    if source == "538":
        return feed, lv_pairs
    kind, ref = cfg["pollist"]
    pl = cached_excel(ref) if kind == "hosted" else pd.read_csv(C.ARCHIVE / ref)
    pl = pl[pl.candidate_name.isin([cfg["dem"], cfg["rep"]])]
    wide = pl.pivot_table(index="poll_id", columns="candidate_name", values="pct", aggfunc="mean")
    meta = pl.drop_duplicates("poll_id").set_index("poll_id")
    rid = meta.pollster_rating_id if "pollster_rating_id" in meta else pd.Series(np.nan, index=meta.index)
    p = pd.DataFrame({
        "pollster": meta.pollster, "geo": meta.state.map(_geo_from_label),
        "population": meta.population.astype(str).str.lower(), "n": pd.to_numeric(meta.samplesize, errors="coerce"),
        "start": pd.to_datetime(meta.startdate, format="mixed"), "end": pd.to_datetime(meta.enddate, format="mixed"),
        "tracking": meta.tracking.astype(str).str.lower().isin(["true", "1", "yes", "t"]),
        "D": wide[cfg["dem"]], "R": wide[cfg["rep"]], "silver_weight": meta.weight, "rid": rid,
    })
    extra = feed.set_index("poll_id")[["created", "partisan", "versions", "K", "rid"]].rename(columns={"rid": "rid_feed"})
    p = p.join(extra, how="left")
    p["rid"] = p.rid.fillna(p.rid_feed)
    p = p.drop(columns="rid_feed")
    p["created"] = p.created.fillna(p.end + pd.Timedelta(days=1))
    p["versions"] = p.versions.fillna(1)
    p.loc[p.pollster.isin(C.HOUSE["always_rep"]), "partisan"] = "REP"
    p["mid"] = p.start + (p.end - p.start) / 2
    p["n"] = p.n.fillna(C.WEIGHT["default_n"])
    p = p[p.geo.notna()]
    rt = pollster_ratings(cycle)
    p = p.join(rt[["ppm", "grade"]], on="rid")
    p["rated"] = p.ppm.notna()
    return p.reset_index(), lv_pairs


def _load_feed(cycle):
    cfg = C.CYCLES[cycle]
    d = pd.read_csv(cfg["feed538"], low_memory=False)
    d = d[(d.cycle == cycle) & (d.stage == "general") & (d.ranked_choice_reallocated.astype(str) != "True")]
    d["end"] = pd.to_datetime(d.end_date, format="%m/%d/%y")
    if cfg["first_poll_end"]:
        d = d[d.end >= cfg["first_poll_end"]]
    cands = d.groupby("question_id").candidate_name.agg(set)
    others = {"Joe Biden"} if cycle == 2024 else set()
    dem = cfg.get("feed_dem", cfg["dem"])
    ok = cands[cands.apply(lambda s: {dem, cfg["rep"]} <= s and not (s & others))].index
    d = d[d.question_id.isin(ok)]
    q = d.pivot_table(index="question_id", columns="candidate_name", values="pct", aggfunc="first")
    meta = d.drop_duplicates("question_id").set_index("question_id")
    n3 = cfg["n3pc"]["name"] if cfg["n3pc"] else None
    qs = pd.DataFrame({
        "poll_id": meta.poll_id, "pollster": meta.pollster, "rid": meta.pollster_rating_id,
        "geo": meta.state.map(_geo_from_label), "population": meta.population.astype(str).str.lower(),
        "n": pd.to_numeric(meta.sample_size, errors="coerce"),
        "start": pd.to_datetime(meta.start_date, format="%m/%d/%y"), "end": meta.end,
        "created": pd.to_datetime(meta.created_at, format="%m/%d/%y %H:%M", errors="coerce"),
        "partisan": meta.partisan, "tracking": meta.tracking.astype(str).str.lower() == "true",
        "D": q[dem], "R": q[cfg["rep"]],
        "K": q[n3] if n3 and n3 in q else np.nan,
    })
    qs = qs[qs.geo.notna()]
    pv = qs[qs.population.isin(["lv", "rv"])].groupby(["poll_id", "population"])[["D", "R"]].mean().unstack().dropna()
    lv_pairs = pd.DataFrame({"dD": pv[("D", "lv")] - pv[("D", "rv")], "dR": pv[("R", "lv")] - pv[("R", "rv")]})
    lv_pairs["created"] = qs.groupby("poll_id").created.min().reindex(lv_pairs.index)
    rank = {"lv": 0, "v": 1, "rv": 2, "a": 3}
    qs["prank"] = qs.population.map(rank).fillna(4)
    qs = qs[qs.prank == qs.groupby("poll_id").prank.transform("min")]
    agg = qs.groupby("poll_id").agg(
        pollster=("pollster", "first"), rid=("rid", "first"), geo=("geo", "first"), population=("population", "first"),
        n=("n", "max"), start=("start", "first"), end=("end", "first"), created=("created", "min"),
        partisan=("partisan", "first"), tracking=("tracking", "first"), D=("D", "mean"), R=("R", "mean"),
        K=("K", "mean"), versions=("D", "size"))
    agg["partisan"] = agg.partisan.where(agg.partisan.isin(["DEM", "REP"]))
    agg["mid"] = agg.start + (agg.end - agg.start) / 2
    agg["n"] = agg.n.fillna(C.WEIGHT["default_n"])
    rt = pollster_ratings(cycle)
    agg = agg.join(rt[["ppm", "grade", "banned"]], on="rid")
    agg = agg[agg.banned.astype(str).str.lower() != "yes"].drop(columns="banned")
    agg["rated"] = agg.ppm.notna()
    agg.loc[agg.pollster.isin(C.HOUSE["always_rep"]), "partisan"] = "REP"
    return agg.reset_index(), lv_pairs
