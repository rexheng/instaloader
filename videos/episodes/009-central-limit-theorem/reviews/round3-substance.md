# Round 3: substance review (science and story editor; every dimension scored)

## Evidence

**Review pack.** I used the existing `review/` pack. Its metrics.json (21:54) is newer than final.mp4 (21:52). From it I read:
- report.md and narration_diff.txt
- transcript.txt, plus the word timings around 1:52–2:08 and 3:28–3:34
- all 13 contact sheets
- full-resolution keyframes kf_02, kf_07, kf_17, kf_19, kf_21, kf_25, kf_27, kf_31, kf_34, kf_36 and kf_40
- extra frames I extracted at 1:19.2, 2:39.8, 2:40.6, 2:53.2, 3:43.2 and 3:44.2

**Episode files.** I read script.md, narration.txt and facts.md, along with the round-2 substance review and the round-3 craft review.

**Recomputation.**
- Every number, from `data.npz` and with scipy.
- I simulated 95% t-intervals on exponential data:
  - n = 30: 10⁶ replications
  - n = 1,420: 3·10⁵ replications

**Sources.**
- The Kohavi et al. 2014 PDF (exp-platform.com), re-read line by line for Rule #7 and reference [42].
- Alex Deng's book, *Causal Inference and Its Applications in Online Industry*, ch. 8, which derives the rule.
- Kohavi, Deng & Vermeer 2022, *A/B Testing Intuition Busters* (KDD), which gives 1/√355 = 0.053.
- Gull 1988 (bayes.wustl.edu/sfg, Kluwer volume pp. 53–74), confirmed by web search.

```
EPISODE: 009 — "Why Bell Curves Are Everywhere, and When They're Not"
IDEA: Collecting more lopsided data never makes it a bell; averaging does, because an average's skewness is one piece's over root n (and its tail weight over n), which for bus waits means about 1,420 per average rather than the textbook's 30, and only while no single piece can outweigh the rest (finite variance).
SCORES: Hook 8.5 · Clarity 7.5 · Visual 8 · Motion 8.5 · Audio 8 · Concision 8 · Originality 9
WEIGHTED: 8.1   AFTER CEILING: 8.1 (lowest 7.5 + 2 = 9.5, not binding)
CAPS: none (no literally false sentence, number or plotted value; every empirical claim has an on-screen citation somewhere in the video; mechanics all within limits; 0 banned phrases). See FACTS row "tail meter ↔ Kohavi's rule": it is misleading by implication and must be fixed, but I did not apply cap 6.
FINAL: 8.1   PASS: no
```

## FACTS

