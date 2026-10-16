EPISODE: 009 — "Why Bell Curves Are Everywhere, and When They're Not"
REVIEWER: science/story editor, round 1 (independent; did not read round1-craft.md)
IDEA: More data never makes lopsided data bell-shaped; averaging does, because an average's skewness is one piece's skewness over root n, and only while no single piece can outweigh the rest (finite variance).

SCORES: Hook 8 · Clarity 8 · Visual 8 · Motion 8 · Audio 8 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.1   AFTER CEILING: 8.1 (lowest 8 + 2 = 10, not binding)
CAPS: none. Considered and rejected: (a) "355 · 5.2² ≈ 9,700" @ 2:05–2:10. Arithmetic gives 9,599, but 9.7k is the paper's own table value (from the unrounded skewness) and "≈" is within 1%, so it is a fix, not cap 6. (b) Tags crossing "skew = 1.98" @ 0:43.0. They overlap only while moving, for under 0.5 s, so this is a motion fix, not cap 7.
FINAL: 8.1   PASS: no

---

## 1. Script read cold

One sentence: see IDEA. It is coherent and the beats follow §6: cold open 0:00, stakes 0:12, naive "collect more" 0:21, measured fail 0:29, fix by averaging 0:40, insight formula 1:02, universality 1:14, payoff (Kohavi/Bing) 1:30, limit (lighthouse) 2:07, landing back on the cold-open frame 2:52.

## 2. Fact-check (every number recomputed; `sim.py` re-run; Kohavi PDF read)

FACTS:
- Exponential waits have skewness 2; sample skewness 1.90 / 1.96 / 2.01 / 1.98 at 10²–10⁵ (0:33–0:40) | Verified | sim.py re-run: 1.900 / 1.958 / 2.005 / 1.978; exact = 2
- Example group 5.2, 1.8, 25.7, 5.3 → average 9.5 (0:43–0:45) | Verified | 38.0 / 4 = 9.5
- Averages of 4/16/64 have skew 0.99 / 0.50 / 0.25 (0:47–0:57) | Verified | sim.py: 0.989 / 0.501 / 0.252; exact 2/√n = 1, 0.5, 0.25
- "Averages crowd toward ten minutes", panels zoom (0:57–1:02) | Verified | SD = 10/√n = 5, 2.5, 1.25 (sim 4.99, 2.52, 1.26)
- skew(x̄) = skew(x)/√n (1:06–1:14) | Verified (re-derived) | third cumulant of a sum = nκ₃, variance nσ², so skew = nκ₃/(nσ²)^{3/2} = γ/√n; needs a finite third moment (not stated, harmless here)
- Coin with p = 0.1: skew 2.67; mean of 64 flips skew 0.33 (1:17–1:26) | Verified | (1−2p)/√(p(1−p)) = 0.8/0.3 = 2.667; /8 = 0.333
- CLT needs independent pieces plus finite variance (1:26, 2:40) | Verified | Lindeberg–Lévy (i.i.d., finite variance). "No single piece can outweigh the rest" is a fair gloss of Lindeberg/Feller negligibility
- "A classic textbook says thirty pieces are enough, whatever the shape" (1:30) | Verified with a caveat | Kohavi et al. 2014 quote Montgomery (5th ed., Wiley 2010): "In many cases of practical interest, if n ≥ 30, the normal approximation will be satisfactory regardless of the shape of the distribution." The narration drops the hedge "in many cases of practical interest" (fix 8). The book's authors are Montgomery & Runger, as on screen
- 2/√30 = 0.37 (1:39) | Verified | 0.365
- "Kohavi's team at Microsoft demands 355 × skewness squared" (1:43) | Verified | Kohavi, Deng (Microsoft), Longbotham (SW Jiaotong), Xu (LinkedIn), "Seven Rules of Thumb for Web Site Experimenters", KDD 2014, Rule #7: "355 × s² for each variant … when |skewness| > 1", derived from Boos & Hughes-Oliver 2000. "Kohavi's team at Microsoft" is loose (two of the four authors were elsewhere), but the Bing data is Microsoft's and the on-screen citation is correct
- "Our formula asking for a skewness under point oh five" (1:49) | Verified (our algebra) | n ≥ 355s² ⇔ s/√n ≤ 1/√355 = 0.0531
- "For these waits, fourteen hundred" (1:53) | Verified | 355 × 4 = 1,420
- Bing revenue/user skewness near 18 → 114,000 users (1:55–2:01) | Verified | corrected table: 17.9 → 114k (355 × 17.9² = 113,746); text: 18.2; erratum Jan 2015
- "Capping each user at ten dollars a week cut that below ten thousand" (2:02–2:07) | Verified | "capped Revenue/User to $10 per user per week … skewness drop from 18 to 5.3"; table: 5.2 → 9.7k
- On screen "355 · 5.2² ≈ 9,700" (2:05–2:10) | Imprecise | 355 × 5.2² = 9,599. Paper's 9.7k reflects an unrounded skewness. Fix 6
- Lighthouse one mile off a straight shore with uniform angles gives a Cauchy landing spot; Gull 1988; Sivia & Skilling 2006 (2:07–2:17) | Verified | Gull, "Bayesian Inductive Inference and Maximum Entropy", in Erickson & Smith (eds.), Maximum Entropy and Bayesian Methods, 1988, pp. 53–74 (bayes.wustl.edu/sfg); Sivia & Skilling 2006
- Farthest of 1,000 flashes "typically about nine hundred miles" (2:25) | Verified | median of max = tan(π/2 · 0.5^{1/1000}) = 919 mi; this run 902 mi
- "Divided by a thousand, it still drags the average about a mile" (2:31) | Verified | 0.90 mi; the running mean jumps from −0.25 to +0.82
- "The average of a thousand is as scattered as a single flash" (2:36) | Verified | the mean of i.i.d. standard Cauchy draws is standard Cauchy; MC 0.501 vs 0.500 within 1 mile
- "Here the variance is infinite" (2:45) | Verified (standard phrasing) | E[X²] = ∞; strictly, the Cauchy has no mean either
- "The median … homes in" (2:49) | Verified | asymptotic SD π/(2√1000) = 0.050 mi; this run −0.079
- Every empirical claim has an on-screen citation: Montgomery/Kohavi 1:33–1:43, Kohavi 1:43–2:07, Gull/Sivia 2:09–2:17; simulated data tagged "simulated" or "exact" | Verified

