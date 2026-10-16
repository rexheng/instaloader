# Round 1: substance review (science and story editor; every dimension scored)

## Evidence

**Review pack.** `review/metrics.json` (01:09) is newer than `final.mp4` (01:07), so I used the existing `review/` pack.

From it I read:
- report.md, narration_diff.txt and transcript
- all 13 contact sheets
- full-resolution keyframes kf_04, kf_09, kf_10, kf_15, kf_16, kf_19, kf_22, kf_26, kf_28, kf_29, kf_31, kf_33, kf_35, kf_36 and kf_40
- extra frames I extracted at 2:29.6, 2:30.0, 2:30.4, 2:30.8 and 2:31.3–2:33.2, to check whether "it's our formula" and "the average's skewness" are tied visually to the top-right formula (they are: the formula turns yellow at 2:31.3)

I also read script.md, narration.txt and facts.md.

**Recomputation.**
- I recomputed every number by hand or with numpy/scipy.
- Independent Monte Carlo of the z-interval with sample SD, x̄ ± 1.96·s/√n, on Exp(mean 10). Columns: n, tests, low miss, high miss.
  - n = 30, 400k tests: low 7.26%, high 1.00%.
  - n = 300, 100k tests: low 3.58%, high 1.72%.
  - n = 1,420, 40k tests: low 2.89%, high 2.16%.
  - All three agree with the on-screen values 7.2/1.0, 3.7/1.7 and 3.0/2.1 to within about 1.4 Monte Carlo SE.

**Sources.**
- The Kohavi et al. 2014 KDD PDF (exp-platform.com), re-read for:
  - the n ≥ 30 quote and its reference [42], which is Montgomery & Runger, Wiley 2010, ISBN 978-0470053041
  - the 2%–3% tail criterion and its derivation "from the work of Boos and Hughes-Oliver [43]" (*Am. Stat.* 2000, 54(2):121-128)
  - the table: Revenue/User 17.9 → 114k; capped 5.2 → 9.7k
  - the correction note (18.2/5.3 in the published text)
  - "After we capped Revenue/User to $10 per user per week, we saw skewness drop from 18 to 5.3"

```
EPISODE: 009 — "Why Bell Curves Are Everywhere, and When They're Not"
IDEA: Collecting more lopsided data never makes a bell; averaging does, because an average's skewness is one piece's over root n, so for bus waits an A-B test needs about 1,420 per average rather than the textbook's 30, and only while no single piece can outweigh the rest (finite variance).
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 8.5 · Audio 8 · Concision 8 · Originality 9
WEIGHTED: 8.3 (8.25)   AFTER CEILING: 8.3 (lowest 8 + 2 = 10, not binding)
CAPS: none
FINAL: 8.3   PASS: no
```

## FACTS

