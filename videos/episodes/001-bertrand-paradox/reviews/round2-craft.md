# Round 2 review: craft critic (visual design, motion, A/V sync)

**Evidence.** I used the existing `review/` pack, since metrics.json (14:39) is newer than final.mp4 (14:37). I read:
- report.md, all 13 contact sheets, and the transcript, transcript_words.tsv, script.md, narration.txt, facts.md and CHANGELOG.md.
- Full-resolution keyframes kf_07 (0:50.7), kf_11 (1:22.1), kf_19 (1:51.7), kf_22 (2:10.9), kf_27 (2:31.2), kf_30 (2:47.6), kf_39 (3:28.4) and kf_40 (3:43.3).
- 44 extra frames I pulled with ffmpeg: 0:15.2, 0:44.6, 0:45.0, 0:45.4, 0:46.0, 0:46.3, 0:46.6, 0:47.0, 0:47.4, 0:47.8, 0:48.6, 1:25.0, 1:43.0, 1:45.2, 1:50.6, 1:51.4, 1:53.0, 1:54.0, 1:55.0, 2:06.0, 2:09.0, 2:14.0, 2:16.0, 2:26.0, 2:27.5, 2:41.0, 2:43.0, 2:57.0, 3:12.0, 3:13.0, 3:16.0, 3:20.0, 3:29.5, 3:30.3, 3:31.0, 3:31.6, 3:32.2, 3:32.8, 3:33.5, 3:34.5, 3:35.5, 3:36.0, 3:38.6 and 3:39.2.

I also re-ran the invariance test on my own (2 M lines per program, small circle of radius R/2 centred 0.4 R off-centre). I got midpoints 0.250 / 0.411, endpoints 0.334 / 0.471 and radius 0.500 / 0.500, which matches the scoreboard. The class toy checks out too: (10+10+100)/3 = 40 and (100+100+10000)/120 = 85.

