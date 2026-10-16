# Episode 5, review round 1 (craft critic: visual design, motion, A/V sync)

Evidence used: the `review/` pack (metrics.json 01:26 is newer than final.mp4 01:25), report.md, all 14 contact sheets, full-resolution keyframes kf_01, 04, 05, 08, 15, 17, 21, 24, 26, 33, 36 and 38, and extra frames I pulled with ffmpeg at 1:05.8, 1:46.0, 1:46.8, 1:48.2, 1:52.4, 2:08.0, 2:10.0, 2:39.8, 2:43.6, 2:46.4, 2:47.1, 2:47.6, 3:17.0 and 3:33.6, plus 2–4 fps strips over 1:57.5–2:01 and 2:38.5–2:41.5. I also read script.md, facts.md, narration_diff.txt, transcript.txt and data.json, and recomputed the numbers in Python.

```
EPISODE: 005 — "Why Random Darts Beat Grids in 100 Dimensions"
IDEA: A grid of N points in d dimensions gets only N^(1/d) values per axis and collapses (one point, 50 points off, at d = 100), while each random dart is an independent coin flip with chance equal to the answer, so the darts' error is one dart's spread over root N, with no d in it.
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 8 · Audio 8.5 · Concision 7.5 · Originality 9
WEIGHTED: 8.2   AFTER CEILING: 8.2  (lowest 7.5 + 2 = 9.5, so the ceiling does not bind)
CAPS: none (all mechanics inside the bar; no settled overlap, typo, missing citation or factual error found)
FINAL: 8.2   PASS: no
FACTS:
- 10^6 grid points in 100-D give 1 value per axis (floor(10^(6/100)) = 1) | Verified | recomputed
- 2^100 = 1,267,650,600,228,229,401,496,703,205,376 (31 digits), matches on screen @0:21 | Verified | recomputed
- Quarter disc of r = √(2/π) has area exactly ½ | Verified | recomputed
- 10×10 midpoint grid puts 52/100 inside; 100 darts put 44 inside | Verified | recomputed grid; data.json darts2d.count = 44
- Ball covering exactly half the box in every d (r² = 33.30 at d = 100) | Verified | data.json cdf_check ≈ 0.5
- Values per axis 1000/100/10/3/1/1; points used 10^6/10^6/10^6/59,049/1/1 | Verified | data.json grid
- Centre inside the ball from d = 20 on (d/4 = 5 ≤ 6.63), so the grid says 1.000, 50 points off | Verified | data.json r2
- 2 values on 19 axes = 2^19 = 524,288 points, 17.6 ≈ 18 points off | Verified | P(Bin(19, ½) ≤ 10) = 0.6762 recomputed
- Darts (10^6, simulated) under 0.1 point in all six dimensions shown (max 0.038) | Verified (simulated) | data.json darts
- 10^6 points on the diagonal: 57.7% inside, 7.7 points off | Verified | data.json diag100
- Gauges 1.20 > 0.64 (2-D) and 31.8 < 33.3 (100-D) | Verified | data.json
- 300 runs of 100 darts: ±4.8 / ±4.8 pts; of 400 darts: ±2.6 / ±2.4 pts | Verified (simulated) | data.json hist SDs 0.0485, 0.0481, 0.0262, 0.0236
- 16 ±½ misses stray about 4 halves; N stray about √N halves; per dart ½/√N | Verified | SD of a sum of N ±½ = ½√N
- ½/√(10^6) = 0.0005 = 0.05 points; two runs in three land closer; all six did | Verified | 0.683; all six errors < 0.05
- Grid error ∝ N^(−2/d) for smooth f; Monte Carlo σ/√n for all d | Verified | Glasserman 2003, §1.1.1 (quoted in facts.md; consistent with the standard text)
- Metropolis & Ulam 1949, JASA | Verified | JASA 44(247):335–341
- Bergstra & Bengio 2012: random search as good as grid search in a fraction of the time; 9 grid trials test 3 values, 9 random test 9 | Verified | JMLR 13:281–305, abstract and Fig. 1
- Radius-1 ball in 30-D fills 2.04 × 10^-14 of the box; drops below 10^-6 after d = 17 | Verified | recomputed π^(d/2)/Γ(d/2+1)/2^d
MECHANICS: runtime 3:57.1 · wpm 163 (speech time) · max silence 1.73 s · max static 3.23 s (3:04.3–3:07.5, the planned prediction hold) · −14.0 LUFS / −2.0 dBTP · lead 0.0 s / trail 1.8 s · WER 2.5 %

FIXES (highest impact first):
1. [2:40.6–2:47.0][Clarity + Motion] The argument jumps from "√N halves" (the total miss of N darts) to "spread = ½/√N" without the divide-by-N step. On screen the walk's √N simply flies into the denominator (2:43.6–2:46.4), so the viewer has to take the move on faith. → Insert one TransformMatchingTex chain: "total miss ≈ √N · ½" → "share's miss = (√N · ½) / N", where the N in the denominator is a TransformFromCopy of the BLUE N in "N halves if they never cancelled". Then go to "½/√N" and flash the cancelled √N for under 1 s. Narration (+2 s): "Divide by the N darts: a half over root N." This lifts Clarity to 9 and makes the formula come out of the picture, as BAR §5 asks.
2. [2:47–3:13][Visual + Motion] For 26 s the frame holds only an equation on an empty background (2:49, 2:51, 2:55, 3:01, 3:07, 3:11 and kf_33 @3:12.5 are all formula-only). The insight picture is gone just as the payoff arrives. → Keep the walk and the 0–1 coin line at 30 % opacity to the left of the formula through B16. On "back to our ball with a million darts" (2:59.8), bring the dimension chart back at 30 % (it currently returns only at 3:14) and compute √1,000,000 → 1000 → 0.05 points beside its dashed line, so that "0.05 points" drops onto the line on "five hundredths". Also add one check label next to the formula at 2:49: "½/√100 = 5 pts ≈ 4.8 measured". It ties the law back to the histograms (SMH-style measure).
3. [1:48–2:01][Clarity] "Shadows alone are not the fix" shows the diagonal failing (7.7 points off) but never says why. The cause, that all coordinates are equal and the points move together, is left for the viewer to infer, and it is the exact contrast that "on its own" (2:03) depends on. → Add to the label under "one point: (t, t, …, t)": "every coordinate the same". Change the narration to "…and still miss by eight points: the million points move in lockstep." At 2:03, on "on its own", flash the single flat diagonal line (dimmed) against the jagged dart polyline.
4. [whole][Concision] At 3:57 the episode sits at the runtime ceiling, and the insight section (1:36–3:13) chains six sub-moves (shadows, diagonal, coin collapse, flip, histograms, walk, σ/grid law). That produces the midway sag. → Trim about 12 s: cut "Hold that thought." (0:36.3–0:38.3; the "off by ?" readout already holds it). Merge "In two dimensions, the estimates spread this wide. In 100, just as wide." into "In two dimensions or a hundred: the same width." (−2 s). Cut "Two runs in three land closer, all six of ours did." (3:11.9–3:16.2; the dashed "typical miss" line and the six dots already show it). Shorten B9 to "Even half a million points, two values on 19 axes: 18 points off." (−1.5 s).
5. [2:21–2:31][Visual] The histogram beat has three competing focal points in one row: left histogram, the 0–1 coin close-up with its red ½ bracket, and the right histogram (kf_26 @2:31.1). The coin line sits in the gap and its "1" nearly touches the right histogram's frame. → Move the coin line to the top centre at 30 % (or offstage) while the histograms fill. Widen each histogram by about 15 % into the freed space, and bring the coin back at full opacity only at 2:31.4 ("Each dart misses by a half").
6. [2:33–2:45][Visual] The random walk, the episode's best "why" picture, is drawn small and thin: steps about 0.3 units, about 3 px strokes, in one band between y ≈ 0 and −0.6 (f@2:39.8), with the upper-left third of the frame empty. → Scale the walk group 1.5×, centre it at (−0.8, −0.2), use stroke width 6 on the steps, and put the 0–1 coin line at 60 % in the lower right.
7. [3:16.2–3:18][Motion] The chart's curves morph letter by letter into "grid search" and "random search". The mid-transition frame (3:17.0) shows scrambled glyphs ("gri d search", "randomsearch" with overlapping letters) over the ghosted chart. The motion is decorative and looks broken. → FadeOut the chart (0.6 s), then Write both titles. Better: Transform the PURPLE grid curve's dots into the 3×3 grid-search dots and the BLUE curve's dots into the 9 random dots, so that correspondence carries the meaning.
8. [3:33–3:35][Motion] The Bergstra–Bengio squares' axes morph into the limit chart's axes (f@3:33.6). That implies "important setting" became "dimensions", a false correspondence. → Cross-fade instead, or carry meaning: Transform the 9 BLUE random dots into the dashed BLUE 1/N line as "Darts do have a blind spot" begins.
9. [1:36.6–1:40][Audio/sync] "Look at the shadows on one axis" is spoken while the chart is still unfolding into the squares (1:37), and the rails stay empty until about 1:40 (sheet 6). The deictic lands about 2 s early. → Start the shadow drop on the word "shadows" by moving the unfold 1.5 s earlier, or add a 1.0 s pause before the sentence.
10. [2:39.5–2:40.6][Motion] "16 halves / if they never cancelled" is legible for only about 1.0 s before 16 becomes N (2:38.5–2:41.5 strip). BAR §5 asks for at least 1.5 s. → Add a 0.6 s pause after "not 16" and start the 16 → N swap on "N darts".
11. [2:46.4–2:47.2][Visual] On its way to centre, the formula slides down through the fading "N halves / if they never cancelled" label (f@2:47.1: √N lies on top of "halves"). → Fade the walk labels out first (0.3 s), then move the formula.
12. [0:00–0:05][Hook] The first 5 s show 100 identical grey axes with no motion except the header (kf_01). It is clean but not irresistible. → Draw the axes on with a left-to-right sweep during "Your budget, a million evaluations", and show the "d = 100" counter ticking 1 → 100 as "100 inputs" is spoken, so the first frame already says "this is a lot of dimensions".

REACHES 9 IF ALL FIXED: yes, but narrowly. Fixes 1–3 bring Clarity to 9 and Visual/Motion to 9. Fix 4 brings Concision to about 8.5 and fix 9 brings Audio to 9, which gives about 9.0 weighted. The structure is right (hook → 2-D build → measured collapse → mechanism → law → real payoff → honest limit → return to the cold open). What remains is attaching the symbolic second half to pictures and tightening it.
KEEP:
- The parallel-coordinates cold open, where a million-point grid in 100-D is one flat purple line through "the centre", and its return at 3:50 with the blue darts flooding every axis.
- The dimension chart with its "values per axis / points used" table, where each spoken number lands with its column (1:11–1:35), and the grid dots flying into "100" and the axes into the exponent's "2" (1:43–1:47).
- The dart gauges, where one dart is outside in 2-D (1.20 > 0.64) but inside in 100-D (31.8 < 33.3), collapsing into the coin blocks (2:03–2:11).
```

