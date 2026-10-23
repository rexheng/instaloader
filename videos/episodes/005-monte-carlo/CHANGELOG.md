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
N" + [pause 0.8]); B16 adds [pause 0.6], "The root N remains" (the transcriber heard "root N stays" as "root end stays") and "A grid's error, even for smooth functions, has d in its exponent."; B17
"So, back to our ball", [pause 0.8] before "Two runs in three"; B20 "The darts never noticed the axes: a million coin
flips, in any dimension."

**Facts (facts.md).** New #19a (the walk: darts 62–77 of the 2-D run, 10 in / 6 out, net +4 halves; SD of N ±½
misses = ½√N; per dart ½/√N) and #20a (Glasserman §1.1.1 quote for O(n^(−2/d)); midpoint rule same order; slower
than N^(−1/2) for d > 4, matching the chart's crossover between d = 3 and 6). #12 and #26 reworded; a round-3
resolutions section explains why the cell-width variant of the laws was not used (1/N^(1/d) = 0.50 at d = 20 while
the integer grid's cell is the whole box).

## Round 5 revisions

Round-5 critics (files round5-craft.md / round5-substance.md, which review the 01:25 cut): craft 8.2, substance 8.5,
no caps, no factual errors (every number and all three citations re-verified by both). Both said "reaches 9 narrowly".

**Plan of the climb (BAR §3 "9" anchors vs the round-5 cut), written before editing.**
- Hook 8.5 -> 9 ("viewer commits to a likely-wrong prediction by 0:12; ... the ending re-sees the first frame"): the
  first 5 s were 100 static grey axes and an abstract "average a function"; the stake arrived at 0:22. Upgrade: the
  axes sweep in left to right while a YELLOW "d = 1 -> 100" counter counts them, and the first sentence carries the
  stake ("to price an option on a hundred stocks, an average over a hundred inputs", Glasserman on screen from 0:02).
- Clarity 8-8.5 -> 9 ("viewer could re-derive it after one watch; assumptions stated"): (a) the ball's radius grew
  silently (0.80 -> 5.77) and collided with the radius-one limit beat; now said ("grown just enough"), shown (a GRAY
  "ball radius" row, the gauges' "= 0.80²" / "= 5.77²") and cashed in ("Keep the radius at one instead");
  (b) the diagonal's cause was unnamed; now "all hundred coordinates move in lockstep", shown by one flat line sliding
  as a whole, and contrasted with the dart ("A dart's coordinates are drawn independently"); (c) √N halves -> ½/√N
  skipped the divide-by-N; now an explicit chain (√N·½)/N -> ½/√N with the cancelled √N flagged; (d) the two laws were
  never cashed in; now "The exponents tie at four dimensions, near where our lines crossed", with N^(−2/d) = N^(−1/2)
  at d = 4 and a YELLOW d = 4 marker on the returning chart; (e) one name, "typical miss", for the estimate's spread
  (formula, chart axis "miss", dashed line).
- Visual 8-8.5 -> 9 ("one focal point per frame"): the 26 s formula-only stretch is replaced by laws above a compact
  copy of the dimension chart, and the 0.05-point answer drops from the formula onto the chart's dashed line; the
  histograms no longer share their row with the coin line (it waits at 30 % above them); the random walk is ~1.4x
  larger with thicker steps.
- Motion 8-8.5 -> 9 ("every motion encodes a relation"): no glyph-scramble (the chart's grid dots become the 3x3
  grid-search dots and its dart dots the nine random trials); no false axis morph into the limit chart (the
  Bergstra & Bengio panel fades out completely before the new axes are drawn); nothing slides through fading labels.
- Audio 8.5 -> 9: the chart -> squares unfold now happens before "Look at the shadows", so the shadows drop on the
  word; "16 halves / if they never cancelled" holds through a 0.6 s pause.
- Concision 7.5-8 -> 9: cut "Pricing an option ... is this kind of average", "Hold that thought", "in every dimension",
  "just as wide" (merged), "Two runs in three land closer; all six of ours did" (the six dots under the dashed line
  show it); added sentences each carry a new step (radius, lockstep, divide by N, the d = 4 tie).

**What changed, by critic fix.**
- Craft 12 / substance 2 (hook, stakes): first sentence "A million evaluations to price an option on a hundred
  stocks: an average over a hundred inputs. An even grid feels thorough." The 100 axes sweep in left to right while a
  YELLOW counter "d = 1 -> 100" counts them (lands on "a hundred stocks"); "e.g. an option on 100 stocks" + Glasserman
  from 0:02; the separate stakes sentence is gone. The question still ends at 0:11.3 with a 1.5 s hold.
- Substance 6: "Since Metropolis and Ulam's 1949 paper, the standard tool has been random points" with Glasserman and
  M&U stacked bottom-left (≈5 s). Craft 4 / substance 4: "Hold that thought" cut.
- Substance 1: "a ball, grown just enough to cover exactly half the box" with "ball radius 0.80 -> 0.98" ticking beside
  the cube; GRAY "ball radius" row (0.80 ... 5.77) under the chart; gauges "> 0.64 = 0.80²" and "< 33.3 = 5.77²";
  limit beat "Fix the radius at one, and by thirty dimensions the ball fills ...".
- Substance 4/5, craft 4: B8 "just the centre" (no "just one:"), B9 "two values on nineteen axes", "The darts stay
  under a tenth of a point" (no "in every dimension").
- Craft 9: the chart -> squares unfold runs before "Look at the shadows", so the rails and shadows land on the word.
- Craft 3: "...and still miss by eight points: their coordinates move in lockstep" while the one flat line slides up
  and back as a whole; B13 opens "A dart's coordinates are drawn independently", with the diagonal's flat line kept at
  30 % and flashed against the dart's jagged polyline.
- Craft 5: during the histograms the coin line waits at 30 % above them (one focal point); histograms 10 % wider;
  "In two dimensions or a hundred, the estimates spread this wide" grows both brackets together.
- Craft 6, 10, 1: walk ≈1.4x larger (0.42 x 0.21 steps, 6 px arrows), coin line full size lower right; "16 halves /
  if they never cancelled" holds through a 0.6 s pause; the explicit chain "typical miss = (√N · ½)/N" (√N from the
  walk's label, ½ from the coin's bracket, N from "N halves") -> "½/√N" with the numerator's √N dropping into the N,
  narrated "N darts stray about root N halves. Divide by the N darts: a half over root N."
- Craft 2, 11 / substance 3, 8, 10: the walk dims to 30 % (no slide through fading labels); the darts' law sits top
  left ("random darts"), σ-swap, "no d"; the grid's law top right ("grid, smooth f: miss ∝ N^(−2/d)", Glasserman
  §1.1); "The exponents tie at four dimensions, near where our lines crossed": copies of N^(−2/d) and √N build
  "N^(−2/d) = N^(−1/2) at d = 4" while a compact copy of the dimension chart is drawn beneath, and a YELLOW dashed
  d = 4 marker rises where the lines cross (segments cross at d ≈ 4.6). The prediction is computed above that chart and
  "0.05 points" drops onto its new dashed "typical miss" line; the six dart dots (all under it) flash. "Two runs in
  three ..." cut. One name throughout: "typical miss" (formula, dashed line), "miss" (grid law, chart axis).
