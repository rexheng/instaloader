# Episode 5, review round 2 (craft critic: visual design, motion, A/V sync)

Evidence: the existing `review/` pack (metrics.json 16:31 is newer than final.mp4 16:29): report.md, all 13 contact sheets, transcript and word timings, and narration_diff. Full-resolution keyframes read: kf_01, 02, 05, 10, 11, 15, 18, 20, 21, 29, 30, 36 and 40. Extra frames pulled with ffmpeg at 0:00.2, 0:38.6, 0:39.5, 1:00.6, 1:04.0, 1:06.5, 1:29.0, 1:49.0, 2:05.6, 2:06.6, 2:08.0, 2:08.8, 2:13.8, 2:24.6, 2:27.8, 2:39.0, 2:39.3, 2:41.8, 2:46.8, 2:49.5, 3:22.0, 3:23.0, 3:23.6 and 3:43.6. I also read script.md, facts.md, CHANGELOG.md and the round-1 craft review. I recomputed the key numbers in Python.

```
EPISODE: 005 — "Why Random Darts Beat Grids in 100 Dimensions"
IDEA: An even grid of N points in d dimensions gets only N^(1/d) values per axis and collapses as d grows. Each random dart returns one in/out bit, so the darts' error is one dart's spread over √N (½/√N for a yes/no question) with no d in it, unless the answer itself is tiny.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 7.5 · Motion 8 · Audio 8 · Concision 8 · Originality 8.5
WEIGHTED: 8.2 (817.5/100 = 8.175)   AFTER CEILING: 8.2 (lowest 7.5 + 2 = 9.5, does not bind)
CAPS: none.
  - Overlap (cap 7) checked. Every overlap found is mid-transform and under 0.6 s: the label double exposure "±2.6/±2.0 pts" and "±2.4/±2.4 pts" @2:39.0, the scrambled "spr"/"ead" glyphs @2:39.3, the σ→½ blob @2:49.5, and the shadow ticks crossing the dimmed "input 1" @1:49.0. In settled layouts, the closest call is the climax formula, 30 px under "100 dimensions" @2:59.5. That is above the 20 px minimum.
  - Static stretches: max 3.1 s (2:51.9–2:55.0, the planned prediction hold). Silences: max 1.96 s. Runtime 3:54.6 is inside 4:00. Every empirical claim has an on-screen citation (Glasserman @0:23–0:28, Metropolis & Ulam @0:28–0:37, Bergstra & Bengio @3:09–3:24).
FINAL: 8.2   PASS: no
FACTS:
  2^100 has 31 digits | Verified | len(str(2**100)) = 31
  1,000,000 grid points in 100-D give 1 value per axis, the centre | Verified | floor(10^(6/100)) = 1
  Quarter disc r = √(2/π) has area ½; the 10×10 midpoint grid has 52 inside, 2 points off | Verified | recomputed: 52
  100 darts give 44 inside, 6 points off | Verified (simulated, labelled) | sim.py / facts #6
  Values per axis 1000, 100, 10, 3, 1, 1; points used 10^6, 10^6, 10^6, 59,049, 1, 1 | Verified | floor(10^(6/d)); 3^10 = 59,049, 4^10 = 1,048,576 > budget
  Ball covering exactly half the box; the centre is inside at d = 20 and 100 | Verified | d/4 = 5 < r²₂₀ ≈ 6.63; 25 < 33.3
  2^19-point rescue grid at d = 20 is 18 points off | Verified | P(Bin(19, ½) ≤ 10) = 0.6762 → 17.6 points
  Darts under 0.1 points in every dimension (six simulated runs) | Verified (simulated) | facts #13, max 0.038
  Shadows: 100 grid points cast 10 values, 100 darts cast 100; N^(1/d) | Verified | algebra
  One yes/no flip misses its mean by exactly ½; spread = ½/√N; quadrupling N halves it | Verified | Bernoulli(½) SD = ½
  300-run histograms ±4.8/±4.8 → ±2.6/±2.4 points | Verified (simulated) | theory 5.0 → 2.5
  General f: σ/√N "for all d" | Verified | Glasserman 2003 §1.1.1 (quoted in facts.md)
  ½/√10^6 = 0.0005 = 0.05 points; "two in three" under 1 SD; all six of ours (p ≈ 0.10) | Verified | P(|Z| < 1) = 0.683; 0.683^6 = 0.10
  Radius-1 ball fills 2×10^-14 of the box at d = 30; drops below 10^-6 after d = 17 | Verified | V_d/2^d: 2.04e-14 at 30; 1.08e-6 at 17; 3.1e-7 at 18
  Metropolis & Ulam 1949, JASA, "The Monte Carlo Method" | Verified | JASA 44(247):335–341
  Bergstra & Bengio 2012, JMLR: random search as good as grid in a fraction of the time; 9 trials → 3 vs 9 distinct values | Verified | JMLR 13:281–305, abstract and Fig. 1 caption
  Option on 100 stocks = a 100-dimensional average | Verified | Glasserman 2003 §1.1.1
MECHANICS: runtime 3:54.6 · wpm 159 (speech) / 185 excl. pauses · max silence 1.96 s (0:10.3, planned) · max static 3.1 s (2:51.9, planned) · −14.0 LUFS / −2.1 dBTP · leading 0.00 s · trailing 1.72 s · 0 banned phrases · WER 3.5 %
FIXES (highest impact first):
1. [2:11–2:19][Clarity+Visual] The 100-D panel is a haze. 99 faint polylines plus one bold one fill a 730×480 px block (kf_21, 2:13.8), and nothing on screen shows inside or outside in 100-D, so "inside → 1" is only asserted at the exact moment the episode claims "darts never meet the dimension". Fix: drop the 99 faint polylines (or set them to 10 % opacity). Under each panel, add one gauge: a horizontal bar "distance² from corner" that grows to the dart's actual Σx² (2-D ringed dart vs r² = 0.637; 100-D bold dart vs r² = 33.3, from data.json), with a dashed INK tick at r². The bar ends short of the tick → "inside → 1", or past it → "outside → 0". Then `ReplacementTransform` each gauge into its single coin before the 10×10 coin blocks form. 100 coordinates visibly collapse to one bit, so the central claim is shown, not said.
2. [2:41–2:47][Visual] The formula-assembly frame (2:46.8) has three competing focal points: the formula, the coin number line and two red brackets. It carries about 19 words of prose ("N = 400 darts per experiment", two titles, "σ = one dart's spread", "one yes/no dart", "estimate from one experiment", two "10 runs"), against the 12-word limit. Fix: as "spread =" begins (2:38.3), dim both histograms, their brackets, the number line and the "2/100 dimensions" titles to 30 % (each source term still flashes at full opacity for ≤ 0.8 s as it flies in). Fade "estimate from one experiment" and both "10 runs" to 0. Set the formula at font_size 56, centred at (0, 2.2).
3. [2:57–3:00][Visual] The episode's answer, "spread = 0.0005 = 0.05 points", sits off-centre (centre x ≈ 1185 px against a 960 px frame centre) and only 30 px under the dimmed "100 dimensions" title (kf_29). Fix: when the histograms dim at 2:47.3, fade the header and both titles to 0. Then `formula.animate.move_to(UP*0.6).scale(1.15)` before √1,000,000 → 1000. The climax number gets the centre of an otherwise empty frame and keeps its existing flight onto the chart line.
4. [2:05–2:09, 2:45–2:47][Clarity+Motion] The grid's law N^(1/d) is fully on screen for only about 3 s (2:05.4–2:08.5) and then is gone for good, so the episode's two laws never sit side by side. Fix (visual only, no new narration): during "Any other function swaps that half for its own spread, sigma. The root N stays." (2:41.3–2:47.3), bring back "grid: N^(1/d) values per axis" (PURPLE, with YELLOW d) to the left of "darts: σ/√N". `Indicate` the yellow d on the grid side, and on the darts side draw a YELLOW "no d" strike-through under √N for 1 s. Also start the 2:08.6 grid-side FadeOut 1 s later, so N^(1/d) holds ≥ 3.5 s the first time.
5. [1:05–1:12][Visual] The square → cube → eighth-ball inset and its "d = 2/3" label are drawn inside the empty plot area of the error chart (kf_11): two unrelated graphics share one canvas, exactly where data will land. Fix: run the square → cube → ball morph centred at (0, 0.3) before the chart is drawn. Then shrink it to a 1.6-unit thumbnail at (5.0, 2.4) beside "true answer ½ in every dimension", and only then `Create` the axes. Keep the thumbnail at 40 % through 1:30, so "the centre sits inside the ball" has a picture to point at.
6. [2:38.9–2:39.6][Motion] "spread" is built from glyph copies of the "pts" labels, which reads as letter soup ("spr" … "ead" @2:39.3). At the same moment the "±4.8 → ±2.6 / ±2.4 pts" labels cross-fade into double exposures (@2:39.0). Fix: `Write("spread =")` in place, and `TransformFromCopy` only the two red bracket lines into a short red underline beneath "spread" (shape → meaning). Change the bracket numbers with `ChangeDecimalToValue` on a DecimalNumber, with "pts" as a separate static mobject, so no glyphs double-expose.
7. [2:49.2–2:49.8][Motion] The σ → ½ swap morphs through an unreadable red blob (2:49.5). Fix: use `FadeTransform(sigma, half)` (0.5 s), then a ≤ 1 s `Indicate` of the new ½, the same as the other changed-term flags.
8. [1:27–1:31][Visual] "its one point, the centre, is inside" is set on the same baseline as "error (percentage points)", 40 px apart, so the two read as one 10-word line (frame 1:29.0). Fix: place it as a 2-line PURPLE label "centre is / inside the ball" at (3.3, 2.4), right of the d = 20 column with an arrow to the d = 20 tick. Pulse the thumbnail from fix 5 (centre dot inside the ball) on "which sits inside the ball" (1:26).
9. [2:19–2:29][Visual] The single-coin derivation runs on a 230 px number line with a 115 px red bracket and ~30 px labels (frame 2:24.6), while the bottom 40 % of the frame is empty. This is the step every later term comes from. Fix: during 2:19.3–2:26.3, scale the "one yes/no dart" group ×1.8 at (0, −0.6), with the coin flip 0 → 1 → 0 and the bracket swapping sides. Shrink it back into its slot as the histogram axes are created at 2:27.
10. [3:05–3:09][Motion] The chart fades to a near-empty frame (3:06.6: faint titles and two bare baselines) before Bergstra & Bengio is drawn. This is the one remaining soft cut inside a beat. Fix: `ReplacementTransform` the chart's PURPLE grid polyline into the "grid search" title and the BLUE darts polyline into "random search", then `Create` the squares. The method colours carry across, and so does the claim "same wall".
11. [1:47–1:50][Audio] "A hundred grid points in a square cast only ten" is heard as "100 grid, points in a square" (transcript 1:47.3). The TTS breaks the phrase after "grid". Fix the narration: "The grid's hundred points cast only ten shadows." Re-run the transcript to confirm.
12. [whole][Audio] Nearly every inter-sentence gap is 0.4–0.6 s (silence list: 0:05, 0:07, 0:16, 0:20, 0:22 … 3:49). The cadence is metronomic and does not mark the beat boundaries. Fix: 0.25 s gaps inside a thought, and 0.8–1.0 s at the beat boundaries after "In two dimensions, the grid wins." (1:01.4), "...in every dimension." (1:41.9), "All six of ours did." (3:04.7) and "Off by the entire answer." (3:42.5). Absorb the time with fix 13.
13. [0:00–3:55][Concision+Hook] The episode runs 3:55 against a 3:00 template, close to the 4:00 limit, and the cold-open question ("how many values per input?") is closed at 0:12, so no open loop runs to the payoff. Fix (script level): at 0:22 add one 8-word line that plants the payoff question: "And a million random darts? Hold that thought." Answer it explicitly at 2:55 ("...five hundredths of a point; that's the darts' answer"). Pay for it, and for fix 12, by cutting about 12 s. Merge B9's narration into one clause, "Even the best two-value grid, half a million points, is 18 off" (−2 s). Cut "Two values per input would already take two to the hundredth points, thirty-one digits" to "Two values per input: a thirty-one-digit number of points" (−2 s). Drop "Machine learning hit the same wall." and let the transform from fix 10 say it (−2 s). Shorten the B18 sentence to "By thirty dimensions a radius-one ball fills two parts in a hundred trillion" (−2 s). Target ≤ 3:40.
REACHES 9 IF ALL FIXED: yes, narrowly, and only with all of 1–4 and 13. Execution fixes 1–12 alone lift Visual and Motion to about 8.5–9 and Clarity to 9, which gives a weighted score of about 8.7–8.8. The last step needs the script-level change in fix 13 (an open loop from the cold open to the 2:55 answer, and a runtime ≤ 3:40) to move Hook and Concision to 9. Nothing structural is missing: hook, naive build, measured failure, visual insight, sourced payoff, honest limit and callback landing are all present and correct.
KEEP:
- The 100-axis parallel-coordinates cold open: grid = one PURPLE centre line, a random point = one BLUE polyline that collapses into the 2-D dart, and the landing that floods every axis BLUE (3:45–3:53).
- The coins → 300-run histograms with identical 2-D and 100-D spreads, then the ×4 darts → both halve (2:27–2:41). This is the episode's proof by animation.
- The shadow device (1:45–1:53) carried into Bergstra & Bengio's 3-vs-9 shadows on the score curve (3:17–3:24), so the payoff is the same picture.
```

