# Time horizon and forecast dynamics

93 findings from 54 articles, oldest first.

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**parameter or number** · FiveThirtyEight 2016 presidential · explicit

The state polling average is blended with the regression estimate, which gets more weight early and with less polling: 100 percent with no polls, while polls can get up to 95 percent late in an abundantly polled state. Polls-only and now-cast give the regression slightly less weight.

*Numbers:* max poll weight late = 95 percent (2016)

> The polling average can get as much as 95 percent of the weight late in the race in a state with abundant polling.

<sub>fte_2016-general-election-forecast-users-guide#15</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**parameter or number** · FiveThirtyEight 2016 presidential · explicit

In late June 2016, polls-plus gave fundamentals 35 to 40 percent of the weight, declining to zero by Election Day. The fundamentals weight is constrained against overfitting using a calculation derived from Lauderdale and Linzer (2014).

*Numbers:* fundamentals weight late June = 35-40 percent (2016 polls-plus)

*Why:* Fundamentals forecasts are prone to overfitting.

> Because fundamentals forecasts are subject to overfitting, the weight assigned to the fundamentals is constrained, based on a calculation derived from a 2014 paper by Lauderdale and Linzer .)

<sub>fte_2016-general-election-forecast-users-guide#17</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**design principle** · FiveThirtyEight 2016 presidential · explicit

Be conservative early and aggressive late: summer poll fluctuations are often noise or short-term bounces, so the model reacts conservatively, while late fluctuations are more meaningful and the model reacts more aggressively.

> Fluctuations late in the race are more meaningful, and the model will be more aggressive.

<sub>fte_2016-general-election-forecast-users-guide#26</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**parameter or number** · FiveThirtyEight 2020 presidential · explicit

The 'enhanced snapshot' for each state blends the state's polling average with the ensemble estimate, with poll weight depending on polling volume and recency. At the 2020 launch (Aug. 12) about 55 percent of the weight went to polls in the average state; in well-polled states near the end, as much as 97 to 98 percent. States without polls use the ensemble alone.

*Numbers:* poll weight in average state at launch = around 55 percent (Aug 12, 2020); poll weight late in well-polled states = 97-98 percent (end of campaign)

> As of the forecast launch (Aug. 12), around 55 percent of the weight goes to the polling average rather than to the ensemble in the average state.

<sub>fte_2020-presidential-forecast-methodology#12</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**parameter or number** · FiveThirtyEight 2020 presidential · inferred_from_chart

Published schedule of weight on polls versus fundamentals by days until the election: 0 days 100/0; 5 days 97/3; 10 days 94/6; 25 days 89/11; 50 days 84/16; 75 days 79/21; 100 days 74/26; 150 days 65/35; 200 days 57/43; 250 days 47/53. At the 2020 launch it was 77/23. Fundamentals help the trailing side at the margin, and higher-elasticity states are shifted slightly more.

*Numbers:* poll weight at 100 days = 74 percent (2020 schedule); poll weight at 50 days = 84 percent (2020 schedule); poll weight at 25 days = 89 percent (2020 schedule); poll weight at 0 days = 100 percent (2020 schedule); poll weight at 250 days = 47 percent (2020 schedule)

*Why:* Fundamentals have more misses once data before 1948 is included.

<sub>fte_2020-presidential-forecast-methodology#18</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**parameter or number** · FiveThirtyEight 2020 presidential · explicit

National drift is calculated as Constant x (Days Until Election)^(1/3) x Uncertainty Index. The cube root implies polls do not become more accurate linearly but sharply toward the end.

*Numbers:* drift exponent on days = 1/3 power (cube root)

*Why:* August is still early as far as polling goes.

> Constant x (Days Until Election)^⅓ x Uncertainty Index

<sub>fte_2020-presidential-forecast-methodology#21</sub>

### 2023-09-18 · [Is a Trump-Biden rematch inevitable?](https://www.natesilver.net/p/is-a-trump-biden-rematch-inevitable)
**interpretation guidance** · general principle · explicit

Silver says the FiveThirtyEight early-polling curve understates a leader's chances later in the cycle. It was built on January-June polling of the pre-election year, and polling later in the year (with the leader still strong) should be more predictive.

*Why:* Polls gain predictive power as the calendar advances.

> It pertains to polling conducted in the first half of the year before the election (that is, January-June). We’re now in the second half of the year, and Trump’s polling has only gotten stronger.

<sub>2023-09-18_is-a-trump-biden-rematch-inevitable-by-nate-silver#2</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**empirical regularity** · general principle · explicit

Polls taken in March of an election year are historically not very reliable predictors of November results. One reason is that campaigns have time to change course and tweak strategies that are not working.

*Why:* Campaigns can respond to bad polling.

> one reason polls in March aren't historically all that reliable is because campaigns have the opportunity to change course and tweak a strategy that isn't working.

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#8</sub>

### 2024-04-17 · [Announcing 2024 election model plans](https://www.natesilver.net/p/announcing-2024-election-model-plans)
**parameter or number** · 2024 presidential · explicit

The 2024 model update cadence is about once a week from launch through Labor Day, about twice a week from Labor Day through mid-October, and about three times a week or 'as needed' from mid-October through Nov. 5. Bonus updates may follow major news or significant polling shifts.

*Numbers:* updates launch-Labor Day = ~1 per week (2024); updates Labor Day-mid-October = ~2 per week (2024); updates mid-October-Nov. 5 = ~3 per week (2024, or as needed)

*Why:* A 'slow food' approach gives time for context. Changing priors after every poll has little value unless you are betting.

> Unless you're literally betting on the outcome, there's not a lot of value in changing your priors after every new poll that comes out.

<sub>2024-04-17_announcing-2024-election-model-plans-by-nate-silver#4</sub>

### 2024-04-17 · [Announcing 2024 election model plans](https://www.natesilver.net/p/announcing-2024-election-model-plans)
**assumption** · 2024 presidential · explicit

For the 2024 Biden-Trump rematch, Silver expects the fundamentals to be fairly 'locked in', so many polling shifts will be noise.

*Why:* A rematch between two well-known candidates.

> the fundamentals of a Biden-Trump rematch are likely to be fairly "locked in" and polling shifts will often be noise.

<sub>2024-04-17_announcing-2024-election-model-plans-by-nate-silver#5</sub>

### 2024-06-22 · [The model is coming](https://www.natesilver.net/p/the-model-is-coming)
**method** · 2024 presidential · explicit

Updates to the Silver Bulletin 2024 presidential forecast were planned for about once a week at launch, becoming more frequent as election day approaches.

*Numbers:* initial update frequency = once a week or so updates (Early phase of the 2024 forecast after the late-June launch)

*Why:* Silver describes a "slow food" approach and wants to keep the model from consuming all his other newsletter work.

> with updates once a week or so initially before accelerating as the election approaches

<sub>2024-06-22_the-model-is-coming-by-nate-silver-silver-bulletin#1</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**empirical regularity** · 2024 presidential · explicit

