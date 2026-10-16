# Round 4 review: craft critic (visual design, motion, A/V sync)

**Evidence.** I used the existing `review/` pack, since metrics.json (23:40) is newer than final.mp4 (23:38). I read:
- report.md, narration_diff.txt, transcript.txt, transcript_words.tsv, script.md, narration.txt, facts.md (claims C2–C5, H5b, H7, H8 and the histogram table), CHANGELOG.md (round 3 revisions) and round3-craft.md.
- All 13 contact sheets.
- 15 full-resolution keyframes: kf_02 (0:13.9), kf_07 (0:55.3), kf_11 (1:23.2), kf_16 (1:44.5), kf_19 (2:04.7), kf_22 (2:20.2), kf_25 (2:31.6), kf_29 (2:47.0), kf_31 (2:59.9), kf_33 (3:03.6), kf_35 (3:18.5), kf_36 (3:22.3), kf_37 (3:29.0), kf_38 (3:31.7) and kf_40 (3:51.3).
- 35 extra frames I pulled with ffmpeg: 0:50.0, 0:50.6, 1:02.6, 1:03.4, 1:47.6, 1:48.4, 2:15.6, 2:16.2, 2:28.2, 2:29.0, 2:41.0, 2:42.5, 2:46.0, 2:48.0, 2:59.8, 3:00.6, 3:16.0, 3:16.2, 3:16.4, 3:16.6, 3:16.8, 3:17.0, 3:17.2, 3:17.4, 3:17.8, 3:19.6, 3:20.2, 3:20.8, 3:38.4, 3:39.4, 3:40.2, 3:48.6, 3:49.0, 3:49.4 and 3:50.0. I made full-resolution crops of the citation strip (3:16.2–3:17.4) and of the Stony Brook rows (3:49.0).

**Independent checks.**
- I re-ran the invariance scoreboard with 2 M chords per program, using a small circle of radius R/2 whose centre sits 0.4 R off-centre. I measured that geometry off kf_29 and kf_31: the big circle has R = 270 px, the small one r = 135 px, and the offset is 108 px. Results: endpoints 0.333 / 0.470, radius 0.500 / 0.500, midpoint 0.250 / 0.411. These match the board.
- The demo line at 2:47 (kf_29) sits about 160 px from the big centre, which is more than R/2, so it is short there and correctly drawn grey. It sits about 52 px from the small centre, which is less than r/2 = 68 px, so it is long there and correctly drawn gold.
- The toy chart is to scale (kf_37): baseline y = 667 and the 100-bar top y = 263 give 4.04 px per student. The 40 line sits at y = 505 and the 85 line at y = 324. The dots are 2 × 5 under each 10-bar and 20 × 5 under the 100-bar.
- The landing chord's midpoint lies 38 px from the centre, inside the incircle radius of 58 px (kf_40 sheet scale), so "gold" is correct.