```
EPISODE: 001 — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly; the three recipes give 1/3, 1/2 and 1/4 because each scatters chord midpoints differently around the one small circle (the triangle's incircle) that decides "long", and only the recipe that real tossed straws follow gives the same answer on every circle.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.4   AFTER CEILING: 8.4   (lowest 8, ceiling 10; 842.5/100 = 8.43)
CAPS: none.
  - Transient overlaps: the enlarged panel circle passes over the dimmed "0.498" tally at 1:43.0 and over the fading brace at 1:25.0. Both happen mid-transform, last ≤ 1.5 s, and involve dimmed text, so I scored them under Visual and did not apply the overlap cap. This matches round 1.
  - Sync: the narration names something not on screen within ±2 s exactly once: "forty and a hundred and forty-seven" at 3:38.3–3:40.1, while 40/147 left the screen at 3:32.5. The cap needs ≥ 2 such cases, so it does not apply.
  - Every empirical claim has an on-screen citation.
FINAL: 8.4   PASS: no
FACTS:
  Inscribed triangle side = r√3; long ⇔ midpoint within r/2 (the incircle) | Verified | re-derived: 2√(r²−d²) > r√3 ⇔ d < r/2
  Endpoints 120°/360° = 1/3, sim 0.334 | Verified | facts.md G4, sim.py 0.3343
  Radial (r/2)/r = 1/2, sim 0.498; midpoint π(r/2)²/πr² = 1/4, sim 0.248 | Verified | re-derived; sim.py 0.4976 / 0.2482
  "Each tally is good to about one percentage point"; "disagree by twenty-five percentage points" | Verified | 95% half-widths 0.85–0.98 pp; 0.4976−0.2482 = 24.9 pp
  Endpoint histogram's five gold bars sum to 0.334 | Verified | 0.065+0.063+0.065+0.067+0.075 = 0.335 (rounded bars), 3,343 midpoints
  Bertrand 1889, Calcul des probabilités; « Aucune des trois n'est fausse, aucune n'est exacte » | Verified | Bertrand 1889 ch. I §5 (facts.md H3; round-1 substance check)
  Jaynes 1973, Foundations of Physics; invariance picks the uniform-distance solution | Verified | Found. Phys. 3(4):477–492, §5
  Invariance scoreboard: midpoints 0.25 ≠ 0.41, endpoints 0.33 ≠ 0.47, radius 0.50 = 0.50, straws 0.50 = 0.50 | Verified | my own 2M-line run: 0.250/0.411, 0.334/0.471, 0.500/0.500
  Jaynes & Charles Tyler, broom straws, 5-inch circle, 128 that crossed it fit | Verified | Jaynes 1973 §6 ("128 successful tosses", "5-in.-diameter circle")
  "A skilled tosser could produce other answers" (shown as simulated, 1.00) | Verified | Jaynes 1973 §1, §6
  Toy classes 10, 10, 100: per class 40, per student 85 | Verified | arithmetic
  Stony Brook 1974, 737 classes, 40 per class vs 147 per student; Feld & Grofman 1977, Research in Higher Education | Verified | Feld & Grofman 1977, 6(3):215–222, pp. 215–216 (facts.md C2)
  "Whatever number you picked … some way of drawing chords makes it right" | Verified | constructive (facts.md G9); Jaynes §6
MECHANICS: runtime 3:43.3 · wpm 160 in speech (156 overall, 580 words) · max silence 1.92 s (0:07.7, the planned "Pick a number" hold) · max static 3.1 s (3:26.1–3:29.2) · −14.0 LUFS / −1.6 dBTP · leading 0.00 s / trailing 1.90 s · WER 2.3 %
FIXES (highest impact first):
1. [3:15.0–3:32.5][Clarity/Visual] The made-up classes 10/10/100 are drawn for 16 s directly under the header "Stony Brook, 1974 · 737 classes" (contact sheet 3:15, 3:19; kf_39 3:28.4). The toy's per-class mean also equals Stony Brook's 40 by construction, so the frame reads as real data. Then the real 147 appears at 3:31.0 and the frame is gone by 3:32.5, so the cited payoff is readable for about 1.5 s. The chart also never labels what the bar *width* encodes, and that width is the whole mechanism. → Open the beat (3:15) with the toy chart only, plus a grey "example" tag (Text ≥ 18) left-aligned above "class size". FadeIn "Stony Brook, 1974 · 737 classes" only on "At Stony Brook" (3:25.5). On "forty" (3:29.2), write "per class 40" in the right column, and on "forty-seven" (3:31.1) write "per student 147" above it, with row labels that match the left-hand lines. When the bars start widening (3:22.6), add "width = students" under the baseline (Text 22, grey). Hold the finished chart without motion until ≥ 3:34.5 (≥ 3 s after "forty-seven") by inserting about 2 s of silence before "So whatever number…". Runtime goes to about 3:45, still within 2:30–4:00.
2. [3:37.6–3:41.5 and 3:29.2–3:32.0][Audio/Hook] The landing's last clause, "the same way forty and a hundred and forty-seven are both right", names numbers that left the screen 5 s earlier (gone at 3:32.5). The TTS phrasing is also ambiguous: Whisper heard "40 and 100 and 47" both times (3:30.2 and 3:39.0, transcript_words.tsv 209.23–211.95 and 218.31–220.11), which turns "both" into nonsense for some listeners. → In narration.txt, change both occurrences to "forty and one forty-seven". In the landing, on "the same way" (3:37.8), FadeIn a small grey "40 · 147" pair under the number line, right of the 1/2 label (buff ≥ 0.3), and hold it to the end. Re-run review_kit and confirm the ASR hears "147".
3. [2:41.0–2:57.5][Visual] The invariance test is the episode's best new image, but its frame is cluttered. The big circle's dimmed triangle and its own gold incircle stay up while the small circle's rim and its incircle cut straight through them (kf_30 2:47.6: two gold circles overlap, plus bright/dim chords). At 2:56–2:57 a fresh straw rain floods the box while all four scoreboard rows and every program chord are still up, which makes it the densest frame in the video (frame 2:57.0). → On "and judge them" (2:43.5), FadeOut the big triangle completely and dim the big incircle to 20 %. On "like the straws" (2:55.5), first FadeOut the program chords, the small circle and the midpoints/endpoints rows (0.6 s), and only then start the straw re-rain.
4. [0:46.4–0:47.4][Motion] "120°/360° = 1/3" completes at 0:46.4 and starts dissolving at 0:47.0 (frames 0:46.3, 0:47.0, 0:47.4), so it holds about 0.6 s against the §5 minimum of 2 s + 0.4 s × 3 terms ≈ 3.2 s. This is the only exact derivation in the naive build. → Add a 1.0 s pause after "a third of the rim" in narration.txt. Hold the equation and the gold arc unchanged through "Case closed", and start the panel shrink on "a second way" (≈ 0:49.5 after the retime).
5. [3:38.6–3:39.4][Visual/Motion] The landing's gold incircle is drawn with Create on a filled circle, so the fill renders as a wedge or half-moon with a straight edge (frames 3:38.6 and 3:39.2). It happens in the final image. → Create the stroke only (0.8 s, smooth), then FadeIn the fill to its 0.15 opacity over 0.4 s. Or build it as GrowFromCenter of the filled disk.
6. [1:50.6–1:54.0 and 2:08.8–2:10.3][Visual/Motion] The tally shows a dangling "0.248 ≈" with no right-hand side for about 3.4 s (frames 1:50.6, 1:51.7, 1:53.0), and "0.498 ≈" for about 1.5 s (2:09). An unfinished relation reads as a missing glyph. → Write the "≈" in the same AnimationGroup as the first term arriving (the π(r/2)² numerator and the r/2 numerator), not before it.
7. [2:41.0][Clarity] The midpoints row fades in already reading "0.27 / 0.41" before a single midpoint chord has rained (frame 2:41.0), so the 0.41 exists before its evidence. → Start both cells at "–", and start each DecimalNumber only when its rain begins, as the straws row already does (kf_27).
8. [3:12.7–3:15.5][Clarity/Originality] "The same split hides in everyday data": "split" refers to nothing named, and the class beat never shows *what is spread evenly*, which is the episode's own idea. It is linked to the chords by narration only. → Say "Same question, everyday data: what gets counted evenly?". When the bars widen (3:22.6), drop 120 small grey dots (r = 0.05) into the bars, one per student, using the same dot style as the 1:47 midpoints. That makes "count each student once" the same picture as "spread midpoints evenly", and lets the 85 line visibly come from the dots.
9. [1:42.4–1:44.4][Visual] As the enlarged panel shrinks back, its gold disk passes over the re-appearing "0.498" (frame 1:43.0), and at 1:25.0 over the fading "25 points" brace. → Delay the green tally's FadeIn until the circle has landed (≥ 1:44.4), and finish the brace FadeOut before the enlarge starts.
10. [0:45.0–0:45.6][Motion] In the arc → "120°" and rim → "360°" build, both shrink to icons in place over the chord (a 70 px blue ring sits on the chord at 0:45.0) and fly to the fraction in about 0.4 s. That is at the §5 tracking floor. → Lift a copy of the gold arc off the rim and TransformFromCopy it straight into "120°" over 0.9 s, then do the same with the rim into "360°". Skip the icon shrink.
REACHES 9 IF ALL FIXED: yes, but narrowly. Fixes 1–7 are craft-level and would lift Visual and Motion to 9, Audio and Hook to 9, and Clarity to 9. With Concision and Originality held at 8.5 that totals about 8.9. Reaching 9.0 also needs fix 8: the class-size beat has to *show* "what is spread evenly" with the same dot language as the chord midpoints, not just state it. That lifts Originality to 9 and makes the closing line land on a picture. No restructure of the chord spine is needed.
KEEP:
- The two-circle invariance scoreboard (2:37–2:56): one rain judged on a big and a small off-centre circle, = / ≠ filling row by row, radius matching straws. It turns Jaynes from an appeal to authority into a visible test.
- The midpoint collapse with its three histograms, and the endpoint's five gold bars stacking into the 0.334 column (1:47–2:17). Gold = long holds as one meaning from 0:28 to 3:43.
- The bookend: P(── > ──) = ? built from copies of the chord and side (0:03–0:07), returning at 3:33 with the marker sweeping 0→1 and revealing 1/4, 1/3 and 1/2, and the opening chord turning gold with its midpoint inside the incircle (kf_40).
```

