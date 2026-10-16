# Episode 5, review round 3 (substance: science and story editor)

**Evidence.** I reused the existing `review/` pack, because metrics.json (22:24) is newer than final.mp4 (22:22). I read:
- report.md, narration_diff.txt, transcript.txt and transcript_words.tsv.
- All 13 contact sheets.
- 17 full-resolution keyframes: kf_01, 03, 05, 09, 10, 12, 15, 19, 22, 24, 27, 29, 30, 32, 33, 35, 37 and 40.
- 22 extra frames extracted with ffmpeg into /tmp/ep5r3s:
  - 0:10.6, 0:20.2, 0:36.6, 1:06.5, 1:47.0, 2:13.5, 2:24.3, 2:44.5 and 2:51.0;
  - a 0.2–0.6 s sequence over 0:17.0–0:20.0 (the 2^100 line);
  - 1:33.6–1:34.8 (the chart → squares morph);
  - 2:27.6–2:28.4 ("this wide");
  - 3:25.4–3:26.6 ("this line").
- script.md, facts.md, narration.txt and sim.py (darts section).

I recomputed every number independently in Python against data.json:
- the half-volume radii (2×10^6-point MC per dimension);
- every grid estimate, by exact lattice enumeration;
- the 2^19 rescue, exactly (binomial);
- the diagonal threshold;
- the 2-D dart count and dart #1, the 100-D dart's Σx², and the 100-D coin count;
- the four histogram SDs;
- the radius-1 ball volumes and P(0 hits);
- P(|Z| < 1) and its 6th power.

I also re-ran the seed-2024 million-dart simulation from scratch, and it reproduces all six hit counts exactly. I checked all three citations by web search (jmlr.org abstract page, tandfonline and the JSTOR scan, the Springer/LoC listing).

```
EPISODE: 005 — "Why Random Darts Beat Grids in 100 Dimensions"
IDEA: A million-point even grid gives each of d axes only N^(1/d) values (one value, the centre, from d = 20 on), so its answer collapses. Each random dart is an independent coin whose chance of "inside" is the answer itself, so the darts' error is σ/√N with no d in it, until the answer itself becomes tiny.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 9
WEIGHTED: 8.5 (127.5 + 212.5 + 127.5 + 127.5 + 85 + 80 + 90 = 850 / 100)   AFTER CEILING: 8.5 (lowest 8 + 2 = 10, does not bind)
CAPS: none
  - Facts: I found no Wrong or fabricated claim (see FACTS).
  - Citations: every empirical claim has one on screen. Glasserman at 0:20.5–0:24.5, Metropolis & Ulam at 0:24.5–0:31.5, Bergstra & Bengio at 3:00–3:16. Each is held ≥ 3 s.
  - Mechanics: everything is in band (see MECHANICS).
  - §4 slop: 0 banned phrases. There are no question chains: each question is followed by a statement or a hold (0:08, 0:31, 1:33, 2:47). "Darts do have a blind spot: tiny answers" (3:16) has no teaser question, so I did not count it as a colon fake-reveal.
  - Layout: the overlaps I saw are mid-crossfade only, never held: the Metropolis citation over the fading-in "a million random points: off by ?" at 0:31.3 (kf_05), and the σ ↔ ½ cross-dissolve at 2:44.5.
FINAL: 8.5   PASS: no
```

## FACTS

