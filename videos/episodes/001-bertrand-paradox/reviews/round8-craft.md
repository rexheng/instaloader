# Round 8 — craft critic (visual design, motion, A/V sync; all dimensions scored)

**Evidence used**
- The existing `review/` pack. metrics.json (18:48) is newer than final.mp4 (18:46), so I reused it and did not regenerate it.
- I read report.md, narration_diff.txt, transcript.txt and transcript_words.tsv, plus all 12 contact sheets.
- I read 17 full-resolution keyframes: 0:04.2, 0:54.1, 1:09.9, 1:22.3, 1:54.8, 2:12.0, 2:22.7, 2:26.7, 2:35.2, 2:39.7, 2:43.8, 2:52.2, 3:01.6, 3:11.2, 3:16.8 and 3:33.4, plus a frame I extracted at 2:21.0.
- I extracted 5 fps strips with ffmpeg, saved in the session scratchpad:
  - 0:47.6–0:50.6, the arc equation hold and hand-off;
  - 1:17.6–1:20.0, the fail-to-insight breath;
  - 1:52.0–1:55.6, the prediction hold;
  - 2:10.2–2:12.6, the equation fold;
  - 2:19.0–2:21.4, the panels-to-floor dissolve;
  - 2:27.6–2:31.2, the gold-rule hand-off;
  - 2:49.8–2:52.8, the board exit;
  - 3:01.6–3:04.0, the survey entrance;
  - 3:11.6–3:14.0, the class-to-student split;
  - 3:19.0–3:21.4, the landing entrance.
- I measured the text spacing at 3:01.6 from the pixels.
- I read script.md, narration.txt and facts.md (H5, H7), and round 7's craft and substance reviews.
- I re-ran the invariance board with my own Monte Carlo, written independently of sim.py: 2M lines per program, small circle R/2 at 0.4R. Results: endpoints 0.333 / 0.470, radius 0.500 / 0.500, midpoint 0.250 / 0.411.

**What changed since round 7, checked against round 7's craft fixes**
1. Straw rain (2:23–2:29). Fixed. Only the newest strokes are bright, and the texture sits at about 25 %. In the 2:27.6–2:31.2 strip, the shrinking copy is the brightest moving object.
2. Gold-rule hand-off (2:28–2:31). Fixed. The big triangle and the big gold circle fade before the copy moves, and the strip shows exactly one gold circle in every frame. No dark halo or crescent is visible at 0.2 s sampling.
3. Tyler right column (3:01.6). Fixed. It has three items: "straws ≈ radius", the histogram title and the histogram. "128 straws crossed it" now sits on the floor under the "5 in" mark. I measured 23 px between it and the citation (≥ 20 px).
4. Demo-line verdicts (2:35–2:40). Fixed. "short" (grey) and "long" (gold) are written beside their pieces, and the dashed big rule holds about 1.6 s before the cross-fade.
5. Prediction hold (1:53.4–1:55.6). Fixed. Panels 1 and 3 drop to about 40 % and nothing else moves.
6. Board exit (2:51.4–2:52.8). Fixed. The steps run in sequence, and no two gold circles are visible at once.
7. "the code has no bug" (1:18.1). Fixed. It is followed by a 1.2 s silence while the number line fades.
8. Board rows. Fixed. Each row now has its panel's glyph: blue rim, green radius, purple disk.
9. Honest limit. Fixed. At 3:29–3:33 the landing reads "1/2 straws / unaimed".
10. Board entrance (2:19–2:21). Fixed. Board text is about 50 % before the last panel clears.

