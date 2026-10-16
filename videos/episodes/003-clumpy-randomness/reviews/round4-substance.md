# Round 4: substance review (science and story editor)

**Evidence.** I used the existing `review/` pack, because metrics.json (00:46) is newer than final.mp4 (00:43). I read:
- report.md, all 13 contact sheets, the transcript, narration_diff, narration.txt, script.md, facts.md and the CHANGELOG tail;
- 15 full-resolution keyframes: 0:08.0, 0:19.1, 0:57.7, 1:22.1, 1:37.5, 1:57.9, 2:08.9, 2:30.6, 2:36.4, 2:48.9, 2:54.5, 3:14.5, 3:34.3, 3:44.2 and 3:49.5;
- frames I extracted myself at 0:52.0, 1:13.2, 1:57.3, 2:23.6, 2:45.0 and 3:38.6, plus a 4-frame crop of the χ² readout from 2:44.4 to 2:46.2.

**Recomputation.** I recomputed every number independently with scipy, from `sim_data.npz` and `v1_impacts.csv`, without using `sim.py` or `realdata.py`.

**Citations.** I checked them by web search:
- Clarke 1946, JIA 72:481, through the Berkeley scan and Shaw & Shaw's verbatim quotes.
- Shaw & Shaw 2019, *Significance* 16(5):12–17, through the Wiley and ORA full text.
- Falk & Konold 1997, *Psych. Review* 104(2):301–318, through PsycNet and the SRRI abstract.
- The Zenodo record 14883986 (L. Shaw; V1-impacts.csv md5 matches).

```
EPISODE: 003 — "Which Map Is Random?"
IDEA: Pure chance leaves gaps, and the gaps force clumps, so clusters are not evidence of aim; the honest test scores the whole count histogram against Poisson's prediction, and a pattern that is too even is the real fingerprint of a rule.
SCORES: Hook 8.5 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 8.5 · Concision 9 · Originality 8.5
WEIGHTED: 8.8 (875/100 = 8.75)   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.8   PASS: no
```

## FACTS