| Claim | Status | Source / recomputation |
|---|---|---|
| Bus waits skew about 2 at every sample size; bars 1.90 / 1.96 / 2.00 / 1.98 | Verified | data.npz src_skew 1.9004 / 1.9581 / 2.0047 / 1.9777; the exact exponential skew is 2 |
| Skewness = average cubed gap from the mean, left gaps negative, over the spread cubed; a bell scores 0 | Verified | E[(x−μ)³]/σ³, the same as Kohavi Rule #7's definition |
| (5.2 + 1.8 + 25.7 + 5.3)/4 = 9.5 | Verified | example4 = 5.206, 1.797, 25.692, 5.292, and the mean is 9.497 |
| Averages of 4 / 16 / 64 skew 0.99 / 0.50 / 0.25; ×4 in n gives ÷2 | Verified | 0.989 / 0.501 / 0.252; exact 2/√n |
| Cubed gaps add (×4), spread doubles so its cube ×8; n / n^{3/2}; skew(x̄) = skew(x)/√n | Verified | third cumulant of a sum is nκ₃ and the variance is nσ² |
| Coin p = 0.1: skew 2.67; average of 64 flips 0.33 = 2.67/√64 | Verified | 0.8/0.3 = 2.667, and /8 = 0.333 |
| "Kurtosis, the extra tail weight, fades … as one over n"; on screen kurt(x̄) = kurt(x)/n | Verified for *excess* kurtosis | fourth cumulant additivity. The on-screen label "kurt" does not say "excess" (raw kurtosis tends to 3, not 0). Nitpick, fix 9 |
| "Every finer difference faster still. Only the bell survives. That's the CLT." Needs independence + one condition | Verified (as the standard cumulant heuristic) | standardized r-th cumulant ∝ n^{1−r/2}; Lindeberg–Lévy needs i.i.d. pieces with finite variance |
| "Textbooks say the average of 30 is safe to treat as a bell"; "Montgomery & Runger, 2010, via Kohavi et al., 2014" | Verified | Kohavi PDF quotes ref [42] (Montgomery, *Applied Statistics and Probability for Engineers*, 5th ed., Wiley 2010): "if n ≥ 30, the normal approximation will be satisfactory regardless of the shape of the distribution". The citation appears on screen only from 1:59 (fix 7) |
| "A-B tests lean on that bell" | Verified | "Experimentation methodologies typically rely on the means, which are assumed to be normally distributed" |
| "On revenue data, thirty is off by a factor of thousands" | Verified | 114,000/30 = 3,800 |
| 2/√30 = 0.37; the n = 30 averages put 1.4% left and 3.4% right vs 2.5% | Verified | 0.3651; Gamma(30, 10/30) exact 1.403% / 3.402% (known-σ cut points μ ± 1.96σ/√n) |
| Kohavi et al. want each tail 2–3%; rule n ≥ 355·s² | Verified | PDF: "both two tail probabilities (nominally 0.025) are no greater than 0.03 and no less than 0.02"; "355 × s² for each variant"; "derived from the work of Boos and Hughes-Oliver [43]" (*Am. Stat.* 54(2):121–128, 2000). The citation lists the four authors and KDD. Correct |
| "Divide by n and take the root: it's our formula, the average's skewness at most 0.053" | Verified (algebra) | n ≥ 355s² ⇔ s/√n ≤ 1/√355 = 0.05307. Kohavi, Deng & Vermeer (KDD 2022) state the rule this way too ("skewness … no greater than 1/√355 = 0.053"). The rearrangement is correct, but it is not new |
| **Tail meter ↔ Kohavi's rule (2:05–2:41).** The video measures the known-σ tails of x̄, says Kohavi wants them in 2–3%, then applies the 355·s² rule and lands at 1,420 "and both tails land inside" | **Misleading by implication** | The meter shows the exact tails of x̄ with σ known (Gamma). For that quantity the 2–3% band is reached at about **n ≈ 130–150**, not 1,420 (Gamma exact: n = 130 → 1.99% / 2.96%; n = 150 → 2.03% / 2.93%; n = 300 → 2.17% / 2.81%). The first-order Edgeworth term gives n ≥ 30.6·s² = 123. Kohavi's 355·s² is the **estimated-σ (t-interval)** threshold. Deng's book says it directly: "Kohavi et al. (2014) derived 355s² based on similar calculation for the unknown variance case". My simulation of 95% t-intervals on these waits (10⁶ replications each, MC se 0.02 points): n = 30 → intervals wholly above μ 1.00%, wholly below μ **7.21%**; n = 150 → 1.48% / 4.26%; n = 300 → 1.68% / 3.66%; n = 1,420 → 2.09% / 3.00%, exactly the band edge the rule is built to hit. So "over a thousand" is the right answer for an A-B test that estimates the spread, but the picture the video shows would reach the band at the "300" chip. A viewer who re-derives the answer with the video's own logic gets the wrong number. Every literal sentence is true, which is why there is no cap. Fix 1 |
| 355·2² = 1,420; tails 2.35% / 2.64% | Verified | Gamma(1420) 2.351% / 2.645%; skew 0.0531 |
| Bing Revenue/User skew near 18 → 114,000 users; on screen 355·17.9² ≈ 114,000 | Verified | Table 17.9 / 114k; text "skewness of 18.2 and therefore 114k users"; 355·17.9² = 113,746 |
| "Capping each user at ten dollars a week cut that to under ten thousand"; 355·5.2² ≈ 9,600 | Verified | "After we capped Revenue/User to $10 per user per week, we saw skewness drop from 18 to 5.3"; table 5.2 / 9.7k; 355·5.2² = 9,599 |
| "Using Bing's data" | Verified | "a few select metrics from Bing" |
| Lighthouse one mile off a straight shore, random angles: Cauchy (Gull 1988; Sivia & Skilling 2006) | Verified | Gull, "Bayesian Inductive Inference and Maximum Entropy", in *Maximum-Entropy and Bayesian Methods in Science and Engineering* (Kluwer 1988), pp. 53–74; Sivia & Skilling, *Data Analysis*, 2nd ed., OUP 2006 |
| Farthest of 1,000 flashes typically about 900 mi; this run 902 mi; 902/1,000 ≈ 0.9 mi | Verified | median max = tan(π/2·0.5^{1/1000}) = 918.8 |
| Half of single flashes within a mile; the 1,000-flash average repeated 200 times, still only half | Verified | (2/π)·arctan 1 = 0.5; the mean of n Cauchy draws is standard Cauchy |
| Infinite variance; the median homes in | Verified | E[X²] = ∞; the sample median is asymptotically normal, SD π/(2√n) |

