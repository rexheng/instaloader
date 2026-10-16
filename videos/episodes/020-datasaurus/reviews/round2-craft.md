# Episode 20, review round 2 (craft critic: visual design, motion, A/V sync)

**Evidence.** I used the `review/` pack, since metrics.json (13:34) is newer than final.mp4 (13:32). I read:
- report.md and all 12 contact sheets;
- transcript.txt and transcript_words.tsv;
- narration_diff.txt, script.md, facts.md and CHANGELOG.md.

Full-resolution keyframes I read: kf_01 (0:03.5), kf_04 (0:21.1), kf_08 (0:35.0), kf_11 (0:46.2), kf_14 (0:53.1), kf_16 (1:18.2), kf_18 (1:26.1), kf_20 (1:39.3), kf_24 (2:01.4), kf_26 (2:11.4), kf_33 (2:46.5), kf_35 (3:07.3) and kf_36 (3:16.7).

Extra frames I extracted with ffmpeg into /tmp/ep20r2: 0:00.05, 0:13.0, 0:44.5, 0:59.3, 2:38.5, 2:39.0, 2:58.6, 2:59.0, 2:59.6, 3:00.2, 3:00.8, 3:01.4, 3:17.5, 3:18.2 and 3:29.5. I also used:
- a 3× zoom of the s_x label at 3:07.3;
- a pixel-extent measurement of kf_35;
- a 4 fps frame-difference trace over 2:01–2:16.

I recomputed all 13 Datasaurus sets from datasaurus_dozen.tsv: means, SDs, r and the y median.

