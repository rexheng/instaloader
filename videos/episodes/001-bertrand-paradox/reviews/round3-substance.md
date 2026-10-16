# Round 3 review: substance (science and story editor)

Reviewer role: independent science editor and story editor. My emphasis is factual and mathematical correctness, hook and tension, clarity, concision, originality and slop. I still score every dimension.
Evidence used:
- `review/` pack (metrics.json 19:57 is newer than final.mp4 19:56, so it was reused).
- All 13 contact sheets.
- 15 full-resolution keyframes: kf_01, 06, 08, 11, 17, 19, 21, 24, 28, 31, 33, 34, 37, 38, 40.
- An extra frame sweep at 1:37.5–1:44.5 (0.5 s steps, extracted with ffmpeg).
- transcript.txt, narration_diff.txt, script.md, narration.txt and facts.md.
- An independent 2M-chord simulation (my own code) and primary sources fetched and read directly.

```
EPISODE: 001-bertrand-paradox — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly (rim, radius or area), because each recipe scatters chord midpoints differently around the one small circle that decides "long"; a stated physical process (unaimed straws) picks one, just as "random class" vs "random student" give 40 vs 147.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 9 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6  (127.5 + 212.5 + 127.5 + 135 + 85 + 85 + 90 = 862.5 / 100)   AFTER CEILING: 8.6  (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.6   PASS: no
```

## FACTS

| Claim (spoken / on screen) | Status | Source / check |
|---|---|---|
| Inscribed triangle side = r√3; chord length L = 2√(r² − d²); L > side ⇔ d < r/2; the r/2 circle is the triangle's incircle | Verified | Re-derived. 2√(r² − d²) > √3 r ⇔ d² < r²/4. Equilateral inradius = R·cos 60° = R/2. |
| Random endpoints → 1/3 ("far arc, a third of the rim", 120°/360°) | Verified | Fix a vertex at the first point. The chord beats the side iff the second point is on the opposite 120° arc. |
| Random radial point → 1/2 ("half the radius") | Verified | d ~ U(0, r), so P(d < r/2) = 1/2. |
| Random midpoint → 1/4 (π(r/2)²/πr²) | Verified | Area ratio. |
| "Inner rings are small; every ring gets an equal share" (radial recipe crowds the centre) | Verified | d is uniform and ring area ∝ d, so areal density ∝ 1/d. |
| "Endpoint program piles them against the rim, so only a third land inside" | Verified | The density of d is (2/π)/√(r² − d²), which diverges at d → r. P(d < r/2) = (2/π)·asin(1/2) = 1/3. |
| Tallies 0.334 / 0.498 / 0.248 of 10,000; "good to about one percentage point"; "disagree by 25 percentage points" | Verified | 95% half-width 1.96·√(p(1−p)/10⁴) ≈ 0.85–0.98 pts. Gap 0.498 − 0.248 = 0.25. |
| Invariance test: midpoints 0.25 → 0.41, endpoints 0.33 → 0.47, radius 0.50 → 0.50 (small circle R/2, centre 0.4R off) | Verified | My own run (2M chords per recipe, seed 7, my code): 0.2502/0.4114, 0.3334/0.4714, 0.5000/0.5004. |
| Bertrand published the puzzle in 1889 (*Calcul des probabilités*) | Verified | archive.org scans `calculdesprobab00bertgoog` and `calculdesprobab01bertgoog` (1889, Gauthier-Villars), ch. I §5. Some catalogues give 1888 for the first printing; 1889 is defensible. |
| « Aucune des trois n'est fausse, aucune n'est exacte » / "none is wrong and none is right" | Verified (verbatim) | 1889 OCR: "Entre ces trois réponses, quelle est la véritable? Aucune des trois n'est fausse, aucune n'est exacte, la question est mal posée." The three arguments in the scan match the three recipes, including the "perpendicular diameter" version of the radial one. |
| "A warning about two words: at random" | Verified (paraphrase) | Jaynes 1973 summarises Bertrand's position as "ill posed, the phrase 'at random' being undefined". |
| Jaynes 1973 argued a physical process picks one; unaimed straws ⇒ answer independent of circle's position and size | Verified | E. T. Jaynes, "The Well-Posed Problem", *Found. Phys.* 3:477–492 (1973). Read in the bayes.wustl.edu PDF: solution C is "eliminated for lack of translational invariance", and B is "incompatible with either scale or translational invariance". |
| Jaynes and Charles Tyler tossed broom straws at a 5-inch circle; the 128 that crossed matched the radius program's chord-length distribution | Verified | Same PDF, §6: "performed by the writer and Dr. Charles E. Tyler, tossing broom straws from a standing position onto a 5-in.-diameter circle drawn on the floor. Grouping the range of chord lengths into ten categories, 128 successful tosses confirmed Eq. (13) with an embarrassingly low value of chi-squared." |
| "A skilled tosser, Jaynes noted, could produce other answers" | Verified | §1: "if the circle becomes sufficiently large, and the tosser sufficiently skilled, various results could be obtained at will". |
| Classes 10, 10, 100: random class 40, random student 85 | Verified | 120/3 = 40. (10² + 10² + 100²)/120 = 85. On-screen line heights also check: 161/405 and 344/405 of the 100-bar give 39.8 and 85 (kf_37). |
| Stony Brook 1974: 40 for a random class, 147 for a random student; 737 classes | Verified | Feld & Grofman, *Res. High. Educ.* 6:215–222 (1977), read in the UCI PDF. p. 216: "In the spring of 1974, at … Stony Brook, 737 classes … mean of 40.5 … students experienced a mean class size of 147". Consistency check: 40.5·(1 + 65.8²/40.5²) = 147.4. |
| "Whatever number you picked, some way of drawing chords makes it right" | Verified (mathematically) | Any P(d < r/2) ∈ [0, 1] can be built. Jaynes §6 says a precise machine can "produce any distribution of chord lengths we please". The story problem with this line is fix 2. |

