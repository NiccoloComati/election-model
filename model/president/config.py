"""Parameters for the presidential model (v0.2). Cycles: 2024 (Silver Bulletin) and 2020 (Silver's FiveThirtyEight).

Source tags:
  [SB]   stated in a Silver Bulletin article (see notes/components/)
  [538]  stated in a Silver-era FiveThirtyEight methodology article
  [FIT]  fitted to Silver's published outputs or to historical data (calibrate.py, economy.py, uncertainty.py)
  [ASSUMED] our choice where the sources give no number
  [NOT IMPLEMENTED] part of Silver's method we have not built yet; see NOT_IMPLEMENTED
"""
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HOSTED = ROOT / "data" / "silver_bulletin_datasets" / "hosted"
ARCHIVE = ROOT / "sources" / "fivethirtyeight" / "archive"
GITHUB_538 = ROOT / "sources" / "fivethirtyeight" / "github-data"
RESULTS = ROOT / "sources" / "results" / "medsl" / "1976-2024-president.csv"
OUT = ROOT / "output" / "president"
CACHE = OUT / "_cache"
CALIBRATION = Path(__file__).with_name("calibration.json")

NOT_IMPLEMENTED = {
    "economist_projection": "Projection of economic indicators to Election Day uses mean reversion only; Silver also "
                            "uses Survey of Professional Forecasters GDP forecasts and recent stock returns. Needs SPF data.",
    "news_volume": "Uncertainty-index factor 'news volume' (count of full-width New York Times headlines, recent days "
                   "weighted more) is left out of the index. Needs a headline archive.",
    "pre1946_proxies": "Before each official series starts, the economic index averages only the indicators available "
                       "(1880-1912: stocks and prices); Silver extends all six with proxies back to 1880.",
    "early_polls_1936": "Election Day polling error is checked on 1968-2024 averages; Silver calibrates back to 1936.",
    "economic_uncertainty_survey": "Uncertainty-index factor 'economic uncertainty' should come from a Federal Reserve "
                                   "survey of economists (expected change in the economy); we use the spread of the "
                                   "six index components as a stand-in.",
    "pit_before_1972": "Point-in-time (as first published) economic data from 1972 (jobs, industrial production) and "
                       "1984 (income, spending); earlier elections use revised data.",
}


def election_day(year):
    """First Tuesday after the first Monday in November."""
    d = dt.date(year, 11, 2)
    while d.weekday() != 1:
        d += dt.timedelta(days=1)
    return d.isoformat()


ELECTION_DAYS = {y: election_day(y) for y in range(1868, 2032, 4)}

# home states (pres, vp) by party, for the home-state adjustment                 [538 2016]/[SB 2024]
HOME = {
    2012: {"D": ("IL", "DE"), "R": ("MA", "WI")},
    2016: {"D": ("NY", "VA"), "R": ("NY", "IN")},
    2020: {"D": ("DE", "CA"), "R": ("FL", "IN")},
    2024: {"D": ("CA", "MN"), "R": ("FL", "OH")},
}
HOME_BONUS = {"pres": 3.5, "vp": 1.0}   # [ASSUMED] 538 2016 found ~7 and ~2 historically; SB 2024 "permanently reduced" it

