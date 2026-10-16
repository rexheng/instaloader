# Episode 5, review round 3 (craft critic: visual design, motion, A/V sync)

**Evidence.** I used the existing `review/` pack, because metrics.json (22:24) is newer than final.mp4 (22:22). I read report.md, all 13 contact sheets, transcript.txt, transcript_words.tsv, narration_diff.txt, narration.json word timings, script.md, facts.md, CHANGELOG.md and the round-2 craft review.

Full-resolution keyframes read: kf_01, 03, 06, 09, 11, 15, 19, 22, 23, 24, 26, 27, 28, 30, 32, 33, 35, 37 and 40.

Extra frames pulled with ffmpeg: 0:18.6, 0:36.3, 0:37.0, 0:37.6, 1:02.0, 1:03.0, 1:04.0, 1:18.6, 1:29.3, 1:32.0, 1:59.0, 2:00.5, 2:05.2, 2:05.8, 2:12.6, 2:13.4, 2:14.0, 2:16.6, 2:17.4, 2:25.5–2:30.5 (1 s steps), 2:43.0, 2:44.2, 3:16.4, 3:16.9, 3:17.4, 3:24.5–3:26.5 and 3:33.4–3:34.4.

Other checks:
- **Audio energy.** I measured audio energy around 2:43.8, because the transcriber dropped "Back".
- **Recomputed numbers** (in Python): 2^100 digit count, the 10×10 grid count (52), floor(10^(6/d)), 3^10 and 4^10, P(Bin(19, ½) ≤ 10), the diagonal cutoff √(33.302/100), the radius-1 ball share at d = 17, 18 and 30, ½/1000, and 0.683^6.

