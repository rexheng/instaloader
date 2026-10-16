# Round 1 review: substance (science and story editor)

Independent critic. My focus is factual and mathematical correctness, the hook and narrative tension, clarity, concision, originality and AI slop. I still score every dimension.

**Evidence used**
- The existing `review/` pack. metrics.json (Oct 15 23:40) is newer than final.mp4 (23:38), so I reused it rather than regenerating.
- report.md, narration_diff.txt, transcript.txt and transcript_words.tsv.
- All 13 contact sheets.
- 12 full-resolution keyframes: kf_02 (0:13.9), kf_05 (0:40.7), kf_07 (0:55.3), kf_11 (1:23.2), kf_19 (2:04.7), kf_22 (2:20.2), kf_26 (2:33.8), kf_30 (2:54.0), kf_33 (3:03.6), kf_36 (3:22.3), kf_38 (3:31.7) and kf_40 (3:51.3).
- 10 extra frames I pulled with ffmpeg: 1:03.0, 1:03.5, 1:04.0, 1:20.5, 1:21.0, 1:21.5, 1:22.0, 2:08.0, 2:46.5, 3:13.0, 3:17.0 and 3:49.0.
- Episode files: script.md, narration.txt and facts.md.

**Independent recomputation** (my own code, not sim.py)
- **Invariance board.** I ran 2,000,000 lines per program. The small circle has radius R/2 and its centre sits 0.4 R from the big centre. Each line was judged by its distance from each circle's centre.

  | program | big circle | small circle |
  |---|---|---|
  | midpoint | 0.2502 | 0.4114 |
  | endpoints | 0.3338 | 0.4712 |
  | radius | 0.5005 | 0.4997 |

  The on-screen 0.25/0.41, 0.33/0.47 and 0.50/0.50 are correct.
- **Class sizes.** (10+10+100)/3 = 40. (10²+10²+100²)/120 = 85. Stony Brook: 40.5·(1 + 65.8²/40.5²) = 147.4, consistent with 147.
- **95 % half-widths at n = 10⁴.** 0.92, 0.98 and 0.85 points, so "good to about one percentage point" holds. The on-screen error bars measure about ±0.0085 to ±0.01 at kf_11. The gap is 0.498 − 0.248 = 0.250, matching "25 points".
- **Re-derived formulas:**
  - L = 2√(r² − d²) > r√3 ⇔ d < r/2, and r/2 is the inradius.
  - Endpoints: the far arc is 120°/360° = 1/3.
  - Radius: (r/2)/r = 1/2.
  - Midpoint: π(r/2)²/πr² = 1/4.
  - Endpoint midpoint-distance density: (2/π)/√(r² − d²). The last band should hold 0.287; the bar shows 0.284.
- **Plotted positions.** At kf_11 the number-line dots sit at x = 490, 790 and 1357 px, which on the 0.2–0.5 axis is 0.248, 0.334 and 0.498. Correct.
- **Opening chord.** At kf_40 its midpoint is about 116 px from the centre, inside the 176 px incircle, so turning it gold in the landing is correct.

---

```
EPISODE: 001 — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly: each recipe scatters chord midpoints differently around the one small circle that decides "long", giving 1/3, 1/2 or 1/4, and only a specified physical process (Jaynes's straws) picks one.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.6   AFTER CEILING: 8.6 (ceiling 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.6   PASS: no
```

**FACTS**