Poll stability to date predicts future stability. Highly stable races such as 2012 feature many 'fake turning points' that don't move the race. Volatile years such as 2016 and the uncertain 2020 warranted higher model uncertainty.

> The polls have been extremely stable so far, which tends to predict future stability.

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#50</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**critique of other approach** · 538 2024 vs Silver Bulletin 2024 · explicit

The 2024 538 model assumes polls could move a lot before November, giving very wide confidence intervals. Silver disagrees because polls move much less in recent elections than they once did, likely due to higher polarization, though he calls the assumption within the bounds of reasonableness.

*Why:* Polls have barely moved in 2024, and polarization reduces volatility.

> the polls move much less in recent elections than they once did — indeed, they've barely changed this year at all — likely as a result of higher polarization

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#15</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**adjustment rule** · 2024 presidential · explicit

Drift is scaled by the uncertainty index. A low index (as in 2024, with very steady polling) yields smaller drift. The uncertainty index affects Election Day error only at the margin.

*Why:* Steady polling usually predicts continued steadiness.

> The uncertainty index also affects the model's estimate of Election Day error, but only at the margin.

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#28</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**interpretation guidance** · 2024 presidential · explicit

Because drift is low relative to Election Day error in 2024, the model will become only somewhat, not dramatically, more confident as Election Day approaches.

*Why:* Most remaining uncertainty is Election Day error, which doesn't shrink over time.

> Since "drift" is low this year, the model won't get that much more confident as we approach Election Day.

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#30</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**parameter or number** · 2024 presidential · explicit

Before fully accounting for the debate, the model implied roughly a 25% chance that Biden would lead the Silver Bulletin Electoral College forecast on Election Day morning. Silver would take the under given the debate.

*Numbers:* P(Biden ahead in EC forecast on Election Day) = on the order of 25 percent (as of July 1, 2024, debate not fully priced in)

> the chance that Biden will be ahead in the Electoral College forecast at Silver Bulletin on Election Day morning are somewhere on the order of 25 percent

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#32</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**method** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model first builds a polling-based 'snapshot' of the current race, then regresses that snapshot toward a prior based on 'fundamentals'.

> First, we take a current “snapshot” of the race — which is based on polling, although with some fancy adjustments to smooth out the data in states where there isn’t much polling — and then regress it toward a prior

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#0</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**parameter or number** · 2024 presidential · explicit

As of July 18, 2024, the Silver Bulletin model blends the polling snapshot and the fundamentals roughly 70/30 in favor of polls. The national calculation is (-2.0 x 70%) + (2.5 x 30%) = -0.6, so Biden is projected to lose the popular vote by about 0.6 points.

*Numbers:* snapshot weight = ~70 % (July 18, 2024, ~110 days out); fundamentals weight = ~30 % (July 18, 2024); polling snapshot national margin = -2.0 percentage points (Biden) (July 18, 2024); fundamentals national margin = +2.5 percentage points (Biden) (July 18, 2024); blended national margin = -0.6 percentage points (Biden) (July 18, 2024)

> Currently, our model uses roughly a 70/30 blend of the snapshot and the fundamentals.

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#3</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**critique of other approach** · 538 2024 (Morris) · inferred_from_chart

Morris often cites a 538 chart of expected absolute change in state polling-average margins (1948-2020) by days before the election. It shows about 9-10 points of expected change from 300 to about 150 days out and about 9 points at 155 days. The change declines slowly to about 8 points near 75 days, then falls rapidly to 0 on Election Day.

*Numbers:* expected absolute change at 155 days = ~9 percentage points of margin (538 chart, state polls 1948-2020); expected absolute change 200-300 days = ~9-10.5 percentage points of margin (538 chart); inflection point = ~75 days before election (roughly late August)

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#11</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**critique of other approach** · 538 2024 (Morris) · explicit

Silver says 538's drift chart badly exaggerates future poll movement because it is based on state polling averages. Those are noisy since each state is polled only a few times a month or less, so much of the measured movement is statistical noise rather than real change in the race.

> Much of what a state polling average captures is just statistical noise, not real movement in the race.

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#12</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**critique of other approach** · 538 2024 (Morris) · explicit

Silver says the 538 2024 model gives polls very little influence before roughly Labor Day. Its forecast moved toward Biden after the June 2024 debate even though 538's own polling average moved about 2 points toward Trump.

*Numbers:* 538 polling average shift toward Trump since debate = 2 percentage points (late June to mid-July 2024)

> Biden has actually gained ground in their forecast over the past few weeks even though their polling average has moved toward Trump by 2 points!

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#13</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**critique of other approach** · 538 2024 (Morris) · explicit

Nationally, 538's full forecast was Biden +2.6. That falls between its Election Day polling forecast (Trump +1.9) and its fundamentals (Biden +3.3), which implies about a 15:85 polls-to-fundamentals weighting.

*Numbers:* 538 national full forecast = D+2.6 percentage points (July 2024); 538 national polling average today = R+2.7 percentage points (538 chart); 538 adjusted / Election Day polling forecast = R+1.9 percentage points (538 chart); 538 national fundamentals = D+3.3 percentage points (538 chart); implied 538 weights = 15:85 polls:fundamentals (July 2024)

> Whereas our mix is roughly 70:30 in favor of polls, theirs is apparently about 15:85 in favor of fundamentals.

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#14</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**interpretation guidance** · 2024 presidential · explicit

Higher forecast uncertainty spreads tipping-point probability across more states, lowering any single state's tipping-point chance.

> meaning that it will be harder to pinpoint the tipping-point state with as much precision

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#16</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**empirical regularity** · 2024 presidential · inferred_from_chart

The forecast's projected two-party race was tighter than the current polls. Trump led Biden 45.2% to 41.2% in the national polling average on July 21, but the model's predicted popular vote was Trump 47.5% to Biden 46.7%. Projected shares for the major candidates exceed their polling numbers as undecided and third-party voters are reallocated, and the margin narrows, possibly through fundamentals or reversion.

*Numbers:* Trump national polling average = 45.2% percent (July 21, 2024); Biden national polling average = 41.2% percent (July 21, 2024); Trump predicted vote share = 47.5% percent (July 21, 2024); Biden predicted vote share = 46.7% percent (July 21, 2024); Trump popular vote win probability = 57.3% probability (July 21, 2024)

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#12</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**empirical regularity** · 2024 presidential · inferred_from_chart

The forecast history from launch (late June) to July 21 shows Trump's win probability moving from about 65% to about 72% after the first debate, and staying roughly in the 69-74% range through the assassination attempt and VP pick. Before the debate the forecast had been stable at roughly 63-67%.

*Numbers:* Trump win probability pre-debate = ~63-67% probability (June 2024); Trump win probability post-debate = ~69-74% probability (July 2024)

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#24</sub>

