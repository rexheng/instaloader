# Episode 5 changelog

## Round 1 revisions

Round-1 critics: craft 7.9, substance 8.1 (no caps, no factual errors). Every fix from both reviews was
applied; the three "keep" items (100-axis cold open and blue-flood landing, the coins -> identical
2-D/100-D histograms, the shadow device reused for Bergstra & Bengio) are unchanged in substance.

**Central formula derived, not written (craft 1, 4; substance 9).**
- New beat B13: a copy of one coin moves onto a 0–1 number line ("one yes/no dart"), flips 0 -> 1, and a
  RED "½" bracket to the dashed average ½ shows that every flip misses its average by exactly a half.
- In B14 every term of `spread = (1/2)/√N` arrives from its referent: "spread" from the bracket labels,
  the ½ from the coin's bracket, the √ while copies of the wide brackets replay their shrink, and N from
  the "N = 400" header.
- All formula morphs use isolated tokens (`\frac{1/2}{`, `\sqrt{`, `N`, `}}`) and an explicit part-to-part
  morph, so only the changed term moves (N -> 1,000,000 -> 1000; fraction -> 0.0005; "= 0.05 points" appended).
- The shadows formula is built from the picture ("A hundred points over two axes: ten per axis, the
  square root of a hundred"): the 100 grid dots fly into "100", the square's two axes into the
  exponent's "2"; "100^(1/2) = 10 values" holds ~4 s, then 100 -> N and 2 -> d with "= 10" removed first.

**Mislabelled frame and the answer's hold (craft 2, 3; substance 2).** The "N = 400 darts per experiment"
header now stays and dims with its histograms; 1,000,000 appears only inside the formula. The answer
`spread = 0.0005 = 0.05 points` stays on screen about 4 s; then its "0.05 points" flies onto the dashed
chart line as that line's label while the chart returns with its labels (no whole-scene dissolve).

**Honest statistics (craft 8; substance 1, 4, 7, and the "unstated assumption" note).**
- B9: "The darts stay under a tenth of a point in every dimension" (2 SD; true for all six runs).
- B16: "Two runs in three land under that typical miss; all six of ours did." The line is labelled
  "typical miss".
- B15 (new): "Any other function swaps that half for its own spread, sigma. The root N stays." (½ -> σ,
  "σ = one dart's spread"; Glasserman 2003 §1.1.1.) B16 then asks about "a million yes-or-no darts".
- B18: "...so they usually report zero: off by the entire answer" ("darts report 0: 100% off").
- B19 closing line: "The darts never noticed the axes: a million coin flips, in any dimension."

**Budget fairness (substance 3).** A GRAY "points used" row (10^6, 10^6, 10^6, 59,049, 1, 1) under
"values per axis", and a new beat B9: the fairest two-value grid at d = 20 (2^19 = 524,288 points) still
lands 17.6 points off (hollow PURPLE dot that drops from 50; exact count in `sim.py` "rescue20").

**Stakes and encoding (craft 9; substance 5, 6).** B2 now opens on a concrete use: "Pricing an option on
a hundred stocks is exactly this kind of average", with "e.g. an option on 100 stocks" and the citation
"Glasserman, 2003 · Monte Carlo Methods in Financial Engineering" (≈4.5 s), then Metropolis & Ulam.
The cold open adds "each line: one input, from 0 to 1" while axis 1 flashes, and the random point is
labelled "a random point: one value per input".

**Units (craft 7; substance 10).** Percentage points everywhere: "off by 2 points", "off by 6 points",
histogram axes in %, brackets "±4.8 pts" -> "±2.6 / ±2.4 pts", "0.05 points".

**Visual and motion fixes.**
- Eighth-of-a-ball inset rebuilt in 3-D (craft 5; substance 12): the quarter-disc square becomes the cube's
  back face and the exact r = 0.985 octant (convex hull of the projected solid, faint fill) bulges toward
  the viewer; nothing pokes outside the cube.
- Counters (craft 6; substance 8): inside dots fill one by one while an Integer ticks 0 -> 52 / 0 -> 44;
  no glyph copies.
- Chart -> squares (craft 11; substance 16): the chart's d = 2 dots grow into the two squares (no empty frame).
  Going the other way, the two squares shrink into the chart's d = 2 column before the chart is drawn.
  The other scene changes (chart -> Bergstra & Bengio -> limit chart -> landing) use a 0.4 s fade followed
  by the next picture being drawn: no whole-scene cross-dissolves, no near-empty frame.
- While "Spread N grid points evenly over d axes, and each axis gets..." is spoken, the 100, the 2 and the
  "10 values" flash with the grid dots, the two axes and the 10 shadow ticks they stand for (no static stretch).
- Falling shadow ticks: "input 1" and the 0/1 ticks dim to 25 % during the drop (craft 13).
- Truth lines are created after the coin blocks become bars (craft 12); "10 runs" scale bar on each
  histogram (substance 13); the 2-D spread bracket grows on "spread".
- Cold open recentred (axes x -5.05..4.35) (craft 14).
- Bergstra & Bengio panel: "model score (schematic)" attached left of the left curve, titles lowered,
  curves shortened (craft 15; substance 15).
- "a hundred per axis in three" (craft 10; substance 14) to stop "hundred in" being heard as "103".
- Cut "A million points over twenty axes: fewer than two" and its label (substance 11).

Narrator speed 0.84 -> 0.86 to absorb the added content (runtime ~3:55, inside the 4:00 limit).

## Round 2 revisions

Round-2 critics: craft 8.2, substance 8.1 (no caps, no factual errors; all 25 claims re-verified by both).
Every fix from both reviews was applied. The keep items are intact: the 100-axis cold open with "One." and the
blue-flood landing; the fixed-budget climb with "points used" and the 2^19 rescue; the coins -> identical 2-D/100-D
histograms that both halve under N -> 4N; the shadow device carried into Bergstra & Bengio.

**Plan of the climb (BAR §3 "9" anchors vs this cut).**
- Clarity (8 -> 9, "assumptions stated; viewer could re-derive it"): the mechanism was never said and "more
  shadows" was a competing explanation. Now: a diagonal beat shows a million values per axis still 7.7 points off,
  then "each one lands inside with a chance equal to the answer, on its own", with gauges that show one dart's 2 or
  100 coordinates collapsing to one bit; "Back to our ball" makes ½/√N exact for p = ½.
- Visual (7.5 -> 9, "one focal point per frame"): no 99-polyline haze; the climax formula is alone and centred;
  the formula frame keeps context at 30 % with ≤ 12 prose words; the cube inset no longer shares the chart.
- Motion (8 -> 9, "every motion encodes a relation"): no glyph soup (DecimalNumber brackets, Write("spread ="),
  FadeTransform for σ <-> ½, d = 2 -> 3, √1,000,000 -> 1000); chart curves morph into the B&B method titles; the
  one-coin derivation is shown 1.8x; both laws side by side.
- Audio (8 -> 9, "pauses are intentional"): ~0.25 s inside a thought, ~0.75 s at the six beat boundaries.
- Hook/Concision (8–8.5 -> 9): an open loop ("How far off would a million of them land? Hold that thought.")
  answered by the 2:45 prediction, where the same BLUE "?" returns as "= ?" and turns into "0.05 points";
  runtime 3:55 -> 3:42 despite the added diagonal beat.

**Narration (script.md).** New open loop in B2; "Since Metropolis and Ulam's 1949 paper, such averages use random
points"; the 2^100 line shortened; the climb's per-axis line shortened ("then a hundred, ten, three"); B8 "From
twenty dimensions on, just one"; B9 one clause ("the largest two-value grid that fits" — "best" would overclaim);
"The grid's hundred points cast only ten shadows" (the TTS no longer breaks "grid, points"); new diagonal beat; new
mechanism sentence; "The root N stays, and there's no d in it"; "Back to our ball, ..." (exact for p = ½);
"Two runs in three land closer"; "Machine learning hit the same wall" dropped; landing recap sentence dropped.
Explicit pauses: [pause 0.15–0.25] between sentences, BEAT_GAP 0.1, gap 0.6 (+ tail ≈ 0.75 s) at boundaries.

**Scene (scene.py), by critic fix.**
- Craft 1 / substance 1, 5: the 100-D panel shows only the bold cold-open dart. Under each panel a gauge: readout
  "x1² + x2² = 1.20 > 0.64" / "x1² + ... + x100² = 31.8 < 33.3" (live DecimalNumber), a BLUE bar growing against a
  dashed INK tick at r², then "outside -> 0" / "inside -> 1"; everything but the two verdicts steps away and each
  verdict becomes its dart's single coin before the other 99 coins arrive.
- Substance 2: new beat on the 100-axis panel: 26 PURPLE flat lines sweep up ("10^6 points on the diagonal"),
  every axis flashes, a dashed INK level at t = 0.577 and the lines above it fade: "57.7% inside: 7.7 points off".
- Craft 2, 3 / substance 3: from "spread =" the histograms, brackets, coin line and titles fade to 30 %, "estimate
  from one experiment" and "10 runs" to 0; formula size 56 at (0, 2.2). On "Back to our ball" everything else leaves
  and the formula moves to (0, 0.6) at 1.15x; the answer "spread = 0.0005 = 0.05 points" is centred alone.
- Craft 4: during B16 the grid's law returns at the left ("grid: N^(1/d) values per axis", YELLOW d indicated)
  beside "darts: spread = σ/√N", with "no d" under √N; held about 3 s. The first N^(1/d) holds ~4 s.
- Craft 5 / substance 12: square -> cube -> eighth-ball runs centred on an empty frame, then shrinks to a 40 %
  thumbnail in the top-right corner beside "true answer ½ in every dimension"; only then are the axes drawn.
- Craft 6 / substance 6: "spread =" is written in place while copies of the two bracket lines fly into a RED
  underline beneath it; bracket labels are ± DecimalNumber + static "pts" driven by trackers; d = 2 -> 3 by
  FadeTransform.
- Craft 7: σ <-> ½ by FadeTransform (≈0.5 s) then a ≤ 1 s flag.
- Craft 8: two-line PURPLE "centre is / inside the ball" with an arrow to the d = 20 column; a PURPLE dot appears at
  the cube's centre in the thumbnail and pulses on "inside the ball"; the note leaves before the line is drawn and
  "grid says 1.000" fades in after (no text cross-fade).
- Craft 9: the one-coin number line is shown 1.8x at (0, −0.6) and shrinks back into its slot as the histogram
  axes are drawn. Word load on the histogram frame cut from ~21 to ~13: the header is "N = 100 darts", the
  "one yes/no dart" caption leaves once the coin line is back in its slot, and only one "10 runs" scale label.
- Craft 10: the chart's PURPLE grid curve morphs into "grid search", the BLUE darts curve into "random search".
  B&B -> limit chart and limit -> landing are 0.35 s fades at beat boundaries followed at once by the next chart.
- Substance 4: the RED zone is shaded only from the crossing (d = 17.06); y axis extended to 10^-18 so the label
  "darts report 0: / off by the whole answer" sits inside the zone under the curve's tail.
- Substance 11: B&B random trials from seed 119736: on-screen x-values ≥ 0.06 apart (nine distinct shadows) and
  uncorrelated with y, so the nine points also look random (an earlier candidate seed lined them up).
- Substance 8: "Glasserman, 2003 · Monte Carlo Methods in Financial Engineering, Springer".
- Layout: every formula stage is removed part by part after its morph (no leftover glyphs); tick labels, readouts,
  "10 runs", "grid says", "2 × 10^-14" and the coin-line caption moved to ≥ 0.15 clearance. Formula parts typeset by
  LaTeX itself are declared with allow_overlap (reason recorded).

**Data (sim.py -> data.json).** New "diag100" (estimate 0.577075, 7.7 points off) and "dart2d_sum_sq" (1.196); B&B
seed 119736. Every other value is unchanged (sim.py is deterministic).

## Round 3 revisions

Round-3 critics: craft 8.4, substance 8.5 (no caps, no factual errors; every number and all three citations
re-verified, the million-dart simulation re-run exactly). Every fix from both reviews was applied; the keep items are
intact (100-axis cold open and blue-flood landing; the fixed-budget climb with "points used", the 2^19 rescue and the
diagonal counterexample; the gauges collapsing one dart's coordinates to one bit, feeding identical 2-D/100-D
histograms; the shadow device carried into Bergstra & Bengio).

**Plan of the climb (BAR §3 "9" anchors vs the round-3 cut).**
- Clarity 8.5 -> 9 ("viewer could re-derive it after one watch"): √N was measured, never explained; the diagonal
  beat needed a rewatch; the closing comparison set a count against an error. Now: a random walk of sixteen real ±½
  misses (net 4 halves = √16, vs 16 if they never cancelled) derives ½/√N on screen; the diagonal shows one flat line
  labelled "one point: (t, t, …, t)" before the sweep and labels the dashed level "ball's edge" (solid = inside,
  dashed = outside); the grid's side is now its error law, N^(−2/d) for smooth f (Glasserman §1.1), set under the
  darts' σ/√N, its d copied from the darts' "no d".
- Visual 8–8.5 -> 9 ("every frame has one focal point"): the formula no longer shares a band with dimmed titles (the
  histograms and titles leave before it is built); caption "one yes/no dart" at Text 28, no longer the largest text;
  the coin line beside the histograms at 0.75x (labels ≥ 24 px); one label "typical miss: 0.05 points" above its own
  line; one type size on "centre is / inside the ball"; "2 values on 19 axes".
- Motion 8.5 -> 9 ("every motion encodes a relation"): the thumbnail's centre dot itself flies onto the chart as the
  grid's 50-point estimate; d = 3 lands with the depth edges, the outline inflates and the fill follows; the square's
  outline becomes the coin block's frame and the other 99 100-D darts fan in as polylines and collapse into their
  coins; the search squares' axes become the limit chart's axes; the limit's 1/N line becomes the cold-open header
  and its x-axis the floor the 100 axes grow from. Equation pacing: ½/√N holds ~4 s (its ½ is flagged on "half" and
  becomes σ only on the word "sigma"), a 0.6 s pause after σ, the grid law in its own sentence ~4 s after the σ swap,
  and the 0.05-point answer lands on "five hundredths" and holds ~3.4 s before it flies to the chart, where the
  grid's annotations return at 40 % so the darts and their dashed line are the focus.
- Hook/Audio 8.5 -> 9: the wrong belief is voiced ("Spread them out as an even grid; that feels thorough.");
  "So, back to our ball" (the bare "Back" was dropped by the transcriber); 2^100 written on "two to the hundredth"
  and held ~2 s.
- Concision 8 -> 9: the shadow beat's third telling of values-per-axis cut (four sentences -> one); "A hundred axes,
  a million points." cut from the landing (the header says it).

**Narration (script.md).** B0 adds "that feels thorough"; B1 ends with [pause 0.8]; B2 "are usually done with random
points" (substance 6: quasi-random points exist, Paskov & Traub 1995); B9 "Even two values on nineteen of the axes";
B10–B11 shortened to "Look at the shadows on one axis: the grid's hundred points cast ten, a hundred darts cast a
hundred. With N points over d axes, each axis gets the d-th root of N."; B12 adds "each one a flat line here" and
[pause 0.6]; B15 ends at "twice as narrow"; new B15b (the walk, ending "per dart, that's a half over the square root of
N" + [pause 0.8]); B16 adds [pause 0.6] and "A grid's error, even for smooth functions, has d in its exponent."; B17
"So, back to our ball", [pause 0.8] before "Two runs in three"; B20 "The darts never noticed the axes: a million coin
flips, in any dimension."

**Facts (facts.md).** New #19a (the walk: darts 62–77 of the 2-D run, 10 in / 6 out, net +4 halves; SD of N ±½
misses = ½√N; per dart ½/√N) and #20a (Glasserman §1.1.1 quote for O(n^(−2/d)); midpoint rule same order; slower
than N^(−1/2) for d > 4, matching the chart's crossover between d = 3 and 6). #12 and #26 reworded; a round-3
resolutions section explains why the cell-width variant of the laws was not used (1/N^(1/d) = 0.50 at d = 20 while
the integer grid's cell is the whole box).
