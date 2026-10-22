# Round 8: substance critic (facts, story, clarity, concision, slop)

Evidence: `review/metrics.json` (22:47) is newer than `final.mp4` (22:45), so I used the existing `review/` pack. I read:
- report.md, narration_diff.txt, transcript.txt, narration.txt, script.md, facts.md (in full), and the headers of the round-7 substance and round-8 craft reviews (only to see which fixes landed);
- all 13 contact sheets;
- 12 full-resolution keyframes: kf_02 0:08.8, kf_06 0:39.0, kf_09 0:48.0, kf_15 1:19.5, kf_17 1:37.5, kf_22 2:04.5, kf_24 2:14.5, kf_28 2:30.8, kf_33 2:55.6, kf_36 3:06.5, kf_38 3:20.2, kf_40 3:40.3;
- 10 extra frames I extracted with ffmpeg (scratchpad r8s/): 0:26.5, 0:27.8, 1:29.5, 2:58.0, 2:58.8, 3:07.8, 3:08.6, 3:09.4, 3:10.0, 3:10.5.

Citations re-verified by web search and scrape on 2026-10-22:
- Manrai et al.: the PMC4955674 full text. Quoted: a convenience sample of 24 attending physicians, 26 house officers, 10 students and 1 retired physician "at a Boston-area hospital"; prevalence 1/1000 with a 5% false-positive rate; 14 of 61 correct (23%); most common answer 95%, 27 of 61 (44%).
- BBC News, 4 May 2018: about 170,000 people; 2,470 potential matches, 2,297 wrong. The Guardian (5 May 2018) and WalesOnline give the same numbers.
- Davies, Innes & Dawson (2018), Cardiff University PDF:
  - "around 1200 images were enrolled onto watchlists for this event";
  - "proportion of true positives increased from 3% at the initial Champions League deployment to 46% at the Six Nations … due to both the new algorithm and increased operator familiarity";
  - "2632 matches (alerts) … 3% (N=78) were 'true positives' (confirmed by the operators)";
  - Six Nations: 56 matches, 48 after removing blues;
  - "Of the initial 22 'true positives' … 32% (n=7) … turned out to be false positives".