## Notes behind the scores

- **Hook 8.5.** The prediction lands by 0:11 with a 1.7 s hold (0:11.3–0:13.0), the answer "one" is surprising and concrete, the open loop "off by ?" (0:35) closes at 3:11, and the landing re-sees the first frame. What keeps it under 9 is the midway sag from the long chain of sub-arguments (1:36–3:13) and a static first frame.
- **Clarity 8.** Concrete before abstract, every number checks, and assumptions are stated (σ for other functions, the tiny-answer limit). There is one real notation jump (fix 1) and one unnamed cause (fix 3).
- **Visual 8.** The semantic palette holds for the whole episode (PURPLE grid, BLUE darts, YELLOW d, RED error), citations sit bottom-left above y = −3.2, chart axes carry names, and type sizes are at or above the minimums. Deductions: the 26 s equation-only stretch (2:47–3:13), three focal points at 2:21–2:31, and the undersized walk at 2:33–2:45.
- **Motion 8.** Most transforms encode correspondence (polyline → dot at 0:38–0:41, square → cube → thumbnail, centre dot → chart points at 50, column → squares at 1:37, darts → coins, ½ bracket → walk steps, 1/N line → cold-open header at 3:50). The deductions are the decorative glyph-scramble at 3:17, the false-correspondence axis morph at 3:33, the short 16-halves hold, and the formula-only motion of the payoff.
- **Audio 8.5.** Loudness and peak are on target, pace is 163 wpm, pauses are intentional (both prediction holds, plus 1.7 s after the two laws), and WER is 2.5 % with no mistranscribed terms ("Bengio", "Ulam" and "dth" all came through). "This quarter disk" (0:42), "like this one" (0:29–0:34), "spread this wide / just as wide" (2:23–2:27) and "below this line" (3:42) all land. The "shadows" deictic is early (fix 9).
- **Concision 7.5.** Little is outright padding, but at 3:57 there is about 10 % trimmable restatement (fix 4).
- **Originality 9.** The 100-D parallel-coordinates view of grids, diagonals and darts, the "the grid is one point" reveal, and the dart → coin gauge are non-obvious images worth sharing. No §4 banned phrases or patterns were found in the transcript (the kit also reports 0).
