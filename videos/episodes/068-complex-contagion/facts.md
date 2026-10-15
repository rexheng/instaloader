# Facts — Episode 68 (complex contagion)

Every claim spoken or shown, how it was checked, and where it comes from.

## Simulated (our model; labelled "simulated" on screen)
Model: 40 people on a ring, each tied to the 2 nearest on each side (k = 4, 80 ties). "Random" = the same 80 ties with every tie moved once by degree-preserving double-edge swaps (everyone keeps exactly 4 friends). Synchronous rounds: a person adopts when at least T friends have adopted (T = 1 "disease", T = 2 "habit"). Code: `sim.py`, `make_data.py` (seeded numpy RNG); output `data.json`.

| Claim | Check | Result |
|---|---|---|
| Ring, one seed, T = 1: everyone in 10 rounds | exact: front advances 2 per side per round, ceil(39/4) = 10 | Verified (sim prints 10) |
| Random network shown, one seed, T = 1: everyone in 4 rounds | sim on the displayed network; over 2,000 random rewirings: 4 rounds in 81 %, 5 in 19 %, mean 4.19 | Verified; the displayed network is the typical case |
| Ring, two adjacent seeds, T = 2: all 40 in 19 rounds, one person each way per round | exact: 38 / 2 = 19 | Verified |
| Random network shown, T = 2: stays at 2 of 40 | sim | Verified |
| "Two thousand random rewirings: not once did it reach all forty; eight times in ten it never got past the first two" | sim.py, 2,000 networks, random tied seed pair: P(all 40) = 0.000, P(stuck at 2) = 0.822, max reach 7, mean 2.22 | Verified |
| Ring: two adjacent people share exactly 2 friends (k − 2 in general) | exact: N(i) ∩ N(i+1) = {i−1, i+2} | Verified |
| Random: expected shared friends ≈ 3·3/38 ≈ 0.24 ("about a quarter of a person") | back-of-envelope: Ben's 3 other friends, each one of 38 other people, 3 of whom are Ann's. Simulated mean on degree-preserving rewired nets = 0.19 (exact 4-regular constraints lower it slightly). Spoken/shown with "about" / "≈" | Verified as an approximation; both values under a quarter |
| General: ≈ (k−1)²/(N−2) → 0 as N grows; N = 4,000 gives ≈ 0.002 | 9/3998 = 0.00225 | Verified |
| Dial: swapping 4 of 80 ties (5 %) drops the habit's average reach to 46 % (below half); the disease's rounds fall from 10 to 7.7 | make_data.py, 2,000 nets per point | Verified |
| Fully rewired: habit reach 5.6 % average; disease 4.2 rounds | make_data.py | Verified |

## Empirical (cited on screen)
| Claim | Verification | Source |
|---|---|---|
| Watts and Strogatz showed a few random shortcuts let a disease spread much faster | Paper: rewiring a lattice with a small fraction of shortcuts gives short path lengths; abstract: "infectious diseases spread more easily in small-world networks than in regular lattices"; their epidemic simulation shows the time to global infection falls sharply once a small fraction of ties is rewired | Watts & Strogatz (1998) *Nature* 393:440–442, doi:10.1038/30918 |
| "Complex contagion": a behaviour that needs contact with multiple sources; long ties can hinder it; bridges must be wide | Abstract and Wikipedia summary checked | Centola & Macy (2007) *American Journal of Sociology* 113(3):702–734 |
| 2010 experiment; 1,528 participants recruited from health-interest websites; anonymous profiles; matched with "health buddies" | Full text (Science HTML via BYU copy) read: "an Internet-based health community, containing 1528 participants" | Centola (2010) *Science* 329(5996):1194–1197, doi:10.1126/science.1185231 |
| Randomly assigned to clustered-lattice or random network; random = rewired lattice keeping each node's number of neighbours | Full text | same |
| Behaviour = registering for a health forum | Full text: "the decision to register for an Internet-based health forum" | same |
| Six trials, 12 networks, N = 98, 128 or 144, each with 6 or 8 buddies, 3 weeks each | Full text | same |
| Reached 53.77 % (clustered) vs 38.26 % (random) on average; shown as 53.8 % and 38.3 %, spoken "fifty four" and "thirty eight" | Full text | same |
| Spread more than four times faster in clustered networks: 0.2820e-3 vs 0.0643e-3 nodes/s = 4.4× | Full text; ratio recomputed = 4.39 | same |
| Differences significant, P < 0.01 (Wilcoxon / Mann-Whitney) | Full text | same |
| A second signal made adoption significantly more likely (P < 0.001, Cox model) | Full text: "significantly more likely to adopt after receiving a second signal than after receiving only one signal (P < 0.001 ...)" | same |
| Some people adopted after a single signal | Logical: at time 0 only the seed is active, so the first adopters in every network adopted on one signal; the paper's Fig. 3 uses "the baseline likelihood of adoption after receiving one social signal" | same |
| Strangers in designed networks; generalising to real friendships is an inference | Design: anonymous buddies, blinded identifiers, fixed topology | same (curriculum pitfall) |

## Deliberate simplifications (stated or visible)
- Our model uses strict thresholds; real people are probabilistic (said in beat 17; the frozen mini random ring labelled "strict model" sits beside the real 38.3 % bar, with no number attached so the two are not compared as like-for-like).
- We seed two tied friends for the habit; Centola seeded one node and let probabilistic adoption carry it.
- Complex contagion does not refute the strength of weak ties for information; the closing line keeps "for a rumour, plant it on the right".
