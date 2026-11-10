# Fundamentals economy

43 findings from 22 articles, oldest first.

### 2016-06-29 · [A User’s Guide To FiveThirtyEight’s 2016 General Election Forecast](https://fivethirtyeight.com/features/a-users-guide-to-fivethirtyeights-2016-general-election-forecast/)
**parameter or number** · FiveThirtyEight 2016 presidential · explicit

The 2016 economic index averaged six normalized, equally weighted variables over the past year: nonfarm payrolls, industrial production, real personal income, PCE, CPI and the S&P 500. In the fundamentals forecast, an index 0.5 standard deviations above average implied the incumbent party winning nationally by 4 to 5 points. An elected-incumbent variable was neutral in 2016.

*Numbers:* national margin per 0.5 SD economy = 4 to 5 percentage points (2016 fundamentals)

> if the economic index was 0.5 standard deviations above average, it would have the incumbent party winning by 4 to 5 percentage points nationally.

<sub>fte_2016-general-election-forecast-users-guide#16</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

The FiveThirtyEight economic index, used since 2012, has six variables: nonfarm payrolls (jobs), real personal consumption expenditures (spending), real disposable personal income (income), industrial production (manufacturing), CPI (inflation) and the S&P 500 (stock market). Each is standardized to roughly equal mean and standard deviation over data since 1946, measured over the two years before the election with much heavier weight on roughly the final six months, and calibrated on vintage real-time data where possible.

*Numbers:* number of economic variables = 6 variables (2020 index); lookback window = 2 years (heavier weight on last ~6 months)

*Why:* Equal-weighted blend avoids p-hacking among many economic measures.

> All variables are standardized so that they have roughly the same mean and standard deviation

<sub>fte_2020-presidential-forecast-methodology#14</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**parameter or number** · FiveThirtyEight 2020 presidential · explicit

The economic index is a z-score (0 is an average economy) extended approximately to 1880. Election Day values include 1932 -2.34, 1980 -1.71, 2008 -1.34, 1920 -1.52, 1936 +1.55, 1880 +1.37, 1984 +0.86, 1964 +0.70, 2012 -0.10 and 2016 +0.08. The economy explains only about 30 percent of the variation in incumbent-party performance.

*Numbers:* 1932 index = -2.34 z-score; 2008 index = -1.34 z-score; variance explained by economy = around 30 percent (incumbent party performance)

*Why:* Expanding the sample matters even with less reliable early data.

> In fact, we found that the economy explains only around 30 percent of the variation in the incumbent party’s performance

<sub>fte_2020-presidential-forecast-methodology#15</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**method** · FiveThirtyEight 2020 presidential · explicit

The model forecasts each of the six economic variables to Election Day with some mean reversion, using recent stock market performance, which has some predictive power, and surveys of professional economists.

*Why:* Conditions at forecast time may not resemble November.

> the model makes a simple forecast for each of the six economic variables, which accounts for some mean-reversion

<sub>fte_2020-presidential-forecast-methodology#17</sub>

### 2020-08-12 · [How FiveThirtyEight’s 2020 Presidential Forecast Works — And What’s Different Because Of COVID-19](https://fivethirtyeight.com/features/how-fivethirtyeights-2020-presidential-forecast-works-and-whats-different-because-of-covid-19/)
**critique of other approach** · general principle · explicit

Silver considers fundamentals-only presidential models overrated: with many ways to measure the economy and few elections, it is easy to p-hack. Their telltale failure is fitting past elections well and predicting unknown ones poorly; one Q2-GDP model implied Biden would win nearly 1,000 electoral votes in 2020.

> it’s easy to “p-hack” your way to glory with these models because there are so many ways to measure “the economy” but only a small sample size of elections

<sub>fte_2020-presidential-forecast-methodology#19</sub>

### 2023-12-07 · [The incumbency advantage is disappearing. Maybe it's the algorithms' fault.](https://www.natesilver.net/p/the-incumbency-advantage-is-disappearing)
**assumption** · general principle · implied

Silver leans toward explaining weak consumer sentiment in 2023 through fundamentals, especially cumulative inflation under Biden, rather than media 'vibes'. This suggests economic fundamentals should include inflation, not just labor-market strength.

*Why:* Inflation was very high through most of Biden's term, even though it has since abated.

> I lean more toward the “this is explicable through fundamentals” side of the argument