### 2024-07-29 · [kamala_mode will be activated tomorrow](https://www.natesilver.net/p/kamala_mode-will-be-activated-tomorrow)
**interpretation guidance** · 2024 presidential · explicit

Right after relaunch with Harris, the Silver Bulletin presidential model was expected to be more likely than usual to show further shifts over the following week or so. The baseline rested on limited new data.

*Numbers:* period of elevated volatility = next week or so (after July 30, 2024 relaunch)

*Why:* Only a short window of Harris polling was available.

> the model is more likely than usual to show further shifts over the course of the next week or so

<sub>2024-07-29_kamala-mode-will-be-activated-tomorrow-by-nate-silver#7</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**parameter or number** · 2024 presidential · explicit

The model projects polling averages forward to Election Day (November 5) through a series of adjustments before running the simulations.

> after making a bunch of fancy adjustments to go from our polling averages to predictions for November 5th

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#14</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**parameter or number** · 2024 presidential · inferred_from_chart

The Silver Bulletin forecast history chart shows Trump at about 62 percent to win before the model's late-July launch. Harris overtook him in early August and held roughly 53-57 percent through Aug 24, 2024.

*Numbers:* Trump win probability pre-launch = ~62 percent (chart, late July 2024)

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#25</sub>

### 2024-08-26 · [How big will the bounce be?](https://www.natesilver.net/p/how-big-will-the-bounce-be)
**interpretation guidance** · 2024 presidential · explicit

As of Aug 26, 2024, Harris was about 4 points up nationally and her forecast odds were essentially unchanged from before the DNC, consistent with an expected-size bounce being offset by the adjustment. The forecast had her as an ever-so-slight favorite in a near-tossup.

*Numbers:* Harris national lead = about 4 points (post-DNC, Aug 26 2024)

> Harris is up by about 4 points nationally and her odds of winning in our forecast are basically unchanged from before the convention

<sub>2024-08-26_how-big-will-the-bounce-be-by-eli-mckown-dawson#19</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**empirical regularity** · 2024 presidential · explicit

Because pre-landmark polls are discounted, the 2024 model moved a lot on new Pennsylvania polling in late August 2024. Silver describes this as naturally self-correcting: better Pennsylvania polls for Harris would raise her numbers.

> it’s also naturally self-correcting (e.g. if/when Kamala Harris gets some better Pennsylvania polls, her numbers will improve)

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#5</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**interpretation guidance** · 2024 presidential · explicit

Because of the fundamentals prior and the convention adjustment, in late August 2024 the model expected Trump to more likely than not outperform his current polling. This is a forward projection of the race, not an assumption that polls are biased today.

> That does not mean it assumes the polls would be predictably biased if you held an election today — but the election isn’t today.

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#17</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**parameter or number** · 2024 presidential · explicit

The forecast reverts the polls toward the fundamentals prior. In early September 2024 the fundamentals got about 20% of the weight, declining to 0% (polls-only) by Election Day.

*Numbers:* fundamentals weight = about 20 percent (as of ~Sept 1-3, 2024); fundamentals weight on Election Day = 0 percent (polls-only)

> As of now, the fundamentals get about 20 percent of the weight, but the model will revert to "polls-only" by Election Day.

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#12</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**empirical regularity** · 2024 presidential · explicit

Silver gives a model-behavior scenario: if every poll through November exactly matched the Sept 1 averages (national D+3.5, Michigan D+1.9, North Carolina R+0.3, and so on), Harris would eventually become a 60%+ favorite. She would not be a heavy favorite, because of the close race and the risk of systematic polling error.

*Numbers:* Harris win probability under hold-steady scenario = 60 percent or higher percent (eventually, by Election Day)

*Why:* Bounce adjustment decay, fading fundamentals weight and shrinking uncertainty all help a steady leader.

> probably enough to take the model out of what we consider to be toss-up range, meaning she'd be a 60 percent favorite or higher.

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#14</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**parameter or number** · 2024 presidential · inferred_from_chart

Reference points on the forecast trajectory: at the July 30 relaunch national polls were roughly tied and Harris was a slight Electoral College underdog. She peaked near 55-57% in mid-August. Before the June 28 debate Biden was about a 2:1 underdog.

*Numbers:* Biden pre-debate odds = about 2:1 underdog odds (before June 28, 2024); Harris peak win probability = ~56-57 percent (mid-August per chart)

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#26</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**adjustment rule** · 2024 presidential · explicit

The convention bounce adjustment in the 2024 Silver Bulletin model is temporary. As of Sept. 6, 2024, it would begin to work its way out of the model over the following week or two, roughly 2.5–4 weeks after the DNC started on Aug. 19.

*Numbers:* time for convention bounce adjustment to phase out = the next week or two weeks (from Sept. 6, 2024)

> it will begin to work its way out of the model over the course of the next week or two.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#1</sub>

### 2024-09-07 · [Oops! I made the convention bounce adjustment disappear.](https://www.natesilver.net/p/oops-i-made-the-convention-bounce)
**design principle** · general principle · explicit

Forecasts should behave like a random walk, with no predictable direction of future movement. An asymmetric convention bounce rule like 538's means candidates on average look better after their conventions than before, which introduces autocorrelation.

*Why:* Predictable drift violates the martingale property of good forecasts.

> candidates will be in a better position in their forecast after their conventions than before, which introduces autocorrelation and violates the notion that forecasts should be a random walk

<sub>2024-09-07_oops-i-made-the-convention-bounce-adjustment-disappear#13</sub>

### 2024-09-11 · [A guide to post-debate poll-watching](https://www.natesilver.net/p/a-guide-to-post-debate-poll-watching)
**parameter or number** · 2024 presidential · inferred_from_chart

The September 11, 2024 poll-shift table shows Harris win probabilities by uniform shift from current polls. Toward Harris: +5 gives 73.9%, +4 gives 67.5%, +3 gives 60.4%, +2 gives 52.9%, and +1 gives 45.5%. The current forecast is 38.1% (Trump 61.6%). Toward Trump: +1 gives 31.2%, +2 gives 25.1%, +3 gives 19.7%, +4 gives 14.9%, and +5 gives 11.1%. Each point near the center is worth about 7-8 percentage points of win probability, with the effect tapering in the tails.

*Numbers:* Harris +5 = 73.9 percent (Harris win probability); Harris +4 = 67.5 percent; Harris +3 = 60.4 percent; Harris +2 = 52.9 percent; Harris +1 = 45.5 percent; Current = 38.1 percent (Trump 61.6%); Trump +1 = 31.2 percent (Harris win probability); Trump +2 = 25.1 percent; Trump +3 = 19.7 percent; Trump +4 = 14.9 percent; Trump +5 = 11.1 percent (Trump 88.7%)

<sub>2024-09-11_a-guide-to-post-debate-poll-watching-by-nate-silver#19</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**empirical regularity** · 2024 presidential · explicit

