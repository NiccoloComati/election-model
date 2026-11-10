# House effects

67 findings from 32 articles, oldest first.

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**method** · FiveThirtyEight 2016 presidential · explicit

House effects are found by comparing a firm's polls with others of the same state. A proportion is subtracted that depends on how many polls the firm has; for example, a 3-point lean might yield a 1-point adjustment with few polls and 2.8 with dozens. They are computed separately per candidate, so a firm with few undecideds can lean toward both. The reference 'average poll' is weighted by pollster rating.

*Numbers:* example adjustment, few polls = 1 point of 3 (illustration); example adjustment, dozens of polls = 2.8 points of 3 (illustration)

> The model might subtract only 1 point from Clinton if the firm has conducted only a few polls. But it might subtract 2.8 points if the firm has conducted dozens of polls

<sub>fte_2016-general-election-forecast-users-guide#9</sub>

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**parameter or number** · FiveThirtyEight midterm models · explicit

Polls are classified as partisan by sponsor, not by who conducts them: a candidate, party, campaign committee, or a PAC, super PAC or 501(c)(4/5/6) mostly active for one party. Partisan polls get lower weight and a house-effect prior of about 4 points toward the sponsor's side, overridden if the pollster's results match nonpartisan polls over time.

*Numbers:* partisan poll bias prior = about 4 percentage points (toward sponsor)

*Why:* Partisan-sponsored polls are historically less accurate.

> the house effects adjustment starts out with a prior that assumes these polls are biased by about 4 percentage points toward their preferred candidate or party.

<sub>fte_midterm-house-senate-governor-methodology#12</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

The 2020 house-effects adjustment corrects polls that consistently lean toward a party or report more or fewer undecideds than others in the same state. Polls keep part of their house effect, since a small number of polls may reflect noise. House effects are computed mostly from polls of the same state, so a firm can lean differently in different states.

> In calculating house effects, the model mostly uses polls from the same state, so a polling firm could theoretically have a Trump-leaning house effect in one state and a Biden-leaning house effect in another.

<sub>fte_2020-presidential-forecast-methodology#4</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**method** · FiveThirtyEight (Silver era) / general principle · explicit

A pollster with a strong, consistent partisan lean relative to the consensus, such as Rasmussen's Republican lean, should be handled statistically through a house effects adjustment in the polling average rather than through exclusion.

*Why:* Statistical adjustment corrects the lean while keeping the information in the polls.

> there are ways to adjust for that — statistical ways like a house effects adjustment, not ways that involve acting like you're the House Un-American Activities Committee.

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#2</sub>

### 2024-06-27 · [Are these guys trying to muddle through? Or playing to win?](https://www.natesilver.net/p/are-these-guys-trying-to-muddle-through)
**adjustment rule** · 2024 presidential · explicit

The Silver Bulletin model adjusts for partisan polls. One example is state polls from a Republican-aligned group that showed bad numbers for Biden.

> there were a bad set of numbers for Biden from a Republican group, but the model adjusts for the fact that they're partisan polls

<sub>2024-06-27_are-these-guys-trying-to-muddle-through-or-playing-to-win#9</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**adjustment rule** · 2024 presidential polling averages · explicit

The Silver Bulletin polling averages apply house-effect adjustments to individual pollsters.

> and house effects

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#3</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

Older polling data, back to the one-year cutoff, is kept mainly to calibrate the model's adjustments. These include pollster house effects, for example that Rasmussen Reports nearly always has strong numbers for Trump.

*Why:* A longer sample gives better estimates of house effects.

