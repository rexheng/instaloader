# Episode 20 changelog

## Round 1 revisions

Reviews: `reviews/round1-craft.md` (8.4) and `reviews/round1-substance.md` (8.2). No factual errors
were claimed. The new sourced claim (Weissgerber et al. 2015) was checked against the PLOS Biology
article before use (facts.md #22).

**Hook and stakes**
- The first frame now shows the axes and "n = 142". Each readout row is written on its spoken words.
- The commit is now "Picture the scatterplot, and its best-fit line." The title does not give the line
  away. The guess cloud carries a grey dashed line, and the landing grows the yellow best-fit line onto
  it ("the line you pictured was its line").
- The generic stakes line is replaced by a sourced one: of 703 physiology papers, 86 % used bar graphs
  and 13 % showed the points (Weissgerber et al., 2015 · PLOS Biology). On screen, the dinosaur
  squeezes into a strip of its y-values, then becomes a bar (ȳ) with an error bar (±s_y).

**Readout and fail beat**
- The "now" column fades in at its final position, shifted 0.3 and staggered by row. No digit strings
  overlap any more.
- Added a grey note: "first two decimals, as published".
- The fail beat is animated as it is narrated. A yellow dot and mean ± SD error bars mark the
  dinosaur. Red ones slide to the star's centre, stretch in x and shrink in y. When the points go back
  to the dinosaur, the red cross merges into the yellow one. The box later grows from these arms.
- Cut "Version one only looked at the shape…". "Version one:" became "Version one slides…".
- Removed every Circumscribe, which caused the stray red strokes. Flags now use Indicate.

**Insight**
- During the correlation sweep, the r row and the counter dim to 35 %. A yellow live "r = …" label
  rides the touch dot (−0.06 → 0.88 → −0.06), then fades, and the restored r row is Indicated.
- The replay is trimmed to "Now replay version one, and watch the ellipse." "Tip it" is now "tip it, a
  slight shear". "All five match now, to every decimal place" merges the two lines that repeated each
  other.
- The median row is "med y", aligned with the five rows above.

**Payoff**
- In the Datasaurus Dozen, each `[pause 0.4]` became `[pause 1.5]`. Each shape lands 0.3 s before its
  noun and holds for 1.6–1.9 s. The box, the centre and both touch dots stay on screen, and they are
  recomputed from the points every frame.
- From `dots` the sequence goes straight to Anscombe I. Eleven points travel, the other 131 fade out
  with the old tick labels, and the ellipse, box, centre and touch dots morph into Anscombe's. The old
  ticks fade out before the new ones fade in. The two citations swap in succession, so they never
  overlap.
- The slope is now derived: slope = cov(x,y)/s_x² → r s_x s_y/s_x² → (cancelled s_x and exponent struck
  through) → r s_y/s_x. The terms then fly onto the rise and run segments, and the line grows from the
  centre through the touch point. The s_x label sits directly under the run segment, on a background
  patch.
- B21 now reads "…the ellipse and the line. [pause 0.3] A trend, …".

**Landing**
- The quartet fades out as its sentence ends, and the opening frame fades in at once, so no frame is
  empty. The ellipse is drawn on "this ellipse", and the best-fit line on "its line".

**Verification (final master, 3:30.1)**
- render.sh: 0 scene warnings. review_kit: 0 flags. Pace is 159 wpm on speech time, loudness is
  −14.0 LUFS with a −1.6 dBTP true peak, and the longest internal silence is 1.98 s.
- Static stretches are 3.4 s and 3.5 s, both planned prediction holds. No frame shows only the
  background.
- WER is 3.0 %, and whisper now hears "a trend".
- Checked frame by frame:
  - the "now" column split;
  - the fail-beat error bars;
  - the r-sweep label;
  - the Dozen holds (star 140.9–142.4 s, bullseye 143.4–144.9 s, X 145.9–147.4 s, stripes
    148.4–149.9 s);
  - the Anscombe tick swap;
  - the cancellation (fixed: cancelled pieces had drifted toward the origin, and stray axis titles
    were left behind);
  - the label flights, the s_x label patch and the landing.

## Round 2 revisions

Reviews: `reviews/round2-craft.md` (final 7.0, weighted 8.4) and `reviews/round2-substance.md` (final 7.0,
weighted 8.3). Both capped at 7 by one settled overlap: the s_x run label on the ellipse arc (3:00.8–3:08.5).
No factual errors were claimed.

### Plan of the climb (written before editing)

| Dimension | BAR "9" anchor | Where round 2 fell short | Upgrade |
|---|---|---|---|
| Hook 8–8.5 | commit by 0:12; ending resolves the opening exactly | commit ended 0:13.8; frame 1 was empty axes | shorter B0 (commit by ~0:10); the five symbol slots are on screen from frame 1; the dashed guess line is labelled "your line" and paid off at the landing |
| Clarity 8.5 | re-derivable after one watch | touch height r·s_y used at 2:57 but never shown; Anscombe's numbers never shown; median beat implied the Dozen fix the median | B9 states the rule and draws the live rise r s_y; Anscombe readout on screen and flown into the substitution; live med y row through the Dozen ("and a different median") |
| Visual 8 | all §5 standards met | s_x label on the ellipse (cap); "≈ 0.50" past the safe edge; meaningless x ticks under the strip; white Anscombe points | zoomed Anscombe axes, s_x under the part of the run outside the ellipse, asserted clearances; equation block left-aligned and asserted ≤ 6.2; x ticks dimmed during the strip; points stay BLUE |
| Motion 8.5 | every motion encodes a relation | static dinosaur under "Nudge"; stacked-glyph flights; cross-dissolve landing | one point is nudged, breaks the numbers and is rejected on screen; flights Indicate their source then arc around text; panel I's ellipse is carried into the landing |
| Audio 8.5 | every deictic lands | "these five numbers" with none visible | the readout is on screen and Indicated on the phrase |
| Concision 8–8.5 | cutting any sentence loses something | "Those three moves only protect…" restated the row; "almost none" | both cut; "slower search" replaced by what the search does |

### What changed

**Cap 7 removed: the s_x label (3:00.8–3:08.5 in round 2)**
- The background patch is gone. The Anscombe axes are zoomed to x 3–15, y 3.5–11.5 (the suggested 4–14
  would have put two of his points on the axes). The ellipse is about 1.2× larger.
- s_x sits under the right part of the run (proportion 0.75), where the ellipse has already crossed
  above the centre line, so nothing is behind it. scene.py asserts ≥ 0.15 units from 200 samples of
  the ellipse, the box, the centre and touch dots, all eleven points, the best-fit line and the rise;
  the same check covers r s_y, and the frame was checked at 3× zoom.
- Every other placement that was a risk is asserted the same way (guess labels, the 86 % / 13 % labels,
  the B9 labels at both ends of the sweep, the readout and substitution, the quartet rows), and the
  equation block is asserted inside x ≤ 6.2 (the substitution now ends at x = 5.2).

**Clarity**
- B9 states the rule: "The correlation picks the one ellipse that touches all four walls. Raise it,
  and the touch point on the right wall climbs toward the corner: it always sits r times s y above the
  center." A dashed centre line, a live rise segment and the label r s_y show it; at 2:59 the same
  rise and run come back. The sweep is a "what if" ellipse, so the dinosaur fades out while it runs
  (the picture never contradicts the data's r = −0.06, which is dimmed), and returns on "everything
  the five numbers know".
- The median beat is now honest about the Dozen: "But add a sixth number…" (merged, about 3 s
  shorter); "built a search that holds whatever numbers you choose. They chose these five." The
  readout stays on screen and live through the search and the Dozen, the median row included: the
  five = marks never change while the median jumps 51.02, 50.11, 47.38, 39.87, 50.47, 51.29 (all ≠
  46.02), and the narration ends "…this same ellipse, and a different median."
- Anscombe's own five numbers are on screen (bottom right, yellow) from "five numbers of his own".
  0.82, 2.03 and 3.32 are each Indicated there and fly into the substitution, in yellow. "These five
  numbers" (3:16) gets a box around them; the readout stays under the quartet.
- "with exactly these five numbers" → "with these same five numbers".

**Hook**
- B0 is "A hundred and forty-two points, five numbers: …" and the commit ends at 0:11.9 (was 13.8),
  with the 1.5 s hold kept. The five symbol slots are on screen from the first frame. The dashed
  guess line is labelled "your line", and the landing grows the yellow line over it.

**Motion and sync**
- The nudge is acted out: on "Nudge" one tail point is ringed and stepped at random, and x̄, ȳ, s_x
  turn red ≠; on "target shape" the dashed circle is drawn; on "keep the nudge only if" the step is
  undone and the column returns to =; then the staggered morph runs on "Repeat it enough times".
- Rise and run flights Indicate their source first and arc around "slope =" (over it for the
  numerator, under it for the denominator).
- The Anscombe readout no longer morphs digits: the dinosaur's values leave as the plot starts to
  turn, the symbols glide into the new slot, Anscombe's values fade in.
- The landing carries panel I's ellipse: it grows back into the dinosaur-scale ellipse while the
  quartet fades and the opening frame fades in (overlapping fades, never a near-empty frame), and is
  pulsed on "this ellipse" instead of being redrawn.
- "≈ 0.50" joins "slope = r s_y / s_x" before the quartet instead of floating alone.

**Visual**
- Stakes: grey "86 %" beside the bar, "13 %" beside the returning points; the x ticks, numbers and
  "x" dim to 25 % while the strip has no x meaning.
- Anscombe's travelling points stay BLUE (scaled, not flashed white).
- Fixed a bug found in review: dimming the x-axis numbers by animating a sub-group split the axes
  and dropped the x-axis line from 0:29 to 2:40 in the first master; the dim is now driven through
  the axes object.

**Not adopted, with evidence (facts.md #12)**
- "Ran two hundred thousand tiny nudges" with a 0 → 200,000 counter over the dinosaur → circle
  morph. The Autodesk page's 200,000 iterations caption Fig. 4, a random cloud turned into a circle,
  and the paper's 200,000 refers to its Figure 1 example dataset; no count is published for the
  dinosaur → circle run. The adjective "slower" is gone instead, and the search is shown, not rated.
- The automatic overlap audit flagged three things in the first audited master, all now fixed: the
  axis names "x" sat 0.09–0.11 from the last tick label (moved), and the strike-throughs of the
  cancelled s_x and exponent (deliberate, 0.45 s) are declared with a reason.

**Verification (final master, 3:37.0)**
- render.sh: 0 scene warnings; layout audit 0 issues in 237 checks. review_kit: 0 flags.
- Pace 162 wpm on speech time, −14.1 LUFS, −2.0 dBTP, longest internal silence 1.96 s, static
  stretches 3.3 s and 3.5 s (both planned prediction holds), WER 2.5 % (whisper now hears "r times
  S-Y" where it heard "our standard deviations" in the preview).
- Looked at all 12 contact sheets and the keyframes at 1:24, 2:11, 3:16, 3:20 and 3:29, plus frame
  strips across the sweep (1:20–1:32), the nudge (2:09–2:18), the Anscombe hand-off (2:39–2:47), the
  slope flights (3:04–3:14), the quartet (3:15–3:24) and the landing hand-off (3:23.9–3:25.6, sampled
  every 0.17 s: the frame is never near empty). The s_x label checked at 3× zoom at 3:13.8.

## Round 3 revisions

Reviews: `reviews/round3-craft.md` (final 8.7) and `reviews/round3-substance.md` (final 8.6). No caps and
no factual errors were claimed; both critics recomputed every number and verified all four citations.
New or reworded claims were checked before use (facts.md #26, #27, #30, #32–#35; the
Freedman–Pisani–Purves regression sentence behind "one SD right, on average r SDs up" was checked
against the 4th edition, p. 160).

### Plan of the climb (written before editing)

| Dimension | BAR "9" anchor | Where round 3 fell short | Upgrade |
|---|---|---|---|
| Hook 8.5 / 8.5 | commit to a likely-wrong prediction by 0:12; ending resolves the opening exactly | commit was an open "picture…" ending 0:12.3, spoiled by the title; the bar-graph stakes never came back | commit on the line ("Which way does their best-fit line tilt, and how steeply?", ends ~0:11.5, "?" in the hold); landing states the reversal ("Your line was exactly right… Your cloud was this ellipse") and pays off the stakes (the ellipse squeezed into the ȳ ± s_y bar) |
| Clarity 9 / 8.5 | viewer could re-derive it after one watch | r·s_y touch height asserted; "the one ellipse" misstated uniqueness; cov → r s_x s_y announced | "Many ellipses touch all four walls. The correlation picks one" with two grey ghosts; "Correlation r means one SD to the right, on average r SDs up" with a run (s_x) and a rise (r s_y) drawn from its end; cov(x,y) = r s_x s_y built from the readout's own symbols |
| Visual 8.5 / 8.5 | every frame one focal point; all §5 standards met | empty top-right 2:45–2:53; quartet labels crowding the readout and off baseline; small decimals note; busy prediction-hold frame; referentless 86 % / 13 % | readout lands mid-right level with the touch point, then steps down; labels on one baseline, readout ≥ 0.45 below; note at Text 25 held to the dinosaur's return; boxes dimmed in the hold; "86% used bars", "13% showed points" |
| Motion 8.5 / 9 | every motion encodes a relation | nudge moved away from its target; cov glyph crossfade; stacked copy train; double-exposure landing; double axes at the quartet hand-off | nudge steps toward the circle; side-line derivation; copies arc over the row farthest-first; landing sequenced around the one continuous ellipse; old axes out before panel axes in |
| Audio 9 / 8.5 | pauses intentional | metronomic 0.5 s gaps and four 1.6 s roll-call pauses | 0.15–0.2 s gaps inside a thought, 0.65–0.7 s at beat boundaries; roll-call pauses 1.3 / 1.0 / 1.2 / 0.9 |
| Concision 8.5 / 8.5 | cutting any sentence loses something | "five numbers:", "Go back to the dinosaur.", "and five numbers of his own", long roll-call silences | all cut (≈ 4.5 s), paying for the new B9 reason and the stakes payoff |
| Originality 8.5 / 8.5 | a non-obvious angle viewers would remember | the "your line was right" reversal was implicit; the stakes ended at 0:38 | the reversal is said; the closing picture turns the ellipse into the bar graph 86 % of papers used |

### What changed (every fix from both reviews)

**Hook and landing (craft 1, 8; substance 3, 4, 10)**
- B0 drops "five numbers:" (the slots are on screen from frame 1) and asks one committable question
  about the thing the five numbers really fix: "Which way does their best-fit line tilt, and how
  steeply?" The question ends at 0:11.5; "n = 142" fades and a faint grey "?" fills the plot centre
  for the 1.5 s hold, so the axes are never empty while the viewer commits.
- B1: "A shapeless oval cloud" (the drawn cloud is a tall oval).
- Landing, rewritten as the reversal: "Your line was exactly right: five numbers fix it. Your cloud
  was this ellipse, all that five numbers can draw. Most of those papers used a bar graph, which
  draws only two. The dinosaur lived in everything they leave out." The dashed "your line" is
  Indicated on "exactly right" and the yellow line grows over it on "five numbers fix it". On "Most
  of those papers" the Weissgerber citation and "86% used bars" return; on "bar graph" a copy of the
  ellipse is squeezed horizontally to its vertical extent, which is exactly ȳ ± s_y, so it becomes
  the stakes beat's error bar as the ȳ bar grows under it; the ȳ and s_y rows flag on "two". On the
  final line the bar dims and the points return to the dinosaur around the ellipse, line and bar.
  ("Most … used a bar graph" rather than "86 % … drew two": 85.6 % had at least one bar graph, and
  a bar with an error bar encodes two numbers whether the bar is SD or SE; facts #35.)
- Landing hand-off sequenced around one continuous object: the quartet fades out (0–0.48 s) while
  panel I's ellipse grows back to dinosaur scale, then the opening frame fades in (0.5–1.06 s); no
  text overlaps text and the frame is never empty.

**Clarity of the insight (substance 1, 2)**
- "Many ellipses touch all four walls. The correlation picks one." Two grey ghost ellipses
  (touch heights ±0.5 s_y, 40 %) appear on "Many" and give way to the yellow one on "picks one".
- "Correlation r means one standard deviation to the right, on average r standard deviations up. So
  the touch point on the right wall sits r times s y above the center." The sweep now starts from
  r = 0 (touch point level with the centre); a thin yellow run from the centre to the right wall,
  labelled s_x, is drawn on "one standard deviation to the right", and the rise grows from its end
  on "r standard deviations up" (r 0 → 0.80). The same run and rise return in the slope at 3:05.
  The s_x label sits above the run's left part, the only place that stays ≥ 0.15 from the ellipse
  for every r in the sweep (checked numerically, then asserted in scene.py).

**Derivation (craft 3)**
- cov(x,y) → r s_x s_y is no longer a glyph crossfade. A side line "cov(x,y) = r s_x s_y" is built
  under the fraction: cov(x,y) is copied down, then r, s_x and s_y are each Indicated in Anscombe's
  readout and flown up on their spoken words. Its right side is carried up a lane to the right of
  the fraction (never through the denominator) while the old numerator vacates its slot, slides
  in, is flagged, and the side line fades; then the s_x cancels as before. "[pause 1.0]" after
  "s y," gives the move its time.

**Motion (craft 2, 4; substance 7)**
- Nudge: the dashed target circle and the ring are drawn on "Nudge"; on "biased toward" the ringed
  tail point steps 5.5 units straight toward the circle (inward): x̄ 54.22 ≠ and s_x 16.68 ≠ break,
  the rest hold; it is undone on "keep the nudge only if" (facts #27).
- Quartet copies arc over the panel row (path_arc, LaggedStart lag 0.5 over 1.75 s), farthest panel
  first (IV, III, II for the ellipses, then the lines). With the critic's II, III, IV order the
  copy for III passes panel II exactly when II's copy lands there; farthest-first means no two
  copies ever share a position.
- Quartet hand-off: the zoomed Anscombe axes fade out over the first 40 % of the move and panel I's
  axes fade in from 45 % (panels II–IV after), so the two sets of tick labels never overprint.

**Visual (craft 5, 6, 10; substance 5, 6)**
- Anscombe's readout lands mid-right with r first, its upper row level with his touch point
  ("r = 0.82  s_x = 3.32  s_y = 2.03" / "x̄ = 9.00  ȳ = 7.50"); on "His correlation…" the
  "r = 0.82" item travels straight left into the touch dot. On "Least squares" the readout steps
  down to the bottom slot (0.8 s) to make room for "slope =".
- Quartet: panels raised to y = 0.68, the four labels baseline-aligned (each starts with a letter
  that sits on the baseline: a, a, a, o), and the readout ≥ 0.45 below the lowest label (0.48,
  asserted); its lower row shares the citation's baseline and stays above −3.2.
- "first two decimals, as published" is Text 25 (was 22) and is held until the dinosaur returns
  (1:01).
- Prediction hold: both boxes dim to 30 % on "How would you fix the star?" so the two ellipses and
  centres carry the frame; they return to full on "Stretch it until the boxes match".
- Stakes labels: "86% / used bars" and "13% / showed points" (MathTex 36 over Text 26, grey).

**Concision and cadence (craft 9; substance 8, 9)**
- Cut "five numbers:", "Go back to the dinosaur." (the points return during "So what exactly do five
  numbers pin down?") and "and five numbers of his own" (now "with eleven points of his own").
- Roll-call pauses 1.3 / 1.0 / 1.2 / 0.9 s (were four × 1.5), each shape landing 0.25 s before its
  noun with a 0.6 s move, so every state still holds ≈ 1.5 s.
- Beat-boundary gaps 0.65–0.7 s (before the stakes, at 1:00, at 1:56, before Anscombe), 0.1–0.2 s
  inside a thought (B3→B4, B7→B8, B8→B9, B11→B12, B16→B17, B19→B20, B21→B22), "[pause 0.2]" inside
  B5 and B22 and "[pause 0.6]" before the landing's last two sentences.

### Verification (final master, 3:42.3)
- render.sh: 0 scene warnings; layout audit 0 issues in 256 checks. review_kit: 0 flags.
- 160 wpm on speech time, −14.0 LUFS, −1.7 dBTP, longest internal silence 1.96 s (the commit hold),
  longest static stretch 2.97 s (no stretch ≥ 3 s), lead 0.00 s / trail 1.83 s, WER 3.1 %.
- New layout asserts in scene.py (render fails if broken): the s_x run label at r = −0.06, 0 and 0.8;
  the mid-right readout against the Anscombe plot; the cov side line and its rhs lane (≤ 6.35, clear of
  the fraction); the quartet labels against panels and the readout (≥ 0.45); the landing "86% used
  bars" against the guess cloud, bar, error bar, ellipse and line.
- Looked at all 13 contact sheets and keyframes kf_05 (stakes labels), kf_10 (note at Text 25), kf_16
  (run + rise sweep), kf_30 (readout level with the touch point), kf_33/34 (quartet hand-off, baseline
  labels) and kf_38 (ellipse → error bar), plus frame strips across the quartet copy flights
  (3:17.6–3:20.0, 5 fps: old axes gone before panel I's arrive; copies never overlap), the cov side
  line and rhs lane (2:57–3:02.6, 4 fps: the rhs never crosses the denominator, the numerator slot is
  empty when it arrives), the landing hand-off (3:23.6–3:26.0, 5 fps: no text over text) and the bar
  payoff (3:34.6–3:37.0: the squeezed ellipse spans exactly ȳ ± s_y).
- Runtime rose from 3:37.0 to 3:42.3: the cuts (≈ 4.5 s) paid for most of the B9 reason and the
  stakes payoff; the rest is the deliberate beat-boundary gaps and the cov lane.

## Round 1 revisions (second review cycle: craft 8.5, substance 8.3)

Reviews: `reviews/round1-craft.md` (8.5) and `reviews/round1-substance.md` (8.3). No caps, no factual
errors claimed; both critics recomputed every number and verified all four citations.

### Plan of the climb (written before editing)

| Dimension | BAR "9" anchor | Where it fell short | Upgrade |
|---|---|---|---|
| Hook 8.5 / 8 | viewer commits to a likely-wrong prediction by 0:12; ending resolves the opening exactly | the commit was only about the line (which the guess gets right); the narrator supplied the cloud; "how steeply" never answered | B0 "Picture the cloud. Which way does its best-fit line tilt?" (the cloud is now the viewer's own, likely-wrong guess); B1 "You probably pictured a shapeless oval…"; landing resolves both halves ("Your line was exactly right … Your cloud was wrong") and answers the slope with a number built from the readout (−0.06 × 26.93 / 16.76 ≈ −0.10) |
| Clarity 8 / 8 | viewer could re-derive it after one watch | touch point = regression point asserted with "So"; covariance announced, never defined | B9 draws the best-fit line (dashed, riding the touch dot) and five vertical slices whose midpoints sit on it, then slides the slices to the wall where each collapses onto the touch point; the covariance sentences are cut and Anscombe's slope is read off the run and rise ("follows the same rule"), every term flown from its referent |
| Visual 8.5 / 8.5 | one focal point, all §5 standards met | red cross in a matching state; 30 % boxes in the hold; final frame layered; "x  med y"; grey text 6.1:1 | cross turns yellow as it slides home; boxes gone in the hold, back on "Stretch"; bar and error bar slide out of the plot at the end; readout block shifted right 0.3; text grey lifted to #A6ADB7 (8.0:1) |
| Motion 9 / 8.5 | every motion encodes a relation; reading time respected | 1.0 s reveal; glyph smears (16.76 / 26.93, cov); short equation hold; axes-less panel I | 1.8 s reveal + 0.4 s hold before "A dinosaur"; numbers travel intact to their half-arms, box grows on "box"; cov derivation removed; quartet axes crossfade |
| Audio 8.5 / 8.5 | deictics land, pauses intentional, terms clear | "s x" fused ("when sx cancels") | symbols respelled "ess ex" / "ess why"; box lands on "box" |
| Concision 8 / 8.5 | cutting any sentence loses something | slack search mechanics; 13 s covariance detour; long roll-call pauses | search in two sentences with the readout flashed on "these"; derivation is one sentence plus "rise over run"; roll-call pauses 1.0 / 0.8 / 1.0 / 0.8 |

### What changed (every fix from both reviews)

**Hook and landing (craft 2; substance 1, 2, 5)**
- B0: "…a correlation of minus point oh six. Picture the cloud. Which way does its best-fit line
  tilt? [pause 1.5]". The viewer now commits to the cloud (likely wrong) and the line (likely
  right). The colon after "points" became "with", so the question still ends by about 0:11.5.
  "n = 142" fades on "Picture the cloud" and the grey "?" holds through the pause.
- B1: "You probably pictured a shapeless oval, with a nearly flat line." The narrator no longer
  supplies the guess as fact, and there is no "most people" claim to source.
- The landing resolves both halves: "Your line was exactly right: five numbers fix its slope, minus
  point one. Your cloud was wrong: a blur around this ellipse, all that five numbers can draw." The
  quartet's "slope = r s_y / s_x" is carried into the landing (top right). On "five numbers" the
  dinosaur's −0.06, 26.93 and 16.76 fly from their readout rows into it, in a lane to the right of
  the readout so they never cross the other rows. On "slope" the yellow line grows over the dashed
  one, and on "minus point one" "≈ −0.10" is written. The formula holds about 7 s. "A blur around
  this ellipse" replaces the overstated "your cloud was this ellipse".

**Clarity of the insight (craft 1; substance 4)**
- B9 now shows why the touch point sits r·s_y above the centre. "…on average r standard deviations
  up. That's the best-fit line, through the middle of every vertical slice. At the wall, the slice
  is just the touch point, r times ess why above the center." On "best-fit line" a dashed yellow
  line grows out of the centre through both touch dots. On "middle" and "vertical" five vertical
  slices of the ellipse appear, with midpoint dots that all sit on the line. On "At the wall" the
  slices slide right and shrink until each collapses onto the touch dot. During the sweep back to
  −0.06 the dashed line follows r, so the dot visibly rides it. The s_x label leaves when the line
  is drawn (no position clears both the sweeping ellipse and the line; searched numerically).
- The covariance sentences (about 13 s) are cut (substance 3). In their place: "His best-fit line
  follows the same rule: one ess ex across, r ess why up, through the center and that touch point.
  So the slope is rise over run." s_x, then r and s_y, fly from Anscombe's readout to label the run
  and the rise as they are drawn. The line grows out of the centre through the touch point. Then
  "slope =" is written, and the r s_y label arcs over it into the numerator and the s_x label
  under it into the denominator. Every term comes from the segment it measures, and the formula
  holds about 1.5 s alone before the substitution is added below it. This makes craft 4 (the
  1.5 s cov hold and "when sx cancels") and the cov glyph smear (substance 7) moot.

**Visual (craft 5, 7, 8, 10; substance 6, 8)**
- The drifted cross turns RED → YELLOW as it slides back with the points and is then dropped,
  since it coincides with the yellow cross. It is never red over the 5/5 readout.
- Prediction hold: both boxes fade out completely. They come back on "Stretch", the move that
  matches them.
- Final image: on "dinosaur" the ȳ bar and its error bar slide out of the plot to x = 124 at 40 %,
  beside the 142 points. Nothing crosses the dinosaur but the ellipse and the line.
- The readout block moved 0.3 right, so "med y" sits about 0.6 units from the axis name "x".
- Grey text (tick numbers, axis names, "your guess", "your line", headers, "matching", the decimals
  note, the percentages, all citations) is now #A6ADB7, 8.0:1 on the background. GRAY stays for
  axes, ghosts and outlines.

**Motion and sync (craft 3, 6, 9, 11; substance 7, 9, 10)**
- Reveal: "Here are the real points. [pause 1.1] A dinosaur…". The morph starts on "real", runs
  1.8 s (smooth) and holds 0.4 s before "A dinosaur".
- B8: "The two standard deviations reach one deviation out on each side, and draw a box." 16.76
  and 26.93 travel intact, on a small opaque patch, to sit beside the half-arms they measure. The
  arms light up, the numbers fade, and on "draw" the four walls grow out of the arm tips, complete
  on "box".
- Search in two sentences: "built a search that keeps these five numbers fixed. It nudges a random
  point toward a target shape, and undoes any nudge that breaks them." The readout flashes on
  "these" and "They chose these five" is gone. The ring, step and undo run at 0.45 s per move.
- Roll-call pauses are 1.0 / 0.8 / 1.0 / 0.8 (were 1.3 / 1.0 / 1.2 / 0.9), with 0.5 s moves
  landing 0.2 s before each noun.
- Quartet hand-off: the zoomed axis lines and panel I's crossfade over the same 0.8 s, and the tick
  numbers hand over in sequence so they never overprint. The points are never without axes.
- Anscombe readout: the dinosaur's column leaves with its values, and his two-row layout fades in
  during the plot hand-off (symbols first, r first), with his values on "points". The empty
  five-row column and the glyph reshuffle at 2:43 are gone. A glide was tried first, but the two
  layouts interleave, so some symbols crossed in flight.
- Symbols are spoken "ess ex" / "ess why".
- Fixed a toolkit-usage bug found on the way: `go()` passed `rate_func` to `play()`, which
  overrides every animation's own rate function. Windowed fades inside a point move (for example
  "86% used bars" leaving at the landing) therefore ran over the whole move. The rate function now
  goes on the point flow only.

**Facts.** No factual error was claimed. New or reworded claims were checked before use and are
recorded in facts.md:
- #26: the slice midpoints lie on y − ȳ = r(s_y/s_x)(x − x̄), and the slice collapses to the touch
  point at the wall. This was derived and checked numerically for all five slices.
- #34: −0.06 × 26.93 / 16.76 = −0.096 → −0.10; unrounded and from polyfit it is −0.1036.
- #12: the search wording.
- #32: "You probably pictured…" is not a population claim.

### Verification (final master, 3:35.5)
- render.sh: 0 scene warnings. Layout audit: 0 issues in 251 checks. review_kit: 0 flags.
- Pace is 158 wpm on speech time, loudness −14.0 LUFS with a −1.8 dBTP true peak.
- The longest internal silence is 1.97 s (the commit hold). The longest static stretch is 2.90 s.
- Lead silence is 0.00 s and trailing silence 1.85 s. WER is 4.0 %; Whisper now hears "s y" and
  "sx" where it heard "when sx cancels".
- The question ends at 0:11.9.
- Runtime fell from 3:42.3 to 3:35.5. The search (−4 s), the covariance detour (−11 s) and the
  roll-call pauses (−1 s) paid for the B9 proof (+5 s), the reveal hold and the slope-at-landing
  line.
- I looked at all 12 contact sheets and at keyframes kf_02, kf_18, kf_20, kf_24, kf_29, kf_31,
  kf_36 and kf_39. I also checked frame strips at the fixed moments:
  - the cross recolour (1:00.6–1:02);
  - the SD numbers beside their arms and the walls on "box" (1:09.6–1:13);
  - the slices collapsing onto the touch dot (1:29.6–1:31.8);
  - the landing value flights (3:16.9–3:18.5): each number stays legible in the right-hand lane and
    never crosses another row;
  - the Anscombe readout hand-off (2:40.6–2:43.8);
  - the parked bar in the final frame (3:33.6).
- Two bugs were found in the first master and fixed before this one:
  - The slices never moved: their VGroup was not in the scene, so its updater never ran. The
    collapse is now driven by UpdateFromFunc.
  - Landing values flown with a per-glyph lane offset collapsed into a smear. The offsets are now
    computed from the whole mobject.

## Round 5 revisions

The two round-5 review files (`reviews/round5-craft.md`, `reviews/round5-substance.md`) are
byte-identical to the second cycle's round-1 reviews (craft 8.5, substance 8.3; they review the
3:42.3 cut). Every one of their 21 fixes was already applied in "Round 1 revisions (second review
cycle)" above, and no factual error was claimed in them (both critics recomputed every number and
verified all four citations). This round therefore re-audits the current 3:35.5 master the way a
fresh critic would: every contact sheet, the keyframes, and 4 fps frame strips across every
transform (§11.6). It also clears the round-4 fixes that the cycle-2 critics did not repeat but a
fresh critic could raise again.

### Plan of the climb (written before editing)

| Dimension | BAR "9" anchor | Where the current cut falls short (evidence) | Upgrade |
|---|---|---|---|
| Visual 8.5 | every frame one focal point, all §5 standards met | flash on "these" (2:12) scales each row 1.08 about its own centre, so the yellow values crowd their "=" ("x̄ =54.26"); the r-row Indicate at 1:37 does the same ("r =−0.06"); two yellow labels stacked on the rise ("r s_y" over "r = 0.80", 1:31–1:34, round-4 craft 6); at the landing four yellow strokes meet at the bar top (line, bar top, error bar, ellipse; 3:29–3:31, round-4 craft 4); prediction hold has the full-strength star competing with the two ellipses (1:45–1:48, round-4 substance 7) | "these" becomes a yellow box round the five rows (as for Anscombe's "these five numbers"); r-row flags run per value; the live "r = …" label moves to the box's top-right corner while "r s_y" names the rise, and rides there through the sweep back; line to 30 % and ellipse to 60 % while the ellipse is squeezed into the error bar, restored on "dinosaur"; star points at 40 % for the prediction hold, back to full on "Slide" |
| Motion 8.5–9 | every motion encodes a relation; nothing smears | 4 fps strips show glyphs dragged across neighbouring text: the r value flown into the touch dot crosses "r =" (1:16.8–1:17.3); Anscombe's s_x / r / s_y symbols leave the readout across "0.82" and "2.03" (2:53.6–2:56.0); the substitution and landing fractions sit empty ("= ——", "slope = ——") for about 0.5 s before their values arrive (3:01.3, 3:17.8; round-4 craft 7) | touch dots grow out of the centre-line ends instead of a glyph-to-dot morph (r is flagged on "correlation" and its live label takes over in the sweep); symbol copies lift straight up out of the readout before travelling (constant offsets per mobject, so each glyph stays legible); fraction bars grow with the first value's flight; at the landing each symbol fades only as its value arrives |
| Hook 8.5 / Clarity 9 / Audio 9 / Concision 8.5–9 / Originality 9 | — | no new defect found in narration, sync or facts; WER 4 %, every deictic lands within 0.3 s, 0 banned phrases | narration unchanged, so the verified sync and every fact in facts.md stay valid |

### What changed

Narration, timing of every beat, and every number on screen are unchanged (facts.md needs no
edit). All changes are to motion and layout, found by 4 fps frame strips across every transform.

**Glyphs no longer smear in flight (§11.6).** The root cause, found in full-resolution crops, was
structural: a value or symbol that is one *part* of a readout entry (`MathTex(sym, "=", val)[2]`)
was transformed into a *whole* `MathTex`, which has one more level of nesting. Manim then pairs
the glyphs badly and the digits merge mid-flight ("0.82" read as "0⁂"; "3.32" as "33ꞩ"). Every
flight now uses a copy with the same structure as its target, so each glyph maps onto itself, and
leaves its row along a path that rises straight out of the table before travelling (`lift_path`),
so it never drags across "r =" or a neighbouring value.
- 1:16 "picks one": the r value no longer morphs into the touch dot across the "r =" glyphs. The
  ellipse is drawn starting at its right touch point; each touch dot appears as the stroke reaches
  its wall.
- 1:04 "single point": 54.26 and 47.83 travel intact (on opaque patches) one after the other to
  the corner beside the centre dot and settle into it, instead of eight glyphs morphing into a dot.
- 1:09 "reach": 16.76 and 26.93 travel one after the other (their straight paths cross; in the old
  cut the two numbers overprinted at 1:09.0).
- 2:48 "touches": Anscombe's 0.82 rises out of its row, then travels left, intact, into the touch dot.
- 2:53–2:56: s_x, r and s_y rise out of the readout and travel to label the run and the rise.
  They are flagged one at a time; the old group Indicate scaled the pair about their common centre
  and pushed s_y into its "=" ("s_ȳ 2.03" on the 2:55 contact-sheet frame).
- 3:01–3:03: 0.82, 2.03 and 3.32 rise out of the readout and fly to the substitution intact.

**No empty templates.** The substitution's fraction bar grows with the first value's flight (it
used to sit as "= ——" for about 0.4 s). At the landing, "r s_y" and "s_x" fade only as the
dinosaur's values arrive, so "slope = ——" never shows empty.

**One label per object (B9).** The live "r = 0.80" label steps up to the box's top-right corner
on "touch point", before "r s_y" is written beside the rise, and rides there through the sweep back
to −0.06. The two yellow labels no longer stack on the rise (round-4 craft 6).

**Indicate effects stay inside their own space.** "these five numbers" (2:12) is a yellow box
round the five rows (as for Anscombe's readout at 3:05) instead of a 1.08 scale flash that pushed
each value into its "="; the r-row flag at 1:37 flags −0.06 and −0.06 separately.

**Focal point.**
- Prediction hold (1:45–1:48): the star dims to 40 % with the boxes gone, so the two ellipses and
  centres carry the question; it returns to full strength during "Slide" (round-4 substance 7).
- Landing squeeze (3:27–3:33): the best-fit line steps back to 30 % and the ellipse to 60 % while
  a full-strength copy of the ellipse is squeezed into the ±s_y error bar, so the squeezed copy,
  the bar and the error bar are the only full-strength strokes where they meet (round-4 craft 4).
  Both return to full strength on "dinosaur".

### Continuation (after the interrupted pass)

The pass above was cut off twice: after its first plan, and again after a 13:31 master (3:33.0)
whose fixes were never logged. This continuation picks up from those files, logs what that pass
changed, audits its master as a fresh critic would, and fixes what that audit found.

**Logged from the interrupted pass (already in scene.py, script.md and facts.md):**
- *Concision, 536 → 494 words (3:35.5 → 3:33).* Two retellings were cut. The first was the
  one-point nudge-and-undo demonstration and its two sentences: the star fix had already proved
  "hold the five". The second was "Plug in his numbers, and it's one half", with its Anscombe
  substitution: the landing plugs in the dinosaur's numbers, which is the one substitution the
  story needs. facts.md #12, #18, #27 and #28 record the cuts.
- *Audio.* There are planned pauses after the key results ("lost all five numbers" 0.9 s,
  "everything the five numbers know" 1.0 s, "every decimal place" 0.6 s). "For minus point oh
  six" became "For the dinosaur", so the cold open's phrase is no longer repeated. The roll call
  starts on "this circle". "So the slope is rise, over run" is spoken at 0.82, so no sentence runs
  above 200 wpm.
- *Motion.* "(x̄, ȳ)" is flown as one label: copies of the x̄ and ȳ symbols leave the table's
  left-most column, so nothing crosses a value. This fixes the 1:08.2 clearance warning. Anscombe's
  0.82 now marks the touch height until "high up", which clears the 4.0 s static stretch at
  2:47.6. At the landing, s_y and s_x travel in a true elbow lane (sideways, down, sideways), and
  their sources are fully hidden while the copies leave. In the 13:31 master the 16.76 copy
  overprinted its own row ("16.7616.76" at 3:15).
- *Cadence.* Beat gaps are 0.66 s where they were 0.46–0.51 s. The review kit had flagged
  "metronomic" (full stops 0.51 s, beat turns 0.64 s, needed ≥ 0.66 s).

**Found in the audit and fixed now:**
- *Landing (3:13–3:24), Visual.* "slope =" started 35 px right of the plot's axis name "x", so
  the frame read as one expression, "x slope =". This was the round-1 "x  med y" defect again.
  The formula is now label size 36 and moved 0.5 right. Its left edge sits 0.78 units from "x",
  which is asserted in scene.py, and the substituted form ends at the safe margin.
- *Final image (3:31–3:33), Visual.* The parked bar and error bar had no tag once "86% used bars"
  faded. The tag now fades out at the top left and back in over the parked error bar, so the last
  frame reads as 142 points beside "86% used bars", one bar and one error bar, with the citation
  still on screen. It never crosses the returning points.
- *Anscombe beat (2:41–2:58), Visual and composition.* His readout sat level with his touch
  point, so the lower-right quadrant stayed empty for about 16 s. BAR §13.1 allows at most 4 s.
  The two rows now straddle his centre line. The 0.82 rises out of its row and travels up and
  left, intact, to the touch dot. The s_x, r and s_y copies still cross above the box, on the same
  route as before. The readout's later step down to make room for the formula ends where it did.
- Re-checked and left as they are: "one" is held 0.62 s in "Version one" (TTS variants gave
  0.50–0.59 s; it is a stressed name, not a function word); the commit ends at 0:12.9; the landing
  is four sentences.

Narration, beat order and every number on screen are unchanged by this continuation, so
facts.md needs no edit. No critic claimed a factual error in round 5.

### Verification (final master, 3:34.5)
- render.sh reported 0 scene warnings. The layout audit found 0 issues in 235 checks, and
  review_kit raised 0 flags; the round-5 cadence flag ("metronomic") is gone.
- Words and timing: 494 words, 150 wpm over speech time, no sentence above 200 wpm.
- Loudness: −14.0 LUFS integrated, −1.6 dBTP true peak.
- Silence: the longest is 2.09 s, the commit hold. Leading silence is 0.00 s and trailing 1.92 s.
- The longest fully static stretch is 3.40 s.
- Cadence: full stops median 0.51 s, beat turns 0.68 s.
- WER 3.7 %; 12 deictics, all synced.
- I looked at all 12 contact sheets and at keyframes kf_29 (2:52.2), kf_34 (3:15.7), kf_35
  (3:21.7) and kf_39 (3:32.7).
- I also checked frame strips at 4–7.5 fps across every moved or changed transform:
  - the landing value flights (3:16.0–3:18.4): every number stays legible and nothing
    overprints, where the 13:31 master printed "16.7616.76";
  - the landing hand-off (3:12.3–3:13.7);
  - the "(x̄, ȳ)" flight (1:07.3–1:08.7);
  - the 0.82 flight to the touch dot (2:47.5–2:48.5);
  - the s_x, r and s_y flights to the run and the rise (2:53–2:56).
- The SD-symbol flights (1:12.2–1:13.8, unchanged code) were checked on the 13:31 master.
- Runtime rose from 3:33.0 to 3:34.5 because of the longer beat-turn gaps. It stays inside the
  3:15–3:35 budget.

## Round 6 revisions

Both critics scored 8.5 (no caps, no factual errors) and said every fix is local. Plan, per
dimension below 9 (BAR §3 "9" anchor → where it fell short → upgrade):

- **Hook (8.5/8.5).** Anchor: "viewer commits to a likely-wrong prediction by 0:12". Short: the
  first frame was empty axes with blank slots, the commit landed at 0:12.9, and it asked only
  about the tilt (the half the viewer gets right). Upgrade: all five values and a faint "?" are
  on screen at frame 0; one question asks both halves, "What shape is the cloud, and which way
  does its best-fit line tilt?", ending at 0:10.4 with a 1.8 s hold; three grey candidate lines
  (up, nearly flat, down) through (x̄, ȳ) are drawn as it is asked, and in B1 two fade and the
  nearly flat one becomes "your line".
- **Clarity (8.5/8.5).** Anchor: "viewer could re-derive it after one watch". Short: B9 packed
  six moves into 22–25 s and only asserted "on average r SDs up"; "Correlation" was swallowed.
  Upgrade: B9 is split. B9a: "Many ellipses touch all four walls. The correlation, r, picks one."
  B9b: "Say r is point eight. Go one standard deviation right. On average, the cloud rises r
  times a standard deviation." over a simulated r = 0.80 cloud (tagged "simulated"), whose 12 points in
  the slice at the wall are singled out and averaged: their mean lands on the top of the rise.
  Holds of 0.7 s after the run and rise and after the slices' midpoints; "the slices shrink to the
  touch point". Also "keeping the box" for the tip (a pure shear would break s_y) and "Your line
  was right: five numbers fix it exactly".
- **Visual (8.5/8.5).** Anchor: "every frame has one focal point; nothing to remove". Short: an
  occluded error bar (0:35), a lone ellipse in an empty frame (3:13.4), the bar crossing the "x"
  label (3:30.9), a citation under the wrong dataset (2:40.6), the what-if in the dinosaur's
  solid yellow, doubled glyphs as copies left their sources, a final frame with no focal point.
  Upgrade: each fixed (list below).
- **Motion (8.5/9).** Anchor: "every motion encodes a relation". Short: two fade joins (Anscombe
  entry, landing hand-off). Upgrade: panel I's axes transform into the opening's axes around the
  growing ellipse; Anscombe's ticks hand over before his readout lands.
- **Audio (8.5/8).** Anchor: "pauses are intentional; each deictic lands". Short: 12.4 s without a
  breath, "1sx / rsy / overrun", "one" held 0.62 s. Upgrade: pauses in B9, B2, B16, B22; "ess ex
  across, r times ess why up" at 0.82 (no "one" before "ess ex"); "the rise over the run";
  "The first version".
- **Concision (8/8).** Anchor: "cutting any sentence loses something". Short: the Anscombe block
  re-made the Dozen's point and re-taught B9's rule over 23 s. Upgrade: B19 cut, B18 and B20
  shortened to one sentence each; 494 → 471 words (3:34.5 → 3:29.1).

**Fixes, as applied (craft = C, substance = S):**
1. *Hook (C3, S1).* As above. The "?" now sits in the upper half of the plot and "n = 142" in the
   lower half, so the candidate lines never cross either (asserted in scene.py).
2. *B9 (C1, S2, S4, S10, C9).* As above. The what-if geometry (ellipse, touch dots, run, rise,
   dashed line, slices and midpoints) is drawn at 60 % and returns to full strength as r sweeps
   back on "For the dinosaur"; the live "r = …" sits under the "simulated" tag at the top left
   of the plot, where the r = 0.80 cloud never goes. The simulated cloud is uniform inside the
   2-SD ellipse with exactly the dinosaur's means and SDs and r = 0.80 (seed 10371; facts #36):
   its least-squares line is the dashed line, and the 12 slice points average 69.41 against the
   touch point's 69.38.
3. *Anscombe (C2, C7, S3, S5).* "Francis Anscombe made the same point in 1973, with eleven
   points. [pause 1.2]" (his 0.82 flies to the touch dot in the pause) · "Same rule: ess ex
   across, [pause 0.3] r times ess why up." · "So the slope is the rise [pause 0.3] over the
   run." The three label flights, the line grown on "up" and the formula built from the segments
   are kept.
4. *Error bar (C4).* The strip dims to 30 % with the bar, the bar's fill is 12 % (z under the
   error bar), the error bar has stroke 5 and is drawn on top.
5. *Hand-off (C5).* Panel I's axis lines and ticks ReplacementTransform into the 0–100 axes, its
   "y" travels to the big "y", its ellipse grows into the dinosaur's; the tick numbers hand over
   (old out, then new in: TransformMatchingTex would morph "10" into "25", which BAR treats as
   glyph soup); only the guess cloud, its labels and the readout fade in.
6. *Parked bar (C6).* It fades out in place (0.4 s) and fades in at the parked spot (0.4 s); it no
   longer slides across the cloud or the "x" label.
7. *Anscombe entry (C8).* Ticks hand over in the first 42 % of the move, his readout lands after
   them, and his citation fades in only as his points settle.
8. *"Version one" (C10).* "The first version" (and "replay the first version").
9. *Doubled glyphs (S9).* Every symbol copy that leaves a table glyph (x̄, ȳ, s_x, s_y in B7–B8;
   0.82, s_x, r, s_y in B18–B20; the rise and run labels in B21) now dims its source to 20 % over
   the first 5 % of the flight and restores it once the copy is clear (10 fps strip at 1:10.9:
   one frame shows the bright copy beside a faint source, the next shows them apart).
10. *Final frame (S8).* On "dinosaur" the ellipse and the line step back (60 %, stroke 4.5 → 2.5)
    while the points return at full strength, so the last frame is one blue dinosaur beside one
    60 % bar. A first master used 40 % as asked (35 %); that yellow read as olive (the hue slip
    PRODUCTION_GUIDE §13.2.8 warns of), so the step back is a thinner stroke at 60 % instead.
11. *Breath (S10).* B2 gets [pause 0.4] after "bar graphs:", B16 is split into two sentences with
    [pause 0.4], B22's mid pause is 0.5 s.

**Not changed, with reasons.**
- The fix lists conflicted on the hook: craft asked for a tilt question with candidate lines,
  substance for a shape commit with no tilt question. The one-question form asks both halves
  ("What shape is the cloud, and which way does its best-fit line tilt?"), so the likely-wrong
  shape is staked, the candidate lines make the tilt choice visible, and the landing ("Your line
  was right … Your cloud was wrong") answers both.
- Craft fix 5 asked for TransformMatchingTex between the tick labels. "0, 10, 20" and "0, 25, 50,
  75, 100" are different strings, so that would be a glyph morph (BAR §5, PRODUCTION_GUIDE
  §13.2.6). The axis lines and ticks transform, the "y" travels, and the numbers hand over old-out
  then new-in.
- Craft fix 7 asked for "one ess ex across, r times ess why up" at speed 0.78. With "one" in front,
  whisper still fused the words into "1sx" at both 0.78 and 0.82 (tested on the clip). "ess ex
  across, r times ess why up" at 0.82 is heard as "SX across, R times SY up". 0.78 is below the
  guide's 0.80 floor.
- "r standard deviations" was heard as "our standard deviations" in the full mix, so B9b says
  "rises r times a standard deviation" (heard "R times a standard deviation").
- The 1.8 s commit hold makes the longest internal silence 2.37 s (0:10.3–0:12.7). It is a planned
  prediction pause, under the 2.5 s limit.
- The Anscombe readout fades in at 2:43.3, after his axes are numbered. That leaves the right half
  empty for about 2.8 s while his points travel, which is under the 4 s limit.

**Facts.** Neither critic claimed a factual error. New material is recorded in facts.md #36 (the
simulated r = 0.80 cloud: seed, its exact five numbers, its least-squares line through the touch
point at 69.381, and its 12 slice points averaging 69.409) and #37 (wording changes; the pure-shear
check that a shear alone would push s_y to 26.99, verified with numpy).

### Verification (final master, 3:29.1)
- render.sh: 0 scene warnings. The layout audit found 0 issues in 227 checks, and review_kit
  raised 0 flags. A first master printed one cue warning: "times" now occurs twice in B9b, so the
  cue was moved to the second occurrence.
- 471 words. Pace is 152 wpm over speech time, and no sentence runs above 200 wpm; "Then tip it,
  keeping the box" ran at 200 until a 0.2 s pause was added. The longest stretch without a breath
  is 6.7 s, down from 12.4 s. Full stops have a median gap of 0.52 s and beat turns 0.69 s.
- Loudness: −14.2 LUFS, −4.1 dBTP. Leading silence 0.00 s, trailing 1.94 s. The longest static
  stretch is 2.77 s.
- WER 2.6 %. The transcript reads "What shape is the cloud, and which way does its best fit line
  tilt?" (ends 0:10.5), "the cloud rises R times a standard deviation", "Same rule, SX across, R
  times SY up", "So the slope is the rise, over the run" and "Your line was right". All 12 deictics
  are synced.
- I looked at all 12 contact sheets and at keyframes kf_39 (final frame) and kf_01. I checked frame
  strips at 5–10 fps across:
  - the cold-open candidate lines (0:08–0:17);
  - the simulated slice and its average (1:27.8, 1:29.4, full resolution);
  - the s_x flight out of the table (1:10.85–1:11.45);
  - the Anscombe entry, where the ticks hand over before the readout and the citation lands at
    2:44.5;
  - the landing hand-off (3:06.9–3:08.5), where the axes grow around the ellipse and the formula
    comes down the open middle;
  - the bar parking (3:24.5–3:26.1), where the bar fades in place and reappears beside the plot
    without touching "x".

## Round 7 revisions

Round 7 scored 8.7 from both critics (craft: Clarity, Visual, Motion, Concision 8.5; substance:
Clarity, Visual, Audio, Concision 8.5). No caps, no factual errors. Both said the fixes would
reach 9.

### Plan of the climb (written before editing)
- **Clarity (8.5/8.5).** Anchor: "viewer could re-derive it after one watch". Short: the central
  step at 1:21–1:42 said "rises r times a standard deviation" (which one?), the rise sat on the
  box wall with no label until 1:38.8, the averaged slice point landed on a touch dot drawn at
  1:21, the "now" column showed r = −0.06 with a bright "=" next to a cloud tagged r = 0.80, and
  "the middle of every vertical slice" was true only of the ellipse's chords. Upgrade: say "r
  times ess why" while the label r s_y is built beside the rise; hide the touch dots so the slice
  average lands as a new dot that becomes the touch dot; dim the dinosaur's live column to 25 %;
  "every slice of the ellipse".
- **Visual (8.5/8.5).** Anchor: "every frame has one focal point". Short: wall, rise, band and
  touch dot in one 20 px column; the s_x plate clipping dots into half-moons; a knot of strokes at
  r = −0.06 (kf_17); the bar under full-strength dots at 0:35 (kf_07); an 8-element last frame.
  Upgrade: the rise moves 0.15 right of the wall and the box steps back; no plates, the simulated
  cloud leaves the label spots bare; run, rise and label leave on the sweep back; the bar leaves on
  "Only thirteen percent"; the three rows a bar cannot draw step back at the end.
- **Motion (8.5/9).** Anchor: "every motion encodes a relation". Short: tick numbers and readout
  fade out before the new ones arrive (2:41.5–2:44.5); the readout jump at 2:52.9; a tickless
  hand-off frame (3:07.6). Upgrade: tick numbers cross-fade in place; the readout builds in its
  final slot while the dinosaur's rows step back; the 0–100 numbers ride their ticks during the
  hand-off.
- **Audio (9/8.5).** Short: 6.7 s without a breath in B9b. Upgrade: [pause 0.4] after "Go one
  standard deviation right." and B9b at speed 0.80.
- **Concision (8.5/8.5).** Short: "so they share the ellipse and line", "reach one deviation out",
  the repeated "r times ess why above the center". Upgrade: cut all three.

### What changed (craft = C, substance = S)
1. *B9b, the one hard step (C1, C2, C3, C7, S1, S2, S3, S4).* New narration: "Say r is point
   five. Go one standard deviation right. [pause 0.4] On average, the cloud rises r times ess why.
   [pause 0.7] That's the best-fit line, through the middle of every slice of the ellipse.
   [pause 0.7] At the wall, the slices shrink to the touch point. [pause 0.4] For the dinosaur,
   it's just below the middle." (speed 0.80).
   - On "Say": the dinosaur's "now" column, all five = marks, "matching 5/5" and its own r row
     step back to 25 % (green and yellow go grey first, so nothing reads olive); the yellow
     "r = 0.50" is the only live r. The SD box steps back to a 40 % grey and both touch dots go.
   - The run is labelled s_x under its left third, with no backing plate; the label stays until
     the slices start.
   - The rise stands 0.15 right of the wall (stroke 6) as a dimension, with thin ticks back to the
     wall at ȳ and at the touch height. "r s_y" is built beside it on "r times ess why": its r
     flies from "r = 0.50", its s_y from the readout (each source dips while its copy leaves).
   - The 14 slice points' copies merge into one new white dot at their average (61.27 vs 61.30),
     which turns yellow and becomes the touch dot; the left touch dot appears as the dashed line
     reaches it.
   - "At the wall": the box returns to full strength as the slices collapse; the touch dot and
     "r s_y" flag on "touch point".
   - "For the dinosaur": the run, the rise and its label fade as r sweeps back; only the dashed
     line, the centre and the two touch dots remain, and the touch dot flags on "middle".
   - **r = 0.50 instead of 0.80, and why.** With the plate removed, the s_x label has to keep
     0.15 clear of the ellipse, the dashed line, the run and the centre dot. A grid search over
     label positions found no such spot within ~0.3 units of the run at r = 0.80 (the thin ellipse
     and steep line cut through every candidate); at r = 0.50 there is one under the run's left
     third. The simulated cloud draws again any point that would land under the three labels or
     outside the plot (2 of 142 for seed 13458; facts #36). Bonus: at r = 0.50 the touch point is
     visibly halfway up the half-box.
2. *Stakes (C4, S8).* A grey "± 1 SD" tag beside the error bar's top cap (most reviewed bar
   graphs drew ± SE). On "Only thirteen percent" the bar, error bar, tag and "86%" fade to 0 and
   the strip alone carries "13% showed points"; they return at the landing.
3. *Anscombe entry (C5, C6).* The median row leaves first. Old and new tick numbers cross-fade in
   place over the same 0.8 s (the one shared spot, x 75 / 12, hands over in sequence). The
   dinosaur's rows step back to 30 % and drift up while his readout builds entry by entry in its
   final bottom-right slot; it never moves again (the B20 copies now rise straight out of it).
4. *B22 (C8, S5).* "All four of his datasets share these five numbers." The quartet forms on "All
   four", the ellipse and line copies start on "share", the readout is boxed on "these".
5. *Hand-off (C9).* Each 0–100 tick number rides its own spot on the growing axes and fades in
   during the transform (window 0.22–0.6 of the 1.5 s), so no tickless frame remains.
6. *B8 (S6).* "The two standard deviations reach out on each side, and draw a box."
7. *Landing (S7, S8).* On "only" the x̄, s_x and r rows step back to a 30 % grey, so ȳ and s_y
   are the two bright rows on "two" and through the end card; the parked bar carries "± 1 SD"
   beside its top cap.
8. *Sync.* "Here are the real points": the reveal now starts 0.25 s before "real" (the deictic
   check had it at +0.46 s).

**Not changed, with reasons.**
- Substance fix 9 (retitle) was marked optional; the title is fixed in curriculum.json, and the
  commit asks for a shape and a tilt, not for "dinosaur".
- "r times ess why" now occurs in B9b and in B20 ("Same rule: ess ex across, r times ess why
  up"). The second is a deliberate callback, introduced by "Same rule".
- Craft fix 7 asked for the s_x label "0.2 below the midpoint of the run". At r = 0.50 that spot
  is 0.06 from the ellipse; the label sits under the run's left third instead (≥ 0.15 from every
  stroke, asserted).
- With the readout in its final bottom-right slot, the upper right is empty from about 2:41 until
  "slope =" at 2:50.5; the action in those 9 s is in the plot and the flights out of the readout.

**Facts.** Neither critic claimed a factual error. facts.md #36 is rewritten for the r = 0.50
cloud (seed, redraw rule, exact five numbers, least-squares line through the touch point at
61.300, slice average 61.27, and the label-clearance search that ruled out 0.80); #26 gains the
r = 0.50 slice numbers; #38 records the wording changes and the ± SE / ± SD figures (77.6 % /
15.3 %) behind the new tag.
