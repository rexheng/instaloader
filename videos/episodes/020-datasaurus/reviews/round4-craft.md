# Episode 20, round 4 craft review (visual design, motion, sync)

**Evidence.** I used the `review/` pack: metrics.json was written at 23:13, after `final.mp4` (23:11), so it is current. I read report.md, transcript.txt, transcript_words.tsv, narration_diff.txt and narration.json word timings. I looked at all 13 contact sheets and at these keyframes at full resolution: kf_01, kf_05, kf_10, kf_13, kf_16, kf_17, kf_19, kf_30, kf_32, kf_33, kf_34, kf_36, kf_38 and kf_40.

I also pulled extra frames with ffmpeg into /tmp/ep20r4:
- the median readout at 2:26.2, 2:27.2, 2:28.7, 2:29.3, 2:30.2, 2:30.7, 2:32.6 and 2:34.5 (settled medians in the Dozen roll call);
- 2 fps strips over 2:40–2:45 (Anscombe intro), 2:56.4–3:02.4 (cov side line) and 3:15–3:18 (readout box, quartet hand-off);
- 4 fps strips over 3:23.6–3:26.6 (landing hand-off) and 3:39.6–3:42.3 (end);
- a full frame at 1:27.6, and a crop of the bar and error bar at 3:37.8.

I recomputed all 13 Datasaurus Dozen datasets (means, SDs, r, medians) from `datasaurus_dozen.tsv`. I read script.md, facts.md, the CHANGELOG and the round-3 craft review.

