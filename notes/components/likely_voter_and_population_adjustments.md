# Likely voter and population adjustments

60 findings from 32 articles, oldest first.

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**parameter or number** · FiveThirtyEight 2016 presidential · explicit

Historically Republicans gain a net 1 to 2 points in likely-voter polls versus RV or adult polls. Polls-plus started with this default; polls-only and now-cast used zero. Both update from paired polls, and LV polls show fewer undecideds.

*Numbers:* historical R gain in LV polls = 1 to 2 percentage points net (pre-2016)

> Historically, Republicans gain slightly in likely voter polls — a net of 1 to 2 percentage points

<sub>fte_2016-general-election-forecast-users-guide#5</sub>

### 2018-09-12 · [How FiveThirtyEight’s House, Senate And Governor Models Work](https://fivethirtyeight.com/methodology/how-fivethirtyeights-house-and-senate-models-work/)
**method** · FiveThirtyEight midterm models (2018-2022) · explicit

The midterm likely-voter adjustment is dynamic: it starts with a prior that LV polls slightly help Republicans, smaller in midterms with a Republican president, and updates as pollsters publish paired LV/RV results. FLIPR later replaced this with a more neutral prior.

> it starts with a prior that likely voter polls slightly help Republicans, but this prior is updated as pollsters publish polls that directly compare likely and registered voter results.

<sub>fte_midterm-house-senate-governor-methodology#10</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**adjustment rule** · FiveThirtyEight 2020 presidential · explicit

The 2020 likely-voter adjustment shifted registered-voter polls toward what LV polls would show. Historically Republicans gain under LV screens, mitigated when the Republican is an incumbent; in 2020 paired polls showed Trump gaining about 1 point in LV versions.

*Numbers:* Trump LV gain = around 1 percentage point (2020 paired polls)

> Generally speaking, this means that Republicans (such as Trump) gain ground relative to Democrats when applying a likely voter screen, although this effect is mitigated when the Republican is an incumbent.

<sub>fte_2020-presidential-forecast-methodology#3</sub>

### 2023-07-01 · [Polling averages shouldn't be political litmus tests](https://www.natesilver.net/p/polling-averages-shouldnt-be-political)
**interpretation guidance** · general principle · explicit

The quoted letter raises a likely-voter issue: if a pollster weights to census data first and then screens for likely voters, it may need to rebalance the LV sample. Women are less likely than men to say they will definitely vote, yet usually make up at least half of the electorate. Silver calls this a reasonable but very in-the-weeds question.

*Numbers:* women's share of electorate = at least half share (US electorate, per the Morris letter quoted)

> women are less likely than men to say they're definitely going to vote, but they usually make up at least half of the electorate anyway.

<sub>2023-07-01_polling-averages-shouldnt-be-political-litmus-tests#13</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**method** · 538 2008-2020 presidential · explicit

The model adjusts polls of registered voters and of all adults toward a likely-voter equivalent. In previous versions this adjustment used a prior that Republicans gain from the shift from registered to likely voters, and that challengers rather than incumbents also gain.

*Why:* Historically Republicans were more reliable voters, and challengers' supporters tend to be more enthusiastic.

> The model had a prior that Republican candidates were likely to benefit from the shift from registered to likely voter polls and that challengers

<sub>2024-06-26_2024-presidential-election-model-methodology-update#4</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**model change** · 2024 presidential · explicit

In 2024 the registered-to-likely-voter adjustment uses a 'zero prior': conversion is assumed equally likely to help either party. The prior is updated as polls that directly compare registered and likely voters enter the database.

*Why:* There is robust evidence, such as special elections, that Democrats now have the more engaged voters.

> I’ve simply reverted to a “zero prior” instead, meaning that the model assumes that the conversion from registered to likely voter polls is equally likely to help Democrats or Republicans.

<sub>2024-06-26_2024-presidential-election-model-methodology-update#5</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**model change** · 2024 presidential · explicit

The weight on the likely-voter prior was lowered to make the adjustment more strictly empirical. By late June 2024 the prior was almost entirely phased out, with full phase-out expected soon, so the adjustment becomes driven by data from polls that report both registered- and likely-voter results.

*Why:* Make the adjustment more strictly empirical.

> I’ve also lowered the weight on the prior to make the adjustment more strictly empirical.

<sub>2024-06-26_2024-presidential-election-model-methodology-update#6</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**interpretation guidance** · 2024 presidential · explicit

