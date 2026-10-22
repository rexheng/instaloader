# Round 9: craft critic (visual design, motion, A/V sync; all dimensions scored)

**Evidence.** I used the `review/` pack: metrics.json (23:03) is newer than final.mp4 (23:01).
- Pack: report.md, narration_diff.txt, transcript.txt, transcript_words.tsv (0:35–0:39, 1:21–1:52, 2:40–3:21), all 12 contact sheets.
- Full-resolution keyframes read: kf_01, 07, 08, 10, 15, 16, 17, 19, 20, 22, 24, 27, 29, 30, 31, 33, 35, 37, 38, 39, 40.
- Extra frames (ffmpeg): 0:30.6, 0:31.4, 0:34.8–0:36.8 (0.4 s steps), 0:37.0–0:39.0 (0.4 s), 1:23.4–1:27.0 (0.4 s), 1:24.2, 1:25.0, 1:34.6, 1:35.2, 1:51.0, 1:52.0, 2:42.0–2:43.5 (0.5 s), 2:46.6–2:49.6 (0.6 s), 2:52.4–2:53.6 (0.4 s), 3:00.4–3:04.2, 3:02.4–3:03.9 (0.3 s), 3:13.6–3:22.0 (0.6 s).
- Measured: the "13% / showed points" label brightness at 0.1 s steps (0:36.0–0:39.0); the parked formula's glyph height in kf_20.
- Recomputed (Python, from the episode's own datasaurus_dozen.tsv and anscombe.csv) every Datasaurus and Anscombe statistic shown or spoken.
- Read script.md, narration.txt, facts.md #22/#30/#35/#38, the round-8 craft and substance reviews and the round-8 CHANGELOG, to check which fixes landed.

```
EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"
IDEA: Two means, two SDs and a correlation pin down exactly one ellipse (a centre, a box, and touch points on the
      best-fit line), so any shape with that ellipse (a dinosaur, a star, Anscombe's four) has the same five numbers
      and the same line, and only a plot shows the shape.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 8.5 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.9 (892.5/100 = 8.925)   AFTER CEILING: 8.9 (lowest 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none
FINAL: 8.9   PASS: no
```

## FACTS
| Claim | Status | Source / check |
|---|---|---|
| Dinosaur n = 142; x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified | My recompute: 54.2633, 47.8323, 16.7651, 26.9354, −0.0645 (first two decimals, as the screen says) |
| Circle, star, bullseye, X, stripes share the five; medians 51.02 / 50.11 / 47.38 / 39.87 / 50.47 vs 46.02 | Verified | Recompute: 51.025, 50.111, 47.383, 39.876, 50.474; dino 46.026. Settled frames (kf_27 51.02, kf_29 50.47, sheet 9) match |
| "Drawn by Alberto Cairo" (Cairo, 2016 · The Functional Art) | Verified | Cairo 2016; credited in Matejka & Fitzmaurice 2017 |
| 703 physiology papers, 86% bar graphs, 13% showed the points | Verified | Weissgerber et al. 2015, PLoS Biol 13(4):e1002128: n = 703, 85.6% ≥ 1 bar graph, 13.4% ≥ 1 univariate scatterplot (facts #22) |
| v1 star: centre (50, 50), s_x 20.51, s_y 20.50, "y spread shrank by almost a quarter" | Verified | 26.93 → 20.50 = −23.9% (kf_10) |
| Touch point (x̄ + s_x, ȳ + r s_y); best-fit line through the midpoints of the ellipse's vertical chords | Verified | Re-derived (support of the 1-SD covariance ellipse in direction (1, 0)); r = 0.50 touch height 47.83 + 0.5·26.94 = 61.30; the band is tagged "simulated" |
| "For the dinosaur, it's just below the middle" | Verified | 47.83 − 0.0645·26.94 = 46.10 |
| Star median misses by "six" | Verified | 52.16 − 46.02 = 6.14 |
| Matejka & Fitzmaurice 2017, CHI: search keeps the five fixed and nudges points toward a target; 12 shapes | Verified | CHI 2017, doi:10.1145/3025453.3025912 |
| Anscombe 1973, 11 points, all four share r 0.82, s_x 3.32, s_y 2.03, x̄ 9.00, ȳ 7.50; same line | Verified | Recompute: r 0.8162–0.8165, s_x 3.317, s_y 2.030–2.032, slope 0.4997–0.5001, touch 9.16 |
| slope = r s_y / s_x; dinosaur ≈ −0.10, "minus point one" | Verified | −0.06·26.93/16.76 = −0.0964 → −0.10; unrounded −0.1036 |
| "A bar graph, which draws only two" | Verified | A bar + one error bar encodes ȳ and one spread; the squeezed 1-SD ellipse is exactly ȳ ± s_y |

No claim is wrong, fabricated or uncited. All four sources carry bottom-left citations held for 3 s or longer.

## MECHANICS
- runtime 3:22.3 · 150 wpm on speech time (134 overall; 451 words heard, 442 scripted) · longest internal silence 2.37 s (0:10.3–0:12.7, the planned commit hold) · longest static stretch 2.30 s · −14.1 LUFS / −1.6 dBTP · leading 0.00 s, trailing 1.94 s · WER 1.4% (only "oh"/"zero", "ess why"/"S-Y", "dinosaur's"/"dinosaurs") · 0 banned phrases · 12/12 deictics animated within the window · layout audit 0 issues in 216 checks · 0 black frames.
- Transcript sweep: no §4 phrase or pattern. The questions (0:06, 0:38, 1:02, 1:55) stand alone. There is no fake reveal and no recap ending. The ident (≈3:21.0–3:22.3) is a ≤ 1.5 s series card.
- No cap triggers.

## Round-8 craft fixes: what landed
1. **Ticks before data: landed.** At 2:42.0 the 131 non-travelling points, the dinosaur readout, the median row and the CHI citation fade first. At 2:42.5 the 11 points still sit under 0–100 ticks. The ticks, points, ellipse and box then change together (2:43.0).
   - Residue: at 2:43.0 both scales are half-visible, and the x axis reads "0 4 25 8 50 12 100" for about 0.5 s (fix 5).
2. **Stale rise: landed.** The run, rise and "r s_y" are gone at r = 0.50 before the sweep (sheet 6, 1:43).
3. **Empty hand-off: landed.** By 3:01.4 the guess cloud, "your guess", "your line", the readout and the formula are all in.
4. **Doubled ellipse: landed.** At 2:53.6 the copy is already in flight to panel II, and no stationary duplicate sits on panel I.
5. **Repeated star cut: landed.** The roll call runs circle → bullseye → X → stripes (2:29–2:37).
6. **"The same point" cut: landed.** B18 now reads "did it with just 11 points".
7. **"13%" over the fade: landed.** The bar, error bar and tag are gone by 0:35.6, and "13%" writes from 0:36.4 on bare strip.
   - It now leaves too early instead (fix 2).
8. **Band clutter: landed.** The band points step back to 40% (kf_16), and nothing sits between the wall and the rise.
9. **Empty upper right: landed.** The parked formula moves up grey to the top right (kf_30, kf_31).

## What I saw, beat by beat
- **0:00–0:12. The puzzle in frame 1.** Frame 1 is the puzzle (kf_01): axes, "?", n = 142 and five yellow values. Three dashed candidates are drawn on "which way", then the 2.4 s commit hold. Clean and legible.
- **0:12–0:25. Guess cloud into dinosaur.** The guess cloud's own points travel into the dinosaur (0:17–0:19). The citation arrives on "drawn by" (0:21). Still the episode's best image-to-image move.
- **0:25–0:39. Stakes.**
  - The dinosaur collapses to its y-strip, and the bar and the ±1 SD error bar are built over it (kf_07, sheet 2).
  - On "Only" they fade (0:35.0–0:35.6), and the strip stands alone.
  - "13% / showed points" writes from 0:36.4 to about 0:37.5, then fades out at 0:38.4–0:38.5 as the strip springs back. That is about 0.9 s of hold after drawing, against the §5 minimum of max(1.5, 0.8 + 0.3 × 3) = 1.7 s. The number also appears about 1 s after "thirteen" is spoken (0:35.4).
- **0:39–1:02. Build and fail.**
  - The dashed star, the "dinosaur | now" readout with = / ≠ glyphs, and "matching 5/5 → 0/5".
  - Live red values (kf_10), then red and yellow mean ± SD crosses (sheet 4). Failure measured, cause named. Excellent.
- **1:02–1:21. Five numbers become geometry.** The red cross rides back and turns yellow. (x̄, ȳ) copies fly in, then s_x and s_y copies (1:07–1:13). The walls grow from the arm tips, the ghost ellipses appear on "Many", and the yellow ellipse and touch dots arrive on "picks one" (1:15–1:21). Each element is born from the number it encodes.
- **1:21–1:48. The insight.**
  - Slip at 1:24.2: the "simulated / r = −0.06" tag writes while the real dinosaur's dimmed points are still on screen, so for about 0.4 s real data carries the "simulated" label.
  - From 1:24.6 to 1:25.0 the plot holds only the ellipse, the box and the centre while r sweeps −0.05 → 0.14. The simulated cloud fades in only from about 1:25.2, already at r ≈ 0.4 (frames 1:24.2–1:25.4).
  - So the one move that should show "the cloud tilts as r grows" is a cross-fade over an empty plot. It is short, but it sits on the key "what if".
  - After that the sequence is the animation as proof:
    - The band's 12 points merge into an average dot on a bare wall, and "r s_y" is built from flown glyphs (kf_16).
    - The s_x label and the r s_y copy run their lanes into the slope (1:34.6, 1:35.2, kf_17).
    - The chords' midpoints sit on the dashed line, then the chords collapse onto the touch point (sheet 6).
    - The sweep back is clean (kf_19).
- **1:48–2:12. Replay and fix.** The parked formula sits small and grey under "matching" (kf_20). The live red ellipse drifts off the yellow one (1:52.0, kf_22). In the 1.5 s hold the boxes fade and the star dims. Slide, stretch and tip each turn their own rows green (sheet 7, kf_24). Every move encodes one number.
- **2:12–2:41. The honest limit and the Dozen.** The median row arrives red. The star walks back with the five held, and the rows are boxed on "these" (2:25). The points stream into the dashed circle. Each shape lands on its "this" (2:31 circle, 2:33 bullseye, 2:35 X, 2:37 stripes), and every settled median is correct.
- **2:41–3:01. Anscombe.**
  - The three-step change works (see fix 1 above). Residue: at 2:43.0 the x axis reads "0 4 25 8 50 12 100" for about 0.5 s, and the y axis stacks "10/75", "8/50", "6/25".
  - On the pause the readout's r value leaves its row, so the row reads "r = ␣" at 2:47.2. The row refills by 2:47.8 while the flown "0.82" is still parked beside the touch dot until about 2:49.0 (kf_31).
  - Parked there at y ≈ 9.16 on a 4–10 scale, "0.82" reads as the dot's coordinate, and it is doubled with the readout for about 1.2 s.
  - Then "Same rule" lights the formula, the run and rise are drawn, and the line grows (2:49.0–2:51.0). The quartet (kf_33) is screenshot quality.
- **3:01–3:22. Landing.**
  - The hand-off is full by 3:01.4. At 3:03.0 the formula's numerator is empty ("slope = —/s_x"), and "−0.06" is still dropping out of the r row.
  - At 3:03.3 the s_y row's value is blank while 26.93 flies, but at 3:03.6 the s_x value only dims while 16.76 flies. The three sources get three different treatments within 0.6 s.
  - Then it is excellent:
    - "≈ −0.10" on "minus point one" (kf_35).
    - The ellipse squeezes into the ±s_y error bar as the bar grows (3:14.8–3:16.0, kf_38).
    - The x̄, s_x and r rows step back on "only two".
    - On "dinosaur" the guess cloud's points re-form into the dinosaur (3:18.4–3:19.0), and the bar parks beside the plot (kf_39).
    - The ident follows within about 1 s.

## Scores, with evidence
- **Hook 9.** The puzzle is in frame 1 (kf_01). The viewer commits to both shape and tilt by 0:10.5, with visible candidates. The reveal comes at 0:17–0:19. The landing resolves both halves on the cold-open frame ("Your line was right… Your cloud was wrong", 3:02–3:13, kf_35).
- **Clarity 9.** It is concrete first, and every number checks (FACTS). The insight is re-derivable after one watch: the averaged slice dot on bare wall, the rise labelled r s_y, and the slope assembled from the run's and rise's labels (1:28–1:36). The median is shown as the honest limit. The one ambiguity, "0.82" parked as if it were the touch dot's coordinate (2:47.8–2:49.0), is brief, and the run and rise clarify it 1 s later.
- **Visual 9.** Every settled frame I opened has one focal point, a held palette (yellow = summary, blue = data, red + ≠ / green + =, grey = context), bottom-left citations and clean margins:
  - kf_01, 07, 08, 10, 15, 16, 17, 19, 20, 22, 24, 27, 29, 30, 31, 33, 35, 37, 38, 39.
  - The layout audit is clean.
  - Nitpick: the parked grey formula (1:49–2:41) has about 27 px ascenders and about 12 px subscripts (measured in kf_20). That is at the floor, acceptable for 50%-opacity context.
- **Motion 8.5.** Objects persist and transform throughout. The chord collapse, the guess cloud re-forming into the dinosaur, and the ellipse squeezed into the error bar are motion as argument. All nine round-8 items landed. Five small choreography slips remain, and one breaks a §5 standard, so this is not yet "reading time respected; every motion encodes a relation":
  1. **Reading time (0:37.5–0:38.4).** "13% showed points" holds about 0.9 s after drawing, against 1.7 s required (measured at 0.1 s steps).
  2. **"Simulated" over real data, empty sweep (1:24.2–1:25.2).** The tag sits over the fading dinosaur, r sweeps over an empty plot, and the cloud fades in late.
  3. **"0.82" parked as a coordinate (2:47.2–2:49.0).** The readout blanks, then the value is doubled.
  4. **Numerator hole (3:03.0–3:03.6).** The sources are treated inconsistently.
  5. **Interleaved tick scales (2:43.0).** About 0.5 s.

  Each is 0.4–1.8 s, and none is severe, but together, and with one a hard standard, they hold Motion at 8.5.
- **Audio 9.** −14.1 LUFS and −1.6 dBTP, at 150 wpm. Pauses are shaped: 2.4 s after the commit, 1.4 s after "picks one", 1.6 s after "everything the five numbers know", 2.0 s after "How would you fix it?". All 12 deictics land, letter names are spoken as letters, and WER is 1.4%.
- **Concision 9.** 442 words in 3:22. The round-8 slack (the repeated star, the self-flagged repeat) is gone. Each remaining sentence carries a number, a reason or a payoff. Anscombe now earns his 20 s by applying the slope rule to a real tilted line ("Same rule, same line"), which pays off the tilt half of the hook.
- **Originality 9.** Images I have not seen elsewhere and would share:
  - the five numbers drawn as one ellipse;
  - the star repaired one readout row at a time;
  - the vertical chords collapsing to the touch point;
  - the ellipse squeezed into the bar graph's error bar.

## FIXES (highest impact first)
1. **[0:36.4–0:38.5][Motion / reading time] "13% showed points" holds 0.9 s, not 1.7 s, and arrives 1 s after "thirteen".**
   - Start the Write as soon as the 0.4 s fade ends, on "thirteen" (≈0:35.4), run_time 0.6. "13%" lands with the word, and "showed points" lands by ≈0:36.0.
   - Leave the spring-back to the dinosaur (B3) where it is (≈0:38.4).
   - That gives a hold of about 2.4 s and removes the lag.
2. **[1:24.2–1:25.4][Motion] "simulated" labels the real dinosaur, and r sweeps over an empty plot.**
   - (a) Finish the dinosaur's FadeOut (to 0) before the "simulated" tag starts writing, on "Say" (≈1:24.0).
   - (b) Make the simulated cloud tilt *with* r rather than fade in at r ≈ 0.4. Take the current seeded r = 0.50 cloud, compute z1 = (x − x̄)/s_x and z2 = ((y − ȳ)/s_y − 0.5·z1)/√0.75.
   - Give each point an updater x = x̄ + s_x·z1, y = ȳ + s_y·(r·z1 + √(1 − r²)·z2) on the live r tracker. Fade the points in at r = −0.06 (a round blob), then sweep.
   - The cloud then visibly tilts into the r = 0.50 shape. It ends on exactly today's points, so the band and rise exclusions still hold, and the five numbers stay exact at every r (z1 and z2 are already standardised and orthogonal).
3. **[2:47.2–2:49.0][Motion / Clarity] The flown "0.82" reads as the touch dot's coordinate, and the readout blanks, then doubles.**
   - Use TransformFromCopy, so the readout's r = 0.82 never blanks.
   - Park the copy where the rise's label will go: right of the right wall, at height (ȳ + touch)/2 ≈ 8.33, buff 0.25.
   - On "Same rule", TransformMatchingTex it into the rise's "r s_y" label (the s_y copied from the readout), so the 0.82 becomes the r it multiplies rather than a number next to a dot.
4. **[3:03.0–3:03.6][Motion] The numerator is empty for ≈0.4 s, and the three sources get three treatments.**
   - Keep "r s_y" in place until the copies arrive. ReplacementTransform the r glyph into the landing "−0.06", and the s_y glyph into "26.93", in the last 0.25 s of each flight. Do the same for s_x into "16.76".
   - Fly all three as TransformFromCopy from readout rows that stay at full strength. Do not blank s_y, lower r or dim s_x.
5. **[2:42.8–2:43.4][Motion] Both tick scales are half-visible, and the x axis reads "0 4 25 8 50 12 100".**
   - Inside the same 1.2 s play, give the old tick numbers rate_func=lambda t: smooth(min(1, t/0.4)) on their FadeOut.
   - Give the new ones rate_func=lambda t: smooth(max(0, (t − 0.6)/0.4)) on their FadeIn.
   - No frame then carries both scales, and the data move is unchanged.
6. **[1:49–2:41][Visual, nitpick] The parked formula is at the type floor.** The parked grey "slope = r s_y / s_x" has ≈27 px ascenders and ≈12 px subscripts (kf_20). Raise its parked scale from 0.65 to 0.75, and keep 50% opacity.

**REACHES 9 IF ALL FIXED: yes.**
- Fixes 1–5 are local timing and transform changes in existing beats. They remove the reading-time miss and every transitional slip I found, which lifts Motion to 9.
- With every dimension at 9, the weighted score is 9.0. Fixes 1 and 2 alone, which are the standard violation and the key-beat slip, would very likely carry Motion to 9.
- No structural change is needed. Commit, reveal, measured failure, the single picture, the three-move fix, the honest limit, the sourced payoff and the callback landing are all present, correct and in order.

**KEEP:**
- The guess cloud travelling into the dinosaur (0:17–0:19), and re-forming into it on the last line (3:18.4–3:19.0).
- The B9 insight as built (1:26–1:41): the averaged slice dot on bare wall, "r s_y" from flown glyphs, the slope assembled from the run's and rise's labels, and the chords collapsing onto the touch point.
- Slide / stretch / tip turning one readout row green each (1:58–2:08), and the ellipse squeezed into the ±s_y error bar (3:14.8–3:16.0).