## MECHANICS

- **Runtime and pace:** 3:54.9. 158 wpm over speech time, 154 overall, 601 words.
- **Silence:** the longest internal silence is 2.0 s (0:11.6–0:13.6, a planned prediction hold). Leading silence 0.00 s, trailing 1.92 s.
- **Static frames:** the longest static stretch is 3.77 s (0:10.9–0:14.7, the same hold).
- **Loudness:** −14.0 LUFS, −1.6 dBTP.
- **Other checks:** WER 3.1%. No black frames. The layout audit found 0 issues.
- **Caps:** no mechanical cap fires. The runtime is 5 s under the 4:00 ceiling, so any added beat must be paid for (see fixes 1 and 5).

## Transcript and slop sweep

- **Banned phrases:** 0.
- **Banned patterns:** no "not just X", no question chain (one question, at 0:08), no abstract triplet, no recap ending.
- **Signposting:** "Now the condition" (2:52) is the episode's one allowed signpost. "Back to the textbook's thirty" refers back to the cold open rather than signposting.
- **Colon reveal:** "Divide by n and take the root: [1.1 s] it's our formula" comes close to the colon fake-reveal pattern, but the reveal carries content, so I did not count it.
- **Delivery:**
  - "so so" at 3:32.25–3:33.0: the "so" lasts 0.76 s and whisper heard it twice.
  - "waits" was heard as "weights" 7 times. These are homophones, not a mispronunciation. The screen says "waits", which disambiguates for viewers but not for audio-only listeners.
- **Hook:** the question lands at 0:08–0:11 with chips 30 / 300 / 1,000+, followed by a 2 s hold. It lands by 0:15.

## Structure (§6) and story

The beats run in order:
- cold open with a numeric prediction (0:00–0:13)
- stakes (0:13–0:20)
- naive build, collecting more data (0:20–0:30)
- measured fail, skew about 2 at every n (0:30–0:44)
- the fix, averaging (0:44–0:57)
- readings that halve
- a formula grown from the readings (0:57–1:18)
- the block "why" (1:18–1:34)
- universality and kurtosis, giving the CLT (1:34–1:58)
- textbook 30, measured in the tails (1:58–2:17)
- Kohavi's rule rearranged into our formula (2:17–2:40)
- Bing (2:40–2:52)
- the condition, shown with the lighthouse (2:52–3:42)
- the landing re-sees the cold open: "1,000+" lit, the arrow reads "average of 1,420", and the real bell grows (3:42–3:55)

It is a complete, well-built arc. The weak point is the climax. The answer to the opening question rests on a demonstration that measures a different quantity from the rule it invokes (FACTS row above). Everything else is nitpick to medium.

## Scores, with evidence

