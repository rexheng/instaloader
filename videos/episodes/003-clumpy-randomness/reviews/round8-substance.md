EPISODE: 003 — "Which Map Is Pure Chance?"
IDEA: Pure chance leaves empty squares, and those gaps force pile-ups, so clusters are no evidence of aim. The honest test scores the whole count histogram against Poisson's prediction, and a pattern that is too even is what gives away a rule.

SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 8.5
WEIGHTED: 8.6 (862.5/100)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none.
- I recomputed every number and verified every citation by web search. None is wrong.
- No §4 banned phrase or pattern. "Let's call" (1:16.3) is not on the list, and "Backwards." (0:35.2) is a one-word reveal, not a colon fake-reveal.
- Every empirical claim carries an on-screen citation held ≥ 3 s:
  - Clarke and Shaw & Shaw: 0:11–0:21 and 2:51–3:24.
  - Falk & Konold: 0:47.6–0:52.4, measured on extracted frames.
  - Evans & Delaney: 3:11–3:24.
  - "hits/km²: our count · L. Shaw, 2025 · Zenodo": 3:15–3:24.
- All mechanics are inside the limits (see MECHANICS).
FINAL: 8.6   PASS: no

FACTS:
- 537 hits, 576 squares, λ = 537/576 ≈ 0.93 | Verified | 0.932292; Clarke 1946, p. 481
- One bomb lands in a given square with chance 1/576; P(empty) = (1 − 1/576)^537 ≈ 0.3933; 0.3933 × 576 ≈ 227 | Verified | 0.393332, × 576 = 226.56
- (1 − λ/n)^n dots at n = 1, 2, 5, 20, 537 → e^−λ ≈ 0.3937, "almost exactly" | Verified | 0.0677, 0.2850, 0.3564, 0.3849, 0.3933; e^−λ = 0.393651
- Map A: 222 empty, 39 squares with 3+ hits | Verified | my own recount of sim_data.npz coordinates: 222, 223, 92, 28, 9, 2
- 537 − (576 − 222) = 183 extra hits, "must land where another already did" | Verified | 537 − 354 = 183, the exact number of non-first hits
- C(537, 2) = 537·536/2!, "since each pair counts twice"; (1/576)²; the rest miss ≈ e^−λ | Verified | (575/576)^535 = 0.3947 ≈ 0.3937 (the "≈")
- P(k) ≈ λ^k e^−λ / k!; chance bars 227, 211, 98.5, 30.6, 7.1, 1.6 | Verified | 226.74, 211.39, 98.54, 30.62, 7.14, 1.57
- "Thirty-nine targets, and chance predicts thirty-nine" (39.3 on screen) | Verified | 30.62 + 7.14 + 1.57 = 39.33
- χ²_A = 2.00, terms 0.10, 0.64, 0.43, 0.22, 0.49, 0.12 | Verified | recomputed 2.000
- "Three out of four simulated chance maps score worse", p = 0.74 | Verified | 74.5 % of the stored 20,000 null misfits are ≥ 2.0; χ²₄ tail 0.736
- Whiskers ±12 (bar 0) and ±2.7 (bar 4) | Verified | binomial s.d. 11.73 and 2.65
- Map B: "no two hits closer than four fifths of a square"; 0 targets; 109 empty ("half the expected"); 397 singles; misfit 271.7 | Verified | minimum pair distance 0.8005; counts 109, 397, 70, 0, 0, 0; χ² = 271.71; 109/226.7 = 0.48
- Aimed map: extra empty squares and extra pile-ups | Verified | counts 399, 58, 37, 30, 13, 39; matches Clarke's description of clustering ("an excess number of squares containing either a high number … or none at all")
- Clarke: "…tended to be grouped in clusters"; 229, 211, 93, 35, 7, 1; χ² = 1.17; P = .88 | Verified | Berkeley-hosted scan of JIA 72:481; recomputed χ² = 1.169, p(df 4) = 0.883, and 88.1 % of the stored null maps score ≥ 1.169, so the episode's own simulated definition of p gives the same 0.88
- "precise aim would put factories at risk" | Verified | Shaw & Shaw 2019, Significance 16(5):12–17 (Wiley abstract): "if it could be accurately targeted at munitions factories it would also become a strategic threat to the war effort"
- Falk & Konold, 1997 · Psych. Review 104(2): the eye expects chance to look too even | Verified | psycnet record 1997-03612-004 (pp. 301–318): people "judge overalternating sequences as maximally random"; the paper also covers 2-D grids
- Aimed at central London, fell short | Verified | Evans & Delaney 2018, Applied Geography 99:44–53 (McGill-hosted PDF): Tower Bridge is the nominal aiming point and the mean point of impact lay in Dulwich, to the south
- North 1.9 vs Clarke's area 3.7 hits/km², "about half as dense" | Verified | 86/45 = 1.91 (my recount of real_data.npz) and 537/144 = 3.73
- North alone, p = 0.45 | Verified | my own 50,000-map Monte Carlo of 86 uniform hits in 180 squares gives χ² = 2.80 and p = 0.450
- Data: L. Shaw, 2025 · Zenodo 14883986 | Verified | zenodo.org/records/14883986, "V1 and V2 impact sites in London", creator Shaw, Liam

