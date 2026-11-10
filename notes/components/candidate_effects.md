# Candidate effects

69 findings from 24 articles, oldest first.

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**parameter or number** · FiveThirtyEight 2022 midterm · explicit

In 2022 the model began multiplying funds raised from within a candidate's state by 5 when assessing fundraising edge, because a dollar from in-state was found to be about five times as predictive as an out-of-state dollar.

*Numbers:* in-state contribution multiplier = 5 x (2022 onward)

*Why:* Empirically about five times as valuable in predicting outcomes.

> We found that a dollar received from within a candidate’s state is about five times as valuable as a dollar received outside of it

<sub>fte_midterm-house-senate-governor-methodology#1</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

The partisan lean index includes a home-state adjustment for presidential and vice-presidential candidates. It is much larger for presidential candidates, larger in smaller states, and split when a candidate has two home states, e.g. Biden primary Delaware and secondary Pennsylvania, Trump primary New York and secondary Florida.

> The size of the home-state adjustment is much larger for presidential candidates than for their running mates.

<sub>fte_2020-presidential-forecast-methodology#9</sub>

### 2024-07-05 · [The broken leg problem](https://www.natesilver.net/p/the-broken-leg-problem)
**assumption** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model implicitly assumes each candidate will run a league-average campaign for their party between now and election day. It has no adjustment for a candidate who is incapable of campaigning normally. Silver offers 2004 John Kerry as an example of a league-average Democrat.

*Why:* The model is trained on historical candidates, so it reflects average campaign performance.

> Roughly speaking, the model assumes that Joe Biden will be a league-average Democratic candidate between now and November.

<sub>2024-07-05_the-broken-leg-problem-by-nate-silver-silver-bulletin#4</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**limitation or failure mode** · general principle · explicit

Fundamentals models cannot account for potentially material candidate-specific factors such as Biden's age, because the sample is too small. Silver's hypothetical: with 1,000 elections you might find candidates over 80 underperform fundamentals by 3 points. Congressional data might help. Without such an estimate, this is a reason to trust polls more than fundamentals.

*Numbers:* hypothetical age penalty = 3 percentage points (illustrative only, candidates over 80); hypothetical sample = 1,000 elections (illustrative)

> if you can’t, it’s at least a reason to trust the polls more than the fundamentals

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#23</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**method** · 2024 presidential · explicit

The Silver Bulletin presidential model estimates home-state ('favorite son/daughter') effects for both the presidential nominee and the VP pick. It does so from before-and-after data: how the ticket performed in the home state relative to four years earlier and four years later, adjusting for overall national trends.

