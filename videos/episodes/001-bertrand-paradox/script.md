# Episode 1 — Three Right Answers to One Probability Question

**Idea (one sentence):** "Pick a chord at random" has no answer until you say what is spread evenly; Bertrand's chord gets 1/3, 1/2 or 1/4 because each recipe scatters chord midpoints differently around the one small circle that decides "long".

**Runtime target:** 3:15–3:35, ≤ 500 words (PRODUCTION_GUIDE §13); narrator speed 0.83, `CADENCE = "shaped"`.

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

> Draw a chord across this circle, at random. What's the chance it's longer than a side of this triangle? Pick a number. *[pause 1.5]*

### Stakes (0:12–0:24)
Citation bottom-left. The words "at random" appear under the question and are underlined; they flag on "vague". Then the stakes in the payoff's own numbers: "average class" and, on their words, "40", "or 147" (dimmed grey label, ink numbers). They leave with "at random" when the simulation starts.

> Bertrand posed this puzzle in eighteen eighty-nine, as a warning about two words: at random. Leave them vague, and one college's average class is forty, or a hundred forty-seven.

### Naive build (0:24–1:00)
Recipe 1 on the big circle: two rim dots, a chord, gold if longer than the side. Then the rain: 10,000 simulated chords accumulate as a texture while a live tally converges (0.334) and a counter climbs.

> Start with the obvious simulation: two random points on the rim, joined. If the chord beats the triangle's side, it turns gold.

> Ten thousand chords in, the gold share settles near point three three.

The texture dims. The triangle rotates so a vertex sits on the first point; the second point sweeps the rim; the chord is gold only on the far arc, which lights up gold. A copy of the gold arc lifts off the rim and flies straight into "120°" (0.85 s), then a copy of the whole rim flies into "360°", then "= 1/3". The equation and the arc hold, unchanged, for ≈ 3.3 s (through "Case closed").

> Geometry agrees. With a corner on the first point, the chord is long only when its other end lands on this arc, a third of the rim. *[pause 1.0]*

### Fail (0:45–1:23)
On "a second way" the sweep, the arc, the question and "120°/360° =" fade in place while the triangle turns back upright (0.6 s, before anything moves); then the big circle shrinks into the left panel (its settled rain dimmed to 30 %) while its label, its tally and the exact 1/3 from the arc equation travel with it in the same move, and in the second half of that move the shared number line and panel 2's circle start drawing (so the frame is never one small panel in a corner); the ≈ appears once they have landed. A "gold share" number line appears underneath, captioned under its title "10,000 simulated chords each" (round 6: moved there from mid-frame, where the green and purple dots flew through it): the blue tally drops a dot onto it. Panel 2 builds its recipe (random radius, random point on it, perpendicular chord), rains, settles at 0.498 and dims. Panel 3 (random point inside = midpoint) settles at 0.248 and drops a purple dot. Bertrand's verdict appears in French on one line, centred under all three tallies (Text 26 italic, its two halves on "wrong" and "right"; round 6: the panel group sits 0.2 higher and the number line 0.08 lower, so the quote has ≥ 0.35 clearance above and below), while the recipe labels dim. Each dot grows its 95 % error bar (about ±0.01); a flat brace measures the gap, its label "25 points" sitting right on it while the three tallies step back to 35 % (they come back on "none of the code").

> Case closed, until you code it a second way: a random radius, a point on it, and the chord through it at right angles.

> This one settles near point five.

> A third program picks any point inside as the chord's midpoint. That settles near point two five.

> Bertrand printed all three, writing that none is wrong, none is right. Each tally is good to about one percentage point. They disagree by twenty-five, and the code has no bug. *[pause 0.8]*

(Round 7: the number line, error bars, brace and "25 points" fade on that pause, so the insight opens on a clean breath.)

### Insight (1:23–2:23)
The number line, error bars and brace fade first; then panel 2 enlarges as an ink-only "any chord" circle (its label, tally and rain fade; the other panels dim). One chord with its midpoint: the midpoint slides down a radius, the chord shrinks; at half the radius it matches the triangle's side; the triangle's inscribed circle draws in gold. The midpoint wanders: gold inside, grey outside.

> One point sets a chord's length: its midpoint. Slide it outward and the chord shrinks. It matches the side at half a radius, on the circle inside the triangle.