Several strong Times/Siena Sunbelt polls (Trump +2 to +5) and a MassINC Wisconsin poll (Harris +6 to 7) produced only incremental moves in state win probabilities. Harris moved from 40% to 37% in NC, 37% to 34% in GA, 37% to 32% in AZ, and 57% to 60% in WI.

*Numbers:* NC Harris win prob before/after = 40 -> 37 percent (after Times/Siena poll, Sep 23, 2024); GA Harris win prob before/after = 37 -> 34 percent (after Times/Siena poll); AZ Harris win prob before/after = 37 -> 32 percent (after Times/Siena poll); WI Harris win prob before/after = 57 -> 60 percent (after MassINC poll)

*Why:* Polls are averaged with other polls and with priors.

> Harris's win probability in North Carolina fell from 40 percent to 37 percent, in Georgia from 37 percent to 34 percent and in Arizona from 37 percent to 32 percent

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#4</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**empirical regularity** · 2024 presidential · explicit

Changes in the Silver Bulletin model are usually incremental. The exceptions are inflection points after major events such as debates.

> Outside of inflection points following major events like debates, changes in the model tend to be incremental.

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#5</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**method** · 2024 presidential · explicit

The fundamentals prior and the regression component get less weight as Election Day approaches. By Election Day the model defaults toward being more 'polls-only'.

> Those factors play less and less of a role as the model defaults toward being more “polls-only” by Election Day

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#4</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**assumption** · 2024 presidential · explicit

With 38 days left and no debates scheduled, most remaining forecast uncertainty comes from close polls and ordinary polling error rather than from the potential for October surprises.

*Numbers:* days remaining = 38 days (as of Sept 29 2024)

> most of it is just because the polls are really close, will probably remain close, and are frequently in error to some degree even when they aren’t that close.

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#16</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**method** · 2024 presidential · explicit

During the final weeks of the campaign the model is updated roughly daily.

> We’ll be updating the model basically every day during these final 38 days

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#19</sub>

### 2024-10-01 · [SBSQ #13: October Surprise edition](https://www.natesilver.net/p/sbsq-13-october-surprise-edition)
**empirical regularity** · 2024 presidential · explicit

The peaks of the two 2024 models ran in opposite directions. Harris peaked at 64 percent in the revised 538 forecast, while Trump peaked at 64 percent in the Silver Bulletin forecast. A reader noted that Harris was as low as 40% in Silver Bulletin when 538 had her at 60%.

*Numbers:* Harris peak in 538 = 64 percent (538 2024 revised model); Trump peak in Silver Bulletin = 64 percent (Silver Bulletin 2024 model, around the post-convention period); Harris low in Silver Bulletin (reader claim) = 40 percent (Same period, when 538 had Harris at 60%); Harris in 538 at same time (reader claim) = 60 percent (Same period)

*Why:* Silver says the Silver Bulletin forecast converged with 538's as much as 538's converged with his. The questioner speculated that the Silver Bulletin convention bounce adjustment was heavily weighted.

> Harris peaked at 64 percent in their forecast while Trump peaked at 64 percent in ours.

<sub>2024-10-01_sbsq-13-october-surprise-edition-by-nate-silver#5</sub>

### 2024-10-08 · [55/45 is a really close race](https://www.natesilver.net/p/5545-is-a-really-close-race)
**empirical regularity** · 2024 presidential · explicit

The Silver Bulletin 2024 popular-vote forecast barely moved from model launch to Oct 7, 2024, apart from a jump when RFK Jr. dropped out and both candidates gained. The Electoral College probability, by contrast, swung between roughly 35% and 64% for Harris, because of the steep popular-vote-to-EC mapping.

*Numbers:* Harris projected popular vote = 50.8 percent (Oct 7, 2024); Trump projected popular vote = 48.1 percent (Oct 7, 2024); Harris win probability = 54.7 percent (Oct 7, 2024); Trump win probability = 45.0 percent (Oct 7, 2024); Trump peak win probability = ~64 percent (around Sept 9, 2024, chart); Trump win probability at launch = ~62 percent (late July 2024, chart)

> Our forecast of the popular vote has barely moved, other than when RFK Jr. quit the race and both candidates gained ground

<sub>2024-10-08_5545-is-a-really-close-race-by-nate-silver#10</sub>

### 2024-10-08 · [55/45 is a really close race](https://www.natesilver.net/p/5545-is-a-really-close-race)
**empirical regularity** · 2024 presidential · explicit

With four weeks left, Silver expects the 2024 probabilities to stay in the 50/50 to 60/40 range. His reason is that there are extremely few undecided voters: Harris plus Trump total 95.5% in the Silver Bulletin national average, and third parties typically take another 1-2%.

*Numbers:* Harris+Trump combined share = 95.5 percent (national polling average, Oct 2024); typical third-party share = 1 or 2 percent (general)

*Why:* Not enough votes are in play to move the needle.

> there just aren't enough votes in play to really move the needle

<sub>2024-10-08_5545-is-a-really-close-race-by-nate-silver#14</sub>

### 2024-10-08 · [55/45 is a really close race](https://www.natesilver.net/p/5545-is-a-really-close-race)
**assumption** · 2024 presidential · explicit

In the weeks before the Sept 10, 2024 debate, the Silver Bulletin model implicitly hypothesized that momentum was shifting against Harris. Silver notes this hypothesis cannot be properly tested because the debate intervened.

> The model's hypothesis that the momentum had been shifting against Harris before the debate will never quite be appropriately tested

<sub>2024-10-08_5545-is-a-really-close-race-by-nate-silver#18</sub>

### 2024-10-09 · [When you should panic about the polls](https://www.natesilver.net/p/when-you-should-panic-about-the-polls)
**adjustment rule** · 2024 presidential · explicit

The Silver Bulletin model is designed to be more aggressive toward the very end of the race, specifically in the last week or week-and-a-half. Four weeks out is too soon for this.

*Numbers:* late-aggressiveness window = 1-1.5 weeks (before Election Day); too early = 4 weeks (not yet in aggressive window)

*Why:* There is no time left for mean reversion, and some voters decide at the very end.

> the model is designed to be more aggressive toward the very end of the race. But by this I mean specifically the last week or week-and-a-half: four weeks out is a little too soon.

<sub>2024-10-09_when-you-should-panic-about-the-polls-by-nate-silver#5</sub>

### 2024-10-09 · [When you should panic about the polls](https://www.natesilver.net/p/when-you-should-panic-about-the-polls)
**assumption** · 2024 presidential · explicit

Earlier in the race, the Silver Bulletin model assumes temporary disruptions to polling tend to mean-revert toward the fundamentals. Late in the race there is no time for this reversion, so shocks are taken more at face value.

*Why:* A temporary shock at the top of voters' minds on Election Day can decide the outcome.

> there's no longer time for any mean reversion

<sub>2024-10-09_when-you-should-panic-about-the-polls-by-nate-silver#6</sub>

### 2024-10-09 · [When you should panic about the polls](https://www.natesilver.net/p/when-you-should-panic-about-the-polls)
**interpretation guidance** · 2024 presidential · explicit

