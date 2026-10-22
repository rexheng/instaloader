# Episode 4 changelog

## Round 1 revisions

Reviews: `reviews/round1-craft.md` (8.1) and `reviews/round1-substance.md` (6.0: the cap for a
factual error; 8.1 on the dimensions). Both critics said every fix would reach 9 without a new
structure. Both also said the −8 baseline was asserted rather than derived. That is the one
change bigger than polish, so the back half (1:57 to the landing) was rebuilt around it.

**Factual (substance cap 6)**
- The critic was right: the expected gap at n = 1,000, k = 3 is ≈ −0.70, not −0.75. Ours from
  10⁶ simulated sequences is −0.71 (s.e. 0.006). The v1 figure was Monte Carlo noise from a
  40k-rep run. The "1,000 shots" ghost marker and label are removed from the video;
  "longer records shrink it" stays as narration, sourced to the M&S abstract. `check_numbers.py`
  now uses 10⁶ reps and adds an exact dynamic program for E[P(hit | k hits)]. That program
  reproduces 17/42 and gives 46.0% / 54.0% for Cornell's design. facts.md rows 17, 17b and 18
  are rewritten, and rows 12b, 12c and 23 are new.

**Deriving the −8 (craft 1, substance 2)**
- New *mirror* beat: "Tails crowd the same way, so after a tails, the share of heads reads hot:
  twenty five out of forty two." The vote strip rises to an "after heads" lane. A copy drops into
  an "after tails" lane and flips over (heads ↔ tails, mirrored about 50%), so its heads part
  ends at 25/42. Then "Subtract the two averages… minus nineteen points", drawn as a red arrow
  between the two lane cursors and worded as a difference of averages, per the craft critic's
  note.
- Cornell: the lanes become "after 3 hits" / "after 3 misses" sliders. Both cursors glide back to
  50% (the obvious guess), then "the same crowding pulls those to forty six and fifty four
  percent". The values are exact, and M&S state the direction ("by symmetry"). The gap arrow
  shrinks from −19 to −8, and the narration says "Longer streaks grow the bias and longer records
  shrink it", which explains why −19 at 4 flips becomes −8 at 100 shots.

**Axis transform (craft 2, substance 3, 9)**
- No cross-fade. The share labels fade out first, then the line is rescaled to 40–60% with
  5 ticks. On "gap" the % labels fade out, the slider pair slides left until the after-misses
  cursor sits on the dashed line, and the same tick marks are relabelled −10…+10. The blue
  after-hits cursor is carried along and becomes the −8 random-shooter marker. The arrow becomes
  the red "bias". The two label sets never coexist. The title is now MathTex with a true minus:
  "after 3 hits − after 3 misses / (percentage points)".

**Payoff frame (craft 3, 4, 7; substance 6)**
- No hollow rings: the mini coin rows are gone, and the readings sit in a two-row right-column
  table (blue 46/54, then purple 49/45). The purple values fly down into a +4 marker.
- The brace runs from −8 to +4, 0.22 above the two marker tops. "bias" is below its arrow. No
  "the obvious guess" text on the gap axis. On "evidence", the header, the citations and the
  table dim to 30%.

**Hook, concision, composition (craft 5, 6, 8; substance 4, 8)**
- Cold open: "Do that for all sixteen possible sequences and average the shares." A ghost
  miniature of all 16 sequences fades in under the row and collapses into the "?". The row starts
  at the vertical centre, and the axis is centred until the right column is needed (it slides left
  during "Yet no flip is biased").
- The test beat is cut to "Heads are hits", with the coin letters morphing into hit/miss words
  (and back on "a fair coin"). "Test the test" saves another second. The table is on screen by
  about 0:40, instead of 0:45.
- 17/42 is said once: "Line up the votes, and heads hold seventeen out of forty two. That's the
  row average, one vote per row. Pool the counts first, and you get one half."

**Formula and labels (craft 9, substance 5, 10, 11)**
- The 1/14 is full size, in ink. It is built by TransformFromCopy from 14 equal vote outlines
  drawn over the strip on "one vote per row". hᵢ/nᵢ flies from the table's scores. No Write is used
  on formula parts (stroke 0), so the weight is consistent.
- "cold" writes on "reads cold" and "−9.5 points" on "nine". The label sits 0.25 left of the blue
  line and holds about 6 s, until "Gather".
- The table moved down 0.1, and the HHHH box buff is 0.06, so it stays inside title-safe.
- Closing line: "A fifty percent shooter whose rows average one half here is already running hot."
- Citation format is "Gilovich et al., 1985 · Cognitive Psychology" (BAR format), which also
  clears the two-line gap-axis title.

**Audio (craft 10)**
- Pauses vary by role. Gaps inside a thought are 0.12 s plus pads (≈0.25 s). Some reveals get
  0.6 s ("Yet no flip is biased.", "…twelve points hot."). Beats that close a section get
  0.6–0.8 s. The prediction hold stays at 1.6 s.

**Transitions and pronunciation (self-review of the renders)**
- The landing no longer cross-dissolves. The payoff fades out (0.6 s), then the cold-open frame
  fades in (1.0 s), so the two frames are never superimposed. In the mirror clearing, the
  "after heads" label fades in only after 17/42 has landed beneath it.
- Added an IPA override for "Sanjurjo's". Whisper had heard the possessive as "Sanjeros"; it now
  hears "Sanjorjo's", which matches the Spanish /xuɾxo/.

**Mechanics (final master):** 3:10.8, 152 wpm over speech time, −14.1 LUFS / −2.2 dBTP,
longest silence 2.07 s (the planned prediction hold), longest static stretch 3.4 s, 0 render
warnings, 0 review flags, and no banned phrases.

**Kept:** the one-vote strip sequence, the landing on the cold-open frame, and the deictic boxes
on "this row's three heads" / "this lone tails".

## Round 2 revisions

Reviews: `reviews/round2-craft.md` (8.2) and `reviews/round2-substance.md` (8.2). No caps and no
factual errors; both said every fix would reach about 9, narrowly, with no structural change. The
two blockers both critics named were the 0.3 s mirror flip and the verbal-only −19 → −8 step.

**Climb plan (BAR §3 "9" anchors, where the episode fell short, the upgrade)**
- *Clarity 8 → 9* ("viewer could re-derive it after one watch; assumptions stated"): the mirror was
  invisible, −19 → −8 was words only, p ≈ .5 was unstated, and the landing dot was one row's 1/2.
  Upgrade: a two-step, narrated mirror; streak/record ghost ticks; "from where they'd hit about
  half"; the landing answers the cold-open question with the sixteen rows, not one row.
- *Motion 7.5 → 9* ("every motion encodes a relation; reading time respected"): flip 0.3 s, four
  shatter transforms, a 3.1 s static axis, end card over the last word. Upgrade: explicit 0.8 s
  drop + recolour + 1.4 s flip; fly-in transforms that keep glyphs whole; ghost ticks move on every
  clause; no end card.
