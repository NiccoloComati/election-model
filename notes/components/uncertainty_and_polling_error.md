# Uncertainty and polling error

207 findings from 67 articles, oldest first.

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**data source** · FiveThirtyEight 2016 presidential · explicit

The 2016 model's probabilities are based on the historical accuracy of election polls since 1972, effectively 11 elections from 1972 to 2012.

*Numbers:* elections in calibration = 11 elections (1972-2012)

> Our probabilities are based on the historical accuracy of election polls since 1972.

<sub>fte_2016-general-election-forecast-users-guide#1</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**method** · FiveThirtyEight 2016 presidential · explicit

The 2016 national error magnitude grew with time until the election, the number of undecided voters and the third-party vote. National error is applied to every state about equally, subject to elasticity.

> The magnitude of the national error is based upon: The amount of time until the election (more time = more error); the number of undecided voters (more undecideds = more error); and the number of third-party voters

<sub>fte_2016-general-election-forecast-users-guide#19</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**method** · FiveThirtyEight 2016 presidential · explicit

State-specific error is larger when a state has fewer polls, when polls and the demographic regression disagree (e.g. Utah 2016), and when the state has a smaller population, since small states are more idiosyncratic and harder to poll and model.

> And states have more state-specific error when they have smaller populations.

<sub>fte_2016-general-election-forecast-users-guide#21</sub>

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**method** · FiveThirtyEight midterm models · explicit

The midterm models account for four error types: (1) local error, larger with less polling, conflicting indicators, or high elasticity, such as New Hampshire versus the bifurcated South; (2) regional and demographic error simulated with CANTOR similarity; (3) incumbency-driven error, for instance polls systematically underestimating Republican incumbents; (4) a uniform national swing, smaller for governor races. Error shrinks as Election Day approaches.

> Third, there can be error driven by incumbency status.

<sub>fte_midterm-house-senate-governor-methodology#22</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

The 2020 model distinguishes four error types: national drift (change in the national forecast before Election Day), national Election Day error (final forecast miss), correlated state error along demographic or geographic lines, and state-specific error.

> With that disclaimer out of the way, here are the four types of uncertainty that the model tries to account for:

<sub>fte_2020-presidential-forecast-methodology#20</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

The FiveThirtyEight Uncertainty Index is an equally weighted blend of eight measures: (1) undecided share in national polls; (2) undecided plus third-party share; (3) polarization from House roll-call distance, which lowers uncertainty; (4) volatility of the national polling average; (5) volume of national polling; (6) gap between the polling snapshot and the fundamentals forecast; (7) standard deviation of the economic index components; (8) news volume, measured by full-width New York Times headlines over the past 500 days with recent days weighted more. In 2020 the overall level was about average relative to elections since 1972.

*Numbers:* index components = 8 measures (equal weights); news lookback = 500 days (NYT full-width headlines)

*Why:* With small samples and correlated measures, use an equal-weight blend rather than picking one or two metrics.

> we think it is better to use an equally-weighted blend of all reasonable metrics rather than picking and choosing just one or two metrics.

<sub>fte_2020-presidential-forecast-methodology#22</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

National Election Day error uses a version of the uncertainty index that de-emphasizes components 6 to 8, which relate to future movement, and is calibrated on final-poll errors in elections since 1936 for sample size. Fat-tailed distributions are used for many error components, including Election Day error.

*Numbers:* calibration start = 1936 year (final-poll errors)

*Why:* Conservative given small samples; very accurate 2004-2012 polls may not be replicable.

> the calculation is based on the error in final polls in elections since 1936 , rather than solely on more recent elections.

<sub>fte_2020-presidential-forecast-methodology#23</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**parameter or number** · FiveThirtyEight 2020 presidential · explicit

For 2020 the model increased national Election Day error, correlated state error and state-specific error by 20 percent, since pandemic primaries showed about 50 percent higher turnout variability and a 50 percent rise in turnout error is estimated to raise vote-share error by 20 percent. This COVID adjustment was removed in 2024.

*Numbers:* error inflation = 20 percent (2020 COVID); turnout variability increase = about 50 percent (pandemic primaries)

> we increase national Election Day error, correlated state error and state-specific error by 20 percent relative to their usual values

<sub>fte_2020-presidential-forecast-methodology#24</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

Residual state-specific error is relatively small and mainly a function of polling volume, larger in states with no polling, which is why unpolled Oregon had higher Trump odds than expected at the 2020 launch.

> This tends to be relatively small, and is primarily a function of the volume of polling in each state, especially in states that have had no polling at all.

<sub>fte_2020-presidential-forecast-methodology#28</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**parameter or number** · FiveThirtyEight pollster ratings 2023 · explicit

Poll error decomposes as Total Error = sqrt(Sampling Error^2 + Temporal Error^2 + Pollster Error^2). A 1,000-voter poll misses the final margin by only about 2.5 points on average from sampling error alone. Even with no temporal or sampling error, the average poll would still miss the margin by about 2 points from pollster-induced error.

*Numbers:* sampling error, n=1000 = about 2.5 points (margin) (average miss); irreducible pollster error = about 2 points (margin) (average miss)

> the average poll would still miss the final margin in the race by about 2 points.

<sub>fte_pollster-ratings-methodology#6</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**limitation or failure mode** · general principle · explicit

Training or calibrating forecasting models on historical data cleaned with hindsight leads to overconfidence. Real-time data will contain edge cases and minor errors that would have been removed in hindsight but cannot be caught in advance, so error estimates from cleaned data understate live uncertainty.

*Why:* Cleaned data neglects the challenges of handling new, messy data as it arrives.

> it can lead to overconfidence when using that data to train or build models. If you clean up a past data set based on information that wouldn't have been available to you at the time

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#8</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**empirical regularity** · general principle · explicit

The direction of polling error has historically been impossible to predict in advance. Conventional wisdom has usually been wrong when it tried to guess which party polls would underrate, so forecasts should treat systematic polling error as symmetric around zero rather than assuming error in one party's favor.

*Why:* In 2012 and 2022 insiders expected Democrats to underperform their polls but they outperformed. In 2014 and 2016 the reverse happened.

> it's historically been impossible to predict the direction in which polls are wrong, and the conventional wisdom has usually been wrong when it tried to guess.

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#0</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**method** · 538 pollster accuracy database (2023) · inferred_from_chart

The FiveThirtyEight polling-bias and polling-error metrics use polls whose median field date falls in the final 21 days before the election. They include presidential, Senate, House and gubernatorial general elections since 1998, plus special elections and runoffs, and exclude pollsters banned by FiveThirtyEight.

