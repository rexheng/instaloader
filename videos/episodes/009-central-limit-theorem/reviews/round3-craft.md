# Round 3: craft critic (visual design, motion, A/V sync; every dimension scored)

Evidence: the `review/` pack. Its metrics.json (21:54) is newer than final.mp4 (21:52), so I reused it. I read:

- report.md, narration_diff.txt, transcript.txt and word timings (around 1:52–2:08 and 3:30–3:34)
- all 13 contact sheets
- full-resolution keyframes kf_02, kf_08, kf_10, kf_15, kf_18, kf_21, kf_24, kf_25, kf_28, kf_32, kf_34 and kf_40
- extra frames I extracted at 0:05.5, 1:18.6, 1:19.2, 1:30.5, 2:38.4, 2:39.6, 2:40.2, 2:40.8, 3:42.4, 3:43.4, 3:44.2 and 3:54.5
- script.md, narration.txt, facts.md and the round-2 craft review

I recomputed the tails with scipy:

- Gamma(30): 1.403% / 3.402%
- Gamma(1420): 2.351% / 2.645%
- 355·17.9² = 113,746 and 355·5.2² = 9,599
- 1/√355 = 0.0531 and 2/√30 = 0.365

```
EPISODE: 009 — "Why Bell Curves Are Everywhere, and When They're Not"
IDEA: Collecting more lopsided data never makes it a bell; averaging does, because an average's skewness is one piece's over root n (its tail weight over n), which for bus waits means about 1,420 per average, not the textbook's 30, and only while no single piece can outweigh the rest (finite variance).
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8 · Concision 8.5 · Originality 9
WEIGHTED: 8.6   AFTER CEILING: 8.6 (lowest 8 + 2 = 10, not binding)
CAPS: none
FINAL: 8.6   PASS: no
FACTS:
- Exponential waits skew 2; samples 1.90/1.96/2.00/1.98 | Verified | exact exponential skew = 2; sim.py values in facts.md
- skew(x̄) = skew(x)/√n; 0.99/0.50/0.25 at n = 4/16/64 | Verified | third cumulant additivity, re-derived (n·k3 / (nσ²)^{3/2})
- "4 over 8, half the lean"; n / n^{3/2} | Verified | E[(S−4μ)³] = 4·k3 (cross terms vanish), SD(S)³ = 8σ³
- Coin p = 0.1: skew 2.67; 64 flips 0.33 | Verified | 0.8/0.3 = 2.667; /8 = 0.333
- kurt(x̄) = kurt(x)/n (excess kurtosis) | Verified | fourth cumulant additivity
- 2/√30 = 0.37; tails 1.40% / 3.40% vs 2.5% | Verified | scipy: 0.365; 1.403% / 3.402%
- Kohavi et al. 2014 KDD Rule #7: n ≥ 355·s², each tail 2–3% | Verified | paper text quoted in facts.md; matches the paper
- 1/√355 ≈ 0.053; 355·2² = 1,420; tails 2.35% / 2.64% | Verified | scipy 0.0531; 2.351% / 2.645%
- Bing Revenue/User skew ≈ 18 → 114,000; capped $10/user/week → 5.2 → ≈ 9,600 | Verified | 113,746 / 9,599; paper table (Jan 2015 correction)
- "Textbooks say 30" (Montgomery & Runger 2010, via Kohavi) | Verified | quoted in Kohavi et al. 2014
- Cauchy: farthest of 1,000 ≈ 900 mi; half within 1 mi, for single flashes and for 1,000-flash averages | Verified | median max = tan(π/2·0.5^{1/1000}) ≈ 918; mean of Cauchy is Cauchy
- "on revenue data, thirty is off by a factor of thousands" (0:15) | Verified, but no citation on screen at 0:15 | 114,000/30 = 3,800; the citation only appears at 2:17
MECHANICS: runtime 3:54.9 · 158 wpm (speech) / 154 overall · max silence 2.0 s (0:11.6 planned prediction hold) · max static 3.8 s (0:10.9–0:14.7, prediction hold) · −14.0 LUFS / −1.6 dBTP · lead 0.0 s / trail 1.9 s · WER 3.1% · 0 banned phrases · layout audit 0 issues
FIXES (highest impact first):
1. [2:38.5–2:41.0][Motion/Clarity] The 1,420 result is the answer to the cold-open question: panel n = 1,420, meter bars 2.35% / 2.64% inside the gray 2–3% band. It is fully lit for only about 1.0 s (frames 2:39.6 → 2:40.6) and dims at 2:40.8 as the Bing line starts. The 1.5 s reading minimum is violated on the episode's key payoff. Fix: add a [pause 1.2] after "both tails land inside". On "inside", Indicate both meter bars and the band together (green outline, ≤ 1 s). Start the dim only on "Bing's". The finished state should be held ≥ 2.5 s.
2. [1:18.6–1:32][Visual/Motion] When the formula opens, frame 1:18.6 shows an orphan "=" colliding with the fraction bar of skew(x)/√n, and frame 1:19.2 a floating duplicate "skew(x)". From 1:20 to 1:31 the equation reads "skew(x̄) =  [empty]  · E[(x−μ)³]/σ³". A dangling multiplication dot with nothing before it looks like a broken equation for about 11 s. Fix: open it with TransformMatchingTex, keeping "= skew(x)/√n" fixed and fading the old copy out before the new terms arrive. Put a dashed gray rounded box (the size of n/n^{3/2}) in the empty slot from 1:20. The "×n" and "×n^{3/2}" labels then fly into that box at 1:31.
3. [1:20–1:30][Clarity/Motion] The block stacks are unlabeled rectangles (frame 1:30.5). "The spread only doubles" is asserted, not shown, and that is the step a viewer has to take on trust. Fix: caption the stacks "cubed gaps" (blue) and "spread³" (gray), at Text font_size ≥ 18 under each stack. On "spread only doubles" (1:24.5), grow a gray horizontal bar of length σ to 2σ above the gray stack (label "×2"). On "its cube grows eight times", stack 2×2×2 = 8 blocks from that bar.
4. [whole episode][Audio] The cadence is metronomic: about 70 of the gaps in the silence list are 0.4–0.6 s, at almost every sentence boundary regardless of beat. Fix: in narration_text.py, cut the gaps inside a beat to 0.2–0.3 s and put 0.8–1.0 s pauses only at beat boundaries (0:43.9, 1:17.9, 1:34.6, 1:58.1, 2:52.3, 3:30.5, 3:42.4). That also buys about 6–8 s for fixes 1 and 3. The "so" at 3:32.25–3:33.0 lasts 0.76 s, and whisper heard it as "so so". Regenerate that clip, or rephrase to "The theorem needs finite variance: no single piece can outweigh the rest."
5. [3:31–3:42][Visual] The lighthouse end frame (kf 3:37.0) carries about 15 prose labels: miles, average, 1,000 flashes, 1 mi, variance < ∞, middle half, one flash, miles, ← 12, 12 →, average of 1,000, simulated. That is over the 12-word limit, with two competing focal areas (the trace on top, the two brackets below). Fix: on "The theorem needs finite variance" (3:30.5), dim the top running-average chart to 30% and fade out "1 mi" and the lighthouse glyph label. Restore the trace on "The median" (3:38.3), when the purple median is drawn on it.
6. [2:09–2:52][Visual] The tail meter has no reference labels of its own. The green dashed line and the gray band are unlabeled (kf 2:20.1, 2:30.9), so the viewer has to map the "2.5%" and "2–3%" text on the panel's cut lines over to the meter. Fix: put a green "2.5%" Text (font_size ≥ 18) at the right end of the dashed line. On "two and three percent", transform it into a gray "2–3%" beside the band. Add a gray "in each tail" caption under left/right.
7. [0:13.6–0:20][Clarity] "On revenue data, thirty is off by a factor of thousands" is an empirical claim with no citation on screen until 2:17. Fix: show "Kohavi et al., 2014 · KDD" (gray, bottom-left, above y = −3.2) from 0:15 to 0:20.
8. [0:00, 0:40, 0:46][Audio/Clarity] "Waits" and "weights" are homophones, and whisper heard "weights" 7 times. An audio-only listener at 0:00 hears "a hundred bus weights". Fix: say "A hundred waits for a bus" at 0:00 and "These waits for a bus score about two" at 0:40. Keep "bus waits" elsewhere.
9. [2:53, 3:43][Motion] Two dissolves leave a frame almost empty during live narration: the 2:53 sheet frame is almost blank on "Now the condition", and so is the 3:43.0 frame on "So the answer is over a thousand". Fix: overlap the fades by 0.3 s (start the incoming scene when the outgoing one is at 30%), so no frame under speech is over 80% background. Keep the shore line morph.
10. [0:47–1:58][Visual] The y-label "share" sits in the header row and reads as "share n = 1" (kf 0:53.5, 1:11.3). The coin panel (1:37–1:58) has no vertical axis, while panel 4 does. Fix: rotate "share" to sit beside panel 1's y-axis, mid-height, and keep panel 1's y-axis line when it becomes the coin.
11. [3:52–3:55][Visual] The landing x-ticks "9.5 10.0 10.5" are cramped (kf 3:54.9, about 25 px apart) on the most important frame. Fix: show only "9.5" and "10.5", or "10" alone with the "minutes" label.
REACHES 9 IF ALL FIXED: borderline yes. Fixes 1–3 lift Motion and Visual to about 9 and Clarity to about 9. Fixes 4 and 8 lift Audio to about 8.5. That gives about 8.95–9.0. No structural change is needed: the hook commits by 0:12, the fail beat is measured (skew 1.90–2.00 at every sample size), the insight runs from picture to formula, the payoff is cited, and the landing re-sees the cold open. What stands between this and a 9 is the payoff's 1 s hold and the abstract, half-asserted root-n blocks.
KEEP:
- The cold open is a committed numeric prediction (30 / 300 / 1,000+ chips). The landing lights 1,000+, relabels the arrow "average of 1,420" and grows the real green bell over the averages: "The bell was never in the data. It's in the average."
- The panel row (kf 1:11.3): ×4 header arrows, ÷2 reading arrows and per-panel 2/√n converging into skew(x̄) = skew(x)/√n. The episode's formula is read straight off the data.
- Kohavi's 355·s² rule rearranged on screen into the episode's own skew/√n ≤ 0.053, with the log sample-size axis 30 → 1,420 → 114,000 → 9,600 and the tail meter that turns 1.40% vs 3.40% into a shape.
```