| Claim | Verdict | Source |
|---|---|---|
| Bus waits (simulated exponential, mean 10) are lopsided; skewness about 2 at every sample size (1.90/1.96/2.00/1.98) | Verified | Exp skewness = 2 exactly; values per sim.py; labelled "simulated" |
| Skewness = average cubed gap / spread cubed, left gaps negative; bell = 0 | Verified | definition; matches Kohavi et al.'s s |
| (5.2 + 1.8 + 25.7 + 5.3)/4 = 9.5 | Verified | 38.0/4 |
| Averages of 4/16/64 have skew 0.99/0.50/0.25; "each ×4 halves it"; skew(x̄) = skew(x)/√n | Verified | third cumulant adds: nκ₃/(nσ²)^{3/2} |
| Cubes: 4 cubed gaps over 8 spread-cubed = ½; general n/n^{3/2} | Verified | independence kills cross terms; SD(sum of 4) = 2σ |
| Coin p = 0.1: skew 2.67; average of 64 has skew 0.33 | Verified | 0.8/0.3 = 2.667; /8 = 0.333 |
| Excess kurtosis fades as 1/n; finer cumulants faster still | Verified, but heuristic | standardized r-th cumulant scales as n^{1−r/2}. It is presented as "that's the CLT"; the theorem itself needs only finite variance, which the episode states later |
| CLT needs independent pieces plus finite variance | Verified | Lindeberg–Lévy |
| "Textbooks say the average of 30 is safe to treat as a bell" (Montgomery & Runger, 2010) | Verified | Kohavi et al. 2014 quote "if n ≥ 30, the normal approximation will be satisfactory regardless of the shape of the distribution", ref. [42] = Montgomery & Runger, *Applied Statistics and Probability for Engineers*, Wiley 2010 |
| "A-B tests lean on that bell" | Verified | Kohavi et al. 2014, Rule #7 |
| "On revenue data, 30 is off by a factor of thousands" | Verified | 114,000/30 = 3,800 |
| 2/√30 = 0.37 | Verified | 0.365 |
| 95% interval should miss 2.5% each side | Verified | definition |
| A low average gets a small sample SD, so its interval stops short (example 6.83, SD 6.47 → 4.51–9.14 vs 3.25–10.41) | Verified | arithmetic checked; corr(x̄, s) > 0 for right-skewed data |
| n = 30: 7% low, 1% high | Verified | my MC 7.26/1.00 |
| Kohavi et al. want each tail between 2% and 3% | Verified | quote: "no greater than 0.03 and no less than 0.02" |
| …"using Bing's data" | Misleading wording (not counted as Wrong) | the criterion and the 355 rule come from Boos & Hughes-Oliver theory; Bing data appears only in the table of example sample sizes |
| Rule n ≥ 355·s² ⇔ skew(x̄) ≤ 1/√355 = 0.053 | Verified | 0.05307 |
| n = 300 still misses (3.7/1.7) | Verified | my MC 3.58/1.72 (rounding within MC noise) |
| 355·2² = 1,420; both misses reach the band (3.0/2.1) | Verified | my MC 2.89/2.16 |
| Bing Revenue/User skew near 18 → 114,000; 355·17.9² ≈ 114,000 | Verified | 113,746; table 17.9/114k (text 18.2) |
| Capped at $10/user/week → under 10,000; 355·5.2² ≈ 9,600 | Verified | 9,599; table 9.7k |
| Lighthouse: landing spot = tan θ, standard Cauchy | Verified | Gull 1988; Sivia & Skilling 2006 (on screen) |
| Farthest of 1,000 flashes typically about 900 mi | Verified | median of max = tan(π/2 · 0.5^{1/1000}) = 919 |
| 902/1,000 ≈ 0.9 mi drag | Verified | arithmetic |
| Half of single flashes within 1 mi; half of 1,000-flash averages too | Verified | P(abs(X) < 1) = ½; the mean of n Cauchy is Cauchy |
| Variance infinite; median homes in | Verified | E[X²] = ∞; median SD ≈ π/(2√n) |

**Fabricated or Wrong: none.**

## MECHANICS

| Metric | Value | Status |
|---|---|---|
| Runtime | 3:52.8 | |
| Pace | 161 wpm over speech; 155 overall; 177 with all pauses excluded (brisk) | |
| Longest internal silence | 1.74 s, the prediction hold at 0:12.1 | |
| Leading / trailing silence | 0.00 s / 1.91 s | |
| Longest fully static stretch | 3.53 s (0:11.4–0:15.0) | |
| Loudness / true peak | −14.0 LUFS / −2.2 dBTP | |
| Transcript WER | 2.9% | |
| Black frames | 0 | |
| Layout issues | 0 (2 allowed beam crossings, both plausible) | |

No mechanical caps are triggered.

## Transcript and slop check

- **Banned phrases:** none.
- **Rhetorical-question chains:** none. There is one genuine question, at 0:08.
- **Banned patterns:**
  - No "it turns out" and no hedges.
  - "Divide by n and take the root: … it's our formula" is a pause-reveal, but a real transformation on screen earns it (grid of 2:29.6–2:30.8), so I don't count it.
  - The landing "The bell was never in the data. It's in the average." is a reframe, not "X isn't just Y".
- **Homophones and pronunciation:**
  - Whisper hears "waits" as "weights" 7 times (0:39.5, 0:46.3, 1:11.3, 1:14.9, 1:17.9, 2:12.7, 2:36.2). It is a homophone, not a mispronunciation.
  - The 1:14–1:18 cube beat ("Add four waits … four times one wait's") is the one place a listener can really picture physical weights.
  - "Kohavi" is transcribed correctly.
- **Hook:** the question is on screen at 0:08–0:13 with the three chips (30 / 300 / 1,000+) and a 1.7 s hold, so the hook lands by 0:13.

## Flipbook (contact sheets)

- **0:00–0:20.** The cold open matches §6. The citation arrives on "Textbooks" (0:05) and switches to Kohavi on "revenue" (0:17).
- **0:20–0:43.** The naive build and the measured fail (skew bars 1.90–2.00 against "bell 0") are clear.
  - Story problem: the cold open has already framed the question as "average of 30 → bell?". So "First, look for the bell in the data itself" tests a belief nobody on screen voiced, and it stalls the hook question for 23 s.
