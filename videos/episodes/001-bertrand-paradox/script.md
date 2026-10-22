# Episode 1 — Three Right Answers to One Probability Question

**Idea (one sentence):** "Pick a chord at random" has no answer until you say what is spread evenly; Bertrand's chord gets 1/3, 1/2 or 1/4 because each recipe scatters chord midpoints differently around the one small circle that decides "long".

**Runtime target:** ~3:45 at ~155 wpm (≈ 570 words).

## Palette (colour → one meaning, whole episode)

| colour | meaning |
|---|---|
| YELLOW ("gold") | **long**: a chord longer than the triangle's side, and every region that makes a chord long (far arc, inner half of the radius, the triangle's inscribed circle, midpoints inside it) |
| BLUE | recipe 1, **random endpoints** (spread evenly over the rim): its label, tally, rim, answer |
| GREEN | recipe 2, **random radius point** (spread evenly along a radius) |
| PURPLE | recipe 3, **random midpoint** (spread evenly over the area) |
| INK | the circle, the triangle, the chord or midpoint being followed, text, the dashed 10 % reference line on the histograms (60 %) |
| GRAY / DIM | short chords, axes, citations; dimmed context, straws; the class-size bars and the "random class" line (neutral: they are not a chord recipe) |

Red is not used. Recipe colours never encode "right" or "wrong".

## Beats

### Cold open (0:00–0:12)
Circle and inscribed triangle are on screen in the first frame. A chord draws; a triangle side flashes; the question builds as math from copies of the two segments: P(chord > side) = ?

> Draw a chord across this circle at random. What's the chance it comes out longer than a side of this triangle? Pick a number. *[pause 1.5]*

### Stakes (0:12–0:24)
Citation bottom-left. The words "at random" appear under the question and are underlined; they flag on "vague". Then the stakes in the payoff's own numbers: "average class" and, on their words, "40", "or 147" (dimmed grey label, ink numbers). They leave with "at random" when the simulation starts.

> Joseph Bertrand published this puzzle in eighteen eighty-nine, as a warning about two words: at random. Leave them vague, and one college can report an average class of forty, or a hundred forty-seven.

### Naive build (0:24–1:00)
Recipe 1 on the big circle: two rim dots, a chord, gold if longer than the side. Then the rain: 10,000 simulated chords accumulate as a texture while a live tally converges (0.334) and a counter climbs.

> Start with the obvious simulation. Pick two points on the rim at random, and join them. If the chord beats the triangle's side, it turns gold.

> Run ten thousand chords, and the gold share settles near point three three.

The texture dims. The triangle rotates so a vertex sits on the first point; the second point sweeps the rim; the chord is gold only on the far arc, which lights up gold. A copy of the gold arc lifts off the rim and flies straight into "120°" (0.85 s), then a copy of the whole rim flies into "360°", then "= 1/3". The equation and the arc hold, unchanged, for ≈ 3.3 s (through "Case closed").

> Geometry agrees. Put a corner of the triangle on the first point. The chord is long only when the second point lands on this far arc, a third of the rim. *[pause 1.0]*

### Fail (0:45–1:23)
On "a second way" the sweep, the arc, the question and "120°/360° =" fade in place while the triangle turns back upright (0.6 s, before anything moves); then the big circle shrinks into the left panel (its settled rain dimmed to 30 %) while its label, its tally and the exact 1/3 from the arc equation travel with it in the same move; the ≈ appears once they have landed. A "gold share" number line appears underneath: the blue tally drops a dot onto it. Panel 2 builds its recipe (random radius, random point on it, perpendicular chord), rains, settles at 0.498 and dims. Panel 3 (random point inside = midpoint) settles at 0.248 and drops a purple dot. Bertrand's verdict appears in French as two lines, on "wrong" and "right", while the recipe labels dim. Each dot grows its 95 % error bar (about ±0.01); a brace measures the gap: "25 points".

> Case closed, until you code it a second way. Pick a random radius, a random point along it, and draw the chord through that point at right angles.

> This one settles near point five.

> A third program picks a random point anywhere inside, and makes it the chord's midpoint. That settles near point two five.

> Bertrand printed all three, and wrote that none is wrong, and none is right. Each tally is good to about one percentage point. They disagree by twenty-five percentage points, and none of the code has a bug.

### Insight (1:23–2:23)
The number line, error bars and brace fade first; then panel 2 enlarges as an ink-only "any chord" circle (its label, tally and rain fade; the other panels dim). One chord with its midpoint: the midpoint slides down a radius, the chord shrinks; at half the radius it matches the triangle's side; the triangle's inscribed circle draws in gold. The midpoint wanders: gold inside, grey outside.

