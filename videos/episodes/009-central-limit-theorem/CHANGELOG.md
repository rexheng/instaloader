# Episode 9 changelog

## Round 1 revisions

Round-1 critics: craft 8.0, substance 8.1 (no caps). Every fix from both reviews was applied;
the three "keep" items (semantic palette, the cold-open frame rebuilt at the landing with the
bell moved into the average, the live lighthouse with flash 841 yanking the mean while the
median stays flat) are unchanged. Runtime 3:02 -> about 3:46 (561 words, about 152 wpm).

**Facts (both claims re-verified against the Kohavi et al. 2014 PDF)**
- 355 · 5.2^2 is 9,599, so the screen and the log-axis marker now read ~ 9,600 (was 9,700, the
  paper's value from an unrounded skewness). Narration "under ten thousand" is unchanged.
- The textbook paraphrase keeps Montgomery's hedge: "thirty is usually enough, whatever the shape".
- Fail-chart bar labels show 1.90 / 1.96 / 2.00 / 1.98 (the third value is 2.0047, which rounds to 2.00).

**Hook and stakes**
- Stakes now seed the payoff: "Textbooks say thirty is usually enough, and A-B tests lean on
  that bell. On revenue data, thirty is off by a factor of thousands", with a gray "n >= 30 ?" under
  the A/B glyph. The glyph leaves on "So collect".
- "this tail" now has a referent: a gray "tail" brace over 20-45 min, with the 0-20 min bars dimmed.

**Clarity (the four explanatory gaps)**
- Averaging is slow and named: four chips (25.7 in red) arc into a spaced row and hold; the
  narration says "the one long wait gets diluted by three short ones"; the chips become
  (5.2+1.8+25.7+5.3)/4 = 9.5 with a yellow 9.5 chip, held about 1.8 s, then drop into panel 2.
  This was paid for by cutting "Each panel zooms in...".
- Skewness is defined term by term ("the average cubed distance from the mean, over the spread
  cubed"), built from a mean line and an x - mu arrow on the histogram. It is no longer a FadeIn.
- Why root n: a new beat expands the formula to n/n^{3/2} · E[(x-mu)^3]/sigma^3 = skew(x)/sqrt(n)
  ("the cubed distances grow n times, but the spread cubed grows n to the one and a half").
- 0.37 is now measured in the tails: the n = 16 panel grows into an exact n = 30 panel with
  95% cut lines, green 2.5% tails and live yellow tail shares 1.40% / 3.40%. Kohavi's criterion
  (each tail 2-3%) is shown as a gray band; at 1,420 the panel morphs and the tails read
  2.35% / 2.64%, inside the band. This resolves "0.25 is nearly a bell, yet 0.37 fails".
- The 355 s^2 <=> 0.053 equivalence is shown as algebra: n >= 355 skew^2 -> skew^2/n <= 1/355 ->
  skew/sqrt(n) <= 1/sqrt(355) ~ 0.053, with exact constants on screen.
- Cauchy spread is shown, not asserted: 200 yellow dots (each an average of 1,000 simulated flashes)
  on a second line, with counts beyond each edge. Both "middle half" brackets grow from their own
  quartile dots (single flashes -1.08 to 0.90; averages -0.99 to 1.02). Narration: "Half of single
  flashes land within a mile of the middle. Repeat the thousand-flash average two hundred times,
  and still only half do."
- Coin beat: the panels get their own labels (tails/heads, "share of heads"), and
  2.67/sqrt(64) = 0.33 is built from the coin's reading, the header and the result.
- Bing line rewritten without the garden path: "Capping each user's revenue at ten dollars a
  week dropped the skewness to about five, [pause] and the users needed to under ten thousand."

**Visual and motion**
- Transition into the panel row is sequential: the old axes fade, the bars alone shrink into
  panel 1, and the 1.98 bar label flies into "skew = 1.98".
- The general formula is assembled without glyph shatter: the values fade, the four 2s, bars
  and radicals converge, "skew(x-bar) =" slides in, and the 2 becomes skew(x). The formula is
  centred at x = 0.
- Panels are 12% wider and 15% taller. Windows are mean -3.5 SD to +4 SD, so every bell is whole.
- The ÷2 arrows are shortened (0.27 units clear of each reading).
- The capped marker: only the dot travels, along an arc, and its label fades in at the
  destination. There is no doubled "Bing revenue" text.
- The duplicate "textbook: n >= 30" text is removed; the gray log-axis marker remains.
  Citations are shortened so they clear the axis title.
- Lighthouse: the upper y label is now "running value (miles)". On "infinite", the 902/1,000
  label, jump bracket, ghost circle, brackets and strip dim to 30%; on "median" the yellow
  trace dims to 40%. A dimming helper keeps curves unfilled.
- The counter cross-fades instead of morphing glyphs.

- The log-axis markers (1,420 and 114,000) rise from their dots while the source number
  flashes, so no number flies across the inequality.
- The landing is a single 1 s dissolve into the rebuilt cold-open frame, with no dip to an
  empty frame. The guessed dashed bell fades as the real green bell is traced over the
  average-of-64 histogram, with no dash-to-curve morph.

**Audio**
- "Kohavi's" now has a whole-token override /kOhˈɑviz/; the old override dropped the
  possessive into a separate token, which whisper heard as "Cohave's". The narration now says
  "Ron Kohavi's team", which whisper transcribes correctly. Four whisper tests were run on
  variants; only the two with the first name passed.

**Verification**: render.sh showed no warnings. The review_kit flags nothing: 3:46.5, 157 wpm,
-14.0 LUFS / -1.6 dBTP, longest silence 1.97 s, longest static stretch 3.03 s, WER 3.4%,
no banned phrases. Every transition I changed was checked with 0.3-0.6 s frame strips.

## Round 2 revisions

Round-2 critics: craft 8.0, substance 8.2 (no caps, no wrong numbers). Every fix from both reviews
was applied (one deliberate exception below). The three "keep" items survive: the landing rebuilds
the cold-open frame and grows the real bell where the guessed one stood ("The bell was never in the
data. It's in the average."); the live lighthouse (902-mile flash yanking the mean, matching
middle-half brackets, purple median); Kohavi's 355·s² rule rearranged into skew/√n ≤ 0.053 with the
log-axis markers. Runtime 3:46 -> 3:54.9 (about 595 words, 158 wpm over speech).

**Plan of the climb (guide §12), by dimension below 9**
- Hook (8.5/8.5). 9 = "commits to a likely-wrong prediction by 0:12; the ending resolves the
  opening exactly". "Will this shape turn into a bell?" was easy to answer no, and "It's tempting to
  say yes" gave it away. Now the cold open asks the number: "Textbooks say the average of thirty is
  safe to treat as a bell. Does it really take thirty, three hundred, or over a thousand?" (three
  gray chips, 1.5 s hold, question ends 0:12.4). The landing rebuilds that frame, lights the 1,000+
  chip, relabels the arrow "average of 1,420" and grows 10,000 simulated averages of 1,420 waits
  under a solid green bell where the guess stood.
- Clarity (8/8). Root n is now drawn; the CLT is no longer equated with the skew rule; the spoken
  and on-screen thresholds agree; "distance" became a signed gap.
- Visual (7.5/8), Motion (7.5/8), Audio and Concision (8/8): itemized below.

**Facts and wording (substance)**
- The CLT step: "Kurtosis, the extra tail weight, fades faster, as one over n, and every finer
  difference faster still. Only the bell survives. That's the central limit theorem." On screen
  kurt(x̄) = kurt(x)/n is built from a copy of skew(x̄) = skew(x)/√n (excess kurtosis; exponential
  6 -> 1.5 -> 0.375 -> 0.094, coin 5.11 -> 0.080, all exact; facts.md has the cumulant argument).
- "asking for a skewness under point oh five" -> "the average's skewness at most point oh five
  three" (1/√355 = 0.0531; n = 1,420 gives exactly that).
- "the average cubed distance" -> "the average cubed gap from the mean, left gaps counting
  negative", with a leftward blue "x − μ < 0" arrow flashed on "negative".
- "Ron Kohavi's team at Microsoft" -> "Ron Kohavi and colleagues, using Bing's data" (two of the four
  authors were elsewhere at publication; the citation still names all four).
- The second textbook line is now "Back to the textbook's thirty."; the Bing cap is one clause
  ("Capping each user at ten dollars a week cut that to under ten thousand").

**Root n, drawn (craft fix 1)**: on "Add four waits" one blue block grows out of E[(x−μ)³] and one
gray block out of σ³; the blue stacks to 4 ("×4"), the gray to 8 ("×8") on "its cube grows eight
times", the ÷2 arrow between 1.98 and 0.99 flags on "half the lean", and on "In general" the labels
become ×n and ×n^{3/2} and fly into the blank as n/n^{3/2}. The full expansion holds about 5.5 s.

**Visual**
- Lighthouse: axis titles are "miles"; one "simulated" tag (bottom right); the "lighthouse" label
  leaves once the trace starts; on "Half of single flashes" the 902-mile beam, "902 mi", "902 ÷ 1,000
  ≈ 0.9 mi", the ghost circle and the jump bracket fade (the red jump dot stays and flags on "single
  piece"). The running-average label carries an opaque background so the zero line never crosses it.
- Tail asymmetry is a shape: a tail meter beside the n = 30 panel; each tail flashes and its bars
  flow into one meter bar (1.40% left, 3.40% right) against a green dashed 2.5% line; Kohavi's
  2–3% band is drawn on it, and at n = 1,420 both bars move inside it (2.35% / 2.64%).
- Coin beat: on "A coin" the ×4 and ÷2 arrows and panels 2–3 leave entirely (no false "2.67 ÷2 →
  0.99" relation). "central limit theorem" is set large (Text 44, INK) at the top centre with
  "independent pieces + one condition" as one line under it; skew(x̄) and kurt(x̄) sit below.
- Y-axis quantities: "share" on the panel row, "share of averages" on the n = 30 panel, plus an
  "exact" tag there. Log-axis markers are INK dots and values with gray names; blue stays on skew(x).
- The skewness chart moved 0.35 right, clear of the histogram's 50 tick; bar labels, the gap brace,
  the ÷2 labels and the marker names all clear 0.15 (layout audit: 0 issues).

**Motion**
- No data bar ever changes height: every bar flag is a brightness flash; "lopsided" at the landing
  is the gray "tail" brace over 20–45 min with the body dimmed.
- The landing axis is fresh ("minutes", ticks 9.5/10.0/10.5, faded in, never drawn stroke by stroke).
- The landing transition: the lighthouse fades first and the cold-open frame second (no double
  exposure), while the shore line itself slides into the waits axis, so no frame is empty. The
  lighthouse entry likewise draws the shore and the lamp while the payoff fades.
- The finished landing image holds about 2.4 s; no end card (trailing silence 1.9 s).
- Kohavi algebra: the rule's copy arcs down to its row, then becomes skew²/n ≤ 1/355, which holds
  about 2.5 s ("Divide by n and take the root:" plus a pause) before skew/√n ≤ 1/√355 ≈ 0.053, which
  flags together with the top skew(x̄) formula.
- Formula copies (2/√30, the definition, kurt) first arc away from their source, so no frame shows a
  doubled formula. The 1.98 reading travels at full size along the readings row while the panels fade
  in; the chips arc away from it.
- The stills at 2:18 (Kohavi beat start) get a tail flash on "each tail".

**Audio**: "bus waits" on the two key lines; "Repeat ten thousand times" -> "Do that ten thousand
times"; "we'll get to" -> "and one more condition". The opening question was rephrased after a
whisper test showed the colon version transcribing as two questions.

**Deliberate exception**: "and both tails land inside" is kept (substance fix 3 suggested cutting it)
because it narrates the 1.5 s morph in which both meter bars move into the 2–3% band; the clause adds
no new number. Fix 3's other half (the shorter Bing cap) is applied.

**Verification**: render.sh: 0 warnings, layout audit 0 issues (2 allowed: a moving beam crossing
"1 mi" for one frame). review_kit: 3:54.9, 158 wpm, −14.0 LUFS / −1.6 dBTP, longest silence 2.0 s
(the prediction hold), longest still 3.8 s (prediction hold; nothing else over 3 s), trailing 1.9 s,
WER 3.1%, 0 flags, no banned phrases or patterns.
All contact sheets and the keyframes around every fixed timestamp were inspected, plus 0.25–0.5 s
frame strips across the changed transitions.

## Round 3 revisions

Round-3 critics: craft 8.6, substance 8.1 (no caps). Every fix from both reviews was applied. The
"keep" items survive unchanged in substance: the 30 / 300 / 1,000+ cold open answered on the same
frame at the landing ("average of 1,420", the real bell, "The bell was never in the data. It's in
the average."); the panel row whose x4 / /2 arrows and per-panel 2/sqrt(n) converge into
skew(x-bar) = skew(x)/sqrt(n); Kohavi's 355 s^2 rearranged into skew/sqrt(n) <= 0.053 with the log
sample-size axis (now 30 -> 300 -> 1,420 -> 114,000 -> 9,600) and a meter that turns the asymmetry
into a shape; the lighthouse run.

**Plan of the climb (guide §12), by dimension below 9**
- Clarity (8.5 / 7.5). 9 = "viewer could re-derive it after one watch; all numbers check out".
  The climax measured the wrong quantity (see Facts); the root-n picture asserted "the spread
  doubles"; "kurt" was excess kurtosis unlabelled. Fixes: the meter now measures what Kohavi's
  rule controls, the doubling is drawn, the label says "ex. kurt".
- Visual (8.5 / 8). 9 = "every frame has one focal point; nothing to remove". Fixes: no dangling
  equation (dashed slot), captioned cubes, labelled meter, rotated "share", lighthouse chart
  dimmed during the condition, two landing ticks.
- Motion (8.5 / 8.5). 9 = "every motion encodes a relation; reading time respected". Fixes: the
  formula opens in place (no orphan "=", no duplicate skew(x)); the 1,420 answer holds about 3 s;
  dissolves run in the pauses, crossfading at 30%.
- Audio (8 / 8). 9 = "pauses are intentional". Fixes: 0.27 s between sentences inside a beat,
  about 0.9 s at the seven story-beat boundaries; "waits for a bus"; "so so" gone.
- Concision (8.5 / 8). Restatements cut ("So the lean of an average is the lean of one piece, over
  root n"; the Bing cap line), which paid for the mechanism sentence and "Three hundred still
  misses". Runtime 3:54.9 -> about 3:53.
- Hook (9 / 8.5). "Does it really take thirty" telegraphed the answer; now "For these waits, does
  it take thirty, three hundred, or over a thousand?". Montgomery & Runger cited from 0:04.

**Facts (substance critic's factual-error claim: verified, fixed everywhere)**
- The round-2 meter showed the exact KNOWN-spread tails of x-bar (1.40% / 3.40% at n = 30). For
  that quantity the 2-3% band is reached near n = 130-150 (Gamma exact 1.99% / 2.96% at 130), so
  the picture did not support 1,420. Kohavi et al.'s 355 s^2 is the ESTIMATED-spread threshold:
  Deng, *Causal Inference and Its Applications in Online Industry* ch. 8.5 (re-read): "Kohavi et
  al. (2014) derived 355s2 based on similar calculation for the unknown variance case".
- The meter now shows the simulated miss rates of the 95% interval a test computes, x-bar -/+ 1.96
  s/sqrt(n) with the sample SD (sim.py, seeded): n = 30, 2,000,000 tests: 7.23% low / 0.98% high;
  n = 300: 3.66% / 1.72% (still outside the band); n = 1,420: 3.00% / 2.08% (on the band). These
  match the critic's run (7.21 / 1.00, 3.66 / 1.68, 3.00 / 2.09). With the t quantile n = 30 gives
  6.53% / 0.74%; facts.md records both.
- Narration: "But tests live in the tails: a ninety-five percent interval should miss two and a
  half percent on each side. Tests estimate the spread from the same data, so a low average gets a
  small spread, and its interval stops short. With thirty waits: seven percent low, one percent
  high." ... "Three hundred still misses. For these waits: fourteen twenty, and both misses reach
  the band." ("reach", not "inside": the low side sits on the 3% edge.)
- The mechanism is shown with one simulated test (seed 219: average 6.83, sample SD 6.47, the
  median SD for averages of 6.6-7.0): the interval its true spread would give (green dashed,
  3.25-10.41, covers mu) shrinks to its own (yellow, 4.51-9.14) and stops short of mu; it then
  flows into the meter's low bar. corr(average, SD) = 0.74 for tests of 30.
- On screen "ex. kurt(x-bar) = ex. kurt(x)/n" (excess kurtosis, true as written).

**Craft fixes**
1. Payoff hold: "[pause 1.2]" after "reach the band"; on "band" a green ring flashes around the
   bars and the band while the bars glow; the 1,420 state lands with its marker on "fourteen" and
   is fully lit about 2.9 s before the dim starts on "Bing's".
2. Formula opening: skew(x-bar) and "= skew(x)/sqrt(n)" slide to their final places in one move
   (nothing duplicated), "=" fades in, a dashed gray box holds the slot from the start, and the
   definition is written while skew(x) flags; x n and x n^{3/2} fly into the box (n blue,
   n^{3/2} gray: their cubes' colours).
3. Root n drawn: captioned "cubed gaps" (blue) and "spread^3" (gray); one blue cube -> four
   ("x4"); a gray bar sigma over the gray cube grows to 2 sigma ("x2") on "doubles"; the cube
   becomes 2 x 2 x 2 = 8 ("x8") on "cube grows eight times"; "In general" turns the labels into
   x n, x root n and x n^{3/2}.
4. Cadence: see Audio above (`GAP_AFTER` in narration_text.py; "[pause 0.15]" between sentences).
5. Lighthouse: on "finite variance" the running-average chart dims to 30% and "1 mi" fades; the
   chart returns on "median".
6. Meter labels: header "misses (simulated)", "low" / "high", green "2.5%" at the dashed line
   that becomes a gray "2-3%" beside the band.
7. Citations at 0:04 ("Montgomery & Runger, 2010") and 0:15-0:20 ("Kohavi et al., 2014 · KDD").
8. "A hundred waits for a bus" (whisper now hears it correctly) and "These waits for a bus".
9. Dissolves (2:52, 3:40) run in the pause before the next beat; the incoming scene starts when
   the outgoing one is at about 30%, so the lighthouse and the cold-open frame are whole before
   "Now the condition" and "So the answer"; the 1,000+ chip lights on "thousand".
10. "share" is rotated beside panel 1's y-axis (panels shifted 0.12 right); the coin panel keeps
    its y-axis.
11. Landing ticks 9.5 and 10.5 only.
Also: the payoff panel's labels are "share (exact)" and "average (minutes)" (12 prose words on the
busiest payoff frame); the Kohavi beat's 3.6 s still is broken by a flash of the tails and both
meter readings on "each side"; the general formula holds about 2 s before it opens on "comes".

**Verification**: render.sh 0 warnings, layout audit 0 issues (2 allowed beam crossings).
review_kit: 3:52.8, 161 wpm over speech (155 overall), -14.0 LUFS / -2.2 dBTP, longest silence
1.74 s (prediction hold), longest still 3.53 s (prediction hold; nothing else over 3 s), trailing
1.91 s, WER 2.9% (whisper still writes the homophone "weights" for some mid-episode "waits"; the
opening line now transcribes correctly), 0 flags, no banned phrases.
All 13 contact sheets and the keyframes around every fixed timestamp were inspected, plus 0.25-0.5
s frame strips across the formula opening, the cube build, the interval shrink, the 300 / 1,420
morphs and both dissolves.
