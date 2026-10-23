# Episode 5: Why Random Darts Beat Grids in 100 Dimensions

**One idea:** to average a function over d inputs with a fixed budget of N points, an even grid gets only the
d-th root of N values per axis, so it collapses as d grows (in 100-D it is one point, the centre). A random dart
lands inside with a chance equal to the answer, its coordinates independent, in any dimension: each dart is a
coin flip and the estimate is the share of heads. The ±½ misses partly cancel (N darts stray about √N halves),
so the typical miss is one dart's spread over root N (½/√N for our yes/no question), with no d in it.
(Honest limits: a general function swaps the half for its own spread σ; more distinct values per axis is not
the cure, as the diagonal shows; and a vanishingly small answer still defeats plain darts.)

**Round-5 render pass restructure.** Cut to about 485 words (from 604) for a ~3:30 runtime at the guide's voice
settings (`CADENCE = "shaped"`, speed 0.83, beat gaps 0.45-0.65 s): the shadows-on-one-axis detour and its
N^(1/d) formula (B7's spoken numbers already carry values-per-axis), "quadruple the darts" (the random walk
derives √N and is checked against the measured 4.8), and the grid's cited N^(-2/d) law with its d = 4 tie are
gone. The diagonal now voices the misconception itself ("Maybe darts win by giving every axis more values").
Planned holds: 1.5 s at both predictions; 0.9 s after "fifty points off", after 2^100 and after ½/√N; 1.2 s
after the 0.05-point answer.

## Palette (colour -> one meaning, whole episode)

| colour | meaning |
|---|---|
| PURPLE | the grid and any even, deterministic design: its points, estimates, values-per-axis count, the diagonal |
| BLUE | random darts: dart points and 100-axis polylines, their estimates, squared-distance bars, the root-N (dart count) term |
| YELLOW | the dimension d: the "d = 100" readout, the current-dimension marker, "no d" |
| RED | error / miss: "off by ...", the ±spread brackets, one dart's miss (the half, sigma), "typical miss" |
| INK | the target shape (outline), the ball's edge r² (dashed tick / level), the true answer ½ (dashed line), words |
| GRAY / AXIS / DIM | GRAY: ticks, axis titles, citations, notes (7.7:1); AXIS: axis lines and tick marks; DIM: de-emphasised context |

