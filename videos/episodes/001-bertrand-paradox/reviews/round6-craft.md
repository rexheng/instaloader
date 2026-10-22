# Round 6 — craft critic (visual design, motion, A/V sync; all dimensions scored)

Evidence: `review/` pack (metrics.json 08:30 is newer than final.mp4 08:28, so it was reused). I read report.md, all 13 contact sheets and 16 full-resolution keyframes (0:14.2, 0:47.5, 1:15.2, 1:23.1, 1:44.6, 2:04.6, 2:20.1, 2:45.2, 3:01.6, 3:13.0, 3:16.6, 3:29.8, 3:33.2, 3:42.3, 3:48.4), plus 24 extra frames I pulled with ffmpeg (0:20.6, 0:45.6–0:47.0, 1:26.4, 1:47.8, 1:53.6–1:56.6, 2:12.0, 2:22.6–2:26.6, 2:44.6–2:47.8, 3:14.2, 3:15.6, 3:17.8, 3:36.4) and the word timings in transcript_words.tsv. I re-ran the invariance board myself (2M chords per recipe).

```
EPISODE: 001 — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly; every recipe is a way of scattering chord midpoints around the one small circle that decides "long", so the same chord question gives 1/3, 1/2 or 1/4, and the same thing makes one college's average class 40 or 147.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 9 · Concision 8.5 · Originality 9
WEIGHTED: 8.9 (887.5/100 = 8.875)   AFTER CEILING: 8.9 (ceiling = 8.5 + 2 = 10.5)
CAPS: none (0 banned phrases, 0 layout-audit issues, no black frames, background-only stretches < 1 s, all empirical claims cited on screen)
FINAL: 8.9   PASS: no (0.1 short)
FACTS:
- Inscribed triangle side = r√3; L > side ⇔ midpoint distance < r/2 (incircle) | Verified | re-derived: 2√(r²−d²) > r√3 ⇔ d < r/2
- Endpoints 1/3 via far arc 120°/360° | Verified | inscribed-angle argument, matches Bertrand §5
- Radius recipe 1/2, midpoint recipe 1/4 = π(r/2)²/πr² | Verified | exact
- Tallies 0.334 / 0.498 / 0.248 from 10,000 chords; "good to about one percentage point" | Verified | 95 % half-widths 0.92/0.98/0.85 pts (facts.md, recomputed)
- "Disagree by 25 percentage points" | Verified | 0.498 − 0.248 = 0.250
- Bertrand 1889 printed all three, "Aucune des trois n'est fausse, aucune n'est exacte" | Verified | Calcul des probabilités ch. I §5 (facts.md); citation on screen 0:13–1:20
- Invariance board midpoint 0.25 ≠ 0.41, endpoints 0.33 ≠ 0.47, radius 0.50 = 0.50 | Verified | my own 2M-line Monte Carlo, small circle r = R/2 at 0.4R: 0.250/0.411, 0.333/0.473, 0.500/0.500
- Jaynes & Tyler, broom straws, standing height, 5-inch circle, 128 crossings matched the radius program | Verified | Jaynes 1973 Found. Phys. 3(4):477–492 §6 ("5-in.-diameter circle … 128 successful tosses confirmed Eq. (13)"); Eq. 13 = uniform-distance law
- Toy classes 10,10,100: per-class mean 40, per-student mean 85 | Verified | 120/3 = 40; (100+100+10000)/120 = 85
- Stony Brook spring 1974, 737 classes, 40 vs 147 | Verified | Feld & Grofman 1977, Res. High. Educ. 6(3):215–222 (title/venue/year confirmed by search; page quotes in facts.md C2; 40.5·(1+65.8²/40.5²) = 147.4)
MECHANICS: runtime 3:48.4 · wpm 157 (speech) / 151 overall · max silence 1.87 s (planned "Pick a number" hold) · max static 2.97 s · −14.0 LUFS / −1.7 dBTP · lead 0.00 s / trail 1.36 s
```

## What I checked, by dimension

**Hook (9).** First frame is the circle and triangle with a chord drawing (0:01). The question is built as math from copies of the chord and side by 0:07, and "Pick a number" gets a 1.9 s hold (0:07.8–0:09.7), so the viewer commits before 0:10. The stakes line previews the payoff's own numbers ("40 or 147", 0:21–0:23). The landing (3:39–3:48) restores the exact first frame (same chord, same question) and re-reads it with the gold circle and the 0–1 line. Tension climbs through build (0:24), fail (1:20, "25 points") and the Jaynes test. The only sag is the second payoff: after the straws resolve the question at 3:12, the survey beat has to win attention back.

