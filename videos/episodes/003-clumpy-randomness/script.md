# Episode 3 — Which Map Is Pure Chance?

(Curriculum working title: "Randomness Looks Clumpier Than You Think"; retitled in round 3
because that title gave away the cold-open answer. Round 6: "Which Map Is Random?" became
"Which Map Is Pure Chance?" on the end card, because map B is generated at random too, by
random sequential addition with a spacing rule.)

**One idea:** pure chance leaves gaps, and the gaps force pile-ups; so clusters alone
are not evidence of aim. The honest test scores the whole count histogram against Poisson's
prediction (the chi-squared misfit, read against simulated pure-chance maps), and a pattern
that is *too even* is the real sign of a spacing rule.

**Runtime target:** 3:15–3:37 · ≤ 500 words (500 in round 8) · Kokoro `af_heart` at speed 0.84 with
`CADENCE = "shaped"` (gaps follow the sense; 0.9–1.0 s holds after the key results: 222 vs 227,
the Poisson formula, p = 0.74, p = 0.88; 0.6 s after the 183 line). Narration text lives in `narration_text.py`.

## Palette (colour → one meaning, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | observed hit counts: cell shading by count, the "2+ hits" outlines and counter, observed histogram bars, London's numbers |
| PURPLE | pure chance: the Poisson prediction (bars, formula, λ, λ^k, e^−λ), the "pure chance" tag, the "chance" table row, the 20,000 simulated chance maps and their p |
| RED | what the eye/detector flags as a clump or what aim would do: detector outlines, "targets", "false alarms", hit pairs closer than B's rule allows, aim arrows |
| YELLOW | focus: the one square, the empty squares (a full-yellow marker half a square wide in each, no outline), the term being discussed, each bar's gap and its misfit term, map A's score marker, Clarke's area on the real map |
| INK / GRAY / DIM | text and dots / axes, secondary labels, the Thames, neutral exclusion discs / grid. GRAY text is #A6ABB5 in this episode (7.9:1 on the background) |

Dots are INK (raw hits, neutral) so they stay visible on shaded cells. Flags are colour-only
(no scaling), so a flagged frame or bar never grows into its labels.

## Beats

