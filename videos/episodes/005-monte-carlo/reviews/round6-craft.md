# Episode 5, review round 6 (craft critic: visual design, motion, A/V sync; all dimensions scored)

Evidence used: the `review/` pack (metrics.json 23:31 is newer than final.mp4 23:30), report.md, all 12 contact
sheets, full-resolution keyframes kf_01, 04, 05, 10, 12, 13, 17, 21, 23, 25, 29, 32, 35, 37, 39, plus extra frames I
pulled with ffmpeg at 0:17.3/17.8/18.5, 0:36.0, 0:45.0, 0:46.0, 0:46.6–0:52.6 (counter crops), 1:41.0, 1:43.8,
1:44.4, 2:10.6–2:13.0 (and a 0.1 s red-pixel scan of the histogram brackets, 2:11.0–2:13.5), 2:31.5–2:33.5,
2:36.6–2:40.4 and 3:19.4–3:20.5. Also read script.md, facts.md, narration.txt, transcript.txt, transcript_words.tsv
and narration_diff.txt; recomputed the closed-form numbers in Python.

```
EPISODE: 005 — "Why Random Darts Beat Grids in 100 Dimensions"
IDEA: With a fixed budget of N points, an even grid in d dimensions gets only about the d-th root of N values per axis and collapses to the single centre point by d = 20, while each random dart is an independent coin flip with chance equal to the answer, so the darts' typical miss is one dart's spread over root N, with no d in it.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6   AFTER CEILING: 8.6  (lowest 8.5 + 2 = 10.5; ceiling does not bind)
CAPS: none (runtime 3:33.6, 149 wpm, −14.0 LUFS / −2.0 dBTP, max silence 2.06 s, max static 2.97 s, 0 banned phrases, no settled overlap/typo/clipping found, every empirical claim cited on screen ≥ 3 s)
FINAL: 8.6   PASS: no
FACTS:
- 10^6 grid points in 100-D give 1 value per axis (floor(10^0.06) = 1) | Verified | recomputed
- 2^100 = 1,267,650,600,228,229,401,496,703,205,376, on screen @0:21 | Verified | recomputed; digits match kf_05
- Quarter disc r = √(2/π) = 0.798 has area exactly ½ | Verified | recomputed
- 10×10 midpoint grid: 52/100 inside, 2 points off; 100 darts: 44/100, 6 points off | Verified (darts simulated, labelled) | facts.md #5–6, data.json
- Half-volume ball radius 0.80, 0.98, 1.40, 1.82, 2.58, 5.77 (d = 2…100); d = 3 exact r³ = 3/π → 0.985 | Verified | recomputed d = 2, 3; rest facts.md #7
- Values per axis 1000/100/10/3/1/1; points used 10^6/10^6/10^6/59,049/1/1 | Verified | floor(10^(6/d)) recomputed (10^0.6 = 3.98, 10^0.3 = 1.995)
- Centre inside the ball from d = 20 (d/4 = 5 < 6.63), grid says 1.000, 50 points off | Verified | recomputed
- 2 values on 19 axes = 2^19 = 524,288 points, 17.6 ≈ 18 points off | Verified | P(Bin(19,½) ≤ 10) = 0.676
- Darts (10^6, simulated) stay under 0.1 point at all six shown d | Verified (simulated) | data.json, max 0.038
- 10^6 points on the diagonal: 57.7% inside, "8 points" spoken / 7.7 shown | Verified | t ≤ √(33.30/100) = 0.577
- Gauges 1.20 > 0.64 = 0.80² and 31.8 < 33.3 = 5.77² | Verified | data.json
- 300 runs of 100 darts spread ±4.8 pts in both 2-D and 100-D; theory ½/√100 = 5 pts | Verified (simulated) | facts.md #18–19b
- N independent ±½ misses: SD ½√N; share's miss ½/√N; general σ/√N with no d | Verified | derivation; Glasserman 2003 §1.1.1
- ½/√10^6 = 0.0005 = 0.05 points | Verified | recomputed
- Metropolis & Ulam 1949, JASA 44(247):335–341 (origin); Glasserman 2003 Springer (current practice; "option on 100 stocks" as a 100-input average) | Verified | facts.md #25–26 (quoted)
- Bergstra & Bengio 2012, JMLR 13:281–305: random search as good as grid in a fraction of the time; Fig. 1 nine grid trials test 3 values, nine random test 9 | Verified | abstract + Fig. 1 caption quoted in facts.md #28–29
- Radius-1 ball in 30-D fills 2.04 × 10^-14 of the box; below 10^-6 from d ≈ 17 | Verified | π^15/15!/2^30 = 2.041e-14 recomputed
MECHANICS: runtime 3:33.6 · wpm 149 (speech) / 139 overall · max silence 2.06 s (0:12.3, planned prediction hold) · max static 2.97 s · −14.0 LUFS / −2.0 dBTP · leading 0.0 s, trailing 1.6 s · WER 2.5 %
FIXES (highest impact first):
1. [2:05.6–2:12.4][Motion] The episode's only measured evidence that the spread is the same in 2-D and 100-D is rushed: the 300 runs finish filling ~2:10.5, the two "±4.8 pts" brackets are drawing from 2:11.3 and fully legible only 2:11.9–2:12.1 (red-pixel scan), and the whole panel is dimmed and gone by 2:12.3. "We measured 4.8" at 2:30.9 then refers to a number the viewer saw for ~0.3 s. → Add a 1.8 s hold after the brackets complete (wait(1.8) before the panel's FadeOut; insert [pause 1.0] after "spread this wide." in narration.txt), and instead of fading the histograms out, shrink both brackets (with their "±4.8 pts" labels) into a single "measured: ±4.8 pts" tag parked top-left, so the 2:31 "measured" line is that same object returning (TransformFromCopy), not a new Write. Lifts Motion and Clarity.
2. [2:59.8–3:07.8][Clarity] Coherence break: at 1:30.8 the episode voices and refutes "Maybe darts win by giving every axis more values" (the diagonal), yet the Bergstra–Bengio payoff explains random search's win with exactly that argument ("nine grid trials test three values of it; nine random trials test nine"), never reconciling the two. → Rewrite B18's second sentence as: "Only one setting mattered, so the question had one real input: nine grid trials tested three values of it; nine random trials tested nine." and flash the "important setting" axis label on "one real input". This tells the viewer why per-axis values matter here (low effective dimension) but did not rescue the diagonal.
3. [1:21.0–1:29.6][Visual] The d = 20–100 corner carries a five-line label stack ("grid says 1.000 / 50 points off / 2 values on 19 axes / 2^19 = 524,288 points / 18 points off") on top of the chart, its axis title and the three-row table: about 20 words of prose at once (kf_17), above the 12-word limit, and the hollow 17.6 dot sits 0.3 units under the 50 dot so the label stack visually floats between them. → On "Even two values", FadeOut "grid says 1.000" (keep only "50 points off" beside the d = 100 dot) and collapse the rescue stack to two lines: "2 values on 19 axes" and RED "18 points off", moving "2^19 = 524,288 points" into the "points used" row at d = 20 (replacing the dim "1" via swap()). Also dim the table to 30 % for this beat.
4. [1:07.0–1:27.0][Visual/Clarity] The BLUE darts line is drawn point-by-point from 1:09 while the narration talks only about the grid's values per axis; the darts are not mentioned until 1:27 and the line has no label until "darts (simulated)" at 1:29, and the PURPLE line is never labelled "grid" until 2:41. → Delay the darts dots until "while the darts stay" (1:26.8) and draw them all then (LaggedStart, 1.2 s); add a PURPLE "grid" end label at the d = 10 point when the purple line is first drawn (1:09).
5. [2:38.6–2:40.0][Motion] The returning dimension chart draws its two data lines before its axes are visible: at 2:39.2 the purple and blue segments float in empty space (two stray strokes at 2:39.0 on the contact sheet), and the axes fade in after. → FadeIn the axes, ticks and labels first (0.6 s), then Create the lines (1.0 s); or bring the chart back as one rigid FadeIn with shift=UP*0.3 since it is "the same data" returning.
6. [0:45.9–0:46.3, 0:50.6–0:51.1][Audio sync] The counters land about 1 s after the number is spoken: "52" ends at 0:46.34 but the count reads 32 at 0:46.6 and 52 at ~0:47.0; "44" ends at 0:51.10, count reads 30 at 0:51.4 and 44 at ~0:51.9. → Start each count-up 1.0 s earlier (begin on "puts" / "put" at 0:45.6 / 0:50.4) with run_time 1.0 so 52 and 44 land on the spoken word.
7. [2:12.1–2:20.0][Clarity] The single 16-step walk happens to end exactly at +4 halves (facts.md #19a), and the "4 halves" bracket then morphs to "√N halves", implying every walk ends at √N. → Ghost three more 16-step walks (other runs of darts, 25 % opacity, 0.8 s LaggedStart) ending at e.g. +2, −6, +4 before the bracket is drawn, and label the bracket "typically about 4 halves".
8. [1:41.6–1:56.6][Audio] "A dart's coordinates are drawn independently and uniformly, so it lands inside with a chance equal to the answer, in any dimension: each dart is a coin flip." is one 27-word, ~11 s sentence over two gauge animations; the review kit's longest breathless stretch (13.6 s from 1:30.8) is in this beat. → Split into "A dart's coordinates are drawn independently and uniformly. [pause 0.4] So it lands inside with a chance equal to the answer, in any dimension. [pause 0.6] Each dart is a coin flip."
9. [2:28–2:33][Visual] The check line renders "½ /√100" with a small inline ½ and a slash, a different notation from the stacked ½/√N directly above it. → Typeset it as MathTex(r"\frac{1/2}{\sqrt{100}} = 0.05 = 5\text{ pts}") or build it by TransformFromCopy of the main formula with N → 100 substituted (swap()).
10. [1:38–1:47 vs 2:37][Visual nit] "ball's edge" uses a straight typewriter apostrophe while "dart’s spread" at 2:37 uses a curly one. → Use ’ in both Text objects.
11. [2:52][Audio nit] Whisper heard "Berkstra"; the hard g may be soft in Kokoro. → Add a pronunciation override Bergstra -> /bˈɛɹɡstɹə/ and re-listen.
REACHES 9 IF ALL FIXED: yes. Fixes 1–4 lift Motion, Clarity and Visual to 9 (weighted ≈ 8.9), and 6–8 move Audio to 9 (≈ 9.0). No structural change is needed: the hook, the measured failure, the coin-flip picture, the derivation and the landing are already in place. The work left is pacing and label hygiene in three beats.
KEEP: (1) The 100-parallel-axes picture of a single point: the grid collapsing to one flat PURPLE centre line in the cold open, and the landing that floods the same frame with BLUE darts around it. (2) The ±½ coin bracket turning into the random walk, which builds √N·½/N → ½/√N from objects already on screen. (3) The diagonal "lockstep" counterexample (one flat line sliding as a whole, 57.7 % inside, 7.7 points off), which kills the "more values per axis" explanation on screen.
```