No fabricated or misattributed sources. No factual errors that trigger a cap.

## 3. Mechanics

MECHANICS: runtime 3:02.1 · wpm 155 (speech time; 454 words) · max silence 1.97 s (0:10.5 prediction pause) · max static 2.87 s · −14.0 LUFS / −1.9 dBTP · leading silence 0.00 s / trailing 1.88 s · 0 black frames · WER 3.9%. No mechanical caps triggered.

## 4. Transcript

- §4 phrases: 0. Patterns: no "it's not X, it's Y"; no rhetorical-question chain (0:08 and 1:35 are single questions, each followed by a hold); no fake-reveal colons; no recap ending. "The bell was never in the data. It's in the average." is a negate-then-reveal construction close to the banned family. It earns its place as the callback, but it is the only line in the script that reads as a slogan.
- Script vs heard: "waits"→"weights" (×5) is a homophone, not an error. "Kohavi's"→"Cohave's" @ 1:42.9: narration_text.py already forces /kOhˈɑvi/, so this is probably ASR, but someone should listen once. "away away" @ 2:23.7 is a Whisper chunk-boundary duplicate: the word timings overlap (143.70–144.04 and 143.94–144.14), not a TTS stutter. "ten dollars a week cut that" was heard as "$10, a weak cut that" @ 2:04, a real garden-path sentence (fix 5).
- Hook: concrete histogram at frame 1; the question lands 0:08.7–0:10.3, followed by a 2.0 s hold. Commitment comes by 0:12 and the hook is in by 0:15.

## 5. Contact sheets (flipbook)