CYCLES = {
    2024: {
        "dem": "Kamala Harris", "rep": "Donald Trump", "inc_party": "D",
        "pollist": ("hosted", "2024-11-05_pres-pollist"), "feed538": ARCHIVE / "polls" / "data" / "president_polls.csv",
        "ratings": ("sb", "pollster-stats-full-2024"), "first_poll_end": "2024-06-28",
        "conventions": [("2024-07-15", "2024-07-18", "R"), ("2024-08-19", "2024-08-22", "D")],
        "bounce_peak": 2.25,                                  # [SB]
        "landmarks": [("2024-08-19", "2024-08-22", 15)],      # [SB] pre-DNC averages blended back in, gone ~2 weeks after
        "lean_years": {2020: 0.75, 2016: 0.25},
        "n3pc": {"name": "Robert F. Kennedy", "until": "2024-08-23"},
        "error_multiplier": 1.0,
        # kamala_mode [SB, "How the election model handles a candidate swap", 2024-07-31]
        "poll_start_min": "2024-06-28",                       # only Harris-Trump polls fielded from June 28 on
        "volume_fudge": {"start": "2024-07-30", "until": "2024-09-12", "z": 2.0},   # size [ASSUMED]: fitting it to
                                                              # Silver's August odds was not decisive (effect < 2 pts)
        "events": [("2024-06-27", "debate"), ("2024-07-15", "vp_pick"), ("2024-07-18", "convention"),
                   ("2024-07-21", "exit"), ("2024-07-22", "nominee"), ("2024-08-06", "vp_pick"),
                   ("2024-08-22", "convention"), ("2024-08-23", "exit"), ("2024-09-10", "debate"),
                   ("2024-10-01", "vp_debate")],
        "outputs": "sb2024",
    },
    2020: {
        "dem": "Joseph R. Biden Jr.", "rep": "Donald Trump", "inc_party": "R", "feed_dem": "Joe Biden",
        "pollist": ("archive", "2020-general-data/presidential_polls_2020.csv"),
        "feed538": ARCHIVE / "polls" / "data" / "president_polls_historical.csv",
        "ratings": ("538", "2020"), "first_poll_end": None,
        "conventions": [("2020-08-17", "2020-08-20", "D"), ("2020-08-24", "2020-08-27", "R")],
        "bounce_peak": 1.5,                                   # [ASSUMED] 538 2020 reduced the bounce for virtual conventions
        "landmarks": [],
        "lean_years": {2016: 0.75, 2012: 0.25},
        "n3pc": None,
        "error_multiplier": 1.2,                              # [538 2020] COVID: +20% national, correlated and state error
        "poll_start_min": None, "volume_fudge": None,
        "events": [("2020-06-05", "clinch"), ("2020-08-11", "vp_pick"), ("2020-08-20", "convention"),
                   ("2020-08-27", "convention"), ("2020-09-29", "debate"), ("2020-10-07", "vp_debate"),
                   ("2020-10-22", "debate")],
        "outputs": "538_2020",
    },
}
BOUNCE_DAYS = 22             # [SB] linear decay to zero this many days after the convention ends
# Landmark events are leaps ahead in "political time" [SB]: polls before them age faster, and scheduled ones
# still ahead add to the drift horizon. Debate day = one week [SB]; the other sizes are [ASSUMED].
EVENT_JUMP_DAYS = {"debate": 7, "vp_debate": 3.5, "convention": 7, "vp_pick": 7, "exit": 7, "nominee": 7, "clinch": 7}

# --- poll weights ([FIT] per cycle by calibrate.py from Silver's poll list; these are fallbacks) ---
WEIGHT = {"intercept": -1.37, "log_n": 0.22, "ppm": -0.36, "log_nfirm": -0.12, "tracking": -1.66,
          "ppm_unrated": 0.63, "default_n": 600}
RECENCY = {"window_days": 42, "power": 1.5, "sparse_ref_polls": 10, "max_window_days": 120, "early_stretch": 0.2}
LV_PRIOR_POLLS = 5           # [ASSUMED]
HOUSE = {"shrink_polls": 10.0, "partisan_prior_margin": 3.0, "iterations": 4, "center_ppm_max": 99,
         "always_rep": ["Trafalgar Group"]}
# trendline: conservative bandwidth and early aggressiveness [FIT] to Silver's published 2024 daily averages
TREND = {"bandwidth_conservative": 20.0, "bandwidth_aggressive": 5.0, "aggressive_share_early": 0.0,
         "aggressive_share_late": 0.6, "state_poll_discount": 0.5}