| Claim | Verdict | Source |
|---|---|---|
| Joseph Bertrand published the chord puzzle in 1889 | Verified | *Calcul des probabilités*, Gauthier-Villars 1889, ch. I §5. Some catalogues give 1888 for the first printing; 1889 is the title-page year. |
| He printed three answers and wrote « Aucune des trois n'est fausse, aucune n'est exacte » (shown 1:15–1:25) | Verified, verbatim | The sentence continues "la question est mal posée". Quoted identically in D'Agostini, arXiv 1504.01361. |
| "as a warning about two words: at random" | Verified (fair paraphrase) | Jaynes 1973 summarises Bertrand's position as "the phrase 'at random' being undefined". |
| Side = r√3; long ⇔ midpoint within r/2; r/2 = inradius | Verified | Re-derived. |
| Endpoints 1/3 (sim 0.334); radius 1/2 (0.498); midpoint 1/4 (0.248) | Verified | Re-derived. Sim values lie within 95 % CI of the exact values. |
| "Each tally is good to about one percentage point"; "disagree by 25 percentage points" | Verified | 1.96·√(p(1−p)/10⁴) ≤ 0.98 pt; 0.498 − 0.248 = 0.250. |
| Radius program crowds midpoints to the centre (equal share per ring, inner rings small) | Verified | Uniform in d; ring area ∝ d. |
| Endpoints program piles midpoints against the rim | Verified | The density blows up at d → r; last band 28.4 %. |
| Edwin Jaynes, 1973, *Foundations of Physics*: a physical process (unaimed straws) picks one; the answer cannot depend on the circle's position or size | Verified | "The Well-Posed Problem", Found. Phys. 3(4):477–492 (Inspire/PhilPapers metadata; preprint at bayes.wustl.edu). Invariance yields f = 1/(2πRr), "corresponding to solution A" (uniform distance, i.e. the radius program). "Can't be aimed" slightly overstates Jaynes, who says the tosser lacks the skill to make straws hit a given circle with certainty. |
| Scoreboard 0.25≠0.41, 0.33≠0.47, 0.50=0.50 | Verified | My 2M-line simulation, above. |
| Jaynes and Charles Tyler tossed broom straws at a 5-inch circle; 128 that crossed matched the radius program's chord-length spread | Verified | Jaynes 1973 §6: "tossing broom straws from a standing position onto a 5-in.-diameter circle … 128 successful tosses confirmed Eq. (13) with an embarrassingly low value of chi-squared". Eq. (13) is solution A's chord-length law. |
| "A skilled tosser, Jaynes noted, could produce other answers" | Verified | Jaynes §1: "if the circle becomes sufficiently large, and the tosser sufficiently skilled, various results could be obtained at will". |
| Classes 10, 10, 100: random class 40, random student 85 (tagged "example") | Verified | Recomputed. |
| Stony Brook, 1974, 737 classes: 40 per class, 147 as experienced by students | Verified | Feld & Grofman 1977, *Research in Higher Education* 6(3):215–222. JSTOR 40195170 excerpt: "students experience an average class size of 147 students". The paper's 40.5 / SD 65.8 reproduces 147.4. |
| "Whatever number you picked, some way of drawing chords makes it right" | Verified | Constructive: any P(d < r/2) ∈ [0, 1] is achievable. Jaynes §6 says a precise machine can produce "any distribution of chord lengths we please". |

**MECHANICS**
- Runtime 3:51.3 (in window, near the top).
- Pace 161 wpm in speech (152 overall). The rate excluding all pauses is 185, so the sentences themselves run fast.
- Silences: longest internal 1.92 s (the planned "Pick a number" hold at 0:07.7–0:09.6), leading 0.00 s, trailing 1.81 s.
- Static: longest 3.0 s, at 0:16.7.
- Loudness −14.0 LUFS (LRA 2.2), true peak −1.6 dBTP. No black frames.
- Layout audit 0/252. Banned phrases 0. WER 2.0 %: homophones only (chord/cord, Jaynes/Jane(s), numerals).

**Transcript / slop scan**
- No §4 banned phrases. No "not just X, it's Y". No rhetorical-question chain: "Where will they crowd?" is a single question followed by a planned 1.5 s hold. No hedging and no signposting.
- "Three programs, three things spread evenly: rim, radius, area" is a triplet of concrete nouns, not abstract adjectives, so it is fine.
- "One point sets a chord's length: its midpoint" is borderline as a colon reveal, but it carries content. Not counted.
- The ending is not a recap list.
- The hook lands at 0:02.8–0:06.2: the question is spoken over the circle, triangle and chord, which have been on screen since frame 1. "Pick a number" follows at 0:06.8 with a 1.9 s hold. That beats the 0:12 commit target.

**Dimension notes (evidence)**

*Hook 9.*
- Strengths: a concrete object in the first frame, an explicit commit, and an ending (3:39–3:51) that returns to the identical frame with 1/4, 1/3, 1/2 swept onto a 0–1 line and the opening chord re-seen through its midpoint. The opening is re-seen almost exactly.
- The stakes line at 0:16.9–0:21.1 ("Every survey and every simulation has to decide what they mean") is abstract. The episode's best stake, 40 vs 147, is not previewed until 3:16.
- The title gives away the "three answers" twist before the viewer commits.

