# Episode 1 — Three Right Answers to One Probability Question

**Idea (one sentence):** "Pick a chord at random" has no answer until you say what is spread evenly; Bertrand's chord gets 1/3, 1/2 or 1/4 because each recipe scatters chord midpoints differently around the one small circle that decides "long".

**Runtime target:** ~3:52 at ~155 wpm (≈ 590 words).

## Palette (colour → one meaning, whole episode)

| colour | meaning |
|---|---|
| YELLOW ("gold") | **long**: a chord longer than the triangle's side, and every region that makes a chord long (far arc, inner half of the radius, the triangle's inscribed circle, midpoints inside it) |
| BLUE | recipe 1, **random endpoints** (spread evenly over the rim): its label, tally, rim, answer |
| GREEN | recipe 2, **random radius point** (spread evenly along a radius) |
| PURPLE | recipe 3, **random midpoint** (spread evenly over the area) |
| INK | the circle, the triangle, the chord or midpoint being followed, text |
| GRAY / DIM | short chords, axes, citations; dimmed context, straws; the class-size bars and the "random class" line (neutral: they are not a chord recipe) |

Red is not used. Recipe colours never encode "right" or "wrong".

## Beats

### Cold open (0:00–0:12)
Circle and inscribed triangle are on screen in the first frame. A chord draws; a triangle side flashes; the question builds as math from copies of the two segments: P(chord > side) = ?

> Draw a chord across this circle at random. What's the chance it comes out longer than a side of this triangle? Pick a number. *[pause 1.5]*

### Stakes (0:12–0:24)
Citation bottom-left. The words "at random" appear under the question and are underlined.

> Joseph Bertrand published this puzzle in eighteen eighty-nine, as a warning about two words: at random. Every survey and every simulation has to decide what they mean.

### Naive build (0:24–1:00)
Recipe 1 on the big circle: two rim dots, a chord, gold if longer than the side. Then the rain: 10,000 simulated chords accumulate as a texture while a live tally converges (0.334) and a counter climbs.

> Start with the obvious simulation. Pick two points on the rim at random, and join them. If the chord beats the triangle's side, it turns gold.

> Run ten thousand chords, and the gold share settles near point three three.

The texture dims. The triangle rotates so a vertex sits on the first point; the second point sweeps the rim; the chord is gold only on the far arc, which lights up gold. A copy of the gold arc lifts off the rim and flies straight into "120°" (0.85 s), then a copy of the whole rim flies into "360°", then "= 1/3". The equation and the arc hold, unchanged, for ≈ 3.3 s (through "Case closed").

> Geometry agrees. Put a corner of the triangle on the first point. The chord is long only when the second point lands on this far arc, a third of the rim. *[pause 1.2]*

### Fail (0:45–1:23)
On "a second way" the sweep, the arc and the question fade (0.5 s); then the big circle shrinks into the left panel (its settled rain dimmed to 30 %) while its label, its tally and the exact 1/3 from the arc equation travel with it in the same move; the ≈ appears once they have landed. A "gold share" number line appears underneath: the blue tally drops a dot onto it. Panel 2 builds its recipe (random radius, random point on it, perpendicular chord), rains, settles at 0.498 and dims. Panel 3 (random point inside = midpoint) settles at 0.248 and drops a purple dot. Bertrand's verdict appears in French as two lines, on "wrong" and "right", while the recipe labels dim. Each dot grows its 95 % error bar (about ±0.01); a brace measures the gap: "25 points".

> Case closed, until you code it a second way. Pick a random radius, a random point along it, and draw the chord through that point at right angles.

> Same circle, same gold rule. This one settles near point five.

> A third program picks a random point anywhere inside, and makes it the chord's midpoint. That settles near point two five.

> Bertrand printed all three, and wrote that none is wrong, and none is right. Each tally is good to about one percentage point. They disagree by twenty-five percentage points, and none of the code has a bug.

### Insight (1:23–2:23)
The number line, error bars and brace fade first; then panel 2 enlarges as an ink-only "any chord" circle (its label, tally and rain fade; the other panels dim). One chord with its midpoint: the midpoint slides down a radius, the chord shrinks; at half the radius it matches the triangle's side; the triangle's inscribed circle draws in gold. The midpoint wanders: gold inside, grey outside.