<sub>2023-12-07_the-incumbency-advantage-is-disappearing-maybe-its-the-algorithms-fault#6</sub>

### 2024-06-26 · [2024 presidential election model methodology update](https://www.natesilver.net/p/model-methodology-2024)
**parameter or number** · 2024 presidential · explicit

Under both the old and new incumbency/economy formulas, the fundamentals gave Biden a 2-3 point popular-vote advantage based on projected economic conditions as of June 2024. The formula change had negligible effect in 2024.

*Numbers:* Biden fundamentals popular-vote advantage = 2 to 3 percentage points (June 2024)

> Biden is assumed to have a 2 to 3 point advantage in the popular vote based on projected economic conditions as of June 2024

<sub>2024-06-26_2024-presidential-election-model-methodology-update#19</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**parameter or number** · 2024 presidential · explicit

In the 2024 Silver Bulletin model, fundamentals made up about 30 percent of the forecast in late June 2024 and polls about 70 percent. The fundamentals weight gradually fades to zero by Election Day.

*Numbers:* fundamentals weight = about 30 percent (June 26, 2024); polls weight = 70 percent (June 26, 2024); fundamentals weight on Election Day = 0 percent (Election Day)

*Why:* Fundamentals models are prone to overfitting given small samples.

> the fundamentals currently account for about 30 percent of the forecast, as compared to 70 percent for the polls, and this will gradually fade to zero by Election Day

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#2</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**method** · 2024 presidential · explicit

In the Silver Bulletin presidential model, 'fundamentals' means only the economy and incumbency.

> the fundamentals part of our model — which in the case of the Silver Bulletin, just means the economy and incumbency

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#3</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**design principle** · general principle · explicit

Silver cautions against putting much weight on macro fundamentals. They have many possible specifications and few relevant elections, so they often overfit and replicate poorly out of sample. Fancy statistical techniques meant to prevent overfitting can actually make it worse.

*Why:* Small sample size of elections and many researcher degrees of freedom.

> data scientists often talk themselves into thinking they’re avoiding overfitting by using some fancy statistical techniques when they’re actually making it worse

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#4</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**method** · 2024 presidential · explicit

The Silver Bulletin economic index uses six indicators, each expressed as a z-score from the incumbent party's standpoint (higher is better for the incumbent), and averages them. The indicators are real disposable personal income, the consumer price index, nonfarm payrolls, industrial production, personal consumption expenditures and the S&P 500.

*Numbers:* number of indicators = 6 indicators (economic index)

> These z-scores are evaluated from the standpoint of the incumbent party — higher is better for Biden

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#5</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**parameter or number** · 2024 presidential · inferred_from_chart

Economic index z-scores at June 26, 2024 launch, with projections for Nov. 5. The six-indicator average is projected at +0.04.

*Numbers:* Real disposable personal income = -0.68 current / -0.75 projected z-score (June 26, 2024); CPI = +0.01 / +0.40 z-score (June 26, 2024); Nonfarm payrolls = +0.32 / +0.28 z-score (June 26, 2024); Industrial production = -0.28 / -0.11 z-score (June 26, 2024); PCE = -0.05 / -0.14 z-score (June 26, 2024); S&P 500 = +1.10 / +0.58 z-score (June 26, 2024); Average = +0.07 / +0.04 z-score (June 26, 2024)

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#6</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**method** · 2024 presidential · explicit

The economic index does not use actual GDP because it is updated only quarterly. It does use forecasted GDP from the Survey of Professional Forecasters to help project the other indicators forward to Election Day.

*Why:* GDP is only updated quarterly.

> It does use forecasted GDP from the Survey of Professional Forecasters to help predict changes in the other indicators.

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#7</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**empirical regularity** · general principle · explicit

Real disposable (take-home) income growth is historically among the best economic variables at predicting election outcomes.

> real take-home incomes, historically among the best economic variables at predicting election outcomes

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#8</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**interpretation guidance** · 2024 presidential · implied

By June 2024, the 2021-2023 high-inflation period was far enough in the past that it did not really hurt Biden in the model. This implies the economic index measures recent changes or a lookback window rather than cumulative price levels.

> the period of very high inflation is enough in the rearview mirror to not really hurt Biden in the model

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#9</sub>

