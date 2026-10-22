# Round 8 review: substance (science and story editor)

I am an independent critic and did not make this episode. My focus is factual and mathematical correctness, hook and tension, clarity, concision, originality and AI slop (BAR §4). I still score every dimension.

**Evidence used**
- The existing `review/` pack. metrics.json (18:48) is newer than final.mp4 (18:46), so I reused it and did not regenerate it.
- I read report.md, narration_diff.txt, transcript.txt and transcript_words.tsv, plus all 12 contact sheets.
- I read 17 full-resolution keyframes: kf_01 0:04.2, kf_04 0:33.5, kf_08 0:54.1, kf_13 1:19.1, kf_14 1:22.3, kf_18 1:45.8, kf_19 1:54.8, kf_21 2:03.4, kf_23 2:12.0, kf_26 2:22.7, kf_29 2:35.2, kf_31 2:43.8, kf_32 2:52.2, kf_34 3:01.6, kf_36 3:11.2, kf_37 3:14.5, kf_38 3:16.8 and kf_40 3:33.4.
- I extracted frames of my own with ffmpeg:
  - single frames at 2:52.8, 2:53.4, 2:54.0 and 2:54.6 (the hand-off from simulated to real);
  - 4 fps strips of 2:26.6–2:30.6 (the circle move) and 2:33.2–2:37.2 (the demo line's two verdicts);
  - an 8 fps strip of 3:19.6–3:21.6 (Stony Brook to the landing).
- I read script.md, narration.txt, facts.md and the round-7 CHANGELOG.

## Independent recomputation

I wrote my own Monte Carlo (not sim.py), with 2,000,000 lines per program. The big circle has radius R. The small circle has radius R/2, and its centre sits 0.4 R from the big centre. Each line is judged by its distance from each circle's centre, and the small-circle share counts only lines that cross the small circle. Endpoint chords use the signed offset cos((t1 − t2)/2).

| program | big circle | small circle | on screen (2:41–2:51) |
|---|---|---|---|
| radius | 0.5000 | 0.4992 | 0.50 = 0.50 |
| midpoint | 0.2502 | 0.4107 | 0.25 ≠ 0.41 |
| endpoints | 0.3334 | 0.4714 | 0.33 ≠ 0.47 |

**Formulas, re-derived**
- The side of the inscribed triangle is 2r sin 60° = r√3.
- L = 2√(r² − d²) is longer than r√3 exactly when d < r/2, and r/2 is the triangle's inradius.
- The far arc is 120°/360° = 1/3.
- The radius program gives (r/2)/r = 1/2.
- The midpoint program gives π(r/2)²/πr² = 1/4.
- Isotropic lines restricted to a circle inside the big one are still isotropic, so the radius program must give 1/2 on the small circle. The MC confirms it.

**Measured off the frames**
- *Demo line (kf_29, 2:35.2).*
  - Its distance from the big centre is 160 px against R = 270 px, which is 0.59 R, so it is short there.
  - Its distance from the small centre is 52 px against r = 135 px, which is 0.39 r, so it is long there.
  - The small centre sits 108 px (0.40 R) from the big centre.
  - "short" and "long" are therefore both correct.
- *Opening chords (kf_04, 0:33.5).* I checked all six drawn chords against the 608 px side. The gold ones (647–681 px) are long and the grey ones (228 and 517 px) are short.
- *Histograms (kf_21, kf_23).*
  - The midpoint program's last bar is 18.4 % (exact 19 %).
  - The endpoints program's last bar is 28 % (exact 28.7 %).
  - The stacked gold column is 33 %.
  - The radius program's bands are flat on the 10 % line.
- *Class chart (kf_36, kf_37).* The bars are 40 px and 405 px tall, a ratio of 10.1. "random class" sits at 40.0 and "random student" at 85.2.
- *Arithmetic.* (10 + 10 + 100)/3 = 40, and (10² + 10² + 100²)/120 = 85.
- *Stony Brook.* 40.5 × (1 + 65.8²/40.5²) = 147.4, which matches the 147.
- *Landing number line (kf_40).* The dots read 0.250, 0.334 and 0.499. The opening chord's midpoint is 0.33 r from the centre, inside the gold circle, so turning it gold is correct.
- *Error bars.* The 95 % half-widths at n = 10⁴ are 0.92, 0.98 and 0.85 points, which supports "about one percentage point". The gap is 0.498 − 0.248 = 0.250, which is "25 points".

**Citations, verified by web search this round**
- **Bertrand 1889.** *Calcul des probabilités*. arXiv 1504.01361 (D'Agostini) and Malo 2021 (p. 5) both quote « Aucune des trois n'est fausse, aucune n'est exacte, la question est mal posée ». The quote on screen at 1:11–1:15 is verbatim.
- **Jaynes 1973.** "The Well-Posed Problem", *Foundations of Physics* 3(4):477–492. This is confirmed by Inspire-HEP, and PhilPapers gives the end page as 493. In the author's PDF, §6 reads: "…Tyler, tossing broom straws from a standing position onto a 5-in.-diameter circle drawn on the floor. Grouping the range of chord lengths into ten categories, 128 successful tosses confirmed Eq. (13)…". §5 eliminates solution C (uniform midpoint) "for lack of translational invariance". It even uses the phrase "a rain of straws", which the episode's "rain" echoes.
- **Feld & Grofman 1977.** "Variation in Class Size, the Class Size Paradox, and Some Consequences for Students", *Research in Higher Education* 6(3):215–222 (JSTOR 40195170). The JSTOR excerpt reads "experience an average class size of 147 students"; ResearchGate gives a perceptual ratio of 3.7, and 147/3.7 = 39.7 ≈ 40. Feld was at SUNY Stony Brook.

**Transcript artifacts that are not defects**
- "Only a a third" at 2:07 and "Each Each judges" at 2:34 come from Whisper chunk boundaries. Their word timestamps overlap: 127.05–127.19 against 127.11–127.25, and 154.09–154.59 against 154.55–154.57. They are not stutters in the TTS.
- "Janes" is Whisper's homophone spelling of /ʤeɪnz/.

---

```
EPISODE: 001 — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly; each recipe scatters chord midpoints differently around the one small circle that decides "long" (1/3, 1/2, 1/4), an unaimed physical toss picks 1/2 (Jaynes), and the same choice makes one college's average class 40 or 147.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 9.0 (900/100)   AFTER CEILING: 9.0 (lowest 9 + 2 = 11, not binding)
CAPS: none. 0 banned phrases or patterns in my own scan of narration.txt: no rhetorical-question chain, since "Where will they crowd?" at 1:52 is single; no "it turns out"; no fake reveals. 0 factual errors. Every empirical claim has an on-screen citation: Bertrand 0:12–0:24 and 1:07–1:14, Jaynes 2:21–3:01, Feld & Grofman 3:03–3:19. 0 layout-audit issues in 247 checks. Mechanics are all inside the bar.
FINAL: 9.0   PASS: yes (no margin: any half-point drop fails it)
FACTS:
- Bertrand posed the chord puzzle in 1889 (Calcul des probabilités) | Verified | arXiv 1504.01361; Malo 2021 p. 5; title-page year 1889
- "As a warning about two words, at random" | Verified (fair paraphrase) | Bertrand: "la question est mal posée"; Jaynes 1973 summarises the phrase 'at random' as undefined
- "Bertrand printed all three, writing that none is wrong, none is right" + French on screen | Verified, verbatim | « Aucune des trois n'est fausse, aucune n'est exacte »
- With a vertex on the first point, long iff the other end lands on the far 120° arc = 1/3 | Verified | re-derived; arc and 120°/360° = 1/3 on screen 0:45–0:50
- Simulated tallies 0.334 / 0.498 / 0.248 from 10,000 chords each, labelled "simulated" | Verified (within 1 s.e. of 1/3, 1/2, 1/4) | own MC
- "Each tally is good to about one percentage point" | Verified | 95 % half-widths 0.85–0.98 pts
- "They disagree by 25" / "25 points" | Verified | 0.498 − 0.248 = 0.250
- Midpoint sets the chord's length; long iff midpoint inside the triangle's inscribed circle (r/2) | Verified | L = 2√(r²−d²); inradius = r/2
- Midpoint program: a quarter of the area catches a quarter | Verified | π(r/2)²/πr² = 1/4
- Radius program: equal share per ring, so midpoints crowd the centre; half the radius gives a half | Verified | d ~ U(0, r); areal density ∝ 1/d
- Endpoints program piles midpoints against the rim; a third inside | Verified | exact bands 0.064 … 0.287; gold sum 1/3
- Jaynes: unaimed straws ⇒ the answer can't depend on the circle's position or size | Verified | Jaynes 1973 §1, §5–6
- Invariance board 0.25≠0.41, 0.33≠0.47, 0.50=0.50 | Verified | own 2M-line MC (table above)
- Jaynes and Charles Tyler, real (broom) straws, 5-inch (diameter) circle, 128 crossing tosses matched the radius program | Verified | Jaynes 1973 §6 (author's PDF); Eq. (13) is the uniform-distance law, equivalent to the flat histogram labelled "predicted"
- Toy classes 10/10/100: random class 40, random student 85 (tagged "example") | Verified | arithmetic above; bar and line heights measured
- Stony Brook 1974, 737 classes: random class 40, random student 147 | Verified | Feld & Grofman 1977, Res. High. Educ. 6(3):215–222 (JSTOR 40195170); 40.5·(1+65.8²/40.5²) = 147.4
- "Whatever number you picked, some way of drawing chords makes it right" | Verified (any p in [0,1]) | constructive; Jaynes 1973 §6 ("any distribution of chord lengths we please")
MECHANICS: runtime 3:33.5 · 156 wpm (speech) / 145 overall, 500 words · max silence 2.08 s (the planned "Pick a number" hold, 0:08.3–0:10.3) · max static 3.17 s (same hold) · −14.0 LUFS / −1.9 dBTP · lead 0.00 s / trail 1.54 s · WER 2.4 % (homophones, number formatting, chunk-boundary duplicates)
FIXES (highest impact first; all nitpicks, none needed for 9):
1. [2:40.4–2:51.0][Clarity, nit] During the three rains the big circle has no gold rule on screen (kf_31, 2:43.8). The big-circle number is read against an invisible rule, while the small circle's rule is bright. → During each rain, show the big circle's gold rule dashed at 30 % (it is already drawn this way in the demo at 2:34). Keep the small gold rule at 100 %, so "only one gold circle at full strength" still holds and both verdict rules stay visible while their numbers settle.
2. [2:21.0–2:29.0][Visual, nit] Before the small circle exists, the board carries "simulated", "gold share", "big", "small" (at 30 %), the four row names and the citation, about 13 words (kf_26). → Fade "small" in on the circle move (2:29, when it already lights), not at 2:21. That gives 12 words, and the column head arrives with its circle.
3. [0:51.6–0:56.5][Clarity, nit] The second program arrives with no reason to exist beyond "a second way". A viewer may think nobody would code it like that. → Within the budget, change "a random radius, a point on it" to "pick a direction, a distance from the center" (same word count). It then reads as the obvious polar-coordinates program, and the panel label "random radius point" stays the same.
4. [title, curriculum.json][Hook, nit; outside this directory] "Three Right Answers…" announces the twist before the viewer commits at 0:07. → If the publish step allows, use a title that keeps the bet open, such as "Draw a Chord at Random. What's the Chance?". The video never shows the title, so I deducted nothing.
REACHES 9 IF ALL FIXED: yes. It is at 9.0 now: every dimension is at 9, with no caps and no factual errors. Fixes 1–4 are nitpicks that would widen the margin. No structural change is needed.
KEEP:
- The SMH failure chain at 0:24–1:18: "Case closed until you code it a second way", three honest programs, ±1-point error bars, a measured 25-point gap and "the code has no bug". This is the episode's engine.
- The one unifying picture (1:19–2:17): the chord shrinks to its midpoint, the gold inscribed circle decides "long", and three midpoint scatters with histograms read 1/4, 1/2 and 1/3 off one diagram. This includes the "Where will they crowd?" pause with panels 1 and 3 dimmed and nothing moving.
- The two-circle invariance board, ending on the real 128 tosses. The demo line has "short" and "long" verdicts that check out geometrically. The class-size bookend runs from 0:17 to 3:19 to the landing.
```

## Notes on the scores

- **Hook 9.**
  - Circle, triangle and chord are on screen from frame 1 (kf_01).
  - The question is built as math by 0:07, and "Pick a number" is followed by a 2.1 s hold, so the viewer commits by 0:10.
  - The stakes land at 0:17–0:23 in the payoff's own numbers.
  - Tension rises through "Case closed…" (0:48) and the 25-point gap (1:15).
  - The landing (3:20–3:33) returns to the first frame, and the same chord now shows its midpoint inside the gold circle.
  - It is not a 10: the title pre-announces the twist, and the first frame is clean rather than irresistible.
- **Clarity 9.**
  - It is concrete first throughout.
  - Every number I recomputed or measured off the frames matches, and every source says what is claimed for it.
  - The assumption behind the 1/2 is spoken and on screen ("can't be aimed" at 2:25, "unaimed" at 3:29). The limit is stated: "some way of drawing chords makes it right".
  - In the 4 fps strip the demo verdict now holds at full strength for about 1.75 s (2:33.7–2:35.45) before the hand-off on "own", which fixes round 7's weak spot.
  - The remaining soft spot is fix 1, and it is cosmetic.
- **Visual 9.**
  - The palette holds for the whole episode: gold means long, and blue, green and purple stay with their programs.
  - Every frame has a focal point, set by dimming: 1:15, 1:54, 2:09 and 2:51.
  - There are 0 layout-audit issues. My own check of the 3:01.6 label-to-citation gap gives 24 px (0.18 units), which clears 0.15.
  - The real-versus-simulated hand-off is clean: the "simulated" tag is gone by 2:54.0, before "real" at 2:54.3.
- **Motion 9.**
  - The arc copy flies into 120°, the disk outlines fly into π(r/2)²/πr², chords collapse to midpoints, and class dots split into students while the mean line rises continuously from 40 to 85 (3:13).
  - The circle move (2:27–2:30) plays on "where the circle sits, or its size", so the motion literally shows the claim.
  - The 3:19.6–3:21.6 strip shows the Stony Brook header gone before the question fades in, with no ghosting.
- **Audio 9.**
  - 156 wpm in speech, with pauses of 0.9–1.5 s after results.
  - 7 of 7 deictics land.
  - Loudness and true peak are on target.
  - The doubled words in the transcript are Whisper chunk overlaps, as the timestamps show.
- **Concision 9.**
  - 500 words in 3:33.5. My mute test found no removable sentence.
  - "Geometry agrees…" gives the exact 1/3 that "the third we found" later cashes.
  - "Each tally is good to…" is what makes "the code has no bug" credible.
  - The toy class example is the mechanism that Stony Brook's numbers only report.
- **Originality 9.**
  - The midpoint picture is the standard modern framing.
  - The two-circle invariance scoreboard, which makes Jaynes's §5 argument a visible test, and the class-size bookend, which carries "at random" into survey data, are angles a viewer would remember and share.
