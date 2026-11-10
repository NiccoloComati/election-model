# Model evaluation and calibration

68 findings from 36 articles, oldest first.

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**parameter or number** · FiveThirtyEight 2018 midterm · explicit

Share of House races called correctly, 1998-2016 training data, 100 days out and on Election Day: Lite 94.2 and 96.2 percent; fundamentals alone 95.4 and 95.7; Classic 95.4 and 96.7; expert ratings alone 94.8 and 96.6; Deluxe 95.7 and 96.9. In training, Classic miscalled 3.3 percent of House races versus 3.8 for Lite.

*Numbers:* Lite Election Day accuracy = 96.2 percent (House 1998-2016); Classic Election Day accuracy = 96.7 percent (House 1998-2016); Deluxe Election Day accuracy = 96.9 percent (House 1998-2016); fundamentals-only 100 days = 95.4 percent (House 1998-2016)

> In the training data, Classic miscalled 3.3 percent of House races, compared with 3.8 percent for Lite.

<sub>fte_midterm-house-senate-governor-methodology#6</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**empirical regularity** · FiveThirtyEight · explicit

FiveThirtyEight reports its models, including election forecasts since 2008, have been well calibrated over time, and its 2016 forecast gave Trump about 30 percent, higher than other models and markets, partly by detecting his potential Electoral College overperformance.

*Numbers:* 2016 Trump probability = around 30 percent (final)

> Candidates who our models claim have a 30 percent chance of winning really do win their races about 30 percent of the time

<sub>fte_2020-presidential-forecast-methodology#32</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**design principle** · general principle · explicit

Silver argues it is bad practice to retroactively revise already-published data, such as removing a later-banned pollster from historical polling averages and pollster ratings, based on decisions made long after publication.

*Why:* Retroactive revision makes the numbers less reliable as a historical record.

> It's bad practice to revise data that's already been published, based on decisions you made long after that data was published.

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#7</sub>

### 2023-09-20 · [The election model is a little too popular](https://www.natesilver.net/p/the-election-model-is-a-little-too)
**empirical regularity** · 538 2016 and 2022 · explicit

Silver says the FiveThirtyEight model departed from the consensus in two notable years. In 2016 it was much more bullish on Trump than the consensus. In 2022 it was somewhat more bullish on Democrats than the consensus.

*Why:* These examples show the model often got lumped in with other coverage even though it bucked that coverage.

> Our model was much more bullish on Trump than the consensus in 2016 and somewhat more bullish on Democrats than the consensus in 2022.

<sub>2023-09-20_the-election-model-is-a-little-too-popular-by-nate-silver#4</sub>

### 2023-09-20 · [The election model is a little too popular](https://www.natesilver.net/p/the-election-model-is-a-little-too)
**design principle** · 538 2008-2022 · explicit

Silver holds that a forecasting model should be judged by its long-term documented calibration and accuracy record, not by partisan narratives about individual elections. He says 538's models have a long, well-documented record of strong calibration and accuracy.

*Why:* Partisan narratives about the models are detached from their actual track record.

> completely detached from their long, well-documented track record of strong calibration and accuracy

<sub>2023-09-20_the-election-model-is-a-little-too-popular-by-nate-silver#5</sub>

### 2023-12-07 · [The incumbency advantage is disappearing. Maybe it's the algorithms' fault.](https://www.natesilver.net/p/the-incumbency-advantage-is-disappearing)
**limitation or failure mode** · general principle · explicit

Silver cautions that conclusions from historical presidential election data rest on small samples and depend on where the data is cut. The incumbency trend should therefore be treated as suggestive rather than definitive.

*Why:* Few presidential elections exist, and results are sensitive to the cutoff chosen.

> whenever we’re analyzing historical election results, we’re unavoidably doomed to jump to conclusions based on small sample sizes

<sub>2023-12-07_the-incumbency-advantage-is-disappearing-maybe-its-the-algorithms-fault#3</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**empirical regularity** · 538 2022 midterms · explicit

In 2022, polls of the House popular vote were nearly exactly right and polls were highly accurate in aggregate. Democrats were very slightly overestimated overall. Forecast models had Republicans favored in the House and the Senate as close, which the results reasonably matched. 'Red wave' predictions came from pundits and defied the polling averages.

> it was a way better year for the polling industry than the takes industry.

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#11</sub>

### 2024-04-17 · [Announcing 2024 election model plans](https://www.natesilver.net/p/announcing-2024-election-model-plans)
**empirical regularity** · 538 2008-2022 lineage · explicit

Silver claims the model's historical forecasts have been extremely well-calibrated: events forecast at e.g. 70% have happened about 70% of the time over a large sample. He calls it the only model in the business with a long-term track record.

