# Episode 8: round 2 review (substance / science-editor pass)

Evidence: the existing pack `review/` (metrics.json 16:57 is newer than final.mp4 16:55). I read report.md, all 11 contact sheets, and keyframes kf_01, 04, 07, 16, 17, 19, 21, 23, 25, 28, 30, 33, 35, 37 and 39 at full resolution. I also extracted frames at 0:18, 1:11.0, 1:11.6, 1:19, 2:34, 2:39, 2:46 and 3:07 to check transitions. I recomputed every number from `faithful.csv` with my own script (my own EM fit, KL integrals on a 400k-point grid, Nelder–Mead and BFGS minimisation, R's bw.nrd0 kernel smoothing) without using data.py. I checked the citations with web search (Project Euclid and JSTOR for Kullback & Leibler; the arXiv HTML of Blei et al. for the quoted sentence).

```
EPISODE: 008 — "The Distance That Isn't Symmetric"
IDEA: KL divergence only charges where its first argument puts mass, so with the data first a single bell has to cover both humps of Old Faithful (A), while with the bell first it can drop a hump but must not put mass where eruptions never happen (B).
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8 · Audio 8 · Concision 8 · Originality 8
WEIGHTED: 8.2   AFTER CEILING: 8.2   (Σ = 127.5 + 212.5 + 120 + 120 + 80 + 80 + 80 = 820; lowest 8 → ceiling 10)
CAPS: none (no fact wrong or fabricated, 0 banned phrases, mechanics inside every cap, no overlap at rest)
FINAL: 8.2   PASS: no
```

## FACTS

| Claim | Status | Source / my recomputation |
|---|---|---|
| 272 Old Faithful eruptions, timed in minutes; Härdle 1991 · R `faithful` | Verified | 272 rows, range 1.6–5.1 min. R `datasets::faithful` docs give "Source: W. Härdle" and Härdle (1991), *Smoothing Techniques*, Springer |
| Bell A (data first) sits at the data's mean and spread, "three and a half, give or take 1.1", 3.49 ± 1.14 | Verified | sample mean 3.4878; SD (1/n) 1.1393. My EM mixture (0.348/0.652, 2.019/4.273, 0.236/0.437) reproduces those moments exactly |
| D(data‖A) = 0.76 bits | Verified | 0.7619 |
| Shifting or stretching A only raises it | Verified | convex in (μ, log σ) with its minimum at the moments. On screen it rises to 0.93 at 0:33.8 |
| D(A‖data) = 1.69, "1.7 … more than twice as far", ×2.2 | Verified | 1.6948; ratio 2.224 |
| At 2 min p = 0.59, q = 0.15, "about a quarter", "double q twice", log₂ = 1.98 | Verified | p = 0.5881, q = 0.1493, p/q = 3.94, log₂ = 1.978 |
| Clipped depths ↓ −45, ↓ −6.2, ↓ −20 | Verified (facts.md values; spot-checked −20.5 at 7 min) | |
| B (data first) at 2 min: q = 1.6×10⁻⁶, "eighteen and a half doublings" | Verified | q_B(2) = 1.560×10⁻⁶, log₂(p/q) = 18.52 |
| D(data‖B) = 5.77 ≈ "five point eight bits", peak ≈ 11 | Verified | 5.766; integrand peak 10.98 at 1.97 min |
| "More than a third of all eruptions are short", 36 % | Verified | 97 of 272 under 3 min = 35.7 % |
| D(B‖data) = 0.62; B is the bell-first optimum, 4.27 ± 0.44 | Verified | Nelder–Mead 4.2712 ± 0.4408, 0.6161; BFGS started at A lands on the same point. Other local minimum 2.020 ± 0.237 at 1.519 bits (worse) |
| B "almost never imagines a short eruption, so ignoring them costs it nothing" | Verified | 0.197 % of B's mass is below 3 min; the x < 3 part of D(B‖data) is −0.0005 bits |
| A "imagines eruptions in the gap and out in the tails … that costs 1.7 bits" | Verified | gap 2.5–3.5: 1.226; tails: 0.325 + 0.165; humps: −0.026 + 0.005; peak of the integrand is 1.86 at 2.87 min (matches the 2:10.7 frame) |
| "less than half as wide" | Verified | 0.4408 / 1.1393 = 0.387 |
| B keeps 15 % of the posterior variance, (0.44/1.14)² = 15 % | Verified (numerically) | (0.4408/1.1393)² = 0.1497. The denominator is the blue curve's SD, which equals A's only because of moment matching; on screen it is drawn on A and coloured purple (see fix 1) |
| R's default smoothing makes the best bell-first fit wide, B: 3.55 ± 0.99 | Verified, with a nuance | bw.nrd0 = 0.3348. Global minimum 3.547 ± 0.991 at 0.567 bits, but a narrow local minimum 4.188 ± 0.615 at 0.598 bits survives, only 0.03 bits worse. Descent from A reaches the wide one; **descent from B stops at the narrow one**, and the on-screen morph starts from B (fix 3) |
| "With raw points, D(bell‖data) = ∞ for every bell" | Verified | a bell is not absolutely continuous w.r.t. an empirical measure, so the divergence is infinite |
| KL divergence, Kullback & Leibler, 1951 · *Annals of Mathematical Statistics* | Verified | "On Information and Sufficiency", 22(1):79–86, March 1951 (Project Euclid, JSTOR 2236703) |
| "Every maximum-likelihood fit is the closest model by it"; ML puts the data first | Verified | Bishop 2006 §1.6.1, eq. 1.119 (KL from the empirical distribution) |
| "often called a distance" but asymmetric | Verified | Bishop §1.6.1; Blei et al. 2017 §2.2 |
| ML fits "stretch over every hump", VI "settles on one hump" (Bishop 2006 §10.1 on screen) | Verified, as a tendency | Bishop §10.1.2, Fig. 10.3 |
| VI approximates a posterior with the model first: legend D(model‖posterior) | Verified | Blei et al. 2017, eq. 1: q* = argmin KL(q(z)‖p(z\|x)) |
| Blei and colleagues: VI "generally underestimates posterior variance"; Blei et al., 2017 · JASA | Verified | arXiv 1601.00670: "variational inference generally underestimates the variance of the posterior density"; JASA 112(518):859–877 |

No Wrong, no Fabricated, no uncited empirical claim.

MECHANICS: runtime 3:17.4 · 160 wpm (speech), 153 overall · max internal silence 1.97 s (0:12.2, the planned prediction hold) · lead 0.00 s / trail 1.74 s · max static 3.47 s (0:59.6) · −14.0 LUFS / −1.7 dBTP · WER 0.8 % (the differences are number formatting plus "Blei"→"Bly", which is the correct pronunciation) · 0 banned phrases. No mechanical caps.

Transcript §4 sweep: no banned phrases. No question chains: "Does it?" (0:12) and "Which bell wins now?" (1:55) each stand alone and are followed by a hold. No "it turns out", no "not just X", no fake colon reveal. The ending is a reframing pair, not a recap list. The voice is specific ("the bill comes to", "imagines eruptions", "two doublings, or two bits").

## What works (and why it is close)

The structure meets the bar. The cold-open bet ("this bell should stay put. Does it?", 0:07–0:14) is answered exactly by the yellow A→B arrow at 2:25 and the returned cold-open lines at 3:09. The fail is measured (0.76 vs 1.69 bits, ×2.2). The insight is one picture that becomes the formula: p and q bars pulled out, q doubled twice to reach p, log₂ built from the readouts, a scanner, the p-weighting, and an area that counts up to 0.76. The payoff is now measured (15 %) instead of listed, and the honest limit is genuinely honest. Every number checks out. What keeps it below 9 is a set of referent and continuity slips in the last minute, a prediction prompt that gives away its own answer, and some redundancy.

## FIXES (highest impact first)

1. **[2:38–2:54][Clarity] The payoff's referents are off.** (a) The blue curve is relabelled "posterior" (2:39) while the 272 eruption bars stay at full brightness over an axis that still reads "eruption length (minutes)". A statistically literate viewer sees a posterior of eruption lengths, built from a histogram of data. (b) The 15 % denominator is the bracket drawn on **A** at height 0.21 (2:49), with 1.14 coloured purple (model), while the narration says B keeps 15 % of the *posterior's* variance. Change: on "Bayesian posterior" (2:38) dim the bars to 25 % and the x-axis title to 30 %, and put a grey 18-pt tag "(same curve, as a stand-in)" under "posterior". Draw the wide bracket on the **blue curve** (2.35–4.63 min, at the blue curve's height near 0.3, not on A), colour it blue, and colour "1.14" blue in `(0.44 / 1.14)² = 15%`. Keep the narration as it is.
2. **[1:53–1:59][Hook] "Which bell wins now?" telegraphs its answer.** During the hold B is already filled and solid, A is a dim dashed ghost, and the 18 "simulated draws" fall out of B (1:53–1:57). The viewer is shown the winner before committing. Change: for the swap and the 1.5 s hold, draw A and B both solid at equal opacity with no fill and both letters bright, and drop 9 draws from each bell, or none. Restore A dashed and the B fill on "Take bell B first" (1:59).
3. **[3:01–3:06][Clarity] The honest limit relabels a different bell "B" and animates a false descent.** "B: 3.55 ± 0.99 min" (3:05) reuses the name that means 4.27 ± 0.44 in the landing (3:09 "→ B"). The morph also starts from B, which after 2:18 ("let the bell slide downhill") reads as descent, but descent from B under R's smoothing stops at the narrow local minimum 4.19 ± 0.62 (0.598 bits), not at 3.55 ± 0.99. Change: label the new curve "best bell-first fit: 3.55 ± 0.99 min" (or "B′") and start its morph from dashed A, since descent from A really does land there. Then fade it out before B returns at 3:06.
4. **[2:54–3:06][Clarity] The limit doesn't say which smoothing to trust,** so the viewer leaves unsure whether B was an artefact. Add one clause after "…comes out wide too": "Smoothing chosen by cross-validation keeps the gap empty; R's default doesn't." (facts.md: leave-one-out CV picks a bandwidth of about 0.10, and the bell-first optimum stays on the long hump for bandwidths up to 0.25 and for 2–4-component mixtures). Pay for the time with fix 9.
5. **[1:21–1:28, 1:31–1:47, 2:09–2:17][Clarity] The grey negative stretches of the bill are never named.** A viewer who has just learned "bits = doublings" sees the integrand go below zero under the long hump (1:36.8) and under the humps for A (2:10.7) with no explanation, and may wonder how a divergence can be negative. Add a grey 18-pt tag "refund" with a short leader on the first grey dip at 1:25 (x ≈ 2.7 min, y ≈ −0.35), held 2 s. No narration needed.
6. **[3:06.5–3:08][Motion/Visual] The landing crossfade ghosts text on text.** At 3:07 the dim legend ("maximum likelihood", "D(model‖posterior)") is still visible under the incoming "D(data‖bell) → A / D(bell‖data) → B", about 1 s of illegible double print. Fade the legend out completely (0.3 s) before the cold-open lines come back, or `TransformMatchingTex` the shared D, ‖ and parentheses and replace only the argument words.
7. **[2:38.5–2:39.5][Motion] "data" → "posterior" is a crossfade** of two words in the same box (2:39 frame shows both). Use `TransformMatchingShapes`, or FadeOut 0.25 s then Write 0.5 s.
8. **[1:10.8–1:11.6][Motion] The p and q copies fly through the `q = 0.15` readout** (1:11.0 frame: "q =p 0.15"). Give the `TransformFromCopy` a `path_arc` that clears the readouts, or source p and q from the pulled-out bars (their real referents) and assemble log₂(p/q) in its own row.
9. **[1:44–1:47][Concision] "With the data first, every hump must be covered."** says what 1:31 showed and what the landing says ("Bell A never misses an eruption that happens"). Cut it, and give the 3 s to fix 4.
10. **[2:55–3:06][Visual] Word load.** The dim legend (4 words), "R's default smoothing", "B: 3.55 ± 0.99 min" and the 8-word footnote add up to more than 12 words of prose. The legend plays no part in this beat, so remove it at 2:55 instead of dimming it.
11. **[1:49–1:52][Audio] "Every p trades places with q. The bell supplies the lengths…" runs together.** The transcript merges it at 1:50.9 ("…with Q the bell supplies"). Add `[pause 0.3]` after "q." in narration.txt.
12. **[0:00–0:14][Hook, nitpick] The bet is about an unnamed "measure", and the episode title already answers "Does it?".** Make the bet visibly binary: at 0:11 write "stays?" with a faint ghost of the bell shifted right labelled "moves?", and hold both. If the curriculum allows, use a title that doesn't give the answer away (e.g. "Which Way Is Closer?").

REACHES 9 IF ALL FIXED: yes, narrowly. No structural change is needed: hook, measured fail, one transforming picture, measured payoff, honest limit and reframing landing are all present, and every fact checks out. Fixes 1–4 lift Clarity to 9 and Hook to 9. Fixes 5–8 and 10 lift Visual and Motion to 9. Fix 9 plus 4 lift Concision to 9. That gives about 8.9–9.1, so Audio also needs to hold at 8.5 or better, with deictics and pauses as now plus fix 11.

KEEP:
- The "doublings = bits" pull-out at 1:04–1:16: the q bar stacked twice to p's dashed line, then log₂(p/q) = 1.98. This is the canonical way to make the log ratio concrete.
- The swap at 1:48–2:27: the weight p becomes q, the same bill panel is re-scored for B (0.62) and A (1.69, gap and tails boxed), then the bell slides downhill from A to B and the yellow arrow answers the cold open.
- The landing at 3:06–3:16: the answered cold-open lines plus "Bell A never misses an eruption that happens. Bell B almost never imagines one that doesn't."