Example of how the model responds to new polls: a batch of Quinnipiac polls (Trump +3 in Michigan, Trump +2 in Wisconsin, Harris +3 in Pennsylvania) moved the forecast only modestly. Harris's Wisconsin average lead fell from 1.9 to 1.5 points and her Wisconsin win probability from 60% to 57%. Her Michigan win probability fell from 64% to 60%.

*Numbers:* WI Harris lead before = 1.9 percentage points (Oct 2024); WI Harris lead after = 1.5 percentage points (Oct 2024); WI win prob before/after = 60 -> 57 percent (Harris); MI win prob before/after = 64 -> 60 percent (Harris)

*Why:* Dozens of polls are released every week, so one firm's batch moves the average only a little.

> the new polling lowered Harris's lead from 1.9 points to 1.5. In turn, that reduced Harris's win probability in the Badger State from 60 to 57.

<sub>2024-10-09_when-you-should-panic-about-the-polls-by-nate-silver#9</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**design principle** · 2024 presidential · explicit

The Silver Bulletin election forecasts are explicitly designed to be 'momentumless'. The best prediction of what the forecast will say tomorrow is what it says today, so the forecast avoids autocorrelation and behaves like a martingale.

*Why:* Predictable future movement would mean the forecast is leaving information on the table.

> The Silver Bulletin election forecasts are explicitly designed to be momentumless. In other words, the best prediction of what the forecast says tomorrow is what it says today

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#0</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**empirical regularity** · general principle · explicit

As an empirical matter, polling averages more closely resemble random walks than trend-continuing (momentum) processes, at least over the medium term. Silver first concluded this in a 2010 analysis.

*Why:* The behavior is analogous to efficient markets.

> polling generally does not show this pattern, at least not over the medium term. Instead, as an empirical matter, polling averages more closely resemble random walks.

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#9</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**empirical regularity** · 2024 presidential · explicit

Outside of major events like debates, the Silver Bulletin presidential model typically does not move very much from day to day.

> Outside of major events like debates, the model typically does not move very much from day to day.

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#10</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**parameter or number** · 2024 presidential · explicit

Trump's lowest win probability in the Silver Bulletin model was 41.7% on Sept. 27, 2024, about two weeks after the debate. From then to Oct. 17 his odds rose day-over-day 12 times, fell 7 times and were unchanged once. The nominal favorite had changed four times during the cycle.

*Numbers:* Trump low = 41.7 percent (Sept. 27, 2024); up days = 12 days; down days = 7 days; unchanged days = 1 days; lead changes = 4 (2024 cycle as of Oct. 17)

*Why:* Silver wants to avoid ignoring a slow, incremental trend.

> his odds have improved day-over-day 12 times, decreased 7 times, and been unchanged once

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#23</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**empirical regularity** · 2024 presidential · inferred_from_chart

The Silver Bulletin forecast-history chart shows Trump at about 62% at model launch in late July 2024, Harris overtaking him in early August, Trump peaking around 64% near Sept. 8 before the debate, a drop after the Sept. 10 debate, and convergence near 50/50 by Oct. 17. Kennedy's probability shows at roughly 0% until he dropped out in late August.

*Numbers:* Trump at launch = ~62 percent (Late July 2024); Trump pre-debate peak = ~64 percent (Early September 2024)

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#24</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**empirical regularity** · 2024 presidential · inferred_from_chart

The state-level LV shift toward Trump grew steadily through the 2024 campaign: 0.1 points in July, about 0.3 in August, about 0.65 in September and about 0.7 in October. The national LV shift toward Harris was about 0.45 in July, about 0.7 in August, about 0.35 in September and about 0.2 in October.

*Numbers:* State LV shift, July = 0.1 percentage points (R) (State polls, LV vs RV); State LV shift, October = 0.7 percentage points (R) (State polls, LV vs RV); State LV shift, Aug/Sep = ~0.33 / ~0.65 percentage points (R) (Read from chart); National LV shift, Jul/Aug/Sep/Oct = ~-0.44 / ~-0.68 / ~-0.36 / ~-0.22 percentage points (negative = D) (Read from chart)

> In July, LV polls at the state level were only 0.1 points more favorable to Trump than RV polls. Three months later? Trump does 0.7 points better in state-level LV polls.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#9</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**parameter or number** · 2024 presidential · explicit

In the 2024 Silver Bulletin presidential model, the Selzer Iowa poll (Harris +3) raised Harris's chance of winning Iowa from 9% to 17%. A single high-quality poll in a sparsely polled state can nearly double a state win probability.

*Numbers:* Harris Iowa win probability before Selzer poll = 9 percent (Nov 2, 2024); Harris Iowa win probability after Selzer poll = 17 percent (Nov 2, 2024 evening update); Selzer poll result = Harris 47, Trump 44 percent (Final Selzer/Des Moines Register Iowa poll, 2024)

> Harris's chances of winning Iowa nearly doubled in our model from 9 percent to 17 percent tonight

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#1</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**empirical regularity** · 2024 presidential · explicit

After relaunching with Harris, the 2024 Silver Bulletin forecast was stable: it spent 87 of 98 days within the 60/40 range in one direction or the other. Per the chart, it began around Trump 62% / Harris 38% at launch in late July, peaked near Trump 64% in early September before the Harris-Trump debate, peaked near Harris 58% in late September, and finished at Harris 50.0% / Trump 49.6%.

*Numbers:* days within 60/40 range = 87 of 98 days (since model relaunch, 2024); final Harris probability (chart) = 50.0 percent (Nov 5, 2024); final Trump probability (chart) = 49.6 percent (Nov 5, 2024)

> the model has spent 87 of 98 days since we relaunched in the 60/40 range in one direction or another.

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#10</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**empirical regularity** · 2024 presidential · explicit

Silver describes the 2024 race as following a sine-wave-like pattern, with small shifts of momentum roughly every three weeks. He is generally distrustful of 'momentum' because what goes up tends to come back down, but he notes that at the very end of a race there is no time for reversion.

*Numbers:* momentum cycle = roughly every three weeks weeks (2024 race)

*Why:* Polling shifts tend to mean-revert.

> under most circumstances, I'm actually pretty distrustful of the concept of "momentum" in the context of elections. Because what goes up tends to come right back down

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#11</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**design principle** · 2024 presidential · inferred_from_chart

The 2024 Silver Bulletin model places less weight on fundamentals as Election Day approaches, reaching roughly zero on Election Day.

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#17</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**empirical regularity** · 2024 presidential · inferred_from_chart

The 2024 Silver Bulletin forecast launched with Trump at about 62% against Harris at about 37%. Harris led through August; Trump peaked near 64% around September 8, just before the debate; Harris peaked near 58% in late September; the race converged to about 50-50 by November 5.

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#31</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**model change** · 538 2008 vs 2012+ · explicit

