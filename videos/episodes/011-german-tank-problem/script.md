# Episode 11: How Serial Numbers Counted Germany's Tanks

**One idea:** the largest serial number you have seen is the single most likely size for the factory, yet it always comes in too low. Adding one average gap on top fixes it: N-hat = m + (m - k)/k.

## Palette (one meaning per colour)
| Colour | Meaning |
|---|---|
| BLUE | captured serial numbers (the data in hand) and m, the largest one |
| YELLOW | gaps of unseen serial numbers, and the gap-corrected estimate built from them |
| GREEN | the truth: the true N of the simulated factory, and German records |
| RED | error: impossible estimates and shortfalls |
| PURPLE | the spy (intelligence) estimate |
| INK / GRAY / DIM | text, axes and labels, dimmed context |

## Beats (narration exactly as spoken)

**1. Cold open (0:00).** Number line. Five blue ticks drop as their numbers are spoken. "N = ?" sits past the end. A "simulated" tag is shown.
> Five captured tanks have gearboxes stamped eight, fourteen, twenty two, thirty one and eighty nine. The factory numbers them in order, starting from one. How many tanks has it built? [pause 1.5]

**2. Stakes.** A purple "1,550 / month" appears with the citation.
> In the summer of nineteen forty two, this was a real question. Allied intelligence put German tank production at one thousand five hundred and fifty a month. The serial numbers told a different story.

**3. Naive 1.** Copies of the five ticks slide together to their mean (32.8). The 0 to 32.8 segment is copied end to end to reach 65.6.
> Start with the obvious idea. Serial numbers spread evenly, so their average should sit near the middle. These five average thirty two point eight. Double it, and you get about sixty six tanks.

**4. Fail 1.** A red band runs from 66 to 89.
> But you are holding tank eighty nine. Doubling the average just guessed fewer tanks than you have already seen.

**5. Naive 2: maximum likelihood.** Likelihood axes appear under the line on the same scale. The curve is zero below 89, jumps, then decays. A dashed drop from tick 89 meets the peak.
> Second try. Ask which factory size makes these five numbers most probable. Any size below eighty nine is impossible, so its likelihood is zero. Above that, every extra tank makes your five a little less likely. So the likelihood peaks exactly at the largest serial you hold. That is the maximum likelihood estimate, eighty nine.

**6. Fail 2, measured.** A pretend factory with true N = 100 (green line). Histograms of 10,000 estimates grow as a counter runs: 2 x mean, with its impossible part stacked in red, and max, with a red shortfall arrow.
> Test both on a pretend factory of one hundred tanks. Capture five at random, ten thousand times. Doubling the average centers near a hundred, but this red slice, about one capture in five, lands below a serial already in hand. The largest serial never overshoots, and that is its flaw. It averages eighty four, sixteen tanks short.

**7. Prediction pause.**
> The tanks above it are never seen, so it can only undercount. How far past eighty nine should you reach? [pause 1.5]

**8. Insight: gaps.** Back on the number line, yellow gap segments light up. Copies stack end to end into one bar of 84, which splits into 5 equal pieces of 16.8.
> Look at the gaps. Five captures cut the line into stretches of tanks nobody saw. Below eighty nine, those stretches hold eighty four unseen tanks, shared across five gaps. That is about seventeen per gap.

**9.** One average gap slides on top of 89 and lands at 105.8.
> Nothing makes the stretch above eighty nine any different, so add one more average gap on top. Eighty nine plus seventeen is about a hundred and six.

**10. Formula from the picture.** m comes from tick 89 and (m - k)/k from the yellow piece. TransformMatchingTex gives m(1 + 1/k) - 1.
> In symbols, m is the largest serial and k is the number captured. The estimate is m, plus the average gap, m minus k over k. That tidies up to m times one plus one over k, minus one.

**11. Measured win.** A third histogram row in yellow centers on the green line.
> On the same ten thousand captures, it centers on one hundred, with about a third less spread than doubling the average.

**12. Payoff.** Horizontal bars for August 1942: purple 1,550, yellow 327, green 342. Citation.
> Allied economists ran this kind of serial number analysis on captured gearboxes. For August nineteen forty two, it gave three hundred and twenty seven tanks a month. German records, found after the war, said three hundred and forty two.

**13. Honest limits.** Two more months appear smaller. The gearbox and chassis contrast is drawn on a mini line.
> Other months missed by more, by up to forty percent, but never by a factor of four. And it only works when numbers run in one unbroken sequence. Chassis numbers came in separate blocks, and those were much harder to use.

**14. Landing.** Back to the five ticks, the yellow estimate at 106, and a green true N = 100.
> Back to your five tanks. This simulated factory built exactly one hundred. If you guessed near ninety, you picked the most likely answer, and it was still too small. The missing tanks were hiding in the gaps.

## Sources
- Ruggles, R. & Brodie, H. (1947). An Empirical Approach to Economic Intelligence in World War II. *JASA* 42(237):72-91.
- Simon, C. (2023). A Bayesian treatment of the German tank problem. arXiv:2301.00046 (Table 1 reproduces the 1947 table).
- Goodman, L. A. (1952). Serial number analysis. *JASA* 47(260):622-634.
