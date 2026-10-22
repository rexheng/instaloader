# Round 8 — craft critic (visual design, motion, A/V sync; every dimension scored)

Evidence used:
- The `review/` pack. metrics.json (20:00) is newer than final.mp4 (19:58), so I used the existing pack.
- report.md, narration_diff.txt, all 12 contact sheets, and these keyframes at full resolution: kf_01, 05, 10, 14, 17, 18, 19, 20, 22, 25, 26, 27, 30, 33, 35, 37, 38, 40.
- Extra frames I extracted with ffmpeg into /tmp/r8craft060:
  - single frames at 0:21.3, 0:44.6, 0:45.4, 1:39.8, 1:47.6, 1:49.8, 2:18.6, 2:19.4, 2:22.0, 2:42.8, 3:05.6, 3:06.2, 3:27.8, 3:28.6, 3:29.8;
  - strips at 2.5 fps over 1:00.6–1:05.4 (network → beam), 2:56.0–3:00.4 (C&F entrance) and 3:26.6–3:31.4 (landing);
  - a strip at 3.75 fps over 2:44.8–2:48.0 (Facebook number flights).
- transcript.txt and transcript_words.tsv, narration.txt, narration.json word timings, script.md, facts.md, and the round-7 reviews (used only to check which items this cut addresses).
- I recomputed every number from the degree list 1, 4, 4, 2, 3, 3, 2, 1 (Betty, Sue, Alice, Jane, Dale, Pam, Carol, Tina), using the 10 edges drawn at kf_05.

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: A friendship lands on each girl once per friend she has, so the friend average is avg(k²)/μ = μ + σ²/μ; the cross term dies because the distances from the balance point sum to zero. That beats the person average whenever counts vary, which is why named friends catch flu first.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 9 · Originality 9
WEIGHTED: 8.8 (880/100)   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, does not bind)
CAPS: none. 0 banned phrases or patterns. Every empirical claim has an on-screen citation (Feld/Coleman, Ugander, C&F). No overlap or clipping in settled frames (layout audit 0/206). Runtime, pace, silences, static stretches and loudness are all in range.
FINAL: 8.8   PASS: no
FACTS:
- 8 girls, 10 friendships, counts 1,4,4,2,3,3,2,1; μ = 20/8 = 2.5 | Verified | Feld 1991 AJS 96(6) Fig. 1 (Coleman 1961 "Marketville"); recomputed
- "an Illinois high school" | Verified | facts.md: Coleman's 10 northern-Illinois schools (GESIS ZA1196)
- Ring: 16 tokens, 32/16 = 2.0 | Verified | computed; labelled "(hypothetical)"
- Real class: 20 tokens, 60/20 = 3.0; live count 58/19 at 0:49 (the 20th token reads 2); +0.5 = 20 % of 2.5 | Verified | computed; Feld 1991
- Fulcrum 2.5 → 2.7 (38/14) → 2.9 (52/18) → 3.0 (60/20) | Verified | layer sums 20, 18, 14, 8
- Sue 4 × 4 = 16; Σk² = 60; Σk²/Σk → avg(k²)/μ = 7.5/2.5 = 3.0 | Verified | computed
- Distances ±1.5/±0.5; squares 2.25/0.25; σ² = 10/8 = 1.25 (population variance); square sides 84 px and 27 px = ¼ of 324 and 108 px of ruler | Verified | computed; measured on kf_18
- 4² = (2.5 + 1.5)² = 2.5² + 1.5² + 2·2.5·1.5 = 6.25 + 2.25 + 7.5 = 16; avg(d) = 0 ⇒ avg(k²) = μ² + σ² = 7.5 | Verified | algebra
- μ + σ²/μ = 2.5 + 0.5 = 3.0; ring 2 + 0/2 = 2 | Verified | computed
- Facebook 2011: mean 190 friends; ⟨k²⟩/⟨k⟩ = 635 (= the token average); 445 > 2 × 190 | Verified | Ugander et al. 2011 arXiv:1111.4503 ("expected number of friends at the end of a randomly chosen edge, ⟨k²⟩/⟨k⟩ = 635"), per facts.md
- "a few had thousands"; 5,000 limit | Verified | Ugander et al. 2011
- 92.7 % (spoken "93 %") had fewer friends than their own friends' average | Verified | Ugander et al. 2011 (per-user statistic; the on-screen wording "their own friends' average" is correct)
- C&F Harvard 2009: 319 random students, 425 named friends; fitted lead 13.9 d; self-reported 3.2 d | Verified | Christakis & Fowler 2010 PLoS ONE 5(9) e12948 (Abstract; Results "3.2 days, 95% C.I. 2.2–4.3")
- Dashed fits are a logistic refit with the shift held at 13.9 d; in-chart arrow measures 140 px ≈ 13.8 d at 305 px per 30 d | Verified as disclosed ("Fig. 3 redrawn, logistic refit") | sim.py, facts.md; measured on kf_37
MECHANICS: runtime 3:31.8 · wpm 155 (speech time; 140 overall; median sentence 171) · max silence 2.22 s (planned "Pick one" hold, 0:12.1) · max static 3.40 s (0:53.2–0:56.6) · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.90 s · WER 3.0 % (number formatting, a homophone, and "Splitsus")
FIXES (highest impact first):
1. [3:27.6–3:30.0][Motion/Audio] The climax is rushed and fights the last line.
   - In the 2.5 fps strip, four moves happen inside about 1.2 s (3:28.0–3:29.2), all under the words "Most of us are Betty": the girl bar and its 2.5 flash, every friendship flashes, the "?" and drop lines leave, and the friend bar grows to the ringed 3 while the 4 leaves. None of them gets reading time.
   - Meanwhile the sentence names Betty, whose pulse only comes at 3:29.4, after the bar has already taken the eye.
   - Change: lengthen the [pause 0.8] after "sees four" to [pause 2.6] and play the accounting silently in three separated beats:
     - (a) 3:27.8: the girl bar and the 2.5 candidate flash BLUE (0.6 s).
     - (b) 3:28.6: every friendship flashes, then the friend bar grows to 3 with a 1.0 s smooth rate.
     - (c) 3:29.8: ring the 3 while the 4 leaves (0.5 s).
   - Then speak "Most of us are Betty" (≈3:30.4) with only Betty and her token pulsing. Start the end card 1.5 s after the last word.
   - Runtime becomes about 3:33.6, still under the 3:35 budget.
