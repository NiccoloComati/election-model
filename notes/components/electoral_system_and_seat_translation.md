# Electoral system and seat translation

67 findings from 40 articles, oldest first.

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

The presidential model forecasts 54 jurisdictions: 48 states, DC, Maine's two congressional districts and Nebraska's three, with Maine and Nebraska statewide forecasts mostly the sum of district forecasts but also informed by statewide polls. Electoral College ties of 269-269 are reported as ties in 2020 rather than broken. Faithless electors are not modeled.

*Numbers:* jurisdictions forecast = 54 jurisdictions (2020)

> In total, the model calculates a forecast in 54 jurisdictions

<sub>fte_2020-presidential-forecast-methodology#29</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**empirical regularity** · 2024 presidential (March) · explicit

In early 2024, Biden trailed Trump by a wider margin in swing-state polling than nationally, implying an Electoral College disadvantage for Democrats. If the election were held then, Trump would be favored, with Biden within striking distance only through a systematic polling error.

> Biden generally trails Trump by a wider margin in swing state polling.

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#15</sub>

### 2024-06-22 · [The model is coming](https://www.natesilver.net/p/the-model-is-coming)
**method** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model includes explicit handling of ranked choice voting in Maine. Silver describes this as one of the remaining edge cases during development.

> mostly down to edge-case stuff like handling ranked choice voting in Maine

<sub>2024-06-22_the-model-is-coming-by-nate-silver-silver-bulletin#0</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**method** · 2024 presidential · explicit

The 2024 model simulates Maine's ranked-choice voting in two steps. If no candidate has a majority, 'other' votes are reassigned to Biden, Trump and RFK Jr., with a random Biden/Trump split. If there is still no majority, the third-place candidate's votes are reallocated with an uncertainty term. When RFK Jr. is third, the third-party adjustment's Biden/Trump split serves as the prior.

*Why:* Empirically, splits in ranked-choice elections are often not even.

> The split of the vote between Biden and Trump is determined randomly — empirically, in ranked choice elections, there is often not an even split.

<sub>2024-06-26_2024-presidential-election-model-methodology-update#21</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**assumption** · 2024 presidential · explicit

As a simplifying assumption, the Maine ranked-choice simulation ignores ballot exhaustion (wastage). Published Maine vote shares are post-reallocation, which is why RFK Jr. and 'other' show low Maine shares despite it being a good third-party state.

*Why:* Simplification.

> As a simplifying assumption, the model ignores the fact that there is typically wastage in elections featuring ranked-choice voting

<sub>2024-06-26_2024-presidential-election-model-methodology-update#22</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**method** · 2024 presidential · explicit

The ranked-choice reallocation is also applied separately within each Maine congressional district lacking a majority. As a result, the statewide tally can differ from the combined district tallies. The national popular-vote forecast uses the statewide result.

*Why:* Maine awards electoral votes by congressional district.

> The model uses the statewide result in its forecast of the national popular vote.

<sub>2024-06-26_2024-presidential-election-model-methodology-update#23</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**interpretation guidance** · 2024 presidential · explicit

No-majority outcomes are reported separately rather than assigned to a candidate. Silver notes they would probably resolve to Trump through a House contingent election under the 12th Amendment, given the likely Republican advantage in state congressional delegations.

> those cases will probably resolve to Trump because of the likely Republican advantage in congressional delegations in the U.S. House under the 12th Amendment

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#31</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**empirical regularity** · 2024 presidential · explicit

In July 2024, Biden's Electoral College position in the Silver Bulletin model was considerably worse than his popular vote standing, implying a Republican-leaning Electoral College bias.

> Biden’s Electoral College position is considerably worse than his standing in the popular vote

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#5</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**method** · 2024 presidential · inferred_from_chart

The 2024 model tracks a 'No majority' outcome. This covers simulations where neither candidate reaches 270 electoral votes, whether from a 269-269 tie or from a third-party candidate such as RFK Jr. winning electoral votes. It was 0.4% in the final Biden-Trump forecast.

*Numbers:* no Electoral College majority probability = 0.4% probability (July 21, 2024); Kennedy predicted electoral votes = 0.3 electoral votes (July 21, 2024)

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#8</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**empirical regularity** · 2024 presidential · inferred_from_chart

In the final Biden-Trump forecast the Electoral College favored Trump. Biden's Electoral College win probability was 11.4% when he won the popular vote by 0-1 points, 34.3% at D+1 to +2, 63.8% at D+2 to +3, 89.8% at D+3 to +4, and 98.0% at D+4 to +5. Biden's break-even was therefore roughly a 2-2.5 point popular-vote lead.

*Numbers:* Biden win prob at D+0-1 = 11.4% probability (July 21, 2024); Biden win prob at D+1-2 = 34.3% probability; Biden win prob at D+2-3 = 63.8% probability; Biden win prob at D+3-4 = 89.8% probability; Biden win prob at D+4-5 = 98.0% probability; Biden win prob at R+0-1 = 2.4% probability; Biden EV at D+2-3 = 274.6 electoral votes

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#22</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**method** · 2024 presidential · inferred_from_chart

The Silver Bulletin defines a contest's tipping-point chance as the probability that it gives the Electoral College winner their 270th electoral vote. Its Voter Power Index (VPI) is the relative likelihood that an individual voter in a state determines the Electoral College winner. A missing conditional probability means the candidate won that state in 0 of 40,000 simulations.

*Numbers:* electoral vote threshold = 270 electoral votes (tipping-point definition)

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#3</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**parameter or number** · 2024 presidential · inferred_from_chart

