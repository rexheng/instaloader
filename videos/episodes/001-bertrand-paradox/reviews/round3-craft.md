# Round 3 review: craft critic (visual design, motion, A/V sync)

**Evidence.** I used the existing `review/` pack, since metrics.json (19:57) is newer than final.mp4 (19:56). I read:
- report.md, metrics.json, all 13 contact sheets, transcript.txt, transcript_words.tsv, narration_diff.txt, script.md, narration.txt, facts.md, CHANGELOG.md and round2-craft.md.
- Full-resolution keyframes kf_01 (0:03.6), kf_06 (0:49.7), kf_08 (1:06.6), kf_11 (1:23.3), kf_14 (1:43.4), kf_19 (2:12.1), kf_21 (2:21.8), kf_24 (2:32.4), kf_28 (2:50.7), kf_31 (2:59.8), kf_34 (3:16.3), kf_35 (3:19.6), kf_37 (3:28.9), kf_38 (3:32.0), kf_39 (3:44.0) and kf_40 (3:49.2).
- 30 extra frames I pulled with ffmpeg: 0:44.6, 0:45.2, 0:50.3, 0:51.0, 0:51.6, 0:52.2, 1:25.8, 1:26.4, 2:03.5, 2:05.0, 2:15.5, 2:27.5, 2:28.0, 2:28.5, 2:29.0, 2:42.0, 2:56.0, 2:57.0, 3:17.0, 3:17.6, 3:18.2, 3:18.8, 3:26.2, 3:27.0, 3:37.8, 3:38.4, 3:39.0, 3:39.6, 3:40.2 and 3:41.0.

I re-ran the invariance test myself with 2 M chords per program, a small circle of radius R/2, centred 0.4 R off-centre (measured off kf_31: offset 110 px against R = 270 px). I got endpoints 0.333 / 0.470, radius 0.499 / 0.500 and midpoint 0.250 / 0.411, which matches the scoreboard. The class toy also checks out: 120/3 = 40 and 10,200/120 = 85.