*Clarity 8.5.*
- The core (0:21–2:27) is canonical-grade: naive simulation, then the exact 1/3 from the arc, then a second recipe that breaks it by a measured 25 points with error bars and "no bug", then the midpoint pivot, then three midpoint distributions with equations built from the pictures.
- The Jaynes test (2:42–2:59) is the one step a viewer cannot re-derive after one watch.
  - The narration never says that the small circle judges with *its own* gold circle. At 2:46.5 five circles are on screen: big circle, dimmed big triangle, dimmed big incircle, small circle and small incircle, and the rule has to be inferred from a 1.5 s demo line.
  - "So an honest program must score the same on both" asserts invariance in half a clause.
  - "Honest program" is an odd word: the programs are not dishonest, they model different processes.
- At 3:00–3:11 the Tyler result is "matched the radius program's spread of chord lengths", but the episode never showed a chord-length spread, only midpoint-distance histograms. The viewer has to take it on trust.
- At 3:16–3:29 the bridge from chords to classes is left implicit. "Width = students" is on screen, but no sentence says "spread evenly over classes, or over students", so the claim "Surveys hide the same two words" is not cashed out aloud.

*Visual 8.5.*
- Strengths: a semantic palette held all episode (gold = long; blue/green/purple = recipes), the "simulated" tags, citations at bottom-left, and equations coloured by referent (kf_22).
- Lopsided frames:
  - 2:29–2:42 (kf_26): the right ~45 % is empty apart from "gold share", an icon and "straws –".
  - 3:19–3:30 (kf_36): the class chart fills the left third while the right two-thirds are empty for about 10 s.
- The histograms (1:51–2:23) have no y-axis or reference level, so "every ring gets an equal share" (about 10 %) cannot be read as a number.
- At 3:49.0 the flag scale pushes "147" to within about 10 px of "student" and the solid-line glyph against "random". It is transient and below the 20 px clearance.

*Motion 8.5.*
- Excellent persistence: the big circle shrinks into panel 1 carrying its tally (0:49–0:53); panel 2 grows into the "any chord" circle (1:25–1:27); the gold circle copies into all three panels (1:47); chords collapse to midpoints; π(r/2)²/πr² builds from the disks (1:55–1:59); the endpoints' gold bars stack into a 0.334 column (2:17).
- At 3:16.5–3:18 the floor is gone and the frame is background, citation and one half-written glyph (frame 3:17.0). This is a near-empty beat that the script says should not exist.
- The four test rains plus the scoreboard fill run in about 12 s (2:47–2:59), rushed relative to their conceptual weight.

*Audio 8.5.*
- In sync: each deictic ("this far arc" 0:43 → arc lit by 0:45; "this gold circle" 1:43; "25 percentage points" 1:20 → brace label writing 1:21–1:22). Pauses are planned and loudness is on target.
- At 2:29.7–2:31.2, "Edwin" is stretched to 1.2 s and the name is heard as "Jane" (0.28 s), while 3:00 and 3:12 are heard as "Janes". The final /z/ is likely dropped once, and the prosody there is odd.
- The 185 wpm rate excluding pauses makes sentence interiors feel hurried.

*Concision 8.5.*
- Almost every line earns its place.
- Slack:
  - 1:38.9–1:48.9: "So a chord is long exactly when its midpoint lands inside this gold circle. Each program is really asking what share of midpoints land here." The second sentence restates the first.
  - Two payoffs (Jaynes 48 s, class size 22 s) push the runtime to 3:51, 9 s from the cap.

*Originality 8.5.*
- The midpoint unification is the standard treatment of Bertrand's paradox, as in the Wikipedia article.
- What is fresh: the SMH-style "code it a second way" failure with error bars, the animated invariance scoreboard with its "? = ?" straws row, and the class-size bridge. No slop.

