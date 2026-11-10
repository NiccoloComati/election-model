# Data sources and poll inclusion

116 findings from 58 articles, oldest first.

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**design principle** · FiveThirtyEight 2016 presidential · explicit

All versions of the model gain more information from state polls than from national polls. National polls mainly help calibrate the trend-line and house-effects adjustments and contribute, with state polls, to the national popular vote estimate.

> All versions of our models gain more information from state polls than from national polls.

<sub>fte_2016-general-election-forecast-users-guide#2</sub>

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**method** · FiveThirtyEight 2016 presidential · explicit

2016 poll inclusion excluded polls conducted directly for a presidential campaign or affiliated PAC or super PAC, as well as banned pollsters. Polls are listed by polling company, not media sponsor. Version priority was likely voters, then registered voters, then adults; the version including Johnson was preferred; other ambiguous cases, such as multiple LV models, are averaged.

> We prioritize polls as follows: likely voters > registered voters > all adults.

<sub>fte_2016-general-election-forecast-users-guide#3</sub>

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**method** · FiveThirtyEight midterm models · explicit

The midterm models use almost all polls, including partisan and campaign polls, which make up about half of House district polling. Polls are excluded for veracity concerns or known fakers, DIY hobbyist polls on platforms like Google Surveys, subsamples of multistate polls unless conditions are met, and MRP or other blended or smoothed outputs, because FiveThirtyEight wants to do the blending itself.

*Numbers:* partisan share of House district polling = something like half share (2018)

> We want to do the blending and smoothing ourselves rather than inputting other people’s models into ours.

<sub>fte_midterm-house-senate-governor-methodology#8</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

National polls play relatively little role in the 2020 FiveThirtyEight presidential forecast beyond the trend-line adjustment. The national snapshot is the sum of the state snapshots weighted by projected turnout, based on population growth since 2016, voting-ease changes and current closeness, since closer states have higher turnout. National polls are not used in it.

> National polls are not used in the national snapshot; it’s simply a summation of the snapshots in the 50 states and Washington, D.C.

<sub>fte_2020-presidential-forecast-methodology#13</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**design principle** · general principle · explicit

Silver holds that pollsters should not be excluded from polling averages on the basis of an ideological or political litmus test, such as their relationships with partisan media outlets. Exclusion, if any, should rest on methodology or track record.

*Why:* Many pollsters hold strong political opinions and are friendly with operatives, and some poll for campaigns. Applying a political-relationship standard would wipe out dozens of pollsters and would likely be applied asymmetrically.

> I strongly oppose subjecting pollsters to an ideological or political litmus test. Look, there might be good reasons to exclude Rasmussen based on their methodology

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#0</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**design principle** · FiveThirtyEight (Silver era) / general principle · explicit

A polling average needs a consistent, legible set of inclusion rules that can be applied to the hundreds of pollsters encountered over an election campaign. Silver includes pollsters he subjectively dislikes, politically or methodologically, for the sake of consistency.

*Numbers:* number of pollsters encountered = hundreds pollsters (Over the course of a US election campaign); Silver's experience = 15 years (Years running polling averages and models)

*Why:* Case-by-case decisions are extremely time-consuming mid-campaign. They are also highly likely to introduce the modeler's own biases, whether rooting for a political outcome or wanting the model to look smart.

> you need a consistent and legible set of rules that be applied to hundreds of pollsters you'll encounter over the course of an election campaign.

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#9</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**limitation or failure mode** · general principle · explicit

Ad hoc, case-by-case exclusion of pollsters risks the modeler injecting bias, either toward a preferred political outcome or toward whatever will make the model look smart.

*Why:* Subjective judgments are not consistent across pollsters.

> highly likely to result in introducing your own biases, whether it's the political outcome you're rooting for or whatever you think will make your model look smart.

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#10</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**critique of other approach** · FiveThirtyEight (2024, Morris era) · explicit

Silver criticizes the post-2023 ABC News/FiveThirtyEight approach under G. Elliott Morris. It threatened to ban Rasmussen from all aggregation and forecasting models, the polls page, historical averages and pollster ratings unless Rasmussen answered questions about its political relationships and detailed methodology. Silver calls this an ad hoc exclusion effort rather than a consistent standard.

*Numbers:* response window given to Rasmussen = a day-and-a-half days (Just before a four-day summer weekend)

*Why:* The methodological questions were nitpicks that could be asked of almost any pollster, such as Quinnipiac. They demanded more disclosure than pollsters typically provide.

> I think it's clear that the letter is an ad hoc exercise to exclude Rasmussen, not an effort to develop a consistent set of standards.

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#11</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**interpretation guidance** · general principle · explicit

Silver views vague pollster methodology statements as normal and benign, such as weighting by 'age, race, gender, political party, and other factors'. Commercial pollsters may legitimately keep weighting algorithms proprietary, so missing detailed disclosure of randomization or weighting should not by itself justify exclusion.

*Why:* Such disclosure goes well beyond what pollsters typically provide.

> a commercial polling organization would be within its rights to keep some of the details of its weighting algorithms proprietary.

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#12</sub>

### 2023-09-18 · [Is a Trump-Biden rematch inevitable?](https://www.natesilver.net/p/is-a-trump-biden-rematch-inevitable)
**data source** · FiveThirtyEight 2023 / RCP · explicit

FiveThirtyEight (2023) dropped Marianne Williamson from its Democratic primary polling averages, so Silver used RCP's average instead. Per the RCP chart, the average was Biden 66.7, Kennedy 11.9, and Williamson 5.6.

*Numbers:* Biden RCP = 66.7 percent (Dem primary, Sept 2023); Kennedy RCP = 11.9 percent; Williamson RCP = 5.6 percent

> FiveThirtyEight actually dropped Williamson from their polling averages, so here are the RCP numbers instead

<sub>2023-09-18_is-a-trump-biden-rematch-inevitable-by-nate-silver#11</sub>

### 2023-09-18 · [Is a Trump-Biden rematch inevitable?](https://www.natesilver.net/p/is-a-trump-biden-rematch-inevitable)
**interpretation guidance** · general principle · explicit

Silver says survey responses wanting 'a different candidate' should be discounted when there is no consensus alternative. In the CNN poll, two-thirds of Democrats wanted someone else, but 82% of them wanted 'just someone besides Joe Biden'; no named alternative exceeded 3%.

*Numbers:* Dems wanting different candidate = two-thirds (CNN poll Aug 25-31 2023); just someone besides Biden = 82 percent (n=258); top named alternative = 3 percent (Sanders, Buttigieg)

*Why:* Generic dissatisfaction doesn't translate into support for a viable challenger.

> there is absolutely no consensus on who this “different candidate” might be

<sub>2023-09-18_is-a-trump-biden-rematch-inevitable-by-nate-silver#14</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**adjustment rule** · 538 pollster accuracy database · inferred_from_chart

For presidential primary polling-error calculations, FiveThirtyEight excludes the following polls: New Hampshire primary polls taken before the Iowa caucuses; other states' primary polls taken before the New Hampshire primary; polls where the leader or runner-up dropped out before the primary; polls where any candidate receiving at least 15% dropped out; and polls where any combination of candidates receiving at least 25% dropped out.

*Numbers:* single dropout threshold = 15 percent (poll excluded if a candidate at or above this share dropped out); combined dropout threshold = 25 percent (poll excluded if dropped-out candidates combined reach this share)

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#4</sub>

### 2024-03-05 · [The White House is betting the election on a theory of skewed polls 🚩🚩🚩🚩🚩](https://www.natesilver.net/p/the-white-house-is-betting-the-election)
**interpretation guidance** · general principle · explicit

