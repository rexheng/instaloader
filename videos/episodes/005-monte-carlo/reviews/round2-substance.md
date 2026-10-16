# Episode 5, review round 2 (substance: science and story editor)

**Evidence.** I reused the existing `review/` pack, because metrics.json (16:31) is newer than final.mp4 (16:29). I read:
- report.md, narration_diff, transcript.txt and the word timings.
- All 13 contact sheets.
- 14 full-resolution keyframes: kf_01, 05, 09, 11, 16, 19, 21, 24, 26, 29, 33, 36 and 40.
- 5 extra frames extracted with ffmpeg: 1:49.0, 2:13.8, 2:39.2, 3:23.3 and 3:41.5.
- script.md, facts.md, narration.txt, CHANGELOG.md and the round-1 reviews.

I recomputed every number independently in Python (scratch script, run against data.json):
- the half-volume radii, using a 4×10^6-point Monte Carlo per dimension and the exact d = 3 radius;
- every grid estimate, by full enumeration;
- the 2^19 rescue, exactly (binomial);
- the 2-D dart count, the 100-D dart's Σx², the 100-D coin count and the histogram SDs;
- the radius-1 ball volumes;
- P(|Z| < 1).

I checked all three citations by web search (tandfonline/JSTOR, jmlr.org, Springer listings).

```
EPISODE: 005 — "Why Random Darts Beat Grids in 100 Dimensions"
IDEA: An even grid of N points in d dimensions gets only N^(1/d) values per axis, so a million-point grid in 20–100 dimensions is a single point and is 50 points wrong. Each random dart is an independent yes/no coin flip whose chance is the answer itself, so the darts miss by σ/√N (½/√N here) with no d in it, unless the answer is tiny.
SCORES: Hook 8.5 · Clarity 8 · Visual 7.5 · Motion 8 · Audio 8 · Concision 8 · Originality 8.5
WEIGHTED: 8.1 (805/100 = 8.05)   AFTER CEILING: 8.1 (lowest 7.5 + 2 = 9.5, does not bind)
CAPS: none
  - Fact check: no Wrong or fabricated claim (see FACTS).
  - Citations: every empirical claim has one on screen. Glasserman 0:23–0:28 (~4.5 s), Metropolis & Ulam 0:28–0:37, Bergstra & Bengio 3:09–3:24.
  - Mechanics: max silence 1.96 s; max static 3.1 s (planned hold at 2:51.9); runtime 3:54.6 (inside 4:00 by 5.4 s); −14.0 LUFS / −2.1 dBTP.
  - §4 slop: 0 banned phrases and no question chains. "Darts do have a blind spot: tiny answers" (3:23.9) is the only colon-reveal-like line. It has no teaser question, so I did not count it.
  - Overlaps: the overlaps I found are all mid-transform and under 1 s: the glyph soup at 2:39.2, the falling shadow ticks over the dimmed "input 1" at 1:49.0, and the "d = ³" morph at 1:07. None is held, so no cap 7.
FINAL: 8.1   PASS: no
```

## FACTS