Aug 8, 2024 tipping-point chances, with VPI in parentheses: PA 34% (8.1), WI 14% (6.7), MI 12% (3.5), GA 10% (3.1), AZ 8% (3.4), NC 6% (1.8), NV 3% (3.2), TX 2% (0.3), FL 2% (0.2), VA 2% (0.6), NM 1% (2.0), NE-2 1% (4.3), NH 1% (1.6), CO 1% (0.3). The model treats Maine and Nebraska's congressional districts (e.g., NE-2) as separate contests.

*Numbers:* PA tipping chance = 34 percent (Aug 8, 2024); PA VPI = 8.1 index (Aug 8, 2024); NE-2 VPI = 4.3 index (Aug 8, 2024)

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#4</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**parameter or number** · 2024 presidential · explicit

With an N3PC in the race, the Silver Bulletin presidential model in about 2 percent of simulations had RFK winning some electoral votes, which could produce an Electoral College deadlock with no one reaching 270. With no N3PC, the only deadlock is an exact 269-269 tie, at about a 0.3 percent chance. Removing these deadlock scenarios slightly helped Harris.

*Numbers:* RFK winning EVs probability = about 2 percent (pre-removal simulations); 269-269 tie probability = 0.3 percent (Aug 24, 2024)

*Why:* Plausible exact 269-269 maps are combinatorially rare.

> Now the only deadlock scenario is an exact 269-269 tie, which is only a 0.3 percent chance given how the states line up combinatorially.

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#20</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**empirical regularity** · 2024 presidential · explicit

With little high-quality state polling after the DNC and RFK Jr.'s exit, the 2024 model defaulted toward its regression estimates. Those estimates encode the large Electoral College vs. popular vote gap that hurt Democrats in 2016 and 2020, which made the model somewhat bearish on Harris in late August 2024.

> it defaults somewhat toward its regression-based estimates, which reflect the relatively large gap between the Electoral College and the popular vote that hurt Democrats in 2016 and 2020

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#24</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**empirical regularity** · 2024 presidential · explicit

In the 2024 model, a tied national popular vote implies Democrats are underdogs in the Electoral College. This reflects a GOP Electoral College advantage, so Harris can be favored to win the popular vote while being a slight underdog for the presidency.

> Harris being a favorite to win the popular vote but perhaps a slight underdog to win the White House because of the GOP advantage in the Electoral College.

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#25</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**method** · 2024 presidential · explicit

Silver measures Electoral College bias as each battleground state's margin minus the national margin, averaged with weights equal to each state's tipping-point probability. This can be computed from polling averages (state average vs national average) or from the forecast (Nov. 5 state projection vs projected national popular vote).

> Weighted by each state’s tipping-point probability, it was R +3.7 in 2016 and R +3.5 in 2020.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#10</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**parameter or number** · 2024 presidential · explicit

The tipping-point-weighted Electoral College bias was R+3.7 in 2016 and R+3.5 in 2020. As of Sept. 6, 2024, it was R+2.4 in Silver Bulletin polling averages and R+2.5 in the forecast.

*Numbers:* EC bias 2016 = R+3.7 percentage points (actual result); EC bias 2020 = R+3.5 percentage points (actual result); EC bias 2024 polling average = R+2.4 percentage points (Sept. 6, 2024); EC bias 2024 forecast = R+2.5 percentage points (Sept. 6, 2024)

> By comparison, our polling averages and our forecast have it at R +2.4 and R +2.5 this time around, respectively.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#11</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**parameter or number** · 2024 presidential · explicit

As of Sept. 6, 2024, the Silver Bulletin model has the Electoral College as a toss-up if Harris wins the popular vote by 2–3 points. She needs roughly a 4-point popular-vote win to be safe. The model gives a 20% chance she wins the popular vote but loses the Electoral College.

*Numbers:* toss-up popular-vote range = 2-3 percentage points (Harris margin); safe popular-vote margin = roughly 4 percentage points; P(Harris wins PV, loses EC) = 20 percent (Sept. 6, 2024)

> there’s now a 20 percent chance that she wins the popular vote but loses the Electoral College.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#17</sub>

### 2024-09-07 · [Oops! I made the convention bounce adjustment disappear.](https://www.natesilver.net/p/oops-i-made-the-convention-bounce)
**empirical regularity** · 2024 presidential · explicit

In September 2024, the cross-state hedging in the 2024 model implied an Electoral College/popular vote gap slightly wider than the polls showed. It was skeptical of Harris's Wisconsin polling, which hurt her at the margin.

> This calculation implies that the Electoral College/popular vote gap will be slightly wider than what polls currently show — it's skeptical of Harris's polling in Wisconsin

<sub>2024-09-07_oops-i-made-the-convention-bounce-adjustment-disappear#10</sub>

### 2024-09-11 · [A guide to post-debate poll-watching](https://www.natesilver.net/p/a-guide-to-post-debate-poll-watching)
**parameter or number** · 2024 presidential · explicit

As of September 2024, the Silver Bulletin 2024 presidential model estimates an Electoral College bias of around 2.5 points against Democrats. Under this estimate, Harris needs roughly a 3-point national lead to be a slight favorite.

*Numbers:* Electoral College bias = Around 2.5 percentage points (against Democrats, model estimate as of September 2024); National lead needed to be a slight favorite = 3 percentage points (Harris)

> Around 2.5 points against Democrats.

<sub>2024-09-11_a-guide-to-post-debate-poll-watching-by-nate-silver#5</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**empirical regularity** · 2024 presidential · explicit

