# Round 9: substance critic (facts, story, clarity, concision, slop)

Evidence: `review/metrics.json` (00:21) is newer than `final.mp4` (00:19), so I used the existing `review/` pack. I read:
- BAR.md in full; report.md, narration_diff.txt, transcript.txt, transcript_words.tsv (1:43–1:48 and 3:28–3:34), narration.txt, script.md, and facts.md (the Davies, Manrai and Cardiff rows);
- all 12 contact sheets;
- 13 full-resolution keyframes: kf_01 0:07.4, kf_06 0:44.4, kf_09 0:54.3, kf_14 1:20.7, kf_17 1:44.3, kf_18 1:49.8, kf_22 2:12.0, kf_26 2:24.5, kf_29 2:41.4, kf_34 3:00.4, kf_36 3:12.0, kf_39 3:34.1, kf_40 3:34.8;
- 9 extra frames I extracted with ffmpeg (/tmp/ep2r9/f_*.png): 0:12.6, 0:47.6, 2:21.0, 2:21.8, 3:20.5, 3:31.0, 3:32.6, 3:33.4, 3:33.9.

Re-verified by web on 2026-10-23:
- Manrai et al. 2014. JAMA Intern. Med. page and PMC4955674: 61 respondents; 14 gave the correct answer of 2%; the most common answer was 95%, given by 27 of 61.
- BBC News, 4 May 2018: about 170,000 people were in Cardiff for Real Madrid v Juventus. 2,297 of the matches were incorrect. The Guardian (5 May 2018) gives the same 2,470 / 2,297.
- Davies, Innes & Dawson 2018, cardiff.ac.uk AFRReportDigital.pdf, quoted directly:
  - "the total number was larger at the Champions League, 1200";
  - "the proportion of true positives increased from 3% at the initial Champions League deployment to 46% at the Six Nations deployments";
  - the table row "Champions League (4 days) | extremely large | 2632 | 78 (3%) | 1".