### 2024-06-26 · [The presidential election isn't a toss-up](https://www.natesilver.net/p/the-presidential-election-isnt-a)
**parameter or number** · 2024 presidential · explicit

In June 2024 the fundamentals projected Biden to win the national popular vote by 2 to 3 points (about 2.5). Because of his Electoral College disadvantage, that margin alone would make the race roughly a toss-up.

*Numbers:* fundamentals popular vote margin = 2 to 3 percentage points (Biden, June 2024)

> they currently project him to win the popular vote by 2 to 3 percentage points

<sub>2024-06-26_the-presidential-election-isnt-a-toss-up-by-nate-silver#14</sub>

### 2024-06-27 · [Are these guys trying to muddle through? Or playing to win?](https://www.natesilver.net/p/are-these-guys-trying-to-muddle-through)
**data source** · 2024 presidential · implied

New economic reports are an input that can materially change the Silver Bulletin 2024 presidential forecast. This implies that economic data enter the model, for example through a fundamentals component.

> some other data (such as a new economic report) that materially affects the model

<sub>2024-06-27_are-these-guys-trying-to-muddle-through-or-playing-to-win#1</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**parameter or number** · 2024 presidential · explicit

The fundamentals component of the Silver Bulletin presidential model is calibrated on elections going back to 1880.

*Numbers:* fundamentals calibration start = 1880 year (start of the fundamentals calibration sample)

> The "fundamentals" part goes even further back — to 1880.

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#2</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**method** · 2024 presidential · explicit

In the Silver Bulletin 2024 presidential model, the fundamentals prior consists of the economy and incumbency.

> “fundamentals” (which in our case consist of the economy and incumbency)

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#2</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**empirical regularity** · general principle · explicit

Election models based on fundamentals alone have a poor out-of-sample track record, doing not much better than a random guess.

> Models based on fundamentals alone have a poor out-of-sample track record, not doing much better than a random guess.

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#22</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**method** · 2024 presidential · inferred_from_chart

The 2024 Silver Bulletin economic index combines six indicators: real disposable personal income, the consumer price index, nonfarm payrolls, industrial production, personal consumption expenditures, and the S&P 500. Each is standardized as a z-score, where 0 is an average economy and positive is better than average, and the index is the average of all six.

*Numbers:* number of economic indicators = 6 indicators (2024 fundamentals); economic index current = +0.09 z-score (July 21, 2024); economic index projected Nov 5 = +0.07 z-score (July 21, 2024)

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#13</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**method** · 2024 presidential · inferred_from_chart

The economic index uses readings of the six indicators over the two years before the election, weighting more recent data more heavily. The model also projects each indicator forward to Election Day (Nov. 5).

*Numbers:* lookback window = two years years (economic index)

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#14</sub>

### 2024-07-29 · [Silver Bulletin 2024 Biden-Trump forecast archive](https://www.natesilver.net/p/silver-bulletin-2024-biden-trump)
**parameter or number** · 2024 presidential · inferred_from_chart

Economic indicator z-scores on July 21, 2024, shown as current then projected to Nov. 5: real disposable personal income −0.62 then −0.65; CPI +0.13 then +0.45; nonfarm payrolls +0.27 then +0.22; industrial production −0.13 then +0.02; PCE −0.17 then −0.23; S&P 500 +1.06 then +0.64.

*Numbers:* RDPI = -0.62 / -0.65 z-score (current / projected); CPI = +0.13 / +0.45 z-score (current / projected); Nonfarm payrolls = +0.27 / +0.22 z-score (current / projected); Industrial production = -0.13 / +0.02 z-score (current / projected); PCE = -0.17 / -0.23 z-score (current / projected); S&P 500 = +1.06 / +0.64 z-score (current / projected)

<sub>2024-07-29_silver-bulletin-2024-biden-trump-forecast-archive#15</sub>

### 2024-07-31 · [How the election model handles a candidate swap](https://www.natesilver.net/p/how-the-election-model-handles-a)
**data source** · 2024 presidential · explicit

Uncertainty index factor 5 is economic uncertainty, meaning how much the economy is expected to change before the election. It is based on a Federal Reserve survey of economists and was unchanged by the swap.

> Factor 5 is economic uncertainty, which is basically based on how much the model expects the economy to change between now and the election based on a Federal Reserve survey of economists.

<sub>2024-07-31_how-the-election-model-handles-a-candidate-swap#22</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**method** · 2024 presidential · explicit