```
EPISODE: 005 — "Why Random Darts Beat Grids in 100 Dimensions"
IDEA: A grid of N points in d dimensions gets only N^(1/d) values per axis and collapses as d grows. Each random dart independently lands inside with probability equal to the answer, so the darts' error is one dart's spread over √N (½/√N for this yes/no ball), with no d in it. The exception is an answer so tiny that a million darts expect no hit.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.4 (842.5/100 = 8.425)   AFTER CEILING: 8.4 (lowest 8 + 2 = 10, does not bind)
CAPS: none.
  - Overlap/clipping (cap 7) checked. Nothing in a settled frame overlaps or leaves the safe area. The closest calls:
    - Formula vs dimmed titles: 45–67 px apart @2:35.6 (kf_28).
    - "no d" vs the dimmed "±2.4 pts": about 30 px apart @2:43.6 (kf_30).
    - Right-edge "typical miss" label ends at x ≈ 1815 px (6.33 units) @2:59 (kf_33).
    The automatic audit's 5 allowances are glyphs inside one LaTeX formula; I accept them.
  - Sync cap checked. Every deictic I timed lands:
    - "this wide" @2:27.5 → bracket grows from 2:27.5.
    - "just as wide" @2:29.9 → 100-D bracket by 2:30.5.
    - "Below this line" @3:25.4 → the 1/N line is drawn 3:25.5–3:26.0.
    - "like this one" @0:30.4 → the polyline is drawing.
    - "this quarter disk" @0:39.3 → the arc and fill are in by 0:41.
  - Static: max 2.97 s. Dead air: max 1.73 s (the planned hold at 0:10.0). Runtime 3:42.2. Pace 163 wpm over speech time. −14.0 LUFS / −2.1 dBTP. No banned phrases, no rhetorical-question chains. Every empirical claim has an on-screen citation (Glasserman 0:21–0:27, Metropolis & Ulam 0:25–0:32, Bergstra & Bengio 3:01–3:16).
FINAL: 8.4   PASS: no
FACTS:
  1,000,000 grid points in 100-D → 1 value per axis, the centre | Verified | floor(10^0.06) = 1
  Two values per input → 2^100 points (31 digits on screen) | Verified | len(str(2**100)) = 31
  Quarter disc r = √(2/π) has area ½; the 10×10 midpoint grid has 52 inside, 2 points off | Verified | recomputed: 52
  100 darts → 44 inside, 6 points off (labelled "simulated") | Verified (simulated) | sim.py / facts #6
  The ball covers exactly half the box in every d; r = 0.985 at d = 3 | Verified | r³ = 3/π; facts #7 (exact CDF + MC cross-check)
  Values per axis 1000/100/10/3/1/1; points used 10^6/10^6/10^6/59,049/1/1 | Verified | floor(10^(6/d)); 4^10 = 1,048,576 > budget
  From d = 20 on, one value; the centre is inside the ball; grid says 1.000, 50 points off | Verified | 10^0.3 = 1.995; d/4 = 5 < r²₂₀ ≈ 6.63
  Largest two-value grid that fits (2^19 points) is 18 points off | Verified | P(Bin(19, ½) ≤ 10) = 0.6762 → 17.6
  Darts stay under 0.1 points in every d (six simulated runs) | Verified (simulated) | facts #13, max 0.038
  Grid 100 points → 10 shadows; darts 100 → 100; N^(1/d) | Verified | algebra
  Diagonal: 10^6 points, every axis 10^6 values, 57.7% inside, 7.7 points off | Verified | cutoff t = √(33.302/100) = 0.5771
  Gauges: 1.20 > 0.64 (outside), 31.8 < 33.3 (inside) | Verified | data.json via facts #16a
  One flip misses its mean ½ by exactly ½; spread = ½/√N; ×4 darts halves it | Verified | Bernoulli(½) SD = ½
  300-run histograms ±4.8/±4.8 → ±2.6/±2.4 points | Verified (simulated) | theory 5.0 → 2.5
  General f: σ/√N with no d | Verified | Glasserman 2003 §1.1.1 (quoted in facts.md)
  ½/√10^6 = 0.0005 = 0.05 points; two runs in three land closer; all six of ours did | Verified | P(|Z| < 1) = 0.683; 0.683^6 = 0.10
  Radius-1 ball fills 2×10^-14 of the box at d = 30; drops below 1/N after d = 17 | Verified | 2.04e-14; 1.08e-6 at 17, 3.1e-7 at 18
  Metropolis & Ulam 1949, JASA | Verified | JASA 44(247):335–341
  Bergstra & Bengio 2012, JMLR: random search as good as grid in a fraction of the time; 9 trials → 3 vs 9 distinct values | Verified | JMLR 13:281–305, abstract and Fig. 1 caption
  Option on 100 stocks is a 100-dimensional average | Verified | Glasserman 2003 §1.1.1
MECHANICS: runtime 3:42.2 · wpm 163 (speech) / 159 overall · max silence 1.73 s · max static 2.97 s · −14.0 LUFS / −2.1 dBTP · leading 0.00 s · trailing 1.48 s · WER 3.4 % · banned phrases 0
FIXES (highest impact first):
1. [1:54–2:04][Clarity+Visual] The diagonal beat is the one transition that needs a rewatch.
   Problem:
   - 26 flat PURPLE lines sweep up the 100-axis panel (2:00.5). Nothing says that a flat line is one diagonal point (t, t, …, t).
   - The dashed INK level at t = 0.577 (kf_22, y ≈ 353 px) has no label. The viewer is told "57.7% inside" without being shown why "below the dashes" means inside.
   Change:
   - Before the sweep, draw one PURPLE flat line alone with the label "one point: (t, t, …, t)" for 1 s, then sweep the other 25.
   - Label the dashed level "ball's edge" at its right end (buff 0.2, INK, Text 26).
   - When the lines above it fade, render the lines below it as solid and the lines above as hollow-dash (the episode's filled = inside, hollow = outside convention).
   - Add [pause 0.6] after "miss by eight points".
2. [2:40–2:46][Clarity] The "two laws side by side" frame (kf_30) compares a count, "N^{1/d} values per axis", with an error, "spread = σ/√N". The diagonal beat 40 s earlier has just argued that values per axis are not the cause, so this pairing undercuts the episode's own correction.
   Change: make the left side an error rate too.
   - Show "grid: error ∝ N^{−2/d}" (PURPLE, YELLOW d), with a small grey tag "smooth f · Glasserman 2003 §1.1". This is the trapezoid-rule rate the facts sheet already quotes from the same page.
   - Keep "darts: spread = σ/√N" and "no d" opposite it.
   - The two exponents now read against each other (−2/d vs −1/2), which is the real comparison.
3. [2:34–2:44][Motion] Four equation events land in about 8 s:
   - "spread = ½/√N" is complete at about 2:36.6.
   - ½ → σ at about 2:38.5.
   - The grid law returns at about 2:41.
   - "no d" at about 2:43.
   This breaks BAR §5 "≤ 1 new equation per 5 s" and "hold ≥ 2 s + 0.4 s/term". The ½/√N result, the episode's central formula, is fully visible for under 2 s before σ replaces it.
   Change:
   - Insert [pause 0.8] after "that half over the square root of N" and [pause 0.6] after "sigma".
   - Bring the grid law in 1 s after "The root N stays" starts, not on it.
   - Net +1.4 s.
4. [2:34.5–2:38][Visual] The formula "spread = 1/2 / √N" sits in the same band as the dimmed "2 dimensions" and "100 dimensions" titles (kf_28: titles at y ≈ 198 px, the formula spans 150–335 px, horizontal gaps 45–67 px). The frame reads as one line, "2 dimensions spread = ½/√ 100 dimensions", with "N = 400 darts" stacked above it.
   Change:
   - FadeOut both titles (to 0, not 30 %) on the first stroke of Write("spread =").
   - The histograms underneath already identify themselves by position; keep them at 30 %.
5. [2:16–2:23, 2:34–2:55][Visual] Two problems in this stretch.
   - **Inverted hierarchy.** The scaled caption "one yes/no dart" (kf_26) has a cap height of about 60 px, larger than the section titles (about 45 px), and is set in grey. A dim caption is the largest text on screen.
   - **Notation jump.** The coin's ½ is a stacked \frac{1}{2}, but the formula it flies into typesets "1/2" with a slash. The TransformFromCopy changes the glyph's form mid-flight.
   Change:
   - Set the caption at the titles' size (Text 26–30), placed at (0, 1.4).
   - Typeset every ½ in the formula as \frac{1}{2}, here and in the 2:45–2:53 substitutions.
6. [1:17–1:21][Visual+Motion] The "centre is / inside the ball" label (frame 1:18.6) has two problems.
   - Its two lines are set at different sizes (cap height about 34 px vs about 44 px).
   - Its arrow points left into empty plot area (tip ≈ (1148, 243) px). The thing it describes, the PURPLE centre dot, sits in the thumbnail to its right.
   Change:
   - Set one size (Text 26).
   - Drop the arrow. Indicate the thumbnail's centre dot on "which sits inside the ball".
   - Then TransformFromCopy that dot onto the d = 20, 50-point data position as "grid says 1.000" appears. This encodes "the centre is the grid's whole estimate" instead of asserting it.
7. [2:56–3:01][Visual] Three labels stack within about 180 px at the right edge (kf_33): "0.05 points" (RED, above the dashed line), "typical miss" (BLUE, below it) and "darts (simulated)" (BLUE). Two BLUE labels sit next to two BLUE lines, and it is ambiguous which label names which line.
   Change:
   - Merge the first two into one label, "typical miss: 0.05 pts", left-aligned just above the dashed line in the empty band between d = 20 and d = 100 (x ≈ 1150–1480 px).
   - Leave "darts (simulated)" alone at the polyline's end.
8. [1:01.5–1:05][Motion] Two problems during the square → cube → ball morph.
   - The "d = 2" label stays up while the cube's depth edges are already drawn (frame 1:03.0). The "d = 3" swap lags the geometry by about 1 s.
   - Mid-morph, the disc's fill renders as a jagged, stair-stepped polygon (1:03.0).
   Change:
   - FadeTransform "d = 2" → "d = 3" at the moment the depth edges begin.
   - Draw only the outline arcs during the inflation, and FadeIn the eighth-ball fill (0.4 s) after the outline settles.
9. [2:12.6–2:15][Motion] When the gauges collapse into coins, three things go wrong.
   - The 2-D square's frame and disc vanish first, leaving loose floating dots (frame 2:13.4).
   - On the 100-D side, the bold polyline collapses to one dot.
   - The other 99 coins of the 100-D block appear with no origin (2:14.0).
   Change:
   - Keep the square's outline at 30 % and Transform it into the 2-D coin block's bounding box.
   - On the 100-D side, fan in 99 polylines at 10 % opacity for 0.5 s and collapse each one into its coin. Every coin then comes from a dart.
10. [3:16.4–3:17.4 and 3:33.4–3:34.4][Motion] Both of the last beat changes fade through a near-empty frame, then draw the next picture from scratch:
    - 3:16.4: only an axis stub is visible.
    - 3:33.9: all 100 axes are being redrawn.
    These cuts are allowed at beat boundaries, but the landing is the one return that should feel continuous.
    Change:
    - Transform the limit chart's dashed BLUE "1/N" line into the cold-open header "N = 1,000,000 points". It is the same quantity.
    - Grow the 100 axes up from the limit chart's x-axis instead of fading to black.
11. [2:43.6–2:44.2][Audio] The transcriber dropped "Back" from "Back to our ball". The word is present (energy from 163.75 s), but it is a 0.25 s word with a soft onset straight out of 1.2 s of digital silence, and the visual is mid-transition at the same instant.
    Change:
    - Re-synthesise the sentence as "So, back to our ball, with a million darts…", or add 0.1 s of pre-roll.
    - Re-run the transcript to confirm.
12. [0:05–0:08][Hook] The cold open asks an arithmetic question but never voices the belief it is about to break.
    Change: give the wrong belief one reasonable sentence, and keep the 1.5 s hold:
    "Spread them out as an even grid; that feels thorough." (+1 s)
    Pay for it by cutting "A hundred axes, a million points." at 3:33. The header on screen already says it (−2 s).
REACHES 9 IF ALL FIXED: yes, narrowly.
  - Fixes 1–2 lift Clarity to 9: no rewatch is needed, and the closing comparison becomes like-for-like.
  - Fixes 3–7 lift Visual to 9: one focal point per frame and consistent type.
  - Fixes 3 and 6–10 lift Motion to 9: every object has an origin, and the equation holds are respected.
  - Fixes 11–12 bring Hook and Audio to 9.
  - The weighted score would be about 8.9–9.0.
  No structural change is needed. The hook, the 2-D build where the grid wins, the measured failure, the visual insight (shadows → gauges → coins → histograms → formula), the cited payoff, the honest limit and the callback landing are all present and correct.
KEEP:
- The 100-axis parallel-coordinates frame as the cold open and the landing. The grid is one PURPLE centre line, a random point is one BLUE polyline, and the end floods every axis BLUE.
- The gauges (2:05–2:12): one dart's 2 or 100 coordinates visibly collapse to one bit (1.20 > 0.64 → 0; 31.8 < 33.3 → 1), then become coins, then histograms whose spreads match in 2-D and 100-D and both halve when N is ×4.
- The shadow device (1:35–1:53) reused as Bergstra & Bengio's 3-vs-9 shadows on the score curve (3:09–3:16), with the chart's method curves morphing into "grid search" and "random search".
```

