# Episode 20, review round 1 (craft critic: visual design, motion, A/V sync)

Evidence: `review/` pack (metrics.json 10:00 is newer than final.mp4 09:58). I read report.md, all 11 contact sheets, the transcript, script.md, facts.md and narration.txt. Full-resolution frames checked: kf_01 (0:10.7), kf_07 (0:36.1), kf_12 (1:18.0), kf_14 (1:34.7), kf_17 (1:55.8), kf_33 (2:51.4), kf_37 (3:01.5) and kf_40 (3:12.8). I also extracted these with ffmpeg into /tmp/ep20r1: 0:00.1, 0:00.8, 0:26.0, 0:32.6, 0:33.2, 0:44.5, 0:46.0, 0:47.5, 0:48.6, 0:49.0, 1:57.0, 1:59.5, 2:18.5–2:22.3 (6 frames), 2:23.9–2:26.2 (4 frames), 2:29.0, 2:29.8, 2:30.6, 2:34.5, 2:35.5, 2:56.8–2:58.4 (3 frames) and 3:01.0–3:04.2 (4 frames). I measured audio RMS over 2:56.4–2:57.6.

```
EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"
IDEA: Two means, two SDs and a correlation fix exactly one ellipse (a centre, a box, and where the ellipse touches the box walls), so any shape with that ellipse (a star, the Datasaurus Dozen, Anscombe's quartet) shares those five numbers and even the best-fit line, and only a plot shows the shape.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.4   AFTER CEILING: 8.4 (lowest 8 + 2 = 10, not binding)
CAPS: none. I checked these and they do not trigger:
  - All three empirical sources are on screen (Cairo 0:20, Matejka & Fitzmaurice 2:02, Anscombe 2:30).
  - Transient text overlaps at 0:33.2 and 2:29.8 happen mid-transform or mid-crossfade and are not settled layouts, so they are listed as fixes rather than cap 7.
  - No banned phrases. "Picture the scatterplot" is an instruction, not "picture this".
FINAL: 8.4   PASS: no
FACTS:
  The dinosaur has 142 points | Verified | datasauRus TSV (facts #1)
  x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified (first two decimals truncated, as published) | Matejka & Fitzmaurice 2017; facts #2
  Datasaurus drawn by Alberto Cairo, 2016, The Functional Art | Verified | thefunctionalart.com, Aug 2016; Autodesk acknowledgements
  v1 star: centre moves to 50/50, s_x 16.76→20.51, s_y 26.93→20.50 (−23.9 %, "almost a quarter"), r→0.00 | Verified (our construction, numbers recomputed in facts #4 and consistent on screen 0:41–0:57)
  Means = a point; SDs = a box; r sets the right-wall touch at ȳ + r·s_y; r→1 moves it to the corner | Verified (1-SD covariance ellipse support function)
  At r = −0.06 the touch point sits just below the middle (46.10 vs 47.83) | Verified
  The ellipse is everything the five numbers know | Verified (bijection with mean and covariance)
  Translate / scale / shear each fix their own numbers and leave the others unchanged; after all three the star matches exactly | Verified (affine invariances; counter 0→2→4→5 at 1:37–1:45 agrees)
  Median y: 46.02 vs 52.16, "misses by six" | Verified (6.14)
  Matejka & Fitzmaurice 2017, CHI: random nudges biased toward a target, kept only if stats hold to 2 dp; works for any statistic | Verified (CHI 2017 pp. 1290–1294, Autodesk project page)
  "Twelve shapes", all with the same five numbers | Verified (Datasaurus Dozen = dino + 12)
  Anscombe 1973, The American Statistician, 11 points per set, r = 0.82, all four share the five numbers | Verified (r 0.816 in all four; means 9 / 7.50; SDs 3.32 / 2.03)
  OLS line passes through the centre and the right-wall touch point; slope = r·s_y/s_x = 0.82·2.03/3.32 ≈ 0.50 | Verified (0.5001)
MECHANICS: runtime 3:12.8 · wpm 155 (speech) · max silence 1.96 s (1:33.7, planned prediction hold) · max static 3.77 s (1:31.9–1:35.6, planned) · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.84 s · blank background run 0.66 s at 3:02.4–3:03.0
FIXES (highest impact first):
1. [1:13–1:21][Clarity/Visual] The ellipse sweeps to r ≈ 0.85 (kf_12 at 1:18.0 shows a steep diagonal ellipse with the touch dot near the top corner) while both readout columns still say r = −0.06 and the counter says "5/5". The picture and the numbers disagree for about 6 s at the key moment of the insight. Fix: dim the readout r row to 35 % for the sweep. Attach a yellow `r = ` DecimalNumber (font_size 36, buff 0.2 right of the right-wall touch dot) whose updater reads the sweep ValueTracker, so it rides the dot from −0.06 → 0.85 → −0.06. Fade it out on "at minus point oh six" and Indicate the readout r row back to full opacity.
2. [2:17–2:27][Motion] The Datasaurus Dozen flipbook is too fast to read. The star dataset is on screen for about 0.6 s (fully formed at 2:20.2, already dissolving at 2:20.8), and the bullseye and X for about 1 s each. Viewers cannot register the shapes, or the fact that the ellipse never moves, which is the claim. Fix: change each `[pause 0.4]` in B18 to `[pause 1.0]`, and time every transition to land 0.3 s before its noun ("star" 2:19.8, "bullseye" 2:21.1, "X" 2:22.6, "stripes" 2:23.8, "dots" 2:25.4). Then hold each shape for ≥ 1.2 s with the ellipse visible. Optionally add a 26-pt grey dataset-name tag at the bottom-right of the plot.
3. [3:01.5–3:03.0][Motion/Sync] The landing passes through 0.66 s of empty background (blank run 182.37–183.03). "The shapeless cloud you pictured" is spoken at 3:02.1–3:02.9 over nothing, and the cloud fades in only around 3:03.3. This is the one place where the episode cuts instead of transforming. Fix: run the quartet FadeOut and the opening-frame FadeIn concurrently (AnimationGroup, lag_ratio 0, 1.0 s), starting at 3:01.6. Better still, carry the yellow ellipse across: ReplacementTransform the panel-I ellipse into the dinosaur-scale ellipse position while the axes cross-fade, so the cloud is visible by 3:02.1.
4. [0:32.8–0:33.6][Visual/Motion] When the readout splits into "dinosaur / now", the new column's digits morph through each other into illegible glyph soup (frame 0:33.2: "5ᵡ26", "1ⁱ76" and similar beside each value). Fix: create the "now" column as its own DecimalNumbers. TransformFromCopy each whole yellow value mobject (not digit-matched submobjects) along a straight path to its slot, run_time 1.0, lag_ratio 0.1, or FadeIn the column shifted 0.3 left→right. No frame may show two digit strings overlapping.
5. [2:45–2:51][Visual] The `s_x` brace sits under the bottom edge of the box (kf_33: brace at y ≈ 5.2 data units), about 2 units below the run segment it names (drawn at y = ȳ = 7.5 from centre to the right wall). The rise label `r s_y` sits right next to its segment, so the two labels are inconsistent. Fix: put the brace (or a plain `s_x` label, buff 0.15) directly beneath the horizontal run segment, and draw both segments in the same stroke width as the labels' TransformFromCopy source.
6. [2:28.8–2:31][Motion] After "Every one of them has this same ellipse", the dots morph back into the full dinosaur (2:29.0) without narration, then 131 of the 142 points disappear into Anscombe's 11 (2:30.6). This is an unexplained round trip. Fix: go straight from `dots` to Anscombe I. Keep the yellow ellipse as the persistent object and morph it to Anscombe's ellipse while the axes rescale, and FadeOut the surplus dots with the old axes.
7. [2:29.6–2:30.2][Visual] The Matejka and Anscombe citations cross-dissolve in the same spot, so two citation strings overlap (frame 2:29.8, ghost text after "CHI"). Fix: FadeOut the old citation (0.3 s), then FadeIn the new one, in Succession.
8. [0:48.6–0:49.4, 1:59.5][Visual] The Circumscribe flags leave a stray red stroke beside the value mid-animation ("20.50ˈ" at 0:49.0, "52.16ˈ" at 1:59.5), which reads like a typo or prime mark. Fix: replace Circumscribe with `Indicate(row, scale_factor=1.1, color=RED)`, or a SurroundingRectangle Create→FadeOut in 0.8 s that completes in full.
9. [1:57–2:00][Visual] The "median y" row is wider than the readout block. Its label starts at x ≈ 930 px, left of the readout's alignment, and hangs over the end of the plot's x-axis about 45 px above the "x" label. Fix: write it as `\tilde y` (or "med y") so its "=" aligns with the five rows above at the same left edge, buff ≥ 0.3 from the axis label.
10. [2:56.5–2:57.6][Audio] Whisper drops "a trend" (narration diff at 2:57.3). There is speech from 2:57.1, but it is swallowed straight after "...and the line." with no breath. Fix: in B21 write "...so they share the ellipse and the line. [pause 0.3] A trend, a curve, an outlier, and one point doing all the work." Re-TTS, then confirm by ear and by WER.
11. [0:00–0:03][Hook] The first frame (0:00.1) is effectively empty, with the readout fading in row by row and the axes arriving only at 0:03. Fix: have the axes and "n = 142" present at frame 1 and Write the readout rows on their spoken words, so the puzzle object is on screen in the first frame.
12. [1:47–1:51][Concision] "The star has the dinosaur's exact numbers, to every decimal place" repeats "All five match now". Fix: merge them into "All five match now, to every decimal place." That saves about 3 s, which can go toward fix 2's longer holds.
13. [0:25–0:30][Hook] The stakes line ("When a report shows only these five numbers…") is generic. Fix: name a concrete reader decision without any empirical claim, for example "If a dashboard tile showed only these five numbers, how much could it hide?"
REACHES 9 IF ALL FIXED: yes. The structure is already at bar: misconception (round cloud) → reveal → measured v1 failure (0/5) → one picture (ellipse in box) → three-move fix (2/5 → 4/5 → 5/5) → honest limit (median off by 6.14) → real sources → landing on the opening frame. Fixes 1–4 remove the frames where the picture contradicts the narration or text becomes illegible. That lifts Visual and Motion to 9 and Clarity to 9. Hook and Originality stay near 8.5–9 because the Datasaurus itself is well known; the ellipse-plus-affine-fix angle is what carries it.
KEEP:
  - The live "dinosaur / now" readout with ≠/= marks and the "matching k/5" counter. It turns v1's failure (0:39–0:57) and the three-move repair (1:35–1:47: 0→2→4→5) into measured, watchable proof.
  - The ellipse construction from flying copies of the numbers: means → dot (1:01), SDs → half-segments → box (1:05–1:09), r → wall touch point (1:11). Then the red live ellipse drifting off the yellow one on the replay (1:27–1:35).
  - The landing back on the "a guess" cloud with the ellipse drawn through it, then the dinosaur returning around the same ellipse (3:04–3:11).
```

