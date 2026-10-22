EPISODE: 003 — "Which Map Is Pure Chance?"
IDEA: Pure chance leaves empty squares, and those gaps force pile-ups, so clusters alone are not evidence of aim. The honest test scores the whole count histogram against Poisson's prediction, and a pattern that is too even is what gives away a spacing rule.

SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.6 (857.5/100)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none.
- Every number I recomputed checks out, and every citation was verified by web search.
- No banned phrase or §4 pattern. "Let's call" at 1:22.6 is not on the list, and the one-word "Backwards." at 0:35 is a reveal, not a colon fake-reveal.
- Every empirical claim carries an on-screen citation held for at least 3 s: Clarke and Shaw & Shaw 0:11–0:21 and 2:53–3:24, Falk & Konold 0:49–0:52, Evans & Delaney 3:15–3:24, "hits/km²: our count" 3:19–3:24.
- Mechanics are inside every limit.
FINAL: 8.6   PASS: no

FACTS:
- λ = 537/576 ≈ 0.93 | Verified | 0.93229
- P(empty) = (1 − 1/576)^537 ≈ 0.3933; "0.3933 × 576 ≈ 227" | Verified | 0.393332 × 576 = 226.56
- (1 − λ/537)^537 ≈ e^−λ ≈ 0.3937, "almost exactly" | Verified | e^−0.93229 = 0.393651
- Map A: 222 empty; 354 occupied; 537 − 354 = 183 extra hits; 131 squares with 2+ | Verified | sim.py counts 222, 223, 92, 28, 9, 2
- C(537, 2) = 537·536/2, "since each pair counts twice" | Verified | 143,916 pairs
- (1/576)² · (575/576)^535 ≈ … · e^−λ | Verified | (575/576)^535 = 0.3947 vs 0.3937, covered by the "≈"
- P(k) ≈ λ^k e^−λ / k!, bars 576·P(k) = 227, 211, 98.5, 30.6, 7.1, 1.6 | Verified | 226.74, 211.39, 98.54, 30.62, 7.14, 1.57
- "39 targets and chance predicts 39" (39.3 on screen) | Verified | 30.62 + 7.14 + 1.57 = 39.33
- Map A χ² = 2.0, terms 0.10, 0.64, 0.43, 0.22, 0.49, 0.12 | Verified | 2.00001 (terms 0.099, 0.638, 0.434, 0.225, 0.486, 0.119)
- "Three out of four simulated chance maps score worse", p = 0.74 | Verified | my own 20,000-map Monte Carlo (seed 5): 0.743; χ²₄ tail 0.736
- Map B χ² = 271.7, "half the expected empty squares" (109 vs 226.7), "tower of single hits" (397) | Verified | Recomputed 271.71; 109/226.7 = 0.48
- Clarke 1946, J. Inst. Actuaries 72:481: 537 hits, 576 squares, table 229/211/93/35/7/1, χ² = 1.17, P = .88, "tended to be grouped in clusters" | Verified | Berkeley-hosted scan of p. 481; recomputed χ² = 1.169, p(df 4) = 0.883
- Shaw & Shaw 2019, Significance 16(5):12–17: factories at stake, Londoners' impression of clusters | Verified | Wiley full text: "if it could be accurately targeted at munitions factories it would also become a strategic threat"
- Evans & Delaney 2018, Applied Geography 99:44–53: Tower Bridge aiming point; mean point of impact in Dulwich; lower density north of the Thames | Verified | McGill-hosted PDF
- Falk & Konold 1997, Psych. Review 104(2):301–318: people judge over-alternating (too even) patterns as most random, in sequences and 2-D grids | Verified | APA PsycNet record and the paper's abstract
- "farther north, hits were about half as dense": 1.9 vs 3.7 hits/km² | Verified (own count, credited as such) | real_data.npz: 86/45 = 1.91 and 532/144 = 3.69 (Clarke's 537/144 = 3.73)
- Arrow from the Tower Bridge × to Dulwich is about 5.6 km long | Verified | about 210 px at 36.5 px/km ≈ 5.75 km (kf_35)

MECHANICS: runtime 3:34.6 · wpm 158 (speech time; 496 script words) · max silence 1.76 s (0:08.0) · leading 0.00 s / trailing 1.33 s · max static 2.73 s · −14.0 LUFS / −1.9 dBTP. Transcript WER 2.9%. The only term heard differently is "Clark" for "Clarke", a homophone.

WHAT WORKS (evidence):
- **Hook (9).**
  - The first frame is the puzzle. "Which is chance?" lands at 0:06.9, the "A or B?" commitment holds through the 1.8 s silence at 0:08.0–0:09.7, and the stakes arrive at 0:10.
  - The naive detector is built by 0:28 and fails at 0:35 ("Backwards").
  - The landing (3:29–3:33) re-shows the cold-open pair with "misfit 2.0" and "misfit 271.7" under them, and the last line ("If you chose map B, you chose the rule") pays off the viewer's own guess.
- **Motion.** The derivation is carried by objects:
  - 537 hits become a 537-dot "bombs" block (1:37), two bombs drop into the square, and 1/576 is carried into (1/576)².
  - The 536 turns into a 537 in place (1:51–1:53), and 537 with 576 fold into λ^k (1:59).
  - The squares fly into histogram bars (2:09), and gap slivers become χ² terms (2:19).
- **Substance.** This is the standard textbook example done honestly. The null is simulated and shown (20,000 maps), the narration says what p means in words ("three out of four… score worse"), and the episode admits the bombs were aimed and fell short.

FIXES (highest impact first):

1. [3:12–3:25][Clarity + Originality] The honest limit is asserted, not measured.
   - Problem: "The test needs one lambda" is told, never shown. The viewer never sees what goes wrong when λ varies, even though the screen already holds the data that shows it.
   - Evidence: I recomputed from real_data.npz. Pooling the north box (45 km², 86 hits) with Shaw & Shaw's rectangle (144 km², 532 hits) gives 756 squares of 0.5 km with counts 352, 235, 132, 30, 6, 1 against Poisson 333.8, 272.9, 111.5, 30.4, 6.2, 1.2. That is χ² = 10.0, df 4, p = 0.04. It shows extra empty squares, missing singles and extra pile-ups: the aim fingerprint, made by pure chance at two densities.
   - Change: on "farther north… half as dense" keep the current picture. Then replace "The test needs one lambda: Clarke chose an area where it held steady." with "Pool the two, and chance at two densities fakes the aim fingerprint: p equals point oh four. Clarke chose an area where lambda held steady."
   - On screen: the 756-square pooled bars grow under the purple Poisson outlines, with "χ² = 10.0, p = 0.04" written in place of Clarke's "p = 0.88".
   - Pay for the extra 4 s with fix 9.
   - This turns the limit into the StuffMadeHere move: the method fails here, by this much. It is also the episode's one non-obvious image (clusters from no aim at all, just uneven λ), which is what lifts Originality to 9.

2. [0:45–0:52][Clarity, fairness] The A-versus-B zoom is stacked, in an episode about not being fooled by picked clumps.
   - Problem: facts.md (zoom row) says A's zoom is "the densest such block (rows 9–12, 23 hits)", while B's is "the edge block whose count is closest to the 16-hit average". In kf_08 (0:51.4), 22 red overlapping discs in A sit beside 16 clean discs in B. That compares A's worst case with B's typical case. The episode's own thesis is that picking the densest clump misleads, so its key comparison picture should not do it.
   - Change: choose A's right-edge 4×4 block by the same rule as B's (count closest to 16), recount the overlapping discs, and update facts.md. Chance will still show many overlaps, because a 0.8-square spacing is violated constantly at λ = 0.93. If you keep the densest block, tag it "densest corner" in GRAY (Text ≥ 18) under the zoom.

3. [1:24.9–1:32.0][Clarity] The step to e^−λ is announced.
   - Problem: "One minus a small slice, raised to a big power, is e to the minus lambda, almost exactly" asks the viewer to accept a limit they cannot see. The 0.3933 vs 0.3937 check (1:31) confirms the claim but does not explain it.
   - Change, with no new words: during "One minus a small slice, raised to a big power", put a short GRAY number line under the second row. Drop dots for (1 − λ/n)^n at n = 1, 2, 5, 20, 537, at 0.068, 0.285, 0.356, 0.385 and 0.3933, each tagged with its n. The dots should crowd toward a purple tick at e^−λ = 0.3937, which writes on "e to the minus lambda".
   - The viewer then sees why "big power" matters and could rebuild the step.

4. [2:14.5–2:22.8][Clarity] Why divide by chance's bar is never said.
   - Problem: "squares each bar's gap and divides by chance's bar, so a miss on a short bar counts more" gives a consequence, not a reason. A viewer cannot re-derive Pearson's weighting from it.
   - Change: narrate "…and divides by chance's bar, because short bars wobble less. So a miss on a short bar counts more."
   - On screen, on "wobble", draw thin INK whiskers on two bars:
     - bar 0: ±12 (binomial s.d. √(576·0.394·0.606) = 11.7);
     - bar 4: ±2.7 (√(576·0.0124·0.988) = 2.66).
   - Map A's 4.7 miss on bar 0 then sits inside its whisker, and its 1.9 miss on bar 4 nearly fills its own. That is the reason, made visible. Do not label the whiskers "√chance": for bar 0 that would be ±15, which is wrong.

5. [1:03.5–1:05.9][Audio/Clarity] The answer to the prediction is spoken before it is on screen.
   - Problem: "About two hundred twenty-seven" runs 1:03.5–1:05.4. At 1:04.6 (extracted frame) the line reads a doubled "≈ 0.3933" with half-written glyph fragments where "× 576 ≈ ?" will be, and "227" appears only at about 1:05.6.
   - Change: build "0.3933 × 576 ≈ ?" during the guess hold (1:02.0–1:03.5). On "two hundred" (1:03.6), FadeTransform only the "?" into "227" (0.5 s).

6. [2:22.8–2:24.2][Motion] The χ² terms render as glyph soup.
   - Problem: at 2:23.6 (extracted frame) the six terms shrink into "0.100.640.430.220.490.12", about 10 px tall, beside a readout reading 1.1.
   - Change: do not fly copies. Flag each term yellow in place with LaggedStart (lag 0.25, 1.4 s total) while the readout steps through the running sums 0.10, 0.74, 1.17, 1.39, 1.88, 2.0 (the sums of the two-decimal terms shown).

7. [3:33.6–3:34.3][Visual/Motion] The end card double-exposes over map A.
   - Problem: at 3:33.9, "Sample Space" and "Which Map Is…" sit on top of map A's dots and red outlines.
   - Change: FadeOut the A/B pair fully (0.35 s) before the card fades in, or end on the A/B frame with its misfit tags and drop the card.

8. [3:15–3:25][Visual] The limits frame reads across empty space.
   - Problem (kf_35 at 3:22.6): "1.9 hits/km²" sits about 885 px right of the north box, and "3.7 hits/km²" about 600 px right of the rectangle. Prose plus four citation lines exceed the §5 word load.
   - Change:
     - Put "north · 1.9 hits/km²" next_to(north_box, RIGHT, buff 0.25), and drop the long white arrow.
     - Put "3.7 hits/km²" directly under "≈ Clarke's area", and move "re-created" to the rectangle's lower-left corner.
     - Fade "real V-1 hits, 1944–45" and "Thames" to 35% from "farther".

9. [1:18.5–1:21.9][Concision] One slack beat, a forward signpost.
   - Problem: "To judge London, chance must predict every bar" says what the next 45 s will do. The 227 bar with "?"s over the others (1:21) already says it without words.
   - Change: cut the sentence (8 words, about 3.4 s). Keep the preview axes and the "?"s, drawn during the 0.6 s turn. This pays for fix 1 and keeps the runtime at about 3:35.

10. [0:51.7–1:18.5][Clarity] Number load.
    - Problem: six new figures are spoken in 27 s (576, 537, 227, 222, 354, 183).
    - Change: drop the spoken "three hundred fifty-four" and say "…force pile-ups: a hundred eighty-three hits must land where another already did." "537 − 354" stays on screen, built from the counter as now, so the arithmetic is still visible.

11. [1:34.5–1:36.5][Motion] Nitpick: four moves start together on "For two hits in the square, pick…" (sheet 6, 1:35: rows collapse, 1/576 relocates, the square enlarges, the dots stream out).
    - Change: sequence them on the words: rows collapse on "For two hits", the square enlarges on "in the square", and the dots stream on "pick two bombs".

REACHES 9 IF ALL FIXED: yes, narrowly, and only if fix 1 lands.
- Fixes 2–5 and 10 lift Clarity to 9: the derivation and the χ² weighting become rebuildable, and the one unfair picture goes.
- Fixes 5–8 and 11 lift Motion, Audio and Visual to 9.
- Fix 9 lifts Concision to 9.
- That gives 15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·9 + 10·8.5 = 895, so 8.95 rounds to 9.0. That is not a safe margin, and the clear 9 needs Originality at 9. Clarke's V-1 table is a Feller-era textbook staple. What would make this telling memorable is fix 1's picture: chance at two densities producing the aim fingerprint (p = 0.04), right after the same test cleared London (p = 0.88).
- No other structural change is needed. The hook, the measured failure (39 flagged vs 39.3 expected), the transformed derivation, the simulated null and the sourced payoff are all in place.

KEEP:
- The cold open: two simulated maps with the same 537 hits, one pure chance and one a spacing rule (not "aimed"). The landing re-shows them with "misfit 2.0" and "misfit 271.7".
- The derivation done with objects: 537 counter → exponent, the 537-dot "bombs" block with two bombs dropping into the square, 536 → 537 in place, folding into λ^k.
- Clarke's real table built under the same purple bars, with the honest "aimed at central London but fell short" limit kept and cited.
