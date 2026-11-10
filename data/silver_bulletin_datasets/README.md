# Silver Bulletin datasets

Downloaded on 2026-11-06 with `tools/download_datasets.py`, from links preserved in the saved article PDFs.
Silver Bulletin allows free use of its raw poll data with attribution. The other files came from a paid subscription and are for private research only.

## hosted/ — files Silver Bulletin hosts (20 XLSX, paywalled)

**2024 presidential model outputs** (final forecast page, Nov. 5, 2024). One row per model run date. Columns ending `_inc` are the incumbent party's candidate (Harris), `_chal` the challenger (Trump), `_3rd` the third candidate (Kennedy, while in the race). The Harris-era files start on 2024-07-29.

| File | What it holds |
|---|---|
| national-topline | Daily national win probabilities, EV and popular-vote projections (35 columns) |
| state-topline | Daily state forecasts incl. win probability, tipping point, voter power index (32 columns) |
| forecast-steps | State-by-state values at each model step (polls → adjusted → fundamentals → forecast) |
| poll-average | Daily state and national polling averages, raw and trend-adjusted |
| pres-pollist | Every presidential poll used, with pollster rating ID, sample size and weights |
| econ-index | Economic index: current and projected z-scores with ranges |
| ev-probabilities | Probability distribution over electoral votes |
| voteshare-probabilities | Probability distribution over popular-vote share |
| ec-vs-popvote | Electoral College win probability by popular-vote bin |
| election-paths | The 128 swing-state combination paths and their probabilities |
| scenario-analysis | Named scenarios and their probabilities |

**Pollster ratings**

| File | What it holds |
|---|---|
| rawpolls-061224 / -021325 / -040626 | Every poll in the ratings database (about 11,500 to 12,350 rows, 29 columns), three editions |
| pollster-stats-full-2024 / -2025 / -2026 | Ratings, plus-minus scores, bias, herding stats per pollster, with a column dictionary sheet |

**Historical averages**

| File | What it holds |
|---|---|
| generic-topline-all-cycles | Daily generic-ballot averages with 90% bands, 1994–2026 cycles, by subgroup |
| historical-approval-averages | Daily presidential approval and disapproval averages, Truman to Trump, by subgroup |
| biden-schedule | Biden's daily public-event schedule (from a 2025 media article) |

## sheets/ — published poll databases (Google Sheets, as CSV)

Every poll in each Silver Bulletin average, with pollster, dates, sample, population, weight and influence:
Trump approval (about 6,800 polls), generic ballot (about 690), Iran War support, Elon Musk favorability.

## charts/ — Datawrapper chart data (505 CSVs, public)

The data behind every chart in the saved articles, in one folder per article. Names are `<chart id>__<chart title>.csv`.
`charts/index.csv` lists each chart's title and the articles that use it. Charts with identical titles on FLIPR pages are usually the Deluxe, Classic and Lite versions of the same view. Some files are tab-separated rather than comma-separated.
