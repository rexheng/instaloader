# Episode 9, review round 1 (craft critic: visual design, motion, A/V sync)

Evidence: `review/` pack (metrics.json 13:18, newer than final.mp4 13:17): report.md, all 11 contact sheets, 14 full-res keyframes (kf_02, 06, 07, 13, 18, 19, 25, 27, 31, 34, 36, 39 among them), plus extra frames extracted with ffmpeg at 0:22.8, 0:41.0, 0:41.5, 0:43.0, 0:44.0, 1:11.0, 1:12.5, 1:31.0, 1:45.0, 2:05.0, 2:06.0, 2:49.5, 2:52.8, 3:01.5. Transcript, transcript_words.tsv, script.md, facts.md and scene.py read. Kohavi et al. 2014 checked against the paper's PDF (exp-platform.com) via web search.

```
EPISODE: 009 — "Why Bell Curves Are Everywhere, and When They're Not"
IDEA: Collecting more lopsided data never makes it bell-shaped; averaging does, because an average's skewness is one piece's skewness over root n, and that only works when no single piece can outweigh the rest (finite variance).
SCORES: Hook 8.5 · Clarity 8 · Visual 7.5 · Motion 7.5 · Audio 8.5 · Concision 8 · Originality 8.5
WEIGHTED: 8.0   AFTER CEILING: 8.0  (lowest 7.5 + 2 = 9.5, not binding)
CAPS: none (the overlaps at 0:41.5 and 2:05 are mid-transition, about 0.5–1 s each, and every settled frame is clean, so I did not apply cap 7; they are fixes 5 and 6)
FINAL: 8.0   PASS: no
FACTS:
- Exponential waits have skewness 2; sample skew 1.90/1.96/2.01/1.98 at 10^2..10^5 | Verified | standard result; sim.py values match the screen
- Averages of 4/16/64 have skew 0.99/0.50/0.25, and skew(x̄) = skew(x)/√n | Verified | cumulant additivity: n·κ3/(nσ²)^{3/2}; needs a finite 3rd moment
- Coin p = 0.1: skew 2.67; share of heads in 64 flips: 0.33 | Verified | (1−2p)/√(p(1−p)) = 0.8/0.3; 2.67/8
- 2/√30 = 0.37 | Verified | 0.365
- Textbook "n ≥ 30 whatever the shape" | Verified | Montgomery & Runger 2010 as quoted in Kohavi et al. 2014 Rule #7; cited on screen at 1:33
- Kohavi et al. rule n ≥ 355·s² | Verified | Kohavi, Deng, Longbotham & Xu, KDD 2014, Rule #7 (PDF); cited on screen at 1:43. "Kohavi's team at Microsoft" is loose (Xu was at LinkedIn) but not wrong, and the screen gives all four authors
- 355·s² ⇔ s/√n ≤ 0.053 | Verified (algebra) | 1/√355 = 0.0531. Narration says "under point oh five", a rounding, so a nitpick only
- 355·2² = 1,420 ("fourteen hundred") | Verified | arithmetic
- Bing revenue/user skew "near 18", 114,000 users; capped at $10/user/week gives 5.2 and 9,700 | Verified | paper table (corrected 2015: 17.9 and 114k; 5.2 and 9.7k; the original text said 18.2 and 5.3)
- Lighthouse: uniform angle gives a Cauchy landing spot; the average of n Cauchy is Cauchy; the median of the max of 1,000 is about 919 mi ("about 900") | Verified | tan(π/2·0.5^{1/1000}) = 918.5; stability of the Cauchy distribution
- Gull 1988; Sivia & Skilling 2006 (lighthouse problem) | Verified | standard attribution; cited on screen at 2:09–2:17
- The median homes in (SD π/(2√n) = 0.05 mi at n = 1000) | Verified | asymptotic theory of the median
MECHANICS: runtime 3:02.1 · wpm 155 (speech) · max silence 1.97 s (planned prediction hold at 1:37.8) · max static 2.87 s · −14.0 LUFS / −1.9 dBTP · lead 0.0 s / trail 1.88 s · WER 3.9% (all diffs are homophones: waits/weights, week/weak)
```