```
EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"
IDEA: Two means, two SDs and a correlation fix exactly one ellipse (centre, box, and where it touches the side walls), so every shape sharing that ellipse (a star, the Datasaurus Dozen, Anscombe's quartet) shares the five numbers and even the best-fit line; only a plot shows the shape.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.4   AFTER CEILING: 8.4 (lowest 8 + 2 = 10, not binding)
CAPS: Text overlapping another element → 7. At 3:00.8–3:08.5 (settled layout, about 8 s; kf_35 at 3:07.3, zoomed) the "s_x" run label sits directly on the lower arc of the yellow ellipse. A background-coloured patch erases about 25 px of the ellipse stroke under the glyphs, so the episode's central object shows a visible break exactly where the derivation is landing. BAR §5: "keep ≥ 0.15 units between text and any other object. Overlaps are never allowed." This is not a transient mid-transform frame.
  Checked and not triggered:
  - No banned phrases or patterns. "Picture the scatterplot" is an instruction, not "picture this".
  - Only one deictic miss (3:09, below), so the ≥ 2 sync cap does not apply.
  - All empirical claims carry an on-screen citation.
  - No black or empty frames. The longest static stretch is 3.5 s, a planned prediction hold.
  - Loudness and peak are on target.
FINAL: 7.0   PASS: no
FACTS:
  Dinosaur n = 142; x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified (my numpy: 54.263, 47.832, 16.765, 26.935, −0.0645; shown truncated "as published", and the note is on screen at 0:49) | datasauRus TSV; Matejka & Fitzmaurice 2017
  All 13 Dozen sets share the five numbers to the first two decimals | Verified (recomputed; e.g. x_shape ȳ 47.8397 → 47.83) | datasauRus TSV
  Datasaurus drawn by Alberto Cairo, 2016 | Verified | Cairo, The Functional Art (Aug 2016); paper acknowledgements
  703 physiology papers; 86 % bar graphs; 13 % showed points | Verified (85.6 %, 13.4 % univariate scatterplots, n = 703) | Weissgerber et al. 2015, PLoS Biol 13(4) e1002128
  Version-one star: centre (50, 50), s_x 20.51, s_y 20.50 (−24 %, "almost a quarter"), r 0.00 | Verified (our construction; on-screen values match facts #4) | computed
  Means = balance point; SDs = box; r sets the side-wall touch at ȳ + r·s_y; r → 1 moves it to the corner | Verified (1-SD covariance ellipse) | derivation
  Translate, scale and shear each fix only their own numbers; the fixed star matches exactly | Verified (affine invariance; counter 0→2→4→5 at 1:41–1:49) | derivation
  Median y: dinosaur 46.02 vs star 52.16, "misses by six" | Verified for the dinosaur (46.026). The star value is from facts #11; I cannot recompute our star from the data files | computed
  Matejka & Fitzmaurice 2017, CHI: random nudges biased toward a target, kept only if the stats hold to 2 dp; works for any statistic; 12 shapes from the dinosaur | Verified | CHI 2017 pp. 1290–1294, doi:10.1145/3025453.3025912
  Anscombe 1973: 11 points per set, r = 0.82, all four share the five numbers | Verified | The American Statistician 27(1):17–21
  OLS slope = cov/s_x² = r·s_y/s_x = 0.82 × 2.03 / 3.32 ≈ 0.50; the line passes through the centre and the right-wall touch point | Verified (0.5001) | derivation
MECHANICS: runtime 3:30.1 · wpm 159 (speech time) · max silence 1.98 s (1:38.2, planned) · max static 3.5 s (1:36.7–1:40.2, planned prediction hold) · −14.0 LUFS / −1.6 dBTP · lead 0.00 s / trail 1.85 s
FIXES (highest impact first):
1. [3:00.8–3:08.5][Visual] The s_x run label overlaps the ellipse's lower arc, and its background patch cuts a visible gap in the stroke (cap 7).
   - Delete the background patch.
   - For the slope beat only, zoom the Anscombe axes to x ∈ [4, 14], y ∈ [4, 11.5] (an animate.set on x_range/y_range with the plot, about 1 s, during "Least squares sets the slope…" at 2:45.5). This makes the ellipse about 1.4× larger.
   - Place `s_x` (MathTex 40) under the LEFT third of the run segment: `next_to(run.point_from_proportion(0.25), DOWN, buff=0.15)`. That spot sits between the run (y = ȳ) and the lower arc, which at x = x̄ + 0.2·s_x is still about 0.9 data units below the run.
   - Assert in scene.py that the label's bounding box keeps ≥ 0.15 units from the ellipse: sample 200 `ellipse.point_from_proportion` points and require the minimum distance to the bounding box to be ≥ 0.15. Do the same check for `r s_y` against the blue point at (13, 7.58).
   - Result: removes cap 7, and Visual moves to 8.5.
2. [2:40–3:12][Visual/Clarity/Sync] Three problems share one cause:
   - For about 17 s the right half of the frame holds only "r = 0.82" (kf_33).
   - At 3:05 the substitution "0.82 × 2.03 / 3.32" introduces 2.03 and 3.32 from nowhere, in white, although their symbols r, s_y, s_x are yellow.
   - At 3:09 the narration says "share these five numbers" while no five numbers are visible. This is the episode's one deictic miss.

   Fix:
   - When the Anscombe morph lands (2:38–2:40), ReplacementTransform the cleared readout position into Anscombe's own readout. Use two compact lines in YELLOW, MathTex 36: "x̄ = 9.00 · ȳ = 7.50" / "s_x = 3.32 · s_y = 2.03", with "r = 0.82" written on "His correlation is 0.82" as it is now.
   - At 3:05 TransformFromCopy 0.82, 2.03 and 3.32 out of that readout into the substitution, and colour them YELLOW like their symbols.
   - At 3:09, on "these five numbers", Indicate the readout before panel I shrinks. Then move the readout above the quartet in place of the bare slope line, or set it beside the slope.
3. [3:05–3:08.5][Visual] The substitution's "≈ 0.50" extends to x = 1861 px (measured on kf_35), i.e. x = 6.68 units. That breaks the 6.4 title-safe edge (1824 px). Left-align the substitution under "slope =" with `next_to(slope_eq, DOWN, buff=0.5, aligned_edge=LEFT)` and drop it to font_size 44, or shift the whole equation block 0.5 left. Then assert `eq.get_right()[0] ≤ 6.2`.
4. [2:09.5–2:13.3][Motion/Sync] "Nudge a point at random" is spoken at 2:09.6, but the dinosaur is fully static from 2:09.6 to 2:12.0, and the first nudges start only at 2:13.3, a 3.7 s lag. The algorithm is described over a still picture. Make the picture act it out:
   - On "Nudge" (2:09.6), ring one point in white and move it a small random step (0.5 s).
   - On "biased toward a target shape" (2:10.9–2:12.9), draw the dashed circle as now, and give the ringed point a second step toward it.
   - On "keep the nudge only if the five numbers still hold" (2:13.5), Indicate the yellow ellipse and box once (the acceptance test), then start the staggered morph.
5. [1:16.7–1:30][Clarity] "An ellipse inside the box" is never pinned down: which ellipse, and why its touch height is ȳ + r·s_y. The sweep shows the behaviour but not the rule, and the rule is exactly the "rise" reused at 2:59.
   - Rewrite B9's first sentence as: "The correlation picks the one ellipse that touches all four walls, and sets how high it touches the side walls: r standard deviations above the centre."
   - On "r standard deviations", draw a thin yellow vertical segment from the centre line to the right touch dot, labelled `r\,s_y` (MathTex 36, right of the wall, buff 0.2). Keep it live during the sweep, so the label grows to 0.88·s_y and back.
   - At 2:59 the Anscombe "rise" then becomes a recognised object, not a new one.
6. [3:16.6–3:18.6][Motion] The landing is a cross-dissolve through a near-empty frame. At 3:17.5 everything is at about 15–20 % opacity while "The cloud you pictured" is spoken (3:17.3). Keep panel I's yellow ellipse alive and ReplacementTransform it (1.2 s, from 3:16.6) into the dinosaur-scale ellipse at the opening plot's position, while the quartet fades and the guess cloud and readout fade in. Then "this ellipse" (3:19) Indicates a carried object instead of drawing a new one. This is the one place where continuity, the episode's best asset, breaks.
7. [2:58.6–3:01.4][Motion] The rise and run flights start as stacked glyphs: "r r s s_y" at 2:59.0 and "s s_x x" at 3:00.8. The s_x copy's path then crosses the word "slope" at 3:01. Indicate the source term for 0.4 s first. Then fly the copy with `path_arc=-0.5`, routed below the equation block, so its path never intersects "slope =".
8. [0:00–0:13.8][Hook] The commit prompt finishes at 0:13.8, and the title already says "dinosaur", which blunts the reveal at 0:21. Tighten B0 so "Picture the scatterplot, and its best-fit line" ends by 0:11: replace "Five numbers summarize a hundred and forty-two points:" with "A hundred and forty-two points, five numbers:" (about 1.5 s shorter, with n = 142 already on screen). Keep the planned 1.5 s hold.
9. [0:27.6–0:40][Clarity/Visual] The two sourced percentages are spoken only. Write "86 %" (grey MathTex 36) above the yellow bar as it grows on "bar graphs" (0:33). Write "13 %" beside the strip as the points return on "showed the points" (0:38). Both are short labels next to their referent, so they do not breach the word limits.
REACHES 9 IF ALL FIXED: yes, narrowly.
  - Fix 1 removes cap 7, which returns the episode to about 8.4.
  - Fixes 1–3 lift Visual to 9; fixes 4, 6 and 7 lift Motion to 9; fixes 2 and 4 lift Audio/sync to 9; fix 5 lifts Clarity to 9.
  - Weighted is then about 8.9. Reaching 9.0 also needs Hook (fix 8) or Concision/Originality to land at 9.
  - The structure is already at bar: a misconception with commit, then the reveal, a measured v1 fail (0/5), one picture (the ellipse in its box), the three-move repair (0→2→4→5), an honest limit (median off by 6), the Dozen and Anscombe, and a landing back on the opening frame. No structural change is needed.
KEEP:
  - The live "dinosaur / now" readout with ≠/= and the "matching k/5" counter (0:47–1:53). Together with the red live ellipse drifting off the yellow one on the replay (1:33–1:40), it turns failure and repair into measured, watchable proof.
  - The persistent yellow geometry through the Datasaurus Dozen (2:13–2:35), recomputed every frame and never moving. The picture IS the claim "every one of them has this same ellipse".
  - The slope derivation that ends with the best-fit line growing from the centre through the touch point (2:49–3:07), and the landing where that same line grows over the viewer's dashed guess (3:21–3:23).
```