## Notes by beat (evidence behind the scores)

**Hook (9).** The first frame (0:00–0:01) is the object itself: "N = 1,000,000 points", a YELLOW d counter racing to 100 while the axes sweep in. The question "How many values does each input get?" ends at 0:12.3 and is followed by a 2.06 s planned hold before "One." (0:14.3). Most viewers will guess "plenty", so they are committed to a wrong answer. The open question "How far off would a million random points land?" (0:31.3) is answered exactly at 2:45.8–2:50.8 ("five hundredths of a point"), and the last frame (3:31, kf_39) is the cold-open frame seen again. One small sag: the payoff (2:50–3:08) moves to a different setting and argues by a different mechanism (fix 2).

**Clarity (8.5).** The order is concrete and checkable: 2-D first (the grid wins, 2 vs 6 points off), then the measured collapse, the voiced misconception (the diagonal), the mechanism (gauges → coins), the derivation (the walk) and a numeric check (5 predicted, 4.8 measured). Deductions: the payoff argument contradicts the debunked misconception (fix 2). 1:03–1:30 packs 8+ distinct numbers into 20 s, with the grid's rescue sentence the hardest to parse (fixes 3–4). The single walk landing exactly on √N over-sells the typical value (fix 7).

**Visual (8.5).** The palette holds for the whole episode (PURPLE grid, BLUE darts and N, YELLOW d, RED miss, INK truth), and there is generous negative space. Typography is uniform and the citations are well placed (kf_01, kf_35). The layout audit is clean and I found no settled overlap. Deductions: the crowded 1:21–1:29 corner (kf_17), lines left unlabelled during the climb, the inconsistent check notation at 2:29, and the apostrophe nit.

