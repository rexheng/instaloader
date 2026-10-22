# Round 7 — craft critic (visual design, motion, A/V sync; all dimensions scored)

Evidence: the existing `review/` pack (metrics.json 17:38 is newer than final.mp4 17:35, so it was reused). I read report.md, all 12 contact sheets and 16 full-resolution keyframes (0:04.2, 0:41.2, 0:54.1, 1:18.6, 1:21.8, 1:45.3, 2:10.0, 2:13.0, 2:18.5, 2:33.0, 2:50.8, 3:00.0, 3:03.5, 3:13.0, 3:31.7). I also pulled about 60 extra frames with ffmpeg into /tmp/r7c: 0:47.8–0:51.0, 1:36.0–1:37.8, 1:52.4–1:55.4, 2:18.8–2:21.0 at 0.2 s, 2:28.4–2:31.2 at 0.4 s (crop), 2:29.6 at full resolution, 2:49.6–2:52.8, 3:00.0–3:01.8 at 0.2 s and 3:19.6–3:22.0. I read script.md, the transcript and the narration diff, and I re-ran the invariance board myself (2M lines per program).

```
EPISODE: 001 — "Three Right Answers to One Probability Question"
IDEA: "Pick a chord at random" has no answer until you say what is spread evenly: each program scatters chord midpoints differently around the one small circle that decides "long" (1/3, 1/2, 1/4), only the radius program survives Jaynes's can't-aim test, and the same choice makes one college's average class 40 or 147.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.8 (880/100)   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none (0 banned phrases; 0 layout-audit issues in 245 checks; no black frames; max static 3.17 s; max silence 2.08 s; runtime and pace inside the window; −14.0 LUFS / −2.0 dBTP; every empirical claim cited on screen)
FINAL: 8.8   PASS: no
FACTS:
- Inscribed triangle side = r√3; chord longer ⇔ midpoint within r/2 (incircle) | Verified | 2√(r²−d²) > r√3 ⇔ d < r/2
- Endpoints 1/3 = 120°/360° (far arc, 0:41–0:49) | Verified | inscribed-angle argument
- Radius program 1/2 = (r/2)/r; midpoint program 1/4 = π(r/2)²/πr² | Verified | exact
- Tallies 0.334 / 0.498 / 0.248 of 10,000; "good to about one percentage point" | Verified | 95 % half-width ≤ 0.98 pt at n = 10,000
- "They disagree by 25" / "25 points" | Verified | 0.498 − 0.248 = 0.250
- Endpoints histogram: last band 0.284, gold bands sum to 0.334 | Verified | (2/π)(asin 1 − asin 0.9) = 0.287 exact; facts.md sample
- Bertrand 1889, Calcul des probabilités; « Aucune des trois n'est fausse, aucune n'est exacte » | Verified | ch. I §5 (facts.md H3); narration's "none is right" is a fair gloss of "exacte"
- Invariance board: midpoint 0.25 ≠ 0.41, endpoints 0.33 ≠ 0.47, radius 0.50 = 0.50 (small circle R/2 at 0.4R) | Verified | my 2M-line run: 0.250/0.412, 0.334/0.471, 0.500/0.500 (and the same at three other offsets' directions)
- Jaynes 1973, Foundations of Physics 3(4):477–492: straws from a standing position, 5-in.-diameter circle, with C. E. Tyler, 128 successful tosses matched the uniform-distance law | Verified | §6 quotation in facts.md H7; on-screen "5-inch-wide" matches "diameter"
- Toy classes 10, 10, 100: per-class mean 40, per-student mean 85 | Verified | 120/3 = 40; 10,200/120 = 85; on-screen line heights measured at 0.40 and 0.85 of the 100 bar (3:09, 3:13)
- Stony Brook spring 1974, 737 classes, 40 per class vs 147 experienced | Verified | Feld & Grofman 1977, Res. High. Educ. 6(3):215–222 (facts.md C2; 40.5·(1+65.8²/40.5²) = 147.4)
- Landing: opening chord is long and its midpoint is inside the gold circle | Verified | measured on 3:31.7 frame: chord 663 px vs side 610 px; midpoint 116 px from centre vs r/2 = 176 px
- "Whatever number you picked, some way of drawing chords makes it right" | Verified | mixtures of chord distributions reach any share in [0, 1]
MECHANICS: runtime 3:31.7 · wpm 156 (speech) / 145 overall · max silence 2.08 s (planned "Pick a number" hold) · max static 3.17 s (same hold) · −14.0 LUFS / −2.0 dBTP · lead 0.00 s / trail 1.54 s
```

