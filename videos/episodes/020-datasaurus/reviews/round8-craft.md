# Round 8: craft critic (visual design, motion, A/V sync; all dimensions scored)

**Evidence.** I used the `review/` pack as it stands: metrics.json (21:34) is newer than final.mp4 (21:32).

- From the pack I read report.md, narration_diff.txt, transcript.txt, transcript_words.tsv (1:34–1:50), all 12 contact sheets, and these full-resolution keyframes: kf_01, 07, 08, 16, 23, 33, 35 and 37.
- I extracted frames with ffmpeg at 0:34.6/35.0/35.4, 1:26.0/27.4/28.4/29.8, 1:38.6, 1:40.0, 2:39.4, 2:40.2, 2:44.0, 2:56.0, 3:02.6/03.4/04.2 and 3:20.0/21.6/22.4/24.0/24.6.
- I made 0.2 s tiles of 2:37.8–2:41.0 and 3:22.6–3:24.8, and crops of the median readout at the settled time of each Dozen shape (2:26.4, 2:28.4, 2:30.4, 2:32.4, 2:34.0).
- I read script.md, the round-7 CHANGELOG section and the round-7 craft review, so I could check which fixes landed.
- From the episode's own `datasaurus_dozen.tsv` and `anscombe.csv` I recomputed every Datasaurus statistic (dino, circle, star, bullseye, x_shape, h_lines) and every Anscombe statistic.

```
EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"
IDEA: Two means, two SDs and a correlation pin down exactly one ellipse (a centre, a box, and touch points on the
      best-fit line), so any shape with that ellipse (a dinosaur, a star, Anscombe's four) has the same five numbers
      and the same line, and only a plot shows the shape.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 8.5 · Audio 9 · Concision 8.5 · Originality 9
WEIGHTED: 8.9 (887.5/100 = 8.875)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none
FINAL: 8.9   PASS: no
```