*Numbers:* poll window = 21 days (final days before election, based on poll's median field date); start year = 1998 (first cycle in the accuracy database tables)

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#1</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**method** · 538 pollster accuracy database · inferred_from_chart

Statistical bias in the FiveThirtyEight table is calculated only for elections in which the top two finishers were a Republican and a Democrat. It is therefore not calculated for presidential primaries.

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#3</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**parameter or number** · 538 pollster accuracy database · inferred_from_chart

Weighted-average statistical bias of final-21-day polls, by cycle, for president, Senate, House and governor. Positive D values mean polls overstated Democrats. Combined values are partially truncated in the image.

*Numbers:* 1998 bias = Sen R+4.5, House R+0.9, Gov R+5.7, Combined R+3 percentage points (1998 cycle); 2000 bias = Pres R+2.4, Sen R+2.8, House D+1.1, Gov R+0.2 percentage points (1999-2000 cycle); 2002 bias = Sen D+2.0, House D+1.6, Gov D+3.4 percentage points (2001-02 cycle); 2004 bias = Pres D+1.2, Sen D+0.8, House D+2.2, Gov D+2.0 percentage points (2003-04 cycle); 2006 bias = Sen R+2.1, House D+1.1, Gov D+0.4 percentage points (2005-06 cycle); 2008 bias = Pres D+0.9, Sen D+0.4, House D+1.3, Gov R+0.1 percentage points (2007-08 cycle); 2010 bias = Sen R+0.8, House D+1.3, Gov R+0.2 percentage points (2009-10 cycle); 2012 bias = Pres R+2.5, Sen R+3.2, House R+3.3, Gov R+1.6 percentage points (2011-12 cycle); 2014 bias = Sen D+2.7, House D+4.0, Gov D+2.3 percentage points (2013-14 cycle); 2016 bias = Pres D+3.3, Sen D+2.8, House D+4.1, Gov D+3.1 percentage points (2015-16 cycle); 2018 bias = Sen EVEN, House R+0.5, Gov R+1.0 percentage points (2017-18 cycle); 2020 bias = Pres D+4.1, Sen D+4.9, House D+6.1, Gov D+5.6 percentage points (2019-20 cycle); 2022 bias = Sen R+0.3, House D+0.2, Gov D+1.3 percentage points (2021-22 cycle); all-years bias = Pres D+1.2, Sen D+0.6, House D+1.2, Gov D+0.9 percentage points (1998-2022 pooled)

*Why:* Shows that bias is unpredictable from election to election.

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#5</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**parameter or number** · 538 pollster accuracy database · inferred_from_chart

Weighted-average absolute error of final-21-day polls, by cycle and election type. Presidential primary error is roughly double general-election error. 2021-22 was historically accurate.

*Numbers:* all-years error = Pres primary 9.2, Pres general 4.3, Sen 5.4, House 6.1, Gov 5.4 percentage points (1998-2022 pooled); 2022 error = Sen 4.8, House 4.0, Gov 5.1 percentage points (2021-22 cycle); 2020 error = Pres primary 10.2, Pres general 5.0, Sen 5.8, House 6.5, Gov 6.4 percentage points (2019-20 cycle); 2016 error = Pres primary 10.2, Pres general 4.9, Sen 5.0, House 5.8, Gov 5.4 percentage points (2015-16 cycle); 2018 error = Sen 4.2, House 4.9, Gov 5.2 percentage points (2017-18 cycle); 2014 error = Sen 5.3, House 6.8, Gov 4.5 percentage points (2013-14 cycle); 2012 error = Pres primary 8.9, Pres general 3.7, Sen 4.7, House 5.5, Gov 4.9 percentage points (2011-12 cycle); 2010 error = Sen 4.9, House 7.0, Gov 4.7 percentage points (2009-10 cycle); 2008 error = Pres primary 7.7, Pres general 3.5, Sen 4.7, House 5.9, Gov 4.4 percentage points (2007-08 cycle); 2006 error = Sen 5.2, House 6.5, Gov 5.1 percentage points (2005-06 cycle); 2004 error = Pres primary 7.0, Pres general 3.3, Sen 5.3, House 5.8, Gov 5.5 percentage points (2003-04 cycle); 2002 error = Sen 5.5, House 5.6, Gov 5.2 percentage points (2001-02 cycle); 2000 error = Pres primary 7.9, Pres general 4.4, Sen 6.0, House 4.3, Gov 4.9 percentage points (1999-2000 cycle); 1998 error = Sen 7.5, House 7.1, Gov 8.1 percentage points (1998 cycle)

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#6</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**empirical regularity** · general principle · explicit

There is no clear long-term trend in polling accuracy. Polls were pretty good in 2012, 2018 and 2022, quite bad in 2016 and 2020, and in between in 2014. Silver accepts a mild prior that polling is getting worse because of declining response rates, but rejects a binary 'polls work vs. polls are broken' framing.

*Why:* Poor polling years also occurred before the modern era (1998, 1980, 1948).

> If you want to start with the prior that polling is getting worse a priori because of declining response rates, I don't have a big problem with that.

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#7</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**empirical regularity** · general principle · explicit

In both elections with Trump on the ballot (2016 and 2020), polls overstated the Democrat. Biden in 2020 considerably underperformed his polls but held on in tipping-point states such as Georgia and Wisconsin because his lead was large.

> that's what happened to the Democrat the only other two times that Trump was on the ballot in 2016 and 2020.

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#12</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**model change** · 2024 presidential vs 2020 · explicit

The 2020 model added a COVID-related increase in overall uncertainty. It is removed in the 2024 model.

*Why:* The pandemic is over.

> increasing the overall amount of uncertainty in the model

<sub>2024-06-26_2024-presidential-election-model-methodology-update#3</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**model change** · 2024 presidential · explicit

The 2024 uncertainty index adds a ninth component: whether one or both parties renominated the previous election's candidate. Repeat candidates make elections more stable and less uncertain. Because both 2024 candidates are repeaters, overall uncertainty is slightly reduced.

*Numbers:* uncertainty index components = 9 components (2024 model, up from 8)

*Why:* Repeat candidates are better known.

> The model also now includes a ninth component in its uncertainty index, indicating whether one or both parties have nominated the same candidate as in the previous election.

<sub>2024-06-26_2024-presidential-election-model-methodology-update#20</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**method** · 2024 presidential · explicit

The uncertainty index estimates overall error in the system. It has a modest effect on expected Election Day polling error and a much bigger effect on expected poll volatility (drift) between now and the election.

> The uncertainty index has a modest effect on how much error the model expects there to be in the polls on Election Day — but the much bigger effect is on how much volatility

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#33</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**model change** · 2024 presidential · explicit

The 2024 uncertainty index uses nine variables, up from eight in 2020. The new variable captures whether candidates are repeat candidates: when both were on the last ballot, they are better known and the polls are less volatile.

*Numbers:* uncertainty index variables 2024 = 9 variables (2024); uncertainty index variables 2020 = 8 variables (2020)

*Why:* Repeat candidates are better known by voters.

> repeat candidates tend to produce less volatility in the polls than first-time ones since they are better known by voters. (This is the factor we newly account for this year.)

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#34</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**method** · 2024 presidential · explicit

The nine uncertainty index variables are: (1) poll stability to date; (2) polarization level; (3) repeat candidates; (4) economic volatility; (5) polling volume; (6) the gap between polls and fundamentals; (7) the volume of news, measured by the number of full-width New York Times headlines; (8) the undecided vote share; (9) third-party vote share. Higher stability, polarization, polling volume and repeat candidates mean lower uncertainty. Higher undecided and third-party shares mean higher uncertainty.

> as measured by the number of full-width New York Times headlines

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#35</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**parameter or number** · 2024 presidential · explicit

In June 2024, seven of the nine uncertainty index factors pointed toward low uncertainty and two (high undecided vote, Kennedy's third-party share) toward higher. The index read 'low' rather than the 'average' Silver expected.

*Numbers:* factors pointing to stability = 7-2 (June 2024)

> So by a 7-2 verdict, the factors in the uncertainty index imply that this will be a relatively stable race.

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#36</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**parameter or number** · 2024 presidential · explicit

The model calibrates Election Day polling accuracy on elections back to 1936, including big misses like 1948. This makes expected polling error about 35 percent higher than training only on recent polling, so the model anticipates possible secular decline from the 'Golden Age of Polling' of roughly 2004-2012.

*Numbers:* polling error calibration start = 1936 year (Election Day polling error); expected error inflation vs recent-only training = about 35 percent (2024 model)

*Why:* Conservative assumptions about systematic polling error.

> This makes the error it expects about 35 percent higher than if we’d trained it only on more recent polling.

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#38</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**assumption** · general principle · explicit

The direction of polling error is hard to predict, so the model treats a candidate as roughly as likely to underperform their polls as to overperform them. The error is unbiased in direction.

> it’s hard to predict the direction of polling error. Biden could easily overachieve his current polls — but it’s roughly as likely that he’ll underachieve them instead

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#39</sub>

### 2024-06-27 · [Are these guys trying to muddle through? Or playing to win?](https://www.natesilver.net/p/are-these-guys-trying-to-muddle-through)
**adjustment rule** · 2024 presidential · explicit

In the Silver Bulletin model, a larger undecided vote in polls increases the model's uncertainty parameter. This helps whichever candidate is currently behind.

*Why:* More undecided voters means more room for the race to move, which widens the outcome distribution and benefits the trailing candidate.

> These polls also showed a large undecided vote, which increases the model's uncertainty parameter (helpful for whichever candidate is currently behind).

<sub>2024-06-27_are-these-guys-trying-to-muddle-through-or-playing-to-win#8</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**parameter or number** · 2024 presidential · explicit

The polls component of the Silver Bulletin presidential model is calibrated on presidential elections since 1968. That sample includes many cycles with sparse polling or polling that began late in the campaign, so the model should in theory handle a late candidate switch.

*Numbers:* polls component calibration start = 1968 year (start of the calibration sample for the polls component)

*Why:* The historical sample includes data-sparse cycles.

> The "polls" part of the model was calibrated based on elections since 1968

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#1</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**method** · 2024 presidential · explicit

The Silver Bulletin presidential model computes an 'uncertainty index'. Inputs include the volume of polling (fewer polls means more uncertainty) and the amount of major news, measured by things like banner newspaper headlines.

*Why:* A candidate switch would automatically raise uncertainty through these inputs, without ad hoc parameters.

> the model would account for the fact that there were initially far fewer polls, and therefore more uncertainty. And the candidate switch would undoubtedly inspire days and days of banner newspaper headlines

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#7</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**critique of other approach** · Economist 2024 · explicit

Silver thinks the Economist model likely errs toward overconfidence, but considers this probably fine in 2024 because the uncertainty index is low. At the time, it gave Trump 74% to win, the most confident model.

*Numbers:* Economist Trump win probability = 74 percent (as of July 1, 2024)

> I think it likely errs on the side of overconfidence. But that's probably fine for this year, when the uncertainty index is relatively low.

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#12</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**method** · 2024 presidential · explicit

The Silver Bulletin presidential model has two main uncertainty parameters. 'Drift' is how much the forecast will move between now and Election Day, based on polls and other inputs. 'Error' is how accurate the forecast, essentially the polling, will be on Election Day, when the model is mostly polls-only.

> what in the model I call "drift" as opposed to "error"

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#26</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**assumption** · 2024 presidential · explicit

Election Day error is calibrated conservatively on polling data back to 1936, so the model expects a fairly large systematic polling error is possible. Against that sample, the 2020 error was relatively normal even though it was bad by recent standards.

*Numbers:* error calibration start = 1936 year (Election Day polling error calibration)

*Why:* A hedge against polls possibly becoming secularly less accurate as response rates decline.

> the model is calibrated based on polling dating all the way back to 1936, when the industry was pretty young and the polls often weren't that accurate

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#27</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**parameter or number** · 2024 presidential · explicit

As of July 2024, drift had a one-SD value of about 3-4 points on the Trump-Biden margin and Election Day error about 3 points. They combine by root sum of squares to a little under 5 points for the national popular vote, with additional error for state-level predictions.

*Numbers:* drift SD = about 3 to 4 percentage points (margin) (July 1, 2024, about 4 months out); Election Day error SD = about 3 percentage points (margin) (2024); combined national error = a little under 5 percentage points (margin) (root sum of squares, July 2024)

> "drift" takes on a value where a one standard deviation shift is about 3 to 4 points in the margin between Trump and Biden, while Election Day "error" is about 3 points

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#29</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**interpretation guidance** · 2024 presidential · explicit

A decent portion of a trailing candidate's win probability (Biden in 2024) comes from the possibility of a systematic polling error. Such errors are symmetric and need not favor the trailing side; they did not favor Democrats in 2016 or 2020.

> these errors don't always work in your favor — they didn't for Democrats in 2016 or 2020

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#31</sub>

### 2024-07-05 · [The broken leg problem](https://www.natesilver.net/p/the-broken-leg-problem)
**assumption** · general principle · explicit

Polling error preserves some chance for a trailing candidate even in a 'deterministic-seeming' situation. Unlike a game's final score, the polls can be wrong.

> unlike in football, the "final score" in elections isn't always accurate — sometimes the polls are wrong.

<sub>2024-07-05_the-broken-leg-problem-by-nate-silver-silver-bulletin#8</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**method** · 2024 presidential · explicit

The Silver Bulletin model separates two sources of uncertainty. 'Drift' is how much the polls will move between now and Election Day. 'Error' is how well Election Day polls capture the actual result.

> First, there’s how much the polls will move between now and Election Day. This is what we call “drift” in our forecast. And second, there’s uncertainty in how well Election Day polls will capture the actual result — what we call “error”.

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#8</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**empirical regularity** · 2024 presidential · explicit

In the current highly polarized era, poll drift is much smaller than it once was, because few votes are up for grabs and polls settle on their final margin earlier. Election Day error can still be large, as in 2020 when polls underestimated Trump.

*Why:* Polarization reduces the number of persuadable voters.

> in a time of extremely high polarization, “drift” is much less than it once was: the polls hone in toward their final margin earlier since few people’s votes are actually up for grabs

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#9</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**design principle** · 2024 presidential · implied

Silver implies that drift estimates should be calibrated toward recent, polarized-era elections rather than pooling polls back to 1948 equally, because polls are much less swingy now.

> their estimates of polling movement are derived from polls since 1948 — but polls now are much less “swingy” than they once were

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#10</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**critique of other approach** · 538 2024 (Morris) · explicit

The 95 percent interval on 538's national fundamentals-only forecast spans roughly Trump +20 to Biden +30. Silver calls these results nearly impossible in today's polarized environment.

*Numbers:* 538 fundamentals 95% range = Trump +20 to Biden +30 percentage points (national, July 2024)

> covers everything from roughly Trump +20 to Biden +30 (!), results that are nearly impossible in today’s highly polarized political environment

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#17</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**parameter or number** · 2024 presidential vs 538 2024 · explicit

In July 2024, 538 gave Biden a 14 percent chance of winning the national popular vote by double digits. The Silver Bulletin model gave 1.4 percent.

*Numbers:* 538 P(Biden wins popular vote by 10+) = 14 % (July 2024); Silver Bulletin P(Biden wins popular vote by 10+) = 1.4 % (July 2024)

> they say that Biden has a 14 percent chance of winning the national popular vote by double digits. Our model says the chances of that are just 1.4 percent

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#18</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**critique of other approach** · 538 2024 (Morris) · explicit

538's 95th percentile forecast range in Pennsylvania ran from roughly Biden +18 to Trump +17, which Silver says is almost certainly too wide. 538's Pennsylvania median was D+0.6.

*Numbers:* 538 PA 95% range = Biden +18 to Trump +17 percentage points (July 2024)

> 538’s 95th percentile forecast covers outcomes ranging from roughly Biden +18 to Trump +17

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#19</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**limitation or failure mode** · 538 2024 (Morris) · explicit

538's published component chart may hide steps. It shows a forecast of the Nov. 5 polling average, not the actual result, so Election Day poll error may be added separately.

> their chart only shows what they forecast the polling average to be on Nov. 5, not the actual result

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#28</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**method** · 2024 presidential (Harris version) · explicit

Silver expects higher overall forecast uncertainty in the Harris-Trump model. He says this arises organically from factors the model already considers, such as there being far fewer Harris-Trump polls than Biden-Trump polls, not from any ad hoc added uncertainty.

*Why:* A smaller poll sample means more uncertainty, which makes the tipping-point state harder to pinpoint.

> It emerges organically from the factors that the model already considers, like that we have far fewer Harris-Trump polls so far than Biden-Trump polls.

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#15</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**method** · 2024 presidential · inferred_from_chart

The 2024 model reports 80% intervals (10th to 90th percentiles) on the forecasted margin in each state.

*Numbers:* interval coverage = 80% percent (10th-90th percentile state margins)

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#25</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

The model's uncertainty index has nine factors. It mainly governs how much the model expects the polls to change before Election Day, and to a lesser extent how accurate it expects the polls to be on Election Day.

*Numbers:* uncertainty index factors = 9 factors (2024 presidential model)

> one of the nine factors used in the model's uncertainty index — which governs how much the model expects the polls to change before Election Day

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#15</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

Uncertainty index factor 7 is the volume of polling: more data means less sampling error and less uncertainty. It is computed from recent polling only, not from all polling throughout the year.

*Why:* Recent volume is usually highly correlated with overall volume.

> this calculation is based only on how much recent polling there is, not how much polling there has been throughout the year

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#16</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

Uncertainty index factor 1 is the number of undecided voters. It was about unchanged after the candidate swap.

> Factor 1 is the number of undecided voters.

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#18</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

Uncertainty index factor 2 is the number of undecided plus third-party voters. It fell slightly, meaning less uncertainty, as RFK Jr. declined after Harris's entry.

> Factor 2 is the number of undecided plus third party voters. This is now slightly lower

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#19</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

Uncertainty index factor 3 is political polarization: more polarization means a more stable race and less uncertainty. It is set at the start of the year from Congressional voting patterns and does not depend on the candidates.

> Factor 3 is political polarization — more polarization means a more stable race, and therefore less uncertainty. This factor is set at the start of the year based on Congressional voting patterns

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#20</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

Uncertainty index factor 4 is the variation in national polling so far. It was very low for the steady Trump-Biden race and is now higher because Harris-Trump polls have bounced around.

> Factor 4 is the amount of variation in national polling — that is, how much the polls have swung around so far.

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#21</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**data source** · 2024 presidential · explicit

Uncertainty index factor 6 is news-event uncertainty, measured by the number of New York Times full-width banner headlines. It was higher after the recent run of major political news.

> Factor 6 is uncertainty based on news events, as determined from the number of New York Times full-width banner headlines.

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#23</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

Uncertainty index factor 8 is the gap between polls and fundamentals. It is now quite low because both project a roughly tied national popular vote; under Biden it was larger because he underperformed the fundamentals.

> Factor 8 is the gap between polls and fundamentals. This is now quite low

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#24</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**model change** · 2024 presidential · explicit

Uncertainty index factor 9, new in 2024, is the number of repeat candidates who ran in the previous election. More repeat candidates means less volatility; with only Trump repeating, uncertainty from this factor is higher than under Biden-Trump.

*Numbers:* repeat candidates = 1 (was 2) candidates (Harris-Trump vs Biden-Trump)

*Why:* Repeat candidates are closer to known commodities.

> Factor 9 — newly added this year — is the number of repeat candidates. Races with incumbents or challengers who also ran in the previous election tend to be less volatile

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#25</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**interpretation guidance** · 2024 presidential · explicit

After the swap, four uncertainty factors pointed toward more uncertainty, two toward less, and three were unchanged, so the forecast's error bars widened somewhat. The index is still somewhat below average by historical standards, and a double-digit win for either candidate is highly unlikely.

*Numbers:* factors up = 4 factors; factors down = 2 factors; factors unchanged = 3 factors

*Why:* The environment remains highly polarized, with stable polling.

> The uncertainty index is higher than before, but still somewhat below-average by historical standards.

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#26</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**interpretation guidance** · 2024 presidential · explicit

Conditional probabilities for very unlikely state outcomes (e.g., Trump wins California in 143 of 40,000 simulations, about 0.4%, and wins the EC in 123 of those, 86.0%) should be read cautiously. They rest on small simulation samples. More importantly, by Bayesian reasoning they mix two routes: a national landslide and a state-specific freak shock. The model treats the freak-shock route as only about 6 times less likely than the landslide route.

*Numbers:* Trump CA wins = 143 simulations (out of 40,000, Aug 8, 2024); Trump P(EC | CA) = 86.0 percent (Aug 8, 2024); freak vs landslide odds ratio = 6:1 ratio (freak accident less likely than landslide)

> The freak accident scenario is more unlikely, but by "only" by about a 6:1 ratio, the model thinks.

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#9</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**limitation or failure mode** · 2024 presidential · explicit

The authors say the model probably overstates outlier outcomes. One reason is that fat-tailed state-specific errors can produce six-sigma results. Another is that noncompetitive states are rarely polled, and the model is very uncertain about states with little or no polling.

*Numbers:* tail outcome size = six sigma standard deviations (state-specific error)

> our model is probably too generous about accounting for these outlier occurrences, i.e. it overstates their likelihood.

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#10</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**method** · 2024 presidential · explicit

Simulated errors in the Silver Bulletin model, including state-specific error, are drawn from a t-distribution, which is fat-tailed.

*Why:* There are few elections with reliable polling (national polls since about 1936, material swing-state polling since about 1976), so the long-run error distribution is uncertain and catastrophic polling errors are possible.

> the reason we use fat-tailed distributions at all — specifically, a t-distribution — is because we don't actually have have all that many elections with reliable polling data

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#11</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**method** · 2024 presidential · explicit

The Silver Bulletin presidential model's uncertainty index includes a component related to the presence of an N3PC. Removing the N3PC lowers that component and so reduces overall forecast uncertainty, which benefits the leading candidate.

> removing the N3PC reduces the value of one of the components of the model's uncertainty index

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#21</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**model change** · 538 2020 presidential · explicit

As a COVID provision, the 2020 FiveThirtyEight presidential model widened the forecast's error bars because turnout was expected to be harder to predict in a pandemic. Silver says he feels OK about this, since the 2020 polls were quite far off.

*Why:* Turnout would potentially be harder to predict in a pandemic.

> widening the error bars in the forecast, given that turnout would potentially be harder to predict in a pandemic

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#1</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**assumption** · 2024 presidential · explicit

The Silver Bulletin presidential model assumes that by Election Day polls will not be predictably biased. Polls are expected to be centered on the truth over the long run but imprecise in any given election: high accuracy, low precision.

*Why:* There is no historical autocorrelation in bias, pollsters have incentives to self-correct, n=2 is too small a sample, and conventional wisdom often guesses the direction wrong.

> The model assumes that, by Election Day, polls won't be predictably biased.

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#11</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**empirical regularity** · general principle · explicit

A polling error of a few points in any direction is normal. Years like 2008, when polls nailed the outcome with great precision, are the unusual ones.

*Numbers:* typical polling error = a few points (any given election)

> A polling error of a few points is normal, in fact — it’s years like 2008 when polls nail the outcome with incredible precision that are unusual.

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#12</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**data source** · 2024 presidential · explicit

The Silver Bulletin model's estimate of Election Day polling error is based on an analysis of all election cycles since 1936. This deliberately includes early, rough-polling eras, such as before landline telephone penetration reached 75% in the mid-1950s, so the model learns from examples of large misses (fat tails).

*Numbers:* start year of polling error training data = 1936 year (Election Day polling error estimation); landline telephone penetration = 75 percent (reached by the mid-1950s)

*Why:* Including eras when polls were far off the mark captures the chance of misses larger than a few points.

> Our estimate of Election Day polling error is based on an analysis of all election cycles since 1936.

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#13</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**design principle** · 2024 presidential · explicit

Silver would build predictable polling bias into the model if he believed it existed. He does not adjust for Trump's 2016 and 2020 overperformance, so a final Harris +3 should not be shaded to Harris +2.

> if I thought polling was predictably biased, I’d have built that into the model somehow

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#27</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**empirical regularity** · general principle · explicit

Historically there has been no relationship in polling bias from one election to the next. For example, polls were biased against Democrats in 2012 and toward them in 2014 and 2016.

> there’s historically been no relationship in polling error from one election to the next

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#28</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**empirical regularity** · 538 pollster ratings data, 1998-2022 · inferred_from_chart

538's table of weighted-average statistical bias of polls in the final 21 days before elections since 1998 shows Presidential bias of R+2.4 (2000), D+1.2 (2004), D+0.9 (2008), R+2.5 (2012), D+3.3 (2016) and D+4.1 (2020), averaging D+1.2. Combined bias across races includes D+4.x in 2019-20 and near zero in 2017-18 and 2021-22. (D+ means polls overstated Democrats.)

*Numbers:* presidential bias 2019-20 = D+4.1 points (final 21 days); presidential bias 2015-16 = D+3.3 points; presidential bias 2011-12 = R+2.5 points; presidential bias 2007-08 = D+0.9 points; presidential bias 2003-04 = D+1.2 points; presidential bias 1999-2000 = R+2.4 points; presidential bias all years = D+1.2 points (1998-2022); Senate bias all years = D+0.6 points; House bias all years = D+1.2 points; Governor bias all years = D+0.9 points; Senate bias 2019-20 = D+4.9 points; House bias 2019-20 = D+6.1 points; Governor bias 2019-20 = D+5.6 points; Senate/House/Gov bias 2021-22 = R+0.3 / D+0.2 / D+1.3 points; Senate/House/Gov bias 2017-18 = EVEN / R+0.5 / R+1.0 points; Senate/House/Gov bias 2011-12 = R+3.2 / R+3.3 / R+1.6 points

*Why:* Shows bias direction is unpredictable from cycle to cycle.

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#29</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**assumption** · general principle · explicit

Pollsters have strong incentives to self-correct after misses like 2016 and 2020. Silver likens this to the efficient markets hypothesis: the bias is hard to outguess.

> pollsters have strong incentives to self-correct and get the answer right

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#31</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**interpretation guidance** · general principle · explicit

Trump's overperformance of polls in 2016 and 2020 is a sample of n=2. Polls were biased toward Republicans in 2012 and basically unbiased in the 2018 and 2022 midterms.

*Numbers:* sample size = 2 elections (Trump overperformance)

> people are probably making too much out of a sample size of n=2

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#32</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**empirical regularity** · general principle · explicit

Conventional wisdom often guesses the direction of polling bias wrong. In 2022 the expected 'red wave' was not justified by the polls; 2022 was among the most accurate polling years on record, though Democrats slightly overperformed polling averages in key Senate races.

> conventional wisdom often guesses wrong about the direction the bias will run

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#33</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**interpretation guidance** · 2024 presidential · explicit

Silver's own judgment is that polls are about equally likely to miss in either direction, with only the slightest lean toward Trump overachieving. The lean is not enough to bet at -110 odds.

*Numbers:* bet odds = -110 American odds (would not bet either way)

> I have just the slightest lean in that direction. But if DraftKings offered such a bet at -110

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#37</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**parameter or number** · 2024 presidential · explicit

In the Silver Bulletin 2024 model as of early September, the chance of a landslide, defined as either candidate winning the popular vote by 10 or more points, was about 5%.

*Numbers:* landslide probability (popular vote margin >=10 for either candidate) = about 5 percent (forecast as of ~Sept 1, 2024)

> the chance of a landslide — either Harris or Trump winning the popular vote by 10 points or more — is only about 5 percent in our model.

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#2</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**method** · 2024 presidential · explicit

Forecast uncertainty shrinks as Election Day approaches, so a constant small Electoral College lead translates into a rising win probability. Uncertainty never reaches zero because of the risk of systematic polling error, as in 2016 and 2020.

> as we get closer to the election, the uncertainty in the forecast decreases. Not to zero by any means: there could be another systematic polling error.

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#13</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**limitation or failure mode** · general principle · explicit

Partisan non-response bias can produce temporary 'sugar highs' in polls. Enthusiastic partisans, such as Democrats after the Harris candidate swap, are considerably more likely to respond to surveys. Polls may therefore become more accurate when both parties are equally enthused.

*Why:* Explains post-honeymoon reversion in Harris's state numbers.

> sometimes enthusiasm translates into unsustainable sugar highs in polls because enthusiastic voters are considerably more likely to respond to surveys.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#9</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**empirical regularity** · 2024 presidential · explicit

Pennsylvania, Michigan and especially Wisconsin had significant polling errors in 2016 and 2020. Silver suggests that 2024 polls showing a much smaller GOP lean in Wisconsin than its past results are a possible red flag.

> polls show a considerably smaller GOP lean in Wisconsin than in 2016 and 2020, a possible concern for Harris given the history of polling errors there.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#19</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**parameter or number** · 2024 presidential · explicit

Even in Trump landslide scenarios, the 2024 Silver Bulletin model gives Trump only small chances in deep-blue states: 0.2 percent in California, 0.6 percent in New York and 0.3 percent in Massachusetts.

*Numbers:* Trump win probability, California = 0.2 percent (Sept. 17, 2024 model); Trump win probability, New York = 0.6 percent (Sept. 17, 2024 model); Trump win probability, Massachusetts = 0.3 percent (Sept. 17, 2024 model)

> states like California (an 0.2 percent chance of a Trump win), New York (0.6) and Massachusetts (0.3) should be Safe Democrat.

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#7</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**design principle** · 2024 presidential · explicit

Silver says the 2024 Silver Bulletin model is 'pretty tolerant of outlier outcomes,' meaning it uses fat-tailed uncertainty. As a result, the small probabilities it assigns to upsets in safe states may be generous.

> those percentages might be generous given how the model is pretty tolerant of outlier outcomes.

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#8</sub>

### 2024-09-19 · [Don't let randomness make a fool of you](https://www.natesilver.net/p/dont-let-randomness-make-a-fool-of)
**parameter or number** · general principle · explicit

A typical state poll has about 800 respondents. Its theoretical margin of error is about ±3.5 points on one candidate's vote share.

*Numbers:* typical poll sample size = about 800 respondents (typical poll, e.g. Wisconsin 2024); margin of error, single candidate share = ±3.5 percentage points (800-person poll, 95% confidence)

> A typical poll has about 800 respondents. Well, the margin of error in an 800-person poll is plus or minus 3.5 points.

<sub>2024-09-19_dont-let-randomness-make-a-fool-of-you-by-nate-silver#3</sub>

### 2024-09-19 · [Don't let randomness make a fool of you](https://www.natesilver.net/p/dont-let-randomness-make-a-fool-of)
**empirical regularity** · general principle · explicit

In a two-way race with negligible third-party vote, the margin of error on the gap between the candidates is roughly twice the margin of error on one candidate's share. For an 800-person poll this is about ±7 points.

*Numbers:* margin of error on the margin = about 7 percentage points (800-person poll, two-candidate race); multiplier = roughly 2 x (margin-of-error on the gap vs. on one candidate's share)

*Why:* Nearly every vote that is not a Harris vote is a Trump vote, so errors in the two shares are perfectly negatively correlated.

> So the margin of error on the difference separating the candidates is roughly twice that: about 7 points.

<sub>2024-09-19_dont-let-randomness-make-a-fool-of-you-by-nate-silver#4</sub>

### 2024-09-19 · [Don't let randomness make a fool of you](https://www.natesilver.net/p/dont-let-randomness-make-a-fool-of)
**empirical regularity** · general principle · explicit

With a true margin of Harris +1, sampling error alone will produce some polls ranging from Trump +5 to Harris +7. About 1 poll in 20 will be an outlier beyond the 95% interval, such as Harris +10 or Trump +8.

*Numbers:* margin-of-error coverage = 95 percent (share of polls expected inside the stated margin of error); outlier frequency = 1 in 20 polls (polls outside the margin of error if pollsters are honest)

> about 1 time in 20, you'll get a true outlier — a Harris +10 or a Trump +8 — provided that pollsters are being honest

<sub>2024-09-19_dont-let-randomness-make-a-fool-of-you-by-nate-silver#5</sub>

### 2024-09-19 · [Don't let randomness make a fool of you](https://www.natesilver.net/p/dont-let-randomness-make-a-fool-of)
**design principle** · 2024 presidential · explicit

The Silver Bulletin model's more important function is to account for systematic polling error that affects polls collectively. An example is the error that substantially underestimated Trump in both 2016 and 2020.

*Why:* Sampling error understates real-world uncertainty.

> their more important function is by accounting for another possibility: the chance of a systematic polling error

<sub>2024-09-19_dont-let-randomness-make-a-fool-of-you-by-nate-silver#9</sub>

### 2024-09-19 · [Don't let randomness make a fool of you](https://www.natesilver.net/p/dont-let-randomness-make-a-fool-of)
**method** · 2024 presidential · explicit

The Silver Bulletin model calibrates its win probabilities to the historical empirical accuracy of polls, not to theoretical sampling margins of error. Empirical error is considerably wider than theoretical error.

*Why:* Real-world margins of error are considerably wider than theoretical ones.

> they're derived from how accurate the polls really have been, in practice — and in practice, the margins of error are considerably wider than they are in theory

<sub>2024-09-19_dont-let-randomness-make-a-fool-of-you-by-nate-silver#10</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**assumption** · 2024 presidential · explicit

In the 2024 presidential model, uncertainty includes both systematic polling error and real shifts in the race over the remaining campaign. As of September 21, 2024, the final six weeks of the campaign were still treated as a source of possible movement.

*Numbers:* time remaining = six weeks (as of Sept 21, 2024)

> A systematic polling error, or a shift in the race in the final six weeks of the campaign

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#2</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**design principle** · 2024 presidential · explicit

The model should enumerate even unlikely scenarios, such as weird regional shifts like those in 2022. One example is Harris losing the Blue Wall plus New Hampshire and Minnesota while sweeping Florida, Georgia and North Carolina. The simulation therefore must allow region-specific (non-uniform) error components.

*Why:* Elections like 2022 had a lot of weird regional shifts.

> there are sometimes elections like 2022 with a lot of weird regional shifts, and the model's job is to enumerate even the unlikely scenarios.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#12</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**limitation or failure mode** · 2024 presidential · explicit

Silver thinks the model is probably overly cautious in giving Iowa any tipping-point probability. Iowa is strongly correlated with the Blue Wall, so a Harris win in Iowa almost always comes with Blue Wall wins and a non-close electoral outcome.

*Why:* If Harris wins Iowa, she'll almost certainly also win the Blue Wall states.

> it's probably being overly cautious in thinking that Iowa could ever be the tipping point.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#14</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**design principle** · 2024 presidential · explicit

For lightly polled, safe-ish states (Minnesota, New Mexico, Virginia), the model assigns a 0 to 1 percent tipping-point probability out of an abundance of caution. Sparse polling leaves more uncertainty.

*Numbers:* MN/NM/VA tipping-point probability = 0 to 1 percent (Sept 21, 2024)

*Why:* There hasn't been a ton of polling in these states.

> where there hasn't been a ton of polling and the model assigns a 0 to 1 percent tipping-point probability out of an abundance of caution.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#15</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**interpretation guidance** · general principle · explicit

Individual poll swings (e.g., a NYT/Siena Harris +4 in Pennsylvania) are often just noise, because the margin of error on polls is higher than people intuitively think.

*Numbers:* NYT/Siena PA margin = 4 percentage points (Harris lead) (Sept 11-16, 2024)

> Some of this is probably just noise: the margin of error on polls is higher than you might think intuitively

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#20</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**limitation or failure mode** · general principle · explicit

Herding (file-drawering outliers, weighting toward priors, peeking at other polls) can make the average individual poll more accurate while making the polling average worse. In particular, averages may then miss genuine large demographic shifts. Silver describes this as a tragedy-of-the-commons problem.

*Why:* Herded polls do not add independent information.

> herding can make the average poll more accurate even as it makes the polling average worse

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#13</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**empirical regularity** · general principle · explicit

The margin of error on the gap between two candidates is roughly double the margin of error on one candidate's vote share. The Times polls of GA, AZ and NC had a combined MoE of 2.5 points on vote share, about 5 points on the margin. A Trump +3 average is therefore consistent with anything from Harris +2 to Trump +8.

*Numbers:* combined MoE on vote share = 2.5 percentage points (Times/Siena GA, AZ, NC polls combined); MoE on margin = ~5 percentage points (same polls); plausible range around Trump +3 = Harris +2 to Trump +8 margin (Sunbelt)

> the margin of error is closer to 5 points on the difference separating the candidates

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#14</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**empirical regularity** · general principle · explicit

One in 20 polls will fall outside its margin of error, which corresponds to a 95% confidence interval.

*Numbers:* share of polls outside MoE = 1 in 20 (sampling error)

> one in 20 polls will fall outside the margin of error

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#15</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**interpretation guidance** · general principle · explicit

Subgroup crosstabs carry huge sampling error. The Times Arizona poll's 149 Hispanic respondents imply about a 16-point margin of error on the Trump-Harris gap. Using crosstabs to debunk polls is therefore misguided, since every honest poll will show some odd subgroup results.

*Numbers:* Hispanic subsample = 149 respondents (Times/Siena Arizona poll); subgroup MoE on margin = 16 percentage points (same subsample)

*Why:* Only polls that over-massage their data avoid odd subgroup results.

> the Times poll of Arizona surveyed 149 Hispanic voters. That translates to a margin of error of 16 points

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#16</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**interpretation guidance** · general principle · explicit

Polling averages contain more noise than people assume, and a state's recent gains, such as Harris's post-debate gains in PA, may revert to the mean.

> there could be some reversion to the mean and there’s more noise in polling averages than people might assume

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#20</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**parameter or number** · 2024 presidential · explicit

Silver describes a 'normal-sized' polling error as 3 to 4 points across the board. An error that size in either direction would decide all seven swing states when all are polling within 2 points.

*Numbers:* normal-sized polling error = 3 or 4 percentage points (uniform error across swing states); swing state polling range = within 2 percentage points (all seven battlegrounds, Sept. 29, 2024)

> even a normal-sized polling error of 3 or 4 points across the board would make the Electoral College uninteresting.

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#3</sub>

### 2024-10-08 · [55/45 is a really close race](https://www.natesilver.net/p/5545-is-a-really-close-race)
**method** · 2024 presidential · inferred_from_chart

The Silver Bulletin 2024 popular-vote forecast chart displays 80% intervals for each candidate's vote share. On Oct 7, the band ran roughly ±2.5 points around each candidate's projection.

*Numbers:* interval coverage = 80 percent (popular vote chart); approx half-width = ~2.5 percentage points (read from chart, Oct 2024)

<sub>2024-10-08_5545-is-a-really-close-race-by-nate-silver#12</sub>

### 2024-10-08 · [55/45 is a really close race](https://www.natesilver.net/p/5545-is-a-really-close-race)
**limitation or failure mode** · 2024 presidential · explicit

Polls are not accurate enough to support much more than 50/50 to 60/40 confidence in a race this close. Unlike a sports final score, the final polling average before Election Day isn't always correct.

> polls simply aren't accurate enough to provide for much more confidence than that

<sub>2024-10-08_5545-is-a-really-close-race-by-nate-silver#13</sub>

### 2024-10-09 · [When you should panic about the polls](https://www.natesilver.net/p/when-you-should-panic-about-the-polls)
**interpretation guidance** · 2024 presidential · implied

In the Wisconsin example, a 0.4-point drop in Harris's lead lowered her state win probability by 3 points. This implies roughly 7-8 points of win probability per point of margin near a toss-up, about four weeks out.

*Numbers:* implied sensitivity = ~7.5 percentage points of win probability per point of margin (Wisconsin, 4 weeks out)

<sub>2024-10-09_when-you-should-panic-about-the-polls-by-nate-silver#10</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**interpretation guidance** · 2024 presidential · explicit

Even a small systematic polling error in Trump's favor, like in 2016, could produce a Trump sweep of every swing state. Silver says this illustrates the strong correlation between swing states.

> With even a small systematic polling error in his favor, like in 2016, Trump could sweep every swing state

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#13</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**empirical regularity** · 538 2020 · explicit

In 2020, the final state polling averages (FiveThirtyEight) were mostly accurate in deep-blue states. They considerably underestimated Trump in purple states and massively underestimated him in red states. Errors exceeded 10 points in some states.

*Numbers:* Montana error = 12 points toward Trump (2020); Utah error = 10 points toward Trump (2020); Wisconsin error = 7.8 points (D+8.4 polled vs D+0.6 result); Michigan error = 5.1 points (D+7.9 vs D+2.8); ME-2 error = 10.2 points (D+2.8 vs R+7.4); New York error = 6.3 points (D+29.4 vs D+23.1); New Jersey error = 4.5 points (D+20.4 vs D+15.9); Maine error = 3.9 points (D+13 vs D+9.1); New Hampshire error = 3.7 points (D+11.1 vs D+7.4); Pennsylvania = D+4.7 polled vs D+1.2 result margin (2020); Maryland = D+31.4 polled vs D+33.2 result margin (2020; overestimated Trump); NE-2 = D+3.8 polled vs D+6.5 result margin (2020)

> Mostly, the polls were pretty accurate in deep blue states. But they considerably underestimated Trump in purple states

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#5</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**assumption** · general / 2020 · explicit

Silver offers a possible explanation for the 2020 polling error: COVID-related differential nonresponse. Democrats were more likely to socially distance and so had more time to answer surveys. He argues the skew would be larger in red states with voluntary distancing than in locked-down blue states, which fits the asymmetric error pattern.

*Why:* In uniformly locked-down states everyone changed behavior, while in red states progressives selectively stayed home.

> Voters who were socially distancing had more time on their hands to respond to surveys, and Democrats were more likely to socially distance than Republicans.

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#6</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**empirical regularity** · 2020 · explicit

Polls early in the 2020 cycle (February–March, before COVID) were more accurate than the final 2020 polls.

*Why:* Supports the COVID nonresponse hypothesis.

> polls early in 2020 cycle — in February and March before COVID greatly disrupted people's daily lives — were more accurate than the final numbers

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#7</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**assumption** · 2024 analysis · explicit

Silver raises the possibility that 2024 polls understate polarization: underestimating Harris in blue states and Trump in red states. Mechanisms would be undecideds breaking toward each state's dominant party, or depressed minority-party turnout in lopsided states. He notes there are few undecideds.

*Why:* For example, there is little reason for a Republican in Massachusetts to vote.

> undecided voters in blue states will mostly wind up voting for Harris and red-state undecideds for Trump (though there aren't many undecideds)

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#8</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**limitation or failure mode** · general principle · explicit

Partisan non-response bias can create artificial momentum: voters may be more likely to respond to polls when their candidate is getting favorable news coverage.

> voters may be more likely to respond to polls when their candidate is getting favorable news coverage

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#15</sub>

### 2024-10-22 · [Likability isn't enough](https://www.natesilver.net/p/likability-isnt-enough)
**empirical regularity** · 2016 retrospective · explicit

In 2016, Clinton underperformed her polls, but the errors were mostly at the state level. National polls were quite accurate.

> Clinton underperformed her polls in 2016 — but the errors were mostly at the state level. National polls were quite accurate.

<sub>2024-10-22_likability-isnt-enough-by-nate-silver-silver-bulletin#6</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**parameter or number** · 2024 presidential · explicit

Silver states that polls are typically off by around 3 points in one direction or the other. He treats this as a 'normal-sized' polling error.

*Numbers:* typical polling error = around 3 points (typical polling miss in presidential elections)

> polls are typically off by around 3 points in one direction or the other

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#0</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**assumption** · 2024 presidential · explicit

The baseline assumption of the Silver Bulletin model is that the polls will probably be wrong to some degree, but the direction of the error is extremely hard to predict. The model therefore does not build in a directional bias correction for Trump's past overperformance.

*Why:* Empirically there is basically no correlation in polling error from one cycle to the next.

> the baseline assumption of the Silver Bulletin model is that while the polls could be wrong again — and in fact, they probably will be wrong to some degree — it's extremely hard to predict the direction of the error.

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#7</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**empirical regularity** · general principle · explicit

Empirically, there is basically no correlation in the direction of polling error from one election cycle to the next.

> Empirically, there's basically no correlation in polling error from one cycle to the next one.

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#8</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**interpretation guidance** · 2024 presidential · explicit

Forecasters should assume a pro-Trump polling error is roughly as likely as a pro-Harris one, i.e., the error distribution is centered on zero.

*Why:* Pollsters changing their methods, possible overcompensation, and possible herding cut in different directions.

> you should probably assume that a pro-Trump polling error is roughly as likely as a pro-Harris one.

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#9</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**limitation or failure mode** · general principle · explicit

Pollsters may overcompensate for past misses on Trump, consciously or unconsciously making assumptions that favor him. The 2017 UK election is an example: pollsters adjusted for 'shy Tories' and Labour beat its polls instead.

*Why:* Polls are increasingly like mini-models with many subjective decision points.

> If pollsters are terrified of missing low on Mr. Trump again, they may consciously or unconsciously make assumptions that favor him.

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#13</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**assumption** · general principle · explicit

One possible cause of the 2020 polling error was COVID: Democrats were more likely to socially distance and had more time to respond to polls. If that was the main cause, the bias may not recur, and corrections for it could overcompensate.

> if the 2020 polling error was primarily caused by COVID: Democrats being more likely to "socially distance" and having more time to respond to polls

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#14</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**assumption** · 2024 presidential · explicit

Silver speculates that if pollsters had published unadjusted, unherded numbers, the results might be a hair more favorable to Harris than the public record, which has been influenced by recent Trumpy vibes. He explicitly does not try to predict the direction of polling bias.

> it would be a hair more favorable to Harris than the numbers we're seeing in the public record

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#16</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**limitation or failure mode** · general principle · explicit

LV screens involve subjective pollster decisions. They are one source of uncertainty that makes a polling error in either direction highly plausible, possibly including aggressive swing-state screens or herding toward a toss-up.

> They're one of the factors that makes the polling situation uncertain and a polling error in either direction highly plausible.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#14</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**interpretation guidance** · general principle · explicit

As a benchmark for polling error, pollsters are criticized when off by 3 points, and larger misses are considered disasters. A 14-point miss, like the average early-vote misprediction, would be unacceptable for a poll.

*Numbers:* criticized poll error threshold = 3 points (pollster accuracy norms)

> Pollsters get yelled at when their polls are off by even 3 points, and anything more than that is considered an absolute disaster.

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#4</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**method** · general principle · explicit

The theoretical sampling margin of error on the two-candidate margin is roughly double the reported single-candidate margin of error, because nearly every vote not cast for one candidate goes to the other. In an 800-person poll of a 49-49 race with 2% third party, each candidate's MoE is about ±3 and the margin's MoE is ±6.

*Numbers:* single-candidate MoE = about ±3 percentage points (n=800); MoE on margin = ±6 percentage points (n=800, 49-49 race, 2% third party); third-party share assumed = 2 percent (retained in the calculation)

*Why:* If Trump gets 52 instead of 49, Harris gets 46.

> the margin of error that’s usually reported in polls is only for one candidate’s vote share

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#7</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**limitation or failure mode** · 2024 presidential · explicit

Herding and hedging raise the risk of a systematic polling error. The error could favor Trump again, could favor Harris (pollsters afraid to show Harris leads after two cycles of underestimating Trump), or could run in both directions across states (a scrambled map).

> All of this herding — and hedging — increases my concern about another systematic polling error.

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#17</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**method** · general principle · explicit

The margin of error on the lead (the difference between candidates) in a poll is roughly double the reported per-candidate margin of error. For an 808-likely-voter poll, the 95% margin of error on the margin is ±6.6 points.

*Numbers:* Sample size = 808 likely voters (Selzer Iowa poll); Margin of error on the lead = ±6.6 percentage points (95% interval for an n=808 poll); 95% interval for Selzer poll = Trump +3.4 to Harris +9.6 percentage points (Selzer Iowa poll)

> the margin of error for the difference separating the candidates in a poll of that size is ±6.6 points.

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#3</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**limitation or failure mode** · general principle · explicit

Theoretical sampling margins of error understate true polling error. They do not capture non-sampling sources, especially nonresponse: the overwhelming majority of people pollsters try to contact never complete the survey.

*Why:* Nonresponse bias adds error beyond sampling error.

> The theory, however, doesn't capture all possible sources of polling error — especially the fact that the overwhelming majority of people who pollsters attempt to contact never complete the survey.

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#4</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**empirical regularity** · 2024 presidential · explicit

The 2024 Silver Bulletin model projected Harris to win New Mexico by about 7 points on average, yet gave Trump an 11% chance there. The model is more uncertain about eccentric, sparsely polled states, and weak Harris polling in nearby Arizona and Nevada feeds into New Mexico through regional correlation.

*Numbers:* Harris projected NM margin = 7 percentage points (average); Trump NM win probability = 11 percent

*Why:* Little polling means wider uncertainty, and regional correlation transmits signal from neighboring states.

> it's also pretty uncertain about an eccentric state without much polling. And Harris's polling has been weak in nearby Arizona and Nevada, so it does have Trump winning it 11 percent of the time.

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#17</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**limitation or failure mode** · 2024 presidential · explicit

Silver lists anomalies in 2024 polling that raise his concern about a systematic polling error of unknown direction. Likely-voter models help Harris nationally but hurt her in swing states. Non-herding pollsters (Selzer, NYT/Siena) differ sharply from the rest. Large crosstab shifts among Black and Latino voters produce small topline swings. Swing-state polls are too tightly clustered. A favorability gap favors Harris but she does not consistently lead head-to-heads. National polls moved toward Trump more than battleground polls did.

*Why:* Herding may concentrate on head-to-heads, which pollsters tinker with more than favorability ratings.

> I've become increasingly concerned about the possibility of another systematic polling error — although I don't know whether it will favor Trump, favor Harris, or produce a map that's just really strange.

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#20</sub>

### 2024-11-04 · [The polls are close, but that doesn’t mean the results will be](https://www.natesilver.net/p/the-polls-are-close-but-that-doesnt)
**parameter or number** · 2024 presidential · explicit

The 2024 Silver Bulletin forecast of the national popular vote margin had a standard deviation of 3.1 points on the eve of the election. This value is mostly based on the historical accuracy of national polls in elections since 1936.

*Numbers:* Standard deviation of popular vote margin forecast = 3.1 percentage points (Nov 3, 2024); Start year of historical polling accuracy data = 1936 year (basis for the SD)

*Why:* The uncertainty is calibrated to the empirical history of national polling error.

> it has a standard deviation of 3.1 points. That number is mostly based on how accurate — or inaccurate — national polls have been in elections since 1936.

<sub>2024-11-03_the-polls-are-close-but-that-doesnt-mean-the-results-will-be#2</sub>

### 2024-11-04 · [The polls are close, but that doesn’t mean the results will be](https://www.natesilver.net/p/the-polls-are-close-but-that-doesnt)
**empirical regularity** · 2024 presidential · explicit

Because the race was so close, applying a uniform 3.1-point polling error flips every swing state to one side. A Trump-favoring error puts him ahead in all 7 by at least 2 points and wins him 312 EVs. A Harris-favoring error wins her all 7, with a smallest margin of 0.7 points in Arizona, and 319 EVs.

*Numbers:* Trump EVs with 3.1-pt R error = 312 electoral votes; Harris EVs with 3.1-pt D error = 319 electoral votes; Harris smallest swing-state margin = 0.7 percentage points (Arizona); PA polling average = Trump +0.3 percentage points (Nov 3, 2024); MI polling average = D +1.1 percentage points; WI polling average = D +0.9 percentage points

> A normal polling error of 3.1 points in his favor would put him ahead in all 7 by at least two points. He'd win 312 electoral votes.

<sub>2024-11-03_the-polls-are-close-but-that-doesnt-mean-the-results-will-be#9</sub>

### 2024-11-04 · [The polls are close, but that doesn’t mean the results will be](https://www.natesilver.net/p/the-polls-are-close-but-that-doesnt)
**design principle** · 2024 presidential · explicit

The direction of polling error is treated as essentially unpredictable in advance. Past errors (2016 and 2020 underestimating Trump) are not used to predict the direction of error in 2024.

*Why:* Two elections is a small sample, polls underestimated Obama in 2012, and pollsters have worked to correct their methods.

> past error really won't tell you much about how things will go this year. Two is a small sample size

<sub>2024-11-03_the-polls-are-close-but-that-doesnt-mean-the-results-will-be#10</sub>

### 2024-11-04 · [The polls are close, but that doesn’t mean the results will be](https://www.natesilver.net/p/the-polls-are-close-but-that-doesnt)
**empirical regularity** · 2024 presidential · inferred_from_chart

Applying past state-level polling errors (data from the New York Times) to the 2024 swing-state averages gives three different maps. Under 2020 errors, Trump leads by AZ +4.4, GA +2.3, MI +4.0, NV +3.4, NC +4.1, PA +4.4, WI +8.1. Under 2016 errors, the margins are AZ +3.4, GA +3.3, MI +2.0, NV -0.1, NC +7.1, PA +5.4, WI +4.1. Under 2012 errors, they are AZ +2.9, GA -0.7, MI -6.0, NV -3.6, NC +0.1, PA -0.6, WI -3.9. Positive values indicate a Republican advantage.

*Numbers:* WI under 2020 error = +8.1 points R; NV under 2016 error = -0.1 points (D lead); MI under 2012 error = -6.0 points (D lead)

<sub>2024-11-03_the-polls-are-close-but-that-doesnt-mean-the-results-will-be#11</sub>

### 2024-11-04 · [The polls are close, but that doesn’t mean the results will be](https://www.natesilver.net/p/the-polls-are-close-but-that-doesnt)
**limitation or failure mode** · general principle · explicit

Herding (pollsters publishing only results that match the consensus) may raise the risk of a systematic polling error.

> a systematic polling error is always possible, perhaps especially if you think pollsters are herding

<sub>2024-11-03_the-polls-are-close-but-that-doesnt-mean-the-results-will-be#12</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**design principle** · general principle · explicit

Silver says the model's uncertainty is not inflated by a default tendency to hedge or by adding extra uncertainty parameters without reason. He points to past cycles in which the model showed clear favorites.

*Why:* The model's record shows clear favorites in most years.

> It's not because my default is to hedge or just throw some extra uncertainty parameters in the model for no reason.

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#6</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**interpretation guidance** · 2024 presidential · explicit

Close polls do not necessarily predict a close result. A systematic polling error in either direction (favoring Trump or Harris) remains possible.

> the close polls don't necessarily predict a close result. How there could be another systematic polling error favoring either Trump or Harris

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#17</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**empirical regularity** · 2024 presidential · explicit

Silver says that, empirically, past polling has systematically underestimated Trump, and that Trump's voters are the harder ones to reach in polls.

> the answer in an empirical sense is obviously Trump.

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#24</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**method** · 2024 presidential · inferred_from_chart

The 2024 Silver Bulletin model reports a forecast margin for each contest with 10th-90th percentile intervals, so 80% of outcomes fall within the interval shown.

*Numbers:* interval = 10th-90th percentile (state margins)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#27</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**design principle** · general principle · explicit

Silver says the model's real value-add is not identifying who leads the polling average. It is quantifying how accurate polls are in practice and how polling errors are correlated across states.

> it’s in understanding the uncertainties in the data: how accurate polls are in practice, and how these errors are correlated between the states

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#8</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**empirical regularity** · 2024 presidential · explicit

Silver calls the 2024 polling miss a textbook normal-sized polling error. Final margins were quite close to the polling averages in the swing states but less close in blue states.

> this was more or less a textbook illustration of the normal-sized polling error that we frequently wrote about

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#10</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**design principle** · general principle (2020 onward) · explicit

Over the years Silver has tended, when making modeling decisions about confidence intervals, to err on the side of more uncertainty.

> I’ve generally tended over the years to make decisions rather than err more on the side of uncertainty when calculating confidence intervals.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#7</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**limitation or failure mode** · 2024 presidential · explicit

The 2024 model is probably too generous with uncertainty in 'weird' states such as Alaska and Hawaii. It gave Trump about a 3 percent chance in Hawaii when the true figure was more like 0.3 percent. Silver already toned this down in 2024 but may not have gone far enough.

*Numbers:* model's Trump win probability in Hawaii = 3 percent (2024 model); Silver's judged true probability = 0.3 percent (Trump winning Hawaii, 2024)

*Why:* Underconfidence isn't ideal either, after a phase of fearing overconfidence.

> I doubt that Trump actually had a 3 percent chance of winning Hawaii, for instance — maybe more like 0.3 percent.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#17</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**empirical regularity** · 2016-2024 · explicit

Most aggregators' polling averages had a statistical bias toward Democrats in 2016, 2020 and 2024. RCP's was smaller, and Republican-leaning indicators looked good in 2024.

> other aggregators’ polling averages had a statistical bias toward Democrats in 2016, 2020, and 2024, and RCP had less of one.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#26</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**empirical regularity** · 2024 presidential · explicit

In the 2024 presidential election, polls missed by about 2.5 points nationally and about 2 points in the average swing state. Silver Bulletin characterizes this as slightly below-average polling error.

*Numbers:* 2024 national polling error = about 2.5 percentage points (2024 presidential, national popular vote); 2024 average swing-state polling error = 2 percentage points (2024 presidential, average swing state)

> the polls missed by about 2.5 points nationally and 2 points in the average swing state.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#0</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**empirical regularity** · general principle · explicit

Polls underestimated Trump in three consecutive presidential cycles (2016, 2020, 2024), so systematic polling bias has run in the same direction repeatedly. The 2024 error was smaller than in 2016 and 2020.

*Numbers:* consecutive cycles underestimating Trump = 3 cycles (2016, 2020, 2024)

> They underestimated Trump for the third time in a row after pollsters spent the cycle trying to avoid that exact result.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#1</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**empirical regularity** · general principle; relevant to FLIPR 2026 · explicit

Midterm polls in 2018 and 2022 showed little overall partisan bias. The Republican-underestimation pattern has appeared mainly in elections with Trump on the ballot, so it is unclear whether it will carry over to the 2026 midterms.

*Why:* Jackson's hypothesis is that Trump draws out low-propensity voters who don't vote in midterms.

> The 2018 and 2022 polls performed well on this front, with little overall bias.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#2</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**interpretation guidance** · general principle · explicit

A 1-point lead in a poll should not be reported as a candidate 'leading', because that grossly overstates poll precision. Error much lower than 2024's level should not be expected. Blumenthal says being within about 1.5 points of the target is good performance given non-random samples.

*Numbers:* error Blumenthal considers good = a point-and-a-half percentage points (error relative to the true value, given non-random samples)

*Why:* Polls no longer acquire effectively random samples.

> Although headlines might tout a mere 1-point advantage in a poll as a candidate “leading,” that grossly overstates the precision of polls.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#3</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**limitation or failure mode** · general principle · explicit

AtlasIntel's CEO argues the smaller pro-Democratic bias in 2024 may reflect luck from a tighter race rather than methodological improvement. A forecaster should therefore not assume the systematic bias has been fixed.

> maybe that was actually more luck than a methodological improvement.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#4</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**empirical regularity** · general principle · explicit

Eligible polls in the 2024 Republican presidential primaries missed the final margin between the top two candidates by an average of 9.7 percentage points. This is consistent with the long-term average presidential primary poll error since 2000 of 9.3 points.

*Numbers:* 2024 presidential primary average absolute error = 9.7 percentage points (margin between the top two candidates); long-term primary poll average error since 2000 = 9.3 percentage points (presidential primaries)

> missed the final margin between the top two candidates by an average of 9.7 percentage points

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#4</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**empirical regularity** · general principle · explicit

2024 Republican primary polls had a pro-Trump bias, overestimating Trump's margin over Nikki Haley by an average of 4.4 points.

*Numbers:* pro-Trump bias = 4.4 percentage points (2024 GOP primaries, Trump vs. Haley margin)

> overestimating Trump's margin against Nikki Haley by an average of 4.4 points

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#5</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**parameter or number** · Silver Bulletin pollster ratings · inferred_from_chart

The weighted-average absolute polling error across all race types since 1998 is 5.9 points. By race type it is: presidential primary 9.1, presidential general 4.2, Senate 5.4, House 6.0, governor 5.4.

*Numbers:* all-years combined error = 5.9 points (1998-2024); pres primary = 9.1 points (all years); pres general = 4.2 points (all years); Senate = 5.4 points (all years); House = 6.0 points (all years); Governor = 5.4 points (all years)

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#7</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**empirical regularity** · Silver Bulletin pollster ratings · explicit

In the 2023-24 cycle, average absolute polling error was 4.5 points, the lowest of any cycle since 1998. By race type it was: presidential general 3.4 (second-lowest on record), Senate 4.1 (lowest on record), House 5.2, governor 5.4, presidential primary 9.8.

*Numbers:* combined 2023-24 = 4.5 points; pres general 2024 = 3.4 points; Senate 2024 = 4.1 points; House 2024 = 5.2 points; Governor 2024 = 5.4 points; pres primary 2024 = 9.8 points

> in 2023-2024, the average polling error was lower than in any cycle in our database at only 4.5 points

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#8</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**parameter or number** · Silver Bulletin pollster ratings · inferred_from_chart

Historical average error in presidential general election polls by cycle was: 2000 4.3, 2004 3.2, 2008 3.5, 2012 3.8, 2016 4.9, 2020 5.0, 2024 3.4. Combined error across all race types by cycle was: 1998 7.7, 2000 5.5, 2002 5.4, 2004 4.8, 2006 5.7, 2008 5.5, 2010 5.8, 2012 5.3, 2014 5.4, 2016 6.8, 2018 4.8, 2020 6.3, 2022 4.8, 2024 4.5.

*Numbers:* pres general 2016 = 4.9 points; pres general 2020 = 5.0 points; combined 2020 = 6.3 points; combined 2016 = 6.8 points

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#9</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**parameter or number** · Silver Bulletin pollster ratings · inferred_from_chart

House poll error by cycle was: 1998 7.1, 2000 4.4, 2002 5.6, 2004 5.9, 2006 6.5, 2008 5.9, 2010 6.9, 2012 5.5, 2014 6.8, 2016 5.8, 2018 4.8, 2020 6.4, 2022 4.0, 2024 5.2. Senate poll error by cycle was: 7.5, 6.0, 5.4, 5.3, 5.3, 4.9, 5.1, 4.7, 5.3, 5.0, 4.2, 5.8, 4.8, 4.1.

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#10</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**design principle** · general principle / Silver Bulletin 2024 presidential model · explicit

Because polls tend to err in the same direction, averaging does little to reduce systematic bias. Forecast models must therefore explicitly account for systematic (correlated) polling error. This is an advantage of probabilistic models over simple polling averages.

*Why:* Averaging doesn't help when almost all polls are off in the same direction.

> it's more important than ever to account for the possibility of a systematic polling error. Because probabilistic election models do this, that's one advantage they have over simple polling averages

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#14</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**method** · Silver Bulletin pollster ratings · explicit

Statistical bias is the signed average error, i.e. how far polls consistently underestimate one party. It is calculated only for races where the top two finishers were a Democrat and a Republican, so it is not computed for presidential primaries.

> statistical bias: the extent to which polls miss in the same direction and consistently underestimate Democrats or Republicans

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#16</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**empirical regularity** · general principle · explicit

Historically, the direction of polling bias has been unpredictable from cycle to cycle. For example, polls underestimated Democrats in 2012 and Republicans in 2014 and 2016.

*Numbers:* 2012 combined bias = R+2.8 points; 2014 combined bias = D+2.8 points

> Historically, the direction of bias has been unpredictable cycle-to-cycle.

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#17</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**empirical regularity** · general principle · explicit

Polls overestimated Democrats in three consecutive presidential elections. Combined bias was D+3.0 in 2016 (described as about 3 points), D+4.7 in 2020 and D+2.9 in 2024. Presidential-only bias was D+3.2 in 2016, D+4.1 in 2020 and D+2.9 in 2024.

*Numbers:* 2016 bias = 3 points D (combined); 2020 bias = D+4.7 points (combined); 2024 bias = D+2.9 points (combined); pres 2020 = D+4.1 points; pres 2016 = D+3.2 points

> In 2016, the polls had a 3-point average bias toward Democrats. In 2020, bias was D+4.7 points. And this year, it was a smaller but still substantial at D +2.9.

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#18</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**parameter or number** · general principle · inferred_from_chart

All-years average bias since 1998 is D+1.1 combined. By race type: president D+1.3, Senate D+0.7, House D+1.3, governor D+0.9. Midterm cycles show small bias: 2018 R+0.5 combined (Senate EVEN, House R+0.4, governor R+1.0) and 2022 D+0.8 combined (Senate R+0.3, House D+0.2, governor D+1.3).

*Numbers:* all-years combined bias = D+1.1 points; 2018 combined = R+0.5 points; 2022 combined = D+0.8 points

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#20</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**parameter or number** · general principle · inferred_from_chart

Combined bias by cycle was: 1998 R+3.8, 2000 R+1.8, 2002 D+2.7, 2004 D+1.4, 2006 R+0.1, 2008 D+0.8, 2010 D+0.3, 2012 R+2.8, 2014 D+2.8, 2016 D+3.0, 2018 R+0.5, 2020 D+4.7, 2022 D+0.8, 2024 D+2.9. Presidential bias by cycle was: 2000 R+2.4, 2004 D+1.1, 2008 D+0.8, 2012 R+2.5.

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#21</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**assumption** · general principle · explicit

The repeated Democratic bias may be Trump-specific, because bias was much lower in 2022 and slightly Republican in 2018 when Trump was not on the ballot. If so, 2026 and 2028 polls might not show the same bias. Pollsters Silver Bulletin spoke with were mixed on this.

> It could, for example, be a Trump-specific issue.

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#22</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**empirical regularity** · general principle · explicit

Historical call accuracy by the poll's margin: under 3 points 56.0%, 3-6 points 69.1%, 6-10 points 85.8%, 10-15 points 93.8%, 15-20 points 96.9%, 20 or more points 99.5%. This gives an empirical mapping from poll lead to win probability.

*Numbers:* <3 = 56.0 % (correct call); 3-6 = 69.1 %; 6-10 = 85.8 %; 10-15 = 93.8 %; 15-20 = 96.9 %; 20+ = 99.5 %

> Historically, polls showing leads of less than 3 points call only 56 percent of races correctly — not much better than a coin flip.

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#27</sub>

### 2025-03-22 · [How low is Trump's popularity floor?](https://www.natesilver.net/p/how-low-is-trumps-popularity-floor)
**method** · Silver Bulletin approval tracker, 2025 · inferred_from_chart

The Silver Bulletin approval tracker chart displays shaded uncertainty bands within which 90% of individual polls are projected to fall. The bands are a poll-dispersion interval, not just uncertainty about the average.

*Numbers:* poll coverage of shaded band = 90 percent (share of polls projected to fall within the shaded region of the approval tracker chart)

<sub>2025-03-22_how-low-is-trumps-popularity-floor-by-nate-silver#1</sub>

### 2025-05-06 · [We're tracking more data on Trump's popularity](https://www.natesilver.net/p/were-tracking-more-data-on-trumps)
**method** · Silver Bulletin approval dashboard 2025 · inferred_from_chart

The strong/weak approval chart displays shaded bands within which 90% of polls are projected to fall, so the average carries a poll-dispersion interval.

*Numbers:* poll interval coverage = 90 percent (shaded regions on the strong/weak approval chart)

<sub>2025-05-06_were-tracking-more-data-on-trumps-popularity#3</sub>

### 2025-05-06 · [We're tracking more data on Trump's popularity](https://www.natesilver.net/p/were-tracking-more-data-on-trumps)
**empirical regularity** · general principle / midterms · explicit

Midterm polling has not repeated the presidential-year pattern of underestimating Republicans. Polls were largely unbiased and quite accurate in 2018 and 2022.

> midterm elections haven't upheld the pattern of polling error from presidential years, with polling being largely unbiased and quite accurate in 2018 and 2022

<sub>2025-05-06_were-tracking-more-data-on-trumps-popularity#13</sub>

### 2025-06-02 · [SBSQ #21: Why young men don't like Democrats](https://www.natesilver.net/p/sbsq-21-why-young-men-dont-like-democrats)
**method** · Silver Bulletin election models (general) · explicit

Silver's election models use fat-tailed distributions rather than normal distributions for outcomes, so extreme outcomes are comparatively more likely than under a normal assumption.

*Why:* Empirically, the normal-distribution assumption may not always be valid.

> Empirically, this assumption may not always be valid: we actually use fat-tailed distributions in our election models, for instance.

<sub>2025-06-02_sbsq-21-why-young-men-dont-like-democrats#0</sub>

### 2025-06-02 · [SBSQ #21: Why young men don't like Democrats](https://www.natesilver.net/p/sbsq-21-why-young-men-dont-like-democrats)
**empirical regularity** · general principle · explicit

Polling error is much higher in primary elections than in general elections, especially in low-turnout primaries. A 9-point deficit a few weeks out would be nearly insurmountable in a general election but not in a primary.

*Numbers:* Mamdani deficit to Cuomo, final RCV round = 9 percentage points (Emerson College poll, NYC Democratic mayoral primary, ~3 weeks before June 24, 2025)

*Why:* Low-turnout primaries are harder to poll.

> But polling error is much higher in primary elections, especially low-turnout primaries, and RCV adds an additional element of uncertainty.

<sub>2025-06-02_sbsq-21-why-young-men-dont-like-democrats#9</sub>

### 2025-09-09 · [Is Susan Collins toast?](https://www.natesilver.net/p/is-susan-collins-toast)
**empirical regularity** · general · explicit

In 2020, polling suggested Sara Gideon would beat Collins, but Collins won by 8.6 points. The article attributes this to "Shy Susan voters", a large race-specific polling miss in Collins's favor.

*Numbers:* Collins 2020 margin = 8.6 percentage points (Maine Senate 2020)

> much of the polling suggested that their nominee Sara Gideon... was poised to do it. But there turned out to be a lot of Shy Susan voters.

<sub>2025-09-09_is-susan-collins-toast-by-eli-mckown-dawson#9</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**empirical regularity** · Silver Bulletin pollster ratings database · explicit

Historically, polls showing a 6-10 point margin pick the winner 86% of the time. The rate is 94% for a 10-15 point margin and 97% for a 15-20 point margin.

*Numbers:* call accuracy, 6-10 pt margin = 86 percent (historical); call accuracy, 10-15 pt margin = 94 percent (historical); call accuracy, 15-20 pt margin = 97 percent (historical)

> Polls that show a race with a 6-10 point margin have 86 percent call accuracy, historically.

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#12</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**parameter or number** · Silver Bulletin pollster ratings · explicit

Average polling error across all polls in the Silver Bulletin database since 1998 is 5.9 points. This figure is inflated by error-prone presidential primary polls. The 2025 cycle average error was 7.1 points across 40 polls.

*Numbers:* historical average error = 5.9 percentage points (all polls since 1998); 2025 average error = 7.1 percentage points (40 qualifying polls)

> the average error across all polls in our database since 1998 is only 5.9 points — and that figure is inflated by surveys of presidential primaries

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#13</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**parameter or number** · Silver Bulletin pollster ratings · inferred_from_chart

In 2025, the 38 gubernatorial polls had an average error of 7.0 points and an average bias of R+6.9. The historical gubernatorial averages are 5.4 points of error and D+0.9 bias.

*Numbers:* 2025 gubernatorial polls = 38 polls (2025); 2025 gubernatorial error = 7.0 percentage points (2025); historical gubernatorial error = 5.4 percentage points (since 1998); 2025 gubernatorial bias = R+6.9 percentage points (2025); historical gubernatorial bias = D+0.9 percentage points (since 1998)

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#14</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**parameter or number** · Silver Bulletin pollster ratings · explicit

In the 2025 New Jersey governor's race, 22 polls had an average error of 9.0 points and a bias of R+9.0. The state's historical averages are 3.7 points of error and D+0.7 bias, making 2025 the worst year for New Jersey gubernatorial polls since 2000.

*Numbers:* NJ polls = 22 polls (2025); NJ 2025 error = 9.0 percentage points (2025); NJ historical error = 3.7 percentage points (historical); NJ 2025 bias = R+9.0 percentage points (2025); NJ historical bias = D+0.7 percentage points (historical)

> an average 9-point error compared to only 3.7 points historically, making 2025 the worst year for New Jersey gubernatorial polls since the turn of the century

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#15</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**parameter or number** · Silver Bulletin pollster ratings · explicit

In the 2025 Virginia governor's race, 16 polls had an average error of 5.9 points and a bias of R+5.8. Since 2001, Virginia gubernatorial polls have averaged 4.4 points of error and D+0.8 bias.

*Numbers:* VA polls = 16 polls (2025); VA 2025 error = 5.9 percentage points (2025); VA historical error = 4.4 percentage points (since 2001); VA 2025 bias = R+5.8 percentage points (2025); VA historical bias = D+0.8 percentage points (historical)

> Since 2001, the average polling error in Virginia gubernatorial elections was 4.4 points, compared to 5.9 points in 2025.

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#16</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**parameter or number** · Silver Bulletin pollster ratings · explicit

The two qualifying 2025 special House election polls had an average error of 8.4 points and a bias of D+8.4. Historically, House polls average 6.0 points of error and D+1.3 bias. The text says these polls overestimated Democrats, which it attributes mostly to Democrats overperforming expectations in FL-06 and TN-07.

*Numbers:* House polls = 2 polls (2025); House 2025 error = 8.4 percentage points (2025); House historical error = 6.0 percentage points (historical); House 2025 bias = D+8.4 percentage points (2025); House historical bias = D+1.3 percentage points (historical)

> the two 2025 House polls we added to our database did overestimate Democrats by 8.4 points on average, but that mostly comes down to the blue team overperforming expectations in FL-06 and TN-07

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#17</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**empirical regularity** · general principle · explicit

The direction of polling bias has historically been unpredictable from cycle to cycle. The average bias since 1998 is only D+1.1, but 2025 polls had an average R+6.1 bias, meaning they overestimated Republicans.

*Numbers:* historical average bias = D+1.1 percentage points (since 1998); 2025 average bias = R+6.1 percentage points (2025 cycle)

> Directionally, bias has historically been unpredictable cycle-to-cycle: the average bias since 1998 is just D +1.1.

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#18</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**empirical regularity** · general principle · explicit

Average polling bias by cycle: 2016 D+3.0, 2018 R+0.5, 2020 D+4.7, 2022 D+0.8, 2024 D+2.9, 2025 R+6.1. D+ means the polls overestimated Democrats. Pro-Democratic bias has been concentrated in presidential cycles, while midterms have been near-unbiased.

*Numbers:* 2016 bias = D+3.0 percentage points (presidential cycle); 2018 bias = R+0.5 percentage points (midterm); 2020 bias = D+4.7 percentage points (presidential cycle); 2022 bias = D+0.8 percentage points (midterm); 2024 bias = D+2.9 percentage points (presidential cycle)

*Why:* Possibly partisan nonresponse among low-propensity voters, who turn out in presidential years.

> recently, Democratic polling bias has been mostly confined to presidential cycles

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#19</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**interpretation guidance** · general principle · explicit

Silver Bulletin considers average bias near zero (such as D+0.8 in 2022 and R+0.5 in 2018) to be about as good as polls can realistically achieve.

> those results are about as good as you realistically can get

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#20</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**parameter or number** · 2024 presidential · explicit

Average polling error in 2024 was lower than in any cycle since 1998, yet polls underestimated Trump and Republicans for the third straight presidential election.

> average polling error in 2024 was lower than in any cycle since 1998

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#21</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**limitation or failure mode** · FLIPR 2026 / general · explicit

There is a risk that pollsters overcompensate after underestimating Trump three times, so the substantial Republican bias seen in 2025 could continue into the 2026 midterms.

*Why:* Weighting choices have become a guessing game.

> If pollsters who are worried about underestimating Trump three times end up overcompensating, the substantial Republican bias from 2025 could continue into 2026.

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#26</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**method** · Silver Bulletin polling averages (2026) · explicit

The approval and generic ballot averages display shaded bands showing where 90 percent of new polls are projected to fall, based on historical analysis of such averages over several decades. The bands widen when there are fewer polls and when polls disagree more.

*Numbers:* band coverage = 90 percent of new polls (shaded error region on charts)

> The shaded areas indicate where we project 90 percent of new polls to fall

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#16</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**parameter or number** · Silver Bulletin 2026 generic ballot average · explicit

The correlation between the late-January generic ballot average and the eventual House popular vote in midterms since 1994 is 0.53.

*Numbers:* correlation = 0.53 (January generic ballot vs House popular vote, midterms 1994-2022)

> The correlation between the generic ballot at this point in the cycle (early January) and the eventual House popular vote is 0.53

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#7</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**parameter or number** · Silver Bulletin 2026 generic ballot average · explicit

The empirical 95% margin of error of the January generic ballot average against the House popular vote margin is 5.7 points. Applied to D+5.3, that gives a range from D+11.0 to R+0.4.

*Numbers:* margin of error (January) = 5.7 percentage points (95% interval, ~285 days out); current Dem lead = 5.3 percentage points (generic ballot Jan 22, 2026); interval upper = D+11.0 percentage points (95% range); interval lower = R+0.4 percentage points (95% range)

> the empirical margin of error on the January polling average, compared to the popular vote, is 5.7 points.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#8</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**empirical regularity** · general principle · explicit

By party label, the late-January generic ballot has overestimated Democrats' eventual House popular vote margin by 4.6 points on average in midterms since 1994. The averages by stage are D+3.2 in late January, D+1.6 on Election Day, and D−1.4 in the actual House vote.

*Numbers:* average overestimate of Democrats = 4.6 percentage points (Jan generic ballot vs House vote, 1994-2022); late-Jan avg Dem margin = +3.2 percentage points (table); Election Day avg Dem margin = +1.6 percentage points (table); House vote avg Dem margin = −1.4 percentage points (table)

> in midterms since 1994, the generic ballot at this stage of the race has overestimated Democrats’ eventual finish in the House popular vote by 4.6 points.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#12</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**assumption** · FLIPR 2026 · explicit

The FLIPR 2026 model will embed the longstanding Silver assumption that the direction of systematic polling bias is unpredictable from year to year, so the model does not adjust for an expected bias direction.

*Why:* Polls are often systematically biased (against Republicans in 2016, against Democrats in 2025), but predicting the direction in advance is usually futile.

> we’d stand by our longstanding proposition, which will be embedded in our election model, that polling bias tends to be unpredictable from year to year.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#14</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**empirical regularity** · general principle · explicit

The authors attribute the historical pro-Democratic bias of the January generic ballot to four factors. First, polls have tended to overrate Democrats recently. Second, Democrats were the in-party in 5 of the 8 midterms. Third, early polls use registered voters or adults, while midterm turnout is low. Fourth, the generic ballot and House vote diverge because of uncontested seats and top-two primaries such as California's.

*Numbers:* midterms with Dem in-party = 5 of 8 (1994-2022)

> What accounts for this historical bias? This answer isn’t quite so straightforward; it’s likely a combination of several factors.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#15</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**empirical regularity** · general principle · explicit

Recent Democratic underperformance relative to polls has been concentrated in presidential years with Trump on the ballot. Polling was basically unbiased in 2018 and 2022, and Democrats considerably overperformed their polls in the 2025 off-year elections.

> Polling was basically unbiased in 2018 and 2022, and Democrats considerably overperformed their polls in the off-year elections of 2025.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#16</sub>

### 2026-06-01 · [Should Democrats panic about Platner?](https://www.natesilver.net/p/should-democrats-panic-about-platner)
**empirical regularity** · Silver Bulletin polling database · explicit

Since 2014, in Maine races with two or more polls in the final three weeks, Republicans have beaten their polls by about 4 points on average. There was no consistent bias before 2014, though Collins outperformed her polls substantially in 2008 and underperformed them in 2002.

*Numbers:* average Republican overperformance of polls in Maine = about 4 points (races since 2014 with 2+ polls in final three weeks)

> Since 2014, in Maine races with two or more polls in the final three weeks, Republicans have beaten their polls by about 4 points on average.

<sub>2026-06-01_should-democrats-panic-about-platner-by-nate-silver#1</sub>

### 2026-06-01 · [Should Democrats panic about Platner?](https://www.natesilver.net/p/should-democrats-panic-about-platner)
**empirical regularity** · polling database · explicit

Collins beat Sara Gideon by 8.6 points in 2020 despite trailing in almost every poll, one of the largest polling errors in the Silver Bulletin/FiveThirtyEight database.

*Numbers:* Collins 2020 margin = 8.6 points (Maine Senate 2020)

> wound up beating Gideon by 8.6 points, making for one of the largest polling errors in our extensive polling database.

<sub>2026-06-01_should-democrats-panic-about-platner-by-nate-silver#2</sub>

### 2026-06-01 · [Should Democrats panic about Platner?](https://www.natesilver.net/p/should-democrats-panic-about-platner)
**empirical regularity** · 2020 analysis · explicit

Silver attributes the 2020 Maine miss partly to a general 2020 polling error that badly overestimated Democrats, possibly due to COVID-related behavior, and partly to late news (Collins voting against Amy Coney Barrett) that most polling predated.

> polls badly overestimated Democrats that year

<sub>2026-06-01_should-democrats-panic-about-platner-by-nate-silver#8</sub>

### 2026-08-11 · [Everything is breaking Democrats’ way. Is it enough to win the Senate?](https://www.natesilver.net/p/everything-is-breaking-democrats-way)
**method** · FLIPR 2026 · explicit

The Lite (polls-only) version of FLIPR carries considerably greater uncertainty than Classic and Deluxe. It can be more optimistic about expected seat gains yet give a lower win probability, because its error bars are much wider when only polls are used.

*Why:* Adding fundamentals reduces forecast error.

> if you’re only allowed to look at polls, the error bars are much wider.

<sub>2026-08-11_everything-is-breaking-democrats-way-is-it-enough-to-win-the-senate#4</sub>

### 2026-08-11 · [Everything is breaking Democrats’ way. Is it enough to win the Senate?](https://www.natesilver.net/p/everything-is-breaking-democrats-way)
**interpretation guidance** · 2022 evaluation · explicit

Silver judges that the 2022 race-level polls were largely accurate and unbiased, contrary to a narrative that polls underestimated Democrats; Democrats lost only 9 House seats and gained a Senate seat.

*Numbers:* 2022 Democratic House losses = 9 seats (2022 midterm)

> The polls were largely accurate and unbiased.

<sub>2026-08-11_everything-is-breaking-democrats-way-is-it-enough-to-win-the-senate#13</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**adjustment rule** · FLIPR 2026 · explicit

New in 2026: when simple and fancy fundamentals disagree, as for popular Republican Gov. Phil Scott in Vermont, FLIPR trusts fundamentals less, puts more weight on polls and expert ratings, and increases the race's uncertainty. When they agree, it increases the weight on fundamentals.

> In cases where “simple fundamentals” and “fancy fundamentals” are not aligned, the model trusts fundamentals less in general.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#22</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**interpretation guidance** · FLIPR 2026 · explicit

Illustration of FLIPR's uncertainty logic: a candidate leading by 3 points with a 5-point margin of error wins 88 percent of the time; if the margin of error doubles to 10 points, 72 percent.

*Numbers:* win prob, 3-pt lead, 5-pt MoE = 88 percent (illustration); win prob, 3-pt lead, 10-pt MoE = 72 percent (illustration)

> A candidate with a 3-point lead in a race where the margin of error is 5 points will win her race 88 percent of the time.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#33</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

Step 6: race-level uncertainty in FLIPR is higher when there is less polling, more undecided voters, more time until the election, and more disagreement between model subcomponents such as fundamentals versus polls. Primary polls often miss by double digits.

*Why:* The degree of uncertainty is itself predictable.

> There’s more time to go until the election;

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#34</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

FLIPR splits error into layers. National error shifts all races together, scaled by each unit's elasticity, and has two parts: 'drift', the change in the national environment before Election Day, which is smaller under high polarization and goes to zero by Election Day, and Election Day systematic polling error. Local error has a statewide draw shared by all races in a state (new in 2026) and a race-specific draw. Correlated demographic error uses CANTOR's variables to simulate over- or underperformance among subgroups such as Hispanics, Catholics or the Northeast, producing clustered regional errors like those of 2018 and 2022.

*Why:* Errors are more correlated across similar places.

> Finally, correlated demographic error is an intermediate layer that sits between these and is the most complex layer.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#35</sub>

### 2026-08-13 · [Prediction markets aren't magic](https://www.natesilver.net/p/prediction-markets-arent-magic)
**parameter or number** · Silver Bulletin polling database · explicit

Historically, presidential primary polls have an average error of 9 points on the margin between the top two finishers, which implies a 95 percent margin of error of about 22 points. Silver suspects down-ballot primaries, with lower turnout, have effective margins of error of 25 to 30 points.

*Numbers:* average presidential primary poll error = 9 points (margin) (historical); 95% margin of error, presidential primaries = 22 points (historical); suspected MoE, gubernatorial/Senate primaries = 25-30 points (Silver's estimate)

*Why:* Lower turnout makes primaries harder to poll.

> Historically, the average error of presidential primary polls is 9 points in predicting the margin between the top two finishers

<sub>2026-08-13_prediction-markets-arent-magic-by-nate-silver#3</sub>

### 2026-08-20 · [Are Democrats on a summer sugar high?](https://www.natesilver.net/p/are-democrats-on-a-summer-sugar-high)
**assumption** · FLIPR 2026 · explicit

FLIPR assumes correlated polling errors are fairly common, so one party may sweep most toss-ups as Trump did the 2024 swing states. It also assumes these systematic errors are unpredictable and symmetric, equally likely to favor either party over the long run. Silver calls this a big but deliberate assumption.

> It also assumes, however, that these errors are equally likely to benefit Republicans or Democrats.

<sub>2026-08-19_are-democrats-on-a-summer-sugar-high-by-nate-silver#0</sub>

### 2026-08-20 · [Are Democrats on a summer sugar high?](https://www.natesilver.net/p/are-democrats-on-a-summer-sugar-high)
**interpretation guidance** · general principle · explicit

Poll-error datasets spanning many polls but few cycles are effectively small samples, because errors are heavily correlated within a cycle; Ruffini's summer-bias data is closer to n=4 than n=hundreds.

*Numbers:* effective sample = 4 cycles (2018-2024 summer Senate polls)

> So in some ways, this is closer to n=4 than n=hundreds.

<sub>2026-08-19_are-democrats-on-a-summer-sugar-high-by-nate-silver#3</sub>

### 2026-08-20 · [Are Democrats on a summer sugar high?](https://www.natesilver.net/p/are-democrats-on-a-summer-sugar-high)
**empirical regularity** · empirical · explicit

Polls considerably overestimated Democrats in 2020 and 2024 but were accurate and unbiased by historical standards in the 2018 and 2022 midterms. The generic ballot has historically overstated Democrats early in cycles but also understated the opposition party, so long-term trends conflict.

*Numbers:* Ruffini summer Senate poll bias = about 5 points toward D (late August, 2018-2024)

> the polls were both quite accurate and quite unbiased by historical standards in the past two midterms, 2018 and 2022.

<sub>2026-08-19_are-democrats-on-a-summer-sugar-high-by-nate-silver#4</sub>

### 2026-08-25 · [Do I really buy that Texas could turn blue?](https://www.natesilver.net/p/do-i-really-buy-that-texas-could)
**empirical regularity** · Silver Bulletin polling database · explicit

In the Silver Bulletin polling database since 1998 (polls in the final three weeks), Texas Democrats have been about as likely to outperform their polling averages as to underperform them. Polls have had an average Democratic bias in recent cycles, but no worse in Texas than nationally, unlike Maine.

> they’ve been roughly as likely to outperform their polling averages as to underperform them.

<sub>2026-08-25_do-i-really-buy-that-texas-could-turn-blue#7</sub>

### 2026-09-03 · [Beware big swings in midterm forecasts](https://www.natesilver.net/p/beware-big-swings-in-midterm-forecasts)
**parameter or number** · Silver Bulletin generic ballot history · explicit

Since 2010 the average absolute error of the Labor Day generic ballot in predicting the national House popular vote is 3.5 points, falling to 2.1 points for the final generic ballot average. Because the 2.1-point Election Day error exceeds the 1.4-point drift, most remaining national uncertainty after Labor Day comes from polling error rather than opinion movement.

*Numbers:* Labor Day generic ballot error = 3.5 points (average absolute, since 2010); final generic ballot error = 2.1 points (average absolute, since 2010)

> In terms of the national picture, most of the remaining uncertainty in the forecast stems from polling error rather than further movement in public opinion.

<sub>2026-09-03_beware-big-swings-in-midterm-forecasts#1</sub>

### 2026-09-20 · [Expert ratings are ignoring signs of a blue wave](https://www.natesilver.net/p/expert-ratings-are-ignoring-signs)
**empirical regularity** · FLIPR 2026 · explicit

Polls showing very red states like Kansas or Nebraska as toss-ups warrant caution, because recent polling error has been concentrated in such states. Classic and Deluxe hedge toward fundamentals there, and de-biased expert ratings still hurt Democrats in Kansas, Nebraska and South Carolina.

> History says to be wary of states as red as Kansas polling as toss-ups; they’re where most of the polling error has been concentrated in recent years.

<sub>2026-09-20_expert-ratings-are-ignoring-signs-of-a-blue-wave#11</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**assumption** · FLIPR 2026 · explicit

FLIPR's core constraint is that the forecast is 'party-neutral'. Polling averages may be predictably biased, for example a red state's polls understating the Republican or a blue state's understating the Democrat, and fundamentals correct for that. But the direction of error in the blended forecast is assumed unpredictable; no party-specific assumption such as 'polls always underestimate Republicans' is built in, which Silver would call unskewing.

*Why:* Past directional biases are consistent with chance given small effective samples.

> we assume that the direction of the bias of our polling averages might be predictable, but the direction of the bias in our blended forecasts (polls + fundamentals + expert ratings) isn’t predictable.

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#0</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**method** · FLIPR 2026 · explicit

FLIPR simulates four layers of polling uncertainty: (1) a uniform national error across all races; (2) demographically or geographically correlated errors, e.g. Democrats beat polls among Hispanics but Republicans in the Midwest; (3) a statewide error shared by a state's Senate, governor and House races; (4) a single-race error. In presidential years most uncertainty sits in layer 1, while in midterms it is more evenly spread across the four.

*Why:* Midterm errors in 2018 and 2022 were largely unbiased overall but regionally significant.

> For the midterms, they’re more evenly distributed between the four layers.

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#1</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**parameter or number** · Silver Bulletin polling database · explicit

In Silver Bulletin's pollster database, a simple average of all polls in the final three weeks of the 2016, 2020 and 2024 general elections overestimated Democrats by 3.8 points. Midterm polls in 2018 and 2022 were almost completely unbiased in aggregate, and off-year and special election polls in the Trump years were biased toward Republicans by 1.3 points on average.

*Numbers:* Trump presidential years poll bias = 3.8 points toward D (2016, 2020, 2024 final 3 weeks); off-year/special election bias = 1.3 points toward R (Trump era)

> they overestimated Democrats by a margin of 3.8 percentage points.

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#2</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**empirical regularity** · historical analysis · explicit

In the nine cycles since 2008, polls were systematically biased against Democrats once (2012, by about 3 points with Obama beating RCP averages in all 11 toss-up states), against Republicans four times (2014, 2016, 2020, 2024), and roughly unbiased four times. Five biased cycles splitting 4-1 happens 37.5 percent of the time with a fair coin.

*Numbers:* 2012 pro-R poll bias = about 3 points (national and state); probability of 4+ of 5 same direction = 37.5 percent (fair coin)

> if you flip a fair coin 5 times, then 37.5 percent of the time, either heads or tails will come up at least 4 out of 5 times.

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#3</sub>

### 2026-10-15 · [Welcome to midterm silly season 🤡](https://www.natesilver.net/p/welcome-to-midterm-silly-season)
**parameter or number** · FLIPR 2026 · explicit

On Oct. 15, 2026 FLIPR forecast a D+7.8 House popular vote with an 80 percent prediction interval of roughly D+4 to D+12, leaving a 10 percent chance of an outcome beyond each end.

*Numbers:* House popular vote forecast = D+7.8 points (Oct 15, 2026); 80% prediction interval = D+4 to D+12 points (Oct 15, 2026)

> This spans from roughly D +4 to D +12.

<sub>2026-10-15_republicans-are-spending-big-its-not-working#0</sub>

### 2026-10-15 · [Welcome to midterm silly season 🤡](https://www.natesilver.net/p/welcome-to-midterm-silly-season)
**interpretation guidance** · FLIPR 2026 · explicit

Late in a midterm, most remaining uncertainty is measurement error, polls being wrong, rather than opinion changing; to the extent they are wrong, they have probably been wrong all along. Silver recommends mentally shifting all competitive races 3 to 4 points toward either party as a stress test.

*Numbers:* stress-test shift = 3 to 4 points (all competitive races)

> Most of the remaining uncertainty in the election is this kind of uncertainty — about the polls being wrong, not about anything changing.

<sub>2026-10-15_republicans-are-spending-big-its-not-working#2</sub>

### 2026-10-17 · [The good, bad and ugly outcomes in the Senate](https://www.natesilver.net/p/the-good-bad-and-ugly-outcomes-in)
**parameter or number** · Silver Bulletin general · explicit

Silver Bulletin defines a 'normal-sized polling error' as 3 to 4 points in the same direction across states, about the margin by which polls underestimated Trump in 2016, 2020 and 2024. Larger systematic errors are in the tails.

*Numbers:* normal-sized systematic polling error = 3-4 points (Silver Bulletin rule of thumb)

> I’m choosing 3-4 points since that’s basically what we refer to as a “normal-sized polling error” around these parts.

<sub>2026-10-17_the-good-bad-and-ugly-outcomes-in-the-senate#1</sub>

### 2026-10-17 · [The good, bad and ugly outcomes in the Senate](https://www.natesilver.net/p/the-good-bad-and-ugly-outcomes-in)
**parameter or number** · FLIPR 2026 · explicit

Splitting FLIPR Deluxe simulations into thirds by the national error draw: when the error is modest (within about 1.3 points), Democrats win the House 100 percent (238 seats) and the Senate 87.8 percent (52.4 seats). With an error against Democrats (R+1.4 or worse, averaging 3.5): House 81.4 percent (224), Senate 37.7 percent (49.7). With an error against Republicans (averaging 3.5): House 100 percent (254), Senate 99.3 percent (54.6).

*Numbers:* Senate D prob, modest error = 87.8 percent (Oct 17, 2026); Senate D prob, error vs D = 37.7 percent (Oct 17, 2026); Senate D prob, error vs R = 99.3 percent (Oct 17, 2026); House D seats, modest/vsD/vsR = 238/224/254 seats (Oct 17, 2026); tercile boundary = about 1.3 points (national error)

> On average in this scenario, the forecast overestimates Democrats by 3.5 points

<sub>2026-10-17_the-good-bad-and-ugly-outcomes-in-the-senate#2</sub>

### 2026-10-17 · [The good, bad and ugly outcomes in the Senate](https://www.natesilver.net/p/the-good-bad-and-ugly-outcomes-in)
**method** · FLIPR 2026 · explicit

FLIPR's probabilities reflect the estimated error of its blended forecasts (polls plus fundamentals, plus expert ratings in Deluxe), not just the error of the polling averages; Silver notes that 'polling errors' in this context are technically forecast errors.

> The probabilities you see in FLIPR are based on the errors it estimates in these blended forecasts and not just the error associated with the polling averages on their own.

<sub>2026-10-17_the-good-bad-and-ugly-outcomes-in-the-senate#3</sub>

### 2026-10-17 · [The good, bad and ugly outcomes in the Senate](https://www.natesilver.net/p/the-good-bad-and-ugly-outcomes-in)
**interpretation guidance** · FLIPR 2026 analysis · explicit

Uniform-shift stress tests on Senate polling averages: as-is, Democrats 54-46; polls overrating Democrats by 2 points, 52-48 Democratic; by 3 points, a 50-50 tie; by 4 points, Republicans 52-48. Many narrow leads, as in the 2012 and 2016 presidential maps, make the outcome sensitive to small systematic errors.

*Numbers:* Senate seats, 3-pt error vs D = 50 D seats (Oct 17, 2026)

> With a 3-point polling error, though, Maine and Texas turn into narrow GOP wins, and Democrats would top out at 50 seats.

<sub>2026-10-17_the-good-bad-and-ugly-outcomes-in-the-senate#7</sub>

### 2026-10-17 · [The good, bad and ugly outcomes in the Senate](https://www.natesilver.net/p/the-good-bad-and-ugly-outcomes-in)
**assumption** · general · explicit

Predicting polling error means predicting the behavior of pollsters, who are aware of past errors and adjust their methods.

> So in predicting polling error, in some sense you’re predicting the behavior of human beings and how they adjust to changing conditions in the polling landscape.

<sub>2026-10-17_the-good-bad-and-ugly-outcomes-in-the-senate#9</sub>

### 2026-10-20 · [My pet peeve about the polling error debate](https://www.natesilver.net/p/my-pet-peeve-about-the-polling-error)
**empirical regularity** · Silver Bulletin polling database · explicit

In the Silver Bulletin pollster database (polls in the final three weeks of congressional, gubernatorial and presidential elections since 1998), there is almost zero correlation in the direction of polling error between cycles. Pollsters are about as likely to undercompensate as overcompensate for past errors, so there is no zig-zag pattern either.

*Why:* Pollsters have strong incentives to calibrate toward unbiased results but polls are too imprecise to do so reliably.

> Instead, there’s almost literally zero correlation in polling error between cycles.

<sub>2026-10-20_my-pet-peeve-about-the-polling-error-debate#1</sub>

### 2026-10-20 · [My pet peeve about the polling error debate](https://www.natesilver.net/p/my-pet-peeve-about-the-polling-error)
**parameter or number** · Silver Bulletin analysis · explicit

Silver's simulation of random cycle-level polling error used a standard deviation of 2.8 points, matching the variance in the actual historical data. Random draws easily produce streaks such as seven straight cycles underestimating Republicans, which shows how narratives overfit to noise.

*Numbers:* cycle-level polling error SD = 2.8 points (historical, used in simulation)

> A standard deviation of 2.8 points.

<sub>2026-10-20_my-pet-peeve-about-the-polling-error-debate#2</sub>

### 2026-10-20 · [My pet peeve about the polling error debate](https://www.natesilver.net/p/my-pet-peeve-about-the-polling-error)
**design principle** · FLIPR 2026 and predecessors · explicit

FiveThirtyEight/Silver Bulletin forecasts treat the direction of systematic polling error as unpredictable because pollsters self-correct: the model need not 'fix' bias as long as pollsters are expected to recalibrate. Polls today are 'mini-models' as much as pure measurements. FLIPR does not play the guessing game on direction.

> A lot of the reason FLIPR and most of the other models regard polling bias as being unpredictable is because pollsters themselves have a lot of incentive to account and adjust for it.

<sub>2026-10-20_my-pet-peeve-about-the-polling-error-debate#3</sub>

### 2026-10-20 · [My pet peeve about the polling error debate](https://www.natesilver.net/p/my-pet-peeve-about-the-polling-error)
**parameter or number** · Silver Bulletin polling database · explicit

In the 2025 interim elections polls badly underestimated Democrats: Abigail Spanberger beat her Virginia polling average by 6 points and Mikie Sherrill beat hers in New Jersey by 9, one of the worst misses in a well-polled race, comparable to Collins in 2020.

*Numbers:* Spanberger beat polls by = 6 points (VA gov 2025); Sherrill beat polls by = 9 points (NJ gov 2025)

> And in New Jersey, Mikie Sherrill beat her polls by 9 points

<sub>2026-10-20_my-pet-peeve-about-the-polling-error-debate#4</sub>

### 2026-10-25 · [Let’s talk shop about every Senate race](https://www.natesilver.net/p/lets-talk-shop-about-every-senate)
**method** · FLIPR 2026 · explicit

Whenever polls and fundamentals disagree, FLIPR raises the race's uncertainty; for example Minnesota had an 11 percent chance of a Republican win and was the tipping point 7 percent of the time despite a D+13 baseline.

*Numbers:* Minnesota R win prob = 11 percent (Oct 25, 2026); Minnesota tipping-point prob = 7 percent (Oct 25, 2026)

> Whenever there’s a disagreement between polls and “fundamentals,” uncertainty tends to be higher, and FLIPR accounts for this.

<sub>2026-10-25_lets-talk-shop-about-every-senate-race-by-nate-silver#7</sub>

### 2026-11-02 · [Where polls and fundamentals clash](https://www.natesilver.net/p/where-polls-and-fundamentals-clash)
**interpretation guidance** · FLIPR 2026 · explicit

In most battleground Senate races in November 2026, the Democrat's polling lead was within a normal-sized polling error of flipping, so FLIPR's base case of a 53-47 Democratic Senate could easily become 51-49 or a Republican hold.

> It wouldn’t take much for FLIPR’s base case — a 53/47 Democratic Senate majority — to turn into 51/49 or even a Republican hold.

<sub>2026-11-02_where-polls-and-fundamentals-clash-by-eli-mckown-dawson#6</sub>

### 2026-11-03 · [Who’s ahead on the generic congressional ballot?](https://www.natesilver.net/p/generic-ballot-average-2026-nate-silver-bulletin-congress-polls)
**method** · Silver Bulletin generic ballot average · inferred_from_chart

The generic ballot chart's shaded bands show where 90 percent of polls are projected to fall.

*Numbers:* band coverage = 90 percent of polls (chart)

<sub>2026-11-03_generic-congressional-ballot-latest-polls-silver-bulletin#6</sub>
