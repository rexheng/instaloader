# Round 3: substance review (science and story editor)

**Evidence.** I used the `review/` pack as it stands, because metrics.json (20:57) is newer than final.mp4 (20:55). I read:
- report.md, all 14 contact sheets, the transcript, narration_diff, narration.txt, script.md, facts.md and CHANGELOG.md;
- 15 full-resolution keyframes: 0:14.7, 0:19.1, 0:39.6, 0:57.7, 1:18.7, 1:34.4, 2:04.4, 2:13.0, 2:37.1, 2:47.3, 2:59.6, 3:09.7, 3:27.6, 3:40.9 and 3:50.3;
- three frames I extracted myself at 2:44.6, 2:50.5 and 3:19.8.

**Recomputation.** I recomputed every number with scipy and re-counted the simulated maps from `sim_data.npz`, including the 20,000-map null. I also recomputed the V-1 densities from `v1_impacts.csv` and the OS Thames line.

**Citations.** I checked them against the Clarke 1946 record (JIA 72:481, doi:10.1017/S0020268100035435) and the full text of Shaw & Shaw 2019 (ORA Oxford PDF; Wiley, Significance 16(5):12–17).

```
EPISODE: 003 — "Which Map Is Random?"
IDEA: Pure chance leaves gaps, and the gaps force clumps, so clusters are not evidence of aim; the honest test scores the whole count histogram against Poisson, and a pattern that is too even is the real sign of a rule.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.5   AFTER CEILING: 8.5 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.5   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| Each map holds 537 hits; 576 squares (24 × 24) | Verified | sim_data.npz: A and B both 537 points |
| Map A is uniform random; counts 0…5+ = 222, 223, 92, 28, 9, 2 | Verified | re-counted |
| "39 targets" on A (≥ 3 hits); "Map B gets none" | Verified | 28 + 9 + 2 = 39; B = 109, 397, 70, 0, 0, 0 |
| B's rule: "no two hits closer than four fifths of a square" | Verified | min pair distance 0.8005 (A: 0.050) |
| One bomb lands in a given square with probability 1/576 | Verified | uniform over 576 equal squares |
| (1 − 1/576)^537 ≈ 0.3933, "point three nine three" | Verified | 0.393332 |
| "0.3933 × 576 ≈ 227" (on screen); "about 227" (spoken) | Verified | 226.54; exactly 576 × 0.393332 = 226.56 |
| "Map A has 222" | Verified | re-counted |
| 354 squares share 537 hits, "one and a half each", "plenty must double up" | Verified | 537/354 = 1.517; pigeonhole forces at least 183 extra hits |
| "131 squares with 2+" | Verified | 92 + 28 + 9 + 2 |
| λ = 537/576 ≈ 0.93; 1/576 = λ/537 | Verified | 0.93229; exact identity |
| (1 − λ/537)^537 ≈ e^−λ ≈ 0.3937, "almost exactly" | Verified | e^−0.93229 = 0.39365 |
| P(2) ≈ (537·536/2!)(1/576)² e^−λ | Verified (≈) | 0.17076 vs exact binomial 0.17121 |
| 537·536 ≈ 537² | Verified | 287,832 vs 288,369 (0.19 %) |
| P(k) ≈ λ^k e^−λ / k! | Verified (≈, small k) | standard binomial → Poisson limit |
| Purple bars 227, 211, 98.5, 30.6, 7.1, 1.6 | Verified | 576·Pois(0.93229) = 226.74, 211.39, 98.54, 30.62, 7.14, 1.57 |
| "chance predicts thirty-nine" / "chance: 39.3" | Verified | 30.62 + 7.14 + 1.57 = 39.33 |
| χ² terms 0.10, 0.64, 0.43, 0.22, 0.49, 0.12; "Map A scores two point oh" | Verified | 0.099, 0.638, 0.434, 0.225, 0.486, 0.119; sum 2.000 |
| "Pure-chance maps score worse three times in four: p = 0.74" | Verified | null array: 74.5 % ≥ 2.0 (n = 20,000); χ²₄ tail 0.736. The reading of p is correct |
| B: "half the expected empty squares", "tower of single hits", "misfit of 272" (readout 271.7) | Verified | 109/226.7 = 0.48; 397 vs 211; χ² = 271.71 (max of the null 36.6) |
| Aimed bombs give "extra empty squares, extra pile-ups" | Verified | aimed sim 399, 58, 37, 30, 13, 39; matches Clarke's own description of clustering ("an excess number of squares containing either a high number … or none at all") |
| 1944: Londoners claimed the flying bombs fell in clusters; quote "…tended to be grouped in clusters." | Verified | Clarke 1946 p. 481 ("frequent assertions were made…"); Shaw & Shaw: "As Londoners observed at the time, there are multiple clusters" |
| Precise aim would put factories at risk | Verified | Shaw & Shaw 2019: "if it could be accurately targeted at munitions factories it would also become a strategic threat to the war effort" |
| "In 1946, the actuary R D Clarke published this test" | Verified | JIA 72:481 (1946); byline F.I.A., Prudential |
| 537 hits, 576 squares, south London | Verified | Clarke 1946; Shaw & Shaw ("144km² area … 537 V-1 hits") |
| Clarke table: London 229, 211, 93, 35, 7, 1; χ² = 1.17, p = 0.88 | Verified | Shaw & Shaw Table 1; recomputed χ² = 1.169, p(df 4) = 0.883 |
| "No sign of clustering" | Verified | Clarke: "lends no support to the clustering hypothesis" |
| "real V-1 hits, 1944–45" (887 dots) | Verified | Shaw & Shaw: "In total, the map contains 887 V-1s" (LCC maps) |
| They were aimed at London, too loosely to choose a street | Verified | Shaw & Shaw: V-1s "tended to fall short of the centre of London" |
| "North of the river, hits fell about half as densely" (1.9 vs 3.7 hits/km²) | Verified as a number, but the picture contradicts the wording (fix 2) | my recount: north box 86/45 = 1.91; Clarke area 537/144 = 3.73. Across the LCC, 287 of 887 hits are north of the Thames. The "≈ Clarke's area" rectangle itself has about 20 km² north of the river, with 55 of its 532 hits there (about 2.7/km² vs 3.9/km² south) |
| Citations "R. D. Clarke, 1946 · J. Inst. Actuaries 72:481"; "Shaw & Shaw, 2019 · Significance 16(5)"; "L. Shaw, 2025 · Zenodo" | Verified | author, year, venue and volume correct |
| Implied: the blue "London" bars are a count of the gridded dots shown (3:13–3:28) | Misleading juxtaposition, not stated (fix 1) | The bars are Clarke's 1946 counts of 537 hits. The dots in the yellow grid are Shaw & Shaw's re-created area, with 532 hits and counts 237, 189, 115, 28, 6, 1. "Single hits: 211, exactly as predicted" is true of Clarke's table and false of the squares on screen (189) |
| "The detector, like your eye, expected chance to spread out that evenly" (0:54.8) | Plausible, uncited (fix 7) | The finding exists: Falk & Konold 1997, *Psychological Review* 104(2):301–318, show people judge over-alternating sequences as most random. It is not cited on screen. Because the line is framed as the viewer's assumption and is backed by the cited Londoners' claim, I did not apply cap 8 |

There are no wrong numbers and no fabricated or misattributed sources, so no cap 4 or 6 applies. Two juxtapositions mislead a careful viewer (fixes 1 and 2).

## MECHANICS

- runtime 3:55.3
- wpm 162 on speech time, 156 overall (613 words)
- max internal silence 1.98 s (the planned hold at 0:09.8)
- leading silence 0.00 s, trailing 1.74 s
- max static 3.57 s (0:45.1–0:48.7)
- −14.0 LUFS / −2.1 dBTP
- 0 black frames, WER 2.6 %

No mechanical caps. The layout audit's only flag (e^−λ 0.08 from a rectangle at 2:12.3) happens mid-motion.

**Slop scan (§4).** No banned phrases. No "not just X", no two questions in a row, no adjective triplets, no recap ending. "Backwards." is a one-word reversal followed by evidence, not a fake reveal. "The chi-squared misfit: square each…" is a definition, not a colon reveal. The voice is specific and numeric, so the slop scan is clean.

## STORY / CLARITY NOTES

- **Hook (8.5).** The first frame poses the puzzle and the viewer commits by 0:10 ("Which one is chance?", followed by a 1.7 s hold). Stakes arrive by 0:24 with a cited quote. The misconception is voiced, built into a detector (0:24–0:42), and broken by a measured number: 39 false alarms against chance's 39.3 (2:27–2:31). The landing returns to the cold-open maps. Three things hold it below 9:
  - Two-panel "random vs. even" dot pairs are a familiar demo.
  - Tension sags through the 47 s derivation (1:33–2:20).
  - The last line, "the one with a plan" (3:49.6), contradicts the episode's own payoff (fix 4).
- **Clarity (8.5).** The mathematics is correct and built from the picture: λ from the counter, e^−λ from the row above, P(2) from the bomb row and the square, then P(k). Assumptions are stated (one λ everywhere) and the honest limits are shown. Three things keep it below 9:
  - The real-data beat lets the viewer believe Clarke's bars count the dots on screen (fix 1).
  - The limits beat says "north of the river" over a rectangle that straddles the river (fix 2).
  - B's histogram appears beside A's thumbnail and A's p for 9 s with no label (fix 3).
- **Concision (8.5).** 3:55 is near the ceiling. The 1:48.6–2:11.3 block packs the P(2) build and the k-generalisation into 22.7 s with gaps of 0.3–0.5 s. It is dense rather than padded, but it is the one place a rewatch is needed.
- **Originality (8.5).** The V-1/Poisson story is a textbook staple (Feller; Shaw & Shaw won an award for retelling it). This episode adds the "too even" counter-example, the gaps-force-clumps argument, the 20,000 null maps, the aimed counterfactual and the real map with the Thames. Together these are a genuinely fresh angle.

```
FIXES (highest impact first):
1. [3:13–3:28][Clarity] Clarke's 1946 counts (229/211/93/35/7/1, 537 hits) grow as blue bars directly beside the gridded "≈ Clarke's area" rectangle, whose 532 dots actually count 237/189/115/28/6/1 — so "Single hits: 211, exactly as predicted" reads as a claim about the squares on screen, which it is not (189). → Rename the table row header "London" to "Clarke, 1946" (BLUE, same size), and change the narration at 3:17 to "Clarke counted two hundred and twenty-nine." Also change 3:08 to "five hundred and thirty-seven, in five seventy-six squares of south London; his grid's location is lost, so this box is a re-creation." If that is too long, put a GRAY Text 18 tag "re-created" (≤ 1 word) under the "≈ Clarke's area" label and keep the spoken "Clarke counted" change; that alone removes the false correspondence.
2. [3:37–3:43][Clarity] Narration says "north of the river, hits fell about half as densely, so Clarke chose an area where lambda held steady", while the yellow "Clarke's area" visibly straddles the Thames (kf 3:40.9: the river runs through its top third; ~20 km² of it is north of the river). A viewer sees the chosen area contain the very region the narration says was avoided. → Change the line to "Farther north, hits fell about half as densely, so Clarke chose an area where lambda held steady", and drop the Thames yellow flash on "river" (flash the dashed north box instead, on "Farther north"). Keep the river line itself as geography.
3. [2:43.4–2:52.5][Clarity] Map B's bars (109/397/70) morph in while the only map on screen is A's thumbnail with "A" and "p = 0.74" beside them (frames 2:44.6, 2:47.3, 2:50.5); B is first named on screen by the "B: 271.7" arrow at ~2:52.5. → On "Map B" (2:43.4) FadeIn a thumbnail of map B (same 1.1-unit size as A's) with label "B" just right of A's thumbnail, and dim A's thumbnail and "p = 0.74" to 35 % over 0.5 s; restore them at 2:52.5 when the "B: 271.7" arrow lands so the two misfits can be compared.
4. [3:49.6–3:53.6][Hook/Clarity] Closing line "If you picked map B, you picked the one with a plan" conflates B's spacing rule with aim — but 2:55.8 just established that aim (a plan) produces the opposite fingerprint (extra empties, extra pile-ups). The final line thus muddies the episode's thesis. → Replace with "If you picked map B, you picked the one following a rule." (matches the cold open's "The other follows a rule" and the flashing "rule: gap ≥ 4/5 square" tag), keeping speed 0.78.
5. [1:25–1:37][Visual] kf 1:34.4: yellow empties (85 %), blue count shading, red 3+ outlines, blue 2+ outlines and white dots all at full strength; neither 131 nor 39 reads. → On "so plenty must double up" (1:31) fade yellow empties to 35 % and red outlines to 0; only the 131 blue outlines and dots stay full until the 1:33.3 dim. Restore yellow/red at 2:23 as now.
6. [1:48.6–2:11.3][Audio/Concision] 22.7 s single breath group for the P(2) and general-k steps (inter-sentence gaps 0.3–0.5 s at 1:51.1, 1:55.6, 2:00.4, 2:02.7). → Insert 0.6 s pauses after "over two, ways." and after "e to the minus lambda again."; pay for them by cutting "The chance is point three nine three, so" at 1:14.5 (say "About two hundred and twenty-seven squares stay empty."; 0.3933 stays on screen) — net runtime unchanged.
7. [0:54.8–0:59.1][Clarity] "The detector, like your eye, expected chance to spread out that evenly" is a claim about human perception with no on-screen source. → Add a citation line at bottom-left, GRAY Text 18, held ≥ 3 s from 0:55: "Falk & Konold, 1997 · Psych. Review 104(2)" (they found people judge over-alternating, i.e. too-even, sequences as most random). This also makes the misconception Veritasium-grade rather than asserted.
8. [3:48.5–3:53][Visual] A's 39 targets return as 40 % red fills that read maroon-brown (kf 3:50.3, e.g. cells near (240,465) px) — a colour in no palette entry. → Redraw them as the same 3 px RED outlines from 0:39 (LaggedStart Create, lag 0.02, 1.0 s, on "no aim at all"); no fill.
9. [3:07–3:43][Visual] The "Thames" label's background knockout clips ~6 real V-1 dots (kf 3:09.7 around the "Th"). → Remove the knockout and place the label at the river's east end outside the dot cloud (≈ (835, 440) px), ≥ 0.15 units from every dot.
10. [0:10.1–0:11.8][Hook] The commit is spoken but nothing on screen holds it. → During the hold, FadeIn GRAY Text 30 "A or B?" centred between the maps at y = −3.0; FadeOut on "Both are simulated".
REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1–3 take Clarity to 9 (25 % weight); fix 4 plus 10 take Hook to 9; fixes 5, 8, 9 take Visual to 9; fix 6 takes Audio/Concision to ~9. Weighted ≈ 8.9–9.0. No structural change is needed: misconception-first hook, measured failure (39 false alarms vs chance's 39.3), picture-built derivation, measured v2 against 20,000 simulated null maps, real cited data with honest limits, and a landing on the cold-open maps are all in place. For margin, also trim ~8 s from the 1:33–2:20 derivation.
KEEP:
- The measured failure-and-repair: "39 targets, and chance predicts 39" (2:27–2:31) followed by the misfit scored against 20,000 simulated chance maps (2:38–2:43) — the detector's failure is quantified, then the fixed detector is calibrated, not asserted.
- "Those gaps force the clumps" with 222 yellow empties and 537 hits / 354 squares ≈ 1.5 (1:20–1:33): a pigeonhole argument the viewer can verify by eye.
- The honest limits beat on real data (3:28–3:43): aimed at London but too loosely for a street, and one λ required — with the densities credited as "our count".
```
