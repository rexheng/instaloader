# 024 — Why Praise Seems to Fail and Punishment Seems to Work

**One idea:** when a score is skill plus luck, the people picked for extreme scores drift back toward average on the next try (by a factor r), so any feedback given right after extremes gets credit or blame for that drift.

## Palette (colour -> one meaning)

| Colour | Meaning |
|---|---|
| BLUE | skill (the stable part of a score); real people in Galton's data |
| YELLOW | luck (the part that is redrawn every try) |
| GREEN | cadets who were praised (always labelled "praised") |
| RED | cadets who were screamed at (always labelled "screamed at") |
| PURPLE | slice averages / the regression line / predicted next score |
| GRAY | axes, the dashed "same score twice" line, the silent control group, citations |
| INK | text and equations |

Data: cadets are **simulated** (400, `default_rng(325)`, skill ~ N(50,10), luck ~ N(0,10), feedback effect = 0), labelled "simulated" on screen. Galton heights are **real** (928 children, 1886 table), jittered within his 1-inch groups.

## Beats

| t (approx) | Beat | Narration | Visual |
|---|---|---|---|
| 0:00 | Cold open | Praise a cadet pilot's best maneuver, and the next one gets worse. Scream at the worst, and the next one gets better. If the words did nothing at all, would these arrows go flat? [pause 1.5] | Score axis. Green "praised" marker high on try 1, arrow down to try 2; red "screamed at" marker low, arrow up. On "flat", dashed flat ghost arrows. |
| 0:14 | Stakes | A flight instructor in the Israeli Air Force told Daniel Kahneman exactly this, and concluded that screaming works. Every fix applied right after a bad result gets judged this way: a new coach, a new pill, a new policy. | Citation Kahneman 2002/2011. The red label cycles "new coach", "new pill", "new policy", returns. |
| 0:28 | Build | So let's build the instructor's world on purpose, with feedback that does nothing. One cadet's score is skill plus luck. Feedback adds zero. | Arrows dim. One cadet's stacked bar (blue skill 61, yellow luck 15) on the axis; the equation is pulled out of the bar; "+ 0 x feedback" in gray. Bar collapses to a dot at 76. |
| 0:40 | | Here are four hundred simulated cadets. Skill and luck are equally spread. The instructor praises the top forty, in green, and screams at the bottom forty, in red. | 400 dots fill the try-1 column. Top 40 turn green on "top forty", bottom 40 red on "bottom forty". |
| 0:52 | | Then everyone flies again. Same skill, fresh luck. | Every dot copies across to the try-2 column at its new score. |
| 0:57 | Fail | The praised cadets dropped twelve points. The screamed-at cadets rose twelve. A before-and-after study would report that screaming adds twelve points. Our code says it adds exactly zero. | Group-mean arrows grow, landing exactly on the dimmed cold-open arrows: −12.4, +12.0. Left: measured effect counts up to +12.0 vs "in the code: 0". |
| 1:10 | Cause | Twelve points from nothing. To find where they came from, put each cadet's second score above their first. | Try-1 column tips onto the x axis; every try-2 dot slides sideways to its try-1 score: the scatter. |
| 1:17 | Insight | A cadet who scored the same twice would land on this dashed line. The cloud tilts less than that. | Dashed diagonal drawn on "this dashed line"; green dots visibly below it, red above. |
| 1:24 | | Take every cadet who scored about seventy the first time. On the second try, they averaged about sixty. Slice the cloud anywhere, and the averages land on this purple line, with half the slope. | Band at 65–75 lights up, purple mean dot at 60. Band sweeps to 60, 50, 40, 30 leaving purple dots; purple line drawn. |
| 1:38 | Why | Seventy is twenty points above average, but those twenty points are part skill and part luck. Skill makes up half the variation here, so on average ten of them are skill. Skill flies again. Luck is redrawn, and averages zero. | Horizontal bracket 50→70 splits into blue 10 + yellow 10. Blue piece rotates up to vertical at x = 70, landing on the purple dot at 60; yellow piece shrinks to nothing. |
| 1:55 | Formula | That fraction is the correlation between the two tries, r. The expected next gap is r times this gap, when both tries are equally spread out. | Equation built from the pieces: expected next gap (from the vertical blue piece) = r (blue) x this gap (from the bracket). r ≈ 0.5. Assumption in small gray. |
| 2:05 | Prediction | A cadet scores ninety, forty points above average. Predict the next score. [pause 1.5] About seventy, whatever the instructor yells. | Marker at x = 90; left: 40 x 0.5 = 20 -> 50 + 20 = 70; purple dot lands on the line at 70. |
| 2:15 | Payoff | Francis Galton drew this cloud first, in eighteen eighty-six, from nine hundred and twenty-eight adult children and their parents. Tall parents had tall children, but less tall: about two thirds of the parents' gap came back. | Axes relabel to mid-parent / child height (in); cadets dissolve into Galton's 928 real points. Slice means, purple line slope 0.65; quote "two-thirds of the height-deviate". Citation Galton 1886. |
| 2:30 | Limit | He called it regression towards mediocrity, but no force pulls anyone to the middle. Slice the cloud sideways, and the tallest children have less extreme parents too. | Horizontal band at child ≥ 71 in; purple marker: their parents average 69.8 in, left of the diagonal. |
| 2:42 | Fix | So here is the honest test. Take the forty worst cadets. Scream at a random half, and leave the other half alone. The silent half rises twelve points too. Screaming's effect is the gap between the arrows: less than one point, which is noise. | Back to the two-column chart: bottom 40 only. Red arrow +11.6 and gray "left alone" arrow +12.4 side by side; difference −0.8 ≈ 0. |
| 2:58 | Landing | Kahneman put it this way: because we reward people after their best and punish them after their worst, we are statistically punished for rewarding, and rewarded for punishing. The arrows in the instructor's story were real. His voice just was not what moved them. | The cold-open arrows return in full colour; short quote with citation Kahneman 2002. End card. |

Word count ≈ 480; target runtime ≈ 3:20.

## Sources
- Kahneman, D. (2002). Autobiography. *Les Prix Nobel 2002*. nobelprize.org.
- Kahneman, D. (2011). *Thinking, Fast and Slow*, ch. 17.
- Galton, F. (1886). Regression towards mediocrity in hereditary stature. *J. Anthropological Institute* 15:246–263. Data: R HistData::Galton (928 rows).