## What I checked, by dimension

**Hook (9).** The first frame (0:01) is the object itself: circle, triangle and a chord drawing. By 0:07 the question is built as math from copies of the chord and a flashed side (0:05–0:06.2 sweep), and "Pick a number" gets a 2.1 s hold (0:08.3–0:10.3), so the viewer commits before 0:11. The stakes line (0:17–0:23) previews the payoff's own numbers ("40 or 147"). The landing (3:20–3:31) restores the exact first frame, the same chord turns gold and shows its midpoint inside the gold circle, and the 0–1 line resolves "pick a number". Tension rises through build (0:24), fail ("25 points", 1:17) and the invariance test. Nothing to change here beyond nitpicks.

**Clarity (8.5).** Concrete before abstract, and the insight is the canonical one. Midpoint slides (1:21–1:25), the chord matches the side at r/2 (1:27), the incircle draws (1:29), "each program is a way of scattering midpoints" (1:35), then each panel's chords collapse to midpoints and their histograms grow (1:39–2:10). Every number checks. Two things keep it below 9.
- (a) 2:30–2:49, the invariance test. In about 19 s the viewer gets a two-circle setup, the rule that each circle judges with its own gold circle, one demo line with two verdicts, and then three rains with six numbers. The demo line (2:32.4–2:37) is the only place the "own rule" idea is read off the picture, and its verdicts are carried by colour alone: grey big chord, gold small piece. Nothing names them "short" or "long". On first viewing the board reads as "numbers differ", not as "why they must not". This is the one transition that needs a rewatch.
- (b) The honest limit is only implicit. Jaynes's answer holds for unskilled tosses ("can't be aimed", 2:23). The landing's "name the way, and the answer is fixed" covers it, but nothing says when 1/2 would be wrong. This is a nitpick, but it is the BAR's "say when the result breaks".

**Visual design (8.5).** The palette is disciplined: gold for "long" everywhere, blue, green and purple for the three programs on labels, tallies, highlights and landing fractions, and ink or grey for the rest. No red/green-only encoding. Type is large: the "random endpoints" labels are about 40 px cap height, and the tick labels and histogram captions clear the 24 px floor (the layout audit is clean). Most frames have one focal point. The 3-panel insight frames (1:45, 2:10, 2:18) are dense, with about 300 dots per panel, but they read because the others dim to 35 %. Defects:
1. **2:23–2:31, straw rain buries the focal move.** The simulated straws are drawn at about 70 % grey and accumulate to roughly 200 lines that cover the whole floor box (full-res 2:29.6). The key action of the sentence, "where the circle sits, or its size" (the circle copy shrinking and sliding off-centre), happens underneath that texture, and the small gold circle is nearly invisible in it.
2. **2:28.4–2:29.8, the gold-rule handoff breaks the episode's own "one gold circle at a time" rule and leaves a smudge.** At 2:28.4 the big gold circle and the shrinking copy are both at full gold and overlap off-centre. At 2:29.2–2:29.6 the small circle's dark halo stays visible while its gold stroke is near 0 %, and it morphs into a dark, distorted crescent inside the small circle (cropped frames, /tmp/r7c/K.png). It is dark on dark and lasts about 0.5 s, so I do not treat it as a render-artifact cap, but it is a visible blemish.
3. **2:53–3:00, the right column turns into a text stack while the real experiment has no picture.** It holds "straws ≈ radius / radius 0.50 / 5-inch-wide circle / 128 straws crossed it / radius program predicted / center … rim": five stacked text items and 13 prose words, over the §5 limit of 12. "radius 0.50" repeats what "≈ radius" and the predicted histogram already say, and the word "radius" appears three times. The left half, the actual experiment, is an empty circle. "5-inch-wide circle" duplicates the "5 in" mark already drawn under it.
4. **2:21 onward, naming and order drift.** The panels say "random endpoints / random radius point / random midpoint" in that order. The board renames them "midpoint / endpoints / radius" and reverses the order. A viewer has to remap colour to row once. This is a nitpick, because colour carries it.

