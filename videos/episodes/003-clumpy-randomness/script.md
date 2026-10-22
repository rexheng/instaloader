# Episode 3 — Which Map Is Pure Chance?

(Curriculum working title: "Randomness Looks Clumpier Than You Think"; retitled in round 3
because that title gave away the cold-open answer. Round 6: "Which Map Is Random?" became
"Which Map Is Pure Chance?" on the end card, because map B is generated at random too, by
random sequential addition with a spacing rule.)

**One idea:** pure chance leaves gaps, and the gaps force pile-ups; so clusters alone
are not evidence of aim. The honest test scores the whole count histogram against Poisson's
prediction (the chi-squared misfit, read against simulated pure-chance maps), and a pattern
that is *too even* is the real sign of a spacing rule.

**Runtime target:** 3:15–3:37 · ≤ 500 words (495) · Kokoro `af_heart` at speed 0.84 with
`CADENCE = "shaped"` (gaps follow the sense; 0.9–1.0 s holds after the key results: 222 vs 227,
the Poisson formula, p = 0.74, p = 0.88). Narration text lives in `narration_text.py`.

## Palette (colour → one meaning, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | observed hit counts: cell shading by count, the "2+ hits" outlines and counter, observed histogram bars, London's numbers |
| PURPLE | pure chance: the Poisson prediction (bars, formula, λ, λ^k, e^−λ), the "pure chance" tag, the "chance" table row, the 20,000 simulated chance maps and their p |
| RED | what the eye/detector flags as a clump or what aim would do: detector outlines, "targets", "false alarms", hit pairs closer than B's rule allows, aim arrows |
| YELLOW | focus: the one square, the empty squares, the term being discussed, each bar's gap and its misfit term, map A's score marker, Clarke's area on the real map |
| INK / GRAY / DIM | text and dots / axes, secondary labels, the Thames, neutral exclusion discs / grid. GRAY text is #A6ABB5 in this episode (7.9:1 on the background) |

Dots are INK (raw hits, neutral) so they stay visible on shaded cells. Flags are colour-only
(no scaling), so a flagged frame or bar never grows into its labels.

## Beats

