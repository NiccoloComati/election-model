# Simulation and aggregation

103 findings from 45 articles, oldest first.

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**method** · FiveThirtyEight 2016 presidential · explicit

The national popular vote is projected from a blend of top-down (national polls) and bottom-up (state polls controlled for PVI) estimates, with considerably more weight on bottom-up, which has been more accurate. It is held constant when demographic regressions are applied, which are recalibrated so they only redistribute the vote across states.

*Why:* Regressions should create a realistic distribution, not shift the national total.

> The model uses a blend of both approaches but puts considerably more weight on the state polls strategy, which has been more accurate historically.

<sub>fte_2016-general-election-forecast-users-guide#12</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**parameter or number** · FiveThirtyEight 2016 presidential · explicit

National, regional and state-specific errors are drawn from a t-distribution with 10 degrees of freedom, which turns normal-distribution odds of 50-to-1 into about 30-to-1 and 1,000-to-1 into about 180-to-1. It is used because only 11 elections from 1972 to 2012 inform the tails.

*Numbers:* t-distribution degrees of freedom = 10 df (2016)

*Why:* Small sample of elections; conservative tail assumptions.

> Specifically, they’re drawn from a t -distribution (with 10 degrees of freedom).

<sub>fte_2016-general-election-forecast-users-guide#22</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**method** · FiveThirtyEight 2016 presidential · explicit

In 2016 the model ran at least 20,000 simulations per version per day, so changes under one percentage point may be simulation noise. Maine and Nebraska were simulated by congressional district. An Electoral College deadlock was assigned to Trump half the time, since Republicans controlled most House delegations, and to the popular-vote winner the other half.

*Numbers:* daily simulations per version = at least 20,000 simulations (2016)

> If no candidate receives a majority of electoral votes, the model assigns the election to Trump half the time

<sub>fte_2016-general-election-forecast-users-guide#23</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**method** · FiveThirtyEight 2016 presidential · explicit

Tipping-point chance: in each simulation where the popular vote is close enough for the Electoral College to matter, states are sorted by margin and electoral votes accumulated until one candidate reaches 270; that state is the tipping point, shared in a 269-269 tie. Voter Power Index is each state's tipping-point chance divided by its share of national turnout; for example, a VPI of 3.5 means a vote there is 3.5 times as powerful as the national average.

> Tipping-point chance is the probability that a state will provide the decisive vote in the Electoral College.

<sub>fte_2016-general-election-forecast-users-guide#25</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

In each of 40,000 simulations per update, the model first draws national drift and national Election Day error and applies them roughly uniformly across states, scaled by elasticity. It then draws correlated state errors as random permutations over demographic and geographic variables, and finally residual state-specific error.

*Numbers:* simulations = 40,000 simulations (each update)

> the model first picks two random numbers to reflect national drift (how much the national forecast could change) and national Election Day error

<sub>fte_2020-presidential-forecast-methodology#25</sub>

### 2024-04-17 · [Announcing 2024 election model plans](https://www.natesilver.net/p/announcing-2024-election-model-plans)
**method** · 2024 presidential · explicit

The 2024 model produces probabilistic forecasts for every state and for the Electoral College.

> probabilistic forecasts of every state and the Electoral College

<sub>2024-04-17_announcing-2024-election-model-plans-by-nate-silver#3</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**method** · 2024 presidential · explicit

RFK Jr.'s ballot access is probabilistic in the 2024 model. States the Kennedy campaign says it has qualified for are taken at its word, except New York, where a Democratic lawsuit is reported to be credible. In unqualified states, qualification probability is estimated from the ratio of required signatures to the voting-eligible population. Each simulation draws a random number to decide eligibility in ambiguous states.

*Why:* He has a well-funded ballot access campaign, so the model errs toward assuming inclusion.

> based on the ratio of signatures required to the voting-eligible population

<sub>2024-06-26_2024-presidential-election-model-methodology-update#15</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**parameter or number** · 2024 presidential · explicit

Conditional on winning Wisconsin, Michigan and Pennsylvania, Biden wins the Electoral College about 97% of the time in simulations. The remaining risk comes from states such as NH, VA, NM, MN and NE-2.

*Numbers:* P(Biden EC win | wins MI, WI, PA) = about 97 percent (June 26, 2024)

> conditional on winning Wisconsin and Michigan and Pennsylvania, Biden wins the Electoral College about 97 percent of the time

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#27</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**parameter or number** · 2024 presidential · explicit

Biden winning exactly 270 electoral votes (Trump 268) is among the modal outcomes of the model's electoral vote distribution, yet occurs only 3-4% of the time.

*Numbers:* P(Biden exactly 270) = 3 to 4 percent (June 2024)

> there’s still only a 3 to 4 percent chance of it occurring, according to the forecast

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#28</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**parameter or number** · 2024 presidential · inferred_from_chart

The 2024 model runs 40,000 simulations. Launch outputs: Biden 33.7% EC, 51.0% popular vote, 250.4 expected EV, 47.2% vote share. Trump 65.7% EC, 49.0% popular vote, 287.2 EV, 47.1% vote share. Kennedy 0.0% EC, 0.4 EV, 4.3% vote share. No majority 0.5%.

*Numbers:* simulations = 40,000 simulations (2024 model); Trump EC probability = 65.7 percent (June 26, 2024); Biden EC probability = 33.7 percent (June 26, 2024); No majority = 0.5 percent (June 26, 2024); Biden popular vote win probability = 51.0 percent (June 26, 2024); Biden expected EV = 250.4 electoral votes (June 26, 2024); Trump expected EV = 287.2 electoral votes (June 26, 2024); Kennedy expected EV = 0.4 electoral votes (June 26, 2024); Kennedy projected vote share = 4.3 percent (June 26, 2024)

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#29</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**method** · 2024 presidential · explicit

Each simulation draws a national random draw plus a state-level random draw for each candidate, including third-party candidates. Third-party outcomes are partly correlated across states. A trailing third-party candidate wins a state only when both draws are favorable and the major-party race there is close; for example, RFK at 20% nationally could win Maine with 35%.

*Numbers:* example national RFK share = 20 percent (illustrative tail scenario); example winning state share = 35 percent (Maine, illustrative)

> he needs both his national random draw and his state random draw to come up perfectly for him

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#25</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**limitation or failure mode** · 538 2024 (Morris) · explicit

With very wide uncertainty, tipping-point probabilities default toward states with many electoral votes. 538 ranked Texas (40 EVs) as the 3rd-most-likely tipping-point state at 9.8 percent, ahead of Michigan (9.1 percent) and Wisconsin (6.6 percent).

*Numbers:* 538 Texas tipping-point chance = 9.8 % (July 2024); 538 PA tipping-point chance = 12.0 % (July 2024); 538 GA tipping-point chance = 10.4 % (July 2024); 538 FL tipping-point chance = 9.3 % (July 2024); 538 MI tipping-point chance = 9.1 % (July 2024); 538 NC tipping-point chance = 9.1 % (July 2024); 538 WI tipping-point chance = 6.6 % (July 2024); 538 AZ tipping-point chance = 6.4 % (July 2024); Texas electoral votes = 40 electoral votes (2024)

*Why:* Electoral vote counts are known exactly, while the polling is uncertain.

> we know exactly how many electoral votes Texas has (40) while the polling is more uncertain

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#20</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**parameter or number** · 2024 presidential · explicit

The Silver Bulletin presidential model runs 40,000 simulations per forecast run (for example, the July 10, 2024 Biden-Trump run).

*Numbers:* simulations = 40,000 simulations (July 10, 2024 run)

> I pulled up the 40,000 simulations we ran on July 10

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#10</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**method** · 2024 presidential · explicit

