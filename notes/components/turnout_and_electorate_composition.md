# Turnout and electorate composition

21 findings from 12 articles, oldest first.

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**method** · FiveThirtyEight midterm models · explicit

The midterm models project turnout in each race from the eligible population and past midterm and presidential turnout, with competitive races producing higher turnout. Turnout matters for translating the national popular vote into seats.

> Projecting turnout is important in understanding the relationship between the national popular vote and the number of seats that each party might gain or lose.

<sub>fte_midterm-house-senate-governor-methodology#23</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**model change** · 2024 presidential vs 2020 · explicit

The 2024 model removes a component introduced in 2020 that was based on the Cost of Voting Index. It assumed Democrats benefit from changes that liberalize voting rules and Republicans benefit from changes that tighten them.

*Why:* Implied: changed turnout dynamics, with Democrats now the more engaged voters, undercut the assumption.

> I’ve also removed a component of the model that we introduced in 2020 based on the Cost of Voting Index

<sub>2024-06-26_2024-presidential-election-model-methodology-update#8</sub>

### 2024-07-29 · [kamala_mode will be activated tomorrow](https://www.natesilver.net/p/kamala_mode-will-be-activated-tomorrow)
**method** · 2024 presidential · inferred_from_chart

The code screenshot shows a flag use_early_vote="no". Its comment says it served as a failsafe in case early-vote turnout differed from what the turnout model predicted, and that it is being turned off for now. This implies the model contains a turnout model and an optional early-vote input.

*Why:* Failsafe against a turnout model mismatch; not needed in July.

<sub>2024-07-29_kamala-mode-will-be-activated-tomorrow-by-nate-silver#9</sub>

### 2024-09-11 · [A guide to post-debate poll-watching](https://www.natesilver.net/p/a-guide-to-post-debate-poll-watching)
**parameter or number** · 2024 presidential · explicit

As of September 2024, the Silver Bulletin 2024 presidential model projects November turnout of 150-165 million voters.

*Numbers:* Projected turnout = 150 million to 165 million voters (2024 general election)

> our model is projecting November turnout to be somewhere between 150 million and 165 million voters

<sub>2024-09-11_a-guide-to-post-debate-poll-watching-by-nate-silver#17</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**limitation or failure mode** · 2024 presidential · explicit

The simulations do not model swing-state-specific effects, such as a Harris overperformance in swing states from ground game or heavier ad spending. They also do not model countervailing pro-Trump swing-state effects, such as RFK Jr. telling his voters to back Trump only in swing states.

*Numbers:* model odds of Harris EC win / PV loss = about 300-1 odds (Sept 26 2024)

*Why:* These factors are usually minor, but even a few tenths of a point in swing states could make a Democrat-favoring split somewhat more likely.

> There’s one other factor our simulations don’t really consider

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#21</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**adjustment rule** · 2024 presidential · explicit

The only use of early-vote data in the Silver Bulletin 2024 model is this: if the total number of votes already counted in a state exceeds the model's turnout prediction, the model raises its turnout projection for that state.

> we'll up our turnout projections in a state if the total number of votes already counted exceeds our model's prediction.

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#1</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**empirical regularity** · general principle · explicit

In 2016, across 13 states with partisan early-vote breakdowns compiled by Michael McDonald, the D-minus-R early-vote margin missed the final Clinton-minus-Trump margin by an average of 14 points.

*Numbers:* average early vote misprediction = 14 percentage points (2016, 13 states); states with data = 13 states (2016)

*Why:* Early voters are not a representative sample of the electorate.

> On average, the D less R margin in the early vote mispredicted the final Clinton/Trump margin by 14 points!

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#2</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**empirical regularity** · general principle · inferred_from_chart

The 2016 table (University of Florida Election Lab) shows the gap between the D-R early-vote margin and the final margin in each state. It is smallest in Oregon (1.1), Florida (2.6), Arizona (2.9) and Nevada (3.5). It is largest in West Virginia (53.5), Louisiana (25.5) and Nebraska (22.3). In West Virginia, Democrats led the early vote by 12 points while Trump won by 41.7.

*Numbers:* Arizona error = 2.9 percentage points (early vote -6.4, final -3.5); Colorado early vote margin = -0.8 percentage points (final +4.9); Florida error = 2.6 percentage points (early +1.4, final -1.2); Iowa error = 16.1 percentage points (early +6.7); Louisiana error = 25.5 percentage points (early +5.9); Maryland error = 15.2 percentage points (early +41.6, final +26.4); Nebraska error = 22.3 percentage points (early -2.8, final -25.1); Nevada error = 3.5 percentage points (early +5.9, final +2.4); North Carolina error = 13.5 percentage points (final -3.7); California error = 15.4 percentage points (final +30.0); Oregon error = 1.1 percentage points (2016); West Virginia error = 53.5 percentage points (final -41.7)

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#3</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**limitation or failure mode** · general principle · explicit

Early-vote baselines are unstable for several reasons: early-voting rules change, states made one-off COVID provisions in 2020, voters take time to adopt new methods, and parties change their emphasis. Trump discouraged early voting in 2020 but encouraged it in 2024, and Democrats shifted heavily to mail in 2020.

*Why:* You are aiming at a moving target, so comparisons across cycles are unreliable.

> But you're aiming at a moving target.

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#6</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**empirical regularity** · general principle · explicit

Vote method shifts without vote choice shifting. Early voting mostly cannibalizes enthusiastic voters who would have voted on Election Day anyway. In Maryland, the in-person early vote was purple in 2020 and blue in 2022, and the Election Day vote was red in 2020 and blue in 2022, yet Biden in 2020 and Moore in 2022 both won 67-33. Split Ticket's chart puts mail at 53% of ballots in 2020 versus 29% in 2022, and Election Day at 14% versus 52%.