```
EPISODE: 001 — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly; endpoints, radius and midpoint recipes give 1/3, 1/2 and 1/4 because they scatter chord midpoints differently around the one small circle that decides "long", invariance (Jaynes) picks the radius recipe for tossed straws, and the same choice (random class vs random student) turns 40 into 147 in real survey data.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.9 (135 + 225 + 127.5 + 127.5 + 90 + 90 + 90 = 885 / 100 = 8.85)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none.
  - Layout audit: 0 issues in 252 checks. My frames show no clipping or settled overlap. The only touches are transient: a citation cross-fade at 3:16.6 and a flag scale-up at 3:49.0. Both are under 0.6 s and both are listed as fixes; neither is a layout cap.
  - Sync: every deictic I checked lands within ±1 s of its element:
    - "this far arc" (word 0:44.4) → arc lit by 0:45.0
    - "this gold circle" 1:43.7 → filled incircle (kf_16)
    - "this circle, with a quarter of the area" 1:54.7 → purple panel's gold disk
    - "rim" 2:15.7 → blue outer ring and last bar (frame 2:15.6)
    - "the third we found" 2:18.9 → 0.334 column
    - "rim, radius, area" 2:22.6–2:24.9 → blue / green / purple lights
    - "honest program" → demo line judged twice (2:45–2:48)
    - "5-inch circle" 3:03.9 and "128" 3:05.8 → labels at 3:05 and 3:07
    - "two words" 3:17.7 → "at random" writing at 3:17.2–3:17.8
    - "147" 3:34.6 → row at 3:35
    - "straws" tag and 1/2 flag on "Name the way"
    That is 0 misses.
  - Every empirical claim carries an on-screen citation (Bertrand 1889, Jaynes 1973, Feld & Grofman 1977). The simulations are tagged "simulated" and the toy is tagged "example".
  - Mechanics are all inside the bar. No banned phrases.
FINAL: 8.9 (8.85)   PASS: no
FACTS:
  Inscribed-triangle side = r√3; long ⇔ midpoint within r/2 (the incircle) | Verified | re-derived: 2√(r²−d²) > r√3 ⇔ d < r/2
  Endpoints: far arc 120° of 360° = 1/3; sim 0.334 | Verified | re-derived; facts.md / sim.py
  Radius: (r/2)/r = 1/2, sim 0.498; midpoint π(r/2)²/πr² = 1/4, sim 0.248 | Verified | re-derived
  "Each tally is good to about one percentage point"; "disagree by twenty-five percentage points" | Verified | 1.96·√(p(1−p)/10⁴) = 0.85–0.98 pp; 0.498 − 0.248 = 0.250
  Radius program: equal rings get equal shares, inner rings small → crowd at centre; endpoints pile against the rim (last band 0.284) | Verified | d ~ U(0,r); endpoint-midpoint density (2/π)/√(r²−d²); facts.md histogram table
  Five gold endpoint bars stack to 0.334 | Verified | 0.065+0.063+0.065+0.067+0.075 = 0.335 ≈ 0.334 (rounding of the same 3,343 midpoints)
  Bertrand 1889, Calcul des probabilités: « Aucune des trois n'est fausse, aucune n'est exacte » | Verified | Bertrand 1889 ch. I §5 (facts.md; checked in rounds 1–3)
  Jaynes 1973: unaimed tosses ⇒ answer cannot depend on circle position or size | Verified | Found. Phys. 3(4):477–492 §6 (facts.md H5b)
  Scoreboard 0.25≠0.41, 0.33≠0.47, 0.50=0.50 | Verified | my own 2M-chord run: 0.250/0.411, 0.333/0.470, 0.500/0.500
  Jaynes & C. E. Tyler, broom straws, 5-inch circle, 128 successful tosses matched the uniform-distance chord-length law | Verified | Jaynes 1973 §6 quoted in facts.md H7
  "A skilled tosser could produce other answers" (shown simulated, share → 1.00) | Verified | Jaynes 1973 §1 ("tosser sufficiently skilled, various results could be obtained at will")
  Toy 10/10/100: random class 40, random student 85 | Verified | 120/3 = 40; 10,200/120 = 85
  Stony Brook spring 1974, 737 classes: 40 per class, 147 per student; Feld & Grofman 1977, Research in Higher Education 6(3):215–222 | Verified | paper pp. 215–216 as quoted in facts.md C2; 40.5·(1+65.8²/40.5²) = 147.4; JSTOR/ResearchGate listing confirms title and venue
  "Whatever number you picked, some way of drawing chords makes it right" | Verified | constructive (skilled-tosser 1.00 shown; facts.md G9)
MECHANICS: runtime 3:51.3 · wpm 161 in speech (152 overall, 585 words) · max silence 1.92 s (0:07.7, the planned "Pick a number" hold) · max static 3.0 s (0:16.7–0:19.7) · −14.0 LUFS / −1.6 dBTP · leading 0.00 s / trailing 1.81 s · WER 2.0 % (homophones chord/cord, Jaynes/Janes, "a"/"one" only)
FIXES (highest impact first):
1. [3:16.6–3:29.4][Visual] The survey beat opens on a near-empty frame: one italic "at random" at x ≈ 290–605 px plus the citation, held about 2.5 s (kf_35 3:18.5; frames 3:17.2, 3:17.8). The phrase sits neither at frame centre nor where it lived in the stakes beat (x ≈ 1415 px under the question, 0:15–0:21), so the "same two words" callback does not register as the same object. The toy chart is then built in x ≈ 130–780 px, leaving the right 1,100 px empty for 10 s, from 3:19.5 until Stony Brook arrives at 3:29.5 (kf_36, kf_37). This is the weakest composition in the episode. → (a) Write "at random" at exactly its stakes-beat position and size (copy the 0:15 mobject's `get_center()`), so the eye recognises it, then move it to the caption slot as now. (b) Build the toy chart group centred on x = 0, not left-anchored at x ≈ −6.1. On "At Stony Brook" (3:29.4), in the same AnimationGroup that dims the toy to 30 %, `chart.animate.shift(LEFT*3.3)`, so the toy slides aside to make room for the real data block. The chart then fills the frame while it is the subject and yields when it is not.
2. [3:16.5–3:19.5 and 3:22–3:29][Motion] The beat change is still a fade to (nearly) nothing followed by a fresh Write, and the class dots appear from nothing. The episode's own thesis is "what gets spread evenly decides the average", and script.md says these dots are "the same picture as the chord midpoints", but no motion carries that rhyme. → On "Surveys hide the same two words", keep the skilled-tosser floor's gold/grey chord set for 0.6 s and collapse it to its midpoints (reuse the 1:49 collapse code), then `Transform` that dot cloud into the three class dots under the bars on "Pick a class at random" (3:22.1). One continuous object then links the two halves. No narration change is needed. If time is tight, at minimum `ReplacementTransform` the floor's big circle into the "at random" underline rather than fading both.
3. [2:41–2:48][Visual] While the one-line demo runs, the big triangle is still visible at about 30 % inside the big circle (kf_29 2:47.0, frames 2:46.0, 2:48.0). It is irrelevant to the small circle (which has no triangle) and adds three extra lines crossing the demo line. → Move `FadeOut(big_triangle)` into the 2:39–2:41 shrink-and-slide animation of the small-circle copy, so the demo frame contains only the two circles, their gold incircles, and the one judged line.
4. [2:17–2:29][Visual] The stacked "0.334" column is placed left of the endpoints histogram's origin with its left edge at x ≈ 88 px and its baseline stub at x ≈ 80 px (kf_22 2:20.2). That is outside the 96 px safe edge and makes the left histogram visibly off-centre against the other two. → Put the column on the right of the histogram (after the "r" tick, buff 0.35), or shift the whole endpoints histogram group RIGHT by 0.45 units for this beat, so the column's left edge sits at x ≥ −6.2 units.
5. [3:48.6–3:49.4][Visual] When "random student" flags on "who's picked", its scale-up brings it to about 10 px from "147" and from its own line glyph (crop at 3:49.0). This is under the 20 px clearance, at the very last image. → Flag with colour, not scale: `label.animate.set_color(GOLD)` then back (0.8 s), or `Indicate(label, scale_factor=1.04)`. Alternatively, raise the label-to-number buff from about 0.2 to 0.4 units.
6. [3:16.5–3:16.9][Visual] The Feld & Grofman citation fades in on top of the still fully opaque Jaynes citation in the same slot, so for about 0.4 s two citations are overprinted (crop 3:16.6: "…igher Education" ghosting through "Foundations of Physics"). → Use `Succession(FadeOut(jaynes_cite, run_time=0.3), FadeIn(fg_cite, run_time=0.4))`.
7. [1:21–1:25][Visual] "25 points" sits about 20 px directly under the green "0.498" (kf_11), so it reads as a caption of the radius tally instead of the brace's measurement. → Raise the three tallies by 0.25 units for the Fail beat, or set the brace label smaller (MathTex 34) and give it buff 0.08 from the brace tip, so it has ≥ 0.3 units clearance from the tally row.
8. [2:29.6–2:31.0][Audio] "Edwin Jaynes said" is heard as "Edwin Jane said" (transcript 2:30.9), with the s–s merged. → Write "Edwin Jaynes argued" in narration.txt. That removes the merge and is also the more accurate verb.
REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1, 3, 4 and 5 lift Visual to 9. Fixes 1 and 2 (an object-led entrance and a carried rhyme into the survey beat) lift Motion to 9. That gives 135 + 225 + 135 + 135 + 90 + 90 + 90 = 905, which is 9.05. No structural change is needed: the misconception → three programs → midpoint picture → invariance test → real data → bookend spine is right, and all remaining defects are local.
KEEP:
- The midpoint picture and its derivations: chords collapsing to midpoints with live histograms; π(r/2)²/πr², (r/2)/r and the stacked gold bars built from the picture; the rim ring and the last bar lighting blue together on "rim" (2:15.6); gold = long held from 0:30 to 3:51.
- The two-circle invariance scoreboard with the new one-line "judged twice" demo (kf_29) and the "? = ?" straws row: one rain, two verdicts, rows filled with breaths, failed rows dimmed (kf_31).
- The bookend: P(── > ──) = ? built from the chord and side at 0:03–0:07, returning at 3:39 with the marker sweep, the "straws" tag on 1/2, and the opening chord turning gold with its midpoint inside the incircle (kf_40).
```