| # | Claim | Status | Source / my check |
|---|---|---|---|
| 1 | 10^6 grid points in 100-D → **1** value per input, the centre | Verified | floor(10^(6/100)) = floor(1.148) = 1 |
| 2 | 2 values per input → 2^100 points, **31 digits**; the on-screen string 1,267,650,600,228,229,401,496,703,205,376 | Verified | Python `len(str(2**100)) = 31`; the string matches |
| 3 | Quarter disc share = exactly ½ | Verified | r² = 2/π → πr²/4 = ½ |
| 4 | 10×10 grid: **52** inside, 2 points off | Verified | enumeration = 52; I also counted the filled dots in kf_09: 3+5+6+7+7+8+8+8 = 52 |
| 5 | 100 darts: **44** inside, 6 points off; dart #1 (cold-open dart) is outside | Verified (simulated, labelled) | recount = 44; dart #1 (0.625, 0.897) has x²+y² = 1.196 > 0.637 |
| 6 | "The ball always covers exactly half the box" | Verified | my MC: 0.49985, 0.49968, 0.49965, 0.49996, 0.50025 at d = 3, 6, 10, 20, 100 (SE 0.00025); d = 3 exact r² = (3/π)^(2/3) = 0.9697 |
| 7 | Values per axis 1000, 100, 10, 3, 1, 1; points used 10^6, 10^6, 10^6, 59,049, 1, 1 | Verified | floor(10^(6/d)); 4^10 > 10^6 |
| 8 | Grid errors 0.002, 0.001, 0.10, 2.4 points | Verified | full enumeration: 0.50002, 0.499989, 0.501022, 0.524463 |
| 9 | Centre inside the ball at d = 20 and 100 → "grid says 1.000", 50 points off | Verified | d/4 = 5 < 6.63 and 25 < 33.30 |
| 10 | "Half a million points, two values on 19 axes … 18 points off" | Verified | Σx² = (23+8k)/16 ≤ 6.63 ⇔ k ≤ 10; P(Bin(19,½) ≤ 10) = 0.6762 → 17.6 |
| 11 | Darts (10^6, simulated) "under a tenth of a point in every dimension" | Verified (simulated, about these six runs) | 0.038, 0.013, 0.022, 0.028, 0.025, 0.004 |
| 12 | 100 grid points cast 10 shadows, 100 darts cast 100; N^(1/d) | Verified | algebra |
| 13 | 100-D dart is "inside → 1" (2:15) | Verified | Σx² = 31.77 < r² = 33.30 |
| 14 | Coin blocks 44/100 (2-D) and 48/100 (100-D) | Verified | 100-D recount = 48 |
| 15 | One flip misses its average by exactly ½; spread = ½/√N; quadrupling N halves it | Verified (exact for p = ½) | Bernoulli(½) SD = ½ |
| 16 | 300 runs: ±4.8 / ±4.8 → ±2.6 / ±2.4 pts | Verified (simulated) | SD 4.84, 4.80 → 2.61, 2.35; theory 5.0 → 2.5; bracket widths measured in kf_24/kf_26 match (88 px / 16.9 px per % = ±2.6) |
| 17 | "Any other function swaps that half for its own spread, sigma. The root N stays." | Verified | Glasserman 2003 §1.1.1: σ_f/√n "for all d" |
| 18 | "A million yes-or-no darts … one half over a thousand, five hundredths of a point" | Verified for this p = ½ problem | 0.5/1000 = 0.0005 = 0.05 pts. For a general yes/no answer p it is √(p(1−p))/√N ≤ ½/√N, an upper bound the narration doesn't state (fix 9) |
| 19 | "Two runs in three land under that typical miss; all six of ours did" | Verified | P(\|Z\| < 1) = 0.683; 0.683^6 = 0.10, stated as what happened |
| 20 | Radius-1 ball fills 2 × 10^-14 of the box at d = 30 | Verified | π^15/15!/2^30 = 2.041e-14 |
| 21 | "Below this line … usually report 0" | Verified | the line is crossed between d = 17 (1.08e-6) and d = 18 (3.1e-7). Every plotted point below it has P(0 hits) ≥ 0.73 (d = 18), and 1 − 2e-8 at d = 30 |
| 22 | Option on 100 stocks = this kind of 100-D average | Verified | Glasserman, *Monte Carlo Methods in Financial Engineering*, Springer 2003 (Applications of Mathematics 53), §1.1 |
| 23 | Metropolis & Ulam published "The Monte Carlo Method", 1949, JASA | Verified | JASA 44(247):335–341, Sept 1949 (tandfonline doi 10.1080/01621459.1949.10483310) |
| 24 | Bergstra & Bengio 2012: random search tuned neural nets as well as grid "in a fraction of the time" | Verified | JMLR 13:281–305, abstract: "as good or better within a small fraction of the computation time" |
| 25 | "9 grid trials test 3 values … 9 random trials test 9" | Verified | same paper, Fig. 1 caption; the redraw is labelled "schematic" |

No Wrong or Fabricated claims. Two places are imprecise without being wrong:
- #18 omits "at most".
- The radius-1 chart's "100% off" switches to relative error after 3½ minutes of percentage points (fix 4).

## MECHANICS
```
runtime 3:54.6 · wpm 159 (speech) / 155 overall / 185 excl. pauses · max silence 1.96 s (0:10.3, planned prediction hold) · max static 3.1 s (2:51.9, planned) · −14.0 LUFS / −2.1 dBTP · leading 0.00 s · trailing 1.72 s · WER 3.5 % · 0 banned phrases
```
- **Pronunciation.** Bengio, Ulam, Metropolis and "d-th" were all transcribed correctly, so I infer they are pronounced correctly. "a hundred per axis in three" now transcribes cleanly (the round-1 "103" problem is fixed).
- **Cadence.** About 60 of the inter-sentence gaps are 0.4–0.6 s (report.md silence list). Beat boundaries get the same 0.5 s as mid-thought sentence breaks, for example 1:01.4, 1:42.1, 3:04.7 and 3:23.6. This uniform rhythm is the main thing that makes the voice sound synthetic.

## Story read (BAR §6)