| # | Narration | Picture |
|---|---|---|
| 1 Cold open | Each map holds five hundred thirty-seven bomb hits. One is pure chance; the other follows a rule. Which is chance? *[pause 1.2]* | Two square maps A and B ("simulated"); 537 dots rain into each while both "hits" counters count to 537. "A", "B" flag on "Which"; a GRAY "A or B?" holds the commitment through the 1.5 s prediction hold. |
| 2 Stakes | In nineteen forty-four, Londoners claimed flying bombs fell in clusters, and precise aim would put factories at risk. | "A or B?" gives way to the citation. Clarke quote "…tended to be grouped in clusters." + citation (Clarke 1946; Shaw & Shaw 2019); yellow circles land on A's three densest interior clumps. |
| 3 Naive build | Build the detector your eye is running. Cut each map into five hundred seventy-six squares, and flag any square with three or more hits, like this one. | 24×24 grids draw; cells shade blue by count in a left-to-right sweep; one 3-hit square gets a red outline and a red ring on "this one". |
| 4 It "works" | Map A lights up with thirty-nine targets, map B with none. So A looks aimed. | 39 red outlines lag in on A with a live counter ("1 target" → "39 targets") that lands on 39 as "thirty-nine" is spoken; B "0 targets"; tags "aimed?" / "chance?". |
| 5 Fail | Backwards. *[pause 0.6]* I dropped every hit on map A at random, so all thirty-nine targets are false alarms. Map B's rule: no two hits closer than four fifths of a square. Your eye, like the detector, expects chance to look that even. | Tags swap to "pure chance". On "I dropped every hit" A's hits, shading and red outlines clear and the hits rain in again (same order and places, counter 0 → 537); each cell re-shades by the hits landed in it and its red outline returns when it reaches 3 (target counter 0 → 39). "39" stays put while "targets" lifts off and "false alarms" rises in. On "Map B's rule" both maps shrink into the [A][A zoom][B][B zoom] row; B's tag "rule: spacing ≥ 4/5 square"; B's discs (radius 0.4 square) never overlap; A's 22 overlapping discs turn red on "that even" (Falk & Konold, 1997 · Psych. Review 104(2)). |
| 6 One square | Each bomb has a one in five seventy-six chance of landing in this square. To stay empty, all five hundred thirty-seven must miss. | B and the zooms leave; A grows back and one empty square is outlined yellow as "Each bomb" is spoken; on "one in" it and the grid become 1/576; on "this square" the square pulses; on "all five hundred thirty-seven" the hits counter's 537 is carried into the exponent: P(empty) = (1 − 1/576)^537, in the middle of the right half. |
| 7 Prediction | Guess how many squares stay empty. *[pause 1.1]* | "empty squares ≈ ?" |
| 8 Answer | About two hundred twenty-seven. *[pause 0.3]* Map A has two hundred twenty-two. *[pause 0.5]* | "≈ 0.3933" writes, then "0.3933 × 576 ≈ 227" is built from it; on "Map A" a yellow outline of each region of empty squares draws over A's 222 empty squares (no fill: a yellow tint under 60 % reads olive on the slate) while the "222 empty" counter lands on the spoken number. |
| 9 Gaps → pile-ups | Those empty squares force pile-ups: *[pause 0.3]* the other three hundred fifty-four share all the hits, so a hundred eighty-three must land where another already did. To judge London, chance must predict every bar. | On "Those" the yellow outline of the empty regions pulses; on "pile-ups" the 131 squares with 2+ hits get BLUE outlines and the blue shading drops to 40 % (the red 3+ outlines stay off); on "the other" the 227 line leaves and the empty outline and "222 empty" turn grey; on "three hundred fifty-four" the hits counter's 537 is carried down into "537 − 354", and "= 183 extra hits" (blue) is written on "a hundred eighty-three"; the blue outlines pulse on "already". On "To judge London" the 183 line, the grey outline and its count leave, then the equation rises and the histogram axes draw with chance's bar 0 (227, purple) and GRAY "?" over 1, 2, 3, 4, 5+ on "every bar". |
| 10 λ and e^−λ | Let's call the average hits per square lambda. *[pause 0.5]* One minus a small slice, raised to a big power, is e to the minus lambda, almost exactly. Call that P of zero. | The preview axes step aside; map A dims to 30 %; λ = 537/576 ≈ 0.93 from the 537 counter and the 576 of 1/576; second row = (1 − λ/537)^537 (λ and 537 fly in from λ's definition); "≈ e^−λ ≈ 0.3937" is written on "e to the minus lambda" and 0.3933 and 0.3937 light up together (yellow) on "almost exactly"; on "P of zero" the yellow word "empty" gives way to a yellow 0 inside the same P(…) line. |
| 11 Two hits | For two hits in this square, pick two bombs: five thirty-seven times five thirty-six ways, over two, since each pair counts twice. *[pause 0.8]* Each has that same chance, and the rest miss: e to the minus lambda again. *(0.8 s beat gap)* | The rows collapse to P(0) ≈ e^−λ, and their 1/576 settles beside the big square; on "this square" the yellow square is enlarged while A's 537 dots line up as "537 bombs"; on "pick" two bombs turn yellow and drop in. On "five thirty-seven" the block lights and "537" is carried out of its label; on "five thirty-six" the other 536 light and 536 writes; on "over two" the two hits light and 2! writes; on "each pair counts twice" the two hits trade places. On "that same chance" the square's 1/576 flags and is carried into (1/576)²; on "the rest miss" the other 535 bombs dim; e^−λ is copied from P(0) on "e to the minus lambda". |
| 12 Poisson | Five thirty-six is almost five thirty-seven. *[pause 0.3]* For three hits, each two becomes a three; for any k, a k. *[pause 0.5]* The powers merge into lambda to the k: the Poisson distribution. *[pause 0.5]* Times five seventy-six squares, it predicts these purple bars. | In place: the 536 lights up and becomes a 537; 537·537 folds into 537². On "each two" all four 2s light up, on "becomes a three" they turn to 3s (P(3) ≈ 537³/3!…), on "k" to k's. 537, 576 and λ = 537/576 light up and shrink into the purple λ^k: P(k) ≈ λ^k/k! · e^−λ, named "Poisson" on the word and held through the pause; it rises to the top on "Times", the axes return, P(k) is copied down into the axis title and "= 576·" is written in front of it once it has landed ("squares = 576·P(k)"), and the purple bars and ×5 tail inset grow on "these purple bars". |
| 13 Fix (v2) | The honest detector compares whole histograms. *[pause 0.4]* Thirty-nine targets, and chance predicts thirty-nine. *[pause 0.4]* The chi-squared misfit squares each bar's gap and divides by chance's bar, so a miss on a short bar counts more. Map A scores *[pause 0.2]* two point oh. Three out of four simulated chance maps score worse. That share, p, is point seven four. *[pause 0.7]* | Map A returns with its blue shading and red outlines (no yellow). Count by count, the k-hit squares outline and copies of exactly those squares fly into bar k. Red brace "39 targets"; chance's tail bars flag and "chance: 39.3" writes. "χ²_A = Σ gap²/chance = ?" writes as A (and the Poisson formula) step back (the readout says "?" until its terms are added, never a false "0.0"); yellow gap slivers grow and lift into their terms (0.10 … 0.12); on "short bar" the 4-hit sliver, its term 0.49 and chance's 7.1 bar flag; on "Map A scores" the terms fly into the readout, the "?" gives way and it counts up to 2.0. A shrinks to a dots-and-frame thumbnail on a yellow marker at 2.0 of a "misfit" axis with a "maps" axis (ticks 1000, 2000); the 20,000 simulated chance maps grow; bins from 2.0 up brighten on "score worse"; "p = 0.74" comes out of them on "That share, p". |
| 13b Map B | Now map B: half the expected empty squares, a tower of single hits, misfit two hundred seventy-two. *[pause 0.3]* A pattern this even is the fingerprint of a spacing rule. | B's dots-and-frame thumbnail appears past the end of the misfit axis, where its score will land; the subscript becomes χ²_B and A's 2.0 gives way to "?"; bars morph to B's and the purple "227" leaves; on "half" B's bar 0 is ringed in INK and chance's outline flashes INK; on "tower" B's bar 1 is ringed in INK and "397" (blue) is written above it (no fill changes: yellow in the chart means only gap); the Poisson line is hidden for this stretch (it returns at the aimed map); the two values leave, then B's gaps light yellow while the readout counts up to 271.7; "B: 271.7" with an arrow off the axis; on "this even" B's thumbnail and its score light up. |
| 14 Aim + Clarke | Aimed bombs would miss the other way: extra empty squares, extra pile-ups. *[pause 0.4]* In nineteen forty-six, R D Clarke published the same test on London's real hits: five thirty-seven in five seventy-six squares. | The aimed map: frame, DIM grid, header and counter, then 537 hits rain in around 3 aim points; on "extra empty squares" its 399 empties are outlined yellow while red outline bars grow over chance's; red × on the aim points on "pile-ups". The red bars ride the chart up while they fade. The real map rains in (887 V-1 sites; title and Thames arrive on "London's real hits"; citations Clarke 1946 and Shaw & Shaw 2019); Clarke's area (re-created) draws on "five thirty-seven", grids into 576 squares on "five seventy-six"; hits outside dim. |
| 15 Payoff | Chance predicted two hundred twenty-seven empty squares; Clarke counted two hundred twenty-nine. *[pause 0.3]* Overall, p equals point eight eight. *[pause 0.5]* London's clusters were no sign of precise aim. | Clarke's table builds under the bars ("chance" purple, "Clarke" blue): chance's row is copied out of the purple bars; on "Clarke counted" his bars grow into the outlines with his row of counts; "Poisson" gives way to "χ² = 1.17" on "Overall" and "p = 0.88" on "p equals", held through the pause. |
| 16 Limits | The bombs were aimed at central London but tended to fall short, so farther north, hits were about half as dense. *[pause 0.6]* The test needs one lambda: Clarke chose an area where it held steady. *(0.9 s beat gap: the area squares up)* | The chart leaves, then the real map grows ×1.35 into the frame; "≈ Clarke's area" moves onto the rectangle's row in a column east of the map and a yellow arrow ties it to the rectangle. On "London" a red × lands on Tower Bridge ("aim: Evans & Delaney, 2018 · Applied Geography 99" joins the citation lines, "aim:" in the marks' red); on "fall short" a red arrow grows from it to Dulwich, their mean point of impact. On "farther" the north box draws and its hits brighten; "north" is written in the same column, level with the box's top (off the Thames label's baseline), and a white arrow points from it to the box; on "half" both densities fill one value column, "1.9 hits/km²" and "3.7 hits/km²" (credit "hits/km²: our count · L. Shaw, 2025 · Zenodo"); λ in the Poisson formula flags on "one lambda"; Clarke's rectangle pulses on "Clarke chose"; on "where it held steady" everything else (title, river, boxes, labels, marks, citations) fades at once, and the area squares up (equal area) while London's hits hand over to map A's. |
| 17 Landing | The clumps in map A *[pause 0.4]* are what no aim at all looks like. If you chose map B, *[pause 0.3]* you chose the rule. | The square opens into map A's frame as B slides back in (the cold-open pair); A's header is written once its frame is there. A's 39 targets redrawn as the 0:39 red outlines on "are what"; "pure chance · misfit 2.0" under A on "no aim"; "spacing rule · misfit 271.7" under B on "map B" (the episode's measurement on the opening frame); B's frame flashes yellow on "rule". End card "Which Map Is Pure Chance?". |

