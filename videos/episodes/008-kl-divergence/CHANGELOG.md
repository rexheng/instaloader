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


## Round 3 revisions

Round-3 critics: craft 8.6, substance 8.6 (no caps; every number recomputed by both). The one
borderline cap (craft: a transient false equation "D(bell‖data) = ∫p log₂(p/q) dx = 5.77 bits"
during the swap at 1:48) is treated as a factual error and removed at the root.

**Plan of the climb (BAR §3 "9" anchors → upgrade).**
- *Hook 8.5 → 9 ("tension rises…; ending resolves the opening exactly").* Stakes made concrete
  at 0:20: "Bayesian machine learning uses it with the order flipped" + grey "variational
  inference" tag under the flipped line (Blei 2017 cited there). The bet's answer gets the
  cold-open picture back: the dashed ghosts 2 (25 %) and 3 (60 %) and the yellow 1/2/3 return on
  "Now start from A", B slides exactly into ghost 3, the 1→3 arrow lands on "three", then a 1 s
  pause and a ≈2.5 s hold. Landing line "One or three, depending on which curve goes first",
  with the yellow 1 and 3 re-shown on A's and B's crowns.
- *Clarity 8.5 → 9 ("all numbers check out; sources correct").* The swap never shows a false
  equation: the copy drops in already reading "= ?", arguments, weight and fraction swap in one
  move. The payoff's number is now a real measured result, not a relabelled data curve:
  Giordano, Broderick & Jordan (2018, JMLR 19:1–49, Table 3), a logistic GLMM on Criteo
  ad-conversion logs: for covariate effect β₃, MCMC 0.110 ± 0.020 vs mean-field VI 0.110 ± 0.004
  (same mean, a fifth of the spread). Toy brackets labelled "±1.14"/"±0.44"; the curve is tagged
  "if this were a posterior". "a one-bell fit stretches", "tends to settle" (Bishop's wording).
  "a distance" goes grey with a strike on "more than twice as far". Footnote now "Raw points:
  data first still ranks bells; bell first is ∞ for all".
- *Visual 8.5 → 9.* Formula blocks become two lines ("D(·‖·) = x bits" over "= ∫…dx"), each
  centred on its own bill panel, so the blocks are separated by 3× their line gap (the stacked
  chart is narrowed to 7 units to make room). Axis titles dimmed with the posterior relabel.
  Honest-limit fit label pinned up-right of the fit's crown with a dashed leader that follows
  the fit through both morphs (live numbers), y-axis extended to 1.1. The bell-first panel stays
  hidden until "Which bell wins now?". "peak ≈ 11" on one baseline.
- *Motion 8.5 → 9.* Whole-curve pulses (stroke + fill) on "supplies"/"judges" instead of pip
  flashes; the 2:33 teardown fades bills, blocks, panel axes, ghosts and labels first (chart at
  full strength), then scales the chart; panel tick labels fade, never morph; "?" fades before
  the bits number arrives; landing: A solid with its fill sweep on "Bell A", back to dashed as B
  fills on "Bell B".
- *Audio 8.5 → 9.* 1.0 s after "five point eight bits" before "Now keep that bill"; [pause 1.0]
  after "moves to three".
- *Concision 8.5 → 9.* Honest limit merged into two short sentences (≈ 4 s shorter); the landing's
  first line now answers the bet instead of restating the title.


## Round 5 revisions

Round-5 critics: craft 8.1, substance 8.1 (no caps). Both reviewed the 23:04 render, which
predates the round-3 edits above: that revision was interrupted after editing scene.py and was
never rendered. This round renders those edits together with every round-5 fix.

**Plan of the climb (BAR §3 "9" anchors).**
- *Hook 8 → 9 ("commits to a likely-wrong prediction by 0:12").* The bet now rests on a stated
  belief, not on undefined words: `D(data ‖ bell)` writes on the first frame with the curve, its
  blue "data" slot flashes on "Data first", the arguments arc on "Swap the order", and the wrong
  belief is voiced as the symmetry of a distance: "If closeness is a distance, order can't
  matter: it stays at one. Or does it move to two, or three?" Stakes made concrete: "Every
  maximum-likelihood fit shrinks it with the data first, and Bayesian machine learning shrinks
  it with the order flipped." The answer (yellow 3) now persists on B's crown through the
  teardown and the chart's regrowth until "settle on one hump"; 1.2 s pause after "moves to three".
- *Clarity 8 → 9.* No false equation can appear (copy drops in as "= ?", one swap move). Bracket
  labels "±1.14" / "±0.44". The payoff number is a measured result: Giordano, Broderick & Jordan
  2018 (JMLR) Tables 2–3, re-verified against the paper (β₃ means 0.110 / 0.110, SDs 0.020 /
  0.004), citation now names both tables. Honest limit rebuilt around the assumption the viewer
  needs, in one clause each: raw points make every bell-first score infinite (272-tick rug,
  `D(bell ‖ data) = ∞`), so the data is smoothed; smooth more heavily and the best bell-first fit
  spreads wide, "almost back to A". "R's default" and "cross-validation" are no longer spoken.
  Readouts p, q, log₂ dim to 30 % while the scanner is away from 2 min and come back with it,
  so the slide to B starts from 1.98.
- *Visual 7.5–8 → 9.* Three-panel stretch rebuilt: the chart (the subject) is 2.8 units tall
  instead of 1.85; bills share a [−0.5, 2.5] bits/min range; each bill names its order in its
  corner ("data first" / "bell first"); once the integrals have been read the blocks collapse
  to two D-lines with live totals, each centred on its own bill. Payoff legend moved right
  (left edge −1.0, clear of the y-axis title), set as `D(data ‖ bell)` / `D(bell ‖ posterior)`
  to match the episode's own notation; row 1 dims when row 2 lands; A steps out during the
  bracket comparison. "peak ≈ 11" at size 36 with its arrow stopping short of the plateau.
- *Motion 8.5 → 9.* The pull-out's baseline draws while the chart shrinks (the empty half has a
  destination); highlight boxes fade in whole (no corner dot); landing: each closing sentence
  writes its own answered D-line and returns its yellow number while its bell fills.
