EPISODE: 003 — "Which Map Is Random?"  (round 6, substance / science-and-story editor)
IDEA: Pure chance leaves about 227 of 576 squares empty, and those gaps push the hits to pile up, so clusters on their own are not evidence of aim. The honest test scores the whole count histogram against Poisson, and a pattern that is *too even* is the real sign of a rule. Clarke's 1946 V-1 data fit chance (p = 0.88).
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.5   AFTER CEILING: 8.5   (lowest 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none. Every empirical claim has an on-screen citation held for at least 3 s: Clarke + Shaw & Shaw 0:15–0:21, Falk & Konold 0:51–0:56, Clarke/Shaw 2:55–3:23, Evans & Delaney 3:15–3:23, "hits/km²: our count" 3:19–3:23. No banned phrases.
FINAL: 8.5   PASS: no

Evidence used: the review/ pack (metrics.json 18:06 is newer than final.mp4 18:04), report.md, all 12 contact sheets, keyframes at 0:14.7, 0:54.2, 1:22.3, 1:41.3, 1:53.9, 2:05.6, 2:22.9, 2:34.6, 2:42.2, 2:50.7, 3:01.5, 3:10.9, 3:23.5 and 3:34.7, extra frames at 0:46.0, 1:09.5, 2:36.0, 2:55.0 and 3:24.6, plus the transcript, script.md, narration.txt and facts.md.

## FACTS

Every number was recomputed from scratch (python, scipy). Citations were checked by web search.

| Claim | Status | Source / check |
|---|---|---|
| λ = 537/576 ≈ 0.93 | Verified | 0.9323 |
| P(empty) = (1 − 1/576)^537 ≈ 0.3933; × 576 ≈ 227 | Verified | 0.39333; 226.56 |
| (1 − λ/537)^537 ≈ e^−λ ≈ 0.3937 | Verified | e^−0.9323 = 0.39365 |
| Map A: 222 empty, 39 squares with ≥ 3 hits; map B: 0 squares with ≥ 3 | Verified | sim.py counts 222/223/92/28/9/2 and 109/397/70/0/0/0; both sum to 576 squares and 537 hits |
| 354 occupied squares share 537 hits (≈ 1.5) | Verified | 1.517 (but see Fix 1 on what this forces) |
| C(537,2) = 537·536/2!; 537·536 ≈ 537²; P(k) → λ^k e^−λ / k! | Verified | standard binomial → Poisson; 0.19 % error at k = 2 |
| Purple bars 227, 211, 98.5, 30.6, 7.1, 1.6; "chance predicts 39" (39.3) | Verified | 576·Pois(0.9323); 30.62 + 7.14 + 1.57 = 39.33 |
| Map A misfit terms 0.10, 0.64, 0.43, 0.22, 0.49, 0.12 → 2.0; "short bar counts more" | Verified | Pearson χ² = 2.000; χ²₄ tail 0.736 |
| "Three out of four simulated chance maps score worse … p = 0.74" | Verified (simulation not re-run) | facts.md reports 74.5 % of 20,000; the χ²₄ tail, 0.736, matches independently |
| Map B misfit 272 (271.7); "half the expected empty squares" (109/226.7) | Verified | 271.71; 0.48 |
| Aimed map: extra empties and extra pile-ups (399 empty; 39 squares at 5+) | Verified | bars at 2:50.7 match sim counts 399/58/37/30/13/39 |
| Clarke 1946, J. Inst. Actuaries 72:481: 537 bombs, 576 squares of ¼ km², observed 229/211/93/35/7/1, χ² = 1.17, P = 0.88 | Verified | scanned paper (doi:10.1017/S0020268100035435); recomputed χ² = 1.17, p(df 4) = 0.883 |
| "Londoners claimed flying bombs fell in clusters"; on-screen quote "…tended to be grouped in clusters" | Verified | Clarke 1946 p. 481 ("frequent assertions"); Shaw & Shaw 2019 |
| "precise aim would put factories at risk" | Verified | Shaw & Shaw 2019, *Significance* 16(5):12–17 (Wiley / ORA record confirmed) |
| "Your eye … expects chance to look that even" | Verified | Falk & Konold 1997, *Psychological Review* 104(2):301–318: over-alternating sequences are judged most random; the paper covers 2-D grids too |
| "aimed at central London but tended to fall short, so farther north, hits were about half as dense" | Verified | Evans & Delaney 2018, *Applied Geography* 99:44–53: Tower Bridge aiming point, mean point of impact in Dulwich, lower density north of the Thames; 1.9 vs 3.7 hits/km² is the channel's own count, credited on screen; 86/45 = 1.91, 537/144 = 3.73 |
| "Clarke chose an area where [λ] held steady" | Verified | Clarke 1946: mean density "not subject to material variation" |
| "≈ Clarke's area, re-created" rectangle holding 532 dots while the narration says 537 | Verified as honestly labelled | Shaw & Shaw re-creation; the table is Clarke's own counts |

No claim is wrong, fabricated or uncited.

## MECHANICS

runtime 3:34.7 · 157 wpm on speech time (151 overall), 492 words · max silence 1.76 s (the planned prediction hold at 0:08) · leading 0.00 s / trailing 1.62 s · max static 2.6 s · −14.0 LUFS / −1.5 dBTP · WER 2.5 % (the only differences are number formatting and "Clark" for Clarke, which sound identical) · 0 banned phrases · 0 black frames · layout audit 0 issues

## Transcript / §4 check

- **Banned phrases and patterns:** none. "Let's call…" (1:24) is not banned. The narration has only one question mark ("Which is chance?"), so there is no rhetorical-question chain. "Backwards." (0:38) is a genuine reversal, not a colon fake-reveal.
- **Hook:** two maps rain in from frame 1. "Which is chance?" lands at 0:07, followed by a 1.8 s hold over "A or B?", so the viewer commits by 0:09. The likely-wrong pick is B.
- **Ending:** it re-sees the opening frame exactly. "If you chose map B, you chose the rule" plays over the restored A/B frame at 3:31–3:33.

## Per-dimension notes

- **Hook 8.5.** This is a real commitment, with a sourced stakes line by 0:21 and a sharp reversal at 0:38. Two things keep it from a 9:
  - Tension flattens during the 43 s derivation (1:24–2:07). No new question is raised there, and six different numbers arrive between 1:35 and 1:55.
  - The stated stakes, "precise aim would put factories at risk" (0:18), are never explicitly answered. The video gives p = 0.88 (3:08) and moves straight to the caveat, so the viewer has to infer "so the factories were safe from precision".
- **Clarity 8.5.**
  - **Strengths:** concrete before abstract (one square, then 227 vs 222). The guess prompt at 1:04 works. p is defined as "the share of simulated chance maps that score worse", which is the clearest p-value definition in the series. Assumptions are stated (one λ).
  - **Deductions:**
    - "Those empty squares force the clumps" at 1:12.9–1:15 over-claims (Fix 1).
    - P(empty) silently becomes P(0) at 1:35.
    - (1 − λ/n)^n → e^−λ is asserted at 1:27–1:33 rather than shown. The 0.3933 vs 0.3937 check helps.
    - The 1:35–1:55 stretch is number-dense: 537, 536, 2, 576, 537 again, then 3 and k.
- **Visual 8.5.** The palette holds for the whole episode: blue is observed, purple is chance, red is flags and aim, yellow is focus. Charts are labelled, and the A/B frames are clean (0:14.7, 0:46.0). Deductions:
  - 2:25–2:45 is the busiest frame in the episode: two charts, two thumbnails, the dim P(k) line, the χ² readout, "20,000 chance maps simulated", p = 0.74, "B: 271.7" and the "227" label (kf 2:42.2).
  - At 2:36 the blue "109" sits inside chance's purple 0-bar outline, so it reads as chance's value.
- **Motion 8.5.** Motion is meaningful throughout:
  - the re-rain on "I dropped every hit" (0:41)
  - 537 carried into the exponent (1:01)
  - 536 → 537 morphed in place (1:51–1:53), and the 2 → 3 → k sweep (1:55–1:57)
  - count-by-count flight of squares into bars (2:09)
  - gap slivers that fly into terms and then into 2.0 (2:19–2:25)
  - the rectangle → equal-area square → map A landing (3:24.6)

  Small deductions: the aimed map → London change at 2:52–2:55 is a cross-fade with a 1–2 s near-empty left half, and the "0 empty" counter shows a momentarily false 0 at 1:09.5 before it counts up.
- **Audio 8.5.** All measured targets are met: 157 wpm, −14.0 LUFS, 6/6 deictics on an animation, planned holds of 1.8 s and 1.6 s. The longest run without a breath is 12.1 s, at 3:11.4–3:23.4: "The bombs were aimed … held steady", which carries two new ideas. The deliberate 0.53 s "A" at 3:26.9 may read as an odd emphasis. Nothing here was heard as mispronounced.
- **Concision 8.5.** 492 words; little is removable. The slack is in the 1:24–2:07 derivation, where three sentences each re-introduce 537/576 ("one in five seventy-six" also appears at both 0:56 and 1:44), and in the arch "Both are simulated. The question isn't." (0:09.7).
- **Originality 8.5.** Clarke's V-1 table is a textbook staple (Feller), and "which pattern is random?" is a known trope. The fresh parts are the "gaps force pile-ups" mechanism, the too-even fingerprint, the simulated-null p-value, and the Tower Bridge → Dulwich bias on the real map. Those are memorable; the frame of the episode as a whole is not new.

## FIXES (highest impact first)

1. **[1:12.9–1:20.4][Clarity]** "Those empty squares force the clumps", with the red 3+ outlines returning on "clumps" (sheet 1:15), over-claims. The arithmetic only forces 537 − 354 = 183 hits onto already-hit squares. All 354 occupied squares could hold one or two hits, so zero 3+ "targets" is possible. "So many must double up" is also loose: the forced quantity is hits, not squares.
   - **Narration:** "Those empty squares force the pile-ups: the other three hundred fifty-four share all the hits, so a hundred eighty-three hits must land where another already did."
   - **Screen:** on "pile-ups", re-show the blue 2+ outlines, not the red 3+ ones. Swap the "537 hits / 354 squares ≈ 1.5" line into "537 − 354 = 183 extra" on "a hundred eighty-three".
   - **Word budget:** cut "The other … so many must double up" as written; the replacement adds about 4 words.
2. **[3:08–3:11][Hook/Clarity]** The opening stakes ("precise aim would put factories at risk", 0:18) are never answered in words. Right after "Overall, p equals point eight eight." add one 10-word line: "London's clusters were map A's: no aim fine enough for a factory." Then go into "The bombs were aimed at central London…".
   - The line is supported by Clarke ("no support to the clustering hypothesis") and by Evans & Delaney's 12.5 km CEP; the E&D citation is already on screen from 3:15.
   - Pay for it by cutting "So look again." (3:24), which the landing transform already says.
3. **[1:33.8–1:36][Clarity]** P(empty) silently becomes P(0). Before "For two hits…", say "Call that P of zero" and TransformMatchingTex "empty" → "0" inside the existing P(empty) ≈ e^−λ line. Do not write a new P(0) line, so the viewer sees that it is the same quantity.
4. **[2:25–2:45][Visual]** The frame is overloaded (kf 2:42.2):
   - Fade the dim "P(k) ≈ λ^k/k! e^−λ Poisson" line to 0 for this stretch and bring it back at 2:52, where the aimed map needs it.
   - Remove the "227" bar label while B's bars are shown.
   - Shorten "20,000 chance maps simulated" to "20,000 chance maps (simulated)" on one line, placed above the "maps" axis.
5. **[2:34–2:38][Visual]** The blue "109" label sits inside chance's purple 0-bar outline (frame 2:36.0) and reads as chance's value. Place it under the purple "227", left-aligned as "B: 109" (BLUE), or to the right of the bar outside the outline with buff ≥ 0.15.
6. **[1:35.5–1:55][Clarity/Concision]** Too many numbers inside 20 s. Speak "pick two of the five hundred thirty-seven bombs: five thirty-seven times five thirty-six ways, over two". Change the second occurrence at 1:44 to "Each lands here with chance one in five seventy-six" without re-saying it as a new figure. Or drop the spoken "one in five seventy-six" there entirely and flag the (1/576)² term on screen while "each has the same chance" is spoken. This also removes the repeated phrase the report flags (0:56 / 1:44).
7. **[3:11.4–3:23.4][Audio]** 12.1 s with no breath across two ideas (the bias, then one-λ). Insert [pause 0.5] after "hits were about half as dense." so "The test needs one lambda" lands as the conclusion.
8. **[1:27–1:33][Clarity]** "almost exactly e to the minus lambda" is asserted. When "almost exactly" is spoken, flag 0.3933 and 0.3937 together in yellow for ≤ 1 s so the claim is checked visibly in the frame.
9. **[0:09.7–0:13.2][Concision/Originality]** "Both are simulated. The question isn't." is a writerly flourish. Tighten to "Both are simulated. London's version wasn't." That keeps the disclosure and points forward to the real data.
10. **[title/end card 3:34.7][Clarity]** Map B is also generated at random: random sequential addition with a spacing rule. The narration's "pure chance" vs "follows a rule" is the precise distinction, but the title "Which Map Is Random?" is loose. Consider "Which Map Is Pure Chance?" on the end card. Nitpick.

REACHES 9 IF ALL FIXED: yes, provided the fixes land cleanly. Fixes 1–3 lift Clarity and Hook to about 9: the one argumentative overreach is gone, the stakes are paid off, and the notation is continuous. Fixes 4–5 lift Visual to about 9, and fixes 6–7 lift Concision and Audio to about 9. That would give a weighted score of about 9.0. Originality stays at about 8.5 because the Clarke dataset is a textbook staple, so the margin is thin. No structural change is needed: the hook, the failure beat, the visual insight (227 predicted vs 222 empty) and the sourced payoff are all in place.

KEEP:
- The A/B cold open with the committed guess. It returns as the closing frame, and "If you chose map B, you chose the rule" plays over it.
- One square → (1 − 1/576)^537 → "guess how many stay empty" → 227 vs 222, with the empty regions outlined. This is the episode's one picture.
- The p-value defined as the share of 20,000 simulated chance maps that score worse, with A's 2.0 marker and B's 271.7 arrow off the axis. Keep the honest one-λ limit with the Tower Bridge → Dulwich arrow as well.