**Cold open (0:00–0:12): strong.**
- A concrete budget and the question "How many values does each input get?" (0:08–0:10), then a 2 s hold. Most viewers anchor on 10,000 or 10.
- The answer "One." at 0:12 is a genuine jolt, and the 2^100 line makes it visceral.

**Stakes (0:23–0:37): fixed since round 1.** The option on 100 stocks has its citation on screen. Metropolis & Ulam names the method.

**Naive build and fail (0:37–1:42): the best part of the episode.**
- In 2-D the grid wins (2 vs 6 points off).
- At a fixed million-point budget the grid's error climbs to 50 points.
- The fairest rescue (2^19 points) is still 18 points off.
- The "points used" row answers the budget objection. This is textbook SMH.

**Insight (1:42–3:04): correct, with one logical gap at its centre.**
- The shadows give N^(1/d), which explains the grid side.
- Then comes "Darts never meet the dimension. Each one reports a single bit." A grid point also reports a single bit, inside or outside. What makes the darts' bits a fair coin is that each dart is independent and uniform, so its chance of landing inside equals the answer in any dimension. The narration never says this. It leans on the word "coin" to carry it.
- The shadows beat also invites a wrong lesson: "darts win because they cast more shadows." A diagonal line of 100 points casts 100 shadows and is still badly wrong. The episode never closes that door, so a viewer leaves with two mechanisms and does not know which is the real one.

**Payoff (3:04–3:42): the honest limit is good.**
- Bergstra & Bengio reuses the shadow device, which is a strong callback.
- The tiny-answer limit is stated, with "off by the entire answer".

**Landing (3:42–3:53): weaker.**
- It returns to the cold-open frame, which works. But "The grid gives each axis one value" re-says 0:12 verbatim in substance, so the ending is half recap.
- The last clause, "a million coin flips, in any dimension", does reframe the opening question: the darts never had to answer "how many values per input".

## FIXES (highest impact first)

1. **[2:07–2:19][Clarity] The core mechanism is never stated, and the claim as worded fits grid points too.**
   - Problem: "Each one reports a single bit, inside or outside" is true of every grid point as well. Independence, and P(inside) = the answer, are never said.
   - Narration: replace "Each one reports a single bit, inside or outside, whether it has two coordinates or a hundred." with "Each one lands inside with a chance equal to the answer, on its own, whether it has two coordinates or a hundred."
   - Visual: under the ringed 2-D dart, write "x² + y² = 1.20 > 0.64 → outside → 0". Under the bold 100-D polyline, write "Σx² = 31.8 < 33.3 → inside → 1" (values from data.json; I verified both). Then `ReplacementTransform` each readout into its coin before the 10×10 blocks form.
   - Effect: 100 coordinates visibly collapse to one bit, and the frame shows why that bit is a fair coin in any d.
2. **[2:04–2:07][Clarity] Close the "more shadows" misreading.**
   - Do the demonstration in 100-D, not 2-D. A 2-D diagonal of 100 midpoints puts 56 inside, only 6 points off, which is no worse than the darts, so it would prove nothing.
   - In 100-D, a million evenly spaced points on the main diagonal (t, t, …, t) give every axis a million distinct values. Yet only t ≤ √(33.30/100) = 0.577 is inside, so the estimate is 0.577 and 7.7 points off (I computed 0.577075). The darts at d = 100 are 0.004 points off.
   - Visual: on the 100-axis panel, draw the diagonal's polylines as flat horizontal lines sweeping 0 → 1, with the label "a million values per axis · 7.7 points off", for about 3 s.
   - Narration: "Shadows alone aren't the fix: a million points on the diagonal give every axis a million values, and still miss by eight points."
   - Pay for the time with fixes 7 and 8.
3. **[2:41–3:00][Visual] The climax frame is cluttered and off-centre.**
   - At 2:47 (kf_26) there are about 25 words of prose on screen against a 12-word limit: header, two titles, "σ = one dart's spread", "one yes/no dart", two "10 runs", and "estimate from one experiment".
   - The answer "spread = 0.0005 = 0.05 points" sits right of centre, about 30 px under a dimmed title (kf_29, 2:59.5).
   - At 2:47.3, fade the header, both titles, "10 runs", "estimate from one experiment" and the coin number line to 0, and keep the histograms at 25 %.
   - Then run `formula.animate.move_to(UP*0.8).scale(1.15)` before √1,000,000 → 1000, so the episode's one number owns the centre.
