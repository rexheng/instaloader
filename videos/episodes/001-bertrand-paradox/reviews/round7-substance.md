# Round 7 review: substance (science and story editor)

I am an independent critic. I did not make this episode. My focus is factual and mathematical correctness, the hook and tension, clarity, concision, originality and AI slop. I still score every dimension.

**Evidence used**
- The existing `review/` pack. metrics.json (17:38) is newer than final.mp4 (17:35), so I reused it and did not regenerate it.
- I read report.md, narration_diff.txt and transcript.txt, plus all 12 contact sheets.
- I read 13 full-resolution keyframes: kf_01 0:04.2, kf_07 0:54.1, kf_11 1:10.1, kf_12 1:18.6, kf_19 1:58.6, kf_23 2:13.0, kf_25 2:22.2, kf_31 2:50.8, kf_34 3:00.0, kf_35 3:03.5, kf_38 3:15.3 and kf_40 3:31.7.
- I extracted frames of my own with ffmpeg:
  - single frames at 2:32.8, 2:33.8, 2:34.6, 2:35.4 and 2:36.4;
  - a 5 fps zoom of 2:32.9–2:35.3;
  - 4 fps sweeps of 0:47.8–0:50.8, 1:35.4–1:38.4, 2:17.8–2:20.8, 2:59.6–3:02.6 and 3:17.6–3:20.6;
  - a 10 fps zoom of 3:18.7–3:19.5.
- I read script.md, narration.txt and facts.md in full, and the round-6 CHANGELOG.

## Independent recomputation

I wrote my own Monte Carlo (not sim.py), with 2,000,000 lines per program. The small circle has radius R/2 and its centre sits 0.4 R from the big centre. Each line is judged by its distance from each circle's centre, and the small-circle share is conditioned on the line crossing the small circle.

| program | big circle | small circle | on screen (2:41–2:51) |
|---|---|---|---|
| radius | 0.4995 | 0.4999 | 0.50 = 0.50 |
| midpoint | 0.2503 | 0.4111 | 0.25 ≠ 0.41 |
| endpoints | 0.3328 | 0.4702 | 0.33 ≠ 0.47 |

**Formulas, re-derived**
- The side of the inscribed triangle is 2r sin 60° = r√3.
- A chord of length L = 2√(r² − d²) is longer than r√3 exactly when d < r/2, and r/2 is the triangle's inradius.
- The far arc is 120°/360° = 1/3.
- The radius program gives (r/2)/r = 1/2.
- The midpoint program gives π(r/2)²/πr² = 1/4.

**Endpoint-program midpoint bands, exact:** 0.064 0.064 0.066 0.068 0.071 | 0.076 0.084 0.097 0.123 0.287. On screen, the last bar measures about 27 % against the 10 % dashed line (2:05), and the stacked gold column measures 0.33 of the bar scale (2:13, kf_23).

**Error bars:** 95 % half-widths at n = 10⁴ are 0.92, 0.98 and 0.85 points. Measured in kf_12, the on-screen bars are ±0.0086, ±0.0094 and ±0.0097, so "good to about one percentage point" holds. The tallies differ by 0.498 − 0.248 = 0.250, which is the "25 points" on screen.

**Classes**
- Per-class mean: (10 + 10 + 100)/3 = 40.
- Per-student mean: (10² + 10² + 100²)/120 = 85.
- On screen, the 40 and 85 lines sit at the right heights against the 100 bar (3:09 and 3:13).
- Stony Brook: 40.5 × (1 + 65.8²/40.5²) = 147.4, which matches the 147.

**Landing number line (kf_40):** 0 is at x = 1061 px and 1 is at x = 1762 px. The dots at 1236, 1294 and 1411 px read 0.250, 0.332 and 0.499. The opening chord's midpoint is 115 px from the centre, which is 0.33 r, inside the 0.5 r gold circle. So turning that chord gold is correct.