> One point sets a chord's length: its midpoint. Slide it outward and the chord shrinks. It matches the triangle's side when the midpoint is half a radius out, on the circle that fits inside the triangle.

(Round 3: the chord draws on "length", its midpoint on "midpoint"; the slide starts on "Slide".)

> So a chord is long exactly when its midpoint lands inside this gold circle. Each program is really asking what share of midpoints land here.

Panel 2 shrinks back; only once it has landed do its label and tally return, and the gold circle copies into all three panels. Panel 3's chords collapse to their midpoints (even spread) and its histogram grows, captioned right above it. In the tally row, π(r/2)² over πr² is built from the two disks' outlines flying straight down into the terms; the ≈ arrives with them (never a dangling "0.248 ≈"), then = 1/4.

> Shrink every chord to its midpoint. The midpoint program spreads them evenly, so this circle, with a quarter of the area, catches a quarter of them.

Prediction pause, then panel 2 collapses: midpoints crowd the centre; its flat histogram grows and the caption moves to the middle of the row. The innermost disk and the outer ring flash with their equal bars; (r/2)/r builds in the tally row from the two halves of a radius → 1/2, and stays up through the next beat.

> The radius program spreads them evenly along the radius. Where will they crowd? *[pause 1.5]* Toward the center: every ring gets an equal share, and inner rings are small. Half the radius, so one half.

Panel 1 collapses: midpoints pile against the rim (tall last bar). On "rim" the panel's outer ring (0.9r–r) and the last histogram bar (0.284) light up blue together for 1 s, so the claim is read off the measured bar. Copies of its five gold bars stack into a separate column just left of the axis origin (no tick), labelled 0.334, while the originals stay in place dimmed to 35 %, so the histogram still shows the rim pile-up; the 1/3 flags.

> And the endpoints program piles them against the rim, so only a third land inside, the third we found.

The 1/2 folds into the green tally. The histograms dim to context on "spread evenly"; each panel's evenly-spread thing then lights in its colour on its word: rim (blue), a fresh thick radius (green), area (purple). On "never said which" the three recipe labels flag.

> Three programs, three things spread evenly: rim, radius, area. At random never said which. *[pause 1.0]*

(The flagged labels hold still through the pause; the panels clear after it.)

### Payoff (2:23–3:20)
Panels clear; one circle remains and becomes the big circle on a "floor". The scoreboard ("gold share", a big-circle icon, the "straws" row label at 40 % with a dash) and the Jaynes citation are there from the first frame; the scoreboard's label column starts 0.7 units right of the floor box. Simulated straws fall across the floor as plain lines (not judged: their answer is what we want to know), and the straws row's dash becomes "?". On "where the circle sits or how big it is" a copy of the circle shrinks and slides to a smaller, off-centre spot inside it; the row becomes "straws ? = ?": unknown, but the same on both.

> In nineteen seventy-three, Edwin Jaynes said a physical process picks one: straws tossed from a standing height can't be aimed, so the answer can't depend on where the circle sits or how big it is.

The test. First the premise: the other straws dim and one straw is followed; on "both circles" dots mark where it crosses each rim (two on the big circle, two on the small one). Then the straws fade and the three program rows appear with "–" in both cells (labels "midpoint / endpoints / radius", the names the narration uses). On "honest program" one line of the midpoint program is shown judged twice: its chord of the big circle (grey: short there), then the piece of the same line inside the small circle (gold: long there). Then the rains: each program's chords rain on the big circle (subdued) and are judged on the small one (70 % opacity, under the small circle's own gold rule drawn on a dark halo); a row's dashes become live numbers only when its rain starts. The straws' "? = ?" flags on "the same on both" (invariance is the criterion; no simulated straw share is the target). The big triangle leaves and the big incircle dims to 20 %. The scoreboard fills row by row, with a breath after each row: midpoint 0.25 ≠ 0.41, endpoints 0.33 ≠ 0.47, radius 0.50 = 0.50. On "on both" the failed rows dim to 30 %, the program chords clear, and the radius row's "=" flags with the straws' "? = ?". The finished board holds ≈ 2.3 s.

> One rain lands on both circles at once, so an honest program must score the same on both. Midpoint gives a quarter, then point four one. *[pause 0.75]* Endpoints give a third, then point four seven. *[pause 0.75]* Only the radius program gives a half on both. *[pause 1.0]*