## Notes by step

**Script read cold.** The idea fits in one sentence (above). There is one coherent through-line, and the payoff (Anscombe's shared best-fit line) is derived from the same ellipse picture rather than bolted on.

**Transcript.** No banned phrases or patterns. There is one question chain risk: "So what exactly do five numbers pin down?" at 0:53.9 is a single question, so it is fine. "How would you fix the star?" (1:32) is followed by a planned 2.0 s silence on a picture that answers it. The hook ("Picture the scatterplot" at 0:11.2 plus a 1.9 s hold) lands before 0:15.

**A/V sync spot-checks (word timings vs extracted frames).**
- "these stripes" (2:23.4–2:25.0): stripes on screen at 2:23.9.
- "these dots" (2:25.2–2:26.0): dots at 2:25.4.
- "this bullseye" (2:20.6–2:21.8): bullseye at 2:21.5.
- "this star" (2:19.6–2:20.4): star at 2:20.2, but gone by 2:20.8 (fix 2).
- "the touch point climbs toward the corner" (1:13–1:17): sweep visible, but r is unlabelled (fix 1).
- "slide / stretch / tip" (1:35.6–1:43): the counter reaches 2/5 at 1:39, 4/5 at 1:41 and 5/5 at 1:45, each on its verb.
- The only miss is the landing gap (fix 3).

**§5 checks at full resolution.**
- Safe area: the highest text is the y label at about 85 px; citations sit at about 932–946 px, so y ≈ −2.96 to −3.0, above −3.2.
- Palette: yellow (summary), blue (data), red (drifted summary), green (= marks), plus greys and ink. This stays consistent all episode, and red and green are always paired with ≠ or =.
- Type: the readout is about 45 px cap height, and citations are about 24–26 px cap height.
- The prose word load is tiny.
- Axes are named x and y. The data has no units, which is acceptable here.