In the 2024 Silver Bulletin model, Harris has an almost 25 percent chance of winning the popular vote but losing the Electoral College. The reverse outcome, Trump winning the popular vote but losing the Electoral College, has little probability.

*Numbers:* P(Harris wins popular vote, loses EC) = almost 25 percent (mid-September 2024 model)

*Why:* Democrats waste many votes in the large, lopsided states of California and New York.

> there’s almost a 25 percent chance that Harris wins the popular vote but loses the Electoral College — but little of the other way around.

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#2</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**empirical regularity** · 2024 presidential · inferred_from_chart

Per the Sept. 17, 2024 expected value table, Harris's expected EVs in key states were: Virginia 12.2 of 13, Minnesota 8.4 of 10, Pennsylvania 8.1 of 19 and Michigan 7.7 of 15. Trump's expected EVs were about 10 in Pennsylvania and about 7 in Michigan. Safe states such as California (53.9 of 54) and New York (27.8 of 28) were near their full totals.

*Numbers:* Harris EV expectation, California = 53.9 electoral votes (of 54); Harris EV expectation, New York = 27.8 electoral votes (of 28); Harris EV expectation, New Jersey = 13.7 electoral votes (of 14); Harris EV expectation, Virginia = 12.2 electoral votes (of 13); Harris EV expectation, Washington = 11.9 electoral votes (of 12); Harris EV expectation, Colorado = 9.7 electoral votes (of 10); Harris EV expectation, Minnesota = 8.4 electoral votes (of 10); Harris EV expectation, Pennsylvania = 8.1 electoral votes (of 19); Harris EV expectation, Michigan = 7.7 electoral votes (of 15)

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#9</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**method** · general principle (analytical metric, not model input) · explicit

Silver defines Net eXcess Votes (NXV) as the votes a party wins in a state beyond what was needed to win it by X points, where X = 3 percentage points plus 0.1 point per electoral vote. For example, Tennessee's 11 EVs give a threshold of 4.1 points. Nebraska and Maine congressional district electoral votes are ignored.

*Numbers:* NXV base threshold = 3 percentage points (base competitive margin); NXV per-EV increment = 0.1 percentage points per electoral vote (sliding scale); Tennessee NXV threshold = 4.1 percentage points (2020)

*Why:* Empirically, parties pour resources into states within 3 to 5 points of the tipping-point state, and bigger states justify a play at wider margins because of their larger reward.

> I’ll define the threshold as winning a state by 3 percentage points, plus one-tenth of a percentage point for every electoral vote.

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#12</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**empirical regularity** · general principle · explicit

In 2020, Biden accumulated 11.1 million NXVs and Trump 5.5 million. The 5.6 million difference is 3.5 percent of the 159 million votes cast. That almost exactly matches the gap between Biden's national popular vote margin (4.5 points) and his margin in the tipping-point state, Wisconsin (0.7 points). Silver says this is not a coincidence, because NXVs are by definition votes that help in the popular vote but add no marginal Electoral College advantage.

*Numbers:* Biden NXVs 2020 = 11,050,000 votes (2020); Trump NXVs 2020 = 5,450,000 votes (2020); NXV difference = 5.6 million votes (2020); NXV difference share of electorate = 3.5 percent (2020); total votes cast 2020 = 159 million votes (2020); Biden national margin = 4.5 percentage points (2020); Biden Wisconsin margin = 0.7 percentage points (2020 tipping-point state)

> NXVs are defined as votes that help you in the popular vote, but don’t net you any marginal advantage in the Electoral College.

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#13</sub>

### 2024-09-18 · [Mad about the Electoral College? Blame California.](https://www.natesilver.net/p/mad-about-the-electoral-college-blame)
**empirical regularity** · general principle · inferred_from_chart

2020 NXV leaders by state were: Biden, California 3.62M, New York 1.48M, Massachusetts 1.07M, Maryland 0.89M, Illinois 0.72M, Washington 0.61M, New Jersey 0.52M, Colorado 0.31M, Connecticut 0.30M, Oregon 0.29M and DC 0.29M; Trump, Tennessee 0.58M, Alabama 0.50M, Kentucky 0.47M, Oklahoma 0.46M, Indiana 0.36M, Missouri 0.34M, Louisiana 0.32M and Arkansas 0.29M. The data come from the U.S. Election Atlas.

*Numbers:* California Biden NXV = 3,620,000 votes (2020); New York Biden NXV = 1,480,000 votes (2020); Massachusetts Biden NXV = 1,070,000 votes (2020); Maryland Biden NXV = 890,000 votes (2020); Illinois Biden NXV = 720,000 votes (2020); Washington Biden NXV = 610,000 votes (2020); New Jersey Biden NXV = 520,000 votes (2020); Colorado Biden NXV = 310,000 votes (2020); Connecticut Biden NXV = 300,000 votes (2020); Oregon Biden NXV = 290,000 votes (2020); DC Biden NXV = 290,000 votes (2020); Tennessee Trump NXV = 580,000 votes (2020); Alabama Trump NXV = 500,000 votes (2020); Kentucky Trump NXV = 470,000 votes (2020); Oklahoma Trump NXV = 460,000 votes (2020); Indiana Trump NXV = 360,000 votes (2020); Missouri Trump NXV = 340,000 votes (2020); Louisiana Trump NXV = 320,000 votes (2020); Arkansas Trump NXV = 290,000 votes (2020)

<sub>2024-09-18_mad-about-the-electoral-college-blame-california#14</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**method** · 2024 presidential · explicit

