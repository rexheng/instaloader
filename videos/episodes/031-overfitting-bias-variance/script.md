# 031 — Why a Perfect Fit Is a Warning Sign

**One idea:** a model with enough knobs can fit any data, so a perfect fit says nothing about
prediction; error on new data = bias squared + variance + noise, and it is U-shaped in the
number of knobs while training error slides to zero.

## Palette (colour -> one meaning, whole episode)

| colour | meaning |
|---|---|
| BLUE | training points (the ten we fit) and training error |
| RED | new / held-out points and the error measured on them (test error) |
| GREEN | the hidden true rule, a sine wave (always drawn as a curve, never as dots) |
| YELLOW | fitted models (line, polynomials, the elephant outline) and their spread = variance |
| PURPLE | bias: gap between the average fit and the true rule |
| GRAY | noise floor sigma squared; axes and secondary text |

All data is simulated (labelled on screen): y = sin(2 pi x) + noise with sigma = 0.3, ten points at
x = 0.05, 0.15, ..., 0.95. "Knobs" = polynomial coefficients (degree + 1).

## Beats (target ~3:10, ~500 words)

**1. Cold open (0:00–0:12).** Ten blue dots appear. A yellow line, then a yellow ten-knob curve.
> Ten measurements, scattered around a hidden rule. This straight line has two knobs, slope and height, and misses every point. This curve has ten knobs, and passes through all ten exactly.

**2. Prediction.** Ten red ghost rings (unrevealed) pulse in at the bottom as "next 10".
> Ten new measurements are coming from the same rule. Which will predict them better, the line or the curve? [pause 1.5]

**3. Stakes: Fermi and Dyson.** Data panel slides left and dims; big yellow "4" appears; elephant traces itself.
> In nineteen fifty three, Freeman Dyson showed Enrico Fermi a theory that matched Fermi's own measurements. Fermi asked how many free parameters it used. Dyson said four. Fermi answered with a line from John von Neumann. With four parameters I can fit an elephant, and with five I can make him wiggle his trunk.
Citation: Dyson, 2004 · Nature 427, 297

**4. The elephant is real.** "4" splits into the four complex numbers; p5 appears.
> In twenty ten, three physicists drew it. Four complex numbers, so eight real knobs, trace this outline. A fifth sets the eye and the trunk wiggle.
Citation: Mayer, Khairy & Howard, 2010 · Am. J. Phys. 78, 648

**5. Pivot.**
> Fermi's point: if your knobs can fit anything, fitting your data proves nothing. So let's measure it.

**6. Naive build.** Error chart appears on the right; the curve morphs 2 → 10 knobs; blue training error dots land.
> The obvious rule: score each curve by its average squared miss on the points it was fitted to, and keep the smallest. The line misses by point one six. Four knobs, point oh three. Ten knobs, zero. This rule always picks the most knobs.

**7. Fail.** Red rings land; red test dots per knob count; the spike at ten.
> Here are the ten new points. Score on these instead. The line, point two three. The ten knob curve, point seven oh, three times worse than the line.

**8. Cause.** Green true sine draws; the ten-knob curve's swings highlighted between points.
> Here is the hidden rule, a sine wave plus noise. Between the old points, the ten knob curve swings to chase that noise, and new points don't share it.

**9. Insight: bias.** 50 resampled lines, tight bundle; dashed average; slice at x = 0.8; purple gap.
> To see why, rerun the experiment. Fifty fresh sets of ten points, one line fitted to each. The lines barely move, but their average, this dashed line, sits off the wave. At this spot it misses by point four. That miss is bias.

**10. Insight: variance.** Lines morph into 50 ten-knob curves; yellow dots at the slice.
> Now fit fifty ten knob curves. On average they land right on the wave, but each one sprays wide, a spread of point six at the same spot. That spread is variance.

**11. Formula from the picture.** Purple gap -> bias^2, yellow spread -> variance, gray scatter -> sigma^2.
> Your expected error on a new point is the bias squared, plus the variance, plus the noise in the point itself, sigma squared, point oh nine, which no model removes.

**12. Prediction pause.**
> Add those three up for every number of knobs. Where will the total bottom out? [pause 1.2]

**13. Stacks build the U.** Stacked bars (gray, purple, yellow) rise at each knob count; red jagged dots morph into the 50-dataset average, sitting on the bar tops.
> Bias collapses at four knobs. Variance creeps up, then explodes at ten. The total bottoms out at four knobs, von Neumann's number. Training error, meanwhile, slid to zero.

**14. Payoff: held-out data in the wild.**
> Held out data is how real studies catch this. In twenty twenty, a hundred and sixty teams got nearly thirteen thousand variables on four thousand families, and predicted outcomes like a child's grades at fifteen, for families they never saw. The best entries were only slightly better than a regression with four variables.
Citation: Salganik et al., 2020 · PNAS 117, 8398

**15. Honest limit.** Schematic.
> The U is not the whole story. Models with far more knobs than points, like big neural networks, can see test error fall again past a perfect fit. Belkin and colleagues called it double descent.
Citation: Belkin et al., 2019 · PNAS 116, 15849

**16. Landing.** Back to the opening curve; its 49 siblings fade in behind it.
> Look again at the curve that hit all ten points. It is one strand of this tangle. With ten knobs and ten points, a perfect fit was guaranteed before we saw a single measurement.

## Sources
See facts.md.