(Round 3: the chord draws on "length", its midpoint on "midpoint"; the slide starts on "Slide".)

> So a chord is long exactly when its midpoint lands in this gold circle. Each program is a way of scattering midpoints.

(The gold circle fills on "this gold circle"; on "each program" panel 2 shrinks back and the gold circle copies into all three panels.)

Panel 2 shrinks back; only once it has landed do its label and tally return, and the gold circle copies into all three panels. Panel 3's chords collapse to their midpoints (even spread) and its histogram grows, captioned right above it ("midpoints / by distance from center"; round 7: "share of" dropped, so the frame stays at 12 words). On "this circle" the gold disk itself lights up (fill 0.14 → 0.5 → 0.14). In the tally row, π(r/2)² over πr² is built from the two disks' outlines flying straight down into the terms, each on its own word: the gold outline on "quarter", the purple rim on "area"; the ≈ arrives with the first (never a dangling "0.248 ≈"), then = 1/4.

> Shrink every chord to its midpoint. The midpoint program fills the disk evenly, so this circle, a quarter of the area, catches a quarter.

Prediction pause: on "Where" panels 1 and 3 step back to 40 % and nothing moves but the viewer (round 7: the purple equation no longer folds here; it stays whole and folds with the green one on "Three programs"). On "Toward the center" panels 1 and 3 come back while panel 2 collapses: midpoints crowd the centre; its flat histogram grows and the caption moves to the middle of the row. The innermost disk and the outer ring flash with their equal bars; (r/2)/r builds in the tally row from the two halves of a radius → 1/2, and stays up through the next beat.

Every histogram carries a dashed 10 % reference line (the share each of ten bands gets if midpoints are spread evenly along the radius), with a "10%" tick left of the midpoint and radius histograms; the radius program's bars sit on it.

> The radius program spreads them evenly along the radius. Where will they crowd? *[pause 1.5]* Toward the center: every ring gets an equal share, and inner rings are small. Half the radius: one half.

