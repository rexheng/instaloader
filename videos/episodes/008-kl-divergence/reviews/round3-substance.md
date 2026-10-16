# Episode 8: round 3 review (substance / science-editor pass)

**Evidence.** I used the existing pack in `review/`, because metrics.json (23:06) is newer than final.mp4 (23:04). I read:
- report.md, narration_diff.txt, transcript.txt and transcript_words.tsv;
- script.md, facts.md, narration.txt and CHANGELOG.md;
- all 12 contact sheets;
- full-resolution keyframes kf_02, 06, 09, 14, 18, 20, 22, 25, 27, 31, 36 and 38;
- extra frames I extracted at 0:11.0, 0:11.6, 0:12.2, 0:12.6, 1:46.9 and 2:31.0, plus a 5 fps strip over 1:46.2–1:47.8.

**Independent recomputation.** I wrote my own script and did not use data.py. It loads faithful.csv and runs:
- my own 2-normal EM fit;
- KL integrals on a 200k-point grid;
- Nelder–Mead minimization for both orders;
- R's bw.nrd0 Gaussian KDE;
- a leave-one-out likelihood CV scan over 0.050–0.400 min.

**Citations.** I checked them by web search: Kullback & Leibler (Encyclopedia of Mathematics / Project Euclid listing) and Blei et al. 2017 (ar5iv full text, sentence quoted below).

```
EPISODE: 008 — "The Distance That Isn't Symmetric"
IDEA: KL divergence only charges where its first argument puts mass, so with the data first a single bell must cover both Old Faithful humps (A), while with the bell first it can drop a hump but must not put mass where eruptions never happen (B).
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6   AFTER CEILING: 8.6   (127.5+212.5+127.5+127.5+85+85+90 = 855 → 8.55 → 8.6; lowest 8.5 → ceiling 10.5)
CAPS: none (every number recomputes, no fabricated or misattributed source, 0 banned phrases, mechanics inside all caps, no overlap at rest)
FINAL: 8.6   PASS: no
```

## FACTS (my recomputation in brackets)

| Claim | Verdict | Source / check |
|---|---|---|
| 272 eruptions, R `faithful`, Härdle 1991 | Verified | n = 272; R docs: source W. Härdle, ref. Härdle 1991 *Smoothing Techniques with Implementation in S* |
| "More than a third are short ones", "36%" box | Verified | 97/272 = 35.7% under 3 min |
| Smoothed curve = 2-normal ML mixture, which keeps the sample mean and SD | Verified | EM: weights 0.348/0.652, means 2.019/4.273, SDs 0.236/0.437; mixture mean 3.4878, SD 1.1393 = sample (1/n) values |
| Bell A = 3.49 ± 1.14 min, closest data-first ("three and a half, give or take 1.1") | Verified | Nelder–Mead from an offset start → 3.48778 ± 1.13927 |
| D(data‖A) = 0.76 bits | Verified | 0.7619 |
| "Shift it or stretch it, and that number only grows": 1.12 and 1.11 on screen | Verified | −0.8 min shift → 1.1176; σ×1.8 → 1.1112. The objective is convex in (μ, log σ) |
| D(A‖data) = 1.69 bits ("1.7"), ×2.2 ("more than twice") | Verified | 1.6948; ratio 2.224 |
| At 2.0 min: p = 0.59, q = 0.15, "about a quarter", log₂(p/q) = 1.98 ("two doublings") | Verified | p = 0.5881, q = 0.1493, q/p = 0.254, log₂ = 1.978, 4q = 0.597 |
| Grey dips "pay a little back" | Verified | Negative part of A's data-first integrand = −0.175 bits |
| Bell B = 4.27 ± 0.44 min, closest bell-first | Verified | 4.2712 ± 0.4408. Other local minimum on the short hump: 2.020 ± 0.237 at 1.519 bits (worse) |
| q_B(2) = 1.6×10⁻⁶, "18 and a half doublings" | Verified | 1.5605×10⁻⁶; log₂(p/q) = 18.524 |
| D(data‖B) = 5.77 ("5.8"); "peak ≈ 11" bits/min | Verified | 5.7661; integrand peak 10.98 at 1.97 min |
| D(B‖data) = 0.62 ("point six two") | Verified | 0.6161 |
| B "almost never imagines a short eruption" | Verified | B's mass below 3 min = 0.20% |
| A "imagines eruptions in the gap" | Verified | A's mass in 2.5–3.5 min = 31.1% vs raw data 12/272 = 4.4% |
| "less than half as wide" | Verified | 0.4408/1.1393 = 0.387 |
| (0.44/1.14)² = 15% | Verified (arithmetic) | 0.1497. The *framing* as "the posterior's variance" is a stand-in; see Fix 2 |
| R default smoothing bw.nrd0 = 0.335 min → best bell-first fit 3.55 ± 0.99 (global) | Verified | h = 0.33478; from A → 3.547 ± 0.992 (0.567 bits); from B → 4.188 ± 0.615 (0.598). The wide fit is the global minimum |
| LOO-CV smoothing keeps the fit on one hump: 4.28 ± 0.39 | Verified | CV picks h = 0.103 (LOO log-lik −270.8); fit 4.275 ± 0.389 (0.698 bits) |
| "With raw points, D(bell‖data) = ∞ for every bell" | Verified, but misleading by omission | True (bell ≪̸ empirical). D(data_raw‖bell) is also ∞ under the measure-theoretic definition; maximum likelihood ranks bells by the finite bell-dependent part. The footnote implies only the bell-first order breaks. See Fix 9 |
| KL divergence named for Kullback & Leibler, 1951, *Annals of Mathematical Statistics* | Verified | "On Information and Sufficiency", AMS 22(1):79–86 (1951) |
| "Every maximum-likelihood fit is the closest model by it" (data first) | Verified | Bishop 2006 §1.6.1, eq. 1.119 |
| "Often called a distance", yet asymmetric | Verified | Bishop §1.6.1; Blei et al. 2017 fn. 2: "It is asymmetric … and nonnegative" |
| ML (data first) spans both humps; VI (model first) settles on one | Verified, slightly overstated | Bishop §10.1.2, Fig. 10.3 says VI "will **tend** to find one of these modes". The narration says "its fits stretch over every hump" and "it settles on one hump" as absolutes. See Fix 8 |
| VI minimizes KL(q‖posterior) | Verified | Blei et al. 2017, eq. 1 |
| "Blei and colleagues note that variational inference generally underestimates posterior variance" | Verified | Blei, Kucukelbir & McAuliffe 2017, *JASA* 112(518):859–877, §1: "We do know that variational inference generally underestimates the variance of the posterior density; this is a consequence of its objective function." |

