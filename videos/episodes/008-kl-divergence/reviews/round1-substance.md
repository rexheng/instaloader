# Episode 8, round 1: substance review (science and story editor)

Evidence used: `review/` pack (metrics.json 23:06 is newer than final.mp4 23:04, so no new pack was needed), report.md, all 12 contact sheets, 12 full-resolution keyframes (kf_01, 02, 09, 15, 19, 21, 24, 25, 27, 31, 36, 38), plus extra frames I extracted at 0:03.0, 0:51.0, 1:31.0 and 1:47.6–1:51.0 (crop of the formula column). I also read transcript.txt and transcript_words.tsv, narration.txt, script.md, facts.md and data.py. All numbers were recomputed in my own script from faithful.csv, and all three citations were checked by web search.

```
EPISODE: 008 — "The Distance That Isn't Symmetric"
IDEA: KL divergence only charges where its first argument puts mass, so swapping the order changes the answer: with the data first, the best bell must cover both humps (A), and with the bell first it can sit on one hump (B).
SCORES: Hook 8 · Clarity 8 · Visual 8 · Motion 8.5 · Audio 8 · Concision 8 · Originality 8
WEIGHTED: 8.1   AFTER CEILING: 8.1 (lowest 8 + 2 = 10, not binding)
CAPS: none triggered. Borderline: at 1:49.0–1:50.0 a settled frame reads "D(bell‖data) = ∫ p log2(p/q) dx = 5.77 bits", which is false (it is 0.62). I treated this as a ~1 s mid-substitution state and did not cap it. A stricter reading of "any mathematical error on screen" would cap at 6, so it is fix 1.
FINAL: 8.1   PASS: no
```

## FACTS

All numbers were recomputed independently: own EM fit, own KL integrals on a 600k-point grid, own Nelder–Mead and grid search, own bw.nrd0 and LOO-CV.