| Claim | Status | Source / my check |
|---|---|---|
| Each map holds 537 hits on 576 (24 × 24) squares | Verified | sim_data.npz: a, b and aimed are each 537 points in [0, 24)² |
| Map A is uniform; counts 0…5+ = 222, 223, 92, 28, 9, 2; "39 targets" (≥ 3 hits) | Verified | recounted: 28 + 9 + 2 = 39 |
| "Map B gets none"; B counts 109, 397, 70, 0, 0, 0 | Verified | recounted |
| B's rule: "no two hits closer than four fifths of a square" | Verified | nearest-neighbour minimum 0.8005 (A: 0.050) |
| One bomb lands in a given square with chance 1/576; P(empty) = (1 − 1/576)^537 ≈ 0.3933 | Verified | 0.393332 |
| "0.3933 × 576 ≈ 227"; "about 227 stay empty"; "Map A has 222" | Verified | 226.54; exact 226.56; A = 222 |
| 354 squares share the hits, "one and a half each", "plenty must double up"; "131 squares with 2+" | Verified | 537/354 = 1.517; 92 + 28 + 9 + 2 = 131 |
| λ = 537/576 ≈ 0.93; 1/576 = λ/537; (1 − λ/537)^537 ≈ e^−λ ≈ 0.3937 | Verified | 0.93229; exact identity; e^−λ = 0.39365 |
| P(2) ≈ (537·536/2!)(1/576)² e^−λ; 537·536 ≈ 537²; P(k) ≈ λ^k e^−λ / k! | Verified (as ≈) | binomial-to-Poisson limit; 287,832 vs 288,369 |
| Purple bars 227, 211, 98.5, 30.6, 7.1, 1.6; "chance: 39.3" | Verified | 576·Pois(0.93229) = 226.74, 211.39, 98.54, 30.62, 7.14, 1.57; tail sum 39.33 |
| χ² terms 0.10 + 0.64 + 0.43 + 0.22 + 0.49 + 0.12 = 2.0 | Verified | 0.099, 0.638, 0.434, 0.225, 0.486, 0.119 (sum 2.00) |
| "Pure-chance maps score worse three times in four: p = 0.74" (20,000 simulated maps) | Verified | null array: 74.5 % ≥ 2.0; χ²₄ tail 0.736 |
| B: "half the expected empty squares", "a tower of single hits", misfit 271.7 ("272") | Verified | 109/226.7 = 0.48; 397 vs 211; χ² = 271.71 (the null's maximum is 36.6) |
| Aimed bombs give extra empty squares and extra pile-ups (simulated) | Verified | aimed sim 399, 58, 37, 30, 13, 39. This is Clarke's own description of clustering, as quoted in facts.md |
| 1944: Londoners claimed the flying bombs fell in clusters; quote "…tended to be grouped in clusters." | Verified | Clarke 1946, p. 481, quoted verbatim in Shaw & Shaw 2019 |
| Precise aim would put factories at risk | Verified | Shaw & Shaw 2019: "if it could be accurately targeted at munitions factories it would also become a strategic threat to the war effort" |
| "In 1946, the actuary R D Clarke published this test… 537, in 576 squares of south London" | Verified | JIA 72:481 (1946); F.I.A., Prudential; 144 km², 537 hits |
| Clarke's row 229, 211, 93, 35, 7, 1; χ² = 1.17, p = 0.88 | Verified | Shaw & Shaw Table 1; my recomputation χ² = 1.169, p(df 4) = 0.883 |
| "Single hits: 211, exactly as predicted" | Verified | 211 observed vs 211.39 expected |
| "No sign of clustering" | Verified | Clarke: "lends no support to the clustering hypothesis" |
| "Clarke chose an area where lambda held steady" | Verified | Shaw & Shaw: Clarke "selected a 144 km² area where the mean number of V-1s seemed roughly constant" |
| Aimed at London, "too loosely to choose a street" | Verified | Shaw & Shaw: V-1s "tended to fall short of the centre of London"; the 5 km scale bar matches the data's coordinates |
| "Farther north, hits fell about half as densely": 1.9 vs 3.7 hits/km² | Verified | my count: north box (E 526–535, N 181–186) 86/45 = 1.91; Clarke 537/144 = 3.73; ratio 0.51. Credited on screen as "our count · L. Shaw, 2025 · Zenodo" |
| "real V-1 hits, 1944–45" (887 dots); re-created rectangle holds 532 | Verified | 887 rows; Shaw & Shaw: "the map contains 887 V-1s"; 532 inside E 525–543, N 172–180 |
| "The detector, like your eye, expected chance to spread out that evenly" + "Falk & Konold, 1997 · Psych. Review 104(2)" | Verified | Falk & Konold, *Psychological Review* 104(2):301–318: people "judge overalternating sequences as maximally random", in sequences and 2-D grids |
| All on-screen citations: author, year, venue | Verified | none fabricated or misattributed |

All figures check out. Nothing is wrong, fabricated or uncited, so caps 4, 6 and 8 do not apply. There is one mild word/picture tension; see fix 6.

## MECHANICS

- Runtime 3:49.5, pace 161 wpm on speech time (154 overall), 588 words.
- Longest silence 1.98 s (the planned prediction hold at 0:09.8); leading silence 0.00 s, trailing 1.74 s.
- Longest static stretch 3.57 s (0:45.1–0:48.7).
- Loudness −14.0 LUFS integrated, −1.8 dBTP; no black frames.
- WER 3.3 %, 0 banned phrases.
- One clearance note at 2:05.8, mid-motion and not held.

None of these triggers a cap.

**§4 sweep (transcript).**
- No banned phrases. No "not just X", no rhetorical chains (only one question, at 0:08.7) and no signposting.
- "Backwards." (0:42.6) is a measured one-word reversal over a visible tag swap, not a fake reveal.
- The colons ("Map B's rule:", "The chi-squared misfit:") introduce definitions, not reveals.
- The one triplet, "half the expected empty squares, a tower of single hits, and a misfit of 272", is three concrete measurements, not abstract adjectives.
- The narration's voice is specific and numerical. I found no slop.

## SCORE RATIONALE (evidence for every move off 7)

**Hook 8.5.**
- Strengths:
  - The first frame is the puzzle itself, two maps raining 537 hits (0:01).
  - The commitment comes at 0:08.7, "Which one is chance?", with "A or B?" held on screen through a 2.0 s silence.
  - Stakes arrive by 0:24.
  - Tension rises through the detector's verdict "39 targets / 0 targets" (0:35–0:42) and breaks on "Backwards." (0:42.6).
  - A second arc, "were the V-1s aimed?" (0:15), pays off at 3:13–3:21.
  - The ending returns to the exact cold-open frame (3:41–3:47).
- Held below 9 by:
  - A sag at 1:31–2:14. Some 43 s of derivation (λ, e^−λ, P(2), P(k)) run without a stated purpose: no line says why we now need every bar and not just the empty ones. The last open question was answered at 1:14.
  - The cold-open puzzle, which of two dot patterns is random, is a familiar pop-science image, so savvy viewers will not commit to the wrong answer.

**Clarity 9.**
- Strengths:
  - The order is concrete first: one square, then 1/576, then 227 vs 222 (0:59–1:20).
  - The pigeonhole "gaps force clumps" step is shown with real counts (1:21–1:31).
  - P(2) is read off the picture (1:41–1:56). The ≈ is kept honest throughout.
  - The p-value is stated as a frequency, "worse three times in four" (2:32).
  - Assumptions are stated, "the test needs one lambda everywhere" (3:28).
  - Every number checks out.
- Nitpicks:
  - "over two" (1:44–1:48) is never explained, so a viewer who doesn't know combinations hits a bare 2!.
  - "One minus a small slice, raised to a big power, is almost exactly e to the minus lambda" (1:33–1:40) is announced as a fact. The numeric check 0.3933 vs 0.3937 rescues it.

**Visual 8.5.** The palette is semantic and stable: blue observed, purple chance, red flagged/aimed, yellow focus. Frames are mostly single-focus. Deductions:
- 2:51–2:56 (kf_28): the aimed histogram counts squares, but the aimed map has no grid, so "extra empty squares" cannot be seen on the map.
- 2:25–2:35 (kf_23): the dimmed "222 empty" label renders olive-brown. That is the exact colour problem the CHANGELOG says was removed elsewhere.
- 3:01–3:37 (kf_31): the "south London" rectangle visibly straddles the drawn Thames.

**Motion 9.**
- Strengths:
  - Cells fly into bars (2:19–2:21).
  - Gap slivers lift into the χ² terms and the terms fly into the readout (2:27–2:31).
  - P(2) becomes P(k) one glyph at a time (2:01–2:05).
  - The London rectangle opens into map A (3:38–3:41).
- Nitpick: a sub-second double-render of the readout at 2:45.0, "2771.7" ghosting, while the "B: 271.7" copy launches. It is clean by 2:45.6.

**Audio 8.5.**
- Strengths:
  - Pace and loudness are on target.
  - Deictics land: the red ring on "like this one" (0:33), the purple bars growing on "these purple bars" (2:13).
  - Pauses are intentional.
- Deductions:
  - 2:32.5–2:35.6: Whisper heard the key p-value line as "score worse three times **than** four". The "in" is under-articulated on the one sentence that defines p.
  - 3:43.6–3:47.9: the closing line was heard as "you **pick** the one following a rule". The "-ed" is swallowed before "the" on the last words of the video.

**Concision 9.** 3:49 is long for one idea, but each beat carries weight:
- the naive detector and its failure;
- the one-square derivation;
- the honest test on A, then B;
- what aim would look like;
- Clarke's real data;
- the limits;
- the landing.

I could not find a sentence to cut without loss.

**Originality 8.5.**
- Strengths:
  - Running the same honest test on the *too-even* map B (2:37–2:49).
  - The 20,000-map null drawn as a histogram (2:33–2:37).
  - Real digitised V-1 hits with the Thames (2:57–3:37).
  - The London rectangle morphing into map A (3:38–3:41).
- Held below 9: the core example (Clarke's V-1 Poisson fit) is the canonical textbook case (Feller), and the A/B dot-pattern opening is a well-worn trope (0:00–0:12).

## FIXES (highest impact first)

1. **[1:31–1:33][Hook + Clarity] The 43 s derivation has no stated purpose, so tension sags.**
   - Insert one line before "Call the average hits per square lambda.": "Empty squares are one bar. To judge a map, chance has to predict every bar."
   - On "every bar", flash the six empty bar slots: a GRAY dashed x-axis with ticks 0–5+ appearing faintly where the histogram will grow at 2:09.
   - Recover the ~3 s by cutting the 0.7 s pause after "the Poisson distribution." and the 0.5 s pause after "lambda.".
   - Effect: Hook to 9; it also sets up "The honest detector compares whole histograms" (2:15).
2. **[2:32.5–2:35.6][Audio + Clarity] "three times in four" reads as "than four".**
   - Rewrite it as "Three out of four pure-chance maps score worse: p equals point seven four.", spelled for Kokoro as "Three out of four pure chance maps score worse."
   - Re-synthesize, then confirm that Whisper hears "out of four".
3. **[3:43.6–3:47.9][Audio + Hook] The closing line loses its "-ed".**
   - Change it to "If you chose map B, you chose the one following a rule." "Chose" has no stop consonant to elide before "the".
   - Keep the 0.78 speed and the B frame flashing yellow on "rule".
4. **[2:51–2:56][Visual + Clarity] The aimed map has no grid, so its histogram's "extra empty squares" are invisible on the map.**
   - Draw the same 24×24 DIM grid as maps A and B under the aimed frame before the hits rain in.
   - On "extra empty squares", fill the 399 empty cells YELLOW at full strength for 1 s, then fade them out. Don't use a dimmed fill, because yellow at 35 % reads olive.
5. **[2:25–2:35][Visual] The dimmed "222 empty" label turns olive (kf_23).**
   - On "The chi-squared misfit", FadeOut the "222 empty" label instead of dimming it to 35 %.
   - Bring it back with A's thumbnail if needed. The thumbnail at 2:33 does not need it.
6. **[3:01.5–3:06.5][Clarity] "576 squares of south London" is spoken over a re-created rectangle that visibly crosses the Thames (kf_31).**
   - Either say "in five seventy-six squares of London" and keep the GRAY "re-created" tag,
   - or keep "south London" and add a GRAY "Shaw & Shaw's re-creation" tag in place of "re-created" while the narration names the area.
   - Either way, the word and the picture stop disagreeing.
7. **[1:44–1:48][Clarity] "over two" is unexplained.**
   - Say "five thirty-seven times five thirty-six ways, over two, because the order doesn't matter".
   - While that plays, swap the two yellow bombs in the big square in 0.6 s, which shows the double count. About +1.2 s.
8. **[0:00–0:03][Originality] The generic "which pattern is random" opening.**
   - Make frame 1 specific to the story: change "Each map holds five hundred and thirty-seven hits" to "Each map holds five hundred and thirty-seven bomb hits".
   - Retitle the counters "537 bomb hits" if the width allows.
   - This ties the familiar puzzle to the 1944 question from the first second, so "Both are simulated, but the question is real" lands as a turn, not a pivot.
9. **[2:44.8–2:45.6][Motion] The readout double-renders while the "B: 271.7" copy launches.** Start the copy only after the roll-to-271.7 finishes, wait 0.3 s, and copy from a fresh DecimalNumber, not the rolling one.

**REACHES 9 IF ALL FIXED: yes.**
- Fixes 1–3 lift Hook and Audio to 9.
- Fixes 4–6 lift Visual to 9.
- Fixes 1 and 8 lift Originality to 9 by tying the familiar opening and the derivation to the story's own question.
- Result: 0.15·9 + 0.25·9 + 0.15·9 + 0.15·9 + 0.10·9 + 0.10·9 + 0.10·9 = 9.0.

No structural change is needed. The science is clean, and what remains is narrative purpose in the derivation and four executional nitpicks.

**KEEP**
- The "39 targets, and chance predicts 39" failure-into-fix (2:21–2:24), with the gap slivers flying into χ² = 2.0 and then A's thumbnail landing on the 20,000-map null at p = 0.74.
- The same test catching the *too-even* map B at 271.7, plus the aimed simulation showing the opposite fingerprint (2:37–2:56).
- Clarke's real table building over the gridded V-1 map, the honest limits beat (one λ, the north box at 1.9 vs 3.7 hits/km²), and London's rectangle opening into map A for the landing.
