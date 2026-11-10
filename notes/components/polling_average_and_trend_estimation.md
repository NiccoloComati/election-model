# Polling average and trend estimation

99 findings from 47 articles, oldest first.

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**method** · FiveThirtyEight 2016 presidential · explicit

The 2016 trend-line adjustment detects movement by comparing successive editions of the same poll (same pollster and geography), separately for each candidate, then fits a loess regression trend line and adjusts older polls by the subsequent trend, scaled by state elasticity. Empirically, more smoothing early and less smoothing late works best.

*Why:* Same-poll comparisons remove a lot of noise.

> Empirically, using more smoothing early in the race and less smoothing late in the race works best.

<sub>fte_2016-general-election-forecast-users-guide#8</sub>

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**parameter or number** · FiveThirtyEight midterm models · explicit

The congressional timeline adjustment shifts a race poll by roughly two-thirds of the subsequent generic ballot change in congressional races and about half in gubernatorial races, modulated by the state's or district's elasticity. It is much more conservative than the presidential model's timeline adjustment.

*Numbers:* timeline factor, congressional = roughly two-thirds share (2018-2022); timeline factor, gubernatorial = half share (2018-2022)

> by roughly two-thirds that amount in congressional races and half that amount in gubernatorial races, depending on the elasticity score of the state or district

<sub>fte_midterm-house-senate-governor-methodology#11</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

The presidential polling averages blend a simple weighted average with a more aggressive trend-line method. Early in the campaign they rely mostly on the weighted average, and in the final weeks mostly on the trend line, so averages become more aggressive as Election Day nears.

> So early on in the campaign, we rely mostly on the more conservative weighted average method, while in the final few weeks, we mostly use the trend line method

<sub>fte_2020-presidential-forecast-methodology#2</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**adjustment rule** · FiveThirtyEight 2020 presidential · explicit

The timeline adjustment shifts older state polls for movement in the race since they were conducted, based on national polls and polls of similar states; for example, an older Arizona poll is shifted toward Trump if national and Nevada polls moved toward him.

> Finally, we apply a timeline adjustment , which is based on a poll’s recency, and adjusts “old” polls for shifts in the overall race since it was conducted.

<sub>fte_2020-presidential-forecast-methodology#5</sub>

### 2023-09-18 · [Is a Trump-Biden rematch inevitable?](https://www.natesilver.net/p/is-a-trump-biden-rematch-inevitable)
**method** · FiveThirtyEight 2024 primary averages · inferred_from_chart

The FiveThirtyEight 2024 Republican primary national average shown in the article adjusts each poll for recency, sample size, methodology and house effects. It displays a band in which 95% of polls are projected to fall. As of Sept 15, 2023 the average was Trump 55.5, DeSantis 14.2, Ramaswamy 7.6, Haley 6.1 and Pence 4.7.

*Numbers:* Trump = 55.5 percent (Sept 15 2023); DeSantis = 14.2 percent; poll range band = 95 percent (of polls projected to fall in range)

<sub>2023-09-18_is-a-trump-biden-rematch-inevitable-by-nate-silver#12</sub>

### 2024-04-17 · [Announcing 2024 election model plans](https://www.natesilver.net/p/announcing-2024-election-model-plans)
**method** · 2024 presidential polling averages · explicit

The Silver Bulletin national and state presidential polling averages are not simple averages. They use a Bayesian-type process that draws inferences from national polls and from polls in other states. If a state such as Arizona has not been polled recently but a candidate has improved in other polls, the state's average is adjusted to reflect that shift.

*Why:* Lets sparsely polled states reflect trends seen elsewhere.

> These aren't simple polling averages but instead use a Bayesian-type process to make inferences based on national polls and polls from other states.

<sub>2024-04-17_announcing-2024-election-model-plans-by-nate-silver#2</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**adjustment rule** · 2024 presidential · explicit

The 2024 polling averages include a third-party adjustment, analogous to the likely-voter adjustment, that estimates what polls omitting RFK Jr. would show if they included him. It is estimated specifically from polls that include Biden, Trump and Kennedy but no other minor candidates. Its net effect was neutral, because RFK Jr. drew about equally from Biden and Trump.

*Why:* Most polls include RFK Jr., but some do not.

> the model guesses at what polls would say if they included RFK Jr. when they do not. Overall, the effect of this is neutral: RFK Jr. draws about equally from both Biden and Trump.

<sub>2024-06-26_2024-presidential-election-model-methodology-update#13</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**method** · 2024 polling averages · explicit

The polling averages draw inferences from state polls to national polls and vice versa (a trend-line adjustment), which makes them more stable.

*Why:* Increases stability.

> they make inferences from state polls to national polls and vice versa, which tend to make them more stable

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#18</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**data source** · 2024 polling averages · explicit

The 2024 polling averages were backfilled to late February 2024.

> We’ve backfilled the polling averages to late February.

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#20</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**parameter or number** · 2024 polling averages · inferred_from_chart

Polling averages on June 26, 2024 (Biden / Trump / Kennedy): National 41.3/42.3/8.0; PA 43.2/44.6/5.4; MI 42.1/43.2/6.2; WI 42.7/43.2/6.9; GA 39.2/44.7/6.5; AZ 38.7/43.9/8.0; NC 38.4/45.1/7.0; NV 39.3/44.1/7.7; FL 37.9/45.9/6.1; TX 36.8/46.1/7.4. Nationally, Biden gained 1 point over the month but lost 0.4 over the week.

*Numbers:* National Trump lead = 1.0 points (June 26, 2024); National month change = D+1 points (June 2024)

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#22</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**design principle** · general principle · explicit

Even a polling average involves many researcher degrees of freedom: which polls to include, how to weight them, how much to prioritize recency. Fundamentals add essentially infinite further choices.

> there are basically infinite “researcher degrees of freedom” in exactly how you do it

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#46</sub>

### 2024-06-27 · [Are these guys trying to muddle through? Or playing to win?](https://www.natesilver.net/p/are-these-guys-trying-to-muddle-through)
**method** · 2024 presidential · explicit

The Silver Bulletin forecast is mostly determined by state polls rather than national polls. National polls mainly influence the model indirectly, through how they affect the calculations the model makes about state polls, for example trend adjustments applied to state polls.

> our forecasts are mostly determined by state polls rather than national polls, and national polls mostly influence the model only indirectly through how they affect the calculations it makes about state polls

<sub>2024-06-27_are-these-guys-trying-to-muddle-through-or-playing-to-win#3</sub>

### 2024-06-27 · [Are these guys trying to muddle through? Or playing to win?](https://www.natesilver.net/p/are-these-guys-trying-to-muddle-through)
**empirical regularity** · 2024 presidential · explicit