## MECHANICS

runtime 3:27.4 · wpm 164 over speech time (157 overall, 183 excluding pauses) · max internal silence 1.96 s (0:12.4, the planned prediction hold) · max static 3.63 s (2:46.8) · −14.0 LUFS / −1.6 dBTP · leading silence 0.00 s / trailing 0.91 s · WER 1.3% · 0 banned phrases.

No cap triggers.

## Transcript and §4 scan

- **Banned phrases and patterns.** None found:
  - no "it turns out" or other signposting;
  - no chain of two or more questions (each question stands alone, at 0:12 and 1:57);
  - no "not just X" construction, no colon fake-reveals, no empty superlatives.
- **Recap risk.** "So closeness depends on which curve goes first" (3:16.7) is close to a restatement of the title (see Fix 10). The closing A/B pair is a real reframe, not a recap.
- **Names.** "cullback / lie blur / Bly" are the correct pronunciations of Kullback, Leibler and Blei. No mispronounced technical terms.
- **Hook.** The question "…or does it move to two or three?" ends at 0:12.5. The ghosts 2 and 3 appear on the words: "2" at 0:11.6, "3" at 0:12.2 (extracted frames). A 1.9 s hold follows. The commitment lands at about 0:12.5, so the hook is in time.

## Flipbook notes (contact sheets)