The value of a VP home-state bonus can be estimated from saved model simulations. Count the simulations where (a) the candidate lost the state by no more than the bonus and (b) the state's electoral votes would be pivotal. For Pennsylvania this means Biden had 251-269 electoral votes, so adding PA's 19 gets him to 270+. Both conditions are required.

*Numbers:* pivotal EV range = 251-269 electoral votes (Biden EV without PA); winning threshold = 270 electoral votes (Electoral College)

*Why:* Being decisive in the state is not enough; the state must also be decisive in the Electoral College.

> we're looking for simulations where Biden lost Pennsylvania by 0.4 points or less and Biden had between 251 and 269 electoral votes

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#11</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**parameter or number** · 2024 presidential (Biden version) · explicit

In the July 10, 2024 Biden-Trump run, Biden lost Pennsylvania by 0.4 points or less in 1,915 of 40,000 simulations (about 5%). He also had 251-269 electoral votes in 427 of those simulations (about 1%). A PA VP's home-state bonus therefore adds roughly 1 percentage point to Electoral College win probability.

*Numbers:* sims losing PA by ≤0.4 = 1915 simulations (of 40,000; about 5 percent); sims where PA bonus is decisive = 427 simulations (of 40,000; about 1 percent); EC win probability gain from PA VP = about 1 percentage point (Biden-Trump model)

> These conditions were satisfied in 427 of the 40K simulations, or about 1 percent of the time.

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#12</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**parameter or number** · 2024 presidential (Biden version) · explicit

In the Biden-Trump model, an Arizona VP would have raised Biden's Electoral College win probability by only 0.2 percentage points, about 1 lost simulation converted to a win in 500.

*Numbers:* EC win probability gain from AZ VP = 0.2 percentage points (Biden-Trump model)

> a VP from Arizona would have improved Biden's chances of winning the Electoral College by only 0.2 percentage points

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#13</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**parameter or number** · 2024 presidential · inferred_from_chart

The 2024 Silver Bulletin presidential model produces its probabilities from 40,000 simulations. Each simulation forecasts every state's vote share and tallies the electoral votes each candidate wins.

*Numbers:* number of simulations = 40,000 simulations (2024 presidential model, per forecast run)

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#7</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**parameter or number** · 2024 presidential · inferred_from_chart

Final Biden-Trump forecast (July 21, 2024): Trump 72.8% and Biden 26.9% to win the Electoral College. Predicted electoral votes were Trump 298.2 and Biden 239.5. Trump's popular-vote win probability was 57.3%.

*Numbers:* Trump EC probability = 72.8% probability (July 21, 2024); Biden EC probability = 26.9% probability; Trump predicted EV = 298.2 electoral votes; Biden predicted EV = 239.5 electoral votes

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#23</sub>

### 2024-07-29 · [kamala_mode will be activated tomorrow](https://www.natesilver.net/p/kamala_mode-will-be-activated-tomorrow)
**parameter or number** · 2024 presidential · inferred_from_chart

The code screenshot shows that the Silver Bulletin 2024 presidential model runs 40,000 simulations (scalar howmanysims=40000).

*Numbers:* howmanysims = 40000 simulations (2024 presidential model code, July 2024)

<sub>2024-07-29_kamala-mode-will-be-activated-tomorrow-by-nate-silver#8</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**parameter or number** · 2024 presidential · explicit

In its final step, after adjustments that turn polling averages into Election Day predictions, the Silver Bulletin 2024 presidential model simulates 40,000 election outcomes. These simulations produce the national and state topline predictions.

*Numbers:* number of simulations = 40,000 simulations (each model run, 2024 presidential)

> we simulate 40,000 election outcomes. These simulations give us our topline predictions nationally and in each state

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#0</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**method** · 2024 presidential · explicit

Conditional probabilities in the Silver Bulletin 2024 presidential model are computed empirically from the simulations. Among all simulations where a candidate wins a given state, the model counts the share in which that candidate also wins the Electoral College. For example, Harris won Pennsylvania in 22,448 of 40,000 simulations and the Electoral College in 20,539 of those, giving 91.5%.

*Numbers:* Harris PA wins = 22,448 simulations (Aug 8, 2024 run; about 56%); Harris EC wins given PA win = 20,539 simulations (Aug 8, 2024 run); Harris P(win EC | win PA) = 91.5 percent (Aug 8, 2024); Trump PA wins = 17,552 simulations (Aug 8, 2024 run)

> We just look at all of the simulations where a candidate wins a certain state, and check how often that candidate won the Electoral College in that set of simulations.

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#1</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**method** · 2024 presidential · explicit

The same counting approach extends to conditioning on several states at once. In the Aug 8, 2024 run, Harris wins the election 95% of the time when she wins both Pennsylvania and Wisconsin, and loses only 2% of the time when she wins all three Blue Wall states (PA, WI, MI).

*Numbers:* P(Harris wins | PA and WI) = 95 percent (Aug 8, 2024); P(Harris loses | wins PA, WI, MI) = 2 percent (Aug 8, 2024)

> We can even extend this logic to get conditional predictions for multiple states.

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#2</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**method** · 2024 presidential · explicit

Ballot access for an N3PC is simulated probabilistically in the Silver Bulletin presidential model. In states where RFK's ballot status was uncertain, he randomly appeared on the ballot in some simulations but not others. Where he was off the ballot, his votes were reallocated to the major-party candidates.

> he'd randomly make the ballot in some simulations but not others

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#12</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**method** · 2024 presidential · explicit

The Silver Bulletin forecast of the national popular vote is not based directly on national polls. It is the sum of state-level projections weighted by projected turnout in each state. National polls affect it only indirectly through adjustments such as the trendline adjustment.

> we project the results in each state, and then sum up these estimates, weighted by the projected turnout in each state, to come up with a national number

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#19</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**parameter or number** · 2024 presidential · explicit

As of Sept. 6, 2024, the Silver Bulletin model gives 88% probability that one of seven states (PA, MI, GA, NC, WI, AZ, NV) is the tipping-point state. Nevada, with 6 electoral votes, has only 3% tipping-point probability.

*Numbers:* combined tipping-point probability of 7 battlegrounds = 88 percent (Sept. 6, 2024); Nevada tipping-point probability = 3 percent (Sept. 6, 2024)

> Collectively, there’s an 88 percent chance that one of these states determines the winner, the model calculates.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#14</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**parameter or number** · 2024 presidential · inferred_from_chart

Silver Bulletin simulation results, conditional on Harris's national popular vote margin bucket (Harris win prob / Harris mean EV) as of Sept. 6, 2024:

| Margin | Harris win prob | Harris mean EV |
|---|---|---|
| D+6–7 | 99.9% | 340.1 |
| D+5–6 | 98.8% | 322.5 |
| D+4–5 | 95.8% | 306.0 |
| D+3–4 | 84.8% | 288.9 |
| D+2–3 | 56.3% | 271.9 |
| D+1–2 | 26.3% | 256.0 |
| D+0–1 | 7.7% | 241.8 |
| R+0–1 | 1.9% | 231.6 |
| R+1–2 | 0.4% | 223.7 |
| R+2–3 | 0.0% | 216.0 |
| R+6–7 | 0.0% | 183.5 |

The electoral-vote response is roughly 15–18 EV per point near the center of the distribution.

*Numbers:* Harris win prob at D+2 to +3 = 56.3 percent (Sept. 6, 2024); Harris win prob at D+3 to +4 = 84.8 percent; Harris win prob at D+0 to +1 = 7.7 percent; Harris EV at D+2 to +3 = 271.9 electoral votes

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#15</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**method** · 2024 presidential · inferred_from_chart

In some Silver Bulletin simulations, neither candidate wins an Electoral College majority (e.g. a 269-269 tie). As a result, conditional Harris and Trump win probabilities may not sum to 100%.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#16</sub>