In the Silver Bulletin model, national polls can have a big effect on states that have not been polled much recently. In other cases the model largely ignores national polls ('shrugs its shoulders at them').

*Why:* Sparsely polled states lean more on the trend information inferred from national polls.

> Sometimes national polls can have a big effect, especially in states that haven't been polled much recently — but sometimes the model just shrugs its shoulders at them.

<sub>2024-06-27_are-these-guys-trying-to-muddle-through-or-playing-to-win#4</sub>

### 2024-06-27 · [Are these guys trying to muddle through? Or playing to win?](https://www.natesilver.net/p/are-these-guys-trying-to-muddle-through)
**method** · 2024 presidential polling averages · inferred_from_chart

Silver Bulletin polling averages, both state and national, are adjusted based on trends in both state and national polls. Each poll is weighted by its quality, sample size and recency.

<sub>2024-06-27_are-these-guys-trying-to-muddle-through-or-playing-to-win#5</sub>

### 2024-06-27 · [Are these guys trying to muddle through? Or playing to win?](https://www.natesilver.net/p/are-these-guys-trying-to-muddle-through)
**parameter or number** · 2024 presidential polling averages · explicit

Heading into the June 27, 2024 debate, the Silver Bulletin national polling average had Trump at 42.1% and Biden at 40.6%, so Biden trailed by 1.5 points. Through March-June 2024 the average was quite stable, with Trump consistently slightly ahead.

*Numbers:* Trump national average = 42.1 percent (June 27, 2024); Biden national average = 40.6 percent (June 27, 2024); Trump margin = 1.5 percentage points (national average June 27, 2024)

> he now trails Donald Trump by 1.5 points in our national average headed into the debate

<sub>2024-06-27_are-these-guys-trying-to-muddle-through-or-playing-to-win#11</sub>

### 2024-07-05 · [The broken leg problem](https://www.natesilver.net/p/the-broken-leg-problem)
**method** · 2024 presidential · explicit

When swing-state polls are out of date, the Silver Bulletin 2024 presidential model revises its state-by-state forecasts using national polling data, transmitting national shifts to the states.

> The model is supposed to revise its state-by-state forecasts using national data if the swing state polls are out-of-date

<sub>2024-07-05_the-broken-leg-problem-by-nate-silver-silver-bulletin#9</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**method** · 2024 presidential · explicit

The Silver Bulletin snapshot includes adjustments that smooth out the data in states with little polling, combining state and national polls to give a more precise picture.

*Why:* Sparse state polls are noisy.

> fancy polling averages that 538 or Silver Bulletin do, which can combine state and national polls to give you a much more precise snapshot of the race

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#1</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**method** · Silver Bulletin polling averages 2024 · inferred_from_chart

The Silver Bulletin polling average accounts for each poll's quality, sample size and recency. Averages are adjusted based on trends in both state and national polls. On July 18, 2024, the national average was Trump 43.3, Biden 41.2 and RFK Jr. 8.0.

*Numbers:* Trump national average = 43.3 % (July 18, 2024); Biden national average = 41.2 % (July 18, 2024); RFK Jr. national average = 8.0 % (July 18, 2024)

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#30</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**method** · 2024 presidential polling averages · explicit

The Silver Bulletin polling averages use national polls to make inferences about state polls and vice versa. A chart note says state averages are adjusted based on trends in both state and national polls.

*Why:* Produces a more stable average that is not thrown off by outliers, at the cost of extra computation.

> they use national polls to make inferences about state polls and vice versa

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#5</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**design principle** · 2024 presidential polling averages · explicit

Silver's stated design goal for the polling averages is a stable average that resists outliers, and he accepts extra computational cost to get it.

> the reward is a more stable average that doesn't get psyched out by outliers

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#6</sub>

### 2024-07-29 · [kamala_mode will be activated tomorrow](https://www.natesilver.net/p/kamala_mode-will-be-activated-tomorrow)
**method** · 2024 presidential · inferred_from_chart

The code screenshot shows a run_polling_averages option. "today" calculates polling averages only for the current date. "no" assumes the averages have already been calculated. "yes" or "backfill" calculates averages for the whole election cycle (comment truncated).

<sub>2024-07-29_kamala-mode-will-be-activated-tomorrow-by-nate-silver#10</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

The Silver Bulletin presidential model estimates the race by fitting several trendline curves, some more conservative and some more aggressive. The procedure is similar to, but not the same as, loess regression.

> The way the model works is basically by plotting a series of several trendline curves — some more conservative, some more aggressive. (The procedure is similar to, but not exactly the same as, loess regression.)

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#2</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

The model's trendline curves can bend sharply, so the model can detect nonlinear inflection points in the race. Examples are the shift toward Trump after the June 27, 2024 debate and an emerging shift toward Harris.

> Curves can bend, sometimes sharply, which is why the model can sometimes decide that there's been a nonlinear inflection point in the race

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#3</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**assumption** · 2024 presidential · explicit

Old polls, such as one from the previous December, have essentially no effect on the model's estimate of the current state of the race.

*Why:* The trendline curves are driven by recent data.

> it's not like a poll from last December will have any impact on the model's impression of the current state of the race

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#4</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

For thinly polled states, old state polls are adjusted by the change in the national race since the poll was taken (a trend-line adjustment). Example: a New Jersey poll showing Trump down 13 when national polls were tied would imply Trump down 9 after the national race moved to R+4.

*Numbers:* example old NJ margin = Trump -13 points (national tied at time of poll); national shift = R+0 to R+4 points (before Biden dropped out); imputed NJ margin = Trump -9 points (after national shift)

*Why:* Old polls remain informative about relative state lean.

> if the national race has shifted from R +0 to R +4 (as it had before Biden dropped out), the model could infer that Trump was now down by 9 points instead of 13 in New Jersey

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#7</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**limitation or failure mode** · 2024 presidential · explicit

The Harris-Trump polling flow, with very little data before June 27 and then a lot, is unusual relative to the model's training data. In the training data the number of polls rises gradually and roughly linearly through the year, so the trendline curves face an out-of-sample situation.

> In the training data, the "flow" of polling is much more linear, with the number of polls gradually increasing over the course of the year.

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#10</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**parameter or number** · 2024 Silver Bulletin polling average · explicit

Effect of removing RFK on the Silver Bulletin national polling average (Aug 23 to Aug 24, 2024): Harris rose from 48.0 to 48.8 (+0.8) and Trump from 43.7 to 44.8 (+1.1). The net shift was 0.3 points toward Trump, which means Kennedy drew slightly more from Trump.

