# Round 6 review: substance (science and story editor)

Evidence: `review/` pack (metrics.json 00:18, newer than final.mp4 00:16), report.md, all 12 contact sheets, 14 full-resolution keyframes (0:03.1, 0:21.2, 0:34.4, 0:55.8, 1:11.6, 1:28.9, 1:43.4, 2:06.8, 2:22.1, 2:32.7, 2:56.4, 3:06.1, 3:18.8, 3:21.6, 3:29.4), plus extra frames I pulled at 1:55.0 and 2:23.0. I read script.md, narration.txt, facts.md and transcript.txt. I recomputed every number from `faithful.csv` with my own EM fit, KL integrals, Nelder–Mead and KDE, and did not rely on data.py. I re-read the Giordano et al. JMLR PDF and the Blei et al. arXiv text myself.

```
EPISODE: 008 — "The Distance That Isn't Symmetric"
IDEA: KL divergence only charges where its first argument puts mass, so with the data first the best single bell must cover both humps of Old Faithful (A), and with the bell first it may drop a hump but must never put mass where the data has none (B).
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6 (855/100 = 8.55)   AFTER CEILING: 8.6 (ceiling 8.5 + 2 = 10.5, no effect)
CAPS: none
FINAL: 8.6   PASS: no
```

## FACTS

All values are my own recomputation unless a source is named.

| Claim | Verdict | Source / my check |
|---|---|---|
| 272 Old Faithful eruptions, R `faithful`, Härdle 1991 (0:01–0:17 on screen) | Verified | csv has 272 rows; R dataset documentation credits Härdle (1991) |
| Smoothed curve = 2-normal ML mixture | Verified | my EM: w = 0.348/0.652, μ = 2.019/4.273, σ = 0.236/0.437; its moments are 3.4878 ± 1.1393, exactly the sample moments |
| A = data-first optimum, 3.49 ± 1.14 min (0:43) | Verified | ML normal = moments; D(p‖N) is convex in (μ, log σ) |
| D(data‖A) = 0.76 bits (0:35, 1:33) | Verified | 0.7619 |
| Shift by −0.8 gives 1.12, stretch ×1.8 gives 1.11 ("only grows", 0:37) | Verified | 1.1176, 1.1112 |
| D(A‖data) = 1.69 ("1.7"), ×2.2, "more than twice" (0:49–0:53) | Verified | 1.6948; ratio 2.224 |
| At 2 min: p = 0.59, q = 0.15, "about a quarter", log₂(p/q) = 1.98 (1:02–1:15) | Verified | 0.5881, 0.1493, q/p = 0.254, 1.978 |
| Clipped tags ↓−45, ↓−6.2, ↓−20; sweep readout −31.98 at 0.3 min (1:19–1:21) | Verified | −45.43 at 0; −6.18 at 2.84; −20.45 at 7; −31.98 at 0.30 |
| Negative ("refund") part is small (1:29) | Verified | −0.175 of 0.762 bits |
| B = bell-first optimum 4.27 ± 0.44 min (1:39, 1:53) | Verified | Nelder–Mead 4.2712 ± 0.4408, D = 0.6161 |
| q_B(2) = 1.6×10⁻⁶, "18 and a half doublings", 18.52 (1:39–1:43) | Verified | 1.56×10⁻⁶, 18.524 |
| "More than a third of all eruptions are short", 36 % (1:45) | Verified | 97/272 = 35.7 % below 3 min |
| D(data‖B) = 5.77 ("5.8"), peak ≈ 11 (1:47–1:49) | Verified | 5.766; integrand peaks at 10.98 near 1.97 min |
| D(B‖data) = 0.62 (2:11) | Verified | 0.616 |
| "Bell B almost never imagines a short eruption" | Verified | 0.20 % of B's mass is below 3 min |
| "Bell A imagines eruptions in the gap and the tails" | Verified | 31.1 % of A's mass is in 2.5–3.5 min, where the data has 4.4 % |
| Descent from A on the bell-first bill ends at B; "less than half as wide" (2:23–2:32) | Verified | descent from A lands at B; 0.4408/1.1393 = 0.387 |
| Option 2 is a real but worse local minimum (cold-open bet) | Verified | 2.020 ± 0.237 at 1.519 bits, vs B's 0.616 |
| Kullback & Leibler 1951, *Annals of Mathematical Statistics* (0:19 on screen) | Verified | 22(1):79–86 (Encyclopedia of Mathematics; Project Euclid) |
| ML puts the data first; VI puts the model first and tends to sit on one mode; Bishop 2006 §10.1 (2:36–2:51) | Verified | Bishop eq. 1.119 and §10.1.2 / Fig. 10.3; Blei et al. eq. 1 |
| "Blei and colleagues note that VI generally underestimates posterior variance"; Blei et al., 2017 · JASA (2:52) | Verified | arXiv 1601.00670 §1: "variational inference generally underestimates the variance of the posterior density"; JASA 112(518):859–877 |
| Real ad-conversion model: mean 0.110 for MCMC and VI, SD 0.020 vs 0.004, "a fifth" (3:01–3:08) | Verified | JMLR 19 (2018) PDF, §5.3 "Criteo Dataset"; Table 2 row β3: 0.110 / 0.110; Table 3 row β3: 0.020 / 0.020 / 0.004 (MCMC / LRVB / uncorrected MFVB); "The uncorrected MFVB variance estimates of β are particularly inaccurate" |
| Against raw points, every bell-first score is infinite (3:09–3:15) | Verified | a bell is not absolutely continuous with respect to a 272-atom measure, so KL = ∞ |
| Heavier (R default, bw.nrd0 = 0.335) smoothing: gap partly fills; best fit 3.55 ± 0.99, "almost back to A" (3:16–3:21) | Verified | my bw = 0.3348; gap mass 9.8 % (vs 3.2 %); fit from A 3.547 ± 0.991 (0.567 bits, global), from B 4.188 ± 0.615 (0.598, local) |
| Silverman 1986 as the source of R's default bandwidth (3:17 on screen) | Verified | R `bw.nrd0` documentation cites Silverman (1986, p. 48, eq. 3.31) |

