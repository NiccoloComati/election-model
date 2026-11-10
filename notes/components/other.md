# Other

10 findings from 8 articles, oldest first.

### 2023-09-20 · [The election model is a little too popular](https://www.natesilver.net/p/the-election-model-is-a-little-too)
**design principle** · general principle · explicit

Silver defends probabilistic election forecasting as one of the fundamental ways to test whether one's view of the world is accurate. He considers most critiques of such forecasting ill-considered.

*Why:* Journalists ought to be concerned with accuracy.

> forecasting is one of the fundamental ways to test whether your view of the world is accurate

<sub>2023-09-20_the-election-model-is-a-little-too-popular-by-nate-silver#6</sub>

### 2024-06-27 · [Are these guys trying to muddle through? Or playing to win?](https://www.natesilver.net/p/are-these-guys-trying-to-muddle-through)
**method** · 2024 presidential · explicit

The Silver Bulletin 2024 presidential model was originally planned to update once a week until Labor Day. Instead it is updated most of the time when interesting polling or other data, such as a new economic report, materially affects the model. In practice this means a few updates a week.

*Numbers:* original update frequency = once a week (original plan until Labor Day 2024); practical update frequency = a few updates per week (summer 2024)

*Why:* The team found it could do better than weekly updates.

> we'll try to get you an update most of the time once there's interesting polling or some other data (such as a new economic report) that materially affects the model

<sub>2024-06-27_are-these-guys-trying-to-muddle-through-or-playing-to-win#0</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**design principle** · general principle · explicit

Model builders face a trade-off between rigid empiricism and assumptions tailored to the present environment. Academics favor buttoned-up assumptions that assess conditions in historical context. Bettors care only about predictive value and accept fuzzy assumptions if the model makes money.

> there's a trade-off between being more rigidly empirical, and building in more assumptions that potentially make a model more suited to the present environment, but also complicate the epistemology

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#16</sub>

### 2024-07-01 · [SBSQ #10: Everything you always wanted to know about the election model but were afraid to ask](https://www.natesilver.net/p/sbsq-10-everything-you-always-wanted)
**critique of other approach** · general · explicit

Silver says all current forecast models are basically reasonable, and that models with truly indefensible assumptions were weeded out after 2016.

> The ones that made truly indefensible assumptions were weeded out after 2016.

<sub>2024-07-01_sbsq-10-everything-you-always-wanted-to-know-about-the-election-model-but-were-a#35</sub>

### 2024-07-18 · [Why I don't buy 538's new election model](https://www.natesilver.net/p/why-i-dont-buy-538s-new-election)
**design principle** · general principle · explicit

When blending two or more components into an average, a model should place more weight on the more reliable component. 538's fundamentals error bar is wider than its polling error bar, yet it seemingly gives fundamentals 85 percent of the weight.

*Why:* Inverse-variance logic.

> it’s almost axiomatic that if you’re blending two or more components into an average, you’ll want to place more weight on the more reliable component

<sub>2024-07-18_why-i-dont-buy-538s-new-election-model-by-nate-silver#16</sub>

### 2024-08-24 · [We removed RFK Jr. from our model. But it didn’t hurt Kamala.](https://www.natesilver.net/p/we-removed-rfk-jr-from-our-model)
**design principle** · general principle · explicit

Mid-campaign changes to a model should be minimally invasive. Ad-hoc, election-specific fixes should be avoided when the model's preexisting logic offers a solution. Silver frames this partly as a critique of competitors.

> changes to a model in the midst of a campaign should be minimally invasive.

<sub>2024-08-24_we-removed-rfk-jr-from-our-model-but-it-didnt-hurt-kamala#15</sub>

### 2024-08-31 · [SBSQ #12: Will the polls lowball Trump again?](https://www.natesilver.net/p/sbsq-12-will-the-polls-lowball-trump)
**parameter or number** · 2024 presidential · explicit

The Silver Bulletin presidential model is several thousand lines of code.

*Numbers:* code size = several thousand lines of code (2024 model)

> it’s several thousand lines of code

<sub>2024-08-31_sbsq-12-will-the-polls-lowball-trump-again#25</sub>

### 2024-09-07 · [Oops! I made the convention bounce adjustment disappear.](https://www.natesilver.net/p/oops-i-made-the-convention-bounce)
**design principle** · general principle · explicit

A model's rules should be set ahead of time to avoid ad hoc adjustments that might reflect the modeler's political leanings or what readers want. Silver keeps the full bounce adjustment despite doubts for this reason.

*Why:* Precommitment guards against bias; Silver notes he plans to vote for Harris and his readers lean ~3:1 Harris.

> The whole point of building a model is that you set up rules ahead of time so you aren't tempted to make ad hoc adjustments, which might reflect your political leanings or what your readers want.

<sub>2024-09-07_oops-i-made-the-convention-bounce-adjustment-disappear#21</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**critique of other approach** · general principle · explicit

Silver argues that machine learning is inappropriate for election modeling except under three conditions: (a) very large data, millions of observations or more, versus the dozens to thousands typical of elections; (b) ambiguous relationships among variables, whereas politics has a finite list of well-specified factors such as incumbency, moderation and presidential vote; and (c) priority on prediction over causal explanation.

*Numbers:* data size suited to ML = millions or more observations (threshold for ML); typical election data size = dozens to thousands observations (election analysis)

*Why:* Small, structured datasets favor classical inference guided by domain knowledge.

> not the dozens or hundreds or at best thousands of observations that you're usually limited to in election analysis

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#17</sub>

### 2025-08-20 · [Real talk on models, moderation, and the misuse of academic authority](https://www.natesilver.net/p/real-talk-on-models-moderation-and)
**critique of other approach** · B&G BG-WAR · explicit

Silver describes B&G's glmnet approach as essentially lasso regression, which on small datasets is a close cousin of stepwise regression. He says automated variable selection is unsophisticated and generally inferior to choices made by an experienced researcher with domain knowledge.

> it's a form of lasso regression, which when applied to a small dataset like this, is a kissing cousin of the much-derided stepwise regression.

<sub>2025-08-20_real-talk-on-models-moderation-and-the-misuse-of-academic-authority#18</sub>
