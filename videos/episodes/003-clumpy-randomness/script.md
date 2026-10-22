# Episode 3 — Which Map Is Random?

(Curriculum working title: "Randomness Looks Clumpier Than You Think"; retitled in round 3
because that title gave away the cold-open answer.)

**One idea:** pure chance leaves gaps, and the gaps force clumps; so clusters alone
are not evidence of aim. The honest test scores the whole count histogram against Poisson's
prediction (the chi-squared misfit, read against simulated pure-chance maps), and a pattern
that is *too even* is the real sign of a spacing rule.

**Runtime target:** ~3:55 · ~560 words · Kokoro `af_heart` at speed 0.86 (0.83 on the
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
| 1 Cold open | Each map holds five hundred thirty-seven bomb hits. On one, every hit landed by pure chance. The other follows a rule. Which one is chance? *[pause 1.5]* | Two square maps A and B ("simulated"); 537 dots rain into each while both "hits" counters count to 537. "A", "B" flag on "Which"; a GRAY "A or B?" holds the commitment through the 1.5 s prediction hold. |
| 2 Stakes | Both are simulated. The question isn't. In nineteen forty-four, Londoners claimed German flying bombs fell in clusters, and precise aim would put factories at risk. | "simulated" tags flag. Clarke quote "…tended to be grouped in clusters." + citation (Clarke 1946; Shaw & Shaw 2019); yellow circles land on A's three densest interior clumps. |
| 3 Naive build | Build the detector your eye is running. Cut each map into five hundred seventy-six squares, count the hits, and flag any square with three or more, like this one. | 24×24 grids draw; cells shade blue by count in a left-to-right sweep; one 3-hit square gets a red outline and a red ring on "this one". |
| 4 It "works" | Map A lights up with thirty-nine targets. Map B gets none. So A looks aimed. | 39 red outlines lag in on A with a live counter ("1 target" → "39 targets") that lands on 39 as "thirty-nine" is spoken; B "0 targets"; tags "aimed?" / "chance?". |
| 5 Fail | Backwards. *[pause 0.9]* I dropped every hit on map A at random, so all thirty-nine targets are false alarms. Map B's rule: no two hits closer than four fifths of a square. The detector, like your eye, expected chance to spread out that evenly. | Tags swap to "pure chance". On "I dropped every hit" A's hits clear and rain in again (same order and places, counter 0 → 537). "39" stays put while "targets" lifts off and "false alarms" rises in. On "Map B's rule" both maps shrink into the [A][A zoom][B][B zoom] row; B's tag "rule: spacing ≥ 4/5 square"; B's discs (radius 0.4 square) never overlap; A's 22 overlapping discs turn red on "spread out that evenly" (Falk & Konold, 1997 · Psych. Review 104(2)). |
| 6 One square | Take one square. Each bomb has a one in five hundred seventy-six chance of landing in it. To stay empty, all five hundred thirty-seven must miss. | B and the zooms leave; A grows back. One empty square outlined yellow; on "Each bomb" it and the grid become 1/576; the 537 counter flies into the exponent: P(empty) = (1 − 1/576)^537. |
| 7 Prediction | Guess how many squares get no hit at all. *[pause 1.5]* | "empty squares ≈ ?" |
| 8 Answer | About two hundred twenty-seven squares stay empty. Map A has two hundred twenty-two. | "≈ 0.3933", then "0.3933 × 576 ≈ 227"; A's 222 empty squares get a light yellow tint (40 %) inside a full-yellow outline of each empty region while the "222 empty" counter lands on the spoken number. |
| 9 Gaps → clumps | Those empty squares force the clumps: the other three hundred fifty-four squares share all the hits, one and a half each, so plenty must double up. To judge London, chance must predict every bar. | Red 3+ outlines return on "clumps"; 537 hits / 354 squares ≈ 1.5; on "plenty" the 131 squares with 2+ hits get BLUE outlines with a live counter while the yellow tint, its outline and the "222 empty" label leave and the blue shading drops to 40 %. On "To judge London" the histogram axes appear with chance's bar 0 (227, purple) and GRAY "?" over 1, 2, 3, 4, 5+ on "every bar". |
| 10 λ and e^−λ | Call the average hits per square lambda. *[pause 0.5]* One minus a small slice, raised to a big power, is almost exactly e to the minus lambda. *[pause 0.5]* | The preview axes step aside; map A dims to 30 %; λ = 537/576 ≈ 0.93 from the 537 counter and the 576 of 1/576; second row = (1 − λ/537)^537 ≈ e^−λ ≈ 0.3937 (λ and 537 fly in from λ's definition). |
| 11 Two hits | For two hits, pick which two bombs land here: five thirty-seven times five thirty-six ways, over two, since order doesn't matter. *[pause 0.4]* Each lands with chance one in five seventy-six, and the rest miss: e to the minus lambda again. *[pause 0.4]* | P(0) ≈ e^−λ; A's 537 dots line up as "537 bombs"; the yellow square is enlarged; two bombs turn yellow and drop in. 537 out of the bomb block, 536 out of the rest, 2! from the two yellow hits; on "order doesn't matter" the two hits trade places. (1/576)² from the big square, e^−λ from P(0). |
| 12 Poisson | Five thirty-six is almost five thirty-seven. *[pause 0.4]* For three hits, each two becomes a three; for any k, a k. *[pause 0.6]* The powers merge into lambda to the k: the Poisson distribution. *[pause 0.7]* Times five hundred seventy-six squares, it predicts these purple bars. | In place: the 536 lights up and becomes a 537; 537·537 folds into 537². On "each two" all four 2s light up, on "becomes a three" they turn to 3s (P(3) ≈ 537³/3!…), on "k" to k's. 537, 576 and λ = 537/576 light up and shrink into the purple λ^k: P(k) ≈ λ^k/k! · e^−λ, named "Poisson" on the word and held through the pause; it rises to the top on "Times", the axes return with "squares = 576·P(k)", and the purple bars and ×5 tail inset grow on "these purple bars". |
| 13 Fix (v2) | The honest detector compares whole histograms. *[pause 0.8]* Thirty-nine targets, and chance predicts thirty-nine. The chi-squared misfit: square each bar's gap and divide by chance's bar, so a miss of two on seven outweighs a miss of five on two hundred twenty-seven. Add them up: map A scores two point oh. Three in four simulated chance maps score worse. *[pause 0.3]* That share, p, is point seven four. | Map A returns with its blue shading and red outlines (no yellow). Count by count, the k-hit squares outline in BLUE and copies of exactly those squares fly into bar k. Red brace "39 targets"; chance's tail bars flag and "chance: 39.3" writes. "χ²_A = Σ gap²/chance" writes as A dims to 35 %; yellow gap slivers grow, lift into their terms (0.10 … 0.12); the 4-hit bar (miss ≈ 2 on 7.1 → 0.49) and the 0-hit bar (miss ≈ 5 on 227 → 0.10) flag on their words; the terms fly into the readout, 2.0. A shrinks to a dots-and-frame thumbnail on a yellow marker at 2.0 of a "misfit" axis with a "maps" axis; the 20,000 simulated chance maps grow; bins from 2.0 up brighten on "score worse"; "p = 0.74" comes out of them on "That share, p". |
| 13b Map B | Map B: half the expected empty squares, a tower of single hits, and a misfit of two hundred seventy-two. A pattern this even is the fingerprint of a spacing rule. | B's dots-and-frame thumbnail appears past the end of the misfit axis, where its score will land; the subscript becomes χ²_B; bars morph to B's ("109", "397" flagged); B's gaps light yellow while the readout rolls to 271.7; after it settles, "B: 271.7" leaves it with an arrow off the axis. |
| 14 Aim + Clarke | Aimed bombs would miss the other way: extra empty squares, extra pile-ups. In nineteen forty-six, the actuary R D Clarke published this test on real flying-bomb hits: five hundred thirty-seven, in five hundred seventy-six squares of London. | The aimed map: frame, DIM grid, header and counter, then 537 hits rain in around 3 aim points; on "extra empty squares" its 399 empties tint and outline yellow while red outline bars grow over chance's; red × on the aim points on "pile-ups". The red bars ride the chart up while they fade. The real map rains in (887 V-1 sites; Thames; citations Clarke 1946 and Shaw & Shaw 2019 at 20); Clarke's area (re-created) draws, grids into 576 squares; hits outside dim. |
| 15 Payoff | Chance predicted two hundred twenty-seven empty squares; Clarke counted two hundred twenty-nine. *[pause 0.2]* Single hits: two hundred eleven, exactly as predicted. *[pause 0.2]* Same test: p equals point eight eight. | Clarke's table builds under the bars ("chance" purple, "Clarke" blue) as his bars grow into the outlines; "Poisson" gives way to "χ² = 1.17, p = 0.88". |
| 16 Limits | The bombs were aimed, at Tower Bridge, but half fell outside this circle, more than twelve kilometres away. And the test needs one lambda everywhere: farther north, hits were about half as dense, so Clarke chose an area where lambda held steady. | The chart leaves; "≈ Clarke's area" moves onto the rectangle's row in a column east of the map. A red × lands on Tower Bridge (Evans & Delaney, 2018 · Applied Geography 99 joins the citation line); on "half" a red circle of radius 12.5 km with its radius and "12.5 km" draws: it encloses the whole county map. On "one lambda" the circle leaves and λ flags. On "farther north" the north box draws, its hits brighten, "north" appears on its row; "1.9 hits/km²" and, on "Clarke chose", "3.7 hits/km²" fill the same value column (credit "hits/km²: our count · L. Shaw, 2025 · Zenodo"). |
| 17 Landing | So look again. *[pause 1.2]* The clumps in map A are what no aim at all looks like. If you chose map B, you chose the one following a rule. | Everything but Clarke's area leaves; London's hits fade as the rectangle becomes a square of equal area; map A's hits appear in it at their true geometry; the square opens into map A's frame and B slides in. Yellow circles on A's clumps, tag "pure chance"; A's 39 targets redrawn as the 0:39 red outlines; B's tag "rule: spacing ≥ 4/5 square"; B's frame flashes yellow on "rule". End card "Which Map Is Random?". |

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
  doi:10.1016/j.apgeog.2018.07.019. (Aiming point Tower Bridge; CEP-T 12.5 km: half the V-1s
  launched at London fell more than 12.5 km from it.)
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
- Numbers are written as words, without "and" ("five hundred seventy-six"): Kokoro stretched
  the "and" inside numbers to 0.7–0.8 s and whisper heard two numbers. Deliberate pauses: 0.9 s
  after "Backwards.", 0.5 s after "Call the average hits per square lambda." (the second row is
  copied in it), 0.4 s after "since order doesn't matter." and after "e to the minus lambda
  again.", 0.4 s after "Five thirty-six is almost five thirty-seven.", 0.6 s after "for any k, a
  k.", 0.7 s after "the Poisson distribution." (the finished formula holds), 0.8 s after
  "compares whole histograms." (the count-by-count flight into the bars), 0.3 s before "That
  share, p", 0.2 s inside the Clarke table read, 1.2 s after "So look again." (the landing
  transform).
- "five hundred seventy-six squares" where a split would be heard as "five, seventy-six"; "A
  pattern this even" (not "Too even", heard as "two even"); "Aimed bombs" (not "Aim would", heard
  as "AIM"); "Three in four simulated chance maps score worse" (round 4's "three times in four"
  was heard as "three times than four"); "If you chose map B, you chose" (round 4's "you picked
  the one" lost its -ed).