- *Audio 8–8.5 → 9.* 0.8 s after "one point one" (beat turn); the densest stretch (bell B,
  1:30–1:46) spoken at speed 0.80; 1.0 s after "five point eight bits"; 1.2 s after the answer.
- *Concision 8 → 9.* Honest limit cut from three concepts to one assumption and one
  consequence; the restating line before the closing pair is cut (the D-lines with → A / → B
  and the yellow 1 / 3 return silently, each with its sentence).



## Round 5 revisions (final pass)

Picked up an interrupted pass: scene.py and script.md had been edited after the 14:30 master and
not rendered. This pass rendered those edits together with the fixes below.

- **Rendered the pending edits.** The bet is now one question, "Or does the closest bell move to
  two, or to three?", spoken at 0.77. Whisper used to hear two questions and the slop scan
  flagged a question chain; the transcript now has one. The 18 s breathless run at 0:57 is split
  (0.45 s after "call it p" and after "you reach p"). In the honest limit, "272 raw points" now
  swaps with "if this were a posterior". The two tags were superimposed at 3:08.
- **Label flying through a formula (2:01, caught on the contact sheet).** On "Which" the
  x-axis name used to slide from the data-first bill to the bottom row, through
  `= ∫ q log₂(q/p) dx`. Now the numbers drop and the name fades out, then fades back in at its
  new place. Checked at 4 fps.
- **Empty top-right quadrant (1:50–2:37, about 47 s).** The chart's key now sits where the p/q
  readouts stood: `A: 3.49 ± 1.14 min` over `B: 4.27 ± 0.44 min`. On "less than half as wide"
  0.44 and 1.14 flag together, so the claim can be read off the screen. This replaces B's crown
  label, which had shown B's spread with no A to compare it to.
- **Audio.** The closing pair gets 0.5 s between its sentences (was 0.1 s). Before, "Bell B" was
  crushed and whisper heard "be"; now it hears "Bell B". The honest limit no longer says
  "bell-first", which whisper heard as "belfirst". It now says "with the bell first, every score
  is infinite … the best fit spreads almost back to A". The on-screen label is unchanged.
- **Facts.** Re-read Giordano, Broderick & Jordan 2018 (JMLR PDF): β₃ is 0.110 / 0.110 in
  Table 2 and has SDs 0.020 / 0.004 in Table 3; the data are the Criteo 2014 conversion logs.
  Recomputed the naive shift and stretch (1.118 and 1.111 bits; the 1.11 on the old contact
  sheet was a mid-move frame). Added the key's numbers (0.4408 / 1.1393 = 0.387) to facts.md.
- **Result.** 3:30.6, 500 words, 159 wpm over speech, −14.0 LUFS / −1.9 dBTP, longest silence
  2.09 s (the planned prediction hold), longest static 3.4 s, WER 1.6 %. The report has 0 flags,
  0 banned phrases or patterns, 0 render warnings, and the layout audit found 0 issues in 192
  checks. Looked at all 12 contact sheets, the keyframes at 2:06, 2:19, 2:32, 2:56, 3:12, 3:21
  and 3:26, and 4 fps strips across the label swap (2:01), the key flag (2:31), the collapse
  (2:20), the teardown (2:36) and the tag swap (3:08).
