# Episode 5, round 6: substance review (science and story editor)

Evidence: `review/` pack (metrics.json 23:31 is newer than final.mp4 23:30, so it was used as is). I read report.md,
all 12 contact sheets, 13 full-resolution keyframes (kf_01, 07, 10, 18, 20, 21, 25, 27, 29, 33, 35, 37, 39), and
16 extra frames I extracted with ffmpeg (0:20.6, 0:21.2, 0:22.0, 1:00.6, 1:01.0, 1:02.0, 1:54.0, 2:11.3, 2:11.8, 2:12.3,
2:13.0, 2:32.6, 2:39.2 and others). I read the transcript, transcript_words.tsv, narration.txt, script.md, facts.md and
data.json. Every number was recomputed in Python (lattice counts, half-volume radii by fresh Monte Carlo, binomial
tail, ball volumes, the crossing point), and the three citations were checked by web search.

```
EPISODE: 005 — "Why Random Darts Beat Grids in 100 Dimensions"
IDEA: With a fixed budget of N points, an even grid gets only the d-th root of N values per axis and collapses to
      the single centre point in high dimension, while each random dart is an independent coin flip whose ±½ misses
      partly cancel, so the typical miss is ½/√N (σ/√N in general), with no d in it.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6   AFTER CEILING: 8.6   (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.6   PASS: no
```

## FACTS

| Claim | Status | Source / my check |
|---|---|---|
| 10^6 grid points in 100-D give 1 value per axis | Verified | floor(10^(6/100)) = floor(1.148) = 1 |
| The one grid point is the centre | Verified | midpoint rule, n = 1 gives (½, …, ½) |
| Two values per input would take 2^100 points (31-digit number on screen at 0:21) | Verified | 2^100 = 1,267,650,600,228,229,401,496,703,205,376, 31 digits, matches the frame at 0:21.2 |
| Quarter disc has average exactly ½ | Verified | r² = 2/π gives πr²/4 = ½ |
| 10×10 midpoint grid puts 52 inside, 2 points off | Verified | recount = 52; also counted dot by dot in kf_10 (8+8+8+7+7+6+5+3) |
| 100 darts put 44 inside, 6 points off | Verified (simulated, labelled) | data.json darts2d count 44 |
| Ball radius grows to keep half the box (0.80, 0.98, 1.40, 1.82, 2.58, 5.77) | Verified | my 400k-sample medians of ΣU²: r = 0.985, 1.403, 1.816, 2.576, 5.771; d = 3 exact 0.9847 |
| Values per axis 1000, 100, 10, 3, 1, 1; points used 10^6, 10^6, 10^6, 59,049, 1, 1 | Verified | floor(10^(6/d)), 3^10 = 59,049 |
| Grid misses 0.002, 0.001, 0.10, 2.4 points at d = 2, 3, 6, 10 | Verified | exact lattice DP: 0.50002 (from facts), 0.499989, 0.501022, 0.524463 |
| From d = 20 on, just the centre; it is inside the ball, so the grid says 1.000, 50 points off | Verified | 10^(6/20) = 1.995; d/4 = 5 ≤ 6.634, and 25 ≤ 33.30 |
| Two values on 19 axes (2^19 = 524,288 points) is 18 points off | Verified | P(Bin(19, ½) ≤ 10) = 0.6762, so 17.6 points |
| Darts stay under a tenth of a point (six runs) | Verified (simulated) | data.json errors max 0.038 |
| 10^6 diagonal points: 57.7% inside, 7.7 points off ("eight points") | Verified | t ≤ √(33.30/100) = 0.5771 |
| Gauges: 1.20 > 0.64 = 0.80²; 31.8 < 33.3 = 5.77² | Verified | data.json 1.1957 / 0.6366; 31.766 / 33.30; frame 1:54.0 |
| A dart with independent uniform coordinates lands inside with probability equal to the answer, in any d | Verified | uniform on the cube, so P(inside) = volume |
| One flip misses its average by exactly ½ | Verified | p = ½ |
| 300 runs of 100 darts spread ±4.8 points in both 2-D and 100-D | Verified (simulated) | SD 4.85 / 4.81 vs theory 5.0 |
| 16 darts stray about 4 halves; N darts about √N halves; typical miss ½/√N | Verified (math) | SD of a sum of N independent ±½ steps = ½√N. *Presentation issue, see fix 1* |
| ½/√100 = 5 points; measured 4.8 | Verified | |
| General f: σ/√N, no d | Verified | Glasserman 2003 §1.1.1: "the O(n^−1/2) convergence rate holds for all d" (Springer PDF, found by search) |
| A million darts: ½/1000 = 0.05 points | Verified | |
| Radius-1 ball fills 2 × 10^−14 of the 30-D box | Verified | π^15/15!/2^30 = 2.041 × 10^−14 |
| Below 1/N, under one hit expected, "usually report zero" | Verified | crossing at d = 17.06; at d = 18, P(0 hits) = e^(−0.313) = 0.73 (facts.md says 0.75 and 2.9e-7, actual 3.13e-7; neither is on screen) |
| Metropolis & Ulam, 1949 · JASA | Verified | JASA 44(247):335–341, Sept 1949 (T&F, PubMed 18139350, JSTOR scan) |
| Glasserman, 2003 · *Monte Carlo Methods in Financial Engineering*, Springer | Verified | Springer, Applications of Mathematics 53 |
| Bergstra & Bengio, 2012 · JMLR: random search found nets as good as grid search in a fraction of the time | Verified | JMLR 13(10):281–305; abstract: "as good or better within a small fraction of the computation time" |
| "Nine grid trials test three values of it; nine random trials test nine" | Verified | same paper, Figure 1 caption |