No wrong, fabricated or uncited empirical claims. All three sources are on screen with author, year and venue, each held well over 3 s.

## MECHANICS

```
MECHANICS: runtime 3:49.3 · wpm 163 (speech; 188 excluding all pauses) · max silence 1.92 s · max static 3.50 s · −14.1 LUFS / −1.7 dBTP
```
Leading silence is 0.00 s and trailing is 1.78 s. There are no black frames, and the layout audit found 0 issues.

Transcript and slop:
- Banned phrases: 0. Banned patterns: none. There is one genuine question ("Where will they crowd?", 2:00.6), and it is followed by a 1.6 s hold.
- No "it turns out", no fake reveals, and no recap ending. "Three programs, three things spread evenly…" (2:19) is a one-line synthesis that adds the "rim/radius/area" contrast, so I don't count it as a recap.
- WER 3.7%. Every difference is a homophone or number formatting (chord/cord, poll/pole, Jaynes/Janes, "a hundred" → "100"). Nothing points to a mispronunciation.

Hook:
- The question and the circle are on screen in the first frame.
- "Pick a number" comes at 0:06.8 and is followed by a 1.9 s hold, so the viewer commits before 0:12.

## Where the frames and story fall short of 9

- **The invariance test's target looks circular (2:31–2:59, kf_24, kf_28, kf_31).**
  - The simulated "straws" are isotropic lines with uniform offset. That is the radius program extended to lines, by construction.
  - The scoreboard puts "straws 0.50 = 0.50" at the top as the thing a program must "match", so the test looks rigged toward the radius answer.
  - The real arbiter is the invariance logic plus Jaynes and Tyler's 128 real tosses. The simulated straw row adds nothing to that, and it invites an attentive viewer to object.
- **The landing line undoes the Jaynes payoff (3:38–3:47).**
  - 2:27–3:12 builds up that "a physical process can pick one", and the real straws backed 1/2.
  - The last line then says "whatever number you picked … some way of drawing chords makes it right". That is true, but it drops the resolution and leaves the episode on pure relativism.
  - The opening question was really asking which way of drawing is meant. The ending should give both halves: every number answers some process, and naming the process gives one answer.
- **"40 · 147" sits on the 0–1 probability axis (3:41–3:49, kf_40).**
  - It is grey, directly below the axis, between the 0.6 tick and the "1" label, so it reads like axis values.
  - It is the only element of the final frame that doesn't belong to the chord picture.