## Notes by step

**1. Script read cold.** I can state the idea in one sentence (above). The payoff is derived from the same picture rather than bolted on: the OLS line through the centre and the touch point is the ellipse again. The palette block is declared and followed: yellow = the summary geometry, blue = data, red = drifted summary, green = matches, grey = context.

**2. Fact-check.** Every number I could recompute checks out (table above). One soft point: the star's median (52.16) comes from our own construction and I cannot rebuild it from the data files, but it is consistent with facts #11. No Wrong or Unverifiable items.

**3. Mechanics.** These are all inside the bar. Planned holds: 0:12.6–0:16.0 (3.4 s) and 1:36.7–1:40.2 (3.5 s). The 1.6 s silences between Dozen shapes (2:21–2:31) are deliberate reading holds, and each shape is on screen while it is named.

**4. Transcript.**
- WER is 3.0 %. The differences are number formatting only ("oh" heard as "zero", "s x" heard as "sx"); I found no mispronounced term. "Matejka", "Fitzmaurice" and "Weissgerber" are all transcribed correctly.
- No banned phrases. The question "So how much can five numbers hide?" (0:40) and "So what exactly do five numbers pin down?" (1:01.7) are separated by a whole beat, so they do not form a chain.
- The hook question lands at 0:11.2–0:13.8.