The model simulates Nebraska and Maine congressional-district electoral votes separately (NE-2, ME-2). In 610 of 40,000 simulations (about 1.5%), Harris won exactly the Blue Wall states plus NE-2 and lost the other battlegrounds, giving a 270-268 win. Without NE-2 that map would be a 269-269 tie, probably resolved for Trump in the House.

*Numbers:* Blue Wall + NE-2 exact scenario = 610 simulations (out of 40,000, Sept 21, 2024); share of simulations = about 1.5 percent (Sept 21, 2024)

> Without that extra vote in Omaha, though, it's a 269-269 tie, which would probably be resolved for Trump in the U.S. House.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#16</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**assumption** · 2024 presidential · explicit

A 269-269 Electoral College tie would probably be resolved for Trump in the U.S. House. This is relevant for how a replicator should score tie outcomes.

> it's a 269-269 tie, which would probably be resolved for Trump in the U.S. House.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#17</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**assumption** · 2024 presidential · explicit

Pennsylvania, Michigan, Wisconsin and Nebraska's 2nd Congressional District together give Harris exactly 270 electoral votes. Nebraska's split allocation of electoral votes was assumed to remain after a Republican push to revert to winner-take-all appeared to fail.

*Numbers:* electoral votes needed = 270 electoral votes (PA+MI+WI+NE-2 path)

> Those states, plus the 2nd Congressional District of Nebraska ... would suffice to give Harris 270 electoral votes.

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#7</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**parameter or number** · 2024 presidential · explicit

On Sept 26, 2024 the model gave a 20% chance that Harris wins the popular vote but loses the Electoral College, versus 0.3% for the reverse split. Harris was a 3:1 favorite in the popular vote while the Electoral College was roughly a toss-up.

*Numbers:* P(Harris wins PV, loses EC) = 20 percent (Sept 26 2024); P(Trump wins PV, loses EC) = 0.3 percent (Sept 26 2024 (~300:1)); Harris PV odds = 3:1 odds (favorite)

> there’s a 20 percent chance that Harris wins the popular but loses the Electoral College, but only a 0.3 percent chance of the same thing happening to Donald Trump

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#14</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**parameter or number** · 2024 presidential · explicit

The model projected Harris +2.5 nationally and +1.0 in Pennsylvania (the tipping point), a point-estimate Electoral College gap of 1.5 points. Averaged across simulations, the gap is about 2 points. Splits can occur at popular vote margins anywhere from about Trump +1 to Harris +5.

*Numbers:* projected national margin = Harris +2.5 percentage points (forecast); projected PA margin = Harris +1.0 percentage points (forecast); point-estimate EC gap = 1.5 percentage points (forecast); average simulated EC gap = about 2 percentage points (after uncertainty; about half the 2020 gap); split range = Trump +1 to Harris +5 popular vote margin (range where splits occur)

*Why:* Because outcomes are probabilistic, small misses in PA, MI or WI widen the effective gap.

> in our average simulation after accounting for this uncertainty, the Electoral College / popular vote winds up being about 2 points, not 1.5

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#15</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**parameter or number** · 2024 presidential · inferred_from_chart

The model's conditional win probability by popular vote bin shows the Electoral College bias. Harris's win probability is 10.5% at D+0 to +1, 32.8% at D+1 to +2, 63.3% at D+2 to +3, 87.0% at D+3 to +4, 96.7% at D+4 to +5 and 99.5% at D+5 to +6. Trump wins 96.9% of the time at R+0 to +1, and Harris wins only 3.0% there. Harris's mean electoral votes are 274.0 at D+2 to +3 and 243.4 at D+0 to +1.

*Numbers:* Harris win prob D+0-1 = 10.5 percent (Sept 26 2024); Harris win prob D+1-2 = 32.8 percent; Harris win prob D+2-3 = 63.3 percent; Harris win prob D+3-4 = 87.0 percent; Harris win prob D+4-5 = 96.7 percent; Harris win prob R+0-1 = 3.0 percent; Harris win prob R+1-2 = 0.6 percent; Harris EV D+6-7 = 337.5 electoral votes; Harris EV R+6-7 = 186.5 electoral votes

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#16</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**adjustment rule** · 2024 presidential · explicit

In the swing-state path table, 269-269 Electoral College ties are counted as Trump wins. Silver's rationale is that a tie would likely be decided for Trump in the U.S. House.

*Numbers:* tie = 269-269 electoral votes (counted as Trump win)

*Why:* A tie goes to the House, where Trump is likely to win.

> For purposes of the table, ties are counted as Trump wins.

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#8</sub>

### 2024-10-01 · [SBSQ #13: October Surprise edition](https://www.natesilver.net/p/sbsq-13-october-surprise-edition)
**critique of other approach** · 538 2024 (revised) · explicit

Silver says the revised 538 2024 model's output of Florida as a more likely tipping-point state than Wisconsin looks a little weird. He concedes that the Silver Bulletin model has quirks too and that modelers mostly make reasonable choices.

> some things in the 538 model look a little weird, like Florida being a more likely tipping-point state than Wisconsin

<sub>2024-10-01_sbsq-13-october-surprise-edition-by-nate-silver#9</sub>

### 2024-10-08 · [55/45 is a really close race](https://www.natesilver.net/p/5545-is-a-really-close-race)
**empirical regularity** · 2024 presidential · explicit

In the Silver Bulletin 2024 model, the mapping from national popular-vote margin to Electoral College win probability is steep around the tipping region. Moving from a 2-3 point Harris popular-vote lead to a 3-4 point lead raises her win probability from about 28% to 59% (the chart table gives 58.8%). So small popular-vote changes produce large probability swings.

