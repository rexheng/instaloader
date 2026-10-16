# Episode 6 — changelog

## Round 1 revisions

Round 1: craft 7.9, substance 8.1 (both FAIL, no caps, no factual errors). Both critics said the
structure can reach 9; the gap was the rising-sequence picture, two asserted bridges (accuracy
formula, 230 / n-scaling), clutter in the one-chart section, and a rushed landing.

### Plan of the climb (BAR §3 "9" anchors vs where the episode fell short)
- **Hook 8.5 → 9** ("viewer commits to a likely-wrong prediction by 0:12; ending resolves the
  opening exactly"): the viewer was never made to pick a number, and the stakes line was generic
  (and wrong about simulations riffling). → Explicit commit: "fifty, seventy five, or a hundred
  percent of the time?" with the "?" hopping across the three ticks and a 1.5 s hold. New stakes:
  card rooms, and any simulation that mixes by random steps ("stopped early, it still remembers
  where it started"), with the sorted deck's profile drawn over the shuffled deck. Second
  prediction at the chart: "How many more riffles to bring it below a half?" + 1.5 s hold on the
  d = ½ line. Landing payoff now held, not crossfaded.
- **Clarity 7.5/8 → 9** ("viewer could re-derive it after one watch"): rising sequences were
  never defined visually and the 14 vs 26 traces were a tangle; the theorem, the accuracy formula,
  230 and the n-scaling were announced. → (1) Riffle 1 shows the two sequences with labels
  "1, 2, 3, …, 26" / "27, 28, …, 52" and a dot reading sequence 1 left to right ("runs of
  consecutive cards, read left to right"). (2) New **level view**: every bar's height becomes its
  sequence's index, so each rising sequence is one horizontal level and the deck's height IS the
  count; each riffle visibly splits every level in two (2 → 4 → 8 → 14) under a rising dashed
  ceiling ≤ 2², 2³, 2⁴. The perfect deck in the same view is visibly almost twice as tall (26).
  (3) Theorem shown: "chance 3.5 × 10⁻⁶⁰" stays fixed while the deck rearranges into a different
  14-sequence deck ("same chance"), then each deck collapses into one block of its histogram bar.
  (4) Accuracy derived at k = 6 from areas: "say riffled / say perfect" zones, P = 0.78 and
  U = 0.17 fly out of the shaded areas into ½(0.78) + ½(1 − 0.17) → ½ + ½(0.78 − 0.17) → ½ + ½d.
  (5) 230 built from the data: a "× 2^k: 198 → 221 → 227 → 229 → 230" row from the gap values;
  then 230 → 52·53/12 and 2.1 → √(53/12), 52 → n, with "∼ n²" / "∼ √n" tags, and the −1.8 tagged
  "(gap = spread rule)". (6) "between the centers" (means), and the spread line now says
  purple's spread settles to blue's (1.08 → 2.08).
- **Visual 7.5 → 9** ("every frame has one focal point; all §5 standards met"): → no separate d
  readout (the value rides on the moving dot); accuracy formula dims after use and leaves; gap
  bracket's legs stand on the two histograms; gap row removed when the equation forms; chart
  raised so the x-axis title and citations sit on different rows; meter ghost "top card 52.4 %"
  moved under the track so it never stacks with the live value; meter end labels kept (40 %)
  whenever the meter is shown; text grey lightened to #A3AAB4 (7.7:1; GRAY kept for axes);
  "(each step ≈ ÷2)" instead of exact "÷2"; "one simulated deck (GSR model)" tags.
- **Motion 8 → 9** ("every motion encodes a relation"): → level splits, deck → histogram block
  collapse, area → number TransformFromCopy, value-on-dot, landing riffles at ≈ 1.1 s each with
  marks kept (marks are redrawn from the bars every frame), landed meter held, scene fully faded
  before the end card. Transitional duplicates removed (copies are frozen glyph subsets: "gap",
  "230", "2.1"; equation moved with .animate before being re-mapped; meter fades before the
  citation fades in).
- **Audio 8/8.5 → 9**: deictics re-cued (each option on its tick, "split" on the split, "same
  count" on the chance labels, "seventy eight"/"seventeen" on their areas).
- **Concision 8 → 9**: cut "Start again from order", "So everything fits in one chart",
  "in the standard model", the long top-card/Markov phrasings; every new sentence carries a
  visible step.
- **Originality 8.5 → 9**: the level view (a deck whose height is its number of rising sequences,
  growing by doubling) is new, plus the meter-based landing kept.

### Fact changes
- Attribution: "Aldous, then Bayer and Diaconis, proved it"; citations Aldous 1983 · Séminaire de
  Probabilités XVII and Bayer & Diaconis 1992 · Ann. Appl. Probab. (facts #21).
- New verified numbers: 3.5 × 10⁻⁶⁰ = 1431/2^208, 1/52! = 1.2 × 10⁻⁶⁸, P(A) = 0.7824,
  U(A) = 0.1688 at k = 6, gap × 2^k products, E[R] closed form (facts #11, #13, #18, #20).

### Fix-by-fix (craft C1–C11, substance S1–S14)
- C1/S1 rising sequences: labelled sequences + reading dot at riffle 1; level view with visible
  2 → 4 → 8 → 14 splits under the ≤ 2^k ceiling (4, 8, 16); 14 vs 26 readable as deck height.
- C2 theorem: fixed "chance 3.5 × 10⁻⁶⁰" while the deck rearranges into another 14-sequence deck,
  "same chance", then both decks collapse into their histogram blocks (no cut).
- C3 clutter: no separate d readout (value rides on the dot), accuracy formula dims then leaves,
  gap bracket legs on the histograms, rows dim once the equation takes their numbers, fixed
  "k riffles" legend, zones as tints rather than brackets.
- C4/S3 n-scaling: × 2^k row from the data → 230 → 52·53/12, 2.1 → √(53/12), 52 → n with ∼n²/∼√n,
  k ≈ (3/2)log₂n − 1.8 tagged "(gap = spread rule)".
- C5/S7 landing: riffles 8–10 ≈ 1.1 s each with marks; needle lands before "takes ten"; ghost
  flashes on "ten"; scene fades fully, then the end card (trailing silence 1.9 s).
- C6 ghost "top card 52.4 %" under the track. C7/S9 citation and axis title on separate rows.
- C8/S13 transitional duplicates removed. C9 end labels kept at 40 %. C10/S4 stakes rewritten
  with commit + hold. C11 "between the centers".
- S2 accuracy derived from areas at k = 6. S5 trace-plot trap named over the top-card vs
  whole-deck curves. S6 Aldous attribution + heuristic tag. S8 prediction pause on the d = ½
  line. S10 halving shown as approximate: a grey "(each step ≈ ÷2)" note at the end of the gap row (per-arrow marks crowded the arrows). S11 "one simulated deck (GSR model)". S12 text grey #A3AAB4. S14 purple's
  spread settles to blue's.
- Also found and fixed in review: the k = 5 gap is 6.89 (not 6.90) to 2 decimals; product row
  uses the displayed values (≈ 198, 220, 227, 229); live gap label matches the row; dashed
  ceilings sit half a level above the allowed maximum; cold-open options rephrased as "Pick …"
  so the transcript is one question, not a question chain; "Aldous" pronunciation override.
- Layout audit (toolkit b70c54d, added mid-revision): the first master with the audit showed 35
  findings (1 overlap, 34 clearance < 0.15), almost all from the meter's stacked label rows. The
  meter moved up to y = −2.05 so its rows are track / 50 %, 75 %, 100 % / "top card 52.4 %" with
  ≥ 0.15 between them; the top-card chart, the side-by-side decks and the landing deck moved up
  to clear the live value label; the needle label sits 0.18 above the needle; payoff value labels
  sit 0.22 from their dots and fade before the Trefethen band appears; the cold-open deck moved up
  so the "?" clears "bottom". Target: 0 findings in the final render.

### Final mechanics (review/report.md)
Runtime 3:51.7 · 156 wpm (speech) · −14.0 LUFS / −1.9 dBTP · lead 0.00 s / trail 1.89 s · max
silence 1.99 s (planned prediction hold) · max static 3.10 s · WER 2.3 % · 0 banned phrases or
patterns · 0 render warnings · layout audit 0 issues in 256 checks · 0 review flags.

## Round 2 revisions

Round 2: craft 8.4, substance 8.4 (both FAIL, no caps, no factual errors; one imprecise line).
Both critics: reaches 9 if fixed. The gap was execution at the climax (crossfaded algebra held
~1 s, a mechanism sentence narrated over a picture that contradicts it, the cliff location derived
twice), an undersized level view whose doubling was only asserted, a single-deck cold open, and a
blurred deck-to-histogram collapse.

### Plan of the climb (BAR §3 "9" anchors vs where the episode fell short)
- **Hook 8.5 → 9** ("commits by 0:12; tension rises; ending resolves the opening exactly"): the
  cold open showed one deck under two tags, and the stakes were a generic, unsourced "card rooms".
  → Two decks from the first frame (both sorted): the left one riffles four times under its purple
  tag, the right one is shuffled perfectly under its blue tag. They are the same two decks that
  return side by side in level view at 1:19 (14 vs 26 levels), so the reveal answers the
  cold-open picture. Stakes now lead with the payoff's real consequence (MCMC): "Any simulation
  that mixes by random steps faces this question: stopped too early, it still remembers where it
  started." (−3 s).
- **Clarity 8.5 → 9** ("viewer could re-derive it after one watch"): the doubling was asserted;
  "several spreads" was said over a k = 7 frame; the cliff location was derived twice; slide values
  belonged to non-integer k. → (1) "The cut crosses each level once, so a riffle can at most split
  it in two": cut line drawn through the 2-level deck, rings where it crosses each level, the
  right packet tinted, riffle, and the four new levels alternate tinted/untinted (exact for this
  deck: L1-left, L1-right, L2-left, L2-right). (2) Mechanism shown by rewinding the chart: the
  histogram slides back to 4 riffles and spread-sized hops are laid along the gap ("5.9 spreads",
  d = 1), then forward to 7 ("0.85 spreads", d = 0.33) while the red dot falls down the cliff.
  (3) One derivation chain in place, no re-layout: gap ≈ 230/2^k = 2.1 → 2^k ≈ 230/2.1 ≈ 110 →
  k ≈ 6.8, then the same equation becomes (52·53/12)/√(53/12) and 52 → n, 53 → n+1, and k ≈ 6.8
  becomes k ≈ (3/2)log₂n − 1.8. (4) Gap and d labels hidden during slides, written only at whole
  riffle counts. (5) "Only the old top card stands out", with only card 1's excess red.
- **Visual 8 → 9** ("one focal point; all §5 standards met"): level view tiny at 1:07; k = 6 frame
  with 13 text groups; detached "k riffles" legend. → Level unit 0.55 → 0.5 → 0.32 → 0.2 as levels
  grow (deck ≈ 1.2–3.4 units tall instead of 0.4–1.0); gap row, gap bracket and "perfect" label
  leave during the accuracy derivation; "k riffles" rides above the purple histogram; inset d-plot
  lowered so the equation column has room; y-title stays "distance d" throughout.
- **Motion 8 / 8.5 → 9** ("every motion encodes a relation; reading time respected"): equation
  steps crossfaded and held ~1 s; the collapse smeared while the axes drew. → Axes drawn first
  (during a 0.5 s pause), then each deck's 52 bars squeeze, in order, into one square on x = 14 and
  x = 26 ("1 deck"), then the bars grow. Equation copies fly on arcs from dimmed sources (gap from
  the gap bracket, 230 from the row, 2.1 from the spread label); the rearrangement is staged (fade
  gap/=, 2^k arcs over, 2.1 arcs under, then ≈ 110); 52 and 53 glyphs transform alone into n and
  n+1. eq holds ≈ 3.3 s, k ≈ 6.8 stays at full opacity until it becomes the general formula.
  Riffle 3 now 1.4 s + 0.8 s split. Histogram fades before the deck moves at 0:48.
- **Audio 8.5 → 9**: "read left to right" (heard as "red") → "reading left to right"; "trace plot"
  (never shown) → "one statistic can settle, like the top card". Cues re-timed to the new lines.
- **Concision 8 / 8.5 → 9**: stakes −3 s; "Many Markov chains show the same cliff" folded into one
  sentence with the trap; the chart-clearing second derivation removed.
- **Originality 9**: kept (level view, meter through-line); the rewind-with-spread-hops picture is
  new.

### Fact changes
- "Only the old top card still turns up too often" (round-2 substance critic: literally false,
  23 of 52 cards sit above 1/52) → "Only the old top card stands out: one time in fifteen", and only
  card 1's excess is drawn red. Recomputed: the other 22 exceed 1/52 by ≤ 0.06 points; card 1
  carries 96.2 % of the excess (facts #9).
- Stakes no longer mention card rooms (unsourced); the MCMC line is the payoff's consequence
  (facts #0). "Trace plot" (never shown) → "one statistic" (facts #24).
- New on-screen numbers verified: "5.9 spreads" = 12.401/2.1016, "0.85 spreads" = 1.790/2.1016,
  `(52·53/12)/√(53/12) ≈ 110` (109.28), riffle-2 levels = (level, packet) pieces exactly
  (cards 1–10, 11–26, 27–37, 38–52) (facts #4, #17, #19).

### Fix-by-fix (craft C1–C11, substance S1–S10)
- C1/S5/S4 equation chain: eq1 builds during a 1.2 s pause right after "→ 230" (rows and the
  spread label dim to 30 % first; "gap" flies from the gap bracket and "2.1" from the spread label
  on arcs that bow away from the d-plot) and holds 3.2 s; the rearrangement is staged ("gap" and
  "=" fade, then 2^k arcs over and 2.1 arcs under, then "≈ 110" on "a hundred and ten"); "⇒ k ≈
  6.8" stays at full opacity ~11 s until it becomes the general formula. No title morph: the d-plot
  y-title stays "distance d" throughout (C10).
- S1 merged derivation: no chart-clearing crossfade. The same equation becomes
  (52·53/12)/√(53/12) ≈ 110 (held 3.0 s) and then only the 52s and 53s crossfade into n and n+1
  (/12, the bar and the root just move); "∼ n²" / "∼ √n" on their words; k ≈ 6.8 →
  k ≈ (3/2)log₂n − 1.8. The histogram dims to 30 % instead of leaving. "Both numbers come from the
  deck's size" kept as the bridge.
- C2 mechanism: on "several spreads" the chart rewinds to 4 riffles and blue spread-long hops are
  laid along the gap ("5.9 spreads", red dot back at d = 1, dots 1–3 appear at 1); on "about one
  spread" it slides forward to 7 riffles, the hops disappear one by one, the last one cut where the
  gap ends ("0.85 spreads"), and the red dot falls to 0.33; dots 6–7 flash and dot 8 appears on
  "halves too"; the cliff is drawn through the dots on "That's the cliff".
- C3/S3 level view: level unit 0.55 → 0.5 → 0.32 → 0.2 (2-level deck 1.2 units tall, was ≈ 0.4).
  New line "The cut crosses each level once, so a riffle can at most split it in two": cut line
  (21 | 31) with "cut", yellow rings where it crosses each level, right packet tinted; after the
  riffle the four new levels alternate untinted/tinted. Riffle 3 = 1.4 s + 0.8 s split, riffle 4
  = 1.25 s + 0.8 s, with "[pause]"s in the narration so the counts land on "eight"/"sixteen".
- C4 collapse: during the pause after "equally likely" each deck's 52 bars squeeze, in order,
  into one square token in place (no translucent smear); then the axes draw on their own; then on
  "pile each deck onto its count" the tokens drop onto x = 14 and x = 26 under "14"/"26" and
  "1 deck"; the labels fade before the bars grow.
- C5/S7 k = 6 frame: gap row, gap bracket and the in-chart "perfect" label leave during the
  accuracy derivation (return on the seventh riffle); "k riffles" rides above the purple
  histogram (just above the plot, following its centre). Accuracy is now a two-line derivation
  (copies of each term slide down into "= ½ + ½(0.78 − 0.17)"; the second line rises into
  "accuracy = ½ + ½d"), so nothing piles up in place. "chance" kept as the standard y-axis title.
- C6 "trace plot" → "one statistic can settle, like the top card". C7 the Markov sentence folded
  into one: "Many Markov chains share this cliff, and samplers share the trap: …" (−0.75 s).
- C8/S9 "read left to right" → "reading left to right" (transcript now correct).
- C9 the top-card chart fades (0.45 s) before the deck moves. C11/S8 the tag switches to the target
  count at the start of every slide; gap and d labels are hidden during slides and written only at
  whole riffle counts.
- S2 cold open: two sorted decks from frame one; the left riffles under "heads: 4 riffles", the
  right is shuffled perfectly under "tails: perfect shuffle" on "shuffles it perfectly"; the same
  two decks return in the same places in level view at 1:17 (14 vs 26 levels).
- S6 top card: see fact changes. S10 stakes: MCMC first, card rooms dropped (−3 s).
- Also found in review: "d = 0.33" crossed x = 6.4 → low-d labels go down-left of the dot;
  a pause before "when" made whisper hear "n" → pause moved before "So"; "Here it's one" heard as
  "Where it's one" → "Right now it's one"; FadeTransform used (without stretching) for the
  changed glyphs (230 → 52·53/12, 52 → n, 53 → n+1, 6.8 → formula, (0.78 − 0.17) → d) so no
  frame shows a point-morph glyph soup; TransformFromCopy arcs bow opposite to Transform arcs
  (fixed for the "2.1" copy, which had grazed the d-plot title).

### Final mechanics (review/report.md)
Runtime 3:53.9 · 155 wpm (speech) · −14.0 LUFS / −1.9 dBTP · lead 0.00 s / trail 1.89 s · max
silence 1.98 s (planned prediction hold) · max static 3.23 s (the gap ≈ 230/2^k = 2.1 hold; the
other ≥ 3 s stretch is the 52·53/12 hold, 3.0 s) · WER 1.4 % (remaining diffs are number
normalisation, homophones and "Aldous" heard as "all does", the intended ALL-dus) · 0 banned
phrases · 0 render warnings · layout audit 0 issues in 269 checks · 0 review flags.
Four master renders this round; every contact sheet and the frames around each fixed timestamp
were checked, plus 0.25–0.3 s frame steps through the accuracy, eq1, eqF, n and k transitions.
