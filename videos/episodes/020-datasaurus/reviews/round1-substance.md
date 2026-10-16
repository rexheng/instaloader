# Review: round 1, substance (science and story editor)

Evidence: `review/` pack (metrics.json 10:00 is newer than final.mp4 09:58, so it was reused). I read report.md, all 11 contact sheets and 9 full-resolution keyframes (kf_03, 07, 12, 14, 18, 21, 32, 34, 37). I also pulled 20 extra frames and crops at 0:32.6, 0:33.2, 0:33.6, 0:34.0, 0:34.4, 0:36.0, 0:48.8, 0:49.2, 0:56, 1:15, 1:50, 2:18.6, 2:19.6, 2:20.2, 2:21.4, 2:22.8, 2:24.4, 2:25.6 and 2:26.6. Every Datasaurus and Anscombe number was recomputed with numpy from the episode's data files, and the version-one star and fixed star were rebuilt from scene.py's own construction. Each citation was checked by web search.

```
EPISODE: 020 — "A Dinosaur Hiding in Your Summary Statistics"
IDEA: Two means, two SDs and a correlation pin down exactly one ellipse (centre, box, wall-touch height), so any shape with that ellipse, whether a dinosaur, a star or Anscombe's four sets, shares the five numbers and even the best-fit line; only a plot shows the shape.
SCORES: Hook 8 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8 · Concision 8 · Originality 8
WEIGHTED: 8.2   AFTER CEILING: 8.2
CAPS: none (0 banned phrases; all 3 empirical sources cited on screen; runtime 3:12.8; 155 wpm; −14.0 LUFS / −2.1 dBTP; max silence 1.96 s; max static 3.77 s; no black frames)
FINAL: 8.2   PASS: no
FACTS:
- Dino n = 142 | Verified | datasaurus_dozen.tsv (142 rows)
- x̄ 54.26, ȳ 47.83, s_x 16.76, s_y 26.93, r −0.06 | Verified (truncated first two decimals; raw 54.2633, 47.8323, 16.7651, 26.9354, −0.0645; ordinary rounding would give 16.77/26.94) | numpy; Autodesk Research page Fig. 5 quotes the same truncated values
- All 13 Dozen sets agree to two decimals | Verified under truncation: all 13 truncate to 54.26 / 47.83 / 16.76 / 26.93 / −0.06 (edge cases wide_lines s_x 16.76999962 and high_lines s_y 26.93999796 still truncate correctly) | numpy, 8-decimal check
- Version-one star: 50.00, 50.00, 20.51, 20.50, 0.00; s_y −23.9 % ("almost a quarter") | Verified | rebuilt from scene.py star_spots + match
- Fixed star equals the dino's five numbers "to every decimal place" | Verified (max diff 3e-14) | rebuilt fix
- "tip it just a hair" | Verified (shear coefficient a = −0.064, b = 0.998) | rebuilt
- Median y: 46.02 vs 52.16, "misses it by six" | Verified (46.0256 vs 52.1617) | numpy
- 1-SD ellipse touches right wall at ȳ + r·s_y; r → 1 moves it to the corner; at r = −0.06 it sits 1.74 below centre | Verified | derivation (support function of Σ)
- "That ellipse is everything the five numbers know" | Verified ((μ, Σ) ↔ ellipse is one-to-one for |r| < 1) | derivation
- OLS line passes through centre and touch point; slope r·s_y/s_x | Verified (cov/var_x = r s_x s_y / s_x²) | derivation
- Anscombe r = 0.82, slope 0.82·2.03/3.32 ≈ 0.50 | Verified (0.8164·2.0316/3.3166 = 0.5001; all four sets 0.4997–0.5001) | anscombe.csv
- Anscombe 1973, 11 points per set, The American Statistician | Verified | Anscombe, Am. Stat. 27(1):17–21, doi:10.1080/00031305.1973.10478966 (JSTOR 2682899)
- Matejka & Fitzmaurice 2017, CHI: random nudge, biased toward target shape, kept only if stats hold to two decimals; method agnostic to which statistics are held; 12 shapes grown from the Datasaurus | Verified | research.autodesk.com/publications/same-stats-different-graphs (Method; Fig. 5; abstract)
- Datasaurus drawn by Alberto Cairo, 2016, The Functional Art | Verified (blog post Aug 2016; the dino points are Cairo's DrawMyData redraw for the paper) | thefunctionalart.blogspot.com/2016/08/download-datasaurus-never-trust-summary.html
- Circle set's 3 points above the ring at 2:16 | Verified real data (y = 82.4, 85.6, 83.4) | numpy
MECHANICS: runtime 3:12.8 · wpm 155 (speech time) · max silence 1.96 s · max static 3.77 s · −14.0 LUFS / −2.1 dBTP
```

