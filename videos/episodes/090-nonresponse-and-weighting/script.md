# 090 · A Poll Can Match the Census and Still Be Wrong

**One idea:** weighting resizes the columns a sample is split into (its demographic
widths), but it cannot change who answered *inside* a column; when the reason people answer is
tied to the answer itself, the bias sits in the heights and survives any weighting.

Target runtime ≈ 3:15 · narrator af_heart · speed 0.78

## Palette (colour -> one meaning, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | the poll / its respondents (poll bars, respondent mosaic, poll estimate) |
| GREEN | the government benchmark / the true population value (benchmark bars, population mosaic, dashed true heights) |
| YELLOW | volunteers (the hidden trait), and `h` (the share of volunteers inside a column) |
| PURPLE | the weighting variable: education columns and their widths `W` |
| RED | error: the gap between an estimate and the truth (always carried by a bracket and a number) |
| GRAY / DIM | axes, non-volunteers, secondary text, dimmed context |

## Beats

| # | Time | Narration | Picture |
|---|---|---|---|
| 1 | 0:00 cold open | This poll of fifteen hundred Americans lands within four points of the government on homeownership, marriage and citizenship. The government says twenty-seven percent of adults volunteered last year. What did the poll say? [pause 1.5] | Paired bars (BLUE poll / GREEN government) grow row by row: own home 63/62, married 50/54, U.S. citizen 95/92. Fourth row "volunteered": GREEN 27, BLUE bar is a "?". Prediction hold. |
| 2 | 0:13 reveal | Fifty-five percent. That's twenty-eight points too high, nearly ten times the poll's margin of error, and Pew traces the gap at least partly to who agreed to talk. | BLUE bar grows to 55. RED bracket 27→55 "+28 points". Gray whisker ±2.9 at the bar tip. Citation Pew Research Center, 2012. |
| 3 | 0:24 stakes | Only nine percent of the households Pew called took part, down from thirty-six percent in nineteen ninety-seven. Weighting makes those nine stand in for everyone, so the question is what weighting can repair. | 10×10 grid of households: 36 lit BLUE (1997), 27 go dark (2012: 9). The nine lit tiles swell (weights). |
| 4 | 0:37 naive | The usual suspect is education. Thirty-nine percent of these respondents had a college degree, against twenty-eight percent of adults, and graduates volunteer more. | Grid reflows into two PURPLE-labelled columns: respondents 39 / 61 vs adults 28 / 72. |
| 5 | 0:47 | So here is a simulated population with that pattern. Graduates volunteer at forty-two percent, everyone else at twenty-one. Overall, twenty-seven percent, like the government's figure. | Left: population mosaic (GREEN outline, "simulated"): columns 28 / 72, YELLOW heights 42 / 21. Estimate 27%. |
| 6 | 0:59 | Now make volunteers more willing to answer, and poll it. Yellow fills seventy percent of the graduate column and forty-seven percent of the other. The raw estimate is fifty-six percent. | Right: respondent mosaic (BLUE outline): widths 39 / 61, heights 70 / 47. Live estimate 56%. |
| 7 | 1:11 fail | Now weight. Graduates count for less and everyone else for more, until the columns match the census. The estimate slides to fifty-three: three points recovered, twenty-six still missing. Pew's real poll was weighted on education, age, sex and race too, and still said fifty-five. | Respondent column boundary slides 39→28 (ValueTracker); live estimate 56→53; RED miss 29→26. |
| 8 | 1:31 insight | Look at what the weights moved. Only widths. The estimate is each column's width times its yellow height, added up. Weighting sets every width to the census. It never touches a height. | Formula assembles from the picture: W (from PURPLE width braces) × h (from YELLOW heights): p̂ = W₁h₁ + W₂h₂ = 0.28·0.70 + 0.72·0.47 ≈ 0.53. |
| 9 | 1:48 | And the heights are where the poll is wrong. In each column the dashed line marks the true share, and yellow overshoots it by more than twenty-five points. | GREEN dashed lines at 42 and 21 inside the respondent columns; RED gaps 28 and 26. |
| 10 | 1:59 prediction | That overshoot comes from who answers. How much more often must volunteers answer to turn twenty-seven percent into fifty-five? [pause 1.5] | Single column: 27 YELLOW / 73 GRAY, target 55 marked. Prediction hold. |
| 11 | 2:08 | Twice is not enough: doubling only gets you to forty-three. Answering multiplies the odds. Twenty-seven to seventy-three becomes twenty-seven k to seventy-three, and reaching fifty-five to forty-five takes a k of about three point three, the rate this simulation used. | k tracker 1→2 (share 43%) →3.3 (55%); odds equation built from the two stacked blocks: p̂/(1−p̂) = k · p/(1−p). |
| 12 | 2:30 payoff | When the reason people answer is something you can measure, adding it as a column works. In twenty sixteen the University of New Hampshire poll weighted on age, sex and region, but not education, and had Clinton ahead by eleven. She won by less than half a point. With an education weight, the pollster reported, the poll matched the result. | BLUE bar +11, GREEN bar +0.4; a PURPLE "education" split is added; BLUE bar shrinks onto GREEN. Citation AAPOR (Kennedy et al.), 2017. |
| 13 | 2:52 limit | Willingness to volunteer has no census column. Pew borrowed the government's twenty-seven percent to weight on it, and the Republican share barely moved, from forty-one to thirty-nine. The bias reaches only answers linked to answering. | BLUE bar 41→39. Citation Pew 2012. |
| 14 | 3:06 landing | So look again at the opening bars. Homes, marriage and citizenship matched because they are barely linked to who picks up. A poll can match the census on every width and still be wrong in the height. | Opening rows return; the volunteered row's gap is re-drawn as a height inside a column. End card. |

## Sources
- Pew Research Center (May 15, 2012), *Assessing the Representativeness of Public Opinion Surveys* (standard survey Jan 4–8 2012, n = 1,507, RR3 9%, MoE ±2.9; benchmarks from CPS).
- AAPOR Ad Hoc Committee on 2016 Election Polling (Kennedy et al., 2017), *An Evaluation of 2016 Election Polls in the U.S.*, §3.4.
- BLS (Feb 22, 2012), *Volunteering in the United States, 2011* (26.8%; by education for the simulation's rates).