> the older data is still useful for calibrating the various adjustments the model makes: for instance, the house effects associated with certain polling firms (Rasmussen Reports nearly always has strong numbers for Trump

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#5</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**design principle** · general principle · explicit

Silver takes a 'macro' approach to polls: use topline numbers with reasonable adjustments such as house effects, rather than analyzing crosstabs.

> I believe in looking at the topline numbers and making reasonable adjustments for things like house effects, but not driving myself crazy by delving into the crosstabs.

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#26</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**method** · 2024 presidential · explicit

Besides weighting, the Silver Bulletin model applies a house effects adjustment to each poll, correcting for a firm's consistent lean toward Democrats or Republicans. A heavily weighted poll may still be adjusted heavily.

*Why:* Makes the polling averages more stable and strips out firms' statistical bias toward certain candidates.

> even if a poll that's known to lean toward Donald Trump or Kamala Harris gets a large weight in our forecast, it's often being adjusted heavily on the backend

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#5</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**assumption** · general principle · explicit

House effects measure statistical bias, not political bias. The two sometimes correlate and sometimes don't; Fox News's polling department is unbiased despite its editorial slant.

> By "bias", we mean statistical bias. Sometimes this correlates with political bias and sometimes this doesn't

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#6</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**method** · 2024 presidential · explicit

House effects for the 2024 Harris race use only Harris/Trump polls. No leftover Biden/Trump matchup data is used after the candidate switch.

> We don't use any leftover data from the Biden/Trump matchup.

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#7</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**method** · 2024 presidential · explicit

Published house effects are mean-reverted estimates, meant to approximate a pollster's long-run house effect if it surveyed the race every day. Firms with only a handful of polls are shrunk heavily toward the mean; prolific firms such as Morning Consult get more precise, less-shrunk estimates.

*Why:* Few polls give imprecise estimates.

> If a pollster has only conducted a handful of polls, its house effects are discounted heavily toward the mean

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#8</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**adjustment rule** · 2024 presidential · explicit

For nonpartisan polls, house effects are mean-reverted toward a prior of zero.

*Numbers:* prior mean for nonpartisan house effect = 0 percentage points (nonpartisan sponsors)

> For nonpartisan polls, house effects are reverted toward a mean of zero.

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#9</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**adjustment rule** · 2024 presidential · explicit

Polls with partisan sponsors are treated as 'biased until proven unbiased'. Their house effect prior is a lean toward the sponsor's candidate, because presidential partisan-sponsored polls typically exaggerate their candidate's margin by about 3 points, and the model accounts for this.

*Numbers:* typical partisan sponsor exaggeration = about 3 percentage points of margin (presidential polls with partisan sponsors)

*Why:* Empirical tendency of partisan-sponsored polls.

> Presidential polls with partisan sponsors typically exaggerate their candidate's margin by about 3 percentage points and the model accounts for this.

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#10</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**adjustment rule** · 2024 presidential · explicit

Partisan classification depends on the poll's sponsor, not the polling firm, since some firms poll for both partisan and nonpartisan sponsors. The exception is Trafalgar Group, which is always treated as inherently Republican.

*Why:* Trafalgar has a history of failing to disclose who it conducts polls for.

> it's the sponsor of a poll that matters in this calculation, not the polling firm

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#11</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**method** · 2024 presidential · explicit

House effects are calculated by comparing a firm's polls to the trendline of other polls of the same state, or to other national polls for national surveys.

> we basically look at how a firm's polls compare to the trendline of other polls from that state (or compared to other national polls)

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#12</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**method** · 2024 presidential · explicit

House effect estimation is iterative. The model computes trendlines, estimates house effects against them, recomputes trendlines with house-effect-adjusted polls, re-estimates house effects, and so on.

> we calculate the trendlines, then calculate the house effects based on the trendlines, then recalculate the trendlines with adjustments for house effects

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#13</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**method** · 2024 presidential · explicit

In the iterative house-effect process, the more highly rated nonpartisan firms act as the center of gravity: the 'true' values against which other firms are compared. As a result, top-rated firms tend to show little net house effect.

> the more highly rated, nonpartisan firms serve as essentially the center of gravity: the "true" values against which other firms are compared

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#14</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**interpretation guidance** · 2024 presidential · explicit

A raw poll result is shifted by the firm's house effect. An R+1 Rasmussen poll (house effect −2.6 on Harris margin) is treated roughly like a D+2 poll, while an R+1 NYT/Siena poll is treated essentially as R+1.

*Numbers:* Rasmussen house effect = -2.6 points of Harris margin (Sept 27, 2024); NYT/Siena house effect = -0.06 points of Harris margin (Sept 27, 2024)

> If we get an R +1 Rasmussen poll for example, the model thinks about it more like a D +2 poll due to Rasmussen's large house effect.

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#15</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**method** · 2024 presidential · explicit

The model calculates separate house effects for each candidate's vote share (Harris and Trump), not just the margin, because pollsters differ in how many undecided or third-party voters they show. The net margin house effect is roughly Harris house effect minus Trump house effect.

*Why:* Some pollsters show more undecided voters than others.

> we technically calculate separate house effects for Harris's and Trump's vote shares because some pollsters show more undecided voters than others

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#16</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**parameter or number** · 2024 presidential · explicit

YouGov has negative house effects for both Harris (−0.6) and Trump (−0.5), meaning more undecided or third-party voters but little net house effect. Marist has positive house effects for both candidates (table: Harris +0.5, Trump +0.2).

*Numbers:* YouGov Harris house effect = -0.6 points (vote share); YouGov Trump house effect = -0.5 points (vote share); Marist Harris house effect = +0.5 points (vote share, table); Marist Trump house effect = +0.2 points (vote share, table)

> YouGov actually has negative house effects for both Harris (-0.6) and Trump (-0.5)

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#17</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**parameter or number** · 2024 presidential · inferred_from_chart

Mean-reverted house effects on Harris margin as of Sept 27, 2024, for pollsters with at least 5 Harris/Trump polls. Democratic-leaning: Ipsos +1.9, Outward Intelligence +1.9, PPP +1.4, Morning Consult +1.2, Big Village +1.0, Bullfinch +0.8, Change Research +0.7, UNH +0.4, Focaldata +0.4, Benenson/GS +0.3, Marist +0.3, SurveyUSA +0.3, MassINC +0.2, Fox (Beacon/Shaw) +0.1, TIPP +0.1, Suffolk +0.0. Near zero or slightly Republican-leaning: Quinnipiac −0.0, YouGov −0.0, NYT/Siena −0.1, Fabrizio/Impact −0.1, SSRS (CNN) −0.1, POS −0.1, Emerson −0.3, FAU/Mainstreet −0.3, Patriot Polling −0.3. Republican-leaning: GSG/GBAO (Navigator) −0.4, RMG −0.4, Redfield & Wilton −0.5, Cygnal −0.8, InsiderAdvantage −0.8, Harris Insights & Analytics −1.3, Capitol Weekly −1.5, Spry −2.3, Rasmussen −2.6, Trafalgar −2.7.

*Numbers:* Ipsos = +1.9 points of Harris margin (Sept 27 2024); Outward Intelligence = +1.9 points; Public Policy Polling = +1.4 points; Morning Consult = +1.2 points; Big Village = +1.0 points; Bullfinch = +0.8 points; Change Research = +0.7 points; University of New Hampshire = +0.4 points; Focaldata = +0.4 points; Benenson/GS Strategy Group = +0.3 points; Marist College = +0.3 points; SurveyUSA = +0.3 points; MassINC = +0.2 points; Beacon/Shaw (Fox News) = +0.1 points; TIPP Insights = +0.1 points; Suffolk = +0.0 points; Quinnipiac = -0.0 points; YouGov = -0.0 points; NYT/Siena = -0.1 points (text says -0.06); Fabrizio Lee/Impact Research = -0.1 points; SSRS (CNN) = -0.1 points; Public Opinion Strategies = -0.1 points; Emerson = -0.3 points; FAU/Mainstreet = -0.3 points; Patriot Polling = -0.3 points; Global Strategy Group/GBAO (Navigator) = -0.4 points; RMG Research = -0.4 points; Redfield & Wilton = -0.5 points; Cygnal = -0.8 points; InsiderAdvantage = -0.8 points; Harris Insights & Analytics = -1.3 points; Capitol Weekly = -1.5 points; Spry Strategies = -2.3 points; Rasmussen Reports = -2.6 points; Trafalgar Group = -2.7 points

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#18</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**parameter or number** · 2024 presidential · inferred_from_chart

Separate vote-share house effects (Harris, Trump) with poll counts and pollster ratings, from the table as of Sept 27, 2024: NYT/Siena 16 polls, A+, −0.3/−0.2; Fox (Beacon/Shaw) 13, A, −0.1/−0.2; Cygnal 7, A, −0.6/+0.1; Marist 10, A, +0.5/+0.2; SurveyUSA 15, A, −0.1/−0.3; Emerson 37, A-, +0.3/+0.6; POS 5, A-, −0.1/+0.0; PPP 15, A-, +0.1/−1.3; Quinnipiac 9, A-, +0.0/+0.0; Suffolk 5, A-, −0.4/−0.4; MassINC 5, A/B, +0.2/−0.0; TIPP 9, A/B, −0.6/−0.7; Harris Insights & Analytics 10, B+, +0.2/+1.5; Trafalgar 11, B+, −1.6/+1.0; YouGov 40, B+, −0.6/−0.5; Big Village 8, B, −0.9/−1.9; InsiderAdvantage 15, B, −0.5/+0.3; Rasmussen 21, B, −1.3/+1.3; Change Research 6, B-, −0.3/−1.1; Ipsos 14, B-, −0.6/−2.5.

*Numbers:* Rasmussen Harris/Trump house effects = -1.3/+1.3 points (21 polls, rating B); Ipsos Harris/Trump house effects = -0.6/-2.5 points (14 polls, rating B-); Trafalgar Harris/Trump house effects = -1.6/+1.0 points (11 polls, rating B+); Emerson Harris/Trump house effects = +0.3/+0.6 points (37 polls, rating A-); minimum polls for inclusion in chart = 5 polls (Harris/Trump polls)

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#19</sub>

### 2024-10-09 · [When you should panic about the polls](https://www.natesilver.net/p/when-you-should-panic-about-the-polls)
**empirical regularity** · general principle · explicit

Quinnipiac polls tend to be 'bouncy' (high variance) and the firm is not one accused of herding. Its swings should therefore be read in the context of the many other polls rather than as decisive.

> Quinnipiac polls tend to be "bouncy": they're not one of those firms you can accuse of herding.

<sub>2024-10-09_when-you-should-panic-about-the-polls-by-nate-silver#12</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**adjustment rule** · Silver Bulletin polling averages 2024 · explicit

Publicly released internal polls must be debiased. The Silver Bulletin polling averages do this through their house effects adjustment, together with the trendline adjustment.

*Why:* Released internals have a predictable, empirically trackable bias toward their sponsor.

> Our polling averages account for this tendency through our house effects adjustment.

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#1</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**empirical regularity** · general principle / Silver Bulletin data · explicit

Historically, publicly released presidential internal polls have been biased by an average of about 3 points toward the sponsoring campaign's candidate. The bias is somewhat larger for Congressional and downballot races.

*Numbers:* average bias of presidential internal polls = about 3 percentage points (margin) (toward the sponsoring candidate, public-record internals); downballot internal bias = a bit larger than 3 percentage points (Congressional and downballot races)

*Why:* Because released internals enter the public record, their bias can be tracked against results over time.

> presidential internal polls are biased by an average of about 3 points toward their candidates and a bit larger than that for Congressional and downballot races

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#2</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**method** · Silver Bulletin polling averages 2024 · explicit

For internal polls, the size of the house effect adjustment varies by state depending on how much the internal poll differs from public polls in that state. After adjustment, the polls almost exactly match the public polling averages.

*Why:* Silver says the state-to-state variation is not particularly important. What matters is that the bias of released internals is highly predictable.

> The magnitude of the adjustment differs slightly from state to state based on how much the Trump poll differed from public polls there

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#3</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**parameter or number** · Silver Bulletin polling averages 2024 · inferred_from_chart

The Trump campaign internals released Oct. 10, 2024 were adjusted by the Silver Bulletin house effects and trendline adjustments as follows. Arizona: Trump +3.0 to Trump +0.5. Georgia: Trump +5.0 to Trump +1.7. Michigan: Trump +1.0 to Harris +1.8. Nevada: Trump +3.0 to Harris +0.3. North Carolina: Trump +1.0 to Harris +1.4. Pennsylvania: Trump +1.0 to Harris +1.8. Wisconsin: Trump +1.0 to Harris +1.9. The implied adjustments run from roughly 2.4 to 3.3 points toward Harris.

*Numbers:* AZ raw/adjusted = Trump +3.0 / Trump +0.5 margin (Oct 10 2024 Trump internal); GA raw/adjusted = Trump +5.0 / Trump +1.7 margin (Oct 10 2024); MI raw/adjusted = Trump +1.0 / Harris +1.8 margin (Oct 10 2024); NV raw/adjusted = Trump +3.0 / Harris +0.3 margin (Oct 10 2024); NC raw/adjusted = Trump +1.0 / Harris +1.4 margin (Oct 10 2024); PA raw/adjusted = Trump +1.0 / Harris +1.8 margin (Oct 10 2024); WI raw/adjusted = Trump +1.0 / Harris +1.9 margin (Oct 10 2024); implied adjustment range = 2.4-3.3 percentage points (computed from table differences)

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#4</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**empirical regularity** · general principle · explicit

Released internal polls are biased partly because of selective release, not only because of methodology. Campaigns poll every week and publicize the batches that look favorable because of sampling noise, or the version run under favorable likely-voter assumptions.

> If one batch happens to be particularly favorable one week, you share it with Politico — otherwise, you don't.

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#5</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**empirical regularity** · general principle · explicit

Campaigns usually keep released internals within the range of credibility; extreme misses like Cantor's are the exception. Released internals are rarely fabricated outright but are nearly always shaded toward the client.

> Usually, campaigns won't go Full McLaughlin; they'll want to publish something within the range of credibility.

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#6</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**empirical regularity** · historical example · explicit

In the 2014 VA-7 Republican primary, a publicly released internal poll by John McLaughlin showed Eric Cantor ahead by 34 points. Cantor lost to David Brat by 11 points, an error of about 45 points.

*Numbers:* Cantor internal lead = 34 points (2014 VA-7 GOP primary); actual result = Brat +11 points (2014 VA-7)

> Eric Cantor lost to David Brat by 11 (!) points after a publicly released internal poll had shown Cantor ahead by 34 (!!)

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#7</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**empirical regularity** · historical example 2012 · explicit

Romney's 2012 campaign internals, obtained after the election, were biased toward Romney by an average of 4.7 points across seven states: an average of Obama +1.0 versus an actual Obama +5.7. Footnote 2 says public polls were also biased toward Romney in 2012, but less so. The state-level biases toward Romney were: CO 7.9, IA 5.8, MN 3.7, NH 9.1, OH 1.0, PA 2.4, WI 2.8.

*Numbers:* average bias = 4.7 points toward Romney (2012 internals, 7 states); CO bias = 7.9 points (Romney +2.5 internal vs Obama +5.4 actual); IA bias = 5.8 points (tie vs Obama +5.8); MN bias = 3.7 points (Obama +4.0 vs Obama +7.7); NH bias = 9.1 points (Romney +3.5 vs Obama +5.6); OH bias = 1.0 points (Obama +2.0 vs Obama +3.0); PA bias = 2.4 points (Obama +3.0 vs Obama +5.4); WI bias = 2.8 points (Obama +4.0 vs Obama +6.8)

*Why:* Shows that even private, unreleased internals can be heavily biased.

> The polls were biased toward Romney by an average of almost 5 points.

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#9</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**assumption** · general principle · explicit

Genuine, unreleased campaign internals may be biased toward their candidate even before any selective release. Silver gives three reasons: campaigns poll for resource allocation and message testing rather than prediction; principal-agent problems and optimism bias discourage delivering bad news to the boss; and staff are partisan true believers prone to motivated reasoning.

*Why:* Campaigns are not harmed by a consistent bias because their decisions do not depend on accurate prediction.

> So you're selecting for people who are high on partisan motivated reasoning, who have organizational incentives to sugarcoat the data

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#10</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**empirical regularity** · 2024 polling landscape · explicit

NYT/Siena polls do not weight by recalled vote. According to Nate Cohn, they would be significantly more Trump-leaning if they did. Polls that do weight by recalled vote produce maps more similar to 2020, because they effectively force the electorate to resemble the last election.

> polls that use recalled vote choice show a map that's more similar to 2020 — in some sense, they're just forcing the electorate to look more like four years ago

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#11</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**empirical regularity** · 2024 · explicit

In October 2024, high-quality pollsters diverged on the state map. NYT/Siena showed Harris +4 in Pennsylvania and Trump +6 in Arizona, while the Wall Street Journal showed Trump +1 in Pennsylvania and Harris +2 in Arizona. The polling averages showed much closer races in both states.

*Numbers:* NYT/Siena PA = Harris +4 points (Oct 2024); NYT/Siena AZ = Trump +6 points (Oct 2024); WSJ PA = Trump +1 points (Oct 2024); WSJ AZ = Harris +2 points (Oct 2024)

> Wall Street Journal polls showed Trump 1 point ahead in Pennsylvania but Harris leading by 2 in Arizona

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#16</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**adjustment rule** · 2024 presidential · explicit

The Silver Bulletin polling averages adjust each poll for its pollster's house effect, so a firm that consistently leans toward one party has that lean corrected before it enters the average.

*Why:* This counteracts systematic lean from partisan-aligned firms, which blunts any 'flooding the zone' strategy.

> adjust them based on pollsters' house effects

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#1</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**empirical regularity** · 2024 presidential · explicit

Fox News polling has no history of GOP bias, so a Fox News poll showing Trump ahead was treated as a high-quality signal that moved the Silver Bulletin forecast.

> yes, it’s from Fox News, but Fox News polling has no history of GOP bias

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#14</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**empirical regularity** · 2024 presidential · explicit

Pollsters differ in the direction of their LV/RV gap. Nationally, Harris does better in the LV version for nearly all firms: NYT/Siena +0.8, YouGov +0.3, Marist +0.5. Harris Insights is the only exception.

*Numbers:* NYT/Siena national LV gain for Harris = 0.8 percentage points (2024); YouGov national LV gain for Harris = 0.3 percentage points (2024); Marist national LV gain for Harris = 0.5 percentage points (2024)

> Harris does 0.8 points better in the LV versions of national New York Times/Siena polls, 0.3 points better in LV YouGov polls, and 0.5 points better in LV Marist polls.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#11</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**empirical regularity** · 2024 presidential · inferred_from_chart

State-level LV-minus-RV margin shifts by pollster (positive = Republican), among firms with at least two state polls: NYT/Siena -0.5, Marquette -0.5, Washington Post -0.4, Morning Consult -0.2, YouGov +0.4, Florida Atlantic +0.4, Marist +0.6, Beacon/Shaw (Fox) +1.6, TIPP +2.0, Focaldata +2.5, Noble Predictive +3.0.

*Numbers:* NYT/Siena = -0.5 percentage points (State LV-RV shift); Marquette = -0.5 percentage points (State LV-RV shift); Washington Post = -0.4 percentage points (State LV-RV shift); Morning Consult = -0.2 percentage points (State LV-RV shift); YouGov = +0.4 percentage points (State LV-RV shift); Florida Atlantic = +0.4 percentage points (State LV-RV shift); Marist = +0.6 percentage points (State LV-RV shift); Beacon/Shaw (Fox) = +1.6 percentage points (State LV-RV shift); TIPP = +2.0 percentage points (State LV-RV shift); Focaldata = +2.5 percentage points (State LV-RV shift); Noble Predictive = +3.0 percentage points (State LV-RV shift)

<sub>2024-10-24_a-mystery-in-likely-voter-polls#12</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**interpretation guidance** · general principle · explicit

A herding test that assumes a tied race understates herding in states whose consensus is not a tie, such as AZ and GA leaning Trump and MI leaning Harris. It overstates closeness deficits for pollsters with house effects, such as YouGov leaning Harris, because herders aim at the consensus rather than at zero.

> if pollsters are trying to match the consensus, a stray Trump +3 in Arizona or Harris +3 in Michigan won’t stand out so much

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#13</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**interpretation guidance** · general principle · explicit

Silver describes Emerson College as a firm that herds heavily, virtually never publishing results that defy conventional wisdom, and says readers should account for that when interpreting its polls. Its final 2024 Iowa poll was Trump +9, with a 95% interval of Trump +15.7 to Trump +2.5.

*Numbers:* Emerson Iowa poll = Trump +9 percentage points (published Nov 2, 2024, before Selzer); Emerson 95% interval = Trump +15.7 to Trump +2.5 percentage points (Emerson Iowa poll)

*Why:* Herding makes a poll less independent and less informative.

> Emerson is a firm that does a lot of herding, so you ought to account for that — they virtually never publish a survey that defies the conventional wisdom.

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#6</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**limitation or failure mode** · 2024 presidential · explicit

Silver theorizes that pollsters herd heavily in high-profile swing states (WI, MI, PA) while showing their true numbers in more obscure Midwestern states. The 2024 Silver Bulletin model is not sophisticated enough to account for differential herding by state profile. Silver says readers should infer that Harris might outperform her Blue Wall polls, especially in Wisconsin.

> Our model isn't quite sophisticated enough to go into this level of detail

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#18</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**empirical regularity** · general principle · explicit

Fewer than 10% of 2024 polls in states like Wisconsin showed anything outside Harris +2 to Trump +2. Sampling error alone makes that statistically very unlikely, which is evidence of herding.

*Numbers:* Share of WI polls outside ±2 = less than 10 percent (2024)

> Why so few polls in states like Wisconsin — less than 10 percent! — dare to show anything outside the range of Harris +2 to Trump +2

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#19</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**adjustment rule** · Silver Bulletin polling averages 2024 · explicit

The Silver Bulletin polling averages adjust for each pollster's house effect.

*Why:* Produces a more stable average.

> and house effects

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#7</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**limitation or failure mode** · general principle · explicit

Herding means pollsters withholding results that differ from consensus, or tweaking likely-voter models until they match. Weighting on variables correlated with vote choice, such as past vote and party, reduces poll-to-poll variance by design. That makes low variance an unreliable signal of herding, and Blumenthal sees it as the main reason aggregates show less variation.

> When pollsters weight on things that are correlated with future vote choice — like past vote choice — you’d expect less variance than you would with a truly random unweighted sample.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#18</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**limitation or failure mode** · general principle · explicit

Pollsters face competing incentives:
- Reputational risk encourages herding, especially in tight races, toward the average and toward 'no clear winner'.
- Trump's lawsuit against Selzer will likely make pollsters more nervous about releasing outliers.
- Some pollsters, e.g. those not weighting on education, may publish high-variance outliers because they attract headlines.

> It’s easier to be wrong with everyone else and to say “let’s analyze what the industry did wrong” than to be wrong on your own

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#19</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**method** · Silver Bulletin pollster ratings June 2024 · explicit

Mean-reverted bias is a pollster's historical average statistical bias toward Democrats or Republicans, shrunk toward zero based on the number of polls in the database. 'D +1.5' means the pollster has historically overrated Democratic candidates.

*Numbers:* example bias score = D +1.5 percentage points (overrated Democrats)

*Why:* Shrinkage reduces noise for pollsters with few polls.

> reverted to a mean of zero based on the number of polls in the database

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#12</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**adjustment rule** · Silver Bulletin pollster ratings June 2024 · explicit

Mean-reverted bias is calculated only for races in which exactly one Republican and one Democrat are the two leading candidates, so it excludes presidential primaries.

*Why:* Partisan bias is undefined without a D-vs-R matchup.

> This is calculated only for races in which exactly one Republican and one Democrat are the two leading candidates

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#13</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**empirical regularity** · general principle · explicit

In 2024, pollsters with Democratic-leaning house effects (such as YouGov) performed worse and those with Republican-leaning house effects performed better. Siena, SurveyUSA and YouGov had biases of about D+5.

*Numbers:* bias = about 5 points D (Siena, SurveyUSA, YouGov 2024)

*Why:* Trump beat his polls again.

> firms like YouGov that had Democratic-leaning house effects performed worse, while those with R-leaning ones were better

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#35</sub>

### 2025-05-06 · [We're tracking more data on Trump's popularity](https://www.natesilver.net/p/were-tracking-more-data-on-trumps)
**empirical regularity** · Silver Bulletin pollster ratings / approval database · explicit

Across pollsters in the 2024 Silver Bulletin presidential approval database, average Trump approval margin correlates at -0.21 with each pollster's mean-reverted historical bias, where positive bias means pro-Democratic. Pollsters with a historical Republican bias show Trump doing better, which indicates house effects persist from cycle to cycle.

*Numbers:* correlation = -0.21 (pollster mean-reverted bias vs. average Trump approval margin)

> Pollster house effects have been persistent from cycle to cycle, in other words.

<sub>2025-05-06_were-tracking-more-data-on-trumps-popularity#7</sub>

### 2025-05-06 · [We're tracking more data on Trump's popularity](https://www.natesilver.net/p/were-tracking-more-data-on-trumps)
**limitation or failure mode** · general principle · explicit

Silver warns that pollsters are increasingly self-conscious about where they stand relative to other polls, which is close to herding. He argues nonpartisan pollsters should aim purely for accuracy rather than identifying as Trump-leaning or anti-Trump.

*Why:* Positioning relative to other pollsters risks herding and narrative-shaping.

> it's a fine line between this sort of thing and herding

<sub>2025-05-06_were-tracking-more-data-on-trumps-popularity#11</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**empirical regularity** · general principle · explicit

Herding appeared less prevalent among 2025 polls than in 2024.

> herding looked to be less prevalent last year than it was in 2024

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#22</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**interpretation guidance** · Silver Bulletin pollster ratings · explicit

House effect and statistical bias are distinct. A house effect compares a firm's results with other polls of the same race; bias compares them with the actual result. A firm showing R+3 where other polls show a tie has an R house effect, but if the Republican wins by 5 it still has a 2-point Democratic bias.

> Note that house effects are distinct from statistical bias.

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#10</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**method** · Silver Bulletin pollster ratings · explicit

House effect measures how a firm's results compare with other polls of the same race. It is distinct from statistical bias, which compares results with the actual outcome. Example: a firm shows R+3 when the other polls show a tie, so it has a Republican house effect. If the Republican wins by 5, the firm still has a 2-point Democratic bias.

*Numbers:* example poll = R+3 percentage points (hypothetical firm's result vs. a tied field); example result = R+5 percentage points (hypothetical actual outcome); example bias = 2 percentage points (Democratic) (resulting bias of the hypothetical firm)

> Note that house effects are distinct from statistical bias.

<sub>2026-01-14_pollster-ratings-silver-bulletin#19</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**empirical regularity** · Silver Bulletin pollster ratings Jan 2026 · inferred_from_chart

House effects can differ in sign from bias. Cygnal has an R+0.59 house effect but a D+2.04 mean-reverted bias. Other house effects include Public Opinion Strategies R+4.14, OnMessage R+3.54, Grove Insight D+3.27 and AtlasIntel R+2.00.

*Numbers:* Public Opinion Strategies house effect = R+4.14 percentage points (Jan 2026); Cygnal house effect = R+0.59 percentage points (Jan 2026)

<sub>2026-01-14_pollster-ratings-silver-bulletin#27</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**method** · Silver Bulletin polling averages (2026) · explicit

A house effect is a firm's persistent difference from other polls of the same race at the same time. Only a proportion of it is removed, and that proportion grows with the firm's total sample size on that question, from a small fraction for a firm with one or two polls to nearly 100 percent for very frequent pollsters.

*Numbers:* share of house effect removed = close to 100 percent (firms that poll a question extremely often)

*Why:* Shrinkage: confidence in a firm's house effect grows with how much it has polled.

> The proportion subject to the house effects adjustment is based on the aggregate sample size of polling conducted by the firm.

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#10</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**model change** · Silver Bulletin generic ballot average (2026) · explicit

The generic ballot uses a newer house-effect formula that starts with a smaller adjustment but ramps up faster as sample size grows. Silver Bulletin considers it slightly more accurate and expects to move approval averages to it, though it only changes results in the decimal places.

*Why:* Slightly more accurate.

> starts out with a lower adjustment but ramps it up more quickly as the aggregate sample size increases.

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#11</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**method** · Silver Bulletin polling averages (2026) · explicit

House effects are estimated separately for each side, approve and disapprove or Democrat and Republican, rather than only on the margin. The model also adjusts for firms that persistently report more or fewer undecided voters than the average.

*Why:* Firms differ systematically in how many undecideds they report.

> Certain firms persistently include more or fewer undecided voters than the polling average, and so we adjust for this, too.

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#12</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**method** · Silver Bulletin polling averages (2026) · explicit

The 'true north' that polls are adjusted toward is weighted toward higher-rated pollsters. For the generic ballot, partisan-sponsored polls are excluded from the true-north calculation.

*Why:* The reference point for bias should come from the most reliable, non-partisan sources.

> Firms with higher pollster ratings have more influence on what our model considers to be "true north"

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#13</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**method** · Silver Bulletin polling averages (2026) · explicit

House effects are found iteratively. First compute an average without adjustments, then estimate each firm's house effect against the polynomial curve, recompute the average with adjusted polls, re-estimate house effects, and repeat several times until there is no further improvement.

*Why:* House effects and the average depend on each other, so they are solved jointly.

> The model loops through the process several times until there are no further gains to be had.

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#14</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**parameter or number** · Silver Bulletin generic ballot and forecast averages (2026) · explicit

For the generic ballot and the horse-race averages used in forecasts, explicitly partisan polls start with a prior that they are biased toward the sponsor by a net of about 1.7 points. Nonpartisan polls start with a zero prior. Both priors are eventually overridden by the firm's actual track record against other polls. The prior is not used for presidential approval.

*Numbers:* partisan poll prior bias = ~1.7 points (net margin) (toward the sponsoring party, generic ballot and forecast horse-race averages)

*Why:* Default to assuming nonpartisan polls are unbiased and partisan polls lean toward their sponsor until data says otherwise.

> we assume they're slightly biased toward the sponsoring candidate or party. (More specifically, by a net of about 1.7 points.

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#15</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**parameter or number** · FLIPR 2026 · explicit

FLIPR's house effects are estimated from both generic ballot and individual race polls, and are more punitive to partisan or internal campaign polls released publicly, which start with a prior that they are biased. Historically that bias averages about 4 points toward the preferred candidate.

*Numbers:* historical bias of partisan/internal polls = about 4 points (toward sponsor's candidate)

> On average in the historical data, this bias is about 4 points toward their preferred candidate.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#8</sub>

### 2026-08-28 · [A tour of the 9 key governor races](https://www.natesilver.net/p/a-tour-of-the-9-key-governor-races)
**adjustment rule** · FLIPR 2026 · explicit

Because FLIPR adjusts partisan-sponsored polls against their sponsor, a Democratic Governors Association poll showing the Democrat up 1 in Florida was treated as evidence the Republican was a few points ahead.

*Why:* Partisan polls get a prior bias toward their sponsor.

> With the way FLIPR adjusts polls for partisanship, it actually thinks that bolsters the case for Donalds being a few points ahead.

<sub>2026-08-28_a-tour-of-the-9-key-governor-races#13</sub>

### 2026-09-03 · [Beware big swings in midterm forecasts](https://www.natesilver.net/p/beware-big-swings-in-midterm-forecasts)
**interpretation guidance** · Silver Bulletin polling averages · explicit

Trends within a single pollster's series tell more than differences across pollsters, but they take more evidence and time to calibrate.

> Trends within a given pollster’s data (i.e., if the New York Times/Siena College poll shows Republicans gaining ground on the generic ballot) tend to tell you more than trends across different pollsters

<sub>2026-09-03_beware-big-swings-in-midterm-forecasts#8</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**method** · FLIPR 2026 · explicit

FLIPR does not assume any individual poll is unbiased: its house-effects adjustment pulls firms with systematic D-vs-R differences, such as Marist's Democratic-leaning 2026 numbers, toward the consensus.

> FLIPR adjusts their polls to be closer to the consensus, as we do with any firm that shows these systematic differences.

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#4</sub>

### 2026-10-22 · [Fake polls are a real problem](https://www.natesilver.net/p/fake-polls-are-a-real-problem)
**parameter or number** · Silver Bulletin 2026 analysis · explicit

The fabricated Wedgewood polls had a mild, inconsistent Democratic house effect of about 0.6 points versus Silver Bulletin averages computed as of the day before their final field date. They were often the first polls in sparsely polled races and favored progressive candidates.

*Numbers:* Wedgewood house effect = about 0.6 points toward D (vs Silver Bulletin averages)

> their “polls” were about 0.6 points more favorable to the Democratic candidate on average.

<sub>2026-10-22_fake-polls-are-a-real-problem-by-nate-silver#6</sub>

### 2026-10-25 · [Let’s talk shop about every Senate race](https://www.natesilver.net/p/lets-talk-shop-about-every-senate)
**adjustment rule** · FLIPR 2026 · explicit

Internal campaign polls carry a typical 3 to 4-point bias toward their sponsor, so in FLIPR logic a Republican internal showing the Republican up only 2 is evidence of a toss-up, and a candidate's own internal showing him up 1 is worse news for him than opposing internals showing him down 2 or 3.

*Numbers:* typical internal poll bias = 3-4 points (toward sponsor)

> In FLIPR logic, that’s actually a worse poll for him than Republican internals showing him trailing by 2 or 3.

<sub>2026-10-25_lets-talk-shop-about-every-senate-race-by-nate-silver#8</sub>