Weakening the Republican-favoring likely-voter prior helps Biden in 2024, because he fared slightly better in likely-voter polls than in registered-voter polls. The old model would have held more stubbornly to the premise that likely-voter polls usually benefit Republicans.

> weakening this prior helps Joe Biden, who so far this cycle has generally fared slightly better in polls of likely voters rather than registered voters

<sub>2024-06-26_2024-presidential-election-model-methodology-update#7</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**model change** · 2024 presidential vs 2020 · explicit

The 2024 model removed the prior that Republicans do better in likely-voter polls than in registered-voter polls. This materially helps Biden, and Silver considers the evidence for the change highly robust.

*Why:* Evidence that the LV Republican advantage no longer holds is highly robust.

> getting rid of the prior that Republicans tend to better in polls of likely voters rather than registered voters

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#15</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**adjustment rule** · 2024 polling averages · explicit

The Silver Bulletin polling averages adjust for likely versus registered voter populations; in 2024 this helps Biden.

> making adjustments for factors like likely versus registered voters (this helps Biden)

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#16</sub>

### 2024-06-27 · [Are these guys trying to muddle through? Or playing to win?](https://www.natesilver.net/p/are-these-guys-trying-to-muddle-through)
**adjustment rule** · 2024 presidential · explicit

The Silver Bulletin model applies a likely-voter adjustment to all registered-voter polls. The size of that adjustment is estimated from polls that report both likely-voter and registered-voter results. For example, the June 2024 NYT/Siena poll showed Biden meaningfully better among likely voters than registered voters, and this shifted the adjustment applied to every registered-voter poll.

*Why:* Polls that publish both versions reveal the current gap between registered and likely voters.

> it did show him doing meaningfully better among likely voters than among registered voters — and that affects the adjustment the model applies to all registered voter polls

<sub>2024-06-27_are-these-guys-trying-to-muddle-through-or-playing-to-win#7</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**adjustment rule** · 2024 presidential polling averages · explicit

The Silver Bulletin polling averages adjust polls for whether they were conducted among registered voters or likely voters.

> They adjust for whether polls are conducted among registered or likely voters

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#1</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**method** · 2024 presidential · explicit

Older polling data is also used to calibrate the likely-voter adjustment, meaning which candidate tends to gain or lose ground in polls of likely voters.

> or which candidate tends to gain or lose ground in polls of likely voters

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#6</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**empirical regularity** · general principle · explicit

Non-response is correlated with vote intention. College-educated voters and high-social-trust voters respond more to polls and lean Democratic, and demographic weighting only partially fixes this.

> You can partially solve issues like these with demographic weighting

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#34</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**limitation or failure mode** · general principle · explicit

Pollster weighting on party ID, party registration or recalled past vote is probably effective against partisan non-response bias. However, it risks missing real movement because party ID is fluid.

*Why:* A voter disillusioned with Trump may start identifying as an independent before changing his registration.

> These techniques are probably pretty effective at avoiding partisan non-response bias, though they may run the risk of missing real movement in the polls.

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#35</sub>

### 2024-09-11 · [A guide to post-debate poll-watching](https://www.natesilver.net/p/a-guide-to-post-debate-poll-watching)
**empirical regularity** · general principle · explicit

Online panel pollsters such as Morning Consult and YouGov weight heavily on past vote or party identification to counter partisan response bias in their non-probability samples. As a result, their polls typically show little movement after events, and they sometimes miss real shifts.

*Why:* Enthusiastic partisans respond more eagerly to surveys after good events for their side, which can bias results.

> these firms tend to weight heavily on past voting patterns or party identification to minimize problems with partisan response bias in their non-probability samples.

<sub>2024-09-11_a-guide-to-post-debate-poll-watching-by-nate-silver#10</sub>

### 2024-09-23 · [Trust a pollster more when it publishes “outliers”](https://www.natesilver.net/p/trust-a-pollster-more-when-it-publishes)
**limitation or failure mode** · general principle · explicit

Some pollsters import so many priors through weighting and massaging that their surveys are de facto closer to models than to polls.

> Some surveys are de facto closer to models than polls

<sub>2024-09-23_trust-a-pollster-more-when-it-publishes-outliers#17</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**empirical regularity** · 2024 polling landscape · explicit

After the 2016 and 2020 misses, many pollsters in 2024 weight samples by recalled past vote, which had been an uncommon technique. Pollsters traditionally avoided it because respondents misremember or misstate their vote, overclaiming a vote for the previous winner.