**5. Flipbook and sync.**
- Each deictic was checked against the word timings:
  - "Here are the real points" (0:21.3): the morph runs 0:21.5–0:23.
  - "bar graphs" (0:33): strip then bar. "error bar" (0:36): drawn at 0:37.
  - "Version 1 slides" (0:48.7): the slide runs 0:49–0:53.
  - "The center moved" (0:57): dots at 0:57. "x spread grew" (0:59) and "y spread shrank" (1:01) each get their own bars.
  - "Slide / Stretch / tip" (1:40.1 / 1:42.1 / 1:45.3): counter 2/5 by 1:43 and 4/5 by 1:45; r goes = by 1:49.
  - "this star / bullseye / X / stripes / dots": each lands on its noun (2:21–2:31).
  - "this ellipse" (3:19): drawn on cue.
  - Misses: "Nudge a point" (fix 4) and "these five numbers" at 3:09 (fix 2).
- Continuity is excellent. The only dissolve-through-near-empty is the landing (fix 6). There are no hard cuts.

**6. Keyframes against §5.**
- Safe area holds everywhere except kf_35 (fix 3). The highest text is the y label at about 80 px; citations sit at about 940 px (y ≈ −2.96). The quartet's "x" ends at 1812 px.
- The settled overlap at 3:00.8–3:08.5 is the cap (fix 1). The transient glyph stacks at 2:59.0 and 3:00.8 come from TransformFromCopy starts and last under 0.5 s (fix 7, not a cap).
- Type sizes:
  - readout about 45 px cap height;
  - ticks about 30 px;
  - citations about 26 px;
  - the grey note "first two decimals, as published" about 24–26 px, which is at the minimum.
- Contrast is fine. Dimmed context during the insight is at about 30 %, as the standard asks.
- Palette is consistent all episode, and red/green is always paired with ≠/=.
- Composition is strong while the readout and plot share the frame (0:00–2:01). It is weakest at 2:40–2:58, where the right half is empty apart from "r = 0.82" (fix 2).
