# Episode 8: round 1 review (substance / science-editor pass)

Evidence: the existing pack `review/` (metrics.json 13:10 is newer than final.mp4 13:08). I read report.md, all 11 contact sheets, and keyframes kf_01, 06, 08, 14, 17, 19, 22, 25, 33, 36, 39 and 40. I also pulled extra frames at 0:31.5–0:35.0 (shift/stretch), 1:08.9 (zoom on ×2/q labels), 1:17, 2:25, 2:30 (zoom on the "A" label), 2:35, 2:35.6, 3:01 and 0:19.6. I measured the yellow streak at 2:34.8–2:35.9 pixel by pixel. Every number was recomputed from `faithful.csv` with my own script (own EM fit, own KL integrals, own Nelder–Mead/BFGS and KDE runs). I did not use data.py.

```
EPISODE: 008 — "The Distance That Isn't Symmetric"
IDEA: KL divergence only charges where its first argument puts mass, so with the data first a one-bell fit must cover both humps (A), and with the bell first it can drop a hump but must never put mass where the data has none (B).
SCORES: Hook 7 · Clarity 7 · Visual 7 · Motion 8 · Audio 8 · Concision 8 · Originality 8
WEIGHTED: 7.5   AFTER CEILING: 7.5
CAPS: factual error on screen → 6: the payoff legend reads "D(model ‖ data)  variational inference · B" (2:33–3:00). VI minimises KL(q ‖ posterior), not a divergence to the data, and a model-first divergence to an empirical data distribution is not a standard procedure (it is infinite without the smoothing this episode had to add) |
      text overlapping another element → 7: lower "×2" and the "q" label sit on top of the purple bell and the blue curve, with knock-out boxes cut into the lines (1:07–1:26, zoom at 1:08.9). The italic "A" touches bell B's flank at the three-curve crossing (1:27–3:12, zoom at 2:30). During the 2:24.5–2:26 transition "bits per minute" collides with tick "1" ("bits per mi1nute") and the x-label slides over the lower panel
FINAL: 6.0   PASS: no
```

## FACTS

| Claim | Status | Source / my recomputation |
|---|---|---|
| 272 Old Faithful eruptions, timed in minutes (R `faithful`, Härdle 1991) | Verified | csv has 272 rows, range 1.6–5.1 min; R datasets docs: Source W. Härdle; Härdle 1991, *Smoothing Techniques*, Springer |
| Bell A = closest bell with the data first = ML normal, 3.49 ± 1.14 min ("three and a half … give or take 1.1") | Verified | sample mean 3.4878, SD(1/n) 1.1393. The 2-component EM mixture keeps the moments exactly (3.4878 / 1.1393), so moment-matching is the minimiser |
| D(data‖A) = 0.76 bits | Verified | 0.7619 |
| Shifting or stretching A only raises the number | Verified | convex in (μ, log σ) with minimum at the moments. On screen it peaks at 0.93 (shift) and 0.95 (stretch) at 0:32.2 and 0:33.6 |
| D(A‖data) = 1.69 bits, "1.7 … more than twice as far", ×2.2 | Verified | 1.6948; ratio 2.224 |
| At 2.0 min, p = 0.59 and q = 0.15, "about a quarter", log₂(p/q) = 1.98 ≈ 2 | Verified | p = 0.5881, q = 0.1493, p/q = 3.94, log₂ = 1.978 |
| Bell B = closest bell with the bell first, 4.27 ± 0.44; descent from A ends at B | Verified | Nelder–Mead 4.2712 ± 0.4408, D = 0.6161; BFGS started at A lands on the same point. Other local minimum (short hump 2.02 ± 0.24, D = 1.519) is worse |
| "less than half as wide" | Verified | 0.4408 / 1.1393 = 0.387 |
| At 2 min under B, log₂(p/q) = 18.52 ("eighteen and a half doublings") | Verified | q_B = 1.56×10⁻⁶, log₂ = 18.52. The **on-screen readout "q = 0.00"** (1:31–1:47) next to log₂(p/q) = 18.52 reads like division by zero (see fix 6) |
| D(data‖B) = 5.77 ≈ 5.8 bits; integrand peak ≈ 11 bits/min | Verified | 5.766; peak 10.98 at 1.97 min |
| "More than a third of all eruptions are short", 36 % | Verified | 97 / 272 = 35.7 % under 3 min |
| D(B‖data) = 0.62; B "almost never imagines a short eruption" | Verified | 0.616; B puts 0.197 % of its mass below 3 min |
| A "imagines eruptions in the gap and the tails" | Verified | A puts 31.1 % of its mass in 2.5–3.5 min (data: 12–14 of 272, depending on bounds) |
| Heavier smoothing (bandwidth 0.36) → bell-first fit wide, 3.53 ± 1.02 | Verified, but **framed too softly** | 3.529 ± 1.017. R's *default* bandwidth (bw.nrd0 = 0.335) already makes the wide minimum the global one (0.566 vs 0.598 bits), so "heavily enough" undersells how fragile the headline is |
| "Every maximum-likelihood fit is the closest model by [KL]" | Verified | Bishop 2006 §1.6.1 eq. 1.119 (KL from the empirical distribution) |
| "often called a distance" yet asymmetric | Verified | Bishop §1.6.1; Blei et al. 2017 §2.2 |
| KL from Kullback & Leibler, 1951, *Annals of Mathematical Statistics* | Verified | Project Euclid / JSTOR: "On Information and Sufficiency", 22(1):79–86, March 1951 |
| Bishop's textbook "draws this same picture" | Verified (loosely) | PRML Fig. 10.3: one Gaussian fit to a two-Gaussian mixture, KL(p‖q) spans both modes and KL(q‖p) locks onto one. It is drawn as 2-D contours, so "same idea" is more accurate than "same picture" |
| Blei et al. 2017: VI "generally underestimates posterior variance"; VI is a fast way to approximate posteriors | Verified | arXiv 1601.00670 / JASA 112(518):859–877: "variational inference generally underestimates the variance of the posterior density; this is a consequence of its objective function" |
| Legend: "D(model ‖ data) — variational inference" | **Wrong** (on screen) | VI's second argument is the exact posterior p(z\|x), not the data. The narration is careful here; the legend is not |
| Legend: "D(data ‖ model) — maximum likelihood" | Verified | (same as Bishop eq. 1.119) |

