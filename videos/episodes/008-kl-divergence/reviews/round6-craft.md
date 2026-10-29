# Round 6 — craft critic (visual design, motion, A/V sync; all dimensions scored)

Evidence: review/ pack (metrics.json 00:18 is newer than final.mp4 00:16, so it was reused), report.md,
all 12 contact sheets, keyframes kf_01, kf_03, kf_09, kf_15, kf_17, kf_20, kf_24, kf_28, kf_33, kf_37,
kf_39 at full resolution, plus my own frames from final.mp4 at 0:00.3, 1:46.5, 1:48.8, 2:37.8, 2:38.6
and 4 fps strips across the swap (0:05–0:07), the shift/stretch (0:36–0:40) and the teardown
(2:36.5–2:39). Transcript, transcript_words.tsv, narration.txt, script.md and facts.md were read.
I recomputed the KL numbers from faithful.csv and the EM mixture, and checked Giordano et al. Table 3
against the JMLR PDF.

```
EPISODE: 008 — "The Distance That Isn't Symmetric"
IDEA: KL divergence only charges where its first argument puts mass, so swapping the order moves the closest one-bell fit to Old Faithful from the wide bell A (covers both humps) to the narrow bell B (sits on one hump).
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 9 · Audio 8.5 · Concision 8.5 · Originality 9
WEIGHTED: 8.6 (127.5 + 212.5 + 127.5 + 135 + 85 + 85 + 90 = 862.5)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none (0 banned phrases; loudness −14.0 LUFS / −1.9 dBTP; max silence 2.09 s; max static 3.43 s; layout audit 0 issues; every empirical claim has an on-screen citation)
FINAL: 8.6   PASS: no
FACTS:
- 272 eruptions, mean 3.488, SD 1.139 min; 97/272 = 35.7 % under 3 min ("more than a third", "36%") | Verified | faithful.csv recomputed
- D(data‖A) = 0.76 bits; D(A‖data) = 1.69 bits; ratio 2.2 | Verified | my recompute: 0.761 / 1.691 from the rounded EM parameters
- shift −0.8 min → 1.12 bits; stretch ×1.8 → 1.11 bits | Verified | recompute 1.117 / 1.110
- at 2.0 min p = 0.59, q_A = 0.15, log₂(p/q) = 1.98 ("about two") | Verified | recompute 0.586 / 0.149 / 1.97
- q_B(2.0) = 1.6×10⁻⁶, log₂(p/q) = 18.52 ("eighteen and a half doublings") | Verified | recompute 1.56e-6 / 18.52
- D(data‖B) = 5.77 ("five point eight"); D(B‖data) = 0.62 | Verified | recompute 5.76 / 0.615
- B = 4.27 ± 0.44, "less than half as wide" as A (0.387) | Verified | facts.md, data.json
- Descent from A on D(bell‖data) ends at B; option 2 is a real but worse local minimum | Verified (by facts.md, data.json path; consistent with my B value) | facts.md
- KL divergence: Kullback & Leibler 1951, Ann. Math. Stat. | Verified | standard
- ML ⇔ data-first KL (Bishop 2006 eq. 1.119); VI minimises KL(q‖posterior) (Blei et al. 2017 eq. 1); mode covering vs seeking (Bishop §10.1.2, Fig. 10.3) | Verified | Bishop 2006; Blei et al. 2017
- "VI generally underestimates posterior variance" | Verified (quote in Blei et al. 2017 §1) | Blei, Kucukelbir & McAuliffe 2017, JASA
- Real ad-conversion model: β₃ mean 0.110 / 0.110, SD 0.020 (MCMC) vs 0.004 (uncorrected MFVB), "a fifth as wide" | Verified | Giordano, Broderick & Jordan 2018, JMLR 19(51), Table 3 row "β3 0.020 0.020 0.004" re-read today; Table 2 means as stated in facts.md
- Raw points: D(bell‖empirical) = ∞ for every bell | Verified | absolute-continuity definition of KL
- R default bandwidth (Silverman rule) → best bell-first fit 3.55 ± 0.99 | Verified (facts.md / data.py; consistent with stated bw.nrd0 = 0.335) | Silverman 1986; R bw.nrd0 docs
MECHANICS: runtime 3:30.6 · wpm 159 (speech time; median sentence 172) · max silence 2.09 s (planned prediction hold, 2:03.0) · max static 3.43 s (2:43.2) · −14.0 LUFS / −1.9 dBTP
FIXES (highest impact first):
1. [1:39.0–1:48.8][Clarity + Visual] The data-first bill for B is clipped flat at 2.5 bits/min from ≈1:39 (frame f_100.0, kf_17 at 1:43.4, f_106.5) but "peak ≈ 11" only appears at ≈1:48.8 (f_108.8). For about 9.5 s, while the narrator says "falls short by eighteen and a half doublings", the viewer sees a flat-topped mountain that looks like a true value of 2.5, and nothing on screen explains why 18.5 doublings becomes a 5.8-bit bill. → Start the live "peak ≈" tag (and its arrow) on the frame where the integrand first crosses the panel top, so it counts up with the slide to B. Add a two-stroke zig-zag break mark at the plateau's left shoulder so the clip reads as a clip. Flash 18.52 and the peak tag together on "doublings" (0.59 × 18.5 ≈ 11 is then readable).
2. [1:53–2:37][Visual] The three-panel stretch is the episode's central picture, and its two bills are the smallest things on screen. Each bill panel is ≈0.9 units tall, and the bell-first bill for B is a ≈0.5-unit bump (kf_20 at 2:06.8, kf_24 at 2:32.7). The shared x-axis title "eruption length (minutes)" sits on the tick-label baseline to the right of the "6", where it reads like an extra tick label and sits ≈0.35 units under "= ∫ q log₂(q/p) dx" (sheet 7, 2:03–2:05). → Shrink the top chart from 2.85 to ≈2.3 units and give each bill ≈1.2 units. Set the bills' y-range to [−0.5, 2.0] so the 0.62 bump is ≈0.4 of the panel. Put the axis title under the lowest axis, right-aligned to the 6 tick, as in every other beat. Once the integrals collapse to D-lines at 2:21 the right column has room for that.
3. [0:00–0:15][Hook] The bet finishes at 0:15.2 ("…or to three?"). The 9 anchor wants the commit by 0:12, and the first two sentences use "Data first" and "closest" before the viewer knows what D measures. → Cut to: "Old Faithful's eruptions. Data first, this bell is closest. Swap the order. If closeness is a distance, it stays at one. Or does it move to two, or to three? [pause 1.5]". That saves ≈2.5 s, so the question lands at ≈0:12 with the ghosts 2 and 3 drawing on their words. Keep the yellow flash on the "data" slot at "Data first".
4. [0:17.1–0:31.3][Audio + Clarity] The stakes are one 14.2 s run with no breath of 0.35 s or more (report: longest stretch without a breath, 0:17.1). It packs "KL divergence", "Kullback and Leibler", "maximum-likelihood fit" and "Bayesian machine learning" into 12 s, and the only visual for the last is a grey tag. → Add [pause 0.5] after "Leibler" and [pause 0.6] after "with the data first". On "flipped", fly a copy of the grey "variational inference" tag's D-line through the swap arc used at 0:05, so the flipped order is shown and not just tagged.
5. [2:36.1–2:51.1][Concision] "Maximum likelihood puts the data first, so a one-bell fit stretches over every hump" re-says the stakes line at 0:21 and the answer just given at 2:33 ("the closest bell moves to three"). → Shorten to "Maximum likelihood is the data-first fit: bell A." (A's fill sweep stays on "A"), then go straight to the VI sentence. That saves ≈3 s and gives the payoff one new claim per sentence.
6. [3:00.5–3:09.6][Visual] The real ad-conversion brackets float above the toy chart while B's fill and the blue curve stay at full strength (kf_33 at 3:06.1), so there are two focal points. The MCMC/VI mean line at x ≈ 4.75 on the eruption axis invites the misreading that 0.110 is in minutes. → On "real", dim bars, curve, B and its fill to 30 %. Put a thin grey baseline with the label "effect β₃" under the two brackets, so the panel visibly has its own scale. Return the chart to full strength on "Against raw points".
7. [2:55.6–2:56.8][Audio] "generally" is stretched to ≈1.2 s, and whisper sets it off with commas ("variational inference, generally, underestimates"), which gives it an odd emphasis on a hedge word. → Drop "generally" (the on-screen claim is already scoped by the citation) or move it: "…note that variational inference tends to underestimate posterior variance."
8. [1:19.0–1:21.5][Motion] The scanner sweeps the whole axis in ≈2 s while the dimmed readouts flicker through −31.98 and −14.28 (sheet 5). Too fast to read, too visible to ignore. → Either hide the three numeric readouts during the sweep (fade to 0, not 30 %) or stretch the sweep to 3 s with linear rate (time-like) over the existing 0.9 s pause.
9. [2:06.8][Visual, nitpick] The bell-first bill's curve is fully drawn while its total still reads "0.00 bits", and that panel has no unit of its own. → Start the counter with the fill sweep (it already does at 2:09). Show "0.00" only once the fill begins, or write the curve and the fill in one move.
REACHES 9 IF ALL FIXED: yes, narrowly. Fixes 1–2 lift Visual and Clarity to 9 (the two remaining legibility faults in the core picture). Fix 3 lifts Hook to 9, fixes 4 and 7 lift Audio, fix 5 lifts Concision. Expected weighted ≈ 9.0–9.1. Nothing structural is missing: the misconception, measured failure (×2.2), doubling-to-bits derivation, two-bill picture and real cited payoff are all in place.
KEEP:
- The doubling picture (1:01–1:17): p and q pulled out on a shared baseline, q stacked ×2 ×2 up to p's dashed line, then log₂(p/q) = 1.98. The cleanest derivation of "bits" I have seen in this series.
- The descent 2:23–2:33: one bell slides while both live bills trade (1.69 → 0.62 and 0.76 → 5.77, peak tag counting 3 → 11). Then the cold-open ghosts return and the 1 → 3 arrow lands B exactly in ghost 3. The animation is the argument.
- Strict colour semantics: blue data / p / MCMC, purple bell / q / VI, red bits, yellow focus, grey refunds. The landing D-lines with yellow underlines under the first slot.
```