Before 2012, the presidential forecast's mean-reversion component reverted the polling margin toward zero, i.e. a tied race. From 2012 on, it reverts toward a fundamentals-based prior.

> Before 2012, the forecast included a mean-reversion component but the forecast was just reverted toward zero — not toward the “fundamentals”.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#3</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**method** · 2024 presidential · explicit

The 2024 Silver Bulletin presidential model reduces the weight on fundamentals gradually over the campaign until it reaches zero on Election Day. By then the forecast is polls-only, although adjustments such as the convention bounce apply earlier.

*Numbers:* fundamentals weight on Election Day = 0 (2024 Silver Bulletin presidential model)

*Why:* It avoids overfitting and p-hacking across many possible fundamentals specifications, and it is easier to explain.

> it’s also just a little bit easier to explain a model that becomes “polls-only” by election day.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#10</sub>

### 2025-03-22 · [How low is Trump's popularity floor?](https://www.natesilver.net/p/how-low-is-trumps-popularity-floor)
**design principle** · general principle · explicit

Silver warns against crude linear extrapolation of early approval trends. Extrapolating Trump's roughly 7-points-per-month decline would give -27.6 by July 21 and -51.2 by Nov. 21, 2025, which he calls almost certainly bad predictions. Early declines are typical for new presidents and tend not to continue at the same rate.

*Numbers:* extrapolated net approval = -27.6 percentage points (July 21, 2025 under linear extrapolation); extrapolated net approval = -51.2 percentage points (Nov. 21, 2025 under linear extrapolation)

*Why:* The early decline is typical for new presidents, so it is not evidence of a continuing trend.

> such crude linear extrapolation will almost certainly lead to bad predictions

<sub>2025-03-22_how-low-is-trumps-popularity-floor-by-nate-silver#3</sub>

### 2025-06-02 · [SBSQ #21: Why young men don't like Democrats](https://www.natesilver.net/p/sbsq-21-why-young-men-dont-like-democrats)
**limitation or failure mode** · ESPN Analytics (critique); general principle · explicit

ESPN's NBA win probability model appears to move too quickly off its priors (pregame odds) early in the game, underrating comebacks. Most 'improbable' comebacks are by teams that were favored pregame. The analogous lesson for forecasting is not to abandon priors too fast in response to early data.

*Why:* Assessments found ESPN overreacts to early-game events.

> It sounds like ESPN's models move too quickly off their priors early in the game, and that most of the "improbable" comebacks are by teams that were favored pregame.

<sub>2025-06-02_sbsq-21-why-young-men-dont-like-democrats#5</sub>

### 2025-09-09 · [Is Susan Collins toast?](https://www.natesilver.net/p/is-susan-collins-toast)
**parameter or number** · FLIPR 2026 · explicit

The Silver Bulletin midterm forecast for 2026 is scheduled to officially launch in summer 2026.

> remind you to check in next summer once we officially launch our midterm forecast.

<sub>2025-09-09_is-susan-collins-toast-by-eli-mckown-dawson#12</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**parameter or number** · Silver Bulletin 2026 generic ballot average · explicit

The margin of error of the generic ballot average against the House popular vote shrinks from 5.7 points in late January to 3.8 points on Election Day.

*Numbers:* Election Day margin of error = 3.8 percentage points (generic ballot vs House popular vote)

> the generic ballot is fairly accurate on election day, with the margin of error shrinking to just 3.8 points.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#9</sub>

### 2026-04-21 · [SBSQ #31: Trump is super unpopular. So why don’t Democrats have a bigger lead?](https://www.natesilver.net/p/sbsq-31-trump-is-super-unpopular)
**assumption** · FLIPR 2026 midterms model · explicit

Silver did not plan to launch the 2026 midterm model before early June, because candidates in key races and even district lines were not yet set; the work is mostly data gathering since the model was built for 2018 and 2022.

> The work is mostly about data gathering, since I put a lot of effort into our midterm model ahead of 2018 and 2022

<sub>2026-04-21_sbsq-31-trump-is-super-unpopular-so-why-dont-democrats-have-a-bigger-lead#7</sub>

### 2026-06-01 · [Should Democrats panic about Platner?](https://www.natesilver.net/p/should-democrats-panic-about-platner)
**method** · FiveThirtyEight 2020 Senate model · explicit

When polling in a state is sparse, the model defaults more toward fundamentals. In 2020 it therefore rated Maine a toss-up instead of following Gideon's polling lead, partly because of Collins's history of landslide wins and her bipartisan voting record.

*Why:* Sparse polls carry little weight, so priors dominate.

> the model defaulted more toward “fundamentals” because polling in the state was sparse.

<sub>2026-06-01_should-democrats-panic-about-platner-by-nate-silver#3</sub>

### 2026-08-11 · [Everything is breaking Democrats’ way. Is it enough to win the Senate?](https://www.natesilver.net/p/everything-is-breaking-democrats-way)
**empirical regularity** · FLIPR 2026 · explicit

Work on FLIPR found the political climate more stable than ever in forecasting-relevant ways: opinions are baked in, voters tune in early, and recent elections have not had the late shifts in the national environment that used to be common in midterms.

> recent elections haven’t featured the late shifts in the political climate that used to be common in midterms.

<sub>2026-08-11_everything-is-breaking-democrats-way-is-it-enough-to-win-the-senate#7</sub>

### 2026-08-11 · [Everything is breaking Democrats’ way. Is it enough to win the Senate?](https://www.natesilver.net/p/everything-is-breaking-democrats-way)
**assumption** · FLIPR 2026 · explicit

Classic and Deluxe expect candidates who trail in polls during or just after contentious primaries to recover toward the state's partisan baseline. In Michigan, Lite had Republican Rogers as a 60 percent favorite, while Classic and Deluxe projected El-Sayed to win by about 3 points against a D+7 to D+8 baseline.

*Numbers:* Lite Rogers win prob = 60 percent (Michigan Senate, Aug 2026); Classic/Deluxe projected El-Sayed margin = about 3 points (Michigan Senate); Michigan baseline = D+7 to D+8 points (projected November baseline)

*Why:* Candidates often poll poorly amid contentious primaries.

> candidates often struggle in the polls when they’re in the midst of contentious primaries.

<sub>2026-08-11_everything-is-breaking-democrats-way-is-it-enough-to-win-the-senate#9</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**model change** · FLIPR 2026 · explicit

For 2026, FLIPR increases the relative weight on fundamentals versus polls because elections have become more predictable from partisanship with less ticket-splitting, while polls have had some rough years. It also accounts for the national environment 'locking in' earlier, so the generic ballot is more predictive months ahead than it once was.

*Why:* Empirical tests on historical data.

> should our model increase the relative weight on “fundamentals” as opposed to polls? The answer is basically yes

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#3</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**design principle** · FLIPR 2026 vs presidential model · explicit

Unlike the presidential model, which defaults toward polls-only by Election Day, FLIPR is a more even blend of polls and fundamentals even at the end, because non-polling data is richer for about 500 races and polling is sparse, with many House races getting little or no nonpartisan polling.