- 0:00–0:20: histogram persists. The arrow, dashed bell and "?" are drawn on "bell curve". The A/B error-bar glyph (yellow means, green bells) is consistent with the palette.
- 0:21–0:40: the counter ticks 100 → 100,000, the bars morph, the exact curve traces on "shape" (0:27–0:29), and the skewness bars rise to about 2. Sync is good.
- 0:41–1:03: the big histogram shrinks into panel 1, the averaging demo runs, and panels fill in order with readings. The readings arrive about 1 s after they are spoken (0:49 → 0:51), which is within tolerance. The bottom 45% of the frame is empty throughout (0:43–1:03).
- 1:03–1:30: ×4 and ÷2 arcs, then 2/√n fractions assembled from the readings, then the general formula. Coin morph on panel 1 and panel 4, other panels dimmed (25–40%, correct). This is the best stretch of the episode.
- 1:31–2:07: formula moves up, "textbook: n ≥ 30", the 2/√30 = ? hold (1:37.8–1:39.8), and the 355·s² ⇔ ≤ 0.053 line with log-axis markers. It is equation-dense but each item is placed next to its referent.
- 2:07–2:52: lighthouse geometry, beams, running mean with the red 902 mi flash, "middle half" brackets, variance < ∞ → = ∞ (red), purple median.
- 2:53–3:02: fade back to the cold-open frame with the 100,000-wait histogram; the dashed bell dims and the yellow average-of-64 histogram grows under a solid green bell. The landing re-sees the first frame.

## 6. Keyframes at full resolution (read: 0:02.6, 0:04.4, 0:06.5, 0:21.5, 0:31.9, 0:43.0, 0:43.6, 0:43.9–0:44.9 strip, 0:45.2, 1:14.9, 1:28.0, 1:29.0, 1:41.0, 2:01.9, 2:07.0, 2:18.5, 2:46.5, 2:52.1, 3:01.0)

- Safe area, type size and contrast are fine everywhere I checked. The upper-chart label "landing spot (miles)" is not clipped; the review sheets' timestamp badge only covers it there. Palette: blue single, yellow average, green bell, red extreme, purple median, used consistently for the whole episode.
- 0:43.0: the 5.2 and 1.8 tags fly across "skew = 1.98", with ghosted digits.
- 0:43.6–0:44.9: the four values are fully readable for about 0.5 s and "9.5" for about 0.4 s (44.5–44.9) before it shrinks into the dot. That is far below the §5 reading time of ≥ 1.5 s.
- 0:57 and 3:01: the panel windows run from mean −2 SD to +4 SD (for example 7.5–15 for n = 64), so each yellow bell and its green curve are cut off on the left at about 18% of peak height while the right tail is drawn out. The "nearly perfect bell" at the landing looks truncated and right-leaning partly because of the window, not the data.
- 1:19–1:30: the shared axis label switches to "share of heads in n flips" while dimmed panels 2–3 still show bus-wait histograms with 0–20 minute ticks. Under n = 64 the coin's reading 0.33 sits next to the dimmed "2/√64 = 0.25", and "2.67/√64" is never written.
- 0:04.4–0:06.0, pixel probe: the "this tail" emphasis is a ×1.6 stretch of 1%-high bars, so no visible change reaches the viewer on the deictic.

## 7. Score rationale

- Hook 8: the first frame is concrete, a prediction pause follows, and the ending re-sees the first frame exactly. But the cold-open question ("will 100,000 waits look like a bell?") is one a stat-literate viewer answers correctly, and the fail beat (0:29–0:40) confirms what they expected: four bars at about 2. The genuinely surprising claim, "textbook says 30, Bing needed 114,000", is not seeded until 1:30, so tension is flat for the first 40 s.
- Clarity 8: concrete before abstract, assumptions stated, every number checks, sources correct. Three gaps keep it from 9:
  - (i) The video calls skew 0.25 "nearly this perfect bell" (0:55), then implies skew 0.37 at n = 30 is inadequate and Kohavi wants ≤ 0.053 (1:39–1:53), without saying why. The reason, significance lives in the tails, is missing, so a careful viewer is left with a contradiction.
  - (ii) The mechanism, one long wait diluted by three short ones, is shown in about 1.3 s and never said.
  - (iii) The 1/√n law is pattern-matched from four readings, so the viewer can repeat the rule but not say why it is √n.
  Smaller issues: 10 numbers in 27 s (1:39–2:07), a garden-path sentence at 2:04, and an overstated textbook paraphrase.
