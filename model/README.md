# Presidential model (v0.3)

A replication of Silver's presidential model. It runs for two cycles. For 2024 it is checked against the Silver Bulletin model. For 2020 it is checked against Silver's FiveThirtyEight model, which he says is the same model.

```
python -m model.president.calibrate                       # refit weights, blend curve and uncertainty index
python -m model.president.run --cycle 2024                # Election Day
python -m model.president.run --cycle 2020 --date 2020-09-01
python -m model.president.run --cycle 2024 --timeseries   # weekly runs, used by the notebook
```

The charts are in `notebooks/president.ipynb`. Outputs go to `output/president/<cycle>/`.

## Components

| Step | What it does | File |
|---|---|---|
| Polls | Silver's final poll list for the cycle. The FiveThirtyEight feed adds partisan sponsor, release time, likely-voter pairs and Kennedy's share | `data.py` |
| Weights, likely voters, house effects, trendline | Fitted to Silver's published poll weights and adjustments | `polls.py` |
| Convention bounce | Applied after the trendline, keyed to field dates. Pre-convention averages are blended back in for 15 days after the 2024 Democratic convention | `polls.py` |
| Political time | Landmark events are leaps in time: a debate day counts as a week. Polls from before a landmark age faster, and scheduled landmarks still ahead lengthen the drift horizon | `polls.py` |
| Candidate swap (2024) | Silver's kamala_mode. Only Harris-Trump polls fielded from June 28 count, and the poll-volume factor of the uncertainty index is raised until September 12 | `polls.py`, `uncertainty.py` |
| Third party | Kennedy's share is imputed where a poll omits him. His projected share fades, ballot access is uncertain, and he can win states in the simulations | `polls.py`, `simulate.py` |
| State estimate | Rigid uniform swing, demographic regression, regional regression, and an estimate borrowed from demographically similar states. Partisan lean includes the home-state adjustment | `forecast.py`, `data.py` |
| Economic index | Six indicators back to 1880, standardized against 1946 onward, projected to Election Day. Each run and each past election from 1972 uses data as first published (FRED's ALFRED archive) | `economy.py` |
| Fundamentals | Economy, incumbency tier, previous margin and rematch, damped by polarization. Fitted on 1880 to the previous cycle. The 2024 fit also uses the five fundamentals values Silver reported that year | `fundamentals.py` |
| Uncertainty index | Eight of Silver's nine factors, standardized against 1968–2024. It scales drift, and Election Day error slightly | `uncertainty.py` |
| Simulation | 40,000 runs with fat-tailed national, demographic, regional and state errors | `simulate.py` |

Every parameter in `config.py` is tagged by source: stated by Silver, from Silver-era FiveThirtyEight, fitted, or assumed.

## Results on Election Day

| | 2024 replication | 2024 Silver | 2020 replication | 2020 Silver |
|---|---|---|---|---|
| Democratic Electoral College win | 50.5% | 50.0% | 84.9% | 89.2% |
| Democratic electoral votes | 271 | 271 | 338 | 348 |
| Popular vote margin, D minus R | +2.6 | +2.2 | +7.4 | +8.0 |
| Swing-state margin gap with Silver | 0.16 | | 0.83 | |
| Average miss against actual results | 3.9 | 3.9 | 5.3 | 5.4 |

The margin gap and average miss are root-mean-square errors in points.

## Not implemented yet

These are flagged in `config.NOT_IMPLEMENTED` and in the notebook:

- **Economists' projections.** The economic index uses mean reversion to project indicators to Election Day. Silver also uses professional forecasters' GDP forecasts and recent stock returns. This is the likely reason the replication's 2024 fundamentals don't move within the campaign as Silver's did.
- **News volume.** Silver's ninth uncertainty factor counts full-width New York Times headlines. It is left out until a headline archive is found.
- **Economic-uncertainty factor.** Silver's 2024 factor comes from a Federal Reserve survey of economists. We use the spread of the six index components as a stand-in.
- **First-release data before 1972.** Payrolls and industrial production are as first published from 1972, income and consumption from 1984. Earlier elections use revised data.
- **Pre-1946 proxies.** Before each official series begins, the economic index averages only the indicators available. Silver extends all six indicators back to 1880 with proxies.
- **Pre-1968 polls.** Election Day polling error is checked on 1968–2024 averages. Silver goes back to 1936.

## Known differences from Silver

- **August 2024.** After Harris entered, the replication's polling averages ran 1 to 2 points more Democratic than Silver's. Its forecast still overshoots his by 5 to 10 points until mid-September. Other periods and all of 2020 track closely.
- **Assumed values.** Some sizes are assumptions because Silver didn't publish them:
  - the jumps in political time other than debates
  - the size of the kamala_mode volume adjustment
  - the home-state bonus
  - the 2020 virtual-convention bounce
  - Kennedy's ballot access and fade
  - the similar-states mix
- **2016 and 2020 district results.** Maine's and Nebraska's district results are hand-entered in `data.py` and should be verified.
- **Demographic profiles.** Both cycles use the 2022 Cooperative Election Study.