*Why:* Recall bias toward the winner (Biden) could make samples look artificially shifted toward Trump.

> many pollsters are applying what until now had been a relatively uncommon technique: weighting their samples based on how people say they voted in the last election

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#9</sub>

### 2024-10-12 · [New York Times polls are betting on a political realignment](https://www.natesilver.net/p/new-york-times-polls-are-betting)
**limitation or failure mode** · 2024 polling landscape · explicit

Recall-vote bias in 2024 is complicated by two factors: Biden's unpopularity may reduce overclaiming of a Biden vote, and many Republicans wrongly believe Trump won. If respondents falsely recall a Biden vote and now back Trump, weighting by recalled vote can create a phantom pro-Trump shift, so polls would underestimate Harris.

> it will look like there's been a shift toward Trump when there actually hasn't been

<sub>2024-10-12_new-york-times-polls-are-betting-on-a-political-realignment#10</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**empirical regularity** · general principle · explicit

Trump's polling overperformance in 2016 and 2020 was likely caused by nonresponse bias rather than 'shy Trump voters' lying to pollsters. Democrats are more likely to respond to political surveys, so pollsters weren't reaching enough Trump voters.

*Why:* There is little evidence for the shy-voter theory, there is no persistent worldwide right-wing overperformance, and there is less stigma than ever to supporting Trump.

> It's not that Trump voters are lying to pollsters; it's that in 2016 and 2020, pollsters weren't reaching enough of them.

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#11</sub>

### 2024-10-23 · [Why Harris could beat her polls](https://www.natesilver.net/p/why-harris-could-beat-her-polls)
**empirical regularity** · 2024 presidential · explicit

Pollsters have changed their methods in response to 2016 and 2020 nonresponse bias. Silver estimates that if they still used their 2016/2020 techniques, polls would probably show a Harris lead in the Electoral College instead of a rough toss-up.

> If polling firms were still applying the same techniques they did in 2016 and 2020, we'd probably be seeing a Harris lead in the Electoral College right now.

<sub>2024-10-23_why-harris-could-beat-her-polls-by-nate-silver#12</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**method** · 2024 presidential · explicit

In the Silver Bulletin polling average and presidential model, when a firm releases both a likely voter (LV) and a registered voter (RV) version of the same poll, the LV version is used instead of the RV version.

*Why:* LV polls are theoretically more accurate than RV polls.

> When a firm releases two versions of a poll, we use the LV version instead of the RV version.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#0</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**adjustment rule** · 2024 presidential · explicit

When a poll publishes only RV numbers, the Silver Bulletin model adjusts it to an LV basis. The size of the adjustment is estimated from polls that release both LV and RV versions of the same survey.

*Why:* Puts RV-only polls on the same footing as the more accurate LV polls.

> when a poll only publishes RV numbers, we adjust it to essentially transform it to an LV basis. The adjustment is based on polls that release both likely-voter and registered-voter versions of the same survey

<sub>2024-10-24_a-mystery-in-likely-voter-polls#2</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**interpretation guidance** · 2024 presidential · implied

The authors call the LV/RV difference something they 'carefully track' as one factor the model accounts for. This implies the RV-to-LV adjustment is estimated from current-cycle data rather than fixed.

> We carefully track the differences between likely voter (LV) and registered voter (RV) polls because this is one factor our model accounts for.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#3</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**empirical regularity** · general principle · explicit

Historically, LV screens helped Republicans. Pollsters traditionally switched from RV to LV polls after Labor Day, which often boosted GOP candidates, for example Bush in 2004. Part of Bush's September 2004 surge was also due to the timing of the Republican convention.

*Numbers:* Example year = 2004 (Bush-Kerry polling, RV-to-LV switch after Labor Day)

*Why:* Republicans were historically the more regular, reliable voters.

> Traditionally, pollsters began switching from registered voter polls to likely voter polls after Labor Day, which often boosted Republican candidates.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#4</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**empirical regularity** · 2024 presidential · explicit

Before his debate and exit from the race, Biden did better in LV polls than in RV polls in 2024, a reversal of the historical pattern of LV screens helping Republicans.

> Joe Biden was doing better in LV polls than in RV polls — a reversal of the historical trend.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#5</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**empirical regularity** · 2024 presidential · explicit

In 2024 national polls that released both versions, Harris averaged D+2.3 among RVs versus D+2.8 among LVs, so LV screens helped her by 0.5 points nationally.