**Clarity (9).** Concrete first, and every step is earned. The insight beat (1:25–1:47) is canonical: the midpoint slides, the chord shrinks, it matches the side at r/2, the incircle draws, and every program becomes "a way of scattering midpoints". Assumptions are stated ("can't be aimed, so the answer can't depend on where the circle sits or how big it is"). Two small wrinkles. (a) 3:41.8–3:47.1: "Name the way, and only one is." is followed 2 s later by "Both averages are right…". "Only one" then "both" sounds like a contradiction on first hearing, and the elided "is [right]" makes it worse. (b) The 2:40–2:50 invariance rule is dense: one 9 s sentence carries the test's whole logic. It works on screen, but only just.

**Visual (8.5).** The semantic palette holds for all 3:48: gold = long, blue/green/purple = the three recipes, grey = short/neutral. Red is never used. Typography is consistent (CMU serif), citations sit bottom-left at legible size, and the safe area and spacing are clean (audit: 0 issues in 244 checks; panel labels top at y ≈ 3.37). Deductions:
- 3:13.4–3:17.6, survey entrance. At 3:14.2 the frame is essentially black except a half-written "at random" at the right. At 3:16.6 (kf_34) it holds three disconnected text items ("example / class size" top-centre, "average class 40 or 147" right, "at random" bottom-centre), with no object and no focal point, for about 3 s. It is the weakest composition in the episode.
- 1:13.5–1:19.5 (kf_10). The two-line French quote is squeezed into the band between the tally row and the number line. Its top is about 20 px under "0.498", and it is centred under the green tally, so it reads as the radius program's caption rather than Bertrand's verdict on all three.
- 2:44.4–2:46.4 (kf_27). The big circle's gold-circle flash crosses the small circle and the small gold circle: two full-strength gold circles intersect while the narration says "each judges with its own gold circle". For about 1.5 s it is unclear which gold circle belongs to which.
- 2:17–2:21 (kf_20). The summary frame holds about 14 elements: 3 × 240 dots, 3 equations, a caption, 3 histograms and the 0.334 stack. On "the third we found" the stack is meant to be the focal point, but the bright panels 2–3 compete with it.

**Motion (9).** Objects persist and transform with meaning throughout. The gold arc flies into 120° (0:49) and the two disk outlines fly into π(r/2)²/πr² (1:55.4). The three panels collapse to midpoints, and the five gold bars stack into the 0.334 column while the originals stay dimmed (2:17). Each class dot splits into its students while the bars widen and the line rises from 40 to 85 (3:25–3:29). The small circle is a shrunken copy of the big one (2:39). The rim, the radius and the area light on their spoken words (rim 2:22.7 = word 142.74; radius 2:24.6 = word 143.72). The panel triangle turns upright before moving (0:53). I saw no decorative motion and no static stretch over 3 s. Nitpicks: the survey entrance choreography ("at random" bowing down into a slot while the title waits) is fussy for what it carries, and the 2:50–3:00 run of three rains, six numbers and three relation signs in 10 s sits at the edge of reading time.

**Audio (9).** −14.0 LUFS and −1.7 dBTP, 157 wpm, WER 1.6 % (homophones only: chord/cord, Jaynes/Janes, digit formatting). Pauses are placed on purpose: the 1.9 s commit, the 1.4 s "Where will they crowd?" prediction hold at 2:04, and 0.8–1.0 s holds after each scoreboard row. Deictics checked against frames:
- "this circle" (0:00) and "this triangle" (0:05) land.
- "this far arc" (word 46.76) lands as the arc starts drawing at about 47.0.
- "this gold circle" (1:43) lands; the fill follows on 1:45.
- The one miss is "So **this** circle, with a quarter of the area" (words 114.14–115.04). Nothing on screen marks the gold disk on "this". The outlines only lift off at about 115.4, during "quarter".

**Concision (8.5).** At 3:48 the episode sits near the top of the window and has two payoffs, Jaynes (2:28–3:12) and the survey (3:13–3:37). Each earns its place. The slack beat is the survey re-entry (3:13.4–3:17.6): about 4 s of re-showing the stakes block before anything new appears. Everything else would lose something if cut.