## Notes by dimension

**Hook (9).** The first frame is the 100-wait histogram. The textbook claim is on screen with an "average of 30" arrow by 0:07, and the three guess chips are complete by 0:11, followed by a 2.0 s prediction hold (0:11.6–0:13.6). Stakes come at 0:13.6–0:19.9: A-B tests, "off by a factor of thousands". The ending answers the exact question asked: the 1,000+ chip lights at 3:44 and the arrow label becomes "average of 1,420". This meets the 9 anchor. It is not a 10 because the first frame is a plain histogram and not yet the irresistible question; the question builds over 11 s.

**Clarity (8.5).** The order is concrete first:

- skewness is built term by term from the x − μ arrow, including the leftward x − μ < 0 arrow (0:31–0:37)
- four real chips are averaged into a dot (0:47–0:53)
- the readings 0.99/0.50/0.25 come before 2/√n, which comes before the general formula
- the universality check (the coin), then the tails, then Kohavi

Every number I recomputed checks out. Deductions:

- The root-n "why" (1:18–1:33) uses unlabeled block stacks, and "the spread only doubles" (√4 = 2) is asserted (fix 3).
- The payoff that answers the hook is on screen for about 1 s (fix 1).
- 2:05–2:52 is dense: tails, then Kohavi, then the rearrangement, then 1,420, then Bing, then capping, in 47 s. It is readable, but right at the limit.