**Motion & animation (9).** This is the episode's strength. Objects persist and transform with meaning:
- the gold arc copies into "120°" and the rim into "360°" (0:45–0:49);
- the big circle shrinks into panel 1 with its tally and its exact 1/3 travelling along (0:49–0:53);
- the gold circle copies out of panel 2 into all three panels (1:36.0–1:37.8);
- the chords collapse to midpoints (1:39–1:41), and the disks' outlines fly into π(r/2)² and πr²;
- the gold bars stack into the 0.334 column (2:07–2:09);
- the class dots split into students while the mean line rises 40 → 85 (3:09–3:13);
- the landing marker sweeps 0 → 1 past 1/4, 1/3 and 1/2 (3:20.8–3:22).

Reading holds are respected: the 120°/360° = 1/3 equation is up about 3.3 s, and π(r/2)²/πr² = 1/4 about 4 s. Live counters converge (0:33–0:37, 0:57–0:59, 1:05). Nitpicks:
- At 1:52.4–1:53.4 the purple equation collapses to 1/4 right on "Where will they crowd?", so the only motion during the setup of the prediction is in the wrong panel.
- At 2:51.2 the big circle's gold rule fades in while the small circle and its gold rule are still fading, and two gold circles overlap for about 0.4 s.
- At 2:19.4 there is about 0.3 s with only the travelling circle; the board text is around 10 %.

**Audio / voiceover (9).**
- Pace is 156 wpm in speech. Loudness is on target (−14.0 LUFS, −2.0 dBTP). Leading silence is 0.00 s and trailing silence 1.54 s.
- Planned holds come after the commit (2.1 s), "a third of the rim" (1.6 s), "Where will they crowd?" (1.6 s), "never said which" (1.5 s), "a half on both" (1.5 s) and "matched the radius program" (1.5 s).
- All 7 deictics land (report). On the sheets, "this arc" lights at 0:45, "this gold circle" fills at 1:33–1:35, and "this triangle" flashes its side at 0:06.
- Whisper differences are homophones or number formatting only: "Janes", "a/one", "toss straws".
- One thin turn: the fail beat's verdict, "and the code has no bug" (1:18.2), gets 0.6 s before "One point sets…", the episode's biggest turn. That is a nitpick, but it is the moment a skilled narrator would let breathe.

**Concision (9).** 500 words in 3:31.7. I tried the mute test on each beat. "Geometry agrees" is cashed later as "the third we found". The error-bar sentence is what makes "the code has no bug" credible. The survey beat pays off the 0:17 promise. I could not find a removable sentence.

**Originality (9).** The unifying picture is uncommon in treatments of Bertrand: every recipe is a way of scattering midpoints around one incircle. So is the invariance scoreboard on an off-centre half-size circle, and the class-size bridge that makes "at random" a survey-design problem, built from the same dots. No slop phrases, no stock visuals.