```
EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"
IDEA: Two means, two SDs and a correlation fix exactly one ellipse (centre, SD box, and a touch point r·s_y up the
      wall), so any shape with that ellipse has the same five numbers and even the same best-fit line; only a plot
      shows the shape.
SCORES: Hook 8.5 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 9 · Concision 8.5 · Originality 9
WEIGHTED: 8.7 (8.725)   AFTER CEILING: 8.7 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.7   PASS: no
FACTS:
  142 points; x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 ("first two decimals, as published") | Verified | recomputed 54.2633 / 47.8323 / 16.7651 / 26.9354 / −0.0645
  Datasaurus drawn by Alberto Cairo, 2016 · The Functional Art | Verified | Cairo 2016 post; Matejka & Fitzmaurice acknowledgements
  703 physiology papers; 86% used bar graphs; 13% showed the points | Verified | Weissgerber et al. 2015 PLoS Biol 13(4) e1002128: n = 703, 85.6% ≥1 bar graph, 13.4% ≥1 univariate scatterplot
  "Your line" slope r·s_y/s_x = −0.10, nearly flat, slightly down | Verified | −0.0645·26.935/16.765 = −0.104
  Version-1 star: all five break; y spread shrinks "almost a quarter" | Verified | 26.93 → 20.50 = −23.9% (our construction, on screen 0:51)
  1-SD ellipse in the ±1 SD box touches the right wall at ȳ + r·s_y; "just below the middle" at −0.06 | Verified | support function of the covariance ellipse; 47.83 − 1.74 = 46.10
  Slide, stretch and shear fix all five "to every decimal place" | Verified (derivation) | translation fixes means, scaling fixes SDs, shear fixes r
  Star median misses by six (52.16 vs 46.02) | Verified | dino median 46.0256; 52.16 from the episode's construction
  Matejka & Fitzmaurice 2017, CHI: perturb a point, bias toward a target, keep only if stats hold to 2 dp | Verified | CHI 2017 pp. 1290–1294
  Twelve shapes, same ellipse, different medians (star 50.11, bullseye 47.38, X 39.87, stripes 50.47, dots 51.29) | Verified | recomputed: 50.1106, 47.3829, 39.8762, 50.4735, 51.2993; all five stats agree to 2 dp. Settled readouts confirmed in frames 2:26–2:35
  Anscombe 1973, 11 points; r 0.82, s_x 3.32, s_y 2.03, x̄ 9.00, ȳ 7.50 shared by all four | Verified | The American Statistician 27(1):17–21 (0.816, 3.317, 2.03, 9, 7.50)
  OLS slope = cov/s_x² = r·s_y/s_x = 0.82·2.03/3.32 ≈ 0.50, "one half" | Verified | 0.501; Anscombe's fitted slope is 0.500
  The 1-SD ellipse squeezed horizontally is exactly ȳ ± s_y, so it becomes the error bar | Verified | the vertical extent of the inscribed ellipse is the box height
MECHANICS: runtime 3:42.3 · 160 wpm (speech), 151 overall · max silence 1.96 s (planned commit hold 0:11.6) · max static 2.97 s · −14.0 LUFS / −1.7 dBTP · lead 0.00 s / trail 1.83 s
FIXES (highest impact first):
1. [0:08.3–0:13.6][Hook] The viewer is asked only about the line, which most will get right ("nearly flat"). The
   likely-wrong belief (a shapeless oval cloud) is then voiced by the narrator at 0:13 instead of being committed by
   the viewer, and the title has already given away the dinosaur. Change B0's question to "Sketch the cloud these
   numbers describe, and its best-fit line." Keep the 1.5 s hold with the grey "?". Change B1's opening to "If you
   drew a shapeless oval with a nearly flat line, that's the reasonable guess." The cloud and the line are now the
   viewer's own, so the reveal at 0:20 breaks the viewer's prediction. The landing ("Your line was exactly right.
   Your cloud was this ellipse.") then pays off a real commitment, not a hypothetical one.
2. [2:05.6–2:21.0][Concision] B16–B17 take about 20 s to explain the search before the circle appears:
   "built a search that holds whatever numbers you choose. They chose these five." and then the full
   nudge/keep/repeat sentence. Cut "that holds whatever numbers you choose. They chose these five." to
   "built a search that holds these five numbers fixed." (about −2.5 s). In B17, cut "at random," and
   "to two decimals" (already stated at 0:45 and on screen at 0:45–1:01), which saves about 1.5 s. Keep the
   ring, step and undo animation as it is. The runtime drops to about 3:38 and the slackest stretch of the
   payoff tightens.
3. [2:39.5–2:44.5][Motion] For about 5 s, five empty slots ("x̄ = … r =") hang in the old single column while
   Anscombe's points arrive. At 2:43.5 they reshuffle into the two-row layout with overlapping glyphs (the
   "s_x = s_y =" stack in the 2:43.5 frame). This is the episode's only motion that carries no relation, and it ends
   in a scramble. Change: on "Francis Anscombe" (2:39.1), TransformMatchingTex the dinosaur's readout directly into
   the two-row mid-right layout (r first, as now) with blank values, run_time 1.0. Then on "eleven points of his
   own" (2:42.7), write the five values with LaggedStart(lag_ratio 0.15). Never show a five-row empty column.
4. [3:34.6–3:38.5][Visual] When the ellipse is squeezed into the error bar, four yellow strokes meet in one spot:
   the best-fit line, the bar top, the error-bar stem and the ellipse (crop at 3:37.8). The line crosses the bar
   top at ȳ, just where the eye should read "ellipse height = error bar". Change: on "Most of those papers"
   (3:33.4), dim the best-fit line to 30% and the ellipse to 60%. Keep the squeezed copy and the bar at full
   strength. Restore both on "dinosaur" (3:38.0), as the points return.
5. [3:24.2–3:24.7][Motion] The landing hand-off morphs Anscombe's tilted panel-I ellipse (r = 0.82) into the
   dinosaur's upright one (r = −0.06). Continuity is good, but the move says "this summary became that summary",
   and they belong to different datasets. Change: fade the quartet out completely (0.5 s). Then fade in the opening
   frame with its readout first, and draw the dinosaur ellipse by TransformFromCopy from the five readout values in
   0.8 s, a one-beat echo of 1:02–1:16. The frame is never empty, because the readout is always there.
6. [1:26.5–1:30.0][Visual] Two yellow labels stack about 20 px apart on the right wall: "r s_y" directly above the
   live "r = 0.80" (frame 1:27.6). The rise has two names at once, and the label hierarchy blurs. Change: on
   "r times s y" (1:26.0), move the live "r = …" label to the top-right corner outside the box, at
   (x̄ + s_x + 0.3, ȳ + s_y), in 0.5 s, smooth. Leave "r s_y" alone, centred on the rise. Bring the r label back
   beside the touch dot on "minus point oh six".
7. [3:10.6–3:12.0][Motion] An empty fraction "= ____" sits on screen for about 1 s before 0.82, 2.03 and 3.32
   arrive (sheet 3:11). Change: grow the fraction bar together with the first TransformFromCopy (0.82 from the
   readout) in the same AnimationGroup, so the template never shows empty.
8. [2:58.9–3:01.6][Audio] "so one s x cancels" is heard as "So when sx cancels" (narration_diff 3:01.4). The
   synthetic voice blurs "one s x". Change the line to "so one factor of s x cancels". It is unambiguous, and the
   strike-through still lands on "cancels".
REACHES 9 IF ALL FIXED: yes, narrowly.
  - Fix 1 → Hook 9. Fixes 3, 5, 7 → Motion 9. Fixes 4, 6 → Visual 9. Fix 2 → Concision 9.
  - (15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·9 + 10·9)/100 = 9.0.
  - No structural change is needed. The arc already runs: commit → reveal → sourced stakes → measured v1 fail (0/5)
    → one picture (ellipse in the box) → three-move repair → median limit → Dozen/Anscombe → slope from the picture
    → landing on the opening frame and the stakes bar.
KEEP:
  - The ellipse built from the readout (1:02–1:33): means fly into the balance point, SDs grow the box, ghosts give
    way to the one ellipse, then the r-sweep with the s_x run and the r·s_y rise.
  - The live "dinosaur | now" readout with =/≠ and k/5, the red live ellipse drifting off the yellow one (1:36–1:42),
    and the three verb-synced fixes closing it (2/5 → 4/5 → 5/5).
  - The landing payoff: "your line" turns out to be the forced line (3:25–3:31), and the ellipse is squeezed into the
    stakes beat's ±s_y error bar (3:34–3:38).
```