- Craft 7 / substance 7: no curve-to-word morph; the chart fades while its grid dots become the nine grid trials and
  its dart dots the nine random trials; the squares are drawn after the fade; "random search" / "grid search" are
  written on those words.
- Craft 8 / substance 9: the Bergstra & Bengio panel fades out completely (0.5 s) before the limit chart's axes are
  drawn; no axis morph.
- Narrator 0.86 -> 0.87, boundary pause 0.6 -> 0.5 s: runtime 3:57 -> about 3:51.

### Round 5 revisions, render pass (after the interrupted attempt)

The interrupted attempt rendered the round-5 cut once (09:33: 3:55.0, 166 wpm FLAG, one sync warning at 0:42) and
then edited scene.py without re-rendering. This pass audits that render as a fresh critic would (all 14 sheets,
keyframes, and 4-8 fps strips across every transition), plans the remaining climb, applies it, and re-renders.

**Plan (BAR §3 "9" anchors vs the 09:33 render), written before editing.**
- Audio ("natural cadence at 140-165 wpm; each deictic lands"): 166 wpm over speech time, a 0.32 s late cue on "two"
  (0:42). -> narrator 0.87 -> 0.86 (~164 wpm, runtime stays under 4:00); grid counter lands before "two".
- Motion ("every motion encodes a relation; reading time respected"): frames pulled during motion still show
  (a) the square's four edges flipping through bow-tie shapes on their way to the cube's back face, with "true
  answer" crossing them (0:54.5-0:55.5); (b) the 2-D squares growing over the still-visible chart (1:27.4) and the
  darts square sliding over the fading grid square (1:41.5); (c) 99 faint polylines collapsing into one bright blob
  (2:03.5-2:04.5); (d) the coin line crossing the fading histogram (2:24); (e) "0.05 points" scrambling glyph by
  glyph on its way to the chart (3:11.8), after the full answer was legible for only ~1 s; (f) the dots flying across
  the fading chart (3:13.5); (g) the 1/N line melting into the header through glyph soup over the fading limit chart
  (3:47.8); (h) the whole 100-point polyline squashing into the 2-D dart (0:32). -> each becomes a staggered or
  one-to-one move: edge-to-edge lines for the cube face, the truth row moving first; fades finish before the next
  picture grows; FadeTransform for the 99 darts -> coins; the answer holds ~1.9 s, then flies as one rigid object
  (scale + move, same glyphs); the limit chart clears before its 1/N line becomes the header; only the two dots on
  inputs 1 and 2 merge into the 2-D dart.
