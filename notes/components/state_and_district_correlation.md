# State and district correlation

87 findings from 49 articles, oldest first.

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**method** · FiveThirtyEight 2016 presidential · explicit

Demographic and regional error in 2016 was simulated by randomly varying the vote among groups in a file of more than 100,000 voters built from exit polls and CCES, using religion, race, region, party ID and college education. This produces correlation matrices, for example a high Wisconsin-Minnesota correlation.

*Numbers:* voter file size = more than 100,000 voters (exit polls + CCES)

> The simulations are conducted from a file of more than 100,000 voters, built from the exit polls and CCES.

<sub>fte_2016-general-election-forecast-users-guide#20</sub>

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**model change** · FiveThirtyEight 2022 midterm · explicit

In 2022 FiveThirtyEight increased the assumed correlation of race-by-race errors in congressional races, because polling errors were becoming more correlated even though correlation remains considerably lower than across states in presidential races. It also reduced the emphasis on sample size in poll weighting, consistent with a pollster-ratings change, and removed 2020 COVID-specific tweaks.

> Therefore, we’ve increased the degree to which race-by-race errors are assumed to be correlated in the model.

<sub>fte_midterm-house-senate-governor-methodology#3</sub>

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**parameter or number** · FiveThirtyEight 2018 midterm · explicit

About three-quarters of the uncertainty in the House and Senate forecasts comes from local, race-by-race factors, unlike the presidential model where outcomes are extremely correlated across states. Governor races are even more localized, with partisanship a much weaker factor.

*Numbers:* share of uncertainty from local factors = about three-quarters share (House and Senate, 2018)

> Nonetheless, about three-quarters of the uncertainty in the House and Senate forecasts comes from local, race-by-race factors.

<sub>fte_midterm-house-senate-governor-methodology#5</sub>

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**method** · FiveThirtyEight midterm models · explicit

CANTOR uses a k-nearest neighbors algorithm on demographic, geographic and political factors to find similar districts and states; districts can be compared with states. Stage one guesses what polls would show from partisan lean and incumbency, e.g. Republican incumbents polling poorly where polled suggests vulnerability elsewhere. Stage two adjusts by similarity scores. Projections are corrected for selection bias, since unpolled districts tend to be less competitive. Governor races do not feed CANTOR for House and Senate, but House and Senate feed governors.

*Why:* Impute polls for unpolled races.

> It uses a k-nearest neighbors algorithm to identify similar congressional districts and states based on a variety of demographic, geographic and political factors.

<sub>fte_midterm-house-senate-governor-methodology#13</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