## Round-2 craft fixes: status

| R2 fix | Status in this cut |
|---|---|
| 1 100-D haze → gauges | Done and good (kf_23, kf_24). The coin collapse still leaves orphans (new fix 9). |
| 2 formula frame clutter | Mostly done (context at 30 %, size 56). The formula still shares a band with the dimmed titles (new fix 4). |
| 3 centred climax number | Done (kf_32): alone on an empty frame, then it flies to the chart. |
| 4 both laws side by side | Done, but the pairing compares a count with an error (new fix 2). |
| 5 cube inset off the chart | Done: the morph runs on an empty frame, then becomes a thumbnail (kf_11). |
| 6 no glyph soup | Done: Write("spread ="), bracket copies → RED underline, DecimalNumber brackets (2:33 shows a clean count-down). |
| 7 σ ↔ ½ blob | Done: clean FadeTransform (2:38–2:39). |
| 8 centre label | Done as specified, but the two-size type and wrong-way arrow remain (new fix 6). |
| 9 coin line 1.8× | Done (kf_26); the caption hierarchy is inverted (new fix 5). |
| 10 chart → B&B titles | Done (2:59–3:01). |
| 11 "grid, points" | Fixed: "The grid's 100 points cast only 10 shadows" transcribes cleanly. |
| 12 metronomic pauses | Fixed: gaps of 0.3 s inside thoughts; 0.7–1.7 s at boundaries (0:34.7, 0:57.8, 1:32.5, 2:42.6, 2:49.7, 3:15.3). |
| 13 open loop + runtime | Done: "How far off would a million of them land? Hold that thought." (0:31) is answered at 2:51 by the same BLUE "?". Runtime 3:55 → 3:42. |