# --- named third-party candidate [SB]: imputed where a poll omits him; right-skewed simulated share ---
N3PC = {
    "draw_share_from_major": 0.8,   # [ASSUMED] share of his support taken from the two majors (538 2016: little from undecideds)
    "projection_factor": 0.85,      # [ASSUMED] third-party support fades toward Election Day
    "ballot_access": 0.85,          # [ASSUMED] per-state probability where status is unknown
    "national_sd": 0.5,             # [ASSUMED] log-scale SD of the national draw (right tail)
    "state_sd": 0.3,                # [ASSUMED]
}

# --- undecided / other [SB]: undecideds split evenly; 'other' lower in battlegrounds (tactical voting) ---
OTHER_SCALE = 1.0
OTHER_BATTLEGROUND_DISCOUNT = 0.25   # [ASSUMED] other share x (1 - 0.25) in a tied state, x1 when lean >= 10

# --- state estimate ---
NATIONAL_BOTTOM_UP_SHARE = 0.75      # [538]
REG_MIX = {"rigid": 0.4, "demographic": 0.25, "regional": 0.15, "similar": 0.2}   # [538] ordering; "similar" [ASSUMED]
DEMO_RIDGE = 30.0                    # [ASSUMED]
REGIONAL_RIDGE = 10.0                # [ASSUMED]
SIMILAR = {"bandwidth": 1.5, "ridge": 5.0}   # [ASSUMED] borrowing from demographically similar states
BLEND_CURVE = [0.18833, 0.66472, -0.14134]   # [FIT] per cycle in calibration.json

# --- fundamentals [538]/[SB] ---
FUNDAMENTALS_SCHEDULE = [(0, 0.0), (5, .03), (10, .06), (25, .11), (50, .16), (75, .21),
                         (100, .26), (150, .35), (200, .43), (250, .53)]
FUNDAMENTALS = {"first_year": 1880, "target_weight": 2.0}   # damping, half-life [FIT]; weight of Silver's reported values [FIT]
FUNDAMENTALS_REPORTED = {  # [SB] values Silver reported in 2024, used to check our fundamentals model
    "2024-06-26 Biden": 2.5, "2024-07-29 Harris": 0.0, "2024-08-31 Harris": 0.0, "2024-09-03 Harris": -0.3,
    "2024-10-17 Harris": 1.0}

# --- economic index [538]/[SB]: six indicators, two years, heavier weight on the final ~six months ---
#     [FIT] economy.calibrate: 6-month annualized growth, averaged over 12 months, last 3 months weighted 3x;
#     reproduces Silver's reported values (1946-2024 Election Day indexes, 2020 and 2024 components) to 0.29 SD
ECON = {"growth_horizon": 6, "window_months": 12, "recent_months": 3, "older_weight": 0.33, "standardize_from": 1946,
        "month": 10, "reversion_per_month": 0.85}   # reversion [ASSUMED] (see NOT_IMPLEMENTED: economist_projection)

# --- uncertainty [SB]/[538] ---
ERROR = {
    "drift_const": 0.75,       # [FIT] by uncertainty.calibrate_drift (fallback); drift = const x days^(1/3) x index
    "index_kappa": 0.3,        # [FIT] index multiplier = exp(kappa x mean factor z)
    "error_index_power": 0.25, # [ASSUMED] index affects Election Day error "only at the margin"
    "national": 4.0,           # [FIT] at index 0; equals 3.2 at 2024's Election Day index (-0.95), the value fitted to
                               # Silver's 2024 final spread (his ~3.1 SD is calibrated on polls since 1936)
    "group_swing": 10.0, "region_swing": 1.0, "state_floor": 1.5, "state_poll_term": 3.0,
    "small_state_extra": 1.0, "t_df": 10,
}
SIMS = 40000
SEED = 2024


def load_calibration(cycle):
    if CALIBRATION.exists():
        c = json.loads(CALIBRATION.read_text()).get(str(cycle), {})
        WEIGHT.update(c.get("weight", {}))
        if "blend_curve" in c:
            BLEND_CURVE[:] = c["blend_curve"]
        ERROR.update(json.loads(CALIBRATION.read_text()).get("uncertainty", {}))
