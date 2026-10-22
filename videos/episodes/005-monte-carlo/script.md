# Episode 5: Why Random Darts Beat Grids in 100 Dimensions

**One idea:** to average a function over d inputs, a grid of N points in d dimensions only gets the d-th root of N
values per axis, so its accuracy collapses as d grows. A random dart lands inside with a chance equal to the
answer, independently of the others, in any dimension, so the darts' estimate is a share of heads in N coin
flips. Their ±½ misses partly cancel (N of them stray about √N halves), so the error is one dart's spread over
root N (one half over root N for our yes/no question), with no d in it; a grid's error, even for smooth
functions, has d in its exponent (N^(−2/d)). (Honest limits: a general function swaps the half for its own
spread sigma; more distinct values per axis alone is not the cure; and a vanishingly small answer still
defeats plain darts.)

Runtime about 3:52, about 600 words, narrator af_heart @ 0.87 (about 163 wpm over speech time).
Pauses: about 0.25 s between sentences inside a thought, about 0.85 s at the beat boundaries (after the
stakes, after "the grid wins", after the fail, after the diagonal, after both laws, after "all six of ours
did", after Bergstra & Bengio), 0.8 s holds after the 2^100 number, the ½/√N result and the 0.05-point answer,
1.5 s at the two prediction holds.

## Palette (colour -> one meaning, whole episode)

| colour | meaning |
|---|---|
| PURPLE | the grid and any even, deterministic design: its points, estimates, values-per-axis count, the N^(1/d) law, the diagonal |
| BLUE | random darts: dart points and 100-axis polylines, their estimates, squared-distance bars, the root-N (dart count) term |
| YELLOW | the dimension d: the "d = 100" readout, the current-dimension marker, d in N^(1/d), "no d" |
| RED | error / miss: "off by ...", the ±spread brackets, one dart's miss (the half, sigma), "typical miss" |
| INK | the target shape (outline), the ball's edge r² (dashed tick / level), the true answer ½ (dashed line), words |
| GRAY / DIM | axes, ticks, citations, de-emphasised context |

Inside vs outside is shown by **shape** (filled vs hollow dot) and by words, never by colour. No green is used.
Errors are in **percentage points** everywhere; the one relative error (the limit) is said in words ("off by
the whole answer").

## Beats

### Cold open (0:00–0:12)
**B0.** A million evaluations to price an option on a hundred stocks: an average over a hundred inputs. An even
grid feels thorough. How many values does each input get? [pause 1.5]
> First frame: "N = 1,000,000 points", axis 1 and a YELLOW counter "d = 1". The 100 grey axes sweep in left to right
> while the counter counts them, landing on "d = 100" on "a hundred stocks"; "e.g. an option on 100 stocks" with
> "Glasserman, 2003 · Monte Carlo Methods in Financial Engineering, Springer" (≈6 s); on "average" the caption becomes
> "each line: one input, from 0 to 1" while axis 1 flashes; PURPLE grid levels sweep on "even grid";
> "grid values per input: ?"; 1.5 s hold.

### Reveal + stakes + open loop (0:12–0:35)
**B1.** One. The whole grid is one point, the centre of the box. Two values per input would take two to the
hundredth points. [pause 0.8]
> "?" -> "1"; a PURPLE dot at ½ on every axis, "the centre"; ghost dots at ¼ and ¾; 2^100 written out (31 digits)
> on "two to the hundredth" (1.2 s) and held about 2 s.

**B2.** Since Metropolis and Ulam's 1949 paper, the standard tool has been random points, like this one. How far
off would a million of them land?
> Both sources on one citation line, bottom-left (≈5 s): "Metropolis & Ulam, 1949 · JASA;   Glasserman, 2003 ·
> Springer"; a BLUE polyline (one random point), "a random point: one value per
> input"; the open question "a million random points: off by ?" (BLUE "?") where the grid's "1" was.

### Naive build in 2-D (0:35–0:58)
**B3.** Start with two inputs: a square. Our function is one inside this quarter disc, zero outside, so its
average is the disc's share: exactly one half.
**B4.** A ten by ten grid puts fifty-two of its hundred points inside: two points off.
**B5.** A hundred random darts put forty-four inside: six points off. In two dimensions, the grid wins.
> Unchanged from round 2 (counters tick 0 -> 52 and 0 -> 44; the grid readout is boxed).

### Fail: the dimension climb at a fixed budget (0:58–1:32)
**B6.** Now give each a million points, and add inputs. The disc becomes a ball, grown just enough to cover exactly
half the box.
> The squares leave; the darts square's frame and disc become the back face of a large cube **centred on an empty
> frame**; "d = 2" -> "d = 3" lands with the cube's depth edges; only the outline inflates into the exact
> r = 0.985 eighth of a ball, then its fill fades in, while "ball radius 0.80" ticks to 0.98; "true answer ½ in every
> dimension" under it.

**B7.** The grid splits its million across the axes: a thousand values per axis in two dimensions, then a
hundred, ten, three.
> The cube shrinks to a 40 % thumbnail in the top-right corner beside "true answer ½ in every dimension" while
> the log-log chart and its "values per axis" row are drawn. YELLOW marker steps; each spoken number lands with its column ("values per
> axis" 1000/100/10/3, "points used" 10^6/10^6/10^6/59,049, GRAY "ball radius" 0.80/0.98/1.40/1.82) and its two
> error dots. The y axis is "miss (percentage points)".

**B8.** From twenty dimensions on, just the centre, which sits inside the ball. So the grid says the ball fills the
box: fifty points off.
> Rows "1", "1". A PURPLE dot appears at the cube's centre in the thumbnail, labelled "centre is / inside the
> ball" (one size, Text 26, beside the thumbnail, no arrow), and pulses on "sits inside the ball". On "fills"
> copies of that dot fly onto the chart as the d = 20 and d = 100 grid points at 50 ("grid says 1.000"); RED
> "50 points off"; the thumbnail leaves.

**B9.** Even two values on nineteen axes, half a million points, is eighteen points off. The darts stay under a
tenth of a point.
> Hollow PURPLE dot drops 50 -> 17.6 at d = 20, "2^19 points · 18 points off" over "2 values on 19 axes"; BLUE
> dots at 0.025 and 0.004.

### Insight (1:32–2:46)
**B10.** Look at the shadows on one axis: the grid's hundred points cast ten, a hundred darts cast a hundred.
> In the breath before the sentence the chart's d = 2 column opens into the two squares; the rails appear by
> "shadows" and the shadows drop onto them: 10 PURPLE ticks vs 100 BLUE.

**B11.** With N points over d axes, [pause 0.4] each axis gets the d-th root of N.
> On "N points" the 100 grid dots fly into "100", on "d axes" the two axes into the exponent's "2", then "= 10
> values" (from the shadow label): "100^(1/2) = 10 values"; on "d-th root of N" it generalises to "N^(1/d)
> values per axis" (held about 3 s).

**B12.** But shadows alone are not the fix. A million points on the diagonal, each one a flat line here, give
every axis a million values, and still miss by eight points: their coordinates move in lockstep. [pause 0.6]
> The 100 BLUE shadows flash. The grid side leaves; the darts square slides left and dims ("2 dimensions"); a
> 100-axis panel ("100 dimensions"); "10^6 points on the diagonal". ONE flat PURPLE line is drawn alone with
> "one point: (t, t, ..., t)" beside it (about 1.5 s), then the other 25 sweep up; every axis flashes PURPLE.
> A dashed INK level at t = 0.577 labelled "ball's edge"; the lines below it stay solid (inside), those above
> turn dashed and faint (outside): "57.7% inside: 7.7 points off". On "coordinates ... lockstep" the one flat line
> slides up the panel and back as a whole while "(t, t, ..., t)" flashes.

**B13.** A dart's coordinates are drawn independently, so it lands inside with a chance equal to the answer, in two
dimensions or a hundred. Their estimate is a share of heads in N coin flips.
> The diagonal clears; the 2-D square returns; the cold-open dart is ringed and its 100-D polyline is drawn alone
> (no haze); the diagonal's flat line stays at 30 % and flashes against the dart's jagged line on "independently".
> Under each, a gauge: "x1² + x2² = 1.20 > 0.64 = 0.80²" with a BLUE bar growing past the dashed INK r² tick,
> "outside -> 0"; "x1² + ... + x100² = 31.8 < 33.3 = 5.77²", bar stopping short of the tick, "inside -> 1". The disc
> fill pulses on "chance equal to the answer". Everything but the two verdicts steps away (the square's outline
> stays at 30 %); each verdict and its dart become that dart's coin; the other 99 darts of the 100-D run fan in
> as faint polylines on the panel; then every dart collapses into its coin, the 2-D 99 from their dots, and the
> square's outline becomes the coin block's frame: "44/100" and "48/100".

**B14.** One flip is zero or one. Its average is a half, and every flip misses that by exactly a half.
> The ringed dart's coin moves onto a 0–1 number line shown 1.8x large below centre, captioned "one yes/no dart"
> (Text 28, above it); flips 0 -> 1; dashed ½; a RED "½" bracket that swaps side with the coin.

**B15.** Repeat the hundred-dart experiment three hundred times. In two dimensions or a hundred, the estimates
spread this wide. Quadruple the darts, and both get twice as narrow.
> The coin line shrinks and waits at 30 % above the gap between the histograms (one focal point); the histograms
> are 10 % wider; header "N = 100 darts"; one "10 runs" scale bar; 300 runs fill; both brackets "±4.8 pts" grow on
> "this wide"; N = 100 -> 400: both bars and brackets narrow, the numbers count down to ±2.6 / ±2.4.

**B15b (why root N).** Each dart misses by a half, up or down at random, so the misses partly cancel: sixteen darts
stray about four halves, not sixteen. [pause 0.6] N darts stray about root N halves. Divide by the N darts:
[pause 0.4] a half over root N. With a hundred darts, that's five points; we measured four point eight. [pause 0.6]
> The histograms have made their point and leave; the coin line moves to the lower right. Sixteen copies of its
> RED ½ miss bracket become sixteen RED step arrows, up for a dart inside, down for one outside (darts 62–77 of
> the 2-D run: 10 in, 6 out), chained into a random walk over a dashed INK zero line; the down steps flash on
> "cancel"; a RED bracket from zero to the walk's end: "4 halves"; on "not sixteen" copies of the steps swing
> into a straight 30 % staircase: "16 halves / if they never cancelled" (held ≈1.8 s). "16" -> "N", "4" -> "√N"
> (BLUE). The walk is ≈1.4x the round-4 size with 6 px steps; the coin line sits full size in the lower right. Then
> the walk's "√N" and the coin's ½ build "√N · ½" at the top; on "Divide" "typical miss =" and a fraction bar are
> written and the BLUE N of "N halves" flies under it: typical miss = (√N · ½)/N; on "a half over root N" the
> numerator's √N drops into the N, which becomes √N: typical miss = ½/√N (the √N flagged). Check line under it:
> "N = 100: ½/√100 = 0.05 = 5 points" and, in RED, "measured: ±4.8 pts" (the histograms' brackets).

**B16.** Any other function swaps that half for its own spread, sigma. [pause 0.4] The root N remains, and there's
no d in it. A grid's miss, even for smooth functions, has d in its exponent. The exponents tie at four dimensions,
near where our lines crossed.
> The walk leaves and the formula settles mid-frame; its ½ is flagged on "half" and FadeTransforms into σ on the
> word "sigma" (0.5 s), then is flagged; "σ = one dart's spread". "darts:" appears
> left of the formula and "no d" under √N. On "A grid's error" the grid's law is written beneath it, left-aligned:
> Round 5 layout: the darts' law moves to the top left under "random darts"; "σ = one dart's spread" under it;
> "no d" beside √N. The grid's law is written top right under "grid, smooth f": "miss ∝ N^(−2/d)" (its YELLOW d a
> copy of the d in "no d"), with "Glasserman, 2003 · ... §1.1". On "The exponents tie" the citation leaves, copies of
> N^(−2/d) and √N build "N^(−2/d) = N^(−1/2) at d = 4" under the grid's law, and a compact copy of the dimension
> chart (same data, no rows) is drawn beneath both laws; on "near where our lines crossed" a YELLOW dashed d = 4
> marker rises at the crossing.

**B17.** So, back to our ball, with a million darts, in any dimension: how far off is a typical estimate?
[pause 1.5] One half over a thousand: five hundredths of a point. [pause 1.2]
> Everything but the formula leaves; the formula moves to (0, 0.6) and grows 1.15x; σ FadeTransforms back to ½
> (our ball); N -> 1,000,000; "no d" flashes on "any dimension"; the open question returns as a BLUE "= ?" for
> the prediction hold; √1,000,000 -> 1000 on "a thousand"; the "?" becomes the answer on "five hundredths":
> "typical miss = 0.0005 = 0.05 points" at the top centre, above the compact chart; then "0.05 points" drops
> onto the chart as its new dashed BLUE line's label, "typical miss: 0.05 points" (right of the line), and the six
> BLUE dots, all under the line, flash. (This closes the B2 question.)

### Payoff + honest limit (2:46–3:38)
**B18.** In 2012, Bergstra and Bengio found that random search tuned neural networks as well as grid search, in a
fraction of the time. If one setting matters most, nine grid trials test three values of it; nine random trials
test nine.
> The compact chart's PURPLE grid dots become the nine grid-search trials and its BLUE dart dots the nine random
> trials as the two squares are drawn (after their Figure 1, "model score (schematic)"); "random search" is written
> on "random search", "grid search" on "grid search"; 3 vs 9 distinct shadows on the score curve (random points from a seed whose x-values are at least 0.06 apart and uncorrelated with y).

**B19.** Darts do have a blind spot: tiny answers. Fix the radius at one, and by thirty dimensions the ball fills
two parts in a hundred trillion of the box. Below this line, a million darts expect under one hit, so they usually
report zero: off by the whole answer.
> The Bergstra & Bengio panel fades out completely; then the log chart's axes are drawn (10^-18 to 1): share of the
> cube inside a radius-1
> ball, d = 2..30 (2 × 10^-14 at 30). Dashed BLUE
> 1/N = 10^-6. RED shading only where the curve is below the line (d ≥ 17.06); its label sits in the zone under
> the curve's tail: "under 1 hit expected" -> "darts report 0: / off by the whole answer".

### Landing (3:38–3:45)
**B20.** The darts never noticed the axes: [pause 0.3] a million coin flips, in any dimension.
> In the breath before it, the limit chart's dashed BLUE 1/N line becomes the cold-open header "N = 1,000,000
> points" and its x-axis becomes the floor from which the 100 input axes grow up; the single PURPLE centre line
> ("1 value per axis"); BLUE polylines flood every axis, "1,000,000 coin flips"; "d = 100" flashes. End card.

## Pronunciation overrides
- Bengio -> /bˈɛnʤiO/ (G2P default had a hard g)
- Ulam -> /ˈulɑm/
- d-th -> /dˈiθ/ (default read the letters D T H)

## Sources (details and checks in facts.md)
- Metropolis, N. & Ulam, S. (1949). The Monte Carlo Method. *JASA* 44(247):335–341.
- Glasserman, P. (2003). *Monte Carlo Methods in Financial Engineering*. Springer (Applications of Mathematics 53), §1.1
  (option prices as high-dimensional averages; σ/√n "for all d"; product trapezoid rule O(n^(−2/d))).
- Bergstra, J. & Bengio, Y. (2012). Random Search for Hyper-Parameter Optimization. *JMLR* 13:281–305.
- Paskov, S. H. & Traub, J. F. (1995). Faster Valuation of Financial Derivatives. *J. Portfolio Management*
  22(1):113–123 (background: Monte Carlo is "widely used"; quasi-random points can do better — why B2 says
  "usually").
- Eckhardt, R. (1987). Stan Ulam, John von Neumann, and the Monte Carlo Method. *Los Alamos Science* 15:131–141 (background).
