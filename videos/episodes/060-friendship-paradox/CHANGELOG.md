# Episode 60 — changelog

## Round 1 revisions

Round 1 scored 8.2 (craft) and 8.1 (substance), with no caps and no factual errors. Every fix from both reviews is applied; the three "keep" items are kept: the token counter 32/16 → 60/20 with the bar overshooting the guess, the token beam with its 2.5 and 3 fulcra, and the redrawn C&F curves with the self-report caveat.

**Insight, from the picture to the formula (both critics' fix 1, substance fixes 2 and 6)**
- The divide step is now three real rows: Σk²÷8 / Σk÷8 = 60÷8 / 20÷8 → k̄²/μ = 7.5/2.5. The BLUE 2.5 flashes with the BLUE fulcrum.
- The variance is drawn under the beam:
  - a PURPLE distance line runs from the BLUE fulcrum to each column (1.5, 0.5, 0.5, 1.5);
  - each distance grows into a PURPLE square under each girl, labelled 2.25 or 0.25;
  - the eight labels travel into the PURPLE row σ² = 10/8 = 1.25.
- The numerators are rebuilt from their referents: the BLUE denominators rise into μ² and 2.5², and σ² and 1.25 drop in from the variance row, giving (μ²+σ²)/μ = (2.5²+1.25)/2.5 = 3.0.
- The split, the INK-boxed cancel of μ²/μ, then 2.5²/2.5 → 2.5 and 1.25/2.5 → 0.5 replace the TransformMatchingShapes glyph soup. Changed content crossfades; nothing morphs into garbage.
- The beam is raised to y = 0.3, so the stacks fill the upper left (craft fix 8).

**Colour semantics (craft fix 4)**
- The average-friend bar is a YELLOW outline (the total), filled BLUE up to μ (the guess fills exactly the dashed box) and PURPLE beyond it. Facebook uses the same scheme: 190 BLUE + 445 PURPLE = 635 YELLOW.

**Hook (craft fixes 6 and 7, substance fix 5)**
- Frame 0 shows the network at 70 %, and the edges draw in.
- The narration is trimmed ("Eight girls at an Illinois high school…", "Does the average friend have more, fewer, or the same?"). The prediction hold now starts at 12.0 s instead of 15.8 s.
- The "?" moves in 0.5 s steps keyed to "more" (10.06 s), "fewer" (10.68 s) and "same" (11.48 s).

**Payoff (craft fixes 2 and 3, substance fix 4)**
- A mechanism sentence is added, sourced to C&F's Fig. 1 rationale: "More friends means more ways to catch flu, so the friends should get sick first."
- There is no hard reset at 2:28. The axes build while the two Facebook bars shrink into the chart's empty corner, then turn into "319 random students" and "425 friends they named" as each is spoken. The calendar starts on "sick first".
- The 13.9-day arrow no longer sits on the raw steps at a chosen height. Dashed cumulative-logistic fits are drawn with a shared shape, shifted by the published 13.9 days and refit to the redrawn data in sim.py. A free fit of the shift gives 14.5 days, inside the 95 % CI. The raw steps dim, and the arrow sits between the fits at 2.8 %.

**Landing (craft fixes 5 and 12, substance fixes 3 and 10)**
- Each of the five girls gets an INK outline and her friends' average in YELLOW (4, 3.5, 3.33, 3.33, 2), with the key "her friends' average".
- On "only Sue", those dim to 30 %. Sue, then Alice, get thick outlines with 2.75 and 3. The critic's suggested 2.5 and 3.25 were wrong; the values were recomputed and logged in facts.md.
- New closing line: "Sue is on four friend lists, Betty on one. Follow any friendship, yours included, and you land on a Sue four times as often as on a Betty." The tokens pile onto Sue and Betty to match.
- The chart dissolves straight into the network, with no empty frame.

**Smaller fixes**
- Network tokens are numbered squares that show the count they read as they land (substance fix 8). The mechanic is now introduced on the ring, where every token reads 2.
- The ring is tagged "(hypothetical)", and the Feld/Coleman citation dims to 25 % while it is on screen (substance fix 7).
- Citations swap sequentially, out then in, never crossfaded (craft fix 11, substance fix 9).
- Text-grade gray is #9EA5AF (7.3:1) for names, ticks, axis titles and citations (substance fix 11).
- The "guess" label is size 26, left-aligned inside the box (craft fix 9). The box grows along the friend row instead of a ghost bar crossing the "average friend" label.
- The fulcrum values no longer fly across the bars (craft fix 10). Each fulcrum appears with a flash of its bar value.
- The bar panel dims to 35 % during the variance and algebra steps (1:51–2:18), so the squares and the equation rows are the only focus. It returns on "the extra half friend we measured", when the PURPLE segment flashes with the 0.5.
- No glyph morphing anywhere. Same-content terms slide into place and are swapped. Changed content (count labels, the divide rows, the ring line, Facebook relabels) crossfades or fades out then in. Stage C of the equation holds about 2.5 s before it splits.
- Verified on the master: 3:39.6, 150 wpm, −14.0 LUFS / −2.1 dBTP, longest static 3.57 s, longest silence 2.09 s (the prediction holds), WER 1.6 %, 0 flags, 0 render warnings.
- Runtime is 3:39. script.md, facts.md and sim.py (variance check, logistic refit) are updated.

## Round 2 revisions

Round 2 scored 7.0 / 7.0 (weighted 8.2 craft, 8.0 substance), capped at 7 by one held overlap: the
"4" token at Sue's end of the Sue–Dale edge covered the "e" of her name. No factual errors. Both
critics: "reaches 9 if fixed: yes, no structural change". All 24 fix items are applied; the three
"keep" items (the token beam with exact fulcra, the YELLOW-outline / BLUE / PURPLE friend bar
reused for Facebook, the redrawn C&F curves with shared-shape fits and the self-report caveat) are
kept.

**Plan of the climb (written before editing, BAR §3 "9" anchors)**
- Visual 7.5 → 9 ("every frame has one focal point; all §5 standards met"): remove the cap with an
  automated clearance assert; give Facebook and the closing frame one focal point; square sides
  that match the drawn distances.
- Clarity 8–8.5 → 9 ("viewer could re-derive it after one watch"): show *why* avg(k²) = μ² + σ²
  on the beam (the cross terms cancel because the beam balances); avg(k²) notation; precise "20 %"
  and Facebook question.
- Motion 8 → 9 ("every motion encodes a relation"): no crossfaded glyphs anywhere; the lead
  visibly shrinks; bars become curves.
- Hook 8 → 9 ("commits to a likely-wrong prediction by 0:12"): ask for a number, not a direction.
- Audio 8 → 9: shorter sentence gaps inside beats, longer ones at section boundaries.
- Concision 8–8.5 → 9: cut the ring's throat-clearing and the slack C&F sentence; trim words.

**Cap removed (both critics' fix 1)**
- `assert_token_clearance()` runs before every render (and `python scene.py` runs it alone). It
  checks every parked token position on both layouts against every name label (≥ 0.15 units),
  node (≥ 0.05), other token (≥ 0.04) and every foreign edge. Against the round-2 label placement
  it reports "token Dale->Sue is 0.000 from label 'Sue'".
- Sue's label sits up-left of her node; Carol's moved below hers (the bigger tokens would have
  come within 0.013 of it on the left).
- A per-beat audit (`Episode.audit`) logs any text within 0.12 units of other text or of a small
  shape into narration.json; the final render has none.

**Why avg(k²) = μ² + σ² (craft 2, substance 2): a new ~20 s beat**
- "Split Sue's four into the balance point, two and a half, plus her distance, one and a half."
  4² = (2.5 + 1.5)², with 4 copied from Sue's node and 1.5 from her distance label.
- "Squaring gives …" → 4² = 2.5² + 1.5² + 2·2.5·1.5. The brackets leave and the shared glyphs slide; the cross
  term rises in place while its 2.5 and 1.5 flash in their colours. The cross term is INK-boxed.
- "Every girl splits this way" (all eight nodes flash) → avg(k²) = μ² + σ² + 2μ·avg(d).
- "Because the beam balances, the left and right distances add to zero": the distance labels become
  −1.5, −0.5, +0.5, +1.5, the left then right arms flash, a PURPLE 0 appears under the balance
  point, avg(d) → 0, the boxed term leaves → avg(k²) = μ² + σ².
- The main row's numerators are then rebuilt from that identity: (μ² + σ²)/μ copied down, 2.5²
  from the BLUE denominator, 1.25 from the variance row.
- The main row dims to 35 % while the split row works, so the frame has one focal point.

**Other clarity fixes**
- "\overline{k^2}" → `avg(k²)` everywhere (substance 4).
- "off by twenty percent" → "friends average twenty percent more than girls" (substance 3).
- Facebook question → "If every friendship sent tokens, what would the tokens average?" This is
  exactly Ugander's ⟨k²⟩/⟨k⟩ = 635 (substance 9).
- Squares are drawn at exactly ¼ of the beam scale. Each girl's distance segment drops to her
  square's top edge, visibly shrinking, before the square grows down from it, and a tag says
  "squares at ¼ scale" (craft 3, substance 5).

**Hook (craft 9, substance 8)**
- "How many friends does the average friend have?" The "?" stops under three candidates: 2.5 (a
  dashed line from the girl bar), 3 and 4 (ghost drop lines above the axis ticks). The 1.6 s hold
  follows, and the fail beat pays off a number (3.0, +20 %).

**Facebook (craft 5)**
- On the first words the beam and the algebra leave. The bar panel scales 1.25× into the centre,
  and μ + σ²/μ slides beneath it.
- The row becomes μ + σ²/μ = 190 + 445 = 635, with each number copied from its bar label.

**Christakis & Fowler (craft 4 and 7, substance 6 and 10)**
- The two Facebook bars park ABOVE the plot frame as a 60 % legend ("average user",
  "average friend"), never inside the data area.
- On "sick first" each bar flies into the origin, and its step curve grows out of it on the shared
  calendar.
- The arrow between the fits is copied up into a read-out above the plot, with "fitted lead: 13.9
  days" beside it.
- On "self-reported" a GRAY copy drops to the row below with its label. On "shrank" it shrinks,
  tip fixed, to 3.2 days at the same day scale.
- "319 random students" moved right, clear of the blue fit.

**Landing (craft 8, substance 11)**
- After the tokens fly, every token except Sue's four and Betty's one dims to 30 %.
- A tally builds in the empty right panel: "Sue ■■■■ 4×" on "a Sue", "Betty ■ 1×" on "a Betty".
  As tags beside the nodes they read as labels of the wrong girl, so they moved.
- New close: "So Betty looks at her one friend and sees four. From most seats in this class, the
  view is the same." Betty's node takes a thick INK outline and Sue's 4 pulses. On "most seats",
  Jane, Pam, Dale and Tina take the same outline: the five seats from which friends look more
  popular.

**Motion (craft 6, substance 7)**
- No crossfade of different glyphs anywhere. Changed terms leave upward (0.35 s), then the new
  term rises in (0.45 s); shared glyphs slide.
- Node counts ride with their nodes and swap 4 → 2 → 4 without overlap.
- Cancellations: the box, the square and the denominator leave, and μ slides into place.
- The dashed guess box stretches instead of morphing its dashes.
- The stakes and landing highlights are thick node outlines, not rings that crowded the name labels.

**Concision and audio (craft 10, substance 12 and 13)**
- Cut "And in an easy case, the guess holds." The ring's 16 tokens fly in 2.5 s (lag 0.04).
- Cut "The steps are flu diagnoses by medical staff." ("flu diagnoses" now rides in the sample
  sentence).
- Trimmed words across the script.
- Sentence gaps inside a beat are 0.26 s (series default 0.38 s). Section boundaries (after
  stakes, the ring, the fail, the result, Facebook, C&F) get 0.7 s. Voice speed 0.82.

**Visual details (craft 11)**
- Network tokens are 0.30 units with digits at 30. Tokens on short edges keep to a right-hand lane.
- The fulcrum labels sit 0.15 below the beam. The distance line moved down to make room.
- The C/D equation rows share one size, chosen so D1 clears the citation and the frame edge.
- The "average friend" label sits 0.05 higher, clear of the dashed guess box.

**Facts**
- Re-checked the one sourcing note (Coleman's school count): ten northern-Illinois schools
  (PEP review; Brookings 2017). The narration's "an Illinois high school" is true either way.
- Every new number (4² = 6.25 + 2.25 + 7.5, signed distances summing to 0, ¼ scale, the read-out
  arrow lengths, Betty's view) is logged in facts.md "Round 2 additions".

**Found while verifying the master (fixed before hand-off)**
- The toolkit's frame-level layout audit found 15 items on the first master; the final master has
  0 in 197 checks. Fixes:
  - wider C/D rows (row buff 0.24, one shared scale, allowed to use the empty space above the
    citation) with tight cancel boxes;
  - the split row moved up to -1.15;
  - μ² as one TeX part in the split and C rows;
  - "+445" 0.2 above its bar;
  - the closing frame's dimmed tokens are an opaque dark yellow, so edges no longer show through
    their digits;
  - tokens sit 0.11 from their node.
- Whisper heard "signed distances" as "sine distances", so the line now says "the left and right
  distances add to zero", which matches the left-arm and right-arm flashes.
- The Facebook question had a 4.2 s static stretch. The "?" now arrives on "every friendship".
- The ring counter no longer counts down through "31/15 = 2.0" on the way back: its digits fade as
  a whole.
- The cross term rises in place while its factors flash, instead of copies sliding across
  "+ 1.5²".
- The legend labels leave before the Facebook bars fly to the curves' origin.

**Mechanics (final master, review/report.md)**
- 3:37.2; 159 wpm on speech time; -14.0 LUFS / -2.1 dBTP.
- Longest silence 2.08 s (the planned prediction holds); longest static 3.43 s.
- WER 0.9 %; 0 banned phrases; 0 render warnings; 0 layout-audit issues; no flags.

## Round 3 revisions (critics: craft 8.4, substance 8.4; no caps, no factual errors)

**Plan (BAR §3 "9" anchors vs. where round 3 fell short)**
- Visual 8 → 9 ("every frame has one focal point"): the insight frame carried nine groups (kf_25).
  Upgrade: the token stacks, Sue's box and "4×4=16" leave on "Split", the old main row leaves until
  it is rebuilt, the area labels fly away themselves, the variance and identity rows leave once
  used, and the bar panel sits at 25 %. Fix the 7 px legend gap by removing the legend.
- Clarity 8.5 → 9 ("could re-derive it after one watch"): name d on screen, keep every girl's name
  on the beam, make the scale tag say what is scaled, and give the algebra 0.6 s holds.
- Motion 8.5 → 9 ("every motion encodes a relation"): no empty chart (curves grow from "tested"),
  a ring that comes back as a picture, the signed distances merging into the 0, a cancel box that
  shrinks with its term, a live self-report number driven by its arrow.
- Hook 8.5 → 9: candidates the viewer can pick, written under the drop lines, and "Pick one."

**Hook (substance 7)**
- YELLOW candidates 2.5, 3 and 4 are written under their drop lines; the "?" stays at the start of
  the friend row; the line ends "Pick one." and the candidates pulse in turn before a 2.0 s hold.

**The beam (craft 1, 5, 10, 11; substance 2, 3, 5, 8)**
- Girls sit 0.8 apart (1.6 per friend), so every name rides onto the beam under its node (Text 20).
  "Sue holds four tokens" flashes her name with the box; "Split Sue's four" flashes it again.
- In the hold after "sigma squared" (just before "Split") the token stacks, Sue's box and
  "4×4=16" fade while the whole picture lifts 1.6 units into the freed band. The old main row fades
  to 0 at the same moment and returns on "So". (On "Split" itself it ran 0.6 s late on the cue.)
- The area labels themselves fly into σ² (no copies on top of the originals, so no "2225"); the
  scale tag reads "square side = distance, drawn at 1/4 scale" in full-size type, sits beside the
  squares in the empty right column (at the bottom-left it was 0.13 from the citation) and fades
  before the labels' flight crosses it.
- The beam draws with the BLUE fulcrum, after the names have settled (drawn earlier, it crossed
  "Betty" and "Carol" in transit).
- "d = k − μ" (PURPLE d, BLUE μ) is written above the right arm of the distance line on "her
  distance", right-aligned past the beam's end so it does not read as "3d" after the fulcrum's 3.
- On "add to zero" the four signed distances merge into the PURPLE 0 under the balance point; that
  0 flies up to replace avg(d) and the box shrinks to fit "2μ·0" in the same move.
- The bar panel dims to 25 % during the algebra; the variance row leaves once its 1.25 is used and
  the identity row once its μ² + σ² is used.
- 0.6 s holds after "sigma squared", "and a cross term" and "cross terms cancel".
- The ring returns as a picture in the freed lower-left band: a thumbnail of the 0:31 ring, a copy
  of the PURPLE distance line collapsing into a point at its centre ("no spread"), the bars meeting
  at 2.0 and 2.0 with no PURPLE ("no gap"), and μ + σ²/μ copied beside it as 2 + 0/2 = 2. In the
  closing pause the bars return to 2.5 and 3.0.

**Reset (substance 4)**
- At 0:42 the ring's friend bar and its "2.0" fade out instead of counting down through 1.9.

**Facebook (craft 9)**
- As 635 lands the bar fills BLUE to 190 and PURPLE beyond. On "A few users" four BLUE dots
  ("a few users") slide past 800, through a break in the axis, toward a "5,000" tick tagged
  "Facebook's limit" (Ugander et al.: "a clear cutoff at 5000 friends, a limit imposed by
  Facebook"). The PURPLE segment flashes on "spread term".

**Harvard (craft 3, 4, 8; substance 1, 6, 9, 10)**
- No Facebook legend over the Harvard chart: each Facebook bar flies straight to the origin of the
  curve it becomes while the axes build, and the step curves grow from "tested this at Harvard".
  The empty-axes stretch and the 7 px legend gap are gone with it.
- Narration: "Friends sit closer to everyone else in the network, so they should catch it first."
  (C&F's centrality mechanism; the old "more ways to catch flu" implied more cases, but the totals
  are level.)
- The plot is 0.4 units shorter so both read-out rows sit above the y-axis title instead of
  beside it.
- Read-out: "C&F fitted lead: 13.9 days" (label left, arrow right, tips aligned); citation
  "Christakis & Fowler, 2010 · PLoS ONE · Fig. 3 redrawn, logistic refit".
- "self-reported:" arrives first with a GRAY copy of the arrow; on "shrank" a live number reads the
  arrow's length as it shrinks and ends at "3.2 days".

**Facts**
- Re-verified the 5,000-friend limit in the arXiv text of Ugander et al. and C&F's centrality
  rationale; every new on-screen number is logged in facts.md "Round 3 additions".

**Found while verifying the masters (fixed before hand-off)**
- Preview: the read-out row sat on the same line as the C&F y-axis title; the plot is now 0.4 shorter
  and both rows sit above it. "d = k − μ" read as "3d" after the fulcrum label; it moved right.
  The beam's Create crossed "Betty" and "Carol" while the names travelled; it now draws with the
  fulcrum. The scale tag was 0.13 from the citation; it moved beside the squares.
- Master 1: the flying 0 crossed "10/8" in the σ² row and "2μ·0" was readable for only ~0.3 s. The
  merge now starts on "distances", the 0 travels under the split row, and the term holds ~1.2 s
  before "cancel" removes it. The live self-report number was readable mid-count ("12.9"); it now
  ghosts in as it counts and is solid only at 3.2. Names crossing nodes during the sort now dim in
  flight. The ring hold is 1.3 s.
- Master 3: a regression (Mobject.interpolate does not descend into Text glyphs, so the names stayed
  at their network positions) was caught by the layout audit (18 issues) and fixed; the final
  master has 0.

**Transcript note**
- review/transcript.txt ends with "Thank you." at 3:40.8–4:10.8 (past the video's end). It is a
  Whisper hallucination on the silent tail: the narration ends at 3:39.9 with "the view is the
  same.", report.md lists 3:39.9–3:41.4 as silence (trailing 1.49 s), and ffmpeg volumedetect
  measures max −62 dB from 3:40.0 to the end (−91 dB after 3:40.3). Nothing is spoken there.

**Mechanics (final master, review/report.md)**
- 3:41.4; 160 wpm on speech time; −14.0 LUFS / −2.1 dBTP; leading 0.00 s, trailing 1.49 s.
- Longest silence 2.23 s (the planned "Pick one" hold); longest static stretch 2.50 s.
- WER 1.5 % (Whisper's "Thank you." insert and "sus four" for "Sue's four" included); 0 banned
  phrases; 0 render warnings; 0 layout-audit issues in 198 checks; no flags.

## Round 1 revisions (second review cycle: craft 8.3, substance 8.5; no caps, no factual errors)

**Plan of the climb (written before editing; BAR §3 "9" anchors vs. where round 1 fell short)**
- Motion 8.5 → 9 ("every motion encodes a relation"): the token fulcrum faded in at 3. Upgrade: the tokens
  land layer by layer and the YELLOW fulcrum, copied from the BLUE one, slides with a live read-out
  2.5 → 2.7 → 2.9 → 3.0 as each layer lands (38/14, 52/18, 60/20), so the motion is the proof. The
  μ²/μ split moves each term to exactly one target; the new bar and denominator rise in after. The
  girl read-out holds 2.0 until the real class has settled.
- Visual 8–8.5 → 9 ("every frame has one focal point; all §5 standards met"): TeX typesets every
  algebra row (μ on the TeX baseline); the guess box collapses into one dashed tick when the friend
  bar is drawn (no doubled outline); during the algebra the bar panel goes to 0 and the beam picture
  is centred at the top with the rows centred under it; the scale tag is 4 words under the squares;
  ring thumbnail at 0.55× with 32-pt digits; C&F read-outs 0.3 down and 0.4 left; a brace, not
  schematic dots, for "a few users".
- Clarity 8.5 → 9 ("could re-derive it after one watch"): the C&F beat now states the link ("named
  friends have more friends, so they sit closer to everyone else"); the ring callback no longer
  changes the bars (picture, row and bars dim; the ring and 2 + 0/2 = 2 carry it); "the average count".
- Hook 8.5 → 9 ("ending resolves the opening exactly"): the landing returns to the cold-open frame
  with the candidates 2.5 / 3 / 4, names the per-girl statistic ("Seat by seat"), and the last line
  answers the opening question: "Two and a half counts the girls; three counts the friendships." The
  friend bar grows to the 3, which gets ringed.
- Concision 8 → 9: cut "friends average twenty percent more than girls", "Sixty over twenty", and the
  landing's token re-flight and 4×/1× tally.
- Audio 8–8.5 → 9: "Split Sue's count, four, into…" (Whisper heard "sus four"); the muddled
  "friends … than girls" comparison is gone.

**Craft fixes**
1. Fulcrum (motion): the tokens now land layer by layer; layer 1 (one per girl) balances at 2.5, and
   from layer 2 a copy of the BLUE fulcrum slides right, turning YELLOW, with a live read-out that
   stops at 2.7, 2.9 and 3.0 (38/14, 52/18, 60/20, each token weighted by how far it has landed).
   It lands on "three" and flashes with the bar's 3.0. Layers drop in from above so they are visible
   while the fulcrum moves.
2. μ baseline (visual): every algebra row from (μ²+σ²)/μ on, plus the Facebook row and the ring's
   2 + 0/2 = 2, is one TeX formula (`trow`), so TeX sets the baseline and spacing; parts are still
   moved one by one. Invisible struts give every numerator and denominator the BAR 0.15 clearance
   from its bar, uniformly, so baselines stay level across a row.
3. Doubled guess outline (visual): when the friend bar is drawn, the dashed box closes onto its right
   edge, which stays as one dashed tick (at 2.0 on the ring, where the bar ends on it; at 2.5 on the
   real class, where the BLUE fill stops at it). On the real class it re-opens leftward from the tick.
4. Wording / pronunciation: "friends average twenty percent more than girls" cut (both critics);
   "Split Sue's count, four, into…".
5. Ring callback (clarity): the bars never change; the class picture, the result row and the bars dim
   to 30 % while the ring thumbnail, its collapsing spread and 2 + 0/2 = 2 play, then brighten.
6. Landing (concision): the second token flight and the 4× / 1× tally are cut (see substance 2).
7. Transient read-outs (motion): the girl read-out holds 2.0 until the real class has settled and
   swaps to 2.5 while invisible; the same swap replaces the 2.5 → 2.0 count-down on the ring, and the
   friend and cold-open read-outs appear with their value instead of counting up from 0.0.
8. Lopsided algebra (visual): on "Measure", the stacks leave, the bar panel and the citation go to 0,
   the main row parks dimmed at the bottom centre, and the beam picture moves up and right so the
   balance point is at x = 0; σ² = 10/8 = 1.25 sits beside the squares and every row is centred under
   the picture. On "exactly the extra half friend we measured" the picture moves back, the bars and
   citation return and the result row moves under them.
9. Scale tag: "sides at 1/4 scale", GRAY Text 18, centred under the squares.
10. C&F read-outs: 0.4 left (arrow ends at x 6.15); the chart is 0.3 shorter with its bottom fixed so
    both rows sit above the y-axis title (row tops at 3.42); the 13.9-day copy arcs up to the read-out.
11. Ring thumbnail at 0.55× with digits at 32 (cap height ≥ 24 px).

**Substance fixes**
1. C&F link: "Christakis and Fowler put this to work at Harvard. Named friends have more friends, so
   they sit closer to everyone else, and should catch flu first." "friends they named" rises in on
   "Named friends" and flashes on "more friends"; "425" joins it when spoken. Re-verified: C&F report
   the friend group's "significantly higher measured in-degree and betweenness centrality".
2. Landing: back to the cold-open frame itself (candidates 2.5 / 3 / 4 under the drop lines). "Seat by
   seat, five have fewer friends than their friends average; only Sue and Alice have more. Betty looks
   at her one friend and sees four. Two and a half counts the girls; three counts the friendships." On
   the last line every friendship flashes, the friend bar grows to the 3 and the 3 is ringed; 2.5 has
   gone under the bar and 4 dims. About 15 s.
3. Ring callback: see craft 5.
4. Concision: "friends average twenty percent more than girls" and "Sixty over twenty" cut.
5. Split doubling: C → D1 moves each term to exactly one place; the second bar grows and its
   denominator rises in after the slide. Copies that start on their source (the numerators rebuilt
   from the identity) leave it with an ease-out instead of lingering half-overlapped.
6. "Split Sue's count, four, into…" (Whisper check below).
7. Facebook: a BLUE brace labelled "a few users" spans the broken axis up to the 5,000 tick
   ("Facebook's limit"), a range instead of dots that read as data.
8. "over the average count, two and a half".

**Found while verifying the previews (fixed before the master)**
- The guess tick stayed at 2.0 on the real class: two animations on one mobject in one play (a slide
  and a fade); the tick now has a single updater.
- The new token layers were hidden while rising through the layer below, so the read-out seemed to
  lead them; they now drop in from above.
- The fulcrum's BLUE → YELLOW blend passed through a muddy grey; it is YELLOW as soon as it moves.
- The ring's "2.0" lingered through the dissolve (its updater overrode the FadeOut); its opacity is
  now driven by the same tracker.
- TeX's own fraction clearance (0.09) tripped the overlap audit; struts fixed it. The cancel boxes
  touched their bars when tightened; 0.035 side buff.
- The self-reported row sat on the line of the chart's y-axis title; lowering the chart crowded the
  citation, so the chart is 0.3 shorter instead. "319 random students" moved to day 75 at 1 %.
- The answered closing frame held only ~0.7 s before the end card; it now holds ~1.5 s.

## Round 5 revisions

Round 5 (craft 8.3, substance 8.5; no caps, no factual errors) returned the same two reviews as the
second cycle's round 1, so their fixes were already in scene.py (see "Round 1 revisions (second
review cycle)" above). That revision had been interrupted: scene.py was edited after its only master
(16 Oct, 03:34), and a master at speed 0.80 never finished. This round finished it, checked each
round-5 fix item on new renders, swept every transition at 4 fps (§11.6) and fixed what the sweeps
still showed.

**Plan (BAR §3 "9" anchors)**
- Visual and Motion ("one focal point"; "every motion encodes a relation"): no frame, even
  mid-transition, may show smeared or stacked glyphs or text crossing text. The 16 Oct sheets
  showed them at 1:25 (÷8 over Σk²), 2:12 to 2:13 (smeared "1.25" and "σ²") and 2:19 (picture
  over the bar panel).
- Audio and Concision ("pauses intentional"; "cutting any sentence loses something"): keep the
  3:33 cut at speed 0.82. The 0.80 change answered a Whisper artefact, not a real pace problem.
- Hook, Clarity and Originality: no structural change. Both critics said the episode reaches 9
  once their fixes are applied, and the fixes are now verified on the master.

**Fixed this round**
1. Divide step (1:25): the terms slide first, and each "÷ 8" fades in only once its term has
   parked. Mid-slide frames had read "Σk²8" and "Σ÷k8".
2. Glyph smear (2:09 to 2:13, 2:44): several transforms paired a MathTex wrapper with a bare TeX
   part, so each glyph morphed into the whole target. "1.25", "σ²", "3.0" and the flying "2.5"
   smeared for about 0.5 s. Every pair now matches level for level. The Facebook read-outs'
   DecimalNumber digits are flattened (`glyphs()`) before they fly into 190 + 445 = 635, and those
   copies leave their source with an ease-out, with no doubled start frame.
3. "d = k − μ" now sits at the right end of the PURPLE distance line it names. Beside the beam it
   had read as one line with the YELLOW "3.0". It fades as the picture moves back at "exactly".
4. The cancel boxes are 0.2 units taller, so the exponent of 2.5² no longer touches the box.
5. Ring to real class (0:44): the ring's 16 tokens and its "what if" label fade within 0.4 s,
   before the nodes sweep through them.
6. Landing (3:17): the chart fades out before the class fades in, so "425 friends they named" is
   no longer double-exposed over the nodes.
7. "a few users" is now Text 26 (was 24).
8. Speed is back to 0.82. The 16 Oct "166 wpm" flag came from Whisper transcribing 1:41 to 1:53
   twice (566 words for a 509-word script). At 0.80 the cut ran 3:48 at about 143 wpm.
9. The answered closing frame holds 0.55 s before the end card, so the trailing silence is under
   2 s with margin.
10. The YELLOW outline of the closing friend bar is now drawn over its fills, as on every other
    friend bar. It had sat beneath them, so the bar's edge was missing.
11. Facebook row (2:43): the straight flights of 190, 445 and 635 into μ + σ²/μ = 190 + 445 = 635
    had crossed "average friend" and the tick labels. 190 now drops below its own label, passes
    right of "average friend" and goes down through the gap between the "400" and "600" ticks.
    445 then takes the same gap, and 635 drops between "600" and "800". The axis numbers and
    title, done with by then, dim to 30 % as context.

Checked and already in place from the interrupted revision: the picture moves back before the
bars return at "exactly" (no overlap at 2:19). The Facebook friend read-out appears with its value
635, without counting up through 473.

**Verified on the master** (review/report.md and frames)
- Runtime 3:33.3. Pace 160 wpm on speech time, 152 overall. −14.0 LUFS / −2.1 dBTP. Leading
  silence 0.00 s, trailing 1.81 s, longest silence 2.23 s (the planned "Pick one" hold), longest
  static stretch 2.60 s.
- WER 0.8 %. The only differences are "divide" (spoken at full level; see facts.md, Round 5),
  "a hundred" → "one hundred" and "twenty oh nine" → "2009". The Whisper repeat and the "Thank
  you." hallucination are gone.
- 0 render warnings, 0 layout-audit issues in 194 checks, 0 flags, 0 banned phrases.
- All 12 contact sheets and the keyframes at 1:10, 1:27, 2:01, 2:13, 2:20, 2:26, 2:43, 2:47, 3:12,
  3:24 and 3:32 were read.
- Frames swept at 1 to 6 fps, on the previews and on the master, across 0:43 to 0:46 (ring to class), 1:24 to 1:27 (divide),
  1:52 to 2:07 (split), 2:08 to 2:14 (C and D rows), 2:25 to 2:31 (into Facebook), 2:40 to 2:46
  (Facebook row), 2:46 to 2:52 (into Harvard) and 3:16 to 3:18 (landing). None shows a smear, a
  stacked glyph or text crossing full-strength text.
- What remains is copies in flight that cross a bar, or text dimmed to 30 %, for at most 0.2 s.
  That is deliberate.

## Round 6 revisions

Round 6: craft 8.4, substance 8.7. No caps and no factual errors; both critics said every fix
together reaches about 9.0, narrowly.

**Plan (BAR §3 "9" anchors, for each dimension scored below 9)**
- **Hook** (8.5/8.5). Anchor: "commits by 0:12; ending resolves the opening exactly". Short of it
  because frame 0 was eight dim circles, the title's "you" was never paid off, the Facebook
  prediction was a blind guess, and the flu stakes vanished for 2.5 minutes. Upgrades:
  - frame 0 shows the friendships and the two question rows as ghosts;
  - the spread cue comes before the Facebook "?";
  - Ugander's 92.7 % pays off the "you";
  - the 0:19 stakes picture returns at Harvard.
- **Clarity** (8.5/9). Anchor: "re-derive after one watch". Short of it because the algebra
  collapse came too fast, "the balance point" was ambiguous, the beam had no scale, the scale tag
  vanished early, and the landing tally did not close. Upgrades:
  - reading pauses, and one collapse;
  - "the girls' balance point, two and a half", with the 3.0 dimmed;
  - a count ruler;
  - the scale tag kept;
  - Carol's tie shown.
- **Visual** (8/8.5). Anchor: "every frame has one focal point; §5 met". Short of it because of
  the crowded 1:13-1:33 and 2:26 frames, tight boxes, small labels and a GRAY data arrow. Upgrades:
  - the panel dimmed in both stretches;
  - box buffs at 0.15;
  - labels at MathTex 36;
  - the self-report arrow in INK.
- **Motion** (8.5/9). Anchor: "every motion encodes a relation; reading time respected". Short of
  it because six states came in 9 s, copies struck labels, and Facebook narration ran over girl
  data. Upgrades:
  - holds of at least 3 s;
  - labels dip during the drop;
  - one synced change on "Facebook".
- **Audio** (8.5/8.5). Anchor: "each deictic lands; pauses intentional". Short of it because of
  the weak "Divide" onset and the Facebook deictic lag. Upgrades:
  - "Now divide";
  - every Facebook change is cued to its word.
- **Concision** (8.5/8.5). Anchor: "cutting any sentence loses something". Upgrade: cut "two and
  a quarter at the ends, a quarter in the middle" and "Back to the eight girls".
- **Originality** (8.5/8.5). Anchor: "a non-obvious image viewers would remember". Short of it
  because the payoff never reused the tokens and the examples were Strogatz's trio. Upgrades:
  - C&F's design runs on the token machine;
  - the 92.7 % personal turn.

**Applied: the round-6 fixes (craft numbering)**
1. Algebra pacing: a 1.6 s pause after "mu squared plus sigma squared" holds the rebuilt row
   (μ² + σ²)/μ = (2.5² + 1.25)/2.5 about 3.5 s; a 1.2 s pause after "over mu" holds the split row
   (its two cancelling fractions boxed) about 3 s; then all three collapses happen in one 1.5 s
   move on "Here that's two and a half, plus a half".
2. Closing pause of the insight: only the result row and the bars return to full strength; the beam
   picture and the ring stay at 30 % and clear as Facebook starts.
3. On "Facebook" the citation (Feld → Ugander), the row label (girl → user) and the axis (0–4 →
   0–800) change in one move.
4. Every highlight box (cross term, the two cancels) has buff 0.15, with widened TeX spaces so the
   neighbouring "+" and "=" stay clear of it.
5. "sides at ¼ scale" is MathTex 30 and stays (at 40 %) as long as the squares; distance and area
   labels are MathTex 36.
6. Frame 0 already poses the question: friendships at 40 %, "average girl" / "average friend ?" as
   30 % ghosts.
7. The Harvard payoff runs on the token machine: the 0:19 stakes picture returns (Jane "random",
   arrow to Alice "named friend"); each girl names one friend ("one possible draw"), the tokens pile
   on Sue and Alice; a flash runs out one, two, three steps from them ("closer to everyone else");
   the girls and the pile fly into the BLUE and YELLOW curves' origins and the two labels become the
   curve labels.
8. The count labels dip to 40 % while the distance copies drop through them.
9. Carol's tie: superseded in 6b (the per-girl tally is cut, see below).
10. The self-report arrow is INK at 50 % (GRAY stays the guess and the axes).
11. Cut "Two and a quarter at the ends, a quarter in the middle" and "Back to the eight girls".

**Applied: the round-6 fixes (substance numbering)**
1. The title's "you": "And ninety three percent of users had fewer friends than their friends
   averaged. Odds are, that includes you." with a BLUE "92.7%" block (re-verified in the arXiv text,
   facts.md). No "so": the mean inequality does not force a majority.
2. The Facebook question is now a transfer test: "...and a few had thousands" (axis break, 5,000
   limit, "a few users" brace) comes before "what would the tokens average?".
3. "Measure each girl's distance from the girls' balance point, two and a half"; the YELLOW 3.0
   fulcrum dims to 30 % for the variance step.
4. A GRAY count ruler (ticks 1–4) under the beam; each pair of girls sits either side of its tick
   and the PURPLE distances are drawn on the ruler, so they visibly end at 1, 2, 3, 4.
5. The bar panel steps back to 35 % from "three" (1:16) to "the extra half friend we measured".
6. Landing: superseded in 6b; the closing words are "three counts the tokens" (60/20, exact).
7. "Now divide ..." gives "divide" a lead-in.
8. The stakes picture returns at Harvard (item 7 above).
9. The cancel boxes clear the exponent; the surviving 2.5 slides to the baseline in the same move.

**Round 6b (same revision, after the toolkit added PRODUCTION_GUIDE §13 budgets mid-pass)**
The first master of this revision (3:40, 542 words) had 0 warnings, but the new review kit flagged
the 500-word / 3:35 budget, four sentences above 200 wpm, a 29 s breathless run and metronomic
full stops. So:
- *Cut to budget* (mute test): "Twenty tokens add up to sixty" (the counter shows it); "In twenty oh
  nine" and the spoken group sizes (axis and labels show them); "from one to four" (the ruler shows
  it); "left and right"; "itself"; and the whole per-girl tally "Seat by seat, five have fewer ...",
  because Facebook's 93 % now makes the per-person point. 542 → 494 words.
- *Landing is one move*: "Betty looks at her one friend, Sue, and sees four" (Betty's token lands on
  Sue and reads 4, the 4 candidate flashes); "Two and a half counts the girls" (girl bar, 2.5);
  "three counts the tokens" (the friend bar grows to the ringed 3). All three candidates are
  accounted for. The chart → class change now happens in the breath before the line.
- *Voice*: CADENCE = "shaped"; [pause 0.9] after "more than twice the mean", "thirteen point nine
  days ahead" and "the extra half friend we measured"; a [pause 0.5] breath in the Harvard beat;
  the fast sentences rewritten ("The guess fell short by half a friend, because ...", "Line the girls
  up ...: they balance at two and a half", "With no spread, the ring had no gap.") and measured under
  200 wpm in Kokoro's timings.
- *Render warnings fixed*: "d = k − μ" touched the ruler's end (moved 0.22 past it); the variance
  beat reached "variance" 0.9 s late (the areas now complete within 1.4 s, are read through a 1.5 s
  pause and fly on "The squares average"); "average three" and the landing cues were late (re-timed).
- *Motion*: the signed distances merge into the 0 along the lane above the ruler, shrinking and
  fading (no doubled glyphs, no label crossing another); the Harvard transition clears the network
  before the axes draw and moves its two labels one after the other.
- *Glyph morphs*: the ring formula is carried beside the ring with a cross-fade (no μ → 2 morph);
  the trow algebra transforms pair identical glyphs whose TeX differs only by an invisible strut, so
  they are exempted (RT_same / TFC_same).
- *Deictics*: "these same eight girls" lands on its highlight (beat.on); "those students" became
  "the students".
- *Type and contrast*: labels Text 27 (34 px), beam names 21 (27 px), "Facebook's limit" 22; grey
  text is the series GRAY #A2AAB5 (7.7:1), lines AXIS.

**Round 6c (render, frame pass and fixes; continues the interrupted pass above)**
State found: the 6b edits (scene.py 13:27) had never been rendered; final.mp4 (12:03) was the
3:40 / 542-word first master. The first 1080p render of 6b then failed at concat: a 48-byte
partial movie left by the interrupted run sat in the render cache. Removed it and re-rendered.
Frame sweeps (5-8 fps strips over every changed transition) then found:
1. 3:00, C&F payoff: the x-axis was drawn in one frame straight across the still-visible class
   (nodes, names, tokens). A `window()` rate function on a lagged `Create` is applied to every
   submobject's sub-alpha, so the first parts finished at once. New `timed()` helper times the
   whole group; the axes now draw 1.0-1.7 s into the move, after the girls and the token pile
   have shrunk into the curves' origins. Same helper for the Write of "d = k - mu".
2. Dimmed YELLOW read olive at 30 % (the 3.0 fulcrum 1:31-2:17, the parked friend-average row
   1:31-2:04; PRODUCTION_GUIDE 13.2.8). Both now sit at 50 %. The raw flu steps behind the fits
   go to 60 % (were 45 %), and the landing's "4" candidate to 55 % (was 30 %).
3. 2:41: the flying copies of 190 / 445 / 635 sat stacked on their own labels for a frame
   ("635 / 635" on the contact sheet). Flights now leave with ease-out and fade in over the
   first 45 % of their path (the other carried values, Sue's 4 and her 1.5, over the first
   20 %). The 3:15 self-report arrow copy starts transparent, so it never doubles the 13.9-day
   arrow. Checked on the master at 10 fps over 2:40.5-2:41.8 and 3:14.6-3:15.7.

**Verified on the master** (review/report.md, all 12 sheets, keyframes at 0:00, 1:24, 1:37,
2:02, 2:13, 2:24, 2:44, 2:46, 2:54, 3:00, 3:14, 3:28; strips over 0:59-1:06, 1:30-1:39,
1:55-2:24, 2:24-2:33, 2:40-2:42, 2:57-3:02, 3:14-3:16, 3:18-3:29)
- Runtime 3:29.5, 494 words (budget 500 / 3:35). Pace 155 wpm on speech time, 0 sentences over
  200 wpm, longest run without a breath 11.5 s. -14.0 LUFS / -2.1 dBTP. Leading silence 0.00 s,
  trailing 1.91 s, longest silence 2.22 s (the "Pick one" hold), longest static stretch 3.7 s.
- 0 render warnings, 0 layout-audit issues in 197 checks, 0 review-kit flags, 0 banned
  phrases, 0 glyph morphs, deictics 2/2 synced. WER 3.6 %; every difference is Whisper's
  number formatting ("seven and a half" -> "7 1/2") or a homophone (girls' / girl's).
  "Divide" is now transcribed.
- Round-6 fixes confirmed in frames: frame 0 poses the question (friendships at 40 %, ghost
  rows); count ruler under the beam, distances end on ticks 1-4; "the girls' balance point, two
  and a half" with the 3.0 fulcrum stepped back; rebuilt row held 4.5 s and split row 3.5 s,
  then one collapse; box buffs 0.15; scale tag kept until the picture moves back; Facebook
  source, label and axis change in one move on "Facebook"; "a few had thousands" before the
  "?"; 92.7 % block on "ninety three percent"; the 0:19 stakes picture and the token draw at
  Harvard; INK self-report arrow; landing in one move ending on the ringed 3.
- facts.md: no new claims; the 92.7 % quote re-checked in the ar5iv text of arXiv:1111.4503.

## Round 7 revisions

Both round-7 critics scored 8.7 (Hook, Visual, Motion, Audio 8.5; Clarity, Concision,
Originality 9), with no caps and no factual errors. Plan: lift the four 8.5 dimensions without
touching the three "keep" items (the token-weighted beam and the 0 that kills the cross term; the
YELLOW-outlined friend bar carried to Facebook; the landing on the cold-open candidates).

**Plan against BAR's 9 anchors**
- *Hook 8.5* (9: "tension rises through build and fail; ending resolves the opening exactly").
  Short of it: 46 s of algebra (1:31–2:17) with no target on screen, and a last line that
  restated 2:16. Upgrade: one spoken question, "Where does the extra half come from?", and a
  full-strength PURPLE "+0.5 ?" tag that the result fills; the last line turns to the viewer:
  "Most of us are Betty."
- *Visual 8.5* (9: "every frame has one focal point; all §5 standards met"). Short of it: dimmed
  YELLOW read brown (1:16–2:20, 3:09+), the C&F read-out 700 px from its arrow, a "random" label
  on one of eight senders, a 2.4:1 explanatory tag, the 92.7 % block beside the 635 bar.
  Upgrade: YELLOW never dims (it goes to 0 or stays at 100 %); read-out directly above its arrow;
  a legend for the redrawn C&F sample; the scale tag at full strength; 92.7 % beside "average
  user".
- *Motion 8.5* (9: "every motion encodes a relation; reading time respected"). Short of it: the
  C&F hand-off emptied the frame, flights crossed tick labels at 2:41, the 2:15 collapse jittered.
  Upgrade: destination first (axes, origin dots), one arc move of each sample into its origin;
  numbers dropping out of their own bar segments through clear gaps; a two-step collapse on
  TeX's baseline.
- *Audio 8.5* (9: "each deictic lands; pauses intentional"). Short of it: five numbers in 9 s
  with flights landing on the next number. Upgrade: [pause 0.4] after "four" and "two and a
  half", each flight on its own word; [pause 0.3] between the two collapse steps; [pause 0.4]
  after "a few had thousands" (the 11.5 s breathless run).

**Applied (craft numbering)**
1. C&F hand-off: on "and should" the axes draw first (0.6 s, 30 %, behind opaque nodes) while
   edges, names and the GRAY caption leave and the BLUE and YELLOW origin dots appear; then one
   1.2 s move: the random students arc (path_arc 0.7) into the BLUE origin, the named friends and
   their tokens (path_arc −0.7) into the YELLOW one, counts riding inside their nodes; then the
   two legend entries glide to their curve-label spots and the axis numbers and titles fade in.
2. YELLOW never dims: the panel's outline and 3.0 go to 0 at 1:16 (rest at 35 %); the 3.0
   fulcrum leaves for the variance and returns at "exactly"; the parked avg(k²)/μ row stays at
   100 %, scaled 0.8 on the bottom edge; ring callback: YELLOW parts to 0; C&F raw steps full
   colour at stroke 1.5, dashed fits stroke 4; the landing's 4 leaves; the cold-open "?" full.
3. "+0.5 ?" tag at top right (5.45, 3.3): the measured +0.5 lifts out of the panel on "extra
   half"; at "exactly" the result's 0.5 flies into it, the "?" drops, and it goes home to the
   PURPLE segment as the panel returns. Opening question added.
4. Facebook flights: tick labels and axis name at 30 % with the bar fill (≈1 s before); the axis
   name moved left of the axis so nothing lies under the ticks; 190 drops from the BLUE segment,
   445 from the PURPLE segment, 635 from under its label, invisible until 0.3 below the friend
   bar, through the 0|200, 400|600, 600|800 gaps; no copy is ever visible on its source.
5. Collapse: D3 (μ + σ²/μ = 2.5 + 1.25/2.5 = 3.0) and D4 typeset first; "two and a half": fades
   in place, μ and 2.5 drop vertically to the baseline, the row closes up; "plus a half": 1.25/2.5
   fades in place, the row closes up, 0.5 rises into the settled slot.
6. Split sentence: [pause 0.4] after "four" and "two and a half"; 4 flies on "four", the 2.5 on
   "two and a half", d = k − μ on "her distance", 1.5 on "one and a half".
7. Read-out left-aligned at the arrow: tips at the in-chart arrow's x, words to the right; y title
   on two lines and "425 friends / they named" on two lines keep the column above the arrow free,
   so the copy rises straight up.
8. "random" on one girl: replaced by the redrawn sampling design and a legend (substance 4).
9. "sides at ¼ scale": full strength (7.7:1) for as long as the squares are on screen.

**Applied (substance numbering)**
1. As craft 3. 2. Last line "Most of us are Betty." (5 of 8 girls; 92.7 % of Facebook users);
   the 2.5 / 3 resolution is silent. 3. As craft 1. 4. The draw follows C&F's design: four
   mutually non-adjacent girls (Betty, Jane, Pam, Tina) are the random sample; only they send
   tokens, along each of their friendships; whoever is named (Sue, Alice, Dale, Carol) is the
   friend sample. Not "one friend each" as suggested: C&F asked for 2–3 friends (out-degree ≤ 3,
   re-read in the PLoS text), so the GRAY caption reads "name their friends" (facts.md).
5. As craft 2. 6. 92.7 % block beside the "average user" row, "their own friends' average".
7. As craft 6. 8. As craft 5. 9. As craft 7. 10. As craft 4.

**Found and fixed while checking frames (round 7)**
- The C&F rings first ran in a LaggedStart: its group was re-added on top of the scene and the
  now-opaque nodes covered their own digits (Betty, Jane, Pam, Tina showed blank). Staggered
  per-node windows instead.
- The Facebook segment flash first tinted the BLUE and PURPLE fills white; it is now an INK flash
  along each segment's bottom edge as its number drops out of it. Each number passes through the
  tick gap where its value lies (190 between 0 and 200, 445 between 400 and 600, 635 between 600
  and 800), drops straight down until clear of the tick labels, then arcs above the row into its
  slot.
- The result's 0.5 copy first slid right along the row through "= 3.0"; it now leaves straight
  up and is invisible until it has cleared its source (no doubled 0.5).
- The hand-off's label move now starts in the second half of the arc move, so no frame shows
  only axes and two parked labels; the shrunken nodes fade over the last quarter of their path.
- "Where does the extra half come from?" was read at 221 wpm at speed 0.82; that one beat is
  spoken at 0.74 (171 wpm). The ring callback now also dims the corner tag with the panel.
- Two landing windows ended after their play (the ring around the 3 stopped 83 % drawn).

**Verified on the master** (review/report.md, all 12 sheets, keyframes kf_19, 32, 35, 37, 39;
4–8 fps strips over 1:30–1:37, 1:45–1:53, 2:16–2:24, 2:44.4–2:47, 2:55–3:07, 3:15–3:22, 3:27–3:31)
- Runtime 3:31.8, 495 words (budget 500 / 3:35); 155 wpm on speech time; 0 sentences above
  200 wpm; longest run without a breath 11.2 s; -14.0 LUFS / -2.1 dBTP; leading 0.00 s, trailing
  1.90 s; longest silence 2.22 s (the "Pick one" hold); longest static stretch 3.4 s.
- 0 render warnings, 0 layout-audit issues in 206 checks, 0 review-kit flags, 0 banned phrases,
  0 glyph morphs, deictics 2/2 synced, WER 3.0 % (number formatting; "Split Sue's" heard as
  "splitsus", as in earlier rounds).
- No dimmed YELLOW anywhere: the panel at 1:16 shows no outline or 3.0; the variance frames
  hold the full-strength parked row and no 3.0 fulcrum; kf_37's raw steps are full colour.
- "+0.5 ?" is on screen at full strength from 1:33 to 2:21, filled by the result's 0.5 and
  returned to the PURPLE segment by 2:23.

## Round 8 revisions

Round-8 critics: craft 8.8, substance 8.9 (no caps, no factual errors). Both said every fix
together reaches 9.0 and no structural change is needed. Kept: the token-weighted beam and the 0
that kills the cross term; the "+0.5 ?" target; the YELLOW-outlined friend bar carried to Facebook.

**Plan against BAR's 9 anchors**
- *Visual 8.5* (9: "every frame has one focal point; all §5 standards met"). Short of it: a 19 px
  stacked ¼, a truncated, navy-dimmed ring callback, the end card dissolving over the class, YELLOW
  going khaki on every fade, area labels reading as one digit string, an 18-word Facebook frame.
  Upgrade: inline "1/4" at label size (plus a sub-part height check in the local audit); whole row
  out and back complete, bars at 45 %; scene out, then card in; YELLOW enters and leaves by growing
  or shrinking at full colour or with ≤ 0.2 s ramps; zigzag area labels; a 5-word 92.7 % line with
  the brace and tags gone.
- *Motion 8.5–9* (9: "every motion encodes a relation; reading time respected"). Short of it: the
  colliding sort at 1:02, the C&F pile-up at 3:05.8, a four-move landing in 1.2 s, the 635 copy
  on the axis. Upgrade: a two-stage sort on nested half circles; a contract-then-two-passes
  hand-off above the axis; a three-step silent resolution in a 2.1 s pause; copies invisible until
  below the tick labels.
- *Audio 8.5* (9: "pauses intentional, deictics land"). Short of it: "Splitsus", a 0.17 s comma
  before "Sue", an 11.2 s breathless payoff, a last line that fought the animation. Upgrade: "Take
  Sue's four"; "[pause 0.3] Sue"; breaths after "named." and "rose first."; the last line only on
  Betty.

**Applied (craft numbering)**
1. Landing: "[pause 2.1]" after "sees four" (2.2 s measured, under the 2.5 s dead-air line, so
   not the suggested 2.6) holds three silent moves: (a) the 2.5 candidate's drop line goes and
   the 2.5 rises into the girl bar's 2.5, which flashes with the bar; (b) every friendship
   flashes, the "?" and drop lines go, and the friend bar grows to 3 at one smooth rate (one
   width, BLUE to 2.5 and PURPLE beyond, under its YELLOW outline) while the 3 steps aside;
   (c) the 3 is ringed as the 4 shrinks away. "Most of us are Betty" then has only Betty and her
   token pulsing. The answered frame holds 0.7 s before the card (trailing silence must stay
   under 2 s, so not 1.5 s).
2. Sort: two stages. Tokens shrink into the girls they landed on and the names leave; "Line the
   girls up": each girl moves onto the beam row in her present left-to-right order (x stays
   close; Dale and Pam share an x, so the row order, not a straight drop, is what keeps the paths
   apart); "by friend count": left-movers arc over the row and right-movers under it, each on a
   half circle centred on her own move, so the paths nest one slot apart (min edge-to-edge node
   gap 0.13 in the first stage and 0.17 in the second, simulated in numpy). Names return under their girls after landing. Alternating ±0.35 arcs
   were tried on paper and rejected: their sagitta (0.04–0.18) is smaller than a node.
3. Ring callback: the whole result row goes to 0 in 0.2 s and comes back whole; the ring's
   "2 + 0/2 = 2" also leaves whole; bars and panel text at 45 %, beam picture at 35 %. At the
   Facebook cut the row's right side "= 2.5 + 0.5 = 3.0" leaves in one 0.2 s move.
4. End card: the whole scene fades out (0.4 s), then the card fades in; no frame holds both.
5. YELLOW: `y_in`/`y_out` (≤ 0.2 s ramps), `shrink_out` (shrink at full colour, then removed),
   `GrowFromCenter`/`GrowFromEdge` and tokens that grow from a quarter size as they leave the
   sender, applied to every YELLOW entrance and exit (candidates, "named friend", arrow, "?",
   read-outs, counter, stack tokens, the 3.0 fulcrum, "4 × 4 = 16", the result's 3.0, "= 2",
   635, legend, origin dot, curves). Alice's and the named friends' YELLOW rings are drawn over
   the BLUE outline (a BLUE → YELLOW stroke recolour passed through khaki).
6. "Take Sue, and split her four, [pause 0.5] into ..." (no possessive: "Take Sue's four" came
   back from Whisper as "Take Sue 4"); "her one friend, [pause 0.3] Sue, and sees four".
7. Area labels zigzag: the right girl of each pair 0.38 lower (MathTex 36 kept; 30 is the tick
   size and the labels are read as values).
8. 92.7 % block: "92.7%" / "below their own friends' average"; brace, "a few users" and
   "Facebook's limit" go to 0 as it is written (11 prose words on screen).
9. Facebook copies: invisible until 0.3 below the tick labels (all three, not only 635).

**Applied (substance numbering)**
1. "sides at 1/4 scale" inline, MathTex 36 (35 px digits); a script-size check (scripts and
   \tfrac at 70 % of the formula size must clear 24 px) added to the scene's own audit.
2. C&F hand-off in four moves: tokens merge into the girls they named; the class contracts to
   0.55 inside the plot area, every node above the coming x-axis (digits kept at 27 px); the axes
   draw while the named friends fly one after another (lag 0.09 s, 0.5 s each) into the YELLOW
   origin; then the random students into the BLUE one while the legend entries glide to their
   curves, each after the girls in its way have left. Every path stays 0.25 above the axis until
   its last 0.16 s; moving rings keep ≥ 0.54 apart (simulated). Each ring keeps its own fill and
   stroke opacity while it shrinks.
3. "[pause 0.5]" after "the students named." and "[pause 0.4]" after "rose first."; the flash
   along the friends' curve lands on "rose first".
4. As craft 6. 5. The re-opened guess box settles before "guess" is written. 6. As craft 5.
7. Cleanup found while checking frames: `Scene.remove` does not reach into a group that is not
   itself in the scene, so the shrunken stack tokens, "4 × 4 = 16" and the C&F tokens stayed in
   the scene at zero size (the layout audit reported them as touching labels until 3:32); every
   shrink is now a remover, and the stack tokens are removed one by one. The end-card fade
   builds its group with `Group` (a `VGroup` refused a Group child).

**Verified on the master** (review/report.md, all 12 sheets, keyframes kf_12, 18, 19, 28, 33,
34, 39, 40; 2.5–30 fps strips over 0:19–0:23, 0:42.6–0:46.6, 1:00.2–1:03.8, 1:06–1:11,
1:34–1:35.6, 1:39.5–1:43.5, 1:46.2–1:49.4, 2:21–2:29, 2:43–2:51, 3:04.3–3:08.3, 3:26.4–3:33.3
and every frame of the final fade 3:32.15–3:32.85)
- Runtime 3:33.3, 497 words (budget 500 / 3:35); 156 wpm on speech time; 0 sentences above
  200 wpm; longest run without a breath 10.7 s (the cold open; the payoff run is now split by
  0.6 s and 0.5 s breaths); -14.0 LUFS / -2.1 dBTP; leading 0.00 s, trailing 1.70 s; longest
  silence 2.22 s (the "Pick one" hold; the landing pause measures 2.2 s); longest static
  stretch 2.67 s.
- 0 render warnings, 0 layout-audit issues in 214 checks, 0 review-kit flags, 0 banned
  phrases, 0 glyph morphs, deictics 2/2 synced, WER 0.6 % (the only differences: "averaged",
  "girl's", "one" for "a"). Whisper now hears "take Sue and split her four" and "Betty looks at
  her one friend. Sue and sees four." The first master's transcript ended on a hallucinated
  "Thank you." over 2.03 s of trailing silence; at 1.70 s it is gone.
- Sort: frames at 1:00.6–1:01.2 show the row forming in left-to-right order, 1:01.6–1:02.2 the
  nested arcs (left-movers over, right-movers under), no two nodes touching and no names in
  flight; names return at 1:02.8.
- YELLOW: candidates, stack tokens, the 3.0 fulcrum, "4 × 4 = 16", C&F tokens and rings, and
  the landing's "?" and 4 grow or shrink at full colour; every YELLOW opacity ramp seen in the
  strips lasts ≤ 6 frames.
- Ring callback: the row is absent from 2:24.6 and back whole at 2:27.6; "2 + 0/2 = 2" leaves
  whole; at the Facebook cut "= 2.5 + 0.5 = 3.0" leaves in one move (2:28.6).
- 1:40.6 (kf_18): the area labels zigzag, 0.12 vertical and 0.17 horizontal clearance;
  "sides at 1/4 scale" at MathTex 36. 2:50–2:56: 11 prose words. 2:45: 190 / 445 / 635 appear
  only below the tick labels.
- C&F: 3:04.5–3:05.1 the contracted class sits wholly above the coming x-axis; the named friends
  then leave one after another as rings (no filled disks), the random students follow while
  the legend entries glide (YELLOW first; they never cross); no frame is empty.
- Landing: 3:27.9 the 2.5 rises into the girl bar's 2.5; 3:28.7–3:29.7 the bar grows smoothly to
  3; 3:29.9 the 3 is ringed as the 4 shrinks; 3:30.1 "Most of us are Betty" with only Betty and
  her token pulsing; 3:32.4–3:32.8 the scene fades out, then the card (3:33.1). No frame holds
  both.

## Round 9 revisions

Round-9 critics: craft 8.8, substance 8.9 (no caps, no factual errors; both: every fix
together reaches 9.0, no structural change). Kept: the token-weighted beam and the 0 that kills
the cross term; the "+0.5 ?" target; the YELLOW-outlined friend bar carried to Facebook and the
silent landing.

**Plan against BAR's 9 anchors**
- *Motion 8.5* (9: "every motion encodes a relation; reading time respected"). Short of it: the
  variance squares pop in (0.3 s) before their sides drop; the divide chain shows four states in
  8 s and passes through a blank numerator; the Facebook -> C&F change dips through an empty
  frame. Upgrade: side first, then the square grows down from it, then its area; two divide
  states (the second held for ~9 s) with in-slot pinch swaps and the "÷ 8" flashing BLUE as it is
  absorbed; the BLUE "average user" bar splits into the class's eight BLUE nodes.
- *Visual 8.5-9* (9: "one focal point; all §5 standards met"). Short of it: four distances drawn
  on top of each other; "4 × 4 = 16" lingering 18 s; C&F tokens 10-15 px from rings; the squares
  outliving their scale tag; fits above 0 before the first case; the card still fading at the
  end. Upgrade: one segment per distance in two lanes, labels over their own segments; the 16
  flies into Σk² and the label leaves; tokens parked mid-edge, >= 0.15 from both rings (exact
  box-to-circle check); squares leave with their tag; fits start at each group's first case;
  card held.
- *Audio 8.5* (9: "pauses intentional"). Short of it: a 10.7 s breathless cold open; the 199 wpm
  "A girl with k friends ..." sentence; "girl's ... girls'". Upgrade: breaths after the first two
  cold-open sentences, the k-squared sentence at 0.78 after a breath, the divide sentence at 0.78
  with a 0.8 s hold, "from the balance point".
- *Clarity* (substance 4): the C&F "random students" were a low draw (mean 1.75). Upgrade: the
  draw {Betty, Dale, Carol} (counts 1, 3, 2, mean 2.0), whose six tokens 4, 4, 4, 2, 3, 1
  average exactly 3.0.
