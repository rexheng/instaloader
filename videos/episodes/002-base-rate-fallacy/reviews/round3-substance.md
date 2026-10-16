# Round 3 review: substance (science + story editor), episode 002

Evidence: I used the existing `review/` pack, because metrics.json (19:27) is newer than final.mp4 (19:25). I read:
- report.md and all 12 contact sheets;
- full-resolution keyframes kf_03 (0:15.3), kf_06 (0:28.3), kf_10 (0:58.0), kf_14 (1:26.7), kf_19 (1:45.1), kf_22 (2:00.7), kf_24 (2:12.8), kf_26 (2:25.7), kf_29 (2:36.3), kf_33 (2:54.9), kf_36 (3:10.2) and kf_40 (3:34.6);
- 22 frames I extracted with ffmpeg at 0:13.8, 1:41.0, 2:01.6–2:05.8 (10 crops of the formula), 2:03.0, 2:27.5, 3:04.6, 3:05.0, 3:05.4, 3:12.6, 3:13.4, 3:14.2, 3:18.6, 3:19.0 and 3:19.4;
- transcript.txt, transcript_words.tsv, narration.txt, script.md and facts.md.

I checked the sources on the web: BBC News 4 May 2018, The Guardian 5 May 2018, the Davies/Innes/Dawson 2018 PDF (cardiff.ac.uk), and Gigerenzer et al. 2007 (MPG PDF, PubMed, Frontiers 2015 citing it). I wrote this independently of the round-3 craft review and read only its header, after I had scored.

```
EPISODE: 002-base-rate-fallacy — "When a 99% Accurate Test Says You're Sick"
IDEA: A positive result doesn't give you the test's 99%; it shrinks the sample space to the people who tested positive, and when the condition is rare (1 in 500) that crowd is mostly false alarms, so the chance is 17%. Bayes' theorem, and a classifier's precision, is that share.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 7.5
WEIGHTED: 8.5 (847.5/100 = 8.475)   AFTER CEILING: 8.5 (ceiling = 7.5 + 2 = 9.5, not binding)
CAPS: none. Every number checks; every empirical claim is cited on screen; 0 banned phrases or patterns; mechanics are in range. Glyph collisions occur only inside transforms (≤ ~0.5 s at 1:41.0, 2:03.2, 2:05.8, 3:05.0, 2:27.5). I treat them as fixes, not cap 7, as rounds 1–3 did.
FINAL: 8.5   PASS: no
```

## FACTS