*Numbers:* Harris average change = 48.0 to 48.8 (+0.8) percent (national average, RFK removal); Trump average change = 43.7 to 44.8 (+1.1) percent (national average, RFK removal); net shift to Trump = 0.3 percentage points (RFK removal)

> Harris's polling average has improved from 48.0 percent yesterday to 48.8 percent today (+0.8), while Trump's has increased from 43.7 to 44.8 (+1.1).

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#16</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**method** · 2024 Silver Bulletin polling average · inferred_from_chart

The Silver Bulletin national polling average accounts for each poll's quality, sample size and recency, and is adjusted based on trends in both state and national polls.

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#17</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**parameter or number** · 2024 Silver Bulletin polling average · inferred_from_chart

The Silver Bulletin national polling average chart shows Kennedy at about 15 percent in early July, then declining to about 4 percent by late August 2024.

*Numbers:* RFK early July average = ~15 percent (chart, before ~July 7); RFK late August average = ~4 percent (chart, Aug 23)

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#26</sub>

### 2024-08-26 · [How big will the bounce be?](https://www.natesilver.net/p/how-big-will-the-bounce-be)
**method** · 2024 polling averages · explicit

The Silver Bulletin national polling average accounts for each poll's quality, sample size and recency. In 2024 a Biden-Trump average was used through July 21 and a separate Harris-Trump average afterward.

> Values up to July 21st (the date Biden dropped out) come from our Biden-Trump polling average. Values after that date come from our Harris-Trump polling average.

<sub>2024-08-26_how-big-will-the-bounce-be-by-eli-mckown-dawson#17</sub>

### 2024-08-26 · [How big will the bounce be?](https://www.natesilver.net/p/how-big-will-the-bounce-be)
**empirical regularity** · 2024 polling averages · explicit

In the 2024 Silver Bulletin national average, polls were extremely stable before the June 27 debate. Trump went from up 1 the day before the debate to up 4 when Biden withdrew. Harris went from down 1.2 on the day of the withdrawal to up 4.1 on Aug 26. Harris rose from 47% at the start of the DNC to about 49%. The chart shows Kennedy falling from about 10% in March to about 4-5% by August.

*Numbers:* Trump lead day before debate = 1 points; Trump lead at Biden withdrawal = 4 points (July 21); Harris margin at Biden withdrawal = -1.2 points; Harris margin Aug 26 = +4.1 points; Harris share = 47 to about 49 % (DNC start to latest update)

> Before the debate, the polls were extremely stable.

<sub>2024-08-26_how-big-will-the-bounce-be-by-eli-mckown-dawson#18</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**adjustment rule** · 2024 presidential · explicit

The 2024 Silver Bulletin model treats certain events as 'landmark events', including a party convention and a candidate exiting the race. Polls conducted before a landmark event are treated as substantially out of date, so post-event polls move the forecast more.

