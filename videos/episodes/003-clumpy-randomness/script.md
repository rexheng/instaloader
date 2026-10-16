# Episode 3 — Which Map Is Random?

(Curriculum working title: "Randomness Looks Clumpier Than You Think"; retitled in round 3
because that title gave away the cold-open answer.)

**One idea:** pure chance leaves gaps, and the gaps force clumps; so clusters alone
are not evidence of aim. The honest test scores the whole count histogram against Poisson's
prediction (the chi-squared misfit, read against simulated pure-chance maps), and a pattern
that is *too even* is the real sign of a spacing rule.

**Runtime target:** ~3:51 · ~550 words · Kokoro `af_heart` at speed 0.86 (0.83 on the
derivation beats, 0.80 on the general-k beat, 0.78 on the closing line). Narration text lives in
`narration_text.py`.

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
| 1 Cold open | Each map holds five hundred and thirty-seven hits. On one, every hit landed by pure chance. The other follows a rule. Which one is chance? *[1.5 s hold]* | Two square maps A and B ("simulated"); 537 dots rain into each while both "hits" counters count to 537. "A", "B" flag on "Which" and a GRAY "A or B?" holds the commitment under the maps through the prediction hold (fades on "Both are simulated"). |
| 2 Stakes | Both are simulated, but the question is real. In nineteen forty-four, Londoners claimed German flying bombs fell in clusters, and precise aim would put factories at risk. | "simulated" tags flag. Clarke quote "…tended to be grouped in clusters." + citation; yellow circles land on A's three densest clumps. |
| 3 Naive build | Build the detector your eye is running. Cut each map into five hundred and seventy-six squares, count the hits, and flag any square with three or more, like this one. | 24×24 grids draw; cells shade blue by count in a left-to-right sweep; one 3-hit square gets a red outline and a red ring (radius 0.35) on "this", which leaves after "Map A lights up". |
| 4 It "works" | Map A lights up with thirty-nine targets. Map B gets none. So A looks aimed, and B looks like chance. | 39 red outlines lag in on A with a live counter ("1 target" → "39 targets", singular/plural correct); B "0 targets"; tags "aimed?" / "chance?". |
| 5 Fail | Backwards. *[0.9 s]* I dropped every hit on map A at random, so all thirty-nine targets are false alarms. Map B's rule: no two hits closer than four fifths of a square. The detector, like your eye, expected chance to spread out that evenly. | Tags swap to "pure chance"; "39" stays put while "targets" lifts off and "false alarms" rises in. On "Map B's rule" both maps shrink to 0.7 and the row becomes [A][A zoom][B][B zoom] across the safe area, so each zoom sits in the gutter to its map's right and its leader lines (from a block on the map's right edge) cross no data; the hits counters step out. Both maps step back to 30 %. B's zoom: grey discs of radius 0.4 square grow on the rule sentence (never overlap). A's zoom (its densest edge block, 23 hits): 22 discs that overlap a neighbour turn RED on "spread out that evenly". Citation "Falk & Konold, 1997 · Psych. Review 104(2)" from "The detector" to the next beat. |
| 6 One square | Take one square. Each bomb has a one in five hundred and seventy-six chance of landing in it. To stay empty, all five hundred and thirty-seven must miss. | B and both zooms leave; A grows back into the left slot at full brightness (its counter returns). One empty square outlined yellow; it + the grid become 1/576; the 537 counter flies into the exponent: P(empty) = (1 − 1/576)^537. |
| 7 Prediction | Guess how many squares get no hit at all. *[1.5 s hold]* | "empty squares ≈ ?" |
| 8 Answer | About two hundred and twenty-seven squares stay empty. Map A has two hundred and twenty-two. | "≈ 0.3933" writes as the answer starts, then copies down into "0.3933 × 576 ≈ 227"; A's 222 empty squares fill yellow while the "222 empty" counter lands on the spoken number. |
| 9 Gaps → clumps | Those gaps force the clumps: the other three hundred and fifty-four squares share all the hits, one and a half each, so plenty must double up. | Red target outlines return; 537 hits / 354 squares ≈ 1.5; on "plenty" the 131 squares with 2+ hits get BLUE outlines with a live "131 squares with 2+" counter while the yellow fill leaves the empty squares (they stay visible as unshaded cells; a dimmed yellow reads olive) and the red 3+ outlines (a subset) leave, so only the blue outlines and the dots are at full strength. |
| 10 λ and e^−λ | Call the average hits per square lambda. *[0.5 s]* One minus a small slice, raised to a big power, is almost exactly e to the minus lambda. *[0.7 s]* | Map A dims uniformly to 30 %; only the one yellow square stays lit. λ = 537/576 ≈ 0.93 from the 537 counter and the 576 of 1/576; in the pause the second row is copied from the first, with λ and 537 flying in from λ's definition: = (1 − λ/537)^537; 1/576 and λ/537 flag together on "small slice"; ≈ e^−λ ≈ 0.3937. |
| 11 Two hits | For two hits, pick which two bombs land here: five thirty-seven times five thirty-six, over two, ways. *[0.6 s]* Each lands with chance one in five seventy-six, and the rest miss: e to the minus lambda again. *[0.6 s]* | P(empty) → P(0): only "empty" lifts out and "0" rises in; P(0) ≈ e^−λ moves up beside λ. A's 537 dots line up as "537 bombs"; the yellow square is enlarged; two bombs turn yellow and drop in. P(2) is written straight from the picture: 537 out of the bomb block, 536 out of the rest, 2! from the two yellow hits, (1/576)² from the big square, e^−λ from P(0). |
| 12 Poisson | Five thirty-six is almost five thirty-seven, so for any k, each two becomes a k. The powers merge into lambda to the k: the Poisson distribution. *[0.7 s]* Times five hundred and seventy-six squares, it predicts these purple bars. (speed 0.80) | "537·536 ≈ 537²" is copied out of P(2)'s numerator, 536 and 537² flag yellow; the numerator becomes 537² with the ² dropping in from that line. Then one glyph at a time (each lifts out, the k rises in yellow): P(2) → P(k), 537² → 537^k, 2! → k!, (1/576)² → (1/576)^k. 537, 576 and λ = 537/576 turn yellow; they shrink into the purple λ that flies in from λ's definition: P(k) ≈ λ^k/k! · e^−λ (λ^k purple), which rises to the top ("Poisson"). Histogram axes, purple bars and the ×5 tail inset grow on "these purple bars". |
| 13 Fix (v2) | The honest detector compares whole histograms. Map A sits on the purple bars: thirty-nine targets, and chance predicts thirty-nine. The chi-squared misfit: square each bar's gap, divide by chance's bar, and add them up. Map A scores two point oh. Pure-chance maps score worse three times in four: p equals point seven four. | Map A returns to full brightness (red outlines back); its cells fly into blue bars inside the purple outlines; red brace "39 targets" / purple "chance: 39.3" over the inset. On "The chi-squared misfit" map A and its labels dim to 35 % (its yellow fill leaves) while "χ² = Σ gap²/chance = 0.0" writes. Each bar's gap lights as a yellow sliver (bars 0–2 in the chart, 3–5+ in the ×5 inset); on "divide by chance's bar" each sliver lifts into its term (0.10 + 0.64 + 0.43 + 0.22 + 0.49 + 0.12) while the purple bars flag; on "add them up" the terms fly into the live readout, which counts to 2.0. On "Pure-chance maps" map A returns to full strength as it shrinks into a thumbnail on a yellow marker at 2.0 of a "misfit" axis, and the misfits of 20,000 simulated pure-chance maps grow as a purple histogram ("20,000 chance maps · simulated"); bins from 2.0 up brighten on "three times in four"; "p = 0.74" comes out of them. |
| 13b Map B | Map B: half the expected empty squares, a tower of single hits, and a misfit of two hundred and seventy-two. A pattern this even is the fingerprint of a spacing rule. | On "Map B" a B thumbnail (same size, labelled "B") fades in beside A's, and A's thumbnail, label, marker and p dim to 35 %; the bars morph to B's: "109", "397" labelled with flags. B's big gaps light yellow while the readout rolls 2.0 → 271.7; an arrow off the end of the misfit axis carries "B: 271.7" (copied from the readout) and A comes back to full for the comparison; it flags on "fingerprint". |
| 14 Aim + Clarke | Aimed bombs would miss the other way: extra empty squares, extra pile-ups. In nineteen forty-six, the actuary R D Clarke published this test on real flying-bomb hits: five hundred and thirty-seven, in five seventy-six squares of south London. | The misfit panel leaves; B's bars flatten; on "Aimed bombs" the left slot's frame, its "aimed · simulated" header and a "hits" counter appear first, then the simulated aimed map rains in (537 hits around 3 aim points, s.d. 2 squares) while red outline bars of its histogram grow over the purple bars on "extra empty squares" (399 empty vs 227; 58 and 37 in the middle classes) and "extra pile-ups" (39 squares with 5+), as red × marks land on the three aim points (no separate chart legend: red = aimed). Then the histogram rises, citations appear, and the **real** map rains in: 887 V-1 impact sites of the LCC area ("real V-1 hits, 1944–45"); the Thames (OS Open Rivers) draws with its label in open ground at its east end (no knockout); Clarke's 18 km × 8 km area (Shaw & Shaw's re-creation) draws in yellow, its 576 half-km squares grid in and the hits outside it dim to 35 %; "≈ Clarke's area" + GRAY "re-created". |
| 15 Payoff | Chance predicted two hundred and twenty-seven empty squares; Clarke counted two hundred and twenty-nine. Single hits: two hundred and eleven, exactly as predicted. Same test: p equals point eight eight. No sign of clustering. | Clarke's table builds under the bars with row headers "chance" (purple) and "Clarke" (blue) as his blue bars grow into the outlines (main and inset). "Poisson" on the formula line gives way to "χ² = 1.17,  p = 0.88". |
| 16 Limits | That doesn't mean the bombs were unaimed: they were aimed at London, just too loosely to choose a street. And the test needs one lambda everywhere: farther north, hits fell about half as densely, so Clarke chose an area where lambda held steady. | Histogram dims. Dots flag ("aimed at London"); a 5 km scale bar draws in the map's header row ("too loosely"); λ in the formula flags; on "Farther north" a 9 km × 5 km box north of Clarke's area draws and flashes, its hits brighten to full; "north: 1.9 hits/km²" sits left-aligned on the box, just above the hits over it; the credit becomes "hits/km²: our count · L. Shaw, 2025 · Zenodo"; Clarke's area pulses and its label extends to "≈ Clarke's area: 3.7 hits/km²". |
| 17 Landing | So look again. *[0.9 s]* The clumps in map A are what no aim at all looks like. If you picked map B, you picked the one following a rule. | Everything but Clarke's area and its hits leaves; map A's 537 hits fade in inside the yellow rectangle as London's fade out (A's reach half strength before London's drop below it), then the rectangle opens into map A's frame carrying its hits, and B slides in from the right. The same yellow circles land on A's clumps, tag "pure chance"; on "no aim at all" A's 39 targets are redrawn as the 0:39 red outlines; B's rule tag returns; B's frame flashes yellow on "rule". End card "Which Map Is Random?". |