- Visual ("one focal point; >= 0.15 clearance, nothing reads as clutter"): the walk's "sqrt(N) halves" sat 0.5 units
  from the coin line's red "1/2", reading as "sqrt(N) halves 1/2" (2:31-2:43). -> coin line moved right, walk steps
  0.42 -> 0.40 wide (gap ~1.1 units).
- Clarity: "Their estimate is a share of heads" had an ambiguous antecedent (coordinates or darts). -> "So each dart
  is a coin flip; the estimate is the share of heads in N flips", with the first coins appearing on "coin flip".

### Round 5 revisions, pass 3 (audit of the 14:47 restructured master)

The second interrupted pass restructured the cut to 483 words / 3:30.5 (shaped cadence, speed 0.83: the
shadows-on-one-axis formula, the quadrupled-dart histograms and the grid's N^(-2/d) law with its d = 4 tie were cut
to meet the guide's 500-word / 3:35 budget) and rendered it at 14:47 without reviewing it. This pass ran review_kit
on that master, read all 12 sheets and the keyframes, and pulled 4-5 fps strips across every transition.

**Plan (BAR §3 "9" anchors vs the 14:47 master), written before editing.**
- Visual / Motion ("every frame has one focal point; every motion encodes a relation; nothing reads as an
  artefact"): (a) 1:54.2-1:55.3, the bold 100-D polyline morphs into a blob and the 99 faint polylines
  FadeTransform into their coins through one giant filled blue ellipse (a render artefact, cap 5 territory);
  (b) 0:44.3-44.9, the square's copy doubles its labels ("iinput 2") while "true answer 1/2" slides through the
  moving square; (c) 0:56.6-57.8, the truth row crosses the fading squares and two squares are visible as the
  disc square travels to the cube's back face; (d) 2:47.4, the "0.05 points" copy starts on top of the original
  (double exposure); (e) 2:55-2:57.6, "grid search" is written stroke-first for 2.5 s (white glyph outlines);
  (f) 3:22.8, the cold-open header flashes over the limit chart's title and the 1/N line then FadeTransforms into
  the header through a stretched ghost; (g) 3:07.0-3:07.5 and 2:10.6-2:11.3, near-empty frames between beats.
  -> (a) each polyline shrinks rigidly into its coin as the coin grows (no FadeTransform between unlike shapes);
  (b, c) sequenced moves: the truth steps aside before squares move, the copy carries only lines and disc,
  originals leave the frame before their copies travel; (d) the copy fades in as it flies; (e) titles fade up in
  0.6 s; (f) the chart clears first, then the dashed 1/N line rises and shrinks into a rule under the header
  position and the header fades in on it; (g) the next picture starts while the old one fades.
- Audio / sync ("each deictic lands as the element highlights"): the "1" lands 0.9 s after "One" (0:14.3-15.2);
  "eighteen" is reached 0.48 s late (render warning); "100 values on one axis" is legible for only ~0.8 s
  (1:33.4-34.2); one sentence at 201 wpm ("So the grid says that the ball fills the box: fifty points off").
  -> the "?" -> "1" swap takes 0.6 s from the word; the rescue dot drops during "axes is"; the shadow drop starts
  on "Maybe" so the label holds ~2 s; the sentence is split ("...fills the box. Fifty points off.").
- Clarity ("assumptions stated; all numbers check out"): "A dart's coordinates are drawn independently, so it
  lands inside with a chance equal to the answer" omits that they are uniform (independence alone does not give
  P(inside) = volume) -> "drawn independently and uniformly"; the limit beat's "A radius-one ball" sits beside
  a ball whose radius grew to 5.77 -> "Keep the ball's radius at one, and in thirty dimensions it fills two parts
  in a hundred trillion of the box."
- Visual focal point during the rescue (1:21-1:30: chart, three table rows, two annotation stacks): the "points
  used" and "ball radius" rows dim to 35 % while the rescue dot is the subject.

**What changed in pass 3 (scene.py, script.md, facts.md).**
- Coin collapse (1:54-1:57): the bold 100-D dart's polyline now shrinks rigidly (same shape, 4 % size) onto its
  coin while the coin grows; each of the 99 faint polylines does the same into its own coin (LaggedStart). No
  FadeTransform between a polyline and a dot, so no blob and no filled ellipse. The verdict texts fade toward their
  coins; a [pause 0.6] lets both blocks settle before "One flip".
- 2-D build (0:44): "true answer 1/2" fades up and out, the square slides right while a copy of only its lines and
  disc slides left, then labels, the grid title and the true answer fade in with the grid dots (no doubled labels,
  nothing crossing a moving square).
- Square -> cube (0:56): contents fade first (0.4 s), then the true-answer row assembles below, then the disc
  square leaves the frame as its copy travels to the cube's back face (one square on screen at a time).
- Cold open: the "?" -> "1" swap takes 0.55 s from "One" (the 1 is legible at 0:14.8, was 0:15.3).
- Rescue (1:21): the dot appears by "nineteen" and drops during "axes is" (fixes the 0.48 s "eighteen" warning);
  the "points used" and "ball radius" rows dim to 35 % so the rescue dot is the focal point; table rows re-spaced
  (0.46 apart) to clear the 0.15 audit.
- Misconception picture (1:31): rail on "darts", shadows drop by "by", "100 values on one axis" is fully legible
  ~1.6 s and then dims to 25 % with its square (context) instead of vanishing.
- Answer (2:48): the flag grows "0.05 points" rightward only (no longer touches "="); the copy that labels the
  dashed line starts transparent and becomes opaque in flight (no double exposure).
- Bergstra & Bengio titles fade up in 0.6 s (no stroke-first Write); the limit chart's axes start as the panel's
  last 15 % fades (no empty frame, no mixed frame).
- Landing: the limit chart clears, its dashed 1/N line rises and shrinks rigidly into a rule under the header's
  place, and "N = 1,000,000 points" settles on it (no FadeTransform ghost, no header flash over the chart title);
  transition 1.05 s, longest internal silence 2.06 s (was 2.34 s in the first pass-3 render).
- Narration (490 words, 3:33.6): "drawn independently and uniformly" (facts #16); "So the grid's estimate is the
  whole box. Fifty points off." (the 201-229 wpm sentence is gone: 0 sentences above 200 wpm); "Keep the ball's
  radius at one, and in thirty dimensions it fills two parts in a hundred trillion of the box." (facts #23; the
  fixed radius contrasts with the half-volume ball's 0.80 -> 5.77), with the chart title flashing on "radius at
  one", the d = 30 dot on "thirty" and "2 x 10^-14" on "two parts in a hundred trillion".

**Verification (final master, 23:30; 0 [sample_space] warnings after the second pass-3 render's 0.34 s "win"
sync warning was fixed).** review_kit: 0 flags; 3:33.6, 149 wpm over speech, -14.0 LUFS / -2.0 dBTP, longest silence
2.06 s, longest static 2.97 s, WER 2.5 %, 0 banned phrases, 0 glyph morphs, 5/5 deictics landed, layout audit 0
issues (6 producer-allowed LaTeX-internal spacings). Frames were checked at 4-6 fps across every transition listed
in the plan above (0:14, 0:44, 0:56, 1:21, 1:31, 1:54-1:58, 2:10, 2:47-2:50, 2:54-2:58, 3:08, 3:24-3:28).

## Round 6 revisions

Both round-6 critics scored 8.6 (no caps, no factual errors) and listed 11 + 8 fixes; both said "reaches 9 if fixed:
yes", narrowly. Everything below was applied; where a fix was improved on, the reason is given.

**Plan (BAR §3 "9" anchors vs the round-6 master), written before editing.**
- Clarity ("the viewer could re-derive it after one watch"): the √N law rested on one 16-step window (darts 62-77)
  that happened to land exactly on +4 halves, and "partly cancel" explains *less than N*, not √N. -> all twelve
  consecutive 16-dart groups of the two runs as walks from one start (RMS stray 3.96 halves vs √16 = 4), a ±4 band,
  and the reason drawn: each miss's half-by-half square; sixteen of them tile one square four halves wide ("what adds
  is their squares"). The Bergstra-Bengio payoff re-used the per-axis argument the diagonal had refuted -> "Only a
  few settings really matter. With one, the search is one-dimensional: ..." (the paper's own finding, re-read on
  jmlr.org) with the important axis flashed. The limit switched from absolute to relative error silently -> "a tiny
  miss, but the whole answer".
- Motion ("every motion encodes a relation; reading time respected"): the ±4.8 brackets were legible ~0.5 s, and the
  later "measured 4.8" was a fresh Write -> brackets grow during "spread this wide", hold ~2 s (flagged side by side),
  then both labels fly into one parked "measured: ±4.8 pts" tag, the same object that returns beside the check.
  Disc-to-ball showed two concentric arcs -> one parametrised family (flat disc at s = 0 bulges into the eighth
  ball), so only one boundary exists at any moment; "d = 2" -> "d = 3" is a swap (was a cross-fade). The returning
  chart drew its lines before its axes -> frame first (0.6 s), lines after.
- Visual ("one focal point; ≤ 12 words"): the d = 20-100 corner carried ~20 words -> "grid says 1.000" leaves, the
  stack is two lines, the 524,288 cost swaps into the table's d = 20 "points used" cell, the table dims to 30 %. The
  BLUE line was drawn unlabelled 18 s before the darts were mentioned -> drawn only on "The darts stay ...", all at
  once with its label; the PURPLE line is named "grid" from its first point. Check line used an inline "½ /√100" ->
  stacked \frac{1/2}{\sqrt{100}} built from the formula's own parts with N swapped for 100. Straight apostrophe ->
  "ball’s edge".
- Audio ("each deictic lands; pauses intentional"): counters landed ~1 s after "52" / "44" -> each count starts on
  "puts" / "put" and ends on the number. 13.6 s breathless stretch -> [pause 0.8] after the voiced misconception
  (its picture holds through it) and the 27-word dart sentence split in three. "Berkstra" -> override /bˈɜɹɡstɹɑ/
  (whisper-checked). "noticed" heard as "notice" -> the landing says "The darts never counted the axes" while the
  YELLOW counter counts the regrowing axes 1 -> 100 as in the first frame.
- Concision (budget): the additions cost ~25 words; paid for by cutting the spoken restated question in the
  prediction beat (the on-screen "= ?" carries the 1.6 s hold), "is ... while" in the rescue line, "Darts do have"
  -> "Darts have", and by merging the walk and the division into one beat.