2. [1:01.8–1:03.4][Motion] In the network → beam sort the nodes cross through one another.
   - In the 1:00.6 strip (frames at 1:02.2, 1:02.6 and 1:03.0), Tina, Jane, Carol and Pam pile into one cluster with their names stacked ("Tin(1)ne Carol Pam") for about 1 s. Sorting is the meaning of the move, but here it reads as a jumble.
   - Change: move in two stages. First drop every node straight down, x unchanged, to a staging row 0.6 above the beam (0.5 s). Then slide each one horizontally to its sorted slot (1.0 s), with alternating path_arc ±0.35 and lag_ratio 0.08 so no two paths intersect.
   - Fade the names to 0 over 0.2 s before stage 2 and back in after landing.
3. [2:24.0–2:28.0][Visual] The ring callback leaves a truncated equation on screen.
   - With YELLOW sent to 0, the dimmed result row reads "μ + σ²/μ = 2.5 + 0.5" with "= 3.0" missing (kf_27). The 30 % BLUE bars turn navy, which reads as a fourth hue beside the thumbnail's full BLUE.
   - Change: during the callback, take the whole result row to 0 rather than part of it, and restore it complete at 2:27.6 with the bars.
   - Dim the BLUE bars to 45 % instead of 30 %, so they stay recognisably BLUE.
4. [3:31.0–3:31.8][Visual] The end card cross-dissolves over the still-visible class and bars.
   - In the landing strip at 3:31.0, "Ω Sample Space" sits on top of Pam, Alice and the friend bar.
   - Change: FadeOut the whole scene over 0.5 s, then FadeIn the end card. No frame should hold both.
5. [0:21.3, 0:45.4, 1:00.6, 2:22.0, 3:00.8][Visual] YELLOW still passes through khaki/tan whenever it fades, despite the round-7 rule.
   - Examples: the "named friend" label at 0:21.3; tokens fading in at 0:45.4 and 3:00.8; the stacked tokens fading out at 1:00.6; the returning 3.0 fulcrum at 2:22.0.
   - Each lasts 0.3–0.6 s. Together they make the YELLOW hue unstable at every entrance and exit.
   - Change: for YELLOW mobjects use GrowFromCenter / ShrinkToCenter at full opacity, or fly the tokens in from their source node at full opacity. Keep any opacity ramp ≤ 0.2 s.
6. [1:46.3, 3:26.1][Audio] Two small articulation problems.
   - Whisper hears "Split Sue's" as one word, "Splitsus" (transcript 106.31): the narration.json gap between "Split" and "Sue's" is 0.02 s.
   - In the closing line, the comma before "Sue" is only 0.17 s, so "her one friend Sue" runs together.
   - Change: "Take Sue's count, four, …" (or "Split [pause 0.15] Sue's count"), and "her one friend, [pause 0.3] Sue, and sees four".
7. [1:39.5–1:43.0][Visual] The eight area labels read as one long string of digits.
   - "2.25 2.25 0.25 0.25 0.25 0.25 2.25 2.25" sits at about 20 px (0.15 unit) gaps, the clearance floor (kf_18).
   - Change: set them at MathTex 30 (above the 26 floor) so the gaps are ≥ 40 px, or drop them 0.1 lower and alternate their y by ±0.12.
8. [2:49.0–2:56.0][Visual] Word load is over the limit.
   - With the 92.7 % block written, the frame carries about 18 prose words: "average user", "average friend", "friends (count)", "a few users", "Facebook's limit", plus the 7-word block. That exceeds the 12-word limit (kf_33).
   - Change: shorten the block to "92.7% / below their own friends' average" (5 words), and fade "a few users" with its brace and "Facebook's limit" to 0 when the block writes. They have done their job by then.
