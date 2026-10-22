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
> Counters tick 0 -> 52 and 0 -> 44; the grid's readout is boxed.

### Fail: the dimension climb at a fixed budget (0:52–1:25)
**B6.** Now give each a million points, and add inputs. The disc becomes a ball, grown to cover exactly half the
box.
> The squares' contents leave and the true answer settles below first; then the darts square's four edges and
> disc travel edge to edge onto the back face of a cube centred on an empty frame; "d = 2" -> "d = 3" lands with
> the depth edges; the outline inflates into the exact r = 0.985 eighth-ball while "ball radius 0.80" ticks to 0.98.

**B7.** The grid's million points give each axis a thousand values in two dimensions, then a hundred, ten, three.
> The cube shrinks to a thumbnail; the log-log chart ("miss (percentage points)" vs "dimensions") and its rows
> "values per axis / points used / ball radius" are drawn; each spoken number lands with its column.

**B8.** From twenty dimensions on, just the centre, inside the ball. So the grid's estimate is the whole box.
Fifty points off. [pause 0.8]
> Rows "1", "1"; the thumbnail's centre dot lights, "centre is / inside the ball"; copies of it fly onto the chart
> as the d = 20 and d = 100 grid points ("grid says 1.000", RED "50 points off").

**B9.** Even two values on nineteen axes is eighteen points off, while the darts stay under a tenth of a point.
> Hollow PURPLE dot drops 50 -> 17.6 at d = 20, with a stack beside it: "2 values on 19 axes", "2^19 = 524,288
> points" (about half the budget), "18 points off"; BLUE darts dots at d = 20 and 100; the 0.1 tick flashes.

### Insight (1:25–2:40)
**B12.** Maybe darts win by giving every axis more values. A million points on the diagonal give every axis a
million values, and still miss by eight points: their coordinates move in lockstep. [pause 0.6]
> In the breath before it the chart clears and its 2-D darts point opens into the darts square (left, "2
> dimensions") while the 100-axis panel is drawn at 30 % on the right. The voiced misconception gets its picture: the 100 darts drop 100 BLUE shadows onto one axis,
> "100 values on one axis". Then the square dims and the 100-axis panel is drawn ("100 dimensions"); ONE flat
> PURPLE line, "one point: (t, t, …, t)", then 25 more; every axis flashes; the dashed "ball's edge"; lines above
> it turn dashed: "57.7% inside: 7.7 points off"; on "lockstep" the one flat line slides up and back as a whole.

**B13.** A dart's coordinates are drawn independently and uniformly, so it lands inside with a chance equal to
the answer, in any dimension: each dart is a coin flip. [pause 0.6]
> The cold-open dart is ringed in 2-D and its jagged 100-D polyline drawn alone against the diagonal's flat line
> (30 %). Gauges: "x1² + x2² = 1.20 > 0.64 = 0.80²" -> "outside -> 0"; "x1² + … + x100² = 31.8 < 33.3 = 5.77²" ->
> "inside -> 1". On "coin flip" each verdict and its dart become that dart's coin (the 100-D polyline shrinks
> rigidly into its coin as the coin grows); then the other 99 of each run become coins (each faint 100-D polyline
> shrinks into its own coin): "44/100" and "48/100".

**B14.** One flip is either zero or one. Its average is a half, so every flip misses by exactly a half.
> One coin on a 0–1 line, flips 0 -> 1; dashed ½; a RED "½" bracket that swaps side with the coin.

**B15.** Repeat the hundred-dart experiment three hundred times. In both, the estimates spread this wide.
> The coin line waits at 30 % above the histograms; "N = 100 darts"; 300 simulated runs fill both histograms
> (one "10 runs" scale bar); both brackets "±4.8 pts" grow on "this wide".

