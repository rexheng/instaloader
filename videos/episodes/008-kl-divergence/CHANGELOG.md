# Episode 8 — changelog

## Round 1 revisions

Round-1 critics: craft 7.0 (text-overlap cap), substance 6.0 (on-screen factual error cap).
Every fix from both reviews was applied; the three "keep" items (the doublings picture, the
persistent chart with the live bill, the answered cold-open lines and closing pair) survive.

**Factual (cap 6).** The payoff legend said `D(model ‖ data) · variational inference`; the critic
is right (VI minimises KL(q(z) ‖ p(z|x)), Blei et al. 2017 eq. 1). It now reads
`D(model ‖ posterior)`, the blue curve's tag turns "data" → "posterior" before that row
appears, and the narration says "Variational inference approximates a Bayesian posterior with the
model first, so it settles on one hump". facts.md records the evidence.

**Overlaps (cap 7).** The one-length beat now pulls the p and q bars out of the chart into the
empty right third (same baseline and scale), so the q stacking, ×2 labels and p/q symbols sit in
free space and the dead right column is used (replaces the suggested zoom). The chart's q tag is
gone; the readout switches to scientific notation (`q = 1.6×10⁻⁶`) instead of 0.00. Bell A is
labelled on its isolated left tail and drawn dashed whenever B is on screen. The two-panel →
full-chart change fades the lower-panel labels first (no "bits per mi1nute"). The legend no longer
touches the y-axis title. The measured line no longer flies through the readouts in beat 6.

**Hook / landing.** The cold open voices the wrong belief as a binary bet ("Closeness should work
both ways, so flip the measure around, and this bell should stay put. Does it?") with a yellow
"stays?" pin on bell A; the first frame already shows the eruption bars. Beat 10 answers it ("Flip
the order, and the closest bell moves") with an arrow from A's crown to B's. Landing line: "So
closeness depends on which curve goes first."

**Clarity.** Clipped log-ratio stretches are drawn faint with their true depths tagged (↓ −45,
↓ −6.2, ↓ −20). "Maximum-likelihood fit" / "A: 3.49 ± 1.14" are pinned to bell A's crown by the
dashed mean line. Header decluttered (data label leaves at 0:14, "KL divergence" dims, A label
dims in the fail beat). Payoff is measured: ±1 SD brackets on A and B fly into
`(0.44 / 1.14)² = 15%` ("bell B keeps only fifteen percent of it"). "Bishop draws the same
picture" cut. Honest limit rewritten: "Settling on one hump needs that gap to be nearly empty.
Smooth the data with R's default setting, and the gap fills enough that the best bell-first fit
comes out wide too", demonstrated with R's actual default bandwidth (bw.nrd0 = 0.335 min,
recomputed in data.py: best fit 3.55 ± 0.99 min), labelled, A dimmed, plus a footnote that against
raw points every bell-first score is infinite.

**Motion / audio.** Flashes run only along the parts of a curve above the axis (no streak along
the baseline). Shift/stretch excursions are 2 s each with a 0.5 s hold on the raised number.
Sentence gaps now vary (≈ 0.25 s inside a thought, 0.7–1.0 s after payoff numbers and at beat
turns, the last two lines paired).

**Result.** Master re-rendered (3:17.4, 160 wpm over speech, −14.0 LUFS / −1.7 dBTP, longest
silence 1.97 s, longest static 3.5 s, WER 0.8 %, 0 banned phrases, 0 render warnings). Checked
every contact sheet, full-resolution frames at each fixed timestamp, and 4 fps strips across the
three layout changes (1:15, 1:48, 2:28): no text overlaps at rest or in motion.


## Round 2 revisions

Round-2 critics: craft 7.0 (cap 7: the yellow highlight boxes sat on the parentheses of D(…) at
0:54 and 3:08; weighted 8.0, "core picture is Bishop's textbook figure"), substance 8.2 (no cap).
No factual errors were claimed; every number was re-verified (data.py, facts.md).

**Plan of the climb (BAR §3 "9" anchors → upgrade).**
- *Originality 8 → 9 ("an image viewers would remember").* Restructured the second half around
  one persistent picture that is not Bishop's figure: under the same bell, **two bills side by
  side** — the data-first bill and the bell-first bill, each with its own formula and live total.
  The swap keeps the first bill and adds the second; B is scored on both (5.77 vs 0.62), A on both
  (0.76 vs 1.69), and in the descent from A to B one bill drains while the other swells into the
  clipped mountain (live "peak ≈" counts up to 11). Monotonicity of both totals and of the peak
  along the stored path is verified in facts.md.
- *Hook 8 → 9 ("commits to a likely-wrong prediction by 0:12; ending resolves it exactly").*
  The bet is now spatial and three-way, not about notation: "it stays at one. Or does it move to
  two, or three?" with 1 on A's crown and faint numbered ghosts on the two humps (option 2 is a
  real local minimum, 1.52 bits). The notation is introduced only as an order ("with the data
  first … put the bell first", the arguments arcing). Beat 10 answers it on the same image
  (1 → 3 arrow, "moves to three"). The title does not say which of 2 or 3.
- *Clarity 8.5 → 9.* Grey dips explained ("Where the bell rises above the data, the grey dips pay
  a little back" + a "refund" tag); payoff referents fixed (posterior bracket drawn blue on the
  blue curve, B's bracket above the blue crowns, labels 1.14 / 0.44 fly into the fraction, bars
  and axis title dimmed, "same curve, as a stand-in" note, narration "…fifteen percent of the
  posterior's variance"); honest limit never reuses the name B, its fit starts from A (where a
  slide from A really ends), and a new sentence says which smoothing to trust: "Smoothing chosen
  by cross-validation keeps the gap nearly empty, and the fit on one hump" (LOO-CV bandwidth
  0.103 min, fit 4.28 ± 0.39 min, computed in data.py and shown on screen).