- *Visual 8 → 9* ("one focal point; all §5 standards"): ~25 prose words in the payoff, empty top
  40%, interlocking rings, a 20 px ½. Upgrade: dim-as-you-go (≤ 12 prose words at every payoff
  keyframe), the picture rises 1 unit after the table leaves, smaller table coins, inline 1/2.
- *Hook 8.5 → 9*: question by 0:11.4 (was 0:13.2); the ending now re-sees the opening exactly
  (the same ghost rows that became "?" collapse onto 17/42).
- *Audio 8.5 → 9*: longer breaths in the densest run; the last word is never covered.
- *Concision 8.5 → 9*: cut "So look again at your guess" and "possible"; the vague "the argument
  goes on" became a concrete, sourced limit.

**Mirror (craft 1, substance 1)**
- New narration: "Tails crowd the same way. Swap heads and tails, and the strip flips over one
  half. So after a tails, the test reads hot: twenty five out of forty two."
- The table fades out while "one half" is still sounding (end of the formula beat). On "Tails
  crowd" the vote strip rises to the top lane; a copy drops unchanged to the bottom lane (0.8 s);
  on "Swap heads and tails" its tiles recolour in place; on "the strip flips over one half" it turns
  a half turn about the dashed 50% line (explicit run_time 1.6 s) while the dashed line thickens as
  the mirror axis. 17/42 and 25/42 each come from their lane's heads part as one merged block.
- Root cause of the round-2 0.3 s flip, found in a 10 fps strip of the first round-3 master: the
  flip function applied `smooth()` inside an `UpdateFromAlphaFunc` that already applies `smooth`,
  so the double ease packed the half turn into ≈ 0.45 s even with a 1.4 s run_time. Now the
  updater runs linear and the turn uses one sine ease; verified frame by frame.

**−19 → −8 shown, not said (craft 2, substance 2)**
- On "Longer streaks grow the bias" two dim blue ghost ticks slide out of zero to −1.0 and −3.1
  (1 and 2 hits in a row, yellow ● / ●● glyphs; the −8 marker gets ●●●). On "Longer records
  shrink it" all three slide to their 1,000-shot positions (−0.10, −0.30, −0.71: almost zero,
  label "1,000 shots"); on "but a hundred shots isn't long" they slide back. All positions are
  exact expectations by dynamic programming (`check_numbers.py` now runs n = 1000); no numbers are
  printed on them. The ghosts clear on "Cornell's". The static 3.1 s stretch is gone.

**Substance**
- p ≈ .5 stated (substance 3): "...up to a hundred shots each, from where they'd hit about half";
  the dashed 50% line and its tick pulse on "about half". Verified in M&S §3.1: "at a distance
  from which the experimenters determined he/she would make around 50 percent of the shots".
- Landing (substance 4): HHTH's 1/2 stays in place. The ghost of all sixteen rows returns and
  collapses onto 40.5%, where the 17/42 marker draws (the cold-open question answered on its own
  image). The shooter is a separate blue dot on the 50% line; "hot" arrow from 17/42 to it.
- Honest limit (substance 8): "That's evidence for a hot hand in a gym, not proof it survives
  defenders in a game", with a grey "no defenders" tag under +4. Verified against M&S §3.1 (the
  experiment was designed for "eliminating the effects of shot selection and defensive pressure")
  and fn. 22 (defenses adjust to a hot player in games).
- "this very comparison" → "the same comparison" (substance 9); facts.md row 15 explains why the
  row-average difference is GVT's construction, and notes the −1/3 per-row mean at n = 4.

**Motion (craft 3, 6; substance 6, 10)**
- Scores → dots: a copy of each score shrinks into a dot just right of it (0.6 s, lag 0.04), then
  the dots fall (lag 0.06). No fraction copy crosses a neighbour, and no dot sits on a glyph.
- Cold open: the counted heads' H and the two rings fly into "1" and "2" along an arc *under* the
  row, instead of morphing across coins 3 and 4.
- 12/24 restacks into the pooled formula by cross-fade (FadeTransform), not a glyph morph; the
  17/42 in the vote formula no longer travels through Σhᵢ/Σnᵢ during the rise.
- Coins → tiles: only each coin's disc morphs into its tile (letters stay in the table); 12 and 24
  fly in only after the last tile lands.
- hᵢ/nᵢ, 1/14, Σhᵢ, Σnᵢ, 17/42, 25/42, +4: a `fly_into` helper sends whole copies (glyphs, tiles,
  outlines, one merged block) into the target and shrinks them away as the target appears, two
  grouped flights for numerators and denominators. No glyph-by-glyph shatter anywhere.
- End: the payoff fades out (0.5 s), the cold-open frame fades in (0.8 s) before the landing line;
  the final frame holds ≈ 0.8 s after "hot" (arrow and label complete from the start of "hot"),
  with no end card over it. The first round-3 master held 1.45 s of silence and whisper
  hallucinated "Thank you." into it (not in the audio); the shorter tail avoids that artefact.

**Visual (craft 4, 5, 7, 10; substance 5, 7)**
- Payoff word load: header details dim to 30% once the lanes are relabelled ("Cornell, 1985"
  stays); GVT's citation dims when M&S appears; the zoom title is "next-shot hit rate"; the gap
  title is one MathTex line, "after-hits − after-misses (points)"; the right column dims while it
  is not being read (ghost ticks, brace) and returns for Cornell's 49/45.
- The mirror and payoff sit 1 unit higher (lanes at y 1.4 and 0.0, axis at −0.7) with the lanes
  1.4 apart; the +12 label clears the header by 0.6.
- Table coins radius 0.185 at pitch 0.49 (rings clear the neighbouring coin by ≈ 0.05); scores
  0.3 from their coins.
- "every flip: 1/2 heads" is an inline MathTex 1/2 at 38 (grey: it is a probability, not a test
  score, so it does not borrow the h/n colours).