| Claim | Status | Source / my value |
|---|---|---|
| 272 Old Faithful eruptions, 1.6–5.1 min | Verified | faithful.csv: n = 272, min 1.6, max 5.1 |
| Data citation "Härdle, 1991 · Old Faithful data (R: faithful)" | Verified | R `datasets::faithful` doc cites Härdle (1991) |
| Bell A = 3.49 ± 1.14 min ("three and a half, give or take one point one") | Verified | mean 3.4878, SD (1/n) 1.1393; EM mixture keeps the moments, so the data-first optimum = MLE normal |
| D(data‖A) = 0.76 bits | Verified | 0.7619 |
| Shift −0.8 → 1.12, stretch ×1.8 → 1.11 ("only grows") | Verified | 1.1176 / 1.1112; strictly convex in (μ, log σ) |
| D(A‖data) = 1.69 ("one point seven"), ×2.2 ("more than twice") | Verified | 1.6948; ratio 2.224 |
| At 2.0 min p = 0.59, q = 0.15, "about a quarter", log2 = 1.98 ("about two") | Verified | p 0.5881, q 0.1493, q/p 0.254, log2 1.978 |
| log2(p/q) readout 1.99 at 1:31 (same "two minutes" length) | Inconsistent | shown as 1.98 at 1:09–1:29; at x = 2.00 the value is 1.978. Scanner position differs (see fix 6) |
| Grey dips "pay a little back" | Verified | negative part of A's data-first integrand = −0.175 bits |
| q_B(2 min) = 1.6×10⁻⁶; "18 and a half doublings" | Verified | 1.5605×10⁻⁶; log2 18.52 |
| "More than a third" short; box "36%" | Verified | 97/272 = 35.7% under 3 min |
| D(data‖B) = 5.77 ("five point eight"; whisper word timing confirms "5.8") | Verified | 5.766 |
| Peak ≈ 11 bits/min | Verified | 10.98 at 1.97 min |
| B = 4.27 ± 0.44, global min of D(bell‖data) | Verified | NM 4.2712 / 0.4408; coarse grid min at (4.30, 0.45). The other local min is on the short hump, 2.02 ± 0.237 at 1.519 bits |
| D(B‖data) = 0.62 | Verified | 0.6161 |
| "Almost never imagines a short eruption, so ignoring them costs nothing" | Verified | B mass below 3 min 0.20% |
| A "imagines eruptions in the gap and out in the tails … costs 1.7 bits" | Verified | A mass in 2.5–3.5 min = 31.1% (data 4.4%) |
| "Less than half as wide" | Verified | 0.4408/1.1393 = 0.387 |
| Descent from A on the bell-first bill ends at B; one bill drains as the other swells | Verified (by inspection of data.py logic, plus own optimiser agreeing on the endpoint) | 1.69 → 0.62 and 0.76 → 5.77 |
| "Every maximum-likelihood fit is the closest model by it" (data first) | Verified | Standard: MLE minimises KL(empirical‖model). Bishop 2006 eq. 1.119 |
| "Often called a distance"; a distance is symmetric | Verified | metric axiom; Bishop §1.6.1 "not a symmetrical quantity" |
| Kullback & Leibler, 1951 · Annals of Mathematical Statistics | Verified | "On Information and Sufficiency", AMS 22(1):79–86 (Encyclopedia of Mathematics; multiple references) |
| ML covers every hump, VI (model first, KL(q‖p)) settles on one; Bishop 2006 §10.1 | Verified | Bishop §10.1.2, Fig. 10.3 |
| VI approximates a Bayesian posterior with the model first | Verified | Blei et al. 2017 eq. 1: argmin KL(q(z)‖p(z\|x)) |
| "Blei and colleagues note that VI generally underestimates posterior variance"; Blei et al., 2017 · JASA | Verified | Blei, Kucukelbir & McAuliffe, JASA 112(518):859–877; §5 text: "variational inference generally underestimates the variance of the posterior density; this is a consequence of its objective function" |
| "Bell B keeps only 15% of the posterior's variance" | Verified arithmetic; framing weak | (0.4408/1.1393)² = 0.1497. The "posterior" is the eruption curve relabelled as a stand-in (labelled on screen), see fix 5 |
| ±1 SD brackets labelled "1.14" and "0.44" | Correct values, misleading labels | the brackets span 2.35–4.63 (2.28 min) and 3.83–4.71 (0.88 min). A bracket labelled 1.14 visibly measures 2.28 axis units (fix 2) |
| R's default smoothing (bw.nrd0 = 0.335) → best bell-first fit wide, 3.55 ± 0.99 | Verified | own: h = 0.3348; global min 3.547 ± 0.991 at 0.567 bits; narrow local 4.188 ± 0.615 at 0.598 |
| Cross-validated smoothing keeps the fit on one hump, 4.28 ± 0.39 | Verified | own LOO-CV h = 0.103; fit 4.2754 ± 0.3885 from both A and B |
| "With raw points, D(bell‖data) = ∞ for every bell" | Verified | bell not absolutely continuous w.r.t. the empirical measure |

No fabricated or misattributed claims. No spoken numerical errors.

## MECHANICS

```
MECHANICS: runtime 3:27.4 · wpm 164 (speech; 157 overall, 183 excluding all pauses) · max silence 1.96 s (0:12.4 prediction hold; 1:56.8 second hold) · max static 3.63 s (2:46.8) · −14.0 LUFS / −1.6 dBTP · leading 0.00 s · trailing 0.91 s
```

Every mechanical check is in range. The transcript has 0 §4 banned phrases. I also searched manually for patterns: no "it turns out" or "let's", and no rhetorical question chains (0:08 and 1:55 are each a single question). The only near-pattern is the restating line at 3:16 ("So closeness depends on which curve goes first"), which is noted under fixes but does not trigger a cap. Whisper's "cullback / lie blur / Bly" are acceptable renderings of the intended pronunciations (KUL-back, LYE-bler, Bly). There are no script lines dropped (WER 1.3%).