```
EPISODE: 002 — "When a 99% Accurate Test Says You're Sick"
IDEA: A positive result doesn't hand you the test's 99%. It shrinks the sample space to everyone who tested positive. When the condition is rare that crowd is mostly false alarms, so your chance is its red share, 17%. That share is Bayes' theorem, a model's precision, and the reason only 7% of Cardiff's 2,470 face-recognition alerts were right.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 8.5
WEIGHTED: 8.5 (845/100 = 8.45)   AFTER CEILING: 8.5 (lowest 8 + 2 = 10, not binding)
CAPS: none.
  - 0 banned phrases or patterns (no question chains, no fake reveals, no lesson-list ending).
  - All mechanics are inside the bar.
  - Every empirical claim carries an on-screen citation.
  - Borderline, not applied:
    - From 2:58.5 to 3:06.4 the evaluators' bar shows "3%" next to the tag "Six Nations 2018 · 48 alerts". My frames at 2:58.0, 2:58.8 and kf_36 3:06.5 show this.
    - 3% is the final-week figure, so for about 8 s the chart pairs a value with the wrong event.
    - The narration frames it as before → after ("Months later … rose to 46%"), so I read it as a sequencing defect, not a factual error.
    - A stricter reading of "error in plotted data" triggers cap 6, so fix 1 is mandatory.
FINAL: 8.5   PASS: no
FACTS:
- 1 in 500 sick, catches 99%, flags 1% of the healthy → 0.002·0.99 / (0.002·0.99 + 0.998·0.01) = 99/598 = 16.56% ≈ 17% | Verified | recomputed
- Per 10,000: 20 → 19.8 positive; 9,980 → 99.8 positive; shown as 20 / 100 / 120 ("about"); 20/120 = 16.7% | Verified | recomputed
- "The rule said 99, six times too high" / "99 ÷ 17 ≈ 6×" (5.8; exact 5.98) | Verified | recomputed
- Half sick: 5,000 → 4,950 and 5,000 → 50; 4,950/5,000 = 99%, "the rule holds" | Verified | recomputed
- Slider frames: 1 in 3 → 3,300/3,367 = 98.0% (1:01); 1 in 296 → 33/133 = 24.8% → 25% (1:03) | Verified | recomputed from frames
- Formula: 20×0.99 / (20×0.99 + 9,980×0.01) = 19.8/119.6; ÷10,000 → 0.00198 / 0.00998, ratio unchanged; Bayes with total probability in the denominator | Verified | re-derived
- Landing sweep: 1 in 304 → 33/133 = 25%; 1 in 100 → 99/198 = 50%; 1 in 22 → 450/545 = 82.6% → 83%; 1 in 2 → 4,950/5,000 = 99% | Verified | recomputed from frames
- "99% … recall, how often the sick test positive"; "17% … precision" | Verified (definitions: P(+|sick), P(sick|+)) | —
- "For our test, that's ninety-nine" (accuracy) | Verified (sensitivity = specificity = 0.99, so accuracy = 99% at any prevalence) | recomputed
- Manrai et al. 2014, JAMA Intern Med 174(6):991–3: one Boston-area hospital, doctors and students, 23% right, the most common answer 95% (44%), given a 5% false-positive rate | Verified | PMC4955674
- Waffle 23 / 44 / 33 dots = 14/61, 27/61, 20/61 | Verified | recomputed
- "Their test's own accuracy: 95%" | Verified as interpretation (perfect sensitivity assumed by the authors → accuracy 0.001 + 0.999·0.95 = 95.0%) | recomputed
- Cardiff 2017: 2,470 alerts, 173 right (2,470 − 2,297) = 7.0%, "police count" | Verified | BBC 4 May 2018; Guardian 5 May 2018
- ≈ 170,000 people came | Verified | BBC
- Watch lists held about 1,200 photos → 71 squares at 17 people per square; "≤ 1 in 140" (1,200/170,000 = 1 in 141.7, an upper bound) | Verified | Davies p. 10; recomputed
- "For four days" / "Champions League final week" | Verified (Wired UK: "final week"; I did not re-find Davies's "(4 days)" table cell myself; facts.md quotes it) | secondary
- Evaluators: 78/2,632 = 3.0%, logbook-confirmed | Verified | Davies, Champions League section (quoted)
- Six Nations: 22/48 = 45.8% → 46%; "7 of 22 later proved false" | Verified | Davies, Six Nations section (quoted)
- "a new algorithm and better photos thinned out the false alarms" | Verified with a nuance: Davies credits "the new algorithm and increased operator familiarity"; the better photos come from a separate passage (only high-standard custody images after the final); the 3% includes the blue police list and the 46% excludes it, which is the source's own comparison | Davies
- "That's the blue term in Bayes' denominator" | Verified (direction only: the credited changes lower P(+|not listed)) | reasoning
MECHANICS: runtime 3:40.3 · wpm 148 (speech time) · max silence 2.25 s (0:09.9, planned) · max static 2.90 s · −14.0 LUFS / −1.8 dBTP · leading 0.00 s / trailing 1.58 s ("Thank you" at 3:39.7 is a Whisper hallucination on silence)
FIXES (highest impact first):
1. [2:58.4–3:06.4][Clarity/Visual] The evaluators' bar reads "3%" under the tag "Six Nations 2018 · 48 alerts" for about 8 s, a value paired with the wrong event (borderline cap 6) → keep the tag "final week · 2,632 alerts" until "Their count rose" (3:06.4). Then swap the tag to "Six Nations 2018 · 48 alerts" in the same 1–1.5 s animation that grows the red to 46%. During "Months later … new algorithm and better photos" (2:58.4–3:03.8) show only a small grey "→ 2018" arrow at the bar's right end.
2. [0:24.3–0:28.0][Hook] The episode's real prediction ("what's the chance you're sick?") gets a 0.8 s gap before the Manrai sentence starts. The Cardiff guess, which the viewer has no basis for, gets the 2.2 s hold → add [pause 1.5] after "chance you're sick?" and slide the hollow grey "your guess" marker along the empty "chance you're sick" meter (the same object as at 0:11). Pay for it by cutting the 0:09.9 hold from 2.2 s to 1.2 s.
3. [1:11–1:46][Concision] The 20-of-120 share is computed twice. At 1:11 it is "So of a hundred twenty positives, only twenty are sick. Seventeen percent." At 1:37–1:45 it is "Your chance of being sick is the red share of this crowd. Twenty, out of twenty plus a hundred." → replace the second with "Your chance is this crowd's red share." The 20 / 100 brackets and the fraction already build on screen, so this saves about 4 s.
4. [2:51–3:10][Concision/Clarity] Four Cardiff figures (7%, 3%, 46%, "7 of 22") arrive in 19 s, and "7 of 22 later proved false" is on screen unnarrated for about 2.2 s (3:07.8–3:10.0), under its 2.6 s reading time → merge the lever into two sentences: "Cardiff University's evaluators, counting only logbook-confirmed alerts, got three percent. Months later, a new algorithm and better photos cut the false alarms, Bayes' blue term, and their count rose to forty-six." Either hold the "7 of 22" tag ≥ 3 s, or drop it to facts.md. Fixes 3 and 4 together bring the runtime to ≤ 3:35, the episode's own budget (report.md flags 3:40.3 as over).
5. [3:36.8–3:39.0][Hook] The closing line resolves the disease question. The cold-open image (the 2,470-cell raster with "chance an alert is right ?") was answered at 2:45 and has gone by the end → on "It said you're in this crowd", fade in the coloured 2,470 raster at 35% beside the +, tagged "7%", for the final 1.5 s. The last frame then re-sees the first frame and shows both crowds are the same object.
6. [0:35–0:41 vs 3:23–3:29][Clarity] The same 99% is called "accuracy" (naive answer) and then "recall" (landing) with no bridge. A careful viewer will ask which one the title means → change the landing to "That ninety-nine percent, the test's accuracy, is its recall here: how often the sick test positive." Alternatively, tag the arrow "recall (= accuracy here)" in grey.
7. [2:20.6–2:24][Visual] The "■ watch list" legend appears on "About 170,000" while the crowd has no red square yet (sheet 8, 2:21) → delay the legend to "twelve hundred photos" (≈ 2:24), when the 71 red squares appear.
8. [2:23–2:41][Visual] The scale legend "■ = 17 people" uses a blue swatch, but the red squares are 17 people too → draw the swatch grey (neutral), so blue keeps one meaning.
9. [2:04.2][Audio] "is" is held 0.55 s ("how common each group is,") → regenerate the line without the comma after "is", or swap it for "and these, how often each group tests positive."
REACHES 9 IF ALL FIXED: yes, narrowly. The structure is right: a real cold open with commitment, the naive rule working at 1 in 2 and then failing by a measured 6×, the insight derived from the picture, a real cited payoff with a lever, and a landing that sweeps back to where the rule held. Hook needs fixes 2 and 5. Clarity needs 1, 4 and 6. Concision needs 3 and 4.
KEEP: (1) the single prevalence slider that drains the half-sick block while the meter falls live from the naive 99% marker to 17% (0:57–1:05); (2) the counts → shares → names derivation that keeps "≈ 17%" fixed on screen (1:46–2:10); (3) the Cardiff raster collapsing into the + badge at 0:12, which turns the alerts into "a positive test" in one motion.
```

