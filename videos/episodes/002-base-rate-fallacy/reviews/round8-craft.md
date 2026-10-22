# Round 8: craft critic (visual design, motion, A/V sync)

Evidence: `review/metrics.json` (22:47) is newer than `final.mp4` (22:45), so I used the existing `review/` pack. I read report.md, narration_diff.txt, transcript.txt, narration.txt, script.md, all 13 contact sheets, and these full-resolution keyframes: kf_01 (0:07.3), kf_03 (0:18.4), kf_06 (0:39.0), kf_09 (0:48.0), kf_14 (1:07.3), kf_16 (1:32.2), kf_20 (1:52.2), kf_24 (2:14.5), kf_27 (2:24.3), kf_31 (2:41.7), kf_33 (2:55.6), kf_35 (3:03.4), kf_38 (3:20.2) and kf_40 (3:40.3).

I also extracted these with ffmpeg into /tmp/ep2r8:
- Motion strips: 0:11.5–0:15.2 (raster → + collapse), 1:26–1:36.5 (shrink to the 120), 2:17.5–2:21.2 (handover to Cardiff), 2:57.5–3:07.8 (evaluators' bar re-tag), 3:07.0–3:10.0 ("7 of 22" tag hold), 3:09.6–3:13.0 (landing rebuild) and 3:36.5–3:39.9 (ending).
- An audio level check of the tail: −91 dB after 3:38.9. The transcript's "Thank you" at 3:39.7 is a Whisper hallucination on digital silence, not audio.

I re-checked Davies et al.'s "3% at the initial Champions League deployment to 46%" against the Cardiff University PDF (AFRReportDigital.pdf, executive summary).

```
EPISODE: 002 — "When a 99% Accurate Test Says You're Sick"
IDEA: A positive result doesn't give you the test's 99%. It shrinks the sample space to the people who tested positive, and when the condition is rare most of that crowd are false alarms. The sick share of it (17%) is Bayes' theorem, which machine learning calls precision, and it is why only 7% of Cardiff's 2,470 face-recognition alerts were right.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.5 (850/100)   AFTER CEILING: 8.5 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none.
  0 banned phrases. The layout audit (216 checks) and my frames show no overlap or clipping. Max static 2.90 s, max silence 2.25 s (planned), −14.0 LUFS / −1.8 dBTP, 148 wpm, runtime 3:40.3. Every empirical claim is cited on screen.
  Borderline, not applied: from 2:58.5 to about 3:06.5 the plotted bar reads "3%" beside the tag "Six Nations 2018 · 48 alerts". 3% is the final-week figure, so for about 8 s the chart pairs a number with the wrong event. I read it as a transition defect, because the narration frames it as before → after and the bar animates to 46% at 3:06.4–3:08. A stricter reading of "error in plotted data" would apply cap 6, so treat fix 1 as mandatory.
FINAL: 8.5   PASS: no
FACTS:
- 1 in 500 sick, 99% caught, 1% false positives → per 10,000: 20 sick → 19.8 positive, 9,980 healthy → 99.8 positive; 19.8/119.6 = 16.6% ≈ 17% | Verified | recomputed
- "The rule said 99, six times too high" / "99 ÷ 17 ≈ 6×" | Verified (5.8×) | recomputed
- Half sick: 4,950/(4,950+50) = 99%, "the rule holds" | Verified | recomputed
- Slider frames: 1 in 3 → 3,300/3,367 = 98% (1:01); 1 in 296 → 33/133 = 25% (1:03) | Verified | recomputed from frames
- ÷10,000: 0.002×0.99 = 0.00198, 0.998×0.01 = 0.00998, ratio unchanged | Verified | recomputed
- P(s|+) = P(s)P(+|s) / [P(s)P(+|s) + P(h)P(+|h)] | Verified | derivation
- Landing sweep: 1 in 304 → 33/133 = 25%; 1 in 100 → 99/(99+99) = 50%; 1 in 22 → 450/(450+95) = 83%; 1 in 2 → 4,950/(4,950+50) = 99% | Verified | recomputed
- "99% is recall, how often the sick test positive" | Verified (P(+|sick) = 0.99) | definition
- Manrai et al. 2014, JAMA Intern. Med.: 61 respondents at one Boston-area hospital, 23% right, 44% answered 95%; respondents were given a 5% false-positive rate | Verified | facts.md + earlier substance checks; waffle 23/44/33 = 100 dots
- Cardiff 2017: about 170,000 people; 2,470 alerts, 2,297 wrong, 173 right = 7.0% | Verified | BBC News, 4 May 2018 (South Wales Police figures)
- About 1,200 watch-list photos; "≤ 1 in 140" (1,200/170,000 = 1/142) | Verified (labelled as an upper bound) | Davies et al. 2018 p. 10 via facts.md
- Davies et al. 2018: 3% logbook-confirmed at the final → 46% at Six Nations 2018 (48 alerts) | Verified | cardiff.ac.uk AFRReportDigital.pdf, executive summary
- "7 of 22 later proved false" (Six Nations) | Verified per facts.md (Davies, Six Nations section, 32% n=7) | on screen only and never narrated, see fix 3
- Crowd illustration: ■ = 17 people (170,000/10,000), labelled "illustration" | Verified | recomputed
MECHANICS: runtime 3:40.3 · wpm 148 (speech time) · max silence 2.25 s (3:10.8, planned "Back to your test") · max static 2.90 s · −14.0 LUFS / −1.8 dBTP · lead 0.00 s / trail 1.58 s · WER 3.5% (all "a"→"one" normalisations)
FIXES (highest impact first):
1. [2:58.5–3:06.5][Clarity/Visual] The evaluators' bar keeps its 3% fill (final week, 2,632 alerts) while its tag changes to "Six Nations 2018 · 48 alerts" on "Months later". For about 8 s the chart says Six Nations precision = 3%. This also breaks the script's own rule that "the fill is emptied before a new quantity grows". Change: keep the 3% bar with its "final week · 2,632 alerts" tag and dim it to 35%. On "Months later" draw a third bar directly beneath it with the empty outline, "?" and the tag "Six Nations 2018 · 48 alerts", and fill that bar to 46% on "rose" (3:06.4). Before and after then sit side by side. Cheapest alternative: on "Months later", empty the existing fill to 0 and set its label to "?" in the same 0.6 s as the tag swap.
2. [3:34.4–3:39.0][Hook/Originality] "It said you're in this crowd" lands on the node-and-flow diagram, and no crowd is visible: the deictic points at a + disk. Change: on "this crowd" (3:37.6), TransformFromCopy the + disk into the yellow-outlined 24 × 5 strip of 120 people (20 red, 100 blue) from 1:35. Place it under the 17% meter with the flows feeding it, hold 1.0 s, then fade. The last image then matches the cold open's shape (a yellow-outlined block of positives) and the line becomes literal.
3. [3:08.0–3:09.8][Clarity/Motion] "7 of 22 later proved false" is fully visible for about 1.7 s before the landing fade. Six words need ≥ 2.6 s, and it is never narrated, so "22" has no antecedent. Change: cut it, which also helps fix 8. If the honest-limit caveat must stay, narrate "and a third of those later proved false" and hold the tag ≥ 2.6 s before "Back to your test".
4. [0:07.5–0:12.0][Hook] The viewer is asked "How many were right? Pick a number" (a count) while the meter is "chance an alert is right" (a share), and the "your guess" marker slides along a bar with no scale, so the commitment has no number to land on. Change: add "0%" and "100%" end labels under the meter (MathTex font_size 26, grey) for the cold open, and say "What share were right? [0.3] Pick a number."
5. [0:35–0:42][Visual] The waffle legend is one 4-line, 13-word block ("doctors & students / 23% right / 44% said 95% / their test: 5% false alarms"). Together with the diagram labels and meter title the frame carries about 25 prose words, against a limit of ≤ 7 per block and ≤ 12 per frame. Change: delete "doctors & students", which the narration says at 0:31. Put "23% right" (green) beside the green rows and "44% said 95%" beside the grey rows, each at their own y. Move "their test: 5% false alarms" under the waffle as a separate grey block, and move "1 dot = 1%" into the citation line.
6. [2:51–3:10][Visual] The dimmed police raster keeps a full-strength yellow outline, the largest bright shape on screen, and it sits between the two bars, as if the evaluators' bar belonged to it. Change: dim the outline to 35% with its cells on "Cardiff University's evaluators" (2:51.2). Move the evaluators' bar(s) to sit 0.6 units under the police bar, and slide the raster down (or fade it to 15%) so the bars share one column with one focal point.
7. [0:28.0–0:38.6][Audio] The longest stretch without a breath is 10.7 s ("At one Boston-area hospital … ninety-five percent"), and the 95% reveal arrives at the end of a run-on. Change: "At one Boston-area hospital, doctors and students got a problem like this. [pause 0.4] Most answered with their test's own accuracy: [pause 0.4] ninety-five percent."
8. [2:27.0–2:31.1][Concision] Runtime is 3:40.3 against the ≤ 3:35 budget. "Even a small error rate per face would swamp the real matches" announces what the beam then shows at 2:31–2:38. Change: cut the sentence (about 4 s) and keep the 71-square pulse on "twelve hundred photos". Together with fix 3 this brings the runtime to about 3:35.
9. [3:02.5–3:05.5][Clarity] The ghost of Bayes' denominator still reads P(sick)…P(healthy) in the watch-list context, while the term that rises out of it becomes "P(+ | not listed)". Change: before it rises, swap "sick"→"listed" and "healthy"→"not listed" in the ghost with TransformMatchingTex (0.6 s), so the source term and the label match.
10. [2:04.2][Audio] "is" is held 0.55 s in "how common each group is", which reads as an odd stress. Change: re-synthesise the sentence with "how common each group is, [pause 0.3] and these…" so the hold becomes a pause rather than a drawn vowel.
REACHES 9 IF ALL FIXED: yes. Fixes 1–3 lift Clarity, Visual and Motion to 9, fix 2 lifts Hook and Originality, and fixes 7–8 lift Audio and Concision. That projects to about 9.0 (9 everywhere except Originality at 8.5–9). The structure (real cold open → naive rule → measured failure → picture-to-formula → answer on the same raster) is sound, so no structural change is needed.
KEEP:
- The prevalence slider (0:57–1:05): the block drains while the table ticks and the meter falls live from the naive 99% marker to 17%. This is the episode's proof.
- The cold-open raster of 2,470 grey alerts collapses into the + badge (0:12–0:15) and returns coloured as the shrunk sample space (2:38–2:45), answering the opening question on the same object.
- The formula is built from the braces and the ÷10,000 rescale, then "Name them" turns the numbers into Bayes' theorem in place (1:41–2:11), with colour carried term by term.
```

## Notes behind the scores

- **Hook 8.5.** A real, concrete cold open with an explicit commit and a 2.2 s hold (0:09.9–0:12.1), and the question is answered exactly at 2:45 on the same raster. Two deductions: the commit is to an unscaled bar, and a count is asked against a share meter (fix 4). The final frame is the flow diagram, not a re-seen opening image (fix 2).
- **Clarity 8.5.** The derivation is concrete-first and every step is pictured. The payoff, though, stacks 7% → 3% → 46%, plus 2,470 / 2,632 / 48 alerts, inside 25 s (2:41–3:06). It mislabels the 3% for about 8 s and flashes an unexplained "7 of 22" (fixes 1 and 3).
- **Visual 8.5.** The semantic palette holds for the whole episode (red sick/listed, blue healthy/not listed, yellow positive, green correct, grey naive), and the frames are clean, with nothing near the edges. Deductions: the over-full legend block at 0:35–0:42, the competing yellow outline plus ambiguous bar grouping at 2:51–3:10, and the mislabeled bar.
- **Motion 8.5.** Objects persist and transform almost everywhere: the slider, the shrink to 120, braces → terms, the strip → crowd, the beam → raster. Deductions:
  - The tag swap leads the value change by about 8 s.
  - The tag holds for only 1.7 s.
  - At 2:17.5–2:19.0 the full formula and table leave in under 1 s, which is effectively a cut, at a beat boundary.
  - At 3:10–3:13 the landing redraws the diagram from bare arrows instead of keeping a dim copy alive.
- **Audio 8.5.** On target for loudness and pace, every deictic lands (report: 9 of 9), and the pauses are shaped. Deductions: the 10.7 s run-on at 0:28 and the held "is" at 2:04.
- **Concision 8.5.** 479 words in 3:40. One pre-announcing sentence (2:27) and one unnarrated tag (3:08) could go. Otherwise every line carries something.
- **Originality 8.5.** The Cardiff alerts raster, which persists from frame 1 to the answer and is tied to ML precision, is a fresh angle on a heavily covered topic. The ending image is not yet memorable on its own (fix 2).