## FIXES (highest impact first)

1. **[2:40–2:51][Clarity]** The one formula in the episode is announced, not derived. "The best-fit line runs through the center and that touch point" is asserted, and slope = r·s_y/s_x then appears. Insert a 6–7 s TransformMatchingTex chain built from the on-screen box: `slope = cov/s_x²` → `= r·s_x·s_y / s_x²` → `= r·s_y / s_x`, with the cancelled s_x flagged for under 1 s. Narration: "Least squares sets the slope to covariance over x-variance. Covariance is r times s x times s y, one s x cancels, and what's left is the rise to the touch point over the run to the wall." Then keep the existing 0.82×2.03/3.32 ≈ 0.50 line. Pay for the time with fix 3.
2. **[1:15–1:21][Clarity/Visual]** During "Raise the correlation", the ellipse sweeps to r ≈ 0.88. Both readout columns still say r = −0.06 with a green "=" (kf_12 @ 1:18.0), so the screen contradicts itself. Attach a yellow live `DecimalNumber` "r = 0.88" (MathTex 36) 0.3 units right of the right-wall touch dot that tracks `rt`, and dim the readout to 35 % for the sweep. Alternatively, drive the readout's r cell from `rt` and turn the "now" cell to "≠" while r differs.
3. **[0:41–0:56][Motion/Concision]** The plot is frozen for about 15 s (sheet 3, 0:41–0:55). Only readout flags move while the narration says "the center moved, the x-spread grew, the y-spread shrank". Animate those as they are named: a red centre dot slides from (54.26, 47.83) to (50, 50) on "center moved", a red box widens on "x-spread grew" and flattens on "y-spread shrank". Cut "Version one only looked at the shape, never at the numbers" (0:49.9–0:53.2), which restates what the counter already shows. At 1:25–1:32, keep only "Now watch the ellipse" over the red-vs-yellow geometry. Net saving is about 5 s, which funds fix 1.
4. **[0:22–0:36][Hook]** The stakes are abstract ("When a report shows only these five numbers, how much can they hide?"). Give them one real sentence with a citation: "In 703 physiology papers, 85.6 % showed continuous data as bar graphs: averages and error bars, no points." On screen: "Weissgerber et al., 2015 · PLOS Biology" (doi:10.1371/journal.pbio.1002128; confirm n = 703 against the paper before use). This also gives the ending a real-world consequence. Today the payoff is two demonstrations (Matejka, Anscombe), not a consequence (BAR §6 Payoff).
5. **[0:00–0:14][Hook]** The title already says "Dinosaur", so the "Picture the scatterplot" commit is spoiled before 0:12, and the reveal at 0:19 confirms what the viewer was told. Move the commit to something the title doesn't give away. Example: "Picture the scatterplot. Where would its best-fit line go?" Hold the guess cloud with a grey dashed guessed line. The landing at 3:02 then pays off both the cloud and the line (the line really is fixed by the five numbers, as 2:51 shows). If the title is free to change, use "Five Numbers Can Only Draw One Shape".
6. **[2:19–2:27][Motion/Clarity]** Star, bullseye, X, stripes and dots each hold about 1.2 s (frames at 2:19.6, 2:20.2, 2:21.4, 2:22.8, 2:24.4, 2:25.6). That isn't long enough to check the claim "every one of them has this same ellipse". Give each shape about 2 s, keep the yellow box and both wall-touch dots on screen (they were dropped at 2:01) so the viewer can see the ellipse still touches at the same height, and leave the previous shape as a 25 % ghost.
7. **[0:33.0–0:33.5][Visual]** The "now" column is born on top of the dinosaur column, so for about 0.5 s every row shows mashed digits ("5426" over "54.26", crop @ 0:33.2). Shift each copy 1.4 units right before revealing it (`TransformFromCopy` with the target already offset and `path_arc=0`), or FadeIn the now column in its final position, 0.2 s staggered by row.
8. **[0:48.8–0:49.4][Visual]** Stray arc marks appear above the "o" and "a" of the "dinosaur" header while the s_y flag (red corner bracket) plays. Check `flag()`, which seems to draw a partial outline that clips the header, and limit the flag to a SurroundingRectangle on the "now" cell (buff 0.12).
9. **[0:35, readout][Clarity]** The readout uses truncated decimals (dino s_x 16.765 → "16.76"), which a viewer recomputing would round to 16.77. Add a grey 18-pt "first two decimals, as published" under the column header for 3 s at 0:34, or say "to two decimal places, the way the paper counts them".
10. **[2:57.3][Audio]** Whisper heard only a 0.8 s "a" where the TTS placed "a trend" (177.26–177.88). The word is probably swallowed. Re-synthesize the phrase as "a straight trend," or add a [pause 0.2] before it, then re-check the transcript.
11. **[1:35–1:45][Clarity, nitpick]** "Tip it" is a vertical shear, and the viewer is never told why it leaves the means and SDs untouched (the readout shows it, but not why). One clause would do: "tip it, a shear that slides each point up or down in proportion to x".