*Numbers:* Harris win prob at D+1 to +2 (text: '2-point lead rounded down') = 28 percent (Oct 7, 2024 table); Harris win prob at D+2 to +3 = 59 percent (text value; table 58.8%)

*Why:* It is analogous to late-and-close win probability curves in sports.

> If she goes from a 2-point popular vote lead (rounded down) to a 3-point lead, Harris's win probability zooms up from 28 percent to 59 percent.

<sub>2024-10-08_5545-is-a-really-close-race-by-nate-silver#7</sub>

### 2024-10-08 · [55/45 is a really close race](https://www.natesilver.net/p/5545-is-a-really-close-race)
**parameter or number** · 2024 presidential · inferred_from_chart

The Silver Bulletin chart 'How big is the Electoral College bias?' (Oct 7, 2024) gives conditional outcomes by national popular-vote margin, listed as Harris win % / Trump win % / Harris EV / Trump EV:
- D+6-7: 99.8/0.2/337.4/200.6
- D+5-6: 99.1/0.8/323.5/214.5
- D+4-5: 96.1/3.6/305.6/232.4
- D+3-4: 83.9/15.6/289.8/248.2
- D+2-3: 58.8/40.6/272.9/265.1
- D+1-2: 28.0/71.2/256.3/281.7
- D+0-1: 9.5/90.1/242.6/295.4
- R+0-1: 1.9/98.0/231.5/306.5
- R+1-2: 0.6/99.3/224.1/313.9
- R+2-3: 0.1/99.9/217.9/320.1
- R+3-4: 0/100/210.5/327.5
- R+4-5: 0/100/201.4/336.6
- R+5-6: 0/100/193.9/344.1
- R+6-7: 0/100/185.6/352.4
The Electoral College breakeven for Harris is about a D+2.5 popular-vote margin.

*Numbers:* Harris win prob D+2 to +3 = 58.8 percent (Oct 7, 2024); Harris win prob D+3 to +4 = 83.9 percent (Oct 7, 2024); Harris win prob D+0 to +1 = 9.5 percent (Oct 7, 2024); Harris win prob R+0 to +1 = 1.9 percent (Oct 7, 2024); Harris EV D+2 to +3 = 272.9 electoral votes (mean in simulations); implied EC breakeven = ~2.5 percentage points (D) (inferred from table)

*Why:* Shows the conditional EC outcome distribution across simulations.

<sub>2024-10-08_5545-is-a-really-close-race-by-nate-silver#8</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**empirical regularity** · 2024 presidential · explicit

In mid-October 2024, the Silver Bulletin model identified Pennsylvania as the likeliest tipping-point state.

> In Pennsylvania — the likeliest tipping point state — our average is Harris +0.6.

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#21</sub>

### 2024-10-22 · [Likability isn't enough](https://www.natesilver.net/p/likability-isnt-enough)
**interpretation guidance** · 2024 presidential · explicit

In 2024, a Harris national popular-vote lead of 3 to 5 points would very probably translate into an Electoral College win. A lead closer to 2 points makes an Electoral College win tenuous, which implies a Republican-leaning Electoral College bias of roughly that size.

*Numbers:* national lead implying very probable EC win = 3-to-5 percentage points (Harris national polling lead, Oct 2024); national lead implying tenuous EC position = ~2 percentage points (Harris national polling lead, Oct 2024)

> With a 3-to-5 point national lead, Harris would very probably win the Electoral College. If it's closer to 2 points, it's tenuous.

<sub>2024-10-22_likability-isnt-enough-by-nate-silver-silver-bulletin#0</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**assumption** · 2024 presidential · explicit

The Silver Bulletin presidential model reports 269-269 Electoral College ties as a separate 'no majority' outcome rather than awarding them to a candidate. Silver says a tie would in practice probably be resolved for Trump in the U.S. House.

*Numbers:* electoral vote tie = 269-269 electoral votes (no-majority outcome)

*Why:* Contingent House election rules would likely favor Trump.

> no majority — a 269-269 tie — which practically speaking would probably be resolved for Trump in the U.S. House.

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#2</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**interpretation guidance** · 2024 presidential · implied

Silver says a Harris lead of about 1 point in the national popular vote would probably still leave her an underdog in the Electoral College, implying a Republican-leaning Electoral College bias.

*Numbers:* national lead = 1 percentage points (Harris, 2024)

> Harris leads by 1 point in our final national polling average — that probably still leaves her as un underdog in the Electoral College.

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#13</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**method** · 2024 presidential · explicit

Silver Bulletin coverage enumerates the 128 possible combinations of the 7 swing states (2^7) as 'paths to victory'. The model also treats Nebraska and Maine congressional districts as separate electoral units (NE-2, NE-3, ME-2, etc.).

*Numbers:* paths to victory = 128 combinations (7 swing states); swing states = 7 states (2024)

> guided you through the 128 paths to victory

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#18</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**assumption** · 2024 presidential · explicit

The 2024 Silver Bulletin presidential model counts exact 269-269 ties as a separate 'no majority' outcome rather than as a win for either candidate. The authors note these ties would likely resolve as Trump wins in the House contingent election.

*Numbers:* no majority probability = 0.3% probability (final forecast)

*Why:* Republicans were expected to control more House state delegations.

> these ties are likely to eventually result in Trump wins in the U.S. House of Representatives

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#2</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**assumption** · 2024 presidential · inferred_from_chart

