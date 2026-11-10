# Election model

A replication of Nate Silver's US presidential forecast, rebuilt from his Silver Bulletin articles and published outputs and tested on 2020 and 2024 against his day-by-day forecasts. Replicating his US models comes first; adapting the approach to European elections is the longer-term aim.

- `docs/methodology.html`: short methods note (open in a browser)
- `notebooks/president.ipynb`: charts comparing the replication with Silver over each campaign
- `model/president/`: the model; `model/README.md` explains components, parameters and results
- `notes/`, `data/findings.csv`, `extractions/`: model details extracted from about 100 Silver Bulletin articles
- `tools/`: scripts for downloading and processing sources

## Data not in this repository

| What | Why | How to get it |
|---|---|---|
| Silver Bulletin articles and paywalled datasets | Subscription content, private use only | Paid subscription; `tools/save_tabs.py`, `tools/download_datasets.py hosted` |
| FiveThirtyEight data (github-data, Wayback archive) | Large (about 1.2 GB) | `git clone https://github.com/fivethirtyeight/data`; `tools/fetch_538_archive.py` |
| Cooperative Election Study | Large (about 500 MB) | Harvard Dataverse (see `sources/README.md`) |
| Model outputs | Generated | `python -m model.president.run --cycle 2024 --timeseries` |

Running the model needs the Silver Bulletin final poll list and model outputs for 2024, which come with a subscription.