*Numbers:* MD 2020 mail share = 53 percent of ballots (83% D); MD 2020 in-person early share = 32 percent of ballots (53% D); MD 2020 Election Day share = 14 percent of ballots (41% D); MD 2022 mail share = 29 percent of ballots (83% D); MD 2022 early share = 19 percent of ballots (67% D); MD 2022 Election Day share = 52 percent of ballots (57% D); final margin = 67-33 percent (both elections)

*Why:* It's much easier to change how someone votes than who they vote for.

> it's much easier to get someone to change how they vote than who they vote for.

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#9</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**method** · 2024 presidential · explicit

Party-registration early-vote counts do not reveal vote shares, which depend on crossover rates and independents. Silver's worked example: Harris wins 6% of Republicans, Trump wins 3.5% of Democrats, and Harris wins independents by 4. Under those rates, a 38-40-22 D-R-I early-vote breakdown, which looks like R+2, is actually Harris +1.

*Numbers:* Harris share of Republicans = 6 percent (October 2024 national polls); Trump share of Democrats = 3.5 percent (October 2024 national polls); independent margin = 4 points (hypothetical Harris); D-R-I breakdown = 38-40-22 percent (hypothetical early vote); implied result = Harris +1 points (hypothetical)

> a 38-40-22 D-R-I breakdown in the early vote, which looks like a 2-point Republican lead, would actually be Harris +1.

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#10</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**empirical regularity** · general principle · explicit

Independents typically make up a smaller share of early voters than of the overall electorate. They are generally less enthusiastic and more likely to decide late.

> Independent voters are generally less enthusiastic and more likely to make a decision late in the race.

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#11</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**critique of other approach** · general principle · explicit

Early-vote analysis has too many free parameters to be reliable: trend since 2020 versus since 2016, absolute numbers, demographic subgroups, and voter propensity breakdowns. This invites cherry-picking. It also has a bad track record; in 2016 it helped convince the media and Democrats that Clinton was certain to win. Silver calls it a gateway to poll unskewing that adds more noise than signal.

> there are too many floating parameters — too many ways to cherry-pick to tell yourself the narrative you like.

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#12</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**interpretation guidance** · general principle · explicit

Nevada is a partial exception where early vote matters more, because the state traditionally has little Election Day vote, and Jon Ralston's analysis is worth reading. Ambiguities remain even there: Democrats do well in mail early voting, Republicans win in-person early voting, and mail ballots are reported with a lag of several days.

> the early vote in Nevada matters more than elsewhere because it traditionally has little election-day vote.

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#13</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**empirical regularity** · general principle · explicit

Early-vote partisan patterns vary idiosyncratically across similar states. In 2016, North Carolina's early vote was blue while Florida's was purple, because Republicans in Florida traditionally emphasize early voting to older voters. More Republicans than Democrats voted early in Colorado, yet Clinton won the state.

> Similar states can produce surprisingly different patterns.

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#14</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**data source** · Silver models generally · explicit

Silver's models have traditionally used a Gallup poll of voter enthusiasm to calibrate the turnout forecast.

> according to the Gallup poll we've traditionally used to calibrate our turnout forecast.

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#21</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**method** · general principle · explicit

AtlasIntel attributes its 2024 accuracy partly to turnout modeling that anticipated a differential turnout advantage for Trump. Roman argues that recalled-vote weighting makes sense only if partisan turnout is expected to be similar, and helps less when one side is more engaged.

> It makes sense to weight on vote recall if you think turnout will be more or less the same… between Democrats and Republicans.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#16</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**empirical regularity** · 2024 election · explicit

Nonvoters in 2024 leaned toward Trump. The CES survey, once the lone exception, was revised after validation against voter files and now agrees with all other studies.

> all studies except the CES had found non-voters to be GOP-leaning, and now CES does too.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#24</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

FLIPR simulates turnout probabilistically as a post-processing step that does not affect vote shares or win probabilities. Local turnout is benchmarked on race competitiveness, whether a Senate or governor race is on the ballot, past turnout, and estimated voting-eligible population adjusted for growth. National turnout comes from polls asking whether voters are more or less excited than usual. Turnout within a state must be consistent across House, Senate and governor races within bounds, gets a capped correction for differential party turnout, and district totals are scaled to match the authoritative national estimate.

> The turnout simulations are essentially a post-processing step

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#41</sub>

### 2026-09-29 · [Midterm waves are the rule, not the exception](https://www.natesilver.net/p/midterm-waves-are-the-rule-not-the)
**method** · FLIPR 2026 · explicit

FLIPR's House popular vote forecast is the turnout-weighted sum of its 435 district forecasts. It is more Republican than a simple average because Republican districts have grown faster since the 2020 Census (FLIPR embeds a population growth model), Democratic districts have more ineligible residents (non-citizens and disenfranchised felons), turnout rises with competitiveness while safe urban seats are low-turnout, and red-state Senate races lift House turnout in those states.

*Numbers:* FLIPR House popular vote forecast = D+7.9 points (Sept 29, 2026); LV generic ballot = D+9.6 points (Sept 29, 2026)

> our D +7.9 forecast is formulated by summing up FLIPR’s forecast for each district, weighted by projected turnout.

<sub>2026-09-29_midterm-waves-are-the-rule-not-the-exception#3</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**assumption** · Silver hypothesis · explicit

Silver's theory, not built into FLIPR, which makes no turnout assumptions about bias direction: polls oversample enthusiastic and high-social-trust respondents who are also more likely to vote. In high-turnout presidential elections the oversampling dominates and low-propensity Trump voters are missed; in low-turnout elections those voters also stay home, and pollster corrections may overcorrect.

> FLIPR doesn’t actually make any assumptions about turnout.

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#10</sub>
