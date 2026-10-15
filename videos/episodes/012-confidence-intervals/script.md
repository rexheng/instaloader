# Episode 12 — What "95% Confident" Actually Means

**One idea:** the 95% in a confidence interval is the hit rate of the procedure that draws intervals; once one interval is computed, the true mean is either inside it or not.

Runtime target ≈ 3:20 · ~470 words · narrator af_heart @ 0.78

## Palette (colour → one meaning, whole episode)

| Colour | Meaning |
|---|---|
| YELLOW | the true mean μ (fixed; visible only in the simulation) |
| BLUE | an interval / its endpoints L, U, x̄ before we know whether it hit (random output of the machine) |
| GREEN | an interval that caught μ ("hits") |
| RED | an interval that missed μ ("misses") |
| PURPLE | Bayesian probability about μ (credible interval, needs a prior) |
| INK / GRAY / DIM | text / axes, survey counts, secondary labels / dimmed context |

Green vs red is never colour alone: hits cross the yellow line, misses do not, and every counter is labelled "hits" / "misses".

## Beats

**1 · Cold open (0:00–0:15)** — number line, a blue interval 0.1 to 0.4 labelled "95% confidence interval"; statement "95% chance the true mean is inside?" with *true* / *false* boxes.
> A study reports a ninety-five percent confidence interval for a mean: from point one to point four. True or false: there is a ninety-five percent chance that the true mean lies inside it. [pause 1.8]

**2 · Stakes (0:15–0:27)** — 118 dots, 70 filled ("ticked true"). Citation: Hoekstra, Morey, Rouder & Wagenmakers, 2014 · Psychonomic Bulletin & Review. "false" box gets outlined: "survey's answer".
> In twenty fourteen, Hoekstra and colleagues put this exact sentence to a hundred and eighteen psychology researchers. Fifty-nine percent ticked true. The survey's authors had written it as a false statement.

**3 · Setup** — axis slides into place; yellow line appears.
> To see why, we'll build the machine that makes these intervals, and test it in a world where we know the truth.

**4 · Naive build** — five dots fall on the axis; x̄ tick; interval grows; formula x̄ ± 1.96 · s/√5 is built from the tick, the dots and their count.
> In this simulated world the true mean is point two five: this yellow line. Each run, the machine gets five measurements, these dots, and draws the textbook interval: their average, plus or minus one point nine six times the spread s, over root five.

**5 · It works** — runs 1–4 rise into the stack and turn green; then 96 more rain down; live hits / misses counters.
> The first four intervals all catch the line. Now run it a hundred times. Green caught the true mean, red missed it.

**6 · Fail (measured)** — "promises 95%" under the formula; counters stop at 88 / 12; "10⁶ runs: 87.8%".
> Eighty-eight hits out of a hundred. A million runs settle at eighty-eight percent. The label promised ninety-five.

**7 · Cause** — bars sort by width (narrowest at the bottom); a brace marks the narrower half: 11 of 12 misses.
> Sort the intervals by width, and the misses pile up at the narrow end. With five points, the spread s is itself noisy. When it comes out too small, the interval shrinks and stops short of the line. Over a million runs, nearly nine in ten misses come from the narrower half.

**8 · Fix** — 1.96 → 2.78 (TransformMatchingTex, flagged); every bar stretches by 1.42 about its centre; seven reds turn green; 95 / 100; "10⁶ runs: 95.0%". Citation: Student (W. S. Gosset), 1908 · Biometrika.
> William Gosset, writing as Student in nineteen oh eight, worked out the fix: with five points, multiply by two point seven eight instead of one point nine six. Every bar stretches by the same factor. Ninety-five of a hundred now catch the line, and a million runs give ninety-five percent.

**9 · Insight** — a blue probe interval jumps from run to run with L and U attached; the line stays put. P(L ≤ μ ≤ U) = 0.95 assembled from L, U, the μ label and the 95/100 counter.
> Now read the ninety-five percent off this picture. It counts hits across runs. Before the data arrive, the endpoints L and U are random: they jump from run to run, while the mean mu stays put. The chance that this random interval covers mu is point nine five.

**10 · One interval** — probe lands on 0.1–0.4; L → 0.1, U → 0.4; "= 0.95" → "= 1 or 0".
> Run the study once, and the endpoints become numbers, say point one and point four. Now nothing in the statement is random. Mu is inside or it isn't, so the probability is one or zero, and you can't see which.

**11 · Prediction pause** — two intervals of equal width (A, B) lifted out, centred, axis and line hidden. Hold. Then they slide back: A green, B red.
> Here are two intervals from the machine, the same width. Without the line, which a real study never shows you, which one caught the mean? [pause 1.6] A caught it. B missed. From the inside, a hit and a miss look identical.

**12 · Payoff** — stack shrinks right; P(L ≤ μ ≤ U) = 0.95 returns; citation Neyman, 1937 · Phil. Trans. R. Soc. A; then bars: researchers 3.45 vs first-years 3.51 false statements endorsed (of 6). Citation Hoekstra et al., 2014.
> This is Jerzy Neyman's theory of confidence intervals from nineteen thirty-seven: the confidence belongs to the procedure. In Hoekstra's survey, researchers endorsed on average three and a half of six false readings, about as many as first-year students who had never been taught inference.

**13 · Honest limits** — tags "random sampling", "model fits"; a purple posterior over μ with 95% shaded from 0.1 to 0.4, "needs a prior".
> The promise has conditions: random sampling, and a model that fits the data. And a ninety-five percent chance for one interval is what a Bayesian credible interval offers, but only after you choose a prior.

**14 · Landing** — stack returns full size, line hidden, every bar back to blue; the opening interval 0.1–0.4 joins the stack with a "?".
> So, point one to point four. It is one more bar in this stack, with the line hidden. Ninety-five percent was the machine's record, never this bar's chance.

## Sources
- Hoekstra, R., Morey, R. D., Rouder, J. N., & Wagenmakers, E.-J. (2014). Robust misinterpretation of confidence intervals. *Psychonomic Bulletin & Review*, 21(5), 1157–1164. doi:10.3758/s13423-013-0572-3
- Neyman, J. (1937). Outline of a theory of statistical estimation based on the classical theory of probability. *Phil. Trans. R. Soc. A*, 236(767), 333–380. doi:10.1098/rsta.1937.0005
- Student [W. S. Gosset] (1908). The probable error of a mean. *Biometrika*, 6(1), 1–25.
- Simulation: `sim.py` in this directory (μ = 0.25, σ = 0.13, n = 5, seed 4335 for the 100 displayed runs; 10⁶ runs for long-run rates).