## Notes by dimension

**Hook 9.** The first frame is the object (circle, triangle, chord), and the viewer is asked to commit at 0:06.8 with a 1.9 s hold. The stakes land by 0:21, and "Every survey and every simulation" now pays off at 3:16. Tension rises twice:
- "Case closed, until you code it a second way" (0:47.5);
- "none of the code has a bug", with the measured 25-point gap on screen (1:23, kf_11).

The ending re-sees the first frame exactly and resolves it ("Name the way, and only one is"). The survey beat still runs at lower pressure than the Jaynes test, but it now earns its place.

**Clarity 9.** Round 3's two blockers are fixed:
- The demo line judged on both circles (2:45–2:48, kf_29) makes the hidden step visible, and the geometry is correct by my measurement.
- One name per recipe ("random radius point" / "radius" / "the radius program"; "midpoint"; "endpoints").

The midpoint pivot is motivated ("One point sets a chord's length: its midpoint", 1:25), every number I recomputed checks out, and the assumptions and the limit (the skilled tosser, tagged simulated) are on screen. I could re-derive 1/3, 1/2 and 1/4 from one watch.

**Visual 8.5.** The palette discipline is excellent and consistent: gold means long, blue/green/purple mean the three recipes, grey is neutral. The background is one flat dark tone, the serif typography is consistent, and type sizes are generous (panel labels about 45 px, tallies about 50 px, citations about 28 px cap). Round 3's issues (orphan toy numbers, "40 · 147" on the axis, the scoreboard void, the r-tick baseline) are fixed; kf_38 and kf_40 are now clean. What keeps it below 9 is composition in the survey beat (fix 1): a 2.5 s near-empty frame, then a left-anchored chart with a 10 s right-hand void. Below that are the nitpicks: the triangle residue (fix 3), the edge-hugging column (fix 4), and transient touches (fixes 5–7).