## Sync notes (word timings vs frames)
- "How many values does each input get?" (0:07.9–0:09.9) → "grid values per input: ?" is up by 0:11. The 1.6 s hold is followed by "One." with the "1" swap. Lands.
- "Look at the shadows" (1:34.9) → the rail appears by 1:37. "only ten shadows" (1:40.4) → PURPLE ticks by 1:41. Lands.
- "With N points over d axes … d-th root of N" (1:49–1:53) → "N^{1/d} values per axis" by 1:53. Lands.
- "A million points on the diagonal" (1:56.4–1:58.0) → lines sweeping by 1:57. "miss by eight points" (2:02.6) → "7.7 points off" by 2:03. Lands.
- "x1² … inside → 1" gauges (2:05–2:12) → both verdicts are on screen by "or a hundred" (2:11). Lands.
- "this wide" (2:27.5), "just as wide" (2:29.9), "Quadruple" (2:30.8) → bracket, bracket, then N 100 → 400 at about 2:32. Lands.
- "How far off is a typical estimate?" (2:47.6–2:49.8) → "= ?" is on screen 2:49–2:53. "five hundredths of a point" (2:53) → "0.05 points" by 2:55. Lands.
- "Nine grid trials test three values" (3:10.3) → 3 shadows by 3:11. "Nine random trials test nine" (3:13.3) → 9 shadows by 3:15. Lands.
- "Below this line" (3:25.4) → the line is drawn 3:25.5–3:26.0. Lands.
- No spoken reference names something that is not visible within ±2 s.
