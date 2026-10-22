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