In the 2024 Silver Bulletin presidential model, the 'no majority' outcome can also arise if a third-party candidate receives electoral votes, not only from 269-269 ties.

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#3</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**method** · 2024 presidential · inferred_from_chart

The 2024 Silver Bulletin presidential model forecasts Maine and Nebraska congressional districts (ME-1, ME-2, NE-2, NE-3) as separate contests, because those states award one electoral vote per district plus two to the statewide winner.

*Numbers:* Nebraska EVs = 5 electoral votes (3 districts + 2 statewide); Maine EVs = 4 electoral votes (2 districts + 2 statewide)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#4</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**empirical regularity** · 2024 presidential · inferred_from_chart

In the final 2024 Silver Bulletin simulations, the Electoral College favored Trump: Harris won only 14.3% when winning the popular vote by 0-1, 32.5% at D+1-2 and 58.2% at D+2-3. Trump won 94.0% at R+0-1.

*Numbers:* Harris win prob D+0-1 = 14.3% probability (final); Harris win prob D+1-2 = 32.5% probability (final); Harris win prob D+2-3 = 58.2% probability (final); Harris win prob D+3-4 = 80.2% probability (final); Harris win prob D+4-5 = 92.5% probability (final); Trump win prob R+0-1 = 94.0% probability (final); Harris EVs D+2-3 = 272.5 electoral votes (final)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#21</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**empirical regularity** · 2024 presidential · inferred_from_chart

In the final 2024 Silver Bulletin forecast, Pennsylvania (R+0.1) was the tipping-point state on the ordered path. Harris led Wisconsin by D+1 and Michigan by D+1.2, while Trump led Nevada R+0.5, Georgia R+1, North Carolina R+1.1 and Arizona R+2.4.

*Numbers:* PA forecast margin = R+0.1 percentage points (final)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#29</sub>

### 2025-06-02 · [SBSQ #21: Why young men don't like Democrats](https://www.natesilver.net/p/sbsq-21-why-young-men-dont-like-democrats)
**assumption** · general principle (NYC 2025 primary) · explicit

Ranked-choice voting adds an extra layer of uncertainty to primary forecasts. Its mechanics do not straightforwardly favor compromise candidates such as Brad Lander.

> the mechanics of RCV aren't quite so straightforward as you might think

<sub>2025-06-02_sbsq-21-why-young-men-dont-like-democrats#10</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**interpretation guidance** · general principle · explicit

Differences between the generic ballot and the House popular vote caused by uncontested seats are mostly an accounting issue. Failing to nominate candidates lets the other party run up the popular vote but matters little for seats, as long as candidates run in competitive districts.

> this is a technical accounting issue rather than a substantive one.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#17</sub>

### 2026-08-11 · [Everything is breaking Democrats’ way. Is it enough to win the Senate?](https://www.natesilver.net/p/everything-is-breaking-democrats-way)
**parameter or number** · FLIPR 2026 · explicit

FLIPR finds the House tipping point at a national environment of about D+3 to D+3.5 after mid-decade redistricting, so Republicans are effectively spotted about a field goal. The Senate threshold for a Democratic majority is around D+6 or better.

*Numbers:* House cut point = 3-3.5 points (D national margin) (2026 maps); Senate cut point = about 6 points (D national margin) (2026 map)

> FLIPR, in line with other models, finds that the cut point is somewhere around 3 or 3.5 percentage points.

<sub>2026-08-11_everything-is-breaking-democrats-way-is-it-enough-to-win-the-senate#5</sub>

### 2026-08-11 · [Everything is breaking Democrats’ way. Is it enough to win the Senate?](https://www.natesilver.net/p/everything-is-breaking-democrats-way)
**empirical regularity** · FLIPR 2026 · explicit

Extremely partisan maps drawn by both parties have greatly reduced the number of competitive House districts, so even a D+9 House popular vote would struggle to match the 41-seat gain of 2018.

*Numbers:* 2018 Democratic House gain = 41 seats (reference)

> extremely partisan maps drawn by both parties have greatly reduced the number of competitive districts in the House.

<sub>2026-08-11_everything-is-breaking-democrats-way-is-it-enough-to-win-the-senate#6</sub>

### 2026-08-11 · [Everything is breaking Democrats’ way. Is it enough to win the Senate?](https://www.natesilver.net/p/everything-is-breaking-democrats-way)
**method** · FLIPR 2026 · explicit

FLIPR explicitly simulates ranked-choice voting and Alaska's top-four primary system, which may make its Alaska forecast more volatile than other states.

> FLIPR now explicitly simulates ranked-choice voting and Alaska’s unique top-four primary

<sub>2026-08-11_everything-is-breaking-democrats-way-is-it-enough-to-win-the-senate#12</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

FLIPR's simulations handle ranked-choice voting in Maine and Alaska, Alaska's top-four primary, Georgia-style runoffs when no candidate reaches 50 percent, and Louisiana's House jungle primary, used for the last time in 2026.

> In states like Georgia where elections go to runoffs if no candidate gets 50 percent of the vote, FLIPR simulates this too;

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#40</sub>

### 2026-08-20 · [Are Democrats on a summer sugar high?](https://www.natesilver.net/p/are-democrats-on-a-summer-sugar-high)
**method** · FLIPR 2026 · explicit

After Alaska's top-four primary, FLIPR uses primary results mainly to forecast vote shares within each party for November. It derives only limited information on aggregate party shares, by comparing parties' relative primary performance across the House, Senate and governor races; aggregate party shares come from general-election polls plus priors. The post-primary logic mirrors FLIPR's code for California and Washington top-two primaries, adjusted for four-way incentives.

