"""State and district demographic profiles from the 2022 Cooperative Election Study (adults, commonweight).

Used for (a) correlated simulation errors along demographic lines and (b) the demographic regression.
Silver uses race, religion (incl. white vs Black evangelicals, Mormon, Jewish, Muslim), education,
urbanization, income, age and geography [538 2020 / SB 2024]. The CES gives all of these, including
religion, which the Census does not ask. Small-sample geographies are shrunk toward their region.
"""
import numpy as np
import pandas as pd

from . import config as C
from .data import ABBR, DISTRICTS, REGION, STATES

CES22 = C.ROOT / "sources" / "surveys" / "ces" / "CCES22_Common_OUTPUT_vv_topost.csv"
CACHE = C.OUT / "_cache" / "demographics.csv"
FIPS = {1: "AL", 2: "AK", 4: "AZ", 5: "AR", 6: "CA", 8: "CO", 9: "CT", 10: "DE", 11: "DC", 12: "FL", 13: "GA",
        15: "HI", 16: "ID", 17: "IL", 18: "IN", 19: "IA", 20: "KS", 21: "KY", 22: "LA", 23: "ME", 24: "MD",
        25: "MA", 26: "MI", 27: "MN", 28: "MS", 29: "MO", 30: "MT", 31: "NE", 32: "NV", 33: "NH", 34: "NJ",
        35: "NM", 36: "NY", 37: "NC", 38: "ND", 39: "OH", 40: "OK", 41: "OR", 42: "PA", 44: "RI", 45: "SC",
        46: "SD", 47: "TN", 48: "TX", 49: "UT", 50: "VT", 51: "VA", 53: "WA", 54: "WV", 55: "WI", 56: "WY"}
FEATURES = ["white_college", "white_noncollege", "black", "hispanic", "asian", "white_evangelical", "catholic",
            "mormon", "jewish", "muslim", "secular", "urban", "rural", "age65", "high_income"]
SHRINK_N = 150      # pseudo-respondents pulling small samples toward the regional profile


def _person_features(d):
    hisp = (d.race == 3) | (d.hispanic == 1)
    white = (d.race == 1) & ~hisp
    college = d.educ >= 5
    evangelical = d.pew_bornagain == 1
    return pd.DataFrame({
        "white_college": white & college, "white_noncollege": white & ~college,
        "black": (d.race == 2) & ~hisp, "hispanic": hisp, "asian": (d.race == 4) & ~hisp,
        "white_evangelical": white & evangelical & d.religpew.isin([1, 12]),
        "catholic": d.religpew == 2, "mormon": d.religpew == 3, "jewish": d.religpew == 5, "muslim": d.religpew == 6,
        "secular": d.religpew.isin([9, 10, 11]), "urban": d.urbancity == 1, "rural": d.urbancity == 4,
        "age65": d.birthyr <= 1957, "high_income": d.faminc_new.between(11, 16),
    }).astype(float)


def profiles():
    if CACHE.exists():
        return pd.read_csv(CACHE, index_col=0)
    cols = ["commonweight", "inputstate", "cdid118", "race", "hispanic", "educ", "religpew", "pew_bornagain",
            "urbancity", "faminc_new", "birthyr"]
    d = pd.read_csv(CES22, usecols=cols)
    d["state"] = d.inputstate.map(FIPS)
    d = d.dropna(subset=["state"])
    f = _person_features(d)
    w = d.commonweight.fillna(0).to_numpy()
    fw = f.mul(w, axis=0)
    fw["state"] = d.state.to_numpy()
    fw["w"] = w
    fw["n"] = 1.0
    st = fw.groupby("state").sum()
    shares = st[FEATURES].div(st.w, axis=0)
    shares["n"] = st.n
    # districts of Maine and Nebraska
    rows = {}
    for g, parent in DISTRICTS.items():
        m = (d.state == parent).to_numpy() & (d.cdid118 == int(g[-1])).to_numpy()
        sub = fw[m]
        rows[g] = list((sub[FEATURES].sum() / sub.w.sum()).to_numpy()) + [m.sum()]
    shares = pd.concat([shares, pd.DataFrame(rows, index=FEATURES + ["n"]).T])
    # shrink toward the region (districts toward their state)
    region_of = {g: REGION[DISTRICTS.get(g, g)] for g in shares.index}
    reg_mean = shares[FEATURES].groupby(pd.Series(region_of)).mean()
    out = shares.copy()
    for g in shares.index:
        target = shares.loc[DISTRICTS[g], FEATURES] if g in DISTRICTS else reg_mean.loc[region_of[g]]
        n = shares.loc[g, "n"]
        out.loc[g, FEATURES] = (n * shares.loc[g, FEATURES] + SHRINK_N * target) / (n + SHRINK_N)
    out = out.reindex(list(STATES) + list(DISTRICTS))
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(CACHE)
    return out
