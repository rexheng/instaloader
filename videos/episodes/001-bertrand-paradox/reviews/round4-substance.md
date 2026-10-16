# Round 4 review: substance (science and story editor)

Reviewer role: independent science editor and story editor. My emphasis is factual and mathematical correctness, the hook and narrative tension, clarity, concision, originality and AI slop. I still score every dimension.

**Evidence used**
- The existing `review/` pack. metrics.json (23:40) is newer than final.mp4 (23:38), so I reused it.
- From the pack: report.md, narration_diff.txt, transcript.txt and transcript_words.tsv (I recomputed local speech rates from it).
- All 13 contact sheets.
- 13 full-resolution keyframes: kf_02 (0:13.9), kf_07 (0:55.3), kf_12 (1:25.1), kf_18 (1:54.0), kf_19 (2:04.7), kf_22 (2:20.2), kf_26 (2:33.8), kf_31 (2:59.9), kf_34 (3:15.9), kf_36 (3:22.3), kf_38 (3:31.7) and kf_40 (3:51.3).
- Extra full-resolution frames I pulled with ffmpeg at 2:46.5, 3:02.0 and 3:17.5.
- Episode files: script.md, narration.txt and facts.md.

**Independent checks**
- **Invariance scoreboard.** I re-simulated it with my own code: 2,000,000 lines per program, judged on the big circle and on a circle of radius R/2 centred 0.4 R off-centre.

  | program | big circle | small circle |
  |---|---|---|
  | midpoint | 0.2502 | 0.4114 |
  | endpoints | 0.3338 | 0.4712 |
  | radius | 0.5003 | 0.5004 |

  The board's 0.25/0.41, 0.33/0.47 and 0.50/0.50 are correct.
- **Class sizes.** (10+10+100)/3 = 40. (10²+10²+100²)/120 = 10,200/120 = 85. Stony Brook's paper figures are consistent: 40.5·(1 + 65.8²/40.5²) = 147.4.
- **1/3, 1/2, 1/4.** I re-derived all three. The chord-length rule is L = 2√(r² − d²) > r√3 ⇔ d < r/2, and r/2 is the inradius.
- **Endpoint-recipe histogram.** The midpoint-distance density is (2/π)/√(r² − d²), which puts 0.287 in the last band (shown: 0.284).
- **"Good to about one percentage point."** The 95 % half-widths are 1.96·√(p(1−p)/10⁴) = 0.92, 0.98 and 0.85 points.
- **"25 points."** 0.498 − 0.248 = 0.250.
- **Jaynes's chord-length law.** The radius program's chord-length density is f(L) = L / (2R√(4R² − L²)), which integrates to 1 on [0, 2R]. "Matched the radius program's spread of chord lengths" is the right description of what Jaynes and Tyler tested.
- **Citations.** I checked all three by web search; see FACTS.