*Numbers:* races per cycle = around 500 races (House + Senate + governor)

> FLIPR is more of an even blend between polls and fundamentals

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#5</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

Step 5: a prior for the House popular vote is fit on macro factors since 1946: presidential approval, the previous House popular vote adjusted for uncontested 'blank districts', polarization, and midterm status. Classic and Deluxe nudge the current snapshot toward this prior, with an effect that is gentle and fades to zero by Election Day; Lite uses the snapshot with wider uncertainty. In August 2026 the prior was about D+8.5 versus a snapshot near D+7.

*Numbers:* prior = around D+8.5 points (early Aug 2026); snapshot = closer to D+7 points (early Aug 2026)

*Why:* As the generic ballot became more stable, the prior is less useful than it used to be.

> the effect of this adjustment is relatively gentle, and essentially fades out by Election Day.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#31</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**model change** · FLIPR 2026 · explicit

FLIPR now calibrates drift separately from Election Day error, where it previously blended them; the new specification is more consistent with the presidential forecast. The recalibration showed the national picture locks in earlier than it used to.

> Previously, the model blended drift and Election Day uncertainty together.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#36</sub>

### 2026-08-20 · [Are Democrats on a summer sugar high?](https://www.natesilver.net/p/are-democrats-on-a-summer-sugar-high)
**assumption** · FLIPR 2026 · explicit

Classic and Deluxe treat August polls as not being an unbiased estimator of the November result: they take a weighted average of polls and fundamentals, so a race at R+3 in polls and D+7 in fundamentals might be projected around D+1. The forecast is not a 'now-cast'; reversion toward partisan fundamentals is expected.

*Why:* August reflects a different information environment, with fewer ads and partisan cues.

> Classic and Deluxe FLIPR assume that summer polling can be predictably biased.

<sub>2026-08-19_are-democrats-on-a-summer-sugar-high-by-nate-silver#1</sub>

### 2026-08-20 · [Are Democrats on a summer sugar high?](https://www.natesilver.net/p/are-democrats-on-a-summer-sugar-high)
**model change** · FLIPR 2026 · explicit

One 2026 change to FLIPR was assuming more muted shifts in the national environment when partisanship is high, since late swings in historical generic ballot data have become less frequent: voters lock in earlier and there are fewer true swing voters.

*Why:* Partisanship combined with the 24/7 news cycle.

> one of the changes we made to FLIPR this year was to assume more muted shifts in the national environment when partisanship is high

<sub>2026-08-19_are-democrats-on-a-summer-sugar-high-by-nate-silver#5</sub>

### 2026-08-20 · [Are Democrats on a summer sugar high?](https://www.natesilver.net/p/are-democrats-on-a-summer-sugar-high)
**empirical regularity** · empirical · explicit

Historical summer polling leads that faded: Phil Bredesen led Marsha Blackburn in Tennessee in August 2018 before losing by 11, and Jaime Harrison tied Lindsey Graham into September 2020 before losing by 10. In 2022, race-level polls were too optimistic for Democrats in summer but converged toward the generic ballot by November.

*Numbers:* Blackburn margin = 11 points (TN 2018); Graham margin = 10 points (SC 2020)

> The individual-race polls converged toward the generic ballot

<sub>2026-08-19_are-democrats-on-a-summer-sugar-high-by-nate-silver#13</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**method** · FLIPR 2026 · explicit

With no general-election polls, as in the Kansas governor race, FLIPR relies on fundamentals and de-biased expert ratings.

*Numbers:* Kansas Senate simple fundamentals = R+9.4 points (Aug 2026); Kansas gov R flip prob = 57 percent (Aug 2026)

> there are no polls of the Kansas gubernatorial general election.

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#8</sub>

### 2026-09-03 · [Beware big swings in midterm forecasts](https://www.natesilver.net/p/beware-big-swings-in-midterm-forecasts)
**parameter or number** · Silver Bulletin generic ballot history · explicit

Since 2010, the Silver Bulletin generic ballot average has moved by an average of 1.4 points (absolute margin change) between Labor Day and Election Day; only in 2014 did it move by more than 2 points.

*Numbers:* average Labor Day to Election Day generic ballot swing = 1.4 points (cycles since 2010)

> On average in elections since 2010, the margin between Democrats and Republicans in our generic ballot average has swung by a whopping total of… 1.4 points between Labor Day and Election Day.

<sub>2026-09-03_beware-big-swings-in-midterm-forecasts#0</sub>

### 2026-09-03 · [Beware big swings in midterm forecasts](https://www.natesilver.net/p/beware-big-swings-in-midterm-forecasts)
**parameter or number** · FLIPR 2026 · explicit

A single outlier poll (Harvard-Harris R+2) plus other overnight polls moved the generic ballot from D+6.7 to D+6.4 and FLIPR's House odds from 84 to 81 percent, illustrating the model's damped response to individual polls.

*Numbers:* generic ballot change = D+6.7 to D+6.4 points (Sept 2, 2026); House D win prob change = 84 to 81 percent (Sept 2026)

<sub>2026-09-03_beware-big-swings-in-midterm-forecasts#10</sub>

### 2026-09-29 · [Midterm waves are the rule, not the exception](https://www.natesilver.net/p/midterm-waves-are-the-rule-not-the)
**method** · FLIPR 2026 · explicit

FLIPR's generic ballot estimate is a 'now-cast'. Classic and Deluxe blend in a prior from midterm history since World War II conditioned on presidential approval and other factors, with influence fading to zero by Election Day; in late September 2026 the prior and the current estimate were very close.

> the prior’s influence on the model fades to zero by Election Day.

<sub>2026-09-29_midterm-waves-are-the-rule-not-the-exception#5</sub>

### 2026-09-29 · [Midterm waves are the rule, not the exception](https://www.natesilver.net/p/midterm-waves-are-the-rule-not-the)
**parameter or number** · FLIPR 2026 · explicit

Between Sept. 7 and Sept. 29, 2026 the generic ballot moved from D+6.5 to D+8.9, about 2.5 points, larger than the post-Labor Day swing in most recent midterms. FLIPR's launch odds on Aug. 11 were about 55 percent for the Senate and 85 percent for the House, within a few points of prediction markets, which FLIPR's publication itself influenced.

*Numbers:* generic ballot shift = D+6.5 to D+8.9 points (Sept 7-29, 2026)

> On Sept. 7, they led by 6.5 points; now that lead has expanded to 8.9 points.

<sub>2026-09-29_midterm-waves-are-the-rule-not-the-exception#8</sub>

### 2026-10-15 · [Welcome to midterm silly season 🤡](https://www.natesilver.net/p/welcome-to-midterm-silly-season)
**design principle** · FLIPR 2026 · explicit

By design, the error bars on FLIPR's national popular vote forecast narrow little in the final weeks, because little is learned about the national environment late in modern midterms. Its ingredients, such as presidential popularity, economic perceptions, enthusiasm and incumbency advantage, are detectable early, while individual races stay more dynamic as polls accumulate.

