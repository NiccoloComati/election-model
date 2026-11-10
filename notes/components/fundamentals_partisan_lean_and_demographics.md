# Fundamentals partisan lean and demographics

68 findings from 39 articles, oldest first.

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**parameter or number** · FiveThirtyEight 2016 presidential · explicit

FiveThirtyEight's 2016 PVI weighted the most recent presidential election (2012) 75 percent and the prior (2008) 25 percent, unlike Cook's equal weights. It adjusted for home-state effects: presidential candidates historically perform a net 7 points better at home and VP candidates about 2 points.

*Numbers:* recent election weight = 75 percent (2016 PVI); presidential home-state effect = 7 percentage points net (historical); VP home-state effect = about 2 percentage points (historical)

> Historically, presidential candidates perform a net of 7 percentage points better in their home states.

<sub>fte_2016-general-election-forecast-users-guide#13</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**parameter or number** · FiveThirtyEight 2016 presidential · explicit

Three regression strategies were blended. Strategy 1, pure PVI: national margin plus PVI. Strategy 2, a regional regression of the adjusted polling average on PVI plus four region dummies, with split states such as Maryland half South and half Northeast; historically the most effective. Strategy 3, a demographic regression on PVI plus shares Black, Hispanic, Asian, non-Christian, evangelical, Mormon and college graduates plus a 12-month state economic index, with spurious-variable removal. Polls-plus blended them 30/50/20; polls-only and now-cast used 70/30 of strategies 2 and 3.

*Numbers:* polls-plus blend (PVI/regional/demographic) = 30/50/20 percent (2016); polls-only blend (regional/demographic) = 70/30 percent (2016)

*Why:* Hedging complex methods with simpler ones reduces overfitting.

> The polls-plus model uses a 30/50/20 blend of strategies 1, 2 and 3.

<sub>fte_2016-general-election-forecast-users-guide#14</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**method** · FiveThirtyEight 2016 presidential · explicit

In 2016, elasticity scores were calculated from 2012 CCES individual-level voting records and 2008 state exit polls. Swingy states like New Hampshire have homogeneous moderate voters; Mississippi is bifurcated and inelastic; one-party-dominant states also swing less. National shifts are applied scaled by elasticity.

> Elasticity scores are calculated from individual-level voting records from the Cooperative Congressional Election Study (2012) and state-by-state exit polls (2008).

<sub>fte_2016-general-election-forecast-users-guide#18</sub>

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**model change** · FiveThirtyEight 2022 midterm · explicit

In 2022 the model began blending its complex fundamentals formula with a simple alternative of partisan lean plus generic ballot. Tested on 2018 and 2020, the complex version slightly outperformed the simple one, but a blend beat either alone, so partisanship and the generic ballot gained influence relative to other fundamentals.

*Why:* High partisanship era.

> a blend of the complicated and simple formulas does better than either one taken alone.

<sub>fte_midterm-house-senate-governor-methodology#2</sub>

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**parameter or number** · FiveThirtyEight 2018 midterm · explicit

The 2018 FiveThirtyEight partisan lean formula gives 50 percent weight to the 2016 presidential election, 25 percent to 2012, and 25 percent to state legislative elections, the same structure Silver Bulletin used in 2026.

*Numbers:* latest presidential weight = 50 percent (2018); prior presidential weight = 25 percent (2018); state legislative weight = 25 percent (2018)

> In our partisan lean formula, 50 percent of the weight is given to the 2016 presidential election, 25 percent to the 2012 presidential election and 25 percent to state legislative elections.

<sub>fte_midterm-house-senate-governor-methodology#15</sub>

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**parameter or number** · FiveThirtyEight 2018 governor · explicit

Gubernatorial fundamentals use the Senate factors except roll-call ideology, which is not used, and fundraising based on all contributions from the Campaign Finance Institute. The generic ballot is about two-thirds as predictive as for Congress and partisan lean about one-third as predictive: a state 12 points Democratic for Congress projects only about 4 points Democratic for governor.

*Numbers:* generic ballot predictiveness for governor = around two-thirds ratio vs Congress (2018); partisan lean predictiveness for governor = around one-third ratio vs Congress (2018)

> A state that leans toward the Democrats by 12 points in a race for Congress would be predicted to do so by only about 4 points in a race for governor, for example.

<sub>fte_midterm-house-senate-governor-methodology#17</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**parameter or number** · FiveThirtyEight 2020 presidential · explicit

The 2020 partisan lean index weights the past two presidential elections relative to the nation at 75 percent for 2016 and 25 percent for 2012, so states that trended between them may revert somewhat to the mean.

*Numbers:* weight on most recent election = 75 percent (2016); weight on prior election = 25 percent (2012)

> In our partisan lean index, 75 percent of the weight is assigned to 2016 and 25 percent to 2012.

<sub>fte_2020-presidential-forecast-methodology#8</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

The partisan lean index also adjusts for state elasticity, using a blend of each state's elasticity in 2008, 2012 and 2016, and in 2020 for ease of voting via the Cost of Voting Index. The latter was removed in 2024.

*Why:* Lower voting barriers yield higher turnout and more Democratic votes empirically.

> The elasticity scores we’re using for 2020 are based on a blend of each state's elasticity in 2008, 2012 and 2016.

<sub>fte_2020-presidential-forecast-methodology#10</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