There are no wrong or fabricated claims, and every empirical claim has an on-screen citation.

## MECHANICS

```
MECHANICS: runtime 3:30.6 · wpm 159 (speech) · max silence 2.09 s · max static 3.43 s · −14.0 LUFS / −1.9 dBTP
```

Leading silence is 0.00 s and trailing silence 0.90 s. WER is 1.6 %, there are 0 banned phrases, and the layout audit found 0 issues. None of these trigger a cap.

The transcript changes are benign. "Kullback Leibler" came out as "callback lie blur" (close to the correct sound), "Blei" as "Bly" (the correct pronunciation), and "Bell B." picked up an inserted period at 3:26. The longest stretch without a breath is 14.2 s, in the stakes beat starting at 0:17.

## Transcript and slop pass

- **Banned phrases:** none. "To see why" (0:58) is the one allowed signpost.
- **Banned patterns:** no rhetorical-question chain (0:11 and 2:01 are single questions), no "not just X", no fake reveal, no superlatives.
- **Ending:** the closing pair at 3:22–3:29 reframes the bet. It does not restate a list.
- **Voice:** the writing is specific and visual. "Double q twice and you reach p" and "The bell supplies the lengths, and the data judges them" are strong lines.

## Score rationale (evidence)

**Hook 8.5.** The first frame is concrete: real data and `D(data‖bell)`. The three-way spatial bet is good, and the ending answers it on the same image (2:33–2:37, arrow from 1 to 3; 3:25–3:29, the 1 and 3 return).

The deductions:
- The commit question runs 0:11.3–0:15.2, so the viewer commits at about 0:15, not by 0:12.
- The title already tells the viewer that option 1 is wrong, so the real bet is only 2 versus 3.
- "Data first" (0:02) is order language the viewer cannot yet interpret. Its meaning, that the first argument is the weight, only arrives at 1:21.