Special and off-year elections, such as the 2023 races, are low-turnout contests that may say little about a presidential general election, especially when the president is not on the ballot. The NYT poll replicated Democrats' strong performance in such contests while still showing Biden trailing Trump.

*Why:* Voter concerns specific to Biden, such as his age, would not show up in races where he is not on the ballot.

> it's not clear how much one should take away from these low-turnout races.

<sub>2024-03-05_the-white-house-is-betting-the-election-on-a-theory-of-skewed-polls#10</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**adjustment rule** · 2024 polling averages · inferred_from_chart

The state polling-average table shows only contests surveyed by at least three distinct pollsters or with at least five polls. 'Week change' compares with the average seven days earlier, and 'month change' compares with thirty days earlier.

*Numbers:* min distinct pollsters = 3 pollsters (display threshold); min polls = 5 polls (display threshold); week change lookback = 7 days (table); month change lookback = 30 days (table)

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#21</sub>

### 2024-06-27 · [Are these guys trying to muddle through? Or playing to win?](https://www.natesilver.net/p/are-these-guys-trying-to-muddle-through)
**data source** · 2024 presidential polling averages · inferred_from_chart

In June 2024, Silver Bulletin published polling averages for the national race and 12 states: AZ, FL, GA, MI, MN, NV, NH, NC, PA, TX, VA and WI.

*Numbers:* states with published averages = 12 states (June 2024 interactive (AZ, FL, GA, MI, MN, NV, NH, NC, PA, TX, VA, WI))

<sub>2024-06-27_are-these-guys-trying-to-muddle-through-or-playing-to-win#12</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**data source** · 2024 presidential polling averages · inferred_from_chart

The poll database labels each poll's population as LV (likely voters), RV (registered voters), V (voters), or A (U.S. adults).

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#17</sub>

### 2024-07-29 · [kamala_mode will be activated tomorrow](https://www.natesilver.net/p/kamala_mode-will-be-activated-tomorrow)
**adjustment rule** · 2024 presidential · explicit

kamala_mode includes adjustments to account for the scarcity of Harris-vs-Trump polling before the June 27, 2024 debate. Pollsters had tested that matchup only periodically before then. The exact adjustment is described in a separate methodology update.

*Numbers:* debate date after which Harris-Trump polling became more common = June 27 date (2024)

*Why:* There wasn't much Harris-Trump polling until the debate.

> we need to make some adjustments to account for the fact that there wasn’t much Harris-Trump polling until the debate occurred on June 27

<sub>2024-07-29_kamala-mode-will-be-activated-tomorrow-by-nate-silver#2</sub>

### 2024-07-29 · [kamala_mode will be activated tomorrow](https://www.natesilver.net/p/kamala_mode-will-be-activated-tomorrow)
**data source** · 2024 presidential · inferred_from_chart

The code screenshot shows flags process_cces_data="no" and compress_sample_size="yes". This suggests the model uses CCES (Cooperative Election Study) data, preprocessed separately, and has an option that compresses poll sample sizes, presumably capping the effective weight of large samples.

<sub>2024-07-29_kamala-mode-will-be-activated-tomorrow-by-nate-silver#11</sub>

### 2024-07-29 · [kamala_mode will be activated tomorrow](https://www.natesilver.net/p/kamala_mode-will-be-activated-tomorrow)
**parameter or number** · 2024 presidential · inferred_from_chart

The code screenshot shows scalar create_date_cutoff=23585. This is likely a Stata date value; 23585 days after Jan 1, 1960 corresponds to around July 29, 2024.

*Numbers:* create_date_cutoff = 23585 Stata date (model code July 2024)

<sub>2024-07-29_kamala-mode-will-be-activated-tomorrow-by-nate-silver#12</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**parameter or number** · 2024 presidential · explicit

By default, the Silver Bulletin presidential model uses polls going back one year before the election. For 2024 that meant polls dating back to November 5, 2023.

*Numbers:* poll lookback window = 1 year (default cutoff before Election Day); default cutoff date 2024 = November 5, 2023 date (2024 presidential)

> Usually, the model uses polling going back a year before the election — meaning, dating back to November 5, 2023 in this case.

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#1</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**data source** · 2024 presidential · explicit

Silver Bulletin uses the 538 polling database, which Silver helped design, as a starting point. It adds a supplementary database of polls 538 lacks or that Silver Bulletin catches faster, and keeps a strike list of polls deleted from 538's data.

*Why:* There is no point duplicating the work, but inclusion standards differ.

> we maintain a supplementary polling database of polls that we use that they don't, as well as a strike list of polls we delete from their data

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#29</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**adjustment rule** · 2024 presidential · explicit

Silver Bulletin removed SoCal Research polls, which 538 uses, under a longstanding Silver-era FiveThirtyEight rule against amateur/DIY polling.

*Why:* Longstanding rule.

> We're now removing one pollster that 538 uses because it violates a longstanding rule from the Nate days of FiveThirtyEight of not using amateur/DIY polling.

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#30</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**method** · 2024 presidential · explicit

Poll version selection: when a designated N3PC is in the race, the Silver Bulletin presidential model defaults toward the multiway-ballot version of a poll rather than the head-to-head version.

> When there's an N3PC in the race, the model defaults toward using the multiway version

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#2</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**method** · 2024 presidential · explicit

When there is no designated N3PC, the Silver Bulletin presidential model averages all available versions of a poll (head-to-head and multiway) together instead of preferring one version.

> If there isn't a designated N3PC, it averages all available versions of the survey together instead.

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#4</sub>

### 2024-08-26 · [How big will the bounce be?](https://www.natesilver.net/p/how-big-will-the-bounce-be)
**limitation or failure mode** · general principle · explicit

Polls asking how respondents would react to hypothetical events are unreliable. Hypothetical polls suggested Trump would lose about 5 points if convicted, but he dropped only a little more than half a point in the Silver Bulletin national average.

*Numbers:* hypothetical conviction effect = about 5 points (hypothetical polls); actual conviction effect = a little more than half a point points (Silver Bulletin national average)

> you should be skeptical about polls that ask people how they would react to hypothetical events

<sub>2024-08-26_how-big-will-the-bounce-be-by-eli-mckown-dawson#16</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**interpretation guidance** · 2024 presidential · explicit

A large split in results between pollster methodologies (e.g. phone vs. online) would be a warning sign of polling error. Its absence in 2024 is mildly reassuring.

> if phone pollsters said one thing, and online pollsters said another, that might be more of a cause for concern

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#36</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**method** · Silver Bulletin polling averages 2024 · inferred_from_chart

The state polling averages table shows only contests surveyed by at least three distinct pollsters or with at least five polls.

*Numbers:* min distinct pollsters = 3 pollsters (display threshold); min polls = 5 polls (display threshold)

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#19</sub>

### 2024-09-06 · [The Electoral College bias has returned with a vengeance](https://www.natesilver.net/p/the-electoral-college-bias-has-returned)
**data source** · 2024 presidential polling averages · explicit

As of Sept. 2024, Silver Bulletin excludes polls from ActiVote, Big Data Poll, SoCal Polling and Quantus, all of which 538 used. It includes Rasmussen Reports, which 538 excludes. Silver describes Silver Bulletin as more restrictive than 538 overall.

> We don’t use polls from ActiVote, Big Data Poll, SoCal Polling and Quantus — but we do use polls from Rasmussen Reports, which they don’t.

<sub>2024-09-06_the-electoral-college-bias-has-returned-with-a-vengeance#7</sub>

### 2024-09-19 · [Don't let randomness make a fool of you](https://www.natesilver.net/p/dont-let-randomness-make-a-fool-of)
**limitation or failure mode** · general principle · explicit