The small circle, its column and the failed rows leave first (0.6 s); only then do the straws return on the one circle while the radius row moves up under the straws row ("straws ?"). On "tossed", the simulation dims to 30 % so the real experiment reads as separate; "5-inch circle" and "128 straws crossed it" appear on their words; the green radius row flags on "radius program's": the real tosses answer the "?".

> Jaynes and Charles Tyler tossed real broom straws at a five-inch circle, and the hundred and twenty-eight that crossed it matched the radius program's spread of chord lengths.

The real labels and the radius row dim; the simulation returns, now judged (gold/grey chords), and the straws row's "?" becomes that simulation's live share with an extra "simulated" tag; the straws are pulled toward the centre (a skilled tosser) and the share climbs to 1.00, held through a 0.8 s pause.

> A skilled tosser, Jaynes noted, could produce other answers. *[pause 0.8]*

### The same two words in survey data (3:20–3:43)
The floor cross-fades straight into the stakes beat's italic, underlined "at random" (written on "two words", no empty frame between), with the Feld & Grofman citation. On "Take classes" the chart title "class size (students)" and a grey italic "example" tag fade in and "at random" steps back to a 70 % caption above the title, right-aligned to the chart; it flags on each spoken "at random" and leaves when the real data arrive. The baseline draws with the first bar (no empty-baseline hold). Three bars: classes of 10, 10 and 100. "Pick a class at random": one dot per class appears under each equal-width bar, and a dashed "random class 40" line draws. "Pick a student at random": each class dot splits into its students (10, 10 and 100 dots, five rows under each bar), every bar widens to the width of its students ("width = students" appears under the dots), and a solid line rises continuously from 40 to "random student 85" (the width-weighted mean). These dots are the same picture as the chord midpoints: what is spread evenly decides the average. On "Stony Brook" the example dims to 30 % (its line labels and their numbers 40 and 85 leave, so the only bright numbers are Stony Brook's) and a separate framed block appears on the right: "Stony Brook, 1974 · 737 classes", then "- - - random class 40" on "forty" and "—— random student 147" on "forty-seven" (line glyphs match the example's two lines). A 0.6 s pause holds the finished frame ≈ 2.5 s.

> Surveys hide the same two words. Take classes of ten, ten and a hundred. Pick a class at random, and the average size is forty. Pick a student at random, and it's eighty-five. At Stony Brook in nineteen seventy-four, that was forty for a random class, and a hundred forty-seven for a random student. *[pause 0.6]*

### Landing (3:43–3:55)
Everything fades except Stony Brook's two rows, which step down (dimmed to 35 %) into their own rows left-aligned with the question, ≥ 0.6 below the lowest label of the number line. Back to the first frame: the same circle, triangle, opening chord and question P(chord > side) = ?. The 0–1 line (ticks only at its ends) is drawn first; a marker sweeps it, and 1/4, 1/3 and 1/2 appear in their colours as it passes them. The opening chord turns gold and shows its midpoint inside the gold circle (outline first, fill on "Name"). On "Name the way" a "straws" tag appears beside the green 1/2, which flags; on "only one is" 1/4 and 1/3 dim. On "Forty" the Stony Brook rows brighten; their numbers flag on "both right" and their labels ("random class", "random student") on "who's picked". The frame holds ≈ 1.4 s; no end card.

> So whatever number you picked, some way of drawing chords makes it right. Name the way, and only one is. Forty and a hundred forty-seven are both right, once you say who's picked.

## Sources (on screen)
- Bertrand, 1889 · *Calcul des probabilités* (Gauthier-Villars), ch. I §5 — the three answers and « Aucune des trois n'est fausse, aucune n'est exacte » (the sentence ends "la question est mal posée").
- Jaynes, 1973 · *Foundations of Physics* 3(4):477–492 — invariance argument, straw experiment with C. E. Tyler (128 successful tosses, 5-inch circle).
- Feld & Grofman, 1977 · *Research in Higher Education* 6(3):215–222 — the class size paradox; Stony Brook, spring 1974: 737 classes, mean 40 (40.5), experienced by students 147.
- Simulations: `sim.py` (seeded), labelled "simulated" on screen. See `facts.md`.