Until one day before the election, the Silver Bulletin forecast is not purely polls-based. It combines the polls with a 'fundamentals' prior based on incumbency and the Silver Bulletin economic index.

> it combines the polls with a “fundamentals” prior based on incumbency and our economic index

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#15</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**parameter or number** · 2024 presidential · explicit

As of Aug. 31, 2024, the fundamentals prior received about 20% of the weight and was gradually being phased out, reaching zero by Election Day. The prior implied a roughly tied national popular vote versus Harris +3 to +4 in national polls, and it shaved a net ~0.4 points off Harris's projected Election Day margin.

*Numbers:* fundamentals weight = about 20 percent (late August 2024, ~9-10 weeks before Election Day); fundamentals prior popular vote = roughly a tie (late August 2024); recent national polls = Harris +3 or 4 points (late August 2024); net effect on Harris projection = about four-tenths of a point percentage points (late August 2024); fundamentals weight on Election Day = 0 percent (one day before the election onward)

> they still get about 20 percent of the weight for now, which is shaving a net of about four-tenths of a point off of Harris’s projected finish on Election Day

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#16</sub>

### 2024-09-03 · [There’s no “normal” in this election](https://www.natesilver.net/p/theres-no-normal-in-this-election)
**assumption** · 2024 presidential · explicit

The 2024 fundamentals prior is based on an approximately average economy and no true incumbent in the race. It projects a tied national popular vote, with Democrats as underdogs in the Electoral College.

*Numbers:* fundamentals popular vote margin = 0 (tie) percentage points (2024)

> based on the economy being about average and there being no true incumbent in the race, is that "normal" means a tie in the popular vote but Democrats being underdogs in the Electoral College.

<sub>2024-09-03_theres-no-normal-in-this-election-by-nate-silver#11</sub>

### 2024-09-07 · [Oops! I made the convention bounce adjustment disappear.](https://www.natesilver.net/p/oops-i-made-the-convention-bounce)
**parameter or number** · 2024 presidential · explicit

As of early September 2024, about 18% of the Silver Bulletin presidential forecast was still based on the fundamentals calculation, which combines incumbency and an economic index. The polls carried the remaining weight.

*Numbers:* fundamentals weight = About 18 percent (forecast as of Sept 6-7, 2024, about two months before election)

> About 18 percent of the forecast is still based on our "fundamentals" calculation — basically, the combination of incumbency

<sub>2024-09-07_oops-i-made-the-convention-bounce-adjustment-disappear#5</sub>

### 2024-09-07 · [Oops! I made the convention bounce adjustment disappear.](https://www.natesilver.net/p/oops-i-made-the-convention-bounce)
**method** · 2024 presidential · explicit

The 2024 model's economic index updates as economic data arrive, including revisions. Downward revisions to jobs numbers lowered the index slightly in early September 2024, which hurt Harris.

> our economic index is slightly down in recent days, in part because of downward revisions to jobs numbers

<sub>2024-09-07_oops-i-made-the-convention-bounce-adjustment-disappear#7</sub>

### 2024-09-07 · [Oops! I made the convention bounce adjustment disappear.](https://www.natesilver.net/p/oops-i-made-the-convention-bounce)
**parameter or number** · 2024 presidential · explicit

In early September 2024, the fundamentals formula had Harris losing the national popular vote by 0.3 percentage points. Silver says this very likely translates into a Democratic loss in the Electoral College, given the Democrats' Electoral College disadvantage.

*Numbers:* fundamentals popular vote margin = -0.3 percentage points (Harris margin, Sept 2024)

> it has Harris losing the popular vote by 0.3 percentage points — which very likely translates into a loss for Democrats in the Electoral College

<sub>2024-09-07_oops-i-made-the-convention-bounce-adjustment-disappear#8</sub>

### 2024-09-26 · [Pigs fly. Hell freezes over. The Electoral College favors ... Democrats?](https://www.natesilver.net/p/pigs-fly-hell-freezes-over-the-electoral)
**method** · 2024 presidential · explicit

The Silver Bulletin forecast differs from its polling average in two ways. It incorporates a 'fundamentals' prior based on the economy and incumbency. It also blends the polling average with a regression that infers each state's result from national polls and polls of other states.

> incorporating a “fundamentals” prior based on the economy and incumbency, and blending our polling averages with a regression analysis that makes inferences about the race from national polls and polls of other states