The modeled state estimate is an ensemble of three methods. (1) The 'rigid method': the national margin, imputed mostly from state polls, plus the state's partisan lean, e.g. Biden +5 nationally plus D+10 lean gives Biden +15. (2) A demographic regression fitting current state polls on partisan lean plus combinations of race, income, education, urbanization, religiosity and a COVID severity index: up to 180 regressions with collinearity and size limits, averaged with weights by adjusted R-squared and every regression getting some weight. (3) A regional regression on partisan lean plus four region dummies. The rigid method, historically most accurate, gets the majority of the weight, then demographic, then regional.

*Numbers:* number of demographic regressions = as many as 180 regressions (2020)

*Why:* Infer what polls would say in sparsely polled states from better-polled ones.

> The rigid method, which is the most accurate historically, receives the majority of the weight, followed by the demographic regression and then the regional regression.

<sub>fte_2020-presidential-forecast-methodology#11</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**method** · 2024 presidential · explicit

Most parameters in the Silver Bulletin presidential model are adjusted for rising partisanship. This adjustment tends to make electoral margins closer and to diminish the importance of 'candidate quality'.

*Why:* Partisanship increasingly dominates other considerations.

> Most parameters in the model are adjusted for rising partisanship, which tends to make electoral margins closer and diminish the importance of "candidate quality".

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#7</sub>

### 2024-07-29 · [kamala_mode will be activated tomorrow](https://www.natesilver.net/p/kamala_mode-will-be-activated-tomorrow)
**model change** · 2024 presidential · explicit

During the pause after Biden withdrew, the Silver Bulletin team re-examined minor parts of the model, including the home-state adjustment for presidential and vice-presidential candidates.

*Why:* Downtime allowed the review; a new ticket changes the home states involved.

> We also took the downtime to examine a few other minor things, like the home-state adjustment for presidential and VP candidates.

<sub>2024-07-29_kamala-mode-will-be-activated-tomorrow-by-nate-silver#3</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**model change** · 2024 presidential · explicit

The Silver Bulletin model permanently reduced the home-state bonus for presidential and vice presidential candidates, independent of kamala_mode. It had not been revisited because no 2020 or 2024 candidates were from swing states, but a swing-state VP pick such as Josh Shapiro made it relevant.

*Why:* It should probably have been changed sooner; it now matters for swing states.

> we've now reduced the home-state bonus given to presidential and vice presidential candidates. Unlike the other changes, this one is permanent

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#28</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**method** · 2024 presidential · explicit

State forecasts blend the state polling average with a regression estimate. The regression uses polling from other states and national polls, informed by demographic data and past voting patterns. Example: a lone Hawaii poll at Harris +5 against a regression estimate of about +25 might yield a forecast of Harris +15 to +20.

*Numbers:* hypothetical Hawaii poll = Harris +5 points (illustrative); hypothetical regression estimate = 25 points (illustrative); resulting blended forecast = 15 or 20 points (illustrative)

*Why:* In a sparsely polled state the model is skeptical of an outlier poll and effectively treats it as statistically biased, assuming nothing about pollster intent.

> The model will blend that with an estimate based on a regression analysis using polling from other states and national polls, informed by demographic data and past voting patterns.

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#21</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**assumption** · 2024 presidential · explicit

The Silver Bulletin model does not use Democrats' recent average popular-vote edge as its baseline 'normal'. That edge averaged 3.3 points over 2016-2020 and 2.3 points since 2000.

*Numbers:* avg Dem popular vote margin 2016-2020 = 3.3 percentage points; avg Dem popular vote margin since 2000 = 2.3 percentage points

> although this isn't what our model does, you could calculate "normal" based on the fact that Democrats have had an edge in the popular vote in most recent elections.

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#24</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**interpretation guidance** · 2024 presidential · implied

Silver treats a state's past relative leans (2016, 2020) as a reasonableness check on current polling. He judges post-DNC state numbers more realistic because they are closer to historical leans, which implies reversion to the mean in relative state lean.

> the new numbers look a bit more realistic than the pre-DNC ones given how the country wound up voting in 2016 and 2020.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#20</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**parameter or number** · 2024 presidential · explicit

The 2024 Silver Bulletin model projected Harris to win California by 25 points (vs. Biden's 29), New York by 17 (vs. Biden's 23), and Trump to win Iowa by 7. These shrinking blue-state margins slightly reduce the Electoral College / popular vote bias.

*Numbers:* Harris projected margin, California = 25 percentage points (Sept. 2024; Biden 2020 margin was 29); Harris projected margin, New York = 17 percentage points (Sept. 2024; Biden 2020 margin was 23); Trump projected margin, Iowa = 7 percentage points (Sept. 2024)

> The model projects Harris to win New York by “only” 17 points — down from Biden’s 23, and California by “just” 25, down from Biden’s 29.

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#11</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**method** · 2024 presidential · explicit

The 2024 presidential model's state forecast blends the polling average with other non-polling factors, so it can depart from the polls. In North Carolina the polling average was nearly tied (Trump +0.1), yet the model made Trump a slight favorite (Harris 39%) based on those other factors.

*Numbers:* NC polling average margin = 0.1 percentage points (Trump lead) (Sept 21, 2024); NC Harris win probability = 39 percent (Sept 21, 2024)

> Despite the tie in the current polling averages, it has Trump as the slight favorite instead of a true 50/50 race based on the other factors it considers.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#6</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**method** · 2024 presidential · explicit

In Arizona, the non-polling factors in the 2024 presidential model pushed the forecast toward Harris relative to her polls. The model 'thinks the polls are perhaps lowballing Harris.' Silver cites as context that Biden won Arizona in 2020 and Democrats hold the governorship and both Senate seats.

*Why:* Prior partisan results and state-level political context point more Democratic than the polls do.

> But this is one swing state where the model thinks the polls are perhaps lowballing Harris.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#7</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**method** · 2024 presidential · explicit

