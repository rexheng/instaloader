# 053 · What Happens the Night You Turn 21

**One idea:** when a treatment switches on at a cutoff, people just below and just above it are alike, so the jump in fitted lines right at the cutoff estimates the causal effect there (regression discontinuity); a plain before/after average mixes in the trend and can even get the sign wrong.

**Data on screen:** real. U.S. motor-vehicle-accident death rates per 100,000 person-years in 30-day age cells, ages 19-23, from Carpenter & Dobkin (2009), as distributed with Angrist & Pischke, *Mastering 'Metrics* (2015) (`mlda`/AEJfigs). Only the test-score histogram in the limits beat is simulated, and it is labelled "simulated".

## Palette (colour -> one meaning)

| Colour | Meaning |
|---|---|
| BLUE | the data: crash-death rate, one dot per 30 days of age |
| YELLOW | the age-21 cutoff, the comparison window around it, and the measured jump |
| RED | the biased comparison (before/after averages; bunching that would bias a cutoff) |
| PURPLE | the confounder: aging (age gap and the downward age trend) |
| GREEN | the regression-discontinuity estimate (local fitted lines, their endpoints, the published RD jumps) |
| GRAY / DIM | axes, labels / dimmed context |

## Narration (beat by beat)

| # | Time | Narration | On screen |
|---|---|---|---|
| 1 | 0:00 | Car crash deaths among young Americans, by age. Each dot is thirty days of age. | Axes; blue dots stream in from 19 up to 21. Source line bottom-left. |
| 2 | 0:05 | At twenty one, drinking becomes legal. Past this line, do the dots go up, stay flat, or go down? [pause 1.5] | Yellow line at 21. Three gray arrows fan out: up / flat / down. Prediction hold. |
| 3 | 0:15 | Here is the other side. No one can be assigned to drink for a study, so this is the evidence we get. | Arrows leave; dots 21-23 stream in. |
| 4 | 0:22 | The obvious test: average every dot before twenty one, and every dot after. | Two red mean segments grow across each side. |
| 5 | 0:27 | The average drops from thirty two point five to thirty point eight, five percent fewer deaths. Taken at face value, legal alcohol made young people safer on the road. | Red labels 32.5, 30.8; scoreboard "averages −5%". |
| 6 | 0:39 | The catch is who sits on each side. The people on the right are, on average, two years older, and crash deaths fall with age the whole way across. | Purple age bracket (mean ages 20.0 vs 22.0); purple trend arrow under the cloud. |
| 7 | 0:49 | Two years of that decline is worth about six deaths per hundred thousand. The averages measured getting older, not drinking. | "aging ≈ −6" in purple; red −5% struck. |
| 8 | 0:57 | So shrink the comparison. Someone a month before their twenty first birthday and someone a month after are alike in almost every way, except the law. | Yellow window closes from the full range to the two dots touching 21; others dim. |
| 9 | 1:07 | But that leaves two noisy dots. So fit a straight line on each side, and let each line carry the age trend right up to the birthday. | Window reopens; green lines grow from the edges toward 21. |
| 10 | 1:16 | Watch where the two lines reach the cutoff. [pause 1.5] | Lines reach 21; endpoints appear; yellow gap grows between them. |
| 11 | 1:21 | On the left, just under thirty. On the right, almost thirty four and a half. The gap is four and a half more deaths per hundred thousand: fifteen percent up, not five percent down. | Endpoint values copy into a ledger; τ = 4.53; scoreboard "at the cutoff +15%". |
| 12 | 1:34 | That gap is the estimate. The method is called regression discontinuity: the jump in the fitted lines, right at the cutoff. | Ledger numbers turn into ŷ(21⁺) − ŷ(21⁻) = τ. |
| 13 | 1:43 | Narrow the window from two years to six months, and the gap stays between four and six. | Window shrinks; lines refit live; τ readout moves 4.2-5.6. |
| 14 | 1:50 | Slide the cutoff to twenty, or to twenty two, birthdays where no law changes, and the gap falls below one. | Placebo cutoffs: τ = 0.83 at 20, −0.10 at 22; back to 21. |
| 15 | 2:00 | Carpenter and Dobkin ran this on American death certificates. At twenty one, car crash deaths jump about fifteen percent, deaths that mention alcohol about thirty five, and deaths from every cause about nine. | Plot shrinks left; green bars 15 / 35 / 9 %; the +15% flies into the crash bar. Citation. |
| 16 | 2:14 | It works because no one chooses their birthday, so people spread evenly across the line. Put the cutoff on a test score, and people who just miss can retake it and pile up above it. Then the two sides stop being alike. And the jump describes people turning twenty one, not drinkers at forty. | Two histograms: flat across 21 vs (simulated) hole-and-pile at a pass mark, pile in red. |
| 17 | 2:36 | So, past the line, the dots go up, and then down. Crash deaths jump the night drinking becomes legal, then keep falling with age. The average only saw the fall. | Back to the cold-open plot: yellow up-arrow at the step, purple down-arrow along the right side; the opening's three arrows answered. End card. |

Word count ≈ 440. Spoken numbers are written out for the voice.

## Sources
See facts.md.