## Notes by step

**1. Script, read cold.** The idea fits in one sentence (above). The palette block declares YELLOW = summary, BLUE = data, RED = drifted summary, GREEN = match, GRAY = context, and every frame I saw follows it:
- RED and GREEN always carry ≠ and = glyphs (kf_10, kf_19, kf_30).
- There are at most 4 hues per frame, on one background.

**2. Fact-check.** Every number on screen or in the narration recomputes (table above).
- The truncation convention ("first two decimals, as published") is stated on screen from 0:45 to 1:01. It matters because s_x 16.7651 would round to 16.77.
- The X median 39.876 shows as 39.87, which matches that convention.
- Every empirical claim has an on-screen citation at bottom left: Cairo 0:21–0:26, Weissgerber 0:26–0:39 and 3:34–end, Matejka & Fitzmaurice 2:04–2:39, Anscombe 2:40–3:24.
- I found nothing Wrong and nothing Unverifiable.

**3. Mechanics.** All are inside the bar, so no mechanical cap applies.
- Runtime is 3:42.3, near the top of the window.
- Pace is 160 wpm on speech time.
- The longest internal silence is 1.96 s: the planned commit hold, with the grey "?" fading in.
- The longest static stretch is 2.97 s.
- Loudness is −14.0 LUFS and true peak −1.7 dBTP.
- The end card holds about 1.2 s after "leave out." (220.55 s), so the video ends within 2 s.

**4. Transcript.**
- WER is 3.1%, and every difference is number formatting except two:
  - "Most of those / Those papers" at 3:34 is a 20 ms whisper segment-boundary artefact (213.96–213.98 s). It is not in the audio and does not appear in the TTS word timings.
  - "one s x" heard as "when sx" (fix 8).
- "Matejka", "Fitzmaurice" and "Anscombe" are transcribed correctly.
- I found no §4 banned phrase or pattern. The questions at 0:37.4, 0:58.9 and 1:39.2 are ≥ 20 s apart, so they do not form a chain.
- Hook: the concrete numbers are on screen from frame 1, and the commit question ends at 0:11.5.