## Sources (on screen)

- R. Falk & C. Konold, "Making sense of randomness: Implicit encoding as a basis for judgment",
  *Psychological Review* 104(2):301–318 (1997). (People identify randomness with an excess of
  alternation, in sequences and 2-D grids: the eye expects chance to look too even.)
- R. D. Clarke, "An application of the Poisson distribution", *Journal of the Institute of
  Actuaries* 72 (1946) 481. (Quote, 537/576, table, χ² = 1.17, P = .88.)
- L. P. Shaw & L. F. Shaw, "The flying bomb and the actuary", *Significance* 16(5):12–17
  (2019), doi:10.1111/j.1740-9713.2019.01315.x. (Factories at stake; digitised V-1 map; their
  re-creation of Clarke's rectangle.)
- S. G. Evans & K. B. Delaney, "The V1 (Flying Bomb) attack on London (1944–1945); the applied
  geography of early cruise missile accuracy", *Applied Geography* 99:44–53 (2018),
  doi:10.1016/j.apgeog.2018.07.019. (Aiming point Tower Bridge in central London; the overall
  mean point of impact lay in Dulwich, to the south, and as a consequence impact density was
  lower north of the Thames.)
- Data: L. Shaw, "V1 and V2 impact sites in London", Zenodo (2025),
  doi:10.5281/zenodo.14883986, CC-BY 4.0 (`v1_impacts.csv`, processed by `realdata.py`).
  The 1.9 / 3.7 hits per km² are our own count of it, credited as such on screen.
- River Thames: OS Open Rivers, Ordnance Survey, Open Government Licence v3 — "Contains OS data
  © Crown copyright and database right 2026" (`thames.py` → `thames_os_open_rivers.csv`). Not an
  empirical claim, so it is credited here and in the video description rather than on screen.

All verification notes are in `facts.md`; simulated map data in `sim.py` / `sim_data.npz`,
real map data in `realdata.py` / `real_data.npz`.

## Voice notes

- Speed 0.84 for every beat, `CADENCE = "shaped"` (PRODUCTION_GUIDE §4, §13.3): sentence gaps
  follow the sense, beat turns get 0.45 s, number-dense sentences are spoken 2 % slower.
- Pronunciation overrides: "Poisson" → /pwɑsˈOn/ (misaki defaults to "poison"); the map name
  "A" → /ˈA/ (misaki otherwise reads "Map A lights up" with the article "uh").
- Numbers are written as words, without "and" ("five hundred seventy-six"): Kokoro stretched
  the "and" inside numbers to 0.7–0.8 s and whisper heard two numbers.
- Planned holds: 1.2 s (+ the 0.3 s question gap) after "Which is chance?", 1.1 s after "Guess
  how many squares stay empty." (1.6 s of silence with the beat gap), 0.6 s after "Backwards.",
  0.5 s after "Map A has two hundred twenty-two.", 0.5 s after "the Poisson distribution." (the
  finished formula holds), 0.7 s after "That share, p, is point seven four." and after "p equals
  point eight eight." (about 1.2 s of silence each with the beat gap), 0.8 s after "So look
  again." (the landing transform). Beat turns: 0.55 s after the reveal, the Poisson beat and map
  B (into the insight, the honest detector and aim/the real data), so turns are audibly longer
  than full stops. Round 6: 0.8 s after "since each pair counts twice." and an 0.8 s beat gap after
  "e to the minus lambda again." (whisper heard the two-hit beat as one run), 0.6 s after "half
  as dense." (the limits beat ran 12 s without a breath), 0.9 s after the limits beat for the
  landing transform. Shorter planned breaths: 0.5 s after "lambda." (the second row is copied in
  it), 0.5 s (round 6: 0.8 s) after the "over two" clause (the two-hit beat ran 16 s without a breath at
  0.3 s), 0.3 s after "Five thirty-six is almost five thirty-seven.", 0.4 s after "compares whole histograms." (the count-by-count
  flight), 0.4 s after "extra pile-ups." (the turn to the real data; without it the beat ran
  15.8 s without a breath). Inside sentences: "Map A scores [0.2] two point oh", "The clumps in
  map A [0.4] are what no aim at all looks like", "If you chose map B, [0.3] you chose the rule"
  (Kokoro otherwise spoke these short lines at 202–254 wpm). The closing beat is at 0.82.
- Wording kept for the ear: "A pattern this even" (not "Too even", heard as "two even");
  "Aimed bombs" (not "Aim would", heard as "AIM"); "Each bomb has a one in five seventy-six chance
  of landing in this square" ("with chance one in…" held "one" for 0.52 s); "Three out of four simulated chance maps
  score worse" (round 4's "three times in four" was heard as "three times than four", and "Three in
  four" as "3 and 4"); "Each has a one in five seventy-six chance" in the two-hit beat ("with chance
  one in…" was heard as "1 and 576"); "Let's call the average…" (a bare "Call" at the start of the beat lost its
  /k/ at the clip onset and was heard as "all"); "If you chose
  map B, you chose the rule" (round 4's "you picked the one" lost its -ed). No "here" at a clause
  end (it was held for 0.67 s). No "map A's" (whisper heard "map ace"). "Now map B:" (a bare
  "Map B:" after a pause was heard as "Step B").