**Motion 8.5.** Most motion carries meaning:
- the arc and the rim fly into 120°/360° (0:44–0:47);
- the panels shrink with their tallies (0:50.6);
- the gold circle copies into all three panels (1:47.6);
- the midpoint slides and the chord shrinks (1:27–1:35);
- the collapse to midpoints and the histogram growth (1:49, 2:05, 2:13);
- the scoreboard fills;
- the bars widen to their student counts while the mean line rises 40 → 85 (3:26–3:29), which is the best move in the back half;
- the landing marker sweep.

Reading time is respected throughout. The one transition that still does not carry an object is the step from Jaynes into the survey beat (fade to near-empty, then Write, with student dots appearing from nothing; fix 2). The episode's own "dots = what's spread evenly" rhyme is left to the viewer.

**Audio 9.** Loudness, peak and pace are on target. The new planned pauses do their job:
- 1.4 s after "never said which" (2:27.4) with the flagged labels holding;
- 0.9 s after each failed scoreboard row (2:51.5, 2:55.2);
- 1.4 s after "a half on both" (2:58.7);
- 1.2 s after "other answers" (3:15.3).

The cadence now marks beat changes. Every deictic I checked lands on its highlight. The only artefact is the "Jaynes said" s–s merge (fix 8). "Chord"/"cord" is a homophone, not a mispronunciation.

**Concision 9.** At 3:51 it is near the top of the range, but I could not find a sentence whose removal costs nothing. The Jaynes setup is now one sentence, and the three derivations of 1/3 (sim, arc, midpoint pile-up) are the point: the same answer seen three ways. The only slack is the roughly 2.5 s near-empty transition at 3:17, which fix 1 removes.

**Originality 9.** The two-circle invariance scoreboard with a single line judged twice, the stacked-bar 0.334 column, and the class-size bars widening into their students are images I have not seen in standard Bertrand-paradox treatments. A viewer would remember them.
