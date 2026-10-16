# Round 2 review: substance (science and story editor)

Evidence: `review/` pack (metrics.json 14:39 is newer than final.mp4 14:37, so I used it as is). I read report.md, all 13 contact sheets, 13 full-resolution keyframes (kf_02, 07, 11, 19, 22, 24, 27, 31, 34, 36, 39, 40) plus my own extractions at 0:44.8, 0:48.2, 1:55.2, 2:02.5, 2:14.5, 2:29.0, 3:31.0 and 3:39.0. I also read the transcript and its word timings, narration.txt, script.md, facts.md, CHANGELOG.md and round1-substance.md. I recomputed every number myself: an independent 2M-line simulation of the invariance test, the class-size arithmetic, and the CI half-widths. I checked the Bertrand quote, Jaynes 1973 and Feld & Grofman 1977 with web search.

```
EPISODE: 001: "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly; the three classic recipes scatter chord midpoints differently around the one inscribed circle that decides "long" (1/3, 1/2, 1/4), only the radius recipe survives Jaynes's same-rain-on-every-circle test, and the same choice (count classes or count students) splits real survey averages.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.6  (135 + 212.5 + 127.5 + 127.5 + 85 + 85 + 85 = 857.5 / 100)   AFTER CEILING: 8.6  (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none. No banned phrases or patterns. Each empirical claim has its citation on screen: Bertrand 0:13–0:21 and 1:11–1:21, Jaynes 2:27–3:12, Feld & Grofman 3:15–3:32. Mechanics are all inside the bar. No overlaps or clipping in any settled frame.
FINAL: 8.6   PASS: no
```

## FACTS

| Claim | Status | Source / check |
|---|---|---|
| Inscribed equilateral side = r√3; chord L = 2√(r²−d²); L > side ⇔ d < r/2; the r/2 circle is the triangle's incircle | Verified | Re-derived (inradius = R cos 60°) |
| Random endpoints → 120°/360° = 1/3 (0:41–0:47) | Verified | Inscribed angle; (4π/3 − 2π/3)/2π = 1/3 |
| Random radial point → (r/2)/r = 1/2; random midpoint → π(r/2)²/πr² = 1/4 | Verified | Re-derived |
| Tallies 0.334 / 0.498 / 0.248 from 10,000 chords each | Verified | facts.md / sim.py seed 1889 (round 1 re-run) |
| "Each tally is good to about one percentage point" | Verified | 1.96·√(p(1−p)/10⁴) = 0.92 / 0.98 / 0.85 pp (my run) |
| "They disagree by twenty-five percentage points", brace "25 points" | Verified | 0.498 − 0.248 = 0.250 (24.9 unrounded) |
| Radius recipe crowds the centre: equal share per ring, inner rings small | Verified | d ~ U(0,r), so areal density ∝ 1/d |
| Endpoint recipe piles midpoints at the rim; the five gold bins sum to 0.334 | Verified | density (2/π)/√(r²−d²); 0.065+0.063+0.065+0.067+0.075 = 0.335 ≈ 0.334 (rounded bins) |
| Invariance test: midpoints 0.25 ≠ 0.41, endpoints 0.33 ≠ 0.47, radius 0.50 = 0.50, straws 0.50 = 0.50 (small circle radius R/2, centre 0.4R off) | Verified | My own 2M-line run (`inv.py`, seed 7): midpoint 0.2502 / 0.4114; endpoints 0.3335 / 0.4725; radial 0.5000 / 0.5002 |
| Bertrand published it in 1889, *Calcul des probabilités* | Verified | Gauthier-Villars 1889, ch. I §5 |
| « Aucune des trois n'est fausse, aucune n'est exacte » | Verified, verbatim | Bertrand 1889 p. 5; the sentence continues "…la question est mal posée" (web: andremalo.be quotation with page ref) |
| "Edwin Jaynes argued (1973) that a physical process can pick one"; *Foundations of Physics* | Verified | E. T. Jaynes, "The Well-Posed Problem", Found. Phys. 3(4):477–492, 1973 (bayes.wustl.edu/etj/articles/well.pdf) |
| You can't aim at a small circle, so the answer can't depend on its position or size | Verified (fair paraphrase) | Jaynes §1, §6 ("we lack a fortiori the skill consistently to produce different distributions on different circles") |
| Jaynes and Charles Tyler, broom straws, standing position, 5-inch circle, 128 crossed it, "fit that prediction" | Verified, slightly compressed | Jaynes §6: "5-in.-diameter circle … 128 successful tosses confirmed Eq. (13) with an embarrassingly low value of chi-squared". They tested the whole chord-length distribution (10 bins), not just the 1/2 share, so "that prediction" is loose (fix 5) |
| "A skilled tosser could produce other answers" | Verified | Jaynes §1 ("tosser sufficiently skilled, various results could be obtained at will") |
| Classes of 10, 10, 100: per class 40, per student 85 | Verified | 120/3 = 40; (100+100+10,000)/120 = 85 |
| Stony Brook 1974, 737 classes, 40 per class vs 147 per student; Feld & Grofman 1977, *Research in Higher Education* | Verified | Abstract (JSTOR 40195170): "students … experience an average class size of 147 students … despite … an average class size of 40 students per class"; p. 216 has spring 1974 and 737 classes; 40.5·(1 + 65.8²/40.5²) = 147.4 |
| "Whatever number you picked … some way of drawing chords makes it right" | Verified | Choose any midpoint-distance law with P(d < r/2) = p |