- *Visual 8 → 9.* Boxes no longer touch any glyph (whole D-lines boxed, unfilled; landing uses
  inset underlines under the first argument only); italic A/B everywhere (stats labels, legend,
  landing); footnote D set in math; shared x labels (1–6 and the axis name) sit under the lowest
  panel, the unit "bits/min" inside each panel's corner; formula blocks centred on their bills;
  B's stats pinned to B's crown by a dashed leader; the bell-first panel waits at 30 % until its
  bill draws; legend removed (not dimmed) in the honest limit (word load ≤ 12).
- *Motion 8 → 9.* Every layout change fades its numbers first, then moves (0:55, 1:13, 1:46, 2:33);
  p rises from the pulled-out p bar around the outside of the pull-out and q drops from its
  readout (no flight through a readout); the weight p swings round the left of the readouts;
  "data" → "posterior" is FadeOut then Write; the second formula block fades in only after the
  first has moved clear, then swaps in place; no simulated draws (they gave the answer away).
  Shift/stretch excursions now move the number visibly (0.76 → 1.12 and 1.11, flashed in the hold).
- *Audio 8 → 9.* "With the data first, this bell…" → "Data first, this bell…"; [pause 0.3] after
  "Every p trades places with q."; deictics retimed (sync warnings fixed; no static frame > 4 s).
- *Concision 8 → 9.* Cut "It sits at the data's own mean and spread", "With the data first, every
  hump must be covered", "Both orders are in daily use"; the added sentences each change the
  picture (refund tag, keep-both-bills, CV morph).

**Every round-2 fix, applied.** Craft 1 (boxes) · 2 (ML: A solid with a fill sweep, B at 30 %, swap
back on VI; legend "→ A / → B") · 3 (posterior bracket, B bracket raised, labels, narration) · 4
(grey dips + cut) · 5 (−0.8 min / ×1.8, flash) · 6 (30 % panel, B pinned, block centred) · 7
(spatial three-way bet, arrow lands on 3) · 8 (unit label, x labels under the lowest panel) · 9
(fade before move) · 10 (italic A/B, math footnote) · 11 (draws removed) · 12 (rephrased).
Substance 1 (bars 25 %, axis title 30 %, stand-in note, blue bracket, 1.14 blue) · 2 (A and B equal
during the question, no draws) · 3 (fit labelled "best bell-first fit", started from A, B never
reused) · 4 (CV sentence) · 5 ("refund" tag) · 6 (legend removed before the landing) · 7
(FadeOut → Write) · 8 (p and q flights re-routed) · 9 (cut) · 10 (legend removed) · 11 (pause)
· 12 (binary → three-way spatial bet).

**Keep items preserved.** The doublings pull-out (1:00–1:13); the persistent chart, strict palette,
live bill with the clipped "peak ≈ 11" mountain and q = 1.6×10⁻⁶, the argument-arc swap (now done
in place in the second block) and the descent from A to B; the bookended landing with "→ A / → B"
and the closing pair; the honest-limit beat with R's real default bandwidth.

**Performance.** Redraws are cached on the trackers they depend on (render ~3× faster).

**Result.** Master re-rendered (3:27.4, 164 wpm over speech, −14.0 LUFS / −1.6 dBTP, longest
silence 1.96 s (the planned prediction hold), longest static 3.6 s, trailing 0.9 s, WER 1.3 %
(differences are number formatting, "gray", and the correct "Bly"), 0 banned phrases, 0 render
warnings, layout audit 0 issues in 189 checks). Checked all 12 contact sheets, full-resolution
keyframes at every fixed timestamp, and 3–5 fps strips across every layout change (0:55, 1:08,
1:13, 1:19, 1:46, 1:59, 2:33): no text overlaps at rest or in motion, no double prints. One
Manim gotcha found and fixed on the way: a play-level `rate_func` overrides an animation's own,
so the second block's delayed fade is now its own 0.35 s play after the move.