- Visual 8: semantic palette, persistent objects, correct dimming. Minor issues: the truncated bell windows, 45% empty frame at 0:43–1:03, the coin-beat axis label mismatch, and the doubled "textbook 30" (1:33–1:55).
- Motion 8: meaningful transforms throughout. The fractions are built from the readings, the histogram shrinks into panel 1, the coin morphs, and the landing callback works. The one bad move is the averaging merge (0:43–0:45), which is too fast to read and crosses the skew label.
- Audio 8: 155 wpm, on-target loudness, prediction pauses are intentional, and deictics land except "this tail" (0:05). One sentence has bad prosody (2:04).
- Concision 8.5: 454 words with no preamble, recap or tangent. The only slack is on screen ("textbook: n ≥ 30" and "textbook 30" shown together).
- Originality 8.5: reading Kohavi's 355·s² rule as "skewness of the mean ≤ 0.053", then placing 30 / 1,420 / 9,700 / 114,000 on one log axis, is a non-obvious and shareable angle, and the lighthouse is a rare, well-chosen counterexample. Bus waits as the source distribution are standard.

Weighted = (15·8 + 25·8 + 15·8 + 15·8 + 10·8 + 10·8.5 + 10·8.5)/100 = 8.1.

## 8. Fixes (highest impact first)

