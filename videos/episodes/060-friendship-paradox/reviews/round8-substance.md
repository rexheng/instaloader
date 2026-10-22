# Round 8 — science and story editor (fact-check, hook and tension, clarity, concision, slop; every dimension scored)

**Evidence used**
- The `review/` pack. Its metrics.json (20:00) is newer than final.mp4 (19:58), so I reused it.
- report.md, narration_diff.txt, all 12 contact sheets, and these keyframes at full resolution: kf_01, 05, 10, 12, 15, 19, 20, 23, 25, 27, 33, 35, 37, 39.
- Extra frames I extracted with ffmpeg into /tmp/r8sub060 at 0:45.0, 1:39.5, 2:05.5, 2:19.3, 3:05.0, 3:05.8, 3:26.0, 3:28.3 and 3:29.5. I also took a pixel measurement of the "sides at ¼ scale" fraction in kf_19.
- transcript.txt, transcript_words.tsv (1:38–1:52), narration.txt, script.md, facts.md, and the round-7 substance review, to check which fixes were applied.
- Independent recomputation in Python from Feld's edge list:
  - Degrees: Betty 1, Sue 4, Alice 4, Dale 3, Pam 3, Jane 2, Carol 2, Tina 1.
  - Σk = 20, Σk² = 60, μ = 5/2, σ² = 5/4, Σk²/Σk = 3 = μ + σ²/μ.
  - Token layers: 20/8, 38/14 = 2.71, 52/18 = 2.89, 60/20 = 3.0.
  - Friends' means per girl: 4, 2.75, 3, 3.33, 3.33, 3.5, 2, 2.
  - Facebook: 2 × 68.7e9 / 721e6 = 190.6, and 635 − 190.6 = 444.4. That is 2.34× the mean.