9. [2:45.6–2:46.4][Motion] The YELLOW "635" copy crosses the dimmed axis between the 600 and 800 ticks.
   - In the 3.75 fps strip it sits on the axis line at 2:46.1.
   - Change: route it with path_arc −0.5 to the right of the 800 tick and keep it at 0 opacity until it is 0.3 below the axis labels, as 190 and 445 already do.
REACHES 9 IF ALL FIXED: yes, narrowly.
- Fixes 1, 2 and 9 lift Motion to 9.
- Fixes 3, 4, 5, 7 and 8 lift Visual to 9.
- Fixes 1 and 6 lift Audio to 9: the last line lands on Betty, and the two run-togethers go.
- With every dimension at 9, the weighted score is 9.0.
- No structural change is needed. All the beats are present and earn their time: the misconception hook with three candidates, the ring case where the guess holds, the measured +0.5 failure, the beam proof with a visible target ("+0.5 ?"), the Facebook transfer test, the C&F payoff with its honest 3.2-day limit, and a return to the 0:11 frame.
KEEP:
1. The token-weighted beam (1:06–2:05): the YELLOW fulcrum slides 2.5 → 2.7 → 2.9 → 3.0 as each layer lands, then the signed distances merge into the PURPLE 0 that replaces avg(d). The animation is the proof.
2. The open target "+0.5 ?" held top-right through the derivation (1:33–2:21), and the result's 0.5 flying into it on "exactly the extra half friend we measured" (f 2:22.0).
3. The friend bar as a YELLOW outline filled BLUE to μ and PURPLE beyond. It is carried unchanged from the class (kf_26) to Facebook 190 + 445 = 635 (kf_33), with each number dropping out of its own bar segment.
```

## Notes by dimension

**Hook 9.**
- The first frame is already the question: the network, plus ghosted "average girl / average friend ?" rows (kf_01).
- The prediction is concrete: three YELLOW candidates, 2.5, 3 and 4, each above its own axis tick (kf_05). "Pick one" is followed by a 2.2 s hold.
- The stakes arrive by 0:14–0:20, with Jane ringed "random" and an arrow to Alice, "named friend".
- The derivation no longer sags: the "+0.5 ?" tag keeps the question on screen.
- The landing returns to the exact 0:11 frame (kf_38). "Most of us are Betty" reframes it around the viewer.
- What keeps this from 10: the title gives away the direction ("more"), and the resolution itself is rushed (fix 1).

**Clarity 9.**
- Everything is concrete before it is abstract: the ring check, the token count, the layer-by-layer fulcrum, then Σk²/Σk, then ÷8, then the variance squares, then the cross term.
- Every number checks out (see FACTS).
- The sampling design in the C&F beat now matches the study (kf_35): four non-adjacent random students, and only their named friends ringed YELLOW.
- The 92.7 % wording is the per-user statistic.
- The ¼-scale tag is at full strength while the squares are on screen.

**Visual 8.5.**
- The palette is disciplined: BLUE is a person, YELLOW is reached by a friendship, PURPLE is spread.
- Type sizes and safe area are fine, and the citation is at y ≈ −2.96 on every beat.
- The read-out arrow now sits directly above the in-chart arrow (kf_37, tips at x ≈ 795 px).
- What remains, each minor but together more than two:
  - the truncated, navy-dimmed callback frame (2:24–2:28);
  - the end card dissolving over the scene (3:31.0);
  - YELLOW turning khaki whenever it fades;
  - packed area labels (kf_18);
  - an 18-word frame at 2:53.

**Motion 8.5.**
- Objects persist and transform almost everywhere: tokens to stacks, the fulcrum slide, distances to squares to σ², signed distances to 0, numbers dropping out of bar segments.
- The C&F hand-off is fixed: the axes are drawn first (f 3:05.6, 3:06.2), and no frame is empty.
- The two-step collapse now stays on the baseline (f 2:18.6, 2:19.4).
- Two moves fail the reading-time and correspondence test: the colliding sort at 1:02–1:03, and the 1.2 s four-move landing.

**Audio 8.5.**
- Measured values: −14.0 LUFS, −2.1 dBTP, 155 wpm.
- The pauses are shaped: 1.6 s before "About 635", 2.2 s after "Pick one", and 0.4 s breaths inside the split sentence, so each number lands before the next is spoken.
- Both deictics land.
- Deducted for the "Splitsus" run-together and the 0.17 s comma before "Sue". The final line lands on the bar animation rather than on Betty (fix 1).
- The median sentence pace of 171 wpm is at the top of comfort but acceptable.

**Concision 9.**
- 495 words in 3:31.8.
- The eight "two and a half"s are each the number being operated on, not restatement.
- The ring callback ("With no spread, the ring had no gap") earns its 3 s.

**Originality 9.**
- The moving fulcrum and the "distances add to zero" kill of the cross term are a non-obvious, memorable way to show ⟨k²⟩/⟨k⟩ = μ + σ²/μ.
- The Betty ending is specific to this dataset.