FIXES (highest impact first):
1. [1:39–1:55][Clarity] Unexplained contradiction: 0.25 is "nearly perfect" at 0:55, yet 0.37 fails at 1:41. Turn it into a measured failure. After "Two over root thirty: point three seven." say: "Tests live in the tails. At thirty waits, a ninety-five percent interval's two-and-a-half-percent tails are really one point four and three point four percent." I recomputed these with Gamma(30) and a known-σ z interval: lower tail 1.40%, upper 3.40%. On screen, shade the two tails of an n = 30 yellow histogram against the green bell, with live DecimalNumbers 1.4% and 3.4%. Then: "Kohavi's team at Microsoft wants each tail between two and three percent. That takes three hundred fifty-five times the skewness squared…" At 1,420 waits the tails are 2.35% and 2.64%; show them when the 1,420 marker lands. This closes the logic gap and adds an SMH-style measured fail. It is worth about +1 on Clarity and Hook.
2. [0:12–0:21][Hook] Plant the real stake in the first 20 s. Replace "It's tempting to say yes: with enough data, things look normal. And error bars and A-B tests lean on a bell curve somewhere." with "It's tempting to say yes: with enough data, things look normal. Textbooks say thirty is usually enough, and every A-B test leans on it." Put a gray "n ≥ 30?" under the A/B glyph. The 1:30 beat then pays off a commitment the viewer made at 0:15, and tension carries through the 0:29–1:30 build.
3. [0:41–0:47][Motion/Clarity] The averaging demo is unreadable: tags readable for 0.5 s, "9.5" for 0.4 s, crossing "skew = 1.98" at 0:43.0. Route the four tags along y = −1.6, below the skew label, and hold them 1.5 s. Pulse the 25.7 tag, then build "(5.2 + 1.8 + 25.7 + 5.3) / 4 = 9.5" with TransformFromCopy from the tags and hold it 1.5 s before the dot drops. Change the narration to: "Average four waits: the one long wait gets diluted by three short ones. Drop that one number here." This adds about 2.5 s.
4. [1:06–1:14][Clarity] Say why it is √n. After "two over root n", add one sentence and a two-term picture: "Add n waits and their lean adds up n times, but their spread cubed grows like n to the one and a half." On screen: "lean ×n", "spread³ ×n^{3/2}" → "÷√n", built from the ×4 arcs (×4 vs ×8 → ÷2). Then the viewer can re-derive the rule instead of just repeating it.
5. [2:02–2:07][Audio/Clarity] Garden-path sentence ("…ten dollars a week cut that…" was heard as "a weak cut"). Replace it with: "Capping each user's revenue at ten dollars a week dropped the skewness to five, and the users needed to under ten thousand." Hold 0.4 s before "and".
6. [2:05–2:10][Correctness/Visual] "n ≥ 355 · 5.2² ≈ 9,700" computes to 9,599. Change it to "≈ 9,600" (and the marker label to 9,600), or write "355 · 5.23²" if the paper's unrounded value is wanted. The narration "below ten thousand" is fine either way.
7. [0:57–1:30, 2:55–3:02][Visual] Panel windows from mean −2 SD to +4 SD cut the left side of every yellow bell and its green curve (about 18% of peak at the left edge in the 3:01 frame). Use mean −3.5 SD to +4 SD (n = 64: 5.6–15; n = 16: 1.25–20; n = 4: 0–30, clamped at 0), so the "nearly perfect bell" is drawn whole and any lean the viewer sees is real.
8. [1:30–1:33][Correctness] Restore the hedge in the textbook paraphrase: "A classic textbook says thirty is usually enough, whatever the shape." Montgomery's wording is "in many cases of practical interest".
9. [1:17–1:30][Visual/Clarity] In the coin beat, write the formula with the coin's own numbers. TransformFromCopy "2.67" into a fraction under n = 64, "2.67/√64 = 0.33", replacing the dimmed "2/√64 = 0.25". Fade panels 2–3 fully, or restore their "average of n waits" label, so "share of heads in n flips" doesn't sit under bus-wait axes.
10. [0:41–1:03][Visual] The bottom 45% of the frame is empty while four small histograms crowd the top (panel height about 2 units). Increase panel height by about 40% and move the readings row down to y ≈ −1.2. The yellow-vs-green fit at 0:57 is the episode's key picture and should be big.
11. [0:04.5–0:06][Visual/Audio sync] "this tail" has no visible referent: a ×1.6 stretch of 1%-high bars is imperceptible, and a pixel probe at 4.4–6.0 s shows no change. Draw a gray brace under 20–45 min, labelled "tail", on the word, and dim bars 0–20 to 40% for 1 s.
12. [2:36–2:42][Clarity] The "middle half:" brackets are theory, not this run, and the narration never says "half". Say: "Half of single flashes land within a mile of the lighthouse, and so do half of all thousand-flash averages." Tag the brackets "exact".
13. [1:33–1:55][Visual] Drop the duplicated gray "textbook: n ≥ 30" (left) once the "textbook 30" marker exists on the log axis. One referent, one label.

REACHES 9 IF ALL FIXED: yes, if fixes 1–4 land. The skeleton is right: misconception, measured non-change, formula read off the readings, real sourced payoff, honest limit, callback. What is missing is explanatory. Fix 1 turns the payoff into a measured failure (1.4% / 3.4% tails at n = 30 vs 2.5%), fix 2 gives the opening a stake viewers will get wrong, and fixes 3–4 let a viewer re-derive why averaging works. That moves Hook and Clarity to 9. Fixes 5–13 clean Visual and Motion to 9. No structural rewrite is needed.

KEEP:
- The ×4 / ÷2 panel row with 2/√n fractions assembled from the measured readings into skew(x̄) = skew(x)/√n (1:02–1:16). This is the "formula emerges from the picture" moment.
- The Kohavi reinterpretation: 355·s² ⇔ skew(x̄) ≤ 0.053 on one log axis with 30 / 1,420 / 9,700 / 114,000 (1:43–2:07).
- The lighthouse running mean with the 902-mile flash dragging it about a mile, the median homing in, and the landing that rebuilds the cold-open frame with the bell moved into the average (2:17–3:02).
