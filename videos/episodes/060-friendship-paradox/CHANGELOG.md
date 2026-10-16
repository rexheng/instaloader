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