- **0:44–1:12.** The best stretch.
  - Chips become the sum, the 9.5 dot drops on "here" (0:53), and the panels fill.
  - ×4 arcs and ÷2 arcs show up, and 2/√n per reading converges to one formula.
- **1:13–1:27.** The cube argument is drawn: 4 blue cubes, then a 2×2×2 gray cube, then ×n and ×n^{3/2} fly into the slot. It is good, honest geometry.
- **1:28–1:50.** The densest 22 s.
  - Coin universality, the kurtosis formula, "every finer difference faster still", the CLT name and its conditions all arrive in a row.
  - The kurtosis claim is a formula copy with no picture of anything fading (kf_19).
- **1:51–2:16.**
  - The exact n = 30 panel and the log sample-size axis are clear.
  - The interval-shrinks-into-the-low-bar move (2:09–2:15) is excellent.
  - The causal step "low average → small SD → interval stops short" gets one sentence. It is then never connected to skew/√n.
- **2:16–2:41.**
  - The rule algebra is done by transform (grid at 2:29–2:31), and the top formula flags yellow on "the average's skewness" (2:31.3).
  - The 300 and 1,420 morphs land on their words. The answer holds about 2.5 s.
- **2:41–2:51.** Bing numbers, with the panel dimmed.
- **2:52–3:40.** The lighthouse. It is a strong standalone sequence: beam, landing dots, running average, the 902-mile flash, middle-half brackets.
  - The hook's question was already answered at 2:39, though, so 60 s of material follows the climax before the landing.
  - The "← 12" / "12 →" counts (3:25–3:40) are unlabeled, and the axis right above them is in miles.
- **3:41–3:53.** The landing re-sees the cold open: the 1,000+ chip lights, the arrow relabels to "average of 1,420", and the yellow histogram grows under a solid green bell. This is a true return to the first frame.

## Keyframes (§5)

- **Margins and overlaps:** all clean in the frames I read. The lighthouse "miles" y-label (kf_31) sits at about y = 3.3, inside the safe area.
- **Typos and LaTeX:** none.
- **Palette:** consistent with the declared roles throughout.
  - Blue = single pieces, yellow = averages and intervals, green = bell, red = the dragging extreme.
  - Purple = median, gray = sample sizes and rules.
- **kf_15 (1:16), n = 4 panel:** the green bell starts at about 25% height on the x = 0 axis, so it is cut off. The bell's impossible negative-wait tail is hidden, and the cut looks like an artifact.
- **kf_10 / kf_15, n-panels:** they carry only a rotated "share" on panel 1, with no ticks or unit. §5 asks every axis for a quantity and a unit.
- **kf_22 (2:15.8), the busiest frame:** distribution, interval, μ line, meter, two formulas, log axis and a citation. It has 2–3 competing focal points; it is legible, but it is not "one focal point".
- **kf_35 (3:34.5):** "← 12" / "12 →" in yellow reads as ±12 miles, not as "12 averages off-screen".

## FIXES (highest impact first)

1. **[2:05–2:41][Clarity] The answer's mechanism is asserted, not shown.**
   - Problem:
     - "Tests estimate the spread from the same data, so a low average gets a small spread, and its interval stops short" is one sentence.
     - The meter then falls 7.2 → 3.7 → 3.0, and "Divide by n and take the root: it's our formula" is only an algebraic identity.
     - Nothing shows the viewer why the miss rate is governed by skew(x̄). A viewer cannot re-derive why 1,420 after one watch.
   - Change:
     - When the panel morphs to n = 300 (2:34) and n = 1,420 (2:36), draw a thin gray connector from the "skew = 0.12" / "skew = 0.053" readout to the low bar.
     - Replace "Three hundred still misses." with "At three hundred the lean is point one two: still too much." Then "For these waits: fourteen twenty, lean point oh five three, and both misses reach the band."
     - That way the skewness readout visibly drives the miss, and the "1,420" answer rests on the episode's own formula.
2. **[2:41–2:52][Hook] Tension collapses after the answer at 2:39.**
   - Problem: the lighthouse (48 s, 21% of runtime) arrives as an appendix ("Now the condition").
   - Change: make it the third answer to the cold-open question.
     - Replace "Now the condition." with "And for some data, no number on this axis is enough."
     - On those words, add a fourth gray marker "never" past 10⁵ on the sample-size axis before the dissolve.
     - At the landing (3:41), let the chip row briefly show that marker dimmed next to the lit "1,000+".