### 2024-09-07 · [Oops! I made the convention bounce adjustment disappear.](https://www.natesilver.net/p/oops-i-made-the-convention-bounce)
**empirical regularity** · 2024 presidential · explicit

Without the bounce adjustment, the 2024 model projected Harris at an average of 277 electoral votes to Trump's 261. Because she loses many simulated outcomes narrowly, however, the median outcome was roughly an Electoral College tie. This shows that the mean and median of the simulated EV distribution can diverge.

*Numbers:* Harris mean EV (no adjustment) = 277 electoral votes (Sept 2024); Trump mean EV (no adjustment) = 261 electoral votes (Sept 2024)

*Why:* Harris has narrow leads in the Blue Wall states and lose-by-a-little combinatorics.

> it also has her losing a lot of elections in agonizingly close fashion — so the median rather than the average outcome is basically an Electoral College tie.

<sub>2024-09-07_oops-i-made-the-convention-bounce-adjustment-disappear#3</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**parameter or number** · 2024 presidential · inferred_from_chart

The 2024 Silver Bulletin presidential model runs 40,000 simulations. In each one it forecasts which states each candidate wins and tallies electoral votes, producing a distribution of electoral vote outcomes for each candidate.

*Numbers:* number of simulations = 40,000 simulations (electoral vote distribution chart, Sept. 17, 2024 run)

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#0</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**empirical regularity** · 2024 presidential · explicit

In the 2024 Silver Bulletin model's simulations, Harris has many more blowout outcomes, near 400 electoral votes, than Trump does. These blowouts reflect either the election getting away from Trump or a big polling error in Harris's favor. Trump's distribution is more concentrated just above 270.

*Numbers:* Harris blowout EV level = close to 400 electoral votes (right tail of Harris EV distribution)

> Harris has far more outcomes where she wins in a blowout — close to 400 electoral votes.

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#3</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**empirical regularity** · 2024 presidential · inferred_from_chart

The Sept. 17, 2024 Silver Bulletin electoral vote histograms show Harris's most frequent single outcome at roughly 226 EVs, with smaller spikes near 319 and 400. Trump's most frequent outcome is roughly 312 EVs, and his distribution has a thinner right tail ending near 360.

*Numbers:* Harris modal EV outcome = ~226 electoral votes (read off chart, Sept. 17 2024); Trump modal EV outcome = ~312 electoral votes (read off chart, Sept. 17 2024)

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#4</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**empirical regularity** · 2024 presidential · explicit

In expected value terms, Harris gains about 4 electoral votes from Florida and about 3 from Texas in the 2024 Silver Bulletin model. These longshot states raise her mean EV count without much effect on her Electoral College win probability, which explains part of the gap between the mean and the win probability.

*Numbers:* Harris expected EVs from Florida = about 4 electoral votes (Sept. 2024 model); Harris expected EVs from Texas = 3 electoral votes (Sept. 2024 model)

> In expected value terms, Harris gains about 4 electoral votes from FL and 3 from TX.

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#6</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**parameter or number** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model ran 40,000 simulations for its September 21, 2024 forecast update.

*Numbers:* number of simulations = 40,000 simulations (model run on the morning of Sept 21, 2024)

> it came up 610 times (about 1.5 percent of cases) out of the 40,000 simulations we ran this morning

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#0</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**method** · 2024 presidential · explicit

The Silver Bulletin presidential model reports a tipping-point probability for each state. This is the share of simulations in which that state provides the decisive electoral vote. Values on Sept 21, 2024 were: Pennsylvania 32%, Wisconsin 16%, Michigan 14%, North Carolina 11%, Georgia 9%, Arizona 6%, Nevada 2%, Florida 2%, Texas 1%, and Minnesota, New Mexico and Virginia 0–1% each.

*Numbers:* PA tipping-point probability = 32 percent (Sept 21, 2024); WI tipping-point probability = 16 percent (Sept 21, 2024); MI tipping-point probability = 14 percent (Sept 21, 2024); NC tipping-point probability = 11 percent (Sept 21, 2024); GA tipping-point probability = 9 percent (Sept 21, 2024); AZ tipping-point probability = 6 percent (Sept 21, 2024); NV tipping-point probability = 2 percent (Sept 21, 2024); FL tipping-point probability = 2 percent (Sept 21, 2024); TX tipping-point probability = 1 percent (Sept 21, 2024); MN/NM/VA tipping-point probability = 0 to 1 percent (Sept 21, 2024)

> Pennsylvania: Harris win probability 57%. Tipping-point probability 32%.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#3</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**parameter or number** · 2024 presidential · explicit

The eight key states (seven swing states plus Florida) together held a 92% probability of containing the tipping-point state in the Sept 21, 2024 model run.

*Numbers:* probability tipping point is one of 8 key states = 92 percent (Sept 21, 2024)

> Although there's a 92 percent chance that one of these eight states is the tipping point, there are occasional cases where other states matter.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#4</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**parameter or number** · 2024 presidential · explicit

Harris win probabilities by state in the Sept 21, 2024 Silver Bulletin model run were: Michigan 63%, Pennsylvania 57%, Wisconsin 56%, Nevada 53%, North Carolina 39%, Georgia 36%, Arizona 36% and Florida 17%.

*Numbers:* MI Harris win prob = 63 percent (Sept 21, 2024); PA Harris win prob = 57 percent (Sept 21, 2024); WI Harris win prob = 56 percent (Sept 21, 2024); NV Harris win prob = 53 percent (Sept 21, 2024); NC Harris win prob = 39 percent (Sept 21, 2024); GA Harris win prob = 36 percent (Sept 21, 2024); AZ Harris win prob = 36 percent (Sept 21, 2024); FL Harris win prob = 17 percent (Sept 21, 2024)

> Michigan: Harris win probability 63%. Tipping-point probability 14%.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#5</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**parameter or number** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model ran 40,000 simulations in its run on the morning of September 23, 2024.

*Numbers:* number of simulations = 40,000 simulations (model run on Monday morning, Sep 23, 2024)

> Out of the 40,000 simulations we ran on Monday morning

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#0</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**parameter or number** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model runs 40,000 simulations per forecast update.

*Numbers:* number of simulations = 40,000 simulations (Sept 26, 2024 forecast run)

> we ended up with 102 simulations (out of 40,000) in which Harris did win the Electoral College but lost the popular vote

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#0</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**method** · 2024 presidential (also earlier Silver models) · explicit

The Silver Bulletin presidential model's national popular vote forecast is not based directly on national polls. It is the sum of projected results in 56 contests: 50 states, DC, Nebraska's three congressional districts and Maine's two. National polls play only an indirect role, such as helping infer results in sparsely polled states.

*Numbers:* contests projected = 56 contests (50 states + DC + 3 NE CDs + 2 ME CDs)

*Why:* This bottom-up method is sometimes more accurate than national polls alone.

> our popular vote forecast isn’t actually based on national polls. Rather, it’s based on summing up the results from the 56 contests the model projects

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#1</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**empirical regularity** · 2024 presidential · explicit

Of the 102 simulations in which Harris won the Electoral College but lost the popular vote, Harris won MI in 90%, PA in 88%, WI in 81% and NE-2 in 82%. She won NC in 31%, GA in 21% and AZ in 3%, averaging 277 electoral votes. A few of these were extreme-tail outcomes.

*Numbers:* split sims = 102 simulations (out of 40,000); MI win share = 90 percent (within split sims); PA win share = 88 percent (within split sims); WI win share = 81 percent (within split sims); NE2 win share = 82 percent (within split sims); NC win share = 31 percent (within split sims); GA win share = 21 percent (within split sims); AZ win share = 3 percent (within split sims); average EV = 277 electoral votes (Harris in split sims)