> One point sets a chord's length: its midpoint. Slide it outward and the chord shrinks. It matches the triangle's side when the midpoint is half a radius out, on the circle that fits inside the triangle.

(Round 3: the chord draws on "length", its midpoint on "midpoint"; the slide starts on "Slide".)

> So a chord is long exactly when its midpoint lands in this gold circle, and each program is just a way of scattering midpoints.

(The gold circle fills on "this gold circle"; on "each program" panel 2 shrinks back and the gold circle copies into all three panels.)

Panel 2 shrinks back; only once it has landed do its label and tally return, and the gold circle copies into all three panels. Panel 3's chords collapse to their midpoints (even spread) and its histogram grows, captioned right above it. In the tally row, π(r/2)² over πr² is built from the two disks' outlines flying straight down into the terms; the ≈ arrives with them (never a dangling "0.248 ≈"), then = 1/4.

> Shrink every chord to its midpoint. The midpoint program spreads them evenly, so this circle, with a quarter of the area, catches a quarter of them.

Prediction pause, then panel 2 collapses: midpoints crowd the centre; its flat histogram grows and the caption moves to the middle of the row. The innermost disk and the outer ring flash with their equal bars; (r/2)/r builds in the tally row from the two halves of a radius → 1/2, and stays up through the next beat.

Every histogram carries a dashed 10 % reference line (the share each of ten bands gets if midpoints are spread evenly along the radius), with a "10%" tick left of the midpoint and radius histograms; the radius program's bars sit on it.

> The radius program spreads them evenly along the radius. Where will they crowd? *[pause 1.3]* Toward the center: every ring gets an equal share, and inner rings are small. Half the radius, so one half.

Panel 1 collapses: midpoints pile against the rim (tall last bar). On "rim" the panel's outer ring (0.9r–r) and the last histogram bar (0.284) light up blue together for 1 s, so the claim is read off the measured bar. Copies of its five gold bars stack into a separate column just left of the axis origin (no tick), labelled 0.334, while the originals stay in place dimmed to 35 %, so the histogram still shows the rim pile-up; the 1/3 flags.

> And the endpoints program piles them against the rim, so only a third land inside, the third we found.

The 1/2 folds into the green tally. The histograms dim to context on "spread evenly"; each panel's evenly-spread thing then lights in its colour on its word: rim (blue), a fresh thick radius (green), area (purple). On "never said which" the three recipe labels flag.

> Three programs, three things spread evenly: rim, radius, area. At random never said which. *[pause 0.8]*

(The flagged labels hold still through the pause; the panels clear after it.)

### Payoff (2:27–3:11)
Panels clear; one circle remains and becomes the big circle on a "floor". The whole scoreboard is waiting from the first frame: "gold share", two text column heads "big / circle" and "small / circle" (the second at 30 %), and all four rows ("straws / midpoint / endpoints / radius", the names the narration uses) at 30 % with "–" cells. The Jaynes citation is up. Simulated straws fall across the floor as plain lines (never judged: their answer is what we want to know) and the straws row lights. On "where the circle sits or how big it is" a copy of the circle and its gold circle shrinks and slides to a smaller, off-centre spot inside it; at the same time the big triangle and the big gold circle fade to 0 (the small circle and its gold circle are the only gold pair inside the big one), the "small circle" head lights, and the straws row's dashes become "? = ?": unknown, but the same on both.

> Edwin Jaynes argued that a physical process picks one: straws tossed from a standing height can't be aimed, so the answer can't depend on where the circle sits or how big it is.

The test. The straws fade; one line of the midpoint program is drawn across the floor and on "both circles" dots mark its four rim crossings. On "each judges" the big circle's gold circle flashes in while the line's big chord is drawn grey (it misses: short there); on "own gold circle" the flash leaves and the piece inside the small circle is drawn gold through the small gold circle (long there). This demo holds ≈ 2.3 s; the straws' "? = ?" flags on "the same on both". Then the rains, one per sentence: 36 lines of each program, its big-circle chords at 15 % and the pieces inside the small circle at full strength under the small gold circle (on a dark halo). A row lights and its dashes become live numbers when its rain starts; the numbers (all 100,000 lines) settle by the big-circle number word, each number flags on its word, and the relation sign arrives with the second. Each rain runs ≈ 2.7 s and each finished row holds ≈ 1 s with the floor clear before the next rain: midpoint 0.25 ≠ 0.41, endpoints 0.33 ≠ 0.47, radius 0.50 = 0.50. On "on both" the failed rows dim to 30 % and the radius row's "=" flags with the straws' "? = ?".

