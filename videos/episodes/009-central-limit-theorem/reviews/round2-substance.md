# Round 2 review: substance (science and story editor)

Evidence: `review/` pack (metrics.json 17:32 is newer than final.mp4 17:30, so it was reused). I read report.md, all 13 contact sheets, the full-resolution keyframes kf_02, 06, 09, 17, 20, 24, 27, 29, 32, 36, 38 and 40, and frames I extracted at 0:05.6, 0:06.0, 0:47.0, 0:54.5, 1:05.6, 1:06.4, 2:25.0 and 2:26.5. I also read the transcript, word timings, script.md, facts.md, narration.txt and CHANGELOG.md. I recomputed every number with scipy, and from `data.npz` for the simulated values. I checked the Kohavi et al. 2014 PDF (exp-platform.com) line by line and verified the Gull 1988 attribution by web search.

```
EPISODE: 009 — "Why Bell Curves Are Everywhere, and When They're Not"
IDEA: Collecting more lopsided data never makes it bell-shaped. Averaging does, because an average's skewness is one piece's skewness over root n, and that only works when no single piece can outweigh the rest (finite variance).
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 8 · Audio 8 · Concision 8 · Originality 9
WEIGHTED: 8.2   AFTER CEILING: 8.2 (lowest 8 + 2 = 10, so the ceiling does not bind)
CAPS: none (no wrong number found; all empirical claims carry an on-screen citation; mechanics within limits; 0 banned phrases)
FINAL: 8.2   PASS: no
```

## FACTS

| Claim | Status | Source / recomputation |
|---|---|---|
| Exponential waits have skewness 2; bars 1.90 / 1.96 / 2.00 / 1.98 | Verified | data.npz src_skew = 1.9004 / 1.9581 / 2.0047 / 1.9777 |
| Skewness = E[(x−μ)³]/σ³; a bell scores 0 | Verified (but see the narration wording in fix 4) | standard; identical to Kohavi et al. Rule #7 |
| (5.2 + 1.8 + 25.7 + 5.3)/4 = 9.5 | Verified | 38.0/4 = 9.50; seeded draws 5.206, 1.797, 25.692, 5.292 |
| Averages of 4 / 16 / 64 have skew 0.99 / 0.50 / 0.25 | Verified | data.npz 0.989 / 0.501 / 0.252; exact 2/√n = 1, 0.5, 0.25 |
| skew(x̄) = n/n^{3/2} · E[(x−μ)³]/σ³ = skew(x)/√n | Verified | third cumulant of a sum is nκ₃ and variance is nσ², so nκ₃/(nσ²)^{3/2}; needs a finite third moment |
| Coin p = 0.1: skew 2.67; share of heads in 64 flips: 0.33 = 2.67/√64 | Verified | (1−2p)/√(p(1−p)) = 0.8/0.3 = 2.667; binom(64, 0.1) skew = 0.3333 |
| "That's the central limit theorem" (said right after the skew/√n rule) | Imprecise | skewness → 0 is necessary, not sufficient, for a bell (a uniform has skew 0). See fix 1 |
| CLT needs independent pieces plus finite variance | Verified | Lindeberg–Lévy (i.i.d., finite variance) |
| "Textbooks say thirty is usually enough … whatever the shape"; on screen "Montgomery & Runger, 2010, via Kohavi et al., 2014" | Verified | Kohavi PDF: "Applied statistics books will suggest that small numbers usually suffice. For example, one [42] states 'In many cases of practical interest, if n ≥ 30, the normal approximation will be satisfactory regardless of the shape of the distribution.'" Ref: Montgomery, *Applied Statistics and Probability for Engineers*, 5th ed., Wiley 2010 (co-author Runger) |
| "A-B tests lean on that bell" | Verified | Kohavi: "Experimentation methodologies typically rely on the means, which are assumed to be normally distributed." |
| "On revenue data, thirty is off by a factor of thousands" | Verified | 114,000/30 = 3,800 |
| 2/√30 = 0.37 | Verified | 0.3651 |
| n = 30 tails 1.40% left, 3.40% right | Verified | Gamma(30, 10/30): 1.403% / 3.402% |
| Each tail between 2 and 3% | Verified | Kohavi: "both two tail probabilities (nominally 0.025) are no greater than 0.03 and no less than 0.02" |
| Rule n ≥ 355·s² | Verified | Kohavi Rule #7 (derived from Boos & Hughes-Oliver 2000, *Am. Stat.* 54(2):121–128) |
| Rearranged: s/√n ≤ 1/√355 ≈ 0.053 | Verified on screen; spoken "under point oh five" is imprecise | 1/√355 = 0.05307. At 2:31 the screen shows n = 1,420 with skew = 0.053, which is *not* under 0.05. See fix 2 |
| 355·2² = 1,420; tails 2.35% / 2.64% | Verified | Gamma(1420): 2.351% / 2.644% |
| Bing Revenue/User skew near 18, 114k users; on screen 355·17.9² ≈ 114,000 | Verified | Table (corrected Jan 2015): 17.9 and 114k; text 18.2; 355·17.9² = 113,746. Table caption: "a few select metrics from Bing" |
| Capped at $10/user/week: skew about 5, under 10,000 users; on screen 355·5.2² ≈ 9,600 | Verified | "skewness drop from 18 to 5.3"; table 5.2 and 9.7k; 355·5.2² = 9,599 |
| "Ron Kohavi's team at Microsoft" | Mostly verified | Kohavi and Deng: Microsoft. Longbotham is listed at SW Jiaotong Univ., Xu at LinkedIn. The on-screen citation names all four authors. See fix 9 |
| Lighthouse problem, Gull 1988; Sivia & Skilling 2006 | Verified | Gull, "Bayesian Inductive Inference and Maximum Entropy", in *Maximum-Entropy and Bayesian Methods in Science and Engineering* (Kluwer, 1988), doi:10.1007/978-94-009-3049-0_4 |
| Farthest of 1,000 flashes is typically about 900 mi; this run 902 mi; 902/1000 ≈ 0.9 mi | Verified | median of max = tan(π/2·0.5^{1/1000}) = 919 mi; data.npz flash 841 = 901.6 mi |
| Half of single flashes land within a mile | Verified | (2/π)·arctan 1 = 0.5; this run 0.506, quartiles −1.08 / 0.90 |
| The average of 1,000 flashes, repeated 200 times: still only half within a mile; 12 beyond each edge | Verified | the mean of n Cauchy draws is standard Cauchy; data.npz 0.500, quartiles −0.99 / 1.02; 12/12 beyond ±5.5 |
| Cauchy has infinite variance; the median homes in | Verified | E[X²] = ∞; median SD π/(2√n) = 0.05 at n = 1000; run ends at −0.079 |