**5. Flipbook and sync.** I checked deictics against narration.json word times:
- "Here are the real points" (18.7 s): the morph is complete by 0:21.
- "bar graphs" and "error bar": the bar is up by 0:33 and the error bar is drawn by 0:35.
- "watch the ellipse" (1:37): the red live ellipse is visible at 1:37.
- Slide, stretch, tip: the counter reads 2/5 at 1:45, 4/5 at 1:47 and 5/5 at 1:51.
- Nudge: the ring and the dashed circle are on at 2:11; the step inward breaks x̄ and s_x at 2:13; it is undone with = at 2:15.
- Roll call: each dataset has settled before its noun (median readouts):
  - star 50.11 by 2:26.2 (noun at 145.3 s);
  - bullseye 47.38 by 2:27.2 (147.5 s);
  - X 39.87 by 2:29.3 (149.6 s);
  - stripes 50.47 by 2:32.6 (151.6 s);
  - dots 51.29 (153.7 s).
- "these five numbers" (196.0 s): the box is round the readout at 196.0.
- "this ellipse" (209.8 s): pulsed.
- "bar graph" (215.0 s): the squeeze is under way by 3:35.

Beats: cold open 0:00–0:25, stakes 0:25–0:38, build and fail 0:38–0:59, insight 0:59–1:53, limit 1:56–2:01, payoff 2:01–3:24, landing 3:24–3:42. There are no hard cuts.

**6. Keyframes against §5.**
- Safe area holds. The readout's "≠" ends at about 1770 px and the quartet's "x" at about 1812 px. The citation baseline is about 955 px, above the caption zone. The layout audit reports 0 issues in 256 checks.
- Type: readout cap height about 45 px, ticks about 30 px, citations about 27 px, the decimals note about 28 px (Text 25).
- Word load stays at 12 or below everywhere; the quartet is the worst case.
- Settled overlaps: none. The two crowding issues are fix 4 (3:37.8) and fix 6 (1:27.6).
- Charts: axes are labelled x/y. The Datasaurus is unitless and Anscombe's data are unitless, so I make no deduction.
- The guess cloud is labelled "your guess" and is never presented as data.
- Transitional glyph smears last under 0.5 s and are not capped: 1:09 copies in flight, 0:35 "13%" mid-Write, 2:57 cov side line.
- The cov side line now builds honestly (2 fps strip). r, s_x and s_y are Indicated in the readout on their words and flown up. The rhs is carried round the right of the fraction, and the s_x is struck through. This was round 3's fix 3, and it lands.

## Score rationale
- **Hook 8.5.**
  - For: concrete from frame 1 (axes, n = 142, slots filled on their words); a reveal at 0:20; sourced stakes by 0:37; and a landing that re-sees both the cold open and the stakes bar.
  - Against: the committed prediction is one the viewer probably gets right. The wrong belief belongs to the narrator, and the title spoils the dinosaur (fix 1). Tension dips through the 20 s search explanation (2:05–2:21).
- **Clarity 9.** Concrete before abstract. Every number checks, assumptions are on screen, and sources are correct.
  - The ellipse rule is shown (r-sweep), named, and reused as rise over run for the slope, which closes the loop.
  - Nitpick: "So the touch point … sits r times s y above the centre" (1:23.5) leans on the regression reading of r rather than deriving the tangency. The sweep makes it visible, so it does not need a rewatch.
- **Visual 8.5.**
  - For: a strict semantic palette, a consistent plot-left / readout-right grid, context dimmed rather than deleted (kf_13, kf_16), and clean small multiples (kf_34).
  - Against: yellow convergence at the bar payoff (fix 4), stacked wall labels (fix 6), and the idle empty column at 2:40–2:44 (fix 3).
- **Motion 8.5.** Nearly every move encodes a relation, and all four round-3 motion fixes (nudge, cov, copy train, landing) are in and work.
  - The rest stays below 9: the empty-slot column and its scramble (fix 3), an ellipse morph across datasets at the landing (fix 5), and an empty fraction template (fix 7).
- **Audio 9.** 160 wpm, loudness on target, intentional varied pauses in the roll call, and every deictic I checked lands within 0.6 s of its visual. One blurred phrase (fix 8).
- **Concision 8.5.** Less than 10% is removable. The slack is mostly B16–B17's search description (fix 2), with 3:42 near the ceiling of the runtime window.
- **Originality 9.** Datasaurus and Anscombe are the field's most-shown examples, but the angle is fresh and memorable:
  - five numbers as one ellipse in a box;
  - a hand-built star repaired by slide, stretch and shear on a k/5 counter;
  - "your line was exactly right";
  - the ellipse squeezed into the bar graph's error bar.