REACHES 9 IF ALL FIXED: yes, narrowly. The core is sound: an exact, original ellipse picture, a real build-fail-fix loop with live numbers, correct sources and an ending that re-sees the opening frame. Fixes 1–5 lift Clarity to 9 (derived formula, no contradicting readout), Motion and Concision to 9 (the fail beat animates instead of freezing), and Hook to 9 (a real stake plus an unspoiled commit). Originality stays at about 8–8.5 because the Datasaurus and Anscombe's quartet are among the most-shown examples in statistics teaching. That holds the overall to about 9.0, so fixes 1–5 are required, not optional.
KEEP:
- The ellipse built from the readout (1:01–1:21): dot from the means, box from the SDs, touch point from r. It is exact and memorable, and it is the episode's thesis.
- The three verb-synced repair moves (1:35–1:47): slide, stretch, tip, with the counter going 0 → 2 → 4 → 5/5, then honestly breaking on the median (1:55–2:00).
- The landing (3:02–3:11): the opening guess cloud returns, the ellipse draws through it and the dinosaur reappears around it. "The dinosaur lived in everything they leave out."

## Notes on scoring

- **Hook 8.** A concrete number-first cold open, with the commit prompt at 0:11–0:12.8 and a 1.9 s hold (0:12.6–0:14.6). The ending resolves the opening exactly. It falls short of 9 because the title spoils the reveal and the stakes (0:25–0:29) have no real-world anchor.
- **Clarity 8.5.** Every number checks out to the stated convention and every source is correct. The ellipse explanation would let a viewer re-derive the picture. Deductions: the slope formula is announced (2:40–2:51), and the frozen r readout contradicts the sweep (1:15–1:21).
- **Visual 8.** One flat background, a strict semantic palette (yellow summary, blue data, red drift, green match, always paired with =/≠), clean labels and correct citations at bottom-left. Deductions: transient digit mash (0:33.2), stray header marks (0:48.8) and the self-contradicting readout (1:18).
- **Motion 8.5.** The guess cloud travels into the dinosaur, the repair moves land on their verbs, and panel I shrinks into the quartet while ellipse and line copies fly to the other panels. Deductions: about 15 s with the plot frozen (0:41–0:56), and the dozen montage is too fast to read (2:19–2:27).
- **Audio 8.** 155 wpm at −14.0 LUFS, and the deictics land ("this bullseye" 2:20.6–2:21.8 on the bullseye; "these dots" 2:25.2 on dots). Deductions: "a trend" is possibly swallowed (2:57.3), and "Version one:" runs on with no pause after the colon (0:36.4).
- **Concision 8.** About 5–8 % is removable: the 0:49.9–0:53.2 restatement and part of the 1:25–1:32 replay.
- **Originality 8.** A well-worn example (Datasaurus plus Anscombe). The ellipse framing and the hand-built affine star are a genuinely fresh angle. No slop: zero banned phrases, no question chains, no "it turns out", and no recap ending.