No fabricated or misattributed source. No wrong number. Two wordings are imprecise enough that a sharp viewer will catch them: fix 1 (CLT equated with the skewness rule) and fix 2 ("under point oh five" next to 0.053).

## MECHANICS

runtime 3:46.5 · wpm 157 (speech) / 151 overall · max silence 1.97 s (1:53.1–1:55.1, a planned prediction pause) · leading 0.00 s / trailing 1.88 s · max static 3.03 s (2:12.6–2:15.7) · −14.0 LUFS / −1.6 dBTP · WER 3.4% · 0 banned phrases. No mechanical cap.

Transcript notes: "waits" was heard as "weights" 7 times. These are homophones (/weɪts/), so this is not a mispronunciation. At 1:44.2, "we'll get to" was heard as "will get two", which is a likely slur. At 0:55.3–0:56.0, "Repeat" is missing from the transcript; there is a 0.6 s gap before "10,000", so the word may be clipped. Deixis lands: "this tail" @0:05.3 has the brace visible at 0:05.6, and "this perfect bell" @1:05.5–1:06.7 has the green curves tracing from 1:06.4.

Banned-pattern sweep: no "it's not just X", no question chains (single questions at 0:09 and 1:51), no triplets, no fake reveals. The colon constructions ("Their rule: …") carry content. "It's tempting to say yes" is fine.

## STRUCTURE (§6)

- Cold open 0:00–0:12: histogram on frame 1, question at 0:09, 2 s hold. ✓
- Stakes 0:12–0:26: the "factor of thousands" line sets up the payoff. ✓
- Naive build and fail 0:26–0:46: measured with a live skew of about 2 at every n. ✓
- Insight 0:46–1:45: chips → mean → panels → readings → formula → why root n. ✓
- Payoff 1:45–2:46: textbook 30 → measured tails → Kohavi's rule is our formula → Bing. ✓
- Honest limit 2:46–3:36: the lighthouse. ✓
- Landing 3:36–3:45: the cold-open frame returns and the bell moves into the average. ✓