4. **[3:24–3:42][Clarity/Visual] The red "under 1 hit expected" zone spans d = 2–30, and its label sits at d ≈ 2–9, where the curve is up to 10^6 times above it (kf_36, 3:38.4). "100% off" switches from points to percent unannounced (3:41.5).**
   - Shade only from the crossing (d ≈ 17.1) to 30 below 10^-6.
   - Move the label beneath the curve tail, right-aligned at d = 29, y ≈ 10^-13.5.
   - Reword it to "darts report 0: off by the whole answer".
5. **[2:11–2:19][Visual] The 100-D panel is a haze of 99 faint polylines plus a bold one (2:13.8).** Drop the 99 faint lines, or take them to 8 % opacity, so the bold dart and its Σx² readout from fix 1 are the focal point.
6. **[2:38.9–2:39.6][Motion] Glyph soup.** "spread" is assembled from scrambled glyph copies of the "pts" labels, and "±2.6/±2.4 pts" double-expose (2:39.2 frame). Use `Write("spread =")` in place, and make the bracket labels `DecimalNumber`s with `ChangeDecimalToValue`, with "pts" as a separate static mobject. Do the same for the "d = 2 → 3" morph at 1:07 (garbled "d = ³").
7. **[3:42–3:53][Concision/Hook] The landing half-recaps.**
   - Cut "The grid gives each axis one value." The purple centre line and its "1 value per axis" label already say it.
   - End on: "A hundred axes, a million points. The darts never noticed the axes: a million coin flips, in any dimension." This saves about 2.5 s for fix 2.
8. **[0:27–0:36][Concision] Tighten the citation line.**
   - Replace "Since Metropolis and Ulam published the Monte Carlo method in 1949, such averages are done with random points, like this one." with "Since Metropolis and Ulam's 1949 paper, such averages use random points, like this one." The citation stays on screen.
   - Also add "· Springer" to the Glasserman citation, so it follows the "Author, Year · Venue" format.
   - Saves about 1.5 s.
9. **[2:47–2:58][Clarity] "With a million yes-or-no darts … one half over a thousand" is only exact for a half-full ball.** Change it to "With a million darts at our half-full ball, in any dimension, how far off is a typical estimate?" Or keep the line and add "at most" before "one half over a thousand".
10. **[Audio, whole episode] Metronomic 0.5 s gaps.**
    - Set beat-boundary pauses to 0.8–1.0 s: 0:22.5, 0:59.4 → 1:01.9, 1:42.1, 2:06.4, 3:04.7, 3:23.6, 3:42.1.
    - Shorten within-beat sentence gaps to 0.25–0.35 s, for example 1:13.1, 1:16.4, 2:21.3 and 2:33.3. Net runtime change is about 0.
11. **[3:19–3:24][Visual] Bergstra & Bengio's random trials merge on screen.**
    - The x-values include 0.006/0.027 and 0.860/0.870, so the left pair prints as one blob on the score curve (3:23.3) and the right pair nearly touches. Viewers count about 7–8 shadows while hearing "nine random trials test nine".
    - Redraw with a seed, or a jitter, that gives every pair of x-values a gap of at least 0.06 (the panel is already labelled schematic).
12. **[1:05–1:12][Visual] The cube/eighth-ball inset is drawn inside the empty plot area of the error chart (kf_11).** Run the square → cube → ball morph centred before the axes are created. Then shrink it to a thumbnail at the upper right beside "true answer ½ in every dimension".

**REACHES 9 IF ALL FIXED:** no. My estimate is about 8.6: Clarity 9, Visual 8.5, Motion 8.5, Audio 8.5, Concision 8.5, Hook 8.5, Originality 8.5.

The remaining gap is structural. The insight is two pictures (shadows, then coin histograms) joined by a sentence, not one picture that changes smoothly into the formula, and the runtime sits 5 s under the 4:00 cap with no slack for the missing step. To reach 9:
- (a) Make one insight frame carry both laws side by side: the grid "N^(1/d) values per axis" with a YELLOW d, and the darts "σ/√N" with the d visibly absent. Derive the darts law from fix 1's dimension-collapsing readout, so the frame shows the independence mechanism.
- (b) Buy about 15 s by letting the chart beat fill its values-per-axis row silently. Replace "a thousand values per axis in two dimensions, a hundred per axis in three, ten in six, three in ten" with "watch its values per axis shrink", spoken while the row fills. The cold open, the chart and the shadows currently explain the grid's collapse three times.

**KEEP:**
- The 100-axis parallel-coordinates cold open, with "One." as the answer and the blue-flood return at the end.
- The fixed-budget dimension climb with the honest "points used" row and the 2^19 rescue (the SMH fail beat).
- The identical 2-D and 100-D coin-block histograms that narrow together under N → 4N, and the shadow device reused for Bergstra & Bengio.