- Citations checked online today:
  - Feld 1991, AJS 96(6):1464–77 (UVM PDF). Verified: the eight "Marketville" girls; "a total of 20 friends ... having a total of 60 friends, with a mean of 3.0"; 5 below, 2 above, 1 equal.
  - Ugander, Karrer, Backstrom & Marlow, arXiv:1111.4503 (PDF). Verified: "around 190", "⟨k²⟩/⟨k⟩ = 635", "92.7% of users have less friends than the average friend count of their friends", "cutoff at 5000", May 2011, 721 M users.
  - Christakis & Fowler, PLoS ONE 5(9):e12948, 15 Sep 2010 (journals.plos.org). Verified: Harvard College, late 2009, 744 students; "13.9 days (95% C.I. 9.9–16.6)" from clinical diagnoses; self-reported symptoms "3.2 days". The split N = 319 / 425 was verified in round 7 from the Methods text.

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each person once per friend she has, so the friend average is avg(k²)/μ = μ + σ²/μ (the cross term vanishes because distances from the balance point sum to zero), more than the person average whenever counts vary — which is why the friends students name are an early-warning sample for flu.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 8.5 · Concision 9 · Originality 9
WEIGHTED: 8.9 (887.5/100)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none (0 banned phrases/patterns; every empirical claim carries an on-screen citation; no wrong or fabricated claim; all mechanics in range; no placeholder text or render artifacts)
FINAL: 8.9   PASS: no
FACTS:
- 8 girls at an Illinois high school, every friendship among them | Verified | Feld 1991 Fig. 1 ("Marketville", Coleman 1961, The Adolescent Society; northern Illinois schools)
- Counts 1,4,4,2,3,3,2,1; "on average two and a half" | Verified | recomputed; Feld Table 1
- Ring "everyone has 2", 16 tokens, 32/16 = 2.0, labelled hypothetical | Verified | computed
- Real class: 20 tokens read 1–4, 60/20 = 3.0; "+0.5 · 20%"; "fell short by half a friend" | Verified | Feld p. 1467 "mean of 3.0 friends per friend"; 0.5/2.5 = 20 %
- Partial counters 27/9 (0:47), 58/19 (0:49) | Verified | consistent partial sums mid-flight
- "4 on Sue, 4 on Alice, 1 on Betty" | Verified | degrees
- Two girls at each count; girls balance at 2.5; tokens at 3; live fulcrum 2.7 / 2.9 / 3.0 | Verified | layer sums recomputed
- "Sue holds four tokens, each worth four: sixteen"; k² on top, k on bottom; (60÷8)/(20÷8) = 7.5/2.5 | Verified | algebra
- Distances 1.5/0.5; squares 2.25/0.25; σ² = 10/8 = 1.25 (population variance) | Verified | computed
- 4² = (2.5+1.5)² = 2.5² + 1.5² + 2·2.5·1.5 (= 6.25+2.25+7.5 = 16) | Verified | algebra
- avg(k²) = μ² + σ² + 2μ·avg(d), avg(d) = 0 because the beam balances | Verified | Σ(k−μ) = 0 by definition of μ; complete proof
- (μ²+σ²)/μ → μ²/μ + σ²/μ → μ + σ²/μ = 2.5 + 0.5 = 3.0; ring 2 + 0/2 = 2 | Verified | computed
- Facebook 2011 users averaged about 190 friends; a few had thousands; 5,000 limit | Verified | Ugander et al. 2011, arXiv:1111.4503
- Tokens average about 635 | Verified | Ugander: "expected number of friends at the end of a randomly chosen edge, ⟨k²⟩/⟨k⟩ = 635" — exactly the episode's token average
- 190 + 445 = 635; "spread term more than twice the mean" | Verified | 444.4 ≈ 445 > 380
- "93% of users had fewer friends than their friends averaged" (92.7 % on screen, "their own friends' average") | Verified | Ugander, per-user comparison
- Christakis & Fowler at Harvard; random students vs the friends they named; 319 / 425 | Verified | C&F 2010 PLoS ONE 5(9):e12948 (Harvard College, late 2009, 744 students)
- "Named friends have more friends, so they sit closer to everyone else" | Verified as C&F's stated rationale | C&F abstract ("individuals near the center ... infected sooner"; friends "known to be more central")
- Raw steps = C&F Fig. 3 (diagnoses) redrawn; dashed curves a disclosed logistic refit with the shift held at 13.9 d | Verified as disclosed | on-screen "Fig. 3 redrawn, logistic refit"; facts.md / sim.py
- "Fitted curves put them 13.9 days ahead" | Verified | C&F abstract, clinical diagnoses
- "With self-reported symptoms, the lead shrank to about three" (3.2 d on screen) | Verified | C&F abstract/Results
- "Betty looks at her one friend, Sue, and sees four. Most of us are Betty." | Verified as a fair per-person reading | Feld (5 of 8 below their friends' mean); Ugander 92.7 %
MECHANICS: runtime 3:31.8 · wpm 155 (speech; 140 overall; median sentence 171) · max silence 2.22 s (planned "Pick one" hold, 0:12.1–0:14.3) · max static 3.40 s (0:53.2–0:56.6) · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.90 s · WER 3.0 % (number formatting, girls'/girl's, "Split Sue's" → "Splitsus")
FIXES (highest impact first):
1. [1:36–2:21][Visual] Below the §5 type floor. The fraction in the label "sides at ¼ scale" is a stacked \frac{1}{4}. Its digits measure 19 px tall in kf_19 (numerator rows 481–499, denominator rows 512–530), below the 24 px minimum for ticks and citations and far below the 34 px label minimum. The fraction carries the label's only information: it says the squares are not drawn at beam scale. The layout audit missed it because it checks the whole Text/MathTex group, not its subparts. Change: replace it with an inline label, `Text("sides at 1/4 scale", font_size=26)`, or `MathTex(r"\text{sides at }1/4\text{ scale}", font_size=36)`. Keep it in the same place, left of the squares, with buff ≥ 0.15 to the first square. Then add a subpart-height check to the audit.
2. [3:05.3–3:06.6][Visual] The C&F hand-off tangles. At 3:05.8 (extracted), Sue's YELLOW ring overlaps Pam's BLUE ring. Sue's "4" token sits on top of Pam's digit, so the "3" is half hidden. Carol's ring and two "2" tokens hang below the x-axis line while the axes are already drawn. The round-7 hand-off is now populated, but for about 1 s it reads as a pile-up, not as "two groups go to two origins". Change: split the move into two 0.7 s passes on separate arcs. First, the named friends and their tokens arc along path_arc = +0.8 into the YELLOW origin, with tokens merging into their node in the first 0.2 s. Then the random students arc along path_arc = −0.8 into the BLUE origin. Scale every node to 0.6 at the start of its pass, and route both passes above the x-axis (y ≥ axis_y + 0.25 until the last 0.15 s). No two moving rings may come within 0.15 of each other.
3. [3:06.7–3:17.8][Audio] The episode's longest run without a breath of ≥ 0.35 s (11.2 s, per report.md) carries the three facts of the payoff: what was tracked, which curve rose first, and 13.9 days. Change: in narration.txt, add [pause 0.5] after "in the friends the students named." and [pause 0.4] after "The friends' curve rose first." This adds 0.9 s, giving about 3:32.7, inside the 3:35 budget. Cue the "rose first" flash to start on the first word after the new pause.
4. [1:46.2–1:47.0][Audio] "Split Sue's count, four" comes back from Whisper as "Splitsus count four" (transcript_words.tsv 106.31–106.81). The sibilant run "Split Sue's" smears the name on the step's key word, so I treat it as a likely mispronunciation under §7.4. Change: "Take Sue's four, [pause 0.3] and split it into the balance point, two and a half, [pause 0.4] plus her distance, one and a half." That adds 2 words. Keep the cue so that her 4 flies on "four".
5. [0:44.6–0:45.4][Motion] The dashed "guess" box re-opens leftward from the 2.5 tick, and its left edge slides through the word. At 0:45.0 (extracted) it reads "g|uess", with the dash crossing between the g and the u. Change: give the label an updater that keeps it at `box.get_left() + RIGHT*0.12` (left-aligned inside the box) while the box grows, or fade the label to 0 over the first 0.2 s and write it back once the box has settled.
6. [0:20.5–0:22.0, 0:42.8–0:44.0][Visual, nit] YELLOW still passes through brown during fade-outs: the candidates "2.5 3 4" and "?" at 0:21 (sheet 2), and the ring's tokens at 0:43 (sheet 3). Change: FadeOut these YELLOW elements in 0.3 s (not 1 s), or shrink them to their anchor point while fading, so that no frame shows them at 30–60 % opacity.
REACHES 9 IF ALL FIXED: yes. Fixes 1 and 2 lift Visual to 9, because every §5 standard is then met and no frame overlaps. Fixes 3 and 4 lift Audio to 9. With those two dimensions at 9 and the rest held, the weighted score is 9.0. No structural change is needed. The episode has a committed prediction by 0:12, a case where the guess works, and a measured +0.5 failure with its cause named. The beam turns into the formula by transformation, with a complete proof of the cross term. Two cited payoffs follow, with an honest limit (3.2 days), and the landing re-sees the cold-open frame and accounts for all three candidates.
KEEP: (1) The token-weighted beam. The YELLOW fulcrum slides 2.5 → 2.7 → 2.9 → 3.0 as each layer lands, then the signed distances merge into the 0 that kills the cross term (1:06–2:05). That is the proof, not decoration. (2) The friend bar as a YELLOW outline filled BLUE to μ and PURPLE beyond. It carries unchanged from the eight girls (2.5 + 0.5) to Facebook (190 + 445 = 635), and the "+0.5 ?" target held top-right through the derivation keeps the algebra pointed at the measured gap. (3) The fact discipline. The 635 statistic is exactly the token definition. The 92.7 % sits beside the person row and says "their own friends' average". The C&F illustration samples only the random students, matching the study design. The 13.9-day fit is disclosed as a refit, and the 3.2-day self-report result is stated as the limit.
```

## Notes by dimension (evidence)

**Hook 9.**
- What meets the 9 anchor:
  - Frame 0 (kf_01) already poses the question.
  - By 0:11 the three YELLOW candidates sit on the axis (kf_05), and "Pick one" is followed by a 2.2 s hold.
  - The stakes are done by 0:20.7 and come back at 2:56 with the same picture.
  - The derivation now has a visible target: "+0.5 ?" at full strength, top-right, from 1:33 to 2:21 (sheets 6–8).
  - The landing returns to the 0:11 frame. Betty's token reads 4, which accounts for the 4 candidate. The friend bar grows to the ringed 3 (kf_39). "Most of us are Betty" moves the result from the girls to the viewer.
- Residual: the title's "more" pre-refutes 2.5, so the commitment is really 3 vs 4. That is inherent to the series title, so I do not dock it.

**Clarity 9.**
- The order is concrete before abstract throughout:
  - the guess is tested where it holds (ring, 0:27–0:42), then fails by a measured +0.5 · 20 % (0:53);
  - the cause ("piled up unevenly") is named before any symbol appears;
  - Σk²/Σk becomes a balance point;
  - the cross-term cancellation is derived from the balance condition (2:00–2:06), not asserted.
- Every number recomputes. The C&F illustration now matches the study design: four BLUE random students, pairwise non-adjacent, send tokens only to the girls they name (kf_35).
- Not 9.5: the long derivation (1:31–2:21) packs about 12 numbers into 50 s (report: 6 different numbers in the busiest 20 s window). A first-time viewer may need to rewatch the split and square step.

**Visual 8.5.**
- Strong:
  - the semantic palette is held across all beats;
  - YELLOW no longer dims during holds (kf_15: the panel's YELLOW outline goes to 0, not to brown);
  - the 92.7 % block sits only beside the user row (kf_33);
  - the C&F read-out tips align with the in-chart arrow (kf_37);
  - the collapse lands on TeX's baseline (kf_25).
- Docked for:
  - the 19 px ¼ (fix 1), which fails a §5 standard;
  - the 3:05.8 node/token overlap during the hand-off (fix 2).
- Two minor issues puts this between the 8 and 9 anchors.

**Motion 9.**
- Objects persist and transform throughout:
  - counts fly into the bar (0:07);
  - nodes ride into the ring and the beam (0:29, 1:03);
  - the fulcrum is live;
  - distance segments drop and become squares (1:39);
  - signed labels merge into 0 (2:05);
  - the collapse is in place (2:19–2:21);
  - 190 / 445 / 635 drop out of their bar segments (2:45–2:47);
  - students and friends fly into their curve origins (3:05).
- 0 glyph morphs; the longest static stretch is 3.4 s.
- Fix 5 is a nit.

**Audio 8.5.**
- On target:
  - −14.0 LUFS, −2.1 dBTP;
  - 155 wpm on speech time, with planned holds (2.2 s after "Pick one", 1.6 s after the Facebook question, 1.0 s after "13.9 days ahead");
  - both deictics land.
- Docked for:
  - the 11.2 s breathless payoff run (fix 3);
  - "Splitsus" (fix 4).
- The held "one" in "Pick one" (0.55 s) is intended emphasis and not docked.

**Concision 9.**
- 495 words in 3:31.8, and every beat earns its place:
  - the ring is both the "works at first" case and the honest-limit callback at 2:24;
  - the C&F token picture sets up the curves.
- The eight repeats of "two and a half" each read a number off the screen.
- I found no removable sentence.

**Originality / non-slop 9.**
- The §4 checklist turns up nothing:
  - no banned phrase;
  - no rhetorical-question chain (each of the three questions stands alone, followed by silence or an answer);
  - no "it's not X, it's Y";
  - no recap ending.
- The token-stacked balance beam that slides from 2.5 to 3, and the variance squares hung under it, are an image a viewer would remember and reuse.
- Feld's eight girls and C&F's flu sensors are the canonical examples, but this angle on them is fresh.