```
EPISODE: 002 — "When a 99% Accurate Test Says You're Sick"
IDEA: A positive result doesn't give you the test's 99%. It shrinks the sample space to the people who tested positive, and when the condition is rare most of that crowd are false alarms. Your chance is their red share (17%), which is Bayes' theorem and what machine learning calls precision, and it is why only 7% of Cardiff's 2,470 face-recognition alerts were right.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6 (862.5/100 = 8.625)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none.
  - 0 banned phrases. 0 banned patterns: no question chains (each question stands alone, at 0:07.6 and 0:24.1), no "it's not just", no fake reveals, and no lesson-list ending.
  - Every empirical claim carries an on-screen citation: BBC / South Wales Police from 0:03, Manrai from 0:31, Davies from 2:23.
  - All mechanics are inside the bar.
  - Every number re-checks (see FACTS).
FINAL: 8.6   PASS: no
FACTS:
- 1 in 500 sick, catches 99%, flags 1% of the healthy → 0.002·0.99 / (0.002·0.99 + 0.998·0.01) = 0.00198/0.01196 = 16.56% ≈ 17% | Verified | recomputed
- Per 10,000: 20 → 19.8 positive; 9,980 → 99.8 positive; "about 20 … about 100", "of 120 positives, only 20" (20/120 = 16.7%) | Verified | recomputed
- "The rule said 99, six times too high" / "99 ÷ 17 ≈ 6×": 99/16.56 = 5.98 | Verified | recomputed
- Half sick: 4,950 + 50 = 5,000 lit; 4,950/5,000 = 99% ("the rule holds") | Verified | recomputed
- Slider frames: 1 in 12 → 825/(825+92) = 90.0% (1:03); 1 in 470 → 21/121 = 17.4% (1:05) | Verified | recomputed from frames
- Formula chain: 20×0.99 / (20×0.99 + 9,980×0.01) → ÷10,000 → 0.00198 / (0.00198 + 0.00998); the ratio is unchanged; the named form P(s)P(+|s) / [P(s)P(+|s) + P(h)P(+|h)] | Verified | re-derived (law of total probability in the denominator)
- Landing sweep: 1 in 194 → 51/(51+99.5) = 34%; 1 in 100 → 99/(99+99) = 50%; 1 in 3 → 3,300/(3,300+67) = 98.0%; 1 in 2 → 99% | Verified | recomputed from frames 3:09–3:15
- "That 99%, the test's accuracy, is also its recall": sensitivity = specificity = 0.99, so accuracy = 0.99 at every prevalence, and recall = P(+|sick) = 0.99 | Verified | definitions
- Manrai et al. 2014, JAMA Intern. Med.: one Boston-area hospital; 23% right (14/61); most common answer 95% (27/61 = 44%); "their test: 5% false alarms" | Verified | jamanetwork.com/…/1861033, PMC4955674
- "Their most common answer was the test's own accuracy: 95%": an interpretation. With prevalence 1/1000 and a 5% false-positive rate, accuracy is 0.999×0.95 + 0.001×sens ≈ 95.0% whatever the sensitivity, so it holds | Verified (as interpretation) | recomputed
- Cardiff 2017: about 170,000 people; 2,470 alerts, 2,297 wrong → 173 right = 7.0% | Verified | BBC News 4 May 2018; Guardian 5 May 2018
- "For four days" | Verified | Davies et al. table, "Champions League (4 days)"
- "The watch lists held about twelve hundred photos"; "≤ 1 in 140" (170,000/1,200 = 141.7; an upper bound because some listed people were absent) | Verified | Davies et al. ("1200")
- Evaluators 3% (78/2,632) → Six Nations 46% (22/48) | Verified | Davies et al. key findings and table. Nit: 2,632 includes the police "blue" test list and 48 excludes it. The video makes the comparison the report itself makes, so this is not an error.
- "A new algorithm and better photos cut the false alarms … the blue term" | Verified (direction only) | Davies et al.: the new algorithm, plus high-standard custody images only after the final. The report also credits "operator familiarity", which the narration omits; that is an omission, not an error.
- 1 square = 17 people (170,000/10,000), labelled "illustration" | Verified | recomputed
MECHANICS: runtime 3:34.8 · wpm 148 (speech time; 476 words) · max silence 2.25 s (3:04.5, the planned "Back to your test" beat) · max static 3.13 s (2:39.0) · −14.0 LUFS / −1.8 dBTP · leading 0.00 s / trailing 1.58 s · WER 2.4%
FIXES (highest impact first):
1. [2:45–3:03][Clarity/Concision] For 18 s, kf_34 (3:00.4) shows "police count / 2,470 alerts" directly above "evaluators' count / final week · 2,632 alerts". These are two different alert totals for the same week, and nothing says why. The narration's only reason ("counted only alerts the logbooks confirmed") explains a lower *numerator*, not a larger *denominator*, so a careful viewer sees a contradiction exactly where the episode is asking for trust. Change: replace the second tag line with "logbook-confirmed" (not "· 2,632 alerts"), so the tag states the reason the bar is lower. Leave the 78/2,632 in facts.md. Also cut "Cardiff University's" from the narration: the citation is on screen, and it saves about 1 s. The sentence becomes "The evaluators counted only alerts the logbooks confirmed: three percent."
2. [1:43.8–1:47.1][Audio/Clarity] Whisper hears "twenty sick people times ninety-nine percent" as "26 people times 99%" (transcript_words 105.70–106.20). This is the one sentence where counts become a formula. A listener who hears "twenty-six" sees 20 × 0.99 at kf_18 and has to reconcile the two. Change narration to "Unrounded, the red count is the twenty who are sick, [pause 0.2] times ninety-nine percent; and the blue, every healthy person times one percent." Re-run whisper and confirm it reads "twenty who are sick".
3. [0:11.8–0:17.3][Hook/Clarity] "Each alert is a positive test result. One in five hundred people has *this* disease." "This" has no referent: no disease has been named, and the cold-open frame was about cameras. It is the episode's one non-sequitur, at the hinge between its two questions. Change to "Each alert is a positive test result. [pause 0.4] Take a simpler one: one in five hundred people has a disease." (+3 words; fix 1 frees the time.)
4. [2:17.9–2:35][Clarity] The crowd frame (kf_26, 2:24.5) shows "■ watch list · ≤ 1 in 140", the base rate that drives the answer. The narration never says it and never links it to the 7%: "Shrink to the alerts. Take the red share" just reads off the police count. The transfer from the disease to Cardiff is shown but never stated as Bayes, so the payoff demonstrates *precision* more than *base rate*. Change: replace "Every face they flagged joined the alerts." with "At most one face in a hundred and forty was on a list." (same breath length, about 2.3 s). Scale-pulse the "≤ 1 in 140" legend on "one in a hundred and forty". The beam still visibly files the flagged squares into the raster, so no information is lost.
5. [2:57.4–3:00.1][Clarity, nit] "That's the blue term in Bayes' denominator" credits the whole rise from 3% to 46% to P(+ | not listed). Davies et al. credit "both the new algorithm and increased operator familiarity", and the two events also differ in base rate and in which lists were counted. The direction is right, but the sentence is stronger than the source. Change: "That's mostly the blue term in Bayes' denominator." (+1 word), and leave the on-screen "P(+ | not listed) ↓" as is.
6. [3:00.4][Visual] The lever frame carries 3 bars, 6 tag lines, the dimmed Bayes denominator, "P(+ | not listed) ↓" and 2 citations. That is about 14 words of prose (citations excluded), over the 12-word limit, and two focal candidates (the 46% fill and the blue term) compete. Change: after "P(+ | not listed) ↓" has risen (≈ 2:59.5), fade the ghost denominator band to 0 over 0.5 s rather than holding it at 30%. With fix 1 the evaluators' tag is one line shorter, which brings the frame to ≤ 12 words.
7. [1:20.6–1:23.0][Motion/Clarity] "Six times too high" is spoken 1:21.1–1:22.3, but at 1:21.0 (sheet 5) "99 ÷ 17 ≈ 6×" is still at about 30%, and it is fully drawn only around 1:23. The measured failure arrives after its word. Change: start the bracket's grow on the onset of "six" (≈ 1:20.6), run_time 0.6, with the label written in the same 0.6 s.
8. [3:32.6–3:34.8][Hook/Motion, nit] My frames show the closing strip complete at 3:32.6, on "crowd", and the fade under way by 3:34.8, so the answer image is fully visible for about 1.6 s. Change: hold it 0.4 s longer before the 0.6 s fade. Trailing silence then rises from 1.58 to about 1.98 s, still ≤ 2 s.
REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1–5 take Clarity to 9, fix 2 takes Audio to 9, and fix 1 takes Concision to 9. With Visual 9 (fix 6) and Motion 9 (fix 7 plus the craft critic's motion items), the projection is about 9.0. Without the craft-side motion fixes it lands near 8.9. No structural change is needed: real cold open → naive rule → measured failure on a slider → picture-to-formula → the same raster answering the opening question.
KEEP:
- The prevalence slider (0:57–1:05). The half-sick block drains while the table ticks and the meter falls live from the naive 99% to 17%. The failure is measured, not asserted.
- The 120-person strip with the 20/100 brackets becoming 20/(20+100), then ÷10,000, then the named Bayes form (1:37–2:08). The formula is visibly read off the picture.
- The Cardiff raster bookend: 2,470 grey unchecked cells at 0:00, the same raster coloured at 2:35 ("173 right / 2,297 wrong", 7%), and the final yellow-outlined crowd under the 17% meter echoing it.
```

## Notes on the story (not scored separately)

- **Tension engine.** Two questions are open at 0:24: Cardiff, then "your" test. The second gets the real prediction hold ("your guess" sweeps the empty meter, 0:25–0:29) and the Manrai doctors' 95% as the reasonable wrong belief. That is the Veritasium misconception-first move, done with a real, correctly cited sample and not a straw man. Cardiff stays parked for 2 minutes and is paid off on its own raster. It works. Fix 3 removes the only jolt at the hinge.
- **Honest limit.** "Symptoms raise the one in five hundred" (3:07–3:17) states when the naive rule becomes right (1 in 2 → 99%). That is the episode's "where the method breaks", and it is better than a tacked-on caveat.
- **Slop scan.** Nouns and numbers throughout. The one dry line is "You'd start treatment today." The repeats ("one in five hundred" ×3; "shrink the sample space" ×2; "precision" ×2) are each deliberate callbacks, not restatements. The closing line reframes the test result, not a lesson list.