MECHANICS: runtime 3:34.6 · wpm 159 (speech time; 152 overall) · max silence 1.76 s (0:08.0, the planned prediction hold) · max static 2.57 s · −14.0 LUFS / −1.9 dBTP · leading 0.00 s, trailing 1.60 s · WER 3.1 %, no mistranscribed term ("Poisson", "lambda", "chi-squared" all heard correctly)

WHAT WORKS, IN SHORT. Three moves already meet the bar:
- The cold-open A/B commit ("A or B?" held 0:07.4–0:09.7).
- The reversal "Backwards." (0:35).
- "Thirty-nine targets, and chance predicts thirty-nine." (2:04–2:07): v1's failure is measured, and v2 explains it exactly.

The landing re-sees the first frame. The episode is honest, sourced and correct. What keeps it at 8.6 is that its central surprise (chance leaves about four squares in ten empty when hits average almost one per square) is computed for the viewer instead of being predicted by them, and the limit beat asserts its two key claims ("fits chance too", "hides in lambda") without making them visible.

FIXES (highest impact first):

1. [0:51.7–1:05.9][Hook + Clarity + Originality] The second prediction is arithmetic, not a guess, and the episode's central counterintuitive number is never dramatized.
   - Problem: during the "Guess how many squares stay empty" hold (1:00.4–1:03.9), the screen already shows "P(empty) = (1 − 1/576)^537 ≈ 0.3933" and "0.3933 × 576 ≈ ?" (kf_10, 1:03.9). The viewer is asked to multiply, not to commit, and nothing ever contrasts 227 with what intuition expects.
   - Change: ask before computing.
     - On map A alone (after "…expects chance to look that even."), put up the 24×24 grid and the GRAY line "537 hits · 576 squares".
     - Narrate: "Five hundred thirty-seven hits, five hundred seventy-six squares: almost one each. Guess how many squares stay empty." Hold 1.5 s on a lone yellow "empty squares ≈ ?" beside the map, with no formula.
     - Then run the current one-square build ("Each bomb has a one in five seventy-six chance… all five hundred thirty-seven must miss"). Write "0.3933 × 576 ≈ ?" after it, not during the hold.
     - Answer: "About two hundred twenty-seven: four squares in ten. Map A has two hundred twenty-two."
   - This is the Veritasium beat the episode is missing: most viewers anchor on "a few dozen", and that is the misconception the whole episode refutes.
   - Cost: about +4 s. Pay for it with fix 8.