```
EPISODE: 001 — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly; endpoints, radius and midpoint recipes give 1/3, 1/2 and 1/4 because they scatter chord midpoints differently around the one small circle that decides "long", and the same choice (random class vs random student) turns 40 into 147 in real survey data.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6   AFTER CEILING: 8.6   (135 + 212.5 + 127.5 + 127.5 + 85 + 85 + 90 = 862.5 / 100 = 8.63; lowest 8.5 + 2 = 10.5, not binding)
CAPS: none.
  - Layout audit: 0 overlaps, 0 clearance, 0 safe-area issues across 236 checks. My frames show no clipping. The transient partial glyphs at 0:15 ("at rando…") and 1:21 ("2ɔ") are Write animations mid-stroke, not missing glyphs.
  - Sync: every deictic I checked lands within ±1 s of its element: "this far arc" 0:43, "this gold circle" 1:42, "land here" 1:47, "this circle, with a quarter of the area" 1:53, "the third we found" 2:17, "rim, radius, area" 2:22–2:25, "5-inch circle" 3:05, "128" 3:07, "two words" → "at random" 3:18.2, "forty… a hundred forty-seven" 3:44–3:46 with the pair on screen. 0 misses, so the cap does not apply.
  - Every empirical claim has an on-screen citation (Bertrand 1889, Jaynes 1973, Feld & Grofman 1977). The simulations carry "simulated" tags and the toy carries "example".
  - Runtime 3:49.3, pace 163 wpm, −14.1 LUFS / −1.7 dBTP, max static 3.5 s, max silence 1.92 s. All are inside the bar.
  - No banned phrases. "a warning about two words: at random" is a colon reveal that delivers real content, so I did not count it as the fake-reveal pattern.
FINAL: 8.6   PASS: no
FACTS:
  Inscribed-triangle side = r√3; long ⇔ midpoint within r/2 (the incircle) | Verified | re-derived: 2√(r²−d²) > r√3 ⇔ d < r/2
  Endpoints: far arc 120° of 360° = 1/3; sim 0.334 | Verified | re-derived; facts.md G4 / sim.py
  Radius: (r/2)/r = 1/2, sim 0.498; midpoint: π(r/2)²/πr² = 1/4, sim 0.248 | Verified | re-derived; facts.md
  "Each tally is good to about one percentage point"; "disagree by twenty-five percentage points" | Verified | 1.96·√(p(1−p)/10⁴) = 0.85–0.98 pp; 0.498 − 0.248 = 0.25
  Radius program: equal-width rings get equal shares, inner rings smaller; endpoints pile against the rim | Verified | d ~ U(0,r); d = r cos φ density (2/π)/√(r²−d²)
  Endpoint histogram's five gold bars stack to 0.334 | Verified | facts.md histogram table (3,343 midpoints)
  Bertrand 1889, Calcul des probabilités; « Aucune des trois n'est fausse, aucune n'est exacte » | Verified | Bertrand 1889 ch. I §5 (facts.md H3, checked in rounds 1–2)
  Jaynes 1973, Foundations of Physics; invariance picks the uniform-distance (radius) solution | Verified | Found. Phys. 3(4):477–492, §5
  Scoreboard: midpoints 0.25 ≠ 0.41, endpoints 0.33 ≠ 0.47, radius 0.50 = 0.50, straws 0.50 = 0.50 | Verified | my own 2M-chord run: 0.250/0.411, 0.333/0.470, 0.499/0.500
  Jaynes & C. Tyler tossed broom straws at a 5-inch circle; the 128 that crossed matched the radius program's chord-length spread | Verified | Jaynes 1973 §6 (facts.md H7)
  "A skilled tosser could produce other answers" (shown as simulated 1.00) | Verified | Jaynes 1973 §1, §6
  Toy classes 10, 10, 100: random class 40, random student 85 | Verified | arithmetic
  Stony Brook 1974, 737 classes: 40 per class, 147 per student; Feld & Grofman 1977, Research in Higher Education | Verified | Feld & Grofman 1977, 6(3):215–222 (paper located; numbers per facts.md C2 PDF check)
  "Whatever number you picked … some way of drawing chords makes it right" | Verified | constructive (facts.md G9); Jaynes 1973 §6
MECHANICS: runtime 3:49.3 · wpm 163 in speech (156 overall, 596 transcript words; 138–156 in every 20 s window) · max silence 1.92 s (0:07.7, the planned "Pick a number" hold) · max static 3.5 s (3:35.2–3:38.7, the planned Stony Brook hold) · −14.1 LUFS / −1.7 dBTP · leading 0.00 s / trailing 1.78 s · WER 3.7 % (homophones only: chord/cord, poll/pole, Jaynes/Janes)
FIXES (highest impact first):
1. [3:29.5–3:38.6][Visual/Motion] When the example's word labels leave on "At Stony Brook", the two numbers "85" and "40" stay where they were (x ≈ 1063–1170 px). That is about 300 px right of the line ends they belong to (x = 765 px) and only 60 px from the Stony Brook block's rule. The frame then shows two different "40"s side by side, the toy's and the real one, through the 3.5 s static hold (kf_38 3:32.0, frame 3:37.8). This is the most cluttered and ambiguous moment of the payoff. → In the same AnimationGroup that removes "random class" and "random student", either move each number to its own line end (`num.animate.next_to(line, RIGHT, buff=0.2)`), or FadeOut the numbers together with the words. The dimmed dashed and solid lines already carry the example. Then the only bright numbers in the frame are Stony Brook's 40 and 147.
2. [3:39.4–3:49.3][Visual/Clarity] In the final image, "40 · 147" sits under the 0–1 probability axis at the 0.65–0.92 positions, so it reads as a value plotted on that axis (kf_39, kf_40). It also arrives at 3:39.6, before the axis exists (frames 3:39.6, 3:40.2), and the axis then draws around it, which strengthens the misreading. The axis also keeps an unexplained lone tick at 0.75. → Draw the number line first. On "the same way" (3:44.0), move the pair into its own row clearly off the axis, left-aligned with the "P(" of the question and ≥ 0.6 below the lowest fraction label (the 1/3). Write it as "40 · 147" in INK, not GRAY, because it is the closing referent, not dimmed context. Remove the interior ticks at 0.25/0.5/0.75; the three coloured dots are the only marks that matter.
3. [2:24.5–2:27.0 and 3:15.5–3:17.0][Audio] The episode's thesis line, "At random never said which" (ends 2:26.0), runs into "In nineteen seventy-three" after 0.4 s, the same gap as every ordinary sentence. The Jaynes → surveys boundary is the same: "other answers." → "Surveys…" at 3:16.2 gets 0.4 s while the screen fades to black (frame 3:17.0). The silence list shows almost every inter-sentence gap at 0.4–0.5 s, so the cadence never marks a beat change. → In narration.txt, add [pause 1.0] after "At random never said which." and [pause 0.8] after "could produce other answers." Keep the three flagged recipe labels (2:25) still during the first pause, and start the panel collapse after it. Runtime goes to about 3:51.
4. [2:41.7–2:56.0][Clarity] The invariance test never shows how one program's chords of the big circle get judged on the small circle (they are extended to full lines; facts.md, "program_lines"). The midpoints row's 0.41 appears at 2:47 with no visible reason why a big-circle recipe says anything about the small circle, and it is the one transition I had to rewatch. → At the start of the midpoint rain (≈2:46.5), take ONE purple-rule chord of the big circle and extend it as a thin dashed line through the small circle (0.8 s). Flash its segment inside the small circle gold or grey by the small circle's own rule (0.6 s), then start the rain. No new narration is needed, because "One rain lands on both circles at once" already states the premise.
5. [3:17.0–3:29.5][Visual/Motion] The survey beat starts from a fade to near-black (frame 3:17.0). Then for about 3 s it shows a header, an empty baseline and "at random" floating 900 px away on the right (kf_35 3:19.6, frames 3:17.6–3:18.8). Through 3:29, that italic "at random" (MathTex about 60 px) is the largest and brightest text in the frame while the chart is the subject (kf_37). → Grow the three bars on "Take classes of ten, ten and a hundred" with no empty-baseline hold. Bring "at random" back at font_size 40 and 70 % opacity, placed above the chart title and right-aligned to the chart's right edge (buff 0.3), so it reads as the chart's caption. Indicate it (0.6 s, scale 1.1) on each spoken "at random" (3:22.5, 3:25.6).
6. [2:29.0–2:34.0][Visual] The empty scoreboard (a "gold share" header, one icon and one "–") sits at x ≈ 1540 px, leaving a 450 px void beside the floor box for 5 s (kf_24). → Shift the whole scoreboard group left so its row-label column starts at x ≈ 1180 px (buff 0.6 from the floor box). Show the "straws" row label from the first frame, at 40 % opacity, so the dash has a row.
7. [0:50–3:00][Clarity] Each recipe is named three ways: the panel says "random radial point", the narration says "radius program" and the scoreboard says "radius"; likewise "random endpoints" / "endpoint program" / "endpoints". The scoreboard rows also run in a different order (midpoints, endpoints, radius) from the panels. Colour carries the identity, but the words fight it. → Rename panel 2 to "random radius point". Use the row labels "midpoint / endpoints / radius" exactly as the narration says them. Keep the narration order for the rows, since it builds to the radius reveal.
8. [1:51–2:27][Visual] On all three histograms, the right-hand tick label "r" sits 8–10 px higher than "0" and "r/2" (kf_19). → `r_label.align_to(zero_label, DOWN)`. This is a nitpick.
REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1, 2, 5 and 6 lift Visual to 9; fixes 1 and 5 (no orphan leftovers, an object-led entrance to the survey beat) lift Motion to 9; fix 3 lifts Audio to 9; fix 4 lifts Clarity to 9. That gives 135 + 225 + 135 + 135 + 90 + 85 + 90 = 895, which is 8.95, right at the threshold. A clear 9.0 also needs Concision at 9: the Jaynes section runs 50 s (2:26–3:16), and tightening its setup by about 4 s ("In nineteen seventy-three, Edwin Jaynes argued a physical process picks one: long straws tossed from a standing height can't aim…") would do it. No structural change is needed; the spine of misconception → three programs → midpoint picture → invariance test → real data → bookend is right.
KEEP:
- The midpoint collapse with its three histograms, the formulas built from the picture (outlines → π(r/2)²/πr², radius halves → (r/2)/r, gold bars stacked into the 0.334 column), and the gold = long semantic, which holds from 0:28 to 3:49 (kf_19, kf_21).
- The two-circle invariance scoreboard (2:41–2:59): one rain judged on both circles, = / ≠ filling row by row, failed rows dimmed and radius flagged with straws (kf_28, kf_31).
- The bookend: P(── > ──) = ? built from copies of the chord and side (0:03–0:07), returning at 3:40 with the marker sweeping 0 → 1 to reveal 1/4, 1/3 and 1/2, and the opening chord turning gold with its midpoint inside the incircle (kf_40).
```