**Hook 8.5.**
- *For the score:*
  - The histogram is on screen in the first frame, and the textbook claim and the "average of 30 → ?" bell are up by 0:07.
  - The three chips force a commitment by 0:11, followed by a 2 s hold.
  - Stakes come at 0:13–0:20 and seed the payoff.
  - The landing answers exactly what was asked: the chip lights at 3:44 and the arrow is relabeled "average of 1,420".
- *Against:*
  - "Does it *really* take 30…" telegraphs that 30 is wrong, so the viewer's choice is between 300 and 1,000+.
  - "Safe to treat as a bell" has no criterion until 2:05.
  - Tension sags across 1:34–1:58, a necessary but abstract stretch: coin, kurtosis, the CLT title.

**Clarity & correctness 7.5.**
- *For the score:*
  - Concrete before abstract: skewness is built term by term from the x − μ arrows (kf_07), four real chips are averaged into a dot, and the readings come before 2/√n and before the general formula.
  - Every number I recomputed matches.
  - Assumptions are stated: independence and finite variance, with the lighthouse.
- *Deductions:*
  1. The climax, as set out in the FACTS row. The episode tells the viewer that the tails of the averages need 1,420 waits. The plotted tails reach 2–3% at about 150. The real reason A-B tests need about 1,420 (estimating σ from the same skewed data, which leaves t-interval misses at 1.0% / 7.2% for n = 30) is never mentioned. A viewer could not re-derive "1,420" from what is shown.
  2. In the root-n "why" (1:20–1:31, kf_17) the stacks are unlabeled blocks, and "the spread only doubles" (√4 = 2) is asserted rather than drawn.
  3. The answer frame (n = 1,420, both meter bars in the band) is fully lit for only about 1.2 s: lit 2:39.6–2:40.6, dimming by 2:40.8.
  4. "kurt" carries no "excess" label (kf_21).

**Visual 8.** The palette holds for the whole episode:
- blue for pieces, yellow for averages, green for the bell, red for the extreme piece, purple for the median, gray/ink for rules, sample sizes and citations
- charts tagged "simulated" or "exact"
- citations bottom-left at ≥ 24 px

Deductions (more than two minor issues):
- From 1:20 to 1:31 the equation reads "skew(x̄) = [blank] · E[(x−μ)³]/σ³", with a dangling "·" (kf_17). At 1:19.2 a duplicate floating "skew(x)" appears (extracted frame).
- The tail meter has no labels of its own: the green dashed line and the gray band are unlabeled (kf_25, kf_27).
- The lighthouse end frame carries about 12–13 prose words in two competing focal areas (kf_34).
- The y-label "share" sits in the header row and reads as "share n = 1" (kf_17, kf_19).
- Near-empty dissolve frames run under live narration at 2:53.2 ("Now the condition") and at 3:43 ("So the answer is over a thousand").

**Motion 8.5.** Most motion encodes a relation:
- chips arc out of their bars and the 9.5 drops into panel 2
- the ×4 / ÷2 arcs, and the 2/√n copies converging into one formula
- a formula copy arcs down into kurt(x̄)
- the 30 flies from the panel header into the radicand
- the n = 30 panel morphs into n = 1,420 while the meter bars rise into the band
- the 902-mile beam yanks the running mean
- the shore line slides into the waits axis

Deductions:
- the formula split at 1:18.6–1:20
- the 1.2 s payoff hold
- the two dissolves that leave the frame almost empty

**Audio 8.**
- Loudness is on target, and the pace is 158 wpm.
- Deictics land: "tail" with the brace at 0:03; "here" with the dot at 0:53; "this perfect bell in green" at 1:05; "900 miles" with "902 mi →" at 3:15.
- Deductions: almost every sentence boundary has the same 0.4–0.6 s gap (about 70 of them), which is metronomic. There is the drawn-out "so so" at 3:32, and the waits/weights ambiguity at 0:00 for audio-only listeners.

**Concision 8.**
- 601 words at 3:55, five seconds under the cap.
- One double statement: "two over root n, and two is the skewness of one wait. So the lean of an average is the lean of one piece, over root n" (1:09.5–1:17.9) says the same generalization twice.
- 2:17–2:52 packs 355, 0.053, 1,420, 18, 114,000, $10 and 10,000 into 35 s.
- Under 10% is slack overall, but fix 1 needs about 6 s, and that time has to come from somewhere.