In practice, pollsters herd toward the consensus and suppress outlier results. As a result, the published spread of polls is narrower than pure sampling error would produce.

> In practice, pollsters tend to herd toward the consensus and suppress outlier results.

<sub>2024-09-19_dont-let-randomness-make-a-fool-of-you-by-nate-silver#6</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**method** · 2024 Silver Bulletin polling averages · inferred_from_chart

The Silver Bulletin 2024 polling tables include polls of likely voters (LV), registered voters (RV), voters (V) and U.S. adults (A), labeled by population, and show each poll's influence on the average. For example, a Patriot Polling RV poll in Nevada appears alongside LV polls. The tables show the head-to-head Harris vs. Trump numbers.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#9</sub>

### 2024-09-21 · [A tour of the 7½ key swing states](https://www.natesilver.net/p/a-tour-of-the-7-key-swing-states)
**interpretation guidance** · 2024 presidential · implied

Silver wants more polls in sparsely polled states (Arizona, Alaska, Iowa) to help calibrate the forecast. This implies forecast uncertainty and reliance on non-poll factors are greater where polling is thin.

> this is another state where I wouldn't mind seeing another poll just to help calibrate the forecast.

<sub>2024-09-21_a-tour-of-the-7½-key-swing-states-by-nate-silver#22</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**design principle** · general principle · explicit

Anyone building a polling average must publicly specify the inclusion and weighting rules ahead of time, so that choices are consistent rather than driven by ad hoc vibes or partisan preference.

*Why:* Consistency prevents cherry-picking.

> you have to publicly specify the rules ahead of time

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#11</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**limitation or failure mode** · 2024 presidential · explicit

In 2024 the most populous blue states without any polls were New Jersey and Illinois. Unlike some past years, no pollster had yet run a 50-state survey, so the model relied on imputation for these states.

> usually, some brave pollster has conducted a 50-state survey by now

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#10</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**adjustment rule** · Silver Bulletin polling averages 2024 · inferred_from_chart

The Silver Bulletin polling average table shows only contests surveyed by at least three distinct pollsters or with at least five polls.

*Numbers:* min distinct pollsters = 3 pollsters (display threshold); min polls = 5 polls (display threshold)

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#11</sub>

### 2024-09-27 · [Which polls are biased toward Harris or Trump?](https://www.natesilver.net/p/which-polls-are-biased-toward-harris)
**design principle** · 2024 presidential · explicit

Seeming outlier polls are kept rather than discarded, because they can give critical clues about how the race is trending. Only consistent leans are adjusted, via house effects.

> Even seeming "outlier" polls can provide critical clues as to how the race is trending. But if a pollster consistently leans toward Trump or Harris, we adjust

<sub>2024-09-27_which-polls-are-biased-toward-harris-or-trump#23</sub>

### 2024-10-01 · [SBSQ #13: October Surprise edition](https://www.natesilver.net/p/sbsq-13-october-surprise-edition)
**limitation or failure mode** · 2024 presidential · explicit

Silver is skeptical of polls from North Carolina and Georgia conducted in the days right after Hurricane Helene, when power and basic services were knocked out in many places. This implies polls fielded during disaster disruption may be unreliable.

*Why:* Disrupted infrastructure likely compromises sampling.

> I'm not sure I'd really trust polls from these states conducted over the past several days with power and other basic services knocked out in so many places.

<sub>2024-10-01_sbsq-13-october-surprise-edition-by-nate-silver#11</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**method** · Silver Bulletin polling averages 2024 · explicit

Internal polls that campaigns release publicly are included in the Silver Bulletin polling database and averages, provided the campaign discloses the basic descriptive information aggregators require, such as field dates and sample sizes.

> When campaigns disclose the basic descriptive information that polling aggregators require — field dates, sample sizes, and so on — these surveys are included in polling databases, including Silver Bulletin's.

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#0</sub>

### 2024-10-10 · [Why you should mostly ignore "internal polls"](https://www.natesilver.net/p/why-you-should-mostly-ignore-internal)
**assumption** · general principle · explicit

Genuine internal polls may hold some real informational advantages over public polls, such as proprietary data mining of campaign contacts and possibly better pollster talent, since the money in polling is on the campaign side.

> Campaigns have access to proprietary information that public pollsters lack, like data mining they've done based on campaign contacts.

<sub>2024-10-10_why-you-should-mostly-ignore-internal-polls#11</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**parameter or number** · 2024 presidential · explicit

For this analysis, Silver treats a state as having 'enough' polling if it has at least 5 polls from at least 3 distinct polling firms, or if the polling average makes up at least 65 percent of the state forecast rather than the regression-based estimate.

*Numbers:* minimum polls = 5 polls (enough-polling threshold); minimum distinct firms = 3 polling firms (enough-polling threshold); polling-average share threshold = 65 percent (alternative threshold: share of state forecast from the polling average)

*Why:* Limits the comparison to states where the polling data is reasonably robust.

> defined as either 5 polls from 3 distinct polling firms or at least 65 percent of our forecast in the state being made up of polling averages

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#1</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**limitation or failure mode** · general principle · explicit

Group-level vote estimates (by race) are never hard evidence. They rely on exit polls and ecological inference, both subject to error, and sources differ. For example, Biden's 2020 Latino margin was 28 points per AP VoteCast and 26 points per Catalist. Catalist generally works for Democratic clients.

*Numbers:* Biden Latino margin 2020 (VoteCast) = 28 points (2020); Biden Latino margin 2020 (Catalist) = 26 points (2020)

> there's never any hard evidence of how any racial group votes — we have to rely on exit polls and ecological inference

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#15</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**method** · 2024 presidential · explicit

The Silver Bulletin includes Rasmussen Reports and Trafalgar polls rather than excluding them, but automatically designates them as Republican partisan polls, which subjects them to partisan-poll treatment.

> Split Ticket excludes Rasmussen Reports and Trafalgar; we include them, but automatically designate them as Republican partisan polls.

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#2</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**data source** · 2024 presidential · explicit

The Silver Bulletin average does not use polls from Big Data Poll, Quantus, SoCal Data or ActiVote, whereas 538's 2024 average does use them.

> 538 uses polls from Big Data Poll, Quantus and SoCal Data and ActiVote but we don't.

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#3</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**critique of other approach** · general principle · explicit

Inclusion philosophies differ across 2024 averages: Split Ticket excludes Rasmussen and Trafalgar, VoteHub uses only high-quality nonpartisan polls, and 538 includes some firms the Silver Bulletin excludes. Because all of them weight and adjust reasonably, they converge to about the same result.

*Why:* Reasonable weighting and adjustment matter more than which polls are included or excluded.

> because we're all weighting and adjusting the polls in reasonable ways, we all end up in about the same place.

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#4</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**empirical regularity** · 2024 presidential · explicit

In a simple flat average of October 2024 national presidential polls, all polls showed Harris +3.0. Polls from Rosenberg-listed Republican-leaning firms showed Harris +2.0, and the remaining polls showed Harris +3.4. Republican-leaning firms were therefore 1.4 points more Trump-favorable than other firms, and 1.0 point more than the all-poll average.

*Numbers:* all polls margin = D+3.0 percentage points (October 2024 national, flat average); Republican-leaning margin = D+2.0 percentage points (October 2024 national); non-Republican-leaning margin = D+3.4 percentage points (October 2024 national); R-leaning vs non-R-leaning gap = R+1.4 percentage points (October 2024 national); all vs R-leaning gap = R+1.0 percentage points (October 2024 national)

*Why:* Without quality weighting and house effect adjustment, these firms could push averages rightward.