Correlated state error is simulated over these variables: race (white, Black, Hispanic, Asian); religion (evangelical, mainline Protestant, Catholic, Mormon, other, nonreligious); partisan lean in 2016 and 2012; latitude and longitude; region; urbanization; median household income; median age; gender; education (bachelor's share); immigration (share of the voting-eligible population); COVID severity; and expected mail-vote share. Most end-of-campaign state polling error is assumed correlated with other states.

*Why:* A Michigan miss is likely reflected in Wisconsin and Ohio.

> we estimate that at the end of the campaign, most of the error associated with state polling is likely to be correlated with errors in other states.

<sub>fte_2020-presidential-forecast-methodology#26</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**empirical regularity** · FiveThirtyEight 2020 presidential · explicit

States demographically resembling the nation have less polling error under correlated-error simulation, while outlier states are harder to predict; for example, underestimating Mormons barely affects national or Florida polls but could cause a huge miss in Utah.

> states that are outliers based on some combination of the variables listed above tend to be harder to predict.

<sub>fte_2020-presidential-forecast-methodology#27</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**model change** · 2024 presidential · explicit

State-to-state vote correlations are computed from religious affiliation plus other demographic, geographic and political variables. In 2024, finer religious categories were added: African-American evangelicals separately from white evangelicals, plus Jewish and Muslim voters, who had previously been lumped with other groups.

> It now uses more detailed religious categories, with separate breakouts for African-American evangelical voters

<sub>2024-06-26_2024-presidential-election-model-methodology-update#24</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**method** · 2024 presidential · explicit

The model blends each state's polling average with a series of regression-based estimates that infer what the state's polling 'should' be from polls in other states and national numbers. The historically most reliable of these is uniform swing from the previous election.

*Why:* Uniform swing has historically been the most reliable of these techniques.

> the one that has historically been most reliable is indeed to assume some sort of uniform swing from the previous election

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#23</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**adjustment rule** · 2024 presidential · explicit

The regression estimate gets less weight in heavily polled states such as Wisconsin, Michigan and Pennsylvania. Weight on the regression is inversely related to the amount of state polling.

> Wisconsin, Michigan and Pennsylvania are fairly robustly polled — so the regression estimate doesn’t get that much weight

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#24</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**critique of other approach** · general principle · explicit

Some 2016 models gave Clinton as little as a 1 percent chance of losing. Silver calls them wrong, not just unlucky, because they treated similar states such as Michigan and Wisconsin as relatively uncorrelated, an assumption that can be validated empirically as false.

*Numbers:* Clinton loss probability in some 2016 models = 1 percent (2016)

*Why:* Similar states move in similar directions from election to election.

> They were wrong because they made obviously wrong assumptions, especially that the outcomes in similar states such as Michigan and Wisconsin were relatively uncorrelated.

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#25</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**assumption** · 2024 presidential · explicit

In the Silver Bulletin model, Michigan, Wisconsin and Pennsylvania are heavily but not perfectly correlated. Demographic differences matter: Wisconsin is more rural, and Michigan has the largest Arab/Muslim/Palestinian population. In simulations, Biden wins at least one of the three 54% of the time but all three only 32% of the time.

*Numbers:* P(Biden wins at least one of MI/WI/PA) = 54 percent (June 26, 2024); P(Biden wins all three) = 32 percent (June 26, 2024)

*Why:* Winning several correlated bets is still hard (same-game parlay analogy).

> In our simulations, Biden wins at least one of these states 54 percent of the time. But he wins all three of them in only 32 percent of simulations.

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#26</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**empirical regularity** · general principle · explicit

House and Senate races are correlated with each other, but less than presidential state outcomes, because each contest has different candidates. There can be considerable regional variation, as in 2022.

> House and Senate races are correlated with one another — just not to the same degree that the presidential race is

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#44</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**method** · 2024 presidential · explicit

The Silver Bulletin presidential model infers outcomes in thinly polled states by extrapolating from states with more polling.

*Why:* This lets the model work when polling is sparse.

> using data from states where there's more polling to extrapolate the outcomes to states where there isn't

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#3</sub>

### 2024-07-05 · [The broken leg problem](https://www.natesilver.net/p/the-broken-leg-problem)
**limitation or failure mode** · 2024 presidential · explicit

After the debate, the Silver Bulletin 2024 presidential model was too conservative in reflecting the post-debate poll shift: national polls were plentiful but swing-state polls were sparse. Conflicting heuristics let the model 'hold out hope' that Biden's national decline was concentrated in rarely polled, noncompetitive states such as Alabama and Massachusetts. Silver considers that unrealistic and expects it to correct as state polls arrive.

*Why:* With little state polling, the model allows national shifts to be unevenly distributed across states.

> it's holding out hope that maybe Biden's problems are contained to noncompetitive states — that he's losing ground in states like Alabama and Massachusetts that aren't polled much.

<sub>2024-07-05_the-broken-leg-problem-by-nate-silver-silver-bulletin#10</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**critique of other approach** · 538 2024 (Morris) · explicit

In Wisconsin, 538 had a polling average of R+2.2, an adjusted and Election Day polling forecast of R+2.7, and fundamentals of D+0.2. Yet its full forecast was D+1.3, outside the range of both components. Ohio showed similar behavior. Silver calls this nonsensical and possibly a bug. 538 attributes it to 'patterns of overperformance in similar states'.

*Numbers:* 538 WI polling average = R+2.2 percentage points (July 2024); 538 WI Election Day polling forecast = R+2.7 percentage points (July 2024); 538 WI fundamentals = D+0.2 percentage points (July 2024); 538 WI full forecast = D+1.3 percentage points (July 2024)

*Why:* A blend of two components should lie between them.

> 538 projects Trump to lead the polling average by 2.7 points in Wisconsin on Election Day. And it thinks the fundamentals basically show a tie

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#15</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**parameter or number** · 2024 presidential (Biden version) · explicit

In the Biden-Trump version of the Silver Bulletin model, Pennsylvania had a 40% chance of being the tipping-point state.

*Numbers:* PA tipping-point probability = 40 percent (Biden-Trump model, July 2024)

> Pennsylvania was disproportionately important, with a 40 percent chance of being the tipping-point state

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#14</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**parameter or number** · 2024 presidential · inferred_from_chart

In the final Biden-Trump forecast (July 21, 2024), Pennsylvania had a 40% tipping-point chance and a VPI of 9.2. Other tipping-point chances were Georgia 11% (VPI 3.4), Wisconsin 11% (5.2), Michigan 10% (2.9), North Carolina 7% (2.1), Arizona 4% (2.0), Nevada 4% (4.2), Florida 3% (0.4) and Texas 2% (0.2).

*Numbers:* PA tipping point = 40% probability (July 21, 2024); PA VPI = 9.2 (July 21, 2024); GA tipping point = 11% probability; WI tipping point = 11% probability; MI tipping point = 10% probability; NC tipping point = 7% probability

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#20</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**empirical regularity** · 2024 presidential · inferred_from_chart

The conditional win probabilities show the correlation structure. If Biden wins Florida his chance of winning overall rises to 97.6%, and if he wins Texas, to 98.2%. If Trump wins Minnesota his chance rises to 98.9%, and if he wins Virginia, to 99.7%. Biden winning Pennsylvania gives him 86.8%, while Biden winning Michigan gives only 61.7%.

*Numbers:* Biden win | wins FL = 97.6% probability (July 21, 2024); Biden win | wins TX = 98.2% probability; Biden win | wins PA = 86.8% probability; Biden win | wins MI = 61.7% probability; Trump win | wins MN = 98.9% probability; Trump win | wins VA = 99.7% probability; Trump win | wins PA = 96.7% probability

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#21</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

Separately from the national uncertainty index, the model makes an additional calculation of how accurately it can pinpoint each state's numbers. This state-level uncertainty is higher in states with little Harris-Trump polling.

> The uncertainty index governs how much the model expects the national race to swing. But there's an additional calculation in how accurately the model thinks it can pinpoint the state-by-state numbers.

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#27</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**empirical regularity** · 2024 presidential · explicit

In the Aug 8, 2024 run, Trump's 46% overall chance of winning the Electoral College rose to 95.5% (reported as 96%) when he wins Pennsylvania. Harris has less than a 10% chance of winning if she loses any Blue Wall state. If Harris wins Michigan, Trump still has 17%, reflecting his additional Sunbelt paths.

*Numbers:* Trump EC chance = 46 percent (Aug 8, 2024); Trump P(win | PA) = 96 percent (Aug 8, 2024); Trump P(win | Harris wins MI) = 17 percent (Aug 8, 2024)

> Harris has a less than 10 percent chance of winning the election if she loses any of them.

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#5</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**assumption** · 2024 presidential · explicit

State outcomes in the Silver Bulletin model are correlated rather than independent, with stronger correlation between geographically and demographically similar states.

> Candidates' performances across states aren't independent, so if someone wins Pennsylvania, they're much more likely to win other battleground states — especially geographically and demographically similar states.

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#6</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**empirical regularity** · 2024 presidential · inferred_from_chart

Swing-state win probabilities conditional on Pennsylvania (Aug 8, 2024), shown as unconditional / if Harris wins PA / if Trump wins PA:
- Wisconsin: 57% Harris / 90% Harris / 85% Trump
- Michigan: 63% Harris / 94% Harris / 77% Trump
- Georgia: 57% Trump / 70% Harris / 91% Trump
- Arizona: 55% Trump / 74% Harris / 93% Trump
- North Carolina: 63% Trump / 63% Harris / 97% Trump
- Nevada: 51% Harris / 79% Harris / 86% Trump

*Numbers:* WI Harris | Harris wins PA = 90 percent (Aug 8, 2024); NC Harris | Harris wins PA = 63 percent (Aug 8, 2024); NC Trump | Trump wins PA = 97 percent (Aug 8, 2024)

*Why:* Shows the implied strength of correlation between Pennsylvania and other swing states.

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#7</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**method** · 538 2020, carried into 2024 Silver Bulletin · explicit

Correlated polling error in the simulations, as described for the 2020 FiveThirtyEight model and cited as still applying, comes from random permutations along demographic and geographic characteristics. For example, in one simulation Trump overperforms with Hispanic voters and so does better in heavily Hispanic states; in another, Biden overperforms in states with many Catholics.

> to calculate correlated polling error, the model creates random permutations based on different demographic and geographic characteristics.

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#8</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**assumption** · 2024 presidential · explicit

The model assumes polling error is at least partly systematic and correlated across states. For example, if Trump overperforms his forecast in Wisconsin, he likely also overperforms in Michigan, and the same holds symmetrically for Harris.

> the model assumes that to the extent there’s a polling error, it probably will be systematic, at least in part.

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#14</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**empirical regularity** · 2024 presidential · explicit

Poor polling for Harris in Pennsylvania, the most likely pivotal ('tipping-point') state, made the Electoral College forecast swing more than the popular vote forecast.

*Numbers:* Pennsylvania polling average = D+1.2 percentage points (Sept 1, 2024 table; R+0.5 change over last week)

> Pennsylvania, which is disproportionately important given Pennsylvania's likelihood of being the pivotal state. As a result, the Electoral College forecast has swung more than the popular vote forecast.

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#18</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**parameter or number** · 2024 presidential · inferred_from_chart

Silver Bulletin lists state leans relative to the national margin (2016 result / 2020 result / 2024 polling average / 2024 forecast) as of Sept. 6, 2024:
- PA: R+2.8 / R+3.3 / R+2.4 / R+2.4
- MI: R+2.3 / R+1.7 / R+1.2 / R+1.2
- GA: R+7.2 / R+4.2 / R+2.8 / R+3.1
- NC: R+5.8 / R+5.8 / R+4.0 / R+4.0
- WI: R+2.9 / R+3.8 / R+0.6 / R+1.1
- AZ: R+5.6 / R+4.1 / R+4.9 / R+4.5
- NV: D+0.3 / R+2.1 / R+2.3 / R+2.2
The forecast's relative lean differs only slightly from the polling average's, e.g. Wisconsin is pulled toward its historical lean (R+0.6 to R+1.1).

*Numbers:* WI relative lean polling avg vs forecast = R+0.6 vs R+1.1 percentage points (2024, Sept. 6); GA relative lean polling avg vs forecast = R+2.8 vs R+3.1 percentage points (2024); AZ relative lean polling avg vs forecast = R+4.9 vs R+4.5 percentage points (2024)

*Why:* Forecast blends polls with other information (likely fundamentals/prior partisan lean), shifting outlier relative leans modestly.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#12</sub>

### 2024-09-07 · [Oops! I made the convention bounce adjustment disappear.](https://www.natesilver.net/p/oops-i-made-the-convention-bounce)
**method** · 2024 presidential · explicit

The 2024 model's state forecasts are not based strictly on each state's own polling average. They hedge slightly toward inferences drawn from national polls and polls of other states.

> the model's state-by-state forecasts are not strictly based on the polling averages in each state; instead, it hedges slightly against these with inferences it makes from national polls and polls of other states

<sub>2024-09-07_oops-i-made-the-convention-bounce-adjustment-disappear#9</sub>

### 2024-09-07 · [Oops! I made the convention bounce adjustment disappear.](https://www.natesilver.net/p/oops-i-made-the-convention-bounce)
**assumption** · 2024 presidential · explicit

Arizona and Nevada, bordering states, have highly correlated outcomes in the model's simulations. Winning both together is therefore a plausible joint outcome.

*Numbers:* AZ+NV combined EVs = 17 electoral votes (2024)

*Why:* Geographic and demographic similarity.

> a plausible outcome since these bordering states have highly correlated outcomes

<sub>2024-09-07_oops-i-made-the-convention-bounce-adjustment-disappear#11</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**parameter or number** · 2024 presidential · explicit

In the Sept. 17, 2024 Silver Bulletin model run, Harris had a 14 percent chance of winning Florida and a 7 percent chance of winning Texas. These outcomes happen in the model mainly in Obama-esque landslide scenarios where the states come into play.

*Numbers:* Harris win probability, Florida = 14 percent (Sept. 17, 2024 model run); Harris win probability, Texas = 7 percent (Sept. 17, 2024 model run)

*Why:* The states are highly unlikely to matter in a close election but could be competitive in a blowout.

> Harris is unlikely to win Florida (a 14 percent chance as of Tuesday’s model run) or Texas (7 percent)

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#5</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**method** · 2024 presidential · inferred_from_chart

The article's header image shows a correlation matrix with rows labeled 'tvaryCO', 'tvaryCT', 'tvaryDC', 'tvaryFL' and so on. The image suggests the model uses state-level time-varying error terms with pairwise correlations, including negative values such as about -0.69 between some states. The labels on the columns are not fully legible.

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#10</sub>

### 2024-09-19 · [Don't let randomness make a fool of you](https://www.natesilver.net/p/dont-let-randomness-make-a-fool-of)
**method** · 2024 presidential · explicit

The Silver Bulletin model makes inferences about a state's polling from polls of other states, borrowing strength across states.

*Why:* This is described as part of the model's value beyond simple averaging.

> making inferences about what the polls in one state say based on polls of other states

<sub>2024-09-19_dont-let-randomness-make-a-fool-of-you-by-nate-silver#8</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**empirical regularity** · 2024 presidential · explicit

Errors across the seven swing states are highly correlated in the 2024 Silver Bulletin presidential model. A systematic polling error or a late shift in the race can cause one candidate to sweep all seven. Harris swept all seven in 20% of simulations and Trump in 23%, so a sweep by someone occurred in 43% of simulations.

*Numbers:* Harris sweeps all 7 swing states = 20 percent of simulations (Sept 21, 2024); Trump sweeps all 7 swing states = 23 percent of simulations (Sept 21, 2024)

*Why:* A systematic polling error, or a shift in the race over the final six weeks, moves all the states together.

> A systematic polling error, or a shift in the race in the final six weeks of the campaign, could result in one candidate sweeping all of these states.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#1</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**assumption** · 2024 presidential · explicit

Demographic correlation drives joint state outcomes. Florida becomes part of a Harris winning map mainly in scenarios where her vote collapses among the white working class but she overperforms among Hispanics or voters of color. In that case she can lose all three Blue Wall states and win via Florida, Arizona and Nevada.

> The particular scenario where Florida creates winning maps for Harris is if her vote collapses among the white working class — but she overperforms among Hispanics or voters of color generally.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#13</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**empirical regularity** · 2024 presidential · explicit

Because the Silver Bulletin 2024 model correlates states, it rarely produces outcomes where Arizona and Wisconsin diverge sharply. Only 147 of 40,000 simulations (about 0.37%) had Harris losing Arizona by at least 5 points while winning Wisconsin by at least 6.

*Numbers:* simulations with Harris losing AZ by ≥5 and winning WI by ≥6 = 147 simulations (out of 40,000, Sep 23, 2024 run); AZ loss threshold = 5 percentage points (matches Times/Siena Arizona result); WI win threshold = 6 percentage points (matches MassINC Wisconsin result)

*Why:* You would bet heavily against Democratic overperformance in Wisconsin combined with underperformance in Arizona, so at least one of the two polls is almost certainly wrong.

> there were only 147 cases where Harris both lost Arizona by at least 5 points, matching the Times result, and won Wisconsin by at least 6

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#1</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**interpretation guidance** · 2024 presidential · explicit

New polls showing a candidate behind in states where the model already had that candidate narrowly behind, and which are not on the candidate's minimum path to 270, move the overall forecast less than expected. Conflicting high-quality polls in other states (e.g., Sunbelt vs. Wisconsin) also partly offset each other.

*Why:* Harris's minimum viable path ran through PA, MI, WI and NE-2.

> The polls had less of an effect on our model than I'd expected.

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#6</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**assumption** · 2024 presidential · explicit

In the model, Michigan, Pennsylvania and Wisconsin are correlated but not perfectly, so winning all three is a 'correlated parlay' that remains hard to hit.

*Why:* State-specific shocks, such as a Wisconsin polling error or Arab American voters in Michigan swinging on Gaza, can flip a single state.

> Michigan, Pennsylvania and Wisconsin are correlated, but not perfectly so, and as any sports bettor will tell you, correlated parlays are still hard to win

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#12</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**empirical regularity** · 2024 presidential · explicit

In the Sept. 29 run, the most common swing-state outcome was a Harris sweep of all seven (15,273 of 70,000) and the second most common was a Trump sweep (13,912 of 70,000). Together they make up about 40% of simulations, which reflects strongly correlated state polling errors.

*Numbers:* Harris sweep count = 15,273 of 70,000 simulations (Sept. 29, 2024; default Harris EV 317); Trump sweep count = 13,912 of 70,000 simulations (Sept. 29, 2024; default Harris EV 226); combined sweep probability = about 40 percent (either full sweep)

*Why:* Even a normal-sized across-the-board polling error decides every swing state in the same direction.

> These are far more likely than any other combos; in fact, combined, there’s about a 40 percent chance that one of them will come up.

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#2</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**assumption** · 2024 presidential · explicit

The model expects polling errors to be correlated across states. An across-the-board miss is possible, but errors are more likely to come in regional clusters: Michigan and Wisconsin tend to move together, as do Georgia and North Carolina.

*Why:* Regional and demographic similarity.

> it further expects those errors to be correlated to some degree — perhaps an across-the-board miss, but more likely in some regional clusters: Michigan and Wisconsin will tend to move together, as will Georgia and North Carolina.

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#4</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**assumption** · 2024 presidential · explicit

The model treats Arizona and Nevada as highly correlated because of their similar demographic makeup. With Harris polling +1.8 in NV and -1.3 in AZ, maps where Harris wins AZ but loses NV are the least likely. That combination occurred in 894 of 70,000 simulations (1.3%), and some specific maps of this kind appeared only 2 times.

*Numbers:* NV polling margin = +1.8 percentage points (Harris) (Sept. 29, 2024); AZ polling margin = -1.3 percentage points (Harris) (Sept. 29, 2024); Harris wins AZ but loses NV = 894 of 70,000 simulations (any combination of the other five battlegrounds); Harris wins AZ but loses NV = 1.3 percent (same); least likely combination count = 2 of 70,000 simulations (least likely maps)

*Why:* Flipping relative positions would require a large state-specific error that the polls missed.

> the model expects Arizona and Nevada to be highly correlated — they have a similar demographic makeup.

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#5</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**method** · 2024 presidential · explicit

The model's correlation structure works through demographics. In simulations where Harris loses both Arizona and Nevada, implying Hispanic underperformance, New Mexico also becomes more likely to flip. Where she underperforms with white voters, New Hampshire becomes a risk.

*Why:* Shared demographic groups transmit polling error across states.

> It notices, for instance, that on this map, Harris has lost Arizona and Nevada, which implies significant underperformance with Hispanic voters — and if Harris is really losing ground with Hispanics, New Mexico could be a problem too.

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#6</sub>

### 2024-10-01 · [SBSQ #13: October Surprise edition](https://www.natesilver.net/p/sbsq-13-october-surprise-edition)
**design principle** · general principle · explicit

State polling errors are correlated. Some forecasters in 2016 published a 99+ percent chance of Hillary Clinton winning because they failed to account for this correlation.

*Numbers:* Clinton win probability in some 2016 forecasts = 99+ percent (2016 forecasters that ignored correlated state errors)

*Why:* Ignoring correlated state errors produces drastic overconfidence.

> some forecasters published a 99+ percent chance of Hillary Clinton winning because they didn't understand that state polling errors are correlated.

<sub>2024-10-01_sbsq-13-october-surprise-edition-by-nate-silver#10</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**empirical regularity** · Silver Bulletin 2024 presidential model · explicit

Electoral shifts tend to follow a uniform swing. As a result, the ranking of tipping-point states is stable across very different national environments. In the Silver Bulletin forecasts, the tipping-point order was almost the same when Trump led by 4 nationally (Biden-Trump forecast at shutoff) as when Harris led by 3 (Oct. 2024): Pennsylvania #1; then Michigan, Wisconsin, Georgia and North Carolina in some combination; then Arizona and Nevada a little behind.

*Numbers:* Trump national lead at Biden forecast shutoff = 4 points (July 2024); Harris national lead = 3 points (Oct 10 2024)

*Why:* Because of uniform swing, a consistently biased poll still yields correct relative state ordering; precision matters more than accuracy for resource allocation.

> Because electoral shifts tend to follow a uniform swing, your polls can be biased so long as they're biased in a consistent way.

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#12</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**empirical regularity** · 2024 presidential · inferred_from_chart

Between Sept. 27 and Oct. 17, 2024, Trump's win probabilities in the Silver Bulletin model rose most in the Blue Wall states (MI +12.6, WI +8.9, PA +8.7 points). Gains elsewhere were incremental (GA +4.6, NV +3.5, NC about +3, AZ about +2.6), while the national probability rose +8.5 points. This shows correlated, regionally clustered movement.

*Numbers:* Arizona = 64.4% -> 67.0% percent Trump win prob (Sept. 27 to Oct. 17); Georgia = 59.9% -> 64.5% percent; Michigan = 32.2% -> 44.8% percent; Nevada = 40.8% -> 44.3% percent; North Carolina = 58.2% -> 61.3% percent; Pennsylvania = 37.8% -> 46.5% percent; Wisconsin = 37.5% -> 46.4% percent; National = 41.7% -> 50.2% percent

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#21</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**method** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model's simulations account for correlated polling error across states. As a result, a normal-sized error can push all 7 key battleground states toward the same candidate.

*Numbers:* number of key battleground states = 7 states (AZ, GA, MI, NC, NV, PA, WI)

*Why:* Polling errors are correlated across states, so a sweep is a natural outcome.

> In our simulations yesterday, which account for the possibility of a correlated polling error, the most common outcome was Trump winning all 7 swing states

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#1</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**empirical regularity** · 2024 presidential · explicit

In the Nov 1, 2024 Silver Bulletin model run, all seven core battleground states (AZ, GA, MI, NV, NC, PA, WI) finished within 2.5 points in only about 2.5% of simulations. This shows the model's polling-error distribution routinely produces at least one state with a margin wider than 2.5 points, even though every polling average is close.

*Numbers:* simulations with all 7 swing states within 2.5 pts = 1011 simulations (out of 40,000, Nov 1, 2024); share of simulations with all 7 swing states within 2.5 pts = about 2.5 percent (Nov 1, 2024)

*Why:* Illustrates that surprises are expected: "it would be a surprise if there were no surprises".

> Whatever happens on Tuesday, it would be a surprise if there were no surprises.

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#1</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**empirical regularity** · 2024 presidential · explicit

In the 2024 Silver Bulletin model, a big Iowa poll barely moved the national forecast. Iowa had only a 1% chance of being the tipping-point state, because its outcomes are highly correlated with the Blue Wall states, especially Wisconsin. By the time Harris wins Iowa she has usually already won the Blue Wall.

*Numbers:* Iowa tipping-point probability = 1 percent (Nov 2, 2024)

*Why:* Correlated states are redundant for Electoral College paths.

> mostly it's because Iowa is unlikely — only a 1 percent chance — to be the tipping-point state. The reason is that its outcomes are likely to be highly correlated with the Blue Wall states

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#10</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**parameter or number** · 2024 presidential · inferred_from_chart

The Silver Bulletin 2024 model's simulated state outcome correlations (from 40,000 simulations) for Iowa are: Iowa-Wisconsin .84, Iowa-Michigan .70, Iowa-Pennsylvania .69, Iowa-North Carolina .57, Iowa-Arizona .48, Iowa-Nevada .35, Iowa-Georgia .31.

*Numbers:* IA-WI = .84 correlation (40,000 simulations, Nov 2, 2024); IA-MI = .70 correlation; IA-PA = .69 correlation; IA-NC = .57 correlation; IA-AZ = .48 correlation; IA-NV = .35 correlation; IA-GA = .31 correlation

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#11</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**parameter or number** · 2024 presidential · inferred_from_chart

Simulated correlations among the 2024 swing states in the Silver Bulletin model are: MI-PA .82, MI-WI .83, PA-WI .81, GA-NC .82, AZ-NV .82, MI-GA .57, MI-NC .72, MI-AZ .63, MI-NV .56, PA-GA .55, PA-NC .73, PA-AZ .65, PA-NV .52, WI-GA .41, WI-NC .65, WI-AZ .60, WI-NV .49, GA-AZ .48, GA-NV .40, NC-AZ .60, NC-NV .44. Regional blocs (Blue Wall, Sun Belt South, Southwest) are the most tightly correlated.

*Numbers:* MI-PA = .82 correlation; MI-WI = .83 correlation; PA-WI = .81 correlation; GA-NC = .82 correlation; AZ-NV = .82 correlation; MI-GA = .57 correlation; MI-NC = .72 correlation; MI-AZ = .63 correlation; MI-NV = .56 correlation; PA-GA = .55 correlation; PA-NC = .73 correlation; PA-AZ = .65 correlation; PA-NV = .52 correlation; WI-GA = .41 correlation; WI-NC = .65 correlation; WI-AZ = .60 correlation; WI-NV = .49 correlation; GA-AZ = .48 correlation; GA-NV = .40 correlation; NC-AZ = .60 correlation; NC-NV = .44 correlation

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#12</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**parameter or number** · 2024 presidential · explicit

In 2024 Silver Bulletin simulations where Harris won Iowa, her average margin was +6.7 in Wisconsin, +5.9 in Michigan and +3.8 in Pennsylvania. Conditional on winning Iowa, she won Wisconsin 98% of the time.

*Numbers:* Avg WI margin given Harris wins IA = +6.7 percentage points; Avg MI margin given Harris wins IA = +5.9 percentage points; Avg PA margin given Harris wins IA = +3.8 percentage points; P(win WI | win IA) = 98 percent

> Conditional on winning Iowa, her chances in Wisconsin are 98 percent, for instance.

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#14</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**method** · 2024 presidential · explicit

The Silver Bulletin model defines geographic regions by county rather than by state, so more than a dozen states straddle two or more regions. About two-thirds of Pennsylvania's population falls in the Northeast region rather than the Midwest, which makes Pennsylvania less correlated with Iowa than Wisconsin or Michigan are.

*Numbers:* Share of PA population in Northeast region = about two-thirds; States straddling regions = more than a dozen states

*Why:* County-level regions capture within-state heterogeneity in correlation structure.

> about two-thirds of its population is in what we consider the Northeast, not the Midwest like Iowa. (Our regions are divided by county, not state — so more than a dozen states straddle two or more of them.)

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#15</sub>

### 2024-11-04 · [The polls are close, but that doesn’t mean the results will be](https://www.natesilver.net/p/the-polls-are-close-but-that-doesnt)
**method** · 2024 presidential · explicit

The model's simulations allow correlated regional polling errors, so that in some simulations Harris outperforms her polls in the Midwest while in others Trump overachieves in the Northeast.

*Why:* Errors are often regional, as in 2016.

> We account for these possibilities in our forecast. In some simulations, Harris outperforms her polls in the Midwest, while in others Trump overachieves in the Northeast.

<sub>2024-11-03_the-polls-are-close-but-that-doesnt-mean-the-results-will-be#5</sub>

### 2024-11-04 · [The polls are close, but that doesn’t mean the results will be](https://www.natesilver.net/p/the-polls-are-close-but-that-doesnt)
**method** · 2024 presidential · explicit

For the regional scenario analysis, the analysts used four regions (Northeast, West, South, Midwest) defined at the county level, so some states are split across regions. Each region was assigned a 3.1-point error toward D, a 3.1-point error toward R, or no error (N), giving 81 combinations, and the national uniform swing was zeroed out.

*Numbers:* Regional error size = 3.1 percentage points (applied per region); Number of regions = 4 (Northeast, West, South, Midwest); Number of combinations = 81 scenarios (3^4; the table spans 4 pages)

*Why:* Zeroing the swing isolates the effect of regional swings when there is no uniform polling error.

> For purposes of this exercise, we zeroed out the national swing, since our goal is to see the effect of regional swings if there isn't a uniform polling error.

<sub>2024-11-03_the-polls-are-close-but-that-doesnt-mean-the-results-will-be#6</sub>

### 2024-11-04 · [The polls are close, but that doesn’t mean the results will be](https://www.natesilver.net/p/the-polls-are-close-but-that-doesnt)
**parameter or number** · 2024 presidential · inferred_from_chart

In the regional scenario table, Harris's Electoral College win probability was 96.1% (311 average EVs) with D errors in all four regions. With D errors in the Northeast, West and South and no error in the Midwest it was 88.5% (300 EVs). With a Midwest R error and the other three regions D it was 72.5% (284 EVs). With no errors anywhere (D, N, N, N) it was 61.9% (273 EVs).

*Numbers:* DDDD (NE, W, S, MW) = 96.1% / 311 win prob / EVs (Nov 3, 2024); DDDN = 88.5% / 300 win prob / EVs; DDDR = 72.5% / 284 win prob / EVs; DNNN = 61.9% / 273 win prob / EVs (Northeast D only); DNRN = 49.0% / 264 win prob / EVs; DNRR = 13.4% / 248 win prob / EVs; DDNR = 39.0% / 266 win prob / EVs; DDRR = 21.7% / 256 win prob / EVs

<sub>2024-11-03_the-polls-are-close-but-that-doesnt-mean-the-results-will-be#7</sub>

### 2024-11-04 · [The polls are close, but that doesn’t mean the results will be](https://www.natesilver.net/p/the-polls-are-close-but-that-doesnt)
**parameter or number** · 2024 presidential · explicit

With the national swing zeroed out, a 3.1-point Harris overperformance in the Midwest alone gives her a 69% chance of winning. A Midwest overperformance combined with Trump overperforming in the South and West gives her 36%.

*Numbers:* Harris win prob, Midwest D only = 69 percent (regional scenario); Harris win prob, Midwest D with South and West R = 36 percent (regional scenario)

*Why:* The Midwest D scenario gives Harris a good chance of carrying all three Blue Wall states.

> If Harris overperforms in the Midwest but the polls are accurate elsewhere, she has a 69 percent chance of winning the race.

<sub>2024-11-03_the-polls-are-close-but-that-doesnt-mean-the-results-will-be#8</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**empirical regularity** · 2024 presidential · inferred_from_chart

States are strongly correlated in the 2024 Silver Bulletin simulations. Trump winning all seven battlegrounds was the single most likely scenario at 20.0%, and Harris winning all seven was next at 13.9%. Winning Pennsylvania gave Harris a 90.4% and Trump an 87.9% chance of winning overall.

*Numbers:* all-R battleground sweep = 20.0% probability (AZ GA MI NC NV PA WI); all-D battleground sweep = 13.9% probability (AZ GA MI NC NV PA WI); Harris win prob if wins PA = 90.4% probability (final); Trump win prob if wins PA = 87.9% probability (final)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#24</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**assumption** · 2024 presidential · explicit

The 2024 model treats polling errors as highly correlated between states: when polls underestimate Trump in one key state, they likely underestimate him in most or all of the others.

> When polls miss low on Trump in one key state, they probably also will in most or all of the others.

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#9</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**parameter or number** · 2024 presidential · explicit

Because of correlated error, and because Trump led in 5 of 7 swing states, a Trump sweep of all 7 swing states was the model's most common swing-state scenario (20% of simulations). A Harris sweep was second (14%; 13.9% in the table).

*Numbers:* Trump swing state sweep = 20 percent of simulations (final 2024); Harris swing state sweep = 14 percent of simulations (final 2024; 13.9% in table)

*Why:* Correlated errors make sweeps more likely than independent state draws would imply.

> a Trump sweep of the swing states was actually our most common scenario, occurring in 20 percent of simulations

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#11</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**empirical regularity** · 2024 presidential · explicit

Trump was more likely to sweep than Harris despite a 50/50 topline mostly because of Arizona, where Trump led by 2.4 points in the final polling average. Harris won every swing state except Arizona in about 4% of simulations.

*Numbers:* Trump lead in Arizona final polling average = 2.4 percentage points (final 2024); Harris wins all but Arizona = about 4 percent of simulations (final 2024; table shows 3.8%)

> is mostly because of Arizona, which was teetering into “lean Trump” territory with a 2.4-point Trump lead in our final polling average

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#12</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**parameter or number** · 2024 presidential · explicit

Conditional on Trump winning all 7 swing states, the model gave him these chances in further Democratic-leaning places: New Mexico 22%, Minnesota 21%, New Hampshire 19%, Maine (statewide) 16%, Nebraska's 2nd District 11%, Virginia 10%. This shows strong correlation extending beyond the swing states into landslide scenarios.

*Numbers:* P(NM | sweep) = 22 percent (conditional on Trump sweep); P(MN | sweep) = 21 percent; P(NH | sweep) = 19 percent; P(ME | sweep) = 16 percent; P(NE-2 | sweep) = 11 percent; P(VA | sweep) = 10 percent

> Conditional on winning all 7 swing states, for instance, Trump had a 22 percent chance of also winning New Mexico, a 21 percent chance at Minnesota

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#17</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**empirical regularity** · 2024 presidential · explicit

Maps giving Trump exactly 312 EV with a different combination of states occurred about 0.4% of the time (342 of 80,000 simulations).
- Most common alternative: Harris wins Nevada, Trump wins New Hampshire and Maine statewide. Maine and New Hampshire are highly correlated with each other and with northern white voters in the Blue Wall, while Nevada behaves differently.
- Next alternative (83 of 80,000 sims): Trump wins Minnesota but loses Georgia. This reflects a scenario of Blue Wall/Minnesota overperformance combined with lagging among Black voters, since Georgia has the largest Black voter share among the battleground states.

*Numbers:* alternative 312 maps share = 0.4 percent of simulations (5,002 minus 4,660); MN-win/GA-loss map = 83 simulations of 80,000 (final 2024)

*Why:* State outcomes in the model correlate along demographic lines (northern whites, Black voters) and by geographic proximity.

> Maine and New Hampshire could plausibly follow, and their results are likely to be highly correlated with one another. Whereas Nevada had been one of the bluer swing states in 2020 and marches to a different drummer.

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#18</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**assumption** · 2024 presidential · implied

The model's correlation structure appears to encode demographic dimensions such as northern white voters and Black voter share. Silver explains alternative maps as demographic-specific overperformance or underperformance by Trump.

> if he’s overperforming in the Blue Wall and lagging among African-Americans, he could lose Georgia while doing so, which has the largest Black voter share among the battleground states

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#19</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**model change** · 538 2012/2016 · explicit

The process for calculating state-by-state correlations was tightened up in 2016, or possibly 2012; Silver is unsure which.

> The process for calculating state-by-state correlations was tightened up, although maybe that was in 2012 now that I think about it.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#5</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**empirical regularity** · 2024 presidential · explicit

In the 2024 Silver Bulletin presidential model, the single most likely outcome was Trump sweeping all seven swing states, and the next-most likely was Harris sweeping all seven. This reflects strong correlation of errors between states in the simulations.

*Numbers:* swing states = 7 states (2024)

*Why:* Correlated polling error across states.

> Trump sweeping all seven closely contested swing states was the most likely outcome in our model

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#15</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**empirical regularity** · general principle · explicit

In 2024, polling bias was highly consistent across race types: D+2.9 in presidential, Senate and House polls, and D+1.8 in gubernatorial polls. This is consistent with declining ticket-splitting, which implies polling errors are correlated across offices in presidential years.

*Numbers:* pres/Senate/House bias 2024 = D+2.9 points; Governor bias 2024 = D+1.8 points

*Why:* Less ticket-splitting in presidential years.

> With less and less ticket-splitting in presidential years, that's what you'd expect.

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#19</sub>

### 2026-04-11 · [“AI polls” are fake polls](https://www.natesilver.net/p/ai-polls-are-fake-polls)
**method** · Silver Bulletin forecast · explicit

Silver describes the Silver Bulletin forecast as already doing a form of statistical inference for sparsely polled groups: it smooths noisy survey data using past voting patterns, national polls, and polls of other states.

> They essentially smooth out the kinks in noisy survey data by making inferences based on past voting patterns or national polls or surveys of other states.

<sub>2026-04-11_ai-polls-are-fake-polls-by-eli-mckown-dawson#3</sub>

### 2026-06-01 · [Should Democrats panic about Platner?](https://www.natesilver.net/p/should-democrats-panic-about-platner)
**method** · FLIPR 2026 · explicit

Maine is demographically and politically among the biggest outliers and least correlated with other states. In the model's logic, low correlation with other states makes a state's outcome more uncertain, because less can be inferred from the national picture than in a state like Pennsylvania.

> Demographically and politically, Maine is among the biggest outliers and the least correlated with other states

<sub>2026-06-01_should-democrats-panic-about-platner-by-nate-silver#7</sub>

### 2026-08-11 · [Everything is breaking Democrats’ way. Is it enough to win the Senate?](https://www.natesilver.net/p/everything-is-breaking-democrats-way)
**method** · FLIPR 2026 · explicit

Polling and forecasting errors are correlated across Senate races, but much less than across states in a presidential race where the same two candidates are on every ballot. Congressional races are also more correlated with one another in presidential years than in midterms, and FLIPR now accounts for this.

*Why:* 2018 and 2022 midterm maps were patchy and regionalized.

> congressional races are more correlated with one another in presidential years than in midterms, and FLIPR now accounts for this.

<sub>2026-08-11_everything-is-breaking-democrats-way-is-it-enough-to-win-the-senate#11</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**design principle** · FLIPR 2026 · explicit

FLIPR distinguishes 'micro' indicators that apply to one race (race polls, candidate fundraising) from 'macro' indicators that affect all races (generic ballot, polarization). Races cannot be forecast independently and then simulated, because outcomes are correlated, as in 2016 when Republicans beat their polls across the board.

*Why:* Systematic error versus independent race variance.

> You can’t just forecast each race individually and apply some sort of Monte Carlo simulation on top because race outcomes are somewhat correlated.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#6</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

CANTOR (Congressional Algorithm using Neighboring Typologies to Optimize Regression) computes pairwise similarity scores among all 485 units, 435 districts plus 50 states. It uses political traits (partisan lean), demographics (race, religion, education) and geography (region with Silver's own definitions and some split states, distance, urbanization). It then imputes polling-like estimates for unpolled races from how polls in similar places over- or under-perform their baselines.

*Numbers:* CANTOR units = 485 states+districts (485 x 484 pairwise comparisons)

*Why:* Overperformance tends to cluster in similar places.

> it calculates similarity scores between any given combination of states or districts

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#18</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**model change** · FLIPR 2026 · explicit

For 2026, CANTOR accounts for a wider array of demographics, notably separating religious groups such as Jewish and Muslim voters that were previously lumped with others.

> A wider array of demographics are now accounted for by CANTOR, particularly including religious groups

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#19</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

Classic uses a small weight on CANTOR's imputed polling proxies, because CANTOR is generally less accurate than either fundamentals or actual race polls.

> While CANTOR is a cool system, it’s generally less accurate than either fundamentals or polls directly from the state or district.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#26</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**model change** · FLIPR 2026 · explicit

FLIPR now assumes congressional and gubernatorial races are slightly more correlated with one another in presidential years than in midterms, because the presidential race anchors everything.

> The model now assumes that races are slightly more correlated with one another in presidential years than they are in midterms.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#37</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**interpretation guidance** · FLIPR 2026 · explicit

Contradictory polls across Senate races, such as Brown +8 in Ohio and El-Sayed -4 in bluer Michigan, are plausible because congressional outcomes are correlated much less than presidential ones. The advanced FLIPR versions still expect such divergences to narrow toward fundamentals over the coming months.

> Outcomes in congressional races are correlated with one another, although considerably less so than in presidential races.

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#15</sub>

### 2026-08-22 · [A tour of the 48 key House races](https://www.natesilver.net/p/a-tour-of-the-48-key-house-races)
**method** · FLIPR 2026 · explicit

FLIPR uses its own long-standing regional definitions (Northeast, South, Midwest, West) rather than Census regions. Some states are split between regions; for example some southeastern Florida districts count as 'Northeastern' because the Miami area resembles a Northeastern metro, and parts of Texas count as West.

*Why:* Regions feed correlated error and similarity.

> we’ve traditionally considered a few districts in southeastern Florida to be “Northeastern” rather than “Southern”

<sub>2026-08-22_a-tour-of-the-48-key-house-races#6</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**limitation or failure mode** · FLIPR 2026 · explicit

FLIPR does not use its Senate forecast in a state to predict the governor forecast in the same state, though Silver Bulletin suspects coattails, such as Bottoms sharing the ballot with Ossoff, may have predictive power as ticket-splitting declines, and may examine this in 2028.

> FLIPR doesn’t use its Senate forecasts to predict its governor forecasts

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#7</sub>

### 2026-09-03 · [Beware big swings in midterm forecasts](https://www.natesilver.net/p/beware-big-swings-in-midterm-forecasts)
**empirical regularity** · FLIPR vs presidential model · explicit

In presidential years, swing-state polls can be used reliably to infer the national trend, since the same candidates appear everywhere. For congressional races, shifts in one race often reflect local news or an ad barrage and do not extrapolate well; a new Senate poll in one state mostly affects only that state.

> A new poll in Michigan or Maine or South Carolina or Alaska pretty much affects that state and that state only.

<sub>2026-09-03_beware-big-swings-in-midterm-forecasts#7</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**empirical regularity** · FiveThirtyEight 2016 / general · explicit

Treating state polling errors as independent coin flips is the key modeling mistake: because FiveThirtyEight modeled correlation, it gave Trump 29 percent in 2016 while coin-flip models gave him 1 percent or less. Correlation matters most among demographically similar states; in 2016, a miss with non-college whites concentrated in Midwestern swing states decided the race while national polls were fairly accurate.

*Numbers:* FiveThirtyEight 2016 Trump probability = 29 percent (final forecast); coin-flip models' Trump probability = 1 percent or less percent (2016)

> Precisely because it didn’t do this, FiveThirtyEight’s final forecast gave Trump a 29 percent chance in 2016

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#6</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**empirical regularity** · FLIPR 2026 · explicit

Error correlation lies on a spectrum: presidential years are near uniform national swing; congressional races in presidential years are in between, with coattails and party-line voting; midterms are in the middle; off-year, runoff and special elections are near independent coin flips and produce many surprises, such as Scott Brown in 2010 and Doug Jones in 2017. Many 2026 FLIPR changes sharpened the presidential-year versus midterm distinction.

> Presidential years are very much on the “uniform swing” side of that spectrum whereas midterms are somewhere in the middle.

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#8</sub>

### 2026-10-15 · [Welcome to midterm silly season 🤡](https://www.natesilver.net/p/welcome-to-midterm-silly-season)
**interpretation guidance** · FLIPR 2026 · explicit

How much polling error a party can absorb depends on where the error is located: in 2026 Democrats had less tolerance for an adverse error in the Midwest for the Senate.

> Most importantly, Democrats have less tolerance for a polling error working against them in the Midwest.

<sub>2026-10-15_republicans-are-spending-big-its-not-working#5</sub>

### 2026-10-17 · [The good, bad and ugly outcomes in the Senate](https://www.natesilver.net/p/the-good-bad-and-ugly-outcomes-in)
**method** · FLIPR 2026 · explicit

FLIPR simulates regional and demographic polling errors without privileging any one, considering Midwestern underperformance by Democrats, as in 2016, alongside Southern underperformance, Hispanic overperformance, Midwestern overperformance and others. Even with national error held near zero, Senate win probabilities stay uncertain, for example Texas only rising from 71.5 to 76.0 percent for Talarico.

*Numbers:* Talarico win prob default vs modest-error = 71.5 / 76.0 percent (Oct 17, 2026)

*Why:* Congressional races are correlated but less than presidential ones.

> FLIPR does consider exactly this scenario, although it doesn’t privilege it.

<sub>2026-10-17_the-good-bad-and-ugly-outcomes-in-the-senate#4</sub>

### 2026-10-20 · [My pet peeve about the polling error debate](https://www.natesilver.net/p/my-pet-peeve-about-the-polling-error)
**parameter or number** · FLIPR 2026 · explicit

Benchmarking FLIPR's correlation structure: a Monte Carlo treating each Senate race as independent using Deluxe race probabilities gives Democrats 91 percent to win the Senate. Assuming perfect correlation gives the tipping-point state's probability, 72 percent in Texas. FLIPR Deluxe's 76 percent is much closer to perfect correlation than to independence.

*Numbers:* independent-races Senate D prob = 91 percent (Oct 20, 2026); perfectly correlated Senate D prob = 72 percent (= Texas tipping point); FLIPR Deluxe Senate D prob = 76 percent (Oct 20, 2026)

*Why:* Accounts for both national and regional correlated errors.

> So FLIPR Deluxe’s current 76 percent odds for Democrats are closer to the perfectly correlated scenario (72 percent) than the perfectly independent one (91 percent).

<sub>2026-10-20_my-pet-peeve-about-the-polling-error-debate#0</sub>

### 2026-10-23 · [Do these Senate-governor splits make sense?](https://www.natesilver.net/p/do-these-senate-governor-splits-make)
**parameter or number** · FLIPR 2026 · explicit

In midterms from 1998 to 2022, in states with both a Senate and governor race and at least one qualifying poll in the final three weeks, either both Democrats or both Republicans beat their polls in 68 percent of cases. FLIPR models this with a statewide error draw in each simulation affecting House, Senate and governor races in the state.

*Numbers:* same-direction poll error rate, Senate vs governor = 68 percent (midterms 1998-2022)

> In 68 percent of these cases, either the two Democrats or the two Republicans overperformed their polls in both contests.

<sub>2026-10-23_do-these-senate-governor-splits-make-sense#0</sub>

### 2026-10-23 · [Do these Senate-governor splits make sense?](https://www.natesilver.net/p/do-these-senate-governor-splits-make)
**empirical regularity** · Silver Bulletin analysis · explicit

Projected Senate-governor ticket splits do not narrow on Election Day: across midterms from 1998 to 2022 the average split projected by final polls was 17.3 points and the actual split 17.5, with the split larger than projected in 53 percent of cases. Regression shows adding Senate polling to governor polling, or vice versa, adds no meaningful predictive power for the final outcome.

*Numbers:* average projected split = 17.3 points (midterms 1998-2022); average actual split = 17.5 points (midterms 1998-2022); share with larger split than projected = 53 percent (midterms 1998-2022)

> What’s not true, though, is that ticket splits get narrower on Election Day.

<sub>2026-10-23_do-these-senate-governor-splits-make-sense#1</sub>

### 2026-10-25 · [Let’s talk shop about every Senate race](https://www.natesilver.net/p/lets-talk-shop-about-every-senate)
**empirical regularity** · FLIPR 2026 · explicit

Alaska and Maine are among the states least correlated with national outcomes, so a party can win them on a bad night or lose them on a good one.

> Alaska, up in the Arctic Circle, is one of the least correlated states with the Lower 48.

<sub>2026-10-25_lets-talk-shop-about-every-senate-race-by-nate-silver#12</sub>

### 2026-11-01 · [13 maps for the morning after the midterms](https://www.natesilver.net/p/13-morning-after-the-midterm-maps)
**method** · FLIPR 2026 · explicit

Senate and gubernatorial races within a state are deliberately correlated in FLIPR's simulations, so a strong Senate candidate's overperformance tends to pull the same party's governor candidate along in that simulation.

> Note also that Senate and gubernatorial races are deliberately correlated in FLIPR

<sub>2026-11-01_13-maps-for-the-morning-after-the-midterms-by-nate-silver#1</sub>

### 2026-11-01 · [13 maps for the morning after the midterms](https://www.natesilver.net/p/13-morning-after-the-midterm-maps)
**empirical regularity** · FLIPR 2026 · explicit

Conditional on a low-probability headline outcome, such as Republicans holding the House, FLIPR's simulations are typically disasters for the same party across the board and rank around the 95th upset percentile, reflecting correlated national error.

> conditional upon Republicans holding the House, everything else is likely to be a disaster for Democrats, too.

<sub>2026-11-01_13-maps-for-the-morning-after-the-midterms-by-nate-silver#2</sub>

### 2026-11-03 · [It's Judgment Day for Trump (and for pollsters)](https://www.natesilver.net/p/its-judgment-day-for-trump-and-for)
**parameter or number** · FLIPR 2026 · explicit

In the final FLIPR Deluxe forecast, treating race outcomes as independent would have given Republicans just a 5 percent chance of holding the Senate; with nationally and regionally correlated errors it was 18 percent.

*Numbers:* R Senate odds if independent = 5 percent (final forecast); R Senate odds, FLIPR = 18 percent (final forecast)

> If you were to treat FLIPR Deluxe simulations as a simple Monte Carlo simulation, where the outcome in each race was independent, then Republicans’ winning odds would be just 5 percent.

<sub>2026-11-03_its-judgment-day-for-trump-and-for-pollsters#1</sub>
