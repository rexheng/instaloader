# Episode 3 — changelog

## Round 1 revisions

Round 1 review: craft 7.0 (caps: header overlap, "1 targets"), substance 6.0 (cap: on-screen
"0.39 × 576 ≈ 227"). Both said it reaches 9 if the general-k Poisson stretch is derived from the
picture and the real-data beat gets stronger. Runtime is now 3:52 (was 3:22): the extra time is
the derivation and the measured v2 verdict, and nothing old was padded.

**Caps removed**
- The on-screen product is now "0.3933 × 576 ≈ 227" (226.5), with the line above reading
  "≈ 0.3933" and the narration "point three nine three" (substance 1). The critic's proposed
  "0.393 × 576" would also be wrong (226.4), so four places are shown.
- `flag()` is now colour-only (Indicate with scale 1.0) for every flag in the episode, so no
  frame, bar or label grows into a neighbour. The closing B-frame flash is a stroke-colour
  pulse (craft 1).
- The live counter is a singular/plural label: "1 target" → "2 targets" … "39 targets" (craft 2).

**Derivation, now from the picture** (craft 4–8, substance 2, 9)
- λ = 537/576 is assembled from the map's own "537 hits" counter and the 576 of 1/576.
- e^−λ is derived: a second row is built from the first by TransformFromCopy,
  (1 − 1/576)^537 = (1 − λ/537)^537 ≈ e^−λ ≈ 0.3937, with λ flown in from its definition, "small
  slice" and "big power" flagged as spoken, and 0.3933 / 0.3937 flagged together.
- New "two hits" beat: map A's 537 dots line up as a block of 537 bombs; the yellow square
  returns and is enlarged; two bombs turn yellow and drop into it; "537·536/2! ways" writes in
  time with the words; P(2) ≈ 537·536/2! · (1/576)² · e^−λ is built from the ways label, the
  square and P(0)'s e^−λ.
- P(2) → P(k) term by term; 537, 576 and λ = 537/576 turn yellow together; 537 and 576 shrink
  into the λ that flies in from λ's definition (no glyph shredding, no false intermediate
  equation is ever on screen). The derivation sits mid-panel; the finished formula rises to
  the top only when the histogram arrives.
- "Times five seventy-six squares": the y axis reads "squares = 576·P(k)", and the purple bars
  grow during "it predicts these purple bars".

**Measured v2 detector** (substance 3, 4; craft 3)
- A ×5 inset of the 3/4/5+ tail sits above those bars; the red brace "39 targets" now has a
  purple "chance: 39.3" built from the inset's purple bars, and the narration says "thirty-nine
  targets, and chance predicts thirty-nine".
- "χ² test: p = 0.74" for map A ("pure chance misses by more, three times in four"), then
  "p < 10^−50" for map B, and the same readout gives Clarke's "p = 0.88" ("Same test").
- "Too even is the fingerprint of a **spacing** rule" (substance 8).

**Real data** (craft 9, substance 6, 7)
- The payoff now shows the real V-1 impact sites: 887 dots from Shaw & Shaw's digitised LCC bomb
  damage maps (Zenodo doi:10.5281/zenodo.14883986, CC-BY; `v1_impacts.csv`, `realdata.py`)
  rain in like the cold open. Clarke's 144 km² area (Shaw & Shaw's re-creation, labelled
  "≈ Clarke's area") is drawn and gridded into 576 half-km squares before his table builds.
- The limits beat uses the same real map: a 5 km scale bar ("too loosely to choose a street"),
  and a box north of the Thames at 1.9 hits/km² against 3.7 in Clarke's area ("so Clarke chose
  an area where lambda held steady"). The Shaw & Shaw citation is on screen for ~40 s.
- Removed "whole county p = 0.02": Shaw & Shaw's own supplementary analysis says that p came
  from one circle-sampling run and re-runs give ~0.15. The density comparison from their data
  is robust (p = 1.2 × 10⁻⁹). Evidence in facts.md.

**Smaller fixes**
- Clarke's table rows have headers "chance" (purple) and "London" (blue); citations shrunk to
  stay clear of them (craft 10).