**Clarity 8.5.** The episode works from the concrete to the abstract: one length, then doublings, then the weighted integral, then the swap. Every number checks out. The deductions:
- (a) **The payoff mixes two mechanisms.** The toy illustration (2:53–2:59) shows variance lost by dropping a whole hump: ±0.44 against ±1.14, with different centres. The real case (3:01–3:08) has the *same* mean and a narrower spread. That is mean-field squeezing of a single-mode posterior, not mode dropping. The narration runs them together ("settle on one hump … underestimates posterior variance … a fifth as wide"), so a viewer will assume the ad-model posterior had a hump that VI dropped. It is not false, but it is a misleading implication that a science editor would not let through.
- (b) **The honest limit is left unresolved.** "Smooth it more heavily … the best fit spreads almost back to A" (3:16–3:21) is followed directly by a landing that reasserts B on the original curve. The viewer is never told why the original smoothing is the one to believe, which reopens the bet's answer. The verified fact that resolves it is in facts.md: likelihood cross-validation picks h ≈ 0.10, and the fit stays at 4.28 ± 0.39. It was cut for word budget.
- (c) **"Data first" stays opaque until 1:21** (see Hook).

**Visual 8.5.** The palette is semantic and held for the whole episode: blue is the data, purple the bell, red the bits, yellow the focus. The labels are next to their referents, and the two-bill stack (2:07–2:37) is a frame worth teaching from. The deductions:
- At 3:01–3:09 the "real ad-conversion model" brackets (β₃, a regression coefficient) float over the eruption-length chart, and their dashed mean line sits at about x = 4.75 *minutes* (keyframe 3:06.1). The B bell and the chart stay at full strength, so the frame has two focal points in two incompatible unit systems.
- The three-panel frames (2:07–2:37) are dense: 6 formula or number blocks on the right plus 3 panels. They are legible, but at the limit.

**Motion 8.5.** Objects persist and transform throughout: the argument swap arc (0:05, 1:55), the doubling stack (1:09–1:11), the p swinging into the weight, the live totals, and the precomputed descent with both bills moving in opposite directions (2:23–2:32). The deduction: the stakes beat (0:17–0:33) is 16 s of labels fading onto an unchanged chart (sheet 2, every frame). "Shrinks it" is said twice there, and nothing on screen shrinks.

**Audio 8.5.** The pace is 159 wpm, the loudness is on target and the deictics land ("this one" 0:04, "this high" 1:02). The deduction: in the stakes beat, four claim sentences arrive with 0.3 s gaps (silences at 0:18.9, 0:21.0, 0:25.0, 0:29.2, all 0.3 s), giving a 14.2 s breathless run. It is the most hurried stretch of the episode, and it is where the two big framing claims are made.

**Concision 8.5.** At 500 words there is little fat. The one slack beat: the stakes line "Every maximum-likelihood fit … data first. Much of Bayesian machine learning … order flipped" (0:21–0:29) and the payoff "Maximum likelihood puts the data first … Variational inference … model first" (2:36–2:51) say the same pairing twice. The payoff version is the one that earns its place, because the viewer can then see why.

**Originality 9.** Two "bills" for one bell, with one draining while the other swells, is an image I have not seen in any KL explainer. So is the 18.5-doubling penalty on real Old Faithful data. It is memorable and shareable.

## FIXES (highest impact first)

1. **[2:52–3:08][Clarity] The payoff implies the ad-model VI dropped a hump.** The real case is same-mean squeezing.
   - **Narration:** change "Blei and colleagues note that variational inference generally underestimates posterior variance." to "Blei and colleagues note it generally underestimates posterior variance, even with one hump." (+2 words; "it" = VI, the subject of the previous sentence.)
   - **Screen:** when the real-model panel lands, draw MCMC and VI as two concentric one-hump bells (blue wide, purple narrow, same centre) above the brackets. This moves Clarity from 8.5 to 9.