*Numbers:* National RV margin = D +2.3 percentage points (Paired LV/RV national polls since Harris entered the race); National LV margin = D +2.8 percentage points (Paired LV/RV national polls since Harris entered the race); National LV-RV difference = 0.5 percentage points (In Harris's favor)

> The average margin in these polls is D +2.3 among RVs as compared to a D +2.8 margin in LV polls — a 0.5-point difference in Harris' favor.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#6</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**empirical regularity** · 2024 presidential · inferred_from_chart

In state-level battleground polls, LV versions were on average 0.5 points more favorable to Trump than RV versions (state average D+0.6 RV vs D+0.1 LV). By state (RV margin, LV margin, LV shift): Arizona R+0.7 to R+1.0 (R+0.3); Georgia R+0.2 to R+1.4 (R+1.2); Michigan D+2.0 to D+3.2 (D+1.2); Nevada D+3.3 to D+2.0 (R+1.3); North Carolina EVEN to R+0.9 (R+0.9); Pennsylvania D+2.6 to D+1.7 (R+0.9); Wisconsin D+3.8 to D+3.4 (R+0.4).

*Numbers:* State average RV margin = D +0.6 percentage points (Paired polls, battleground states); State average LV margin = D +0.1 percentage points (Paired polls, battleground states); State average LV shift = R +0.5 percentage points (LV relative to RV); Arizona LV shift = R +0.3 percentage points (RV R+0.7, LV R+1.0); Georgia LV shift = R +1.2 percentage points (RV R+0.2, LV R+1.4); Michigan LV shift = D +1.2 percentage points (RV D+2.0, LV D+3.2); Nevada LV shift = R +1.3 percentage points (RV D+3.3, LV D+2.0); North Carolina LV shift = R +0.9 percentage points (RV EVEN, LV R+0.9); Pennsylvania LV shift = R +0.9 percentage points (RV D+2.6, LV D+1.7); Wisconsin LV shift = R +0.4 percentage points (RV D+3.8, LV D+3.4)

> If you average across all states, you end up with LV polls being 0.5 points more favorable to Trump.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#7</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**interpretation guidance** · 2024 presidential · explicit

Calibrating the Silver Bulletin model on RV rather than LV polls would narrow its Electoral College/popular vote gap and slightly raise Harris's win probability, resembling the universe of NYT/Siena polls. The model's LV preference therefore contributes to its estimated Electoral College bias.

*Why:* State LV polls favor Trump while national LV polls favor Harris.

> If we calibrated our model based on RV rather than LV polls, it would show a narrower Electoral College / popular vote gap, with Harris's overall win probability slightly improving.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#10</sub>

### 2024-10-24 · [A mystery in likely voter polls](https://www.natesilver.net/p/a-mystery-in-likely-voter-polls)
**empirical regularity** · 2024 presidential · explicit

In the Washington Post North Carolina example, Trump led by 4 among RVs and by 3 among LVs. Both candidates gained from third-party and undecided voters in the LV version.

*Numbers:* Trump RV lead = 4 percentage points (WaPo NC poll); Trump LV lead = 3 percentage points (WaPo NC poll)

> And both Trump and Harris gain ground from third-party candidates and the undecided column.

<sub>2024-10-24_a-mystery-in-likely-voter-polls#15</sub>

### 2024-10-30 · [The early vote doesn't reliably predict results](https://www.natesilver.net/p/the-early-vote-doesnt-reliably-predict)
**method** · general principle · explicit

Silver's preferred likely-voter approach for a pollster is probabilistic: each respondent gets a probability of voting, and respondents who have already voted get 100 percent.

*Numbers:* likely voter score for already-voted respondents = 100 percent (Silver's preferred LV method)

> if I were running a poll, I'd treat likely voters probabilistically, and anyone who had already voted would get a score of 100 percent.

<sub>2024-10-30_the-early-vote-doesnt-reliably-predict-results#7</sub>

### 2024-11-01 · [There’s more herding in swing state polls than at a sheep farm in the Scottish Highlands](https://www.natesilver.net/p/theres-more-herding-in-swing-state)
**method** · 2024 presidential herding analysis · explicit

For the herding analysis, Silver Bulletin used likely-voter versions of polls. It used a registered-voter version only when a pollster published no likely-voter version, consistent with a preference hierarchy of LV over RV.

> All the data in this article is based on likely voter polls, unless a pollster only published a registered voter version.

<sub>2024-11-01_theres-more-herding-in-swing-state-polls-than-at-a-sheep-farm-in-the-scottish-hi#5</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**adjustment rule** · Silver Bulletin polling averages 2024 · explicit

The Silver Bulletin polling averages adjust polls according to whether they were conducted among registered or likely voters. Poll populations are labeled LV (likely voters), RV (registered voters), V (voters) and A (adults).

> They adjust for whether polls are conducted among registered or likely voters

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#6</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**empirical regularity** · general principle (2016 lesson) · explicit

In 2016 most polls included too many college graduates, who respond to surveys more and lean Democratic. Afterward, the share of polls weighting by education rose sharply.

> In 2016, most polls included too many college graduates, who are more likely to respond to surveys and also more likely to vote for Democrats.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#8</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**empirical regularity** · general principle · inferred_from_chart

A Schaffner/Soler chart of national polls (July 24 to Sept 25, 2024) shows the share of polls weighting on each factor, 2016 vs 2024 (approximate):
- Age: ~87% to ~98%
- Race: ~94% to ~95%
- Gender: ~87% to ~95%
- Education: ~57% to ~83%
- Region: ~55% to ~68%
- Party: ~21% to ~43%
- Past vote: ~6% to ~33%
- Urban/suburban/rural: ~0% to ~18%
- Income: ~23% to ~18%
- Home ownership: ~6% to ~10%
- Marital status: ~11% to ~8%

*Numbers:* polls weighting on education = ~57 (2016) to ~83 (2024) percent of polls (national pre-election polls); polls weighting on party = ~21 (2016) to ~43 (2024) percent of polls (national pre-election polls); polls weighting on past vote = ~6 (2016) to ~33 (2024) percent of polls (national pre-election polls); polls weighting on urbanicity = ~0 (2016) to ~18 (2024) percent of polls (national pre-election polls)

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#9</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**empirical regularity** · general principle · explicit

Cohn found that weighting to recalled vote would have made polls less accurate in every presidential election since 2004. In 2024 it appears to have helped in most states but struggled with changes in electorate composition, so toplines may have been better while crosstabs were worse. NYT/Siena does not weight on recalled vote.

> weighting to recall would have made polls less accurate in every presidential election since 2004.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#12</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**empirical regularity** · general principle · explicit

By Cohn's count, most pollsters were already weighting on recalled vote in 2024. That leaves limited room for further adoption, a ceiling on how much this technique can further improve polls.

> most pollsters already were weighting on recalled vote by my count.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#13</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**assumption** · 2026 midterms outlook · explicit

Silver Bulletin expects even fewer 2026 polls to lack a partisanship control (recalled vote, party registration, or similar). Ann Selzer's Iowa miss is cited as evidence that minimal-weighting approaches no longer work.

> Ann Selzer’s miss in Iowa gave pollsters even more evidence that the old-school, minimal-weighting approach just doesn’t work anymore.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#14</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**method** · general principle · explicit

Pollsters have proposed variant partisan controls:
- Cohn suggests weighting on past vote using a pollster's prior three polls rather than the last election's result.
- Jackson suggests weighting only the skewed subgroups (e.g., white voters) on recall, since subgroups are rarely equally off.

*Numbers:* prior polls used for recall weighting = three polls (Cohn's proposed approach)

*Why:* These approaches avoid committing to the last election's outcome as the target and prevent extreme outliers.

> pollsters might choose to weight on past vote across their prior three polls.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#15</sub>

### 2025-01-16 · [Polling is becoming more of an art than a science](https://www.natesilver.net/p/polling-is-becoming-more-of-an-art)
**method** · general principle · explicit

Public media polls typically fix a weighting scheme in advance for transparency, while private pollsters adjust dynamically. AtlasIntel dynamically adjusts sampling and weights based on changing response rates late in the cycle, such as one side's supporters becoming more likely to answer polls.

> So it’s quite important to understand response rates, and based on that analysis, incorporate changes in how you figure out your weights.

<sub>2025-01-16_polling-is-becoming-more-of-an-art-than-a-science#17</sub>

### 2026-01-14 · [Actually, sometimes polls underestimate Democrats](https://www.natesilver.net/p/actually-sometimes-polls-underestimate)
**empirical regularity** · general principle · explicit

In 2025 Virginia, according to State Navigate, pollsters who weighted on recalled vote to the 2021 or 2024 electorate (redder years) were less accurate than those who weighted to a modeled, bluer 2025 electorate. Not weighting on recalled vote at all was less accurate than either option.

> pollsters who weighted to a 2021 or 2024 electorate, which were redder years, were less accurate than pollsters who weighted their data to a modeled (bluer) 2025 electorate

<sub>2026-01-14_actually-sometimes-polls-underestimate-democrats#25</sub>

### 2026-01-22 · [How Silver Bulletin calculates our polling averages](https://www.natesilver.net/p/silver-bulletin-polling-average-methodology)
**method** · Silver Bulletin polling averages (2026) · explicit

When a pollster publishes several versions of one survey, the generic ballot average prefers likely voters over registered voters over all adults, while approval averages prefer the reverse order (with a separate likely-voter-only approval average). All averages prefer versions that include leaners. When a survey has several turnout models or methods, all applicable versions are averaged.

*Why:* Election-oriented measures should reflect the electorate; approval measures the whole public.

> we prioritize polls of likely voters > registered voters > all adults. For approval ratings, the opposite is true

<sub>2026-01-22_how-silver-bulletin-calculates-our-polling-averages#3</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**adjustment rule** · Silver Bulletin 2026 generic ballot average · explicit

When a pollster publishes both likely-voter and registered-voter versions, the generic ballot average uses the likely-voter version. It slightly discounts the weight of registered-voter and all-adult polls but makes no further adjustment to their numbers.

> We do prioritize likely voter polls over registered voter polls when pollsters list both, and slightly discount the weight associated with registered voter polls or polls of all adults.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#2</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**model change** · FLIPR 2026 · explicit

The full FLIPR 2026 midterms model will apply an additional likely-voter adjustment to registered-voter and all-adult polls, which the 'simple' generic ballot average does not do.

*Why:* Midterm turnout is lower, and many registered voters reached by pollsters won't vote.

> Our midterms model will make a further adjustment along these lines, but our “simple” generic ballot average does not.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#3</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**parameter or number** · Silver Bulletin 2026 generic ballot average / FLIPR 2026 · explicit

In January 2026 only about 30% of the weight in the generic ballot average came from likely-voter polls. The authors give an illustration: a 2-point Democratic RV-to-LV 'enthusiasm gap' would put Democrats' likely-voter generic ballot edge at about 7 points, versus the D+5.3 average. The 2-point figure is a hypothetical, not an estimated parameter.

*Numbers:* share of average weight from LV polls = about 30 percent (January 2026 generic ballot average); hypothetical enthusiasm gap = 2 percentage points (illustrative difference between RV and LV polls favoring Democrats); implied LV edge = about 7 percentage points (Democratic generic ballot lead among likely voters)

> Currently, only about 30 percent of the weight in our generic ballot average comes from likely voter polls.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#4</sub>

### 2026-01-22 · [Midterm polls have good news, great news, and bad news for Democrats. Wait, what?](https://www.natesilver.net/p/midterm-polls-have-good-news-great)
**empirical regularity** · general principle / 2026 cycle · explicit

Republicans historically gained when pollsters switched from registered-voter to likely-voter screens. That pattern has now reversed: Democrats do well with highly engaged, college-educated voters and often benefit from lower turnout, so the generic ballot tends to get bluer as more pollsters adopt LV screens.

> Until recently, Republicans tended to gain once pollsters switched over from registered voters to likely voters. But that tendency has now reversed.

<sub>2026-01-22_midterm-polls-have-good-news-great-news-and-bad-news-for-democrats-wait-what#5</sub>

### 2026-04-21 · [SBSQ #31: Trump is super unpopular. So why don’t Democrats have a bigger lead?](https://www.natesilver.net/p/sbsq-31-trump-is-super-unpopular)
**empirical regularity** · Silver analysis, 2026 · explicit

Early-cycle generic ballot polls mostly sample registered voters or all adults, so they miss midterm enthusiasm gaps that likely-voter screens capture. Silver expects the switch to likely-voter screens to favor Democrats in 2026, because the opposition party is usually more enthusiastic and the Democrats' college-educated coalition turns out heavily in non-presidential elections.

> generic ballot polls at this point in the cycle are usually based on polls of registered voters or all adults — not likely voters

<sub>2026-04-21_sbsq-31-trump-is-super-unpopular-so-why-dont-democrats-have-a-bigger-lead#4</sub>

### 2026-06-29 · [Is the vibecession real — or is the survey broken?](https://www.natesilver.net/p/is-the-vibecession-real-or-is-the)
**limitation or failure mode** · general · explicit

Partisan nonresponse can bias a survey even with demographic weighting: in the Michigan rotating panel, more Democrats were recruited and Democrats returned for reinterviews at much higher rates after the web switch, while strong Republicans returned less, giving a sample with about twice as many Democrats as Republicans (net-Democratic share about +30 percent).

*Numbers:* net-Democratic share of ICS sample = +30.1 percent (6-month moving average, 2026)

> Democrats who respond at the reinterview stage return at much higher rates than they did during the phone survey

<sub>2026-06-29_is-the-vibecession-real-or-is-the-survey-broken#2</sub>

### 2026-06-29 · [Is the vibecession real — or is the survey broken?](https://www.natesilver.net/p/is-the-vibecession-real-or-is-the)
**method** · general · explicit

Weighting a survey by party identification is possible using Pew's National Public Opinion Reference Survey (NPORS), an annual address-based, multi-mode, incentivized survey with a high response rate whose microdata are published and used to benchmark other polls.

*Why:* Party ID is an attitude that shifts, so it needs an external high-quality benchmark.

> Published periodically by Pew, NPORS is an annual address-based survey, with paper, online and phone response options and financial incentives.

<sub>2026-06-29_is-the-vibecession-real-or-is-the-survey-broken#3</sub>

### 2026-06-29 · [Is the vibecession real — or is the survey broken?](https://www.natesilver.net/p/is-the-vibecession-real-or-is-the)
**empirical regularity** · general · inferred_from_chart

The phone-to-web mode effect differed by party during the April-June 2024 transition: about -3.9 points for Democrats, -7.0 for Republicans and -16.0 for independents, versus -6.5 for all respondents.

*Numbers:* mode effect, Democrats = -3.9 index points (web vs phone); mode effect, Republicans = -7.0 index points (web vs phone); mode effect, independents = -16.0 index points (web vs phone); mode effect, all = -6.5 index points (web vs phone)

<sub>2026-06-29_is-the-vibecession-real-or-is-the-survey-broken#4</sub>

### 2026-08-11 · [Everything is breaking Democrats’ way. Is it enough to win the Senate?](https://www.natesilver.net/p/everything-is-breaking-democrats-way)
**method** · FLIPR 2026 · explicit

FLIPR applies a likely-voter adjustment to generic ballot polls conducted among registered voters. Following longstanding practice, the adjustment is estimated mainly from polls that publish both LV and RV versions of the same survey. In August 2026 the LV versions were better for Democrats, so FLIPR's generic ballot was D+8.1 versus D+6.7 in the raw average.

*Numbers:* raw generic ballot = D+6.7 points (Aug 11, 2026); FLIPR LV-adjusted generic ballot = D+8.1 points (Aug 11, 2026)

*Why:* Registered-voter polls do not account for turnout.

> the adjustment is based mostly on polls that release both likely and registered voter versions of the same survey.

<sub>2026-08-11_everything-is-breaking-democrats-way-is-it-enough-to-win-the-senate#1</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

FLIPR adjusts every registered-voter or all-adult poll toward what it would show among likely voters, estimated from surveys that publish both versions. The shift is shrunk toward a prior until enough paired polls exist to phase the prior out. In 2026 most paired surveys favored Democrats in the LV version.

> the magnitude of the shift is shrunken toward a prior

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#9</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**model change** · FLIPR 2026 · explicit

FLIPR dropped its old prior that the RV-to-LV shift favors Republicans, because Democrats' college-educated coalition now turns out at high rates. It uses a more neutral prior that is overridden more quickly as paired LV/RV polls arrive.

*Why:* Turnout patterns changed.

> the model has discarded its prior that the shift from registered voters to likely voters typically favors Republicans.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#10</sub>

### 2026-08-11 · [How FLIPR forecasts the midterm elections](https://www.natesilver.net/p/flipr-midterms-model-methodology)
**method** · FLIPR 2026 · explicit

FLIPR also applies the likely-voter adjustment to its own versions of the generic ballot and presidential approval, which Silver Bulletin's regular averages do not. In early August 2026 this moved the generic ballot from about D+6.5 to about D+8.

*Numbers:* default generic ballot = about D+6.5 points (early August 2026); LV-adjusted generic ballot = around D+8 points (early August 2026)

> FLIPR also applies the likely voter adjustment to its averages of the generic ballot and presidential approval, which our regular averages do not.

<sub>2026-08-11_how-flipr-forecasts-the-midterm-elections-by-nate-silver#12</sub>

### 2026-08-20 · [Are Democrats on a summer sugar high?](https://www.natesilver.net/p/are-democrats-on-a-summer-sugar-high)
**empirical regularity** · FLIPR 2026 · explicit

Much of the historical Democratic bias in midterm summer polls reflected lower Democratic turnout captured only when pollsters switched to likely-voter screens. FLIPR and its predecessors always applied an LV adjustment for this. The Republican turnout advantage may now have flipped because Democrats' college-educated coalition votes reliably in midterms.

> FLIPR and its various predecessors have therefore always made a likely-voter adjustment

<sub>2026-08-19_are-democrats-on-a-summer-sugar-high-by-nate-silver#12</sub>

### 2026-08-25 · [Do I really buy that Texas could turn blue?](https://www.natesilver.net/p/do-i-really-buy-that-texas-could)
**parameter or number** · FLIPR 2026 · explicit

The standard generic ballot page put Texas's benchmark at R+4.2, but FLIPR uses a likely-voter-adjusted generic ballot that favored Democrats in 2026, bringing the Texas simple-fundamentals benchmark closer to R+3.

*Numbers:* Texas benchmark, standard generic ballot = R+4.2 points (Aug 2026); Texas benchmark, FLIPR LV-adjusted = closer to R+3 points (Aug 2026)

> Our generic ballot page pegs Texas at R +4.2, but FLIPR uses a version of the generic ballot that makes a likely-voter adjustment.

<sub>2026-08-25_do-i-really-buy-that-texas-could-turn-blue#1</sub>

### 2026-10-03 · [What if the polls are wrong again?](https://www.natesilver.net/p/what-if-the-polls-are-wrong-again)
**empirical regularity** · general · explicit

A truly random sample is impossible today: people screen calls and online panels cannot be randomly pinged. Pollsters weight demographically (e.g. education, race) to correct nonresponse, but partisan and enthusiasm-driven nonresponse is a mixed bag because self-selection also acts as a de facto likely-voter screen. Silver calls the 2024 Selzer Iowa poll the last gasp of traditional telephone polls that made little effort to correct for partisan nonresponse.

> The dirty little secret of polling these days is that it’s impossible to get a truly random sample of voters.

<sub>2026-10-03_what-if-the-polls-are-wrong-again-by-nate-silver#11</sub>

### 2026-10-20 · [My pet peeve about the polling error debate](https://www.natesilver.net/p/my-pet-peeve-about-the-polling-error)
**empirical regularity** · general · explicit

Pollsters combat partisan nonresponse by matching to Census demographics, anchoring to past reported vote, tweaking likely-voter models, and sometimes herding or withholding outliers. Non-college and low-social-trust voters, who lean Republican, respond less. Enthusiasm cuts both ways, since enthusiastic respondents both answer polls and vote: it may explain El-Sayed's primary overestimate, while in 2014 the enthusiasm gap exceeded pollsters' expectations.

> They can match to Census Bureau demographics, or they can anchor to the past reported vote.

<sub>2026-10-20_my-pet-peeve-about-the-polling-error-debate#6</sub>

### 2026-11-03 · [It's Judgment Day for Trump (and for pollsters)](https://www.natesilver.net/p/its-judgment-day-for-trump-and-for)
**limitation or failure mode** · general · explicit

Some pollsters worried that voters were misreporting past Trump votes because he had become unpopular; if so, polls weighting to recalled past vote could overrate Republicans by a point or two by miscounting Trump voters as Harris or other voters.

*Numbers:* possible past-vote weighting bias = a point or two points toward R (2026)

> If so, polls that weight toward past vote recall could be overrating Republicans by a point or two

<sub>2026-11-03_its-judgment-day-for-trump-and-for-pollsters#5</sub>

### 2026-11-03 · [Who’s ahead on the generic congressional ballot?](https://www.natesilver.net/p/generic-ballot-average-2026-nate-silver-bulletin-congress-polls)
**method** · Silver Bulletin generic ballot average 2026 · explicit

The default generic ballot average combines polls of adults, registered voters and likely voters. When a pollster releases multiple versions, it prefers likely voters, then registered voters, then adults, because the target is people who plan to vote.

> If a pollster releases multiple versions of the same survey, we use the likely voter version before the registered voter version.

<sub>2026-11-03_generic-congressional-ballot-latest-polls-silver-bulletin#1</sub>