MECHANICS: runtime 3:12.8 · 158 wpm (speech) · max silence 1.96 s (0:10.4, a planned prediction hold; 1:54.5, a planned hold) · max static 3.43 s · −14.1 LUFS / −1.9 dBTP · lead 0.00 s / trail 1.75 s · WER 1.5 % (the dropped "maximum" at 2:27.4 is a transcription miss: there is speech in 2:26.8–2:27.4) · 0 banned phrases. No mechanical caps.

Transcript §4 sweep: no banned phrases. No question chains: each question ("Where does the closest bell go?", "Which bell wins now?") stands alone and is followed by a hold. No "it turns out", no fake colon reveals, no recap ending. The voice is distinctive ("the bill comes to", "imagines eruptions", "two doublings, or two bits"). Cadence: almost every sentence gap is the same 0.4–0.5 s (see the silence list), which makes it sound metronomic.

## FIXES (highest impact first)

1. **[2:33–3:00][Clarity, cap 6] The VI legend is factually wrong.** Change row 2 of the legend from `D(model ‖ data) · variational inference · B` to `D(model ‖ posterior) · variational inference`. Before it appears (2:31, on "Variational inference"), animate the blue curve's tag from "data" to "posterior" with `TransformMatchingTex`, so the analogy is explicit: in VI the blue curve *is* a posterior. Rewrite the line as "Variational inference approximates a Bayesian posterior with the model first, so it settles on one hump." Keep row 1 as `D(data ‖ model) · maximum likelihood`. Removes cap 6.
2. **[1:05–1:26][Visual, cap 7] Labels sit on the curves.** Move the lower "×2" to x = 2.55 min, level with the middle of its stacked bar (clear of both curves by ≥ 0.15 units). Put the upper "×2" at the same x. Move "q" to the left of its bar at (1.7 min, 0.08), or under the axis at the dot. Remove the dark knock-out backgrounds. Check with a zoom at 1:08.9.
3. **[1:27–3:12][Visual/Clarity, cap 7] The "A" label touches bell B and is ambiguous.** Both bells are the same purple, and the italic A sits at the crossing where A, B and the data curve meet (2:30 zoom), so in the landing (3:05, A flagged yellow) a viewer can read "A" as B's tail. Anchor "A" on A's own left shoulder at (1.2 min, 0.06 + 0.15 units), well away from B, and draw A dashed whenever B is also on screen (from 1:27 on), so the two bells differ in shape and not only by a letter. Also move "A: 3.49 ± 1.14 min" (2:31–2:51), which currently floats beside B at x≈5–6, next to A's peak at (3.5 min, 0.45).
4. **[2:24.5–2:26][Visual, cap 7] Transition collision.** In the FULL-layout move, fade out `bot_title2` ("bits per minute") and the lower axes *before* the top axes grow (two sequential plays, 0.4 s + 1.2 s), so "bits per mi1nute" and the sliding x-label never overlap.
5. **[0:00–0:12][Hook] The viewer cannot really commit to a prediction.** At 0:06, "measure closeness the other way round" and the `D(bell‖data)` notation arrive before KL has been defined, so "Where does the closest bell go?" is a puzzle with no handle. Make the likely-wrong belief explicit and binary: "Closeness should work both ways, so if you flip the measure, the closest bell stays right here. Does it?" Hold 1.5 s on the bell with a yellow "stays?" tag. That is the misconception the episode breaks at 0:44 and 2:22, and the viewer has now voted on it.
6. **[1:29–1:47][Clarity] "q = 0.00" next to "log₂ p/q = 18.52"** reads like division by zero. Show `q = 1.6×10⁻⁶` (switch DecimalNumber to scientific notation below 0.005), or show `q ≈ p / 2^{18.5}`.
7. **[2:51–3:00][Clarity] "The jump" is never defined, the wide fit has no label, and the caveat is too soft.** Say: "Bell B only exists because that gap is nearly empty. Smooth the data with R's default setting and the gap fills enough that the bell-first fit comes out wide too." Label the new wide bell "B: 3.53 ± 1.02 min" (at 2:58), and dim A to 30 % so the viewer can tell the two purple curves apart (at 2:59 they are indistinguishable). Also add the one fact that explains why the curve is smoothed at all: with raw points, any bell put first pays infinitely, because the data has zero density between the points. Add it as a 5-word tag on "curve: smoothed" at 0:03 or as a clause here.
8. **[2:41–2:51][Clarity/Originality] The payoff names the consequence but never measures it.** Turn "underestimates posterior variance" into a number on screen: B's variance is 0.44² = 0.19 against the target's 1.14² = 1.30, so B captures 15 % of the spread. Animate the ±1 SD bracket of B shrinking against A's bracket, with a live "15 % of the variance" readout, on "underestimates".
9. **[2:34.8–2:35.9][Motion] Flash on "approximate" spends most of its time on the baseline.** `ShowPassingFlash` on bell B's outline crawls along the flat x-axis from 0 to 3 min and from 5.5 to 7 min, so viewers see a yellow streak on the axis at the far left (measured 2:34.8–2:35.3) and right (2:35.6). Flash only B's x ∈ [3, 5.6] segment, or use `Indicate(lab_B)` together with the bell_fill bump.
10. **[1:15–1:19][Visual] Clipping hides the true values.** The log₂(p/q) curve clips to a flat grey line at −1 across the gap and tails, which suggests a value of −1 where the true value is about −20 (the readout shows −20.45 at 1:17). End the clipped stretches with a small down-arrow "→ −∞" marker at the panel floor, or fade the clipped segments to 30 %.
11. **[0:19–0:39][Visual] The "maximum-likelihood fit" label floats about 250 px above its referent,** about 18 px from the 1.9-min bar and the long-hump curve top. Place it under bell A's peak, inside the gap at (3.0 min, 0.42) and right-aligned to the dashed mean line, or attach it to A with a short leader.
12. **[whole episode][Audio] Metronomic 0.45–0.5 s gaps after almost every sentence.** Vary them: about 0.25 s inside a thought (e.g. 0:31→0:35, 1:12→1:14), 0.8–1.0 s at beat turns (0:55, 1:45, 2:24). The planned 2 s holds already work.
13. **[0:31.5–0:34.5][Motion] The shift/stretch excursions are fast** (out and back in about 1.4 s each, peaks at 0.93/0.95 visible for under 0.5 s). Give each one 2 s and hold the peak readout for 0.5 s, so "only grows" is something the viewer sees.

REACHES 9 IF ALL FIXED: yes, narrowly. The structure is already at the bar: a measured failure (0.76 vs 1.69 bits), one picture that turns into the formula (stacked q bars to log₂, a scanner, the p-weighted bill), a prediction hold, a descent that answers the cold open, an honest limit, and a reframing last line. Fixes 1–4 remove the caps, which brings it to about 7.5. Reaching 9 depends on fix 5 (a real commit-to-a-wrong-answer hook), fix 7 (an honest limit that is both legible and frank) and fix 8 (a payoff that is measured, not listed). Without those three, expect about 8.

KEEP:
- The "doublings = bits" move at 1:06–1:14 (the q bar stacked twice to reach p, then log₂ built from the two readouts). This is the canonical way to make log₂(p/q) concrete.
- The swap at 1:45–2:15: the weight changes from p to q, the bell "supplies the lengths and the data judges them", then the same bill panel is redrawn for B and for A with the gap and tails boxed.
- The closing pair "Bell A never misses an eruption that happens. Bell B almost never imagines one that doesn't." over the two answered cold-open lines.