**Citations, verified by web search this round**
- **Bertrand 1889.** *Calcul des probabilités*, Gauthier-Villars, which gives the quote « Aucune des trois n'est fausse, aucune n'est exacte ». Confirmed via arXiv 1504.01361 (D'Agostini) and Malo 2021, citing p. 5.
- **Jaynes 1973.** "The Well-Posed Problem", *Foundations of Physics* 3(4):477–492. Confirmed via Inspire-HEP and PhilPapers (which gives the end page as 493). The author's PDF (bayes.wustl.edu) §6 reads: "…Tyler, tossing broom straws from a standing position onto a 5-in.-diameter circle … 128 successful tosses confirmed Eq. (13)".
- **Feld & Grofman 1977.** "Variation in class size, the class size paradox, and some consequences for students", *Research in Higher Education* (JSTOR 40195170; ResearchGate 227135568). The 40 and 147 figures were checked against facts.md's page-cited quotes.

---

```
EPISODE: 001 — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly: every recipe is a way of scattering chord midpoints around the one small circle that decides "long" (1/3, 1/2, 1/4); an unaimed physical toss (Jaynes) picks 1/2, and the same choice makes one college's average class 40 or 147.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 9.0 (900/100)   AFTER CEILING: 9.0 (lowest 9 + 2 = 11, not binding)
CAPS: none. 0 banned phrases or patterns (my own scan of narration.txt: the only hit, "enter:", is "center:" at 1:55); 0 factual errors; every empirical claim carries an on-screen citation (Bertrand 0:13–1:13, Jaynes 2:21–2:59, Feld & Grofman 3:03–3:19); 0 layout-audit issues; mechanics all inside the bar.
FINAL: 9.0   PASS: yes (no margin: any single half-point drop fails it)
FACTS:
- Bertrand posed the chord puzzle in 1889 (Calcul des probabilités) | Verified | arXiv 1504.01361; Malo 2021 (p. 5); Gauthier-Villars 1889 title page per facts.md H1
- "As a warning about two words, at random" | Verified (fair paraphrase) | Bertrand ends the section "la question est mal posée"; Jaynes 1973 summarises: ill posed, "the phrase 'at random' being undefined"
- "Bertrand printed all three, writing that none is wrong and none is right" + on-screen French quote (1:09–1:16) | Verified, verbatim | « Aucune des trois n'est fausse, aucune n'est exacte » (sentence continues "la question est mal posée")
- Two random rim points; with a vertex on the first point the chord is long iff the second lands on the far 120° arc = 1/3 | Verified | re-derived; 120°/360° = 1/3 on screen 0:47–0:49
- Simulated tallies 0.334 / 0.498 / 0.248 from 10,000 chords each, labelled "simulated" | Verified (consistent with exact 1/3, 1/2, 1/4 within 1 s.e.) | own MC; error bars measured in kf_12
- "Each tally is good to about one percentage point" | Verified | 95 % half-widths 0.85–0.98 pts
- "They disagree by 25" / on screen "25 points" | Verified | 0.498 − 0.248 = 0.250
- "One point sets a chord's length, its midpoint"; matches the side at half a radius, on the triangle's inscribed circle | Verified | L = 2√(r²−d²); inradius = r/2
- Midpoint program: a quarter of the area catches a quarter, π(r/2)²/πr² = 1/4 | Verified | re-derived
- Radius program: equal share per ring, so midpoints crowd the centre; (r/2)/r = 1/2 | Verified | density of d uniform; areal density ∝ 1/d
- Endpoints program piles midpoints against the rim; only a third land inside | Verified | exact bands above; last band 0.287
- Jaynes: a physical process picks one; unaimed straws ⇒ the answer can't depend on the circle's position or size | Verified | Jaynes 1973 §1, §5–6
- Invariance board 0.25≠0.41, 0.33≠0.47, 0.50=0.50 | Verified | own 2M-line MC (table above)
- Jaynes and Charles Tyler, real (broom) straws, 5-inch(-diameter) circle, 128 crossing tosses matched the radius program | Verified | Jaynes 1973 §6, "128 successful tosses confirmed Eq. (13)"; Eq. (13) is the uniform-distance law, equivalent to the flat histogram shown and labelled "predicted"
- Toy classes 10/10/100: random class 40, random student 85 (tagged "example") | Verified | arithmetic above
- Stony Brook 1974, 737 classes: random class 40, random student 147 | Verified | Feld & Grofman 1977, Research in Higher Education 6(3):215–222 (JSTOR 40195170); 40.5·(1+65.8²/40.5²) = 147.4
- "Whatever number you picked, some way of drawing chords makes it right" | Verified (for any p in [0,1]) | constructive; Jaynes 1973 §6 ("any distribution of chord lengths we please")
MECHANICS: runtime 3:31.7 · wpm 156 (speech) / 145 overall, 500 words · max silence 2.08 s (planned "Pick a number" hold, 0:08.3–0:10.3) · max static 3.17 s (same hold) · −14.0 LUFS / −2.0 dBTP · lead 0.00 s / trail 1.54 s · WER 2.0 % (homophones and number formatting only)
FIXES (highest impact first):
1. [2:33.4–2:34.8][Motion/Clarity] The demo line is the only frame that shows "same line, two verdicts". In the 5 fps zoom, the big circle's dashed gold rule is visible for about 1.4 s in total, and at full strength only from about 2:33.5 to 2:34.3, before the cross-fade hands over to the small circle. That is under the §5 reading hold of ≥ 1.5 s, at the moment the viewer has to compare a grey line with a dashed circle. → Hold the dashed big rule plus the grey big chord at full strength for ≥ 1.5 s, starting on "Each judges". Start the 0.5 s cross-fade on "own", not before it. If needed, take the 0.4 s from the 1.3 s post-row hold after the midpoint rain.
2. [2:30.7–2:33][Clarity] The word "rain" is never defined in the narration (0:33 says "10,000 chords in"). It is spoken first at 2:30.7 ("One rain lands on both circles"), while the simulated straws are still falling. The viewer can take "one rain" to mean the straws, but the next sentence and the board are about the three programs. → Change the line to "One program's rain lands on both circles", which adds one word. Alternatively, start the straws' fade 0.5 s earlier, so the first program's demo line is already on the floor when "rain" is said.
3. [2:57–3:00][Visual] The right column holds five text items: "straws ≈ radius", "radius 0.50", "5-inch-wide circle", "128 straws crossed it" and "radius program *predicted*". With the citation that makes about 16 prose words, over the §5 load of 12. "radius 0.50" also repeats what "≈ radius" and the predicted histogram already say. → Fade the "radius 0.50" row on "matched", at the moment "?" becomes "≈ radius". The column then carries four items, and the green row's job passes to the histogram title.
4. [3:19.0–3:19.3][Visual] At 10 fps the cross-dissolve shows the outgoing "Stony Brook, 1974" header (about 15 % opacity) printed over the incoming "P( — > — ) = ?". The block's vertical rule also crosses the "- - - random class" dash as the rows step down. It lasts about 0.2–0.3 s. → Fade the Stony Brook header and vertical rule fully out (0.25 s) before the question starts fading in, or move the header up and out with the rule.
5. [1:55–2:17][Visual, nit] There are 13 prose words on screen: three recipe labels (7 words) plus "share of midpoints, by distance from center" (6), against the 12-word load. → Drop "share of" from the histogram title ("midpoints by distance from center"). It still names the quantity, and the count falls to 11.
6. [3:26.4][Audio, nit] Whisper hears "for toss straws", so the "-ed" of "tossed" merges into the "s" of "straws" (Kokoro). → Use "a half for straws tossed by hand". It adds one word, and the participle no longer runs into a sibilant. Re-check the clip with Whisper.
7. [title, curriculum.json][Hook, nit; outside this directory] The title "Three Right Answers…" announces the twist before the viewer commits at 0:07. → If the publish step allows, use a title that keeps the bet open, such as "Draw a Chord at Random. What's the Chance?". The video itself never shows the title, so I deducted nothing for it.
REACHES 9 IF ALL FIXED: yes. The episode is at 9.0 now, with every dimension at 9 and no caps. Fixes 1–2 are the only ones that touch comprehension, and they would widen the margin. Fixes 3–7 are nitpicks.
KEEP:
- The SMH failure chain at 0:24–1:18: "Case closed until you code it a second way", three honest programs, error bars of ±1 point, a measured 25-point gap and "the code has no bug". This is the episode's engine; do not shorten it.
- The single unifying picture: the chord shrinks to its midpoint, the gold inscribed circle decides "long", and three midpoint scatters with their histograms read 1/4, 1/2 and 1/3 off one diagram (1:18–2:17), including the "Where will they crowd?" prediction pause.
- The two-circle invariance board ending on the real 128 tosses, and the class-size bookend (stakes at 0:17, toy at 3:03, Stony Brook at 3:15, landing at 3:31). It turns a classic puzzle into a data-science lesson about what "at random" weights.
```

## Notes on the scores

- **Hook 9.**
  - The circle, triangle and chord are on screen in the first frame.
  - "Pick a number" at 0:07, with a 2.1 s hold, makes the viewer commit by 0:10.
  - The stakes land at 0:17, in the payoff's own numbers ("40, or 147").
  - Tension rises through "Case closed" at 0:48 and the 25-point gap at 1:15, and the landing returns to the first frame, which now reads "whatever number you picked…".
  - It is not a 10: the title pre-announces "three right answers", and the opening frame is clean but not irresistible.
- **Clarity 9.**
  - Concrete comes before abstract throughout: one simulation, then the geometry, then the general midpoint picture.
  - Every number checks out against my own recomputation, and every source matches what is claimed for it.
  - The assumption behind 1/2 is stated ("can't be aimed"), and so is the limit ("some way of drawing chords makes it right").
  - The one soft spot is the 2:30–2:51 invariance beat: an undefined "rain", a big-circle verdict held for 1.4 s, then six numbers in about 10 s. It is the payoff rather than the core derivation, so I kept 9; fixes 1–2 address it.
- **Visual 9.**
  - The semantic palette holds for the whole episode: gold means long, and blue, green and purple stay with their recipes.
  - Dimming gives each frame its focal point: the stack at 2:07, the tallies at 1:17, and the right column at 2:51.
  - There is no clipping, and the safe area is respected: the top labels are at y ≈ 3.42.
  - The remaining items are word-load overages by 1–4 words and a 0.2 s dissolve ghost. These are nitpicks.
- **Motion 9.**
  - Every move carries information: the arc copy flies into 120°, the disk outlines fly into π(r/2)²/πr², and chords collapse to midpoints.
  - In the class beat, the class dots split into students while the mean line rises continuously from 40 to 85.
  - There are 0 glyph morphs.
  - The one rushed hold is fix 1.
- **Audio 9.**
  - 156 wpm in speech, with shaped pauses of 0.9–1.5 s after results.
  - All 7 of 7 deictics land.
  - Loudness and true peak are on target.
  - "Janes" is Whisper's homophone spelling of /ʤeɪnz/, not a mispronunciation.
- **Concision 9.**
  - The 500 words fill 3:31.7.
  - Each sentence passed my mute test. The candidates I tested were "Geometry agrees…", "Each tally is good to…" and the toy class example, and each carries a step that the next beat uses.
- **Originality 9.**
  - The midpoint picture itself is the standard modern framing.
  - Two things lift it: the two-circle invariance scoreboard, which makes Jaynes's argument a visible test, and the class-size bookend, which carries "at random" into survey data. Both are angles a viewer would remember and share.
