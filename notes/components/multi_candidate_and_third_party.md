# Multi candidate and third party

46 findings from 24 articles, oldest first.

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**adjustment rule** · FiveThirtyEight 2016 presidential · explicit

The omitted third-party ('missing Johnson') adjustment estimates how much support the third-party candidate draws from the major candidates rather than undecideds: relatively little from undecideds. It assumes he draws equally from both, and it varies by state, taking more where he is stronger.

> The adjustment assumes Johnson takes his support from Clinton and Trump equally.

<sub>fte_2016-general-election-forecast-users-guide#7</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**empirical regularity** · FiveThirtyEight 2016 presidential · explicit

Third-party candidates tend to underperform their early polls, though not necessarily their late ones, because some early third-party supporters are undecideds using them as placeholders. Polls-plus reallocated some early third-party support to undecided; polls-only and now-cast did not.

> Historically, third-party candidates tend to underperform their early polls.

<sub>fte_2016-general-election-forecast-users-guide#10</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**method** · FiveThirtyEight 2016 presidential · explicit

Undecided voters are split evenly between the major-party candidates, which empirically works better in presidential races than a proportional split. Late in the race the third-party candidate also gets a share, and a small 'other' share is reserved in states expected to have four or more candidates on the ballot.

> Undecided voters are split evenly between the major-party candidates. Empirically, an even split works better for presidential races than a proportional split.

<sub>fte_2016-general-election-forecast-users-guide#11</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**method** · FiveThirtyEight 2016 presidential · explicit

The third-party (Johnson) vote is regressed on his 2012 vote, the 1980-2008 third-party vote (Perot/Anderson) and PVI. It has national and state-specific error but no demographic/regional error, since third-party candidates tend to rise or fall everywhere together. It is simulated with a combination of beta and t distributions, producing right-tailed outcomes. Ballot access is assumed where already secured, or where it existed in 2012 and the deadline has not passed.

> The model uses a combination of a beta distribution and a t -distribution to model Johnson’s vote.

<sub>fte_2016-general-election-forecast-users-guide#24</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

A 'major' third-party candidate, modeled explicitly as with Gary Johnson in 2016 or Perot in backtests, must be on the ballot almost everywhere, included in most polls, and usually polling in the mid-to-high single digits. 'Other' votes are predicted per state from the number of third-party candidates on the ballot, write-in rules, historical third-party share and competitiveness, since swing states give third parties fewer votes.

> We defined major as (i) a candidate who is on the ballot almost everywhere, (ii) who is included in most polls and (iii) who usually polls in at least the mid-to-high single digits.

<sub>fte_2020-presidential-forecast-methodology#30</sub>

### 2023-09-18 · [Is a Trump-Biden rematch inevitable?](https://www.natesilver.net/p/is-a-trump-biden-rematch-inevitable)
**empirical regularity** · general principle · explicit

In multi-candidate primaries, a front-runner's opponents gain ground in head-to-head matchup polls; the amount depends on the poll. Races should therefore tighten when the field narrows to two or three candidates.

*Why:* Consolidation of the anti-front-runner vote.

> Trump’s opponents do gain some ground in head-to-head matchups

<sub>2023-09-18_is-a-trump-biden-rematch-inevitable-by-nate-silver#13</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**method** · 2024 presidential (and 538 2016) · explicit

The model distinguishes 'named' third-party candidates, who could plausibly affect the overall dynamics of the race, from 'other' candidates, who are treated as a rounding error. The designation is somewhat subjective. In backtesting since 1968 it applies to Wallace 1968, Anderson 1980, Perot 1992 and 1996, Nader 2000, Johnson 2016, and RFK Jr. in 2024.

*Numbers:* backtesting start year = 1968 year (elections used for backtesting third-party logic)

> meaning one who could plausibly have an effect on the overall dynamics of the race rather than one who can be treated as a rounding error