**Originality (9).** Bertrand is a well-worn topic, but this telling is its own. The single "chords → midpoints" collapse unifies the three answers. The two-circle invariance scoreboard, with one line judged twice, turns Jaynes's argument into a test you can watch. The 0.334 stack is read off the measured histogram. And the class-size bridge ("spread evenly over: classes → students") ties the geometry to a real survey statistic. There are no slop phrases and no stock visuals.

## FIXES (highest impact first)

1. **[3:13.4–3:17.6][Visual + Concision] Near-empty survey entrance** (3:14.2 is black except a half-written "at random"; at 3:16.6 three loose text items hold for about 3 s with no object). Start the chart on "Surveys" (word ≈ 193.4 s), not on "ten": draw the baseline and grow the three bars (10, 10, 100) over 3:13.6–3:15.4 in the chart's centred slot. Overlap that with the board's fade-out (start the bars 0.3 s after the board text begins fading) so the frame never empties. Let "at random" and "average class 40 or 147" come back on the right at the same time, unchanged. Then "at random" steps into its slot under the bars on "Take classes" as now. This removes the 3 s void and about 1.5 s of slack, and gives the beat a focal object from its first second. Visual → 9.
2. **[1:13.5–1:19.5][Visual] French quote crammed under the green tally.** Set it on one line, « Aucune des trois n'est fausse, aucune n'est exacte », Text 24 italic, centred at x = 0 (about 9.5 units wide). Move the whole panel group (labels, circles, tallies) up 0.25 and the number line down 0.1, so the quote has ≥ 0.35 clearance above and below and spans all three tallies instead of hanging under 0.498.
3. **[2:44.4–2:46.4][Visual] Two full-strength gold circles intersect** during "each judges with its own gold circle". During the big-circle judgement, draw the big gold circle dashed at 60 % stroke and dim the small gold circle to 30 %. On "own gold circle" (word 165.30) swap them in one 0.5 s cross-fade: big gold out, small gold to 100 %. Only one gold circle is ever at full strength.
4. **[1:54.1–1:56.1][Audio / sync] "So this circle" lands on nothing.** On word 114.14, Indicate the panel-3 gold disk (fill 0.25 → 0.5, 0.6 s, no scale). Start the gold outline's TransformFromCopy into π(r/2)² on "quarter" (115.44) and the purple outline's into πr² on "area" (116.06), so each term is born on its word.
5. **[3:41.8–3:47.1][Clarity] "only one is" / "Both … are right" sounds contradictory.** Change the narration to "Name the way, and the answer is fixed. Both averages are right, once you say who's picked." Keep the on-screen beats (the straws tag on 1/2, then 1/4 and 1/3 dim) and move the dim cue to "fixed".
6. **[2:16.8–2:21.0][Visual] Summary frame has no single focal point on "the third we found".** While the stack builds, dim panels 2 and 3 (circles, dots, equations, histograms) to 35 %. Restore them to 100 % on "Three programs" (word ≈ 140.9), where all three panels are needed again.
7. **[2:50.4–3:00.6][Motion] Three rains and six numbers in 10 s.** Make the post-row holds 1.1 s instead of 0.8 s (+0.6 s in total, paid for by fix 1). Let each relation sign (≠, ≠, =) arrive 0.2 s after its second number, not with it, so the eye reads number, number, verdict.
8. **[3:04.5–3:07][Clarity, nitpick] "5-inch circle"** could be read as a radius; Jaynes wrote "5-in.-diameter". Change the on-screen label to "5-inch-wide circle" (the narration can stay).

REACHES 9 IF ALL FIXED: yes. Fixes 1–3 lift Visual to 9 (weighted 8.95 → 9.0). Fixes 1 and 4–5 lift Concision and Clarity margins, so the episode clears 9.0 with room to spare. No structural change is needed: the hook, fail beat, visual insight and landing are all in place.

KEEP:
- The 1:25–1:47 midpoint insight (slide, shrink, match at r/2, incircle, "each program is a way of scattering midpoints"), then the three panels collapsing to midpoints and their histograms.
- The two-circle invariance scoreboard, with one line judged twice and the rows filling to ≠, ≠, = and then "≈ radius" on the real 128 tosses.
- The class dots splitting into students while the bars widen and the line rises from 40 to 85, and the landing that returns to the exact first frame.
