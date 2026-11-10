"""Historical inputs: national popular vote 1880-2024, incumbency, polarization, national poll averages 1968-2024."""
import json
import re

import numpy as np
import pandas as pd

from . import config as C
from .data import cached_excel

WIKI = C.ROOT / "sources" / "results" / "history" / "wiki_popvote_margin.json"
VOTEVIEW = C.ROOT / "sources" / "voteview" / "HSall_members.csv"

# Incumbent party, and how the incumbent party's nominee relates to the White House. [538 2020]/[SB 2024]
#   tier: elected = elected president running again; unelected = president who succeeded mid-term
#         (Ford, Truman, ...); vp = sitting vice president; none = other nominee
#   rematch = same two major-party nominees as the previous election   [SB 2024]
#   candidates who were on the previous ballot count toward the uncertainty index's repeat-candidate factor
INCUMBENCY = {
    1880: ("R", "none", 0, 0), 1884: ("R", "none", 0, 0), 1888: ("D", "elected", 0, 1), 1892: ("R", "elected", 1, 2),
    1896: ("D", "none", 0, 0), 1900: ("R", "elected", 1, 2), 1904: ("R", "unelected", 0, 0), 1908: ("R", "none", 0, 0),
    1912: ("R", "elected", 0, 1), 1916: ("D", "elected", 0, 1), 1920: ("D", "none", 0, 0), 1924: ("R", "unelected", 0, 0),
    1928: ("R", "none", 0, 0), 1932: ("R", "elected", 0, 1), 1936: ("D", "elected", 0, 1), 1940: ("D", "elected", 0, 1),
    1944: ("D", "elected", 0, 1), 1948: ("D", "unelected", 0, 1), 1952: ("D", "none", 0, 0), 1956: ("R", "elected", 1, 2),
    1960: ("R", "vp", 0, 0), 1964: ("D", "unelected", 0, 0), 1968: ("D", "vp", 0, 0), 1972: ("R", "elected", 0, 1),
    1976: ("R", "unelected", 0, 0), 1980: ("D", "elected", 0, 1), 1984: ("R", "elected", 0, 1), 1988: ("R", "vp", 0, 0),
    1992: ("R", "elected", 0, 1), 1996: ("D", "elected", 0, 1), 2000: ("D", "vp", 0, 0), 2004: ("R", "elected", 0, 1),
    2008: ("R", "none", 0, 0), 2012: ("D", "elected", 0, 1), 2016: ("D", "none", 0, 0), 2020: ("R", "elected", 0, 1),
    2024: ("D", "vp", 0, 1),
}
# repeat_candidates = how many of the two major-party nominees were nominees in the previous election.

# Shares of the two major parties where the Wikipedia table's runner-up was not D or R.
MANUAL_SHARES = {1912: (41.84, 23.17)}     # Wilson (D), Taft (R); Roosevelt (Progressive) finished second


def popular_vote():
    """D-minus-R national popular vote margin by year (points), parsed from Wikipedia's margin table."""
    t = json.loads(WIKI.read_text(encoding="utf-8"))["parse"]["wikitext"]["*"].replace("−", "-")
    out = {}
    for r in re.split(r"\n\|-[^\n]*\n", t):
        m = re.search(r"\[\[(\d{4}) United States presidential election", r)
        if not m or int(m.group(1)) < 1876:
            continue
        year = int(m.group(1))
        parties = re.findall(r"party shading/([A-Za-z]+)", r)
        cells = [c for c in r.split("\n") if c.startswith("|")]
        pcts = []
        for c in cells:
            v = re.sub(r"<[^>]+>|\{\{[^}]*\}\}", "", c.split("|")[-1]).strip()
            mm = re.fullmatch(r"(-?\d+(?:\.\d+)?)%", v)
            if mm:
                pcts.append(float(mm.group(1)))
        if len(parties) < 2 or len(pcts) < 3:
            continue
        out[year] = {"winner_party": parties[0], "runner_party": parties[1], "winner_share": pcts[1], "margin": pcts[2]}
    df = pd.DataFrame(out).T
    df.index.name = "year"
    dm = []
    for y, r in df.iterrows():
        if y in MANUAL_SHARES:
            d, rr = MANUAL_SHARES[y]
            dm.append(d - rr)
        elif r.winner_party == "Democratic" and r.runner_party == "Republican":
            dm.append(float(r.margin))
        elif r.winner_party == "Republican" and r.runner_party == "Democratic":
            dm.append(-float(r.margin))
        else:
            dm.append(np.nan)
    df["dem_margin"] = dm
    return df