## Notes behind the scores

- **Hook 8.5.** The first frame is a real, concrete number (0:00–0:07, kf_02). There is a commit prompt at 0:08.6 and a 2.2 s hold. The bridge "Each alert is a positive test result" (0:11.6) lands as the raster collapses into the +. Two things cost the 9:
  - The question the episode actually teaches gets no hold (fix 2).
  - The end resolves the second hook, not the first frame (fix 5).
- **Clarity 8.5.** All numbers check, and the derivation is concrete first and never announced. Deductions:
  - the 8 s mislabelled bar (fix 1);
  - number load in the lever (fix 4);
  - the unbridged accuracy/recall naming of 99% (fix 6).
- **Concision 8.** It runs 3:40 for one idea, over the episode's own 3:35 budget. The red share is explained twice (fix 3), and the lever section is roughly 6 s longer than it needs to be (fix 4). About 5% is removable, but it is all in the back half.
- **Originality 8.5.** Using face-recognition alerts as the base-rate case is fresh next to 3b1b's and Veritasium's medical-test treatments. The precision/recall tie gives the idea a data-science home. The test-and-disease spine is still the canonical one.
- **Visual / Motion / Audio 8.5.** The palette is semantic and stays fixed. Objects persist: the raster, the meter, the strip that becomes the crowd and then the raster. The pace is 148 wpm, with no overlaps per the layout audit and my frames. Remaining issues:
  - fixes 7–9;
  - the 3% bar re-tag leading its value change by 8 s;
  - the short-lived "7 of 22" tag.