**Originality 9.**
- Reading an industry rule of thumb off the episode's own skew/√n formula is the kind of non-obvious link viewers share. Kohavi et al. 2022 published the 0.053 form, but no explainer I know builds to it.
- "The bell was never in the data. It's in the average." is a memorable reframe of the first frame.
- The lighthouse is a classic, but it is staged as a live measurement (902 mi, 0.9 mi, half within a mile both before and after averaging).

Weighted = (15·8.5 + 25·7.5 + 15·8 + 15·8.5 + 10·8 + 10·8 + 10·9)/100 = 812.5/100 = **8.1**.

## FIXES (highest impact first)

1. **[2:05–2:41][Clarity/correctness] Make the tail meter measure what Kohavi's rule controls.**
   - **Problem:** the meter shows the known-σ tails of x̄ (Gamma exact). Those already land in 2–3% at n ≈ 150 (2.03% / 2.93%), so "1,420, and both tails land inside" implies a threshold the picture does not support. The 355·s² rule is the *estimated-σ* (t-interval) threshold (Deng, *Causal Inference…* ch. 8; Boos & Hughes-Oliver 2000).
   - **Change:** keep the n = 30 histogram and the cut lines, but switch the meter bars to the miss rates of the 95% interval an A-B test actually computes, using the sample SD. Simulate exponential waits with ≥ 10⁶ replications and label the meter "simulated".
     - n = 30: the interval lies wholly below μ **7.2%** of the time and wholly above μ **1.0%** (my run: 7.21% / 1.00%, MC se 0.02).
     - n = 300: still outside the band, at 3.66% / 1.68%. This shows why the "300" chip is wrong.
     - n = 1,420: 3.00% / 2.09%. Both are on the band's edge, which is exactly what Kohavi's rule guarantees.
   - **Narration, 2:05–2:17:** "But tests live in the tails, and they estimate the spread from the same lopsided data. A ninety-five percent interval should miss two and a half percent each way. With thirty waits it misses one percent on one side and seven on the other."
   - **Narration, 2:31–2:39:** "Three hundred still misses. For these waits: fourteen twenty, and both misses reach the band."
   - **Visual:** recolor the meter label to "interval misses (simulated)". Morph the n = 30 bars (1.0 / 7.2) through n = 300 (1.7 / 3.7, still outside) into the n = 1,420 bars (2.1 / 3.0). The narration then answers "over a thousand" with the picture.
   - **Alternative if the producers want to keep the exact Gamma meter:** add one sentence with a third meter state: "With the true spread known, about a hundred fifty would do. Tests estimate it, which roughly triples the damage." Show the bars at n = 150 (2.03 / 2.93) before 1,420.
   - **Cost:** either way about +5 s. Pay for it with fix 5.
   - **Effect:** lifts Clarity to about 9.
2. **[2:39.6–2:41][Clarity/Motion] The answer to the cold-open question is fully lit for only about 1.2 s.**
   - **Change:** add `[pause 1.0]` after "land inside". On "inside", Indicate both meter bars and the band together (≤ 1 s). Start the dim only on "Bing's". Hold the finished state ≥ 2.5 s.
3. **[1:18.6–1:31][Visual/Motion] The formula split shows a duplicate "skew(x)" at 1:19.2 and a dangling "·" until 1:31.**
   - **Change:** use TransformMatchingTex so "= skew(x)/√n" stays fixed. Put a dashed gray rounded box the size of n/n^{3/2} in the empty slot from 1:20. At 1:31 the "×n" and "×n^{3/2}" labels fly into that box.
4. **[1:20–1:30][Clarity] The block stacks are unlabeled, and "the spread only doubles" is asserted.**
   - **Change:** caption the stacks "cubed gaps" (blue) and "spread³" (gray), in Text ≥ 18 under each stack.
   - On "the spread only doubles" (1:24.5), grow a gray bar from σ to 2σ above the gray stack, labeled "×2 (= √4)".
   - On "its cube grows eight times", the 8 blocks stack out of that bar.