**Hook and audio (craft 8, 9; substance 11, 12)**
- Cold open shortened ("After each heads, check the next flip: here, one of the two is heads. Now
  average that share over all sixteen sequences."): "What do you get?" ends at 0:11.4; the axis
  draws on "average that share" and the sixteen ghost rows on "all sixteen sequences". The stakes
  sentence (1985 study, "an illusion") now starts at 0:17.2 (was 0:19.0), inside the stakes slot.
- Gaps: 0.6 s after "a whole one.", 0.55 s after "across eleven.", 0.38 s after "eight rows.".
- Note on craft fix 8: in this toolkit "[pause 0.12]" *shortens* the 0.38 s sentence gap, so
  removing it would have lengthened the open; the time came from the shorter sentences instead.

**Self-review loop.** Two 1080p masters. After the first, 10 fps strips around every fixed
transition found: the double-eased flip (≈ 0.45 s), seed dots sitting on the score glyphs, the
12/24 glyph scramble, 17/42 crossing Σhᵢ/Σnᵢ, the cold-open "1/2" copies crossing coins 3–4, a
faint 1 s ghost in the landing, and whisper's "Thank you." in the silent tail. All fixed in the
second master and re-checked frame by frame (flip 1:54.2 → 1:55.6, about 1.5 s).

**Mechanics (final master):** 3:13.9, 154 wpm over speech time (484 words), −14.0 LUFS /
−2.1 dBTP, leading silence 0.00 s, trailing 0.91 s, longest silence 2.06 s (the planned
prediction hold), longest static stretch 3.2 s, 0 render warnings, 0 layout-audit issues,
0 review flags, WER 1.3% (remaining diffs are homophones: "rows/rose", "pool/pull", and the
accepted "Sanjorjo's"), no banned phrases.

**Kept (both critics' keep lists):** the vote-strip sequence with pooled 12/24 above and one-vote
17/42 below; the carry from the after-3-hits cursor to the −8 random-shooter marker with the axis
relabelled in place, and the purple +12 brace; the landing on the rebuilt cold-open frame, with
"→ hot" drawn from the 17/42 baseline.

## Round 3 revisions

Reviews: `reviews/round3-craft.md` (8.6) and `reviews/round3-substance.md` (8.6). No caps and no
factual errors (both critics re-verified every number, the GVT quote and M&S's −8 / +12); both said
the fixes reach about 9.0 with no structural change. Nothing in facts.md needed correcting; it now
records the reworded lines and the new on-screen ghost/column design (rows 18, 23 and a "wording
changes" table).

**Climb plan (BAR §3 "9" anchors, the shortfall, the upgrade)**
- *Clarity 8.5 → 9* ("re-derive it after one watch"): the 40.5% marker crossed the pooled strip for
  35 s; 46/54 first sat under a Cornell header; the streak dots were never decoded; the landing line
  was one breath with "rows"/"rose". Upgrade: marker shortened to the vote lane; "random" column head
  and M&S citation arrive with 46/54; "hits in a row" legend with flags that ride their ticks; a
  re-worded, paused landing line.
- *Visual 8.5 → 9* ("one focal point; nothing to remove"): colour-only random/Cornell columns, double
  stroke at −8, axis title saying heads while coins said hits. Upgrade: column heads, the 3-hit ghost
  landing exactly under −8, an axis title that swaps words with the coins.
- *Motion 8.5 → 9* ("every motion encodes a relation; reading time respected"): muddy insight exit,
  rushed ghost beat, Write debris, doubled 12/24 glyphs, a pulse into the dashed line. Upgrade: each
  of these replaced (below), every ghost state now held ≥ 1.8 s.
- *Audio 8.5 → 9*: "pool"/"pull" and "rows"/"rose" removed from the narration; pauses inside the
  reframe line. WER is now 0.6% (only "a"/"one" and the accepted "Sanjorjo's").
- *Hook 8.5–9 → 9*: larger, brighter 16-row ghost; precise question ("Do it for all sixteen sequences
  and average the shares"); the pre-spent "cold ←" arrow is gone.
- *Concision 8.5 → 9*: "That's the row average, one vote per row" → "That's one vote per row";
  "should score above their usual rate. A random one…" → "beats their usual rate; a random one…".

**Fixes, by critic item**
- Marker through the pooled strip (craft 1, substance 1): during "Yet no flip is biased" the blue
  40.5% marker's top animates down to 0.15 above the vote strip (its own ValueTracker), so the pooled
  12/24 strip is read only against the dashed 50% line; the 40.5% label sits at the marker's tip.
- Insight exit (craft 2, substance 5): on "Tails crowd" the pooled strip, Σhᵢ/Σnᵢ = 12/24 and the
  1/14 formula fade out together in place (0.5 s, drifting up 0.3); only then does the vote strip
  rise (0.8 s) and the copy drop (0.8 s). No two strips overlap; nothing reaches "100%".
- Ghost ticks (craft 3, substance 3): three ghost ticks slide out of zero to −1.0, −3.1 and −8 (the
  3-hit one lands exactly under the −8 marker and is drawn behind it: no double stroke). Each carries
  a flag of yellow hit dots hung on the left of its own tick top by an updater (flags left, not above:
  above, the ●●● would sit on the −8 marker line), and a grey "hits in a row" legend (Text 24) sits
  over ●●. New pause after "grow the bias." holds that picture ≈ 1.8 s. On "Longer records shrink it"
  the 1- and 2-hit ghosts step aside and the 3-hit ghost slides with its flag to −0.71, "1,000 shots",
  held ≈ 2.2 s; it slides back on "isn't" (not "but"). Only GVT's 3-hit case is carried to 1,000 shots:
  at that length the three ticks sit within 0.25 units of each other and their flags would collide.
- Payoff columns (craft 4, substance 2): a blue "random" column head is written on "For a random
  shooter", before 46/54 land; the M&S citation now arrives on "the same crowding" (GVT's dims on
  "Miller"); the right column dims to 30% at the gap relabel (2:31) and stays dim until "Cornell's",
  when a purple "Cornell" head appears beside "random" with 49/45 under it. The header's "26 players ·
  up to 100 shots" fades then (it has had its flash) and "Cornell, 1985" re-centres, keeping prose ≤ 12
  words. The 49/45 flights into +4 are arced so they pass between, not through, the column's labels.
- "+12 points" (craft 5, substance 6): FadeIn(shift=DOWN·0.15, 0.6 s) as the brace finishes; no Write.
- Landing line (craft 6, substance 4): "A fifty percent shooter [pause 0.3] who averages one half on
  this test [pause 0.2] is already running hot." (substance's wording; it drops "rows" entirely). The
  dashed 50% line pulses on "fifty percent shooter" (which also removes a 3.6 s static stretch), the
  blue dot grows on "one half", the arrow on "already running hot"; 0.9 s trailing silence.
- 12/24 restack (craft 7): ReplacementTransform 12 → numerator, slash → bar, 24 → denominator (0.6 s,
  smooth); verified at 4 fps, no doubled glyphs.
- "the obvious guess" pulse (craft 8): every pulse of that label (and of the landing's copy) now
  scales about its left edge, growing away from the dashed line.
- Axis title (craft 9): the title is four word groups from one ligature-free Text; on "Heads are hits"
  "checked" and "that are" slide while "flips"/"heads" rise out and "shots"/"hits" rise in, and back
  on "a fair coin". (First attempt sliced a ligatured Text, where "fl" is one glyph, and left debris;
  caught in the preview and fixed.)
- Concision (craft 10, substance 7, 8): lines above; the "cold ←" half-arrow is gone.
- Hook ghost (craft 11): the 16-row ghost is a compact 4 × 4 at coin radius 0.122, 60% opacity, dealt
  in on "all sixteen sequences" and collapsed onto the line as "?" on "average the shares". The landing
  ghost uses the same compact layout.
- Question precision (substance 9): "Do it for all sixteen sequences and average the shares." The
  question now ends at 0:11.6 (was 0:10.9); the prediction hold is unchanged (2.07 s).

**Self-review loop.** Two previews and three 1080p masters. Frame strips (4–5 fps) around every fixed
moment found and fixed: the ligature debris in the axis title, "random"/"Cornell" heads touching, the
100-shot ghost picture held 0 s (the legend fade overlapped the next move), the "1,000 shots" label
crossed by the returning flag, and the 45% flight crossing 54%.

**Mechanics (final master):** 3:15.1, 154 wpm over speech time (486 words), −14.0 LUFS / −2.1 dBTP,
leading silence 0.00 s, trailing 0.89 s, longest silence 2.07 s (the planned prediction hold),
longest static stretch 3.9 s (that same planned hold), 0 render warnings, 0 layout-audit issues,
0 review flags, WER 0.6%, no banned phrases.

**Kept (both critics' keep lists):** the one-vote strip (HHHH's three heads squeezed into one vote,
HTTT's lone tails stretched to a whole one, the yellow sliding onto 40.5%); "test the test" → the live
marker 50% → 40.5% → "cold −9.5 points"; the half-turn mirror and the after-hits cursor carried into
the −8 marker with the axis relabelled in place, ending on the purple +12 brace; the landing on the
rebuilt cold-open frame with the 16 rows collapsing onto 17/42 and "hot" drawn to the 50% dot.

## Round 5 revisions

Reviews: `reviews/round5-craft.md` (8.1) and `reviews/round5-substance.md` (8.3). No caps. They
review the same master as round 4 (`round4-craft.md` 8.8, `round4-substance.md` capped at 6 for the
transient Σᵢ hᵢ/nᵢ = 17/42), so the fixes from all four reviews are applied together.

**Climb plan (BAR §3 "9" anchor → shortfall → upgrade)**
- *Clarity* ("re-derive after one watch; all numbers check out"): a false mid-build equation
  (1:44.4–1:45.6); "reads hot" used for the after-tails reading; 8 vs 11 rows not tied to 17/42;
  the formula pair lived ~3 s. → No "=" until a side is complete; "reads high"; on-screen counts
  "12 heads · 8 rows" / "12 tails · 11 rows" and "Fewer rows, fewer votes"; Σhᵢ/Σnᵢ built where the
  pooled half is computed (1:15) so both formulas sit together ≥ 4 s; named "average of ratios" vs
  "ratio of totals" with the Σ positions flashed.
- *Visual* ("one focal point; all §5 standards"): cluttered climax frame; empty-lane stretch
  2:09–2:21; grey text 5.8–6.5:1; purple header over random-shooter content; 20 px table letters.
  → Table dims and "the obvious guess" text leaves before the formulas; a simulated 100-shot record
  fills 2:09–2:21; grey text #A9AEB6 (8.1:1); header in ink until Cornell's data; table letters 21.
- *Motion* ("every motion encodes a relation"): formula held under the §5 minimum; 0:17–0:32 only
  text events; 2:11–2:21 only header words. → Holds ≥ 3.6 s; coins morph on "basketball shots";
  arcs re-traced on "this kind of check"; rings on the record's shots after 3 hits / 3 misses; the
  axis rescales with its tick labels moving (never unlabeled); the payoff axis and dashed line
  transform into the landing's instead of a dissolve.
- *Hook*: explicit three-way prediction ("Below, at, or above one half?") with options on the axis.
- *Audio*: "Sanjurjo" re-phonemized (/sɑnhˈuɹhO/; whisper now returns "Sanjurjo's").
- *Concision*: "That's one vote per row" and "Count all the flips together first…" cut;
  "Tails crowd the same way" merged into the mirror line.

**Fixes, by critic item** (r5c = round-5 craft, r5s = round-5 substance, r4c/r4s = round 4)
- False intermediate equation (r5s 1, r4s 1): the row-average formula is now built as 1/14 + Σ
  (from the 14 vote outlines), then hᵢ/nᵢ (the 14 row scores fly in whole), and only then "=" next
  to the 17/42 that was parked at its right on "seventeen out of forty two". The pooled
  Σᵢhᵢ/Σᵢnᵢ is built at 1:15 ("Total heads over total flips: exactly half"), so the two formulas
  are born 35 s apart, sit together ≥ 4 s, and its "=" also arrives only once both sides exist.
- Formula hold, typography and focus (r5c 1, 4; r4c 1, 2; r4s 2, 6): both displaystyle, size 40,
  "=" signs on one vertical, each beside the strip it computes. On "line them up" the table dims to
  30% and "the obvious guess" text leaves; the pooled formula dims while the row-average one is
  built and returns on "instead of the ratio of totals", when the 1/14 Σ and then the two inner Σ
  pulse (the one structural difference). On the mirror, the 17/42 itself moves up to become the
  "after heads" lane value; the test's formula returns in the landing beside its marker.
- Crowding made quantitative (r5c 5): "12 heads · 8 rows" and "12 tails · 11 rows" written as the
  boxes are counted, then "Fewer rows, fewer votes" with the thin heads slices pulsing. (Not
  "12 heads ÷ 8 votes": heads hold 17/3 votes, not 8; facts.md row 27.)
- "reads hot" → "reads high" for the after-tails value (r5c 2); "Tails crowd the same way" → "Now
  score the flip after each tails", spoken while the second lane is built (r4s 3, r5c 8).
- Concision (r5c 8, r5s 2): "That's one vote per row" and "Count all the flips together first, and
  you get one half" are cut.
- 2:09–2:21 empty lanes (r5c 3, r5s 5): one simulated 100-shot random-shooter record (seed 292,
  labelled "simulated / random shooter") deals in on "up to a hundred shots each"; blue rings mark
  the shots after three hits, then after three misses; it fades as the cursors move to 46/54
  ("on average" added). Lanes and axis title switch to basketball terms on "the same comparison";
  the 0–100% → 40–60% zoom slides each tick with its label (never unlabeled); the header is built
  centred and in ink. Substance's alternative (26 purple dots from Table 2) was not used: Table 2's
  per-player hit rates span .35–.60, off the 40–60% axis, and the record also teaches the test.
- Purple only with Cornell data (r5c 9, r4c 8): "Cornell, 1985" is ink until "Cornell's players",
  then turns purple with 49%/45%. The right column fades out when the +12 brace lands (r5s 8).
- Hook (r5s 4, r4s 4): "Below, at, or above one half?" with "< 1/2", "= 1/2", "> 1/2" on the line;
  "= 1/2" becomes "the obvious guess". Question ends ≈ 0:12.3.
- Stakes motion (r5c 6, r4c 5): arcs and rings re-trace on "this kind of check"; coins become
  hit/miss and the axis title "shots/hits" on "basketball shots" (moved from "Heads are hits",
  which now pulses the hit words). "ran this same check" → "ran this kind of check" (r4s 5).
- Contrast (r5c 7, r4c 4): grey text #A9AEB6 (8.1:1); grey shapes unchanged. Table coin letters
  Text 19 bold, 24.5 px cap height (r5s 7); coin pitch 0.50 and ring radius r + 0.04 keep ≥ 0.15
  clearance.
- Landing (r5s 6, r4c 7, r4s 8): the payoff's number line and dashed zero line transform into the
  share axis and dashed one-half guess (no full dissolve); the sixteen ghost rows fly into
  (1/14)Σhᵢ/nᵢ beside the 17/42 marker; on "A fifty percent shooter" the row becomes hit/miss and
  the title "shots/hits"; thicker arrow, "hot" at 38; final hold ≈ 1.3 s.
- Sanjurjo (r5c 10, r5s 3): /sɑnhˈuɹhO/; whisper now transcribes "Sanjurjo's".
- Not applied: r5s 9 ("three-hit streaks crowd harder"), optional; it would precede a smaller gap
  (−8 vs −19) and the ghost ticks already show why. r4c 6 / r4s 7 (drop the reverse hit→H morph):
  kept, since "a shooter we know is random: a fair coin" is the mapping back.

**Self-review loop.** One preview and four 1080p masters, each followed by frame strips at 3–4 fps
around every changed transition (§11.6). Found and fixed along the way: table letters at Text 21
touched their coin rims (now 19, pitch 0.50); the inline 12/24 reached x = 6.45 (now right-aligned
to its stacked place); the 14 digit flights into hᵢ/nᵢ read as debris (now whole row ratios fly,
with the pooled formula dimmed while they pass); "26 players" and "up to 100 shots" overlapped
while the header re-centred; adjacent record rings overlapped; text morphs ("= 1/2" → "the obvious
guess", H ↔ hit, 17/42 stacked → inline, "after heads" → "after 3 hits", "?" ↔ values, the axis
title words) showed superposed glyphs mid-way, so every one is now a sequential hand-off (the old
glyphs leave before the new ones arrive) with no frame holding both.

**Mechanics (final master):** 3:24.0, 152 wpm over speech time (499 words), −14.0 LUFS /
−2.1 dBTP, leading silence 0.00 s, trailing 1.32 s, longest silence 2.06 s (the planned
prediction hold), longest static stretch 2.7 s, 0 render warnings, 0 layout-audit issues in 216
checks, 0 review flags, WER 0.4% (only "a" heard as "one" twice; "Sanjurjo's" now transcribed
correctly), no banned phrases.

**Kept (all four reviews' keep lists):** the one-vote strip (HHHH's three heads squeezed into one
vote, HTTT's lone tails stretched to a whole one, the yellow sliding onto 40.5%); "test the test" →
the live 50% → 40.5% marker → "cold −9.5 points"; the half-turn mirror and the two lanes slid into
the difference axis, ending on the purple +12 brace with "no defenders"; the landing on the
cold-open frame, now with the test's formula beside its 17/42 marker.

## Round 6 revisions

Reviews: `reviews/round6-craft.md` (8.5) and `reviews/round6-substance.md` (8.6). No caps, no
factual errors (substance re-derived every number and checked every citation). Both say all fixes
together reach 9 "narrowly" with no structural change; both name the payoff (2:14–3:10) as the
weak minute and the 1:36–1:47 "fewer rows, fewer votes" step as the one asserted link.

**Climb plan (BAR §3 "9" anchor → shortfall → upgrade)**
- *Clarity 8.5* ("re-derive it after one watch"): 17/42 arrived as a parked number after "fewer
  rows, fewer votes" (a row count, not the dilution); the payoff showed nine numbers and three
  axis states in 49 s plus an uncounted simulated record; the landing dot read as "this row is
  hot". → Count the votes on the strip (yellow 5⅔ votes, grey 8⅓ votes), carry 5⅔ and the 14
  vote outlines into 5⅔/14 = 17/42; "Crowded heads split their votes" with the five third-vote
  slices pulsing; cut the record and the 40–60% zoom (one share axis, then the difference axis on
  the same tick marks); write 49 − 45 = +4 from Cornell's own numbers; landing row dims, the dot
  gets an "average over rows" tag.
- *Visual 8 / 8.5* ("one focal point; nothing to remove"): the 1:37–1:44 frame had ~8 groups at
  full strength; left-heavy payoff after the right column left; ink "hot" arrows (ink = the
  assumption); a near-invisible landing ghost; "Cornell, 1985" over non-Cornell data; GVT's
  citation dimmed under GVT's own numbers. → Dim rows without a checked heads (then tails), the
  pooled strip, its formula and "the obvious guess" while each count is made; the chart re-centres
  on x = 0 when the right column goes; "hot" arrows blue (the test's reading); landing ghost at
  coin radius 0.15 / 60% in the cold-open layout; header "1985 design · 26 players · up to 100
  shots" in grey until Cornell's 49/45, then purple "Cornell, 1985"; GVT bright with its data,
  citations never dimmed after that.
- *Motion 8.5* ("every motion encodes a relation"): 49/45 copies superposed then shrank to debris;
  the regroup tiles crossed the 40.5% label; 14 row ratios flew as 20 px debris; doubled H at 0:04.9.
  → 49 and 45 fly whole into "49 − 45", "= +4" lands as the marker grows; labels step back while
  tiles pass; one HHHH 3/3 at table size becomes hᵢ/nᵢ while all 14 ratios answer in place;
  copies that leave their source fade in as they leave (`emerge`), so no glyph is ever doubled.
- *Audio 8.5*: the 1:36–1:53 run was heard as one sentence → split into four clips (lineup, split,
  pack, formula) with 0.5–0.65 s gaps; holds of 0.8 s after "minus eight points." and "no hot hand."
- *Concision 8.5*: the record (10 s teaching the ring rule twice) and the zoom are cut; the hook's
  procedure is shortened to "Do this for every four flip run, and average."
- *Hook 8.5*: the prediction prompt is one instruction shorter; the big row fades while the
  sixteen-run ghost (now readable, r = 0.15) deals, so the viewer looks at one thing.
- *Originality 8.5–9*: unchanged ideas (keep items) made sharper by the vote count.

**Fixes, by critic item** (r6c = round-6 craft, r6s = round-6 substance). The first pass (11:35–
14:45) applied every listed fix; this continuation re-rendered, stepped every changed transition at
4–10 fps and fixed the motion defects that the sampled frames still showed.
- r6c 1 / r6s 2 (crowding → 17/42 asserted): "Twelve heads crowd into eight rows" boxes the 8 rows
  while the 6 rows without a checked heads, the pooled strip, its formula and "the obvious guess"
  dim to 30%; the dimming swaps for the 11 tails rows. "Crowded heads split their votes" keeps only
  HHHH and HHHT bright and pulses their five third-of-a-vote slices. "Line them up: the heads hold
  five and two thirds of the fourteen votes" writes "5⅔ votes" over the packed yellow and "8⅓
  votes" over the grey; 5⅔ travels to the right column, the 14 vote outlines fly into the 14, and
  on "That's" "= 17/42" slides in beside 5⅔/14. (The first pass carried 5⅔/14 into 17/42 as a
  cross-fade: stepped at 7.5 fps it read "5⅔⅔ / 144" for 0.4 s, so nothing flies there now.)
- r6c 2 (49/45 superposed, then debris): copies of 49 and 45 start invisible and travel whole to
  the right of Cornell's marker as "49 − 45"; "= +4" lands as the marker grows. New: the equation is
  no longer shed when the chart re-centres (the first pass faded "49 − 45 =" while "+4" slid left
  through it, a glyph collision at 3:05.6); it travels with its marker and stays under the +12
  brace, with "no defenders" beneath it.
- r6c 3 (left-heavy payoff): the chart, its markers and the equation re-centre by +1.4 on
  "Measured from minus eight", under the centred title.
- r6c 4 (tiles through the 40.5% label): "40.5%" and "the obvious guess" step back to 25% while
  the tiles regroup and return on "however many flips it checked".
- r6c 5 (invisible landing ghost): the sixteen-run ghost returns in the cold open's place and size
  (coin radius 0.15, 60%) and is held ≈ 1 s before its 14 scored rows fly into (1/14) Σ hᵢ/nᵢ.
- r6c 6 (ink "hot" arrows): both are blue, the test's reading; ink stays the assumption.
- r6c 7 / r6s 7 (doubled glyphs at 0:04.9 and 1:50): new `travel()` helper: a copy moves whole
  along a routed Bezier, fading in as it leaves its source and out before its replacement appears.
  The cold open's heads disc and both rings now materialise just *below* the row (while the coin
  and its rings answer) and travel under it into the 1 and the 2 (the first pass still showed a
  full-opacity disc sliding across the H and T coins at 0:04.8; a first reroute still grazed them). The
  row-ratio step is one HHHH "3/3" at table size that comes down onto the empty hᵢ/nᵢ slot from
  above (the first pass's cross-fade crossed "1/14 Σ" at 1:52.4).
- r6c 8 / r6s 1 / r6s 6 (payoff density): the simulated record and the 40–60% zoom are cut; the
  46/54 cursors run on the 0–100% axis and the same tick marks are relabelled −10…+10.
- r6c 9 (run-on 1:36–1:53): four clips (lineup, split, pack, formula) with 0.5–0.9 s gaps. Whisper
  still prints that stretch as one unpunctuated segment (a decoding artefact: its word timings
  carry every full stop, "rows." 1:35.98, "eleven." 1:38.74, "votes." 1:40.58, "up." 1:42.56,
  "votes." 1:46.12, "42." 1:48.86, each followed by a 0.4–1.2 s pause).
- r6c 10 (hook): "Do this for every four flip run, and average."; the big row fades to 40% while
  the 16 ghost runs (r 0.15) deal, then collapse into the "?".
- r6s 3 (landing): on "who averages one half on this test" the row dims to 30% and the blue dot is
  tagged "its rows average 1/2"; the "hot" arrow starts at the 17/42 marker; ≥ 2 s hold.
- r6s 4 (header over non-Cornell data): grey "1985 design · 26 players · up to 100 shots", each
  phrase joining only after the header has slid aside (the first pass let "26 players" fade in on
  top of the still-moving "design" at 2:18.7); the grey header fades out and only then the purple
  "Cornell, 1985" fades in (no cross-fade).
- r6s 5 (GVT citation dimmed under its own data): GVT's line is at full strength from "The Cornell
  players" on; M&S steps back while 49 − 45 = +4 is read; both full from "Measured from minus eight".

**Other motion defects found by stepping frames (not in the reviews)**
- 0:42–0:44 HHHT: disc and ring copies flew through the tight row; now the three rings flash as
  "/3" is written and the two ringed heads pulse as the "2" is written (nothing flies).
- 1:12–1:13: 14 numerator and 14 denominator copies left their table digits (doubled "3̶3") and
  crossed the table as 20 px debris; now the digits pulse in place (about the edge away from the
  slash) while Σᵢhᵢ and then Σᵢnᵢ are written.
- 1:55: the Σ pulses (×1.35 about their centres) grew into the fraction bar and hᵢ; now ×1.25 about
  the corner facing away from their neighbours, and 1/14 Σ grows leftwards.
- 3:15.4–3:16.6: the payoff faded to a lone −10…+10 axis for 0.5 s before the cold open returned;
  now one 1.3 s move (payoff fades in its first third while the line and dashed zero drop into the
  share axis and the row fades back in).
- 3:21: the marker's copy into "17/42" read as a doubled marker line; now the marker flashes and
  "17/42" slides out of it to the left.
- "Now score the flip after each tails…" was the one sentence above 200 wpm: the mirror beat is
  read at 0.80.

**Self-review loop.** Two 1080p masters (after the continuation's fixes, then after the frame check),
each followed by review_kit and frame strips at 4–10 fps across every changed transition (0:04,
0:42, 1:12, 1:46, 1:52, 1:55, 2:18–2:22, 2:54, 3:06, 3:15, 3:21). Found in the first master and
fixed in the second: the cold-open copies, materialising on their own coins, still grazed the T and
the last H; the landing's payoff-to-cold-open move still showed a lone axis for ~0.3 s; the marker
copy into 17/42 read as a doubled line.

**Mechanics (final master):** 3:32.7, 151 wpm over speech time (498 words, budget ≤ 500), voice
0.82 (0.80 for six short-sentence beats), 0 sentences above 200 wpm, −14.0 LUFS / −1.9 dBTP,
leading silence 0.00 s, trailing 1.88 s, longest silence 2.17 s (the planned prediction hold),
longest static stretch 3.6 s, 0 render warnings, 0 layout-audit issues in 220 checks, 0 glyph
morphs, 7/7 deictics landed, 0 review flags, WER 0.8% (only "a" heard as "one" twice and "a half"
as "point five"), no banned phrases. `check_numbers.py` re-run: every value on screen unchanged.

**Kept:** the one-vote strip (now with its vote counts), "test the test" → live 50% → 40.5% →
"cold −9.5 points", the half-turn mirror into −19, and the landing on the cold-open frame with the
test's formula beside its 17/42 marker.

## Round 7 revisions

Both critics scored 8.8 (Hook 9, Clarity 9, Visual 8.5, Motion 8.5, Audio 8.5, Concision 8.5,
Originality 9), with no caps and no factual errors. Both said every listed fix together reaches 9.
The plan per dimension below 9 was: Visual needed one focal point in 1:19–1:35, 17/42 shown when
spoken, and one "Cornell" label. Motion needed a visible rescale, equation holds, and no doubled
copies in flight. Audio needed breaths in the lineup run. Concision needed the two restating lines
and the streak-length aside cut.

**Fixes, by critic item** (r7c = craft, r7s = substance)
- r7c 1 / r7s 3 (no focal point at 1:19–1:35): on "each row gets one vote" the whole table, the
  pooled strip, Σᵢhᵢ/Σᵢnᵢ = 12/24 and "the obvious guess" go to 30%, and the 40.5% readout to 25%.
  They work through a row-level system (`rows_to`) that always restores from the saved full state,
  so dimming never compounds. A row comes back only while it is named:
  - HHHH from "since a heads gets the next flip checked too";
  - HTTT on "this lone tails";
  - the 8 heads rows, then the 11 tails rows, during the lineup;
  - HHHH and HHHT on "split".

  The 14 denominators flash on "however many flips it checked". The readout comes back as the
  heads pack onto its marker. The pooled strip and its formula come back on "the ratio of totals".
- r7c 2 / r7s 1 (17/42 spoken but not shown at 0:57): the marker now settles on "seventeen", and
  "17/42 =" is written beside the readout, which then reads "17/42 = 40.5%". It rides left with the
  axis at 1:05 and leaves at "Gather" (1:07). It sits left of the readout, not under it: under it,
  it would have collided with "cold −9.5 points". That label was also moved 0.1 lower.
- r7c 3 / r7s 5 (hidden rescale at 2:44): the rescale is now shown as a real zoom.
  - On "twenty eighteen paper" the pair slides until after-misses sits on 50%.
  - On "puts the gap" (after a new [pause 0.5]) the red gap gets its number, "−8".
  - On "at about minus eight points" the axis zooms ×5 about the dashed line (2.0 s, smooth).
    The 0/25/75/100% ticks run outward and leave, and −10/−5/+5/+10 grow out of the centre onto the
    same five tick positions (asserted). "50%" hands over to "0". The cursor carries its "−8" to −8,
    and the gap stretches into the "bias" arrow.

  The factor is ×5, not ×10: the 8-point gap was 0.72 units on the share axis, and the gap axis
  uses 0.45 units per point (facts row 45).
- r7c 4 / r7s 2 (equation cadence 1:46–1:56): 5⅔ / 14 = 17/42 is held complete for ≥ 3.25 s
  (asserted by a hold). Σᵢhᵢ/Σᵢnᵢ stays dimmed through the Σ build and brightens on "ratio of
  totals", so it no longer arrives as a third equation. 5⅔/14 = 17/42 and (1/14)Σᵢhᵢ/nᵢ = 17/42
  now complete about 7 s apart.
- r7c 5 / r7s 2 (lineup run-on): about 1.0 s of silence after "split their votes" (gap 0.9),
  [pause 0.8] after "Line them up:", [pause 1.0] after "the fourteen votes", and about 1.6 s after
  "That's seventeen out of forty two".
- r7c 6 / r7s 6 (concision): cut "Score every row the same way." (the cascade now runs in a
  [pause 1.0]). Cut "Longer streaks grow the bias." along with the 1- and 2-hit ghosts and their
  legend. One ghost of the −8 marker now slides to 1,000 shots on "Longer records shrink it". Also
  cut "a fair coin shows" from the −19 line, and trimmed six gaps by 0.1–0.15 s to pay for the new
  pauses.
- r7c 7 (copy across the after-tails strip): no copy. The after-tails heads part flashes in place
  (vertically, so it never grows into its cursor) while "25/42" is written.
- r7c 8 / r7s 7 (doubled vote outlines in flight):
  - On "fourteen" the outlines are counted in place (each one answers in turn) while "14" is
    written.
  - On "an average" the outlines themselves fly, with no copies. They shrink and step back to 40%
    as they lift, then run between the strips into 1/14 Σ (lag 0.08).

  Also new: the HHHH "3/3" copy that flew to hᵢ/nᵢ showed "3/3/3" over its source while it
  materialised. Now all 14 row ratios answer in place while hᵢ/nᵢ is written.
- r7c 9 / r7s 8 (landing ghost): the ghost deals in at 75% (the cold open's ghost too, for the
  rhyme) on "is what a fair coin does". The dashed guess steps back to 25%. The ghost is held
  ≈ 1.8 s (landing pause 0.8), then the rows fly one after another (lag 0.06). The marker draws
  only after the rows have passed. The dashed line returns to full on "A fifty percent shooter".
- r7c 10 (Cornell printed twice): the purple header "Cornell, 1985" itself travels on an arc to
  tag the +4 marker, and the column head "Cornell" leaves, so "Cornell" is printed once.
- r7c 11 (HHHH box 2 px from the rings): the HHHH and HTTT boxes take in the rings and sit 0.13
  clear of them.
- r7s 4 (GVT's significance logic omitted): the line is now "The study found plus four, too close
  to zero to count, so no hot hand." On "zero" the dashed zero line pulses and a grey
  "vs 0: p = .49" appears under "49 − 45 = +4". It was re-verified this round: M&S 2018 §3.1 says
  "GVT's paired t-test finds the difference to be statistically indistinguishable from zero, and
  we replicate this result (p=.49)". Since the p-value is M&S's replication, their citation now
  stays at full strength while it shows (facts row 43).
- r7s 9 (cold-open breath): [pause 0.3] after "check the next flip:" and after "one of the two is
  heads." The question still lands by 0:12.8.

**Found by stepping frames (not in the reviews)**
- In the first preview, the zoom's helper group pulled the −8 marker, its number, the bias arrow
  and the new tick labels out of the scene's top level. All four vanished for 20 s after the zoom.
  The cleanup now re-adds them, and the five tick marks, as one group.
- Moving the header along a Bezier through one absolute point bunched its glyphs mid-flight. It
  now moves rigidly on an arc.
- On the first master, the vote outlines left left-to-right, so each one in flight crossed the
  outlines still waiting on the strip (1:51.8). The right-most now leaves first.
- On the first master, "the obvious guess" was still fading while the landing ghost dealt in
  under it (3:17). It now leaves in the first 0.25 s.
- The p-value label is now MathTex 32 (31 px; citation-level text, above the 24 px floor).

**Self-review loop.** Two previews and two 1080p masters. After each one I ran review_kit and
stepped frames at 2.5–5 fps across every changed transition: 0:55–0:58, 1:17–1:33, 1:44–1:53,
2:06, 2:42–2:47, 3:00–3:06 and 3:15–3:21. Everything listed under "Found by stepping frames" was
caught this way and fixed before the final master.

**Mechanics (final master):**
- Runtime 3:31.0 (was 3:32.7). 487 words, 150 wpm over speech time. Voice 0.82, with 0.80 for six
  beats. 0 sentences above 200 wpm.
- −14.1 LUFS / −2.1 dBTP. Leading silence 0.00 s, trailing 1.74 s. Longest silence 2.17 s (the
  prediction hold). Longest static stretch 3.5 s (the held 5⅔/14 = 17/42 and the +12 frame).
- Longest stretch without a breath 13.3 s (was 12.1 s, now at 2:50).
- 0 render warnings, 0 layout-audit issues in 227 checks, 0 glyph morphs, 7/7 deictics landed,
  0 review flags, WER 1.1%, no banned phrases.

Whisper still prints 1:37.6–1:50.5 as one unpunctuated segment. Its word timings and the measured
silences carry every stop: 1:40.0–1:41.0 (1.0 s), 1:41.9–1:42.8 (0.9 s), 1:46.0–1:47.1 (1.1 s),
1:49.3–1:50.9 (1.6 s). This is a decoding artefact, not a run-on.

`check_numbers.py` was re-run, and every value on screen is unchanged.

**Kept:** the one-vote strip packing onto the 40.5% marker (the same animation, now with a breath before it); "test the
test" → live 50% → 40.5% → "cold −9.5 points"; the half-turn mirror into −19; and the landing on
the cold-open frame, with the ghost flying into (1/14) Σᵢ hᵢ/nᵢ = 17/42 and the blue "hot" arrow.

## Round 8 revisions

Craft scored 8.9 (Motion 8.5, Concision 8.5, the rest 9) and substance 8.8 (Clarity, Motion and
Concision 8.5), with no caps and no factual errors; both said the listed fixes reach 9 with no
structural change. The plan per dimension below 9:
- **Motion / Clarity (both critics' fix 1):** the frame at 2:41–2:44 drew the after-hits cursor at
  42% on an axis still labelled in %, beside a "46%" readout. The 9 anchor ("every frame true if
  paused", "every motion encodes a relation") needs a gap that is re-anchored, not cursors that
  are moved, and an axis that is labelled at every instant of the zoom.
- **Clarity (substance fix 2):** "but a hundred shots isn't long" gave the wrong cause for −8. The
  viewer's own one-heads version is −1.0 at 100 shots; the streak length is what keeps it at −8.
- **Concision:** two restatements ("The skew comes from scoring row by row", "Crowded heads split
  their votes").

**Fixes, by critic item** (r8c = craft, r8s = substance)
- r8c 1 / r8s 1 (cursors at 42% / 50% on a % axis, 2:41–2:44): the pair no longer slides. The
  cursors stay on 46% and 54% until they fade where they stand. On "puts the gap" the red gap
  between them gets "−8" and slides 4 points left until its tail sits on the dashed 50% line (a
  difference measured from the line, with no cursor at its tip). On "at about minus eight points"
  the ×5 zoom about the dashed line stretches that arrow to −8. Only after the zoom does the blue
  random-shooter marker grow, at the arrow's tip, with "random shooter" and "bias". No frame shows
  a cursor at a share its label contradicts (facts row 50).
- r8c 5 / r8s 8 (axis unlabelled mid-zoom): the zoom is one rig, drawn once, so no label is
  double-drawn at partial opacity. 0% and 100% leave in the first 0.2 s. 25% and 75% fall to 40%
  and stay there while −10, −5, +5 and +10 grow in on their own marks (never on the same spot).
  "50%" hands over to "0" while the outer labels carry the axis. The share title drifts right and
  fades while the gap title "after-hits − after-misses (points)" arrives at the axis's left end, so
  the two titles cross-fade in time without sharing a place (a cross-fade in place reads as garbled
  text, §13.2.5). Every frame of the zoom has tick labels and a title.
- r8s 2 (wrong cause for −8): "Longer records shrink it, but a hundred shots isn't long" is now
  "Longer records shrink it; longer streaks grow it." (M&S abstract, re-checked). On "records" the
  ghost of the −8 marker slides to −0.71 ("1,000 shots") while the header's "up to 100 shots"
  answers. On "longer streaks" that ghost leaves, and a ghost at the one-hit gap (−1.01) with one
  yellow dot gains a dot and slides to −3.14, then gains a third and lands under −8 (−7.94), exact
  DP for 100 shots (facts rows 47–49). Round 7 had cut this clause with its three ghost ticks and
  legend; it returns as one ghost and seven words.
- r8c 2 (concision): cut "Crowded heads split their votes." and its 0.9 s gap. On "Line them up:"
  HHHH and HHHT come forward while their five third-of-a-vote slices pulse, then the votes pack.
- r8s 3 (concision): cut "The skew comes from scoring row by row:"; the beat is now "But each row
  gets one vote, however many flips it checked." The regroup runs on "But each row", the resize to
  equal votes lands on "vote".
- r8s 4 (vote strip never named): grey "1 vote per row" (Text 26) above the strip's left end, 0.27
  clear of the 40.5% readout, from "one vote" until the pack, when the readout returns beside it.
- r8s 5 (six numbers in 14 s): [pause 0.6] after "forty five after three misses" (49 − 45 is
  written in it) and [pause 0.4] after "plus four" (the purple marker and "= +4" land in it).
- r8s 6 (copies over other rows at 1:06): each checked flip now pours as a small disc of its
  tile's colour. It appears in the gap just under its own coin, runs left along that gap to its
  card's edge, down the channel between cards, and along the corridor under the table into its
  tile (rounded-corner routes, `route()`). No copy passes over a coin.
- r8s 7 (header vs lanes at 2:15): the lanes ("after 3 hits / after 3 misses") and the axis title
  ("checked shots that are hits") change in the same 1.2 s move that brings in "1985 design"; the
  ●●● / ○○○ conditions arrive on "the same comparison".
- r8c 4 ("Cornell" printed twice, 2:51–3:04): no purple "Cornell, 1985" title. The grey "1985
  design" header stays, the column head turns from "random" to "Cornell", and on "Measured from
  minus eight" that head itself arcs up and over to tag the +4 marker while the header leaves.
- r8c 3 (landing rows bunched): the rows themselves leave one after another, left-most column
  first (lag 0.22, about four in flight and spread along the arc), each stepping back to 40% as it
  lifts and arcing up and over into (1/14) Σᵢ hᵢ/nᵢ. "= 17/42" now lands on "this test", so the
  separate pulse after it is gone.

**Found by stepping frames (not in the reviews)**
- The 14 score dots at 0:52 flew diagonally over the table rows, the same defect as r8s 6. They
  now run down the channel beside their card and along a corridor under the table before
  dropping to the line; the one 2/3 dot goes round the right end of "the obvious guess".
- On the preview "1 vote per row" and the returning "40.5%" read as one phrase for 0.7 s
  during the pack ("1 vote per row 40.5%"). The tag now leaves as the readout comes back.
- The landing rows at scale 0.3 were too small to read as rows in flight; they now shrink to 0.4.

**Self-review loop.** One preview and three 1080p masters (the third only re-routes the 0:52 dots;
the 50% dots no longer detour round "the obvious guess"). After each one I stepped frames at
2.4–5 fps across every changed transition: 0:52–0:54, 1:05.4–1:08.4, 1:14.4–1:18.4,
1:35.5–1:37.9, 2:09.8–2:11.4, 2:37.4–2:45.4, 2:45.6–2:46.8, 3:00–3:01.6 and 3:14.7–3:17.9. I
also read all 12 contact sheets and the keyframes at 1:18.9, 1:37.6, 2:42.5, 2:47.2, 3:05.1 and
3:26.6.

**Mechanics (final master):**
- Runtime 3:26.6 (was 3:31.0). 473 words (was 487), 149 wpm over speech time. Voice 0.82, with 0.80
  for six beats. 0 sentences above 200 wpm.
- −14.0 LUFS / −2.1 dBTP. Leading silence 0.00 s, trailing 1.74 s. Longest silence 2.17 s (the
  prediction hold). Longest static stretch 3.4 s (the held 5⅔/14 = 17/42).
- Longest stretch without a breath 11.2 s (was 13.3 s).
- 0 render warnings, 0 layout-audit issues in 220 checks, 0 glyph morphs, 7/7 deictics landed,
  0 review flags, WER 0.7%, no banned phrases.

`check_numbers.py` was re-run; every value on screen is unchanged, and the three streak-ghost
positions (−1.01, −3.14, −7.94) and the 1,000-shot position (−0.71) are its exact DP output.

**Kept:** the yellow vote slices packing exactly onto the 40.5% marker into 5⅔/14 = 17/42; the
half-turn mirror of the vote strip into −19; the landing that answers the cold-open question on
the cold-open image with (1/14) Σᵢ hᵢ/nᵢ = 17/42 and the blue "hot" arrow; the payoff chain
−8 → 49 − 45 = +4 → +12 with "vs 0: p = .49", "no defenders" and both citations at full strength.