> The model uses primary results in Alaska in a slightly complicated way, but it’s mostly to forecast November vote shares within the same party.

<sub>2026-08-19_are-democrats-on-a-summer-sugar-high-by-nate-silver#9</sub>

### 2026-08-20 · [Are Democrats on a summer sugar high?](https://www.natesilver.net/p/are-democrats-on-a-summer-sugar-high)
**empirical regularity** · FLIPR 2026 · explicit

In ranked-choice voting, eliminated candidates' votes do not all flow to same-party candidates: a fair number are exhausted because voters rank too few names, and some go to other parties. FLIPR models this, and judged a tie between two Democrats slightly worse for Democrats than one clear leader.

> A fair number of these votes are wasted because voters don’t list enough names on the ballot, and some will go to candidates from other parties instead.

<sub>2026-08-19_are-democrats-on-a-summer-sugar-high-by-nate-silver#10</sub>

### 2026-08-22 · [A tour of the 48 key House races](https://www.natesilver.net/p/a-tour-of-the-48-key-house-races)
**parameter or number** · FLIPR 2026 · explicit

After 2025-26 mid-decade redistricting, FLIPR Deluxe found the House map shifted from roughly no bias to a Republican lean of a few points: Democrats are favored to win the House if they win the national popular vote by 3 points or more, and are underdogs below that. At D+7 they are essentially guaranteed a majority, and the 84 percent probability reflects scenarios of polling error or a changing environment.

*Numbers:* House tipping point = D+3 points (Aug 22, 2026); House D win prob = 84 percent (Deluxe, Aug 22, 2026); mean Democratic seats = 232 seats (average forecast outcome)

> FLIPR Deluxe thinks Democrats will be favored to win the House if they win the national popular vote by 3 points or more

<sub>2026-08-22_a-tour-of-the-48-key-house-races#0</sub>

### 2026-08-22 · [A tour of the 48 key House races](https://www.natesilver.net/p/a-tour-of-the-48-key-house-races)
**parameter or number** · FLIPR 2026 · explicit

On August 22, 2026 FLIPR Deluxe rated 198 seats Solid D, 156 Solid R, 13 Likely D, 37 Likely R, 16 Lean D, 8 Lean R and 7 Toss-up. The asymmetry in Likely R seats means a D+11 environment could turn engineered Republican seats competitive, so gerrymanders could become 'dummymanders'.

*Numbers:* Solid D = 198 seats (Aug 22, 2026); Solid R = 156 seats (Aug 22, 2026); Likely R = 37 seats (Aug 22, 2026); Likely D = 13 seats (Aug 22, 2026); Toss-up = 7 seats (Aug 22, 2026)

> We’d note the asymmetry in the number of “Likely R” seats (37) versus “Likely D” ones (just 13).

<sub>2026-08-22_a-tour-of-the-48-key-house-races#2</sub>

### 2026-08-22 · [A tour of the 48 key House races](https://www.natesilver.net/p/a-tour-of-the-48-key-house-races)
**empirical regularity** · FLIPR 2026 · explicit

Extensive gerrymandering has left the fewest realistically competitive House races ever, with most seats rated Solid for one party.

> the number of realistically competitive House races is smaller than ever.

<sub>2026-08-22_a-tour-of-the-48-key-house-races#9</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**method** · FLIPR 2026 · explicit

In Alaska, FLIPR uses blended fundamentals to forecast each party's aggregate first-round vote, then allocates votes within each party through a separate process that uses polls, fundamentals and primary results. It simulates the first round with uncertainty and then the ranked-choice rounds from each simulated first round, so different candidate pairs reach the final two across simulations. Within-party RCV transfers are about 85 percent, not 100, and some ballots exhaust.

*Numbers:* within-party RCV transfer share = about 85 percent (empirical); Alaska gov blended fundamentals = R+3.7 points (Aug 2026)

> Empirically, within-party transfer shares are more like 85 percent than 100 percent.

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#9</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**method** · FLIPR 2026 · explicit

Besides Alaska, FLIPR uses primary results as an extra information layer in states with blanket nonpartisan primaries for some offices: California, Louisiana and Washington.

> Except California, Louisiana and Washington, which also use blanket nonpartisan primaries for some offices.

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#11</sub>

### 2026-09-03 · [Beware big swings in midterm forecasts](https://www.natesilver.net/p/beware-big-swings-in-midterm-forecasts)
**parameter or number** · FLIPR 2026 · inferred_from_chart

FLIPR's September 2026 seat-translation table gives Democratic House win probability and expected seats by popular-vote margin: D+0-1: 7.4 percent, 211 seats; D+2-3: 50.7 percent, 218; D+3-4: 77 percent, 221; D+4-5: 93.4 percent, 225; D+5-6: 98.9 percent, 229; D+6-7: 99.9 percent, 232; D+9-10: 245; D+14-15: 268. That is roughly 4 to 5 seats per point of popular vote. Democrats need about D+3 to be favored and D+4 to 5 for a double-digit majority.

*Numbers:* D win prob at D+2 to +3 = 50.7 percent (Sept 3, 2026); D seats at D+6 to +7 = 232 seats (Sept 3, 2026); seats per point = about 4-5 seats (derived from table)

<sub>2026-09-03_beware-big-swings-in-midterm-forecasts#3</sub>

### 2026-09-20 · [Expert ratings are ignoring signs of a blue wave](https://www.natesilver.net/p/expert-ratings-are-ignoring-signs)
**adjustment rule** · FLIPR 2026 · explicit