There are no Wrong or Fabricated claims. Every round-1 imprecision is fixed ("percentage points", "128 … that crossed it", the spinner is gone).

## MECHANICS
runtime 3:43.3 · wpm 160 in speech (156 overall, 580 words) · max internal silence 1.92 s (the planned "Pick a number" hold, 0:07.7–0:09.6; the second is the 1.6 s prediction hold at 2:01.7–2:03.3) · leading 0.00 s / trailing 1.90 s · max static 3.10 s (3:26.1–3:29.2) · −14.0 LUFS / −1.6 dBTP · 0 black frames · WER 2.3%.

All the WER differences are homophones (chord/cord, poll/pole, Jaynes/Janes) except one. "Forty and a hundred and forty-seven" was transcribed as "40 and 100 and 47" both times (3:29.2–3:31.9 and 3:38.3–3:40.1). The word timings show no break between "hundred" and "and forty-seven", so the parse is ambiguous to a listener too, and this is the closing line (fix 2).

## Transcript and slop audit
- Banned phrases: 0. Banned patterns: none. Each question stands alone and is followed by a hold ("What's the chance…? Pick a number." with 1.9 s; "Where will they crowd?" with 1.6 s). There are no empty superlatives and no recap ending. The voice is specific and deictic: "this far arc" lands as the arc lights (0:43), and "this gold circle" lands as the disk fills (1:40).
- Hook: the circle and chord are on screen at frame 0, the question at 0:03, and the commit prompt at 0:07. That is before 0:12.

## Story
The spine is now complete and the tension rises properly. Naive build (0:21), exact confirmation (0:36), "Case closed, until you code it a second way" (0:47), a measured failure with error bars (1:15–1:24), the one picture (1:24–2:25), a real resolution that is shown rather than asserted (the two-circle scoreboard, 2:39–2:57), an honest limit (3:07–3:12), and a landing on the first frame with a 0–1 sweep (3:33–3:43). The two structural gaps from round 1 are closed.

What still keeps it below 9:
1. **The data beat is attached, not welded (3:12–3:32).** "The same split hides in everyday data." Nothing before this has been called a "split", so the sentence has no referent. The link that makes the beat belong to this episode, *picking a class at random vs picking a student at random*, is never said. "Count each class once / count each student once" is weighting language, and the viewer has to translate it back to "at random" alone. The stakes line at 0:17 promised that "every poll … has to decide what they mean". Saying it in those words here would cash that in exactly and make the landing line hit harder.
2. **The final line's numbers are aurally ambiguous** (see Mechanics).
3. **The Jaynes test skips its premise in one sentence (2:40).** "So rain each program's chords on the big circle, and judge them on the small one too." The reason, that one physical rain lands on every circle at once so it must be fair to all of them, is only implied by the straws' "0.50 = 0.50". A sharp first-time viewer needs one clause more.