```
EPISODE: 001 — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly. Every recipe is a way of scattering chord midpoints around the one small circle that decides "long" (1/3, 1/2, 1/4). An unaimed physical toss (Jaynes) picks 1/2, and the same choice makes one college's average class 40 or 147.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 9.0 (900/100)   AFTER CEILING: 9.0 (lowest 9 + 2 = 11, not binding)
CAPS: none
- 0 banned phrases or patterns (report §4 scan; my own read of narration.txt finds no rhetorical chain or fake reveal; "Where will they crowd?" is a single genuine question followed by a hold).
- 0 layout-audit issues in 247 checks.
- 0 black frames.
- Max static 3.17 s (the planned "Pick a number" hold).
- Max silence 2.08 s.
- Runtime and pace are inside the window.
- −14.0 LUFS / −1.9 dBTP.
- Every empirical claim has an on-screen citation: Bertrand 0:12–1:14, Jaynes 2:20–3:02, Feld & Grofman 3:03–3:20.
FINAL: 9.0   PASS: yes (no margin: a half-point drop on any 15- or 25-weight dimension fails it)
FACTS:
- Inscribed triangle side = r√3; a chord is longer iff its midpoint is within r/2 (the incircle) | Verified | 2√(r²−d²) > r√3 ⇔ d < r/2
- Endpoints 1/3 = 120°/360° (far arc, 0:45–0:49) | Verified | inscribed-angle argument
- Radius program 1/2 = (r/2)/r; midpoint program 1/4 = π(r/2)²/πr² | Verified | exact
- Tallies 0.334 / 0.498 / 0.248 of 10,000, "good to about one percentage point", "25 points" | Verified | 95 % half-widths 0.85–0.98 pt; 0.498 − 0.248 = 0.250
- Endpoints program piles midpoints at the rim; gold bands stack to 0.334 (2:07–2:12) | Verified | exact last band 0.287; stacked column measures one third of the bar scale at 2:12.0
- Bertrand 1889, Calcul des probabilités; « Aucune des trois n'est fausse, aucune n'est exacte » (1:09–1:14) | Verified | facts.md H3; round-7 web check (arXiv 1504.01361)
- Invariance board: midpoint 0.25 ≠ 0.41, endpoints 0.33 ≠ 0.47, radius 0.50 = 0.50 | Verified | my own 2M-line MC: 0.250/0.411, 0.333/0.470, 0.500/0.500
- Jaynes 1973, Foundations of Physics 3(4):477–492: unaimed straws from a standing position; with Dr. Charles E. Tyler, 5-in.-diameter circle, 128 successful tosses confirmed the uniform-distance law | Verified | facts.md H5/H7 quoting §6 of the author's PDF; on-screen "5 in" and "128 straws crossed it" match; the histogram is labelled "predicted", not data
- Toy classes 10/10/100: random class 40, random student 85 | Verified | 120/3 = 40; 10,200/120 = 85; the line heights at 3:11.2 and 3:13.6 sit at 0.40 and 0.85 of the 100 bar
- Stony Brook spring 1974, 737 classes: 40 per class vs 147 experienced | Verified | Feld & Grofman 1977, Res. High. Educ. 6(3):215–222 (facts.md C2; 40.5·(1+65.8²/40.5²) = 147.4)
- Landing: the opening chord is long and its midpoint lies inside the gold circle (3:33.4) | Verified | midpoint about 0.33 r from the centre
- "Whatever number you picked, some way of drawing chords makes it right" | Verified | mixtures of chord laws reach any share in [0, 1]
MECHANICS: runtime 3:33.5 · wpm 156 (speech) / 145 overall, 500 words · max silence 2.08 s (planned, 0:08.3–0:10.3) · max static 3.17 s (same hold) · −14.0 LUFS / −1.9 dBTP · lead 0.00 s / trail 1.54 s · WER 2.4 % (homophones, number formatting and Whisper chunk-boundary duplicates only: the doubled "a" at 2:07.1 and "Each" at 2:34.6 have overlapping 0.02 s timestamps in transcript_words.tsv, so they are not in the audio)
FIXES (highest impact first; all are nitpicks, none changes a score by itself):
1. [3:01.0–3:02.2][Visual] The verdict row reads "straws" and then, about 140 px later, "≈ radius". That gap is the board's old column spacing, so the result breaks into two items. → When "?" swaps to "≈ radius", also shift "≈ radius" left so it starts 0.3 units after "straws", in the same 0.4 s swap. Lift the whole right column (row, title, histogram) 0.6 units, so its centre sits level with the circle's centre and the top third of the frame is not empty.
2. [3:15.4–3:17.6][Visual] The Stony Brook block draws its full-height rule (y ≈ 130–485 px) with only the header beside it, an empty frame for about 2 s. → Grow the rule with the rows: draw it to the header's height first, then extend it with each row as "random class 40" and "random student 147" arrive.
3. [2:20.6–2:21.6][Motion] The floor's rounded box draws stroke by stroke from its top-right corner (a lone arc at x≈1075, y≈135 at 2:21.0) while nothing else moves. It reads as decoration. → FadeIn the box (0.4 s) together with the "simulated" tag, or grow it outward from the big circle's bounding box, so it reads as "this is the floor the circle sits on".
4. [3:12.2–3:12.6][Motion] As the 100-student class splits, its dots start coincident and read as one solid white pill for about 0.4 s before resolving. → Start each class's student dots at the class dot with a 0.05 s lag per row (LaggedStart, lag_ratio 0.1), so the split reads as dots fanning out, not a blob stretching.
5. [3:20.4–3:21.2][Motion] The landing's circle, triangle and question come back by cross-fade, and for about 0.2 s the frame holds only the two Stony Brook rows. → Begin the circle's FadeIn 0.2 s earlier, overlapping the rows' step-down, so the first frame of the bookend is never only two dim rows.
6. [2:43–2:51][Visual] In each rain, the full-strength pieces inside the small circle pile into a dense gold and grey star (2:51.0) that competes with the row being filled. → Cap each rain's full-strength pieces at the newest 12 and step older ones to 40 %, as done for the straws, so the board number is the focal point when it settles.
REACHES 9 IF ALL FIXED: yes. It is already at 9.0 with no caps. These fixes add margin on Visual and Motion, which is the safest place to buy it: Visual 9.5 and Motion 9.5 would lift the weighted score to 9.15. No structural change is needed.
KEEP:
- The insight sequence 1:19–2:19: midpoint slide → incircle → "each program is a way of scattering midpoints" → chords collapsing to midpoints, with each histogram and each equation built from the area or length it measures, then rim, radius and area lit in their colours.
- The invariance board 2:31–2:52 as it now plays: one demo line judged "short" by the big circle and "long" by the small one, then three rains filling rows that carry each panel's glyph.
- The bookend: 0:00 and 3:21–3:33 show the same circle, chord and question. The chord turns gold with its midpoint inside the gold circle, and "1/2 straws unaimed" and "147 random student" resolve "Pick a number" and the 0:17 promise.
```

