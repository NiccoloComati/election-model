# Pollster ratings

110 findings from 23 articles, oldest first.

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**data source** · FiveThirtyEight pollster ratings 2023 · explicit

The pollster ratings database includes polls conducted in 1998 or later with a median field date within 21 days of the election, for presidential general elections, presidential primaries and caucuses, and Senate, House and governor general elections. Special elections, runoffs, instant-runoff rounds, all-party primaries, and national presidential and generic ballot polls are included, even if they were not used in forecasts.

*Numbers:* start year = 1998 year; window = 21 days (median field date before election)

*Why:* 1998 is when multiple comprehensive data sources begin.

> They have a median field date within 21 days of the election date.

<sub>fte_pollster-ratings-methodology#0</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**method** · FiveThirtyEight pollster ratings 2023 · explicit

Collection rules: missing sample sizes are estimated from the reported margin of error or the firm's other polls, with 600 as a last-resort default; only the likely-voter version is kept when multiple populations are published; multiple versions of one survey (e.g. with and without a third-party candidate) are averaged; tracking polls are restricted to non-overlapping dates.

*Numbers:* default sample size = 600 respondents (last resort)

> As a last resort, we use 600 as a default sample size.

<sub>fte_pollster-ratings-methodology#1</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**method** · FiveThirtyEight pollster ratings 2023 · explicit

Presidential primary poll exclusions: New Hampshire polls before the Iowa caucus; polls of later states before New Hampshire; polls whose leader or runner-up dropped out before the primary; polls where any candidate at 15 percent or more, or any combination at 25 percent or more, dropped out before the primary.

*Numbers:* single dropout threshold = 15 percent (exclude poll); combined dropout threshold = 25 percent (exclude poll)

> We exclude primary polls if any candidate receiving at least 15 percent in the poll dropped out before that primary was held.

<sub>fte_pollster-ratings-methodology#2</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**method** · FiveThirtyEight pollster ratings 2023 · explicit

Polls are attributed to the firm that conducted them regardless of sponsor, or to partnerships (e.g. 'Fabrizio, Lee & Associates/Impact Research'). Media companies with in-house operations are credited when they contributed the most methodological IP, which is why NYT/Siena is separate from Siena. Companies run by the same team with the same methodology are evaluated together.

> Our policy is to classify polls based on the pollster that conducted them, regardless of sponsorship

<sub>fte_pollster-ratings-methodology#3</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**method** · FiveThirtyEight pollster ratings 2023 · explicit

Simple error is the absolute difference between a poll's margin and the certified result's margin between the top two finishers in the election, not the top two in the poll. A pollster's simple average error is computed as a root-mean-square error.

> This average is calculated using root-mean-square error .

<sub>fte_pollster-ratings-methodology#4</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**method** · FiveThirtyEight pollster ratings 2023 · explicit

Simple Plus-Minus equals a pollster's simple average error minus the error expected from a regression on election type, the poll's sampling margin of error and days between poll and election; for example, 4.6 actual against 5.3 expected gives -0.7, where negative is better. Presidential general polls are historically the most accurate, primaries the least.

*Why:* Some elections are harder to poll.

> We run a regression analysis that predicts polling error based on the type of election surveyed, a poll’s margin of sampling error and the number of days between the poll and the election.

<sub>fte_pollster-ratings-methodology#5</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**design principle** · FiveThirtyEight pollster ratings 2023 · explicit

Ratings use all polls in the final three weeks rather than only each firm's last poll. Late game-changers are rare; herding increases in the final days; some late movement is artificial, from response bias or bad turnout models; much voting is early (over 80 percent in Arizona's 2022 Senate race); and a larger sample improves confidence. Three, four or five-week windows give no significant differences, and ratings adjust for the slight advantage of polling closer to Election Day.

*Numbers:* early/mail share AZ 2022 Senate = over 80 percent (example)

> But we feel strongly that evaluating a polling firm’s accuracy based only on its very last poll before an election is a mistake.

<sub>fte_pollster-ratings-methodology#7</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**parameter or number** · FiveThirtyEight pollster ratings 2023 · explicit

Advanced Plus-Minus blends Relative Plus-Minus (performance against other polls of the same race) with weight n, the number of other firms polling that race, and Simple Plus-Minus with weight 3; for example, with six other firms, Relative gets two-thirds. Strength of competition is handled by iteration, as in sports power ratings.

*Numbers:* Simple Plus-Minus weight = 3 weight units (vs n for Relative)

*Why:* With many polls, judge relative to peers; with few, judge on absolute error.

> Relative Plus-Minus gets the weight of n , and Simple Plus-Minus gets a weight of three.

<sub>fte_pollster-ratings-methodology#8</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**adjustment rule** · FiveThirtyEight pollster ratings 2023 · explicit

Advanced Plus-Minus also adjusts for how many other firms polled the same race, because polls are more accurate when more are in the field (herding or selection bias). It rewards firms that poll neglected races and penalizes those arriving after a dozen polls. It puts slightly more weight on recent polls and adjusts for the higher volatility of election types such as presidential primaries.

> This has the effect of rewarding polling firms that survey races few other pollsters do and penalizing those that swoop in only after there are already a dozen polls in the field.

<sub>fte_pollster-ratings-methodology#9</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**parameter or number** · FiveThirtyEight pollster ratings 2023 · explicit

Predictive Plus-Minus formula: PPM = [max(-2, APM + herding_penalty) x disc_pollcount + prior x 18] / (18 + disc_pollcount), where disc_pollcount discounts older polls. In 2023 the prior was 0.66 - 0.57 x quality + min(18, disc_pollcount) x -0.03, with quality = 1 if the firm is in the AAPOR Transparency Initiative or contributes to the Roper Center archive, else 0. APM is floored at -2, and the prior gets an effective weight of 18 polls.

*Numbers:* shrinkage weight on prior = 18 effective polls (PPM formula); APM floor = -2 points (PPM formula); prior intercept = 0.66 points (2023); quality bonus = -0.57 points (2023); poll count slope = -0.03 points per poll (capped at 18)

*Why:* Mean reversion toward a methodology-dependent prior.

> it is currently calculated as 0.66 – quality ⋅ 0.57 + min (18, disc_pollcount ) ⋅ -0.03.

<sub>fte_pollster-ratings-methodology#10</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**empirical regularity** · FiveThirtyEight pollster ratings 2023 · explicit

Past performance reflects more noise than signal until a firm has about 30 polls; below that, methodological standards are the better guide, and above it past performance should be favored. In every cycle evaluated, pollsters in AAPOR Transparency or Roper performed significantly better.

*Numbers:* polls needed for track record to dominate = about 30 polls

> Our finding is that past performance reflects more noise than signal until you have about 30 polls to evaluate

<sub>fte_pollster-ratings-methodology#11</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**parameter or number** · FiveThirtyEight pollster ratings 2023 · explicit

Senate polls from 2006 to 2013 showed methodologically poor pollsters improving their accuracy by about 2 points when strong polls were also in the field, evidence of herding. The herding penalty is half the difference between a firm's actual ADPA (average distance from the average of previous polls with median field date at least three days earlier) and its theoretical minimum ADPA from sampling error of its polls and the comparison average.