## Notes by dimension

**Hook 9.** The first frame is the object: a circle, a triangle and a chord drawing (kf_01, 0:00). The viewer is asked to commit at 0:06.8 ("Pick a number") and gets a 1.9 s hold, so the prediction lands before 0:12. The stakes follow at 0:09.6–0:21. Tension rises twice:
- at "Case closed, until you code it a second way" (0:47.5), deadpan and well placed;
- at "none of the code has a bug" (1:22.7), with the measured gap shown on screen ("25 points", kf_11).

The landing reuses the opening frame exactly, and its closing clause now names numbers that are on screen. My only reservation is that the survey beat arrives after Jaynes has resolved the main tension, so 3:17–3:38 runs at lower pressure. It no longer reads as an appendix, because "at random" returns and the class dots mirror the midpoints.

**Clarity 8.5.** It is concrete before abstract, every answer is derived from its picture, the assumptions are stated (the "skilled tosser" limit is shown and tagged), and every number I recomputed checks out. Two things hold it below 9:
- the invariance step's hidden "extend the chord into a line" move (fix 4);
- the triple naming of each recipe (fix 7).

**Visual 8.5.** The semantic palette is disciplined and consistent: gold means long, blue/green/purple mean the three recipes, grey is neutral. The background is one flat dark tone, the serif typography is consistent, and the hierarchy is clear in the first 2:45. Round 2's clutter and wedge issues are fixed: the invariance frame now clears in sequence (kf_31), and the landing incircle draws as an outline before its fill (kf_40). The remaining defects cluster in the last 35 s, which is where the payoff and the final image live:
- orphan numbers and two competing "40"s (fix 1);
- "40 · 147" sitting on a probability axis (fix 2);
- a near-empty, top-heavy opening to the survey beat (fix 5);
- an empty-scoreboard void (fix 6).