## What I saw, beat by beat (flipbook)

- **0:00–0:12 cold open.** One blue histogram of 100 waits, labelled "simulated", with full axis labels. On "bell curve" (0:09) the arrow, "100,000 waits" and a dashed green bell with "?" appear, followed by a 2.0 s silent hold (0:10.5–0:12.5). The prediction prompt is clean and lands by 0:12.
- **0:12–0:29 stakes and naive build.** The A/B error-bar icons (yellow bars with green bells, which matches the palette) appear at 0:17 and then sit small at top-right until 0:29, long after they were mentioned. The counter ticks 100 → 1,000 → 10,000 → 100,000 on the spoken numbers (0:21–0:25). At 0:22.8 the counter morph shows a mid-glyph "1₀,000". The white exponential curve traces on "shape" (0:27–0:29). Sync here is good.
- **0:29–0:41 fail, measured.** A skewness chart is built, with "bell 0" turning green and four blue bars near 2. The definition E[(x−μ)³]/σ³ arrives as a finished FadeIn (scene.py:278), small and grey (cap height about 25 px), and is never spoken. The bars carry no value labels and the gap to the bell is not marked.
- **0:41–0:49 the fix.** At 0:41.0–0:41.5 the transition is messy. A stray axis segment floats mid-frame, the shrinking histogram's ghosted tick glyphs ("0", "40" at large size) overlap the incoming "skew = 1.98", and the "1.98" collides with the old tick labels. At 0:42.3–0:45.3 the four chips (5.2, 1.8, 25.7, 5.3) fly out, overlap "skew = 1.98" (0:43.0) and then collapse into a merged pill with garbled digits (0:44.0). The 9.5 average and the dilution of the 25.7 outlier, which is the whole mechanism of the episode, are never readable for more than about 0.9 s, and the narration never says why averaging cuts the lean.
- **0:47–1:14 readings and formula.** This beat is strong: the panels fill, the readings appear on cue, green bells are traced on "this perfect bell in green" (0:57), and the ×4 / ÷2 arcs sit on "grows four times / halves" (1:03–1:05). The 2/√n fractions are built from the header n values. At 1:11.0 and 1:12.5 the general formula assembles through glyph shatter: the digits of "1.98" morph into the letters of "skew(x)", leaving debris between the fractions. The ÷2 arrows sit about 13–15 px from the neighbouring "skew" labels (kf_13), under the 20 px minimum. Below y ≈ −1 the frame is empty from 0:45 to 1:05.
- **1:14–1:31 universality.** The coin's two spikes morph out of panel 1 and the n = 64 panel morphs into the exact binomial under the green bell. The dimmed n = 4 and n = 16 panels still show minute ticks (0–20, 5–15) under the shared label "share of heads in n flips" (kf_18), and the fraction row still reads 2/√64 = 0.25 while the coin reading is 0.33.
- **1:31–2:07 payoff.** The formula persists to the top of the frame, which is good. The board is mostly text: "textbook: n ≥ 30" and "textbook 30" on the axis say the same thing twice (kf_19). "?" holds for 2 s before 0.37 resolves (1:37.8–1:39.8). The log-axis markers are a good idea (30 / 1,420 / 9,700 / 114,000). At 2:05.0 the capped marker spawns exactly on top of the Bing marker, producing a doubled, illegible "Bingrevenue 114,000" for about 1 s. 0.37 is never shown as a picture: no n = 30 histogram that visibly leans.
- **2:07–2:52 lighthouse.** This is the best visual argument in the film. Beams land live, the red beam goes off-frame at 2:21 with "← 32 mi", flash 841 yanks the yellow running average at 2:29 ("902 mi →"), and the purple median flattens at 0 (kf_36). Two weaknesses. (a) "As scattered as a single flash" (2:35–2:41) is asserted by drawing two identical brackets (a TransformFromCopy of one onto the other); no data shows it. (b) The final frame (kf_36, 2:49–2:52) carries about 19 words of prose labels, two charts, two brackets, a red annotation and four hues. It has no single focal point. The upper chart's y label "landing spot (miles)" is really the running average or median.
- **2:52–3:02 landing.** It dips to the background for 0.53 s (2:52.8), then rebuilds the cold-open frame exactly. The dashed "?" bell is replaced by the yellow average-of-64 histogram under a solid green bell (kf_39). This is the right ending, and it lands on "It's in the average." The ident card overlays a dimmed final frame at 3:01.5, inside the 2 s limit.