```
FIXES (highest impact first):
1. [2:42–2:59][Clarity] The small circle's own judging rule is never spoken and the demo is cluttered (frame 2:46.5: dim big triangle + dim big incircle still visible). → Fade the big triangle and big incircle fully out before the demo line. Rewrite the narration to: "One rain lands on both circles at once. Each circle judges with its own gold circle, and a tosser who can't aim can't favour either, so a fair recipe must score the same on both." Replace "honest program" with "fair recipe". Hold the demo line ≥ 2 s (grey on big, gold on small) before the midpoint rain. Pay for the time with fix 9.
2. [3:00–3:11][Clarity] "matched the radius program's spread of chord lengths" refers to a distribution never shown. → On "radius program's spread", bring back panel 2's flat midpoint histogram (persisting object from 2:09) beside "128 straws crossed it". Change the line to "…matched the radius program's flat spread", since chord length is fixed by midpoint distance (1:25 beat), so the callback is exact.
3. [3:22–3:29][Clarity] The chords→classes bridge is implicit. → Change "Pick a student at random, and it's eighty-five" to "Pick a student at random, spread evenly over students instead of classes, and it's eighty-five", timed to the dot-split and widening bars (adds ~1.5 s).
4. [0:16.9–0:21.1][Hook] The stakes sentence is abstract. → Replace it with a concrete preview of the payoff: "Get them wrong and a college with forty-student classes hears its students say a hundred forty-seven." Optionally flash a dim "40 | 147" beside the question for 1.5 s, which then pays off at 3:29. Optional: retitle so it does not pre-announce the twist (e.g. "Draw a Chord at Random").
5. [2:29–2:42, 3:19–3:30][Visual] Half-empty frames (kf_26, kf_36). → At 2:29, draw all scoreboard row labels (midpoint/endpoints/radius) at 30 % with dashes from the first frame, so the right column is populated. At 3:19, centre the class chart (shift right ~2.5 units) and slide it left only when the Stony Brook block enters at 3:29.
6. [1:51–2:23][Visual] The histograms carry no y reference, so "equal share" cannot be read. → Add one dashed reference line at 10 % with a "10%" tick (MathTex ≥ 26) across each histogram. The flat green bars then visibly sit on it at 2:09.
7. [3:16.5–3:18][Motion] A near-empty frame (3:17.0: background, citation and one half-drawn glyph). → Start writing "at random" while the floor cross-fades out (overlap ≥ 0.5 s), or transform the floor's straws-row label into "at random", so no frame is empty.
8. [2:29.7–2:31.2][Audio] "Edwin Jaynes": "Edwin" is stretched to 1.2 s and the name is heard as "Jane". → Add a phoneme override for Jaynes (dʒˈeɪnz), regenerate that sentence and the 3:00 and 3:11 lines, and confirm Whisper hears "Jaynes" all three times.
9. [1:38.9–1:48.9][Concision] Two sentences say the same thing. → Merge them into "So a chord is long exactly when its midpoint lands in this gold circle, and each program is just a way of scattering midpoints." This saves ~2 s, which funds fixes 1 and 3.
10. [3:47–3:50][Visual] The flag scale pushes "147" within ~10 px of "student" (frame 3:49.0). → Flag by colour or opacity only (no scale), or widen the label-to-number gap to ≥ 0.35 units.
11. [2:47–2:59][Motion] The four rains plus the board fill are rushed. → Add 0.5 s after the midpoint row (before "Endpoints give…") and run each rain ≥ 2.5 s. Fund it from fix 9 or by trimming the 1.0 s pause after "a half on both" to 0.6 s.

REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1–3 lift Clarity to 9; 5–7 and 10 lift Visual and Motion to 9; 8 lifts Audio; 9 lifts Concision. That gives about 9.0 weighted. Originality stays the limiting dimension at 8.5, because the midpoint unification is the textbook route. The invariance scoreboard is the episode's memorable image and should be made even clearer, not trimmed.
KEEP:
- The cold open and the landing on the identical frame: the 1/4, 1/3, 1/2 sweep on the 0–1 line, the opening chord re-seen via its midpoint in the gold circle, and the "straws" tag on 1/2.
- The midpoint pivot and transform chain from 1:25 to 2:27: the chord shrinks as the midpoint slides, the incircle appears, chords collapse to midpoints, histograms grow, equations are built from the disks and radius, and the gold bars stack into the 0.334 column.
- The SMH failure beat at 0:47–1:25 ("Case closed, until you code it a second way"), with error bars, the "25 points" brace and "none of the code has a bug".
```