*Numbers:* example probability = 70 percent (calibration illustration)

*Why:* 'Truth in advertising'.

> events that are forecasted to have e.g. a 70 percent chance of occurring have in fact happened about 70 percent of the time over a large sample of data.

<sub>2024-04-17_announcing-2024-election-model-plans-by-nate-silver#7</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**design principle** · general principle · explicit

A model should sometimes surprise its builder. Always matching intuition suggests wasted effort or reverse-engineering assumptions to match priors. Extremely counterintuitive outputs, such as Obama at 96% in June 2012, still warrant checking for bugs or flaws, so domain knowledge plays a role.

*Why:* Avoid tuning to priors while catching bugs.

> I’d essentially worked backward, tweaking the assumptions in the model until they matched my priors

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#42</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**limitation or failure mode** · general principle · explicit

Presidential forecasting has tiny samples: 2024 is only the 20th presidential election since WWII and roughly the 10th-12th with robust state-level polling. As a result there is no single right model. Congressional forecasting, with almost 500 relatively independent races per cycle, allows assumptions to be tested better.

*Numbers:* post-WWII presidential elections = 20 elections (through 2024); elections with robust state polling = 10th or 12th elections (roughly); House+Senate races per cycle = almost 500 races

> This is only the 20th presidential election since World War II, and only roughly the 10th or 12th with any sort of robust, state-by-state polling data.

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#43</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**limitation or failure mode** · 2024 presidential · explicit

Backtesting on historical data (e.g., 1968) is not the same as publishing in real time. A late replacement candidate might violate implicit model assumptions, so results would need sanity checks before republishing.

> Backtesting a model on 1968 data isn't the same as publishing one in real time.

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#10</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**design principle** · general principle · explicit

Calibration alone is insufficient: you can be perfectly calibrated by predicting every race at 50/50. Discrimination, the ability to distinguish more likely from less likely outcomes, also matters. Silver prefers models that offer a credible, independent opinion even if sometimes wrong.

*Why:* Forecasters have improved at avoiding overfitting, so a model with some 'bite' is acceptable.

> you can be perfectly calibrated just by predicting every race at 50/50. What statisticians call "discrimination" — a model's ability to distinguish relatively less likely outcomes from more likely ones — is important, too.

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#13</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**parameter or number** · 2024 presidential · explicit

On July 18, 2024, the Silver Bulletin forecast gave Biden a 28 percent chance of winning, while 538 gave him 53 percent.

*Numbers:* Silver Bulletin Biden win probability = 28 % (July 18, 2024); 538 Biden win probability = 53 % (July 18, 2024)

> Biden’s chances are probably lower than the current 28 percent in the Silver Bulletin forecast

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#6</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**interpretation guidance** · general principle · explicit

A model should not be judged as having 'won' based on a single election outcome, since a sample of one cannot validate probabilistic forecasts.

> an unsound model is validated because it “won” the model wars based on a sample size of one election

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#24</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**limitation or failure mode** · general principle · explicit

Design flaws and bugs in election models are often hard to detect through backtesting alone and usually surface only under real-world stress tests. Examples are sign flips, misentered polls (such as an Alabama poll coded as Arizona), and complicated components that combine to be less than the sum of their parts.

> it’s often hard to detect these design flaws through backtesting alone — usually you only learn the hard way once a model is stress-tested under real world conditions

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#25</sub>

### 2024-08-08 · [Welcome to the bizarre world of conditional probability](https://www.natesilver.net/p/welcome-to-the-bizarre-world-of-conditional)
**limitation or failure mode** · general principle · explicit