## FACTS
| Claim | Status | Source / check |
|---|---|---|
| Dinosaur n = 142; x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified | My recompute: 54.263, 47.832, 16.765, 26.935, −0.0645. On screen these are truncated to two decimals, and the screen says so ("first two decimals, as published"). |
| Circle, star, bullseye, X and stripes share the five numbers | Verified | 54.26–54.27 / 47.83–47.84 / 16.76–16.77 / 26.93–26.94; r from −0.062 to −0.069 |
| Medians on screen: 51.02, 50.11, 47.38, 39.87, 50.47 vs the dinosaur's 46.02 | Verified | My recompute: 51.025, 50.111, 47.383, 39.876, 50.474; dino 46.026. The crops of the settled frames show exactly these truncated values. Mid-transition frames (2:29.0 "47.71", 2:31.0 "39.92") are live values while points are still moving, so they are not errors. |
| Cairo drew the Datasaurus ("Alberto Cairo, 2016 · The Functional Art") | Verified | Cairo 2016 blog post; credited in Matejka & Fitzmaurice 2017 |
| 703 physiology papers; 86% used bar graphs; 13% showed the points | Verified | Weissgerber et al. 2015, PLoS Biol 13(4):e1002128: n = 703, 85.6% had a bar graph, 13.4% had a univariate scatterplot (quoted in facts.md #22) |
| The "± 1 SD" tag on the error bar | Verified | The bar we draw is ±1 SD. The paper found most bar graphs used ± SE (77.6%), and the tag says which kind ours is (facts #38). |
| Version-one star: centre (50, 50), s_x 20.51, s_y 20.50, "shrank by almost a quarter" | Verified | 26.93 → 20.50 is −23.9% |
| At one SD right, the average rise is r·s_y; the touch point is (x̄ + s_x, ȳ + r s_y); the best-fit line runs through the midpoints of the ellipse's vertical chords | Verified | Re-derived: the support of the 1-SD covariance ellipse in direction (1, 0). The simulated slice average is 61.27 against a touch height of 61.30 (facts #36), shown as "simulated". |
| "For the dinosaur, it's just below the middle" | Verified | 47.83 − 0.0645 × 26.94 = 46.09 |
| Star median misses by "six" | Verified | 52.16 − 46.02 = 6.14 |
| Matejka & Fitzmaurice 2017, CHI: a search that holds the five numbers while nudging points toward a target; 12 shapes grown from the dinosaur | Verified | CHI 2017, doi:10.1145/3025453.3025912 |
| Anscombe 1973, 11 points; r 0.82, s_x 3.32, s_y 2.03, x̄ 9.00, ȳ 7.50 for all four | Verified | My recompute: r 0.8162–0.8165, s_x 3.317, s_y 2.030–2.032, x̄ 9.0, ȳ 7.500–7.501; slope 0.4997–0.5001 |
| slope = r s_y / s_x; for the dinosaur ≈ −0.10, spoken "minus point one" | Verified | −0.06 × 26.93 / 16.76 = −0.0964 → ≈ −0.10; unrounded −0.1036 |
| "A bar graph, which draws only two" | Verified | A bar plus one error bar encodes ȳ and one spread number. The squeezed 1-SD ellipse has exactly the ±s_y vertical extent. |

No claim is wrong, fabricated or uncited. All four sources carry on-screen citations, at bottom-left, held for 3 s or longer.

## MECHANICS
- **Timing:** runtime 3:24.7; 150 wpm on speech time (463 words heard, 456 in the script); longest internal silence 2.37 s (0:10.3–0:12.7, the planned commit hold); longest static stretch 2.73 s.
- **Audio levels:** −14.1 LUFS, −1.7 dBTP; leading silence 0.00 s, trailing 1.94 s; WER 2.4%.
- **Automated checks:** 0 banned phrases; 12 of 12 deictics animated within the window; layout audit 0 issues in 222 checks; 0 black frames.
- **Transcript sweep:** no phrase from §4. The questions stand alone: 0:06–0:10 (one question in two halves), 0:37, 1:01, 1:49. There is no fake reveal and no recap ending. The end card (≈3:23.8–3:24.7) is the ≤ 1.5 s series ident, not a subscribe card.
- **No cap triggers.**

## Round-7 craft fixes: what landed
All nine landed:
1. **Rise on its own line.** The rise now stands 0.15 right of the wall. The box steps back to 40% grey, the touch dots are hidden, and the slice average lands as a new white dot on an empty wall, then turns yellow (frames 1:27.4, 1:28.4, 1:29.8).
2. **Label built on the word.** "r s_y" is built beside the rise on "r times ess why", with r flown from "r = 0.50" and s_y from the readout (1:28.4).
3. **Sweep back cleaned up.** Run, rise and label leave on the sweep back, leaving only the dashed line, the centre and the touch dots (1:40.0).
4. **Stakes column.** The bar and error bar leave on "Only thirteen percent", so the strip alone carries "13% showed points" (kf_08).
5. **Ticks.** The tick numbers now cross-fade in place.
6. **Anscombe readout.** It is built in its final bottom-right slot and never jumps (2:41–2:57).
7. **s_x label.** No plate, no half-moons (1:23–1:31).
8. **B22.** Cut to "All four of his datasets share these five numbers."
9. **Hand-off ticks.** The 0–100 tick numbers ride the hand-off (3:03.4).

Fixes 1 and 5 each leave a new, smaller residue (see FIXES 1 and 3).

## What I saw, beat by beat
- **0:00–0:12. The puzzle in frame 1.** Frame 1 is the puzzle (kf_01): grey axes, a faint "?", n = 142, and five yellow values that flag on their words. Three dashed candidate lines are drawn on "which way" and held through the 2.4 s commit. It is text-led for the first 6 s, which is a nitpick.
- **0:12–0:25. Guess cloud into dinosaur.** The guess cloud forms, the flat candidate becomes "your line", and the guess points travel into the dinosaur (0:19–0:21). It is still the episode's best image-to-image move.
- **0:25–0:39. Stakes.**
  - The dinosaur collapses into its y-strip, which is meaningful: a bar graph discards x.
  - The bar and the ±1 SD error bar are built over the strip at 30% (kf_07).
  - On "Only thirteen percent" the bar leaves, and the strip alone carries "13% showed points" (kf_08). It's clean now.
  - Residue: for about 0.6 s (0:34.9–0:35.5) the "13%" label is being written while the "± 1 SD" tag and the full-strength error bar are still fading. The column reads "±1 SD / 13% / showe…" with the whisker through the dots (frame 0:35.0).
- **0:39–1:01. Build and fail.** A dashed star, the "dinosaur | now" readout, = / ≠ glyphs and "matching 5/5 → 0/5". Red and yellow mean ± SD crosses show the centre moving, x spreading and y shrinking (sheet 4). This is measured failure, done right.
- **1:01–1:21. Five numbers become geometry.** The red cross rides back and turns yellow. The (x̄, ȳ) copies fly in, then the s_x and s_y copies. The walls grow from the arm tips, ghost ellipses appear on "Many", and the yellow ellipse and its touch dots arrive on "picks one". Each element is born from the number it encodes.
- **1:21–1:41. The insight.** This window is now readable on first watch:
  - The dinosaur's "now" column steps to 25%, so "r = 0.50 · simulated" is the only live r.
  - The run is labelled s_x. The slice band picks out 14 white points that span 20–93 in y, and their merged average lands on a bare wall at 61.3 (1:28.4).
  - "r s_y" is built from flown glyphs. The dashed line grows, five chords are drawn with their midpoints on the line, and the chords collapse onto the touch point (1:33–1:37). This is the animation as proof.
  - Two small residues:
    - (a) After the merge, the 14 originals stay full white in the band. One simulated dot (≈738, 466 px) sits between the wall and the rise bracket, the exact spot the viewer is reading (1:28–1:31).
    - (b) As r sweeps back (1:38.4–1:39.2), the rise bracket and "r s_y" still show the r = 0.50 height while the touch dot has already slid down to r ≈ 0.34 (frame 1:38.6). For about 0.6 s the label measures a rise that no longer ends at the dot.
- **1:41–2:07. Replay and fix.** The dinosaur returns inside the ellipse. The v1 replay drifts a live red ellipse off the yellow one (kf_23). In the 1.5 s prediction hold the boxes fade and the star dims. Slide, stretch and tip each turn their own rows green. Every move encodes exactly one number.
- **2:07–2:37. The honest limit and the Dozen.** The median row arrives red, ≠ 52.16. The star walks back with the five held, the rows are boxed on "these", and the points stream into the circle target. The roll call lands each shape on its "this", and the settled medians are correct.
- **2:37–3:03. Anscombe.**
  - The tick numbers cross-fade, but they change *before* the data does. From about 2:39.0 to 2:40.0 the dinosaur's stripes, its tall r = −0.06 ellipse and box, and its full readout sit under Anscombe's 4–12 / 4–10 ticks (frame 2:39.4; 0.2 s tile). For about a second the axes describe the wrong dataset. The 11 points peel off only from about 2:39.8.
  - After that it is excellent: the 0.82 flies to the touch dot it sets (2:44.0), s_x and r s_y label the run and rise, the line grows, and the terms climb into r s_y / s_x.
  - At 2:56.0, panel I shows two offset ellipses for about 0.4 s while the copies peel off for the other panels.
  - The quartet frame kf_33 is screenshot quality.
  - The upper right stays empty from 2:41 to 2:50. That is negative space next to a busy plot, so it's a nitpick.
- **3:03–3:25. Landing.**
  - The hand-off transforms panel I's axes into the 0–100 axes with ticks riding along. For about 1 s (3:02.8–3:03.8) the frame holds only a lone ellipse and a floating formula, with no points and no readout (frame 3:03.4), during a 2.1 s gap in the narration.
  - Then the guess cloud returns, the yellow line grows onto "your line", the values fly into the formula (kf_35, ≈ −0.10), and the ellipse is squeezed into the ±s_y error bar (kf_37 to 3:20).
  - On "dinosaur" the points re-form at full strength while everything else steps back (3:21.6). The landing frame holds about 1 s after "out", then the ident.

## Scores, with evidence
- **Hook 9.** The puzzle is in the first frame (kf_01). The viewer commits to both shape and tilt by 0:10.5, with visible candidate lines. The reveal is at 0:19, and the landing re-sees the opening frame exactly ("Your line was right… Your cloud was wrong", 3:03–3:15). The text-led first 6 s are a nitpick.
- **Clarity 9.** The round-7 blocker is gone. "On average, the cloud rises r times S-Y" (1:25–1:29) now plays while the averaged slice dot lands on bare wall and "r s_y" is built beside a rise that stands clear of the wall (frames 1:28.4, 1:29.8). The step is re-derivable after one watch. It's concrete first, every number checks, the truncation convention is on screen, and the honest limit (the median) is shown and correct.
- **Visual 9.** Every settled frame I opened has one focal point, a held palette (yellow = summary, blue = data, red + ≠ / green + =), bottom-left citations, legal type sizes and clean margins: kf_07, 08, 16, 23, 33, 35, 37, the 1:40 frame and the 3:21.6 frame. The layout audit is clean (222 checks). All the settled-frame defects from round 7 are gone. What remains is transitional and belongs under Motion.
- **Motion 8.5.** Objects persist and transform throughout, and the slices collapsing onto the touch point is the animation as proof. Five choreography slips each put a wrong or doubled picture on screen for 0.4–1.2 s:
  1. **Ticks before data (2:39.0–2:40.0).** The ticks relabel the dinosaur's stripes as Anscombe-scale data. This is the most visible slip, and it's a semantic one.
  2. **Stale rise (1:38.4–1:39.2).** The rise and its label measure the old r while the dot moves.
  3. **Empty hand-off (3:02.8–3:03.8).** Only an ellipse and a formula.
  4. **Doubled ellipse (2:56.0).** Two offset ellipses in panel I.
  5. **Label over the fade (0:34.9–0:35.5).** "13%" is written over the still-fading error bar and tag.

  Any one of these is a nitpick, but five of them, one in the payoff's key transition, keep this at 8.5.
- **Audio 9.** −14.1 LUFS, −1.7 dBTP, 150 wpm. There are shaped pauses after results: 1.4 s after "picks one", 1.4 s after "five numbers know", 1.3 s after "decimal place". All 12 deictics land within the window. Letter names are heard as letters ("S-Y", "SX"), and WER is 2.4%. Nothing citable remains beyond the synthetic voice's timbre, which I do not penalize.
- **Concision 8.5.** 456 words in 3:25, and almost every sentence carries weight. One slack beat remains: two back-to-back demonstrations of "same five numbers, different shapes".
  - The Dozen roll call (2:23–2:37) includes "This star" (2:27), which re-shows the shape the episode spent 1:30 building.
  - Anscombe is introduced as "made the same point" (2:37), so the narration itself flags the repetition.

  Anscombe earns his place (the slope formula, plus a real r where the rise is visible), but the roll call and the framing could be tighter.
- **Originality 9.** Several images here I have not seen elsewhere and would share:
  - five numbers drawn as one ellipse;
  - the star repaired one readout row at a time;
  - vertical chords collapsing to the touch point;
  - the ellipse squeezed into the bar graph's error bar.

## FIXES (highest impact first)
1. **[2:38.6–2:40.0][Motion] Ticks before data.** The tick cross-fade runs before the data moves. For about 1.2 s the dinosaur's stripes, its tall ellipse, its box and its readout sit under Anscombe's 4–12 / 4–10 tick numbers (frame 2:39.4). The change:
   - Play the tick cross-fade in the *same* `self.play` as the 11 travelling points, the fade of the other 131, and the ellipse/box/centre morph to Anscombe's. Start them all together at about 2:39.6, run time 1.0–1.2 s, rate_func smooth.
   - Alternatively, fade the 131 non-travelling stripe points and the old ellipse/box to 0 *before* the ticks start, so no axis ever labels data it doesn't describe.
2. **[1:38.4–1:39.2][Motion/Visual] Stale rise during the sweep back.** The rise bracket and "r s_y" keep the r = 0.50 height while the touch dot slides down with r (frame 1:38.6: the dot is at r = 0.34 and the bracket still ends at 61.3). The change:
   - Finish the FadeOut of the run, rise and "r s_y" (0.4 s) *before* the r sweep starts, then sweep.
   - Or give the rise an updater, `rise.become(segment(ȳ → ȳ + r_live·s_y))`, so it shrinks with r as it fades.
3. **[3:02.8–3:03.8][Motion] Empty hand-off frame.** The frame holds only a lone ellipse and a floating "slope = r s_y / s_x", with no points and no readout (frame 3:03.4). The change:
   - Start the grey guess cloud, "your guess", the dashed "your line" and the 0–100 readout fading in at 0.5 of the 1.5 s axis transform, not after it.
   - Move the formula toward its final slot under the readout during the same play, so the frame is never just two floating objects.
4. **[2:55.6–2:56.4][Motion] Doubled ellipse.** Panel I shows two offset ellipses while the copies peel off for panels II–IV (frame 2:56.0). Launch each copy already moving (TransformFromCopy with path_arc, starting at once) and stagger them by 0.15 s, so no stationary duplicate stroke sits on panel I for more than about 0.15 s.
5. **[2:25–2:34][Concision] Repeated star in the roll call.** "This star" re-shows the shape built for 1:30. Cut "this star, [pause 0.8]" from B17. The roll call becomes circle, bullseye, X, stripes (saves about 1.6 s). Keep the shape sequence on screen without the star, going straight from the circle to the bullseye.
6. **[2:37–2:44][Concision] "The same point".** "made the same point" tells the viewer this is a repeat. Change B18 to "In 1973, Francis Anscombe did it by hand, with eleven points." (similar length, and it presents Anscombe as the original rather than a repeat). The pause and the points' flight stay as they are.
7. **[0:34.9–0:35.5][Motion] "13%" written over the fade.** The "13% showed points" Write starts while the "± 1 SD" tag and the full-strength error bar are still fading, so the column reads "±1 SD / 13% / showe…" with the whisker through the dots (frame 0:35.0). Delay the Write by 0.4 s, until the bar, error bar, tag and "86%" reach opacity 0, or start their FadeOut 0.4 s earlier on "Only".
8. **[1:28–1:31][Visual] Clutter in the band.** After the 14 slice copies merge into the averaged dot, the 14 originals stay full white, and one simulated dot sits between the wall and the rise bracket (≈738, 466 px). The change:
   - Dim the originals to 40% as the merged dot turns yellow.
   - Add the rise bracket's rectangle (wall to bracket, ȳ to ȳ + r s_y, plus 0.1 margin) to the simulated cloud's redraw-exclusion zones, so no point sits inside the dimension.
9. **[2:41–2:50][Visual, nitpick] Empty upper right.** The upper right is empty for 9 s while all the action is in the plot. Optional: draw "slope =" at its final position, dimmed to 30%, when Anscombe's readout first builds (≈2:41), and light it to full on "slope" (2:50.5), so the right half anticipates the formula.

**REACHES 9 IF ALL FIXED: yes.**
- Fixes 1–4 and 7 remove every transitional slip I found, which lifts Motion to 9.
- Fixes 5–6 remove the one slack beat and the self-flagged repeat, which lifts Concision to 9.
- With every dimension at 9, the weighted score is 9.0. Fixes 1–4 alone give 8.95, which is borderline, so the concision cuts matter.
- No structural change is needed. Commit, reveal, measured failure, the single picture, the three-move fix, the honest limit, the sourced payoff and the callback landing are all present, correct and in order.

**KEEP:**
- The guess cloud's own points travelling into the dinosaur (0:19–0:21), and the landing that grows the yellow best-fit line onto "your line" in the same frame.
- The B9 insight sequence as now built (1:21–1:41): the averaged slice dot landing on bare wall, "r s_y" assembled from flown glyphs, and the chords collapsing onto the touch point.
- Slide / stretch / tip, each turning one readout row green (1:52–2:05), and the ellipse squeezed into the bar graph's ±s_y error bar (3:15–3:20).