2. [3:08.5–3:25.7][Clarity] "The aim hides in lambda, which the test holds fixed" is spoken over no visible λ.
   - Problem: the two areas are labelled "1.9 hits/km²" and "3.7 hits/km²" (sheet 11, 3:15–3:17). On "lambda" (3:22) only the formula's λ flags. The viewer has to work out alone that each area passed the test with a different λ.
   - Change:
     - Under the density labels, write the PURPLE "λ = 0.48" (north: 86/180) and "λ = 0.93" (Clarke's area: 537/576), or replace the densities with them. The narration's "half as dense" holds either way (0.48/0.93 = 0.51).
     - On "lambda", flag both λ labels together with the formula's λ, and connect them with a 0.6 s TransformFromCopy from the formula's λ.
     - Keep the "our count" credit and reword it "λ north: our count · L. Shaw, 2025 · Zenodo".

3. [3:17–3:25][Clarity + Visual] "It fits chance too" cannot be seen.
   - Problem: the north histogram (bars at most 115) is drawn on Clarke's 0–400 axis (kf_37, 3:19.3). Bars 2–5+ are a few pixels tall, the ×5 inset is empty, and p = 0.45 is asserted.
   - Change: when the north bars replace Clarke's, animate the y-axis to 0–120 (ticks 0, 40, 80, 120; 1.0 s) and fade the ×5 inset. Under the chart, write two rows, each number under its bar:
     - "chance 112 53 12.7 2.0 0.2 0.0" (PURPLE; 180·Poisson(0.478) = 111.6, 53.3, 12.7, 2.0, 0.24, 0.03);
     - "north 115 46 17 2 0 0" (BLUE).

4. [0:09.7–0:18.3][Hook + Clarity] The stakes sentence glues two claims together with "and".
   - Problem: "Londoners claimed flying bombs fell in clusters, and precise aim would put factories at risk" leaves the viewer to build the chain clusters → aim → factories.
   - Change the narration to: "In nineteen forty-four, Londoners saw flying bombs land in clusters. If that meant precise aim, factories were at risk." (+3 words, same picture.) The 3:07 line "London's clusters were no sign of precise aim" then answers it word for word.

5. [2:40.6–2:43.1][Clarity] "Aimed bombs would miss the other way" is ambiguous.
   - Problem: in an episode about bombs, "miss" is first heard as bombs missing their target, not the fit missing in the other direction.
   - Change: "Aimed bombs would break the fit the other way: extra empty squares, extra pile-ups." Check with whisper that "Aimed" survives (the voice notes' reason for avoiding "Aim would").

6. [1:06.0–1:11.0][Visual] The empty squares read as a maze.
   - Problem: the yellow outlines of the empty regions (kf_11, 1:08.7) form a lattice of lines over the whole map. "222 empty" does not read as 222 squares, and the outlines compete with the grid.
   - Change: fill the 222 empty cells with YELLOW at 35 % opacity, with no outline, and keep the dots at 60 %. On "pile-ups", turn the fill GRAY as now and add the blue 2+ outlines. That gives one focal layer per beat.

7. [1:19.0, 1:27.0, 1:39.0][Motion] Cross-fades leave visible double glyphs.
   - Problem, from the sheets (frames 2 s apart):
     - 1:19: two copies of 537 sit offset in λ's numerator, and "1"/"537" double up in P(empty).
     - 1:27: "P(empty)" and the yellow "0" are superimposed, with "mpty" legible behind the 0.
     - 1:39: the flying 1/576 overlaps "(1/576)²" before landing.
   - Change:
     - Use TransformMatchingTex for P(empty) → P(0), so "P(" and ")" persist, and FadeTransform only "empty" → "0", shifting the old glyphs up by 0.2.
     - For the carried copies, fade the source copy to 0 opacity during the last 30 % of its path, so only one glyph lands. Alternatively, land it on an invisible placeholder and reveal the target only after arrival.

8. [1:43.6–1:46.4][Concision] The spoken "Five thirty-six is almost five thirty-seven." repeats what the screen already does.
   - Problem: at 1:45 the 536 lights up and turns into a 537 in place, with the "≈" already on screen.
   - Change: cut the sentence (about 2.8 s) and let the 536 → 537 morph run in the 0.8 s beat gap after "e to the minus lambda again", flagging the 536 → 537 for 0.6 s. This pays for fix 1 and keeps the runtime at about 3:36.

9. [2:17.3–2:19.7][Audio] "Map A scores [pause 0.2] two point oh" lands as two sentences.
   - Problem: whisper transcribes it as "Map A scores. 2.0.", and the planned pause turns the score into an afterthought.
   - Change: remove the internal pause and speak "Map A scores two point oh." at speed 0.80 for this one sentence (the voice notes say Kokoro rushed it at 0.84).

10. [2:14.5–2:17.3][Clarity, nitpick] The whisker numbers invite a check that fails.
    - Problem: "±12" on bar 0 is the correct binomial s.d. (11.7), but the formula divides by chance's bar, 227 (√227 ≈ 15). A viewer who checks (4.7/12)² = 0.15 against the on-screen 0.10 finds a mismatch.
    - Change: keep the whisker lengths and drop their numeric labels, so the picture says "short bars wobble less" without implying that the divisor is the whisker's square.

REACHES 9 IF ALL FIXED: yes, narrowly.
- Fix 1 is the structural one. It turns 227 from a computed number into a refuted prediction, the episode's one memorable "chance leaves four in ten squares empty" moment. That lifts Originality to 9 and keeps Hook at 9 through the middle.
- Fixes 2–5 lift Clarity to 9: the limit becomes visible, the stakes chain is explicit and "miss" is no longer ambiguous.
- Fixes 3, 6 and 7 lift Visual and Motion to 9.
- Fix 9 lifts Audio to 9.
- With Clarity, Visual, Motion, Audio and Originality at 9 and Hook and Concision at 9, the weighted score is 9.0. Without fix 1 the episode stays around 8.8.

KEEP:
- The cold-open A/B commit, the "Backwards." reversal and the landing "If you chose map B, you chose the rule", which re-sees the first frame.
- "Thirty-nine targets, and chance predicts thirty-nine" (2:04–2:07), with the red 39-target brace over chance's 39.3: v1's failure explained exactly by v2.
- The honest limit built from measured data: the Evans & Delaney fall-short arrow, the north box at half the density that still fits chance (p = 0.45), and "the aim hides in lambda".