| Claim (spoken / on screen) | Status | Source / my check |
|---|---|---|
| Premise: 1 in 500 sick, the test catches 99%, wrongly flags 1% of the healthy; title "99% accurate" | Verified (premise) | With sensitivity = specificity = 0.99, accuracy = 0.99 at any prevalence, so the title is honest. But the video never says so (fix 1). |
| 10,000 people → 20 sick, 9,980 healthy; ≈ 20 and ≈ 100 positive | Verified | 20 × 0.99 = 19.8; 9,980 × 0.01 = 99.8; labelled "expected counts" (0:58) |
| "Of 120 positives, only 20 are sick. That's 17%" | Verified | 20/120 = 16.7%; exactly 19.8/119.6 = 99/598 = 16.56% → 17% |
| "The rule said 99, six times too high" | Verified | 0.99/0.1656 = 5.98 |
| Half sick: "Of the 5,000 who lit up, 99% are sick" | Verified | 4,950 + 50 = 5,000; 4,950/5,000 = 0.990 |
| 19.8/(19.8+99.8) → 20×0.99/(20×0.99 + 9,980×0.01) → ÷10,000 → 0.002, 0.998 | Verified | 20/10,000 = 0.002 ("two in a thousand"); 9,980/10,000 = 0.998; the ratio is unchanged |
| Bayes' theorem as shown at 2:12.8 | Verified | Re-derived: P(s∣+) = P(s)P(+∣s) / [P(s)P(+∣s) + P(h)P(+∣h)] (total probability in the denominator) |
| Sweep: "50% at 1 in 100, 99 at 1 in 2" | Verified at rest | 0.0099/0.0198 = 0.500; 0.495/0.500 = 0.990; 3:12.6 frame "1 in 100 / 50%" ✓; 3:14.2 "1 in 3 / 98%" ✓ (0.330/0.3367 = 98.0%). **In motion the meter lags the label**: 3:19.0 "1 in 74" with 64% (true 57.6%); 3:18.6 "1 in 5" with 97% (true 96.1%); 3:19.4 "1 in 394" with 21% (true 20.1%). Fix 3. |
| Landing flows "20 … along the red arrow, 100 along the blue" | Verified | Widths 19.8 : 99.8 |
| "recall" = 99%, "precision" = 17% | Verified | recall = TP/(TP+FN) = P(+∣sick); precision = TP/(TP+FP) = P(sick∣+) |
| Gigerenzer et al., 2007 · Psychol. Sci. Public Interest: "most doctors given a problem like this got it wrong" (21% right); after one session on natural frequencies, 87% right | Verified | Gigerenzer, Gaissmaier, Kurz-Milcke, Schwartz & Woloshin (2007), PSPI 8(2):53–96: 160 gynecologists; "the gynecologists' confusion disappeared; 87% of them now understood that 1 in 10 is the best answer"; also Frontiers in Psychology 2015 ("increased from 21 to 87%"). Waffle after training counts 3 + 80 + 4 = 87 green (kf_26). "Most doctors" generalizes from gynecologists, but the screen says "gynecologists" and the structure matches; acceptable. |
| "At the 2017 Champions League final, about 170,000 people were in Cardiff" | Verified | BBC 4 May 2018: "about 170,000 people were in Cardiff for the Real Madrid v Juventus game" |
| "The watch lists held about 1,200 faces" | Verified | Davies, Innes & Dawson 2018, Cardiff University: "In total, around 1200 images were enrolled onto watchlists for this event" |
| "raised 2,470 alerts. Only 173 were right, 7%" | Verified as the police figure, with a caveat | BBC, Guardian, Davies et al. ("2,470 total matches, 173 'true'"); 2,470 − 2,297 = 173; 173/2,470 = 7.0%. **Caveat:** the same Davies report's own analysis says "the proportion of true positives increased from 3% at the initial Champions League deployment to 46% at the Six Nations deployments", and that the pilot ran across the final *week* (city centre, fan zones, airport, station). The video's 7% is the force's figure, so it is not wrong, but "were right" states it more firmly than the sources do (fix 2). |
| "so even a small error rate per face would swamp the real matches" | Reasoning, sound | ≤ 1,200/170,000 = 0.7% could be listed, so a per-face false-match rate of order 0.1% already gives more false than true alerts. No number is claimed. |
| "Police also blamed poor-quality photos" | Verified | BBC: false matches "down to 'poor quality images' supplied by other agencies including UEFA and Interpol"; Davies: "A key influence upon these figures was the poor quality of many of the images" |
| "In machine learning, the share of alerts that are right is called precision" | Verified | definition |

No wrong or fabricated claims.

## MECHANICS

- Runtime 3:34.6.
- Pace: 154 wpm on speech time (148 overall), 530 words.
- Silence: longest internal 2.08 s, the planned "Pick a number" hold at 0:13.4–0:15.5. Leading 0.00 s, trailing 1.73 s.
- Longest static stretch 3.63 s (1:58.0–2:01.6).
- Loudness −14.1 LUFS, true peak −2.2 dBTP.
- WER 2.1%; the only differences are "a"/"one" and "head count"/"headcount".
- 0 banned phrases, 0 layout-audit issues.

No caps triggered.

## STORY / TRANSCRIPT NOTES

