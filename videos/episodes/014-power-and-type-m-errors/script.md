# Episode 14 — Why Small Studies Find Huge Effects

**One idea:** passing the significance filter is what makes small studies' effects huge: with n per group, nothing smaller than 1.96·√(2/n) can be printed, so when the truth sits inside that wall every printed estimate is an exaggeration.

## Palette (colour -> one meaning, whole episode)
- GREEN  — the true effect (0.2 SD; later the plausible true sex-ratio effect)
- BLUE   — study estimates that exist (the blocks, the sampling bell)
- PURPLE — the significance walls, ±1.96 standard errors
- YELLOW — what gets printed (significant estimates, their average, the exaggeration ratio)
- INK / GRAY / DIM — text, axes, dimmed context

## Beats

**B0 Cold open (0:00)** — number line "estimated effect (standard deviations)", green truth at 0.2, a grid of 1,000 lab squares, "printed average = ?" in yellow.
> The true effect of this treatment is small: point two. A thousand small labs test it, and journals print only the significant results. On average, what effect do the printed studies report? [pause 1.5]

**B1 Stakes**
> Point two is a fair guess, maybe a little more. Reviews, guidelines and the next lab's sample size are all built on that printed number.

**B2 Naive build** — lab squares drop onto the line as blocks (simulated).
> So run it. Each lab gives twenty people the treatment and twenty a placebo, and measures the difference. Each block on this line is one lab's estimate.

**B3**
> Noise scatters them widely, from about minus point eight to plus one and a half. But the pile is centred on the truth: all thousand together average point two oh.

**B4 Fail** — purple walls rise at ±0.62; blocks between dim, blocks beyond turn yellow, a counter climbs to 97.
> Now apply the filter. A result is significant only if it lands beyond these walls. Ninety-seven of the thousand get through.

**B5** — yellow average marker at 0.69, bracket to the green line, "×3.5".
> Their average is point six nine, three and a half times the true effect. And six of them point the wrong way.

**B6 Cause**
> No lab made a mistake. The filter only lets through the estimates that noise pushed far from zero.

**B7 Insight** — the blocks melt into a bell; SE bracket; equation built from the bracket and the wall.
> So where do the walls sit? A single lab's typical error, its standard error, is the square root of two over twenty: point three two. Significance needs one point nine six of those, so the wall stands at point six two.

**B8**
> That is the smallest effect this design can print, three times the truth. The real answer, point two, sits inside the walls, where no study of this size can print it.

**B9 Prediction**
> Now give every lab four hundred people per group. Where do the walls go? [pause 1.5]

**B10 Fix (live readouts n, power, printed ÷ truth)**
> N sits under the square root, so the bell narrows and the walls close in. Near two hundred per group, they pass the truth. At four hundred, power is eighty-one percent, and the printed average is only twelve percent too high.

**B11 Still fails**
> But choosing that sample size needs a guess at the true effect. Plan for the printed point six nine, and the standard formula says thirty-three per group. Against the real point two, that study has thirteen percent power.

**B12 Payoff 1** — slider to n ≈ 66; citation Button et al., 2013.
> Real fields often sit there. Button and colleagues estimated the median power of neuroscience studies at twenty-one percent. In this picture, that power means printed effects about two point two times the truth.

**B13 Payoff 2** — axis morphs to percentage points; walls at ±6.5; reported 8; green band ≤ 1. Citation Gelman & Carlin, 2014.
> Gelman and Carlin called this a Type M error, M for magnitude. Their example: a 2007 study found eight points more girls born to the most attractive parents. That study's walls sat at six and a half points, while known sex-ratio effects are about one point or less.

**B14**
> If the true effect were point one, a significant result would overstate it seventy-seven times on average, and nearly half would point the wrong way.

**B15 Landing** — back to the 20-per-group picture: green 0.2 inside the walls, yellow 0.69 outside.
> Back to the thousand labs. Point six nine was never a fluke. With twenty per group, nothing under point six two could get out. In a small study, huge is the only size an effect is allowed to be.

## Sources
- Button, K. S., Ioannidis, J. P. A., Mokrysz, C., Nosek, B. A., Flint, J., Robinson, E. S. J., & Munafò, M. R. (2013). Power failure: why small sample size undermines the reliability of neuroscience. *Nature Reviews Neuroscience*, 14, 365–376.
- Gelman, A., & Carlin, J. (2014). Beyond power calculations: Assessing Type S (sign) and Type M (magnitude) errors. *Perspectives on Psychological Science*, 9(6), 641–651.
- Kanazawa, S. (2007). Beautiful parents have more daughters. *Journal of Theoretical Biology*, 244, 133–140 (as analysed by Gelman & Carlin 2014).
- Simulation: own (numpy seed 13), normal model, z-test, σ known; see facts.md.