<sub>2024-09-26_pigs-fly-hell-freezes-over-the-electoral-college-favors-democrats#3</sub>

### 2024-10-01 · [SBSQ #13: October Surprise edition](https://www.natesilver.net/p/sbsq-13-october-surprise-edition)
**limitation or failure mode** · 538 2024 (original) · explicit

According to 538's own admission, the old 538 2024 model could deviate from the polls because it did not explicitly dictate how much weight to put on polls versus fundamentals. The lesson for replication is that a model should specify the polls-vs-fundamentals weighting explicitly.

*Why:* Without an explicit weighting, the model's estimates drifted away from the polls once the polls moved away from the fundamentals.

> This divergence was possible because the old model did not explicitly dictate how much weight to put on polls versus fundamentals.

<sub>2024-10-01_sbsq-13-october-surprise-edition-by-nate-silver#1</sub>

### 2024-10-08 · [55/45 is a really close race](https://www.natesilver.net/p/5545-is-a-really-close-race)
**method** · 2024 presidential · implied

Economic data feed into the Silver Bulletin 2024 presidential forecast. Economic headwinds in late August and early September 2024 contributed to the forecast drifting toward Trump, and later data were better.

> plus some economic headwinds (there's since been better data)

<sub>2024-10-08_5545-is-a-really-close-race-by-nate-silver#5</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**parameter or number** · 2024 presidential · explicit

As of Oct. 17, 2024, the Silver Bulletin economic index implied that Harris 'should' win the national popular vote by roughly 1 percentage point.

*Numbers:* fundamentals-implied popular vote margin = roughly 1 percentage points (Harris) (Economic index as of Oct. 17, 2024)

> our current economic index implies that Harris “should” win the popular vote by roughly 1 percentage point

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#11</sub>

### 2024-10-17 · [Does Trump have momentum?](https://www.natesilver.net/p/does-trump-have-momentum)
**interpretation guidance** · 2024 presidential · explicit

Polling moves toward the fundamentals baseline can be read as mean reversion rather than momentum. Silver views Trump's October 2024 gains as the race returning to a fundamentals-implied baseline after Harris's strong debate, which had inflated her national lead to 3-3.5 points.

*Numbers:* Harris peak national polling lead = 3 or 3.5 percentage points (After the September 2024 debate)

> Trump’s recent gains in the polls are actually not “momentum” but mean reversion, the race returning to its natural baseline after Harris’s strong debate

<sub>2024-10-17_does-trump-have-momentum-by-nate-silver#13</sub>

### 2024-11-03 · [A shocking Iowa poll means somebody is going to be wrong](https://www.natesilver.net/p/a-shocking-iowa-poll-means-somebody)
**empirical regularity** · general principle · explicit

Silver reports a statistically significant correlation between state-level inflation since Biden took office and the 2020-to-2024 shifts shown in polls. Harris held up in the low-inflation Midwest (except high-inflation Minnesota) and in North Carolina, but lost ground in high-inflation Florida, Nevada, Arizona, New York and Virginia. This geographic inflation effect is not described as a model input.

*Why:* Possible mechanism for regionally varying swings.

> this is conspicuously (and statistically significantly!) well-correlated with where the polls have shown shifts from 2020.

<sub>2024-11-02_a-shocking-iowa-poll-means-somebody-is-going-to-be-wrong#22</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**parameter or number** · 2024 presidential · inferred_from_chart

In the 2024 Silver Bulletin model, the polls-based 'snapshot' is blended with economic fundamentals. On Election Day the fundamentals weight was 0.00, so the projected vote share equaled the snapshot. The fundamentals estimate in Arizona was 47.4/51.6, more favorable to Trump than the polls.

*Numbers:* fundamentals blend weight AZ = 0.00 weight (Nov 5 2024); economic fundamentals estimate AZ = 47.4% Harris / 51.6% Trump vote share (Nov 5 2024)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#16</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**method** · 2024 presidential · inferred_from_chart

The Silver Bulletin Economic Index (SBEI) averages z-scores of six indicators: real disposable personal income, consumer price index, nonfarm payrolls, industrial production, personal consumption expenditures, and the S&P 500. Variables are standardized to roughly the same mean and standard deviation; zero is an average economy. Readings cover the two years before the election, with heavier weight on recent data, and are projected forward to Election Day.

*Numbers:* number of indicators = 6 (SBEI); lookback window = 2 years (SBEI)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#18</sub>

### 2024-11-05 · [FINAL Silver Bulletin 2024 presidential election forecast](https://www.natesilver.net/p/nate-silver-2024-president-election-polls-model)
**parameter or number** · 2024 presidential · inferred_from_chart

Final 2024 SBEI z-scores were: RDPI −0.21, CPI +0.48, nonfarm payrolls +0.07, industrial production −0.43, PCE +0.24, S&P 500 +0.91, for an average of +0.18. That means a slightly above-average economy.

*Numbers:* RDPI = -0.21 z-score (Nov 5 2024); CPI = +0.48 z-score (Nov 5 2024); nonfarm payrolls = +0.07 z-score (Nov 5 2024); industrial production = -0.43 z-score (Nov 5 2024); PCE = +0.24 z-score (Nov 5 2024); S&P 500 = +0.91 z-score (Nov 5 2024); SBEI average = +0.18 z-score (Nov 5 2024)

<sub>2024-11-05_final-silver-bulletin-2024-presidential-election-forecast#19</sub>

### 2024-11-26 · [SBSQ #15: Democrats have a "fool me twice" problem](https://www.natesilver.net/p/sbsq-15-democrats-have-a-fool-me)
**design principle** · 2024 presidential · explicit

Silver believes a backtest of 'polls, plus a bit of fundamentals even on Election Day' would beat 'just polls'. He keeps zero Election Day weight anyway because the backtest gain may reflect overfitting: there are many ways to specify the fundamentals, which creates room for p-hacking even when you are trying to avoid it.

*Why:* The concern is overfitting and p-hacking across fundamentals specifications.

> I’m pretty sure that if you backtested “just polls” versus “polls, plus a bit of fundamentals even on Election Day”, the latter would do better. But one question is whether that reflects some degree of overfitting

<sub>2024-11-26_sbsq-15-democrats-have-a-fool-me-twice-problem#11</sub>

### 2025-05-06 · [We're tracking more data on Trump's popularity](https://www.natesilver.net/p/were-tracking-more-data-on-trumps)
**limitation or failure mode** · general principle · explicit

Consumer data could serve as a proxy for economic approval, but 'soft' data such as consumer confidence and 'hard' data such as consumer spending have diverged.

> there's been a split between "soft" data like consumer confidence numbers and "hard" data like consumer spending

<sub>2025-05-06_were-tracking-more-data-on-trumps-popularity#14</sub>

### 2026-06-29 · [Is the vibecession real — or is the survey broken?](https://www.natesilver.net/p/is-the-vibecession-real-or-is-the)
**limitation or failure mode** · general (economic indicator data quality) · explicit

Since its 2024 switch from phone to web, the University of Michigan consumer sentiment index has shown a persistent downward level shift of nearly 9 points, even though phone and web series correlated at 0.97 during the overlap. A high time-series correlation does not rule out a level shift, so ICS data since mid-2024 is not comparable with earlier periods.

*Numbers:* mode-shift level change = nearly 9 index points (web vs phone, Tedeschi and Cummings); phone-web correlation = .97 correlation (Michigan overlap period)

> A high time-series correlation only means the phone and web series moved together; it does not rule out a persistent level shift

<sub>2026-06-29_is-the-vibecession-real-or-is-the-survey-broken#0</sub>

### 2026-06-29 · [Is the vibecession real — or is the survey broken?](https://www.natesilver.net/p/is-the-vibecession-real-or-is-the)
**empirical regularity** · general · explicit

The partisan gap in consumer sentiment, the president's party's advantage controlling for demographics, has grown from about 15 points under George W. Bush to over 20 under Obama's second term, 38 in Trump's first term, about 34 under Biden, and nearly 53 in Trump's second term.

*Numbers:* partisan sentiment gap, G.W. Bush = 14.9 index points (from chart); Obama II = 21.5 index points (from chart); Trump I = 37.9 index points (from chart); Biden = 33.6 index points (from chart); Trump II = 52.8 index points (from chart)

*Why:* Partisan expressive responding has intensified.

> But so far during Trump’s second term, the gap between partisans equates to nearly 53 points of consumer sentiment.

<sub>2026-06-29_is-the-vibecession-real-or-is-the-survey-broken#1</sub>