- **Hook (9).** Frame 1 is the problem itself. "Pick a number" at 0:12.6 gets a 2.1 s silent hold, so the viewer commits by 0:13. "Most doctors … got it wrong" at 0:15.5 raises the stakes with a cited baseline. The half-sick case, where the rule holds (0:27–0:43), sets up the measured failure: "six times too high", with a brace (1:11). The landing re-forms the exact cold-open diagram (3:05) and closes on a chiasmus that re-reads the opening 99%. This is textbook §6.
  - What stops it at 9.5: the title promises a "99% *accurate*" test, and "accuracy" is never named or paid off.
- **Clarity (8.5).** The count-then-shrink-then-formula chain (1:16–2:14) is the strongest stretch in the episode. The strip of 120 hangs under the meter with its red columns under the red share (kf_14). The formula is built term by term from the table, and "one glyph = one quantity" is respected.
  - Deductions:
    - the Cardiff beat presents 7% as a base-rate effect. Its own cited source attributes much of it to poor images and the old algorithm, and records 46% at later events. "Police also blamed poor-quality photos" (2:54) gestures at this but does not resolve it;
    - the live meter disagrees with its own prevalence label during the return sweep (3:18.6–3:19.4).
- **Slop scan.** I found no §4 phrases. There are no rhetorical-question chains: the one question, 0:09–0:12, is followed by an instruction. "All it does is…" (2:09) is plain, not a pattern. There is no recap ending.
- **Concision (8.5).** 20/100 is stated three times: 0:58–1:04, 1:27–1:33 and the landing 3:18–3:25. The third earns its place because it labels the flows, but it is the closest thing to slack.
- **Originality (7.5).** The medical-test premise and the Gigerenzer gynecologist statistic are exactly what 3Blue1Brown's *The medical test paradox* (2020) uses, and the "restrict to the evidence" picture is 3b1b's Bayes geometry. Veritasium's *Bayesian Trap* covers the same ground.
  - Fresh: the Cardiff precision case with the watch-list base rate, the prevalence sweep with people-width flows landing on the naive marker, and the recall/precision chiasmus.
  - Missing: the one non-obvious line this title invites (fix 1).

FIXES (highest impact first):
1. [2:57.8–3:02.5][Originality/Hook] The title's "99% accurate" is never paid off, and that is the episode's most shareable data-science point. After "…is called precision.", add: "And accuracy, the title's ninety-nine percent? The test is right about nine thousand nine hundred of ten thousand people. A test that calls everyone healthy scores ninety-nine point eight." On screen, in the landing diagram, write a grey "accuracy 99%" beside the badge. Under it, a grey "says 'healthy' to everyone: 99.8%" fades in on the second sentence and out before "Back to your test". The numbers: 19.8 + 9,880.2 = 9,900 of 10,000 is 99.0%; 9,980/10,000 is 99.8%. Add both to facts.md. This adds ~8 s, for a runtime of about 3:42.
2. [2:50.5–2:57.2][Clarity] Make the honest limit complete and attribute the figure accurately.
   - Change "Only a hundred and seventy-three were right" to "Police counted a hundred and seventy-three as right". Davies et al.'s own analysis gives 3% for this deployment.
   - Replace "Police also blamed poor-quality photos." with "With better photos and a new algorithm, later deployments got forty-six percent right."
   - On screen: grey note "later (Six Nations 2018): 46% right", with the citation "Davies et al., 2018 · Cardiff University" kept on until the note.
   - This shows that precision depends on the denominator's other term (the per-face error rate) and not only on the base rate. That is Bayes again, and it heads off the expert objection.