```
EPISODE: 001-bertrand-paradox — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly: each recipe scatters chord midpoints differently around the one small circle (radius r/2) that decides "long", giving 1/3, 1/2 or 1/4. A stated physical process (unaimed straws, Jaynes) picks one, and the same choice (random class vs random student) turns 40 into 147 in real survey data.
SCORES: Hook 8.5 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.7  (127.5 + 225 + 127.5 + 127.5 + 85 + 85 + 90 = 867.5 / 100 = 8.675)   AFTER CEILING: 8.7  (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none. No fabricated or wrong claim. Voiceover is present and in sync. No placeholder or debug text. 0 banned phrases. No bullet slide. Hook lands at 0:02.8–0:07.5. Longest silence 1.92 s. Longest static stretch 3.0 s. Runtime and pace are within limits. Loudness is on target. Every empirical claim carries an on-screen citation.
FINAL: 8.7   PASS: no
FACTS:
- Bertrand published the chord puzzle in 1889 (Calcul des probabilités, Gauthier-Villars, ch. I §5) | Verified | archive.org scan; secondary sources quote the passage
- « Aucune des trois n'est fausse, aucune n'est exacte » = "none is wrong, and none is right" | Verified (verbatim; the sentence continues "la question est mal posée") | web search, multiple sources quoting p. 5
- "a warning about two words: at random" | Verified as a paraphrase (Bertrand: the question is ill-posed; Jaynes 1973 summarises it as "the phrase 'at random' being undefined") | Jaynes 1973 §1
- Recipe 1 (random endpoints) → 1/3 via the 120° far arc | Verified | re-derived; sim 0.334
- Recipe 2 (random radius point) → 1/2 | Verified | re-derived; sim 0.498
- Recipe 3 (random midpoint) → 1/4 = π(r/2)²/πr² | Verified | re-derived; sim 0.248
- "Each tally is good to about one percentage point" | Verified | 95 % half-widths 0.85–0.98 points
- "They disagree by twenty-five percentage points" | Verified | 0.498 − 0.248
- "One point sets a chord's length: its midpoint"; long ⇔ midpoint inside the incircle (half a radius out) | Verified | L = 2√(r² − d²)
- Histogram shapes: midpoint even over area, radius flat in distance, endpoints piled at the rim (last band 0.284) | Verified | (2/π)(asin 1 − asin 0.9) = 0.287
- Jaynes 1973: unaimed straws ⇒ answer invariant to the circle's position and size | Verified | E. T. Jaynes, "The Well-Posed Problem", Foundations of Physics 3(4):477–492 (bayes.wustl.edu/etj/articles/well.pdf), §1, §5–6
- Board values midpoint 0.25 ≠ 0.41, endpoints 0.33 ≠ 0.47, radius 0.50 = 0.50 | Verified | my 2M-line simulation, numbers above
- Jaynes and Charles (E.) Tyler tossed broom straws at a 5-inch(-diameter) circle; the 128 that crossed it matched the radius program's chord-length law | Verified | Jaynes 1973 §6: "128 successful tosses confirmed Eq. (13) with an embarrassingly low value of chi-squared"
- "A skilled tosser could produce other answers" | Verified | Jaynes 1973 §1 ("various results could be obtained at will")
- Toy classes 10, 10, 100 → 40 per class, 85 per student | Verified | arithmetic above; tagged "example" on screen
- Stony Brook 1974: 40 per random class, 147 per random student (737 classes) | Verified | Feld & Grofman 1977, Research in Higher Education 6(3):215–222 (JSTOR 40195170; ResearchGate record); mean 40.5, SD 65.8 ⇒ 147.4
- "Whatever number you picked, some way of drawing chords makes it right" | Verified | any p ∈ [0,1] is reachable by choosing the midpoint-distance distribution; Jaynes §6 ("any distribution of chord lengths we please")
MECHANICS: runtime 3:51.3 · 161 wpm (speech time; 152 overall) · max silence 1.92 s · leading 0.00 s / trailing 1.81 s · max static 3.0 s · −14.0 LUFS / −1.6 dBTP
FIXES (highest impact first):
1. [3:16.5–3:29.5][Visual + Motion] The survey beat is the weakest stretch, for three reasons. First, it opens on a near-empty frame: an italic "at random" at x ≈ 290–605 px, mid-height, plus the citation (frame 3:17.5). That is not where the phrase lived in the stakes beat (under the question, x ≈ 1300–1550 px, 0:15–0:21), so the "same two words" callback does not read as the same object. Second, the toy chart is then built left-anchored (x ≈ 130–780 px), leaving the right 60 % of the frame empty for ~10 s (kf_36 3:22.3). Third, the class dots appear from nothing, although the script says they are "the same picture as the chord midpoints". → (a) Write "at random" at exactly the stakes-beat mobject's position and scale (store it at 0:15 and `.copy()` its center), then move it to the caption slot. (b) Build the toy chart centred on x = 0. On "At Stony Brook" (3:29.4), in the same AnimationGroup that dims it, `chart.animate.shift(LEFT*3.3)` to make room for the Stony Brook block. (c) On "Surveys hide the same two words", collapse the skilled-tosser floor's chords to their midpoints (reuse the 1:49 collapse), then `Transform` that dot cloud into the three class dots on "Pick a class at random" (3:22.1). This lifts Visual and Motion toward 9.
2. [3:00.1–3:11.4][Clarity + Hook] The climax is under-shown. The real experiment, the moment the "?" is answered by data, is shown only as two text lines ("5-inch circle", "128 straws crossed it") beside a dimmed *simulated* floor that keeps its "simulated" tag (frame 3:02.0, kf_33). A viewer cannot see what "matched the radius program's spread of chord lengths" means, and may read the flagged "radius 0.50" row as the real tosses' share, which the paper never reports. → On "spread of chord lengths", replace the dimmed floor with the radius program's chord-length curve f(L) = L/(2R√(4R²−L²)) on 0…2R (x axis "chord length", ten outlined bins to echo Jaynes's ten categories, all in green), titled "radius program: chord lengths". Put the label "128 real tosses: matched (Jaynes 1973)" beside it. Then turn the straws row's "?" into a green "≈ radius" (a word, not a number, so no unpublished data is implied). This shows the real evidence. It also resolves the episode's open "?" on screen rather than in the narration only.
3. [2:28.8–2:43.4][Clarity + Audio] The invariance premise is compressed into one 14 s run-on sentence, transcribed with no internal punctuation ("...picks one straws tossed from a standing height can't be aimed so the answer can't depend on where the circle sits or how big it is one rain lands..."). "Jaynes said" is also heard as "Jane said" (2:30.9, s–s merge). This premise carries the whole second act, and it needs a breath. → In narration.txt, replace it with: "In nineteen seventy-three, Edwin Jaynes argued that a physical process picks one. [pause 0.4] Straws tossed from a standing height can't be aimed, so they can't treat a small circle differently from a big one." Then keep "One rain lands on both circles at once…" unchanged. The word count is about the same, it gains a pause, it removes the merge, and "argued" is the accurate verb.
4. [2:41–3:00][Visual] The demo and rain frames carry two pieces of residue: the big triangle at ~30 % (frame 2:46.5) and the big circle's gold incircle at ~20 %. That incircle ring crosses the small circle and its own gold incircle (kf_31 2:59.9), so the eye sees three gold-ish rings where the argument needs two. → Fade the big triangle out inside the 2:39–2:41 shrink-and-slide. Dim the big incircle to ≤ 10 % (or remove it) for 2:41–3:00, and restore it at 3:00.1 when the small circle leaves.
5. [0:00 / title][Hook] The title "Three Right Answers to One Probability Question" gives the twist away before the viewer commits at 0:07, which blunts the "Pick a number" commitment and the 0:47 "Case closed…" turn. → Retitle so it keeps the question open, e.g. "Draw a Random Chord. What Are the Odds It's Long?" The thumbnail can carry 1/3 · 1/2 · 1/4 as the intrigue.
6. [2:17–2:29][Visual] The stacked "0.334" column sits at x ≈ 90–123 px (kf_22 2:20.2), outside the 96 px title-safe edge, and pushes the left histogram off-centre against the other two. → Place the column right of the endpoints histogram (after the "r" tick, buff 0.35), or shift that histogram group RIGHT by 0.45 units for the beat.
7. [1:21–1:25][Visual] "25 points" sits ~22 px directly under the green "0.498" (kf_12 1:25.1), so it reads as a caption of the radius tally rather than the brace's measurement. → Raise the tally row 0.25 units for the Fail beat, or set the brace label at MathTex 34 with buff 0.08, so it keeps ≥ 0.3 units clearance from the tallies.
8. [3:38–3:49][Concision] "Forty and a hundred forty-seven" is spoken at 3:29–3:38 and again at 3:45–3:49. → Keep the bookend but shorten the last line to "Both are right, once you say who's picked." That saves about 1.5 s and lets the final frame hold on the gold chord. Still flag the 40/147 rows on "Both".
9. [3:48.6–3:49.4][Visual] The scale flag on "random student" brings it to ~10 px from "147". → Flag with colour (`set_color(GOLD)` and back, 0.8 s), not scale.
REACHES 9 IF ALL FIXED: yes. Fixes 1, 4, 6, 7 and 9 lift Visual to 9, and fix 1(c) lifts Motion to 9. Fix 3 lifts Audio to 9, and fixes 2 and 5 lift Hook to 9. That gives 135 + 225 + 135 + 135 + 90 + 85 + 90 = 895 → 9.0 (8.95), so it is borderline on its own. Fix 8 (Concision 9) adds the margin: 900 → 9.0. No structural change is needed. The misconception → three programs → midpoint picture → invariance test → real data → bookend spine is right, every number is correct, and the remaining defects are local.
KEEP:
- The midpoint pivot and its derivations: chords collapsing to their midpoints with live histograms; π(r/2)²/πr², (r/2)/r and the stacked gold bars built from the picture; gold = "long" held from 0:30 to 3:51.
- The two-circle invariance scoreboard: one rain, two verdicts, the one-line "judged twice" demo, the "? = ?" straws row, rows filling with breaths and the failed rows dimming (2:41–3:00).
- The bookend: P(── > ──) = ? built from the chord and the side at 0:03–0:07, returning at 3:39 with the marker sweep, the "straws" tag on 1/2, and the opening chord turning gold with its midpoint inside the incircle (kf_40).
```