**Motion 8.5.** Most motion encodes a relation:
- the arc and the rim fly into 120°/360° (0:44.6–0:45.4);
- each panel shrinks with its own label and tally (0:50.3–0:52.2);
- the midpoint slides and the chord shrinks to the side length (1:27–1:35);
- chords collapse to their midpoints and histograms grow (1:49, 2:05, 2:13);
- the mean line rises continuously as the bars widen to their student counts (3:26.2–3:29, the best new move this round);
- the marker sweeps the landing axis.

Reading time is respected (the 120°/360° holds about 3.5 s, the Bertrand quote about 5 s). Below 9 because:
- the two entrances in the last 35 s are fades instead of carried objects: to black at 3:17.0, and the landing circle fading in at 3:40.2;
- the label removal at 3:29.5 leaves pieces behind.

**Audio 8.5.** Loudness, peak and pace are all on target, and the deictics land. The cadence is the TTS default: about 0.4–0.5 s between almost every pair of sentences, with only three planned holds (0:07.7, 0:46.1, 2:02.9). The thesis line and two beat boundaries get no breath (fix 3). Pronunciation is fine: "Jaynes" is correctly said as "Janes", and "chord"/"cord" is a homophone.

**Concision 8.5.** Very little is removable, but at 3:49 the episode sits near the top of the range. The Jaynes setup (2:26–2:41) could lose about 4 s without losing an idea.

**Originality 9.** The two-circle invariance scoreboard and the class-dots-as-midpoints rhyme are angles I have not seen in standard Bertrand-paradox treatments, and they would be remembered.
