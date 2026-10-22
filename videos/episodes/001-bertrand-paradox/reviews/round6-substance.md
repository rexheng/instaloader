# Round 6 review: substance (science and story editor)

I am an independent critic. My focus is factual and mathematical correctness, the hook and tension, clarity, concision, originality and AI slop. I still score every dimension.

**Evidence used**
- The existing `review/` pack. metrics.json (08:30) is newer than final.mp4 (08:28), so I reused it.
- report.md, narration_diff.txt, transcript.txt, all 13 contact sheets.
- 13 full-resolution keyframes: kf_02 0:14.2, kf_06 0:47.5, kf_11 1:23.1, kf_15 1:44.6, kf_17 2:04.6, kf_21 2:23.0, kf_26 2:42.4, kf_29 2:53.7, kf_31 3:04.8, kf_33 3:15.5, kf_37 3:29.8, kf_40 3:48.4.
- 8 frames I extracted with ffmpeg: 0:00.0, 1:20.6, 2:31.5, 2:50.0, 3:01.8, 3:12.6, 3:36.4, 3:38.2.
- Episode files: script.md, narration.txt and facts.md.

**Independent recomputation** (my own Monte Carlo, not sim.py, 2,000,000 lines per program; small circle of radius R/2 centred 0.4 R from the big centre, each line judged by its distance from each circle's centre and conditioned on crossing the small circle)

| program | big circle | small circle | on screen |
|---|---|---|---|
| radius | 0.5000 | 0.4992 | 0.50 = 0.50 |
| midpoint | 0.2502 | 0.4119 | 0.25 ≠ 0.41 |
| endpoints | 0.3335 | 0.4725 | 0.33 ≠ 0.47 |

- **Board geometry**, measured from pixels at 3:01.8: big radius 270 px, small radius 135 px (R/2), centre offset 108 px (0.4 R), small gold circle 69 px (about r/2). This matches the simulation set-up.
- **Formulas**, re-derived:
  - Side of the inscribed triangle = 2r·sin 60° = r√3.
  - L = 2√(r² − d²) > r√3 ⇔ d < r/2, and r/2 is the inradius.
  - The far arc is 120°/360° = 1/3.
  - Radius program: (r/2)/r = 1/2.
  - Midpoint program: π(r/2)²/πr² = 1/4.
- **Endpoint midpoint bands**, exact: 0.064 0.064 0.066 0.068 0.071 | 0.076 0.084 0.097 0.123 0.287. The on-screen simulated bars (last 0.284, gold sum 0.334) are within sampling noise.
- **95 % half-widths at n = 10⁴**: 0.92, 0.98 and 0.85 points, so "good to about one percentage point" holds. The gap 0.498 − 0.248 = 0.250 matches "25 points".
- **Class sizes**:
  - (10+10+100)/3 = 40.
  - (10²+10²+100²)/120 = 85.
  - Stony Brook: 40.5·(1 + 65.8²/40.5²) = 147.4, consistent with 147.
- **Landing number line** (kf_40): 0 is at 1061 px and 1 at 1762 px. The dots sit at 1236, 1294 and 1411 px, which is 0.250, 0.333 and 0.499. Correct.
- **Opening chord** (kf_02 = kf_40): endpoints at (291, 347) and (708, 862). Its midpoint is about 115 px from the centre, inside the 176 px incircle, so turning it gold in the landing is correct.

---

```
EPISODE: 001 — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly — every recipe is a way of scattering chord midpoints around the one small circle that decides "long" (1/3, 1/2, 1/4); a physical process (Jaynes's unaimed straws) picks 1/2, and the same choice makes one college's average class 40 or 147.
SCORES: Hook 9 · Clarity 9 · Visual 8.5 · Motion 9 · Audio 9 · Concision 8.5 · Originality 9
WEIGHTED: 8.9 (887.5/100 = 8.875)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none (0 banned phrases or patterns; no factual error; every empirical claim carries an on-screen citation; 0 layout-audit issues; mechanics all inside the bar)
FINAL: 8.9   PASS: no
FACTS:
- Bertrand published the chord puzzle in 1889 (Calcul des probabilités, Gauthier-Villars) | Verified | archive scan per facts.md H1; arXiv 1504.01361 and several secondary sources quote the 1889 edition
- "None is wrong and none is right" = « Aucune des trois n'est fausse, aucune n'est exacte » (on screen 1:15–1:20) | Verified | quote confirmed by web search (arXiv 1504.01361; Malo 2021, citing p. 5); the sentence continues "la question est mal posée"
- "A warning about two words, at random" | Verified (fair paraphrase) | Bertrand's chord problem reads "On trace au hasard une corde…", and he concludes the question is ill-posed
- Recipe answers 1/3, 1/2, 1/4; simulated 0.334 / 0.498 / 0.248 from 10,000 chords each | Verified | exact derivations above; s.e. consistent
- "Each tally is good to about one percentage point" | Verified | 95 % half-widths 0.85–0.98 pts
- "They disagree by 25 percentage points" | Verified | 0.498 − 0.248 = 0.250
- A chord is long iff its midpoint is within r/2, the triangle's inscribed circle | Verified | re-derived
- Radius program: equal share per ring, so midpoints crowd the center; endpoints program piles them against the rim (last band 0.284) | Verified | density of d uniform vs (2/π)/√(r²−d²)
- Invariance board 0.25≠0.41, 0.33≠0.47, 0.50=0.50 | Verified | my 2M-line Monte Carlo (table above)
- Edwin (E. T.) Jaynes argued an unaimed physical process fixes the answer via translation and scale invariance | Verified | Jaynes 1973, "The Well-Posed Problem", Found. Phys. 3(4):477–492, §5–6 (bayes.wustl.edu/etj/articles/well.pdf)
- Jaynes and Charles (E.) Tyler, broom straws from a standing position, 5-inch circle, 128 crossing tosses matched the radius program's law | Verified | same paper §6: "5-in.-diameter circle … 128 successful tosses confirmed Eq. (13)"; Eq. (13) is the uniform-distance solution's chord-length law, equivalent to a flat midpoint-distance spread
- Toy classes 10, 10, 100: per-class mean 40, per-student mean 85 | Verified | arithmetic above; tagged "example"
- Stony Brook 1974: random class 40, random student 147, 737 classes | Verified | Feld & Grofman 1977, Research in Higher Education 6(3):215–222 (JSTOR 40195170 snippet: students "experience an average class size of 147 students … despite the fact …"); 40.5·(1+65.8²/40.5²) = 147.4
MECHANICS: runtime 3:48.4 · wpm 157 (speech) / 151 overall · max silence 1.87 s (planned "Pick a number" hold, 0:07.8–0:09.7) · max static 2.97 s · −14.0 LUFS / −1.7 dBTP · lead 0.00 s / trail 1.36 s
FIXES (highest impact first):
1. [3:15.5, kf_33, 3:13.4–3:16.5][Visual] Left 60 % of the frame is empty while "at random / average class / 40 or 147" sits alone at the right edge (x ≈ +3.3) for about 3 s. Bring the returning stakes block back centred (x = 0) on "Surveys hide the same two words". Then on "Take classes" translate it (0.8 s, smooth) to its right-hand slot while the chart title fades in. This is the episode's emptiest frame; with fix 2 it lifts Visual to 9.
2. [3:01.6–3:13.0, f_3-12.6, kf_31][Visual/Clarity] While the narration describes the real Jaynes–Tyler tosses, the floor still carries the italic "simulated" tag and the simulated straw texture (dimmed to about 30 %). A viewer can read the real 128 tosses as simulated, and it is the one moment where real and simulated share a frame. On "Jaynes and Charles Tyler" (3:01.6), fade the "simulated" tag and the straw texture to 0. Leave the clean circle with a small "5 in" dimension mark across it in grey, matching the "5-inch circle" label.
3. [3:36.9–3:47.1][Concision/Clarity] The landing has two closers, and their words collide: "Name the way, and only one is." is followed 2 s later by "Both averages are right…". "Only one" then "both" sounds like a contradiction on one hearing, and the elided "is [right]" adds to it. Replace both sentences with one: "Name the way, and only one is: a half for tossed straws, a hundred forty-seven for a random student." On "a half" flag the green 1/2 and its "straws" tag. On "random student" brighten the 147 row and leave 40 dim. This is about the same length (≈ 5 s) and ends on one resolved answer for each half of the opening. If the class tie-in must stay two-sided, keep the current visuals and just cut the final sentence; the rows on screen carry it.
4. [2:41.0–2:49.8][Clarity] "so a fair recipe must score the same on both" brings in a new noun. The episode says "program" everywhere else (0:50, 1:03, 1:46, 1:58, 2:13, 2:20, 2:59). Say "so a fair program must score the same on both". Also split the 9 s sentence after "at once" ("One rain lands on both circles at once. Each judges with its own gold circle, so…") to give the demo line's two verdicts a breath.
5. [3:03–3:09, sheet 11][Visual] The right column holds only "straws ?" / "radius 0.50" over an empty lower half for about 6 s before "5-inch circle" and the predicted histogram arrive. Bring the predicted-histogram axis (baseline, "center … r/2 … rim", 10 % line) in dim at 3:03 so the block has its final shape. The bars then grow on "flat spread" as now.
6. [0:00–0:09][Hook, nitpick] The title "Three Right Answers…" gives away that the answer is plural before the viewer commits at 0:07 ("Pick a number"). Consider a title that keeps the bet open, e.g. "What's the Chance a Random Chord Is Long?", and keep "three right answers" as the line that lands at 1:11.
REACHES 9 IF ALL FIXED: yes. Fixes 1, 2 and 5 take Visual from 8.5 to 9 (+0.75 weighted), and fix 3 takes Concision from 8.5 to 9 (+0.5), giving 900/100 = 9.0. Fix 4 makes Clarity 9 safe. Nothing structural is missing: the hook, the failure beat, the one picture, the real-source payoff and the return to the first frame are all present.
KEEP:
- The midpoint reduction (1:25–1:47): the chord shrinks as its midpoint slides, the incircle is drawn at r/2, then three panels collapse to midpoints with histograms and π(r/2)²/πr² built from the disks. This is the canonical picture.
- The two-circle invariance board with one line judged twice (2:41–3:01): grey on the big circle, gold on the small one, "? = ?" for the straws, then 0.25≠0.41, 0.33≠0.47, 0.50=0.50, all independently verified.
- The landing restores the exact first frame (same chord, same P(— > —) = ?), turns that chord gold through its midpoint and sweeps the 0–1 line.
```

## Notes by dimension

**Hook (9).** The first frame (0:00.0) is the circle and triangle, with a chord drawn by 0:03. The question is built from copies of the two segments by 0:07, and "Pick a number" gets a 1.9 s hold, so the viewer commits before 0:10. The stakes (0:17–0:24) preview the payoff's own numbers. Tension climbs through the confident 1/3 ("Case closed", 0:50), the 25-point split (1:20) and the "? = ?" test. The ending returns to the first frame exactly (kf_02 vs kf_40, the same chord pixels). Against a 10: the title spoils the plurality before the bet (fix 6), and "40 or 147" at 0:22 is cryptic until 3:30.

**Clarity (9).** The order is concrete first throughout. The naive simulation works and is confirmed by geometry, then breaks. The one insight is "a chord is the distance of its midpoint", and every answer is read off that one picture. Assumptions are stated: "can't be aimed, so the answer can't depend on where the circle sits or how big it is". Honest limits are kept: "some way of drawing chords makes it right". Every number checks. Two soft spots:
- the "only one / both" collision in the landing (fix 3);
- the 9 s invariance sentence with a new noun, "recipe" (fix 4). The one-line demo at 2:43–2:49 rescues it.

**Visual (8.5).** The palette is semantic and consistent: gold = long, blue, green and purple = the three recipes, grey = neutral and class bars. Charts carry quantity names ("gold share", "share of midpoints, by distance from center", "class size (students)"). Simulated content is tagged, and citations sit bottom-left. Below 9:
- 3:15.5, a mostly empty frame (fix 1);
- 3:01–3:13, the leftover "simulated" floor during the real experiment (fix 2);
- 3:03–3:09, a half-empty right column (fix 5).

The 35 % dimming of tallies at 1:20–1:23 and of scoreboard rows at 2:31 is intentional context dimming and is allowed.

**Motion (9).** Objects persist and transform:
- the arc flies into 120° (0:47–0:49);
- the big circle shrinks into panel 1 with its tally;
- the disks fly into π(r/2)²/πr² (1:57);
- the midpoints collapse in place;
- the class dots split into students while the bars widen and the mean line rises continuously from 40 to 85 (3:23–3:29).

The longest static stretch is 2.97 s. Nothing I saw was decorative.

**Audio (9).** Pace is 157 wpm in speech. Loudness and peak are on target. WER is 1.6 %, and the differences are only homophones (chord/cord, Jaynes/Janes) and number formatting. The deictics land: "this far arc" lights at 0:47, "this gold circle" fills at 1:43–1:45, and "rim, radius, area" highlight on their words at 2:23–2:25. I could not hear the audio, so I make no deduction beyond what the transcript shows.

**Concision (8.5).** There are 576 words at 3:48, near the top of the window, with two payoffs (Jaynes, then class sizes). Each beat earns its place. The slack is the double closing line (3:41–3:47), plus the mild restatement at 2:20–2:28. That one is acceptable because it is the general rule ("three things spread evenly").

**Originality (9).** Bertrand's paradox is well-trodden, but three things here are not stock. The invariance test is shown as a live two-circle scoreboard with a line judged twice. The real Jaynes–Tyler result is the arbiter. The bridge to size-biased sampling ("spread evenly over students instead of classes") turns the toy into a data-science consequence.

**AI-slop scan.** I found no banned phrases (my grep agrees with the report's count of 0). There are no question chains: 2 questions, at 0:03 and 2:03. There are no "it's not just" constructions, no empty superlatives and no recap ending. "One point sets a chord's length: its midpoint" (1:25) has the colon-reveal shape, but it is a real definition delivered with a picture, not a fake reveal, so I do not count it.
