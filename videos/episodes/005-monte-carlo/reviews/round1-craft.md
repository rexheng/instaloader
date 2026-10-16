# Episode 5, review round 1 (craft critic: visual design, motion, A/V sync)

Evidence: `review/` pack (metrics.json 12:28 is newer than final.mp4 12:26), all 12 contact sheets, keyframes kf_01, 03, 05, 09, 12, 14, 18, 32 at full resolution, and extra frames pulled with ffmpeg at 0:50.8, 0:57.0, 1:05.5 (cube crop), 1:43.0, 1:53.3, 1:56.8, 2:12.6, 2:25.2, 2:35.8, 2:37.0, 2:37.6, 2:38.2, 2:38.8, 2:39.3, 2:55.5, 3:14.5 and 3:24.5. I also read the transcript, word timings, script.md, facts.md and scene.py (beats B12/B13).

```
EPISODE: 005 — "Why Random Darts Beat Grids in 100 Dimensions"
IDEA: A grid of N points in d dimensions gets only N^(1/d) values per axis, so it collapses as d grows, but each random dart returns one in/out bit, so the darts' error is a coin-flip spread (1/2)/√N with no d in it, unless the answer itself is tiny.
SCORES: Hook 8.5 · Clarity 7.5 · Visual 7.5 · Motion 7.5 · Audio 8 · Concision 8 · Originality 8.5
WEIGHTED: 7.9   AFTER CEILING: 7.9 (lowest 7.5 + 2 = 9.5, so it does not bind)
CAPS: none triggered. Two items come close and are noted, not applied:
  - overlap (cap 7): every text/element overlap I found happens during a transform, not in a settled layout: the digit swarm @0:50.8 and @0:57, the falling shadow ticks crossing "input 1" @1:43, and the dashed 0.5 truth line cutting "44/100"/"48/100" for about 1 s @2:12.6. If any of them is still on screen while it is at rest next round, cap 7 applies.
  - on-screen error (cap 6): from 2:29 to 2:38 the header reads "N = 1,000,000 darts" above histograms that still show the 400-dart experiments (±0.026 / ±0.024). The narration frames it as a hypothetical ("So with a million darts…"), so I count it as a clarity defect. If it is unchanged next round, I will treat it as a mislabelled plot.
FINAL: 7.9   PASS: no
FACTS:
  2^100 has 31 digits | Verified | recomputed (len(str(2**100)) = 31)
  A million points on a 100-D grid give 1 value per axis, the centre | Verified | floor(10^6^(1/100)) = 1
  Quarter disc of radius √(2/π) has area exactly 1/2 | Verified | π(2/π)/4 = 1/2
  The 10×10 midpoint grid has 52 points inside, 2 points off | Verified | recomputed count = 52
  100 darts give 44 inside, 6 points off | Verified (simulated, labelled "simulated") | sim.py
  Values per axis at 10^6: 1000, 100, 10, 3, 1, 1 | Verified | floor(10^6^(1/d))
  Grid error at d = 2 is 0.002 points | Verified | recomputed with a 1000×1000 midpoint grid
  The centre is inside the half-volume ball at d = 20 and d = 100 | Verified | d/4 = 5 ≤ r² = 6.63 (facts.md); consistent with the median of ΣU² ≈ d/3
  10^6^(1/20) ≈ 1.995, "fewer than two" | Verified | recomputed
  Spread of the share is √(p(1−p)/N) = (1/2)/√N at p = 1/2 | Verified | binomial SD
  (1/2)/1000 = 0.0005 = 0.05 points | Verified |
  Histogram SDs 0.048/0.048 → 0.026/0.024 after quadrupling | Verified (simulated) | consistent with the theory values 0.05 and 0.025
  "Every blue dot came in under it" | Verified as stated, but see the clarity note: the line is 1 SD, not a bound (P(all 6 under 1 SD) ≈ 0.10) |
  Radius-one ball fills 2.04e-14 of the box at d = 30; it drops below 10^-6 after d = 17 | Verified | recomputed: 1.08e-6 at d = 17, 3.1e-7 at d = 18
  Metropolis & Ulam 1949 published the Monte Carlo method (JASA 44(247):335–341) | Verified | facts.md + standard bibliography; cited on screen @0:27–0:36
  Bergstra & Bengio 2012: random search found models as good as grid search's, in a fraction of the time; with nine trials, grid tests 3 distinct values of the important setting and random tests 9 | Verified | JMLR 13:281–305, abstract and Fig. 1 caption; cited on screen @2:45–3:00
MECHANICS: runtime 3:25.1 · wpm 156 (speech time) · max silence 1.96 s (0:10.7, planned prediction hold) · max static 3.0 s (0:41–0:44) · -14.0 LUFS / -2.0 dBTP · leading 0.00 s · trailing 1.74 s · 0 banned phrases · WER 3.4 %
FIXES (highest impact first):
1. [2:24–2:28][Clarity+Motion] The key formula is not derived from the picture. "spread =" comes from the brackets, but the 1/2/√N term is just `Write`-n (frame 2:25.2 shows "1/?" being hand-drawn), and the "a half" (one coin's spread) is asserted and never shown. Fix: before the formula, pull ONE coin out of the 10×10 block onto a mini 0–1 line: its value is 0 or 1, with mean 1/2 and a ±1/2 red bracket. Then `TransformFromCopy` that ±1/2 bracket into the numerator. Next, `TransformFromCopy` the "N" from the "N = 400 darts" header into the denominator, and flash the √ while the 0.048→0.026 bracket shrink replays (4× darts → ½ width). This is the episode's central equation and must grow out of its referents.
2. [2:29–2:38][Clarity] The header "N = 1,000,000 darts" replaces "N = 400 darts per experiment" while the 400-dart histograms (±0.026/±0.024) stay on screen, so a paused viewer reads "a million darts → ±0.026", which is 50× wrong. Fix: leave the "N = 400 darts per experiment" header alone and dim both histograms to 30 % on "So with a million darts". Then substitute 1,000,000 only inside the equation (`TransformMatchingTex` of the N term).
3. [2:37.4–2:38.3][Motion/Visual] The answer "spread = 0.0005 = 0.05 points" is fully legible for under 1 s, and then a 0.9 s whole-scene dissolve (2:38.8 frame shows the two scenes double-exposed) replaces it. §5 asks for ≥ 3.2 s on a 3-term result. Fix: hold eq_v ≥ 3.2 s, then instead of FadeOut, `TransformFromCopy(eq_v[4], pred_lab)` so that "0.05 points" visibly becomes the dashed line's label on the returning chart. Bring the chart in with `ReplacementTransform`/`FadeTransform` per group, not a global cross-fade.
4. [1:52–1:54, 2:35–2:38][Motion] `TransformMatchingTex` falls back to cross-fades because the substrings don't match. The frames show double-exposed glyphs: "N^{1/d}100^{1/2}…valpes" @1:53.3, "√1,000,000 / 1000" stacked @2:35.8, and "0.0005 = 0.05 points" ghosted behind "1/2 over 1000" @2:37.0. Fix: build the MathTex with isolated tokens (e.g. `MathTex(r"\frac{1/2}{", r"\sqrt{", r"N", r"}}")`, and "values" as its own substring in both the "100^{1/2} = 10 values" and "N^{1/d} values per axis" forms), or use `TransformMatchingShapes` with an explicit `key_map`. Each step then morphs only the changed term, with the changed term flagged ≤ 1 s.
5. [1:05–1:11][Visual/Clarity] The "eighth of a ball in a cube" inset is drawn wrong. The floor arc bulges out past the cube's front-right edge (a loop at ~(795,440) px in kf_14), and the left-face arc pokes above the top edge (~(640,265) px). It does not read as a ball covering half the cube. Fix: generate the three boundary arcs as `ParametricFunction`s in 3-D (r = 0.985 of the edge), project them with the same oblique projection used for the cube edges, and add a faint INK fill. Check that the endpoints land on the cube edges.
6. [0:50–0:52, 0:56–0:58][Visual/Motion] The counters "52/100" and "44/100" are made by flying copies of digit glyphs out of every inside dot, which leaves a swarm of "5/2/4" glyphs over the square and over "input 1" (frames 0:50.8, 0:57.0). Fix: sweep an `Indicate` over the filled dots while a `DecimalNumber` under the square ticks 0→52 (and 0→44), with no glyph copies.
7. [0:50–1:01, 2:19–2:38][Clarity] The units switch without warning: the narration says "two points off" and "six points off", but the screen says "off by 0.02" and "off by 0.06". The brackets read "±0.048", the chart is in "percentage points", and the equation goes "0.0005 = 0.05 points". Fix: pick points everywhere the viewer reads an error: "off by 2 points", "off by 6 points", brackets "±4.8 pts" → "±2.6 pts", eq "(1/2)/1000 = 0.05 points".
8. [2:38–2:41][Clarity] "Every blue dot came in under it" presents a 1-SD typical miss as if it were a ceiling (about 1/3 of runs should exceed it; all 6 under has p ≈ 0.10). Fix the line: "…five hundredths of a point, the size of a typical miss, and that is where the blue dots sit, in every dimension." Keep the dashed line labelled "typical miss".
9. [0:23–0:25][Hook] The stakes are one bare assertion ("Yet such averages are routine"), and nothing concrete arrives until 2:41. Fix: foreshadow the payoff here, e.g. "Tuning a model with a dozen settings is exactly this problem," and keep the Metropolis & Ulam line. The 0:12 commitment then has a reason to matter.
10. [1:16][Audio] "a hundred in three" is elided: whisper hears "103" (1:16.3–1:17.7, script word "in" dropped), so the listener hears one hundred three. Fix: change the narration to "a hundred per axis in three," or put a comma pause: "a hundred, in three;". Re-check the transcript.
11. [1:35–1:38][Motion] The chart fades to an almost empty frame (1:37) and the two squares fade back in unchanged: a cut disguised as a fade, and the only beat where objects vanish instead of persisting. Fix: shrink the chart to a 30 % inset top-right, or `ReplacementTransform` the chart's purple/blue dots at d = 2 into the two square titles, so the return to 2-D is motivated.
12. [2:12–2:13][Visual] The dashed 0.5 truth lines are created before the coin blocks drop, so they bisect "44/100" and "48/100" (frame 2:12.6). Fix: `Create(truthL/R)` after the `ReplacementTransform` into the bars, or offset the count labels 0.35 left of the line.
13. [1:42–1:44][Visual] The falling shadow ticks pass through the "input 1" label (frame 1:43.0). Fix: fade "input 1" to 30 % during the drop and restore it after, or move the axis name to the left end of the rail.
14. [0:00–0:36][Visual] The cold-open block is off-centre: the axes span x ≈ 170–1440 px and leave ~480 px of empty right margin for a single label (kf_03, kf_05). Fix: shift the axes group right by ~1.0 unit and set "the centre"/"a random point" with buff 0.3 off the last axis, so the frame balances.
15. [2:45–3:00][Visual] "model score (schematic)" floats between the two panels and belongs to neither (frame 2:55.5), and a ~1.3-unit empty band separates the titles from the squares (2:45). Fix: attach one 26-pt label left of the grid-side curve as its y-name, and move both titles down 0.4.
REACHES 9 IF ALL FIXED: yes. The structure meets the bar: the cold-open commitment at 0:10 with a 1.7 s hold, the naive grid winning in 2-D, the measured collapse to 50 points off, the shadow insight, the 2-D/100-D histograms, the sourced payoff, the honest limit and the exact callback landing. What keeps it near 8 is execution: the central formula is not derived on screen (fix 1), there is one mislabelled frame (fix 2), and the transforms degrade into cross-fades exactly at the climax (fixes 3–4). Fixes 1–8 alone should lift Clarity, Visual and Motion to about 8.5–9.
KEEP:
- The 100-axis parallel-coordinates cold open: the single purple "centre" line for the grid, the random point as a blue polyline that collapses into the 2-D dart, and the landing that floods every axis blue (3:19–3:23).
- The coins → histogram sequence showing 2-D and 100-D spreads are identical (2:09–2:24). This is the episode's best "the animation is the proof" moment.
- The shadow argument (1:39–1:50) carried into Bergstra & Bengio's 3-vs-9 shadows on the score curve (2:53–3:00), which makes the payoff the same picture.
```

## Notes on audio/visual sync (checked against word timings)
- "like this one" (0:31–0:34): the blue polyline is drawing across the axes at that moment. Lands.
- "this quarter disk" (0:39): the arc is being created at 0:39. Lands.
- "the grid wins" (1:00): the grid readout gets its box at 1:01. Lands.
- "a thousand … three in ten" (1:13–1:20): each per-axis value appears on its word. Lands.
- "spread this wide" (2:15.5–2:18.6): the ±0.048 bracket grows only at ~2:18.5–2:19. About 1 s late but inside ±2 s; move `GrowFromCenter(brL)` to start on "spread".
- "Below this line" (3:11.6): the dashed 10^-6 line is created at ~3:12. Lands.
- I found no case where the narration names something that is not visible within ±2 s.