- **Beat structure follows §6:**
  - cold open 0:00–0:14;
  - stakes 0:14–0:27;
  - naive build with a live number 0:27–0:40;
  - fail, measured at ×2.2, 0:40–0:55;
  - insight: the doublings pull-out, then the weighted bill, 0:55–1:30;
  - second failure (B's 5.77 mountain) 1:30–1:46;
  - second prediction 1:46–1:59;
  - both bills, then the descent 1:59–2:33;
  - payoff 2:33–2:58;
  - honest limit 2:58–3:16;
  - landing 3:16–3:27.
- **Sync.** Deictics land within ±1 s throughout. Examples: "gray dips" → "refund" tag at 1:25; "more than a third" → "36%" at 1:41; "Every p trades places with q" → the swapped block at 1:51; "moves to 3" → arrow 1→3 at 2:31–2:33.
- **Persistence.** One chart lives for the whole episode; objects transform and nothing cuts hard.
- **Weak spots:**
  - The posterior stand-in on an eruption-length axis (2:38–2:58).
  - The undimmed "a distance" claim during its own refutation (0:41–0:55).
  - A transient tick-label garble at 1:46.9.
  - The six-line right column, 1:59–2:33.

## FIXES (highest impact first)

1. **[0:14–0:27][Hook] The stakes are abstract.**
   - Problem: the only stakes before 2:33 are "every maximum-likelihood fit is the closest model by it". The viewer bets at 0:12 without knowing why the answer matters, and the real consequence (Bayesian approximations under-report uncertainty) is held back for 2½ minutes.
   - Change: replace "and it's often called a distance between distributions" with "Bayesian AI uses it with the order flipped, and it's often called a distance." Write a small grey "variational inference" tag under "KL divergence" on "Bayesian".
   - Then at 2:38 the payoff answers a question the viewer has carried since 0:20. This lifts Hook to 9.
2. **[2:38–2:58][Clarity / payoff] The "15% of the posterior's variance" is computed on the eruption-data curve relabelled "posterior", on an axis still reading "eruption length (minutes)".**
   - Problem: a posterior lives over parameters, not eruption lengths. The narration states the 15% as a fact about a posterior ("Here, bell B keeps only fifteen percent of the posterior's variance"). The only real-world claim is qualitative (Blei).
   - Minimum change: narration "If this curve were a posterior, bell B would keep only fifteen percent of its variance." On screen, replace "same curve, as a stand-in" with "if this were a posterior".
   - Better change: after Blei's line, add one measured published case of mean-field VI vs MCMC posterior SDs, with author, year and venue on screen. For example, Giordano, Broderick & Jordan 2018, *JMLR*, "Covariances, Robustness, and Variational Bayes"; verify the exact figure before use. This turns the payoff into the real data-science result BAR §6 asks for.
3. **[2:51–2:57][Clarity] The ±1 SD brackets are labelled with σ but span 2σ.**
   - Problem: the blue bracket runs 2.35–4.63 min (2.28 min long) and is labelled "1.14"; the purple one runs 3.83–4.71 and is labelled "0.44". A viewer who reads the bracket against the x-axis gets lengths twice the labels.
   - Change: label them "±1.14" and "±0.44" (or draw half-brackets from the mean to mean + σ). Strip the "±" as the numbers fly into (0.44/1.14)².
4. **[0:41–0:55][Clarity] The refuted claim stays asserted on screen.**
   - Problem: the yellow label "a distance" (with its "?" removed at 0:29) stays fully lit while the narration shows it fails (×2.2).
   - Change: on "more than twice as far" (0:47), Transform "a distance" to grey with a strike line, or bring the yellow "?" back. The screen then records the failure the narration names.
5. **[1:46.8–1:47.2][Motion] Tick labels morph into junk glyphs.**
   - Problem: while the panels re-stack, the bill panel's y-tick labels Transform into the new panel's ticks ("1" → "ʔ", "−1" → "●0", "2" over "2"). This shows in the 5 fps strip at about 1:46.9.
   - Change: FadeOut the old tick labels (0.3 s) before the move and FadeIn the new ones after it. Never Transform one Tex numeral into a different one.
6. **[1:59–2:33][Visual] The right column reads as one six-line block.**
   - Problem: D(data‖bell) / = ∫… / = 5.77 bits and D(bell‖data) / = ∫… / = 0.62 bits are stacked at equal spacing, so the two bills' formulas visually merge.
   - Change: add 0.35 units of extra gap between the blocks, and vertically centre each block on its own panel. The top block would then sit about 0.2 higher, level with the data-first bill.
7. **[1:45.7–1:46.0][Audio] The beat turn after the payoff number is rushed.**
   - Problem: the gap after "five point eight bits" is only 0.3 s (word timings 105.66 → 105.96), and the narration runs straight into "Now keep that bill". The script's own rule is 0.7–1.0 s after a payoff number or at a beat turn.
   - Change: insert [pause 0.8] after "five point eight bits."
8. **[2:33–2:46][Clarity / accuracy] Two absolutes need softening.**
   - "so its fits stretch over every hump" overstates: maximum likelihood with a mixture family fits each hump. Change to "so a one-bell fit stretches over every hump".
   - "so it settles on one hump" overstates: Bishop says VI "tends to" find one mode. Change to "so it tends to settle on one hump".
9. **[3:03–3:16][Clarity] The footnote implies only the bell-first order breaks on raw points.**
   - Problem: "With raw points, D(bell‖data) = ∞ for every bell" suggests the data-first order is fine there. Strictly, D(raw‖bell) is also ∞; maximum likelihood ranks bells by the finite bell-dependent part.
   - Change the footnote to "Raw points: data first still ranks bells; bell first is ∞ for all" (≤ 12 words).
10. **[3:16.7–3:19.7][Concision / Hook] The first landing line restates the title.**
    - Change: replace "So closeness depends on which curve goes first." with "One, or three: it depends on which curve goes first." Briefly re-show the yellow 1 and 3 at A's and B's crowns. The landing then re-sees the cold-open bet exactly.
11. **[2:58–3:16][Concision] The honest-limit beat runs 18 s for one idea.**
    - Change: merge its sentences, saving about 3 s: "That needs the gap nearly empty. R's default smoothing fills it, and the best bell-first fit goes wide; cross-validated smoothing keeps it empty, and the fit on one hump." Keep both morphs.

**REACHES 9 IF ALL FIXED:** yes, narrowly.
- Fixes 1 and 10 → Hook 9.
- Fixes 2, 3, 4, 8 and 9 → Clarity 9. Fix 2 is the decisive one: the payoff must be a real result, not a relabelled data curve.
- Fix 6 → Visual 9.
- Fix 5 → Motion 9.
- Fix 7 → Audio 9.
- Fix 11 → Concision 9.

With Originality at 9, the weighted score is 9.0. Without Fix 2 the episode stays at about 8.7–8.8: its insight is canonical-quality, but its payoff is a textbook statement illustrated on a stand-in.

**KEEP:**
- The "double q twice" pull-out that turns log₂(p/q) into a count of doublings (1:00–1:13), together with the weighted bill and its refund dips.
- The two bills side by side with live totals, where one drains while the other swells along the descent A → B (1:46–2:33), answering the 1/2/3 bet on the same image.
- The closing pair "Bell A never misses an eruption that happens. Bell B almost never imagines one that doesn't."