3. [3:18.4–3:20.0][Motion/Clarity] During the return sweep the meter lags its own prevalence label: "1 in 74" shows 64% (true 57.6%), "1 in 5" shows 97% (96.1%) and "1 in 394" shows 21% (20.1%). Drive the "1 in N" label, the flow widths and the meter from a single ValueTracker in one `add_updater` that computes P(sick∣+) from the same value each frame, with no second animated value. Lengthen the return to ≥ 1.5 s, using `smooth`.
4. [2:55–3:02][Visual] Word load is about 24 prose words in the kf_33 frame, against the 12 allowed: "watch lists: about 1,200 faces", "about 170,000 people", "chance an alert is right", "173 right", "2,297 wrong", "2,470 alerts", plus the note. When the raster finishes colouring (≈ 2:52), fade the two crowd labels to 0 and drop "2,470 alerts", since the braces already sum to it. Bring the crowd labels back only if they are needed.
5. [2:03.0–2:03.4, 2:05.6–2:06.0, 2:07.2][Motion] The naming steps cross-fade and leave ghost double glyphs ("0.002" under "P(sick)", "0.998" under "P(healthy)", "×0.99" under "P(+∣sick)"). Use `TransformMatchingTex` with an explicit `key_map`, or `FadeOut(old, shift=UP*0.2)` then `FadeIn(new, shift=UP*0.2)` with `lag_ratio` 0.5, so the two strings never overlap.
6. [3:04.8–3:05.2][Motion] The "99%" and "1%" rate labels double-strike while moving toward the nodes (frame 3:05.0 reads "99⁰⁄" and "1Ϋ"). Move the existing Tex objects with `.animate.move_to(...)` instead of transforming them into new Tex.
7. [1:40.8–1:41.4][Motion] Mid-rebuild, the denominator shows "20 ␣␣␣ + 99.8" with a visible hole and a misaligned bar. Do 19.8 → 20 × 0.99 in one `TransformMatchingTex` on the whole fraction, with the incoming "20" and "0.99" as `TransformFromCopy` from the table, so the bar stretches continuously.
8. [0:17–0:24, 2:17–2:26][Visual/Clarity] The waffle has 100 dots for 160 gynecologists, with no unit. Add a grey "1 dot = 1%" under "gynecologists", at Text size ≥ 18.
9. [3:18.0–3:21.5][Audio/Visual sync] "Twenty people reach **this plus sign**": in my sampled frames (3:19.4, 3:21, 3:23) the + badge is not visibly flagged. Scale-pulse the ring and badge (1.0 → 1.15 → 1.0, 0.6 s), keeping the colour, on "this plus sign".
10. [2:33–2:49][Clarity] The crowd squares the beam lights (145 squares = 2,470 at 17 per square) imply 2,470 distinct people flagged. Davies et al. report that the top 15 watch-list images produced more than 25% of all matches, and that the deployment covered the final week across several sites. Change "1 square = 17 people" to "1 square = 17 people · illustration".

11. [3:18.0–3:25.3][Concision] This is the third statement of 20/100 (after 0:58–1:04 and 1:27–1:33). Tighten "But for a random screen, twenty people reach this plus sign along the red arrow, and a hundred along the blue." to "On a random screen, twenty reach this plus along the red, a hundred along the blue." That saves about 2 s and offsets part of fix 1's 8 s.

REACHES 9 IF ALL FIXED: yes, narrowly, and only if fix 1 lands.
- Fixes 3–8 and 10 lift Visual and Motion to 9, and fix 2 lifts Clarity to 9. That alone gives 9·15 + 9·25 + 9·15 + 9·15 + 8.5·10 + 8.5·10 + 7.5·10 = 875, i.e. 8.75.
- Adding fix 1 (Originality about 8.5, Hook about 9.5) gives 8.9.
- 9.0 also needs Audio 9 (fix 9: every deictic lands on a flagged element) and Concision 9 (fix 11).
- The structural limit is that the premise and the cold-open statistic are 3b1b's *medical test paradox*. The accuracy-vs-precision line and a fuller Cardiff precision beat are what make the episode this channel's own. Without them, polish alone tops out near 8.8.

KEEP:
- The 120-person strip hanging under the meter, with its red columns exactly under the 17% red share, and the formula built term by term from it and the table (1:21–2:14).
- The SMH failure chain: the half-sick case where the rule holds, then the same test at 1 in 500 failing by a measured "6× too high" brace (0:27–1:11).
- The landing: the cold-open diagram re-formed, the prevalence sweep landing back on the naive 99% marker, and the recall/precision chiasmus over people-width flows (3:05–3:33).