3. **[0:20–0:23][Hook/Clarity] The naive build tests a belief nobody voiced.**
   - Problem: the cold open is already about averages of 30.
   - Change: replace "First, look for the bell in the data itself." with "Maybe thirty is about collecting enough waits, not averaging them." This ties the naive attempt to the hook's number and keeps the following lines.
4. **[2:16–2:21][Clarity/correctness wording] "using Bing's data" misattributes the criterion.**
   - Problem: "Ron Kohavi and colleagues, using Bing's data, want each side between 2 and 3%" implies Bing data produced the 2–3% criterion or the rule. Per the paper, the rule "was derived from the work of Boos and Hughes-Oliver"; Bing appears only in the example table.
   - Change:
     - Narration: "Ron Kohavi and colleagues want each side between two and three percent." Bing then enters at 2:41 as it already does.
     - Optionally add "rule from Boos & Hughes-Oliver, 2000" to the citation line at 2:21–2:30.
5. **[1:35–1:46][Clarity/Visual] Kurtosis is announced with a formula and no picture.**
   - Problem: "every finer difference faster still. Only the bell survives" has no visual referent.
   - Change, either of:
     - (a) Keep the n = 1/4/16/64 panels for this line and write excess-kurtosis readouts under the skew readouts: blue 6, then yellow 1.5 / 0.38 / 0.09, with "÷4" arcs. That is the same ×4 rhythm as the skew arcs, and it makes "faster" visible.
     - (b) Cut the kurtosis sentence and its formula (about 8 s), keeping "Only the bell survives."
6. **[3:25–3:40][Visual/Clarity] Unlabeled overflow counts read as miles.**
   - Change: "← 12" / "12 →" → "12 more ←" / "→ 12 more", or "+12 off-scale". Keep them yellow and at Text font size ≥ 18.
7. **[1:03–1:50][Visual] The n = 4 bell is cut at x = 0 (kf_15).**
   - Change, either of:
     - Extend the n = 4 x-range to −5 min, with ticks −5/0/10/20, so the bell's negative tail is drawn whole and dimmed to 40% left of 0.
     - Or end the curve at 0 with a small dimmed tick "bell predicts < 0".
   - Either removes what looks like a clip.
8. **[0:45–1:50][Visual] The n-panels lack a scale.**
   - Change: on panel 1 only, change "share" to "share (%)" and add two ticks (0, 10).
   - The shared-scale panels can stay tickless if a gray note "same scale" sits under the panel row, or simply leave the other panels as they are.
9. **[1:14–1:19][Audio] Homophone risk in the cube beat.**
   - Change: "Add four waits: their cubed gaps add up, four times one wait's" → "Add four bus waits: their cubed gaps add up to four times one wait's." Whisper heard "weights" twice here, and "cubes" plus "weights" invites a wrong mental image.
10. **[3:43–3:47][Concision] Landing line repeats 0:26–0:29.**
    - Problem: "And collect forever: this histogram stays lopsided" repeats "the shape doesn't budge".
    - Change: keep the "tail" brace visual, but cut the sentence to "Collect forever: still lopsided." This saves about 1.5 s and keeps the reframe crisp.

## REACHES 9 IF ALL FIXED

Yes, narrowly. No fact is wrong, the mechanics are clean, and the core picture (chips → average → ×4/÷2 → cubes → formula) is already near 3b1b quality.

What holds the score at 8.3 is story and clarity:
- the payoff's mechanism is not visualized (fix 1)
- the hook question is answered 70 s before the end (fix 2)
- the naive beat is a straw man (fix 3)
- one dense stretch is announced rather than shown (fix 5)

Fixes 1–3 together should lift Hook to 9 and Clarity to 9, and fix 5 plus fixes 6–8 lift Visual to about 8.5–9. Without fixes 1 and 2 it will not reach 9.

## KEEP

- The cold-open frame and its exact return at 3:41–3:53: chips, "average of 30" relabelled "average of 1,420", and a solid bell grown from real averages.
- The 0:44–1:27 build: the four chips become one dropped dot, ×4/÷2 arcs collapse into skew(x)/√n, and the 4-blue-cube versus 2×2×2-gray-cube argument for root n.
- The interval that shrinks short of μ and flows into the 7.2% low bar (2:09–2:15), and the 30 → 300 → 1,420 morphs landing on their words with independently verifiable miss rates.