- **The pivot to midpoints is announced, not motivated (1:25).** "Follow one chord's midpoint" comes straight after "none of the code has a bug". The one step the viewer could have invented (what single point decides a chord's length?) is skipped.
- **Orphaned "85" and "40" (3:31–3:37, kf_38).**
  - When the example dims, the words "random student/class" leave, but the numbers stay at x≈1090–1170.
  - That is about 330 px from their lines and right against the Stony Brook block's rule, so the dimmed toy "40" reads as if it labels Stony Brook.
- **"Piles them against the rim" vs the dot cloud (2:13–2:21, kf_21).**
  - The endpoint panel's 240 midpoints also visibly clump at the centre. This is correct: the areal density ∝ 1/(d√(r² − d²)) diverges at both ends.
  - The narration names only the rim. The histogram carries the claim, but the eye is on the dots.
- **The Jaynes section is dense (2:41–2:59).**
  - In 18 s it shows two circles, a followed straw, four scoreboard rows and eight numbers, with three program rains.
  - The delivery runs at 188 wpm without pauses, and the transcript shows 2:18–3:38 with almost no sentence breaks.
  - It is followable, but it is the one stretch that needs a rewatch.
- **The stakes line is abstract (0:16.9–0:20.9).** "Every poll and every simulation has to decide what they mean." Polls never return. The payoff at 3:16 says "Surveys", so the setup and payoff use different words.

## FIXES (highest impact first)

1. **[2:41–2:59][Clarity] The scoreboard asks programs to "match the straws", but the simulated straws are the radius program by construction (circular).**
   - Make invariance the criterion, not the simulated straws. Narration: "One rain lands on both circles at once, and nobody can aim at either, so an honest program must score the same on both."
   - Remove the straws row's numbers during the test: show "straws  ?  =  ?" in grey, or drop the row and keep only the two circle icons.
   - Reveal the real experiment (5-inch circle, 128 crossed it, matched the radius spread) as the arbiter at 2:59.
   - Keep the "simulated" tag on the rain.
   - Effect: removes the circular look and lifts Clarity 8.5 → 9.
2. **[3:38–3:49][Hook/Clarity] The closing line says every answer is right, which cancels the Jaynes resolution. The "40 · 147" pair sits on the probability axis.**
   - Change the last line to (≈ same length): "So whatever number you picked, some way of drawing chords makes it right. Name the way, and only one is. Forty and a hundred forty-seven are both right, once you say who's picked."
   - Or, shorter: "…some way of drawing chords makes it right; say which way, and there's one answer."
   - Move "40 · 147" off the 0–1 axis to its own spot under the question, e.g. "class 40 · student 147" at y ≈ −1.8 aligned with the equation.
   - On "Name the way", flag the green 1/2 together with a tiny straw glyph (one grey line through the circle).
   - Effect: the ending re-sees the opening and resolves it.
3. **[1:25–1:30][Clarity] The midpoint pivot is unmotivated.**
   - Replace "Follow one chord's midpoint." with "Every program ends with a chord, and one point sets its length: its midpoint."
   - Keep the same slide animation, starting on "its midpoint".
   - Effect: about +1.5 s, and the step becomes one the viewer could have invented.
4. **[3:29–3:37][Visual] Orphaned dimmed "85" and "40" sit next to the Stony Brook block.**
   - Fade the two numbers out together with "random student / random class" on "Stony Brook".
   - Alternatively, move them to the line ends (x ≈ 790 px, buff 0.2) before the dim.
   - Effect: removes the misreading that the toy 40 belongs to Stony Brook.
5. **[2:26–2:41][Concision] The Jaynes setup takes 15 s before the test starts.**
   - Rewrite as: "In nineteen seventy-three, Edwin Jaynes said a physical process picks one: long straws tossed from a standing height can't be aimed, so the answer can't depend on where the circle sits or how big it is."
   - Effect: saves about 3 s. Spend them on fix 6.
6. **[2:47–2:59][Audio/Motion] Eight numbers arrive in 12 s, with no breath between rows.**
   - Insert 0.35 s silences after "then point four one", after "then point four seven" and after "like the straws".
   - Hold the finished scoreboard (kf_31 state) ≥ 2 s before "Jaynes and Charles Tyler".
   - Effect: reading time respected, and the 188 wpm (excluding pauses) drops toward 175.
7. **[2:13–2:17][Clarity] "Piles them against the rim" while the dots also clump at the centre.**
   - On "piles them against the rim", flash the last histogram bar (0.284) together with the outer 0.9r–r annulus of panel 1 (blue stroke, ≤ 1 s).
   - Effect: the claim is read off the measured bar, not the dot cloud.
8. **[0:16.9–0:20.9][Hook] The stakes line is abstract and uses a word ("poll") that never pays off.**
   - Change to "Every survey and every simulation has to decide what they mean."
   - Effect: the setup now matches "Surveys hide the same two words" at 3:16.

**REACHES 9 IF ALL FIXED: yes, narrowly.**
- Fixes 1, 3 and 7 take Clarity to 9. Fix 2 takes Hook to 9 and, with fix 4, Visual to 9. Fix 5 takes Concision to 9. Fix 6 takes Audio to 9.
- Total: 135 + 225 + 135 + 135 + 90 + 90 + 90 = 905, which is 9.05.
- No structural change is needed. The spine is right: naive sim, then "geometry agrees", then two more programs disagreeing by a measured 25 points with error bars, then the incircle unification, then the invariance test and real data, then the survey analogue, then back to the first frame.
- The two fixes that matter most are both story fixes, not craft fixes:
  - **(1)** the test must not look rigged;
  - **(2)** the last line must keep Jaynes's resolution instead of erasing it.

**KEEP:**
- The measured failure at 1:11–1:25: three tallies on one "gold share" line with 95% error bars and a "25 points" brace, plus "none of the code has a bug". It is the Stuff Made Here beat done right.
- The incircle unification, 1:25–2:23. One chord's midpoint slides to r/2, the gold circle appears, every chord collapses to its midpoint, and π(r/2)²/πr², (r/2)/r and the stacked 0.334 column are each built from their own picture.
- The class-size dots, 3:22–3:29. Each class dot splits into students, the bars widen to "width = students", and the mean line rises continuously 40 → 66 → 85. It reuses the episode's own "what is spread evenly" picture on real social-science data.