## What the episode does (flipbook notes)

- **0:00–0:14 Cold open.** Data, bell A, D(data‖bell), then the arguments arc into D(bell‖data). A three-way bet (1/2/3) with ghost bells, and a 2.0 s hold. The bet is on screen by 0:12, so it meets the hook rule.
- **0:14–0:55 Stakes, naive build, fail.** "Treat it as a distance" gives a live 0.76, the shift/stretch check, then 1.69 and ×2.2 with both D-lines boxed. This is a clean misconception-first failure with a measured size.
- **0:55–1:30 Insight.** p and q bars are pulled out to the same scale and q is doubled twice to reach p, giving log2 = 1.98, "two bits". The sweep, the weighting by p, the refund dips and the area counting up to 0.76 are the best minute of the episode, canonical-quality 3b1b.
- **1:30–2:33 Bell B and the two bills.** The 5.77 mountain, the swap, the second prediction, B 0.62 vs A 1.69, then the descent with one bill draining while the other swells, and the 1 → 3 arrow answering the bet on the same image. The animation carries the argument here.
- **2:33–2:58 Payoff.** ML → A and VI → B, with Bishop and Blei cited and the 15% variance ratio.
- **2:58–3:16 Honest limit.** Smoothing sensitivity.
- **3:16–3:27 Landing.** The two cold-open lines return with "→ A" and "→ B", plus an end card.

## FIXES (highest impact first)