*Numbers:* comparison window = 4 years (before and after the candidate's election cycle)

*Why:* National swings (e.g., Obama's narrower 2012 margin vs 2008) must be netted out so that home-state gains are not overstated.

> how did the presidential ticket perform relative to four years earlier and four years later, adjusting for overall national trends?

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#0</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**parameter or number** · 2024 presidential · explicit

In the Silver Bulletin model, the home-state effect for a VP pick is about one-quarter the size of the home-state effect for the presidential nominee.

*Numbers:* VP home-state effect relative to presidential nominee = about one-quarter ratio (model estimate)

> Home-state effects are only about one-quarter as large for the VP pick than for the presidential nominee.

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#1</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**empirical regularity** · 2024 presidential · explicit

In the Silver Bulletin model, home-state effects are roughly inversely proportional to the number of electoral votes in the state, so they are larger in small states (e.g., Palin in Alaska, Biden in Delaware).

*Why:* In a smaller state a politician is more likely to feel like they are from voters' proverbial backyard.

> Home-state effects are roughly inversely proportional to the number of electoral votes in a state.

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#2</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**parameter or number** · 2024 presidential · explicit

The Silver Bulletin model estimates that a VP from Pennsylvania (19 electoral votes) would improve the ticket's Pennsylvania margin by slightly more than 0.4 percentage points.

*Numbers:* PA VP home-state effect = slightly more than 0.4 percentage points of margin (2024; the article does not say whether this figure includes the partisanship adjustment announced for the Harris version); PA electoral votes = 19 electoral votes (2024)

> having a VP from Pennsylvania would improve a ticket's margin in the Keystone State by slightly more than 0.4 percentage points

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#3</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**parameter or number** · 2024 presidential · explicit

The Silver Bulletin model estimates that a VP from Arizona would improve the ticket's Arizona margin by a hair over 0.7 percentage points. The effect is larger than Pennsylvania's because Arizona has fewer electoral votes.

*Numbers:* AZ VP home-state effect = a hair over 0.7 percentage points of margin (2024)

*Why:* Follows from the inverse-proportionality to electoral votes.

> In Arizona, the effect would be slightly larger according to the model's logic — a hair over 0.7 percentage points — since it has fewer electoral votes.

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#4</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**limitation or failure mode** · 2024 presidential · explicit

Silver says the home-state effect estimates rest on relatively small sample sizes and carry a lot of intrinsic uncertainty.

> these estimates are based on relatively small sample sizes and include a lot of intrinsic uncertainty

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#5</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**assumption** · 2024 presidential (Biden version) · explicit

When a presidential matchup is a rematch, as Biden-Trump was of 2020, the candidates' home-state effects are already priced into the partisan lean of their home states. No separate adjustment is needed in that case.

*Why:* Partisan lean is computed from prior results that already included the same candidates.

> so whatever effects Trump and Biden had were already priced into the partisan lean of their respective home states

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#8</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**empirical regularity** · 2024 presidential · explicit

Biden improved Democratic margins in Delaware in 2020 relative to Clinton-Kaine in 2016, but by less than the unadjusted model expected. This is evidence that home-state effects have diminished with partisanship.

> it was by less than the (rather large amount since Delaware is a small state) improvement the model expected

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#9</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**empirical regularity** · Silver congressional model · explicit

Silver's congressional model found that incumbency effects are more powerful in smaller states (e.g., Joe Manchin in West Virginia, Susan Collins in Maine).

> My Congressional model has also found that incumbency effects are more powerful in smaller states

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#17</sub>

### 2024-07-27 · [Could Josh Shapiro win Kamala Harris the Electoral College?](https://www.natesilver.net/p/could-josh-shapiro-win-kamala-harris)
**limitation or failure mode** · 2024 presidential · implied

The model's home-state effect may understate a candidate like Shapiro: unlike a House member such as Paul Ryan, he is a popular sitting governor. The article does not say the model distinguishes officeholder type or popularity.

> maybe you could argue that this is on the low side. Unlike, say, Ryan, who only represented a single congressional district

<sub>2024-07-27_could-josh-shapiro-win-kamala-harris-the-electoral-college#19</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**limitation or failure mode** · 2024 presidential · explicit

The Silver Bulletin presidential model does not account for endorsements, such as RFK's endorsement of Trump, in any way. Silver says the model may be 'running a little hot' on Harris as a result.

*Why:* The endorsement's net effect is uncertain. The direct effect is likely pro-Trump, but the indirect effects are unknown because RFK's favorability is net-negative.

> the model doesn't account for the endorsement in any way

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#22</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**empirical regularity** · general principle · explicit

Silver says home-state effects for presidential candidates are pretty small. He notes Pennsylvania was Biden's birth state, whereas Harris is a California native, which may subtly matter.

> home-state effects are pretty small, but Pennsylvania was Biden's birth state, whereas Harris is a California native.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#18</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**assumption** · general principle · explicit

Silver generally does not believe in 'reverse coattails': the top of the ticket affects down-ballot races, but down-ballot candidates (e.g., NC gubernatorial candidate Mark Robinson) usually do not affect the presidential race.

> I generally don't believe in "reverse coattails" — the top-of-the-ticket can effect down-ballot races, but usually not the other way around.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#19</sub>

### 2024-10-22 · [Likability isn't enough](https://www.natesilver.net/p/likability-isnt-enough)
**design principle** · general principle · explicit

Silver cautions against overstating the importance of campaign tactics, which are largely constrained by underlying conditions of the race outside the candidates' control. Messaging matters only at the margin.

*Why:* Fundamentals constrain campaigns.

> I don't want to overstate the importance of campaign tactics, a lot of which are constrained by the underlying conditions of the race that are outside of the candidates' control.

<sub>2024-10-22_likability-isnt-enough-by-nate-silver-silver-bulletin#7</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**method** · 538 congressional models, multiple cycles · explicit

Silver's congressional forecasts (FiveThirtyEight and successors) have for many years included measures of candidate ideology or partisanship as predictors, and these measurably improve predictive accuracy.

*Why:* Moderates tend to outperform fundamentals by a few points.

> various measures of ideology or partisanship have been incorporated into our congressional forecasts for many years, and they meaningfully contribute to predictive accuracy.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#0</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**data source** · 538 congressional model 2018+, likely carried into Silver Bulletin · explicit

After dropping CFScores, Silver's congressional model measures candidate ideology solely from congressional roll-call voting. Candidates who break with their party more often usually outperform.

> we now solely used a measure based on Congressional voting, and find that candidates who break with their party more often usually overperform.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#2</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**empirical regularity** · general / congressional models 2022+ · explicit

The declining importance of moderation extends to all 'candidate quality' factors, including incumbency and experience, as partisanship increasingly dominates. Example: Herschel Walker lost, but not by much.

> But that's also true for all "candidate quality" factors such as incumbency or experience. Herschel Walker lost, for instance, but not by all that much.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#4</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**method** · Split Ticket WAR · explicit

Split Ticket WAR is designed to be a residual: a candidate's performance after accounting for district presidential vote, incumbency and other fundamentals. Bonica and Grumbach instead put those factors into regression terms. A higher residual for moderates means moderation is one measure of candidate quality; Silver calls this a feature, not a bias.

*Why:* If a metric's residual correlates with an omitted variable, the metric is biased against that variable, not toward it (NFL draft-pick analogy).

> Split Ticket WAR is deliberately intended to capture the residual — what's left over after you account for the presidential vote in each district, incumbency, and some other "fundamental" factors

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#7</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**empirical regularity** · general · explicit

Controlling mainly for incumbency and district partisanship, moderate candidates usually do a few points better than progressives. The relationship is noisy and declining, but Silver judges it almost certainly real signal.

*Numbers:* moderate overperformance = a few points (Split Ticket WAR finding)

> moderates, controlling for other factors — mainly incumbency and the partisan makeup of the district in other races — indeed usually do a few points better.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#8</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**interpretation guidance** · B&G critique · explicit

Bonica and Grumbach's supplementary specifications found moderation effects under 3 points of vote share. In margin terms that is up to about 6 points, and some of their specifications were statistically significant. Silver argues they chose a specification showing little effect despite these results.

*Numbers:* B&G max effect = under 3 percentage points vote share (supplementary analyses); margin equivalent = up to 6 points of margin (Silver's conversion)

> So in terms of vote margin, the effects of moderation are up to 6 points in some of the models they tried out. That's huge!

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#11</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**limitation or failure mode** · general / congressional models · explicit

Partisan primaries, even in opposite-colored states, tend to nominate more extreme candidates. This leaves few high-leverage data points on how moderate Republicans or conservative Democrats would perform. Larry Hogan-type candidates appear to overperform, but the sample is increasingly small.

> When the Larry Hogans of the world get through to a general election, they seem to overperform, but it's an increasingly small sample.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#23</sub>

### 2025-09-09 · [Is Susan Collins toast?](https://www.natesilver.net/p/is-susan-collins-toast)
**empirical regularity** · general · inferred_from_chart

Susan Collins has beaten Maine's expected lean in every one of her Senate races. Her actual margins against expectations were: 2020 R+8.6 vs D+8.8 expected; 2014 R+37.0 vs D+5.3; 2008 R+22.8 vs D+16.4; 2002 R+16.9 vs D+2.4; 1996 R+5.3 vs D+0.7.

*Numbers:* Collins 2020 result = R+8.6 percentage points (Maine Senate); Collins 2014 result = R+37.0 percentage points (Maine Senate); Collins 2008 result = R+22.8 percentage points (Maine Senate); Collins 2002 result = R+16.9 percentage points (Maine Senate); Collins 1996 result = R+5.3 percentage points (Maine Senate)

*Why:* Collins is far from a generic Republican.

<sub>2025-09-09_is-susan-collins-toast-by-eli-mckown-dawson#2</sub>

### 2025-09-09 · [Is Susan Collins toast?](https://www.natesilver.net/p/is-susan-collins-toast)
**method** · 538 2020 · explicit

Nate Silver's 2020 FiveThirtyEight Senate forecast gave Collins better than a 40% chance of winning despite her polling deficit. Factors such as her moderation and her strong electoral track record pulled her odds up.

*Numbers:* Collins 2020 win probability in 538 = >40 percent (2020 FiveThirtyEight Senate forecast)

*Why:* Candidate-specific factors (ideology, past overperformance) entered the model alongside the polls.

> Nate's forecast for FiveThirtyEight had Collins with better than a 40 percent chance of winning despite her deficit in the polls because of factors like her moderation and her strong track record.

<sub>2025-09-09_is-susan-collins-toast-by-eli-mckown-dawson#4</sub>

### 2025-09-09 · [Is Susan Collins toast?](https://www.natesilver.net/p/is-susan-collins-toast)
**empirical regularity** · general / 2026 midterms · explicit

Silver Bulletin has found that candidate-specific factors such as moderation and past track record are becoming less predictive. Increasingly, only party label matters, which implies smaller weights on candidate-quality and incumbency-overperformance terms in recent cycles.

*Why:* Ticket splitting has declined rapidly over the past decade.

> those factors are becoming less predictive and increasingly often, the only thing that matters is whether you have a "D" or an "R" by your name.

<sub>2025-09-09_is-susan-collins-toast-by-eli-mckown-dawson#5</sub>

### 2025-09-09 · [Is Susan Collins toast?](https://www.natesilver.net/p/is-susan-collins-toast)
**interpretation guidance** · general · explicit

Lesser-known challengers are higher-variance choices. A high-risk, high-reward nominee arguably makes more sense the stronger the incumbent is expected to be.

> The case for a high-risk, high-reward choice arguably becomes better the tougher you think Collins might be to defeat

<sub>2025-09-09_is-susan-collins-toast-by-eli-mckown-dawson#15</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**empirical regularity** · general principle · explicit

A Senate benchmark deficit of 5 to 8 points can be overcome with strong candidates or weak opponents, but large candidate overperformances relative to partisanship are becoming rarer.

*Numbers:* overcomable benchmark range = −5 to −8 percentage points (Senate races)

> A benchmark in the range of −5 to −8 is just narrow enough that it can be overcome with strong candidates — or weak opponents — but large overperformances are getting rarer.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#24</sub>

### 2026-04-21 · [SBSQ #31: Trump is super unpopular. So why don’t Democrats have a bigger lead?](https://www.natesilver.net/p/sbsq-31-trump-is-super-unpopular)
**assumption** · FLIPR 2026 · implied

Silver expects party-brand weakness to matter less once named candidates replace generic labels, and argues the model will reflect individual race-level data, with Democrats tending to nominate fairly strong congressional candidates.

> We’ll see what the model says based on individual-level race data

<sub>2026-04-21_sbsq-31-trump-is-super-unpopular-so-why-dont-democrats-have-a-bigger-lead#8</sub>

### 2026-06-01 · [Should Democrats panic about Platner?](https://www.natesilver.net/p/should-democrats-panic-about-platner)
**empirical regularity** · FiveThirtyEight/FLIPR Senate model · explicit

Candidates who defy their party more often in congressional votes tend to overperform electorally, and the model has used voting-record independence as a fundamentals factor.

> candidates who more often defy their party in Congress tend to overperform electorally

<sub>2026-06-01_should-democrats-panic-about-platner-by-nate-silver#4</sub>

### 2026-06-01 · [Should Democrats panic about Platner?](https://www.natesilver.net/p/should-democrats-panic-about-platner)
**model change** · FLIPR 2026 vs FiveThirtyEight 2020 · explicit

After 2020, the model was tweaked to be less sensitive to candidate-quality factors of any kind and more keyed to raw partisanship, as expressed in the statewide benchmark. Fundamentals still matter some.

> We’ve since tweaked our model to be less sensitive to “candidate quality” factors of any kind and more keyed to raw partisanship

<sub>2026-06-01_should-democrats-panic-about-platner-by-nate-silver#5</sub>

### 2026-06-01 · [Should Democrats panic about Platner?](https://www.natesilver.net/p/should-democrats-panic-about-platner)
**empirical regularity** · FLIPR 2026 · explicit

The model penalizes a candidate's lack of electoral experience, and Silver Bulletin has found that prominent scandals can subtract several points from a candidate's vote share even with less ticket-splitting than in the past.

*Numbers:* scandal penalty = several points (prominent scandals)

> we’ve found that prominent scandals can subtract several points from a candidate’s vote share

<sub>2026-06-01_should-democrats-panic-about-platner-by-nate-silver#6</sub>

### 2026-08-11 · [Everything is breaking Democrats’ way. Is it enough to win the Senate?](https://www.natesilver.net/p/everything-is-breaking-democrats-way)
**parameter or number** · FLIPR 2026 · explicit

FLIPR's analysis finds candidate-quality factors matter only about half as much as when Silver published his first midterm forecast in 2010.

*Numbers:* candidate quality effect relative to 2010 = about half ratio (FLIPR 2026 analysis)

*Why:* Rising partisanship and less ticket-splitting.

> candidate quality factors matter only about half as much as when I published my first midterms forecast in 2010.

<sub>2026-08-11_everything-is-breaking-democrats-way-is-it-enough-to-win-the-senate#8</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

Fancy fundamentals include fundraising from individual contributions only, excluding party and PAC money, with in-state contributions weighted 5x. They also include elected experience on a 0-3 scale, from never elected to current or former senator or governor; party-loyalty scores from congressional votes for incumbents only, since defectors outperform; and scandals, with new scandals counting more than ones a candidate has already survived. The scandal list was compiled by Nathaniel Rakich and is one of the more subjective parts of the model.

*Numbers:* home-state contribution weight = 5x multiplier (fundraising); elected experience scale = 0-3 points (0 never elected, 3 senator/governor)

> Home-state contributions get a 5x weight.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#24</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**model change** · FLIPR 2026 · explicit

FLIPR now estimates the in-state share of contributions from donors whose state is known and extrapolates it to all individual contributions, including small-donor money the FEC does not itemize by state, fixing a clumsy 2022 implementation. Late replacement candidates and candidates who eschew individual contributions, such as JB Pritzker, now have fundraising treated as missing and estimated by proxy instead of zero; FLIPR does not account for self-funding.

> Because FLIPR does not account for self-funding, these candidates would previously have been treated as raising zero money

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#25</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**method** · FLIPR 2026 · explicit

FLIPR collapses all of a candidate's scandals into a single line, essentially keeping only the most recent one, which is lenient to candidates like Ken Paxton who have several.

> it collapses all scandals, however many there are, into a single line, essentially keeping only the most recent one.

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#1</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**parameter or number** · FLIPR 2026 · explicit

Ohio example: simple fundamentals R+3, fancy fundamentals D+1.6 (Sherrod Brown as a strong former senator who ran 8 points ahead of Harris in 2024, against an appointed incumbent), final fundamentals R+0.6, polling average Brown +3.2, Democratic win probability 62 percent.

*Numbers:* Ohio fancy fundamentals = D+1.6 points (Aug 2026); Ohio final fundamentals = R+0.6 points (Aug 2026); Ohio D win prob = 62 percent (Aug 2026)

> Our final fundamentals estimate thus shows an essentially neutral environment in Ohio: R +0.6.

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#4</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**method** · FLIPR 2026 · explicit

FLIPR uses a candidate's past election margin only for incumbents, not challengers.

> FLIPR uses the past election margin only for incumbents and not challengers.

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#5</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**parameter or number** · FLIPR 2026 · explicit

Maine example: simple fundamentals D+15; candidate-specific fancy fundamentals R+11, reflecting Collins's cash advantage, history of overperformance and incumbency; final fundamentals D+1.8; polls Jackson +3; Democratic win probability 70 percent.

*Numbers:* Maine simple fundamentals = D+15 points (Aug 2026); Maine fancy fundamentals = R+11 points (Aug 2026); Maine final fundamentals = D+1.8 points (Aug 2026)

> adding in candidate-specific information takes Maine all the way to R +11, and the model’s final fundamentals estimate is a tight D +1.8.

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#6</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**method** · FLIPR 2026 · explicit

Candidates who enter on an emergency basis, such as Troy Jackson in Maine or Darline Graham in South Carolina, get a partial mulligan: they are treated as having below-average but nonzero fundraising until they file reports.

> the model essentially gives a partial mulligan to candidates who enter the race on an emergency basis

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#7</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**limitation or failure mode** · FLIPR 2026 · explicit

FLIPR uses party-loyalty scores (a bonus for breaking with one's party, usually moderates) only for congressional incumbents, and does not estimate subjective ideology scores for the hundreds of non-incumbents. Candidate ideology, such as Abdul El-Sayed's progressivism, is therefore a known gap that shows up only implicitly through polls and expert ratings.

*Why:* Subjective ideology scoring for hundreds of challengers is impractical.

> So this is a known limitation of the system

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#8</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**method** · FLIPR 2026 · explicit

FLIPR's elected-experience variable counts only elected positions; appointed posts such as El-Sayed's Wayne County Health Director role do not count.

> El-Sayed’s previous positions like Wayne County Health Director were appointed, not elected ones

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#10</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**limitation or failure mode** · FLIPR 2026 · explicit

In Alaska, FLIPR was a bit more bearish on Democrat Mary Peltola than prediction markets, possibly because it does not credit her history of overperformance (Split Ticket WAR scores of D+9 and D+22) or her moderate record, since she is not an incumbent. Such subjective misses are expected to cancel out across many races.

*Numbers:* Alaska baseline = R+7 points (Aug 2026); Alaska D win prob = 42 percent (Aug 2026)

> FLIPR accounts for a lot of things, but not everything.

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#16</sub>

### 2026-08-20 · [Are Democrats on a summer sugar high?](https://www.natesilver.net/p/are-democrats-on-a-summer-sugar-high)
**parameter or number** · FLIPR 2026 · explicit

When Angie Nixon (under $1 million raised, DSA member) beat Alexander Vindman (over $16 million raised) in Florida's Democratic Senate primary, FLIPR Deluxe's Democratic odds fell from 21 to 11 percent, partly via expert rating changes. Silver suspects FLIPR may have over-credited Vindman's fundraising even though it discounts out-of-state money. FLIPR makes no special provision for similar candidate names on ballots.

*Numbers:* FL D win prob with Vindman = 21 percent (Deluxe); FL D win prob with Nixon = 11 percent (Deluxe)

> Democrats’ chances in Florida have fallen from 21 percent with Vindman to 11 percent with Nixon

<sub>2026-08-19_are-democrats-on-a-summer-sugar-high-by-nate-silver#11</sub>

### 2026-08-22 · [A tour of the 48 key House races](https://www.natesilver.net/p/a-tour-of-the-48-key-house-races)
**limitation or failure mode** · FLIPR 2026 · explicit

FLIPR cannot account for an event like incumbent Marcy Kaptur's hospitalization affecting her campaign until it is reflected in expert ratings, which feed the Deluxe version.

> Our model can’t account for any effect that has on her ability to campaign, at least until it’s reflected in expert ratings.

<sub>2026-08-22_a-tour-of-the-48-key-house-races#7</sub>

### 2026-08-22 · [A tour of the 48 key House races](https://www.natesilver.net/p/a-tour-of-the-48-key-house-races)
**empirical regularity** · FLIPR 2026 analysis · explicit

Candidate overperformance is tracked with Split Ticket WAR scores in the analysis: serial overperformer Brian Fitzpatrick (PA-1) has WAR of R+7 to R+15, while Mariannette Miller-Meeks (IA-1) ranges from R+0.6 in 2014 to D+11.3 in 2024, winning by 0.2 where Trump won by 8.4.

*Numbers:* Fitzpatrick WAR range = R+7 to R+15 points (Split Ticket); Miller-Meeks 2024 WAR = D+11.3 points (Split Ticket)

> Her Split Ticket WAR scores range from a neutral R +0.6 in 2014 to an abysmal D +11.3 in 2024.

<sub>2026-08-22_a-tour-of-the-48-key-house-races#8</sub>

### 2026-08-25 · [Do I really buy that Texas could turn blue?](https://www.natesilver.net/p/do-i-really-buy-that-texas-could)
**parameter or number** · FLIPR 2026 · explicit

A scandal flag is worth several points of vote margin in FLIPR's fancy fundamentals, but Silver Bulletin considers the effect of a scandal to be roughly half of what it was a decade or two ago given high polarization. Multiple scandals are folded into one binary flag rather than treated cumulatively.

*Numbers:* scandal effect vs 10-20 years ago = roughly half ratio (FLIPR 2026)

> Basically, we consider the effect of a scandal to be roughly half what it was a decade or two ago

<sub>2026-08-25_do-i-really-buy-that-texas-could-turn-blue#3</sub>

### 2026-08-25 · [Do I really buy that Texas could turn blue?](https://www.natesilver.net/p/do-i-really-buy-that-texas-could)
**design principle** · FLIPR 2026 · explicit

FLIPR uses individual-contribution fundraising from FEC data as a candidate-quality input because money buys ads and staff, proxies a campaign's organizational skill, and proxies voter enthusiasm. It excludes contributions to party organizations, self-funding and Super PAC spending, for practical reasons and because self-funding often signals a lack of organic support.

> self-funding isn’t a good proxy for voter enthusiasm; in fact, candidates often self-fund because they aren’t generating enough organic support

<sub>2026-08-25_do-i-really-buy-that-texas-could-turn-blue#4</sub>

### 2026-08-25 · [Do I really buy that Texas could turn blue?](https://www.natesilver.net/p/do-i-really-buy-that-texas-could)
**limitation or failure mode** · FLIPR 2026 · explicit

Silver worries fundraising may now be a less reliable indicator than FLIPR assumes, because giving is highly nationalized and algorithmized through platforms like ActBlue, and Democrats have had a persistent individual-contribution edge in the Trump era. He names revisiting fundraising as a plausible FLIPR improvement for 2028/2030, especially if candidates like Talarico underperform.

*Numbers:* Talarico in-state itemized individual contributions = 17.5 million USD (as of June 30, 2026); Paxton in-state itemized individual contributions = about 7.6 million USD (as of June 30, 2026); overall fundraising ratio = greater than 7:1 ratio (Talarico vs Paxton)

> part of me wonders whether fundraising is a less reliable indicator than it once was

<sub>2026-08-25_do-i-really-buy-that-texas-could-turn-blue#5</sub>

### 2026-08-25 · [Do I really buy that Texas could turn blue?](https://www.natesilver.net/p/do-i-really-buy-that-texas-could)
**limitation or failure mode** · FLIPR 2026 · explicit

FLIPR handles around 1,000 candidates per cycle and would need ideology estimates for past cycles to train on, so it does not quantify ideology for non-incumbents. For incumbents it uses objective party-loyalty scores from congressional votes; defectors such as Collins get a fancy-fundamentals bonus.

*Numbers:* candidates per cycle = around 1000 candidates (House+Senate+governor)

*Why:* Ideology must be objective and available historically to train on.

> FLIPR handles around 1000 candidates per cycle between House, Senate and gubernatorial elections, and we’d also need to have estimates for past election cycles to train the model.

<sub>2026-08-25_do-i-really-buy-that-texas-could-turn-blue#6</sub>

### 2026-08-25 · [Do I really buy that Texas could turn blue?](https://www.natesilver.net/p/do-i-really-buy-that-texas-could)
**model change** · FiveThirtyEight midterm models pre-2022 · explicit

Before 2022, FLIPR's predecessors used only fancy fundamentals without the simple-fundamentals hedge, so candidate scandals like Paxton's would have carried more weight.

> Prior to 2022, we didn’t use the “simple fundamentals” hedge, so Paxton’s scandals would have gotten more weight in the model.

<sub>2026-08-25_do-i-really-buy-that-texas-could-turn-blue#9</sub>

### 2026-08-25 · [Do I really buy that Texas could turn blue?](https://www.natesilver.net/p/do-i-really-buy-that-texas-could)
**data source** · FLIPR 2026 · explicit

FEC fundraising data for federal races is highly organized and serves as one of the better remaining objective benchmarks; gubernatorial fundraising data is much messier.

> Gubernatorial fundraising data is another story.

<sub>2026-08-25_do-i-really-buy-that-texas-could-turn-blue#10</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**design principle** · FLIPR 2026 · explicit

Because it cannot anchor on partisanship as much, FLIPR puts relatively more weight on candidate factors such as individual contributions, scandals and elected experience in governor races. Gubernatorial fundraising data is less reliable, with incomplete databases requiring state-by-state patchwork.

> Because it can’t anchor on partisanship as much, FLIPR really cares about this kind of stuff for gubernatorial candidates

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#1</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**method** · FLIPR 2026 · explicit

For overwhelmingly self-funded candidates such as Rick Jackson in Georgia or JB Pritzker, FLIPR imputes a fundraising total based on party, office type and the state's partisan lean, treating missing individual contributions as missing data rather than zero. Defining 'self-funder' is tricky, because some candidates self-fund for lack of other support.

*Numbers:* Rick Jackson primary self-funding = 100 million USD (Georgia 2026)

*Why:* Using zero would be unfair to true self-funders.

> FLIPR therefore imputes a fundraising total based on party, the office type and the state’s partisan lean score

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#2</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**method** · FLIPR 2026 · explicit

FLIPR's fundraising variable uses the total amount raised from individuals, not the number of donors.

> Though FLIPR only uses the total amount raised, not the number of donors.

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#3</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**method** · FLIPR 2026 · explicit

FLIPR's threshold for flagging a scandal is a credible accusation. A dismissal removes the flag only if it shows the accusation was false or not credible, not if it was pro forma. Scandals matter more in gubernatorial races with little other information, especially unpolled ones.

> Our threshold for a scandal is a credible accusation

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#4</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**method** · FLIPR 2026 · explicit

Experience is graded by office: a House member such as Tom Tiffany is rated higher than a county executive such as David Crowley. Appointed roles such as Ohio health director Amy Acton earn no experience bonus. Resurfaced offensive social media posts, such as Crowley's 2010 'Dirt McGirk' account, were flagged as a scandal.

> Tiffany has held the more highly-rated office as a member of the House.

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#12</sub>

### 2026-09-23 · [Do Republicans really have a money advantage?](https://www.natesilver.net/p/do-republicans-really-have-a-money)
**method** · FLIPR 2026 · explicit

Individual contributions to candidates are the only campaign-finance data in FLIPR's fancy fundamentals. They are treated as a measure of grassroots support, so contributions from the candidate's own state or district get more weight; party committee, PAC and Super PAC money and ad reservations are not used.

> Democrats also have an advantage when it comes to individual contributions, which is the only campaign finance data that feeds into FLIPR’s “fancy fundamentals” estimates.

<sub>2026-09-23_do-republicans-really-have-a-money-advantage#0</sub>

### 2026-09-23 · [Do Republicans really have a money advantage?](https://www.natesilver.net/p/do-republicans-really-have-a-money)
**adjustment rule** · FLIPR 2026 · explicit

FLIPR gives late-entrant candidates 'amnesty' on fundraising: Troy Jackson, who replaced Graham Platner in Maine and had not yet filed a report, gets credit for half of what Platner raised.

*Numbers:* late-entrant fundraising credit = half share of predecessor's total (Troy Jackson, Maine)

> The model gives him amnesty as a late entrant, so he gets credit for half of what Graham Platner raised.

<sub>2026-09-23_do-republicans-really-have-a-money-advantage#1</sub>

### 2026-09-23 · [Do Republicans really have a money advantage?](https://www.natesilver.net/p/do-republicans-really-have-a-money)
**parameter or number** · FLIPR 2026 data · explicit

In-state shares of itemized individual contributions to 2026 Senate candidates were similar by party: 36 percent for Democrats and 38 percent for Republicans.

*Numbers:* in-state share, D Senate candidates = 36 percent (2026 itemized individual contributions); in-state share, R Senate candidates = 38 percent (2026)

> 36 percent of itemized individual contributions to Democratic Senate candidates are in-state, compared to 38 percent for Republicans.

<sub>2026-09-23_do-republicans-really-have-a-money-advantage#2</sub>

### 2026-09-23 · [Do Republicans really have a money advantage?](https://www.natesilver.net/p/do-republicans-really-have-a-money)
**assumption** · general view · explicit

Silver Bulletin's view is that money is closer to overrated than underrated, at least in high-profile campaigns like Senate and presidential races, where earned media matters more than paid media and diminishing returns set in on saturated airwaves.

> Our view at Silver Bulletin is that money is closer to overrated than underrated

<sub>2026-09-23_do-republicans-really-have-a-money-advantage#3</sub>

### 2026-09-23 · [Do Republicans really have a money advantage?](https://www.natesilver.net/p/do-republicans-really-have-a-money)
**empirical regularity** · general · explicit

Super PACs often pay several times what campaigns do for comparable broadcast TV ads, so ad spending does not equal ad impressions and party or PAC cash is less efficient than candidate dollars.

> Super PACs often pay several times what campaigns do for comparable broadcast TV ads.

<sub>2026-09-23_do-republicans-really-have-a-money-advantage#4</sub>

### 2026-09-23 · [Do Republicans really have a money advantage?](https://www.natesilver.net/p/do-republicans-really-have-a-money)
**parameter or number** · FLIPR 2026 data · explicit

2026 individual-contribution gaps cited as drivers of FLIPR fancy fundamentals: Talarico $66M vs Paxton $9M in Texas; Brown $25M ahead of Husted in Ohio; Peltola $12M ahead of Sullivan in Alaska; El-Sayed $7M ahead of Rogers in Michigan. Totals: Democratic House nominees $648M vs Republicans $437M; Democratic Senate nominees $329M vs $133M.

*Numbers:* Talarico individual contributions = 66 million USD (Sept 2026); D House nominees raised = 648 million USD (2026 cycle); R House nominees raised = 437 million USD (2026 cycle); D Senate nominees raised = 329 million USD (2026 cycle); R Senate nominees raised = 133 million USD (2026 cycle)

<sub>2026-09-23_do-republicans-really-have-a-money-advantage#5</sub>

### 2026-10-23 · [Do these Senate-governor splits make sense?](https://www.natesilver.net/p/do-these-senate-governor-splits-make)
**limitation or failure mode** · FLIPR 2026 · explicit

FLIPR's fundamentals have no variable for a non-incumbent's ideology (e.g. El-Sayed's progressivism); for incumbents, party-loyalty scores from congressional votes capture bipartisanship, which predicts overperformance. Voter views on ideology appear to be priced into the polls instead.

> But we don’t make any similar calculation for non-incumbents.

<sub>2026-10-23_do-these-senate-governor-splits-make-sense#5</sub>

### 2026-10-25 · [Let’s talk shop about every Senate race](https://www.natesilver.net/p/lets-talk-shop-about-every-senate)
**limitation or failure mode** · FLIPR 2026 · explicit

Because fancy fundamentals credit past winning margins only to incumbents, FLIPR may underrate strong non-incumbent candidates with 'proof of concept': Sherrod Brown (won Ohio by almost 7 in 2018, lost by only 3.6 in 2024 while outrunning Harris) and Mary Peltola. Races with appointed incumbents, like Husted in Ohio, are treated as open seats.

> Our “fancy fundamentals” calculation incorporates past winning margins for incumbents, although not for non-incumbents like Brown.

<sub>2026-10-25_lets-talk-shop-about-every-senate-race-by-nate-silver#5</sub>

### 2026-10-25 · [Let’s talk shop about every Senate race](https://www.natesilver.net/p/lets-talk-shop-about-every-senate)
**limitation or failure mode** · FLIPR 2026 · explicit

FLIPR lacks a mechanism for a non-incumbent's ideology; in Michigan, El-Sayed's fundraising made fancy fundamentals better than his polls, and Silver thinks accounting for his ideology would bring FLIPR close to Polymarket.

> FLIPR doesn’t really have any mechanism to account for El-Sayed’s progressivism, even though I think it would be reasonable to do so.

<sub>2026-10-25_lets-talk-shop-about-every-senate-race-by-nate-silver#6</sub>

### 2026-11-02 · [Where polls and fundamentals clash](https://www.natesilver.net/p/where-polls-and-fundamentals-clash)
**method** · FLIPR 2026 · explicit

Fancy fundamentals' candidate-specific factors are incumbency, individual fundraising, elected experience and scandals. Ideology per se is not used, though party-loyalty scores from congressional voting are. Scandal flags can be switched on during a campaign, as Peltola's was late in 2026.

> We don’t account for candidate ideology per-se, but we do calculate party loyalty scores based on congressional voting records.

<sub>2026-11-02_where-polls-and-fundamentals-clash-by-eli-mckown-dawson#4</sub>