## Notes by dimension

**Hook 8.5.** The first frame is the object: circle, triangle and chord, with no title card (kf_01, sheet 1). The question is built as math from the two segments by 0:07, and "Pick a number" is followed by a 1.9 s hold (0:07.7–0:09.6). Tension turns twice, at "Case closed, until you code it a second way" (0:46.7) and at "none of the code has a bug" with the 25-point gap measured (1:23). The Jaynes act then adds a real reversal: one answer *is* physically right. The ending re-sees the first frame (3:39–3:51). Three things hold it below 9:
- The title gives the three-answer twist away before the viewer commits (fix 5).
- "Every survey and every simulation has to decide what they mean" (0:16.9) stays abstract until 3:16.
- The second act's climax, the real tosses, is told rather than shown (fix 2).

**Clarity 9.** Concrete comes before abstract throughout. The 1/3 is derived from the 120° arc flying into 120°/360°. The midpoint pivot ("One point sets a chord's length", 1:25) is shown by sliding the midpoint until the chord sits on the triangle's side at r/2 (1:35, sheet 6). All three answers are then read off one picture with measured histograms (kf_22). I could re-derive 1/3, 1/2 and 1/4 after one watch. Every number I recomputed checks out, the assumptions are stated (unaimed straws, a circle small compared with the toss), and the limit is shown and tagged simulated (the skilled tosser, kf_34). The invariance step (2:28–3:00) is the one place a general viewer may need a rewatch. It is defensible at 9 only because the one-line demo at 2:46 (frame 2:46.5) makes "judged on both circles" concrete. Fixes 2 and 3 would make it airtight.