> Harris won Michigan in 90 percent of these simulations

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#13</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**method** · 2024 presidential · inferred_from_chart

Some simulations produce no Electoral College majority for either candidate (e.g., 269-269 ties), so win probabilities do not always sum to 100%.

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#17</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**parameter or number** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model typically runs 40,000 simulations per model run. For the Sept. 29, 2024 run it was raised to 70,000 to get a larger sample for this analysis.

*Numbers:* typical simulations = 40,000 simulations (standard model run, 2024); special run simulations = 70,000 simulations (Sept. 29, 2024 run for this column)

*Why:* A larger sample size gives better counts of rare swing-state combinations.

> Typically, we run 40,000 simulations, but I upped it to 70K today to get a larger sample size for this column.

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#0</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**method** · 2024 presidential · explicit

The model's simulation outputs can be tabulated by the 128 (2^7) win/loss combinations of the seven swing states (MI, PA, WI, GA, NC, AZ, NV). Florida is excluded from the swing-state set for this purpose.

*Numbers:* swing-state combinations = 128 combinations (2^7 permutations of seven swing states)

> The seven major swing states — for purposes of this column, I won’t get cute and count Florida as one — produce a total of 128 possible combinations (2 to the 7th power).

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#1</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**empirical regularity** · 2024 presidential · explicit

For the 270-268 Rust Belt-only Harris map (PA/MI/WI D, other swing states R), the default Harris EV is 270, but she wins only 86% of these simulations. In about 14% she loses somewhere outside the seven states (NE-2, NH, NM). The model sees NH and NM as more likely spoilers than NE-2 because Harris leads NE-2 polls by a wide margin.

*Numbers:* default Harris EV = 270 electoral votes (Rust Belt map without NV); Harris EC win share = 86 percent (conditional on that map (table)); tripped-up share = about 14 percent (same); map frequency = 1,504 of 70,000 (9th-most likely map)

*Why:* Winning with exactly 270 leaves no margin for error.

> the Rust Belt map without Nevada “should” be a win for Harris, but about 14 percent of the time, she gets tripped up somewhere

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#7</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**empirical regularity** · 2024 presidential · explicit

In the model's simulations, knowing the outcome of the seven core battleground states predicts the Electoral College winner 99% of the time. Other states such as Alaska matter only in edge cases.

*Numbers:* EC winner predictability = 99 percent (given seven swing state outcomes)

> if you know the outcome in the seven core battleground states, you can predict the Electoral College winner 99 percent of the time.

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#9</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**method** · 2024 presidential · explicit

The path table reports two figures per swing-state combination. 'Default Harris EV' assumes every non-swing state goes as expected. A simulated Harris EC win probability is drawn from the simulations matching that combination.

> how many electoral votes she’d win if every state apart from the seven swing states goes as expected — and a probabilistic projection of her chances as drawn from our simulations.

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#10</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**empirical regularity** · 2024 presidential · explicit

The most likely map in which Harris loses at least two Rust Belt states but still wins (Harris wins MI, GA, NC; loses PA, WI, AZ, NV; default 273 EV) occurred in 167 of 70,000 simulations. Harris won the EC in only 58% of those simulations because of risks such as NH (which would produce a 269-269 tie) and MN.

*Numbers:* map frequency = 167 of 70,000 simulations (Scenario 5 map); default Harris EV = 273 electoral votes (map shown); Harris EC win rate = 58 percent (conditional on that map)

*Why:* This map is consistent with polls underestimating Harris among Black voters but overestimating her with white and Hispanic voters, which correlates with NH and MN.

> this is only a winning map for Harris 58 percent of the time, because other states potentially get in the way.

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#11</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**empirical regularity** · 2024 presidential · inferred_from_chart

Other top maps from the Sept. 29 run, as listed in the table:
- 3rd: Harris wins all but AZ (3,146; 306 EV; 100%).
- 4th: Rust Belt + NV (2,769; 276 EV; 99%).
- 5th: Trump wins all but NV (2,765; 232 EV; 0%).
- 6th: Harris wins all but GA (2,701; 302 EV).
- 7th: Harris wins Rust Belt + AZ + NV (2,103; 287 EV).
- 8th: Harris wins Rust Belt + NC + NV (1,641; 291 EV).
- 10th: Harris wins Rust Belt + GA + NC (1,287; 300 EV).
- 11th: Harris wins only WI (1,276; 236 EV).
- 12th: Harris wins only MI (1,228; 241 EV).

*Numbers:* all but AZ = 3,146 of 70,000 (3rd most likely); Rust Belt + NV = 2,769 of 70,000 (4th most likely, 276 EV, 99% Harris); Trump all but NV = 2,765 of 70,000 (5th); all but GA = 2,701 of 70,000 (6th)

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#12</sub>

### 2024-10-08 · [55/45 is a really close race](https://www.natesilver.net/p/5545-is-a-really-close-race)
**parameter or number** · 2024 presidential · explicit

Averaged over all forecasts since the Silver Bulletin 2024 presidential model relaunched on July 30, 2024, Harris won 49.4% of simulations and Trump 50.2%. The remainder reflects 269-269 Electoral College ties, which the model simulates as a separate outcome.

*Numbers:* Harris average simulation win share = 49.4 percent (July 30 - Oct 7, 2024 average); Trump average simulation win share = 50.2 percent (July 30 - Oct 7, 2024 average); tie electoral votes = 269-269 electoral votes (tie outcome counted separately)