No factual or mathematical errors were found. No cap is triggered.

## MECHANICS

runtime 3:33.6 · 149 wpm over speech time (496 words heard / 490 scripted) · max internal silence 2.06 s (0:12.3) ·
leading 0.00 s / trailing 1.63 s · max static 2.97 s · −14.0 LUFS / −2.0 dBTP · WER 2.5 % · 0 banned phrases
(I also checked the §4 patterns by hand: no question chains, no "it turns out", no "not just X", no recap ending).
Every caps threshold is clear.

## What holds it below 9 (evidence)

1. **Clarity, the crux step is asserted from one hand-picked walk (2:12–2:27).** The √N law is the whole episode,
   and the only evidence on screen is a single 16-step walk that lands exactly on +4 halves ("4 halves", kf_27 at
   2:21.5). That walk is darts 62–77 of the 2-D run (facts #19a), a window that does not start on a block boundary
   and happens to hit √16 exactly. The six consecutive 16-dart blocks of the same run land at −10, +2, −2, 0, +4 and
   −4 halves (I computed this from data.json). A viewer leaves thinking 16 darts land at 4. They cannot re-derive
   why it is √N rather than N/2 or log N: "partly cancel" explains less than N, not √N.
2. **Clarity and story, the payoff brings back the misconception the episode just refuted (1:30.8 vs 2:59.8).**
   At 1:30.8 the narration voices "Maybe darts win by giving every axis more values" and kills it with the
   diagonal (7.7 points off). At 2:59.8 the payoff's mechanism is exactly that: "nine grid trials test three values
   of it; nine random trials test nine", with 3 vs 9 shadows on screen (kf_35). Nothing says the job has changed from
   averaging to searching, or that one important axis makes the search one-dimensional. A careful viewer hears a
   contradiction in the last 40 seconds.
3. **Visual and Motion, the measured spread is not readable (2:11.3–2:12.3).** On "this wide" the two RED
   "±4.8 pts" brackets grow from 2:11.0 to 2:11.8, then dim by 2:12.3 (extracted frames), so they are fully legible
   for about 0.5 s against the §5 minimum of 1.5 s. This is the measurement the formula is later checked against
   ("We measured 4.8", 2:30.9).
4. **Motion, the 2-D to 3-D inflation has a double outline (1:00.6–1:01.5).** At 1:01.0 the 2-D disc's arc and its
   dark fill stay inside while a second, larger arc grows outside it, giving two concentric quarter arcs. At 1:00.6
   a stray stroke pokes past the cube's lower-right corner. It reads as a ghost, not as "the disc becomes a ball".
5. **Audio, the misconception and its refutation run together (1:30.8–1:44.4).** report.md logs 13.6 s with no
   breath of 0.35 s or more. "Maybe darts win by giving every axis more values" gets only a 0.3 s pause before
   "A million points on the diagonal". The turn from the voiced wrong idea to its refutation should be the most
   audible pause in the act. Minor: "noticed" is heard as "notice" (3:27.6), which drops the past tense the landing
   line depends on, and "Bergstra" is heard as "Berkstra" (2:52.0).
6. **Concision, the same point is made twice.** "Two values per input would take two to the hundredth points"
   (0:18–0:21.7) and "Even two values on nineteen axes is eighteen points off" (1:21.9–1:26) both make the point
   that two values per axis costs 2^d. The second one earns its place as a budget-fairness check. Together they cost
   about 9 s at the 3:33 end of the runtime band.

## FIXES (highest impact first)

1. [2:12–2:27][Clarity] One cherry-picked walk lands exactly on √16, so √N is shown by coincidence rather than
   derived. **Change:** draw all six consecutive 16-dart blocks of the 2-D run as faint walks from one origin (their
   ends are −10, +2, −2, 0, +4, −4 halves), keep one bold, and put a RED bracket at the typical (root-mean-square)
   stray, which is 4.8 halves for these six. On "sixteen darts stray about four halves, not sixteen", flash the
   16-halves staircase that none of them reaches. If 6 s can be afforded, add the actual reason as one line: "Squared
   misses add: sixteen quarters make four, and its root is two, four halves." That lets the viewer re-derive √N.
   Clarity 8.5 → 9.
2. [2:59.8–3:07.8][Clarity/Hook] The payoff's "more distinct values" mechanism contradicts the diagonal's lesson.
   **Change the narration to:** "Searching is a different job from averaging. When one setting matters most, the
   search is really one-dimensional: nine grid trials test three values of it; nine random trials test nine."
   (+9 words.) On "different job", flash the important-setting axis in both panels. The diagonal then still stands
   for averaging, and B&B is framed as low effective dimension, which is the paper's own argument (its §1).
3. [2:10.4–2:13.0][Visual/Motion] The ±4.8 brackets are legible about 0.5 s. **Change:** start growing both brackets
   on "spread" (2:10.4, word timing 130.4), hold them at full opacity until 2:13.0, and dim the histograms to 30 %
   instead of removing them while the walk builds above. That gives a ≥1.5 s hold, and the "measured ±4.8" check at
   2:30.9 can then TransformFromCopy from the dimmed bracket rather than appear as new text.
4. [1:30.8–1:35][Audio] There is no breath between the voiced misconception and its refutation. **Change:**
   `[pause 0.3]` → `[pause 0.8]` after "more values." Re-time the shadow drop so "100 values on one axis" holds
   through the pause. In the landing, respell "noticed" (e.g., "notissed") or add a 0.15 s pause after it so the -d is
   audible; give "Bergstra" a phoneme override (/bˈɜːɡstɹə/).
5. [1:00.6–1:01.5][Motion] There is a double arc and a stray stroke during the ball's growth. **Change:** fade the 2-D
   disc's fill and arc to 0 over the first 0.3 s of the inflation, or Transform the 2-D arc itself into the 3-D
   outline so that only one boundary exists at any moment, and clip the growing outline to the cube.
6. [3:18.8–3:25.8][Clarity] The limit beat switches from absolute error (every earlier chart is in percentage points)
   to relative error without saying so. Here the darts' absolute miss is 2 × 10^−12 points, their best of the episode.
   **Change:** "…so they usually report zero: a tiny miss, but the whole answer." Keep the "off by the whole answer"
   label. (+5 words; offset by fix 7.)
7. [1:21.9–1:30.8][Concision] There are two "two values cost 2^d" beats. **Change:** shorten the rescue line to
   "Two values on nineteen axes: still eighteen points off." Keep the on-screen stack (2 values on 19 axes ·
   2^19 = 524,288 points · 18 points off). This saves about 2 s and pays for fixes 2 and 6.
8. [facts.md #24][Correctness hygiene, not on screen] P(0 hits) at d = 18 is 0.73 and the share there is 3.13e-7,
   not 0.75 and 2.9e-7. Correct the fact sheet.

REACHES 9 IF ALL FIXED: yes, but narrowly. With fixes 1–2, Clarity reaches 9. With fixes 3–5, Visual, Motion and
Audio reach 9. Fix 7 holds Concision at 8.5–9. Expected weighted score is 8.95–9.1. The structure is right: there is
a hook, a naive build, a measured failure, a voiced misconception, the insight and an honest limit. What remains is
the rigour of the √N step and the logic of the payoff, not structure.

KEEP:
- The 100 parallel axes as "one point", with "One." answering the cold-open question, and the same picture returning
  at the landing as a blue flood over the single purple centre line.
- The voiced misconception killed by the diagonal ("57.7 % inside: 7.7 points off", "their coordinates move in
  lockstep"). It is the most original beat in the episode and it states the mechanism.
- The same dart gauged in 2-D (1.20 > 0.64, outside) and in 100-D (31.8 < 33.3, inside), then collapsing to a coin;
  together with the identical 2-D/100-D histograms this is the picture that makes "no d" visible.