This is a complete and well-built arc. The weak spots are two:
- **The opening question.** Most viewers will answer "no" to it, and "It's tempting to say yes" signals that "no" is right, so the commitment is weak.
- **The 2:12–2:46 stretch.** It packs a rule, a rearrangement, 1,420, 114,000, a cap and 9,600 into 34 s.

## FIXES (highest impact first)

1. **[1:38–1:41][Clarity] The video equates the CLT with the skewness rule.**
   - **Problem:** "…its averages make the same bell, by the same rule. That's the central limit theorem." The rule only shows that lopsidedness vanishes. Zero skew does not make a bell: a uniform distribution has skew 0 and is flat. The title promises *why* bells appear, and this is the one step the viewer cannot re-derive.
   - **Change:** after "by the same rule", add one sentence and one visual, e.g. "And every other way a shape can differ from the bell, like fat or thin tails, fades even faster, as one over n. Only the bell survives. That's the central limit theorem."
   - **Visual:** under the n = 64 panel, add a small gray "tail weight ∝ 1/n" line next to skew(x̄), or a second reading row (excess kurtosis for the waits: 6 → 1.5 → 0.38 → 0.09) that falls by ÷4 while skew falls by ÷2.
   - **Cost:** about 7 s. Pay for it with fix 6.
   - **Effect:** lifts Clarity to 9.

2. **[2:21.8–2:26.1][Clarity/correctness] "asking for a skewness under point oh five" contradicts the screen.**
   - **Problem:** the screen shows ≈ 0.053, and at 2:31 it shows n = 1,420 with skew = 0.053, which is above 0.05.
   - **Change:** narration "…asking for a skewness of about point oh five or less", or "…at most one over root three fifty-five, about point oh five". Keep "≈ 0.053" on screen.

