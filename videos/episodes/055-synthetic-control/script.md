# 055 · Building a Fake California to Measure a Real Law

**One idea:** to measure a policy that hit one place, build that place's "no-policy" twin as a
weighted blend of untreated places chosen to match its past; the gap after the policy is the
effect, and running the same recipe on every untreated place tells you whether the gap is unusual.

Data: per-capita cigarette sales (packs per person per year), 39 US states, 1970-2000, as used by
Abadie, Diamond & Hainmueller (2010, JASA). Synthetic-California weights are the paper's published
Table 2 weights. Placebo gaps are our own re-fit (sales path only), labelled on screen.

## Palette (colour -> one meaning)

| Colour | Meaning |
|---|---|
| BLUE | real California (its sales line, its gap line) |
| YELLOW | synthetic California: the counterfactual, its weights, its formula term |
| PURPLE | naive comparison units (38-state average, then Montana alone) |
| RED | pre-1988 miss: how badly a comparison fails to match California before the law |
| GREEN | estimated effect of the law (post-1988 gap credited to the law) |
| GRAY / DIM | axes, donor states, placebo states |

## Beats (narration, ~470 words)

**1 · Cold open (0:00-0:16)** — axes; blue California line draws 1970 -> 1988; Prop 99 marker; line continues to 2000; bracket 90.1 -> 41.6.
> This blue line is cigarette sales in California, in packs per person per year. In nineteen eighty-eight, voters passed Proposition ninety-nine: a twenty-five cent tax on every pack, plus anti-smoking campaigns. By two thousand, sales had fallen from ninety packs to about forty-two. That's a drop of almost forty-nine packs. How many of them did the law cause? [pause 1.5]

**2 · Stakes** — the pre-1988 slope flags; a yellow dashed stub with "?" leaves the 1988 point.
> Sales were already falling before the law, so part of that drop would have happened anyway. To split it, you need a California that never passed the law. Nobody can observe that one, so we have to build it.

**3 · Naive v1** — purple average line; green bracket at 2000 = 50.5.
> First try: the average of thirty-eight states with no big tobacco program. By two thousand, this purple line sits fifty packs above California, more than the whole drop.

**4 · Fail** — red shading between purple and blue before 1988; shifted copy misses 1970.
> But look before the law. In nineteen seventy, the two lines nearly touch. By nineteen eighty-eight, they're twenty-four packs apart. They were drifting apart before the law existed. Shift the purple line down to match in eighty-eight, and it misses nineteen seventy by twenty-seven.

**5 · Metric** — scoreboard row: miss 16.0, effect 50.
> So score every comparison by its typical miss before the law. The average misses by sixteen packs, before anything happened.

**6 · Naive v2** — Montana line (purple), red shading, scoreboard row 4.5 / 34.
> Second try: the one state closest to California before the law, Montana. The miss drops to four and a half packs. But Montana runs twelve packs low in nineteen seventy and seven high in eighty-two, and it would credit the law with thirty-four packs.

**7 · Insight: blend** — 38 gray donor lines; five thicken as yellow weight bars grow.
> So blend states instead. Give each state a weight, none below zero, all adding up to one. Then pick the weights that make the blend track California before the law, in sales, and in price, income, age and beer drinking. Five states get weight: Utah a third, Nevada and Montana about a fifth each, Colorado and Connecticut the rest.

**8 · Formula from picture** — weighted lines merge into yellow dashed synthetic California; formula built from weights and lines; 1988 check; scoreboard 1.8.
> For each year, the blend is every state's sales times its weight, added up. In nineteen eighty-eight, that gives ninety-one point seven, against California's ninety point one. Across all nineteen years before the law, the miss is under two packs.

**9 · Prediction pause + reveal** — only pre-1988 data; dashed yellow continues to 2000; green gap; effect formula; scoreboard 26.
> Those weights only ever saw the years before the law. Now run the blend forward. [pause 1.5] The blend keeps sliding slowly. California falls away from it. By two thousand, the gap is twenty-six packs.

**10 · Placebos** — gap axes: yellow becomes the zero line, blue becomes California's gap; 22 gray placebo gaps.
> Could any state drift twenty-six packs from its blend by chance? Give each of the other states its own blend, and pretend it passed a law in nineteen eighty-eight. Of the twenty-two states fit as well as California, none ends as low.

**11 · Payoff + limit** — citation; "1 in 39"; post-1988 region flagged.
> Abadie, Diamond and Hainmueller ran this test in twenty ten. Measured against how well each state fit before the law, California's gap was the largest of thirty-nine: a one in thirty-nine chance if the law did nothing. A good fit to the past can't rule out some other shock that hit only California after nineteen eighty-eight.

**12 · Landing** — back to the opening chart; the 48.5 bracket splits into 22.8 (yellow) + 25.7 (green).
> So, the forty-nine packs from the start. About twenty-three would have gone anyway: that's where the blend ends up. The other twenty-six belong to the law, and you can only see them against a California that never voted for it.

## Sources
- Abadie, A., Diamond, A., Hainmueller, J. (2010). Synthetic Control Methods for Comparative Case Studies: Estimating the Effect of California's Tobacco Control Program. *JASA* 105(490): 493-505.
- Data: `california_prop99.csv` from the synthdid R package (Arkhangelsky et al.), same series as ADH 2010.