*Numbers:* herding accuracy gain for weak pollsters = roughly 2 points (Senate 2006-2013); herding penalty factor = 0.5 x (min ADPA - actual ADPA); ADPA comparison lag = 3 days (earlier median field date)

> The herding penalty for each pollster is one-half of the difference between a pollster’s actual ADPA and its theoretical minimum ADPA based on sampling error

<sub>fte_pollster-ratings-methodology#12</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**method** · FiveThirtyEight pollster ratings 2023 · explicit

Predictive Plus-Minus is converted to letter grades from A+ to D-, with about 83 percent of firms in the B or C range. Banned firms, for fabrication or for trading in betting markets affected by their own polls, get an F, which no PPM value can produce. Firms with fewer than roughly 20 recent polls get provisional grades of A/B, B/C or C/D.

*Numbers:* share of firms graded B or C = about 83 percent (2023); polls for precise grade = roughly 20 recent polls

> It takes roughly 20 recent polls (or a larger number of older polls) for a pollster to get a precise pollster rating.

<sub>fte_pollster-ratings-methodology#13</sub>

### 2023-03-10 · [How Our Pollster Ratings Work](https://fivethirtyeight.com/methodology/how-our-pollster-ratings-work/)
**interpretation guidance** · FiveThirtyEight pollster ratings 2023 · explicit

For retrospective accuracy, Silver recommends Mean-Reverted Advanced Plus-Minus. For predicting future accuracy, as forecasting models need, Predictive Plus-Minus is used, and letter grades are based entirely on it.

> our letter grades are based entirely on Predictive Plus-Minus.

<sub>fte_pollster-ratings-methodology#14</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**design principle** · general principle · explicit

Silver argues that pollster partisanship should be judged empirically by testing polls against actual election results. Pollsters' track records hold them accountable for any political bias that makes their polls less accurate.

*Why:* Unlike most pundits, pollsters have track records that can be tested against outcomes.

> pollsters have a track record that can be tested against actual results. They can be held accountable for political bias that might render their polls less accurate.

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#1</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**empirical regularity** · FiveThirtyEight pollster ratings · explicit

Rasmussen Reports has had strongly Republican-leaning results relative to the polling consensus for many years. Even so, its overall accuracy in 538's pollster ratings is roughly average, not poor, because polls in general considerably understated Republican performance in 2014, 2016 and 2020.