Panel 1 collapses: midpoints pile against the rim (tall last bar). (Its histogram sits 0.25 right of the panel's centre so the stacked column stays inside the safe area.) On "rim" the panel's outer ring (0.9r–r) and the last histogram bar (0.284) light up blue together for 1 s, so the claim is read off the measured bar. Copies of its five gold bars stack into a separate column just left of the axis origin (no tick), labelled 0.334, while the originals stay in place dimmed to 35 %, so the histogram still shows the rim pile-up; meanwhile panels 2 and 3 (dots, equations, histograms, caption) step back to 35 % so the stack is the one focal point; the 1/3 flags. Panels 2 and 3 come back on "Three programs".

> The endpoints program piles them against the rim: only a third land inside, the third we found.

The 1/2 and the 1/4 fold into their tallies together, so the row reads 0.334 ≈ 1/3, 0.498 ≈ 1/2, 0.248 ≈ 1/4. The histograms dim to context on "spread evenly"; each panel's evenly-spread thing then lights in its colour on its word: rim (blue), a fresh thick radius (green), area (purple). On "never said which" the three recipe labels flag.

> Three programs, three things spread evenly: rim, radius, area. At random never said which. *[pause 0.9]*

(The flagged labels hold still through the pause; the panels clear after it.)

### Payoff (2:27–3:11)
Panels clear while the one remaining circle already travels onto the "floor" and becomes the big circle (one 1.4 s cross-dissolve: the right-hand panel clears in 0.3 s and the board's text is fully up by 0.7 s where it stood, so no frame holds only the travelling circle; the citation waits for the left histogram to go). The whole scoreboard is waiting from the first frame: "gold share", one-word column heads "big" and "small" (the second at 30 %; round 7: the two circles on the floor say "circle"), and all four rows ("straws / midpoint / endpoints / radius", the names the narration uses) at 30 % with "–" cells. Round 7: each program row carries its panel's glyph left of its name, the thing that program spreads evenly as lit on "rim, radius, area" (a blue rim, a green radius, a purple-filled disk), so a row maps to its panel by picture. The Jaynes citation is up. Simulated straws fall across the floor as plain lines (never judged: their answer is what we want to know) and the straws row lights. Round 7: 60 straws, only the newest three at full strength, each stepping back to 25 % within about 0.5 s of landing, so the texture stays light. Once the last straw has settled, the circle move: a copy of the big gold rule lies over it while the original and the big triangle fade (0.4 s, nothing moves yet); then the copy of the circle and its gold rule shrinks and slides to a smaller, off-centre spot inside it (the only gold circle on the floor at every moment), the "small" head lights, and the straws row's dashes become "? = ?": unknown, but the same on both. The small gold rule's dark halo is never morphed: it fades in at the destination (0.4 s) while the straws leave the floor.

> Edwin Jaynes argued a physical process picks one. Straws tossed from a standing height can't be aimed, so the answer can't depend on where the circle sits, or its size.

The test. The floor holds only the two circles. One line of the midpoint program is drawn across it on "One program's rain", and on "both circles" dots mark its four rim crossings. Round 7: on "circles" the big circle judges first: its gold circle comes in dashed at 60 % (the small gold circle steps back to 30 %), the line's big chord is drawn grey and labelled "short" (grey, Text 24, beside the chord outside the small circle), and this verdict holds at full strength ≈ 1.6 s; on "own" one 0.5 s cross-fade hands over (big gold out, small gold back to 100 %) and the piece inside the small circle is drawn gold, labelled "long" (gold, inside the small gold circle). Only one gold circle is ever at full strength. Both words stay up ≥ 1.9 s and leave with the line before the first rain; the straws' "? = ?" flags on "the same on both", followed by a 0.6 s pause. Then the rains, one per sentence: 36 lines of each program, its big-circle chords at 15 % and the pieces inside the small circle at full strength under the small gold circle (on a dark halo). A row and its glyph light and its dashes become live numbers when its rain starts; the numbers (all 100,000 lines) settle by the big-circle number word, each number flags on its word, and the relation sign arrives 0.2 s after the second (number, number, verdict). Each rain runs ≈ 2.7 s and each finished row holds ≈ 1.3 s with the floor clear before the next rain: midpoint 0.25 ≠ 0.41, endpoints 0.33 ≠ 0.47, radius 0.50 = 0.50. On "on both" the failed rows and glyphs dim to 30 % and the radius row's "=" flags with the straws' "? = ?".

> One program's rain lands on both circles. Each judges with its own gold circle, so a fair program scores the same on both. *[pause 0.6]* Midpoint: a quarter, then point four one. *[pause 1.0]* Endpoints: a third, then point four seven. *[pause 1.0]* Only the radius program gives a half on both. *[pause 0.9]*

Round 7, in sequence: the small circle, both column heads, the board's title and every program row (failed rows, the radius row and the glyphs) leave in 0.35 s, the small gold rule last; only then does the big circle's gold rule come back (0.35 s), so two gold circles never share the floor. The simulation leaves the floor entirely (the straws are already gone; the "simulated" tag and the floor's outline fade), and the straws row ("straws ?") moves down to head the right column, with the predicted histogram's empty axis (baseline, "center … r/2 … rim", the dashed 10 % line) waiting under it at 30 %. On "five-inch" a grey "5 in" dimension mark draws under the circle (Jaynes: "5-in.-diameter"); on "hundred twenty-eight" "128 straws crossed it" appears on the floor under that mark (round 7: "5-inch-wide circle" and the "radius 0.50" row are gone; they repeated the mark and the histogram). On "matched" the straws row's "?" is swapped (out, then in: no glyph morph) for "≈ radius": the real tosses answer it. On "radius" the waiting axis comes up to full and the radius program's predicted histogram grows on it: "radius program *predicted*", ten bands of exactly 10 % (gold inside r/2, grey outside) with the dashed 10 % line, the same picture as the insight's flat histogram; its axis ends are named in words, "center … r/2 … rim". It holds ≈ 1.7 s. The right column is three items: "straws ≈ radius", the histogram title, the histogram.

> Jaynes and Charles Tyler tossed real straws at a five-inch circle. The hundred twenty-eight that crossed it matched the radius program. *[pause 0.9]*

### The same two words in survey data (3:13–3:37)
Round 6 entrance: the floor's half of the frame (circle, gold rule, "5 in" mark, citation) clears in the last 0.25 s of the Tyler beat's breath, while the predicted histogram on the right is still up; on "Surveys" the right column fades (0.35 s) while the example chart draws in the centre from the first frame, its baseline and then its three bars (10, 10, 100), with its title "class size (students)" and a grey italic "example" tag (6 fps sweeps show no near-empty frame and nothing drawn over the old circle). At the same moment the stakes beat's promise "average class / 40 or 147" comes back on the right exactly where it was at 0:19–0:23, and italic "at random" is written straight into its slot under the chart; it is underlined on "two words", as at 0:16. The frame never empties and the chart is its one object from the first second. Each size label (10, 10, 100) arrives on its spoken number while its bar's outline flashes ink. The Feld & Grofman citation arrives after the Jaynes one has gone. "Pick a class at random": one dot per class appears under each equal-width bar and "at random" flags on its word (the promise on the right leaves), then gives way to what it means here, "spread evenly over: classes" (a swap: out, then in, never superimposed), while a dashed "random class 40" line draws and lands on "forty". "Pick a student instead": each class dot splits into its students (10, 10 and 100 dots, five rows under each bar), every bar widens to the width of its students, a solid line rises continuously from 40 to "random student 85" (the width-weighted mean), and the label's last word turns from "classes" to "students" on "student" (the narration no longer says the phrase; the label carries it). These dots are the same picture as the chord midpoints: what is spread evenly decides the average. On "Stony Brook" the example slides left and dims to 30 % (its labels and numbers leave, so the only bright numbers are Stony Brook's), then a separate framed block appears on the right: "Stony Brook, 1974 · 737 classes", then "- - - random class 40" on "forty" and "—— random student 147" on "forty-seven".

> Surveys hide the same two words. Take classes of ten, ten and a hundred. Pick a class at random: the average is forty. Pick a student instead, and it's eighty-five. At Stony Brook, the same two picks gave forty and a hundred forty-seven. *[pause 0.5]*

### Landing (3:37–3:50)
Everything fades except Stony Brook's two rows (round 7: the Stony Brook header and its rule are fully gone in 0.25 s, before the question appears where the header stood), which step down (dimmed to 35 %) into one block under the 0–1 line: labels start at the line's left end, numbers end at its right end. Back to the first frame: the same circle, triangle, opening chord and question P(chord > side) = ?. The 0–1 line (ticks only at its ends) is drawn first; a marker sweeps it, and 1/4, 1/3 and 1/2 appear in their colours as it passes them. The opening chord turns gold and shows its midpoint inside the gold circle (outline first, fill on "Name"). On "fixed" 1/4 and 1/3 dim. On "a half" the green 1/2 flags and takes a "straws" tag with a grey "unaimed" under it (round 7: Jaynes's condition, the honest limit of the half, on screen and in the narration). On "a hundred forty-seven" the 147 comes up to full ink, and on "random student" its label does too; the random class's 40 stays dimmed, like the other two chord answers (right for its own way, not the one named). The frame holds ≈ 1.0 s; no end card.

> Whatever number you picked, some way of drawing chords makes it right. Name the way, and the answer is fixed: a half for unaimed straws, a hundred forty-seven for a random student.

(Round 6: one closing sentence replaces "Name the way, and only one is. Both averages are right, once you say who's picked.", where "only one" followed by "both" sounded like a contradiction to both critics.)

## Audio notes
- "Jaynes": misaki's phonemes are /ʤˈAnz/, which is correct. Whisper spells the homophone "Janes" on every variant tested (including "E. T. Jaynes"). Cycle 2 removed "Jaynes said", where the /z/ merged into the /s/ and Whisper heard "Jane".

## Sources (on screen)
- Bertrand, 1889 · *Calcul des probabilités* (Gauthier-Villars), ch. I §5 — the three answers and « Aucune des trois n'est fausse, aucune n'est exacte » (the sentence ends "la question est mal posée").
- Jaynes, 1973 · *Foundations of Physics* 3(4):477–492 — invariance argument, straw experiment with C. E. Tyler (128 successful tosses, "5-in.-diameter circle"; on screen "5-inch-wide circle").
- Feld & Grofman, 1977 · *Research in Higher Education* 6(3):215–222 — the class size paradox; Stony Brook, spring 1974: 737 classes, mean 40 (40.5), experienced by students 147.
- Simulations: `sim.py` (seeded), labelled "simulated" on screen. See `facts.md`.
