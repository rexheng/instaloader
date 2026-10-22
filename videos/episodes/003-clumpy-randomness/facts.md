# Episode 3 — facts and verification

Every number spoken or shown, how it was checked, and the source. Simulations are in
`sim.py` (deterministic; `python3 sim.py` reprints the checks); the real V-1 map numbers are in
`realdata.py` (`python3 realdata.py`). Both simulated maps on screen are labelled "simulated";
the London map is labelled "real V-1 hits".

## Real-world anchor

| Claim (as used in the episode) | Verification | Source |
|---|---|---|
| During the 1944 flying-bomb attack on London, "frequent assertions were made that the points of impact of the bombs tended to be grouped in clusters." (on-screen quote: "tended to be grouped in clusters") | Read on the scanned original page (JIA 72, p. 481); also quoted verbatim in Shaw & Shaw 2019 | R. D. Clarke, "An application of the Poisson distribution", *Journal of the Institute of Actuaries* 72 (1946), p. 481, doi:10.1017/S0020268100035435 |
| Londoners claimed the bombs fell in clusters | Clarke: "frequent assertions"; Shaw & Shaw: "As Londoners observed at the time, there are multiple clusters" | Clarke 1946; Shaw & Shaw 2019 |
| If the bombs could be aimed precisely, factories (the war effort) were at risk | Shaw & Shaw: "if it could be accurately targeted at munitions factories it would also become a strategic threat to the war effort" | Shaw & Shaw 2019, *Significance* 16(5):12–17, doi:10.1111/j.1740-9713.2019.01315.x |
| These were V-1 flying bombs (not V-2 rockets) | Clarke says "flying bombs"; Shaw & Shaw identify them as V-1s | Shaw & Shaw 2019 |
| Clarke was an actuary | Byline: "R. D. Clarke, F.I.A., of the Prudential Assurance Company, Ltd." | Clarke 1946 |
| "In nineteen forty-six, the actuary R D Clarke **published** this test on real flying-bomb hits" (round 2 said "ran this test" in 1946) | The paper appeared in 1946; the analysis itself was done earlier, during the war ("recently had occasion to make in the course of a practical investigation"). "Published" is exactly right; the narration no longer dates the analysis | Clarke 1946; Shaw & Shaw 2019 |
| 144 km² of south London, 576 squares of ¼ km², 537 bombs | Read on the original page | Clarke 1946 |
| "Clarke chose an area where lambda held steady" | Clarke chose the area so that "the theoretical mean density was not subject to material variation" | Clarke 1946 |
| Table: squares with 0,1,2,3,4,5+ hits — expected 226.74, 211.39, 98.54, 30.62, 7.14, 1.57; actual 229, 211, 93, 35, 7, 1 | Read on original page; expected column recomputed exactly (`sim.py`: 576·Poisson(537/576)) | Clarke 1946 |
| (round 4) The blue row is headed "Clarke" (was "London"; "Clarke, 1946" would collide with the citations beside it, and the citation "R. D. Clarke, 1946 · J. Inst. Actuaries 72:481" sits right there) and the narration says "Clarke counted two hundred and twenty-nine" (was "London had") | Round-3 substance review: next to the re-created, gridded rectangle (whose 532 dots count 237, 189, 115, 28, 6, 1) the header "London" let "Single hits: 211, exactly as predicted" read as a claim about the squares on screen. The bars and the row are Clarke's own counts of his 537 hits; the rectangle now carries a GRAY "re-created" tag beside "≈ Clarke's area" | Clarke 1946; `realdata.py` |
| What aim/clustering would look like: extra empty squares and extra pile-ups | Clarke: "an excess number of squares containing either a high number of flying bombs or none at all, with a deficiency in the intermediate classes" | Clarke 1946 |
| "Same test: p = 0.88" | Clarke: χ² = 1.17, 4 degrees of freedom, P = .88; recomputed χ² = 1.171, p(df 4) = 0.883 (Shaw & Shaw's supplement recreates 0.8832 and explains why df = 4: six classes − 1 − 1 estimated λ). The episode's own A/B tests use the same six classes and df = 4 | Clarke 1946; Shaw & Shaw supplementary analysis (2019) |
| "No sign of clustering" | Clarke: the result "lends no support to the clustering hypothesis" | Clarke 1946 |
| (round 5, final) "The bombs were aimed at central London but tended to fall short, so farther north, hits were about half as dense. The test needs one lambda: Clarke chose an area where it held steady." On screen: a red × at Tower Bridge on "London", a red arrow from it to Dulwich on "fall short", the north box with "north 1.9 hits/km²" beside "≈ Clarke's area 3.7 hits/km²"; citation "Evans & Delaney, 2018 · Applied Geography 99" | Re-verified in the paper (McGill-hosted PDF of *Applied Geography* 99:44–53, read 2026-10-22). **Aim:** "Published sources (e.g., Howard, 1990; Hölsken, 1994; Jones, 1978; Young, 1978) give Tower Bridge as the aiming point whereas a number of archival documents assume … Charing Cross Station 'or thereabouts' … These aiming points are within a circle of 1.7 km radius in Central London"; the paper adopts "a nominal primary aiming point … Tower Bridge at 51.505°N/0.075°W". "Central London" is true of either aiming point; the × marks Tower Bridge (OS grid TQ 336 802 → E 533.6 km, N 180.2 km, same transform as the hits). **Fell short:** "The overall MPI [mean point of impact] calculated by British analysts for the main V1 attack … did not, however, correspond to the nominal aiming point … located in Dulwich" (overall MPI of 2,111 V-1 impacts, 22 June – 31 August 1944; "this bias is less than 4% of the range from launch ramps in France"); Shaw & Shaw 2019 say the same in their words: the V-1s tended to "fall short of the centre of London, on less densely populated suburbs", and "the distribution of V-1s was not uniformly random over London but was skewed to the south". The arrow ends at Dulwich Village (TQ 333 735 → E 533.3, N 173.5): the paper names the district, not a point, so the arrow head is approximate to about 1 km. **The causal link to the north box:** Evans & Delaney: "as a consequence of this bias, V1 impact density was less in the densest populated boroughs north of the Thames … than would have been the case with a smaller bias". **Half as dense:** our count, see the north-box row below (1.91 vs 3.73 hits/km², ratio 0.51) | S. G. Evans & K. B. Delaney, "The V1 (Flying Bomb) attack on London (1944–1945); the applied geography of early cruise missile accuracy", *Applied Geography* 99 (2018) 44–53, doi:10.1016/j.apgeog.2018.07.019; Shaw & Shaw 2019; `real_data.npz` |
| (cut in the second round-5 pass) "half fell more than twelve kilometres away, outside this circle and off this map" (CEP-T 12.5 km, the red circle) | Verified (Evans & Delaney: "50% of the cruise missiles launched at London fell within a circle with radius 12.5 km … centred on Tower Bridge"; the circle holds 873 of the map's 887 hits), but it made a second limit beside "one lambda". PRODUCTION_GUIDE §13 budgets one honest limit of ≤ 15 s with no new terms, so the limit is now the bias that *causes* the varying lambda | Evans & Delaney 2018 |
| (removed in round 5) "aimed at London, just too loosely to choose a street" | Round-5 substance review: a qualitative accuracy claim with no specific source. Replaced by the sourced CEP figure above | — |

## The real V-1 map (new in round 1 revisions)

Data: L. Shaw, "V1 and V2 impact sites in London", Zenodo, doi:10.5281/zenodo.14883986
(CC-BY 4.0), file `V1-impacts.csv`, md5 `6fc152898e06207014322ca4481ccbf6`, copied unchanged to
`v1_impacts.csv`. It lists every V-1 impact site marked on the London County Council bomb damage
maps (Ward 2015), digitised for Shaw & Shaw 2019, with British National Grid eastings/northings.

| Claim / on-screen element | Check (`python3 realdata.py`) |
|---|---|
| 887 dots, "real V-1 hits, 1944–45" | 887 rows; the V-1 campaign on London ran June 1944 – March 1945 (Shaw & Shaw: "Over the following nine months") |
| Yellow rectangle "≈ Clarke's area", gridded into 576 squares | Clarke did not publish his grid's location. The Zenodo record gives Shaw & Shaw's re-creation: easting 525–543 km, northing 172–180 km = 18 km × 8 km = 144 km² = 36 × 16 = 576 squares of 500 m. Hence the "≈". It holds 532 of the dataset's hits (Clarke counted 537; the LCC maps may not cover all of his area, per Shaw & Shaw). The histogram on screen is Clarke's own 1946 table, not a recount of these dots |
| (not on screen) the re-created area also fits chance | 532 hits: 237, 189, 115, 28, 6, 1 squares with 0…5+ hits; λ = 0.924. Our Pearson goodness-of-fit test (the test the episode uses): χ² = 6.2, df 4, p = 0.18. **Shaw & Shaw publish p = 0.70 for the same table** ("chi-squared test: p = 0.70", Significance 2019). The two figures come from different procedures: their supplementary code (§3.2) runs R's `chisq.test` on the two-column table (expected, actual), i.e. a homogeneity test that treats the Poisson expectations as a second sample; that gives χ² = 3.06, df 5, p = 0.69 ≈ 0.70 (recomputed with `scipy.stats.chi2_contingency`). Either way the re-created area does not reject chance. Not on screen |
| The yellow rectangle crosses the Thames | Shaw & Shaw's re-creation (E 525–543, N 172–180 km) includes a strip north of the river (Chelsea to the Isle of Dogs): 20.6 km² of it lies north of the OS Thames centreline, holding 56 of its 532 hits (2.7 hits/km², vs 3.9 south of the river; point-in-polygon against `thames_os_open_rivers.csv`). Clarke only says "south London"; the rectangle is labelled "≈ Clarke's area" with a "re-created" tag. Because of this strip, round 4 no longer says "north of the river" (see next rows) |
| "3.7 hits/km²" in Clarke's area | Clarke: 537/144 = 3.73; Shaw & Shaw's rectangle: 532/144 = 3.69 |
| "Farther north, hits fell about half as densely": box "north: 1.9 hits/km²" (round 3 said "north of the river", over a rectangle that itself straddles the river; round-3 substance fix 2) | Box easting 526–535 km, northing 181–186 km (45 km², wholly north of the Thames, wholly north of the rectangle's N 180 km edge, and inside the County of London): 86 hits → 1.91 per km², ratio 0.52 to Clarke's area (537/144 = 3.73) or to the re-created area (532/144 = 3.69). One-density test (binomial share of the two boxes' 618 hits vs their area share): p = 1.2 × 10⁻⁹. The box is drawn and flashed on "Farther north"; the river is no longer flashed |
| 5 km scale bar | drawn at the data's own scale (0.2 scene units per km) |
| River Thames line (new in round 2) | OS Open Rivers (Ordnance Survey, GeoPackage, downloaded 2026-10-15, zip md5 4b62effb1c7980f3320d400b76b4f4b0), Open Government Licence v3: "Contains OS data © Crown copyright and database right 2026". Already in British National Grid metres, so it uses the same transform as the V-1 sites. `thames.py` walks the tidal main channel through the watercourse network from Putney (E 521.3 km) past Woolwich and writes `thames_os_open_rivers.csv` (152 vertices); `realdata.py` stores it in `real_data.npz`. Shaw & Shaw's own supplementary figures also draw the Thames (from geotheory's londonShapefiles) |
| The north box is north of the river | Highest point of the Thames below the box's eastings: N 180.68 km; the box starts at N 181 km (`realdata.py` prints this) |
| "hits/km²: our count · L. Shaw, 2025 · Zenodo" credit on the 1.9 / 3.7 labels | The densities are this channel's count of the Zenodo data, not figures from the paper, so they carry their own credit (round-2 substance fix 6) |
| Real-map dot radius 0.035 (not the series' 0.05) | One of Clarke's 0.5 km squares is 0.1 scene units wide; at radius 0.05 a dot is as wide as a square and the 532 dots in the rectangle merge into a block that hides the grid. Radius 0.035 keeps each dot inside a square (9 px across at 1080p) |

**Why the round-1 "whole county p = 0.02" was removed.** Shaw & Shaw's published whole-map
figure (p = 0.02) came from one random circle-sampling simulation. Their own supplementary
analysis (lukefshaw.netlify.app, archived in the Zenodo record as
`flying-bomb-supplementary-analysis.html`, §4.4) says a re-run gives p = 0.148–0.157 and that p
varies widely across simulation seeds. Quoting 0.02 as "it fails" would overstate a fragile
number, so the limit is now shown with a robust, directly computed quantity from the same
data: the hit density north of the Thames is about half that of Clarke's area. (Also checked:
pooling the two boxes (756 squares) and running the count-histogram test gives χ² = 10.0,
df 4, p = 0.04, far weaker evidence than the density comparison — the histogram test alone has
little power against a smooth density gradient, which is exactly why Clarke
restricted himself to an area of constant density.) Shaw & Shaw's statement that "the
distribution of V-1s was not uniformly random over London but was skewed to the south" is
consistent with the density comparison.

## The mathematics (exact recomputation)

| Claim | Check |
|---|---|
| λ = 537/576 ≈ 0.93 | 0.932292 |
| One bomb lands in a given square with probability 1/576 | uniform landing over 576 equal squares |
| P(square empty) = (1 − 1/576)^537 ≈ 0.3933 (on screen; round 4 no longer reads it aloud) | 0.393332 |
| **On screen "0.3933 × 576 ≈ 227"** (round 1 showed "0.39 × 576 ≈ 227", which is false: 224.6) | 0.3933 × 576 = 226.54 → 227 to the nearest square; exact 576 × 0.393332 = 226.56 |
| 1/576 = λ/537, so (1 − 1/576)^537 = (1 − λ/537)^537 | λ/537 = (537/576)/537 = 1/576 exactly |
| (1 − λ/n)^n ≈ e^−λ for large n; "almost exactly": 0.3933 vs 0.3937 | e^−0.932292 = 0.393651 → 0.3937; difference 0.0003 |
| (cut in round 3: "four in ten" squares empty) | 39.3 % |
| Map A: 576 − 222 = 354 non-empty squares share 537 hits, "one and a half each" | 537/354 = 1.517 |
| "a hundred and thirty-one take two or more" | Map A: 92 + 28 + 9 + 2 = 131 squares with ≥ 2 hits (`sim.py`) |
| "For two hits … five thirty-seven times five thirty-six, over two, ways" | C(537, 2) = 537·536/2! = 143,916 unordered pairs |
| P(2) ≈ (537·536/2!)(1/576)² e^−λ | = 0.1708; binomial exact C(537,2)(1/576)²(575/576)^535 = 0.1712; Poisson 0.1711 |
| "Five thirty-six is almost five thirty-seven": on screen 537·536 ≈ 537² | 287,832 vs 288,369 (0.19 % apart) |
| "so for any k, each two becomes a k": P(2) → P(k) ≈ (537^k/k!)(1/576)^k e^−λ = λ^k e^−λ/k! | C(537,k) = 537·536·…·(538−k)/k! ≈ 537^k/k! and (575/576)^(537−k) ≈ e^−λ for small k (the "≈" on screen); at k = 0…4 binomial and Poisson differ by < 0.3 squares |
| Purple bars (576·P(k)): 227, 211, 98.5, 30.6, 7.1, 1.6 | 226.74, 211.39, 98.54, 30.62, 7.14, 1.57 |
| "chance predicts thirty-nine" / on screen "chance: 39.3" (squares with ≥ 3 hits) | 30.62 + 7.14 + 1.57 = 39.33 |
| ×5 inset | the 3, 4, 5+ bars redrawn with heights × 5, same columns, labelled "×5" |

## The two simulated maps (`sim.py`)

| Claim | Check |
|---|---|
| Map A: 537 points, each uniform and independent on a 24 × 24 square grid (seed 0, the first seed tried — *not* cherry-picked) | counts per square 0..5+: **222, 223, 92, 28, 9, 2** |
| "Map A lights up with thirty-nine targets" (squares with ≥ 3 hits) | 28 + 9 + 2 = 39; over 1000 random maps 39.4 ± 4.6 |
| "Map A has two hundred and twenty-two" empty squares | 222 (expected 226.7) |
| "so plenty must double up" (round 2 said "so a hundred and thirty-one take two or more", which implied 131 follows from the average) | 354 occupied squares share 537 hits, so at least 183 hits are "extra": some squares must hold two or more. The 131 is then shown as a count on map A ("131 squares with 2+"), not derived |
| "The chi-squared misfit: square each bar's gap, divide by chance's bar, and add them up." On screen χ² = Σ gap²/chance | Pearson's statistic Σ (observed − expected)²/expected over the six classes 0…4, 5+ |
| Map A's six terms on screen: 0.10, 0.64, 0.43, 0.22, 0.49, 0.12; "Map A scores two point oh" (2.0) | exact terms 0.0992, 0.6376, 0.4339, 0.2246, 0.4862, 0.1186; sum 2.0000. The displayed two-decimal terms also add to 2.00 (asserted in scene.py) |
| "Pure-chance maps score worse three times in four: p equals point seven four"; left panel "20,000 chance maps (simulated)", bins from 2.0 up highlighted, "p = 0.74" | `sim.null_misfits()`: 20,000 maps of 537 uniform hits (seed 2026), each scored the same way: 74.5 % score ≥ 2.0 (Monte Carlo s.e. 0.3 %). The χ²₄ approximation Clarke used gives 0.736. Both round to 0.74. (Earlier exploratory runs: 10,000 maps, seed 11: 0.753; 1,000-map subsets range 0.72–0.77, which is why 20,000 are shown.) The histogram is drawn in bins of width 1 from 0 to 16; 0.56 % of maps score above 16 and fall off the drawn axis |
| Map B "a misfit of two hundred and seventy-two", readout 271.7, arrow off the end of the 0–16 axis | χ² = 271.7 (terms 61.1, 163.0, 8.3, 30.6, 7.1, 1.6); the highest of the 20,000 chance maps is 36.6; χ²₄ tail p = 1.4 × 10⁻⁵⁷ |
| Map B: 537 points placed one at a time uniformly, rejecting any closer than 0.8 square-widths to an earlier one ("no two hits closer than four fifths of a square") | random sequential addition, d = 0.8, seed 1; min pair distance 0.8005 |
| "Map B gets none" (no square with ≥ 3) | counts 0..5+: **109, 397, 70, 0, 0, 0** |
| "half the expected empty squares" | 109 / 226.7 = 0.48 |
| "a tower of single hits" | 397 vs 211 expected |
| Map B: (round 2 showed "p < 10^−50"; round 3 shows its misfit, 271.7, instead) | χ² = 271.7, df 4, p = 1.4 × 10⁻⁵⁷ |
| "Aimed bombs would miss the other way: extra empty squares, extra pile-ups"; red outline bars "aimed (simulated)" | `sim.aimed_map()`: 537 hits, each normal (s.d. 2 squares) around one of 3 aim points drawn uniformly in the map's central 16 × 16 squares, seed 0 (the first tried); hits off the map are re-drawn. Counts 0…5+: **399, 58, 37, 30, 13, 39** vs chance 227, 211, 98.5, 30.6, 7.1, 1.6: 172 extra empty squares, 82 squares with 3+ hits vs 39.3; misfit 1178.6. This matches Clarke's description of clustering ("an excess number of squares containing either a high number of flying bombs or none at all, with a deficiency in the intermediate classes") |
| Zoom discs: radius 0.4 square, so two discs overlap exactly when two hits are closer than 0.8 square (B's rule) | Round 4 moves each zoom into the gutter to its map's right, so the zoomed block is taken on the map's right edge (columns 21–24). A: the densest such block (rows 9–12, 23 hits): 22 of 23 discs overlap a neighbour (24 close pairs) and turn red. B: the edge block whose count is closest to the 16-hit average (rows 8–11, 16 hits): none can overlap. (Round 3's A block, the densest anywhere in columns 2–12: 16 of 20, 19 pairs) |

## Wording guards

- The episode never says the bombs were unaimed: "The bombs were aimed at central London but
  tended to fall short" (Evans & Delaney 2018; Shaw & Shaw 2019), and the test only shows no
  clustering *at the scale of half-kilometre squares, within an area of constant density*.
- "Flying bombs" throughout (V-1), never "rockets".
- "A pattern this even is the fingerprint of a **spacing** rule" (round 1 said "a rule", which
  over-generalised: aim is also a rule, and it produces the opposite fingerprint; round 2's "Too
  even" was heard as "two even").
- "The detector, like your eye, expected chance to spread out that evenly" now carries an
  on-screen citation (round-3 substance fix 7): **Falk & Konold, 1997 · Psych. Review 104(2)**
  (R. Falk & C. Konold, "Making sense of randomness: Implicit encoding as a basis for
  judgment", *Psychological Review* 104(2):301–318, doi:10.1037/0033-295X.104.2.301). Read in
  the paper (p. 301): "The most prominent and consistent finding of the research on both
  generation and perception of randomness of binary sequences (and two-dimensional [2-D]
  grids) is that people identify randomness with an excess of alternations between symbol
  types … Typical random sequences … are not perceived by participants as maximally random
  because the runs appear too long to be random." Their own experiments include 2-D grids
  ("Sequences and grids with P(A)s equally distant from .50 are not judged equally random").
  Over-alternation in a grid is exactly "too even": the eye expects chance to spread hits out.
- Closing line (round 5, final): "If you chose map B, you chose the rule." (first round-5 draft:
  "If you chose map B, you chose the one following a rule.") (Round 4's
  "you picked the one" lost its final -ed before "the" in the transcript.) Round 4: "If you picked
  map B, you picked the one following a rule." Round 3
  said "the one with a plan", which a reviewer read as conflating B's spacing rule with aim
  (aim produces the opposite fingerprint, shown at 2:56). "Following a rule" repeats the cold
  open's "The other follows a rule" and the rule tag that flashes.
- The "≈ Clarke's area" rectangle is Shaw & Shaw's re-creation, and the numbers in the table are
  Clarke's; facts above explain the 537 vs 532 difference.

## Round 5 additions

| Claim (as used in the episode) | Check |
|---|---|
| "five thirty-seven times five thirty-six ways, over two, since order doesn't matter" (the two yellow hits swap places on screen) | 537 choices for one bomb × 536 for the other counts every pair twice ({a, b} as a-then-b and b-then-a), so C(537, 2) = 537·536/2 = 143,916 |
| "Five thirty-six is almost five thirty-seven": the 536 turns into a 537 in place and 537·537 folds into 537² | 537·536 = 287,832 vs 537² = 288,369 (0.19 % apart) |
| "For three hits, each two becomes a three": P(3) ≈ 537³/3! · (1/576)³ · e^−λ on screen | C(537, 3) = 537·536·535/3!; 537·536·535/537³ = 0.9944. Expected squares with 3 hits: exact binomial 576 × 0.05310 = 30.59, Poisson 576 × 0.05316 = 30.62 |
| "for any k, a k": P(k) ≈ 537^k/k! · (1/576)^k · e^−λ = λ^k e^−λ / k! | as before (the "≈" covers 537·536·…·(538−k) ≈ 537^k and (575/576)^(537−k) ≈ e^−λ) |
| "To judge London, chance must predict every bar": preview of the histogram axes with chance's bar 0 = 227 and "?" over 1, 2, 3, 4, 5+ | 227 is the 576 × 0.3933 just computed; the other bars are what the derivation then supplies |
| "…and divides by chance's bar, so a miss on a short bar counts more" (on "short", the 4-hit bar's sliver, its term 0.49 and chance's 7.1 bar flag) | Map A's own bars: 4 hits: observed 9 vs chance 7.14, miss 1.86 → term 1.86²/7.14 = 0.49; 0 hits: 222 vs 226.74, a bigger miss of 4.74 → term 4.74²/226.74 = 0.10. Both terms stay on screen (0.49 under the short 4-hit bar, 0.10 under the tall 0-hit bar). (The first round-5 draft spoke all four numbers, "a miss of two on seven outweighs a miss of five on two hundred twenty-seven"; cut to one idea per sentence, PRODUCTION_GUIDE §13.1) |
| "Three out of four simulated chance maps score worse. That share, p, is point seven four." (third pass: "Three in four" was heard as "3 and 4") | 74.5 % of the 20,000 simulated chance maps score ≥ 2.0 (Monte Carlo s.e. 0.3 %); χ²₄ tail 0.736 |
| Readouts "χ²_A = … = 2.0" and "χ²_B = … = 271.7" | as before; the subscript names the map |
| The aimed map's empty squares are tinted on "extra empty squares" | 399 empty squares on the aimed map vs 226.7 expected (`sim.py`) |
| "farther north, hits were about half as dense"; densities shown in one column: "north 1.9 hits/km²" and "≈ Clarke's area 3.7 hits/km²" | 86/45 = 1.91 and 537/144 = 3.73 (532/144 = 3.69 for the re-created rectangle); ratio 0.51 |
| "five hundred seventy-six squares of London" (round 4 said "south London") | Shaw & Shaw's re-created rectangle includes a strip north of the Thames (see above), so the narration no longer says "south" over it |
| Cut: "No sign of clustering" | restated p = 0.88, which is on screen and spoken |
| (second round-5 pass) "In nineteen forty-six, R D Clarke published the same test on London's real hits: five hundred thirty-seven, in five hundred seventy-six squares" | Clarke 1946 fits the same six classes (0…4, 5+) with Pearson's χ² (1.17, 4 df, P = .88): the same misfit as the episode's χ²_A / χ²_B readouts. "the actuary" is shown by his citation only |
| (second round-5 pass) "Chance predicted two hundred twenty-seven empty squares; Clarke counted two hundred twenty-nine. Overall, p equals point eight eight." | 226.74 → 227 and 229 (Clarke's table); χ² = 1.17, P = .88 as before. "Single hits: two hundred eleven, exactly as predicted" was cut from the narration (the table still shows 211 under 211); the screen carries the other four classes |
| (second round-5 pass) "Your eye expects chance to look that even." (was "The detector, like your eye, expected chance to spread out that evenly"), with the Falk & Konold citation | Falk & Konold 1997, p. 301: people "identify randomness with an excess of alternations", in sequences and 2-D grids; the over-alternating, too-even pattern is the one judged random |
| (third round-5 pass) "aim: Evans & Delaney, 2018 · Applied Geography 99" credit line under the red × (Tower Bridge) and the red arrow (to Dulwich) | Re-read 2026-10-22 (McGill-hosted PDF): "Published sources … give Tower Bridge as the aiming point", the paper adopts "a nominal primary aiming point … Tower Bridge"; the overall MPI of the main attack "was displaced 5.6 km south of Tower Bridge … located in Dulwich"; "as a consequence of this bias, V1 impact density was less in the densest populated boroughs north of the Thames". The "aim:" prefix names what the source stands behind, like "map:" and "hits/km²:" on the lines beside it |
| (third round-5 pass) "Each bomb has a one in five seventy-six chance of landing in this square" (was "lands in this square with chance one in five seventy-six") | same claim, reworded for the voice (Kokoro held "one" 0.52 s) and so that 1/576 is built as "one in" is spoken, 0.9 s into the beat |
| (third round-5 pass) Misfit readouts show "= ?" until their terms are added | no number on screen is ever false: round 4's readout showed "χ²_A = … = 0.0" for 8 s before the terms arrived and "χ²_B = … = 2.0" (A's score) for 4 s after the subscript changed |