Extreme tail probabilities (e.g., whether Trump's chance of winning California is 0.4% or 0.04%) cannot be validated empirically, because doing so would require hundreds of elections.

*Numbers:* model CA probability = 0.4 percent (Trump wins CA); alternative = 0.04 percent (hypothetical)

> we'd need a sample of hundreds of elections to test that, and we'll never get that in our lifetimes.

<sub>2024-08-08_welcome-to-the-bizarre-world-of-conditional-probability#13</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**limitation or failure mode** · general principle · explicit

Special-case adjustments for one-off events such as the COVID pandemic cannot be validated, because there will never be an adequate sample size for them.

*Why:* A once-in-a-century event gives no repeated sample.

> we’ll never get an adequate sample size for what was (hopefully) a once-in-a-century pandemic

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#2</sub>

### 2024-09-19 · [Don't let randomness make a fool of you](https://www.natesilver.net/p/dont-let-randomness-make-a-fool-of)
**interpretation guidance** · general principle · explicit

A well-calibrated forecast's 20% outcomes should occur about 20% of the time. An 80/20 forecast in which the underdog wins is therefore not evidence that the model failed.

*Numbers:* example forecast = 80/20 percent (Election Day forecast)

> as 20 percent probabilities have an uncanny knack for doing 20 percent of the time

<sub>2024-09-19_dont-let-randomness-make-a-fool-of-you-by-nate-silver#14</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**empirical regularity** · general principle · explicit

Validation example: NYT/Siena October 2022 polls of four battleground House districts showed Democrats doing surprisingly well, and Democrats won all four. In KS-3 the poll had Davids +13 and she won by 12.1.

*Numbers:* KS-3 poll margin = 13 percentage points (NYT/Siena, Oct 2022); KS-3 actual margin = 12.1 percentage points (2022 result); districts polled/won by Dems = 4/4 (NYT/Siena Oct 2022)

> Democrats won all four districts, including Davids by a 12.1-point margin.

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#19</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**empirical regularity** · 538 2012 · explicit

In 2012, Silver's bottom-up (sum of states) popular vote method correctly showed Obama winning the popular vote by a wider margin than national polls projected.

*Why:* Cited as evidence supporting the bottom-up approach.

> like in 2012 when it correctly had Barack Obama winning the popular vote by a wider margin than national polls projected

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#2</sub>

### 2024-09-29 · [The 128 paths to the White House](https://www.natesilver.net/p/the-128-paths-to-the-white-house)
**critique of other approach** · general principle · explicit

Silver argues that anyone projecting the 2024 race with high confidence is overconfident.

> Anybody who’s projecting this race with a great deal of confidence is just selling you hopium or snake oil.

<sub>2024-09-29_the-128-paths-to-the-white-house-by-nate-silver#18</sub>

### 2024-10-08 · [55/45 is a really close race](https://www.natesilver.net/p/5545-is-a-really-close-race)
**design principle** · general principle · explicit

Experienced sports bettors avoid marginal edges such as 53/47 or 54/46, just above the 52.5% vig breakeven. They do this to reduce variance and because there is ultimately no way to know their model is right. Silver's point is that small model edges deserve humility.

*Numbers:* point-spread breakeven = 52.5 percent (sports betting with vig)

*Why:* Model uncertainty and variance.

> there's ultimately no way to know that your model is right

<sub>2024-10-08_5545-is-a-really-close-race-by-nate-silver#16</sub>

### 2024-10-09 · [When you should panic about the polls](https://www.natesilver.net/p/when-you-should-panic-about-the-polls)
**interpretation guidance** · 2024 presidential · explicit

Harris's Electoral College probability had fallen to 54% from a peak of 58% on Sept. 27, 2024. Silver presents this as the model not perceiving a major change in the race.

*Numbers:* Harris EC probability = 54 percent (Oct 9, 2024); peak = 58 percent (Sept 27, 2024)

> now 54 percent, down from a peak of 58 percent on Sept. 27 — it doesn't yet perceive a major change in the race.

<sub>2024-10-09_when-you-should-panic-about-the-polls-by-nate-silver#11</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**empirical regularity** · 538 2022 · explicit

In 2022, Silver's model was bullish on Democrats relative to conventional wisdom and never bought into the 'red wave' narrative.

> we were bullish on Democrats relative to the conventional wisdom and never really bought into the "red wave" narrative

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#8</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**empirical regularity** · 2024 presidential · explicit

The actual 2024 map was the modal map in the final 2024 Silver Bulletin presidential model: Trump swept all 7 swing states, and every other state and district went to its forecast favorite. It appeared in 4,660 of 80,000 simulations.

*Numbers:* simulations with exact actual map = 4,660 simulations (out of 80,000)

> Tuesday’s exact map was the modal (most common) one in our final model, coming up in 4,660 of our final 80,000 simulations

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#3</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**empirical regularity** · 2024 presidential · explicit

Treated as deterministic calls, the final 2024 state forecasts were correct in 48 of 50 states. The misses were Michigan, where Trump led by 1.5 points, and Wisconsin, where he led by 0.9 points; the model had favored Harris narrowly in both.

*Numbers:* correct calls = 48 of 50 states (2024); Trump lead in Michigan = 1.5 percentage points (vote count as of Nov 7); Trump lead in Wisconsin = 0.9 percentage points (vote count as of Nov 7)

> Michigan and Wisconsin are highlighted in a lighter shade of blue because they are the two we missed

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#7</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**method** · 2024 presidential · explicit

Silver evaluates the model by conditioning on the actual map. Among the 4,660 simulations producing the exact actual map, the projected state margins missed actual results by an average of only 2.3 points. He notes this is less impressive than it sounds because the model is told every state's winner, but says it shows the model's internal logic is sound.

*Numbers:* average miss of conditional margins = 2.3 percentage points (preliminary results as of Thursday Nov 7 morning)

*Why:* Tests whether the joint structure of state outcomes is coherent.

> missing by an average of only 2.3 points, given results as reported so far

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#20</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**parameter or number** · 2024 presidential · inferred_from_chart

Conditional projected Trump margins compared with actual results (preliminary), Trump overperformance:
- California: −25.3 projected vs −17.2 actual
- New Jersey: −13.1 vs −5.0
- North Dakota: +30.7 vs +36.7 (+6.0)
- Illinois: −13.0 vs −8.4 (+4.6)
- Hawaii: −27.6 vs −23.1 (+4.5)
- New York: −15.9 vs −11.6 (+4.3)
- Iowa: +9.0 vs +13.2 (+4.2)
- Maryland: −27.1 vs −22.9 (+4.2)
- Florida: +9.0 vs +13.1 (+4.1)
- Texas: +11.0 vs +13.9 (+2.9)

Trump underperformance:
- Utah: +27.6 vs +20.7 (−6.9)
- Washington: −14.8 vs −19.5 (−4.7)
- Oregon: −8.2 vs −12.6 (−4.4)
- Nebraska CD1: +18.2 vs +13.9 (−4.3)
- Delaware: −11.4 vs −14.7 (−3.3)
- Colorado: −9.6 vs −12.4 (−2.8)
- Georgia: +4.1 vs +2.2 (−1.9)
- Louisiana: +23.8 vs +22.0 (−1.8)
- Maine CD2: +10.2 vs +8.5 (−1.7)
- New Mexico: −4.1 vs −5.7 (−1.6)

Other rows: Arizona +5.3 vs +5.5; Alabama +30.4 vs +30.6; DC −88.2 vs −85.7; Maine −6.1 vs −7.0.

*Numbers:* California delta = +8.1 points (computed); New Jersey delta = +8.1 points (computed); Utah delta = -6.9 points

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#21</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**interpretation guidance** · general principle · implied

Judging polls by whether they 'call' the correct winner is misleading in close races. Polls should be judged by the size of their error.

*Why:* In close races, small errors flip the apparent winner.

> often, polls are evaluated by whether they “call” the correct winner, and with such a close presidential race in many states

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#7</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**method** · Silver Bulletin pollster ratings / report card · explicit

Silver Bulletin defines polling error as the absolute difference between a poll's margin and the actual election margin between the top two candidates.

> By error, we mean the difference between a poll's margin and the actual margin of the election between the top two candidates.

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#0</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**limitation or failure mode** · Silver Bulletin pollster ratings · explicit

The 2024 cycle's low average error was partly an artifact of composition. There were few presidential primary polls, which are the highest-error type, so their absence pulled the combined average down.

> primary polls also tend to have the largest polling error... so their relative absence this cycle helped pull down the average error

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#12</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**interpretation guidance** · general principle · explicit

Call accuracy (whether the poll leader won) is a poor measure of poll accuracy and serves only as a sanity check. A poll showing Trump +1 in a state he won by 13 is still a bad result, while a poll showing Trump +1 when Harris won by 1 would be pretty good.

*Why:* Magnitude of error matters, not just direction.

> we've never thought of this as a great way to assess how accurate the polls are

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#23</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**method** · Silver Bulletin pollster ratings · inferred_from_chart

In call-accuracy scoring, a pollster gets half-credit if its poll shows a tie for the lead and one of the tied candidates wins.

*Numbers:* tie credit = 0.5 (call accuracy)

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#24</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**empirical regularity** · Silver Bulletin pollster ratings · explicit

Polls have called the correct winner 77.8% of the time since 1998 (about 78%). In 2024 the rate was 70.1%, the lowest on record. Presidential general election polls called 62.8% correctly, the worst since 1998. House polls called 65.6%, Senate 77.8%, governor 92.2% and presidential primary 97.3%.

*Numbers:* all-years call accuracy = 77.8 %; 2024 combined = 70.1 %; 2024 pres general = 62.8 %; 2024 House = 65.6 %; 2024 Senate = 77.8 %; 2024 Gov = 92.2 %; 2024 pres primary = 97.3 %

> Across all cycles since 1998, polls have predicted the correct winner 78 percent of the time. In 2024, call accuracy was only 70 percent

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#25</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**parameter or number** · Silver Bulletin pollster ratings · inferred_from_chart

All-years call accuracy by race type: presidential primary 82.8%, presidential general 76.9%, Senate 80.8%, House 72.2%, governor 82.1%.

*Numbers:* pres primary = 82.8 %; pres general = 76.9 %; Senate = 80.8 %; House = 72.2 %; Governor = 82.1 %

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#26</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**interpretation guidance** · general principle · explicit

Call accuracy depends heavily on how competitive the polled races are. 2024 primary polls scored high because the race was noncompetitive, and general election polls scored low because the race was close. Pollsters increasingly concentrate on competitive states, which lowers measured call accuracy.

> it's a function of the races being polled in each case

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#29</sub>

### 2025-05-06 · [We're tracking more data on Trump's popularity](https://www.natesilver.net/p/were-tracking-more-data-on-trumps)
**limitation or failure mode** · general principle · explicit

Election polls can be checked against actual vote results, but approval and issue polls have no hard benchmark. Their accuracy can only be inferred indirectly, for example from special elections or consumer data.

> With other types of surveys — issue polling or approval rating numbers — there usually isn't any hard data to compare them against.

<sub>2025-05-06_were-tracking-more-data-on-trumps-popularity#12</sub>

### 2025-06-02 · [SBSQ #21: Why young men don't like Democrats](https://www.natesilver.net/p/sbsq-21-why-young-men-dont-like-democrats)
**design principle** · general principle · explicit

It is far easier to build an overconfident model than an underconfident one. Most ways of making mistakes when building a model lead to underestimating the chance of low-likelihood but nonzero events.

*Why:* Silver states this from long modeling experience. Regression models implicitly assume normal tails, and models have many interacting parameters.

> most of the ways to fuck up when building a model result in overconfidence rather than underconfidence, i.e. underestimating the chance of low-likelihood but nonzero events.

<sub>2025-06-02_sbsq-21-why-young-men-dont-like-democrats#1</sub>

### 2025-06-02 · [SBSQ #21: Why young men don't like Democrats](https://www.natesilver.net/p/sbsq-21-why-young-men-dont-like-democrats)
**critique of other approach** · general principle · explicit

Regression-based probability models implicitly assume a normal distribution rather than a fat-tailed one. This is one source of overconfidence.

*Why:* Extreme outcomes occur more often than normal tails imply.

> regression models implicitly assume a normal distribution rather than a "fat-tailed" distribution where "extreme" outcomes are comparatively more likely.

<sub>2025-06-02_sbsq-21-why-young-men-dont-like-democrats#2</sub>

### 2025-06-02 · [SBSQ #21: Why young men don't like Democrats](https://www.natesilver.net/p/sbsq-21-why-young-men-dont-like-democrats)
**design principle** · general principle · explicit

Model parameters interact: changing one changes how the rest of the system behaves. A modeler should therefore explicitly test the model in specific scenarios (e.g., what happens when a favorite falls behind early), or the model may be miscalibrated.

*Why:* Many moving parts make miscalibration likely without scenario testing.

> If you're not explicitly testing it for certain scenarios — what happen when a pregame favorite falls behind early? — your model could be miscalibrated.

<sub>2025-06-02_sbsq-21-why-young-men-dont-like-democrats#3</sub>

### 2025-06-02 · [SBSQ #21: Why young men don't like Democrats](https://www.natesilver.net/p/sbsq-21-why-young-men-dont-like-democrats)
**interpretation guidance** · general principle · explicit

Win probability models tend to get noticed only when a huge upset happens. Judging them by memorable misses is cherry-picking, and unlikely events do happen. Evaluation should rest on comprehensive calibration evidence instead.

*Why:* Selection bias in public evaluation.

> They pretty much only get noticed when a huge upset happens, so there's inevitably a lot of cherry-picking in how people evaluate them.

<sub>2025-06-02_sbsq-21-why-young-men-dont-like-democrats#4</sub>

### 2025-06-02 · [SBSQ #21: Why young men don't like Democrats](https://www.natesilver.net/p/sbsq-21-why-young-men-dont-like-democrats)
**empirical regularity** · ESPN Analytics (critique) · explicit

A Reddit College Football analysis found severe miscalibration in in-game win probability: home teams given under 1 percent chance of winning in the fourth quarter actually won about 5 percent of the time.

*Numbers:* model-stated win probability = <1 percent (college football home teams in the 4th quarter); actual win rate = ~5 percent (same teams)

> Home teams that are given less than a 1 percent chance of winning in the fourth quarter actually win something like 5 percent of the time.

<sub>2025-06-02_sbsq-21-why-young-men-dont-like-democrats#6</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**design principle** · general principle · explicit

Strong prior regularities such as the median voter theorem should inform model checking. If a model finds that a well-established factor like moderation hardly matters at all, Silver says that result should be regarded with suspicion ('basic Bayesian reasoning').

*Why:* Exercise-is-good-for-health analogy.

> it's a strong enough regularity that if your model finds that exercise hardly matters at all, it should be regarded with suspicion. This is basic Bayesian reasoning.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#13</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**design principle** · general principle · explicit

Running a model under many specifications is good practice. Good model-builders learn which factors are robust across specifications, and this is the 'art' of statistical inference.

> What street smart model-builders do is develop a sense for which factors are most robust once they've tested out a variety of specifications.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#14</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**design principle** · general principle · explicit

If a factor matters a lot in some specifications but not in others, the underlying data may be dubious. The remedy is to quality-check the data, collect more, or develop a more rigorous processing algorithm.

> sometimes the issue is that your underlying data is dubious and you need to go back and QC the data, collect more of it, or go back to the lab

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#15</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**design principle** · general principle · explicit

Domain knowledge, such as forecasting every congressional district, helps vet model specifications and catch mismeasured inputs. Jain found enough candidates with apparently misspecified ideology scores to conclude that CFScores and B&G's other measures add a lot of noise.

> Domain knowledge — for instance, making forecasts of every Congressional district, as Split Ticket does — can help greatly for vetting different model specifications.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#16</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**limitation or failure mode** · general principle · explicit

High explained variance, such as B&G's claimed 92% of congressional vote-share variation, is not impressive because district partisanship explains most of it. Implausibly accurate fit to past elections is a sign of overfitting ('the Allan Lichtman problem').

*Numbers:* BG-WAR R² claim = 92 % of variance (congressional vote shares)

> If you claim to have "predicted" every past election with implausible accuracy, that's usually a sign that you've tortured the past data until it fit.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#19</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**design principle** · general principle · explicit

Silver holds that a true prediction is a claim about an event that has not happened yet. Holdout or out-of-sample testing cannot remove the 'original sin' of knowing the results while designing the model, because knowledge of outcomes shapes which specifications and variables the researcher considers plausible.

> There's no technique that can overcome the "original sin" of knowing what the results were before you started designing your model.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#20</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**critique of other approach** · general principle · explicit

Most advances in election forecasting have come from self-taught outsiders rather than academics, whose published forecasts have a mostly bad track record. Silver attributes this to street smarts, domain knowledge, repetitions, and skin in the game, meaning reputational or financial loss from wrong forecasts.

> In contrast, forecasts published by academics have a mostly bad track record.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#21</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**design principle** · Silver Bulletin NFL metric (in development) · explicit

Silver says he invests heavily in tiny accuracy gains (1%, 0.1%, 0.01%). He gives the example of collecting historical NFL stadium altitudes to refine home-field advantage in a Silver Bulletin NFL metric under construction.

> I can't tell you how many late nights over the years I've spent trying to eke out an extra 1 percent or 0.1 percent or 0.01 percent of accuracy from my models.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#22</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**method** · Silver Bulletin pollster ratings · explicit

Polling error is defined as the difference between a poll's margin and the actual election margin between the top two candidates.

> meaning the difference between a poll's margin and the actual margin of the election between the top two candidates

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#5</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**method** · Silver Bulletin pollster ratings · inferred_from_chart

Statistical bias, the extent to which polls consistently underestimate Democrats or Republicans, is calculated only for elections where the top two finishers were a Republican and a Democrat. It is therefore not calculated for presidential primaries.

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#6</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**interpretation guidance** · general principle · explicit

The share of polls that 'called' the race correctly, meaning the poll's leader won, is a poor accuracy measure, especially in uncompetitive races. All 2025 qualifying polls called their race correctly, but none of the races were close.

*Numbers:* 2025 call accuracy = 100 percent (2025 qualifying polls)

*Why:* Picking the right winner in uncompetitive races isn't impressive.

> Correct calls aren't a great measure of accuracy

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#11</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**method** · Silver Bulletin 2026 generic ballot average · explicit

Historical generic ballot averages for midterms from 1994 to 2022 were produced by retroactively applying the current Silver Bulletin polling average methodology to past generic ballot polls, at equivalent points in each cycle (285 days before Election Day).

*Numbers:* days before Election Day = 285 days (comparison point corresponding to Jan 22, 2026)

> the generic ballot as it appeared on equivalent days in midterm cycles since 1994 — that is, 285 days before Election Day — based on running our algorithm retroactively on past election cycles.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#6</sub>

### 2026-04-11 · [“AI polls” are fake polls](https://www.natesilver.net/p/ai-polls-are-fake-polls)
**parameter or number** · 2024 presidential · explicit

On November 2, 2024 the Silver Bulletin presidential model gave Harris a 48.2 percent chance of winning, versus 50.5 percent in Aaru's synthetic-sampling model.

*Numbers:* Silver Bulletin Harris win probability = 48.2 percent (November 2, 2024); Aaru Harris win probability = 50.5 percent (November 2, 2024)

> For comparison, our odds for Harris on the same day were 48.2 percent.

<sub>2026-04-11_ai-polls-are-fake-polls-by-eli-mckown-dawson#6</sub>

### 2026-04-21 · [SBSQ #31: Trump is super unpopular. So why don’t Democrats have a bigger lead?](https://www.natesilver.net/p/sbsq-31-trump-is-super-unpopular)
**design principle** · general · explicit

Silver scores his own published predictions, such as the 113 predictions for Trump's second term, for calibration and considers forecast calibration valuable in its own right; he found those predictions generally well-calibrated.

*Numbers:* predictions scored = 113 predictions (Trump second term)

> Generally, I found the predictions were pretty well-calibrated.

<sub>2026-04-21_sbsq-31-trump-is-super-unpopular-so-why-dont-democrats-have-a-bigger-lead#9</sub>

### 2026-08-13 · [Prediction markets aren't magic](https://www.natesilver.net/p/prediction-markets-arent-magic)
**interpretation guidance** · general principle · explicit

For a model or market to be well calibrated, 5 percent chances must happen about 5 percent of the time, not zero; quantifying uncertainty is described as most of the work in a model like FLIPR.

> for a model or a market to be well-calibrated, 5 percent chances are supposed to happen 5 percent of the time, not zero percent.

<sub>2026-08-13_prediction-markets-arent-magic-by-nate-silver#4</sub>

### 2026-09-20 · [Expert ratings are ignoring signs of a blue wave](https://www.natesilver.net/p/expert-ratings-are-ignoring-signs)
**design principle** · general principle · explicit

Changes in a forecast should not be predictable: the best prediction of tomorrow's forecast is today's forecast, otherwise predictive information is being left on the table. Forecasts should be evaluated on what they said throughout the cycle, not only on Election Day.

> Put another way, the best prediction of what your forecast says tomorrow should be the forecast today.

<sub>2026-09-20_expert-ratings-are-ignoring-signs-of-a-blue-wave#7</sub>

### 2026-09-29 · [Midterm waves are the rule, not the exception](https://www.natesilver.net/p/midterm-waves-are-the-rule-not-the)
**empirical regularity** · FiveThirtyEight/Silver Bulletin track record · explicit

Silver says Silver Bulletin/FiveThirtyEight forecasts have essentially never been on the opposite side of the conventional wisdom; differences have been in degree of confidence: more cautious than consensus about Clinton in 2016, and confident that Biden's 2020 lead could withstand a 2016-sized polling error, which it did even though 2020 polls were more biased.

> general election polls were actually more biased in 2020 than in 2016, but Biden’s lead was big enough to absorb the blow.

<sub>2026-09-29_midterm-waves-are-the-rule-not-the-exception#7</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**interpretation guidance** · FiveThirtyEight 2012 · explicit

FiveThirtyEight's 2012 model called every state correctly, but its internal diagnostics gave only a slim chance of a perfect score (Florida was about 50/50). Correct calls can mask margin errors; 2012 polls overestimated Romney by about 3 points.

> Our internal diagnostics gave us only a slim chance of getting a perfect score.

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#13</sub>

### 2026-10-20 · [My pet peeve about the polling error debate](https://www.natesilver.net/p/my-pet-peeve-about-the-polling-error)
**critique of other approach** · FiveThirtyEight 2016 / FLIPR 2026 · explicit

Models that treated races as independent coin flips, giving Trump about 1 percent in 2016 versus FiveThirtyEight's roughly 30 percent, have died out. Most 2026 competitor models look reasonable to Silver, and the remaining differences are in how errors are modeled, how polls and fundamentals are blended, and how aggressively averages update.

> The models that wrongly treated races as a series of independent coin flips have died out, and deservedly so.

<sub>2026-10-20_my-pet-peeve-about-the-polling-error-debate#7</sub>

### 2026-11-01 · [13 maps for the morning after the midterms](https://www.natesilver.net/p/13-morning-after-the-midterm-maps)
**method** · Silver Bulletin analysis · explicit

Silver's 'upset percentile' for a simulation scores each race by how unlikely the winner was: a 49 percent winner earns 1 point, a 1 percent winner 49 points. Branch averages are weighted 50 percent Senate, 25 percent House and 25 percent governors, then ranked as a percentile among 40,000 simulations, with no adjustment for the map's overall direction.

*Numbers:* Senate weight in upset score = 50 percent; House weight = 25 percent; governor weight = 25 percent

*Why:* With 506 races, some upsets are almost certain.

> A race where a candidate who had a 49 percent chance of prevailing wins gets 1 Upset Point; a race where a candidate who had a 1 percent chance pulls a rabbit out of their hat is worth 49 Upset Points.

<sub>2026-11-01_13-maps-for-the-morning-after-the-midterms-by-nate-silver#3</sub>

### 2026-11-03 · [How to judge an election model](https://www.natesilver.net/p/how-to-judge-an-election-model)
**design principle** · general principle · explicit

Probabilistic forecasts should be judged by calibration over a large sample of true out-of-sample predictions; for example, of 100 events forecast at 30 percent, 27 to 34 occurring is good. Backtesting does not count, since any competent model fits past data and may be overfit. Silver considers bragging about backtested results a negative sign compared with explaining why a model makes structural sense.

*Why:* Overfitting to random features of past data.

> Backtesting doesn’t count.

<sub>2026-11-02_how-to-judge-an-election-model-by-nate-silver#0</sub>

### 2026-11-03 · [How to judge an election model](https://www.natesilver.net/p/how-to-judge-an-election-model)
**empirical regularity** · FiveThirtyEight/Silver Bulletin lineage · explicit

Over the 18-year FiveThirtyEight/Silver Bulletin track record of published out-of-sample forecasts, sports forecasts were extremely well-calibrated, while politics forecasts were well-calibrated but somewhat underconfident, with too few upsets relative to model expectations. Significance is hard to assess because polling errors are correlated across states.

*Numbers:* track record length = 18 years (2008-2026)

> Our politics forecasts were pretty well-calibrated too, although actually a bit underconfident: there were actually too few upsets relative to what our models expected.

<sub>2026-11-02_how-to-judge-an-election-model-by-nate-silver#1</sub>

### 2026-11-03 · [How to judge an election model](https://www.natesilver.net/p/how-to-judge-an-election-model)
**interpretation guidance** · general principle · explicit

Calibration alone is insufficient: a model forecasting everything at 50/50 is perfectly calibrated but useless, so discrimination (e.g. Brier score) also matters. Under a Bayesian view, a very low-probability event occurring (e.g. 0.03 percent) is much more damaging to a model than a 30 percent event.

> A 0.03 percent chance happening is much more suspect for your model than a 30 percent hitting.

<sub>2026-11-02_how-to-judge-an-election-model-by-nate-silver#2</sub>

### 2026-11-03 · [How to judge an election model](https://www.natesilver.net/p/how-to-judge-an-election-model)
**method** · FiveThirtyEight 2016 / FLIPR 2026 · explicit

A model can also be judged by whether betting on it would have made money against markets and consensus. In 2016, with FiveThirtyEight giving Trump about 1 in 3 and markets offering 5-1 or 6-1, the model implied a large Trump bet. In 2026 FLIPR led Polymarket's Senate odds over time, reaching the same place faster.

> If you trusted our model in 2016, you should actually have made a large bet on Trump

<sub>2026-11-02_how-to-judge-an-election-model-by-nate-silver#3</sub>

### 2026-11-03 · [How to judge an election model](https://www.natesilver.net/p/how-to-judge-an-election-model)
**design principle** · FLIPR 2026 · explicit

A well-constructed model responds proportionally, in magnitude and direction, to new evidence. For example, a set of very strong NYT/Siena polls raised Democratic Senate odds about 2 points, reasonable because odds were already favorable and NYT/Siena was expected to lean somewhat Democratic.

*Numbers:* Senate odds change from NYT/Siena batch = about 2 percentage points (Nov 1-2, 2026)

> The third thing I always look at is whether a model responds proportionally to new evidence.

<sub>2026-11-02_how-to-judge-an-election-model-by-nate-silver#4</sub>

### 2026-11-03 · [How to judge an election model](https://www.natesilver.net/p/how-to-judge-an-election-model)
**design principle** · FLIPR 2026 · explicit

To tell luck from skill, test the model's structural hypotheses against results, for example that incumbency matters less, that midterm state errors are correlated less than in presidential years, and that governor races are less partisan. Judge margins, not just calls: a 1-point loss where the model was confident is a bad forecast even if the call was right.

> For all of this, by the way, margins ought to matter and not just the final calls.

<sub>2026-11-02_how-to-judge-an-election-model-by-nate-silver#5</sub>