**Visual 8.5.** The semantic palette is disciplined:
- Gold means "long".
- Blue, green and purple mean the three recipes.
- Grey is neutral.
- One flat background throughout.

Type sizes are generous (panel labels about 45 px cap, citations about 28 px). Citations are bottom-left and held for whole beats. What keeps it below 9:
- The survey-beat composition: the near-empty frame at 3:17.5, then a 10 s right-hand void (kf_36).
- Residue in the invariance frames (frame 2:46.5, kf_31).
- The edge-hugging 0.334 column (kf_22).
- The ambiguous "25 points" placement (kf_12).
- The histograms carry no y-scale. The caption "share of midpoints, by distance from center" and the 0.334 label carry the meaning, so this is a nitpick.

**Motion 8.5.** The best transforms in the episode encode real relations:
- The gold arc → 120°.
- The disk outlines → π(r/2)²/πr².
- Chords collapsing to midpoints.
- The class bars widening to student-width while the mean line rises continuously from 40 to 85 (3:27, "random student 71" mid-move on sheet 12).

The survey beat's entrance is a fade to almost nothing plus a fresh Write (3:16.5–3:19.5). The class dots also pop in rather than inheriting from the chord midpoints the script says they rhyme with (fix 1c).

**Audio 8.5.** The levels are on target: 161 wpm in speech, −14.0 LUFS, −1.6 dBTP, 0.00 s leading and 1.81 s trailing silence. The deictics land within ±2 s: "this far arc" (0:43.5) against the arc at 0:45, "this gold circle" (1:43) and "rim" (2:24) against the blue rim highlight (sheet 9). The prediction pause after "Where will they crowd?" is intentional (2:04.1–2:05.7). Two issues remain:
- The 14 s run-on at 2:28.8–2:43.4 has no breath at the sentence boundary ("…picks one straws tossed…"), and "Jaynes said" merges to "Jane said" (fix 3).
- The "cord" and "Janes" transcriptions are homophones, not mispronunciations.

**Concision 8.5.** There are 585 words in 3:51, close to the 4:00 limit, and nearly every sentence earns its place. Examples that stay: "Geometry agrees" sets up "Case closed", the one-point error bars make the failure measurable, and the skilled tosser is the honest limit. The back 35 % carries two payoffs (Jaynes, then surveys). Both are justified, but 40/147 is spoken twice within 20 s (3:29–3:38 and 3:45–3:49). Fix 8 trims it.

**Originality 9.** Bertrand's chord problem is well covered; Numberphile made a 2016 video on it with Grant Sanderson. Three things here are not standard: the unification of all three answers as midpoint distributions around one gold circle with live histograms; the two-circle invariance scoreboard, a visual argument I have not seen elsewhere; and the bridge to the class-size paradox with real Stony Brook numbers. The voice is specific and dry ("Case closed, until you code it a second way", "none of the code has a bug"). I found 0 banned phrases and no rhetorical-question chains (the questions at 0:02.8 and 2:02.7 stand alone). There are no "not just X" constructions and no recap ending.