## Notes by dimension

**Hook 8.5.** The first frame is the object (0:00). The viewer is asked to commit at 0:06.8 ("Pick a number") with a 1.9 s hold. The stakes ("Every poll and every simulation…", 0:16.9) are now paid off by the class-size beat. Tension rises at "Case closed, until you code it a second way" (0:46.7) and again at the Jaynes test (2:40). The landing returns to the opening frame exactly. Deductions:
- The closing line points at numbers that are no longer on screen, and they are misheard (fix 2).
- The class beat arrives after Jaynes has already resolved, so it plays a little like an appendix (fix 8).

**Clarity 8.5.** It is concrete before abstract. Each answer is derived from the picture: the 1/3 from the arc and the stacked bars, the 1/2 from the radius halves, the 1/4 from the disk outlines. Round 1's central gap, the invariance step, is now demonstrated, and I verified all the numbers independently. Deductions:
- The toy and real data are conflated under one header (3:15–3:31).
- The cited 147 is readable for about 1.5 s.
- The bar width is unlabelled.
- "The same split" is vague.

**Visual 8.** The palette is semantic and held for the whole runtime. Type is comfortably above the §5 minimums in every frame I measured: citations about 30 px cap, tallies about 45 px. Citations sit bottom-left above y = −3.2, and dimming replaces deletion. Deductions:
- The invariance frame is cluttered (kf_30; frame 2:57.0).
- The dangling "≈" (1:50.6–1:54.0).
- The right half of the class chart is empty for 16 s, apart from a header that misattributes the toy data.
- The wedge-shaped incircle fill in the landing (3:38.6).
- The transient circle-over-tally at 1:43.0.

