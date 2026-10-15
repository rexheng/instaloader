# Episode 15 — The Dead Fish That Lit Up an fMRI Scanner

**One idea:** each test has a small false-alarm rate, but the chance a whole scan stays clean is
(1 − α)^m, which collapses as the number of tests m grows; so the threshold must shrink with m (α/m).

## Palette (colour -> one meaning)
| Colour | Meaning, whole episode |
|---|---|
| GRAY (voxel fill, brightness = noise level) | a voxel that did not pass its test; axes; secondary labels |
| RED | a false alarm: a voxel flagged by noise; the red part of the bar = P(at least one false alarm) |
| BLUE | P(clean): the chance that no test has raised a false alarm yet |
| YELLOW | the per-test threshold α (and the uncorrected threshold lines / uncorrected studies) |
| GREEN | the corrected threshold α/m |
| PURPLE | a truly active voxel (power demo only) |

## Beats (narration exactly as synthesized)

**Cold open (0:00–0:15)** — voxel fish sweeps in, one voxel boxed, the question builds below.
1. This salmon was dead when it went into the brain scanner.
2. Every tiny cube of it, every voxel, gets its own test, and each test raises a false alarm one time in a thousand.
3. A typical scan has about a hundred and thirty thousand voxels. With nothing alive in there, what are the odds of at least one false alarm? Make a guess. [pause 1.5]
   *(prediction pause; the question P(at least one false alarm) = ? stays pinned top-right until answered.)*

**Stakes (0:15–0:30)** — schematic brain-cavity cluster turns red; citation.
4. In two thousand nine, Craig Bennett's team did this for real. They showed the dead fish forty-eight photos of people in social situations, and asked what each person was feeling. A cluster in its brain lit up.
5. If noise can fool a scan of a dead fish, it can fool any brain map.

**Naive build (0:30–1:05)** — simulated fish; voxel brightness = noise; yellow sweep tests each column.
6. So build the scanner yourself. Here is a simulated fish, a thousand voxels of pure noise.
7. Version one tests each voxel at the textbook threshold, p less than point oh five.
8. Fifty-one voxels light up, some in little clumps. That's the threshold doing its job: one false alarm per twenty tests.

**Fail / iterate (1:05–1:20)**
9. Version two uses the salmon study's threshold, p less than point oh oh one. Two voxels survive.
10. Better. But the real scan had a hundred and thirty times more voxels.  *(fish -> one tile of 130)*

**Insight (1:20–2:20)** — the bar of P(clean), sliced by each test; formula read off the bar.
11. To see why that matters, go back to one in twenty. This bar is the chance that the whole scan stays clean.
12. The first test keeps ninety-five percent of it, and loses the rest to a false alarm.
13. The second keeps ninety-five percent of what's left. For independent tests, after m of them, the clean part is point nine five to the m.
14. Fourteen tests, and it's below a half. A thousand, and it's about five times ten to the minus twenty-three.
15. Now set alpha to one in a thousand. Our thousand-voxel fish stays clean only thirty-seven percent of the time.
16. At a hundred and thirty thousand voxels, it's three times ten to the minus fifty-seven. So, your guess: a false alarm is certain, and about a hundred and thirty are expected.

**Fix + honest limit (2:20–2:55)**
17. Fix it by dividing alpha by m, so each test gets stricter as the tests pile up.
18. Now each test can take at most alpha over m from the bar, so all m tests together take at most alpha.
19. On our fish, that's p less than five in a hundred thousand, and the last two voxels go dark.
20. The price is power. A truly active voxel, with a signal three times the noise, used to pass ninety-one percent of the time. Now, nineteen percent.
21. So brain imagers use gentler corrections, like the false discovery rate, that still count the tests.

**Payoff (2:55–3:15)**
22. That's the salmon result. Uncorrected, at p less than point oh oh one with clusters of at least three voxels, the fish showed a cluster in its brain cavity. With false discovery rate or family-wise correction, nothing.
23. Yet in two thousand eight, about one in four fMRI studies in the journal NeuroImage skipped this correction.

**Landing**
24. The salmon never saw a single face. It just gave a one in a thousand fluke a hundred and thirty thousand tries.

## On-screen citations
- Bennett, Baird, Miller & Wolford, 2010 · J. Serendipitous and Unexpected Results (Ig Nobel 2012)
- Benjamini & Hochberg, 1995 · J. Royal Statistical Society B
- Simulated data labelled "simulated" on screen.
