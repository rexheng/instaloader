# 028 · Noisy Data Makes Real Effects Look Smaller

**One idea:** random error in the thing you measure first (the predictor) shrinks the fitted slope by a fixed share, the reliability λ = σ_T² / (σ_T² + σ_E²); measuring twice estimates λ and undoes it.

## Palette (colour -> one meaning)

| Colour | Meaning |
|---|---|
| BLUE | true blood pressure: patient dots, the true line (dashed), σ_T², the 64 |
| RED | measurement error: error arrows, error histogram, σ_E², the 36 |
| YELLOW | the line we fit to recorded data, and its slope b_obs |
| GREEN | the corrected slope / corrected line |
| PURPLE | the second reading (repeat-measurement scatter, r) |
| INK / GRAY / DIM | text / axes and secondary labels / dimmed context |

Layout: persistent scatter (left half) for the whole episode, with a live slope readout; the right panel changes (candidate lines, error histogram, squares and formula, repeat scatter, citations).

## Beats

| # | Time (approx) | Narration | Visual |
|---|---|---|---|
| 0 | 0:00 cold open | This line links blood pressure to stroke risk for two hundred patients. Now make every reading off by a random amount, high as often as low. Does the line get steeper, flatter, or stay the same? [pause 1.5] | Simulated scatter + yellow fitted line, readout slope = 1.02. Red ± arrows on a few dots at "random". Three dashed candidate lines labelled steeper / same / flatter land on each word. |
| 1 | 0:14 stakes | Most people pick the same. The errors cancel out on average, so the trend should survive. | Candidates fade, "same" stays briefly. Red histogram of the 200 cuff errors builds; "average ≈ 0" tick at 0. |
| 2 | 0:21 build | Let's test it. True pressures here spread about eight points either side of eighty. The cuff adds an error that spreads about six. | Blue bracket ±8 around 80 under the cloud; red bracket ±6 on histogram. |
| 3 | 0:30 build | Switch the error on, and refit the line through the readings we would actually record. | ValueTracker: dots slide sideways by their own error; x-title becomes "measured"; yellow line refits live, blue dashed true line left behind; slope readout falls. |
| 4 | 0:36 fail | The slope falls from one to point six four. More than a third of the effect is gone, and no patient changed. | Readout 0.64 flagged; red "−37%". |
| 5 | 0:44 contrast | Now move the same kind of noise onto the risk instead. The cloud thickens, but the slope stays near one. Noise in the outcome blurs. Noise in the predictor flattens. | Dots slide back horizontally, then spread vertically; readout returns to ~1.01; then back to horizontal error. Two tags appear. |
| 6 | 0:56 insight | Here's why. Take the patients whose reading came out high, around ninety five. A few really are that high. Many more are ordinary patients whose cuff read high, because ordinary patients are far more common. | Column band 92–98; its 19 dots slide back to their true pressures (left), leaving red trails. |
| 7 | 1:08 | Their true pressures average only about ninety, so their risk is the risk of ninety. Every column slides toward the middle like this, and the line tilts flatter. | Markers: mean reading 94 vs mean true 90; a second column at 65 shows the pull upward (to 68.5). Arrows toward 80. |
| 8 | 1:20 picture | How much flatter depends on spreads, measured in squares. True pressures give eight squared, sixty four. The cuff adds six squared, thirty six. The readings vary by a hundred in total. | Blue 8×8 square, red 6×6 square grow from the two brackets; they restack into one 10×10 square split 64 / 36. |
| 9 | 1:33 formula | The real share is sixty four out of a hundred, exactly the slope that survived. Call it lambda, the reliability. The observed slope is lambda times the true one. | λ = σ_T²/(σ_T²+σ_E²) built from the square labels; = 0.64 flags with the slope readout; b_obs = λ·b_true. |
| 10 | 1:46 prediction | If the cuff were twice as sloppy, an error spread of twelve, how much slope would survive? [pause 1.5] | Red bracket doubles; hold. |
| 11 | 1:53 | Sixty four out of two hundred and eight, under a third. The line on the left agrees: point three oh. | Red area grows to 144 inside a growing square; λ → 0.31; the scatter's error doubles and the slope readout falls to 0.30. |
| 12 | 2:01 fix | In real data the true pressures are hidden, so measure everyone twice. Two readings share only the true part, so their correlation estimates lambda: point six four. | Error back to 6. Purple scatter reading 1 vs reading 2; r = 0.64 transforms next to λ. |
| 13 | 2:12 | Divide the flattened slope by it, and the line swings back to one, matching the truth we built in. | b̂_true = b_obs / r = 1.00 (TransformMatchingTex); green line rotates from the yellow one onto the blue dashed truth. |
| 14 | 2:20 payoff | Charles Spearman called this attenuation in nineteen oh four, and his cure was the same: repeat the measurements. | Plot dims. Quote "two or more independent series of observations". Citation Spearman 1904 · American Journal of Psychology. |
| 15 | 2:28 | In nineteen ninety, MacMahon and colleagues pooled nine studies, four hundred and twenty thousand people, each with blood pressure measured once at the start. Correcting for this dilution made the links to stroke and heart disease about sixty percent stronger. | "9 studies · 420,000 people"; bars: single reading 1.0× (yellow), corrected 1.6× (green), "+60%". Citation MacMahon et al., 1990 · The Lancet. |
| 16 | 2:43 limits | The fix assumes random error in one predictor. Systematic error, or several noisy predictors at once, can push estimates either way. | Two short tags: "holds: random error, one predictor" / "breaks: systematic error, many predictors". |
| 17 | 2:52 landing | So in the opening, the answer was flatter, by the share of each reading that's noise. The effect was never weaker. The ruler was. | Back to the opening frame: blue dashed truth vs yellow flattened line, "flatter" boxed; at "ruler" the x-axis title "measured blood pressure" is flagged. End card. |

Word count ≈ 450; target runtime ≈ 3:15.

## Sources
- C. Spearman (1904), "The Proof and Measurement of Association between Two Things", *American Journal of Psychology* 15(1):72–101.
- S. MacMahon, R. Peto, J. Cutler et al. (1990), "Blood pressure, stroke, and coronary heart disease. Part 1", *The Lancet* 335:765–774.
- J. A. Hutcheon, A. Chiolero, J. A. Hanley (2010), "Random measurement error and regression dilution bias", *BMJ* 340:c2289 (background for the slope formula and limits).