Inside vs outside is shown by **shape** (filled vs hollow dot) and by words, never by colour. No green is used.
Errors are in **percentage points** everywhere; the one relative error (the limit) is said in words ("off by
the whole answer").

## Beats

### Cold open (0:00–0:12)
**B0.** A million evaluations to price an option on a hundred stocks: an average over a hundred inputs. Spread
them as a grid; that feels thorough. How many values does each input get? [pause 1.5]
> First frame: "N = 1,000,000 points", axis 1 and a YELLOW counter "d = 1". The 100 axes sweep in left to right
> while the counter counts them, landing on "d = 100" on "a hundred stocks"; "e.g. an option on 100 stocks" with
> the Glasserman citation (≈5 s); on "average" the caption becomes "each line: one input, from 0 to 1" while
> axis 1 flashes; PURPLE grid levels sweep on "Spread them as a grid"; "grid values per input: ?"; 1.5 s hold.

### Reveal + stakes + open loop (0:12–0:31)
**B1.** One. The whole grid is one point: the centre. Two values per input would take two to the hundredth
points. [pause 0.6]
> "?" leaves and "1" arrives (a swap, never superimposed); a PURPLE dot at ½ on every axis, "the centre"; ghost dots at ¼ and ¾; 2^100 written
> out (31 digits) on "two to the hundredth" and held.

**B2.** Since Metropolis and Ulam's 1949 paper, the standard tool has been random points, like this one. How
far off would a million random points land?
> Both sources on one citation line, bottom-left (≈5 s); a BLUE polyline (one random point) drawn as "like this
> one" is spoken, "a random point: one value per input"; "a million random points: off by ?" (BLUE "?").

### Naive build in 2-D (0:31–0:52)
**B3.** Start with two inputs. Our function is one inside this quarter disc, zero outside: its average is exactly
one half.
> Only the dart's dots on inputs 1 and 2 survive; they merge into the 2-D dart while axes 1 and 2 swing into the
> square's axes; the disc is drawn on "this quarter disc"; its fill pulses on "average"; "true answer ½".

**B4.** A grid of a hundred points puts fifty-two inside: two points off.
**B5.** A hundred random darts put forty-four inside: six points off. In two dimensions, the grid wins.
> Counters tick 0 -> 52 and 0 -> 44, starting on "puts" / "put" so each lands on its spoken number; the grid's
> readout is boxed.

### Fail: the dimension climb at a fixed budget (0:52–1:25)
**B6.** Now give each a million points, and add inputs. The disc becomes a ball, grown to cover exactly half the
box.
> The squares' contents leave and the true answer settles below first; then the darts square's four edges and
> disc travel edge to edge onto the back face of a cube centred on an empty frame; "d = 2" -> "d = 3" lands with
> the depth edges; the flat disc itself bulges into the exact r = 0.985 eighth-ball (one
> family of shapes, so only one boundary at any moment) while "ball radius 0.80" ticks to 0.98; "d = 2" -> "d = 3" is a swap.

**B7.** The grid's million points give each axis a thousand values in two dimensions, then a hundred, ten, three.
> The cube shrinks to a thumbnail; the log-log chart ("miss (percentage points)" vs "dimensions") and its rows
> "values per axis / points used / ball radius" are drawn; each spoken number lands with its column.

**B8.** From twenty dimensions on, just the centre, inside the ball. So the grid's estimate is the whole box.
Fifty points off. [pause 0.8]
> Rows "1", "1"; the thumbnail's centre dot lights, "centre is / inside the ball"; copies of it fly onto the chart
> as the d = 20 and d = 100 grid points ("grid says 1.000", RED "50 points off").

**B9.** Even two values on nineteen axes: eighteen points off. [pause 0.3] The darts stay under a tenth of a point.
> "grid says 1.000" leaves and the table dims to 30 %; a hollow PURPLE dot drops 50 -> 17.6 at d = 20 with two lines
> beside it, "2 values on 19 axes" and RED "18 points off"; its cost 524,288 swaps into the "points used" cell at
> d = 20. On "darts" the whole BLUE line (all six d) is drawn at once with "darts (simulated)"; the 0.1 tick flashes.
> (The PURPLE line is named "grid" from its first point at d = 2; the BLUE line is not on screen before this.)

### Insight (1:25–2:40)
**B12.** Maybe darts win by giving every axis more values. [pause 0.8] A million points on the diagonal give every
axis a million values, and still miss by eight points: their coordinates move in lockstep. [pause 0.3]
> In the breath before it the chart clears and its 2-D darts point opens into the darts square (left, "2
> dimensions") while the 100-axis panel is drawn at 30 % on the right. The voiced misconception gets its picture: the 100 darts drop 100 BLUE shadows onto one axis,
> "100 values on one axis". Then the square dims and the 100-axis panel is drawn ("100 dimensions"); ONE flat
> PURPLE line, "one point: (t, t, …, t)", then 25 more; every axis flashes; the dashed "ball's edge"; lines above
> it turn dashed: "57.7% inside: 7.7 points off"; on "lockstep" the one flat line slides up and back as a whole.

**B13.** A dart's coordinates are drawn independently and uniformly. [pause 0.3] So it lands inside with a chance
equal to the answer, in any dimension. [pause 0.4] Each dart is a coin flip. [pause 0.6]
> The cold-open dart is ringed in 2-D and its jagged 100-D polyline drawn alone against the diagonal's flat line
> (30 %). Gauges: "x1² + x2² = 1.20 > 0.64 = 0.80²" -> "outside -> 0"; "x1² + … + x100² = 31.8 < 33.3 = 5.77²" ->
> "inside -> 1". On "coin flip" each verdict and its dart become that dart's coin (the 100-D polyline shrinks
> rigidly into its coin as the coin grows); then the other 99 of each run become coins (each faint 100-D polyline
> shrinks into its own coin): "44/100" and "48/100".

**B14.** One flip is either zero or one. Its average is a half, so every flip misses by exactly a half.
> One coin on a 0–1 line, flips 0 -> 1; dashed ½; a RED "½" bracket that swaps side with the coin.

**B15.** Repeat the hundred-dart experiment three hundred times. In both, the estimates spread this wide. [pause 1.4]
> The coin line waits at 30 % above the histograms; "N = 100 darts"; 300 simulated runs fill both histograms
> (one "10 runs" scale bar); both brackets "±4.8 pts" grow during "spread this wide", are flagged side by side and
> hold ~2 s; then both labels fly together into one tag "measured: ±4.8 pts", parked at the right at 60 %.

**B15b.** Those misses fall up or down at random, so they partly cancel. [pause 0.3] Sixteen darts typically stray
four halves, not sixteen. [pause 0.3] What adds is their squares: sixteen of them fill a square four halves wide.
[pause 0.4] N darts stray about root N halves. [pause 0.3] Divide by N, and the typical miss is a half over root N.
[pause 0.8] For a hundred darts: five points. We measured four point eight. [pause 0.3] Any other function swaps the
half for its own spread, sigma; there's still no d.
> Sixteen copies of the coin's RED ½ bracket become a bold random walk (darts 17–32 of the 2-D run); the down steps
> flash on "cancel"; on "Sixteen darts" the other eleven consecutive 16-dart groups of both runs fan out from the
> same start at 35 % ("12 groups of 16 darts (simulated)"; ends −10 … +4, RMS 3.96 halves); a RED band "±4 halves"
> at their end; on "not sixteen" the 30 % staircase "16 halves / if they never cancelled". On "their squares" each
> bold step grows a half-by-half RED square; the sixteen squares tile one 4 × 4 square whose top is the band's +4
> ("four halves wide"). 16 -> N, 4 -> √N. "√N · ½" is built from the band's √N and the coin's ½; on "Divide by N"
> "typical miss =" and the bar arrive and the N of "N halves" flies under it; on "a half over root N" the numerator's
> √N drops into the N, which grows a root sign: ½/√N (flagged), and the staircase clears. Check, built from the
> formula with N swapped for 100: \frac{1/2}{\sqrt{100}} = 0.05 = 5 pts; the parked "measured: ±4.8 pts" tag returns
> under it. Then the walks dim to 30 %, ½ is flagged and becomes σ ("σ = one dart's spread"), and "no d" appears.

**B17.** So, back to our ball: a million darts, any dimension. [pause 1.6] One half over a thousand: five hundredths
of a point. [pause 1.0]
> The walk leaves; the formula takes the top centre; σ -> ½ while the dimension chart's frame (axes, ticks, titles)
> returns beneath it, then its two data lines are drawn; N -> 1,000,000; "no d" flashes on "any dimension"; the open question returns as a BLUE "= ?" for the
> 1.5 s prediction hold; √1,000,000 -> 1000; the "?" becomes "typical miss = 0.0005 = 0.05 points" (each change is a
> swap: the old term leaves before the new one arrives); a rigid copy
> of "0.05 points" drops onto the chart's new dashed BLUE line, "typical miss: 0.05 points", and the six BLUE
> runs, all under it, flash. (This closes the B2 question.)

### Payoff + honest limit (2:40–3:22)
**B18.** In 2012, Bergstra and Bengio found random search tuned neural networks as well as grid search, in a
fraction of the time. [pause 0.45] Only a few settings really matter. [pause 0.2] With one, the search is
one-dimensional: nine grid trials test three values of it; nine random trials test nine. [pause 0.3]
> (Round 6: this says why per-axis values matter here but did not rescue the diagonal: the search has one real
> input. On "one-dimensional" the "important setting" axis flashes and the "unimportant" axis dims to 30 %.)
> The chart fades first, then its PURPLE grid dots become the nine grid-search trials and its BLUE dots the nine
> random trials (after their Figure 1, "model score (schematic)"); 3 vs 9 distinct shadows on the score curve.

**B19.** Darts have a blind spot: tiny answers. Keep the ball's radius at one, and in thirty dimensions it
fills two parts in a hundred trillion of the box. Below this line, a million darts expect under one hit, so they
usually report zero: a tiny miss, but the whole answer.
> The panel fades out completely; the log chart "share of box inside a radius-1 ball"; its curve (d = 2..30) is
> drawn from "tiny answers" to "radius", the title flashes on "radius at one", the d = 30 dot on "thirty", and
> "2 × 10^-14" lands on "two parts in a hundred trillion"; dashed BLUE 1/N drawn on "this line"; RED zone from the crossing (d = 17.06): "under 1 hit expected" ->
> "darts report 0: / off by the whole answer".

### Landing (3:22–3:30)
**B20.** The darts never counted the axes: a million coin flips, in any dimension.
> (Round 6: "noticed" was heard as "notice"; "counted" also answers the cold open's d counter, which counted the
> axes 1 -> 100.)
> The limit chart clears; its dashed 1/N line rises and shrinks into a rule under the cold-open header, which
> settles on it ("N = 1,000,000 points"), and its x-axis
> becomes the floor the 100 axes grow from; the PURPLE centre line ("1 value per axis"); BLUE polylines flood
> every axis, "1,000,000 coin flips"; "d = 100" flashes. End card.

## Pronunciation overrides
- Bengio -> /bˈɛnʤiO/ (G2P default had a hard g)
- Ulam -> /ˈulɑm/
- d-th -> /dˈiθ/ (default read the letters D T H)
- Bergstra -> /bˈɜɹɡstɹɑ/ (round 6: whisper heard "Berkstra" in the master; the override was checked with whisper)

## Sources (details and checks in facts.md)
- Metropolis, N. & Ulam, S. (1949). The Monte Carlo Method. *JASA* 44(247):335–341.
- Glasserman, P. (2003). *Monte Carlo Methods in Financial Engineering*. Springer (Applications of Mathematics 53), §1.1
  (option prices as high-dimensional averages; σ/√n "for all d").
- Bergstra, J. & Bengio, Y. (2012). Random Search for Hyper-Parameter Optimization. *JMLR* 13:281–305.
- Paskov, S. H. & Traub, J. F. (1995). Faster Valuation of Financial Derivatives. *J. Portfolio Management*
  22(1):113–123 (background: Monte Carlo is "widely used"; quasi-random points can do better — why B2 says
  "usually").
- Eckhardt, R. (1987). Stan Ulam, John von Neumann, and the Monte Carlo Method. *Los Alamos Science* 15:131–141 (background).