**A/V sync.** Every deictic I checked lands within ±1 s: "this tail" 0:05, "here" 0:44–0:45, "this perfect bell in green" 0:57, "two spikes" 1:19, "Kohavi" with the citation swap at 1:43, "farthest … 900 miles" with "902 mi" at 2:29, "median" at 2:49. There is no drift and nothing is named that is not visible.

**Palette.** Blue = single pieces, yellow = averages, green = bell, red = extreme or infinite variance, purple = median. It holds without exception from 0:00 to 3:02, which is the episode's strongest craft asset.

## FIXES (highest impact first)

1. **[0:41–0:49][Clarity + Motion] The averaging gesture is rushed and its mechanism is never said.** The chips are legible for under 1 s and 9.5 is never readable (0:43.0, 0:44.0). Rebuild it as about 6 s:
   - Lay the four chips out in a row under panel 1 with ≥0.3 unit gaps, held 1.5 s, with 25.7 tinted RED (an extreme piece, consistent with the palette).
   - Narrate: "one long wait, twenty-five minutes, gets diluted by three short ones."
   - Merge them with a visible "÷ 4" into a yellow 9.5 chip, held ≥1.5 s, then drop it into panel 2.
   - Fund the time by cutting the sentence "Each panel zooms in, because averages crowd toward ten minutes" (0:57–1:02). Keep the dashed 10-minute line and the tick flag silent.
2. **[2:35–2:41][Clarity + Motion] "As scattered as a single flash" is asserted, not shown.** Replace the two copied brackets with data:
   - Drop 200 yellow dots (each the average of 1,000 simulated flashes) onto a second shore line directly under 200 blue single-flash dots, same axis.
   - Grow each "middle half" bracket from its own 25th and 75th percentile dots (TransformFromCopy from those dots), so the viewer sees the equal spread.
   - Keep the narration as is.
3. **[1:30–1:43][Clarity + Visual] 0.37 has no picture, and the payoff is a text board.**
   - Do not FadeOut the panel row at 1:30. Morph panel n = 16 into an n = 30 histogram of simulated averages with its green bell, so the right-lean is visible when "0.37" resolves.
   - Delete the redundant "textbook: n ≥ 30" text and keep only the axis marker "textbook 30".
4. **[2:41–2:52][Visual] The final lighthouse frame is cluttered** (kf_36: about 19 prose words, more than the 12 allowed, with split focus).
   - On "Here the variance is infinite", dim "902 ÷ 1,000 ≈ 0.9 mi", the red jump bracket, the ghost circle and both "middle half" brackets to 30%.
   - On "The median", dim the yellow average trace to 40% so purple is the only bright line.
   - Rename the upper y label to "running value (miles)".
5. **[0:41.0–0:42.0][Motion] The FadeTransform(big, pax[0]) produces ghosted, oversized tick glyphs and a floating axis segment, and "skew = 1.98" overlaps the old tick labels** (frames 0:41.0, 0:41.5).
   - Fade out the old axes and ticks first (0.4 s).
   - Then ReplacementTransform the bars only into panel 1's bars (same bin count), so the shrink reads as one object moving.
   - Bring in the n headers and empty panels, and only then FadeIn reads[0] (use Succession, not concurrent).