> Harris has won 49.4 percent of simulations, and Trump has won 50.2 percent. (These don't quite add up to 100 because of the slim possibility of a 269-269 Electoral College tie.)

<sub>2024-10-08_5545-is-a-really-close-race-by-nate-silver#2</sub>

### 2024-10-08 · [55/45 is a really close race](https://www.natesilver.net/p/5545-is-a-really-close-race)
**method** · 2024 presidential · inferred_from_chart

The Silver Bulletin 2024 model reports win probabilities that may not add to 100% because in some simulations neither candidate wins a majority of electoral votes.

<sub>2024-10-08_5545-is-a-really-close-race-by-nate-silver#9</sub>

### 2024-10-09 · [When you should panic about the polls](https://www.natesilver.net/p/when-you-should-panic-about-the-polls)
**method** · 2024 presidential · explicit

The Silver Bulletin forecast simulates many permutations of state outcomes and counts who comes up with more winning maps, given correlations between states and the uncertainties in the outlook.

> The model's job is to sort through these various permutations and see who comes up with more winning maps given the correlations in the data and uncertainties in the outlook.

<sub>2024-10-09_when-you-should-panic-about-the-polls-by-nate-silver#7</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**empirical regularity** · 2024 presidential · inferred_from_chart

Running the 2024 Silver Bulletin model with only high-quality nonpartisan polls shifted win probabilities slightly toward Trump in most states. Harris win probabilities, full model vs high-quality-only model:
- Electoral College: 50.2% vs 47.3% (Trump 49.5% vs 52.5%).
- Arizona: 33.7% vs 28.0%.
- Georgia: 39.2% vs 38.6%.
- Michigan: 57.4% vs 49.6%.
- Nevada: 56.8% vs 51.8%.
- North Carolina: 37.2% vs 37.1%.
- Pennsylvania: 53.2% vs 53.7%.
- Wisconsin: 53.3% vs 51.2%.

*Numbers:* Harris EC full = 50.2 percent (Oct 15 2024 rerun); Trump EC full = 49.5 percent (Oct 15 2024 rerun); Harris EC high quality = 47.3 percent (high-quality only); Trump EC high quality = 52.5 percent (high-quality only); Michigan Harris full/HQ = 57.4/49.6 percent; Arizona Harris full/HQ = 33.7/28.0 percent; Nevada Harris full/HQ = 56.8/51.8 percent; Pennsylvania Harris full/HQ = 53.2/53.7 percent; Wisconsin Harris full/HQ = 53.3/51.2 percent; Georgia Harris full/HQ = 39.2/38.6 percent; North Carolina Harris full/HQ = 37.2/37.1 percent

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#10</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**limitation or failure mode** · 2024 presidential · implied

The Electoral College win probabilities in the full Silver Bulletin model run (Harris 50.2%, Trump 49.5%) do not sum to 100%. The remaining roughly 0.3% is presumably no Electoral College majority, i.e., a 269-269 tie.

*Numbers:* residual = 0.3 percent (full model, Oct 15 2024)

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#11</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**empirical regularity** · 2024 presidential · explicit

A 0.4-point uniform swing toward Harris in the Oct 15, 2024 Silver Bulletin model would have Harris winning about 54% of Electoral College simulations, up from roughly 50%. This sensitivity estimate shows how much the near-tied Electoral College forecast moves per point of uniform swing.

*Numbers:* uniform swing = 0.4 percentage points (effect of excluding Rosenberg-listed polls); resulting Harris EC win share = about 54 percent of simulations (Oct 15 2024)

> A 0.4 point uniform swing toward Harris would result in her winning about 54 percent of Electoral College simulations.

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#13</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**parameter or number** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model reports an explicit probability of a 269-269 Electoral College tie, separate from each candidate's win probability. On Oct. 17, 2024 the figures were Trump 50.2%, Harris 49.5% and tie 0.3%.

*Numbers:* EC tie probability = 0.3 percent (Oct. 17, 2024); Harris EC win probability = 49.5 percent (Oct. 17, 2024)

> There’s also a 0.3 percent chance of a 269-269 Electoral College tie.

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#20</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**parameter or number** · 2024 presidential · explicit

The Silver Bulletin model computes tipping-point probabilities by state. On Oct. 17, 2024, the Blue Wall states (MI, WI, PA) had a combined 61% chance of being the tipping-point state, and North Carolina had surpassed Wisconsin in tipping-point odds.

*Numbers:* combined Blue Wall tipping-point probability = 61 percent (Oct. 17, 2024)

> the Blue Wall states have a combined 61 percent chance of being the tipping-point state

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#22</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**parameter or number** · 2024 presidential · explicit

In the Silver Bulletin simulations of October 22, 2024, the most common single outcome was Trump winning all 7 swing states (24%, or 24.4% in the table). The next most common was a Harris sweep of all 7 (15%, or 15.3% in the table).

*Numbers:* Trump sweep probability = 24.4 percent (simulations, Oct 22, 2024); Harris sweep probability = 15.3 percent (simulations, Oct 22, 2024)

> the most common outcome was Trump winning all 7 swing states: this happened 24 percent of the time. And the next most common was a Harris sweep, which occurred in 15 percent of simulations

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#2</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**parameter or number** · 2024 presidential · inferred_from_chart

The 'paths to victory' table is built from 40,000 simulations of the Silver Bulletin 2024 presidential model. It enumerates all 128 (2^7) win/loss permutations of the 7 likeliest tipping-point states, with each permutation's probability and Harris's Electoral College win probability in that scenario.

*Numbers:* simulations = 40,000 simulations (model run underlying the table, Oct 22, 2024); permutations = 128 scenarios (2^7 combinations of 7 tipping-point states)

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#3</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**method** · 2024 presidential · inferred_from_chart

In the paths-to-victory table, Harris is given a default number of electoral votes in each scenario. Each state other than the 7 tipping-point states is assigned to whichever candidate currently leads that state's forecast. Harris's win probability within a scenario can still fall between 0 and 100%, which suggests the probabilities are computed from simulations in which non-battleground states also vary.

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#4</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**parameter or number** · 2024 presidential · inferred_from_chart

Scenario rows from the October 22, 2024 table, listed as AZ, GA, MI, NC, NV, PA, WI: (1) R R R R D R R (only Nevada to Harris) 4.6%, 232 Harris EVs, 0.2% Harris win. (2) R D D D D D D 3.4%, 308 EVs, 100%. (3) R R D R D D D (Harris wins MI, NV, PA, WI) 2.9%, 276 EVs, 98.7%. (4) D R D D D D D 2.8%, 303 EVs, 100%. (5) D R D R D D D 2.6%, 287 EVs, 99.8%. (6) R R R R R R D 2.6%, 236 EVs, 0.0%. (7) R R D R R D D (Harris wins the Blue Wall only) 2.2%, 270 EVs, 85.4%. (8) R R D R R R R 1.9%, 241 EVs, 0.1%. (9) R D D D R D D 1.9%, 302 EVs, 99.6%. (10) R R D R R R D 1.9%, 251 EVs, 0.7%. (11) R R D R D R D 1.6%, 257 EVs, 1.6%. (12) R R D D D D D 1.6%, 292 EVs, 99.8%. (13) R D R R R R R 1.3%, 242 EVs, 0.6%. Harris's base is 226 EVs if she loses all 7 and 319 if she sweeps.

*Numbers:* Harris EVs with all 7 lost = 226 electoral votes (default allocation); Harris EVs with all 7 won = 319 electoral votes (default allocation); Blue Wall-only scenario probability = 2.2 percent (Harris wins MI, PA, WI only); Harris win probability in Blue Wall-only scenario = 85.4 percent (270 EVs at default allocation)

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#5</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**interpretation guidance** · 2024 presidential · inferred_from_chart

In the 270-EV Blue Wall-only scenario, Harris wins only 85.4% of the time rather than 100%. This implies the model also varies non-battleground states (e.g., NE-2, or other states) within simulations, and that ties or other-state flips matter.

*Numbers:* Harris win probability at 270 default EVs = 85.4 percent (scenario R R D R R D D)

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#6</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**interpretation guidance** · 2024 presidential · explicit

A Trump sweep of the 7 swing states is more likely than a Harris sweep in the simulations not because of any directional error assumption. Trump has clearer leads in Georgia and Arizona, which tilt toward him, while the other 5 states are basically toss-ups, so a Trump sweep is a slightly less heavy lift.

> he has clearer "leads" in Georgia and Arizona than Harris has in any state — the other 5 states are basically toss-ups

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#10</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**parameter or number** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model ran 40,000 simulations in its Friday-afternoon run of Nov 1, 2024.

*Numbers:* number of simulations = 40,000 simulations (Nov 1, 2024 model run)

> In only 1011 out of our 40,000 simulations on Friday afternoon, or about 2.5 percent, did all seven battleground states actually finish within 2.5 points.

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#0</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**parameter or number** · 2024 presidential · explicit

The 2024 Silver Bulletin presidential forecast runs 40,000 simulations per model run.

*Numbers:* Simulations = 40,000 simulations (Nov 2, 2024 run)

> In our 40,000 simulations tonight

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#13</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**empirical regularity** · 2024 presidential · explicit

In the 2024 Silver Bulletin simulations, scenarios where Iowa is decisive are rare. Examples: Harris loses Pennsylvania but wins Iowa plus North Carolina (273-265). Harris wins the Blue Wall plus Iowa but loses New Hampshire (271-267 rather than 267). Harris loses New Mexico, offset by Iowa (271-267). Weird far-tail maps also occur where polling is a disaster but the Electoral College lands near 269-269.

*Numbers:* PA electoral votes = 19 electoral votes; IA electoral votes = 6 electoral votes; Blue Wall without NH = 267 electoral votes (Harris total)

> The most plausible case probably involves North Carolina, but it's still quite rare in our simulations

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#16</sub>

### 2024-11-04 · [The polls are close, but that doesn’t mean the results will be](https://www.natesilver.net/p/the-polls-are-close-but-that-doesnt)
**method** · 2024 presidential · explicit

The Silver Bulletin presidential model's simulations include essentially three types of error. The first is a national error applied as a uniform swing. The second is state-specific error from states behaving idiosyncratically. The third is a series of demographic and geographic error terms, for example Trump overperforming in states with more Hispanics, or Harris overperforming in dense urban areas.

*Numbers:* Number of error types = 3 (simulation error structure)

*Why:* Polling error does not move the same way in every state; correlated demographic and regional errors matter.

> we calculate essentially three types of error: national error following a uniform swing, state-specific error based on individual states behaving idiosyncratically, and a series of demographic and geographic error terms

<sub>2024-11-03_the-polls-are-close-but-that-doesnt-mean-the-results-will-be#4</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**parameter or number** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model normally runs 40,000 simulations per forecast update. For the final Election Day forecast, it was decided in advance to run 80,000 simulations instead.

*Numbers:* usual simulation count = 40,000 simulations (standard model run, 2024); final run simulation count = 80,000 simulations (final forecast run at midnight on Election Day 2024)

*Why:* The race was expected to be extremely close, and more simulations reduce sampling error.

> We'd decided ahead of time to run 80,000 simulations instead of our usual 40K.

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#0</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**parameter or number** · 2024 presidential · explicit

In the final 2024 Silver Bulletin forecast, Harris won the Electoral College in 40,012 of 80,000 simulations (50.015%). Trump won 39,718, and the remaining simulations (about 270) were 269-269 ties with no majority.

*Numbers:* Harris EC wins = 40,012 simulations (final 2024 run); Harris win probability = 50.015 percent (final 2024 forecast); Trump EC wins = 39,718 simulations (final 2024 run); Trump plus no majority = 39,988 simulations (final 2024 run)

> Kamala Harris won the Electoral College in … 40,012 of them, or 50.015 percent. The remaining 39,988 were split between Trump (39,718) and no majority

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#1</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**limitation or failure mode** · 2024 presidential · explicit

Because the Silver Bulletin model is probabilistic (Monte Carlo) rather than deterministic, the reported win probability carries sampling error. The margin of error is about ±0.5 points of win probability at 40,000 simulations and about ±0.35 points at 80,000.

*Numbers:* MOE at 40,000 sims = ± 0.5 percentage points of win probability (Monte Carlo error); MOE at 80,000 sims = ± 0.35 percentage points of win probability (Monte Carlo error)

*Why:* A finite number of simulations produces sampling noise.

> there's a small amount of error introduced into the model because it's probabilistic rather than deterministic. The margin of error on 40,000 simulations is about ± 0.5 points

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#3</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**empirical regularity** · 2024 presidential · inferred_from_chart

A running tally of Harris's win probability over the final 80,000 simulations swung widely early on (roughly 48% to 52% within the first few thousand simulations). It then converged toward 50%, with Harris ahead 50.7%-49.3% after 18,000 simulations before Trump plus ties caught up. The final ordering was decided only around simulations #79,281-#79,603.

*Numbers:* Harris share after 18,000 sims = 50.7 percent (running tally, final 2024 run); Harris winning streak = 15 of 17 simulations (starting at simulation #79,281)

*Why:* This illustrates how noisy the simulation count is relative to a near-50/50 race.

> Harris jumped out to a huge early lead, ahead 50.7%-49.3% after the 18,000th simulation — but then Trump + no majority mounted a thrilling comeback.

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#4</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**parameter or number** · 2024 presidential · explicit

The final run of the 2024 Silver Bulletin presidential model used 80,000 simulations. Harris won 40,012 (50.015%), Trump won 39,718 outright, and 270 were exact 269-269 Electoral College ties.

*Numbers:* simulations = 80,000 simulations (final run, midnight Nov 5 2024); Harris wins = 40,012 (50.015%) simulations (final run); non-Harris wins = 39,988 (49.985%) simulations (final run); Trump outright wins = 39,718 simulations (final run); 269-269 ties = 270 simulations (final run)

> Out of 80,000 simulations, Kamala Harris won in 40,012 (50.015%) cases.

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#0</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**limitation or failure mode** · 2024 presidential · inferred_from_chart

The chart captions on the 2024 Silver Bulletin forecast page describe results as based on 40,000 simulations, while the text says the final run used 80,000. The standard per-update simulation count may therefore be 40,000, with the final run doubled, or the chart captions may simply be stale.

*Numbers:* simulations cited in charts = 40,000 simulations (captions on topline, tipping-point, EV distribution and paths charts)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#1</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**method** · 2024 presidential · inferred_from_chart

The 2024 Silver Bulletin model converts a state polling average into a forecast in 10 steps. These are: (1) polling average; (2) adjust for bounces and recent events; (3) adjusted polling average; (4) reallocate undecideds and third-party votes; (5) reallocated vote share; (6) blend with a regression; (7) snapshot; (8) blend with economic fundamentals; (9) projected vote share; (10) chance of winning.

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#12</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**parameter or number** · 2024 presidential · inferred_from_chart

Final 2024 Silver Bulletin topline: Harris Electoral College probability 50.0%, Trump 49.6%, no majority 0.3%. Popular-vote probability was Harris 76.2% and Trump 23.8%. Predicted electoral votes were 271.0 to 267.0, and predicted popular vote 50.5% to 48.4%.

*Numbers:* Harris EC prob = 50.0% probability (final); Trump EC prob = 49.6% probability (final); Harris popular vote prob = 76.2% probability (final); Harris EV = 271.0 electoral votes (mean); Trump EV = 267.0 electoral votes (mean); Harris PV share = 50.5% vote share (projected); Trump PV share = 48.4% vote share (projected)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#22</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**method** · 2024 presidential · inferred_from_chart

A contest's 'chance of tipping the election' in the 2024 Silver Bulletin model is the probability that it gives the Electoral College winner their 270th electoral vote. The Voter Power Index (VPI) is the relative likelihood that an individual voter in that state determines the Electoral College winner.

*Numbers:* PA tipping-point chance = 34% probability (final); PA VPI = 7.8 index (final); MI tipping = 14% probability (final); NC tipping = 14% probability (final); GA tipping = 10% probability (final); WI tipping = 10% probability (final)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#25</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**method** · 2024 presidential · inferred_from_chart

The '128 paths' table in the 2024 Silver Bulletin model enumerates all 2^7 win/loss combinations of the seven likeliest tipping-point states. Every other state is assigned to its forecast leader, and the table shows each scenario's probability and Harris's EC win probability. For example, R in AZ, GA, NC and NV with D in MI, PA and WI gives exactly 270 EVs and an 82.5% Harris win probability.

*Numbers:* paths = 128 scenarios (7 states)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#26</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**empirical regularity** · 2024 presidential · inferred_from_chart

The Electoral College distribution in the 2024 Silver Bulletin simulations is lumpy and multimodal. The most frequent Harris outcome was 226 EVs (about 6%, the all-battlegrounds-to-Trump map), with a second peak near 319 (about 3%).

*Numbers:* modal Harris EV = 226 electoral votes (~6% of simulations)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#30</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**parameter or number** · 2024 presidential · explicit

The final 2024 Silver Bulletin presidential forecast was based on 80,000 simulations.

*Numbers:* final simulations = 80,000 simulations (final 2024 forecast)

> coming up in 4,660 of our final 80,000 simulations

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#0</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**parameter or number** · 2024 presidential · inferred_from_chart

The published interactive charts for the 2024 Silver Bulletin presidential model (the 128 tipping-point permutations table and the electoral vote distribution chart) are labeled as based on 40,000 simulations, while the article text cites 80,000 final simulations.

*Numbers:* simulations in published charts = 40,000 simulations (charts updated November 5, 2024)

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#1</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**method** · 2024 presidential · explicit

The 2024 Silver Bulletin presidential model simulates outcomes in all 50 states, the District of Columbia, and the congressional districts of Maine and Nebraska. Each simulation therefore yields a complete map that can be tallied, and the frequency of each exact map can be counted.

> the exact map that occurred most often in our simulations, counting all 50 states, the District of Columbia and the congressional districts in Nebraska and Maine

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#2</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**parameter or number** · 2024 presidential · explicit

The second most common exact map in the final 2024 model was a Harris sweep of the swing states with everything else going to form, at 2,446 of 80,000 simulations.

*Numbers:* simulations with second most common map = 2446 simulations (Harris swing state sweep map)

> The next-most-common map (2446 sims) was Harris sweeping the swing states and then everything else going to form.

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#4</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**method** · 2024 presidential · inferred_from_chart

The '128 paths to victory' table lists every permutation of the 7 likeliest tipping-point states (AZ, GA, MI, NC, NV, PA, WI). For each permutation it gives the scenario probability, Harris's electoral votes, and Harris's Electoral College win probability. All other states are assigned by default to the candidate leading that state's forecast.

*Numbers:* permutations = 128 scenarios (2^7 swing-state outcomes)

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#13</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**parameter or number** · 2024 presidential · inferred_from_chart

Selected rows of the final scenario table, which assigns non-swing states by default:
- Harris wins all but AZ and NV: 4.4%, 302 EV, 99.9% win probability.
- Harris wins all but AZ: 3.8%, 308 EV.
- Harris wins only MI, PA and WI (exact Blue Wall): 3.6%, 270 EV, 82.5% win probability.
- Harris wins only MI and WI: 3.5%, 251 EV, 0.4%.
- Harris wins only WI: 2.9%, 236 EV.
- Harris wins only NV: 2.9%, 232 EV.
- Harris wins MI, NV, PA, WI: 2.8%, 276 EV, 97.9%.
- Harris wins only MI: 2.7%, 241 EV.
- Harris wins AZ, MI, NV, PA, WI: 2.6%, 287 EV, 99.7%.
- Harris wins all but GA: 2.0%, 303 EV.
- Harris wins only GA: 1.9%, 242 EV, 0.3%.
- Harris wins MI, NV, WI: 1.8%, 257 EV, 0.8%.
- Harris wins MI, NC, PA, WI: 1.7%, 286 EV, 99.2%.
Win probabilities below 100% at 270 or more default EV reflect simulations in which other states flip.

*Numbers:* exact Blue Wall scenario probability = 3.6 percent (Harris 270 EV); Harris win prob in Blue Wall scenario = 82.5 percent (non-swing states can flip)

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#14</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**parameter or number** · 2024 presidential · explicit

Trump at exactly 312 EV (Harris 226) was by far the most common electoral vote outcome, occurring in about 6% of simulations (5,002 of 80,000). It appears as a large spike in the electoral vote distribution chart. Trump won more than 312 EV in 16% of simulations.

*Numbers:* Trump exactly 312 EV = 6 percent of simulations (5,002 of 80,000); Trump more than 312 EV = 16 percent of simulations (final 2024)

> Trump @ 312 was by far the most common outcome in our simulations, occurring 6 percent of the time

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#15</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**empirical regularity** · 2024 presidential · inferred_from_chart

In the electoral vote distribution chart, Harris's tallest spike is about 6% at 226 EV. Her second large spike is about 3% at around 319 EV, matching the Harris swing state sweep.

*Numbers:* Harris 319 EV spike = ~3 percent (read from chart)

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#16</sub>

### 2025-06-02 · [SBSQ #21: Why young men don't like Democrats](https://www.natesilver.net/p/sbsq-21-why-young-men-dont-like-democrats)
**method** · general principle (sports win probability) · explicit

Silver describes two approaches to probability estimation. One is a logistic regression on current state variables (score, time left, possession, pregame odds). The other simulates the rest of the event forward many times, which is more computationally intensive and needs well-written code and fast hardware. Both can fail if they omit context-specific factors or state-dependent dynamics.

*Why:* Regression can omit factors that are rare on average but pertinent in particular cases. Simulation can miss dynamics such as the rubber-band effect.

> Alternatively, you could have model that simulates the rest of the game forward some number of times; this is much more computationally intensive and requires well-written code and fast hardware.

<sub>2025-06-02_sbsq-21-why-young-men-dont-like-democrats#7</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**parameter or number** · FLIPR 2026 · explicit

FLIPR runs 40,000 simulations every time the model is updated and uses variance-reduction techniques so the effective sample size is larger than 40,000.

*Numbers:* simulations per update = 40,000 simulations (FLIPR 2026)

*Why:* Simulations are needed because of complex correlations between races.

> we run 40,000 simulations every time the model is updated.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#2</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**model change** · FLIPR 2026 · explicit

Step 7: FLIPR's simulations use slightly fat-tailed distributions for rare out-of-sample events, but the fat tails are less severe than in past years because recent cycles lacked huge outliers.

> Fat tails are less severe than in past years, as we now have more cycles without huge outlier outcomes.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#38</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**method** · FLIPR 2026 · explicit

FLIPR computes a tipping-point probability for each Senate race: the chance it decides chamber control. In August 2026 the top seven had a combined 71 percent; Texas 13, Ohio 12, Iowa 11, Maine 11, Michigan 11, Alaska 9 and North Carolina 4 percent. Because Senate races are less correlated than a presidential ticket, the tipping point is spread over more states.

*Numbers:* combined tipping-point probability, top 7 = 71 percent (Aug 15, 2026)

> Precisely because Senate races are less correlated with one another than the presidential ticket, these states aren’t quite comprehensive in covering possible tipping point states.

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#13</sub>

### 2026-08-22 · [A tour of the 48 key House races](https://www.natesilver.net/p/a-tour-of-the-48-key-house-races)
**empirical regularity** · FLIPR 2026 · explicit

No single House district has a tipping-point probability near double digits because there are 435 districts. The 48 seats covered have a combined 71 percent chance of deciding control. In a presidential race the comparable fraction would be higher, because outcomes are more correlated and the tipping point is less likely to be a surprise.

*Numbers:* combined tipping-point probability = 71 percent (48 House seats, Aug 2026)

> Because presidential outcomes are more correlated than congressional races, it’s less likely that the tipping-point state will be a surprise.

<sub>2026-08-22_a-tour-of-the-48-key-house-races#3</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**parameter or number** · FLIPR 2026 · explicit

FLIPR aggregates governor outcomes into the number of governorships, with Democrats at 62 percent to control a majority and a 16 percent chance of a 25-25 tie, and population governed, with a projected 215 million Americans under Democratic governors versus 127 million.

*Numbers:* D majority of governorships prob = 62 percent (Aug 2026); 25-25 tie prob = 16 percent (Aug 2026); population under D governors = 215 million (projected)

*Why:* Population governed better reflects the importance of large states.

> In fact, they’re projected to govern 215 million compared to Republicans’ 127 million.

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#15</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**empirical regularity** · Silver Bulletin 2024 presidential · explicit

In the final 2024 Silver Bulletin presidential forecast (about 50/50), the single most likely scenario was Trump sweeping all seven swing states, which happened, and the second most likely was Harris sweeping all seven, reflecting correlated errors.

> But the single most likely scenario was Trump sweeping all seven key swing states

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#7</sub>

### 2026-10-17 · [The good, bad and ugly outcomes in the Senate](https://www.natesilver.net/p/the-good-bad-and-ugly-outcomes-in)
**method** · FLIPR 2026 · explicit

In each of FLIPR's 40,000 daily simulations, the uniform national forecast error is drawn from a Student's t distribution, and additional random draws simulate correlated errors (e.g. systematic error among Hispanics) and uncorrelated local errors (e.g. one congressional district).

*Numbers:* simulations per day = 40,000 simulations (FLIPR Deluxe)

*Why:* Fat tails for national error.

> In each sim, FLIPR draws a random number from a Student’s t distribution to simulate uniform, national polling error.

<sub>2026-10-17_the-good-bad-and-ugly-outcomes-in-the-senate#0</sub>

### 2026-10-27 · [The 83 remotely competitive House races, according to FLIPR](https://www.natesilver.net/p/the-83-remotely-competitive-house)
**empirical regularity** · FLIPR 2026 · explicit

FLIPR's House seat distribution in late October 2026 was asymmetric, with a long right tail of possible Democratic gains; the asymmetry is clearer in Classic and Lite, which bake in fewer expectations, than in Deluxe.

*Why:* Many Likely R seats could flip in a wave.

> If you look carefully at FLIPR’s seat distribution chart, you might notice it’s slightly asymmetric.

<sub>2026-10-27_the-83-remotely-competitive-house-races-according-to-flipr#3</sub>

### 2026-11-01 · [13 maps for the morning after the midterms](https://www.natesilver.net/p/13-morning-after-the-midterm-maps)
**parameter or number** · FLIPR 2026 · explicit

FLIPR forecasts 506 races per cycle in 2026. In about 20 percent of simulations, Senate control comes down to exactly one state. Republicans hold the House in about 1 in 20 simulations, and Democrats win the Senate but not the House in about 1 in 1,000.

*Numbers:* races forecast = 506 races (2026); sims where Senate decided by one state = about 20 percent (Oct 31, 2026); sims with R House hold = around 1 in 20 probability (Oct 31, 2026); sims with D Senate but R House = about 1 in 1000 probability (Oct 31, 2026)

> in about 20 percent of FLIPR simulations, control of the Senate will come down to exactly one state.

<sub>2026-11-01_13-maps-for-the-morning-after-the-midterms-by-nate-silver#0</sub>

### 2026-11-03 · [FINAL FLIPR 2026 midterm election forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-polls-model)
**parameter or number** · FLIPR 2026 final · explicit

FLIPR models House, Senate and gubernatorial elections jointly in each simulation, enabling joint outcome probabilities. Final 2026 values: Democratic sweep 82.2 percent, Democratic House with Republican Senate 14.2 percent, Republican sweep 3.4 percent, Republican House with Democratic Senate 0.2 percent.

*Numbers:* D sweep = 82.2 percent (final); D House / R Senate = 14.2 percent (final); R sweep = 3.4 percent (final); R House / D Senate = 0.2 percent (final)

> FLIPR models House, Senate and gubernatorial elections jointly, meaning that we can calculate the probability of things like Republicans holding the Senate but losing the House.

<sub>2026-11-03_2026-midterm-election-forecast-senate-house-silver-bulletin#0</sub>

### 2026-11-03 · [FINAL FLIPR 2026 midterm election forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-polls-model)
**parameter or number** · FLIPR 2026 · explicit

Topline numbers are typically based on 40,000 simulations and include a small amount of sampling error.

*Numbers:* simulations = 40,000 simulations (FLIPR topline)

> They are typically based on 40,000 simulations and include a small amount of sampling error.

<sub>2026-11-03_2026-midterm-election-forecast-senate-house-silver-bulletin#1</sub>

### 2026-11-03 · [FLIPR 2026 Governors forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-governors-model)
**parameter or number** · FLIPR 2026 final · inferred_from_chart

Final FLIPR gubernatorial aggregates on Nov. 3, 2026: Democrats 90.2 percent to hold a majority of governorships, Republicans 4.0 percent, tie 5.8 percent. Projected population governed: 231.2 million under Democrats and 111.3 million under Republicans.

*Numbers:* D governorship majority prob = 90.2 percent (final); tie prob = 5.8 percent (final); population with D governor = 231.2 million (projected)

<sub>2026-11-03_2026-midterm-election-governors-forecast-silver-bulletin#0</sub>

### 2026-11-03 · [FLIPR 2026 House forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-house-model)
**parameter or number** · FLIPR 2026 final · inferred_from_chart

Final FLIPR Deluxe House forecast on Nov. 3, 2026: 96.4 percent chance of Democratic control, average 241 D to 194 R, a net Democratic gain of 26, from 40,000 simulations with a shaded middle 80 percent.

*Numbers:* House D control prob = 96.4 percent (final); average D seats = 241 seats (final)

<sub>2026-11-03_2026-midterm-election-house-forecast-silver-bulletin#0</sub>

### 2026-11-03 · [FLIPR 2026 House forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-house-model)
**parameter or number** · FLIPR 2026 final · inferred_from_chart

House district tipping-point probabilities top out around 3 percent per district (PA-8, MI-7, PA-7, NC-1, AZ-1), with Voter Power Index values around 8 to 11 and elasticities from about 0.92 (VA-2) to 1.09 (OH-7).

*Numbers:* max district tipping-point prob = 3 percent (final); PA-8 VPI = 10.9 relative index (final); OH-7 elasticity = 1.09 (final)

<sub>2026-11-03_2026-midterm-election-house-forecast-silver-bulletin#1</sub>

### 2026-11-03 · [FLIPR 2026 Senate forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-senate-model)
**parameter or number** · FLIPR 2026 final · inferred_from_chart

Final FLIPR Deluxe Senate forecast on Nov. 3, 2026: 82.4 percent chance of Democratic control, average 53 D to 47 R, a 6-seat Democratic gain, with a seat distribution from 40,000 simulations and a shaded middle 80 percent. At 50-50 Republicans control via the vice president, and Democratic seats include aligned independents.

*Numbers:* Senate D control prob = 82.4 percent (Nov 3, 2026 final); average D seats = 53 seats (final)

<sub>2026-11-03_2026-midterm-election-senate-forecast-silver-bulletin#0</sub>

### 2026-11-03 · [FLIPR 2026 Senate forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-senate-model)
**method** · FLIPR 2026 final · inferred_from_chart

For each state, FLIPR reports a tipping-point probability, the chance that state decides Senate control, and a Voter Power Index, the relative likelihood that an individual voter there determines the winner of the chamber, along with elasticity. Final values: Texas tipping point 12 percent (VPI 1.0, elasticity 1.04), Maine 12 (VPI 12.0, 1.07), Ohio 11 (1.8, 1.02), Kansas 10 (6.7, 1.06), Michigan 10 (1.6, 1.00), Iowa 9 (4.6, 1.05), Minnesota 7 (2.1, 0.94), Alaska 7 (VPI 17.1, elasticity 1.27), New Hampshire 4 (4.6, 1.13).

*Numbers:* Alaska VPI = 17.1 relative index (final); Alaska elasticity = 1.27 (final); Texas tipping point = 12 percent (final)

*Why:* Small states have high voter power per voter.

<sub>2026-11-03_2026-midterm-election-senate-forecast-silver-bulletin#1</sub>

### 2026-11-03 · [It's Judgment Day for Trump (and for pollsters)](https://www.natesilver.net/p/its-judgment-day-for-trump-and-for)
**parameter or number** · FLIPR 2026 · explicit

Sorting Senate states by FLIPR's projected margin, the final tipping-point state was Ohio, with Brown +3.4; a uniform Democratic underperformance of 3.3 points would still yield a Senate majority. FLIPR's final Senate win probability was about 80 percent in each of Lite, Classic and Deluxe.

*Numbers:* tipping-point margin = 3.4 points (Ohio, final); final Senate D prob = about 80 percent (all versions)

> the tipping-point state is Ohio, where Sherrod Brown is forecasted to win by 3.4 points.

<sub>2026-11-03_its-judgment-day-for-trump-and-for-pollsters#2</sub>
