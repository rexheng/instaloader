# Episode 20, round 1: craft review (visual design, motion, A/V sync; all dimensions scored)

Evidence: review/ pack (metrics.json 23:13 is newer than final.mp4 23:11, so I reused it). I read report.md, all 13 contact sheets, and 18 full-resolution keyframes (kf_01, 02, 06, 09, 11, 14, 18, 20, 24, 27, 31, 33, 34, 35, 39, 40, plus the sheets). I also pulled extra ffmpeg frames at 19.5–20.7 s (the reveal), 68.6–69.4 s, 78.6–79.2 s, 145.6–154.4 s (the roll call), 166.4–178.0 s and 213.6–217.0 s (the landing). I recomputed the Datasaurus statistics from datasaurus_dozen.tsv and checked Weissgerber 2015 against the PLOS page.

```
EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"
IDEA: Two means, two SDs and a correlation fix exactly one ellipse (centre, box, touch height), and with it the best-fit line, so any shape with that ellipse (a dinosaur, a star, Anscombe's four) has the same five numbers; only a plot shows the shape.
SCORES: Hook 8.5 · Clarity 8 · Visual 8.5 · Motion 9 · Audio 8.5 · Concision 8 · Originality 9
WEIGHTED: 8.5 (8.45)   AFTER CEILING: 8.5 (lowest 8 + 2 = 10, no effect)
CAPS: none
FINAL: 8.5   PASS: no
FACTS:
  Dinosaur n = 142 | Verified | datasaurus_dozen.tsv (142 dino rows)
  x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified | recomputed 54.2633 / 47.8323 / 16.7651 / 26.9354 / −0.0645; the first two decimals are shown, as published
  Dinosaur drawn by Alberto Cairo, 2016 · The Functional Art | Verified | Matejka & Fitzmaurice project page; Wikipedia "Datasaurus dozen"
  703 physiology papers, 86% used bar graphs, 13% showed the points | Verified | Weissgerber et al. 2015, PLOS Biol 13(4):e1002128 (n = 703; 85.6%; 13.4% univariate scatterplots)
  Version-one star: 50.00 / 50.00 / 20.51 / 20.50 / 0.00; "y spread shrank by almost a quarter" | Verified (our construction) | facts.md #4 (−23.9%); the on-screen values match
  Fixed star matches all five "to every decimal place" | Verified (our construction) | facts.md #10; slide, stretch and shear each preserve the other statistics (derivation checks)
  Median of y: dinosaur 46.02, star 52.16, "misses by six" | Verified | 46.0256 vs 52.1617
  Matejka & Fitzmaurice 2017, CHI: perturb a point, bias it toward a target, keep the move only if the stats hold to 2 decimals | Verified | CHI 2017 pp. 1290–1294, project page wording
  "Twelve shapes", medians 50.11 / 47.38 / 39.87 / 50.47 / 51.29 | Verified | recomputed star, bullseye, x_shape, h_lines, dots
  "Every one of them has this same ellipse" | Verified (to 2 decimals) | all 13 sets agree on the first two decimals
  Anscombe 1973, 11 points, r = 0.82, all four share the five numbers | Verified | The American Statistician 27(1):17–21; 0.816 in every set
  OLS slope = cov/s_x², cov = r s_x s_y, slope = r s_y/s_x = 0.82×2.03/3.32 ≈ 0.50 | Verified | derivation; 0.5001 unrounded
  "One SD right, on average r SDs up"; the touch point of the 1-SD ellipse sits at ȳ + r s_y | Verified | regression of y on x; the ellipse's vertical tangents lie on that line
  The guess cloud is labelled "your guess" (simulated) | Verified | facts.md (the cloud is drawn, not real data)
MECHANICS: runtime 3:42.3 · wpm 160.5 (speech; 185 excluding all pauses) · max silence 1.96 s · leading 0.00 / trailing 1.83 s · max static 2.97 s · −14.0 LUFS / −1.7 dBTP
FIXES (highest impact first):
1. [1:16–1:32][Clarity] The step from "one SD right, on average r SDs up" to "so the touch point sits r·s_y above the center" is asserted, not shown. The screen has a run and a rise but no line, so a viewer cannot see why a regression fact places the ellipse's tangent point. That is the one transition that needs a rewatch. Change: while r sweeps 0 → 0.80 → −0.06, grow a thin dashed YELLOW best-fit line through the centre and the touch dot, so the dot visibly rides the line. Narration: "…on average r standard deviations up. That's the best-fit line, and it meets the right wall exactly where the ellipse touches it: r times s y above the center." At 3:05 the Anscombe line then becomes recognition instead of a new claim. Worth +0.5 to +1 on Clarity.
2. [0:08–0:12][Hook] The viewer commits only to the line, and the "reasonable guess" (nearly flat) is correct (the landing at 3:25 says so). The wrong belief, a shapeless cloud, is never something the viewer predicts. Change the question to "Picture the cloud. Which way does its best-fit line tilt, and how steeply?" and keep the 1.9 s hold. The landing's "your line was right / your cloud was this ellipse" then pays off both halves of the viewer's own commitment.
3. [2:10–2:22 and 1:35–1:42][Concision] The runtime of 3:42 holds three payoffs (median limit, search, Anscombe and slope), and the middle sags. Compress the search mechanics to one sentence: "Their search nudges one point toward a target and undoes any nudge that breaks the five." Keep the ring-step-undo visual, but run it at 1.5× (saves about 4 s). Cut the [pause 0.15] and "They chose these five" by letting the readout flash on "these" in the previous sentence. Target runtime 3:30 or less.
4. [2:57–3:04][Motion/Audio] The "slope = r s_x s_y / s_x²" state holds about 1.5 s before the strike-through (BAR: ≥ 2 s + 0.4 s per term, about 3.6 s). The [pause 1.0] comes before the numerator lands instead of after it. Move the pause so that "r s_x s_y over s_x²" sits whole for at least 2.5 s. Also say "so one factor of s x cancels": Whisper heard "So when sx cancels" at 3:01.4, an ambiguous homophone.
5. [1:00.3–1:02.5][Visual, colour semantics] At kf_11 (1:02.3) the RED mean ± SD cross sits on the restored dinosaur while all five rows read "=" and the counter reads 5/5 GREEN. RED is declared as "drifted", so the colour contradicts the readout for about 2 s. Interpolate the colour RED → YELLOW during the slide back so the cross arrives YELLOW (or FadeOut the red copy as it lands on the yellow one), and finish by 1:00.6.
6. [1:08.5–1:10.5][Motion + sync] The copies of 16.76 / 26.93 smear into an unreadable glyph squiggle mid-flight (frame at 1:09.0, x ≈ 960 px). The box starts growing about 1.5 s after "box" (no box at 1:09.4, box at 1:11). Move each number intact (`.animate.next_to(half_arm)`, not a Transform into the line), Indicate the half-arm, fade the number, and start `GrowFromCenter(box)` on the word "box" (about 1:08.8).
7. [1:39–1:47][Visual] During the prediction hold and the slide, both SD boxes sit at 30% opacity (kf_20, 1:44.9). They read as faint stray red and yellow rectangles under the star outline: clutter without information. Either remove them during the hold and Create them on "Stretch", or keep them at 60% with the RED box dashed so the two boxes are distinguishable.
8. [3:38–3:42][Visual] The last data frame (kf_39, 3:40.6) keeps the dimmed ȳ bar and its error-bar line running vertically through the ellipse and the dinosaur's legs: three overlapping layers in the closing image. On "dinosaur", slide the bar and its error bar out of the plot to x ≈ 108 (right of the axis, still at 40%), so the final image contrasts "two numbers" beside "142 points" without crossing them.
9. [0:19.7–0:20.7][Motion] The guess → dinosaur morph, the episode's biggest reveal, completes in about 1.0 s and lands while "A dinosaur" is already being said. Give it 1.8 s (smooth) starting on "real", hold 0.4 s, then name it.
10. [2:01–2:39][Visual] The "med y" label starts about 25 px right of the x-axis label "x" on nearly the same line (kf_24, kf_27), so it reads as "x  med y". Shift the readout block right by 0.3 units, or move the axis "x" label under the arrow tip.
11. [3:16–3:18][Motion] Panel I's points float with no axes for about 1 s while the zoomed axes fade before the quartet axes arrive (sheet frame 3:17). Crossfade the two sets of axes over the same 0.8 s.
REACHES 9 IF ALL FIXED: yes. Fixes 1–3 lift Clarity, Hook and Concision to 9; fixes 4–10 clear the remaining Visual, Motion and Audio nitpicks. The structure is right: misconception reveal, build, measured fail, iterate, honest limit, sourced payoff, landing that re-sees the first frame. No structural change is needed.
KEEP:
- The slide / stretch / shear fix (1:42–1:53): each move turns exactly its own readout rows to "=" GREEN while the live red ellipse snaps onto the yellow one. That is the animation as proof.
- The Dozen roll call (2:22–2:39): the yellow ellipse, box and touch dots stay frozen while the shapes change underneath and the median row jumps. Each dataset lands about 0.3 s before its name (verified at 147.5, 149.5, 151.5 and 153.5 s).
- The landing (3:25–3:41): the opening frame returns, the yellow line lands on "your line", and the ellipse is squeezed into exactly the ±s_y error bar of the ȳ bar before the dinosaur returns. It answers the cold open and the Weissgerber stakes in one picture.
```

