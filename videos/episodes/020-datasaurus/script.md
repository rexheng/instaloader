# Episode 20 — A Dinosaur Hiding in Your Summary Statistics

**One idea:** two means, two standard deviations and a correlation pin down exactly one ellipse
(a centre, a box, and where the ellipse touches the box), so any shape with that ellipse (a
dinosaur, a star, Anscombe's four datasets) has the same five numbers and even the same
best-fit line. Only a plot shows the shape.

Runtime 3:42 · 560 words · narrator af_heart @ 0.84.

## Palette (colour → one meaning, whole episode)

| colour | meaning |
|---|---|
| YELLOW | the summary: the dinosaur's five numbers and the geometry they pin down (centre, mean ± SD error bars, SD box, ellipse, touch dots, the run along the centre line and the rise r s_y, best-fit line, the bar graph built from ȳ and s_y); the live r label during the sweep; Anscombe's five numbers, his summary geometry and the slope formula terms and substituted values in the payoff |
| BLUE | actual data points (whatever dataset is on screen) |
| RED | a summary that has drifted away from the dinosaur's (live values that no longer match, the star's own drifting centre/error bars/box/ellipse, the missed median) |
| GREEN | "matches" marks (always paired with the = glyph; RED always paired with ≠) |
| GRAY | axes, ticks, the cold-open "?", the viewer's guess cloud and its dashed line ("your guess", "your line"), the two ghost ellipses (other members of the family that touch all four walls), the target star and circle outlines, citations and the sourced percentages ("86% used bars", "13% showed points"), the decimals note |
| INK | live "now" values while they still match, words, the white rings that single out one point (the nudged point; Anscombe's outlier and lever point) |

Never red vs green alone: every RED/GREEN mark is also a ≠ / = glyph.

## Beats

### Cold open (0:00–0:26; commit ends about 0:11.5)
**B0.** A hundred and forty-two points: two averages, two standard deviations, and a correlation of
minus point oh six. Which way does their best-fit line tilt, and how steeply? [pause 1.5]
> Frame 1: empty axes (0–100 × 0–100, equal aspect) with "n = 142" in grey inside, and the five
> symbol slots x̄ =, ȳ =, s_x =, s_y =, r = beside them (so the puzzle is on screen from the first
> frame). "n = 142" is flagged on "hundred", the symbols on "points"; each value is written
> (YELLOW) on its spoken words: 54.26, 47.83 on "two averages"; 16.76, 26.93 on "two standard
> deviations"; −0.06 on "correlation" (the published values: first two decimals, facts.md #2).
> "n = 142" fades on "Which way"; a faint grey "?" fades in at the plot centre for the 1.5 s hold.
> The commit is about the line (tilt and steepness), the one thing the five numbers really fix:
> the title gives the dinosaur away, not the line.

**B1.** A shapeless oval cloud with a nearly flat line is the reasonable guess. Here are the real
points: a dinosaur, drawn by Alberto Cairo, with these same five numbers.
> The "?" gives way to 142 grey points fading in as a soft oval cloud, labelled "your guess"; on
> "nearly flat line" a grey dashed line is drawn, labelled "your line" (the best-fit line the five
> numbers fix: slope r·s_y/s_x = −0.10). On "real" both labels and the line fade; the cloud's points
> travel (optimal assignment) into Cairo's Datasaurus and turn BLUE. Citation: "Datasaurus: Alberto
> Cairo, 2016 · The Functional Art".

### Stakes (0:26–0:38)
**B2.** In a review of seven hundred and three physiology papers, eighty-six percent used bar
graphs: an average and an error bar. Only thirteen percent showed the points.
> Citation swaps: "Weissgerber et al., 2015 · PLOS Biology". On "papers" the dinosaur squeezes
> sideways into a strip of its 142 y-values, and the x ticks, numbers and "x" dim to 25 %. On "bar
> graphs" a YELLOW bar grows to ȳ with a grey "86% / used bars" beside it; the ȳ row is flagged on
> "average"; a YELLOW error bar ±s_y is drawn on "error bar" (s_y row flagged); the points dim. On
> "Only thirteen percent" the bar dims, a grey "13% / showed points" is written on the other side,
> and the points return.

**B3.** So how much can five numbers hide? Let's hide a star in them, and demand that all five
still match the dinosaur's to two decimals.
> The strip springs back into the dinosaur; a grey dashed star outline is drawn on "star". The
> readout splits into two columns ("dinosaur | now", the "now" column live), = marks and a counter
> "matching 5/5" (the measurable goal). Grey note (Text 25): "first two decimals, as published",
> held through the fail beat until the dinosaur returns.

### Naive build: version one (0:46–0:51)
**B4.** Version one slides every point onto its own spot on a star.

### Fail (0:51–1:00)
**B5.** We got the star, and lost all five numbers. [pause 0.2] The center moved, the x spread grew, and the y
spread shrank by almost a quarter.
> Counter 0/5, flagged on "lost". YELLOW centre dot and mean ± SD error bars for the dinosaur, RED
> ones sliding to the star's centre (50, 50), stretching in x (16.76 → 20.51) and shrinking in y
> (26.93 → 20.50, −24 %). Each "now" value is Indicated in RED.

### Insight: five numbers = one ellipse (1:00–1:52)
**B6.** So what exactly do five numbers pin down?
> The star outline and the note fade while the points return to the dinosaur and the RED cross
> slides back into the YELLOW one (5/5); the five values flag on "five numbers".

**B7.** The two averages mark a single point: the cloud's balance point.
> Points dim. Copies of 54.26 and 47.83 fly into the YELLOW dot at (x̄, ȳ).

**B8.** The two standard deviations draw a box, one deviation out on each side.
> Copies of 16.76 and 26.93 land on the half-arms of the YELLOW cross; the box grows out of them.

**B9.** Many ellipses touch all four walls. The correlation picks one. Correlation r means one
standard deviation to the right, on average r standard deviations up. So the touch point on the
right wall sits r times s y above the center. At minus point oh six, that's just below the middle.
> On "Many" two GREY ghost ellipses (touch heights ±0.5 s_y, 40 % opacity) appear inside the box; the
> box is Indicated on "walls". On "picks one" the ghosts fade, the YELLOW ellipse is drawn and a copy
> of −0.06 becomes the touch dot on the right wall (its mirror on the left). On "Correlation r
> means" the ellipse becomes a "what if": the dinosaur fades out, the data's r row and the counter
> dim to 35 %, a live "r = …" label appears and r goes to 0 (the touch point level with the
> centre). On "one standard deviation to the right" a thin YELLOW run is drawn from the centre to
> the right wall, labelled s_x; on "on average r standard deviations up" r sweeps 0 → 0.80 and the
> YELLOW rise grows from the run's end to the touch dot. The touch dot is flagged on "touch point";
> "r s_y" is written by the rise on "r times s y". On "minus point oh six" it sweeps back to −0.06,
> the r row returns and is Indicated; the touch dot flags on "middle". (The same run and rise come
> back as the slope at 3:00.)

**B10.** That ellipse is everything the five numbers know.
> Run, rise and labels fade; ellipse pulsed; the dinosaur returns at full opacity around it.

**B11.** Now replay version one, and watch the ellipse.
> Points slide to the star again. A RED centre/box/ellipse, computed live, drifts off the YELLOW one.

**B12.** How would you fix the star? [pause 1.5]
> Both boxes dim to 30 % so the two ellipses and centres carry the prediction hold.

**B13.** Slide it until the centers meet. Stretch it until the boxes match. Then tip it, a slight
shear, until it touches the walls at the same height.
> Translate (x̄, ȳ go green), scale about the centre (s_x, s_y go green; the boxes return to full
> opacity on "Stretch"), shear (r goes green).

**B14.** All five match now, to every decimal place.

### Limit + payoff (1:52–3:22)
**B15.** But add a sixth number, the median of y, and our star misses it by six.

**B16.** In 2017, Justin Matejka and George Fitzmaurice built a search that holds whatever numbers
you choose. They chose these five.
> Citation: "Matejka & Fitzmaurice, 2017 · CHI". The readout goes live again (median row included);
> the YELLOW geometry is recomputed from the points every frame. Our star returns to the dinosaur.

**B17.** Nudge a point at random, biased toward a target shape, and keep the nudge only if the five
numbers still hold to two decimals. Repeat it enough times, and the dinosaur becomes a circle.
> On "Nudge" one tail point is ringed in white and the grey dashed target circle is drawn. On
> "biased toward" the ringed point steps 5.5 units toward the nearest point of the circle (inward):
> x̄ and s_x in the live column turn RED ≠ (facts.md #27). On "keep the nudge only if" the step is
> undone (rejected) and the column returns to =; on "five numbers" the column and the ellipse are
> Indicated and the ring leaves. On "Repeat" the points set off one by one into the real `circle`
> dataset; the five = marks never change, the median wanders.

**B18.** From the dinosaur they grew twelve shapes, like this star, [pause 1.3] this bullseye,
[pause 1.0] this X, [pause 1.2] these stripes, [pause 0.9] and these dots. Every one of them has
this same ellipse, and a different median.
> Each real dataset lands 0.25 s before its name (0.6 s moves) and holds about 1.5 s. The YELLOW
> ellipse, box and touch dots never visibly move; the median jumps 50.11, 47.38, 39.87, 50.47, 51.29
> (all ≠ 46.02). Varied pauses so the roll call is not metronomic.

**B19.** Francis Anscombe made the point in 1973, with eleven points of his own.
> The dinosaur's values leave; citations swap. 11 of the points travel to Anscombe's dataset I (BLUE)
> while the rest fade with the old axes; the YELLOW geometry morphs into Anscombe's (axes x 3–15,
> y 3.5–11.5). On "points" they are flagged while the five symbols glide into Anscombe's readout,
> which now lands mid-right with r first, level with his touch point: "r = 0.82  s_x = 3.32
> s_y = 2.03" / "x̄ = 9.00  ȳ = 7.50" (YELLOW values fade in).

**B20.** His correlation is point eight two, so the ellipse touches the right wall high up.
> "r = 0.82" flagged; on "touches" a copy of it travels straight left into the touch dot.

**B21.** Least squares sets the slope of the best-fit line to the covariance over the x variance.
[pause 0.8] The covariance is r times s x times s y, [pause 1.0] so one s x cancels.
> On "Least squares" the readout steps down to the bottom right (making room). "slope =", then
> cov(x,y) over s_x², each on its word. On "The covariance is" a side line "cov(x,y) = r s_x s_y"
> is built under the fraction: cov(x,y) copied from the numerator, then r, s_x and s_y each
> Indicated in the readout and flown up on its spoken word. The side line's right side is then
> carried up round the right of the fraction (never through it) into the numerator while cov(x,y)
> fades; it is flagged and the rest of the side line fades. On
> "cancels" the s_x and the exponent are struck through and the fraction becomes r s_y / s_x.

**B22.** What's left is the rise to the touch point over the run to the wall. [pause 0.2] So the line runs
through the center and that touch point. Plug in his numbers, and the slope is one half.
> As before: numerator onto the rise, denominator onto the run, best-fit line grown from the centre
> through the touch point, substitution 0.82 × 2.03 / 3.32 ≈ 0.50 built from the readout.

**B23.** All four of his datasets share these five numbers, so they share the ellipse and the line.
[pause 0.3] A trend, a curve, an outlier, and one point doing all the work.
> Box round the readout on "these five numbers". Panel I forms: the zoomed axes fade out first,
> then panel I's axes and panels II–IV fade in (no double tick labels); the readout steps down
> under panels III–IV, ≥ 0.45 below the labels. Copies of the ellipse, then of the line, arc over
> the panel row to panels IV, III, II (farthest first, so no two copies overlap in flight). The four
> labels sit on one baseline; the outlier and the lever point get a white ring.

### Landing (3:23–3:39)
**B24.** Your line was exactly right: five numbers fix it. Your cloud was this ellipse, all that
five numbers can draw. [pause 0.6] Most of those papers used a bar graph, which draws only two.
[pause 0.6] The dinosaur lived in everything they leave out.
> Before the line (a 1.2 s hand-off at the beat boundary): the quartet fades out while panel I's
> ellipse grows back to the dinosaur scale; then the opening frame fades in around it (axes, YELLOW readout, grey guess cloud, "your guess",
> the dashed "your line"). The dashed line is Indicated on "exactly right"; on "five numbers fix
> it" the five values flag and the YELLOW best-fit line grows over it. On "this ellipse" it is
> pulsed; on "all that" the guess labels and dashed line leave and the ellipse and line pulse. On
> "Most of those papers" the Weissgerber citation and a grey "86% used bars" return; on "bar
> graph" a copy of the ellipse is squeezed to its vertical extent, which is exactly the ±s_y error
> bar, as the ȳ bar grows under it; the ȳ and s_y rows flag on "two". On "dinosaur" the bar dims
> and the cloud's points return to the dinosaur, BLUE, around the ellipse, line and bar. End card.

## Sources
- Matejka, J. & Fitzmaurice, G. (2017). Same Stats, Different Graphs: Generating Datasets with
  Varied Appearance and Identical Statistics through Simulated Annealing. CHI 2017, pp. 1290–1294.
  doi:10.1145/3025453.3025912. Data: datasauRus R package (CRAN), DatasaurusDozen.tsv.
- Cairo, A. (2016). The Datasaurus (The Functional Art blog); redrawn with DrawMyData for the
  paper (Matejka & Fitzmaurice, acknowledgements).
- Weissgerber, T. L., Milic, N. M., Winham, S. J. & Garovic, V. D. (2015). Beyond Bar and Line
  Graphs: Time for a New Data Presentation Paradigm. PLoS Biology 13(4): e1002128.
  doi:10.1371/journal.pbio.1002128.
- Anscombe, F. J. (1973). Graphs in Statistical Analysis. The American Statistician 27(1):17–21.
  doi:10.1080/00031305.1973.10478966.