| # | Claim | Status | My check / source |
|---|---|---|---|
| 1 | 10^6 grid points in 100-D → **1** value per input, the centre | Verified | floor(10^0.06) = floor(1.148) = 1; one midpoint per axis = (½, …, ½) |
| 2 | 2 values per input → 2^100 points; on screen 1,267,650,600,228,229,401,496,703,205,376 (0:19.6) | Verified | `str(2**100)` matches digit for digit, 31 digits |
| 3 | Pricing an option on 100 stocks is this kind of average (Glasserman, 2003 · Springer) | Verified | Glasserman, *Monte Carlo Methods in Financial Engineering*, Springer (Applications of Mathematics / SMAP 53), §1.1: derivative prices are expectations, i.e. high-dimensional integrals |
| 4 | "Since Metropolis and Ulam's 1949 paper, such averages use random points" (Metropolis & Ulam, 1949 · JASA) | Verified, but overstated | JASA 44(247):335–341, Sept 1949 (JSTOR scan; doi 10.1080/01621459.1949.10483310). The publication is right. "Use random points" is too absolute: deterministic quasi-random (Sobol/Halton) points are standard for exactly this kind of high-dimensional finance integral (Paskov & Traub 1995, 360-D CMO). Fix 6 |
| 5 | Quarter disc share = exactly ½ | Verified | r² = 2/π → πr²/4 = ½ |
| 6 | 10×10 grid: 52 inside, 2 points off | Verified | enumeration = 52; filled dots in kf_09 = 3+5+6+7+7+8+8+8 = 52 |
| 7 | 100 darts: 44 inside, 6 points off; the cold-open dart is outside | Verified (simulated, labelled) | recount 44; dart #1 = (0.625, 0.897), Σ = 1.196 > 0.637. The same two coordinates head the 100-D polyline at 0:31 and 2:12 (I measured the pixels) |
| 8 | "The disc becomes a ball that always covers exactly half the box" | Verified | MC median of ΣU²: 0.9698, 1.968, 3.302, 6.635, 33.30 at d = 3, 6, 10, 20, 100, against data.json r² = 0.9697, 1.967, 3.301, 6.635, 33.30 |
| 9 | Values per axis 1000, 100, 10, 3, 1, 1; points used 10^6, 10^6, 10^6, 59,049, 1, 1 | Verified | floor(10^(6/d)); 4^10 > 10^6; d = 19 would still get 2, so "from twenty on" is exact |
| 10 | Grid errors 0.002, 0.001, 0.10, 2.4 points (plotted) | Verified | exact enumeration: 0.50002, 0.499989, 0.501022, 0.524463 |
| 11 | Centre inside the ball → "grid says 1.000", 50 points off | Verified | d/4 = 5 ≤ 6.63 (d = 20); 25 ≤ 33.30 (d = 100) |
| 12 | "The largest two-value grid that fits, half a million points, is 18 points off" (2^19 points) | Verified number, imprecise wording | P(Bin(19,½) ≤ 10) = 0.67620 → 17.6 points. The grid is two values on 19 axes plus the centre on the 20th, not a two-value grid. A true two-value grid needs 2^20 > 10^6 and does not fit (fix 7) |
| 13 | Darts (10^6, simulated) "under a tenth of a point in every dimension" | Verified (re-simulated) | seed 2024 reproduces 500382, 499867, 500222, 500280, 499747, 500038 hits → 0.038, 0.013, 0.022, 0.028, 0.025, 0.004 points |
| 14 | 100 grid points cast 10 shadows; 100 darts cast 100; N^(1/d) | Verified | algebra |
| 15 | A million points on the diagonal → 57.7 % inside, 7.7 points off | Verified (exact) | t ≤ √(33.3015/100) = 0.57707 → 0.577075 |
| 16 | Gauges: x1²+x2² = 1.20 > 0.64 → 0; x1²+…+x100² = 31.8 < 33.3 → 1 | Verified | 1.1957 vs 0.6366; 31.766 vs 33.302. Bar geometry measured in kf_24: 0.316 and 0.597 of the 0–2 scale; 0.832 and 0.79 of the 0–40 scale |
| 17 | Each dart lands inside with chance = the answer, independently, in any d; the estimate is the share of heads in N flips | Verified | uniform ⇒ P(inside) = volume; iid ⇒ Binomial(N, p) |
| 18 | One flip: average ½, always misses by exactly ½ | Verified (exact for p = ½) | Bernoulli(½): \|X − ½\| = ½ |
| 19 | 300 runs: ±4.8 / ±4.8 pts → ±2.6 / ±2.4 pts at N = 400; "both get twice as narrow" | Verified (simulated) | SDs 4.84, 4.80 → 2.61, 2.35 (theory 5.0 → 2.5). "Twice" is the theory; the simulated ratios are 1.85 and 2.04, which is fine for 300 runs |
| 20 | spread = σ/√N; "any other function swaps that half for its own spread"; no d | Verified | Glasserman §1.1.1: σ_f/√n "for all d" |
| 21 | Our ball, 10^6 darts: ½/1000 = 0.0005 = 0.05 points | Verified | exact for p = ½ |
| 22 | "Two runs in three land closer; all six of ours did" | Verified | P(\|Z\| < 1) = 0.6827; all six errors < 0.05; 0.683^6 = 0.10, stated as what happened |
| 23 | Bergstra & Bengio 2012: random search tuned neural nets as well as grid "in a fraction of the time" (JMLR) | Verified | JMLR 13(10):281–305 (2012), abstract: "as good or better within a small fraction of the computation time" |
| 24 | "Nine grid trials test three values of it; nine random trials test nine" | Verified | same paper, Fig. 1 caption. The redraw is labelled "schematic"; at 3:15 the nine random shadows are visibly distinct |
| 25 | Radius-1 ball fills 2 parts in 10^14 of the box at d = 30 | Verified | π^15/15!/2^30 = 2.041e-14 |
| 26 | "Below this line a million darts expect under one hit, so they usually report zero" | Verified | the curve crosses 10^-6 between d = 17 (1.076e-6, which is above the line) and d = 18 (3.13e-7). P(0 hits) is 0.73 at d = 18 and 1 − 2e-8 at d = 30. The shading starts at 17.06 (kf_37) |