State-level priors in the Silver Bulletin presidential model are based on state demographics and are blended with state polling.

> its priors based on their demographics

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#3</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**method** · 2024 presidential · explicit

For states with no polling, such as New Jersey and Illinois in 2024, the model imputes results using information from other polls. Those imputations showed Harris's margins in the bluest states down from Biden's 2020 numbers, enough to reduce but not erase the Electoral College gap.

*Why:* Silver says the imputations are usually pretty reasonable.

> Whether through imputation or by directly looking at the polling, the model does expect Harris’s margins in some of the bluest states to be down from Biden’s numbers

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#9</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**empirical regularity** · 2024 presidential polling averages · explicit

As of Oct 12, 2024, Silver Bulletin state polling averages compared with 2020 results show depolarization. Harris trails Biden's 2020 margin in the bluest states and runs ahead of it in some red states (Alaska, Missouri, Nebraska) but not others (Indiana, Montana).

*Numbers:* New York swing = +9 points toward R (D+23.1 in 2020 vs D+13.6 in the 2024 average); California swing = +5.6 points toward R (D+29.2 vs D+23.6); Massachusetts swing = +4.5 points toward R (D+33.5 vs D+29); Maryland swing = +4.0 points toward R (D+33.2 vs D+29.2); Rhode Island swing = +6.0 points toward R (D+20.8 vs D+14.8); Missouri swing = -3.6 points (toward D) (R+15.4 vs R+11.8); Alaska = R+10.1 to R+7.5 margin (2020 result vs 2024 average); Nebraska = R+19.1 to R+17.2 margin (2020 result vs 2024 average); Pennsylvania = D+1.2 to D+0.9 margin (2020 result vs 2024 average); Wisconsin = D+0.6 to D+1.1 margin (2020 result vs 2024 average); Michigan = D+2.8 to D+1.1 margin (2020 result vs 2024 average); Arizona = D+0.3 to R+1.6 margin (2020 result vs 2024 average); Georgia = D+0.2 to R+0.8 margin (2020 result vs 2024 average); Nevada = D+2.4 to D+0.9 margin (2020 result vs 2024 average); North Carolina = R+1.4 to R+0.7 margin (2020 result vs 2024 average); Florida = R+3.4 to R+5.2 margin (2020 result vs 2024 average); Texas = R+5.6 to R+6.3 margin (2020 result vs 2024 average); NE-2 = D+6.4 to D+8.7 margin (2020 result vs 2024 average)

> Harris is underperforming Biden's 2020 numbers on the bluest states in the map, like New York and California.

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#3</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**empirical regularity** · 2024 analysis · inferred_from_chart

Silver regressed 2024 state polling averages on 2020 state results and state white population share across 26 contests. The 2020-result coefficient was about 0.87 (strongly significant), consistent with a compression toward the center. The white-share coefficient was about 0.03 points per percentage point and not significant (p=0.261).

*Numbers:* actual_2020 coefficient = .8663098 (SE .0269775, t=32.11); white_share coefficient = .0306224 (SE .0265559, p=0.261); constant = -2.705415 (SE 1.778665, p=0.142); residual df = 23 (implies 26 observations); Root MSE = ~1.87 points (read from partially cut-off output)

*Why:* Tests whether 2024 shifts follow a racial pattern; the result suggests 'perhaps something there' but falls short of significance.

> it suggests there's perhaps something there but falls well short of the statistical significance threshold

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#4</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**empirical regularity** · general principle · explicit