**Motion (8.5).** Most transforms carry meaning: the 100-D dart's first two coordinates become the 2-D dart (0:35–0:37); the square's edges travel onto the cube (0:59–1:03); the polylines shrink rigidly into their coins (1:55–1:59); the ½ bracket becomes the walk's steps (2:12–2:16); and the dashed 1/N line becomes the landing's rule (3:26–3:28). The static maximum is 2.97 s. Deductions: the histogram beat is rushed and then discarded (fix 1, the most damaging, because it is the "no d" evidence), the chart is redrawn out of order at 2:39 (fix 5), and the counters lag (fix 6).

**Audio (8.5).** Loudness is −14.0 LUFS at a −2.0 dBTP true peak and the pace is 149 wpm; the planned holds land (0:12.3 2.1 s, 1:29.0 1.8 s, 2:44.3 1.6 s). Deictics land: "the centre" label fades in from 0:17.3 against the word at 0:17.1; "this wide" brackets start at 2:11.3 against the word at 2:10.9–2:11.7; "no d" appears at 2:37.4 on "D" at 2:37.4; the 1/N line starts drawing at 3:19.4 on "this" at 3:19.4. Deductions: the 1:45 run-on sentence, the ~1 s counter lag at 0:46 and 0:51, and a possible soft g in "Bergstra".

**Concision (8.5).** At 490 words in 3:33.6 the episode is tight. About 5 % is removable: the "Even two values on nineteen axes" fairness patch (1:21.9–1:30.8) could be shown and not spoken, and "So, back to our ball" partly restates. Nothing is repeated.

**Originality (9).** The episode stays free of slop. Its images are non-obvious and memorable: parallel coordinates for a 100-D point, the grid reduced to the centre line, and the diagonal in lockstep. It also measures its own prediction (5 vs 4.8).