*Numbers:* elections where polls understated Republicans = 2014, 2016, 2020 election years (Reason Rasmussen's R-leaning house effect did not hurt its accuracy)

*Why:* Silver describes this as 'two wrongs making a right': Rasmussen's bias offset the industry's Democratic bias.

> Despite that strong Republican house effect, however, they've had roughly average accuracy overall because polls have considerably understated Republican performance in several recent elections (2014, 2016, 2020).

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#3</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**limitation or failure mode** · FiveThirtyEight pollster ratings · explicit

An accuracy-only pollster rating can reward a biased pollster whose lean happens to offset a systematic industry-wide polling error in the same cycles. Rasmussen's average rating is partly a case of its Republican bias cancelling the field's Democratic bias.

*Why:* Two wrongs making a right.

> Rasmussen has had a Republican bias, but other polls have had a Democratic bias, so they come out of the wash looking OK? Yeah, probably.

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#4</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**method** · FiveThirtyEight pollster ratings (Silver era) · inferred_from_chart

The FiveThirtyEight pollster ratings page shown in the article grades a pollster using polls conducted within 21 days of an election, based on each poll's median field date. The page offers views of accuracy across all polls and of directional error (overestimating Democrats vs. Republicans).

*Numbers:* window for polls used in pollster grades = 21 days before election (Based on the poll's median date, FiveThirtyEight pollster ratings)

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#5</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**empirical regularity** · FiveThirtyEight pollster ratings · inferred_from_chart

The FiveThirtyEight chart of Rasmussen Reports' polls (directional view) shows the distribution of poll errors skewed toward overestimating Republicans. Most dots sit right of the center line, with a long right tail including a couple of large outliers, while a meaningful minority overestimated Democrats.

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#6</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**interpretation guidance** · general principle · explicit

Silver suggests that pollsters may compensate for low phone response rates by moving online and doing more modeling and massaging of their data, even if this departs from the traditional hands-off 'gold standard' approach.

> pollsters may be able to compensate for this by doing more massaging and modeling with their data, even this means a retreat from the traditional, hands-off, "gold standard" approach to polling.

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#13</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**method** · 538 pollster ratings / bias table · inferred_from_chart

In 538's polling bias calculation, bias is computed only for races whose top two finishers were a Republican and a Democrat, so presidential primaries are excluded. Polls are weighted by one over the square root of the number of polls their pollster conducted for that type of election in that cycle. Special elections and runoffs are included, polls from pollsters banned by 538 are excluded, and the 21-day window is based on median field date.

*Numbers:* window = 21 days (final days before election, by median field date); poll weight = 1/sqrt(n polls by pollster for that election type and cycle) (bias table weighting)

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#30</sub>

### 2024-09-11 · [A guide to post-debate poll-watching](https://www.natesilver.net/p/a-guide-to-post-debate-poll-watching)
**interpretation guidance** · Silver Bulletin pollster ratings 2024 · explicit

In the Silver Bulletin pollster ratings, most quick overnight IVR polls have relatively low ratings and ought to be viewed with skepticism. Morning Consult and YouGov are rated as good pollsters.

> Most of these polls have relatively low ratings and ought to be looked at with some skepticism.

<sub>2024-09-11_a-guide-to-post-debate-poll-watching-by-nate-silver#9</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**method** · Silver Bulletin pollster ratings (2024) · explicit

Silver Bulletin pollster ratings penalize polling firms that show clear signs of herding, meaning hedging published results toward the polling averages.

*Why:* Polling averages like Silver Bulletin's potentially contribute to herding, so the ratings counteract it.

> our pollster ratings actually punish polling firms that show clear signs of doing this

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#8</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**empirical regularity** · Silver Bulletin pollster ratings (2024) · explicit

In the 2024 Silver Bulletin pollster ratings, Selzer & Co. is the highest-rated pollster and NYT/Siena is second. MassINC is described as highly rated.

*Numbers:* Selzer rank = 1 rank (Silver Bulletin pollster ratings, Sep 2024); NYT/Siena rank = 2 rank (Silver Bulletin pollster ratings, Sep 2024)

*Why:* Pollsters that stand behind seeming outliers are usually more accurate over the long run.

> That's why Selzer is our highest-rated pollster — the only one to rank higher than the Times.

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#9</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**interpretation guidance** · general principle · explicit

When a pollster publishes results that defy conventional wisdom, treat it as a sign that the pollster is doing good and honest work.

*Why:* Many pollsters file-drawer outliers or massage data toward socially acceptable numbers.

> when pollsters publish results like these, you should take that as a sign that they're doing good and honest work

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#12</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**empirical regularity** · 2024 presidential · inferred_from_chart

Pollster rating and house effect are distinct. Firms with large partisan house effects can still be rated reasonably well, e.g. Trafalgar (B+) and Rasmussen (B). Most of the highest-rated firms have little net house effect.

> most of our most highly-rated firms have little net house effect

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#20</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**limitation or failure mode** · general principle / 2024 · explicit

In some elections, highly rated polls and mediocre polls diverge systematically; for example, higher-quality polls were usually more favorable to Obama in 2012. In such cases, anchoring house effects to top-rated firms matters. In 2024 this divergence was not present, so an average built only from top firms would look about the same as the Silver Bulletin average.

> Higher-quality polls were usually more favorable to Barack Obama in 2012 than lower-rated ones, for instance. But 2024 isn't one of those elections.

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#21</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**empirical regularity** · 2024 · explicit

John McLaughlin, the pollster behind the infamous Cantor internal, was one of the Trump campaign's chief pollsters in 2024.

> Cantor's pollster? None other than John McLaughlin, who is now one of the Trump campaign's chief pollsters.

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#8</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**interpretation guidance** · general principle · explicit

Even top-rated pollsters such as NYT/Siena ('perhaps the best pollster in the country') can show patterns driven by sampling error. Analysts should be wary of backfilling narratives onto noise when other high-quality pollsters disagree.

> our minds can be incredibly clever in backfilling explanations for statistical noise

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#14</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**interpretation guidance** · 2024 presidential · explicit

Partisan alignment and quality are distinct. Rasmussen Reports is credibly alleged to share results with the Trump campaign, which no nonpartisan pollster should do, while Echelon Insights is Republican-associated but high quality in the Silver Bulletin ratings.

> other alleged zone-flooders, like Echelon Insights, are high-quality polling firms that get good marks in both the Silver Bulletin and 538 pollster ratings.

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#16</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**empirical regularity** · Silver Bulletin pollster ratings 2024 · explicit

The direction of a pollster's LV/RV gap does not track pollster quality. A+ pollsters NYT/Siena and Washington Post show Harris better among LVs, while A-rated Marist and Fox News show the opposite.

> It isn't a quality issue. Some of our highest-rated pollsters like NYT and The Washington Post (both A+) show Harris doing better among LVs.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#13</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**adjustment rule** · Silver Bulletin pollster ratings · explicit

Silver Bulletin pollster ratings include a herding penalty. A pollster whose polls consistently match other recently published polls to a highly statistically improbable degree has its rating downgraded.

*Why:* It partially counters the perverse incentive that published polling averages create, giving pollsters a target to herd toward.

> polls that consistently match numbers from other recently published polls in a way that is highly statistically improbable see their ratings downgraded

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#2</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**method** · general principle / pollster ratings · explicit

Silver's herding test works in three steps. First, for each poll, compute from its sample size the probability that it shows a margin within ±2.5 points if the race is truly tied, using the margin-of-error formula for the difference between candidates. Second, sum these probabilities to get the expected number of close polls. Third, use a binomial distribution, assuming independent polls, to get the probability of at least the observed number of close polls.

*Numbers:* closeness threshold = 2.5 percentage points (non-integer chosen because averaged poll versions produce half-point margins); P(within 2.5) for n=400 = about 40 percent (tied race); P(within 2.5) for n=5686 = almost 95 percent (tied race)

*Why:* Honest polls should produce more apparent outliers than observed.

> Based on a binomial distribution — which assumes that all polls are independent of one another, which theoretically they should be

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#9</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**empirical regularity** · 2024 presidential · explicit

Across 249 October 2024 swing-state polls, 193 (78%) were within 2.5 points, against an expected 137 (55%) in a tied race. The odds against this are 1 in 9.5 trillion.

*Numbers:* actual close polls = 193 (78%) polls (October 2024, 7 swing states); expected close polls = 137 (55%) polls (tied race); odds = 1 in 9.5 trillion (binomial)

> the odds are 1 in 9.5 trillion against at least this many polls showing such a close margin

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#10</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**empirical regularity** · 2024 presidential · inferred_from_chart

The state-level herding table shows, for each state, polls, expected close polls in a tied race, actual close polls, and odds against: AZ 32 / 17 (54%) / 22 (69%) / 1 in 15; GA 31 / 18 (58%) / 21 (68%) / 1 in 5; MI 44 / 24 (54%) / 29 (66%) / 1 in 8; NV 28 / 14 (50%) / 21 (75%) / 1 in 144; NC 31 / 18 (57%) / 25 (81%) / 1 in 209; PA 47 / 27 (58%) / 42 (89%) / 1 in 300K; WI 36 / 19 (52%) / 33 (92%) / 1 in 2.8 million.

*Numbers:* WI odds = 1 in 2.8 million (33 of 36 close); PA odds = 1 in 300K (42 of 47 close); NV odds = 1 in 144 (21 of 28 close); NC odds = 1 in 209 (25 of 31 close)

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#11</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**empirical regularity** · 2024 presidential · inferred_from_chart

The pollster-level herding table covers firms with at least 8 October swing-state polls. It lists polls, expected close polls, actual close polls, and odds against: Redfield & Wilton 44 / 25 (56%) / 42 (95%) / 1 in 175 million; Emerson 12 / 7 (56%) / 12 (100%) / 1 in 1148; InsiderAdvantage 10 / 5 (53%) / 10 (100%) / 1 in 576; Morning Consult 14 / 7 (52%) / 12 (86%) / 1 in 105; OnMessage 8 / 4 (45%) / 6 (75%) / 1 in 12; Trafalgar 11 / 7 (61%) / 9 (82%) / 1 in 8; Quinnipiac 8 / 5 (63%) / 5 (63%) / 1 in 3; AtlasIntel 21 / 13 (63%) / 14 (67%) / 1 in 2; Rasmussen 10 / 6 (55%) / 6 (60%) / 1 in 2; Washington Post 8 / 4 (51%) / 4 (50%) / 1 in 2; YouGov 11 / 8 (70%) / 5 (45%) / 9 in 10.

*Numbers:* Redfield & Wilton odds = 1 in 175 million (42 of 44 close); minimum polls for table = 8 polls (October swing-state polls)

*Why:* Highly rated firms (Washington Post) show less herding. YouGov had fewer close polls than expected, partly because its results lean toward Harris.

> Redfield & Wilton are by far the worst herders: 42 of their 44 polls show the margin within 2.5 points or 95 percent.

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#12</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**limitation or failure mode** · general principle · explicit

Herding occurs through two mechanisms: file-drawering (not publishing results that don't match the consensus) and adjusting turnout or likely-voter models until results match.

> file-drawering (not publishing) results that don’t match the consensus or torturing their turnout models until they do

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#14</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**limitation or failure mode** · general principle · explicit

Publishing polling averages (RCP, 538, Silver Bulletin) creates perverse incentives. The averages give pollsters a target to herd toward and make outliers stand out. The incentive is strongest when averages are near zero, because a pollster can herd and avoid taking a stand at the same time.

> which both give pollsters a target to herd toward and make supposed outliers really stand out

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#15</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**interpretation guidance** · 2024 presidential · explicit

Herding is less likely in low-attention, non-competitive races, such as New Hampshire, Kansas, and NE-02 in 2024. Polls there can therefore be informative signals about the true environment. New Hampshire polls ranged from Harris +21 to a nominal Trump lead within a week.

*Numbers:* NH range = Harris +21 to Trump +0.4 percentage points (recent NH polls, e.g. Dartmouth D+20.8, Praecones R+0.4)

> where herding is less likely because these races aren’t expected to be close and they don’t get much attention

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#16</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**interpretation guidance** · general principle · explicit

High-quality pollsters such as NYT/Siena and Ann Selzer publish results that diverge from the consensus. Selzer has historically been proven right on apparent outliers. Willingness to publish outliers is a sign of honest work.

*Numbers:* Selzer Iowa = Harris -4 percentage points (2024 Iowa poll)

> Ann Selzer, who has consistently published seeming “outlier” polls only later to be proven right

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#19</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**parameter or number** · Silver Bulletin pollster ratings 2024 · explicit

In the Silver Bulletin pollster ratings as of November 2024, Selzer & Co. and NYT/Siena College are the two highest-rated pollsters.

*Why:* Both have long track records of bucking conventional wisdom and being right.

> Selzer and NYT/Siena are our two highest-rated pollsters.

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#0</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**interpretation guidance** · 2024 presidential · explicit

Silver names Selzer, Marist College and NYT/Siena as higher-quality pollsters he trusts not to herd. He contrasts them with 'gutless' pollsters that copy others' results.

*Why:* Herding reduces the information value of polls.

> the higher-quality pollsters that I trust not to herd, namely Selzer, Marist College, and for the most part NYT/Siena

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#16</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**model change** · possible 2028 change · explicit

Silver may add further penalties for pollster herding in future versions. This implies some herding penalty already exists.

> Finally, we might look at additional punishments for pollster herding.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#19</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**interpretation guidance** · 2024 · explicit

Silver calls AtlasIntel the most impressive 2024 indicator, uncannily accurate and also strong in 2020. He warns against treating any single pollster as a gold standard, citing Selzer's 2024 miss, and says there are likely upper bounds on poll accuracy.

> counting on any one polling firm to be the gold standard is risky — look at what happened with Selzer.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#27</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**method** · Silver Bulletin pollster ratings (post-2024 update) · explicit

Silver Bulletin will give its official assessment of 2024 poll accuracy through an update of its pollster ratings.

> For the Official Silver Bulletin Take, you’ll have to wait until we update our pollster ratings.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#5</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**empirical regularity** · Silver Bulletin pollster ratings · explicit

AtlasIntel is one of the highest-rated pollsters in the Silver Bulletin pollster ratings and pretty much nailed the 2024 results.

> AtlasIntel — one of our highest-rated pollsters — pretty much nailed the results this year.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#6</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**model change** · Silver Bulletin pollster ratings June 2024 · explicit

The June 2024 Silver Bulletin pollster ratings restore the methodology Silver used for FiveThirtyEight pollster ratings when he left in 2023, with no methodological changes, only new data.

*Why:* Silver says he continues to own the IP for the original FiveThirtyEight models.

> These ratings restore the methodology that I used for pollster ratings when I left FiveThirtyEight in 2023

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#0</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**method** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential forecast uses the pollster ratings, which were recalculated in preparation for the forecast's launch.

> I've recalculated the pollster ratings that the model employs

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#1</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**method** · Silver Bulletin pollster ratings June 2024 · explicit

Each pollster receives an overall letter grade derived from its predictive plus-minus rating.

> An overall grade based on a pollster's predictive plus-minus rating.

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#6</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**adjustment rule** · Silver Bulletin pollster ratings June 2024 · explicit

Grades for pollsters with sparse data are rounded to a combined grade, e.g. 'A/B' rather than 'A-'. In the table, A/B pollsters have roughly 13-29 polls.

*Numbers:* poll counts of A/B-graded pollsters in table = 13-29 polls (read from page 1 of the table)

*Why:* Sparse data warrants a less precise grade.

> Grades for pollsters with sparse data are rounded (e.g. to "A/B" rather than A-)

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#7</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**adjustment rule** · Silver Bulletin pollster ratings June 2024 · explicit

Banned pollsters automatically receive a grade of F regardless of their plus-minus score. For example, Strategic Vision LLC has a predictive plus-minus of -0.38, which would otherwise be good, but is graded F.

*Numbers:* Strategic Vision LLC predictive +/- = -0.38 (graded F because banned)

> banned pollsters automatically receive a grade of F

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#8</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**adjustment rule** · Silver Bulletin pollster ratings June 2024 · explicit

Banned/unbanned decisions in the June 2024 ratings were reverted to those in place in spring 2023.

*Why:* Silver did not want to re-litigate them.

> I'm also reverting back any banned/unbanned decisions to the ones that were in place in spring 2023.

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#9</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**method** · Silver Bulletin pollster ratings June 2024 · explicit

Predictive plus-minus is the expected future accuracy of a pollster, combining its historical accuracy with its transparency/disclosure standards. Negative scores are better and mean the pollster is expected to be more accurate than average.

> Negative plus-minus scores are good and imply that we expect the pollster to be more accurate than average going forward.

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#10</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**adjustment rule** · Silver Bulletin pollster ratings June 2024 · explicit

Pollsters receive a transparency bonus in predictive plus-minus if they are members of the AAPOR Transparency Initiative or share their data with the Roper Center archive.

*Why:* Transparency predicts future accuracy.

> pollsters get a bonus if they're either a member of the AAPOR Transparency Initiative or share their data with the Roper Center archive

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#11</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**parameter or number** · Silver Bulletin pollster ratings June 2024 · inferred_from_chart

Top of the June 2024 ratings table (grade, predictive +/-, mean-reverted bias, number of polls): Selzer A+ -1.27 D+0.1 54; NYT/Siena A+ -1.18 D+1.0 95; ABC/WaPo A+ -0.94 D+0.8 90; Research & Polling A+ -0.92 R+0.5 44; SurveyUSA A -0.86 +0.0 857; Siena College A -0.84 R+0.2 63; Marquette A/B -0.81 D+0.2 15; AtlasIntel A -0.75 D+0.2 24; Marist A -0.70 D+0.3 200; Monmouth A -0.62 D+2.0 123; Emerson A- -0.56 D+0.3 264; PPP A- -0.39 D+0.9 463; Mason-Dixon A- -0.38 R+0.5 446; Quinnipiac A- -0.38 D+0.5 222.

*Numbers:* Selzer predictive +/- = -1.27 (A+, D+0.1 bias, 54 polls); NYT/Siena predictive +/- = -1.18 (A+, D+1.0 bias, 95 polls); ABC/WaPo predictive +/- = -0.94 (A+, D+0.8 bias, 90 polls); Research & Polling predictive +/- = -0.92 (A+, R+0.5 bias, 44 polls); SurveyUSA predictive +/- = -0.86 (A, +0.0 bias, 857 polls); Siena College predictive +/- = -0.84 (A, R+0.2 bias, 63 polls); Marquette predictive +/- = -0.81 (A/B, D+0.2 bias, 15 polls); AtlasIntel predictive +/- = -0.75 (A, D+0.2 bias, 24 polls); Marist predictive +/- = -0.70 (A, D+0.3 bias, 200 polls); Monmouth predictive +/- = -0.62 (A, D+2.0 bias, 123 polls); Emerson predictive +/- = -0.56 (A-, D+0.3 bias, 264 polls); PPP predictive +/- = -0.39 (A-, D+0.9 bias, 463 polls); Mason-Dixon predictive +/- = -0.38 (A-, R+0.5 bias, 446 polls); Quinnipiac predictive +/- = -0.38 (A-, D+0.5 bias, 222 polls)

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#17</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**parameter or number** · Silver Bulletin pollster ratings June 2024 · inferred_from_chart

Grade thresholds can be approximated from page 1 of the table. A+ appears for plus-minus up to about -0.92, A for roughly -0.86 to -0.62, and A- from about -0.58 to -0.38. The cutoffs are not stated in the text.

*Numbers:* approximate A+ range = <= -0.92 (predictive +/-); approximate A range = -0.86 to -0.62 (predictive +/-); approximate A- range = -0.58 to -0.38 (predictive +/-)

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#18</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**parameter or number** · Silver Bulletin pollster ratings June 2024 · inferred_from_chart

The ratings table has 21 pages of roughly 25 rows each, implying roughly 500 rated pollsters.

*Numbers:* table pages = 21 pages (Datawrapper table)

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#19</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**method** · Silver Bulletin pollster ratings · explicit

Advanced Plus-Minus measures how a pollster's average error compares to other pollsters' error in the same election, with further statistical adjustments for race difficulty and sample size. Negative scores are better.

> how the pollster's average error compares to other pollsters' in the same election, with various other statistical adjustments that account for which races are harder and easier to poll

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#30</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**method** · Silver Bulletin pollster ratings · explicit

The pollster ratings use each pollster's data back to 1998 and weight recent years more heavily.

> our pollster ratings weight recent years more heavily

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#31</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**interpretation guidance** · Silver Bulletin pollster ratings · explicit

A pollster's single-cycle performance should not be overweighted. The multi-cycle ratings are better for judging quality, although 2024 shifted the ratings more than most cycles do.

> You shouldn't put too much stock in a pollster's performance in a single cycle

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#32</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**model change** · Silver Bulletin pollster ratings (2025 update) · explicit

After 2024, AtlasIntel was upgraded from A to A+ and became the highest-rated pollster in the database, and OnMessage moved from B/C to A. Selzer kept a B+ despite 12.8 points of average error and D+14.8 bias in 2023-24.

*Numbers:* Selzer error = 12.8 points (2023-24); Selzer bias = D+14.8 points (2023-24)

> AtlasIntel's rating has gone from an A to an A+ — and it is now the highest-rated pollster in our database — while OnMessage moved from a B/C to an A

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#33</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**parameter or number** · Silver Bulletin pollster ratings · inferred_from_chart

2023-24 pollster results, for pollsters with at least 5 polls in the final 21 days (given as error / bias / APM / number of polls): OnMessage 1.2 / D+0.1 / -2.2 / 20; Patriot Polling 1.5 / D+1.5 / -1.2 / 15; AtlasIntel 1.5 / D+0.1 / -1.2 / 67; Mitchell 2.0 / D+1.2 / -1.5 / 6; Echelon 2.0 / D+0.3 / -0.9 / 8; TIPP 2.0 / D+2.0 / -1.3 / 22; Washington Post 2.0 / D+1.8 / -1.4 / 8; Beacon/Shaw 2.1 / D+2.1 / -0.9 / 6; InsiderAdvantage 2.2 / D+1.1 / -1.5 / 25; Trafalgar 2.5 / D+1.0 / -1.3 / 29; Rasmussen 2.7 / D+0.4 / -0.9 / 25; Redfield & Wilton 2.8 / D+2.4 / -0.5 / 36; Quinnipiac 2.8 / D+2.8 / -0.0 / 6; Susquehanna 2.9 / D+1.1 / -0.9 / 6; PPP 2.9 / R+2.1 / -3.7 / 6; Saint Anselm 2.9 / D+2.4 / -2.4 / 5; Monmouth 3.1 / D+1.8 / -1.3 / 8; Emerson 3.3 / D+1.9 / -1.5 / 61; J.L. Partners 3.5 / R+0.7 / -1.3 / 8; Marist 3.5 / D+3.4 / 0.7 / 13; SSRS 3.6 / D+3.6 / 0.5 / 15; OH Predictive 3.7 / D+3.7 / -1.3 / 10; NYT/Siena 3.9 / D+3.9 / 0.4 / 21; Focaldata 3.9 / D+3.9 / 0.5 / 9; Data for Progress 4.0 / D+3.2 / 0.7 / 8.

*Numbers:* minimum polls for table = 5 polls (2023-24 cycle)

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#34</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**design principle** · general principle · explicit

Historical track records matter, but relying on them can be overdone. No single poll should be treated as an oracular gold standard, because previously accurate firms can have bad cycles and newer firms can outperform.

> it's a bad idea to treat one poll as an oracular gold standard

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#36</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**method** · Silver Bulletin pollster ratings · explicit

The Advanced Plus-Minus statistic accounts for poll sample size.

> These polls also had small sample sizes, but our Advanced Plus-Minus stat accounts for that.

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#38</sub>

### 2025-05-06 · [We're tracking more data on Trump's popularity](https://www.natesilver.net/p/were-tracking-more-data-on-trumps)
**method** · Silver Bulletin pollster ratings · inferred_from_chart

Silver Bulletin pollster ratings use 'mean-reverted bias': a pollster's historical average statistical bias toward Democratic or Republican candidates, shrunk toward zero according to how many of its polls are in the database. Positive values mean pro-Democratic bias.

*Why:* Shrinkage guards against noisy bias estimates for pollsters with few polls.

<sub>2025-05-06_were-tracking-more-data-on-trumps-popularity#8</sub>

### 2025-05-06 · [We're tracking more data on Trump's popularity](https://www.natesilver.net/p/were-tracking-more-data-on-trumps)
**interpretation guidance** · Silver Bulletin pollster ratings · explicit

Silver Bulletin defines statistical bias as the extent to which polls miss in the same direction and consistently underestimate Democrats or Republicans. This is distinct from overall accuracy.

> By bias, we mean statistical bias: the extent to which polls miss in the same direction and consistently underestimate Democrats or Republicans.

<sub>2025-05-06_were-tracking-more-data-on-trumps-popularity#9</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**method** · Silver Bulletin pollster ratings (2026 update) · explicit

Silver Bulletin pollster ratings are updated after each election year, including off-year elections such as 2025, using results from qualifying races. The ratings feed into the Silver Bulletin polling averages and the 2026 midterm forecasts.

*Why:* The ratings are an important input to the polling averages and forecasts and are also a public resource.

> they're also an important part of the polling averages and forecasts we'll be using to cover the midterms

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#0</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**method** · Silver Bulletin pollster ratings · explicit

Advanced Plus-Minus measures how a pollster's average error compares to other pollsters' errors in the same election, accounting for which races are harder to poll. Negative scores are better.

*Why:* It controls for race difficulty when comparing pollsters.

> how the pollster's average error compares to other pollsters' in the same election, accounting for which races are harder to poll. Negative plus-minus scores indicate that a pollster did better

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#8</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**design principle** · Silver Bulletin pollster ratings · explicit

A pollster's performance in a single cycle should not be given much weight, especially in an off-year cycle where most firms released only one or two qualifying polls.

*Numbers:* typical polls per firm = one or two polls (2025 off-year cycle)

*Why:* Small samples make single-cycle results noisy.

> You shouldn't pay too much attention to how any pollster does in a single cycle, especially an off-year cycle where most firms released one or two qualifying polls.

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#9</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**method** · Silver Bulletin pollster ratings · explicit

For report cards, off-year election polls are normally grouped with the following midterm or presidential year; for example, 2025 polls would be grouped with the 2026 midterms.

*Why:* Off-year elections are low-key and have few polls.

> which is why we typically group them together with midterm or presidential election years for these report cards

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#10</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**parameter or number** · Silver Bulletin pollster ratings (2026 update) · explicit

2025 rating changes: Trafalgar, which overestimated Republicans by 12.6 points on average in Virginia and New Jersey, fell from B+ to B. AtlasIntel, off by 9.9 points on average, was bumped down to A. Beacon Research/Shaw & Co., which missed New Jersey by 7.4 points, was bumped down to A-.

*Numbers:* Trafalgar bias = 12.6 percentage points toward R (VA and NJ 2025); AtlasIntel error = 9.9 percentage points (2025); Beacon/Shaw NJ error = 7.4 percentage points (NJ 2025)

*Why:* Poor 2025 accuracy moved the ratings even with small samples.

> bringing their pollster rating from a B+ down to a B

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#23</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**parameter or number** · Silver Bulletin pollster ratings (2026 update) · inferred_from_chart

Best 2025 pollsters by simple average error, with Advanced Plus-Minus in parentheses: State Navigate 2.4 (−4.4, 2 VA polls), YouGov 2.4 (−4.6, 2 polls NJ/VA), Zogby 2.4 (−4.9, 1 NJ), GQR 2.4 (−6.5, 1 NJ), Echelon 3.4 (−2.7, VA), Washington Post/George Mason 3.4 (−2.9, VA). Further down: InsiderAdvantage 5.2 (+0.3), Gravis/Kaplan 5.4 (−1.8), Roanoke 5.4 (−0.2), Clarity 5.4 (−1.0), Concord 5.4 (−4.1, NJ), SoCal Research 6.4 (−0.4), Quinnipiac 6.4 (−1.4, NJ), Research Co. 7.0 (bias R+5.4, −0.3), Beacon/Shaw 7.4 (−0.7). All showed Republican bias. The same miss scores a better Plus-Minus in New Jersey, the harder-to-poll race, than in Virginia.

*Numbers:* State Navigate APM = -4.4 (2025); GQR APM = -6.5 (2025 NJ); InsiderAdvantage APM = 0.3 (2025 VA); Concord APM = -4.1 (2025 NJ, 5.4 error); Gravis APM = -1.8 (2025 VA, 5.4 error)

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#24</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**model change** · Silver Bulletin pollster ratings, February 2025 · explicit

The Silver Bulletin pollster ratings use the same methodology as the Nate Silver-era FiveThirtyEight pollster ratings. The February 2025 update made no methodological changes and only added data: about 460 new polls from the 2024 presidential, congressional and gubernatorial elections, plus a handful of missing older polls.

*Numbers:* polls added = about 460 polls (February 2025 update after the 2024 elections)

> These ratings apply the same methodology as the previous, Nate-era FiveThirtyEight pollster ratings.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#0</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**method** · Silver Bulletin pollster ratings · explicit

A pollster's letter grade is based on its Predictive Plus-Minus. Pollsters with sparse data get rounded grades (e.g. 'A/B' instead of 'A-'), and banned pollsters automatically receive an F.

*Why:* Sparse data does not support fine distinctions.

> Grades for pollsters with sparse data are rounded (e.g., to “A/B” rather than A-) and banned pollsters automatically receive a grade of F.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#1</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**method** · Silver Bulletin pollster ratings · explicit

Predictive Plus-Minus is the projected future accuracy of a pollster relative to the average pollster. It combines historical accuracy with transparency: a pollster gets a bonus if it belongs to the AAPOR Transparency Initiative or shares its data with the Roper Center archive. Negative scores are good, meaning less error than average is expected.

*Why:* Transparency predicts future accuracy beyond the track record.

> pollsters get a bonus if they’re either a member of the AAPOR Transparency Initiative or share their data with the Roper Center archive.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#2</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**method** · Silver Bulletin pollster ratings · explicit

Mean-reverted bias is a pollster's historical average statistical bias toward Democratic or Republican candidates, shrunk toward zero according to the number of polls in the database. It is calculated only for races in which exactly one Republican and one Democrat are the two leading candidates, so it excludes presidential primaries.

*Why:* Bias is only meaningful in a clean D-vs-R race; small samples are shrunk.

> reverted to a mean of zero based on the number of polls in the database. This is calculated only for races in which exactly one Republican and one Democrat are the two leading candidates

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#3</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**data source** · Silver Bulletin pollster ratings, February 2025 · explicit

The pollster ratings database goes back to 1998, weights polls from more recent years more heavily, and covers all polls taken in the 21 days before presidential, congressional and gubernatorial general elections and presidential primaries. The raw file contains toplines for more than 12,300 polls.

*Numbers:* database start = 1998 year (pollster ratings database); window before election = 21 days (polls included in ratings); polls in raw data = more than 12,300 polls (Rawpolls 021325 file)

> The database goes back to 1998, though polls from more recent years are weighted more heavily.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#4</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**method** · Silver Bulletin pollster ratings · explicit

Simple Average Error is a firm's average absolute error on the margin between the top two finishers, polled result versus actual result.

> calculated as the difference between the polled result and the actual result for the margin separating the top two finishers in the race.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#5</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**method** · Silver Bulletin pollster ratings · explicit

Simple Plus-Minus is Simple Average Error minus the expected error for the race surveyed. The expected error accounts for the type of election, the number of days until the election, and the poll's sample size.

*Why:* Some races are intrinsically harder to poll.

> which accounts for the type of election polled, the number of days until the election, and the poll's sample size.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#6</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**method** · Silver Bulletin pollster ratings · explicit

Advanced Plus-Minus additionally accounts for how other polling firms performed in the same races and weights recent results more heavily.

*Why:* Controls for race-level difficulty using other firms as a benchmark.

> also accounts for the performance of other polling firms surveying the same races, and which weights recent results more heavily.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#7</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**method** · Silver Bulletin pollster ratings · explicit

Mean-Reverted Advanced Plus-Minus shrinks Advanced Plus-Minus toward zero, with the amount of shrinkage based on how many polls the firm has conducted, discounting polls from previous years.

*Why:* Firms with few polls have noisy scores.

> The amount of mean reversion is based on how many polls the firm has conducted, but with polls in previous years discounted.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#8</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**method** · Silver Bulletin pollster ratings · explicit

Average Distance from Polling Average (ADPA) measures how far a firm's average poll differed from the average of other polls in the field when it was released. A herding penalty is triggered when a firm's ADPA is lower than the theoretical minimum implied by its sampling error. The penalty equals one-half of the gap between the actual ADPA and the theoretical minimum ADPA, and it is added to Advanced Plus-Minus before Predictive Plus-Minus is calculated.

*Numbers:* herding penalty = 0.5 x (theoretical minimum ADPA - actual ADPA) points (from the table note in the PDF)

*Why:* Polls that are closer to the consensus than sampling error allows are probably herding.

> A herding penalty is triggered when a firm's ADPA is lower than the theoretical minimum based on the sampling error in its polls.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#9</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**interpretation guidance** · Silver Bulletin pollster ratings · explicit

The supplementary accuracy tables only list firms with at least 20 polls, because most of those measures are not mean-reverted and have large sampling errors. Ratings for firms that poll irregularly should be interpreted with extreme caution.

*Numbers:* minimum polls for table listing = 20 polls (accuracy and herding tables)

*Why:* Unshrunk measures are noisy for small samples.

> we’re only listing survey firms with at least 20 polls in our database, since most of these measures aren’t mean-reverted and are subject to large sampling errors.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#11</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**interpretation guidance** · Silver Bulletin pollster ratings · explicit

The percentage of races in which a pollster called the winner correctly is computed but is described as generally a poor measure of pollster accuracy compared with polling error.

*Why:* Calls depend on how close races were, not only on poll quality.

> It’s important to note that this is generally a poor measure of pollster accuracy compared to polling error.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#12</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**data source** · Silver Bulletin pollster ratings · explicit

Washington Post polls are treated as the successor to the discontinued ABC News/Washington Post partnership, and their ratings include prior ABC/Post data.

> We consider Washington Post polls to be the successor to this partnership and their ratings include prior ABC/Post data.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#14</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**parameter or number** · Silver Bulletin pollster ratings, February 2025 · inferred_from_chart

In the February 2025 ratings table, the top Predictive Plus-Minus scores were AtlasIntel (A+, -0.96, bias D+0.16, 91 polls), Marquette University Law School (A/B, -0.92), The Washington Post (A+, -0.90, D+0.90, 98 polls), Research & Polling Inc. (A, -0.87), New York Times/Siena College (A, -0.76, D+1.41, 116 polls), Cygnal (A, -0.75) and SurveyUSA (A, -0.73, 871 polls).

*Numbers:* AtlasIntel Predictive Plus-Minus = -0.96 points (Feb 2025); NYT/Siena Predictive Plus-Minus = -0.76 points (Feb 2025); SurveyUSA polls in database = 871 polls (Feb 2025)

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#15</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**parameter or number** · Silver Bulletin pollster ratings, February 2025 · inferred_from_chart

The ratings tables show that firms with very low ADPA receive the largest herding penalties: for example TIPP Insights (ADPA 2.7, penalty +0.5), Cygnal (ADPA 3.5, +0.5) and OnMessage (ADPA 3.3, +0.5), versus +0.1 for firms like AtlasIntel (ADPA 3.7) and SurveyUSA (ADPA 4.9). Simple average errors for top firms range from about 2.1 (TIPP) to 5.7 (Monmouth) points.

*Numbers:* largest herding penalty shown = +0.5 points (TIPP, Cygnal, OnMessage); TIPP simple average error = 2.1 points (Feb 2025)

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#16</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**model change** · Silver Bulletin pollster ratings Jan 2026 · explicit

The January 2026 update has no methodological changes from the February 2025 update. It only adds about 40 polls from 2025: the Virginia and New Jersey gubernatorial elections and the U.S. House special elections.

*Numbers:* polls added = about 40 polls (added for the 2025 off-year since the Feb 2025 update)

*Why:* 2025 was an off-year, so the ratings are not expected to shift much.

> Since there haven’t been any methodological changes since our last update

<sub>2026-01-14_pollster-ratings-silver-bulletin#1</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**method** · Silver Bulletin pollster ratings · explicit

The pollster ratings database goes back to 1998, and polls from more recent years are weighted more heavily.

*Numbers:* database start year = 1998 year (earliest polls in the database)

> The database goes back to 1998, though polls from more recent years are weighted more heavily.

<sub>2026-01-14_pollster-ratings-silver-bulletin#4</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**method** · Silver Bulletin pollster ratings · explicit

Each pollster's letter grade is based on its Predictive Plus-Minus rating.

> An overall grade based on a pollster’s Predictive Plus-minus rating.

<sub>2026-01-14_pollster-ratings-silver-bulletin#5</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**adjustment rule** · Silver Bulletin pollster ratings · explicit

Pollsters with sparse data get rounded letter grades, such as 'A/B' instead of 'A-'.

> Grades for pollsters with sparse data are rounded (e.g., to “A/B” rather than A-)

<sub>2026-01-14_pollster-ratings-silver-bulletin#6</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**adjustment rule** · Silver Bulletin pollster ratings · explicit

Banned pollsters automatically receive a grade of F.

> banned pollsters automatically receive a grade of F.

<sub>2026-01-14_pollster-ratings-silver-bulletin#7</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**method** · Silver Bulletin pollster ratings · explicit

Predictive Plus-Minus is the model's projection of how much error a pollster will have in future elections relative to the average pollster. It combines the pollster's historical accuracy with its transparency and disclosure standards. Negative scores are better.

> how accurate the model expects the pollster to be going forward based on a combination of its historical accuracy and its transparency/disclosure standards

<sub>2026-01-14_pollster-ratings-silver-bulletin#10</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**adjustment rule** · Silver Bulletin pollster ratings · explicit

Pollsters receive a transparency bonus in Predictive Plus-Minus if they are members of the AAPOR Transparency Initiative or share their data with the Roper Center archive. Either one qualifies.

> pollsters get a bonus if they’re either a member of the AAPOR Transparency Initiative or share their data with the Roper Center archive.

<sub>2026-01-14_pollster-ratings-silver-bulletin#11</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**method** · Silver Bulletin pollster ratings · explicit

Mean-reverted bias is a pollster's historical average statistical bias toward Democrats or Republicans, reverted toward zero by an amount that depends on its number of polls. For example, 'D+1.5' means the pollster has historically overrated Democrats by 1.5 points.

*Numbers:* example bias = D+1.5 percentage points (illustrative example of a pollster that overrated Democrats)

> a pollster's historical average statistical bias toward Democratic or Republican candidates, reverted to a mean of zero based on the number of polls in the database.

<sub>2026-01-14_pollster-ratings-silver-bulletin#12</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**adjustment rule** · Silver Bulletin pollster ratings · explicit

Bias is calculated only for races where exactly one Republican and one Democrat are the top two candidates, so it excludes presidential primaries.

> This is calculated only for races in which exactly one Republican and one Democrat are the two leading candidates

<sub>2026-01-14_pollster-ratings-silver-bulletin#13</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**method** · Silver Bulletin pollster ratings · explicit

Simple Average Error is a firm's average absolute difference between the polled margin and the actual margin separating the top two finishers.

> calculated as the difference between the polled result and the actual result for the margin separating the top two finishers in the race.

<sub>2026-01-14_pollster-ratings-silver-bulletin#14</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**method** · Silver Bulletin pollster ratings · explicit

Simple Plus-Minus is Simple Average Error minus the expected error for the race. Expected error accounts for the type of election, the number of days until the election, and the poll's sample size.

> which accounts for the type of election polled, the number of days until the election, and the poll's sample size.

<sub>2026-01-14_pollster-ratings-silver-bulletin#15</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**method** · Silver Bulletin pollster ratings · explicit

Advanced Plus-Minus also accounts for how other firms performed in the same races, and it weights recent results more heavily.

> also accounts for the performance of other polling firms surveying the same races, and which weights recent results more heavily.

<sub>2026-01-14_pollster-ratings-silver-bulletin#16</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**method** · Silver Bulletin pollster ratings · explicit

Mean-Reverted Advanced Plus-Minus reverts Advanced Plus-Minus toward zero. The amount of reversion depends on the firm's number of polls, with polls from earlier years discounted.

> The amount of mean reversion is based on how many polls the firm has conducted, but with polls in previous years discounted.

<sub>2026-01-14_pollster-ratings-silver-bulletin#17</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**interpretation guidance** · Silver Bulletin pollster ratings · explicit

The detailed tables list only firms with at least 20 polls, because most of the measures are not mean-reverted and carry large sampling errors. Ratings for irregular pollsters should be read with extreme caution.

*Numbers:* minimum polls for listing = 20 polls (threshold for the detailed tables)

*Why:* Non-mean-reverted measures carry large sampling error for small samples.

> since most of these measures aren’t mean-reverted and are subject to large sampling errors.

<sub>2026-01-14_pollster-ratings-silver-bulletin#18</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**method** · Silver Bulletin pollster ratings · explicit

Average Distance from Polling Average (ADPA) measures how far a firm's average poll differed from the average of other polls in the field when it was released. A low ADPA is potential evidence of herding.

*Why:* Herding pollsters stay suspiciously close to the consensus.

> A low ADPA is potential evidence of herding.

<sub>2026-01-14_pollster-ratings-silver-bulletin#20</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**adjustment rule** · Silver Bulletin pollster ratings · explicit

A herding penalty applies when a firm's ADPA falls below the theoretical minimum implied by the sampling error in its polls. The penalty equals one-half of the difference between the theoretical minimum ADPA and the actual ADPA. It is added to Advanced Plus-Minus before Predictive Plus-Minus is calculated.

*Numbers:* herding penalty multiplier = 0.5 (fraction of the ADPA shortfall below the theoretical minimum)

> This penalty is added to a firm's Advanced Plus-Minus score before calculating Predictive Plus-Minus.

<sub>2026-01-14_pollster-ratings-silver-bulletin#21</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**interpretation guidance** · general principle · explicit

The percentage of correct calls (calling the race winner) is generally a poor measure of pollster accuracy compared with polling error.

> this is generally a poor measure of pollster accuracy compared to polling error.

<sub>2026-01-14_pollster-ratings-silver-bulletin#22</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**adjustment rule** · Silver Bulletin pollster ratings · explicit

Washington Post polls are treated as the successor to the ABC News/Washington Post partnership, so their ratings include prior ABC/Post data.

*Why:* ABC News discontinued its polling partnership with the Post.

> We consider Washington Post polls to be the successor to this partnership and their ratings include prior ABC/Post data.

<sub>2026-01-14_pollster-ratings-silver-bulletin#23</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**parameter or number** · Silver Bulletin pollster ratings Jan 2026 · inferred_from_chart

Top Predictive Plus-Minus ratings as of Jan 12, 2026, with grade, bias and number of polls:
- Washington Post: A+, -1.09, D+0.90, 98 polls
- Marquette Law School: A/B, -1.00, D+0.32, 17 polls
- Research & Polling Inc.: A+, -0.98, R+0.55, 44 polls
- OnMessage: A, -0.85, R+1.23
- Data Orbital: A/B, -0.83
- TIPP: A, -0.81
- Cygnal: A, -0.80, D+2.04
- NYT/Siena: A, -0.80, D+1.41, 116 polls
- Monmouth: A, -0.77, D+2.00, 131 polls
- SurveyUSA: A, -0.66, 871 polls
- AtlasIntel: A, -0.64, R+0.04
- Emerson: A, -0.61, 320 polls

*Numbers:* Washington Post Predictive Plus-Minus = -1.09 points (Jan 2026); NYT/Siena Predictive Plus-Minus = -0.80 points (Jan 2026); SurveyUSA polls = 871 polls (Jan 2026)

<sub>2026-01-14_pollster-ratings-silver-bulletin#24</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**empirical regularity** · Silver Bulletin pollster ratings Jan 2026 · inferred_from_chart

The tables show that grades do not map to Predictive Plus-Minus by fixed cutoffs alone. Research & Polling (-0.98) gets an A+ while Marquette (-1.00) gets A/B because of sparse data. Grades around -0.6 are A, and around -0.55 to -0.53 they are A-.

<sub>2026-01-14_pollster-ratings-silver-bulletin#25</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**empirical regularity** · Silver Bulletin pollster ratings Jan 2026 · inferred_from_chart

Mean reversion shrinks extreme Advanced Plus-Minus scores substantially for firms with fewer polls. Grove Insight goes from -2.51 to -0.97, and Muhlenberg from -1.85 to -0.99. SurveyUSA, with 871 polls, barely moves, from -0.83 to -0.79. Simple average errors for top firms range from 2.1 (TIPP) to 5.7 (Monmouth).

*Numbers:* Grove Insight Advanced Plus-Minus = -2.51 points (before mean reversion); Grove Insight Mean-Reverted Advanced Plus-Minus = -0.97 points (after mean reversion); SurveyUSA Advanced Plus-Minus / Mean-Reverted = -0.83 / -0.79 points (before / after mean reversion)

<sub>2026-01-14_pollster-ratings-silver-bulletin#26</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**parameter or number** · Silver Bulletin pollster ratings Jan 2026 · inferred_from_chart

Herding penalties among top firms are typically +0.1 to +0.6 points. Muhlenberg College has the largest shown, about +1.2 (ADPA 3.4). ADPA values range from about 2.7 (TIPP) to 5.2 (MassINC, Susquehanna).

*Numbers:* Muhlenberg herding penalty = +1.2 points (Jan 2026); TIPP ADPA = 2.7 points (Jan 2026)

<sub>2026-01-14_pollster-ratings-silver-bulletin#28</sub>

### 2026-10-22 · [Fake polls are a real problem](https://www.natesilver.net/p/fake-polls-are-a-real-problem)
**method** · FLIPR 2026 · explicit

New or unknown pollsters start with fairly low pollster ratings by default, and FLIPR has precautions against being overly influenced by any one poll; removing the fabricated Wedgewood polls left FLIPR's averages and forecasts basically unchanged.

> new/unknown pollsters start with fairly low ratings by default.

<sub>2026-10-22_fake-polls-are-a-real-problem-by-nate-silver#3</sub>