## Clarity
Concrete before abstract all the way through, and every result is derived on screen: the 1/3 from the arc, the 1/4 from disk outlines dropping into the tally row, the 1/2 from the radius halves, and the endpoint 1/3 from stacked gold bins. A viewer could re-derive the core after one watch. Deductions:
- (a) The class-size bridge (above).
- (b) 2:14–2:25: the five endpoint gold bars stack into one column **on the 0–0.1r bin** (frame 2:20.6, kf_24). For about 10 s the histogram says a third of the midpoints sit at the centre, which visually contradicts "piles them against the rim" spoken over it.
- (c) "fit that prediction" (3:05) compresses a chord-length-distribution χ² test into "the half".
- (d) The per-student 85 rises as the bars widen (3:22–3:25), but nothing says *why* width matters (width = number of students). The picture is right and the sentence connecting it is missing.

## Visual (§5)
The palette is semantic and held for the whole episode. Gold always means long. Blue, green and purple are the three recipes, and they colour the rim, radius and area on "rim, radius, area" (2:21–2:24). Grey is short or context. Citations sit bottom-left above y = −3.2. The top labels sit at about y = +3.2 (kf_07, kf_27), inside the safe area. No settled frame has an overlap or a clipped glyph. Issues:
- 2:14–2:25: the stacked column sits on the wrong bin (Clarity b).
- 2:47–2:55 (kf_31): the small circle's own gold incircle, which is the rule being applied on that circle, disappears under the bright gold chords. The viewer cannot see what "long" means there.
- 3:15–3:32: the class chart's y-label "class size" has no unit, and there is no x-axis meaning. §5 requires every axis to carry a quantity and unit. At 3:31 the real "147" is placed at the same height as the toy chart's 85 line, on a chart whose top bar is 100, so it reads as if plotted on that scale. It needs its own visual container.
- 1:13–1:45: the 10,000-line panel textures read as brown fur. This is acceptable as dimmed context and is a nitpick.

## Motion
Objects persist and transform with meaning, and this is now close to "the animation is the proof":
- the triangle rotates so a vertex sits on the first point (0:37);
- the panel shrinks and its tally drops onto the shared axis;
- the error bars grow and the brace measures the gap;
- the midpoint slides down the radius until the chord matches the side;
- every chord collapses to its midpoint;
- the disk outlines drop into π(r/2)²/πr²;
- one circle shrinks and slides inside the other (2:37–2:39);
- the bars widen while the mean line rises continuously;
- the opening chord returns, turns gold and shows its midpoint inside the incircle.

Deductions:
- 3:38–3:40: the gold incircle's fill is drawn as a growing pie wedge (frame 3:39.0), a visible Create artefact on the last image of the episode.
- 0:47.5–0:49.5: "0.334" and "1/3" drift separately across an otherwise empty frame (frame 0:48.2), and the panel arrives before its numbers.
- 2:14.5: the gold bars slide diagonally into the wrong bin (see above).

## Audio
Pace is 160 wpm in speech, loudness −14.0 LUFS, true peak −1.6 dBTP. The pauses are intentional and the deictics land on their highlights. Deduction: the "forty and a hundred and forty-seven" ambiguity, twice, the second time in the final sentence.

## Concision
3:43 is long, but I can't find a sentence whose removal loses nothing. The one slack beat is 3:07–3:09, "Jaynes also named the limit:", a 2 s preamble before the line that carries the content. Below 10% is removable.

## Originality
Round 1 called this "a very good version of a known video" (Numberphile with 3b1b, 2021). That is no longer fair. The same-rain-on-two-circles scoreboard makes Jaynes's invariance argument visible, and I have not seen it animated elsewhere. Pairing Bertrand with the class-size paradox and real Stony Brook numbers is a non-obvious data-science reframing. Holding at 8.5 rather than 9 because the bridge between the two is under-sold (Story 1).