**Visual (8.5).** The palette holds across the episode: blue for pieces, yellow for averages, green for the bell, red for the extreme piece, purple for the median, gray/ink for rules and sample sizes. The round-2 fix moved the markers to INK. The background is flat, every chart is tagged "simulated" or "exact", citations sit bottom-left above y = −3.2, and the "central limit theorem" title now has real hierarchy (kf 1:54.7). Most frames have one focal point. Remaining issues:

- the dangling "·" equation for about 11 s (fix 2)
- the lighthouse end frame over the word budget (fix 5)
- the unlabeled meter references (fix 6)
- the "share" header ambiguity and the coin panel with no axis (fix 10)
- the cramped landing ticks (fix 11)

That is more than two minor issues, but none is a cap trigger. The layout audit found 0 overlaps in settled frames.

**Motion (8.5).** Motion mostly encodes relations:

- the 1.98 label flies to "skew = 1.98"
- chips arc out of their bars and the 9.5 drops into panel 2
- 2/√n copies converge into one formula, which then morphs into the general one
- a copy arcs down into kurt(x̄)
- the "30" flies from the panel into the radicand
- the n = 30 panel morphs into the exact n = 1,420 distribution while the meter bars slide into the band
- the 902-mile beam yanks the trace
- the shore line slides into the waits axis at the landing

Round-2 problems are gone: the double exposure, the bar-height pulse, the "mi" axis, and the cut-short final image (it now holds about 2 s). Remaining issues: the 1 s payoff hold (fix 1), the transient collision at 1:18.6–1:19.2 (fix 2), and two near-empty dissolve frames under speech (fix 9).

**Audio (8).** Loudness is on target (−14.0 LUFS / −1.6 dBTP) at 158 wpm. Deictics land:

- "tail" with the brace at 0:03
- "here" with the dot at 0:53
- "this perfect bell in green" with the curves appearing at about 1:05
- "900 miles" with "902 mi →" at 3:13–3:15
- "Half of single flashes" with the bracket at 3:23

The deductions are the uniform 0.4–0.6 s sentence gaps, the drawn-out "so" at 3:32, and the waits/weights homophone (fixes 4 and 8).

**Concision (8.5).** At 3:55 it sits at the ceiling, but I could not find a sentence that carries nothing. The densest optional beat is the capping line (2:46–2:52). I keep it, because it is the "honest outcome / how practitioners fix it" note. Slack is under 10%.

**Originality (9).** Deriving an industry rule of thumb (Kohavi's 355·s²) from the episode's own skew/√n, and answering the textbook-30 question with "1,420, for these waits", is a non-obvious angle viewers would share. "The bell was never in the data. It's in the average" is a memorable reframe of the cold open. The lighthouse is classic (Gull 1988), but it is staged as a live measurement.