def elections(first=1880, last=2024):
    """One row per election: incumbent-party margin, previous margin, incumbency tier, rematch, polarization."""
    pv = popular_vote()
    rows = []
    for y in range(first, last + 1, 4):
        party, tier, rematch, repeaters = INCUMBENCY[y]
        sign = 1 if party == "D" else -1
        prev = pv.dem_margin.get(y - 4, np.nan)
        rows.append({"year": y, "inc_party": party, "tier": tier, "rematch": rematch, "repeat_candidates": repeaters,
                     "inc_margin": sign * pv.dem_margin.get(y, np.nan), "prev_inc_margin": sign * prev,
                     "dem_margin": pv.dem_margin.get(y, np.nan)})
    e = pd.DataFrame(rows).set_index("year")
    e["polarization"] = polarization().reindex(e.index)
    return e


def polarization():
    """Distance between the Democratic and Republican House medians on DW-NOMINATE dimension 1, by election year.

    Uses the Congress sitting during the election year (e.g. 2024 -> 118th). [538 2020: House roll-call distance]
    """
    v = pd.read_csv(VOTEVIEW, usecols=["congress", "chamber", "party_code", "nominate_dim1"])
    h = v[(v.chamber == "House") & v.party_code.isin([100, 200])]
    med = h.groupby(["congress", "party_code"]).nominate_dim1.median().unstack()
    dist = (med[200] - med[100])
    year_of = {c: 1787 + 2 * c for c in dist.index}          # Congress c starts in Jan of 1787+2c
    s = pd.Series({year_of[c] + 1: d for c, d in dist.items()})   # election year = second year of that Congress
    return s


def national_averages():
    """Daily national poll averages (Silver's) for 1968-2024: D, R, third-party and total shares, plus volume."""
    d = pd.read_csv(C.GITHUB_538 / "polls" / "pres_pollaverages_1968-2016.csv", low_memory=False)
    d = d[d.state == "National"].copy()
    d["date"] = pd.to_datetime(d.modeldate, format="mixed")
    frames = []
    e = elections(1968, 2024)
    from .data import major_candidates
    for cyc, g in d.groupby("cycle"):
        dem, rep = major_candidates(cyc)
        w = g.pivot_table(index="date", columns="candidate_name", values="pct_estimate", aggfunc="mean")
        vol = g.groupby("date").sum_nat_influence.mean()
        f = pd.DataFrame({"D": w[dem], "R": w[rep], "total": w.sum(1), "volume": vol})
        f["cycle"] = cyc
        frames.append(f)
    # 2020 (538 archive) and 2024 (Silver Bulletin) daily national averages
    a20 = pd.read_csv(C.ROOT / "sources" / "fivethirtyeight" / "archive" / "2020-general-data" / "presidential_poll_averages_2020.csv")
    a20 = a20[a20.state == "National"].copy()
    a20["date"] = pd.to_datetime(a20.modeldate, format="mixed")
    w = a20.pivot_table(index="date", columns="candidate_name", values="pct_estimate", aggfunc="mean")
    p20 = pd.read_csv(C.ROOT / "sources" / "fivethirtyeight" / "archive" / "2020-general-data" / "presidential_polls_2020.csv")
    f = pd.DataFrame({"D": w["Joseph R. Biden Jr."], "R": w["Donald Trump"], "total": w.sum(1)})
    f["volume"] = _volume_from_polls(p20[p20.state == "National"], f.index)
    f["cycle"] = 2020
    frames.append(f)
    a24 = cached_excel("2024-11-05_poll-average")
    a24 = a24[a24.state == "National"].copy()
    a24["date"] = pd.to_datetime(a24.modeldate, format="mixed")
    w = a24.pivot_table(index="date", columns="candidate_name", values="pct_estimate", aggfunc="mean")
    pl = cached_excel("2024-11-05_pres-pollist")
    pl = pl[(pl.state == "National") & (pl.candidate_name == "Kamala Harris")]
    f = pd.DataFrame({"D": w["Kamala Harris"], "R": w["Donald Trump"], "total": w.sum(1)})
    f["volume"] = _volume_from_polls(pl, f.index)
    f["cycle"] = 2024
    frames.append(f)
    out = pd.concat(frames).reset_index().rename(columns={"index": "date"})
    out["margin"] = out.D - out.R
    out["undecided"] = 100 - out.total
    out["undecided_third"] = 100 - out.D - out.R
    out["election_day"] = out.cycle.map(lambda y: pd.Timestamp(C.ELECTION_DAYS[y]))
    out["days_left"] = (out.election_day - out.date).dt.days
    out["actual_margin"] = out.cycle.map(e.dem_margin)
    return out


def _volume_from_polls(polls, dates):
    """Sum of weight x recency of national polls on each date (comparable to Silver's sum of influence)."""
    p = polls.copy()
    p["end"] = pd.to_datetime(p.enddate, format="mixed")
    p = p.drop_duplicates("poll_id")
    w = p.weight.to_numpy()
    out = []
    for d in dates:
        age = (d - p.end).dt.days.to_numpy()
        ok = age >= 0
        rec = np.clip(1 - age / C.RECENCY["window_days"], 0, None) ** C.RECENCY["power"]
        out.append(float((w * rec * ok).sum()))
    return out