3. **[1:45–2:46][Visual] Two chart-labeling gaps.**
   - **Problem:** the n = 30 / n = 1,420 panel is an exact Gamma model of the waits, but it carries neither "exact" nor "simulated", while every other panel is tagged. The panel histograms (0:49–1:45) and the n = 30 panel also have no y-axis quantity (§5: every axis carries a quantity name and unit).
   - **Change:** add the gray italic "exact" tag bottom-right from 1:47 (the same style as the coin beat's "exact" at 1:37). Add a single shared gray y-label "share of averages" left of panel 1, font LABEL−2, and the same label on the n = 30 panel.

4. **[0:36–0:40][Clarity] "the average cubed distance from the mean" implies |x−μ|³.**
   - **Problem:** an average of absolute cubed distances is never zero, so "a perfect bell scores zero" would be false under the spoken definition. The on-screen x−μ arrow is right; the word "distance" is not.
   - **Change:** "the average cubed gap from the mean, left gaps counting negative, over the spread cubed". On "negative", flash a short leftward blue arrow from μ with a "−" sign for ≤ 1 s.

5. **[2:12–2:46][Concision/Clarity] Too many new numbers in one stretch.**
   - **Problem:** 355, 0.05, 1,400, 18, 114,000, $10, 5 and 10,000 arrive in 34 s. On first watch the Bing capping sentence is hard to parse, as the 0.4 s pause in the middle of it shows.
   - **Change:** cut "and both tails land inside" (the live 2.35% / 2.64% already show it). Cut the cap sub-beat to one clause: "Capping revenue at ten dollars a week cut that to under ten thousand." Keep the dot-arc animation and the "capped 9,600" marker. This saves about 4 s.

6. **[1:45.4–1:49.5][Concision] The textbook-30 line is a double explanation.**
   - **Problem:** "A classic textbook says thirty is usually enough, whatever the shape" repeats the stakes line at 0:17 almost word for word.
   - **Change:** shorten to "Back to the textbook's thirty." The citation and the gray "textbook 30" marker carry the rest. This saves about 3 s for fix 1.

7. **[0:00–0:12][Hook] The prediction is too easy, and the next line gives it away.**
   - **Problem:** "Will this shape turn into a bell curve?" is one most viewers answer "no", and "It's tempting to say yes" then confirms that "no" is right.
   - **Change:** sharpen the commitment so the likely answer is wrong, e.g. keep the histogram and ask "A textbook says thirty is enough for a bell. How many of these waits do you need before their average is safe to treat as one: 30, 300 or 3,000?" Show three gray chips and hold 1.5 s. The payoff at 2:21–2:31 (1,420) then resolves the opening exactly, and the landing still works.
   - **Alternative:** keep the current question but cut "It's tempting to say yes", and let the bars answer it at 0:30.

8. **[2:29–2:46][Visual] The sample-size markers break the declared palette.**
   - **Problem:** the "waits 1,420", "Bing revenue 114,000" and "capped 9,600" markers and dots are BLUE, but the script's palette assigns sample sizes to GRAY and BLUE to single pieces.
   - **Change:** make the dots and numbers INK/gray like "textbook 30". Keep the blue only on the 2², 17.9² and 5.2² terms, which are skew(x).

9. **[2:12.1–2:15.4][Clarity/attribution] "Ron Kohavi's team at Microsoft" overstates the affiliations.**
   - **Problem:** two of the four authors were not at Microsoft at publication (Longbotham: SW Jiaotong Univ.; Xu: LinkedIn).
   - **Change:** narration "Ron Kohavi and colleagues, using Bing's data, want each tail…". This also introduces Bing before 2:31.

10. **[1:44.2][Audio] "we'll get to" reads as "will get two".**
    - **Change:** rewrite to "…plus one condition, which comes later", or respell "we'll" in narration_text.py. Re-check with whisper.

11. **[0:55.3–0:56.0][Audio] "Repeat" is absent from the transcript.**
    - **Change:** check the TTS segment. If it is clipped, insert a 0.15 s lead-in pause before "Repeat" or change the line to "Do that ten thousand times."

12. **[0:46.5–0:48.0][Motion] A near-empty transitional frame.**
    - **Problem:** at 0:47.0 there is a small histogram at left and a lone tiny "1.98" crossing about 12 units of empty frame. The flight reads as a stray glyph.
    - **Change:** keep the "skew = 1.98" label at full LABEL size during the flight, and start panels 2–4 fading in at the same moment so the destination is visible.

13. **[3:39–3:41][Visual] The landing frame shows "100,000 waits" twice.**
    - **Change:** in the rebuilt cold-open frame, change the arrow label to "collect more" until it becomes "average of 64".

14. **[1:51][Motion] The formula copy overlaps itself mid-transform.**
    - **Problem:** at 1:51.0 the formula copy sits exactly on top of the original, giving a doubled "skew(x̄) =".
    - **Change:** move the copy down 0.9 units with a path_arc before the TransformMatchingTex, so the two never overlap.

REACHES 9 IF ALL FIXED: yes, plausibly.
- There is no structural problem: concrete-first, a measured fail, a formula grown from readings, a sourced payoff that rearranges into the episode's own formula, an honest limit and a landing that re-sees the cold open.
- What keeps it at 8 is substance precision, a soft prediction and a crowded payoff:
  - Fixes 1 and 2 lift Clarity to 9.
  - Fixes 5 and 6 lift Concision to 9.
  - Fix 7 lifts Hook to 9.
  - Fixes 3, 8, 12 and 13 clear the visual nits.
- With Hook 9, Clarity 9, Visual 8.5, Motion 8.5, Audio 8.5, Concision 9 and Originality 9, the weighted score is about 8.9–9.0. So fixes 1, 2, 5 and 7 are all required, not optional.

## KEEP
1. The "Rearranged, it's our formula" beat (2:17–2:31): Kohavi's 355·s² rule turned into skew(x̄) ≤ 1/√355 on screen, then validated live in the tails (1.40% / 3.40% → 2.35% / 2.64%). It is original, correct, and the strongest moment in the episode.
2. The readings-to-formula build (1:07–1:30): ×4 / ÷2 arcs, 2/√n under each reading converging to skew(x)/√n, then the formula opening up into n/n^{3/2}.
3. The lighthouse (2:46–3:36) with flash 841 (902 mi) yanking the running mean, and the landing line "The bell was never in the data. It's in the average." over the rebuilt cold-open frame.