<sub>2024-06-26_2024-presidential-election-model-methodology-update#9</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**adjustment rule** · 2024 presidential · explicit

In the simulations, 'named' third-party candidates can win states and electoral votes, but candidates designated 'other' cannot. As of June 2024, RFK Jr. won electoral votes in about 5% of simulations.

*Numbers:* share of simulations where RFK Jr. wins electoral votes = about 5 percent (as of June 2024)

> “named” third-party candidates are allowed to win states and electoral votes (as Kennedy does in about 5 percent of simulations as of June 2024)

<sub>2024-06-26_2024-presidential-election-model-methodology-update#10</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**empirical regularity** · 2024 presidential · explicit

Third-party vote share has a highly asymmetric, right-skewed distribution. Usually support fades late as voters judge the candidate non-viable and avoid wasting votes. A right tail exists where the candidate takes off, as Perot did in 1992. The model encodes this: RFK Jr.'s modal outcome is about 4% of the vote, yet he occasionally wins electoral votes.

*Numbers:* RFK Jr. modal vote share = something like 4 percent (model's modal outcome as of June 2024); RFK Jr. initial poll share = around 10 percent (earlier in the 2024 cycle); RFK Jr. recent poll share = mid-to-high single digits percent (more recent surveys, especially likely voters)

*Why:* Voters abandon non-viable candidates, but breakout cases exist.

> third-party candidates have a highly asymmetric probability distribution for their vote share. Most of the time, their vote fades down the stretch run

<sub>2024-06-26_2024-presidential-election-model-methodology-update#12</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**empirical regularity** · 2024 presidential · explicit

Biden is probably hurt by the left-of-center third-party candidates Jill Stein and Cornel West, unlike RFK Jr., who draws evenly.

> Biden probably is hurt by the left-of-center third-party candidates Jill Stein and Cornel West.

<sub>2024-06-26_2024-presidential-election-model-methodology-update#14</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**adjustment rule** · 2024 presidential · explicit

In simulations where RFK Jr. is not on a state's ballot, the model backs out the third-party adjustment and reassigns his votes to Biden, Trump and 'other'. These ballot-access guesstimates are phased out as actual qualification becomes known.

> the model backs out the third-party adjustment as described above and reassigns RFK’s votes to Biden, Trump and “other” candidates

<sub>2024-06-26_2024-presidential-election-model-methodology-update#16</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**adjustment rule** · 2024 polling averages · explicit

The polling averages adjust for whether RFK Jr. is included in a poll. This adjustment has little effect on the Biden-Trump margin, somewhat contrary to conventional wisdom.

> the presence or absence of RFK Jr. in polls (this doesn’t have much effect, somewhat contrary to the conventional wisdom)

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#17</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**method** · 2024 presidential · explicit

Model simulations allow RFK Jr. to win some electoral votes, which can produce no-majority outcomes alongside 269-269 ties. The model considers it very, very unlikely he carries the Electoral College.

> The model does contemplate the possibility that Robert F. Kennedy, Jr. could win some electoral votes

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#30</sub>

### 2024-06-27 · [Are these guys trying to muddle through? Or playing to win?](https://www.natesilver.net/p/are-these-guys-trying-to-muddle-through)
**method** · 2024 presidential polling averages · inferred_from_chart

The Silver Bulletin national polling average tracks Robert F. Kennedy Jr. as a separate candidate alongside Trump and Biden. It had him at 7.6% on June 27, 2024, down from about 10-11% in early March 2024.

*Numbers:* RFK Jr. national average = 7.6 percent (June 27, 2024); RFK Jr. national average early March = ~10-11 percent (early March 2024, read from chart)

<sub>2024-06-27_are-these-guys-trying-to-muddle-through-or-playing-to-win#10</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**method** · 2024 presidential · explicit

Third-party vote shares in the Silver Bulletin presidential model are drawn from an asymmetric beta distribution. Most draws are low (RFK Jr. around 4%), with a right tail where the candidate catches fire.

*Numbers:* RFK Jr. typical projected vote share = 4 percent (July 2024, 'or something')

*Why:* Captures the historical possibility of third-party surges.

> Third-party outcomes are modeled with an asymmetric probability distribution called a beta distribution

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#22</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**data source** · 2024 presidential · explicit

The third-party distribution is empirically derived from the historical behavior of the third-party vote in both presidential and Senate races. Senate data is included because presidential years alone lack enough data for reliable priors.

*Why:* Presidential-only data is insufficient.

> there isn't enough data to form reliable priors from presidential years alone

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#23</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**parameter or number** · 2024 presidential · explicit

In July 2024 the model gave RFK Jr. about a 5% chance of surging enough to contend in a state or two (about 4% to win any electoral vote), almost no chance to contend nationally, and no more than about 1% in any individual state. These chances will fall unless he rises in the polls soon.

*Numbers:* chance RFK contends in a state or two = about 5 percent (July 2024); chance RFK wins any electoral vote = 4 percent (per reader's question, July 2024); max RFK win probability in any single state = about 1 percent (July 2024)

> his probability in any individual state isn't higher than about 1 percent right now — even though his chance of winning some vote somewhere is closer to 5 percent

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#24</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**adjustment rule** · 2024 presidential polling averages · explicit

The Silver Bulletin polling averages adjust polls for whether RFK Jr. was included as an option in the poll.

> the presence or absence of RFK Jr.

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#2</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**method** · 2024 presidential · inferred_from_chart

The 2024 model simulates uncertainty about RFK Jr.'s ballot access state by state. Kennedy's simulated vote share in Georgia and Arizona has a high probability mass at 0%, reflecting the chance he does not make the ballot there.

*Numbers:* Kennedy predicted national vote share = 4.3% percent (July 21, 2024 forecast, versus 8.0% in the national polling average)

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#10</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**empirical regularity** · 2024 presidential · inferred_from_chart

The 2024 model projects a third-party candidate's final vote share well below his current polling average: Kennedy was 8.0% in the national polling average but 4.3% in the predicted popular vote. This implies the model expects third-party support to fade.

*Numbers:* Kennedy national polling average = 8.0% percent (July 21, 2024); Kennedy predicted vote share = 4.3% percent (July 21, 2024)

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#11</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**method** · 2024 presidential · explicit

The Silver Bulletin presidential model has a special 'named third-party candidate' (N3PC) mode. For a designated N3PC the model explicitly forecasts the candidate's vote share, and the candidate is eligible to win electoral votes in the simulations.

> N3PC's receive special handling in the model: we explicitly forecast their vote share, and they're eligible to receive electoral votes.

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#0</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**adjustment rule** · 2024 presidential · explicit

Third-party adjustment: in N3PC mode, when a poll does not list the N3PC as an option, the Silver Bulletin presidential model extrapolates (imputes) the N3PC's vote share for that poll, allocating votes to him.

> extrapolates the N3PC's vote share in cases where a poll doesn't list him as an option

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#3</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**adjustment rule** · 2024 presidential · explicit

N3PC designation criterion 1 (described by Silver as admittedly somewhat arbitrary): the candidate is generally polling in the mid-single digits or higher.

*Numbers:* polling threshold for N3PC = mid-single digits or higher percent (general polling level required for N3PC status)

> Whether a candidate is generally polling in the mid-single digits or higher

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#5</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**adjustment rule** · 2024 presidential · explicit

N3PC designation criterion 2: the candidate is expected to qualify for the ballot in enough states that he could theoretically reach 270 electoral votes. Silver applies this by its spirit, so a candidate who exits swing-state ballots and endorses a rival fails it even if he technically meets it.

*Numbers:* electoral votes needed = 270 electoral votes (ballot access must make this theoretically reachable)

*Why:* You don't endorse another candidate and take yourself off swing-state ballots if you seriously want to contest the Electoral College.

> Whether the candidate is expected to qualify for the ballot in most states, enough that he could theoretically reach 270 electoral votes.

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#6</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**model change** · 2024 presidential · explicit

On Aug 24, 2024, the Silver Bulletin presidential model dropped RFK Jr. from N3PC status and lumped him in with 'other' candidates. This was implemented by changing a single cell in one spreadsheet, which implies N3PC status is a configuration flag.

*Why:* Simple is best under these circumstances. He no longer meets the N3PC criteria, and the change uses existing model logic.

> we've changed RFK's status in the model by changing a single cell in one spreadsheet

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#7</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**parameter or number** · 2024 presidential · explicit

After Kennedy's removal from N3PC status, the Silver Bulletin presidential model expects all candidates other than Harris and Trump combined, including Kennedy where he remains on the ballot, to get 1 to 2 percent of the vote on Nov. 5, 2024.

*Numbers:* projected combined 'other' vote = 1 to 2 percent (2024 general election, post-RFK withdrawal)

*Why:* Minor-party support in polls often doesn't translate to ballots.

> to get 1 to 2 percent of the vote combined on Nov. 5

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#8</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**empirical regularity** · 2024 presidential · explicit

Third-party candidates typically poll higher than their eventual vote share. In polls they might get 2 or 3 percent combined, but that support often doesn't materialize. Undecided voters park there, then stay home or switch to a major-party candidate in the booth. The model therefore projects 'other' below its polled level.

*Numbers:* typical combined third-party polling = 2 or 3 percent (when included in polls, 2024)

*Why:* Third-party options act as a 'Free Parking space' for actually undecided voters.

> empirically, support for minor parties in polls often doesn't translate to support on the ballot. Instead, they serve as a Free Parking space for voters who are actually undecided.

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#9</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**adjustment rule** · 2024 presidential · explicit

The Silver Bulletin presidential model gives minor candidates a lower vote projection in battleground states, reflecting tactical voting.

*Why:* Third-party candidates do worse in close elections, especially in swing states, because voters avoid protest votes when their ballot could matter.

> The model accounts for this: if you look carefully, minor candidates get a lower projection in battleground states.

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#10</sub>

### 2024-08-26 · [How big will the bounce be?](https://www.natesilver.net/p/how-big-will-the-bounce-be)
**interpretation guidance** · 2024 presidential · explicit

RFK Jr.'s exit, which coincided with the DNC, is expected to help Trump slightly. Because both events hit the polls simultaneously, Harris's convention bounce could look smaller than it otherwise would.

*Why:* Overlapping events confound the measured bounce.

> His exit will probably help Trump, but not by much.

<sub>2024-08-26_how-big-will-the-bounce-be-by-eli-mckown-dawson#15</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**parameter or number** · 2024 presidential · explicit

The model team initially expected RFK Jr.'s withdrawal to cost Harris 0.5 points or less, because Kennedy drew only slightly more Trump voters than Harris voters. Silver says the effect may be larger because Kennedy also endorsed Trump. The model was switched to an 'RFK-less version' after the dropout.

*Numbers:* expected net effect of RFK dropout on Harris margin = 0.5 points or less percentage points (Aug 2024)

> We initially expected this to hurt Harris by 0.5 points or less, given that RFK Jr. drew more Trump voters than Harris voters but only slightly more.

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#16</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**method** · 2024 presidential polling averages · explicit

Silver Bulletin polling averages make no assumptions about whether a minor candidate (RFK Jr.) is on the ballot. They use whatever numbers the pollster publishes. When a pollster releases multiple versions (e.g. with and without minor candidates), the versions are averaged together.

*Why:* Leaves ballot-composition judgments to pollsters.

> Our model uses whatever numbers the pollster chooses to publish and averages them together if there’s more than one version (e.g. with and without minor candidates).

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#4</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**model change** · 2024 presidential · explicit

After Robert F. Kennedy Jr. dropped out of the 2024 race, he was removed from the Silver Bulletin model. The last model run including him was Aug. 23, when Harris's national lead peaked at 4.3 points.

*Numbers:* Harris peak national lead = 4.3 percentage points (Aug. 23, 2024 run, last before RFK removal)

> Her lead peaked at 4.3 points on August 23 in our last model run before Robert F. Kennedy dropped out and we removed him from our model.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#5</sub>

### 2024-09-11 · [A guide to post-debate poll-watching](https://www.natesilver.net/p/a-guide-to-post-debate-poll-watching)
**parameter or number** · 2024 presidential · explicit

As of September 2024, Silver Bulletin data show a combined 95.4% of voters committed to Harris or Trump, leaving few undecided voters and limiting the potential size of bounces.

*Numbers:* Two-candidate committed share = 95.4 percent (September 2024)

> a combined 95.4 percent of voters are already committed to Harris or Trump.

<sub>2024-09-11_a-guide-to-post-debate-poll-watching-by-nate-silver#20</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**method** · 2024 Silver Bulletin polling averages · inferred_from_chart

The Silver Bulletin state polling averages tracked Robert F. Kennedy Jr. as a separate line, at roughly 2–8% depending on state. His line ends when he dropped out in late August 2024, and Harris and Trump numbers both rise afterward.

*Numbers:* Kennedy state polling share range = ~2-8 percent (July-August 2024 state averages)

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#10</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**adjustment rule** · 2024 presidential · inferred_from_chart

The Silver Bulletin forecast reallocates undecided and third-party votes to the major candidates. In Pennsylvania on Sept 26 the reallocation was equal, +1.6 points each.

*Numbers:* reallocation = +1.6/+1.6 percentage points (PA Sept 26 2024)

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#8</sub>

### 2024-10-08 · [55/45 is a really close race](https://www.natesilver.net/p/5545-is-a-really-close-race)
**method** · 2024 presidential · inferred_from_chart

The Silver Bulletin 2024 model forecast RFK Jr.'s popular vote at roughly 3-4% until he dropped out in late August. After his exit, both Harris and Trump's projected vote shares jumped (about 49 to 50.5 for Harris and 46.5 to 48 for Trump in the chart), meaning his support was reallocated to both.

*Numbers:* Kennedy projected vote before exit = ~3-4 percent (chart, July-Aug 2024)

<sub>2024-10-08_5545-is-a-really-close-race-by-nate-silver#11</sub>

### 2024-10-09 · [When you should panic about the polls](https://www.natesilver.net/p/when-you-should-panic-about-the-polls)
**data source** · 2024 presidential · explicit

Quinnipiac poll numbers cited in the article are from the versions that include third-party options; head-to-head versions differ slightly. This implies the version choice matters for poll inclusion in the averages.

> These numbers are from the versions where voters are given the option of third-party candidates; the numbers vary slightly in the head-to-head versions.

<sub>2024-10-09_when-you-should-panic-about-the-polls-by-nate-silver#13</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**adjustment rule** · 2024 presidential · inferred_from_chart

In the 2024 Silver Bulletin model, undecided and third-party vote is reallocated to the major candidates. In the final Arizona forecast, Harris and Trump each received +1.4 points, an equal split, taking them from 46.9/49.3 to 48.3/50.7.

*Numbers:* reallocation to each candidate, AZ = +1.4 percentage points (final forecast); AZ polling average = 46.9% Harris / 49.3% Trump vote share (final)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#14</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**empirical regularity** · 2024 presidential · inferred_from_chart

The final 2024 Silver Bulletin projected national margin (Harris 50.5 to 48.4, about D+2.1) is larger than the national polling average (48.6 to 47.6, D+1). This suggests that undecided/third-party reallocation and other pipeline steps change the margin, not just the levels.

*Numbers:* national polling average = 48.6% Harris / 47.6% Trump vote share (final)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#23</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**method** · 2024 presidential · inferred_from_chart

The Silver Bulletin national polling average and forecast tracked Robert F. Kennedy Jr. as a third candidate until he dropped out in late August 2024. His average fell from about 15% in June to about 4%.

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#32</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**model change** · 538 2016 · explicit

In 2016 the model added several procedures for handling third-party candidates, prompted by Gary Johnson's initially strong polling. The 'polls-only' version of the model was also introduced that year.

*Why:* Gary Johnson initially polled fairly well in 2016.

> In 2016, we introduced several procedures for handling third-party candidates (since Gary Johnson initially polled fairly well that year) and the “polls-only” version of the model.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#4</sub>

### 2026-03-23 · [SBSQ #30: Will liberals turn against sports betting?](https://www.natesilver.net/p/sbsq-30-will-liberals-turn-against)
**empirical regularity** · empirical observation · explicit

In multi-candidate primaries, second-tier candidates tend to underperform their polls on Election Day while leaders outperform. In the 2025 NYC Democratic mayoral primary, Mamdani and Lander beat their polling averages, Cuomo roughly matched his, and Adams, Stringer and other second-tier candidates considerably underperformed.

*Why:* Strategic voting against wasted votes by high-information primary voters.

> But all of the second-tier Democrats — Adrianne Adams, Scott Stringer and so forth — considerably underperformed their polls on Election Day.

<sub>2026-03-23_sbsq-30-will-liberals-turn-against-sports-betting#7</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

For races with prominent independent candidates, FLIPR simulates the independent's vote share with a right-tailed distribution: usually not close, with an outside chance of real momentum. Independents who are de facto partisans, such as Dan Osborn in Nebraska or Bernie Sanders, are treated as members of that party.

> FLIPR simulates the independent’s vote share using a right-tailed statistical distribution

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#39</sub>

### 2026-08-15 · [A tour of the 7 key Senate races](https://www.natesilver.net/p/a-tour-of-the-7-key-senate-races)
**method** · FLIPR 2026 · explicit

FLIPR treats Dan Osborn in Nebraska, technically an independent but the only major candidate against Republican Pete Ricketts, as a de facto Democrat.

> FLIPR treats him as a de facto Democrat

<sub>2026-08-15_a-tour-of-the-7-key-senate-races-by-eli-mckown-dawson#14</sub>

### 2026-10-17 · [The good, bad and ugly outcomes in the Senate](https://www.natesilver.net/p/the-good-bad-and-ugly-outcomes-in)
**method** · FLIPR 2026 · explicit

FLIPR counts certain independents toward Democratic control, such as Seth Bodnar in Montana.

> More likely in the form of independent Seth Bodnar — whom FLIPR counts toward Democratic control

<sub>2026-10-17_the-good-bad-and-ugly-outcomes-in-the-senate#10</sub>

### 2026-10-25 · [Let’s talk shop about every Senate race](https://www.natesilver.net/p/lets-talk-shop-about-every-senate)
**method** · FLIPR 2026 · explicit

FLIPR assumes independents Dan Osborn (Nebraska) and Seth Bodnar (Montana) would caucus with Democrats. Third-party candidates get asymmetric, feast-or-famine distributions. In Montana, a three-way race with a Democrat taking 22.5 percent, the forecast is assumption-driven and volatile, hinging on tactical voting.

*Numbers:* Bankhead projected share = 22.5 percent (Montana Senate, Oct 2026); Alme projected margin over Bodnar = 8 points (Oct 2026)

> FLIPR builds in some slightly complex assumptions about third-party candidates in cases like this, seeing them as having asymmetric distributions that are a little bit feast-or-famine.

<sub>2026-10-25_lets-talk-shop-about-every-senate-race-by-nate-silver#11</sub>
