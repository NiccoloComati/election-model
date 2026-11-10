# Sources

Everything gathered for replicating Nate Silver's US election models. Downloaded November 2026.

## silver_bulletin/
Text and PDF of the 340 core and related Silver Bulletin articles, plus `index.csv`. Forecast and dashboard pages keep most of their content in the PDFs (embedded tables), not the text files. The datasets those pages link to are in `../data/silver_bulletin_datasets/`.

## fivethirtyeight/
FiveThirtyEight was taken down by ABC/Disney in March 2025. Everything here is a saved copy.

| Folder | What it is |
|---|---|
| `*.txt` + `raw/` | Four Silver-era methodology articles from the Internet Archive: 2016 user's guide, 2020 presidential, House/Senate/governor (2018–2022), pollster ratings (2023) |
| `github-data/` | Full copy of github.com/fivethirtyeight/data (frozen Feb. 2025; see `SOURCE.txt`). Most of it is unrelated (sports etc.). Useful folders: `polls/` (presidential poll averages 1968–2016, primary averages 1980–2016, old model files), `pollster-ratings/` (every edition 2014–2023, raw polls), `state-of-the-polls-2024/` (polls and results 2012–2024), `congress-generic-ballot/`, `special-elections/`, `early-senate-polls/`, `forecast-review/` |
| `archive/` | 290 FiveThirtyEight data files from the Internet Archive. For each file the largest non-HTML snapshot was kept, since "current" feeds were reset after each election and post-shutdown snapshots are redirect pages. `archive/index.csv` gives each file's snapshot date. See below |

`archive/` contents:

| Path | What it is |
|---|---|
| `polls/data/` | The poll feeds as of their last snapshot: president, Senate, House, governor, generic ballot, primaries, approval, favorability (current-cycle and `_historical` files), plus averages |
| `polls-page/data/` | Older (2021–22) location of the same feeds |
| `trump-approval-data/`, `biden-approval-data/`, `generic-ballot-data/`, `congress-generic-ballot-polls/` | Earlier standalone approval and generic-ballot feeds (2017–2022) |
| `general-model/` | 2016 general-election poll list used by the 2016 model |
| `congress-model-2018/` | 2018 midterm model outputs (House, Senate, governor forecasts) |
| `2020-general-data/` | 2020 presidential and congressional model outputs: toplines, forecast steps, economic index, fundamentals, polls, scenarios |
| `2020-primary-data/` | 2020 Democratic primary model and polls |
| `2022-general-election-forecast-data/` | 2022 midterm model outputs: toplines, steps, seat distributions, joint probabilities |
| `pollster-ratings/` | Per-pollster rating detail pages (`data.json`) |

The 2024 FiveThirtyEight forecast is deliberately not included: it is G. Elliott Morris's model, not Silver's.

## results/medsl/
State-level presidential results 1976–2024 from the MIT Election Data and Science Lab (Harvard Dataverse, doi:10.7910/DVN/42MVDX, version of Sept. 2026), plus its codebook. Used for partisan lean and for checking forecasts. Maine and Nebraska district results are not included.

## surveys/ces/
Cooperative Election Study (Harvard Dataverse, CC0). Silver Bulletin estimates state and district elasticity from this voter-level data.

| File | What it is |
|---|---|
| `cumulative_2006-2025.feather` + guide | Harmonized key variables for every CES year, 2006–2025 (read with pandas/pyarrow) |
| `CCES24_Common_OUTPUT_vv_topost_final.csv` + guide, questionnaires | 2024 Common Content with validated vote |
| `CCES22_Common_OUTPUT_vv_topost.csv` + guide, questionnaires | 2022 Common Content with validated vote |

## Not downloaded

| Source | Why |
|---|---|
| New York Times poll database | Blocks automated access; no bulk download |
| FiftyPlusOne poll database | Paid API ($100/month and up) |
| Roper Center iPoll | Needs institutional login (check MIT Libraries) |
| ANES, Pew NPORS | Free, but need a personal account and data-use agreement |
| RealClearPolling, Wikipedia poll tables | No bulk download; mostly duplicate the FiveThirtyEight feeds |
| American Presidency Project approval tables | Page now loads data by script; Silver Bulletin's historical approval file covers the same history |