5. **[1:13.5–1:17.9, 2:46–2:52][Concision] Buy about 6 s for fix 1.**
   - Cut "So the lean of an average is the lean of one piece, over root n." The formula morph from 2/√n to skew(x)/√n already says it; keep the morph silent under a 0.6 s pause.
   - Shorten the Bing cap line to "Capping revenue at ten dollars a week: under ten thousand."
6. **[whole episode][Audio] The cadence is metronomic, and "so so" at 3:32.**
   - **Change:** in narration_text.py, cut intra-beat gaps to 0.2–0.3 s and keep 0.8–1.0 s only at beat boundaries (0:43.9, 1:17.9, 1:34.6, 1:58.1, 2:52.3, 3:30.5, 3:42.4). That also recovers about 6 s.
   - Rephrase the line to "The theorem needs finite variance: no single piece can outweigh the rest."
7. **[0:04–0:20][Clarity] Two empirical claims have no citation on screen until 1:59 and 2:19.**
   - **Problem:** "Textbooks say the average of 30 is safe…" and "on revenue data, thirty is off by a factor of thousands".
   - **Change:** show "Montgomery & Runger, 2010" (0:04–0:08) and "Kohavi et al., 2014 · KDD" (0:15–0:20), gray, bottom-left above y = −3.2, each held ≥ 3 s.
8. **[2:53, 3:43][Motion/Visual] Near-empty dissolve frames under live narration.**
   - **Problem:** the 3:43 frame carries "So the answer is over a thousand", the episode's key line.
   - **Change:** overlap the fades so the incoming scene starts when the outgoing one is at 30%. For the landing, have the cold-open frame fully up before "So the answer", with the 1,000+ chip lighting on "thousand" (currently it lights about 1.5 s late, at 3:45).
9. **[1:43–1:58][Clarity] "kurt" is excess kurtosis.**
   - **Change:** label it `\text{ex.\,kurt}(\bar x) = \text{ex.\,kurt}(x)/n`, or add a gray "(bell = 0)" note under it so the on-screen formula is true as written.
10. **[2:09–2:41][Visual] The meter's green dashed line and gray band are unlabeled.**
    - **Change:** put a green "2.5%" Text (≥ 18) at the right end of the dashed line. Transform it into a gray "2–3%" on "two and three percent". (With fix 1, also show "should miss" or "misses" captions.)
11. **[0:47–1:58][Visual] The y-label "share" reads as part of the "n = 1" header.**
    - **Change:** rotate it beside panel 1's y-axis at mid-height.
12. **[0:00][Audio] Audio-only listeners hear "a hundred bus weights".**
    - **Change:** say "A hundred waits for a bus: mostly short, with a long tail."

REACHES 9 IF ALL FIXED: yes. No structural change is needed:
- the hook commits to a number
- the fail beat is measured
- the formula grows out of the data
- the payoff is cited and rearranges into the episode's own formula
- the limit is stated and demonstrated
- the landing re-sees the first frame

Fix 1 is mandatory. Without it, the climax of a correctness-first episode answers its own question with the wrong measurement, and a statistician viewer will say so in the comments. With fix 1 (Clarity about 9), fixes 2–4 (Visual and Motion about 9), fixes 5–6 (Concision and Audio about 8.5–9) and Hook 8.5–9, the weighted score comes out at about 8.9–9.1.

KEEP:
- The cold-open chips 30 / 300 / 1,000+ are answered at the landing: the 1,000+ chip lights, the arrow becomes "average of 1,420", and the real bell grows beside the unchanged lopsided histogram: "The bell was never in the data. It's in the average."
- The panel row (kf_17): ×4 header arcs, ÷2 reading arcs, and per-panel 2/√n converging into skew(x̄) = skew(x)/√n. The formula is read straight off the data.
- The lighthouse run: flash 841 (902 mi) yanks the running mean by 0.9 mi; half of single flashes and half of 1,000-flash averages land within a mile; the purple median flattens to 0.
