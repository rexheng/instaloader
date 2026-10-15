# 037 · Separating the Inseparable by Adding a Dimension

**One idea:** a straight (flat) cut in a lifted space is a curve in the original one, and because the learner only ever uses dot products, a kernel computes those lifted dot products without building the lift.

Target runtime ≈ 3:20 · ≈ 500 words · narrator af_heart.

## Palette (colour → one meaning, whole episode)

| Colour | Meaning |
|---|---|
| PURPLE | class "in range": the points in the middle |
| BLUE | class "out of range": the ring |
| YELLOW | the cut the learner makes (line, sheet, circle, kernel) |
| GREEN | the added coordinate: height z = x² + y² |
| RED | mistakes (always a ring shape + the word "mistakes", never colour alone) |
| INK rings | points a cut is built from (nudged points, support vectors) |
| GRAY / DIM | axes, bowl wireframe, secondary labels |

All data in the stage is **simulated** (80 points, seed 7) and labelled so on screen.

## Beats

**1 · Cold open (0:00)** — top view: 40 purple points in a disk, 40 blue in a ring; a yellow line sweeps.
> Purple points in the middle, a ring of blue around them. You get one straight cut. Can it put all the purple on one side and all the blue on the other? [pause 1.5]

**2 · Stakes** — legend: "in range" / "out of range".
> It's the shape you get whenever normal means near the middle, like two lab readings that are fine near their usual values and a warning when either one strays. The simplest learners can only make straight cuts.

**3 · Naive build** — perceptron: counters "nudges", "mistakes"; a wrong point gets a red ring, the line moves toward it. Citation Rosenblatt 1958.
> Try one: Rosenblatt's perceptron, from nineteen fifty-eight. Start with a line. Find a point on the wrong side, and nudge the line toward it. Repeat until nothing is wrong.

**4 · Measured failure** — 5,000 nudges fast-forward as a haze of ghost lines; best line (22 wrong) with red rings; "best possible line: 21".
> Here, that never happens. After five thousand nudges, the line is still thrashing. Its best moment left twenty-two of eighty points wrong, and no straight line gets below twenty-one. The perceptron stops only at zero mistakes, so it never stops.

**5 · What would you try** — green radius to one blue point; z = x² + y² built from it.
> What would you try? [pause 1] The two colours differ in one thing a line can't see: distance from the centre. So give every point a third number, its squared distance, x squared plus y squared.

**6 · Lift** — camera tilts; points rise onto the bowl.
> Now use that number as a height. The purple points stay low. The blue ones climb the walls of a bowl.

**7 · Fix works** — 3-D perceptron, 8 nudges, mistakes 40 → 0; a sheet settles between the layers.
> Run the same perceptron on three numbers per point. Eight nudges, and zero mistakes. A flat sheet now slides between the layers.

**8 · Formula from the picture** — sheet levels at height c; z = c and z = x² + y² merge into x² + y² = c; the sheet–bowl curve drops to the floor as a circle.
> Any sheet between them works, so take a level one, at height c. The bowl is height equals x squared plus y squared. Set the two equal, and you get x squared plus y squared equals c. That's a circle, drawn by a flat cut.

**9 · Second failure: cost** — 16×16 pixel grid; ≈ 1.6 × 10¹³ coordinates.
> But I had to guess that extra number. A handwritten digit on a sixteen by sixteen grid has two hundred fifty-six pixels. Every product of up to seven pixels gives about sixteen trillion new numbers, for each image.

**10 · Dot products only** — the 8 nudged points ringed; sheet = ±φ(p₁) ± … ± φ(p₈); score needs only φ(pᵢ)·φ(q).
> Look at what the perceptron actually kept. Its sheet is a tally of the eight lifted points it nudged for, each added or subtracted. So scoring a new point needs only dot products with those eight.

**11 · Kernel** — two points a, b with green height sticks; φ(a)·φ(b) = a₁b₁ + a₂b₂ + z_a z_b = a·b + |a|²|b|² = K(a,b).
> And the dot product of two lifted points never needs the lift. It's the flat dot product, plus the product of the two heights, and each height is just a squared length. A shortcut like this is called a kernel.

**12 · Digits kernel** — K(a,b) = (a·b + 1)⁷; 256 multiplications vs 1.6 × 10¹³.
> For the digits, the kernel is a dot b, plus one, to the seventh power. Two hundred fifty-six multiplications stand in for sixteen trillion.

**13 · Payoff 1: SVM** — sheet moves to the widest-gap sheet; two gutter sheets; 4 support vectors ringed. Citation Boser, Guyon & Vapnik 1992 · COLT.
> In nineteen ninety-two, Boser, Guyon and Vapnik paired kernels with a better sheet: the one with the widest gap to its nearest points. Here, four points pin it down. They're the support vectors.

**14 · Payoff 2: digits** — bar chart of USPS test error: flat cut 12.0 %, degree-7 kernel 4.3 %, humans 2.5 %. Citation Cortes & Vapnik 1995 · Machine Learning.
> In nineteen ninety-five, Cortes and Vapnik ran it on US postal digits. A flat cut on raw pixels misread twelve percent. The seventh-degree kernel misread four point three percent. Human readers miss two point five.

**15 · Honest limit** — the "+1" and "7" in the kernel boxed as hand-chosen.
> Someone still has to choose the kernel. The guess moved from the coordinates into the dot product.

**16 · Landing** — camera returns to the opening top view; the sheet's edge is the circle around the purple points, gutters as a thin street.
> So, back to the one straight cut. In this flat picture it can't be done. One dimension up, it can, and seen from above, that straight cut is this circle.

## Sources
- Rosenblatt, F. (1958). The perceptron. *Psychological Review* 65(6), 386–408. doi:10.1037/h0042519
- Boser, B. E., Guyon, I. M., & Vapnik, V. N. (1992). A training algorithm for optimal margin classifiers. *COLT '92*, 144–152. doi:10.1145/130385.130401
- Cortes, C., & Vapnik, V. (1995). Support-vector networks. *Machine Learning* 20, 273–297. doi:10.1007/BF00994018 (Table 1, Table 2)