*Numbers:* number of landmark events affecting Pennsylvania polling in late Aug 2024 = 2 events (DNC convention and RFK Jr.'s exit)

*Why:* Older polling no longer reflects the race after a major event. Silver concedes this might overdo things a bit but calls it self-correcting.

> earlier polling occurred before what the model considers to be two “landmark events” — the convention and a candidate exiting the race — so the model looks at older polling as being really out of date

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#4</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**method** · 2024 presidential · explicit

The model 'liberally' interprets its polls-only default. State polls inform the national popular vote estimate, national polls inform the state polling averages, and demographic data and past voting patterns are used to smooth state estimates into plausible maps.

> it uses state polls to inform its estimates of the national popular vote and national polls to inform its state-by-state polling averages

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#18</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**adjustment rule** · 2024 presidential · explicit

The model applies a trendline adjustment that uses national polls to bring older state polling data up to date.

> like its trendline adjustment to bring older polling data up to date

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#20</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**design principle** · 2024 presidential; also 2020 538 methodology · explicit

Silver Bulletin polling averages are designed to react very aggressively after big events such as conventions and debates. As a result, they can overshoot when built from relatively few post-event polls.

*Numbers:* Harris national lead on Aug 23 model run = 4.3 percentage points (day after acceptance speech, before the switch to the RFK-less version; possibly an overestimate from few polls)

*Why:* So the averages reflect the changed state of the race quickly. The forecast layer then hedges against that.

> our polling averages are designed to be very aggressive after big events like conventions, and maybe 4.3 points was an overestimate since it was drawn from relatively few polls.

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#8</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**method** · Silver Bulletin polling averages 2024 · inferred_from_chart

According to the chart notes, the polling averages account for each poll's quality, sample size and recency, and are adjusted based on trends in both state and national polls.

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#20</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**parameter or number** · 2024 presidential · inferred_from_chart

The Sept 1, 2024 polling averages table gives these margins. National Harris 49.2 vs Trump 45.7 (D+3.5). Pennsylvania D+1.2. Michigan D+1.9. Georgia D+1.1. North Carolina R+0.3. Wisconsin D+3.3. Arizona R+0.5. Nevada D+0.8. Florida R+4.7. Texas R+6.3.

*Numbers:* National = D+3.5 percentage points (Sept 1, 2024); PA = D+1.2 percentage points (Sept 1, 2024); MI = D+1.9 percentage points (Sept 1, 2024); GA = D+1.1 percentage points (Sept 1, 2024); NC = R+0.3 percentage points (Sept 1, 2024); WI = D+3.3 percentage points (Sept 1, 2024); AZ = R+0.5 percentage points (Sept 1, 2024); NV = D+0.8 percentage points (Sept 1, 2024); FL = R+4.7 percentage points (Sept 1, 2024); TX = R+6.3 percentage points (Sept 1, 2024)

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#21</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**method** · 2024 presidential · explicit

The Silver Bulletin 'raw' polling averages are not subject to the convention bounce adjustment. That adjustment is applied at a later stage of the presidential model, in the forecast step.

*Why:* Separates the description of current polling from the forecast of election day.

> there’s no convention bounce adjustment in these polling averages at all; that comes at a later stage.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#2</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**parameter or number** · 2024 presidential polling averages · inferred_from_chart

Silver Bulletin polling-average margins on Aug. 19 (start of DNC) vs Sept. 6, 2024:
- National: D+2.3 → D+3.0
- PA: D+1.6 → D+0.6
- MI: D+3.1 → D+1.8
- GA: R+1.6 → D+0.2
- NC: D+0.6 → R+1.0
- WI: D+3.6 → D+2.4
- AZ: D+0.9 → R+1.9
- NV: D+0.8 → D+0.7
State and national averages moved in different directions.

*Numbers:* national change = D+0.7 percentage points (Aug 19–Sep 6); AZ change = R+2.8 percentage points (Aug 19–Sep 6); GA change = D+1.8 percentage points (Aug 19–Sep 6)

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#13</sub>

### 2024-09-07 · [Oops! I made the convention bounce adjustment disappear.](https://www.natesilver.net/p/oops-i-made-the-convention-bounce)
**empirical regularity** · 2024 presidential · explicit

Without the bounce adjustment, Harris led the Silver Bulletin polling averages in states totaling 292 electoral votes, yet her EC win probability was only ~50%. Leading the averages in states summing to more than 270 does not imply being favored.

*Numbers:* EVs in states Harris leads = 292 electoral votes (Sept 2024 polling averages)

*Why:* Leads are narrow, fundamentals and cross-state hedging pull against her, and outcomes are correlated.

> Harris is still ahead in our polling averages, albeit extremely narrowly in some cases, in states totaling 292 electoral votes.

<sub>2024-09-07_oops-i-made-the-convention-bounce-adjustment-disappear#4</sub>

### 2024-09-11 · [A guide to post-debate poll-watching](https://www.natesilver.net/p/a-guide-to-post-debate-poll-watching)
**method** · 2024 presidential · explicit

The Silver Bulletin trendline adjustment extrapolates movement in national polls to state estimates when fresh state polls are lacking. For example, if Harris gains 2 points nationally, the model assumes she has gained about 2 points in Pennsylvania. This suggests a uniform-swing-style trend transfer.

*Numbers:* Example national gain transferred to state = 2 percentage points (Pennsylvania example)

*Why:* Without fresh state data, national movement is the best available signal. Actual state data can later produce surprises.

> it will assume that if Harris has gained 2 points in national polls, she's probably gained 2 points in Pennsylvania as well.

<sub>2024-09-11_a-guide-to-post-debate-poll-watching-by-nate-silver#7</sub>

### 2024-09-19 · [Don't let randomness make a fool of you](https://www.natesilver.net/p/dont-let-randomness-make-a-fool-of)
**empirical regularity** · general principle · explicit

Averaging polls reduces sampling error only partially. Four 800-person polls are equivalent to a 3,200-voter sample, which still has a margin of error on the margin of 3 or 4 points. A true Harris +1 race could therefore show an average anywhere from Trump +2 to Harris +4.

*Numbers:* number of polls averaged = 4 polls (Wisconsin example); pooled sample size = 3200 voters (four 800-person polls combined); margin of error on the margin = 3 or 4 percentage points (pooled sample of 3,200)

> The margin of error on the difference separating the candidates is still 3 or 4 points

<sub>2024-09-19_dont-let-randomness-make-a-fool-of-you-by-nate-silver#7</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**method** · 2024 Silver Bulletin polling averages · inferred_from_chart

Silver Bulletin state polling averages account for each poll's quality, sample size and recency. They are also adjusted based on trends in both state and national polls.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#8</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**parameter or number** · 2024 Silver Bulletin polling averages · inferred_from_chart

Silver Bulletin state polling averages as of Sept 21, 2024 (Harris/Trump) were: MI 49.3/46.9, PA 48.9/47.4, WI 49.4/47.6, NV 48.3/47.2, NC 47.9/48.0, GA 47.4/48.3, AZ 47.3/48.1, FL 46.2/50.1.

*Numbers:* MI average = 49.3/46.9 percent Harris/Trump (Sept 21, 2024); PA average = 48.9/47.4 percent (Sept 21, 2024); WI average = 49.4/47.6 percent (Sept 21, 2024); NV average = 48.3/47.2 percent (Sept 21, 2024); NC average = 47.9/48.0 percent (Sept 21, 2024); GA average = 47.4/48.3 percent (Sept 21, 2024); AZ average = 47.3/48.1 percent (Sept 21, 2024); FL average = 46.2/50.1 percent (Sept 21, 2024)

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#23</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**method** · 2024 presidential · explicit

The Silver Bulletin presidential model does not take individual state polls at face value. It averages each new poll with other surveys of that state and with a demographics-based prior for the state.

*Why:* Shrinks the influence of any single possibly-outlying poll.

> the model isn't taking any of these numbers quite at face value, instead averaging them with other surveys of these states as well as its priors based on their demographics

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#2</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**adjustment rule** · 2024 presidential · explicit

The weight on the state polling average versus the regression depends on how much recent polling a state has. With heavy recent polling in Pennsylvania, 93% of the weight went to the polling average and 7% to the regression.

*Numbers:* PA weight on polling average = 93 percent (Sept 26, 2024); PA weight on regression = 7 percent (Sept 26, 2024)

*Why:* More recent state polling means more trust in the state's own average.

> with a lot of recent polling in Pennsylvania, 93 percent of the weight goes to the polling average and just 7 percent to the regression

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#5</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**method** · 2024 presidential · inferred_from_chart

The Silver Bulletin Pennsylvania forecast table lists 10 steps from polling average to win probability: (1) polling average; (2) adjust for bounces and recent events; (3) adjusted polling average; (4) reallocate undecided and third-party votes; (5) reallocated vote share; (6) blend with regression; (7) snapshot; (8) blend with economic fundamentals; (9) projected vote share; (10) chance of winning.

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#6</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**parameter or number** · 2024 presidential · inferred_from_chart

In the Sept 26 Pennsylvania forecast table, the inputs and outputs were as follows. The polling average was Harris 48.8 / Trump 47.3, and the bounce adjustment was about zero. Reallocating undecided and third-party votes added +1.6 to each candidate (50.4 / 48.9). The regression estimate was 49.6 / 49.7, blended at weight 0.06. The snapshot was 50.3 / 48.9. The economic fundamentals estimate was 48.9 / 50.3, blended at weight 0.14. The final projection was 50.1 / 49.1, with a Harris win probability of 59.1%.

*Numbers:* regression blend weight = 0.06 weight (PA, Sept 26 2024 (text says 7%)); fundamentals blend weight = 0.14 weight (PA, Sept 26 2024, roughly 6 weeks before election); undecided/third-party reallocation = +1.6 each percentage points (PA, applied equally to both candidates); PA Harris win probability = 59.1 percent (Sept 26 2024); PA projected vote = 50.1 vs 49.1 percent (Harris vs Trump)

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#7</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**parameter or number** · Silver Bulletin polling averages 2024 · explicit

Silver Bulletin polling averages on Sept 26, 2024 had the following margins: National D+2.8 (49.0-46.2), PA D+1.5, MI D+2.3, WI D+2.2, NC R+0.5, GA R+1, AZ R+1, FL R+3.4, NV D+1.1, MN D+5.9, NM D+8.1, TX R+5.6. Polling averages and the forecast differ.

*Numbers:* national avg = D+2.8 percentage points (Sept 26 2024); PA avg = D+1.5 percentage points (Sept 26 2024); averages EC gap = 1.3 percentage points (vs NYT 0.7)

> In our averages, Harris leads by 2.8 points nationally but by 1.5 points in Pennsylvania.

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#18</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**parameter or number** · 2024 presidential · explicit

The regression component estimated Pennsylvania as roughly a tie based on polls of other states, versus Harris +1.5 in the PA polling average.

*Numbers:* regression PA estimate = tie (Sept 26 2024)

> the regression analysis thinks that the state “should” be a tie based on the polling it sees of other states instead of Harris +1.5

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#19</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**design principle** · 2024 presidential · explicit

Silver Bulletin polling averages are 'aggressive': they put a big premium on newer data, i.e. heavy recency weighting. Other good models use less aggressive recency weighting.

*Why:* Acknowledged as a legitimate design choice that others make differently.

> our polling averages are pretty aggressive — meaning we put a big premium on newer data. Other excellent models take a less aggressive approach.

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#0</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**data source** · 2024 polling averages · inferred_from_chart

Silver Bulletin polling averages on Sept. 29, 2024:
- National: D+3.3 (Harris 49.3, Trump 46.0)
- PA: D+1.3
- MI: D+1.9
- WI: D+1.9
- NC: R+0.2
- GA: R+0.7
- AZ: R+1.3
- FL: R+3.3
- NV: D+1.8
- MN: D+5.9
- TX: R+5.5
- NM: D+8.4
The table shows only contests surveyed by three distinct pollsters or with at least five polls. Weekly change is measured against the average 7 days earlier and monthly change against 30 days earlier.

*Numbers:* minimum distinct pollsters for display = 3 pollsters (polling average table); minimum polls for display = 5 polls (alternative threshold); national margin = D+3.3 percentage points (Sept 29 2024); MN monthly change = R+3.2 percentage points (change from last month)

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#13</sub>

### 2024-10-09 · [When you should panic about the polls](https://www.natesilver.net/p/when-you-should-panic-about-the-polls)
**method** · 2024 presidential · explicit

The Silver Bulletin polling averages 'draw curves'. They fit a set of trendlines to recent polling movements, ranging from more conservative to more aggressive. The resulting curves can have inflection points, sometimes sharp ones.

> we fit a bunch of trendlines from recent polling movements that range from more conservative to more aggressive. And curves can be — well, curvy. They can have inflection points

<sub>2024-10-09_when-you-should-panic-about-the-polls-by-nate-silver#2</sub>

### 2024-10-09 · [When you should panic about the polls](https://www.natesilver.net/p/when-you-should-panic-about-the-polls)
**empirical regularity** · 2024 presidential · explicit

When a candidate has moved sharply (e.g., gained 2 points nationally in a week), the next several polls are high-leverage. The polling average is effectively testing whether the aggressive trendline is correct, much as with exponential data series such as early COVID case counts.

*Numbers:* example steep national shift = 2 percentage points (gain over the past week, described as relatively steep given recent stable elections)

*Why:* With multiple trendlines fitted, new data during a trend strongly discriminates between conservative and aggressive fits.

> the next several polls that come in are high-leverage as the model essentially tries to determine whether the aggressive curve is correct

<sub>2024-10-09_when-you-should-panic-about-the-polls-by-nate-silver#3</sub>

### 2024-10-09 · [When you should panic about the polls](https://www.natesilver.net/p/when-you-should-panic-about-the-polls)
**empirical regularity** · 2024 presidential · explicit

When polls have been steady for several weeks, the Silver Bulletin average resists change. It usually takes several polls telling a consistent story to convince the model that something has changed.

*Why:* Stable data favors the conservative trendlines.

> It usually takes several polls telling a consistent story to convince the model that something has changed.

<sub>2024-10-09_when-you-should-panic-about-the-polls-by-nate-silver#4</sub>

### 2024-10-09 · [When you should panic about the polls](https://www.natesilver.net/p/when-you-should-panic-about-the-polls)
**interpretation guidance** · 2024 presidential · inferred_from_chart

The Wisconsin polling average chart annotates landmark events: Trump assassination attempt, Trump VP pick/RNC, Biden dropping out, model launch, Harris VP pick, DNC, Kennedy dropping out, Harris-Trump debate and Walz-Vance debate. As of Oct 9, 2024 it shows Harris 49.0% and Trump 47.5%. The Kennedy line was tracked at roughly 2-4% until he dropped out in late August.

*Numbers:* Harris WI = 49.0 percent (Oct 9, 2024); Trump WI = 47.5 percent (Oct 9, 2024); Kennedy WI = 2-4 percent (July-August 2024 before dropout)

<sub>2024-10-09_when-you-should-panic-about-the-polls-by-nate-silver#15</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**method** · Silver Bulletin polling averages 2024 · inferred_from_chart

The Silver Bulletin state polling averages weight each poll by quality, sample size and recency, and are adjusted based on trends in both state and national polls. The trendline adjustment is applied to individual polls.

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#14</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**parameter or number** · Silver Bulletin polling averages 2024 · inferred_from_chart

On Oct. 10, 2024, the Silver Bulletin Pennsylvania average was Harris 48.6%, Trump 47.6%. The chart also showed Kennedy's line ending when he dropped out in late August, a Harris rise after the Sept. 10 debate followed by a plateau, and the model launch around late July.

*Numbers:* Harris PA = 48.6 % (Oct 10 2024); Trump PA = 47.6 % (Oct 10 2024)

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#15</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**method** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model's state forecast blends a polling average with a regression-based estimate. The share of the forecast coming from the polling average varies by state, depending on how much polling there is.

*Why:* States with less polling lean more on the regression-based estimates.

> at least 65 percent of our forecast in the state being made up of polling averages rather than our regression-based estimates

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#0</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**method** · 538 2020 · explicit

The 2020 FiveThirtyEight presidential forecast (Silver era) also blended a polling-average component with other estimates. For the 2020 error check, Silver included states where the polling-average component made up at least 65 percent of the final forecast.

*Numbers:* polling-average share threshold = 65 percent (2020 final forecast; state inclusion in the 2020 error table)

> I've included all states where the polling average component made up at least 65 percent of our final forecast in 2020.

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#2</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**design principle** · Silver Bulletin polling averages · explicit

A polling average hedges between competing methodological bets, such as pollsters that weight by recalled vote and those that don't, like NYT/Siena. The forecaster therefore need not choose which theory of the electorate is correct.

*Why:* Uncertainty about which technique is right is best handled by aggregation.

> the beauty of a polling average is that it hedges its bets with a mix of polls that use both techniques

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#13</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**interpretation guidance** · 2024 presidential · explicit

Week-to-week movement in the polling average can be random variation around a stable true margin. With Harris truly up about 3 nationally and about 1 in the Blue Wall states, better and worse weeks are expected. Shifts of about 0.3 nationally and about 1 point in the states should not automatically be read as a trend.

*Numbers:* national weekly change = R+0.3 percentage points (week to Oct 15 2024)

> if Harris really is ahead nationally by 3 points and in the Blue Wall states by about 1 point we'd expect her to have better and worse weeks that vary around that average.

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#18</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**method** · 2024 presidential · inferred_from_chart

Silver Bulletin polling-average tables follow these conventions:
- Change from last week compares with the average 7 days before the latest update.
- Change from last month compares with the average 30 days before.
- Only contests surveyed by at least 3 distinct pollsters, or with at least 5 polls, are shown.

*Numbers:* weekly change lookback = 7 days; monthly change lookback = 30 days; min distinct pollsters to display = 3 pollsters; min polls to display = 5 polls

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#19</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**parameter or number** · 2024 presidential · inferred_from_chart

Silver Bulletin averages on Oct 15, 2024 (Harris-Trump vote shares, margin, change vs one week earlier):
- National: 49.3-46.5, D+2.8, week change R+0.3.
- Pennsylvania: 48.4-47.8, D+0.6, week change R+0.7.
- Michigan: 48.4-47.4, D+1, week change R+0.9.
- Wisconsin: 48.7-47.9, D+0.8, week change R+1.1.
- North Carolina: R+0.8.
- Georgia: R+0.9.
- Arizona: R+1.6.
- Nevada: D+0.8.
- Florida: R+5.2.
- Texas: R+6.2.
- Minnesota: D+6.
- New Mexico: D+7.9.

*Numbers:* national Harris = 49.3 percent (Oct 15 2024); national Trump = 46.5 percent (Oct 15 2024); PA margin = D+0.6 points; MI margin = D+1 points; WI margin = D+0.8 points; FL margin = R+5.2 points; TX margin = R+6.2 points

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#20</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**method** · Silver Bulletin polling averages (2024) · explicit

The sensitivity parameters of the Silver Bulletin polling averages were tuned with minimizing autocorrelation, both positive and negative, as one of the most important objectives.

*Why:* Averages that are too sensitive produce mean reversion (negative autocorrelation). Averages that are too sluggish produce positive autocorrelation, leaving predictable trend information unused.

> one of the most important factors I sought to optimize for when tuning their parameters was minimizing autocorrelation — that is, having neither positive autocorrelation nor negative autocorrelation

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#1</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**interpretation guidance** · general principle · explicit

Silver defines negative autocorrelation as an over-sensitive average whose moves predictably reverse: a candidate going from +1 to +2 implies a reversion to +1.5 next week. He defines positive autocorrelation as an over-sluggish average whose moves predictably continue: +1 to +2 implies +3 next week.

*Numbers:* example margin path = +1 to +2 percentage points (Hypothetical Trump margin in Arizona used to illustrate autocorrelation)

> If Trump rising from +1 to +2 implies that the polling average next week will be +3, this is positive autocorrelation

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#2</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**empirical regularity** · Silver Bulletin polling averages (2024) · explicit

The Silver Bulletin polling averages tend to be more sensitive to new polls than most other averages.

*Why:* This follows from tuning to minimize autocorrelation rather than to minimize visible volatility.

> the Silver Bulletin polling averages tend to be more sensitive than most

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#3</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**critique of other approach** · general principle · explicit

Silver says professional model builders tend to make their models too sluggish, 'easing into' changes more than is optimal for predictive accuracy, because they fear looking silly if the forecast bounces around. Laypeople make the opposite error and overreact to new information.

*Why:* The reluctance to show volatility comes from reputational concerns rather than accuracy.

> They think it makes them look silly if their forecast is bouncing around a lot, so they build models that “ease into” changes more than is optimal

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#4</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**parameter or number** · Silver Bulletin polling averages (2024) · explicit

The Silver Bulletin polling averages are designed to look two weeks out: today's average should optimally predict what new polls will say two weeks from now. This is a middle ground between a short-term focus, which calls for an aggressive average, and a 30-day focus, which calls for a conservative one.

*Numbers:* prediction horizon of polling average = 2 weeks (Target horizon used in tuning, except at the end of the race)

*Why:* The best short-term prediction may extend a bounce, while the best long-term prediction may revert, because bounces from debates and conventions can be short-lived.

> our polling averages are designed to look two weeks out — that is, the polling average today should optimally predict what new polls will say two weeks from now

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#5</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**adjustment rule** · Silver Bulletin polling averages (2024) · explicit

At the end of the race, the Silver Bulletin polling averages switch to a more aggressive (more sensitive) setting, because there is no time left for reversion to the mean.

*Why:* Near election day, the short-term and final-outcome horizons converge.

> except at the end of the race when there’s no time left for reversion to the mean, and we use a more aggressive setting

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#6</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**limitation or failure mode** · Silver Bulletin polling averages (2024) · explicit

Because the Silver Bulletin averages are tuned for a two-week horizon, they may understate momentum over the very short term.

> It’s possible we’ll understate momentum over the very short term, however.

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#7</sub>

### 2024-10-22 · [Likability isn't enough](https://www.natesilver.net/p/likability-isnt-enough)
**parameter or number** · 2024 presidential · explicit

As of Oct 22, 2024, Harris's lead in national polls had fallen to 1.6 points, per the linked polling average (presumably the Silver Bulletin national average).

*Numbers:* Harris national polling lead = 1.6 percentage points (Oct 22, 2024)

> Harris's lead in national polls is down to just 1.6 points.

<sub>2024-10-22_likability-isnt-enough-by-nate-silver-silver-bulletin#1</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**design principle** · general principle · explicit

Polling averages depend on polls being independent. Herding may make individual polls more accurate, but it makes polling averages less accurate because the average stops aggregating independent opinions (a wisdom-of-crowds precondition).

*Why:* Independence is a precondition for the wisdom of crowds (Surowiecki).

> although herding may make individual polls more accurate, they actually make polling averages less accurate. Polling averages are supposed to aggregate independent opinions

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#3</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**empirical regularity** · 2024 presidential polling averages · inferred_from_chart

The Silver Bulletin averages on Nov 1, 2024 showed a larger shift toward Trump over the past month nationally than in most swing states. Margins were National D+1.1 (R+2.5 over the month), PA R+0.6 (R+1.9), NC R+1.2 (R+0.8), MI D+1.2 (R+0.9), GA R+1.7 (R+0.8), WI D+0.8 (R+1.2), AZ R+2.2 (R+0.9), NV R+0.6 (R+2.5), FL R+6.6 (R+3), TX R+7 (R+1.1), NM D+6.6 (R+1.9), NH D+5.2 (R+2.5). The averages table lists only contests surveyed by 3 distinct pollsters or with at least 5 polls. Week change compares to 7 days earlier and month change to 30 days earlier.

*Numbers:* national margin = D+1.1 percentage points (Nov 1, 2024); national month change = R+2.5 percentage points; display threshold = 3 distinct pollsters or 5 polls (averages table)

*Why:* Silver suspects herding in national polls via likely voter models.

> national polls have tightened and moved toward Trump considerably more than state polls have become Trumpier over the past month, except in Nevada and Florida

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#18</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**data source** · 2024 presidential · inferred_from_chart

The Silver Bulletin poll listing displays an 'Influence' column showing how influential each poll is in the model. Population labels are LV, RV, V and A.

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#20</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**parameter or number** · 2024 polling averages · explicit

The Silver Bulletin Iowa polling average stood at Trump +3.4 after the Selzer poll, but rested on only 4 Iowa polls all cycle, so it carries substantial uncertainty.

*Numbers:* Iowa polling average = Trump +3.4 percentage points (Nov 2, 2024); Number of Iowa polls = 4 polls (entire 2024 cycle)

> our current polling average in Iowa falls just within that range of overlap: Trump +3.4 points. (Careful: the "average" is based on only 4 polls of Iowa all cycle long.)

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#7</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**method** · 2024 polling averages · inferred_from_chart

The Silver Bulletin state polling averages account for each poll's quality, sample size and recency. They are also adjusted using trends in both state and national polls, so a state average can move even without new state polls.

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#8</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**parameter or number** · 2024 polling averages · inferred_from_chart

The Silver Bulletin Iowa polling average chart shows Trump 48.8% and Harris 45.4% on Nov 2, 2024. The average starts in mid-September and moves in visible steps when new polls arrive (one jump around Oct 1, one at the end of October), which reflects sparse state polling.

*Numbers:* Trump Iowa average = 48.8 percent (Nov 2, 2024); Harris Iowa average = 45.4 percent (Nov 2, 2024)

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#9</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**method** · 2024 presidential · explicit

The Silver Bulletin model's projected national popular vote margin is largely extrapolated from state polls rather than national polls. In the final 2024 forecast this gave Harris +2.1, versus +1 in the national polling average.

*Numbers:* model popular vote margin = 2.1 percentage points (Harris, final 2024); national polling average = 1 percentage points (Harris lead, final 2024)

*Why:* State polls, including Iowa, were relatively good for Harris.

> The model, however, instead calibrates her popular vote margin at 2.1 points because it's largely based on extrapolations from state polls rather than national polls

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#12</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**empirical regularity** · 2024 presidential · explicit

In the final 2024 Silver Bulletin polling averages, 6 of the 7 key swing states were within 1.2 points. Arizona, leaning Trump, was the only one with something resembling a clear lead.

*Numbers:* swing state margin = within 1.2 percentage points (6 of 7 swing states, final 2024)

> In 6 of the 7 key swing states, our final polling average is within 1.2 points; the only one with something resembling a clear lead is Arizona for Trump.

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#14</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**method** · Silver Bulletin polling averages 2024 · explicit

The Silver Bulletin polling averages use national polls to make inferences about state polls and vice versa. State averages are adjusted based on trends in both state and national polls.

*Why:* The extra computation yields a more stable average that is not thrown off by outliers.

> they use national polls to make inferences about state polls and vice versa

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#9</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**design principle** · general principle · explicit

Silver favors a computationally heavier polling average because stability and robustness to outliers are worth the extra cost.

*Why:* Stability and resistance to outliers.

> the reward is a more stable average that doesn’t get psyched out by outliers

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#10</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**method** · 2024 presidential · explicit

Silver Bulletin 2024 state forecasts combine the state polling average with a regression estimate. The regression is based on national polls and polls of other states and tends to assume a relatively uniform swing from the previous election.

> Our forecasts are based on a combination of polling averages and a regression estimate based on national polls and polls of other states that tends to assume a relatively uniform swing from the previous election.

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#22</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**limitation or failure mode** · 2024 presidential · explicit

The current method by which polls are adjusted after landmark events may introduce unwanted autocorrelation into the 2024 model's forecast.

> we may be introducing some unwanted autocorrelation based on how it’s done currently.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#16</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**method** · Silver Bulletin polling averages (2026) · explicit

The polling average on each date is a local polynomial regression using a blend of more aggressive and more conservative smoothing settings. The settings are chosen empirically so the average is stable, free of autoregression, and minimizes error in predicting the next new survey.

*Why:* The current average should be the best predictor of forthcoming polls.

> the current polling average should be the best predictor of forthcoming surveys.

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#8</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**empirical regularity** · Silver Bulletin polling averages (2026) · explicit

Too little smoothing overfits and makes the curve jumpy, while too much smoothing lags new trends. Empirically the generic ballot tends to be under-smoothed and too bouncy, which is less true for approval ratings, so approval settings are more aggressive.

*Why:* Bias-variance trade-off in smoothing.

> we've found that generic ballot can suffer from under-smoothing, making the average too "bouncy,"

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#9</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**method** · Silver Bulletin 2026 generic ballot average · inferred_from_chart

The generic ballot average chart displays shaded bands within which 90% of polls are projected to fall. The average is updated nearly every day through November.

*Numbers:* poll band coverage = 90 percent (shaded region in chart); Jan 22 2026 Dem = 47.4 percent (generic ballot); Jan 22 2026 Rep = 42.1 percent (generic ballot)

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#27</sub>

### 2026-04-21 · [SBSQ #31: Trump is super unpopular. So why don’t Democrats have a bigger lead?](https://www.natesilver.net/p/sbsq-31-trump-is-super-unpopular)
**empirical regularity** · Silver Bulletin polling averages (2026) · explicit

Generic ballot polls are 'bouncier' than other polling series, with little herding, possibly because the question is abstract and wording-sensitive and pollsters do not expect to be judged on it. Silver Bulletin therefore uses a more conservative smoothing setting for the generic ballot average, while its presidential approval average is tuned to react quickly.

*Why:* Curb noise in a bouncy series.

> we’ve found that you need to use a more conservative setting for the generic ballot than for other sorts of polling averages to curb this bouncy tendency.

<sub>2026-04-21_sbsq-31-trump-is-super-unpopular-so-why-dont-democrats-have-a-bigger-lead#0</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

Step 1: FLIPR's race-level polling averages use the shared Silver Bulletin algorithm. Polls are weighted by recency, sample size and pollster rating, adjusted for house effects, and smoothed by averaging more aggressive and more conservative LOWESS regression curves.

*Why:* Balance responsiveness against bounciness.

> we’ve found the best way to do this is to calculate what are essentially various LOWESS regression curves, and then average more aggressive and more conservative versions.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#7</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**adjustment rule** · FLIPR 2026 · explicit

FLIPR applies a timeline adjustment: if the generic ballot has moved since a race was last polled, a fraction of that movement is added to the race's margin, since a partial correction works better than a full one empirically. Race averages can therefore shift without new polls.

*Why:* Avoid relying on stale polling.

> We’ve found empirically that a partial correction works better than a full correction.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#11</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**interpretation guidance** · Silver Bulletin polling averages · explicit

Presidential approval averages tolerate more aggressive smoothing settings, while the generic ballot average must be fairly conservative or it bounces around too much; Silver says he tried it the other way.

> the generic ballot average needs to be fairly conservative or will bounce around too much

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#13</sub>

### 2026-09-03 · [Beware big swings in midterm forecasts](https://www.natesilver.net/p/beware-big-swings-in-midterm-forecasts)
**design principle** · Silver Bulletin polling averages · explicit

Silver Bulletin uses different smoothing parameters for different polling series. Generic ballot averages are smoothed heavily because Congress makes less national news, races are local, polling is spread over many races, and generic ballot polls are wording-sensitive and unherded (August 2026 polls ranged from D+11 Zogby to D+2 RMG). Presidential election averages and approval averages put a bigger premium on new data.

*Numbers:* range of August 2026 generic ballot polls = D+2 to D+11 points (RMG to Zogby)

*Why:* A polling model should not take a one-size-fits-all approach.

> A polling model shouldn’t take a one-size-fits-all approach to calculate its averages.

<sub>2026-09-03_beware-big-swings-in-midterm-forecasts#4</sub>

### 2026-09-03 · [Beware big swings in midterm forecasts](https://www.natesilver.net/p/beware-big-swings-in-midterm-forecasts)
**design principle** · Silver Bulletin polling averages · explicit

The goal for polling averages is minimal autocorrelation in their changes: today's average should be the best prediction of the near-future average. If a decline would predictably bounce back, the average is overreacting; if it would predictably keep falling, it is underreacting.

*Why:* Learned from building averages that were both over- and under-responsive.

> In technical terms, the goal is for changes in our polling averages to have as little autocorrelation as possible.

<sub>2026-09-03_beware-big-swings-in-midterm-forecasts#5</sub>

### 2026-09-03 · [Beware big swings in midterm forecasts](https://www.natesilver.net/p/beware-big-swings-in-midterm-forecasts)
**critique of other approach** · Silver Bulletin generic ballot average · explicit

The RealClearPolitics generic ballot average, being under-smoothed, swung from D+8.1 in late May to D+4.7 by mid-July 2026, a 3.4-point drop that was mostly noise. The Silver Bulletin average, smoother and with a more comprehensive poll set, moved only 1.2 points (D+7.1 to D+5.9).

*Numbers:* RCP swing = 3.4 points (late May to mid-July 2026); Silver Bulletin swing = 1.2 points (same period)

> Because an under-smoothed average will overfit to small fluctuations in the data, a few days of bad polls can move the topline picture fairly dramatically.

<sub>2026-09-03_beware-big-swings-in-midterm-forecasts#6</sub>

### 2026-09-20 · [Expert ratings are ignoring signs of a blue wave](https://www.natesilver.net/p/expert-ratings-are-ignoring-signs)
**parameter or number** · FLIPR 2026 · explicit

FLIPR's trendline adjustment shifts older race polls by two-thirds of the subsequent change in the generic ballot for congressional races; a May poll at D+4 with Democrats up 3 since becomes D+6. For gubernatorial races the factor is about 47 percent, made slightly less sensitive in September 2026, with an impact of about a tenth of a point.

*Numbers:* trendline factor, congressional = 2/3 share of generic ballot change (FLIPR 2026); trendline factor, gubernatorial = approximately 47 percent (FLIPR 2026)

*Why:* Governor races are less partisan, so the generic ballot is less informative about them.

> In FLIPR, the trendline adjustment shifts “old” polls by 2/3 of the direction of the change in the generic ballot.

<sub>2026-09-20_expert-ratings-are-ignoring-signs-of-a-blue-wave#5</sub>

### 2026-10-22 · [Fake polls are a real problem](https://www.natesilver.net/p/fake-polls-are-a-real-problem)
**parameter or number** · Silver Bulletin polling averages · explicit

Silver Bulletin turns on a polling average for a race once there are three distinct polls from at least two distinct polling firms.

*Numbers:* minimum polls for an average = 3 polls (from at least 2 firms)

> we turn on the average for a race once there are three distinct polls from at least two distinct polling firms.

<sub>2026-10-22_fake-polls-are-a-real-problem-by-nate-silver#2</sub>

### 2026-10-22 · [Fake polls are a real problem](https://www.natesilver.net/p/fake-polls-are-a-real-problem)
**method** · Silver Bulletin 2026 · explicit

Silver Bulletin computes retrospective polling averages for dates before its averages launch (FLIPR launched Aug. 11, 2026), and they closely resemble other aggregators' averages.

> For dates before then, I’ve used our retrospectively-calculated polling averages instead

<sub>2026-10-22_fake-polls-are-a-real-problem-by-nate-silver#7</sub>

### 2026-11-02 · [Where polls and fundamentals clash](https://www.natesilver.net/p/where-polls-and-fundamentals-clash)
**method** · FLIPR 2026 · explicit

The polls-versus-fundamentals comparison includes only races with at least three polls from two unique pollsters, matching the threshold for publishing a polling average.

> Note that we’re only including races that have at least three polls from two unique pollsters in this analysis.

<sub>2026-11-02_where-polls-and-fundamentals-clash-by-eli-mckown-dawson#5</sub>

### 2026-11-03 · [FINAL FLIPR 2026 midterm election forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-polls-model)
**method** · FLIPR 2026 · explicit

Summary of FLIPR's polling averages: they account for registered versus likely voters and house effects, weight more reliable polls more heavily, and apply a 'timeline adjustment' revising outdated polls toward generic-ballot trends. FLIPR uses an LV-adjusted generic ballot.

> They also include a “timeline adjustment”, where outdated polls are revised to reflect trends in the generic ballot.

<sub>2026-11-03_2026-midterm-election-forecast-senate-house-silver-bulletin#2</sub>