| # | Narration | Picture |
|---|---|---|
| 1 Cold open | Each map holds five hundred thirty-seven bomb hits. One is pure chance; the other follows a rule. Which is chance? *[pause 1.2]* | Two square maps A and B ("simulated"); 537 dots rain into each while both "hits" counters count to 537. "A", "B" flag on "Which"; a GRAY "A or B?" holds the commitment through the 1.5 s prediction hold. |
| 2 Stakes | In nineteen forty-four, Londoners saw flying bombs land in clusters. If that meant precise aim, factories were at risk. | "A or B?" gives way to the citation. Clarke quote "…tended to be grouped in clusters." + citation (Clarke 1946; Shaw & Shaw 2019); yellow circles land on A's three densest interior clumps. |
| 3 Naive build | Build the detector your eye is running. Cut each map into five hundred seventy-six squares, and flag any square with three or more hits, like this one. | 24×24 grids draw; cells shade blue by count in a left-to-right sweep; one 3-hit square gets a red outline and a red ring on "this one". |
| 4 It "works" | Map A lights up with thirty-nine targets, map B with none. So A looks aimed. | 39 red outlines lag in on A with a live counter ("1 target" → "39 targets") that lands on 39 as "thirty-nine" is spoken; B "0 targets"; tags "aimed?" / "chance?". |
| 5 Fail | Backwards. *[pause 0.6]* I dropped every hit on map A at random, so all thirty-nine targets are false alarms. Map B's rule: no two hits closer than four fifths of a square. Your eye, like the detector, expects chance to look that even. | Tags swap to "pure chance". On "I dropped every hit" A's hits, shading and red outlines clear and the hits rain in again (counter 0 → 537; targets 0 → 39). "39" stays while "targets" gives way to "false alarms". On "Map B's rule" both maps shrink into the [A][A zoom][B][B zoom] row. Both zooms are the 4×4 edge block whose count is closest to the 16-hit average (round 7: A's used to be its densest block): B's 16 discs (radius 0.4 square) never overlap; 14 of A's 16 overlap and turn red on "that even" (Falk & Konold, 1997 · Psych. Review 104(2)). |
| 6 Guess first | Almost one hit per square. Guess how many squares stay empty. *[pause 1.1]* | B and the zooms leave; A grows back with its grid; its hits counter comes back beside it as the GRAY data line "537 hits · 576 squares" ("· 576 squares" written as the grid flashes on "per square"). On "Guess" a lone yellow "empty squares ≈ ?" is written and held (1.6 s of silence): nothing to compute yet. |
| 7 One square | Each bomb has a one in five seventy-six chance of landing in this square. To stay empty, all five hundred thirty-seven must miss. *[pause 0.4]* | One empty square is outlined yellow on "Each bomb". On "one in" the square and the grid become 1/576, written beside the square on a knockout; on "this square" the square pulses; on "To stay empty" P(empty) = (1 − … ) is written and the 1/576 flies into its slot; on "all five hundred thirty-seven" the data line's 537 is carried into the exponent on an arc above the row; "≈ 0.3933" writes on "must miss"; in the pause the question takes the method: "empty squares ≈ 576 × 0.3933 ≈ ?" (576 and 0.3933 each fall straight down from P(empty); "empty squares" and "?" keep their glyphs). |
| 8 Answer | About two hundred twenty-seven: four squares in ten. *[pause 0.3]* Map A has two hundred twenty-two. *[pause 0.3]* | On "two hundred" only the "?" swaps to a yellow 227; on "four squares in ten" the 0.3933 flags. On "Map A" the blue shading and the dimmed red outlines go to 0, the hits drop to 60 % and a yellow marker appears in each of the 222 empty squares, left to right, as the "222 empty" counter runs. |
| 9 Gaps → pile-ups | Those empty squares force pile-ups: *[pause 0.3]* a hundred eighty-three hits must land where another already did. *[pause 0.5]* | On "Those" the markers flash; on "pile-ups" they turn grey, the 131 squares with 2+ hits get blue outlines, the blue shading returns at 40 % and the hits return to full strength; then the 227 line leaves and "537 − (576 − 222)" is built: its 576 slides into place, 537 is written as the data line's 537 lights up, the 222 counter is carried in; "= 183 extra hits" (blue) writes on "eighty-three"; the blue outlines pulse on "already". (Round 7: the spoken 354 and the forward line "To judge London…" are cut, with their preview chart.) |
| 10 λ and e^−λ | Let's call the average hits per square lambda. *[pause 0.5]* One minus a small slice, raised to a big power, is e to the minus lambda, almost exactly. Call that P of zero. | On "the average hits per square" the data line's 537 and 576 become λ's fraction in place (hits over squares; "hits", "·", "squares" fade), while the 183 line, the grey empties and their count leave and P(empty) rises; on "lambda" "λ =" and "≈ 0.93" write, map A dims to 30 % and the second row's frame "= (1 − ·/·)^537" is written in place under the first; then λ and 537 are written into the slice as λ (in λ = 537/576) and the row's exponent light up. On "small slice" the slices flag and a small plot of (1 − λ/n)^n against n (log axis: 1, 2, 5, 20, 537) draws under the row; on "raised to a big power" its five dots drop in, climbing 0.068 → 0.285 → 0.356 → 0.385 → 0.3933, while the exponent flags; on "e to the minus lambda" "≈ e^−λ ≈ 0.3937" writes and the purple dashed e^−λ line draws over the dots; on "almost exactly" 0.3933, 0.3937 and the n = 537 dot flag; on "Call that" "empty" lifts out, on "zero" a yellow 0 rises in beside ")", then "P(" closes up. |
| 11 Two hits | For two hits in this square, pick two bombs: five thirty-seven times five thirty-six ways, over two, since each pair counts twice. *[pause 0.6]* Each has that same chance, and the rest miss: e to the minus lambda again. *(0.9 s beat gap)* | One move per phrase: on "For two hits" the rows and the plot collapse to P(0) ≈ e^−λ and λ moves aside; on "this square" the yellow square is enlarged with its 1/576; on "pick two bombs" A's 537 dots line up as "537 bombs", then two turn yellow and drop in. On "five thirty-seven" the block lights and "537" is carried out of its label; on "five thirty-six" the other 536 light; on "over two" 2! writes; on "each pair counts twice" the two hits trade places. On "that same chance" the 1/576 lands on the fraction inside (1/576)², then its brackets and the square are written as the two hits flash; on "the rest miss" the other 535 dim; e^−λ is copied from P(0). In the 0.9 s gap, on screen only, the 536 lifts out and a yellow 537 rises in its place. |
| 12 Poisson | For three hits, each two becomes a three; for any k, a k. *[pause 0.5]* The powers merge into lambda to the k: the Poisson distribution. *[pause 0.5]* Times five seventy-six squares, it predicts these purple bars. | On "For three hits" 537·537 folds into 537² while the picture steps back. On "each two" all four 2s light up, on "becomes a three" they turn to 3s (P(3) ≈ 537³/3!…), on "k" to k's. 537, 576 and λ = 537/576 light up and shrink into the purple λ^k: P(k) ≈ λ^k/k! · e^−λ, named "Poisson" on the word and held through the pause; it rises to the top on "Times", the axes return, P(k) is copied down into the axis title and "= 576·" is written in front of it once it has landed ("squares = 576·P(k)"), and the purple bars and ×5 tail inset grow on "these purple bars". |
| 13 Fix (v2) | The honest detector compares whole histograms. *[pause 0.4]* Thirty-nine targets, and chance predicts thirty-nine. *[pause 0.4]* The chi-squared misfit squares each bar's gap and divides by chance's bar, because short bars wobble less: a miss on a short bar counts more. / Map A scores two point oh. *[pause 0.6]* (its own beat, at 0.80) / Three out of four simulated chance maps score worse. That share, p, is point seven four. *[pause 0.7]* | Count by count, the k-hit squares fly into bar k. Red brace "39 targets"; "chance: 39.3". "χ²_A = Σ gap²/chance = ?" writes; yellow gap slivers grow and lift into their terms; on "wobble" INK whiskers (unlabelled: 1 s.d. of chance's own bars, 11.7 on bar 0 and 2.65 on bar 4 in the ×5 inset) show how much chance's bars vary; on "short bar" the 4-hit sliver, its 0.49, its whisker and chance's 7.1 bar flag. On "Map A scores" each term flags in place (LaggedStart) while the readout steps 0.10, 0.74, 1.17, 1.39, 1.88, 2.00. A shrinks to a thumbnail on a yellow marker at 2.0 of a "misfit" axis, and in the pause the null run's first three maps appear in a row beside it, tagged 3.7, 2.1, 2.8 below; on "simulated chance maps" the tags step back and each map shrinks into a purple dot that lands in its bin and stays, then the bins of all 20,000 grow behind the dots; bins from 2.0 up brighten on "score worse"; "p = 0.74" comes out of them on "That share, p". |
| 13b Map B | Now map B: half the expected empty squares, a tower of single hits, misfit two hundred seventy-two. *[pause 0.3]* A pattern this even is the fingerprint of a spacing rule. | B's dots-and-frame thumbnail appears past the end of the misfit axis, where its score will land; the subscript becomes χ²_B and A's 2.0 gives way to "?"; bars morph to B's and the purple "227" leaves; on "half" B's bar 0 is ringed in INK and chance's outline flashes INK; on "tower" B's bar 1 is ringed in INK and "397" (blue) is written above it (no fill changes: yellow in the chart means only gap); the Poisson line is hidden for this stretch (it returns at the aimed map); the two values leave, then B's gaps light yellow while the readout counts up to 271.7; "B: 271.7" with an arrow off the axis; on "this even" B's thumbnail and its score light up. |
| 14 Aim + Clarke | Aimed bombs would break the fit the other way: extra empty squares, extra pile-ups. *[pause 0.4]* In nineteen forty-six, R D Clarke published the same test on London's real hits: five thirty-seven in five seventy-six squares. | The aimed map: frame, DIM grid, header and counter, then 537 hits rain in around 3 aim points; on "extra empty squares" its 399 empties get yellow markers while red outline bars grow over chance's; on "pile-ups" the empties turn grey and red × land on the aim points. On "nineteen forty-six" the aimed map leaves (the red bars ride the chart up while they fade) as the real map starts to rain in half a second later (887 V-1 sites; the title is written on "nineteen forty-six", the Thames arrives on "London's real hits"; citations Clarke 1946 and Shaw & Shaw 2019); Clarke's area (re-created) draws on "five thirty-seven", grids into 576 squares on "five seventy-six"; hits outside dim. |
| 15 Payoff | Chance predicted two hundred twenty-seven empty squares; Clarke counted two hundred twenty-nine. *[pause 0.3]* Overall, p equals point eight eight. *[pause 0.5]* London's clusters were no sign of precise aim. | Clarke's table builds under the bars ("chance" purple, "Clarke" blue) while the title and "Thames" dim to 35 %; on "Clarke counted" his bars grow into the outlines with his row of counts; "χ² = 1.17" on "Overall", "p = 0.88" on "p equals"; the 3+ columns and the ×5 inset are ringed on "clusters". |
| 16 Limits | The bombs were aimed at central London but tended to fall short, so farther north, hits were about half as dense. *[pause 0.6]* Score the north alone, and it fits chance too: p equals point four five. *[pause 0.3]* The aim hides in lambda, which the test holds fixed. *(0.9 s beat gap: the area squares up)* | The chart leaves and the context hits outside both boxes step back to 18 %; the real map grows ×1.35 into the frame with "≈ Clarke's area" below the rectangle. On "London" a red × lands on Tower Bridge (citation "aim: Evans & Delaney, 2018 · Applied Geography 99"); on "fall short" a red arrow grows to Dulwich. On "farther" the north box draws with its own 180 half-kilometre squares, its hits brighten, "north" above it; on "about half" "· λ = 0.48" completes it and "· λ = 0.93" completes Clarke's label (credit "λ north: our count · L. Shaw, 2025 · Zenodo"). On "Score the north alone" the map shrinks back beside the chart with each label riding on its box, "Thames" leaves and the north's own axes come in (0–120 squares, no inset); its purple Poisson bars and the purple row "chance 112 53.3 12.7 2.0 0.2 0.0" grow, then on "fits chance" its blue bars and the blue row "north 115 46 17 2 0 0"; "p = 0.45" writes where p = 0.88 sat. On "aim" the × and arrow flag; on "lambda" the formula's λ and both areas' λ labels light up together; on "holds fixed" the two λ values and the fall-short arrow flash; then everything but Clarke's area fades and the area squares up while London's hits hand over to map A's. |
| 17 Landing | The clumps in map A *[pause 0.4]* are what no aim at all looks like. *[pause 0.9]* If you chose map B, *[pause 0.3]* you chose the rule. | The square opens into map A's frame as B slides back in (the cold-open pair). A's 39 targets redrawn on "are what"; "pure chance · misfit 2.0" under A on "no aim"; "spacing rule · misfit 271.7" under B on "map B"; B's frame flashes yellow on "rule". The A/B frame fades out fully (0.35 s), then the end card (INK Ω) fades in. |

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
  The north box's λ = 0.48 (86 hits in 180 squares) is our own count of it, credited as such on screen.
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
- Round 8: the guess is "Almost one hit per square. Guess how many squares stay empty. [pause 1.2]"
  (1.65 s of silence with the beat gap); "Map A scores two point oh." is its own beat at 0.80 with
  no internal pause (whisper heard "Map A scores. 2.0."); a 0.9 s hold between the landing's two
  sentences (whisper ran them together); "Aimed bombs would break the fit the other way" ("miss"
  was heard as bombs missing their targets).
- Planned holds: 1.2 s (+ the 0.3 s question gap) after "Which is chance?", 0.6 s after "Backwards.",
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