## Notes by dimension

**Hook (9).**
- The first frame is the object: circle, triangle and a chord being drawn (0:01).
- The question is built as math from copies of the chord and the flashed side by 0:07.
- "Pick a number" is followed by a 2.1 s hold (0:08.3–0:10.3), so the viewer commits before 0:11.
- The stakes line (0:17–0:23) puts the payoff's own numbers on screen ("40 or 147").
- The 3:21 landing restores the first frame exactly and resolves it on a 0–1 line.

I found nothing above nitpick level.

**Clarity (9).** The order is concrete before abstract: one simulation, one geometric proof, two more programs that fail to agree by a measured amount (with error bars and "25 points"), then the single picture that explains all three.
- Round 7's one rewatch point was the invariance test. It now reads off the picture: the dashed big rule against the grey chord marked "short", then the small gold rule against the gold piece marked "long" (2:35.2 and 2:39.7).
- The 1/2's limit is on screen as "unaimed" (3:29).
- Every number I recomputed checks.
- A first-time viewer still has to carry six board numbers in 12 s (2:40–2:52). The relation signs (≠, ≠, =) do the work, so I count that as a nitpick.

**Visual design (9).**
- The palette is fixed and semantic in every frame I read: gold means "long", and blue, green and purple mean the three programs on labels, tallies, glyphs, histogram lights and landing fractions. Ink and grey are context.
- No frame uses more than 4 hues. No colour pair relies on red against green.
- Dimmed context sits at 25–40 % instead of being deleted (1:22, 1:55, 2:09, 2:52, 3:16).
- Type clears the §5 floors. The citations sit bottom-left above the caption zone (bottom at 960 px, y ≈ −3.11).
- The densest frame (2:12.0: three panels of about 300 dots, three equations, three histograms) reaches exactly 12 prose words. It holds together because each column is one program in one colour.

All the remaining issues are compositional nitpicks: fixes 1, 2 and 6.

**Motion (9).** Objects persist and transform with meaning throughout:
- the arc copies into 120° and the rim into 360° (0:45–0:49);
- the big circle shrinks into panel 1 with its tally and exact 1/3 (0:50–0:53);
- the gold circle copies out of panel 2 into all three panels (1:36–1:38);
- the chords collapse to their midpoints;
- the disks' outlines fly into π(r/2)² and πr²;
- the gold bars stack into 0.334 (2:07–2:09);
- the equations fold cleanly, with no glyph soup in the 2:10–2:12 strip;
- the circle copy shrinks and slides off-centre (2:29–2:31);
- the class dots split into students while the mean line rises continuously, 40 → 85 (3:11.6–3:13.6).

Reading holds are respected: 120°/360° = 1/3 is up about 3 s, and π(r/2)²/πr² = 1/4 for about 4 s. Only fixes 3–5 are left, and they are cosmetic.

**Audio (9).**
- Pace is 156 wpm in speech. Loudness is on target, leading silence is 0.00 s and trailing silence 1.54 s.
- Planned breaths of 1.1–1.6 s follow each key result: "a third of the rim", "no bug", "Where will they crowd?", "never said which", "a half on both" and "matched the radius program".
- All 7 deictics land on an animation start (report). I confirmed "this arc" (0:45), "this gold circle" (1:33–1:35) and "this circle" (1:45) on the sheets.
- The Whisper differences are homophones ("Janes"), number formatting, or chunk-boundary duplicates that the word timings show are not in the audio.

**Concision (9).** The episode is 500 words in 3:33.5. On a mute test of each beat, I found no removable sentence. "Geometry agrees" is paid off by "the third we found". The error-bar line is what makes "no bug" credible. The survey beat cashes the 0:17 promise.

**Originality (9).** Three things here are uncommon in standard Bertrand treatments: every recipe shown as a way of scattering midpoints around one incircle, the two-circle invariance board, and the class-size bridge built from the same "what is spread evenly" dots. None of it is stock visuals or slop phrasing.