I found no Wrong and no Fabricated claims. Two claims are imprecise without being wrong: #4, which overgeneralizes, and #12, which misnames the grid.

## MECHANICS
```
runtime 3:42.2 · wpm 163 (speech) / 159 overall · max silence 1.73 s (0:10.0, planned prediction hold) · leading 0.00 s · trailing 1.48 s · max static 2.97 s · −14.0 LUFS / −2.1 dBTP · WER 3.4 % · 0 banned phrases · 0 black frames · layout audit 0 issues
```
- **Pronunciation.** "Bengio", "Ulam", "Metropolis" and "d-th" all transcribe correctly. Every narration_diff entry is a spelling or number-format artifact (a→one, disc→disk, centre→center).
- **Cadence.** Beat boundaries now get 0.7–0.8 s (0:34.7, 0:57.8, 1:08.6, 1:32.5, 1:53.3, 2:58.6, 3:15.3) and within-thought breaks get 0.3 s. The round-2 metronome problem is fixed.
- **Deictics.** Four checked, all landing on cue:
  - "like this one" (0:30.4) lands while the polyline finishes drawing;
  - "this quarter disc" (0:39.3) lands as the arc draws;
  - "this wide" (2:27.7) lands while the ±4.8 bracket is already up;
  - "this line" (3:25.4) lands as the dashed 1/N line draws (3:25.4 → 3:26.0).

## Story read (BAR §6)

**Cold open and stakes (0:00–0:35): excellent.**
- The 100 parallel axes, "How many values does each input get?", a 1.7 s hold, then "One." This is a real commitment and a real jolt.
- 2^100 makes it visceral, the option makes it matter, and "How far off would a million of them land?" opens a loop that closes at 2:51.

**Naive build and fail (0:35–1:32): the best stretch.**
- In 2-D the grid honestly wins.
- At a fixed budget the error climbs to 50 points, with an honest "points used" row and a budget-fair rescue that is still 18 points off. This is textbook SMH.