> Harris is ahead by 3.0 points nationally in this simple average. But when you look at only Republican-aligned firms, she's up by only 2.0 points.

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#7</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**empirical regularity** · 2024 presidential · explicit

Restricting the Silver Bulletin national polling average to pollsters rated at least B- by Race to the White House (VoteHub's rule) and dropping all partisan polls changed the Harris lead little:
- National: from 2.8 to 2.6 points.
- Pennsylvania: Harris lead fell by 0.1 point.
- Wisconsin: Trump gained 0.2 points.

*Numbers:* full national lead = 2.8 percentage points (Oct 15 2024); high-quality-only national lead = 2.6 percentage points (Oct 15 2024); PA change = -0.1 percentage points (Harris lead); WI Trump gain = 0.2 percentage points (high-quality only); rating threshold = B- rating (Race to the White House pollster rating)

> If we only include pollsters rated at least B- by VoteHub (they use pollster ratings from Race to the White House) and remove all partisan polls, her lead drops to 2.6 points.

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#9</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**design principle** · general principle · explicit

Silver Bulletin considers it indefensible to exclude polls because they show results favorable to one candidate. Trump-leaning results can reflect legitimate methodological differences, so the right response is adjustment rather than cherry-picked exclusion.

*Why:* Polling is hard, and there is room for legitimate differences in methodology.

> If you just lop off every poll that shows nice numbers for Trump, then of course the forecast would shift toward Harris, but that isn't a defensible practice.

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#14</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**critique of other approach** · 2024 presidential · explicit

Silver Bulletin criticizes Simon Rosenberg's list of 27 'Republican-aligned' pollsters as cherry-picking. Some firms on it, such as Echelon Insights, are high quality and rate well in the Silver Bulletin and 538 ratings, and some have no official or unofficial tie to the GOP.

*Numbers:* Rosenberg-listed pollsters = 27 pollsters (2024 cycle)

> We suspect Rosenberg doesn't like them simply because they tend to show Trump-leaning results

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#15</sub>

### 2024-10-16 · [Are Republican pollsters “flooding the zone?”](https://www.natesilver.net/p/are-republican-pollsters-flooding)
**limitation or failure mode** · general principle · explicit

Campaign internal polls, such as Trump's internals showing a surge, are treated as not particularly informative.

> as his — not particularly informative — internal polls suggest

<sub>2024-10-16_are-republican-pollsters-flooding-the-zone#17</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**limitation or failure mode** · general principle · explicit

Pollster herding can create artificial momentum. Mediocre pollsters may publish more favorable numbers for a candidate who is perceived to be on an upswing, or tinker with their turnout model until results match the perceived narrative.

*Numbers:* example = Trump +4 vs. tie percentage points (Hypothetical Pennsylvania result depending on the perceived narrative)

*Why:* What matters in the end is votes, not polls.

> mediocre pollsters may decide it’s safe to publish more favorable numbers for a candidate when he’s in the midst of a favorable news cycle

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#16</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**limitation or failure mode** · 2024 presidential · explicit

Pollsters may herd toward other polls or decline to publish outliers. In 2024 a conspicuously large number of swing-state polls showed margins within 2 points either way, and almost nobody except maybe NYT/Siena published results like Trump +5 or Harris +6.

*Numbers:* herding band = 2 points (conspicuously many swing-state polls within ±2)

*Why:* Pollsters are influenced by vibes and the media narrative.

> a conspicuously large number of polls in this race show the swing states within 2 points in either direction

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#15</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**limitation or failure mode** · 2024 presidential · explicit

State-level LV/RV comparisons rest on small samples. For example, the Silver Bulletin database had only 10 Michigan polls that published both LV and RV numbers, so state-specific gaps should not be over-interpreted.

*Numbers:* Michigan paired LV/RV polls = 10 polls (Silver Bulletin database as of Oct 24, 2024)

> in Michigan, there are 10 polls in our database that published both LV and RV numbers. That isn't nothing, but it isn't a huge sample either.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#8</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**design principle** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model does not use early-vote data (party breakdowns of early ballots) as an input to its vote-share forecast. Silver doubts that early voting could add much value even with a lot of effort.

*Why:* There are no good baselines, polls already capture early voting, vote choice is unknown, and early-vote-based predictions have a poor track record.

> when people ask me how early voting is incorporated into the model, the answer is that (with one extremely minor exception) it isn't

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#0</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**design principle** · general principle · explicit

Sample size does not fix a biased sample. The 1936 Literary Digest poll of almost 2.3 million voters showed Landon beating Roosevelt 57-43, but Roosevelt won by 24, a 38-point error. Its sample was drawn from lists of telephone and automobile owners, who skewed rich and Republican.

*Numbers:* Literary Digest sample = almost 2.3 million voters (1936); polling error = 38 points (1936 Literary Digest); Roosevelt margin = 24 points (1936)

*Why:* If you're aiming at the wrong target, more respondents don't improve accuracy.

> If you're aiming at the wrong target, it doesn't matter how many people you poll — it won't get any more accurate.

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#5</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**assumption** · 2024 presidential · explicit

Early-vote information is already captured by polls, because pollsters ask respondents whether they have already voted and combine early voters with likely voters who have yet to vote. A poll-based model therefore implicitly includes it. CNN's 2024 polls illustrate this. In Nevada, Trump led early voters by 6 but the topline was Trump +1. In Arizona, Harris led early voters by 9 but the topline was Harris +1.

*Numbers:* CNN Nevada topline = Trump +1 points (Oct 2024); CNN Nevada early voters = Trump +6 points (Oct 2024); CNN Arizona early voters = Harris +9 points (Oct 2024); CNN Arizona topline = Harris +1 points (Oct 2024)

> pollsters, who are fully aware of what the early voting data says in Nevada and ask respondents if they already voted, continue to show the race tied.

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#8</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**method** · 2024 presidential / Silver Bulletin polling averages · explicit

When a poll releases versions with and without third-party candidates, Silver Bulletin averages the versions together into a single result. This produces fractional margins: for example, Harris +2 in the version with third parties and Harris +1 without them is recorded as Harris +1.5.

*Numbers:* example averaged margin = 1.5 percentage points (average of +2 (with third parties) and +1 (without))

> some polls release results both with and without third-party candidates, in which case we just average the different versions together

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#4</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**data source** · 2024 presidential · explicit

The Silver Bulletin poll database applies inclusion standards. As of Nov 1, 2024, it contained 249 polls in the seven battleground states that met those standards and had at least some October fieldwork.

*Numbers:* qualifying October swing-state polls = 249 polls (as of Nov 1, 2024)

> there were 249 polls in the seven battleground states that met Silver Bulletin standards and did at least some of their fieldwork in October

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#6</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**parameter or number** · 2024 presidential · explicit

The median sample size of October 2024 swing-state polls was 800. The smallest was 400 and the largest 5,686, and most fell between 600 and 1,200. Collectively, October swing-state polls surveyed about 230,000 voters.

*Numbers:* median sample = 800 voters (Oct 2024 swing-state polls); min sample = 400 voters; max sample = 5686 voters; typical range = 600-1200 voters; total surveyed = about 230,000 voters (past month, swing states)

*Why:* Averaging many polls greatly increases the effective sample size relative to any individual poll.

> Collectively, they’ve surveyed about 230,000 voters.

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#8</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**limitation or failure mode** · 2024 presidential · explicit

On Nov 2, 2024, the final round of AtlasIntel polls (a highly rated pollster with bearish numbers for Harris) entered the Silver Bulletin database just before the model run. These polls offset what might otherwise have been a decent update toward Harris. Silver says the model should in future (2026/2028) show which surveys are new since the last update.

*Why:* Transparency about which new polls drive each update.

> Absent those, the model might have updated a decent amount to Harris.

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#21</sub>

### 2024-11-04 · [The polls are close, but that doesn’t mean the results will be](https://www.natesilver.net/p/the-polls-are-close-but-that-doesnt)
**parameter or number** · 2024 presidential · explicit

As of Nov 3, 2024, 43 states had at least one poll meeting Silver Bulletin standards for inclusion in the presidential model.

*Numbers:* States with at least one qualifying poll = 43 states (Nov 3, 2024)

> We're up to 43 states with at least one poll that meets our standards.

<sub>2024-11-03_the-polls-are-close-but-that-doesnt-mean-the-results-will-be#1</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**limitation or failure mode** · 2024 presidential · explicit

Late polling may lag real movement because most pollsters conducted their final interviews the week before the election and published over the final weekend. Silver guesses that fresh high-quality polls fielded that weekend would have shown Harris at about 52-53%.

*Numbers:* Silver's guessed Harris probability = 52 or 53 percent (if fresh polls had been fielded)

> most pollsters did their final interviews last week and then published their numbers this weekend and closed up shop

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#15</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**design principle** · general principle · explicit

Silver does not trust gut feelings, early voting data, or rumors of internal polls as election indicators, saying people tend to overweight them.

> I also don't really believe in indicators like early voting or rumors of internal polls that people tend to overweight.

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#20</sub>

### 2024-11-05 · [A random number generator determined the “favorite" in our forecast](https://www.natesilver.net/p/a-random-number-generator-determined)
**empirical regularity** · 2024 polling database · explicit

Many if not most polls in the Silver Bulletin database are conducted online or by other non-phone means. Landline calling is barely needed anymore.

> many if not most of the polls in our database are conducted by the Internet or other means.

<sub>2024-11-05_a-random-number-generator-determined-the-favorite-in-our-forecast#25</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**adjustment rule** · Silver Bulletin polling averages 2024 · inferred_from_chart

The Silver Bulletin polling-average table only displays contests surveyed by at least three distinct pollsters or with at least five polls. Week and month changes compare against the averages 7 and 30 days before the latest update.

*Numbers:* minimum distinct pollsters = 3 pollsters (display threshold); minimum polls = 5 polls (display threshold); week lookback = 7 days (change from last week); month lookback = 30 days (change from last month)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#11</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**data source** · 2024 presidential · explicit

The 2024 Silver Bulletin model publishes raw output files that are updated with each forecast run. They are: Econ Index, EV Probabilities, Election Paths, EC vs Popvote, Scenario Analysis, Forecast Steps, National Topline, Pres Pollist, Voteshare Probabilities, Poll Average and State Topline.

> These spreadsheets contain the raw output from our forecast model.

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#34</sub>

### 2024-11-07 · [The model exactly predicted the most likely election map](https://www.natesilver.net/p/the-model-exactly-predicted-the-most)
**limitation or failure mode** · 2024 presidential · explicit

Iowa's conditional miss (Trump +4.2 versus expectation) is attributed to the inaccurate Selzer poll. Because Iowa was sparsely polled, that single poll carried substantial weight in the state forecast.

*Numbers:* Iowa delta = +4.2 points (Trump vs conditional projection)

> Iowa unto itself, frankly because of the Sezler poll that was, uh, not highly accurate.

<sub>2024-11-07_the-model-exactly-predicted-the-most-likely-election-map#25</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**critique of other approach** · general principle · explicit

Silver's main criticism of the RCP average is not its Republican lean but its unclear, ad hoc poll inclusion standards. A consistent rule, such as excluding polls biased toward Democrats by X points in 2016 and 2020, would be acceptable to him.

*Why:* Consistency and transparency.

> their standards for which polls to include have never been clear.

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#25</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**empirical regularity** · general principle · inferred_from_chart

A Pew chart shows national public pollsters rose from about 29 in 2000 (nearly all live phone) to more than double by 2022, with methods diversifying. The 2022 counts by method:
- Online opt-in only: 28
- ABS with multiple modes: 7
- Probability panel only: 7
- Other: 7
- Online opt-in plus live phone: 4
- IVR alone or with other methods: 4
- Live phone RDD only: 4
- Online opt-in, probability panel and live phone: 3
- Probability panel plus live phone: 3
- Live phone RBS only: 2

*Numbers:* national public pollsters in 2000 = About 29 pollsters (Pew analysis); online opt-in only pollsters 2022 = 28 pollsters (Pew analysis); live phone RDD only 2022 = 4 pollsters (Pew analysis)

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#10</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**empirical regularity** · general principle · explicit

Pollsters use heterogeneous sampling frames:
- NYT/Siena samples from voter registration files.
- YouGov uses nonprobability sampling from an online panel.
- CNN uses a probability-recruited panel sampled nonprobabilistically for later surveys.
Because raw data are nonrepresentative, poll quality is now largely determined by the rigor of weighting.

*Why:* The RDD gold standard of high-response random samples no longer exists.

> The distinction, in my mind, between high-quality and low-quality [polls] is the rigor of the weighting methods.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#11</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**data source** · Silver Bulletin pollster ratings June 2024 · explicit

The June 2024 ratings update added polls from the 2023 gubernatorial elections, congressional special elections and the 2024 Republican presidential primaries. This came to only 63 new polls, so the ratings changed little.

*Numbers:* new polls added since last update = 63 polls (June 2024 update)

*Why:* Most of these elections were uncompetitive and lightly polled.

> only 63 polls since the last update. So the ratings have not changed very much.

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#2</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**adjustment rule** · Silver Bulletin pollster ratings June 2024 · explicit

The 2024 Democratic presidential primaries were excluded entirely from the pollster ratings. There were few polls, the New Hampshire polls involved Biden as a write-in candidate, and named candidates (Phillips, Williamson) often ran behind 'uncommitted'. Few if any of these polls would meet Silver's rules for primary polls.

*Why:* Write-in races are a difficult circumstance that Silver does not think is fair to judge pollsters on.

> Few if any of these polls would qualify by the various rules I apply to primary polls, so I just skipped the Democratic primaries entirely.

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#3</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**method** · Silver Bulletin pollster ratings June 2024 · explicit

The pollster ratings database goes back to 1998. Polls from more recent years are weighted more heavily.

*Numbers:* database start year = 1998 year (pollster ratings database)

> The database goes back to 1998, though polls from more recent years are weighted more heavily.

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#14</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**adjustment rule** · Silver Bulletin pollster ratings June 2024 · explicit

In general, the pollster ratings cover all polls conducted in the 21 days before presidential, congressional and gubernatorial general elections, and before presidential primaries.

*Numbers:* poll eligibility window = 21 days (before the election)

> these ratings cover all polls in the 21 days prior to presidential, Congressional and gubernatorial general elections, and presidential primaries

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#15</sub>

### 2025-02-17 · [Silver Bulletin pollster ratings 2024 archive](https://www.natesilver.net/p/silver-bulletin-pollster-ratings-archive)
**data source** · Silver Bulletin pollster ratings June 2024 · explicit

The raw poll dataset (Rawpolls 061224) contains topline numbers from more than 11,500 polls and is free to use with attribution. A separate file (Pollster Stats Full 2024) gives detailed per-pollster stats, including race-call rates and alternative plus-minus calculations.

*Numbers:* polls in raw dataset = more than 11,500 polls (June 2024)

> including topline numbers from more than 11,500 polls

<sub>2025-02-17_silver-bulletin-pollster-ratings-2024-archive#16</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**method** · Silver Bulletin pollster ratings · explicit

The pollster ratings database used for accuracy evaluation covers polls since 1998 conducted in the final three weeks (21 days) before general elections for president, governor, Senate and House, and before presidential primaries.

*Numbers:* evaluation window = 21 days (before election); database start year = 1998 (pollster ratings database)

> our database since 1998, which covers polls in the final three weeks before general elections for president, governor, and Congress — and presidential primaries

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#1</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**method** · Silver Bulletin pollster ratings · inferred_from_chart

Whether a poll falls inside the 21-day cutoff is determined by the poll's median field date.

*Numbers:* cutoff = 21 days (measured from median field date)

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#2</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**method** · Silver Bulletin pollster ratings · inferred_from_chart

Polls from pollsters banned by Silver Bulletin are excluded from the accuracy and bias analyses.

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#3</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**method** · Silver Bulletin pollster ratings · explicit

Odd-numbered years are grouped with the following even-numbered year into two-year cycles (for example, 2023-2024) for evaluation.

*Why:* Odd years have few qualifying polls, only off-cycle gubernatorial races and special elections.

> We group odd-numbered years (e.g., 2023) together with even-numbered ones (2024) because there aren't many qualifying polls in these

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#5</sub>

### 2025-02-17 · [So, how did the polls do in 2024? It’s complicated](https://www.natesilver.net/p/so-how-did-the-polls-do-in-2024-its)
**data source** · Silver Bulletin pollster ratings · explicit

Silver Bulletin applies specific inclusion rules to presidential primary polls. Because almost none of the few 2024 Democratic primary polls met these rules, the database contains no 2024 Democratic primary polls.

> basically none of them followed the various rules we apply to primary polls — there are no 2024 Democratic primary polls in our database anyway

<sub>2025-02-17_how-did-the-polls-do-in-2024-its-complicated#6</sub>

### 2025-03-22 · [How low is Trump's popularity floor?](https://www.natesilver.net/p/how-low-is-trumps-popularity-floor)
**method** · Silver Bulletin historical approval database · explicit

For comparisons of early-term approval, Silver starts the clock on Feb. 1 rather than inauguration day because approval polling is often sparse very early in a term. George W. Bush is started on Feb. 4 because the Silver Bulletin database contains only one Bush poll before Feb. 1.

*Numbers:* comparison start date = Feb. 1 date (first-year approval comparisons); Bush start date = Feb. 4 date (exception due to sparse data); Bush polls before Feb. 1 in database = one polls (George W. Bush 2001)

*Why:* Sparse early polling makes averages unreliable at the start of a term.

> Let's start the clock on Feb. 1 rather than Jan. 21, though, since approval rating polling is often sparse very early in a president's term.

<sub>2025-03-22_how-low-is-trumps-popularity-floor-by-nate-silver#4</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**data source** · Silver Bulletin pollster ratings · explicit

The Silver Bulletin pollster ratings database includes polls from the final three weeks (21 days) before general elections for president, governor and Congress, going back to 1998. It also includes presidential primary polls, which inflate the database's historical average error.

*Numbers:* poll window = 21 days (final three weeks before the election); database start year = 1998 year (pollster ratings database)

> Our database includes polls in the final three weeks before general elections for president, governor, and Congress and goes back to 1998.

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#1</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**adjustment rule** · Silver Bulletin pollster ratings · inferred_from_chart

The 21-day cutoff for including a poll in the pollster ratings and accuracy analysis is determined by the poll's median field date.

*Numbers:* cutoff = 21 days (based on median field date)

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#2</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**adjustment rule** · Silver Bulletin pollster ratings · explicit

Mayoral race polls, such as the 2025 New York City mayoral race, do not count toward Silver Bulletin pollster ratings. Silver Bulletin keeps this rule even though it lets some pollsters who did poorly in that race off the hook.

*Why:* Giving a mulligan to a few pollsters is not a good enough reason to change the methodology.

> But mayoral polls don't factor into our pollster ratings. Admittedly, that gives a mulligan to a few pollsters who had a tough race

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#3</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**adjustment rule** · Silver Bulletin pollster ratings · inferred_from_chart

Polls from pollsters banned by Silver Bulletin are excluded from the pollster accuracy analysis.

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#4</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings 2025 archive](https://www.natesilver.net/p/pollster-ratings-archive-2025)
**method** · Silver Bulletin pollster ratings · explicit

Some polls, such as those from ActiVote, never enter the database. They are not banned, but they fail the standard for scientific surveys, either because amateurs run them on cheap online platforms or because they use non-random convenience samples without adequate bias correction. They receive no rating.

> These polls aren’t “banned” per se — they just don’t make it into our database in the first place because they don’t meet our standards

<sub>2026-01-14_silver-bulletin-pollster-ratings-2025-archive#13</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**adjustment rule** · Silver Bulletin pollster ratings · explicit

The pollster ratings database excludes mayoral race polls, including the 2025 New York City mayoral election, so pollsters are not penalized for misses in those races.

*Why:* Mayoral polling has historically not been used, and there is no principled reason to include NYC but not other mayoral races.

> Historically, we haven’t used mayoral polling when calculating pollster ratings, and there’s no principled reason to start using polls from NYC but not from other mayoral races.

<sub>2026-01-14_pollster-ratings-silver-bulletin#2</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**method** · Silver Bulletin pollster ratings · explicit

The pollster ratings cover all polls taken in the final 21 days before presidential, congressional and gubernatorial general elections, and before presidential primaries.

*Numbers:* poll window = 21 days (days before the election for a poll to be included in the ratings)

> In general, these ratings cover all polls in the 21 days prior to presidential, Congressional and gubernatorial general elections, and presidential primaries.

<sub>2026-01-14_pollster-ratings-silver-bulletin#3</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**adjustment rule** · Silver Bulletin pollster ratings · explicit

Polls that do not meet Silver Bulletin's standards for scientific surveys are kept out of the database entirely and receive no rating. These are polls run by amateurs on cheap online survey platforms, or polls using non-random convenience samples without adequate bias correction, such as ActiVote. This is a separate category from banned pollsters.

> These polls aren’t “banned” per se — they just don’t make it into our database in the first place because they don’t meet our standards

<sub>2026-01-14_pollster-ratings-silver-bulletin#8</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**limitation or failure mode** · Silver Bulletin pollster ratings Jan 2026 · explicit

When the page was first published, five non-scientific 2025 polls had been included in the ratings database by mistake. They were later removed.

*Numbers:* mistakenly included polls = 5 polls (2025 polls removed after publication)

> five polls conducted in 2025 that fall into this category were mistakenly included in our database. They have since been removed.

<sub>2026-01-14_pollster-ratings-silver-bulletin#9</sub>

### 2026-01-14 · [Silver Bulletin pollster ratings, January 2026 update](https://www.natesilver.net/p/pollster-ratings-silver-bulletin)
**data source** · Silver Bulletin pollster ratings Jan 2026 · explicit

The released raw polls dataset contains topline numbers from more than 12,300 polls, free to use with attribution. A separate full stats file includes alternative plus-minus calculations and methodological transparency details for each pollster.

*Numbers:* polls in raw data = more than 12,300 polls (Rawpolls 011226 file)

> including topline numbers from more than 12,300 polls.

<sub>2026-01-14_pollster-ratings-silver-bulletin#29</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**design principle** · Silver Bulletin polling averages (2026) · explicit

Silver Bulletin polling averages aim to include all professionally conducted surveys, listing them under the polling firm rather than the media sponsor.

*Numbers:* update frequency = ~6 updates per week (polling averages)

*Why:* Inclusivity is the general aim; reliability is handled through weighting rather than exclusion.

> Our general aim is for inclusivity. We seek to include all professionally-conducted surveys.

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#0</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**method** · Silver Bulletin polling averages (2026) · explicit

Silver Bulletin excludes four kinds of polls: those from pollsters banned for known or suspected faked data, DIY polls by non-professional hobbyists on platforms like Google Surveys, 'polls' that blend or smooth data with methods such as MRP, and polls that ask vote choice only after revealing leading information about candidates.

*Why:* These are not genuine, independent, neutrally worded measurements of opinion.

> We don't use "polls" that blend or smooth their data using methods such as MRP.

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#1</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**method** · Silver Bulletin polling averages (2026) · explicit

Internal and campaign polls are included if they meet the other standards. For approval averages they are treated like any other poll; for the generic ballot they get a different house-effect prior. Nominally nonpartisan pollsters with undisclosed histories of partisan work, currently Trafalgar Group and Rasmussen Reports, are automatically classified as partisan.

*Why:* Undisclosed campaign relationships make a firm's polls behave like partisan polls.

> Internal or campaign polls are included, provided they meet these other standards.

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#2</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**method** · Silver Bulletin generic ballot average (2026) · explicit

The generic ballot average pools two question wordings: which party's candidate the voter will support for Congress, and which party they would prefer to control Congress.

> two slightly distinct questions are included in the average

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#4</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**method** · Silver Bulletin 2026 generic ballot average · explicit

The Silver Bulletin generic ballot average includes two types of polls. The first asks which party's candidate the respondent will vote for in the U.S. House election, sometimes with named district candidates. The second asks which party the respondent prefers to control Congress.

*Why:* Empirically the two question types produce nearly identical results, and including both increases sample size.

> We include these too since, empirically, they produce nearly identical results to the other type of survey and increase our sample size.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#0</sub>

### 2026-04-11 · [“AI polls” are fake polls](https://www.natesilver.net/p/ai-polls-are-fake-polls)
**method** · Silver Bulletin polling averages (2026) · explicit

Silver Bulletin excludes all Public Sentiment Institute polls from its averages because it classifies the firm as an amateur polling firm; a poll that 'boosted' 373 real respondents with 114 AI agents would not meet aggregation standards anyway.

*Numbers:* real respondents = 373 respondents (Public Sentiment Institute poll); AI agents added = 114 agents (Public Sentiment Institute poll)

> we exclude all Public Sentiment Institute polls from our averages because we classify them as an amateur polling firm.

<sub>2026-04-11_ai-polls-are-fake-polls-by-eli-mckown-dawson#0</sub>

### 2026-04-11 · [“AI polls” are fake polls](https://www.natesilver.net/p/ai-polls-are-fake-polls)
**method** · Silver Bulletin forecasts and averages (2026) · explicit

Silver Bulletin does not include MRP-produced 'polls' in its forecasts or averages, and considers it misleading when MRP outputs are presented as if original data had been collected in many states or congressional districts.

*Why:* MRP is a model, not original data collection.

> Silver Bulletin does not include “polls” produced by MRP in our forecasts or averages

<sub>2026-04-11_ai-polls-are-fake-polls-by-eli-mckown-dawson#1</sub>

### 2026-04-11 · [“AI polls” are fake polls](https://www.natesilver.net/p/ai-polls-are-fake-polls)
**design principle** · Silver Bulletin (2026) · explicit

Synthetic samples from LLM agents are treated as models rather than polls: polling is data collection, while silicon sampling only predicts what a poll would say from training data and prompts, so it cannot enter a poll average as a poll.

*Why:* Weighting real survey data differs fundamentally from predicting survey results with a model.

> Silicon sampling, on the other hand, produces no new data.

<sub>2026-04-11_ai-polls-are-fake-polls-by-eli-mckown-dawson#2</sub>

### 2026-04-11 · [“AI polls” are fake polls](https://www.natesilver.net/p/ai-polls-are-fake-polls)
**limitation or failure mode** · general principle · explicit

Inference cannot detect genuine opinion shifts within a subgroup that is not directly sampled; only original data collection can. Silver argues that cheaper statistical inference raises the comparative value of collecting original data.

> But you don’t actually know what these voters think unless you’re reaching them directly.

<sub>2026-04-11_ai-polls-are-fake-polls-by-eli-mckown-dawson#4</sub>

### 2026-04-11 · [“AI polls” are fake polls](https://www.natesilver.net/p/ai-polls-are-fake-polls)
**empirical regularity** · general (literature) · explicit

Academic research finds LLM-simulated survey respondents give too few 'don't know' responses, can seriously overstate the favorability of politicians like Trump and Harris, and show too little variation between subgroups such as Democrats and Republicans.

> LLMs suffer from various quirks like producing too few “don’t know” responses

<sub>2026-04-11_ai-polls-are-fake-polls-by-eli-mckown-dawson#5</sub>

### 2026-04-11 · [“AI polls” are fake polls](https://www.natesilver.net/p/ai-polls-are-fake-polls)
**limitation or failure mode** · general · explicit

AI agents infiltrating online survey panels are a threat to real polls; evidence on how well online panels' checks filter them, and how prevalent they are, is conflicting.

> one danger to actual polls is that AI agents can be used to infiltrate online surveys.

<sub>2026-04-11_ai-polls-are-fake-polls-by-eli-mckown-dawson#7</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**data source** · FLIPR 2026 · explicit

FLIPR is fit primarily on Senate races since 1990 and on House and gubernatorial races since 1998.

*Numbers:* Senate training start = 1990 year (FLIPR fit); House and governor training start = 1998 year (FLIPR fit)

> The model is fit primarily based on Senate races since 1990, and House and gubernatorial races since 1998.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#4</sub>

### 2026-08-13 · [Prediction markets aren't magic](https://www.natesilver.net/p/prediction-markets-arent-magic)
**method** · FLIPR 2026 · explicit

Before a state's primary, FLIPR uses 'educated guesses' of each party's nominee, based simply on polls and prediction markets with no attempt at value-added prediction, and replaces them with actual winners after the primary. FLIPR is a general-election model, not a primary model.

> We usually just go by polls and prediction markets and these very much aren’t intended as any sort of value-added prediction; FLIPR is a general election model, not a primary model.

<sub>2026-08-13_prediction-markets-arent-magic-by-nate-silver#0</sub>

### 2026-08-20 · [Are Democrats on a summer sugar high?](https://www.natesilver.net/p/are-democrats-on-a-summer-sugar-high)
**empirical regularity** · FLIPR 2026 · explicit

Summer is 'silly season' for polls: campaigns release internal polls for attention and fundraising, and by fall pollsters publish fewer outliers and herd more. FLIPR's harsh penalties on internal polls smooth its averages.

> FLIPR applies some pretty harsh penalties to internal polls

<sub>2026-08-19_are-democrats-on-a-summer-sugar-high-by-nate-silver#6</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**data source** · Silver Bulletin polling database · explicit

Since 2016 the Silver Bulletin database includes 246 qualifying polls covering 36 special/off-year races across 27 election dates; Democrats usually did better than these polls predicted. Larger historical midterm polling errors exist in the deeper archive, e.g. 1994 and 1998.

*Numbers:* special/off-year polls since 2016 = 246 polls (36 races, 27 dates)

> since 2016, a total of 246 qualifying polls covering 36 distinct races across 27 unique election dates.

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#9</sub>

### 2026-10-15 · [Welcome to midterm silly season 🤡](https://www.natesilver.net/p/welcome-to-midterm-silly-season)
**empirical regularity** · general · explicit

The closing days of campaigns feature more pollster 'discipline', or herding, so the late poll dataset is slightly censored: pollsters are reluctant to publish outliers that defy the consensus.

> We’re probably getting a slightly censored dataset at this point, with pollsters reluctant to publish seeming outlier results that defy the consensus.

<sub>2026-10-15_republicans-are-spending-big-its-not-working#3</sub>

### 2026-10-20 · [My pet peeve about the polling error debate](https://www.natesilver.net/p/my-pet-peeve-about-the-polling-error)
**method** · Silver Bulletin polling database · explicit

The pollster database groups elections into two-year cycles; in this analysis non-November elections (off-year, specials, runoffs) were split into an 'interim' bucket, with a December runoff after a presidential election counting toward the next interim period. Table values are simple averages of all polls, so well-polled races weigh more.

> The data in this table is just a simple average of all polls in our pollster ratings database, so more well-polled races have more influence on it.

<sub>2026-10-20_my-pet-peeve-about-the-polling-error-debate#5</sub>

### 2026-10-22 · [Fake polls are a real problem](https://www.natesilver.net/p/fake-polls-are-a-real-problem)
**data source** · FLIPR 2026 · explicit

FLIPR takes its House, Senate and governor horse-race polls from The New York Times poll database, which is fast, comprehensive, vetted, and explicitly modeled on the old FiveThirtyEight schema and inclusion criteria Silver helped design. Silver Bulletin maintains its own databases for presidential approval, the generic ballot and certain other series. In 2024 it relied on the post-Silver FiveThirtyEight feed instead.

*Why:* No point recreating work done the same way.

> The literal answer is that we take our polling data from The New York Times, subject occasionally to some manual additions and overrides.

<sub>2026-10-22_fake-polls-are-a-real-problem-by-nate-silver#0</sub>

### 2026-10-22 · [Fake polls are a real problem](https://www.natesilver.net/p/fake-polls-are-a-real-problem)
**method** · FLIPR 2026 · explicit

Manual overrides on the NYT feed: 11 permanently banned pollsters (known or believed to have fabricated data or committed gross misconduct, e.g. Strategic Vision, Research 2000) are ignored; 'nonprofessional' DIY firms such as SoCal Strategies and ActiVote are excluded; Rasmussen Reports polls, not listed by the NYT, are added manually; and polls are occasionally added before NYT lists them, though Silver Bulletin generally waits a day or two in case a poll failed vetting.

*Numbers:* permanently banned pollsters = 11 firms (Silver Bulletin list, Oct 2026)

> We have a list of 11 permanently banned pollsters

<sub>2026-10-22_fake-polls-are-a-real-problem-by-nate-silver#1</sub>

### 2026-10-22 · [Fake polls are a real problem](https://www.natesilver.net/p/fake-polls-are-a-real-problem)
**design principle** · Silver Bulletin polling averages · explicit

Silver Bulletin prefers to 'just plug it into the average', weighting established pollsters more, rather than subjectively filtering individual polls, which might reflect an aggregator's rooting interests. It avoids dissecting individual polls, with exceptions for top-rated independent firms like NYT/Siena.

*Why:* Least-worst alternative; outlier attention is preferable to herding.

> But it’s probably the least-worst alternative versus applying some sort of subjective filter to polls

<sub>2026-10-22_fake-polls-are-a-real-problem-by-nate-silver#4</sub>

### 2026-10-22 · [Fake polls are a real problem](https://www.natesilver.net/p/fake-polls-are-a-real-problem)
**method** · FiveThirtyEight history · explicit

Statistical fraud detection: Strategic Vision's fabricated polls (exposed 2009) and Research 2000's (2010) showed far more of some trailing digits (e.g. 5, 7, 8, 9) than others, a canonical sign of forged results, since humans are bad at generating random numbers.

> Strategic Vision “polls” exhibited statistical patterns — namely, being far more likely to contain some trailing digits (such as 5, 7, 8 and 9) than others

<sub>2026-10-22_fake-polls-are-a-real-problem-by-nate-silver#5</sub>

### 2026-10-22 · [Fake polls are a real problem](https://www.natesilver.net/p/fake-polls-are-a-real-problem)
**limitation or failure mode** · general · explicit

New fake-poll risks include manipulating high-volume prediction markets through outlier or fake polls in sparsely surveyed races, discrediting the polling industry, and AI-assisted fabrication that may also defeat vetting.

> One of them is publishing fake polls to manipulate prediction markets.

<sub>2026-10-22_fake-polls-are-a-real-problem-by-nate-silver#8</sub>

### 2026-10-25 · [Let’s talk shop about every Senate race](https://www.natesilver.net/p/lets-talk-shop-about-every-senate)
**design principle** · FLIPR 2026 · explicit

FLIPR does not use early-voting data, except insofar as pollsters' assumptions about early voting are reflected in polls. Silver is skeptical of early-vote analysis, though Joel Wertheimer argues it can help if focused on which party turns out unlikely voters.

> markets may be building in some information — or assumptions — based on early voting data, something that FLIPR doesn’t really look at.

<sub>2026-10-25_lets-talk-shop-about-every-senate-race-by-nate-silver#2</sub>

### 2026-11-03 · [FLIPR 2026 Senate forecast](https://www.natesilver.net/p/nate-silver-2026-midterm-election-senate-model)
**data source** · FLIPR 2026 · explicit

FLIPR draws most election polls from the NYT poll database but collects generic ballot and congressional approval polls itself. It includes polls from a few pollsters the NYT excludes and excludes surveys from banned or non-scientific firms.

> We also include polls from a few pollsters that The New York Times excludes from their database, and exclude surveys from firms we ban or that don’t meet our standards for being scientific surveys.

<sub>2026-11-03_2026-midterm-election-senate-forecast-silver-bulletin#7</sub>

### 2026-11-03 · [It's Judgment Day for Trump (and for pollsters)](https://www.natesilver.net/p/its-judgment-day-for-trump-and-for)
**design principle** · FLIPR 2026 · explicit

FLIPR does not consider most 'other signals' such as primary turnout, special election results, early voting, and party spending or behavior; individual-contributor fundraising is the exception. Silver weighs them informally. For early vote, he favors looking at whether parties turn out unlikely voters and at state experts with strong track records.

*Why:* Individually unreliable, though possibly informative collectively.

> FLIPR doesn’t really consider most of these, other than fundraising from individual contributors

<sub>2026-11-03_its-judgment-day-for-trump-and-for-pollsters#6</sub>

### 2026-11-03 · [Who’s ahead on the generic congressional ballot?](https://www.natesilver.net/p/generic-ballot-average-2026-nate-silver-bulletin-congress-polls)
**data source** · Silver Bulletin generic ballot average · explicit

Silver Bulletin provides retrospective generic ballot averages for every cycle from 1994 to 2024, calculated by applying the current methodology and pollster ratings to past polls, as a downloadable XLSX ('Generic Topline All Cycles'), along with a download of every 2026 generic ballot poll in its database.

*Numbers:* historical coverage start = 1994 year (retrospective generic ballot averages)

> Note that these are calculated retrospectively for previous cycles based on our current methodology and pollster ratings.

<sub>2026-11-03_generic-congressional-ballot-latest-polls-silver-bulletin#5</sub>

### 2026-11-04 · [How popular is Donald Trump?](https://www.natesilver.net/p/trump-approval-ratings-nate-silver-bulletin)
**data source** · Silver Bulletin approval average · explicit

Silver Bulletin provides retrospectively calculated daily approval averages for every president since 1945 (Truman onward) as a downloadable 'Historical Approval Averages' XLSX, plus a download of every Trump approval poll in its database.

*Numbers:* historical coverage start = 1945 year (daily presidential approval averages)

> Note that these are calculated retrospectively; Substack wasn’t around during the Eisenhower administration.

<sub>2026-11-04_trump-approval-rating-latest-polls-silver-bulletin#5</sub>