## Notes by dimension (evidence)

**Hook 8.5.** First frame (0:00.3) is the real histogram and `D(` writing; the bell is on screen by 0:04 on
"this one"; the swap arc at 0:05–0:07 visibly carries each argument to its new slot (4 fps strip); ghosts 2/3 and the
yellow 1 make a spatial three-way bet; the answer at 2:33–2:37 is drawn on the same image and the landing (3:23–3:29)
re-sees it with `→ A` / `→ B`. Held back from 9 by the late commit (0:15.2) and the abstract "Data first" before D is
explained.

**Clarity 8.5.** The structure is the BAR template: naive (0.76; shift and stretch both raise it, live) → fail (1.69, ×2.2,
"a distance" struck through at 0:53) → insight (one length, then weight by p, then integrate; refund tag) → bell that skips
a hump → second bill → descent → payoff → honest limit. All numbers check. Deductions: the unexplained clip (fix 1)
right where the biggest number arrives, and the jargon-dense stakes with no picture for "Bayesian machine learning" (fix 4).

**Visual 8.5.** Palette discipline is excellent and consistent from 0:00 to 3:30; dimming is used (25–40 %) rather than
deletion (readouts at 1:25, legend row 1 at 2:49, posterior tag at 3:01). Type is at or above the floors on the keyframes
checked. Deductions: the cramped three-panel stretch (fix 2, ≈44 s of the episode) and the double focal point in the
real-model panel (fix 6).

**Motion 9.** Objects persist from start to end (one chart, one bell, one curve); transforms carry meaning (argument
swap, bar pull-out, ×2 stacks, the p swinging into the weight, the descent with both bills live, smoothing morph and back).
Static stretches peak at 3.4 s; no hard cuts seen on the sheets. Only the 2 s scanner sweep (fix 8) is too fast.

**Audio 8.5.** On-target loudness, 159 wpm, WER 1.6 % (the "callback lie blur" / "Bly" mishearings match the intended
pronunciations of Kullback-Leibler and Blei). Deictics land: "this one" (0:04, bell draws), "this high" (1:03, bar grows),
"grey dips" (1:29–1:31, refund tag). Deductions: the 14 s breathless stakes run and the stretched hedge "generally".

**Concision 8.5.** 500 words, 3:30. One restated beat in the payoff (fix 5); the rest earns its time.

**Originality 9.** Real Old Faithful data instead of the textbook two-Gaussian toy, "doublings" as the unit of a bit, two
bills kept side by side for the same bell, and a measured VI-vs-MCMC spread as the payoff. This is a memorable way to teach
KL asymmetry.