FIXES (highest impact first):
1. [2:23–2:31][Visual] The simulated straw rain (~200 lines at ~70 % grey, full-res 2:29.6) buries the "where it sits, or its size" move. → Keep only the newest 3–5 straws at full strength and fade every older straw to 25 % as it lands (cap the visible set at about 60). Start the circle-copy shrink and slide only when the texture is at 25 %, so the moving circle is the frame's one focal point. Expected: Visual +0.25.
2. [2:28.2–2:30.0][Visual/Motion] The gold-rule handoff shows two full gold circles (2:28.4), then a dark halo morphing into a smeared crescent (2:29.2–2:29.6). → Fade the big gold circle and the big triangle to 0 over 0.4 s *before* the copy moves. Do not Transform the small gold circle's dark halo: FadeOut the halo at the start, move the bare gold stroke, then FadeIn the halo at the destination over 0.3 s. Expected: Visual +0.25 (meets the one-gold-circle rule the episode set itself).
3. [2:53–3:00][Visual] The right column has 5 stacked text items and 13 prose words; "radius 0.50" and "5-inch-wide circle" duplicate other elements. → Delete the "radius 0.50" row, so "straws ≈ radius" sits directly above the predicted histogram. Move "128 straws crossed it" to the floor, centred just under the "5 in" mark, and delete "5-inch-wide circle" (the "5 in" mark carries it; keep "5-inch" in the narration). Result: 3 text items, 7 prose words, and the circle side of the frame has its own label. Expected: Visual to 9 together with fixes 1–2.
4. [2:32.4–2:37.0][Clarity] The demo line's two verdicts are colour-only, so the "own gold circle" rule is not read off the picture. → When the big chord turns grey, write "short" (grey, Text 22) beside it outside the small circle. When the small piece turns gold, write "long" (gold, Text 22) beside it. Hold both 1.0 s, then FadeOut with the demo line before the first rain. Add "[pause 0.6]" after "so a fair program scores the same on both." (+0.6 s, still ≤ 3:35). Expected: Clarity to 9.
5. [1:52.4–1:53.4][Motion] The purple π(r/2)²/πr² → 1/4 collapse runs during "Where will they crowd?". → Move that collapse to the 0.7 s breath after "catches a quarter" (≈ 1:47.7–1:48.4), and dim panels 1 and 3 to 40 % for the 1.6 s prediction hold (restore them on "Toward the center"), so panel 2's bare radius is the only bright thing while the viewer predicts.
6. [2:50.8–2:51.6][Motion] The big gold rule fades in while the small circle group fades out, and two gold circles overlap off-centre. → Run the two moves in sequence: small circle, small gold rule and column head out (0.35 s), then big gold rule in (0.35 s). Keep the "no frame without a gold rule" intent by letting the small gold rule leave last.
7. [1:18.2–1:18.8][Audio] Only 0.6 s after "and the code has no bug", the biggest turn in the episode. → Add "[pause 1.0]" after that sentence (+0.4 s) and start the number line's fade on the pause, so the insight beat opens on a clean breath.
8. [2:21–2:49][Visual, nitpick] The board renames and reorders the programs relative to the panels. → Use the panel names in short form, "endpoints / radius point / midpoint", or keep the rain order and add each program's tiny panel glyph (rim, radius, dot, at 40 % in its colour) left of each row name, so the row-to-panel mapping is visual, not verbal.
9. [3:22–3:31][Clarity, nitpick] The honest limit is implicit. → Under the green "1/2 straws" tag, add a one-word grey caption "unaimed" (Text 18). This is Jaynes's condition, and it says when the 1/2 breaks without adding narration.
10. [2:19.2–2:19.6][Motion, nitpick] About 0.3 s with only the travelling circle on screen (board text ~10 %). → Start the board text's FadeIn 0.25 s earlier, so it is ≥ 50 % by the time the last panel is gone.

REACHES 9 IF ALL FIXED: yes. Fixes 1–3 bring Visual to 9 and fix 4 brings Clarity to 9: (15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·9 + 10·9)/100 = 9.0, with no caps. Fixes 5–10 add margin on Motion and Audio. No structural change is needed. The hook, failure beat and visual insight are all in place.

KEEP:
- The insight sequence 1:21–2:10: midpoint slide → incircle → "each program is a way of scattering midpoints" → chords collapsing to midpoints with their histograms and equations built from the areas they measure.
- The bookend: 0:00 and 3:20–3:31 are the same circle, chord and question, and the opening chord turns gold with its midpoint visibly inside the gold circle while the 0–1 line resolves "pick a number".
- The class dots splitting into students as the mean line rises 40 → 85 (3:09–3:13), the same "what is spread evenly" picture carried into survey data.