- Halos: B's grey discs grow on "no two hits closer than four fifths of a square"; A's discs
  are the same grey, and the 16 that overlap a neighbour (pairs closer than B's rule) turn red on
  "spread out that evenly" (craft 11).
- "so a hundred and thirty-one take two or more": the 131 squares get blue outlines with a live
  "131 squares with 2+" counter; red stays for detector targets (substance 5).
- Empty squares fill at 85 % yellow (no more olive); when dimmed, the "222 empty" label dims
  with them (substance 10).
- Cadence: 0.9 s pause after "Backwards.", ~1 s after "Map A has two hundred and twenty-two.",
  0.2 s gaps inside the Clarke table read (craft 12).
- Landing: A's 39 target squares re-shade red on "what no aim at all looks like" (craft 13).
- Text-to-text changes (P(empty) → P(0), "≈ Clarke's area" → "3.7 hits/km²") are cross-fades,
  not glyph morphs, so no letters shred mid-transition; the P(0) collapse first clears the old
  rows, then moves.
- Every timing/layout warning from the render is fixed (0 warnings). Master: 3:51.6, 164 wpm on
  speech time, −14.0 LUFS / −2.0 dBTP, longest static 3.6 s, longest silence 2.0 s (the planned
  prediction holds), WER 3.0 %.

## Round 2 revisions

Round 2 review: craft 8.3, substance 8.2, no caps. Both said "reaches 9, narrowly": the
structure holds, and the joins (shredded morphs, a river nobody could see, a competing map, a
crowded Clarke frame) and one black box (the chi-squared verdict) were what held it back.

**Plan the climb** (BAR §3 "9" anchor → where it fell short → the upgrade)
- Clarity (8.5 / 8): "viewer could re-derive it after one watch". Short: the χ² verdict was a
  number with no picture; 537·536 → 537^k was skipped. Upgrade: build the misfit from the gaps
  and read p off 20,000 simulated chance maps; show 537·536 ≈ 537² and change one 2 at a time.
- Visual (8 / 8): "one focal point per frame". Short: bright map behind the derivation, olive
  dimming, crowded Clarke frame, insets covering data, a map with no geography. Upgrade: uniform
  dimming, insets over a dimmed map, the Thames, smaller dots, decluttered Clarke frame.
- Motion (8 / 8.5): "every motion encodes a relation". Short: whole-equation morphs that shred
  glyphs. Upgrade: glyph-level swaps, persistent "39", P( and ) kept, terms flying out of gaps.
- Audio (8 / 8): Short: top-of-band pace in the derivation, uniform gaps, mis-heard lines.
  Upgrade: 0.80 speed on the general-k beat, two 0.7 s pauses, three rewritten lines.
- Concision (8.5 / 8): cut "four in ten…", the separate "ways" label, and the general-k reading.
- Hook (8.5): the title gave the answer away → retitled "Which Map Is Random?".
- Originality (8.5): map A shrinks into one score among 20,000 chance maps; a simulated aimed
  map shows the opposite fingerprint.

**Clarity / substance**
- The χ² verdict is now built on screen (substance 1): each bar's gap lights as a yellow sliver
  (bars 0–2 in the chart, 3–5+ in the ×5 inset), lifts into its term (0.10 + 0.64 + 0.43 + 0.22 +
  0.49 + 0.12) and the terms fly into a live readout "χ² = Σ gap²/chance = 2.0". Map A then
  shrinks onto a marker at 2.0 of a misfit axis as the misfits of 20,000 simulated pure-chance
  maps grow beside it; the bins from 2.0 up brighten and "p = 0.74" comes out of them (simulated
  0.745, χ²₄ 0.736). Map B's huge gaps roll the readout to 271.7 and carry "B: 271.7" off the end
  of the axis. Narration: "The chi-squared misfit: square each bar's gap, divide by chance's bar,
  and add them up. Map A scores two point oh. Pure-chance maps score worse three times in four:
  p equals point seven four."
- 537·536 ≈ 537² (substance 2, craft 2): "Five thirty-six is almost five thirty-seven" copies
  "537·536 ≈ 537²" out of P(2)'s numerator and flags 536 and 537²; the numerator becomes 537²
  with the ² dropping in from that line; then "so for any k, each two becomes a k" swaps one
  glyph at a time (P(2) → P(k), 537² → 537^k, 2! → k!, (1/576)² → (1/576)^k). Nothing is
  morphed as a whole equation any more.
- Aim's fingerprint is shown, not asserted (craft 12): the simulated aimed map itself rains into
  the left slot (537 hits around 3 aim points, s.d. 2 squares, `sim.aimed_map`, seed 0) while
  red outline bars of its histogram grow over chance's: 399 empty vs 227, 58 / 37 in the middle
  classes, 39 squares with 5+; red × marks land on the aim points on "extra pile-ups"; labelled
  "aimed · simulated". The arrows are gone (so is craft 10's arrow-through-frame).
- The Thames (craft 1, substance 3): OS Open Rivers centreline (OGL; `thames.py` →
  `thames_os_open_rivers.csv` → `real_data.npz`), same BNG transform, drawn with a "Thames"
  label as the real map arrives and flashed yellow on "north of the river". Labels now read
  "north: 1.9 hits/km²" and "≈ Clarke's area: 3.7 hits/km²" (the rectangle keeps its name).
- "published this test" in 1946, not "ran" (substance 5). "so plenty must double up" (the 131
  is shown as a count, not derived; substance 9). The densities carry their own credit,
  "hits/km²: our count · L. Shaw, 2025 · Zenodo" (substance 6).
- facts.md: Shaw & Shaw's published p = 0.70 reproduced (their two-column `chisq.test`
  homogeneity test: χ² 3.06, df 5, p 0.69) next to our goodness-of-fit p = 0.18 for the same
  table; the misfit terms, simulation, aimed map, river provenance and the box straddling the
  Thames are all documented.
- Retitled "Which Map Is Random?" (substance 10) in the end card and script; the old title gave
  away the cold-open answer.

**Visual**
- Derivation (craft 3, substance 8): the whole of map A dims uniformly to 30 % on "lambda";
  the yellow fill fades out instead of turning olive; only the one yellow square stays lit.
  Everything returns on "Map A sits on the purple bars".
- Zooms (craft 5, substance 13): both maps step back to 30 % while the insets are up, the insets
  sit on a 0.08-unit background margin, and the maps return on "Take one square".
- Clarke frame (craft 4, substance 4, 15): the "south London" legend is gone; "Poisson" gives way
  to "χ² = 1.17,  p = 0.88" on the formula line; citations end left of x = −1.4 (≤ 770 px);
  real dots are radius 0.035 (narrower than a 0.5 km square) and those outside Clarke's area dim
  to 35 % once it is gridded (the north box's dots return to full when it is drawn); row headers
  and "simulated" tags are 24.
- λ^k is purple from the moment it arrives (craft 9). GRAY text is #A6ABB5, 7.9:1 (craft 11),
  including the end card.

**Motion**
- "39 targets" → "39 false alarms": the 39 never moves; only the word lifts out and the new
  one rises in (craft 6). "0 targets" finishes fading before the rule tag appears
  (substance 14). P(empty) → P(0): P( and ) stay, only "empty" → "0" changes (craft 7). P(2)'s
  numerator is drawn out of the bomb block (537), the rest of the block (536) and the two
  yellow hits (2!), with no stacked duplicate glyphs left behind.

**Audio**
- Speed 0.80 on the general-k beat; 0.7 s pauses after "e to the minus lambda." and "the Poisson
  distribution." (craft 8). "A pattern this even is the fingerprint of a spacing rule", "Aimed
  bombs would miss the other way", "times five hundred and seventy-six squares" (craft 8,
  substance 11, 12). Cut: "four in ten, with almost a bomb per square", "on map A, a hundred and
  thirty-one" (shown, not spoken), the separate "ways" label, the term-by-term reading of P(k).

**Mechanics** (master, review kit): 3:55.3, 162 wpm on speech time (156 overall), −14.0 LUFS /
−2.1 dBTP, longest static 3.6 s, longest silence 2.0 s (the planned prediction hold), WER 2.6 %
(whisper now hears "A pattern this even", "Aimed bombs", "Times 576 squares", "Map A scores
2.0"), 0 sync warnings, 0 overlaps; one clearance note at the last frame of the λ^k merge (not
held) and one declared pair (a fraction bar against its own row's closing parenthesis).

## Round 3 revisions

Round 3 review: craft 8.6, substance 8.5, no caps, no factual errors. Both said "reaches 9,
narrowly" and named the same kind of defect: frames with two or three competing layers, two
pictures that mislead a careful viewer (Clarke's bars beside re-created dots; "north of the
river" over a rectangle that straddles it), an unlabelled B histogram, a landing that dips
through an empty frame, and a flat cadence in the derivation.

**Plan the climb** (BAR §3 "9" anchor → where it fell short → the upgrade)
- Clarity (9 / 8.5): "viewer could re-derive it after one watch; all numbers check out".
  Short: Clarke's 229/211… sat beside a gridded re-creation whose dots count 237/189…; "north
  of the river" was said over a box that is partly north of it; B's bars had no B on screen.
  Upgrade: row header "Clarke" + "Clarke counted", a "re-created" tag, "Farther north"
  with the north box flashed (the river flash is gone), and a B thumbnail beside A's.
- Visual (8.5 / 8.5): "every frame has one focal point". Short: five layers at 1:34, the
  yellow map beside the χ² build, insets over the maps, maroon landing fills, the Thames
  knockout over real dots, a duplicate "aimed simulated" legend, the north label far from its
  box. Upgrade: one layer at a time (yellow fill and red outlines leave on "plenty"; map to
  35 % on "The chi-squared misfit"), a [A][zoom][B][zoom] row, red outlines, a label in open ground, one
  header, the label on its box and the scale bar moved to the header row.
- Motion (8.5 / 8.5): "every motion encodes a relation". Short: the landing dissolved through
  an empty frame; the aimed dots rained in before their frame. Upgrade: Clarke's rectangle opens
  into map A's frame carrying A's hits (cross-faded with London's inside it), B slides in;
  frame, header and counter first for the aimed map.
- Audio (8.5 / 8.5): Short: the P(2)/P(k) steps were one 22.7 s breath group. Upgrade: 0.6 s
  pauses after "over two, ways." and "e to the minus lambda again.", 0.5 s after "lambda.".
- Concision (8.5 / 8.5): cut "The chance is point three nine three, so" and "One over five
  seventy-six is lambda over five thirty-seven" (the on-screen copy carries both).
- Hook (8.5 / 8.5): Short: the commitment was spoken only; the closing "plan" line blurred
  rule and aim. Upgrade: "A or B?" holds the prediction on screen; the close says "the one
  following a rule", echoing "The other follows a rule".
- Originality (8.5): the landing now *is* the payoff: London's re-created area opens out into
  map A, the pure-chance map.

**Clarity / substance** (substance 1–4, 7; craft 12)
- Clarke's counts are attributed to Clarke: the blue table row is headed "Clarke" (was
  "London"; "Clarke, 1946" collided with the citation block, whose first line already reads
  "R. D. Clarke, 1946 · J. Inst. Actuaries 72:481"), the narration says "Clarke counted two
  hundred and twenty-nine", and a GRAY "re-created" tag sits beside "≈ Clarke's area" while the
  table builds. facts.md records why the re-created dots count 237/189/… (532 hits).
- "Farther north, hits fell about half as densely" replaces "north of the river" (the
  re-created rectangle has 20.6 km² and 56 hits north of the Thames; recomputed and logged). The
  north box draws and flashes on "Farther north"; the river is no longer flashed.
- Map B gets its own thumbnail (same size, labelled "B") beside A's on "Map B"; A's thumbnail,
  label, marker and p dim to 35 % and come back when "B: 271.7" lands.
- Closing line: "If you picked map B, you picked the one following a rule." (echoes "The
  other follows a rule"; "plan" blurred rule and aim).
- "The detector, like your eye, expected chance to spread out that evenly" now carries
  "Falk & Konold, 1997 · Psych. Review 104(2)" for ~4.5 s (verified in the paper: people equate
  randomness with excess alternation in sequences and 2-D grids; quote in facts.md).
- "A or B?" (GRAY, 30) holds the prediction under the maps from "Which" until "Both are
  simulated".

**Visual** (craft 1, 2, 4, 5, 6, 8, 9, 11)
- On "so plenty must double up" the yellow fill leaves the empty squares and the red 3+
  outlines leave, so the 131 blue outlines and the dots are the only full-strength layer. (The
  critics asked for yellow at 35 %; a dimmed yellow renders olive-brown on the slate background,
  which round 2 flagged, so it fades out instead and the empties read as unshaded cells.) Red and
  yellow return with the map at the histogram (2:15).
- On "The chi-squared misfit" map A, its outlines and labels dim to 35 % over 0.6 s (yellow
  fill out), leaving the gap slivers as the only full yellow; A returns to full strength as it
  shrinks onto the misfit axis.
- Zooms (0:50–0:59): on "Map B's rule" both maps shrink to 0.7 and the row becomes
  [A][A zoom][B][B zoom] across the safe area; the zoomed blocks sit on each map's right edge
  so the leader lines only cross the gutter (A: densest edge block, 23 hits, 22 discs turn
  red; B: the edge block closest to the 16-hit average). The hits counters step out and return
  with A on "Take one square"; B and the zooms finish fading before A grows over their place.
- Landing targets are the 0:39 red outlines (LaggedStart Create, lag 0.02, 1.0 s), no fill.
- "Thames" has no knockout: it is placed by search in open ground above the river's east end,
  ≥ 0.2 from every hit, 0.15–0.4 from the river, clear of both boxes and ≥ 0.7 from the chart.
- One "aimed · simulated" header (the chart legend is gone).
- "north: 1.9 hits/km²" is left-aligned on the north box, lifted only as far as the hits above
  the box require (directly above them; a label any lower would sit on real dots); the 5 km
  scale bar moved to the map's header row so nothing else competes for that label.
- A red ring (radius 0.35) draws on "like this one" and leaves after "Map A lights up".
- Citations on the real-map frames are set at 18 (BAR minimum) instead of being shrunk below it.
- "≈ Clarke's area" moves (no glyph morph) before ": 3.7 hits/km²" fades in.

**Motion** (craft 3, 7)
- Landing: everything but Clarke's rectangle and its hits leaves; map A's hits fade in inside
  the rectangle (at the real dots' size) while London's fade out, A's reaching half strength
  before London's drop below it; then the rectangle opens into map A's frame carrying A's hits
  (1.3 s) and B slides in from the right. No empty dip; the payoff (London looked like chance)
  becomes the first frame again.
- Aimed map: frame, header and a live "hits" counter appear on "Aimed bombs", then the hits
  rain in, as in the cold open.
- 0.3933 → "0.3933 × 576 ≈ 227" no longer morphs the words "empty squares" into the number:
  the question fades as 0.3933 writes, then the product row builds from a copy of 0.3933.

**Audio / concision** (craft 10, 13; substance 6)
- Cut "The chance is point three nine three, so" and "One over five seventy-six is lambda over
  five thirty-seven" (the second row is now copied in a 0.5 s pause, with λ and 537 flying in
  from λ = 537/576, and 1/576 and λ/537 flag together on "small slice").
- Added 0.6 s after "over two, ways." and after "e to the minus lambda again.", and 0.9 s after
  "So look again." for the landing transform.

**Keep items**: the glyph-by-glyph P(2) → P(k), the measured verdict (slivers → 2.0, A on the
20,000-map histogram, B at 271.7), the "39 targets, chance predicts 39" failure, the
gaps-force-clumps pigeonhole and the honest-limits beat are unchanged. One conflict: craft
kept "the Thames flashing yellow on 'river'", substance asked to drop it because the
rectangle straddles the river. Correctness wins: the word "river" is gone, the river stays
drawn and labelled as geography, and the flash moved to the north box on "Farther north".

**Mechanics** (master, review kit): 3:49.5 (was 3:55.3), 161 wpm on speech time (154
overall), −14.0 LUFS / −1.8 dBTP, longest static 3.6 s, longest silence 2.0 s (the planned
prediction hold), WER 3.3 %, 0 sync warnings, 0 overlaps; the one clearance note is the same
end-of-animation frame as round 3 (2:05.8, not held). Checked frames at 4 fps across the zoom
row, the square-beat return, the B thumbnail, the aimed map, the Clarke label and the landing.

## Round 5 revisions

Round 5 review (the round-4 cut, reviewed twice): craft 8.0 / 8.6, substance 8.3 / 8.8, no
caps. Every critic said "reaches 9, narrowly, if the derivation and the yellow-swamped frames are
fixed". A previous attempt at this revision stopped after the narration rewrite and three small
scene edits (no render); this pass continues from those files.

**Plan the climb** (BAR §3 "9" anchor → where it fell short → the upgrade)
- Hook (8.5): "tension rises through build and fail". Short: 1:31–2:14 ran with no stated
  question. Upgrade: "To judge London, chance must predict every bar" over a preview of the
  histogram (chance's 227 in bar 0, "?" over 1–5+), which the derivation then fills.
- Clarity (8–9): "viewer could re-derive it after one watch". Short: four glyph swaps in 10 s;
  "over two" unexplained; χ² division unexplained; p never named. Upgrade: 536 → 537 in place,
  537·537 → 537²; "for three hits, each two becomes a three; for any k, a k" (all at once, with
  pauses); "since order doesn't matter" with the two hits swapping; "a miss of two on seven
  outweighs a miss of five on two hundred twenty-seven" on A's own bars; "That share, p".
- Visual (7.5–8.5): "every frame has one focal point". Short: solid yellow over 39 % of map A
  (1:19–1:31, 2:17), yellow-speckle thumbnails, unlabelled null histogram, citations 22 px,
  densities 600 px apart, gridless aimed map. Upgrade: 40 % tint + yellow region outline, gone
  before the histogram; blue shading on return; dots-only thumbnails; "maps" axis; citations
  at 20 (≈25 px cap); the two densities in one column on their boxes' rows; aimed grid.
- Motion (8–9): "every motion encodes a relation". Short: static reveal (3.6 s), cells→bars
  cloud, "39.3" shredding, red bars left behind, rectangle squashing map A. Upgrade: re-rain on
  "I dropped every hit"; count-by-count flight (k-hit squares outline, then fly into bar k);
  flag + Write; aimed bars ride the chart while fading; rectangle → equal-area square → frame.
- Audio (8–8.5): "each deictic lands; pauses intentional". Short: stretched "and" in numbers,
  "three times than four", "you pick the one", counter late on "thirty-nine", 1/576 late.
  Upgrade: numbers without "and", "Three in four simulated chance maps score worse", "you chose",
  counter and fraction cued to their words.
- Concision (7.5–9): cut "Map A sits on the purple bars", "No sign of clustering", "and B looks
  like chance", the separate 537·536 ≈ 537² line; shorter stakes line.
- Originality (8–8.5): the real V-1 map now carries the aim itself: Tower Bridge and the
  12.5 km circle that holds only half the V-1s is bigger than the whole county map.

**What changed** (all three round-5 passes; the first two were interrupted before a reviewed
render, this one continued from their files and re-rendered twice)

- *Facts.* Neither critic found an error. The one unsourced line ("aimed at London, just too
  loosely to choose a street", substance 6) is gone. The limit is now "The bombs were aimed at
  central London but tended to fall short, so farther north, hits were about half as dense",
  re-verified in Evans & Delaney 2018 (*Applied Geography* 99: published aiming point Tower
  Bridge; overall mean point of impact of 2,111 V-1s 5.6 km south, in Dulwich; "as a consequence
  of this bias, V1 impact density was less … north of the Thames") and Shaw & Shaw 2019 ("tended
  to fall short of the centre of London"). The red × and arrow are credited on screen with
  "aim: Evans & Delaney, 2018 · Applied Geography 99" ("aim:" in the marks' red). facts.md has
  the quotes.
- *Hook / clarity (substance 1–3, craft 1, 3).* There is a forward line: "To judge London, chance
  must predict every bar", shown over a preview histogram with chance's 227 and "?" over the other
  bars. The k = 3 step is in ("for three hits, each two becomes a three; for any k, a k"), with all
  the 2s changing at once. 536 becomes 537 in place and folds into 537²; the separate side line is
  cut. "Over two, since order doesn't matter" plays while the two hits swap places. The χ² now says
  why it divides ("so a miss on a short bar counts more", with the 4-hit sliver, its 0.49 and
  chance's 7.1 flagged) and names p ("That share, p, is point seven four"). "Gap" now means only
  the bar difference: B's tag is "rule: spacing ≥ 4/5 square", and the line is "Those empty
  squares force the clumps".
- *Visual (craft 2, 4, 7, 10, 12; substance 5, 8).* The empty squares are a yellow outline of
  each empty region with no fill. A yellow tint under 60 % read olive on the slate, so no tint is
  used. The outline goes before the histogram; map A returns with blue shading. Thumbnails show
  dots and frame only. The null histogram has a "maps" axis with 1000/2000 ticks. Readouts read
  χ²_A and χ²_B, and each shows "= ?" until its terms are added: no frame says "= 0.0" or a stale
  "= 2.0" under B. A's score marker never fades below 60 %. The two densities sit in one column on
  their boxes' rows. Citations are at 20 (≈ 25 px cap). The "109" label is lifted to buff 0.22.
  The aimed map has its grid.
- *Motion (craft 5, 6, 11; substance 9).* A's hits re-rain on "I dropped every hit" (the 3.6 s
  static frame is gone). The cells → bars flight is count by count. "chance: 39.3" is a flag
  followed by a Write, with no shredding morph. The aimed bars ride the chart while they fade. The
  histogram axes draw only after the 1.5 line and the 2+ count have left. The P(k) copy lands in
  the axis title before "= 576·" is written. The target counter lands on "thirty-nine". 1/576 now
  forms as "one in" is spoken, 0.9 s into the beat (was 2 s late). Landing: London's rectangle
  squares up (equal area) while A's hits cross London's at half strength and A's header arrives,
  so the frame never dips to an empty square. It then opens into map A as B slides in.
- *Audio (craft 8, 9; substance 4).* Numbers are written without "and". "Three out of four
  simulated chance maps score worse": round 4's "three times in four" was heard as "than", and
  this pass's "Three in four" as "3 and 4". "Each has a one in five seventy-six chance" replaces
  "with chance one in…", which was heard as "1 and 576". "Let's call the average…" (a bare "Call" opening the beat lost
  its /k/ and was heard as "all"). The close is "If you chose map B, you
  chose the rule" (the "-ed" of "picked" was swallowed). The pace is 0.84 with shaped cadence and
  0.82 for the closing beat, with breaths inside the short fast lines. A 0.65 s gap follows the
  three beats that end on a story turn, so turns are longer than full stops (0.66 vs 0.36 s
  median). The two-hit beat has a 0.5 s breath (it ran 16 s without one).
- *Concision (substance 7).* 588 → 492 words and 3:49.5 → 3:34.7. Cut: "Map A sits on the purple
  bars", "No sign of clustering", "Single hits: two hundred eleven, exactly as predicted", the
  537·536 ≈ 537² side line, the second limit (the CEP circle), and "but the question is real" →
  "The question isn't."
- *Keep items preserved.* The cold-open A/B frame returns as the closing frame. The P(2) build
  from the bomb block and the enlarged square is unchanged. So are the gap slivers → terms → 2.0
  → A on the 20,000-map null, B at 271.7, the aimed-map counterexample, Clarke's table growing into
  chance's outlines, and the honest one-λ limit.

**Mechanics** (final master, review kit, 0 render warnings): 3:34.7, 492 words, 157 wpm on speech
time (151 overall), 0 sentences above 200 wpm, full stops 0.36 s vs beat turns 0.66 s, longest
run without a breath 12.1 s, −14.0 LUFS / −1.5 dBTP, longest silence 1.8 s (the planned prediction
hold), longest static stretch 2.6 s, WER 2.5 % (every remaining difference is number formatting
or "Clark"), 0 banned phrases, 0 glyph morphs, 6/6 deictics on an animation, layout audit 0
issues in 227 checks (two declared fraction-bar/parenthesis pairs). Checked: all 12 contact
sheets, keyframes at 0:57, 1:18, 2:34, 3:01 and 3:23, and 4 fps strips across the axes draw
(1:20), the P(k) copy into the axis title (2:04), the A → B readout swap (2:32) and the landing
transform (3:24).

## Round 6 revisions

Round 6 scored craft 8.4 and substance 8.5 (both FAIL, no caps, no factual errors). Both critics
said every listed fix would reach 9, and neither asked for a restructure. So this pass keeps the
structure and the keep items: the A/B cold open that returns as the closing frame, the
one-square derivation, and one histogram reused for A, B, the aimed map and Clarke.

**Plan (BAR §3 "9" anchor → what fell short → upgrade)**

- Hook (8.5): "ending resolves the opening exactly". The stakes ("precise aim would put factories
  at risk") were never answered, and the landing re-told the reveal without the measurement.
  Upgrade: answer the stakes in words after p = 0.88, and write each map's misfit under it on
  the closing frame.
- Clarity (8.5): "re-derive after one watch; all numbers check". Four gaps: "force the clumps"
  over-claimed; P(empty) became P(0) silently; e^−λ was asserted; the two-hit step was
  number-dense. Upgrade: 183 extra hits shown as 537 − 354; "Call that P of zero" renamed in the
  same line; 0.3933 and 0.3937 lit together; "that same chance" carries the visible 1/576.
- Visual (8 / 8.5): "every frame has one focal point". Five problems: triple overlays at
  1:13–1:20, a yellow fill used both for focus and for gap on B's bars, the 109 label inside
  chance's outline, "north" far from its box, and a crowded 2:25–2:45 frame. Upgrade: one blue
  layer, INK rings, no 109 label, labels with arrows, and the Poisson line and the 227 label
  hidden.
- Motion (8.5): "every motion encodes a relation". Two problems: the re-rain contradicted the
  shading, and the landing cross-fade garbled the header. Upgrade: the shading rebuilds per cell,
  and the outgoing elements fade before the square-up.
- Audio (8.5): "pauses intentional". Two problems: the two-hit beat ran as one run, and the
  limits beat went 12 s without a breath. Upgrade: 0.8 s pauses and a 0.6 s pause.
- Concision (8.5): "cutting any sentence loses something". Upgrade: cut "Both are simulated. The
  question isn't." and "So look again." (A cut of "like the detector" was tried and reverted: it
  left "Your eye expects chance to look that even" spoken at 209 wpm.)

**What changed**

- *Facts.* Neither critic found an error. The new line "London's clusters were no sign of
  precise aim" was checked against Clarke 1946 ("lends no support to the clustering hypothesis")
  and Shaw & Shaw 2019, read again today in the Wiley full text. Shaw & Shaw frame Clarke's
  question as "random chance, or … precision guidance?" and name munitions factories as the
  stake. facts.md has a new "Round 6 additions" table covering 183 = Σ(count − 1), the 0.3933 vs
  0.3937 check, P(0), (1/576)², the landing readouts and the retitle.
- *Hook (substance 2, 9; craft 8).*
  - The stakes are answered after "Overall, p equals point eight eight": "London's clusters were
    no sign of precise aim." While it plays, Clarke's 3+ columns (35, 7, 1 over 30.6, 7.1, 1.6)
    and the ×5 tail inset are ringed, and p = 0.88 flags.
  - The landing writes "pure chance · misfit 2.0" under A and "spacing rule · misfit 271.7" under
    B, so the opening frame is shown through the episode's own test. The yellow circles are gone.
  - Craft asked for "misfit 2.0 · p = 0.74" under A. That does not fit beside the tag above the
    caption zone, so both maps carry the same metric.
  - "Both are simulated. The question isn't." is cut. The "simulated" tags stay on screen from
    the first frame.
- *Clarity (substance 1, 3, 6, 8).*
  - Gaps beat:
    - New line: "Those empty squares force pile-ups: the other three hundred fifty-four share
      all the hits, so a hundred eighty-three must land where another already did."
    - On "pile-ups" the blue 2+ outlines draw; the red 3+ outlines stay off.
    - On "three hundred fifty-four" the hits counter's 537 is carried into "537 − 354", and
      "= 183 extra hits" is written in blue.
  - "One minus a small slice, raised to a big power, is e to the minus lambda, almost exactly."
    The value 0.3937 is written first, then 0.3933 and 0.3937 light up together in yellow on
    "almost exactly".
  - "Call that P of zero." The word "empty" gives way to a 0 inside the same P(…) line.
  - In the two-hit beat, the rows collapse and only their 1/576 survives, beside the big square.
    "Each has that same chance" carries it into (1/576)²; "the rest miss" dims the other 535
    bombs. The figure "one in five seventy-six" is no longer spoken twice.
  - End card: "Which Map Is Pure Chance?", because B is random too (substance 10).
- *Visual (craft 3–6, 10; substance 4, 5).*
  - 1:07–1:21: one blue layer (shading at 40 % plus the 2+ outlines). The empty-region outline
    and "222 empty" turn grey on "the other". The live 131 counter is gone, so this stretch holds
    one fewer number.
  - Map B:
    - On "half", bar 0 is ringed in INK and chance's outline flashes INK (stroke only).
    - On "tower", bar 1 is ringed in INK and a full-strength blue "397" appears above it. No
      fill changes, so yellow in the chart means only gap.
    - The 109 label is dropped: the half-height bar reads against the y axis.
  - 2:26–2:44: the dim Poisson line fades to 0 (it returns at the aimed map), the purple "227"
    leaves when B's bars arrive, and the header reads "20,000 chance maps (simulated)" on one
    line.
  - Limits: "north" sits in the density column level with its box's top, off the Thames label's
    baseline, with a white arrow to the box. "≈ Clarke's area" gets a yellow arrow to the
    rectangle. 1.9 and 3.7 hits/km² sit in one column.
  - The aimed counter is laid out at "537 hits" and right-aligned to its frame (the number's
    left edge stays put as it counts).
- *Motion (craft 1, 7).*
  - The re-rain is true at every frame. Shading and red outlines clear with the hits. Each cell
    then re-shades by the hits landed in it, and its red outline returns when it reaches 3.
    Counters recount 0 → 537 hits and 0 → 39 targets ("1 target" singular).
  - Landing, in order:
    1. On "where it held steady", everything but Clarke's area and its hits fades at once
       (title, Thames, boxes, labels, arrows, marks, citations, formula).
    2. The area squares up while London's hits hand over to A's.
    3. It opens into A's frame as B slides in.
    4. A's header and the 0:39 red outlines arrive only after that, on "map A".
- *Audio (craft 2, 9; substance 7).*
  - "since order doesn't matter" became "since each pair counts twice": whisper twice heard
    "doesn matter", and the new clause says what the swap of the two hits shows (537 × 536
    counts the pair a-then-b and b-then-a).
  - 0.8 s after "since each pair counts twice." and an 0.8 s beat gap after "e to the minus lambda
    again."
  - 0.6 s after "half as dense.", where the breath lands on the density write.
  - 0.3 s after "force pile-ups:" (the gaps beat measured 13.5 s without a breath), while the
    blue outlines draw.
  - 0.9 s after the limits beat for the square-up.
  - "London's clusters" follows a 0.5 s pause.
  - To pay for these within the 3:35 budget, three pauses were trimmed. The pause after
    "Backwards." is 0.6 s (was 0.7), the formula hold after "the Poisson distribution." is
    0.5 s (was 0.8), and the three story-turn gaps are 0.55 s (was 0.65), which is still longer
    than a full stop. The end card holds 0.3 s.
- *Also fixed while checking the frames.*
  - A's crowding zoom discs now turn red on "that even" and stay red into the pause. They used
    to turn red after the last word, for about 0.5 s.
  - The 20,000-map panel's header and axes appear only once the shrinking map has cleared their
    place. At 2:25 the map used to pass over "20,000 chance maps (simulated)" and "maps".
  - "≈ Clarke's area / re-created" fades out with the chart and back in at its new place. It
    used to slide across the growing map.
  - In the λ beat the red 3+ outlines no longer flash back for one frame. A stale dimming
    function had set them to full opacity at the start of the map's step back.

**Mechanics** (final master, review kit, 0 render warnings)

| Metric | Value |
|---|---|
| Runtime | 3:34.6 |
| Words | 496 |
| Pace | 158 wpm on speech time (152 overall) |
| Sentences above 200 wpm | 0 |
| Full stops vs beat turns | 0.34 s vs 0.58 s median |
| Longest run without a ≥ 0.35 s breath | 13.2 s (gaps beat; was 12.1 s in the limits beat, which now breaks at "half as dense") |
| Loudness / true peak | −14.0 LUFS / −1.9 dBTP |
| Longest silence | 1.76 s (the planned prediction hold) |
| Longest static stretch | 2.7 s |
| WER | 2.9 % |
| Banned phrases | 0 |
| Glyph morphs | 0 |
| Deictics on an animation | 6/6 |
| Layout audit | 0 issues in 235 checks (two declared fraction-bar/parenthesis pairs) |

- *Two-hit beat.* Measured silences are 0.9 s after "each pair counts twice" (1:43.4–1:44.3) and 0.9 s after "e to the minus lambda again" (1:49.0–1:50.0). Whisper now ends a segment after "over two" and capitalises "Each" and "E to the minus…". It still writes the 11 s window between them without full stops, which is its own punctuation choice and not a missing pause.
- *Transcript fixes.* The transcript no longer contains "doesn matter". An intermediate master's "Thank you" hallucination after the last line, and its doubled "Map B", are gone in the final transcript.
- *Frames checked.*
  - All 12 contact sheets.
  - Keyframes at 1:13, 3:22 and 3:33.
  - Frame strips across the re-rain (0:35–0:39), the gaps beat (1:08–1:20), the λ / P(0) / two-hit build (1:29–1:48), map B (2:32–2:42), the aimed header, the stakes answer (3:09–3:11) and the landing (3:19–3:28).

## Round 7 revisions

**Plan (both critics 8.6; every dimension below 9 except Hook, and craft's Concision).**
- Clarity 8.5 → 9 ("could re-derive it after one watch"): the e^−λ limit, the χ² weighting and
  one entry of the null were announced, not shown, and the A/B zoom was unfair. Upgrade: a
  convergence plot, chance's own whiskers, three simulated maps dropping into their bins, the
  same 16-hit rule for both zooms, and a measured limit.
- Visual 8.5 → 9 ("one focal point per frame"): limits labels far from their boxes, a
  four-layer map at 1:06, the yellow aimed frame, a dense Clarke frame, 1/576 far from its
  square. Upgrade: labels beside their referents, one coloured layer per sentence, dimmed
  context.
- Motion 8.5 → 9 ("every motion encodes a relation"): glyph soup at 2:23, five moves at once
  at 1:35, an end-card double exposure. Upgrade: in-place sum, one move per phrase, sequential
  end fade.
- Audio 8.5 → 9: the 227 reveal landed ~1 s after it was spoken. Upgrade: the method is built
  in the guess hold; only the "?" changes on "two hundred".
- Concision 8.5 (substance): cut the forward signpost and the spoken 354.
- Originality 8.5: the limit becomes a measured surprise (the test passes the north too, yet the
  bombs were aimed: the aim hides in λ).

**Facts.** Neither critic found an error. Substance fix 1's suggested line ("Pool the two, and
chance at two densities fakes the aim fingerprint: p equals point oh four") was checked and
**not** used. The pooled numbers are right (χ² = 10.0, p = 0.04), but the cause is not:
- the two-density mixture sits only 0.7 of misfit away from one-λ Poisson;
- pure chance simulated at the two densities gives a median pooled χ² of 4.0, and χ² ≥ 10 in
  9.5 % of 20,000 runs;
- against the mixture itself, the real pooled histogram still misfits by 8.5, mostly from the
  rectangle's own shortfall of single hits.

The limit is now measured another way (facts.md, "Round 7 additions"). The north box scored
alone fits chance: 115/46/17/2/0/0 against its own Poisson, p = 0.45 by 200,000 simulated maps
(χ²₄ gives 0.59 with expected counts of 0.24 and 0.03; merging to 3+ gives 0.27). So both areas
pass, while their densities differ 2:1. The aim shows only in λ.

**What changed (craft fixes C1–C10, substance fixes S1–S11)**
- *Limits (C1, S1, S8).* The map grows ×1.35 and moves right 1.1. "north · 1.9 hits/km²"
  sits beside the north box (buff 0.25, on a knockout). "≈ Clarke's area re-created" and
  "3.7 hits/km²" sit beside the rectangle, joined by a 0.26-unit leader. The long white arrow is
  gone. The title and Thames label stay at 35 %. New narration: "Score the north alone, and it
  fits chance too: p equals point four five. The aim hides in lambda, which the test holds
  fixed." The map shrinks back, "north" travels to tag the bars, the north's own Poisson bars
  and counts grow in the same chart, and "p = 0.45" writes where p = 0.88 sat.
- *Map A at "Map A has 222" (C2).* The blue shading and the dimmed red outlines go to 0 and
  the hits drop to 60 %, so the yellow empties are the only coloured layer. Blue returns on
  "pile-ups".
- *227 (C3, S5).* "≈ 0.3933" and "0.3933 × 576 ≈ ?" are built in the guess hold, with 0.3933
  and 576 carried from P(empty). On "two hundred" only the "?" swaps to 227.
- *χ² sum (C4, S6).* No copies fly. Each term flags in place (LaggedStart, lag 0.25, 1.4 s)
  while the readout steps 0.10, 0.74, 1.17, 1.39, 1.88, 2.00. The "?" is now animated with the
  readout: it used to be frozen into the static background and showed through the digits.
- *Two-hit beat (C5, S11).* One move per phrase: the rows collapse on "For two hits" (the
  e^−λ climbs on an arc clear of the surviving 1/576), the square enlarges with its 1/576 on
  "this square", and the dots stream into the block on "pick", before the two picks drop.
- *Null (C6).* The null run's first three maps (scores 3.7, 2.1, 2.8, equal to `NULL[:3]`)
  each appear with their score, hold 0.3 s and drop into their bin. Then the 20,000-map bins
  grow. The pause after "two point oh" is 0.6 s (was 0.3).
- *End card (C7, S7).* The A/B frame fades out fully (0.35 s) before the card fades in.
- *Aimed map (C8).* Empty-region outlines skip the map border, so the GRAY frame stays grey (map
  A too).
- *Clarke frame (C9).* The title and "Thames" dim to 35 % as the table builds.
- *1/576 (C10).* The fraction is written beside the square on "one in" and flies into its slot
  on "To stay empty".
- *Zoom fairness (S2).* A's zoom is now its edge block closest to the 16-hit average (rows
  18–21: 14 of 16 discs crowd), the same rule as B's.
- *e^−λ (S3).* A (1 − λ/n)^n plot (log n: 1, 2, 5, 20, 537) draws on "small slice". Its dots
  climb to the purple dashed e^−λ line on "raised to a big power".
- *Why divide (S4).* "…because short bars wobble less. So a miss on a short bar counts more."
  INK whiskers ±12 (bar 0) and ±2.7 (bar 4) show binomial s.d.s of 11.7 and 2.65.
- *Concision (S9, S10).* "To judge London, chance must predict every bar" is cut, with its
  preview chart: drawing it would have cut the reading time of the 183 line. The spoken 354 is
  cut. On screen: 537 − (576 − 222) = 183 extra hits, each number carried from its source.