## Notes by dimension

**Hook (8.5).** The puzzle is on screen in the first frame (kf_01: empty axes, "n = 142", five empty slots). Values are written on their spoken words (0:02–0:07), the question lands by 0:11.5, then a 1.9 s hold under a grey "?". The reveal at 0:20 is strong. One deduction: the commitment is to an answer that turns out correct (fix 2). The 2:01–2:39 stretch sags a little before Anscombe re-raises the line question.

**Clarity (8).** Concrete before abstract throughout, and every number checks (see FACTS). The fail is measured: 0/5, with s_y down 24%. Assumptions and limits are stated: "first two decimals, as published" and the median miss. The deduction is the asserted regression-to-touch-point link (fix 1). The ellipse also arrives as "many ellipses touch all four walls" before the viewer knows why an ellipse is the right object. Only the landing's "your cloud was this ellipse" motivates it in hindsight.

**Visual design (8.5).** One flat background, a declared and consistent palette (YELLOW summary, BLUE data, RED drifted, GREEN matched with "=", GREY guess and citations). Clear left-plot / right-readout hierarchy, citations bottom-left at readable size, held well over 3 s. The layout audit shows 0 issues. Deductions: the RED cross in a matching state (1:01–1:02.5), the near-invisible 30% boxes (1:41–1:46), the cluttered final data frame (3:40), and the crowded "x" / "med y" pair (2:01–2:39). The quartet panels (3:19–3:24) are small but legible, with ticks about 30 px.