State results are highly persistent across recent elections. Adding a uniform 2.4-point swing toward the Democrat to the 2016 state margins (Biden's national popular-vote improvement over Clinton) replicates 2020 state results very accurately. Silver's chart says this uniform swing predicted 2020 better than the polls did.

*Numbers:* uniform swing = 2.4 points toward Democrat (2016 to 2020)

*Why:* Supports weighting persistence/partisan-lean baselines heavily.

> you can very accurately replicate 2020 results by taking 2016 results and adding 2.4 points to the Democrat's number in each state

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#12</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**method** · 2024 presidential · explicit

Alongside the state polling average, the 2024 Silver Bulletin model has an alternative method of forecasting states based on regression analysis. When there is less polling, the model relies more heavily on this regression estimate.

*Why:* When polling is sparse, the model needs a substitute estimate for each state.

> Since there's less polling overall, the model also defaults more to its alternative method of forecasting the states, which is based on regression analysis rather than a straight polling average.

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#12</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**design principle** · general principle · explicit

A forecaster should be Bayesian and combine a surprising poll with priors such as the state's previous result. Flipping a state lost by 8 points last time is a big ask, so a single poll showing it should be discounted.

*Numbers:* Trump 2020 Iowa margin = 8 percentage points (prior for the 2024 Iowa forecast)

> we ought to be good Bayesians here: even if Harris has a very good night on Tuesday, winning a state you lost last time by 8 points is a big ask.

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#5</sub>

### 2024-11-04 · [The polls are close, but that doesn’t mean the results will be](https://www.natesilver.net/p/the-polls-are-close-but-that-doesnt)
**method** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model's projection of the national popular vote is formulated mostly from its state-by-state estimates rather than from national polls. As a result it can diverge from the national polling average.

*Numbers:* Projected national popular vote margin = Harris +2.1 percentage points (Nov 3, 2024 model projection); National polling average margin = Harris +0.9 percentage points (Nov 3, 2024; described as 'about 1 point' in the main text)

*Why:* Strong state polls in usually non-competitive states (e.g., Iowa) pull the state-built national estimate toward Harris.

> Rather, it's formulated from our state-by-state estimates.

<sub>2024-11-03_the-polls-are-close-but-that-doesnt-mean-the-results-will-be#0</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**parameter or number** · 2024 presidential · inferred_from_chart

In the 2024 Silver Bulletin model, the polling average is blended with a state-level regression estimate. On Election Day the regression weight in Arizona was 0.01; the regression estimate was 48.2/50.8, against 48.3/50.7 from polls.

*Numbers:* regression blend weight AZ = 0.01 weight (Nov 5 2024); regression estimate AZ = 48.2% Harris / 50.8% Trump vote share (Nov 5 2024)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#15</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**limitation or failure mode** · 2024 presidential · implied

The uniform-swing regression component struggles in states undergoing differential migration-driven shifts, such as Florida and Texas getting redder. Many polls also failed to catch up to these shifts, so Trump overperformed there.

> those states are getting redder — and many polls weren’t able to catch up to this

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#24</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**method** · 2024 presidential / possible 2028 change · explicit

The 2024 model calculates state partisan baselines (partisan lean) from the past two presidential elections. Silver may revisit this for 2028 because there may now be less mean reversion between cycles than before.

*Numbers:* elections used for partisan baseline = 2 elections (past two presidential elections, 2024 model)

*Why:* There is possibly less mean reversion than in previous cycles.

> currently, they’re based on the past two elections, but we might be at the point now where there’s less mean reversion than in previous cycles.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#13</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**limitation or failure mode** · 2024 presidential / possible 2028 change · explicit

The 2024 model infers demographic swings with 'more inferential methods' rather than poll crosstabs. Silver is considering crosstab-based demographic swings for 2028, but notes that in 2024 crosstabs would have been a mixed bag, overestimating swings in states with large Black populations.

> I wonder if there’s some room for using crosstabs to calculate demographic swings instead of relying on more inferential methods. That would have been a mixed bag this year, overestimating the swings in states with large Black populations

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#14</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**limitation or failure mode** · possible 2028 change · explicit

Silver is curious about accounting for electoral changes driven by voter migration patterns, but this may require data he does not have.

> some way to account for electoral changes based on voter migration patterns, but that might require data we don’t have access to.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#18</sub>

### 2025-09-09 · [Is Susan Collins toast?](https://www.natesilver.net/p/is-susan-collins-toast)
**method** · Silver Bulletin analysis, 2025 · inferred_from_chart

In the article's Collins overperformance table, a state's partisan lean is the Democratic-minus-Republican presidential margin in the state relative to the national popular vote, averaged over the prior two presidential elections. The more recent election gets two-thirds of the weight and the earlier one gets one-third.

*Numbers:* weight on most recent presidential election = 2/3 (partisan lean calculation); weight on earlier presidential election = 1/3 (partisan lean calculation); number of prior elections used = 2 presidential elections (partisan lean calculation)

<sub>2025-09-09_is-susan-collins-toast-by-eli-mckown-dawson#0</sub>

### 2025-09-09 · [Is Susan Collins toast?](https://www.natesilver.net/p/is-susan-collins-toast)
**method** · Silver Bulletin analysis, 2025 · inferred_from_chart

The article computes a race's expected lean as the state's partisan lean plus the national popular vote margin. In presidential years the national figure is the presidential popular vote; in off years it is the national House vote as estimated by Split Ticket.

*Numbers:* 2020 expected lean = D+8.8 percentage points (national D+4.5 plus Maine lean D+4.4); 2014 expected lean = D+5.3 percentage points (national R+5.7 plus Maine lean D+11.0); 2008 expected lean = D+16.4 percentage points (national D+7.3 plus Maine lean D+9.2); 2002 expected lean = D+2.4 percentage points (national R+4.8 plus Maine lean D+7.2); 1996 expected lean = D+0.7 percentage points (national D+0.1 plus Maine lean D+0.6)

<sub>2025-09-09_is-susan-collins-toast-by-eli-mckown-dawson#1</sub>

### 2025-09-09 · [Is Susan Collins toast?](https://www.natesilver.net/p/is-susan-collins-toast)
**data source** · Silver Bulletin Urbanization Index · explicit

The Silver Bulletin Urbanization Index measures how many people live within a 5-mile radius of the average resident. Its scatterplot against 2024 Harris vote share shows a positive relationship, with index values plotted on roughly an 8.5–13.5 scale (likely log-scaled). Maine ranks 6th-most rural and sits well above the trend line, as does Vermont.

*Numbers:* radius = 5 miles (Urbanization Index definition); Maine rurality rank = 6th-most rural (Silver Bulletin Urbanization Index)

> the Silver Bulletin Urbanization Index, which measures how many people live within a 5-mile radius of the average resident.

<sub>2025-09-09_is-susan-collins-toast-by-eli-mckown-dawson#13</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**method** · Silver Bulletin generic ballot average (2026) · explicit

For each state, the generic ballot benchmark equals the state's partisan lean plus the national generic ballot multiplied by the state's elasticity.

> Benchmark = partisan lean score + generic ballot * elasticity

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#17</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**parameter or number** · Silver Bulletin generic ballot average (2026) · explicit

A state's partisan lean weights its vote relative to the nation 50 percent on the 2024 presidential election, 25 percent on 2020, and 25 percent on a rolling average of the last five state legislative elections. The legislative figure estimates the lower-chamber popular vote as if all seats were contested, using regression to handle uncontested seats.

*Numbers:* weight on 2024 presidential = 50 percent (partisan lean); weight on 2020 presidential = 25 percent (partisan lean); weight on state legislative average = 25 percent (rolling average of past five state legislative elections)

*Why:* Blends recent presidential results with down-ballot partisanship.

> the formula gives 50 percent of the weight to the 2024 presidential election, 25 percent to the 2020 presidential election, and 25 percent to a rolling average

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#18</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**parameter or number** · Silver Bulletin / FiveThirtyEight elasticity concept, 2026 values · explicit

Elasticity measures how strongly a state swings with the national environment. It is estimated from 2022 and 2024 Cooperative Election Study microdata by giving each voter a probability of voting D or R and treating voters near 50/50 as more swingable. Current values run from 0.90 in Mississippi to 1.23 in Alaska and 1.25 in Hawaii.

*Numbers:* CES sample size = 60,000 voters per survey (2022 and 2024 Cooperative Election Studies); minimum elasticity = 0.90 (Mississippi); elasticity = 1.23 (Alaska); maximum elasticity = 1.25 (Hawaii)

*Why:* Polarized electorates move little with the national tide, while states with more cross-pressured swing voters move more.

> range from 0.90 in Mississippi to 1.23 in Alaska and 1.25 in Hawaii.

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#19</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**method** · Silver Bulletin elasticity (2026) · explicit

Each voter's vote probability for the elasticity calculation is an average of two models. One uses political variables, namely party identification strength and liberal-conservative self-placement. The other uses demographics only. Cross-pressured voters therefore start closer to 50/50.

*Why:* Combining attitudinal and demographic predictors identifies cross-pressured voters.

> these probabilities are based on an average of two formulas

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#20</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**method** · Silver Bulletin 2026 generic ballot page / FLIPR 2026 · explicit

Silver Bulletin computes state-level benchmarks for 2026 as: Benchmark = generic ballot + partisan lean score × elasticity.

> Benchmark = generic ballot + partisan lean score * elasticity

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#18</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**parameter or number** · Silver Bulletin 2026 partisan lean · explicit

The partisan lean score measures how a state voted relative to the nation. It weights the 2024 presidential election at 50%, the 2020 presidential election at 25%, and a rolling average of the past five state legislative elections at 25%.

*Numbers:* 2024 presidential weight = 50 percent (partisan lean); 2020 presidential weight = 25 percent (partisan lean); state legislative weight = 25 percent (rolling average of past five elections)

> the formula gives 50 percent of the weight to the 2024 presidential election, 25 percent to the 2020 presidential election, and 25 percent to a rolling average of the past five state legislative elections.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#19</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**method** · Silver Bulletin 2026 partisan lean · explicit

The state legislative component of partisan lean uses the aggregate lower-chamber popular vote. Because many seats are uncontested, a regression-based method estimates what the aggregate vote would be if all seats were contested.

*Why:* Uncontested seats distort the raw aggregate vote.

> we use some complicated math based on regression analysis to account for this. In essence, we estimate what the aggregate popular vote would be for the lower house if all seats were contested.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#20</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**method** · Silver Bulletin 2026 elasticity · explicit

Elasticity measures how responsive a state is to national swings. It is high in states with many independents and swing voters, such as New Hampshire, and low in polarized states such as Mississippi. The 2026 scores were calculated from microdata in the 2022 and 2024 Cooperative Election Studies, each with about 60,000 respondents.

*Numbers:* CES sample size = 60,000 voters (each of 2022 and 2024 CES)

> Our current elasticity scores, calculated from microdata in the 2022 and 2024 Cooperative Election Studies, which each surveyed 60,000 voters

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#21</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**parameter or number** · Silver Bulletin 2026 elasticity · inferred_from_chart

2026 elasticity scores by state, read from the table: HI 1.25, AK 1.23, NM 1.18, RI 1.10, CT 1.09, MA 1.09, VT 1.09, IA 1.08, ME 1.08, OK 1.08, KS 1.07, NH 1.07, SD 1.07, AZ 1.06, CA 1.05, CO 1.05, NV 1.05, WV 1.05, ND 1.04, TX 1.03, NY 1.02, WI 1.02, IN 1.01, MT 1.01, OH 1.01, UT 1.01, OR 1.00, DE 0.99, NJ 0.99, WY 0.99, FL 0.98, MI 0.98, TN 0.98, WA 0.98, AL 0.97, ID 0.97, KY 0.97, NE 0.97, IL 0.96, LA 0.96, VA 0.96, NC 0.95, SC 0.95, AR 0.94, MN 0.94, PA 0.94, MO 0.93, GA 0.92, MD 0.92, MS 0.90, DC 0.68.

*Numbers:* max elasticity = 1.25 (Hawaii); min state elasticity = 0.90 (Mississippi); DC elasticity = 0.68 (District of Columbia)

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#22</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**interpretation guidance** · Silver Bulletin 2026 benchmarks · explicit

State benchmarks at the D+5.3 generic ballot: NC D+2.6, ME D+12.7, GA D+1.9, MI D+5.4, AK R+8.4, and IA/TX/OH/FL between R+5 and R+6. At D+10 nationally, IA would be D+0.3, OH R+0.5 and AK R+2.3. Alaska's high elasticity makes it move fastest with the national environment.

*Numbers:* NC benchmark = D+2.6 percentage points (at D+5.3); ME benchmark = D+12.7 percentage points (at D+5.3); GA benchmark = D+1.9 percentage points (at D+5.3); MI benchmark = D+5.4 percentage points (at D+5.3); AK benchmark = R+8.4 percentage points (at D+5.3); IA benchmark at D+10 = D+0.3 percentage points (scenario); OH benchmark at D+10 = R+0.5 percentage points (scenario); AK benchmark at D+10 = R+2.3 percentage points (scenario)

> Alaska gets a boost because of its high elasticity

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#23</sub>

### 2026-03-23 · [SBSQ #30: Will liberals turn against sports betting?](https://www.natesilver.net/p/sbsq-30-will-liberals-turn-against)
**parameter or number** · Silver Bulletin state benchmarks (2026) · explicit

Silver Bulletin computes a current partisan benchmark for each state; California's was D+28.8 in March 2026. California typically votes Democratic by 20 to 30 points, and the benchmark sits at the high end because the national environment favored Democrats.

*Numbers:* California benchmark = D+28.8 points (March 2026)

*Why:* The benchmark moves with the national environment.

> Our current benchmark for California is D +28.8

<sub>2026-03-23_sbsq-30-will-liberals-turn-against-sports-betting#6</sub>

### 2026-06-01 · [Should Democrats panic about Platner?](https://www.natesilver.net/p/should-democrats-panic-about-platner)
**parameter or number** · FLIPR 2026 / Silver Bulletin benchmarks · explicit

Silver Bulletin's statewide benchmark for Maine was D+14.6 as of June 1, 2026, combining Democrats' generic ballot lead with Maine's increasingly blue lean; it represents the expected margin for a generic Democrat versus a generic Republican.

*Numbers:* Maine benchmark = D+14.6 points (June 1, 2026)

> our current benchmark for the state is D +14.6.

<sub>2026-06-01_should-democrats-panic-about-platner-by-nate-silver#0</sub>

### 2026-08-11 · [Everything is breaking Democrats’ way. Is it enough to win the Senate?](https://www.natesilver.net/p/everything-is-breaking-democrats-way)
**empirical regularity** · FLIPR 2026 · explicit

Gubernatorial races are considerably less partisan than congressional races, so FLIPR is much less confident that a weak gubernatorial candidate will revert to the partisan mean.

> gubernatorial races are still considerably less partisan than races for Congress.

<sub>2026-08-11_everything-is-breaking-democrats-way-is-it-enough-to-win-the-senate#10</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

Partisan lean scores for each state and district are based on the past two presidential elections relative to the nation and on recent state legislative elections, and reflect new boundaries after redistricting. They are denominated in margin: R+10 means 10 points more Republican in margin than the nation, which Cook PVI would call R+5 because PVI uses one party's vote share. Texas was about R+11 in 2026.

*Numbers:* Texas partisan lean = around R+11 points (margin) (2026); Cook PVI equivalent ratio = about 2x ratio (margin vs share)

> If we say a district is R +10, that means the vote margin in that district is 10 points more Republican than in the country overall.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#16</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

Elasticity, each state's or district's sensitivity to national swings, is estimated from Cooperative Election Study voter-level microdata for 2016 through 2025. It is applied at various points in FLIPR, including scaling national error shifts, but mostly has a minor impact.

*Numbers:* CES waves used = 2016-2025 years (elasticity microdata)

*Why:* Cross-pressured electorates swing more.

> This elasticity calculation, which is derived from voter-level microdata

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#17</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**model change** · FLIPR 2026 · explicit

The ratio of simple to fancy fundamentals is now tied to a polarization coefficient instead of a fixed ratio. Polarization is measured as the difference in party means from Voteview. Fancy fundamentals now use FLIPR's full national-environment estimate; simple fundamentals use the generic ballot alone.

> Our indicator for polarization is the difference in party means from Voteview.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#21</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**model change** · FLIPR 2026 · explicit

FLIPR treats gubernatorial races as less partisan than congressional races more completely in 2026: fundamentals are considerably upweighted for congressional forecasts and slightly downweighted for governors relative to the 2022 build, because partisan lean and fundraising data are less reliable for governor races.

> fundamentals are considerably upweighted in our congressional forecasts but slightly downweighted for governors.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#42</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**parameter or number** · FLIPR 2026 · explicit

Worked example from Texas: simple fundamentals (generic ballot plus Texas partisan lean) gave R+3.4, versus R+14 in 2024. Fancy fundamentals, driven by Paxton's scandals and Talarico's fundraising edge ($65M vs $9M by mid-July), gave D+9.2. The blended fundamentals were D+3.1, with the polling average at Talarico +1.9.

*Numbers:* Texas simple fundamentals = R+3.4 points (Aug 2026); Texas fancy fundamentals = D+9.2 points (Aug 2026); Texas blended fundamentals = D+3.1 points (Aug 2026); Talarico fundraising = 65 million USD (mid-July); Paxton fundraising = 9 million USD (mid-July)

*Why:* The more partisan the climate, the more FLIPR leans on simple fundamentals.

> The more partisan the background climate, the more FLIPR takes advantage of the simple fundamentals hedge.

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#2</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**parameter or number** · FLIPR 2026 · explicit

Michigan example: baseline D+8 from Trump's 1.4-point 2024 win plus the national environment; fancy fundamentals D+11, since El-Sayed's individual fundraising offsets his lack of elected experience; polling average R+1, with a Democratic super PAC poll among inputs; Democratic win probability 68 percent, betting that Haley Stevens supporters return.

*Numbers:* Michigan simple fundamentals = D+8 points (Aug 2026); Michigan fancy fundamentals = D+11 points (Aug 2026); Michigan polling average = R+1 points (Aug 2026)

> our model’s fancy fundamentals actually give Democratic candidate Abdul El-Sayed the edge and push the environment to D +11.

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#9</sub>

### 2026-08-25 · [Do I really buy that Texas could turn blue?](https://www.natesilver.net/p/do-i-really-buy-that-texas-could)
**method** · FLIPR 2026 · explicit

Silver describes FLIPR's simple fundamentals, generic ballot plus a state's partisan lean, as essentially what British analysts call a 'uniform swing'.

> Simple fundamentals consist (simply!) of the generic ballot and a state’s partisan lean score, producing basically what our British readers might call a “uniform swing”.

<sub>2026-08-25_do-i-really-buy-that-texas-could-turn-blue#2</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**design principle** · FLIPR 2026 · explicit

Because partisanship tells far less in governor races (Vermont has a Republican governor, Kentucky a Democratic one), FLIPR treats gubernatorial races as more uncertain and defers more to polls and expert ratings than to fundamentals.

*Why:* Voters rationally split tickets for governor since control of a chamber is not at stake.

> it therefore tends to treat gubernatorial races as more uncertain without the crutch of “Kentucky always votes for Republicans”

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#0</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**parameter or number** · FLIPR 2026 · explicit

Iowa governor example: simple fundamentals R+3 with a D+6.6 national popular vote forecast; fancy fundamentals D+17 (Sand's large in-state individual contributions, his elected experience, no scandals); blended D+12; expert ratings Lean D, Toss-up and Tilt D; Democratic flip probability 84 percent, while Republicans held 60 percent in the same state's Senate race.

*Numbers:* national popular vote forecast = D+6.6 points (Aug 28, 2026); Iowa gov fancy fundamentals = D+17 points (Aug 2026); Iowa gov blended fundamentals = D+12 points (Aug 2026); Iowa gov D flip prob = 84 percent (Aug 2026)

> All of that works out to a fancy fundamentals estimate of D +17.

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#5</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**parameter or number** · FLIPR 2026 · explicit

Race-level polls are blended with fundamentals that reflect state partisanship: in South Carolina, a polling average of Graham +2.6 became a forecast of Graham +5.3. By symmetry, Democrats are expected to outperform their polls in blue states such as Minnesota.

*Numbers:* SC polling average = R+2.6 points (Oct 2026); SC forecast = R+5.3 points (Oct 2026)

> our forecast shows Graham winning by 5.3 after blending in fundamentals that account for how red South Carolina usually is.

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#5</sub>

### 2026-10-23 · [Do these Senate-governor splits make sense?](https://www.natesilver.net/p/do-these-senate-governor-splits-make)
**parameter or number** · FLIPR 2026 · explicit

The median gap in margin between same-state statewide contests (Senate, governor, at-large House) was about 25 points in 1990, about 13 in 2014 and 8 in 2022 (DDHQ data), and FLIPR projects about 6 in 2026. The median is used because individual splits can be huge, e.g. Vermont 2022.

*Numbers:* median split 1990 = about 25 points (DDHQ); median split 2014 = about 13 points (DDHQ); median split 2022 = 8 points (DDHQ); median split 2026 projected = 6 points (FLIPR)

*Why:* Nationalized politics.

> Based on FLIPR’s current projections, we expect statewide ticket-splitting to decrease even further, with a median gap of just six points in 2026.

<sub>2026-10-23_do-these-senate-governor-splits-make-sense#2</sub>

### 2026-10-25 · [Let’s talk shop about every Senate race](https://www.natesilver.net/p/lets-talk-shop-about-every-senate)
**parameter or number** · FLIPR 2026 · explicit

With a D+9.5 likely-voter generic ballot (about a 12-point swing from 2024), FLIPR's simple fundamentals for the red-state tranche were: Alaska R+0.2, Florida R+1.1, Iowa R+1.2 (about R+1), Ohio R+1.6, Texas R+1.9, with a big gap to Kansas (blended R+4.4). Minnesota was D+13 in the generic-ballot baseline.

*Numbers:* LV generic ballot = D+9.5 points (Oct 25, 2026); Alaska simple fundamentals = R+0.2 points (Oct 25); Texas simple fundamentals = R+1.9 points (Oct 25); Kansas blended fundamentals = R+4.4 points (Oct 25); Minnesota baseline = D+13 points (Oct 25)

> Alaska is only R +0.2, Florida R +1.1, Iowa R +1.2, Ohio R +1.6, and Texas R +1.9.

<sub>2026-10-25_lets-talk-shop-about-every-senate-race-by-nate-silver#4</sub>

### 2026-10-25 · [Let’s talk shop about every Senate race](https://www.natesilver.net/p/lets-talk-shop-about-every-senate)
**limitation or failure mode** · FLIPR 2026 · explicit

In Florida, partisan lean scores lag reality because domestic migrants are heavily Republican and voter registration keeps trending red. Silver names accounting for domestic migration trends in partisan lean as one of the more obvious future model improvements.

> One of the more obvious improvements in our model in future years would be to account for these domestic migration trends in our partisan lean scores.

<sub>2026-10-25_lets-talk-shop-about-every-senate-race-by-nate-silver#9</sub>

### 2026-10-25 · [Let’s talk shop about every Senate race](https://www.natesilver.net/p/lets-talk-shop-about-every-senate)
**interpretation guidance** · FLIPR 2026 · explicit

Highly inelastic states with few swing voters, such as Louisiana, Mississippi and South Carolina with large Black populations and conservative evangelical whites, make big Democratic overperformance unlikely; Silver judged 3 to 5 percent more grounded than markets' 8 to 13 percent for Louisiana and Mississippi. New Hampshire, by contrast, is one of the most elastic states.

> Louisiana and Mississippi are extremely inelastic states, with very few true swing voters.

<sub>2026-10-25_lets-talk-shop-about-every-senate-race-by-nate-silver#10</sub>

### 2026-10-27 · [The 83 remotely competitive House races, according to FLIPR](https://www.natesilver.net/p/the-83-remotely-competitive-house)
**method** · FLIPR 2026 · explicit

In toss-up districts like WI-1, KY-6 and MT-1, FLIPR discounts Democratic polling leads with fundamentals; for example, WI-1's D+2.4 fundamentals offset incumbent Bryan Steil's 3-point polling lead to make a toss-up.

*Numbers:* WI-1 fundamentals = D+2.4 points (Oct 2026)

> FLIPR discounts those with the fundamentals and still gives Republicans a slight edge in all three.

<sub>2026-10-27_the-83-remotely-competitive-house-races-according-to-flipr#5</sub>

### 2026-11-02 · [Where polls and fundamentals clash](https://www.natesilver.net/p/where-polls-and-fundamentals-clash)
**design principle** · FLIPR 2026 · explicit

FLIPR uses the generic ballot within 'simple fundamentals' even though it is poll-based, because it is the best measurement of the national environment, fits a partisan climate with predictable state patterns, and avoids the idiosyncrasies of state polling.

> But the generic ballot is our best measurement of the national political environment

<sub>2026-11-02_where-polls-and-fundamentals-clash-by-eli-mckown-dawson#1</sub>

### 2026-11-02 · [Where polls and fundamentals clash](https://www.natesilver.net/p/where-polls-and-fundamentals-clash)
**parameter or number** · FLIPR 2026 · explicit

On Nov. 2, 2026 FLIPR simple fundamentals: Georgia D+6, North Carolina D+7, Michigan D+9, Maine D+17; Alaska, Ohio, Iowa and Texas R+0.3 to R+2. Fancy fundamentals: Iowa D+1, Ohio D+2, Texas D+8, Maine R+7 (Collins), Alaska worse for Peltola after her scandal flag was activated. Blended Maine D+4; blended Texas, Iowa, Ohio, Alaska and Florida all R+3 to D+3.

*Numbers:* generic ballot = D+8.9 points (Nov 2, 2026); LV-adjusted generic ballot = D+9.2 points (Nov 2, 2026); Maine simple fundamentals = D+17 points (Nov 2); Maine fancy fundamentals = R+7 points (Nov 2); Maine blended = D+4 points (Nov 2); Texas fancy fundamentals = D+8 points (Nov 2)

> Alaska, Ohio, Iowa, and Texas range from R +0.3 to R +2 on the simple fundamentals.

<sub>2026-11-02_where-polls-and-fundamentals-clash-by-eli-mckown-dawson#2</sub>

### 2026-11-03 · [FLIPR 2026 House forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-house-model)
**parameter or number** · FLIPR 2026 final · inferred_from_chart

District elasticity values are published per district, e.g. PA-8 1.01, MI-7 0.93, PA-7 1.03, NC-1 0.98, AZ-1 1.04, AZ-6 0.97, WI-3 0.96, NJ-7 0.93, OH-7 1.09, VA-2 0.92.

*Numbers:* district elasticity range shown = 0.92-1.09 (final)

<sub>2026-11-03_2026-midterm-election-house-forecast-silver-bulletin#3</sub>

### 2026-11-03 · [FLIPR 2026 Senate forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-senate-model)
**parameter or number** · FLIPR 2026 final · inferred_from_chart

The final Senate polls-versus-fundamentals table shows blended fundamentals that are almost exactly a 47/53 to 49/51 weighted average of simple and fancy fundamentals in every state where they differ. Examples: Alaska simple R+1.2, fancy R+5.2, blended R+3.3; Georgia D+6.0, D+17.8, D+12.1; Kansas R+7.8, R+1.3, R+4.4; Maine D+16.4, R+6.9, D+4.3; Massachusetts D+42.1, D+34.1, D+37.9. That implies a simple-fundamentals weight of about 0.46 to 0.49 for Senate races in 2026.

*Numbers:* implied simple-fundamentals weight = 0.46-0.49 share (Senate 2026, derived from table)

*Why:* Consistent with methodology saying simple fundamentals get almost half the weight.

<sub>2026-11-03_2026-midterm-election-senate-forecast-silver-bulletin#3</sub>

### 2026-11-03 · [It's Judgment Day for Trump (and for pollsters)](https://www.natesilver.net/p/its-judgment-day-for-trump-and-for)
**empirical regularity** · FLIPR 2026 · explicit

In practice FLIPR adds about a point or two to Democrats' raw polling average in blue states and subtracts the same in red states, consistent with recent polling errors. In effect it assumes red-state polls somewhat overrate Democrats, except where strong candidate-quality factors such as in Texas and Maine counteract partisanship.

*Numbers:* typical partisan pull on polls = 1-2 points (toward state lean)

> In general, the model adds a point or two to Democrats’ raw polling average in blue states, and subtracts the same amount in red states.

<sub>2026-11-03_its-judgment-day-for-trump-and-for-pollsters#3</sub>

### 2026-11-03 · [Who’s ahead on the generic congressional ballot?](https://www.natesilver.net/p/generic-ballot-average-2026-nate-silver-bulletin-congress-polls)
**method** · Silver Bulletin generic ballot average 2026 · explicit

State-level generic ballot benchmarks combine the generic ballot average with each state's partisan lean and elasticity, shown under four scenarios: the current generic ballot, a neutral environment (0), Democrats gaining 5 points, and Republicans gaining 5 points.

*Numbers:* scenario shift = 5 points (benchmark scenarios)

> We show four versions of these benchmarks: one based on the current generic ballot, one assuming a neutral political environment (generic ballot = 0)

<sub>2026-11-03_generic-congressional-ballot-latest-polls-silver-bulletin#4</sub>