> One rain lands on both circles at once, and each judges with its own gold circle, so a fair recipe must score the same on both. Midpoint gives a quarter, then point four one. *[pause 0.8]* Endpoints give a third, then point four seven. *[pause 0.8]* Only the radius program gives a half on both. *[pause 0.6]*

The small circle, its column head, the failed rows and the board's title leave first (0.6 s); the big circle gets its gold circle back, the simulated straws return only as dim context (30 %, with the floor and its "simulated" tag), and the radius row moves up under the straws row ("straws ?" / "radius 0.50"). "5-inch circle" and "128 straws crossed it" appear on their words. On "matched" the straws row's "?" becomes "≈ radius": the real tosses answer it. On "radius program's" the green row flags and, under the real-experiment lines, the radius program's predicted histogram grows: "radius program *predicted*", ten bands of exactly 10 % (gold inside r/2, grey outside) with the dashed 10 % line, the same picture as the insight's flat histogram. It holds ≈ 1.7 s.

> Jaynes and Charles Tyler tossed real broom straws at a five-inch circle, and the hundred and twenty-eight that crossed it matched the radius program's flat spread. *[pause 0.8]*

### The same two words in survey data (3:11–3:34)
The floor fades out while the stakes beat's italic, underlined "at random" is already being written (no empty frame), with the Feld & Grofman citation arriving after the Jaynes one has gone. The chart starts centred in the frame. On "Take classes" the chart title "class size (students)" and a grey italic "example" tag fade in and "at random" steps down into the slot under where the dots will be. The baseline draws with the first bar. Three bars: classes of 10, 10 and 100. "Pick a class at random": one dot per class appears under each equal-width bar and "at random" flags on its word, then gives way to what it means here, "spread evenly over: classes"; a dashed "random class 40" line draws. "Pick a student at random, spread evenly over students…": each class dot splits into its students (10, 10 and 100 dots, five rows under each bar), every bar widens to the width of its students, a solid line rises continuously from 40 to "random student 85" (the width-weighted mean), and the label's last word turns from "classes" to "students" as it is spoken. These dots are the same picture as the chord midpoints: what is spread evenly decides the average. On "Stony Brook" the example slides left and dims to 30 % (its labels and numbers leave, so the only bright numbers are Stony Brook's), then a separate framed block appears on the right: "Stony Brook, 1974 · 737 classes", then "- - - random class 40" on "forty" and "—— random student 147" on "forty-seven".

> Surveys hide the same two words. Take classes of ten, ten and a hundred. Pick a class at random, and the average size is forty. Pick a student at random, spread evenly over students instead of classes, and it's eighty-five. At Stony Brook in nineteen seventy-four, those two picks gave forty, and a hundred forty-seven. *[pause 0.5]*

### Landing (3:34–3:45)
Everything fades except Stony Brook's two rows, which step down (dimmed to 35 %) into one block under the 0–1 line: labels start at the line's left end, numbers end at its right end. Back to the first frame: the same circle, triangle, opening chord and question P(chord > side) = ?. The 0–1 line (ticks only at its ends) is drawn first; a marker sweeps it, and 1/4, 1/3 and 1/2 appear in their colours as it passes them. The opening chord turns gold and shows its midpoint inside the gold circle (outline first, fill on "Name"). On "Name the way" a "straws" tag appears beside the green 1/2, which flags; on "only one is" 1/4 and 1/3 dim. "40" brightens on "Forty", "147" on "forty-seven", and on "who's picked" both labels come up to the same ink (flagged by opacity, not scale). The frame holds ≈ 1.3 s; no end card.

> So whatever number you picked, some way of drawing chords makes it right. Name the way, and only one is. Forty and a hundred forty-seven are both right, once you say who's picked.

## Audio notes
- "Jaynes": misaki's phonemes are /ʤˈAnz/, which is correct. Whisper spells the homophone "Janes" on every variant tested (including "E. T. Jaynes"). Cycle 2 removed "Jaynes said", where the /z/ merged into the /s/ and Whisper heard "Jane".

## Sources (on screen)
- Bertrand, 1889 · *Calcul des probabilités* (Gauthier-Villars), ch. I §5 — the three answers and « Aucune des trois n'est fausse, aucune n'est exacte » (the sentence ends "la question est mal posée").
- Jaynes, 1973 · *Foundations of Physics* 3(4):477–492 — invariance argument, straw experiment with C. E. Tyler (128 successful tosses, 5-inch circle).
- Feld & Grofman, 1977 · *Research in Higher Education* 6(3):215–222 — the class size paradox; Stony Brook, spring 1974: 737 classes, mean 40 (40.5), experienced by students 147.
- Simulations: `sim.py` (seeded), labelled "simulated" on screen. See `facts.md`.