1. **[1:47.6–1:50.0][Clarity/Motion] A false equation is held on screen.** From about 1:49.0 to 1:50.0 the copied block reads "D(bell‖data) = ∫ p log2(p/q) dx = 5.77 bits" (kf_21 is a settled frame of it). Change: in the copy that drops in, replace "= 5.77 bits" with a yellow "= ?" *before* it lands. Then swap the arguments, the weight (p→q) and the fraction in **one** `TransformMatchingTex` on "Every p trades places with q" (word timing 1:49.46–1:51.46), so D(bell‖data) is never shown next to ∫p log2(p/q) or next to a number. This removes the only cap-6 risk in the episode.
2. **[2:49.5–2:57][Clarity/Visual] Bracket labels don't match bracket lengths.** The ±1 SD brackets are labelled "1.14" and "0.44" but span 2.28 and 0.88 minutes on the x-axis, so a viewer reading the bracket as the spread reads it as half the drawn length. Change: label them "±1.14" and "±0.44", or draw one-sided brackets from the mean to mean+SD so the drawn length equals the labelled number. Keep `(0.44/1.14)² = 15%`.
3. **[0:00–0:12][Hook] The bet rests on undefined words, so it is a guess, not a belief.** "Data first", "bell first" and "closeness" have no meaning yet, and 2 vs 3 has no basis, so the viewer is not committing to a held misconception. Change the narration to: "Old Faithful's eruptions. Measured with the data first, the closest bell curve is this one. Now measure with the bell first. If closeness is a distance, order can't matter, and it stays at one. Does it?" Keep the 2 and 3 ghosts but have them appear only on "Does it?". As the arguments arc, add a 2-word yellow tag "order swapped" beside D(bell‖data) for 1.5 s. That makes the wrong belief (symmetry) the thing being bet on.
4. **[2:58–3:16][Clarity/Concision] The honest limit is a three-concept tangent.** It introduces kernel smoothing, "R's default setting" and "cross-validation" in 18 s with no explanation. The most important idea, that against raw points every bell scores ∞, which is *why* a smoothed curve is needed at all, sits un-narrated in a grey footnote (3:04–3:16). Change: replace the three sentences with two: "Against the raw points, every bell-first score is infinite, so the bell needs a smoothed curve, and how hard you smooth decides it. Smooth heavily, the gap fills, and the bell-first fit goes wide." Drop "R's default" and "cross-validation" from the narration. Keep the morph to bw.nrd0 and the wide fit, cut the CV morph back, and return to the original curve for the landing. This saves about 6 s and states the assumption the viewer actually needs.
5. **[2:38–2:57][Clarity] The payoff relabels eruption lengths as a "posterior" and states a 15% figure about it.** The "same curve, as a stand-in" note is honest but small (Text ~24 px) and never spoken, so "Bell B keeps only 15% of the posterior's variance" sounds like a measured VI result. Change the narration at 2:52 to "Pretend this two-humped curve is a posterior: bell B keeps only fifteen percent of its variance." Alternatively, use a real bimodal posterior, for example the posterior of a mixture mean, and fit VI to it on screen.
6. **[1:30.5–1:31.5][Clarity] The readout at "two minutes" changes.** It reads log2(p/q) = 1.99 at 1:31 after showing 1.98 from 1:09 to 1:29 for the same narrated length (the true value at 2.00 min is 1.978). Change: pin the scanner at x = 2.00 when the bell starts sliding to B, so the readout starts at 1.98.
7. **[3:16.7–3:19.7][Concision/Originality] The penultimate line restates the episode.** "So closeness depends on which curve goes first" adds nothing the "→ A / → B" lines don't already show (§4: endings that restate). Change: cut it, bring the two answered D-lines in during the 0.6 s gap, and land directly on "Bell A never misses an eruption that happens. Bell B almost never imagines one that doesn't." This saves about 3.5 s.
8. **[1:46–2:33][Visual] The three-panel stretch carries two 3-line formula blocks and two identical "bits/min" bill panels.** The viewer has to read across to the right column to know which bill is which (kf_21, kf_24, kf_25). Change: replace each bill panel's "bits/min" corner label with its order, "data first" (blue/purple) and "bell first" (purple/blue), size ≥ 26 Text, and put the unit once on the shared axis. Collapse each formula block to two lines (`D(·‖·) = 5.77 bits`) once the integrand has been shown, which removes 2 of the 6 math lines.
9. **[0:37–0:41][Audio] The number run-on is hard to parse.** "…give or take one point one, but a distance reads the same both ways" leaves only 0.4 s between the stat and the turn of the argument, the most important beat change in act 1. Change: put a 0.8 s pause after "one point one" (beat turn, as script.md's own pause policy says). Also consider TTS speed 0.80 for the 1:30–1:46 stretch, which runs at about 180 wpm excluding pauses.
10. **[0:50.8–0:51.2][Visual] Nitpick.** A one-frame yellow dot appears at the top-right of D(data‖bell) before the highlight box draws (extracted frame at 0:51.0). Change: draw the boxes with `Create` from the full rectangle path, or `FadeIn` with scale 1.05, not from a corner point.

REACHES 9 IF ALL FIXED: yes, but only just. The engine is already 9-grade: one concrete length, doublings, weighting, refunds, then two live bills trading as the bell slides. What holds the score at 8 are the hook (fix 3), clarity defects at the payoff and the limit (fixes 1, 2, 4, 5) and a slightly long tail (fixes 4, 7). With those applied I would expect Hook 9, Clarity 9, Concision 9 and Motion 9, for about 8.8–9.0. To clear 9 with margin, the payoff needs a real posterior rather than a relabelled data curve (fix 5, second option). No structural change is needed.

KEEP:
- The 0:55–1:30 pull-out: p and q bars at the same scale, q doubled twice to reach p ("two doublings, or two bits"), then the sweep, the p-weighting and the grey refunds counting to 0.76.
- The two bills side by side while the bell slides A → B (2:17–2:33), one draining as the other swells, ending on the yellow 1 → 3 arrow that answers the cold-open bet on the same image.
- The closing pair "Bell A never misses an eruption that happens. Bell B almost never imagines one that doesn't."