**Insight (1:33–2:58): now logically complete, but one step is shown rather than explained, and one comparison is mismatched.**
- The shadow beat explains the grid side (N^(1/d)).
- The diagonal closes the "more shadows" misreading.
- The gauges plus "lands inside with a chance equal to the answer, on its own" state the real mechanism.
- *Gap 1: √N is never motivated.* The viewer sees one experiment (N = 100 → 400 halves the spread) and is told "that half, over the square root of N" (2:31–2:36). Why √N, and not N, is never shown. The cancellation of independent ±½ misses is the heart of "no d", and it is skipped. A viewer could repeat the claim but not re-derive it.
- *Gap 2: the side-by-side "laws" at 2:41–2:44 compare unlike quantities.* "N^(1/d) values per axis" is a count where bigger is better. "spread = σ/√N" is an error where smaller is better. The frame claims the punchline (one law has d, the other doesn't), but it does not compare like with like.
- *Redundancy.* "Why does the grid collapse?" (1:33) is answered with what the chart's "values per axis" row showed 20 s earlier, and the cold open showed it before that. The shadow narration (1:33–1:54, about 20 s) is the third telling of the same fact.

**Payoff and limit (2:59–3:33): strong.** Bergstra & Bengio reuses the shadow device (3 vs 9 shadows). The tiny-answer limit is precise: the shaded zone starts exactly where the curve crosses 1/N.

**Landing (3:33–3:42): resolves the opening.** The cold-open frame returns: the single purple centre line, flooded by blue polylines, under "1,000,000 coin flips". "The darts never noticed the axes" re-sees 0:00.

## FIXES (highest impact first)

1. **[2:31–2:37][Clarity + Motion] Show why it is √N, don't just measure it.**
   - Narration: after "Quadruple the darts, and both get twice as narrow," insert: "Each dart misses by a half, up or down at random, so the misses partly cancel: N of them stray about root N halves, not N."
   - Visual (~6 s): take 16 of the 2-D coins as ±½ arrows (RED). First show them laid head-to-tail all aligned, a length of 8 halves, dimmed as "if they never cancelled". Then show them in their random order: a zig-zag random walk whose net, about 2 halves = √16 · ½, is bracketed.
   - Then `TransformFromCopy` that net bracket into the √N under the ½. The formula is then derived on screen rather than read off one data point.
   - Pay for it with fix 3.
2. **[2:40–2:44][Clarity] Make the side-by-side laws comparable.**
   - Replace "N^(1/d) / values per axis" with "grid cell width = 1 / N^(1/d)" (YELLOW d), which is exact for the midpoint grid. Under it, put a small note "d = 20: width ≈ 1, one cell = the box".
   - Narration: "The grid's cell width has d in it; the darts' spread doesn't." This replaces "The root N stays, and there's no d in it."
   - Both sides are then lengths where smaller is better, and the "no d" contrast reads at a glance.
3. **[1:33–1:54][Concision] Cut the third telling of "values per axis".**
   - Replace the four sentences "Why does the grid collapse? … cast a hundred. A hundred points over two axes: ten per axis, the square root of a hundred." with: "Look at the shadows on one axis: the grid's hundred points cast ten, a hundred darts cast a hundred."
   - Then go straight to "With N points over d axes, each axis gets the d-th root of N." Keep the 100^(1/2) → N^(1/d) morph.
   - Saves about 8–9 s and keeps the shadow device that Bergstra & Bengio reuses at 3:11.
4. **[0:19.4–0:20.0][Visual] The 31-digit 2^100 is fully legible for only about 0.4 s.**
   - It finishes writing at about 19.5 s and is fading by 20.0 s (frames 19.4/19.6/19.8/20.0). §5 reading time is ≥ max(1.5 s, 0.8 + 0.3 × words).
   - Start the `Write` on "two to the hundredth" (0:17.3) with run_time 1.2. Lengthen the following pause to 0.8 s. Hold it to 0:21.0, cross-fading into the Glasserman line.
5. **[2:23–2:35][Visual] The shrunken coin line is too small.**
   - Its labels 0, ½, 1 and the RED ½ above the bracket are about 20 px cap height in kf_27, under §5's 24 px tick minimum, and this ½ is the referent the formula's numerator flies from.
   - Shrink it to 0.75× instead of about 0.45×, and centre it between the histograms at y ≈ 0.4, so the flying ½ is legible at its origin.
6. **[0:23.5–0:31][Clarity] "Such averages use random points" overclaims.**
   - Deterministic quasi-random points (Sobol, Halton) are standard for exactly this kind of high-dimensional finance integral (Paskov & Traub 1995).
   - Change it to "such averages are usually done with random points".
   - Optionally add to the limit beat (3:16): "and cleverer non-random patterns can sometimes beat darts", with the citation "Paskov & Traub, 1995 · J. Portfolio Management" on screen. This keeps "random beats grids" honest without implying that randomness itself is the only cure.
7. **[1:23–1:29][Clarity] "The largest two-value grid that fits" misnames the design.** The design is two values on 19 axes plus the centre on the 20th.
   - Narration: "Even two values on nineteen of the axes, half a million points, is eighteen points off."
   - Label: "2 values on 19 axes · 2^19 points".
8. **[2:35–2:53][Visual] Notation drift.** The formula's numerator is an inline "1/2" (kf_29, 2:51), while the coin line, the bracket and "true answer" all use a stacked ½. Typeset the numerator as `\tfrac{1}{2}`, so the ½ that flies in from the coin keeps its shape and the `TransformFromCopy` reads as the same object.
9. **[1:05.9–1:08.3][Motion] "The grid splits its million across the axes" plays over a near-empty frame.** At 1:06.5 there is only the thumbnail and a fading "d = 3". Start `Create` on the axes and the "values per axis" row label 1.2 s earlier, so the row exists when the sentence names it.
10. **[2:53.5–2:56.5][Visual] "spread = 0.0005 = 0.05 points" (3 terms) holds about 2.5 s before flying to the chart.** §5 asks for ≥ 2 s + 0.4 s × 3 = 3.2 s. Extend the hold by 0.8 s. The 0.35 s pause before "Two runs in three" can absorb it if it is raised to 0.8 s.

**REACHES 9 IF ALL FIXED:** yes, narrowly.
- My estimate: Hook 9 (the middle no longer re-explains), Clarity 9 (√N derived, laws comparable, wording exact), Visual 9, Motion 9 (the random walk is an animation that *is* the argument), Audio 8.5, Concision 9, Originality 9 → 8.95 ≈ 9.0.
- Fixes 1–3 carry the gain. Without fix 1, the episode stays at about 8.7.
- No structural change is needed. The skeleton already matches §6, and the one insight picture (gauges → coins → histograms → σ/√N) exists; it lacks only its middle step.

**KEEP:**
- The 100-axis parallel-coordinates cold open ("grid values per input: ? → 1") and its return at 3:35, flooded with blue coin flips.
- The fixed-budget dimension climb with the honest "points used" row, the 2^19 rescue and the diagonal counterexample: the SMH failure chain.
- The gauges that collapse one dart's 2 or 100 coordinates into a single 0/1 verdict (kf_24), feeding the identical 2-D and 100-D histograms.