**B15b.** Those misses fall up or down at random, so they partly cancel: sixteen darts stray about four halves, not
sixteen. [pause 0.4] N darts stray about root N halves. Divide by N, and the typical miss is a half over root N.
[pause 0.8] For a hundred darts: five points. We measured four point eight. [pause 0.3] Any other function swaps
the half for its own spread, sigma; there's still no d.
> Sixteen copies of the coin's RED ½ bracket become a random walk (darts 62–77 of the 2-D run: 10 in, 6 out); the
> down steps flash on "cancel"; "4 halves" vs the 30 % staircase "16 halves / if they never cancelled"; 16 -> N,
> 4 -> √N. "√N · ½" is built from the walk's √N and the coin's ½; on "Divide by N" "typical miss =" and the bar are
> written and the N of "N halves" flies under it; on "a half over root N" the numerator's √N drops into the N,
> which grows a root sign: ½/√N (flagged). Check: "½/√100 = 0.05 = 5 pts", RED "measured: ±4.8 pts". Then the walk
> dims to 30 %, ½ is flagged and cross-fades into σ ("σ = one dart's spread"), and "no d" appears beside √N.

**B17.** So, back to our ball: a million darts, any dimension. How far off is a typical estimate? [pause 1.5] One
half over a thousand: five hundredths of a point. [pause 1.0]
> The walk leaves; the formula takes the top centre; σ -> ½ while the dimension chart (same data) returns
> beneath it; N -> 1,000,000; "no d" flashes on "any dimension"; the open question returns as a BLUE "= ?" for the
> 1.5 s prediction hold; √1,000,000 -> 1000; the "?" becomes "typical miss = 0.0005 = 0.05 points" (each change is a
> swap: the old term leaves before the new one arrives); a rigid copy
> of "0.05 points" drops onto the chart's new dashed BLUE line, "typical miss: 0.05 points", and the six BLUE
> runs, all under it, flash. (This closes the B2 question.)

### Payoff + honest limit (2:40–3:22)
**B18.** In 2012, Bergstra and Bengio found random search tuned neural networks as well as grid search, in a
fraction of the time. [pause 0.45] If one setting matters most, nine grid trials test three values of it; nine
random trials test nine. [pause 0.3]
> The chart fades first, then its PURPLE grid dots become the nine grid-search trials and its BLUE dots the nine
> random trials (after their Figure 1, "model score (schematic)"); 3 vs 9 distinct shadows on the score curve.

**B19.** Darts do have a blind spot: tiny answers. Keep the ball's radius at one, and in thirty dimensions it
fills two parts in a hundred trillion of the box. Below this line, a million darts expect under one hit, so they
usually report zero.
> The panel fades out completely; the log chart "share of box inside a radius-1 ball"; its curve (d = 2..30) is
> drawn from "tiny answers" to "radius", the title flashes on "radius at one", the d = 30 dot on "thirty", and
> "2 × 10^-14" lands on "two parts in a hundred trillion"; dashed BLUE 1/N drawn on "this line"; RED zone from the crossing (d = 17.06): "under 1 hit expected" ->
> "darts report 0: / off by the whole answer".

### Landing (3:22–3:30)
**B20.** The darts never noticed the axes: a million coin flips, in any dimension.
> The limit chart clears; its dashed 1/N line rises and shrinks into a rule under the cold-open header, which
> settles on it ("N = 1,000,000 points"), and its x-axis
> becomes the floor the 100 axes grow from; the PURPLE centre line ("1 value per axis"); BLUE polylines flood
> every axis, "1,000,000 coin flips"; "d = 100" flashes. End card.

## Pronunciation overrides
- Bengio -> /bˈɛnʤiO/ (G2P default had a hard g)
- Ulam -> /ˈulɑm/
- d-th -> /dˈiθ/ (default read the letters D T H)

## Sources (details and checks in facts.md)
- Metropolis, N. & Ulam, S. (1949). The Monte Carlo Method. *JASA* 44(247):335–341.
- Glasserman, P. (2003). *Monte Carlo Methods in Financial Engineering*. Springer (Applications of Mathematics 53), §1.1
  (option prices as high-dimensional averages; σ/√n "for all d").
- Bergstra, J. & Bengio, Y. (2012). Random Search for Hyper-Parameter Optimization. *JMLR* 13:281–305.
- Paskov, S. H. & Traub, J. F. (1995). Faster Valuation of Financial Derivatives. *J. Portfolio Management*
  22(1):113–123 (background: Monte Carlo is "widely used"; quasi-random points can do better — why B2 says
  "usually").
- Eckhardt, R. (1987). Stan Ulam, John von Neumann, and the Monte Carlo Method. *Los Alamos Science* 15:131–141 (background).