In Alaska, FLIPR computes fundamentals for each party's combined vote, allocates it among same-party candidates, and then simulates ranked-choice voting, whereas experts rate the post-RCV outcome. A special adjustment now puts expert ratings and Classic on the same scale at each stage; the fix slightly helped Republicans.

> FLIPR now makes an adjustment in Alaska so that the expert ratings and FLIPR Classic are more on the same scale at each stage of the process.

<sub>2026-09-20_expert-ratings-are-ignoring-signs-of-a-blue-wave#9</sub>

### 2026-09-29 · [Midterm waves are the rule, not the exception](https://www.natesilver.net/p/midterm-waves-are-the-rule-not-the)
**method** · FLIPR 2026 · explicit

FLIPR replicates quirks of the official House popular vote tally: uncontested districts (including whether states count ballots in them), same-party top-two contests in California and Washington, and ranked-choice districts, where it uses the post-RCV tally in simulations where RCV is triggered. Its historical House popular vote estimates adjust for uncontested districts.

> FLIPR tries to faithfully replicate the official tally of the House popular vote

<sub>2026-09-29_midterm-waves-are-the-rule-not-the-exception#4</sub>

### 2026-10-17 · [The good, bad and ugly outcomes in the Senate](https://www.natesilver.net/p/the-good-bad-and-ugly-outcomes-in)
**method** · FLIPR 2026 · explicit

In Alaska, FLIPR explicitly plays out ranked-choice reallocations, so minor Republicans' votes mostly transfer to incumbent Dan Sullivan, making FLIPR more bearish on Peltola than models that look at first-round margins.

> I think this is because it’s explicitly playing out the RCV process when other models might not be.

<sub>2026-10-17_the-good-bad-and-ugly-outcomes-in-the-senate#5</sub>

### 2026-10-17 · [The good, bad and ugly outcomes in the Senate](https://www.natesilver.net/p/the-good-bad-and-ugly-outcomes-in)
**parameter or number** · FLIPR 2026 · explicit

Republicans would need roughly a 5-point uniform error to make the House a toss-up in October 2026. Competitive House races are spread evenly across the map, so regional misses tend to offset when overall polls are right.

*Numbers:* uniform error needed for House toss-up = about 5 points (Oct 2026)

> Republicans would need something like a 5-point uniform polling error to turn the House back into a toss-up

<sub>2026-10-17_the-good-bad-and-ugly-outcomes-in-the-senate#8</sub>

### 2026-10-23 · [Do these Senate-governor splits make sense?](https://www.natesilver.net/p/do-these-senate-governor-splits-make)
**method** · FLIPR 2026 · explicit

FLIPR uses Alaska polls that explicitly report post-RCV results as well as first-round polls. It projects first-round shares and simulates ranked-choice rounds, accounting for voters who do not rank every candidate and those who cross party lines, so a candidate projected at 47 percent in round one can still be a 96 percent favorite.

*Numbers:* Kreiss-Tomkins first-round share = 47 percent (Oct 2026); Kreiss-Tomkins win prob = 96 percent (Oct 2026)

> some Alaska polls explicitly forecast the results after RCV, and FLIPR uses these too.

<sub>2026-10-23_do-these-senate-governor-splits-make-sense#3</sub>

### 2026-10-27 · [The 83 remotely competitive House races, according to FLIPR](https://www.natesilver.net/p/the-83-remotely-competitive-house)
**parameter or number** · FLIPR 2026 · explicit

On Oct. 27, 2026 FLIPR Deluxe gave Democrats a 95 percent chance of winning the House, with an average projection of 239 Democratic seats to 196, a net Democratic gain of 24, and a national popular vote of about D+8. Since late August the model had added one Solid D and 14 Likely D seats, and removed three Solid R and nine Likely R seats.

*Numbers:* House D win prob = 95 percent (Oct 27, 2026); projected D seats = 239 seats (Oct 27, 2026); projected net D gain = 24 seats (Oct 27, 2026)

> we’re well past FLIPR’s average projection of Democrats netting 24 House seats and ending up with a total of 239 to Republicans’ 196.

<sub>2026-10-27_the-83-remotely-competitive-house-races-according-to-flipr#1</sub>

### 2026-11-03 · [FLIPR 2026 House forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-house-model)
**parameter or number** · FLIPR 2026 final · inferred_from_chart

Final FLIPR House translation table: at a D+14 to +15 national popular vote, Democrats win 100 percent with about 269 seats.

*Numbers:* D seats at D+14-15 = 269 seats (final)

<sub>2026-11-03_2026-midterm-election-house-forecast-silver-bulletin#2</sub>

### 2026-11-03 · [FLIPR 2026 Senate forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-senate-model)
**parameter or number** · FLIPR 2026 final · inferred_from_chart

FLIPR's final Senate translation from national popular vote to control: D+1-2: 7.2 percent Democratic, 48 seats; D+2-3: 16.9 percent, 49; D+3-4: 31.8 percent, 50; D+4-5: 50.1 percent, 50; D+5-6: 69.2 percent, 51; D+6-7: 83.4 percent, 52; D+7-8: 92.8 percent, 53; D+8-9: 97.2 percent, 54; D+10-11: 99.8 percent, 55; D+14-15: 57 seats. The Senate tipping point was about D+4.5.

*Numbers:* Senate 50/50 point = D+4 to +5 points (final); D win prob at D+6-7 = 83.4 percent (final)

<sub>2026-11-03_2026-midterm-election-senate-forecast-silver-bulletin#2</sub>