*Why:* The cake goes into the oven early.

> The other thing I’d note is that the “error bars” on the chart aren’t narrowing much. That’s by design.

<sub>2026-10-15_republicans-are-spending-big-its-not-working#1</sub>

### 2026-10-17 · [The good, bad and ugly outcomes in the Senate](https://www.natesilver.net/p/the-good-bad-and-ugly-outcomes-in)
**method** · FLIPR 2026 · explicit

When polling averages are thin, as in South Dakota, the advanced FLIPR versions heavily hedge toward fundamentals rather than taking polls at face value.

> The more advanced versions of FLIPR heavily hedge toward the “fundamentals” in these cases

<sub>2026-10-17_the-good-bad-and-ugly-outcomes-in-the-senate#6</sub>

### 2026-10-23 · [Do these Senate-governor splits make sense?](https://www.natesilver.net/p/do-these-senate-governor-splits-make)
**empirical regularity** · FLIPR 2026 · explicit

In late October 2026, FLIPR's topline had barely moved for weeks given stable polling and a dearth of new polls relative to past cycles, so most remaining uncertainty was potential polling error rather than late shifts.

> at this point, most of the remaining uncertainty in our forecast comes down to potential polling error, not late shifts in the polls themselves.

<sub>2026-10-23_do-these-senate-governor-splits-make-sense#7</sub>

### 2026-10-25 · [Let’s talk shop about every Senate race](https://www.natesilver.net/p/lets-talk-shop-about-every-senate)
**interpretation guidance** · FLIPR 2026 · explicit

Prediction markets tend to become more confident as elections approach. Silver argues this misapplies the time-decay principle: late in a modern midterm most uncertainty is whether polls were right all along, which does not shrink until results arrive, and FLIPR assumes little late poll movement, an assumption tweaked in the 2026 rebuild.

> Most of the remaining uncertainty in the race isn’t about how polls will change over the final week-and-a-half, but rather about whether there will be another major polling error again

<sub>2026-10-25_lets-talk-shop-about-every-senate-race-by-nate-silver#3</sub>

### 2026-10-27 · [The 83 remotely competitive House races, according to FLIPR](https://www.natesilver.net/p/the-83-remotely-competitive-house)
**method** · FLIPR 2026 · explicit

FLIPR defaults to fundamentals more in House races than in Senate races because House races have fewer reliable polls; many are partisan or small-sample, and FLIPR weights these less. In NY-17, a Harris district, Lawler trailing by only 1.1 in polls still had just a 17 percent chance.

*Numbers:* Lawler win prob = 17 percent (NY-17, Oct 27, 2026)

> Generally speaking, FLIPR defaults to the “fundamentals” more in the House because there are fewer reliable polls than in the Senate.

<sub>2026-10-27_the-83-remotely-competitive-house-races-according-to-flipr#0</sub>

### 2026-10-27 · [The 83 remotely competitive House races, according to FLIPR](https://www.natesilver.net/p/the-83-remotely-competitive-house)
**empirical regularity** · general · explicit

The battleground expanding late in a race, with seats moving from Likely R toward competitive, is a hallmark of a wave election.

> The battleground expanding late in the race is a hallmark of a wave election.

<sub>2026-10-27_the-83-remotely-competitive-house-races-according-to-flipr#4</sub>

### 2026-11-02 · [Where polls and fundamentals clash](https://www.natesilver.net/p/where-polls-and-fundamentals-clash)
**method** · FLIPR 2026 · explicit

FLIPR's rule for blending polls with fundamentals: the more polling a race has, and the more recent and reliable the surveys, the more it defaults to the polls. In sparsely polled red states it hedges heavily toward fundamentals or lands between the two.

> Its rule is pretty simple: the more polling there is, and the more recent and reliable the surveys, the more it defaults to them.

<sub>2026-11-02_where-polls-and-fundamentals-clash-by-eli-mckown-dawson#0</sub>

### 2026-11-03 · [FINAL FLIPR 2026 midterm election forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-polls-model)
**parameter or number** · FLIPR 2026 final · explicit

Final 2026 Senate polling averages in battlegrounds: Texas D+3.3, Ohio D+3, Michigan D+4.9, Maine D+3.9, Iowa D+1.1, Kansas Democrat up about 4. At launch in August the Senate was near a toss-up; by the final update Democrats' Senate odds were just a few points below their House odds at launch.

*Numbers:* Texas polling average = D+3.3 points (final); Michigan polling average = D+4.9 points (final)

> Democratic candidates lead in our polling averages of every major battleground state, including Texas (D +3.3), Ohio (D +3), Michigan (D +4.9), Maine (D +3.9), and Iowa (D +1.1).

<sub>2026-11-03_2026-midterm-election-forecast-senate-house-silver-bulletin#3</sub>

### 2026-11-03 · [FLIPR 2026 Senate forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-senate-model)
**parameter or number** · FLIPR 2026 final · inferred_from_chart

Final Senate polls versus blended fundamentals show how far polls diverged: Kansas polls D+4.1 versus blended R+4.4; Florida polls R+6.1 versus blended R+0.0; Iowa D+1.1 versus R+0.0; Maine D+3.9 versus D+4.3; Michigan D+4.9 versus D+9.9; Louisiana R+4.0 versus R+10.7; Alaska D+3.1 versus R+3.3.

*Numbers:* Kansas polls vs blended = D+4.1 vs R+4.4 points (final); Michigan polls vs blended = D+4.9 vs D+9.9 points (final)

<sub>2026-11-03_2026-midterm-election-senate-forecast-silver-bulletin#4</sub>

### 2026-11-03 · [How to judge an election model](https://www.natesilver.net/p/how-to-judge-an-election-model)
**design principle** · FLIPR 2026 · explicit

FLIPR moved slightly toward fundamentals in its 2026 rebuild but remains truer to polls than some competitors, especially for the national environment. Silver warns that models with strong fundamentals that override polls are easy to overfit and have a middling-to-poor track record.

> models that make stronger assumptions about fundamentals and let them override polls are easy to overfit, and frankly have a middling-to-poor track record.

<sub>2026-11-02_how-to-judge-an-election-model-by-nate-silver#7</sub>

### 2026-11-03 · [It's Judgment Day for Trump (and for pollsters)](https://www.natesilver.net/p/its-judgment-day-for-trump-and-for)
**empirical regularity** · historical · explicit

Midterms usually trend steadily against one party rather than see-sawing (Republicans 2006 and 2026, Democrats 2010 and 2014), and sometimes, as in 1994 and 2014, the losing party does even worse than polls; counterexamples like 2022 are rare and may reflect small samples.

> Instead of the back-and-forth that you can get in a presidential year, usually things just get continually worse for one party

<sub>2026-11-03_its-judgment-day-for-trump-and-for-pollsters#7</sub>