**Motion (9).** Nearly every move encodes a relation: optimal-assignment morphs, the strip squeeze into the bar graph (0:27–0:31), the live-readout star morph (0:46–0:51), the live red ellipse in the replay, the nudge-reject loop (2:11–2:17), staggered one-by-one travel to the circle, and the ellipse squeezed to the error bar. Longest static stretch 2.97 s. Nitpicks: fixes 4, 6, 9 and 11.

**Audio (8.5).** −14.0 LUFS / −1.7 dBTP, 160 wpm speech, no dead air (max 1.96 s, a planned hold). Deictics land: "this star / bullseye / X / stripes / dots" were verified frame by frame, and "the center moved", "x spread grew" and "y spread shrank" each light up within 1 s. Deductions: dense 185-wpm runs inside the derivation (2:50–3:14), the "one s x" / "when sx" ambiguity (3:01), and the box arriving about 1.5 s after "box" (1:09–1:11). I can't confirm the Whisper "those Those" at 3:33.9 (a 0.02 s token, probably a transcription artifact), so I didn't penalize it.

**Concision (8).** Little is pure padding, but three payoffs in 3:42 leave one slack beat: the search mechanics, which re-show the "hold the five" idea the star fix already proved (fix 3).

**Originality (9).** The Datasaurus is a well-known example. The angle here is not: five numbers equal one ellipse, the star repaired by translate / scale / shear, the ellipse squeezed into the bar graph's error bar, and "your line was exactly right". No banned phrases or patterns found.