**Motion 8.5.** Most motion encodes a relation:
- The triangle rotates onto the endpoint (0:37).
- The 1/3 travels from the arc equation into the tally (0:47.8).
- The midpoint slides out and the chord greys (1:27–1:31).
- Chords collapse to midpoints (1:47, 2:03, 2:13).
- Gold bars stack into 0.334 (2:15).
- A copy of the circle shrinks and slides to make the test circle (2:37–2:39).
- The straws are pulled inward (3:09–3:11).
- The bars widen while the mean line rises continuously from 40 to 85 (3:22–3:25).

Deductions: two reading-time violations (the equation at 0:46, the 147 at 3:31), the icon fly-in at 0:45, and the Create wedge at 3:38.

**Audio 8.5.** Pace (160 wpm), loudness (−14.0 / −1.6 dBTP) and silences are on target. Deictics land: "this far arc" (0:42) as the arc draws, "this gold circle" (1:40) on the filled incircle, "here" (1:46), and "Where will they crowd?" with a 1.4 s hold before the collapse (2:01–2:03). Deductions: "forty and a hundred and forty-seven", which the ASR hears as three numbers twice, and the closing clause referring to off-screen numbers. The ASR's chord→"cord", poll→"pole" and Jaynes→"Janes" are homophones, not mispronunciations.

**Concision 8.5.** 580 words and no sentence is pure filler. The Jaynes section (2:25–3:12, 47 s) is the longest beat and could lose about 3 s. For example, "So rain each program's chords on the big circle, and judge them on the small one too" could become "Rain each program on the big circle; judge it on the small one."

**Originality 8.5.** Bertrand's paradox is well covered (Numberphile with 3Blue1Brown, 2021). This episode adds three things that aren't standard: a measured failure with error bars, the two-circle invariance scoreboard, and a real sampling consequence (Feld & Grofman). The class-size bridge is still told rather than shown, which is why this is 8.5 and not 9.
