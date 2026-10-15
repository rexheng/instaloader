# 36 · Turning Barely-Better-Than-Chance Rules Into an Expert

**One idea:** boosting reweights the points so that the last rule becomes exactly a coin flip; that forces every new weak rule to look somewhere new, and their weighted vote becomes accurate.

## Palette (colour -> one meaning, whole episode)
| Colour | Meaning |
|---|---|
| BLUE (circles) | class "inside": points inside the hidden circle, and regions the vote/cut calls inside |
| PURPLE (squares) | class "outside": points outside, and regions called outside |
| RED | wrong: a misclassified point (ring), the mistakes' share of weight, epsilon, the error region |
| GREEN | right: the count of points classified correctly, the correct share of weight |
| YELLOW | the current cut and its vote weight alpha |
| INK / GRAY / DIM | text / axes, old cuts, secondary labels / dimmed context |

Points never differ by colour alone: blue = circle, purple = square; red/green pairs always carry the words "wrong"/"right".

## Beats (narration, spoken form) and visuals

**1 · Cold open (0:00)** — 40 points pop in, a yellow vertical cut sweeps the square while a green counter tracks how many it gets right and settles at 26/40.
> These forty points come in two colors, blue and purple. Our only tool is one straight cut, and the best single cut gets twenty six of them right. Guessing would get about twenty.

**2 · Prediction (≈0:11)** — "100 cuts vote: ? / 40" in yellow under the counter. Hold.
> So if a hundred cuts vote together, how many of the forty can they get right? Pick a number. [pause 1.5]

**3 · Stakes** — "barely beats guessing → as accurate as you like" beside the plot. Citation Kearns & Valiant 1988–89.
> In nineteen eighty eight, Michael Kearns and Leslie Valiant posed this in general: whether rules that barely beat guessing can be combined into one that is as accurate as you like.

**4 · Naive build (bagging)** — first cut dims; 100 grey cuts drop in, each from a resample.
> The obvious try is called bagging. Train each cut on a different random resample of the points, then let a hundred cuts take a majority vote.

**5 · Fail, measured** — counter falls 26 → 23; red rings on the vote's 17 mistakes; the five crowded cut positions brighten.
> The vote gets twenty three right, fewer than one cut alone. The cuts pile up in the same few places, so they make the same mistakes.

**6 · Fix** — bagging cleared. First cut back in yellow; red rings on its 14 mistakes; a weight bar is built from the points: red "wrong" 0.35, green "right" 0.65. Mistakes swell, the rest shrink; the bar follows.
> So change what each new cut is graded on. Here are the first cut's fourteen mistakes. Make them heavier, and make the points it got right lighter.

**7 · The rule** — swelling completes; bar reads 0.50 / 0.50. Citation Freund & Schapire 1997.
> AdaBoost, published in nineteen ninety seven, says how far to go. Stop when the mistakes weigh exactly as much as everything else.

**8 · Formula from the bar** — sizes rewind to equal; equation built from the bar's numbers: 0.35·e^α = 0.65·e^−α, while sizes replay the multiplication.
> The mistakes started with point three five of the weight. Call that epsilon. The rest held point six five. Multiply the mistakes by e to the alpha, the rest by e to the minus alpha, and set the two piles equal.

**9 · Solve** — TransformMatchingTex: e^2α = 0.65/0.35 → α = ½ ln(0.65/0.35) ≈ 0.31 → general α = ½ ln((1−ε)/ε).
> Solve, and alpha is one half the log of point six five over point three five, about point three one. In general, one half the log of one minus epsilon, over epsilon.

**10 · Why equal (prediction pause 2)** — bar's 0.50/0.50 flagged; first cut greys.
> Equal is the whole trick. On the new weights, the first cut is exactly a coin flip, so the search cannot choose it again. Where would you put the next one? [pause 1.2]

**11 · Cut 2 + alpha's second job** — cut 2 drops at x = 5.79; heavy purple points on the right flagged. Panel becomes the curve α(ε), dots for cut 1 and cut 2, a dot slides to low error (loud) and to 0.5 (silent).
> It lands here, splitting off the heavy purple points on the right. And alpha has a second job. It is each cut's say in the vote. Lower error, louder vote. A coin flip gets no say at all.

**12 · Iterate, measured** — rounds 2→100 run: cut jumps, point sizes breathe, the vote's blue/purple map fills in, counter 26 → 34 (round 10) → 40 (round 66 onward). "? / 40" becomes "40 / 40".
> Now repeat. Reweight, cut, add the cut to the vote. By round ten, thirty four right. Past round sixty six, all forty, and it stays there. So a hundred weak cuts get every point.

**13 · Payoff** — plot shrinks left; a 24×24 window with an eye band (dark) over a cheek band (light); a brightness-difference axis gets a yellow threshold cut, copied from our cut. Citation Viola & Jones 2001 · CVPR.
> In two thousand one, Paul Viola and Michael Jones did this with faces. Each weak rule compared the brightness of neighbouring rectangles in a small window, then cut at one threshold, just like ours.

**14 · Payoff numbers** — 180,000 → 200; tiles "95% faces found" and "1 false alarm per 14,084 windows".
> AdaBoost chose two hundred such rules from over a hundred and eighty thousand. Together they found ninety five percent of faces, with one false alarm per fourteen thousand windows.

**15 · Honest limit 1** — plot returns; dashed true circle drawn; red error region where the blocky vote disagrees; fresh-point accuracy 78% vs one cut 61%.
> Boosting fits the labels it is given. On five thousand fresh points from our simulation, the vote scores seventy eight percent, up from sixty one for one cut. Its blocky edge only roughly traces the true circle.

**16 · Honest limit 2** — one point inside the circle is relabelled purple ("mislabelled"); its size tracks its simulated weight over 100 rounds, peaking at about 3× average. Citation Dietterich 2000.
> And because mistakes keep gaining weight, wrong labels get chased. On data with noisy labels, Thomas Dietterich found in two thousand that bagging beat boosting.

**17 · Landing** — everything returns to the opening frame: equal points, the first cut, 26 / 40. On the last sentence the points swell to the round-100 weights (the hard points).
> Look at the first cut again. Still twenty six out of forty. No cut in the vote ever got smarter. Each one was handed a harder question.

## Sources
- Kearns & Valiant 1988 (Harvard tech. report) / 1989 (STOC), as cited in Schapire 1990, *Machine Learning* 5:197–227.
- Freund & Schapire 1997, *J. Computer and System Sciences* 55(1):119–139.
- Viola & Jones 2001, CVPR, "Rapid Object Detection using a Boosted Cascade of Simple Features".
- Dietterich 2000, *Machine Learning* 40:139–157.
- Simulation: `sim.py` (seeded). See facts.md.