## FIXES (highest impact first)
1. **[3:12–3:25][Clarity/Hook/Originality] "The same split" has no referent, and the "at random" link is never said.** Narration: "Surveys hide the same two words. Take classes of ten, ten and a hundred. Pick a class at random, and the average size is forty. Pick a student at random, and it's eighty-five." On screen, relabel the dashed line "random class 40" and the solid line "random student 85" (replacing "per class / per student"), and make the Stony Brook rows use the same labels. The words are about the same length, so runtime does not change.
2. **[3:25–3:32 and 3:37–3:41][Audio/Clarity] "forty and a hundred and forty-seven" parses as three numbers** (ASR heard "40 and 100 and 47" both times). Change to "…the real figures were forty for a random class, and a hundred forty-seven for a random student." For the landing: "…the same way forty and a hundred forty-seven are both right." Drop the inner "and" so Kokoro reads one number. Re-check with the review kit that the transcript prints "147".
3. **[2:14–2:25][Clarity/Visual] The stacked endpoint column sits on the 0–0.1r bin and contradicts "piles them against the rim".** Leave the five gold bars in place, dimmed to 35%. Stack `TransformFromCopy`s of them into a separate column 0.5 units to the *left* of the axis origin, with no x tick, and keep the "0.334" label beside it. The histogram stays a true picture of where the midpoints are.
4. **[2:40–2:46][Clarity] The test's premise is skipped.** Replace "So rain each program's chords on the big circle, and judge them on the small one too" with "One rain lands on both circles at once. So rain each program's chords on the big circle, and judge the same lines on the small one." That is about 2.5 s more. Pay for it with fix 8.
5. **[3:03–3:07][Clarity/correctness of wording] "fit that prediction" overstates what was tested.** Change to "…and the hundred and twenty-eight that crossed it matched the radius program's spread of chord lengths." The facts sheet already holds Jaynes §6 for this, so the citation does not change.
6. **[3:22–3:25][Clarity/Visual] Why widening the bars moves the mean is not said, and the axes have no units.** As the widths grow, write a 3-word label under the baseline: "width = students". Change the y label to "class size (students)". Optional narration change: "Give each student one slice of width, and it's eighty-five."
7. **[3:31–3:41][Visual] The real "147" floats at the toy chart's 85 height on a 0–100 scale.** Put the Stony Brook figures in their own framed two-row block (a thin rule on the left, row labels "random class / random student" from fix 1) at y between +1.5 and +0.3, top-aligned under the "Stony Brook, 1974" header and not aligned to the toy lines.
8. **[3:07–3:09][Concision] "Jaynes also named the limit:" is preamble.** Change to "A skilled tosser, Jaynes noted, could produce other answers." This saves about 1.5 s and offsets fix 4.
9. **[2:47–2:55][Visual] The small circle's incircle (its "long" rule) disappears under the bright chords (kf_31).** Draw the small circle's incircle with stroke 4 at a z-index above the judged chords, and judge chords at 70% opacity.
10. **[3:38–3:40][Motion] The gold incircle fill draws as a pie wedge (frame 3:39.0).** `Create` the outline only, then fade the fill to its 0.15 opacity over 0.6 s (or use `DrawBorderThenFill`).
11. **[0:47.5–0:49.5][Motion] The panel move leaves "0.334" and "1/3" adrift on an empty frame (frame 0:48.2).** Move the tally with its panel (`AnimationGroup`, same run_time, lag ≤ 0.2) so no number crosses empty space unattached for more than 0.5 s.

**REACHES 9 IF ALL FIXED: yes, narrowly.** No structural change is needed. Fixes 1, 2, 4 and 5 bring Clarity and Audio to 9 and make the data beat part of the argument instead of an epilogue, which also lifts Originality to 9. Fixes 3, 6, 7, 9, 10 and 11 bring Visual and Motion to 9. Expected: Hook 9, Clarity 9, Visual 9, Motion 9, Audio 9, Concision 8.5, Originality 9, which gives a weighted 9.0. If only fixes 3 and 7–11 are applied (polish only), it stays at about 8.7.

**KEEP:**
1. The measured failure, 0:47–1:24: three tallies dropping onto one "gold share" axis, ±1-point error bars, the "25 points" brace and "none of the code has a bug".
2. The one picture, 1:24–2:25: the midpoint slides out until the chord matches the side, the incircle appears, and every chord collapses to its midpoint, with 1/4, 1/2 and 1/3 each *derived* from the picture.
3. The two-circle scoreboard (2:39–2:57) and the landing on the first frame with the 0–1 sweep: the payoff is shown rather than asserted, and the ending re-sees the opening.
