# 019 — How to Sample From a Shape You Can't Normalize

**One idea:** a walker that accepts downhill steps with probability *new height / old height* never needs the total area Z (it cancels in the ratio), and that same rule balances traffic between every pair of points, so its footprints pile up in proportion to height.

## Palette (colour -> one meaning, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | height of the unnormalized shape p̃ (the curve, height bars, h terms) |
| YELLOW | the walker and its proposed step (focus) |
| GREEN | an accepted move / traffic that flows |
| RED | the total area Z and the cost of computing it |
| PURPLE | footprints: the walker's samples, their histogram and shares (π) |
| INK / GRAY / DIM | text, axes, refused proposals and dimmed context |

## Beats (target ~3:20 at ~150 wpm)

**1. Cold open (0:00–0:13)** — two-hill curve, small hill labelled 1, big hill 3; yellow walker takes a few steps (green = accepted, grey dashed = refused).
> A walker on two hills, one a third as tall as the other. It always steps uphill, and only sometimes steps down. What share of its footprints land on the small hill? [pause 1.5] Climbing keeps pulling it toward the summit, so nearly zero feels right.

**2. Stakes (0:13–0:30)** — curve becomes "prior × likelihood"; area fills RED and becomes Z; Bayes' rule assembles from the curve and the area.
> These hills could be a Bayesian posterior. Bayes' rule hands you its shape: prior times likelihood. To turn that shape into probabilities, you divide by the total area under it, called Z. And Z is an integral over every parameter in the model.

**3. Naive build (0:30–0:45)** — 100 red slices under the curve; counter "100 evaluations"; Z ≈ 5.51.
> The obvious move is to measure Z directly. Evaluate the height at a hundred grid points and add up the slices. One parameter, a hundred evaluations, and Z comes out to five point five one.

**4. Fail (0:45–1:08)** — the row of 100 points sweeps into a 100×100 mesh; counter 10^4 → 10^20; "≈ 3,200 years at 10^9 per second".
> Add a second parameter, and the grid becomes a hundred by a hundred: ten thousand evaluations. Every parameter multiplies the cost by a hundred. Ten parameters need ten to the twentieth evaluations. At a billion per second, that takes over three thousand years. The grid fails because the total needs the height everywhere.

**5. Insight I: Z cancels (1:08–1:25)** — walker on the big hill proposes a downhill step; two blue height segments; ratio formula; Z's cancel by TransformMatchingTex.
> The walker never asks for the total. Its downhill rule: propose a step, and accept it with probability new height over old height. Each true height carries the same unknown Z, so in the ratio, Z cancels.

**6. Insight II: balance (1:25–2:10)** — two spots, heights 3 and 1; 60 purple walkers on each; green flow arrows 20 and 60; prediction pause; rounds settle 100, 87, 91, 90; balance equation built from 90 × 1/3 = 30 × 1.
> Why would that give the right proportions? Shrink the hills to two spots, three units high and one unit high. Put sixty walkers on each, and every round, each one proposes a jump to the other spot. Going down from the tall spot, a third accept: twenty walkers. Going up from the short spot, all sixty move. So the tall spot fills up. At what split does the traffic balance? [pause 1.5] Ninety and thirty. A third of ninety is thirty, and all thirty come back. The flows match when the walkers split three to one, exactly the ratio of the heights. Every pair of points on the curve strikes this same balance, so footprints pile up in proportion to height.

**7. Answer (2:10–2:28)** — back to the hills; 50,000 simulated steps build a purple histogram onto the blue curve; live share → 25.0 %.
> Back on the two hills, fifty thousand simulated steps. The small hill collects twenty-five percent of the footprints, its exact share of the area. The histogram traces the curve, and nobody ever computed Z.

**8. Payoff (2:28–2:55)** — 224 disks in the 14 × 16 lattice from the paper's Fig. 2; jiggle; 448 coordinates; 100^448 in red; citation.
> This rule is from a nineteen fifty-three paper by Nicholas Metropolis, Arianna and Marshall Rosenbluth, and Augusta and Edward Teller. At Los Alamos, they simulated two hundred twenty-four hard disks: four hundred forty-eight coordinates. A grid would need a hundred to the four hundred forty-eighth power points. Arianna Rosenbluth implemented the walker on the Maniac computer, and each pressure value took four to five hours. In nineteen seventy, W. K. Hastings generalized it.

**9. Honest limit (2:55–3:12)** — two simulated trace panels: tiny steps (96 % accepted, stuck on big hill), huge steps (6 % accepted, flat runs).
> The paper also named the catch. With huge steps, most moves are refused. With tiny steps, the walker barely moves: this one never leaves the big hill. And each footprint sits near the last, so fifty thousand steps are worth only a few thousand independent draws.

**10. Landing (3:12–3:22)** — back to the cold-open frame, histogram in place; small-hill share 25 %.
> So the small hill gets a quarter, not nearly zero. The walker never learned how big the hills were. Comparing two heights at a time was enough to map them.

## Sources
- Metropolis, Rosenbluth, Rosenbluth, Teller & Teller (1953), "Equation of State Calculations by Fast Computing Machines", J. Chem. Phys. 21(6):1087–1092, doi:10.1063/1.1699114.
- Hastings (1970), "Monte Carlo sampling methods using Markov chains and their applications", Biometrika 57(1):97–109, doi:10.1093/biomet/57.1.97.
- Arianna Rosenbluth's role: Gubernatis (2005), Phys. Plasmas 12:057303; M. N. Rosenbluth (2003), AIP Conf. Proc. 690:22–30.