6. **[2:04.5–2:05.5][Motion / overlap] The capped marker copy is born on top of the Bing label, giving doubled text** (frame 2:05.0). Instead:
   - TransformFromCopy only the dot (mbing[1] → mcap[1]) along an arc to 9,700.
   - FadeIn the "capped / 9,700" label at its destination after the dot lands.
7. **[1:11–1:15][Motion] The general formula assembles through glyph shatter** (frames 1:11.0, 1:12.5: digits of 1.98 morph into the letters of skew(x)).
   - Build the numerator from the four blue "2"s of the fraction row (TransformFromCopy of f[0][0]), then TransformMatchingTex "2" → "skew(x)" in place with a 0.8 s flash.
   - Build √n from the √1..√64 denominators as now.
   - Centre the finished formula at x = 0 (it currently sits right of centre, about x 950–1480 px).
8. **[0:31–0:41][Visual + Motion] The skewness definition E[(x−μ)³]/σ³ is FadeIn'd as a finished equation, about 25 px cap height, never narrated** (kf_06, scene.py:278). Either delete it, or build it term by term with one spoken line ("the average cubed distance from the mean, so long waits dominate") at MathTex ≥ 36. Also:
   - Put value labels 1.90 / 1.96 / 2.01 / 1.98 above the four bars.
   - Draw a dashed green line at 0 with a brace "gap ≈ 2" on "two at every sample size".
9. **[1:04–1:31][Visual] The ÷2 arrows are 13–15 px from the adjacent "skew" labels** (kf_13, under the 20 px minimum). Shorten each arrow by 0.15 units at both ends, or raise the ÷2 arrows 0.2 units above the readings row.
10. **[1:19–1:31][Visual + Clarity] The coin beat leaves waits artefacts.**
    - Give the coin panels their own x-labels ("heads = 1" under n = 1, "share of heads" under n = 64) instead of the shared label over the dimmed waits panels.
    - Add "2.67/√64 = 0.33" under the coin's n = 64 panel, built by TransformFromCopy from the blue 2.67 and the n = 64 header, so the formula is verified on the second example.
11. **[1:49–1:53][Clarity] The jump from skew/√n ≤ 0.053 to n ≥ 355·skew² is announced, not shown.** Insert one 2 s TransformMatchingTex step: square both sides → n ≥ skew²/0.053² → n ≥ 355·skew², with "1/0.053² ≈ 355" flagged for 1 s.
12. **[1:42.9][Audio] "Kohavi's" was transcribed as "Cohave's", a likely mispronunciation.** Respell it phonetically in narration_text.py ("Ko-HAH-vee's") and re-synthesize that line.
13. **[0:17–0:29][Hook] The stakes are thin and the A/B icons idle for 10 s.**
    - Fade the icons out at "So collect" (0:21).
    - Sharpen the stakes line with the payoff number: "get this wrong and an A-B test on revenue needs thousands of times more users than the textbook says". This foreshadows 114,000 against 30 and raises tension into the payoff.

REACHES 9 IF ALL FIXED: yes. The structure is right: a misconception prompt, the naive method failing by a measured amount, a fix, a formula from data, a real cited consequence, a counterexample, and a return to the first frame. What holds it at 8 is execution in three beats: the averaging moment (fixes 1 and 5), the two asserted claims that should be shown (fixes 2 and 3), and the cluttered or overlapping frames (fixes 4, 6 and 7). Fixes 1–7 together lift Clarity, Visual and Motion to about 9, which gives a weighted score of about 9.0. Without fixes 1–3 it will not reach 9.

KEEP:
- The semantic palette, used without exception: blue pieces, yellow averages, green bell, red extreme, purple median.
- The cold-open frame returning at 2:53 with the dashed "?" bell replaced by the yellow average-of-64 under a solid green bell ("The bell was never in the data. It's in the average.").
- The live lighthouse simulation, with flash 841's red 902-mile beam visibly yanking the yellow running average while the purple median stays flat.