## Round-1 fixes: status

| R1 fix | Status in this cut |
|---|---|
| 1 formula derived from referents | Done: the ½ comes from the coin's bracket, √ from the shrink replay, N from the header (2:38–2:42). The execution leaves glyph soup (new fix 6). |
| 2 mislabelled N = 1,000,000 header | Fixed: the header stays "N = 400" and dims; 1,000,000 appears only inside the formula (2:49). |
| 3 answer hold + no global dissolve | Mostly fixed: the answer is held ~3 s and "0.05 points" flies to the chart (3:00). Placement is off-centre (new fix 3). |
| 4 TransformMatchingTex fallbacks | √1,000,000 → 1000 is clean. σ ↔ ½ still blobs (new fix 7). |
| 5 eighth-ball inset | Geometry now correct (kf_11). Placement over the plot area (new fix 5). |
| 6 counters | Fixed: Integer ticks 0 → 52 / 0 → 44, with no glyph swarm (0:51–0:59). |
| 7 units | Fixed: points everywhere. |
| 8 1 SD as ceiling | Fixed: "typical miss", "two runs in three". |
| 9 stakes | Fixed: option on 100 stocks + Glasserman citation (0:23–0:28). |
| 10 "103" | Fixed: "a hundred per axis in three" is transcribed correctly. |
| 11 chart → squares | Fixed: the dots grow into the squares (1:43–1:45). |
| 12 truth line through counts | Fixed (2:29). |
| 13 ticks through "input 1" | Label dimmed during the drop (1:49.0); acceptable. |
| 14 cold-open centring | Fixed (kf_01). |
| 15 B&B label | Fixed: "model score (schematic)" sits beside the left curve (3:19). |

## Sync notes (word timings vs frames)
- "like this one" (0:35.3): the BLUE polyline is still drawing (0:29–0:37). Lands.
- "this quarter disk" (0:41.5–0:42.5): the arc and fill are complete by 0:43. Lands (within 1 s).
- "the grid wins" (1:00.5): the box around 52/100 appears at 1:01. Lands.
- "a thousand … three in ten" (1:13–1:20): each row value appears on its word, and the YELLOW marker steps. Lands.
- "Look at the shadows" (1:44.4) → the rail appears at 1:45; "cast only ten" (1:49) → PURPLE ticks have landed by 1:51; "a hundred darts cast a hundred" (1:51) → BLUE ticks at 1:53. Lands.
- "spread this wide" (2:32.5) → the ±4.8 bracket is visible at 2:33. Lands.
- "That half over the square root of N" (2:38.3–2:41.3) → the formula is complete at 2:41.8. Lands at the edge, about 0.5 s late.
- "Below this line" (3:34.3) → the dashed 1/N line is in at 3:35. Lands.
- No spoken reference names something that is not visible within ±2 s.