## Sources (on screen)

- R. Falk & C. Konold, "Making sense of randomness: Implicit encoding as a basis for judgment",
  *Psychological Review* 104(2):301–318 (1997). (People identify randomness with an excess of
  alternation, in sequences and 2-D grids: the eye expects chance to look too even.)
- R. D. Clarke, "An application of the Poisson distribution", *Journal of the Institute of
  Actuaries* 72 (1946) 481. (Quote, 537/576, table, χ² = 1.17, P = .88.)
- L. P. Shaw & L. F. Shaw, "The flying bomb and the actuary", *Significance* 16(5):12–17
  (2019), doi:10.1111/j.1740-9713.2019.01315.x. (Factories at stake; digitised V-1 map; their
  re-creation of Clarke's rectangle.)
- Data: L. Shaw, "V1 and V2 impact sites in London", Zenodo (2025),
  doi:10.5281/zenodo.14883986, CC-BY 4.0 (`v1_impacts.csv`, processed by `realdata.py`).
  The 1.9 / 3.7 hits per km² are our own count of it, credited as such on screen.
- River Thames: OS Open Rivers, Ordnance Survey, Open Government Licence v3 — "Contains OS data
  © Crown copyright and database right 2026" (`thames.py` → `thames_os_open_rivers.csv`). Not an
  empirical claim, so it is credited here and in the video description rather than on screen.

All verification notes are in `facts.md`; simulated map data in `sim.py` / `sim_data.npz`,
real map data in `realdata.py` / `real_data.npz`.

## Voice notes

- Pronunciation overrides: "Poisson" → /pwɑsˈOn/ (misaki defaults to "poison"); the map name
  "A" → /ˈA/ (misaki otherwise reads "Map A lights up" with the article "uh").
- Numbers are written as words. Deliberate pause lengths: 0.9 s after "Backwards.", ~1 s after
  "Map A has two hundred and twenty-two.", 0.5 s after "Call the average hits per square lambda."
  (the second row is copied in that pause), 0.6 s after "over two, ways." and after "e to the
  minus lambda again." (round 4: the P(2) and P(k) steps get their own breath groups), 0.7 s
  after "e to the minus lambda." and after "the Poisson distribution.", 0.2 s inside the Clarke
  table read, 0.9 s after "So look again." (the transform into the cold-open maps).
- "five hundred and seventy-six squares" (not "five seventy-six") where a split would be heard as
  "five, seventy-six"; "A pattern this even" (not "Too even", heard as "two even"); "Aimed bombs"
  (not "Aim would", heard as "AIM").