2. **[3:16–3:22][Clarity] The honest limit leaves the bet's answer unresolved.**
   - **Narration:** change "Smooth it more heavily and the gap partly fills." to "Smooth it more than the data supports and the gap partly fills." (+4 words). Verified: LOO likelihood CV picks h = 0.103 (log-lik −270.8 vs −302.1 at R's default).
   - **Tag:** change "heavier smoothing" to "over-smoothed".
   - **Citation:** add "(cross-validation prefers less)" to the Silverman line, or swap in a two-word tag "CV: worse".
3. **[0:17–0:33][Motion] Make "shrinks it" visible.** The beat is currently 16 s of labels fading on.
   - On "Every maximum-likelihood fit shrinks it with the data first", start the bell at a visibly wrong spot (e.g. μ = 2.7, σ = 0.7). Slide and widen it into A while a live `= x.xx bits` next to `D(data‖bell)` counts down to 0.76. This is the same live number the naive build reuses at 0:35, so move its first appearance here.
   - On "order flipped", only flag `D(bell‖data)` and show no number. This moves Motion from 8.5 to 9.
4. **[0:17–0:31][Audio] Give the stakes beat room to breathe.** Change [pause 0.2] to [pause 0.5] after "Leibler" and after "data first", and [pause 0.2] to [pause 0.6] after "order flipped". This removes the 14.2 s breathless run. It costs about 1 s, which fix 6 pays back.
5. **[3:01–3:09][Visual] The real-model brackets sit on the eruption-length chart.** When "real ad-conversion model" lands, dim the bars, the curve, B and the "if this were a posterior" tag to 25 %. Put the brackets in their own boxed inset top right with its own axis label "effect β₃ (log-odds)" and at most 3 ticks, so the mean line no longer reads as about 4.75 min. This moves Visual from 8.5 to 9.
6. **[2:36–2:43][Concision] The ML/VI pairing is stated twice** (stakes and payoff). Shorten the payoff ML line from "Maximum likelihood puts the data first, so a one-bell fit stretches over every hump." to "Maximum likelihood puts the data first, so its bell covers every hump." (−3 words). This pays for fixes 1 and 2 with the budget at about 503 words. Also cut "Now" from "Now keep that bill." (−1).
7. **[0:00–0:15][Hook] Move the commit point to 0:12 or earlier.** Rewrite the cold open as: "Old Faithful's eruptions. Data first, this bell fits best. Swap the order: if closeness is a distance, it stays at one. Or does it move to two, or three?"
   - This keeps the wrong belief and brings the question in at about 0:09.
   - Hold the yellow 1/2/3 numbers and the ghosts 1.5 s after "three".
8. **[0:02][Clarity] "Data first" is undefined at first use.** On "Data first", besides the yellow flash on the blue "data" slot, write a 2-word grey tag under it, "the weight", held to 0:14. It pays off at 1:21, when p becomes the weight (morph the tag into that p).

## REACHES 9 IF ALL FIXED

Yes. With fixes 1–2 Clarity reaches 9, with fix 3 Motion reaches 9, with fix 4 Audio reaches 9, with fix 5 Visual reaches 9, with fix 6 Concision reaches 9, and with fixes 7–8 Hook reaches 9. Originality stays at 9. That gives (135 + 225 + 135 + 135 + 90 + 90 + 90)/100 = 9.0.

None of the fixes is structural. The hook, failure beat, visual insight, payoff and landing are all in place. The episode is held below 9 by two specific clarity gaps in the payoff and the honest limit, plus one under-animated stakes beat.

## KEEP

- The two-bill picture with the live descent from A to B (2:23–2:32), where one total drains while the other swells. This is the episode's signature image.
- The doubling ladder: "Double q twice and you reach p", followed by 18.5 doublings for B at 2 minutes (1:09–1:43). It is concrete, measured and re-derivable.
- The cold-open bet of 1/2/3 on real data, answered on the same image (2:33–2:37) and re-seen in the landing pair (3:22–3:29).
