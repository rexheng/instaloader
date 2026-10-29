# Episode 75 — changelog

## Round 1 revisions

Round 1 review: craft 8.1, substance 8.3; neither passed. Both critics said the jump from ¼ to ⅓ was explained by one household's anecdote instead of a general picture. The substance critic also asked for the landing to be an experiment, not a statement. Both are now new beats; the rest are fixes.

**Structure**
- **New beat: the share ladder** (craft 2, substance 4). On the chart's own x-axis, a bar rises at every share of matching neighbors that a household of the random start actually has. With at most 8 neighbors these are 14 fractions between 0 and 60 %. A purple demand line at ⅓ turns every bar to its left RED, with "unhappy 238" riding on the line. The line then slides to ¼ and crosses exactly two rungs, 2/7 (67 households) and ¼ (76: 66 at 2/8 plus 10 at 1/4). Each turns grey as the line passes, and the count falls 238 → 171 → 95. The household that started the corner's chain (A, 2 gold of 7 at the start) sits between the thumbnails with 2/7 < ⅓ built from its tiles, and the inequality flips to 2/7 ≥ ¼ as the line lands ("…and that chain never starts"). All numbers come from `sim.share_ladder` and `report_extra()` and are asserted in scene.py.
- **New beat: the two-town test** (substance 13). Two simulated towns, both at 76 % (0.7553 and 0.7554), cross-fade in with nothing to say which is which; ours is on the right, where it has never appeared. The two demands, "⅓ demanded" and "0 demanded", wait unassigned in the gap between them: "Which one wanted a third?" and a 1.5 s hold. Then each label flies to its town. The left town's zone lines draw on ("0 demanded · placed by a rule": irregular zones marked for one colour, 92 % of households in their colour's zone, no preferences, nobody moves; `sim.zoned_town`). The Aaronson et al. 2021 citation follows. The landing then grows our town back into the opening frame and resets the marker to "?".
- **Retitled** "Mild Preferences, Segregated Towns" (substance 8). Opening line is now "Every household in this simulated town is free to move" (substance 7: only 341 moves happen).

**Fixes**
- Domino (craft 1): on "Replay one corner" the board dims to 30 % except the focus box, and the counter, plan and round labels fade (no stale "round 1"). The inset is 1.4× larger, at about 530 px, in the right half.
- Stale fraction (substance 1): every departure (A, B, C) is one animation with the relation turning to "?" and the old numbers dimming to 30 %. The new fraction resolves on the narration cue ("two sevenths", "tips").
- Unhappy rings (craft 4): the red is now a 3.8 px ring outside the tile, and the household keeps its full colour. Three gold neighbors now read as three gold tiles.
- 238 vs 200 (craft 9, substance 3): a GRAY note "38 fixed by neighbors' moves". `round1_breakdown()` confirms 200 moved, 38 were content when their turn came, and 0 found no square.
- "Most never moved" is shown (craft 3, substance 9). On "sixty-seven" the content tiles dim and the 7 rings that were already unhappy at the start turn grey. 67 RED rings remain, with the note "67 content at the start", and the narration now says sixty-seven.
- "plan predicts 0" sits directly under the counter, with the 0 under the digits (craft 12).
- Rule (craft 13, substance 5): "counts the occupied squares"; grey × on the two empties plus "empty: not counted".
- Cold open (substance 6): frame 1 is the town centred. It slides left as the meter enters on "on average".
- Chart (craft 5, substance 2): dots at r 0.05 and 38 % opacity with ±0.6 pp jitter, plus an INK mean tick and a GRAY min–max whisker per column. "random mix" moved to the left end, below the line, clear of the band (craft 11).
- Transition (craft 10, substance 10): the town shrinks into its slot first. The axes draw only afterwards, while a copy of the town lands as the dot exactly on "point".
- Payoff motion and sync (craft 7). A GRAY "our jump" bracket over ¼–⅓ appears on "His households". "his rules: nearest square" and "25–30% empty (ours: 10%)" appear on their words. On "came later" the bracket slides to 35–50 % ("Schelling's jump: 35–50%", above the plot, never on the band: substance 2). The band sweeps from 35 to 50 exactly over "between about a third and a half". Longest static stretch is now ≤ 3.3 s.
- Concision (substance 12): cut "Every departure shrinks a minority that was already small".
- Audio (craft 8, substance 11). Gaps are now about 0.25 s inside a thought and 0.8–1.3 s at beat boundaries. The densest beats run at speed 0.80–0.83. The "thirty s" diff was the review kit normalizing whisper's "1930s", not a mispronunciation. The narration text now writes "1930s", which misaki reads "nineteen thirties", so the two sides match.
- End card: the Ω is INK, so BLUE keeps one meaning (craft 14).

**Kept** the cold open with "? demanded" parked at 76 % and the identical landing frame, the tile-built domino with its "?" pause, and the object continuity (rewind, preview arc → real move, thumbnail → dot → full town).

**Found in my own frame review (not in the round 1 reviews)**
- 2:00: the town no longer flies through the fading meter and counter labels. The HUD leaves first (0.5 s), then the town shrinks into its slot.
- 2:38: while the demand line slides from ⅓ to ¼, its "⅓" label fades out first and "¼" appears only when the line lands. A line labelled ⅓ never sits at another x. "unhappy N" follows the line and counts 238 → 171 → 95 as the two rungs cross.
- Schelling beat: the "Schelling's jump: 35–50%" label sits above the plot, so no text sits on the grey band.

**Mechanics (review/report.md):** 3:52.9, 155 wpm in speech, −14.0 LUFS / −1.7 dBTP, longest silence 1.97 s (the planned prediction hold), longest static 3.53 s, trailing silence 1.75 s, 0 render warnings, 0 banned phrases, WER 0.0 %.

## Round 2 revisions

Round 2 review: craft 7.0 (8.6 before cap), substance 7.0 (8.4 before cap). Both caps come from the same defect: the rung labels "1/4" and "2/7" sat on or across the x-axis at 2:41–2:50.

### Plan (written before editing)

| Dimension (lowest score) | BAR "9" anchor | Where it falls short | Upgrade |
|---|---|---|---|
| Visual (8 / 8) | "Every frame has one focal point; all §5 standards met" | Rung labels cross the axis. Count bars sit on a % y-axis and a PURPLE "demanded" x-axis. The board focus box is stale during the domino. The two-town frame has no "simulated" tag. The HUD is ragged | Turn the ladder into its own chart: hide the % y-axis, use the INK x title "share of neighbors matching", put GRAY counts centred above the named bars, put rung fractions under the axis, and use a short PURPLE demand tick across the axis (the meter's marker), so no label ever shares a column with a tall line. Keep the board patch in sync with the inset by moving the real tiles. Add "simulated" to the two-town frame. Right-align the HUD into a label column and a number column |
| Clarity (8.5 / 8.5) | "Viewer could re-derive it after one watch; assumptions stated" | The 3/8 → 2/7 step is not shown in general. The HOLC bridge implies the maps were a rule about where each color could buy. "until round seven" is off by one | GRAY arrow from 3/8 to 2/7 labelled "lose one match", plus the line "Every household at three eighths is one lost match away from it". New HOLC sentence: "placed by a rule, with no preferences at all … by cutting credit to the areas they marked red". "after round seven, nobody wants to move" |
| Motion (8.5 / 8.5) | "Every motion encodes a relation; reading time respected" | Round 3 is unreadable (0.8 s / 1.1 s). Tile copies morph into blobs. "0 demanded" flies across a town | Round 3 gets its own clause and a 1 s pause, with each state held ≥ 1.5 s. Tiles fly as squares and fade into the digit. Chips travel up the gap, then sideways above the towns |
| Hook (8.5 substance) | "Commit by 0:12; tension rises through build and fail" | Frame 1 has no tag or number; the ladder's "Why the jump?" is answered at once | "simulated" is visible from frame 0, and the meter fills to 76 % by 0:03.5. The ladder gets a real prediction: "At a quarter, how many would start unhappy?" with a 1.2 s hold, while all three counts are visible so the viewer can compute it |
| Concision (8.5 / 8) | "Cutting any sentence loses something" | "by hand, on a checkerboard" has no visual; "That cuts both ways" is a fourth thesis line; "Rerun the same rules…" is long; "Slide down to a quarter… a quarter and two sevenths" repeats the picture | Cut all four, which pays for the arrow line, the prediction and the HOLC mechanism |
| Audio (8.5 / 8.5) | "Each deictic lands as the element highlights" | — | Keep cue-driven timing; the new deictics ("these two rungs", "it") are cued to their highlights |

### What changed

**The cap (both critics' fix 1).** The ladder is now its own chart on the same x-axis, built so that no label can touch a line.
- **Rung fractions** "2/7" and "3/8" sit in one row under the axis, 0.34 below it, so they clear the axis and the ladder ticks.
- **Counts** "67", "125" and "76" (GRAY MathTex 26) sit centred above their own bars with `next_to(bar, UP, buff=0.15)`.
- **The demand** is the meter's own marker, a short PURPLE tick across the axis. Its fraction is on the same under-axis row, so no label shares a column with a tall line. The old tall line made "centred above the ¼ bar" impossible.
- **Checks.** scene.py asserts ≥ 0.15 between neighbouring labels in both rows.

**Ladder (craft 2, 3; substance 2, 8)**
- **Axes.** On "Sort", the % y-axis, its title, the x numbers, the 30-town dots and the random-mix line fade to 0. The x title becomes INK "share of neighbors matching", and the chart title is "households by share (simulated start)". Everything returns for the Schelling beat.
- **The general step is drawn.** A GRAY curved arrow "lose one match" runs from the 3/8 bar (125) to the 2/7 bar (67), which is red at ⅓, with the new line "Every household at three eighths is one lost match away from it." After the slide the arrow lands on a grey bar. facts.md (14a″) records what is not claimed: that nobody at ¼ is one lost match from unhappiness.
- **A real prediction.** "At a quarter, how many would start unhappy?" A dashed PURPLE ghost tick appears at ¼, with "76" over its bar, so 238, 67 and 76 are all visible and the viewer can compute 95 during the 1.2 s hold. Then the tick slides on "Only these two rungs change sides", and 238 → 171 → 95 is the payoff.
- "Slide down to a quarter … a quarter and two sevenths, but" was cut; the picture says it.

**Domino (craft 4, 5; substance 4, 5a, 10)**
- **The board's corner box replays in step with the inset**, using the real tiles and real moves:
  - On "Replay one corner", A flies home from its round-1 square and the corner's rings go back to the start state.
  - A, B and C each fly to the square they really moved to, in the same animation as their inset departure and the "?".
  - In round 2, the blue household that moved into A's old square flies in.
  - Rings appear on the board when they appear in the inset.
  - Rounds 2–7 then start each flight from the tile's current square, so the replayed movers do not move twice. Their rings stay off until their real round has passed.
- **HUD.** The 64 % readout, the meter track and its tick fade to 0 during the replay rather than 30 %. Only "⅓ demanded" stays, because the formula copies its ⅓.
- **Round 3 is readable.** It now has its own clause, "In round three, the next one, also at three eighths, tips the same way", after a 1 s pause. C's 2/7 < ⅓ resolves on "drops" and holds about 1.8 s. D's 3/8 ≥ ⅓ holds from "In" to "tips", about 2 s. D's 2/7 < ⅓ holds about 1.5 s into the next beat, whose inset fade now waits for "whole town". This differs from the substance critic's option of cutting the sentence: it follows the craft critic's request to slow it down, and the domino is a keep item.
- **No blobs.** Gold-tile copies fly as squares and fade into the digit, both in the inset and in A's ladder patch (`fly_into`). The inset's A no longer turns red on Indicate; it pulses in its own colour, since RED is only ever a ring.
- **Wording.** "and after round seven, nobody wants to move" replaces "until round seven, when nobody wants to move", which was off by one: round 7 still has one mover.

**Two-town test (craft 6, 7; substance 3, 7)**
- **Tag.** A GRAY "simulated" tag sits centred in the gap, on the row of the "76% match" labels, and fades in with the towns.
- **Chip paths.** Both chips travel up the empty gap, then sideways along a lane above the towns, so they never pass over tiles. "· placed by a rule" appears only after "0 demanded" has landed.
- **HOLC bridge.** "The other was placed by a rule, with no preferences at all. In real cities, one study finds that federal lending maps from the 1930s, by cutting credit to the areas they marked red, increased racial segregation for decades." This follows the abstract's mechanism, "through reduced credit access and subsequent disinvestment", which I re-read on aeaweb.org.

**Hook (substance 6).** "simulated" is on screen from frame 0. The slide starts at about 0:01 and the meter reads 76 % by about 0:03.5, so "three quarters" pulses a number that is already there.

**HUD (craft 9).** The HUD is a two-column table. "unhappy", "plan predicts" and "round" are right-aligned on one edge. 238/74, 0 and the round number are right-aligned on the meter's 100 % end, so the 0 sits under the count's last digit. The notes are right-aligned to the same edge.

**Concision (craft 8; substance 5b, 5c, 8)**
- "Why the jump?" (answered at once) became "To see why that happens, sort the random start…". The ladder's real question is now the ¼ prediction. Whisper dropped "why" from the shorter "To see why, sort" on the full track, so the longer phrasing was checked on Groq whisper first.
- The town now shrinks into its thumbnail while "That whole town is one point on this chart" is spoken, not in a 1.8 s silence before it.
- Cut "by hand, on a checkerboard". On "model", a box now flashes the two simulated towns.
- Cut "That cuts both ways" and shortened its gap.
- "Rerun the same rules thirty times at each demand" became "Thirty towns at each demand".

**Found in my own review (frames every 0.25 s across each transition, plus the audit)**
- **Audit, now 0 findings.** Fixes, in order:
  - The "simulated" tag moved under the board; above it there was no room for 0.15 clearance from the frame and the flash box.
  - The meter's "76% match" and "? demanded" labels moved 0.1 further from the purple tick.
  - "Schelling's jump: 35–50%" no longer touches the band's top edge. This was a held overlap the round-2 critics missed.
  - "random mix" now clears the 0 % and 10 % dot columns.
  - The arrow label, flash boxes and inset each gained a little clearance.
  - "individual motives" is now an underline, because a box would crowd the tick numbers.
- **Text changes no longer morph letter by letter.** The inset caption ("before/after round N") and the ladder's x title now cross-fade in place.
- **No bare axis.** On "sort" the dots fade while the bars grow, as one move.
- **Static stretch broken.** The 3.8 s stretch under "by cutting credit to the areas they marked red" now has a zone-line pulse on "credit".
- **Transcript.** "Now let the whole town run. Round…" became "Now run the whole town. Round…", because whisper transcribed "run. run." over one spoken word.
- **Transcript slips that remain are whisper's, not the voice's.** "aggregating" for "aggregate": misaki gives the adjective /ˈæɡɹəɡət/, and the same audio transcribed correctly in round 2. A 20 ms "be." sits inside the 1.2 s prediction silence. See facts.md.

**Verified frame by frame**
- **Corner box sync.** Upscaled crops of the board's corner box at 1:15, 1:17, 1:20, 1:29, 1:37, 1:43, 1:49, 1:52 and 1:56 match the inset at every step: A home and ringed, A gone, B ringed, B out with the blue arrival in, C ringed, C out with D ringed, then the whole town.
- **Ladder.** At full resolution (2:52 keyframe), the counts sit centred above their bars, 0.15 or more from the axis and from each other. The fractions sit under the axis, and the arrow lands on the 2/7 bar.

**Mechanics (review/report.md):** 3:56.4; 156 wpm in speech; −14.0 LUFS / −1.7 dBTP; longest silence 1.97 s (the planned cold-open hold); longest static 3.3 s; trailing silence 1.75 s; 0 render warnings; layout audit 0 issues in 237 checks; 0 banned phrases; WER 0.4 %; 0 review-kit flags.

**Honest self-score: about 8.9–9.0.** Hook 9 · Clarity 9 · Visual 9 · Motion 8.5–9 · Audio 8.5 · Concision 8.5 · Originality 9.
- **Motion.** The formula's digit and relation morphs (e.g. 3/8 ≥ → ?) still pass through about 0.3 s of in-between glyphs.
- **Concision.** The runtime is 3.5 s longer than round 2. The critics asked for three of the additions (the 3/8 arrow line, the ¼ prediction, the HOLC mechanism) and the craft critic asked for the round-3 clause; four cuts paid for most of it.

## Round 3 revisions

Round 3 review: craft 8.7, substance 8.4, no caps, no factual errors. Both critics said every fix together reaches about 9.0.

### Plan (written before editing)

| Dimension (lowest score) | BAR "9" anchor | Where it falls short | Upgrade |
|---|---|---|---|
| Visual (8.5 / 8) | "Every frame has one focal point; all §5 standards met" | The share ladder is small, floats with no baseline, and its PURPLE tick sits inside a bar. The Schelling label crowds the y title, the band is heavy, and the rule notes sit between our towns. The two-town headers are off-centre on two baselines. The dimmed board takes 42 % of the frame during the domino | Rebuild the ladder as its own chart, about 1.3x larger and 0.8 units higher, with a GRAY baseline, counts at MathTex 32, a PURPLE caret under the baseline and a PURPLE outline on the threshold bar. Put the Schelling label on the bracket row inside the plot, with his rules right under it, and set the band to 0.18. Centre the headers on their boards on one baseline. Shrink the board to 0.7 at the left edge during the replay, and grow the inset from 530 to 675 px |
| Concision (8 / 8) | "Cutting any sentence loses something" | The thesis is stated three times in 45 s; the third domino step repeats the first two; the opening line is set-up | Cut the Schelling quote sentence and fold its source into the landing ("As Schelling argued"). Shorten domino step 3 to "Then the next one, at three eighths, tips". Open on the puzzle |
| Clarity (9 / 8.5) | "Viewer could re-derive it after one watch" | "rungs" is undefined; "only these values occur" ignores the cut at 60 %; the arrow at ¼ implies more than is said; the unspoken "38 fixed" note competes | "bars"; "these are the only shares up to sixty percent", with 0 and 60% marked; fade the arrow during the slide; remove the 38 note |
| Motion (8.5 / 8.5) | "Every motion encodes a relation" | The ladder-to-chart cross-dissolve shows ghost dots; the ⅓ copy flies through "¼ → 58%"; the meter counts up from 0 % | Reverse the 2:19 morph (bars shrink, the baseline becomes the x-axis, then the dots return); copy the ⅓ from "⅓ → 76%"; draw the meter bar at 76 % and write the number on |
| Audio (8.5 / 8.5) | "Pauses are intentional; each deictic lands" | The HOLC sentence garden-paths (a stop after "1930s", a break before "they marked red") | Two sentences with the subject next to its verb; zone pulses on "increased" and "credit" |
| Hook (9 / 8.5) | "Viewer commits by 0:12" | The first line is set-up, not the puzzle | "In this simulated town, on average, three quarters of a household's neighbors match its color." The question lands by about 0:06. "free to move" becomes "If fewer than a third of them match, it moves" in the rule |

### What changed

**Share ladder, rebuilt (craft 1, 5; substance 1, 2, 7, 9)**
- **Its own chart, larger and higher.** The bars stand on a GRAY baseline that spans the ladder. The ladder is about 1.3x wider than before, and its tallest bar reaches y = 2.35, up from 0.68, so the upper-left of the frame is no longer empty. The counts 67 / 125 / 76 are MathTex 32. The dot chart's 0/20/40/60 ticks and numbers fade with the rest of the dot chart, so no tick pokes out under a bar.
- **The demand is a caret plus an outline, never a mark inside a bar.** A PURPLE caret sits between the baseline and the fraction row, and a three-sided PURPLE outline (open at the baseline) surrounds the threshold bar. For the prediction, a 50 % caret and a dashed outline mark ¼. On "Only these two bars change sides", the ⅓ outline and label lift off and the caret slides to ¼. The two bars it crosses turn grey, and when it lands the dashed outline turns solid.
- **The arrow claims only what is said.** The 3/8 → 2/7 "lose one match" arrow and its label fade out during the slide, because at ¼ the 2/7 bar is content.
- **Words.** "rungs" became "bars", and "they're crowded" became "they're tall". "only these values occur" became "these are the only shares up to sixty percent", and the ends are marked "0%" and "60%". On "these" a highlight sweeps along the bars, each growing briefly upward.
- **Into the ladder** (2:16): the dot chart leaves completely (dots, y-axis, x ticks and numbers, random-mix line) while its x-axis line moves up and stretches into the ladder's baseline. The bars grow only after that. **Out of the ladder** (2:52) is the same move in reverse: the bars sink into the baseline, the baseline returns to the x-axis while the x title goes back to PURPLE, and only then do the dots return. Both charts are never on screen at once.
- **A's ⅓** now comes from the "⅓ → 76%" label at top right. Its path crosses nothing, where the old copy flew through "¼ → 58%".

**Schelling beat (craft 3, 6; substance 8)**
- **Cut the quote sentence** "He wrote that inferences about individual motives…" (about 6.5 s). The landing now carries the attribution: "Look again at the first town. As Schelling argued, whatever you guessed its people demanded, the map alone could not have told you." I used "As Schelling argued" rather than "Schelling's point:" so there is no colon reveal.
- **Labels sit on the bracket's row, inside the plot.** "our jump" sits to the left of its bracket. On "came later", "Schelling's jump: 35–50%" takes the same row to the left of the 35–50 bracket. His rules ("his rules: nearest square", "25–30% empty (ours: 10%)") sit right-aligned directly under that row. They no longer touch the y title or sit between our thumbnails. The band fill is 0.18 (it was 0.32).
- The reverse morph above runs under "In his 1971 paper", and the citation fades in with the returning chart.

**Two-town test (craft 2, 7; substance 3)**
- **HOLC wording:** "In real cities, one study finds that 1930s federal lending maps increased racial segregation for decades. It traces this to reduced credit in the areas marked in red." The subject now sits next to its verb. The mechanism is attributed to the study ("It traces this to…") rather than stated as our own fact; the abstract's words are "through reduced credit access and subsequent disinvestment". Kokoro's word timings show no internal break: the largest gap inside either sentence is 0.05 s. The zone lines pulse on "increased" and on "credit", and the two "76% match" labels pulse on "decades".
- **Headers.** "0 demanded · placed by a rule" is one Text with a GRAY t2c suffix, so its baseline is exact. Both headers are centred on their boards, and the word "demanded" sits on one shared baseline 0.25 above the boards.

**Domino (craft 10; substance 4)**
- **More room for the inset.** On "Replay one corner" the board parks at the left edge at 0.7 scale (dimmed context, white focus box on the corner). The inset grows from 530 to 675 px, with the formula to its right and the state caption ("before round 1", "after round 2"…) under the formula, left-aligned with it. On "whole town" the board grows back to full size and full strength while the inset folds away.
- **Step 3 is shorter.** "In round three, the next one, also at three eighths, tips the same way" became "Then the next one, at three eighths, tips". D's 3/8 ≥ ⅓ holds through "at three eighths". On "tips", C leaves and D's fraction changes in the same move, and D's 2/7 < ⅓ then holds through a 1.1 s pause into the next beat.

**Hook and failure (craft 8, 9; substance 5, 6)**
- **Open on the puzzle:** "In this simulated town, on average, three quarters of a household's neighbors match its color. How much matching do these households demand?" The question now ends about 2 s earlier. "Free to move" moved into the rule: "If fewer than a third of them match, it moves."
- **No count-up from zero.** The meter is drawn already at 76 % and the number is written on.
- **Removed** the unspoken "38 fixed by neighbors' moves" note. "67 content at the start" appears on "sixty-seven", as it is spoken.

**Found in my own review (preview frames every 0.6–1 s, plus the audit)**
- **Late cues.** The first preview flagged three. "this" in the replay was 0.31 s late: the caption now fades in with the inset. "seven" was 0.38 s late: the unpark is 0.8 s, and the round minimum is 2.6 s. "paper" was 0.77 s late: the citation now arrives with the chart restore.
- **Clearances.** The audit found the replay caption 0.07 from the inset frame, so the caption is now left-aligned under the formula. The caret was 0.12 from the fraction row, so the row moved 0.06 lower. "60%" and the x title were 0.12 from the flash box around "¼ → 58%", so the ladder is 0.15 narrower. Its counts still clear each other by 0.16.
- **Morphs.** The dashed-to-solid ¼ outline morphed through stray dash fragments; it now fades and draws instead.
- **No more garbled digits.** The first master's sheet frame at 1:45 caught "2/7 → 3/8" mid-morph as garbled glyphs. Every digit or relation change in the formulas now uses `swap()`: the old glyph fades out and the new one fades in on the same object, with no point morph. This covers the inset fraction, A's ladder formula, and the meter's "?" ↔ ⅓.
- **Hold times in the domino.** C's 2/7 < ⅓ was on screen only about 1.1 s before the ring moved on. The fraction now resolves 0.3 s earlier and the pause is 0.9 s, so it holds about 1.7 s. D's 3/8 ≥ ⅓ holds about 1.7 s, helped by a 0.3 s pause before "tips". D's 2/7 < ⅓ holds through a 1.4 s beat gap.
- **In-motion overlaps found in 4 fps strips of the first master:**
  - At 2:17 the x-axis line rose through the fading dots while the two x titles cross-faded on top of each other. Now the dot chart fades out first (0.5 s), then the line moves (0.6 s).
  - At 1:50 the growing board and the fading-in HUD ran over the still-fading inset. The inset now folds away on "Now", before the board grows on "town".
  - At 3:05 "our jump" and "Schelling's jump" were both half-visible on one row. The old label is now gone in the first 40 % of the move, and the new one appears only in the second half.

## Round 1 revisions (second review cycle)

Review: craft 8.5, substance 8.6, no caps, no factual errors; both said every fix together reaches about 9.0. Root cause of the two "fixed but not fixed" defects (garbled glyphs at 1:45, labels superimposed at 3:05): the reviewed final.mp4 (01:12) predates the last scene.py edit (01:18), so those fixes were never rendered. I confirmed in an isolated test that the `swap()` cross-fade itself never shows two glyph sets; this revision replaces it anyway (see below) and re-renders everything.

### Plan (written before editing)

| Dimension (lowest) | BAR "9" anchor | Where it falls short | Upgrade |
|---|---|---|---|
| Visual (8 / 8.5) | "Every frame has one focal point; nothing to remove" | Ladder frame has three focal regions; Schelling frame has ~22 words, a 3-line grey stack and a band drawn over our dots; ladder has no vertical quantity; lower-right empty for 40 s | Thumbnails leave the ladder; A's patch moves to the vacated right column; "households" names the vertical; one merged rules label; hatched band with our dots dimmed to 35 %; HUD lowered with a fourth row |
| Motion (8.5 / 8.5) | "Every motion encodes a relation; reading time respected" | 0.3 s glyph morph at 1:45; labels superimposed at 3:05; inset flies out after the park | A new household's formula slides out left and the next slides in from the right (a different household); same-household changes cross-fade in place ≥ 0.6 s; label out → bracket slides → label in, sequentially; inset flies out with the corner rewind |
| Clarity (8.5 / 8.5) | "Viewer could re-derive it after one watch" | 238 vs 200 gap; spoken columns unmarked; subject household unmarked; "map alone" beatable by texture; zone pulses equate the toy rule with HOLC | "the other thirty-eight were content by their turn" + live "moves" HUD row; ¼ and ⅓ fly from the thumbnail labels to their columns, which brighten; white inner outline on the subject household; rule town regenerated to match the Schelling town's texture (no stray tiles); zone pulses removed, towns dimmed under the HOLC sentence |
| Audio (8.5 / 8.5) | "Each deictic lands as the element highlights" | "this chart" over an empty frame; "this counter" un-highlighted; "other" swallowed | Axes drawn by "point"; counter pulses on "this"; "In one town … In the other, nobody minds …" (whisper-checked) |
| Concision (8 / 8) | "Cutting any sentence loses something" | 3:50; restatements | Cut "So most households are content", "Round after round, the tipping spreads", "Seventy-six percent, the town we started with", "Thirty towns at each demand…" |

## Round 5 revisions

Round 5 reviews: craft 8.5, substance 8.6, no caps, no factual errors (the same text as the second cycle's round-1 reviews, against the 01:12 master). The previous attempt had written the plan above and edited scene.py, script.md and facts.md, but its master render was interrupted, so `final.mp4` still showed the defects the critics saw. This revision continued from those files, rendered them, checked every fix on the frames, and fixed what the frames still showed.

**Every round-5 fix, checked on the new master**

| Fix (critic) | Where it landed | Status |
|---|---|---|
| Garbled 2/7 → 3/8 morph (craft 3, substance 1) | 1:42–1:44: the old household's fraction slides out left and fades, then the next one slides in. Frames at 10 fps never show two digit sets. Same-household changes cross-fade in place, 0.3 s per half | fixed |
| "our jump" and "Schelling's jump" superimposed (craft 4, substance 2) | 2:58–3:00: the label fades out, then the bracket slides, then the new label fades in. Frames at 5 fps show one label at a time | fixed |
| Ladder had three focal regions (craft 1) | Thumbnails leave on "sort". A's patch moves to the vacated right column. Counts appear only as spoken (67, 125, then 76) | fixed |
| Ladder vertical had no name (craft 8) | "households (simulated start)" sits at the top-left, where a y-axis title would be | fixed |
| Schelling frame had about 22 words and the band sat over our dots (craft 2, substance 8) | One label, "nearest move · 25–30% empty". The band is hatched at 7 % fill. Our 30-town dots and mean ticks dim to about 30 %. Our two towns' dots stay bright, marking the ends of "our jump" left of his band | fixed |
| Subject household had no marker (craft 5) | White inner outline on B, then C, then D. A's ring stays at 50 % until "this neighbor" | fixed |
| "this chart" spoken over an empty frame (craft 6) | Axes are drawn before "point" | fixed |
| Spoken columns not marked (craft 7) | ¼ and ⅓ fly from the thumbnail labels to their columns, which brighten | fixed |
| Counter not highlighted on "this counter" (craft 9) | Pulse on "this" | fixed |
| "other" swallowed (craft 10, substance 6) | "In one town … In the other, nobody minds …". Whisper transcribes it | fixed |
| 238 vs 200 gap (substance 5) | "the other thirty-eight were content by their turn", plus a live "moves" row and a note | fixed |
| Rule town beatable by texture (substance 3) | Fine-grained zone field, so the towns are indistinguishable at 3:04 (frame checked) | fixed |
| Zone pulses equated the toy rule with HOLC (substance 4) | Pulses removed. Both towns dim under the HOLC sentence | fixed |
| Concision (craft 11, substance 7) | Cut "So most households are content", "Round after round…", "Seventy-six percent, the town…" and "Thirty towns at each demand…", plus (this round) "The matching share jumps to sixty-four percent", which only read the meter aloud | fixed |
| HUD balance, 2 s near-empty park (craft 12) | HUD sits beside the board's middle. The inset flies out with the corner rewind | fixed |

**Found on the first round-5 master and fixed**
- **"tips" (1:48).** It stood alone after a 0.3 s pause, and the full-track whisper heard "It ips". The line is now "Then the next one, also at three eighths, tips in round three." Synthesized alone, it transcribes word for word, and on the full track WER is 0.2 % (only "corner's"/"corners"). The move starts 0.7 s before "Then", so C's 2/7 < ⅓ still holds about 1.6 s and D's 3/8 ≥ ⅓ holds about 1.9 s.
- **4.2 s static stretch at 3:25 (HOLC sentence).** The towns now dim slowly across "1930s federal lending maps". The two "76% match" labels, our segregation measure, pulse on "segregation". The longest static stretch in the episode is now 3.7 s.
- **Lone line on an empty frame at 2:13.** Both ladder titles now arrive while the axis line moves, and the bars are up within 1.3 s. In the reverse morph (2:46) the thumbnails return while the bars sink.
- **Labels crossed by flying copies.** At 1:57 the town's copy flew over "⅓ → 76%" while it faded in. At 2:04 the ¼ town's copy flew over "→ 58%". Both labels now arrive after their copy lands.
- **Landing (3:33).** Our growing town passed over the fading rule town and its labels. Those now fade first (0.45 s), then the town grows home.
- **Dot dimming.** The no-op dims on our two town dots were removed, so the code matches the picture.

## Round 5 revisions (continued)

The previous attempt was interrupted after its last master render (final.mp4 09:49, from the 08:48 scene.py) and before the review pack was rebuilt (review/ was from 07:37). This pass rebuilt the pack for that master, checked every round-5 fix on its sheets, keyframes and 4 fps strips across each transition, and then fixed what the frames still showed.

### Plan (written before editing)

| Dimension (round-5 low) | BAR "9" anchor | Where the 09:49 master still falls short | Upgrade |
|---|---|---|---|
| Visual (8 / 8.5) | "Every frame has one focal point; nothing to remove" | All round-5 items landed (ladder has one focal region, the vertical is named, Schelling frame has one rules label and a hatched band). New: the sheet frame at 2:11.0 is a bare baseline under two titles, about 0.9 s with no bars (BAR §11.5: never a near-empty frame while narration speaks) | Make the ladder entrance one move in which the bars sprout from the rising line |
| Motion (8.5 / 8.5) | "Every motion encodes a relation" | The garbled 2/7 → 3/8 morph and the superimposed jump labels are gone (10 fps and 5 fps strips). New: at 1:55.2–1:56.0 the shrunken town sits alone on an empty frame before the axes start drawing; at 3:32.6–3:33.2 the dimmed town is left alone before it grows home | Draw the axes during the shrink, once the town is clear of them; bring our town back to full strength while the rest fades |
| Concision (8 / 8) | "Cutting any sentence loses something" | The four restatements the critics named are cut, and so is "The matching share jumps to sixty-four percent" (3:50 → 3:43). Every remaining sentence carries a step the picture needs | Trim the silence before the chart (beat gap 0.5 → 0.25 s) rather than cut a load-bearing sentence |
| Clarity, Audio (8.5) | "Viewer could re-derive it…" / "each deictic lands" | All round-5 items landed (38 spoken, matching texture, no zone pulses, "this counter" pulses, "In the other" transcribed) | No change |

### Every round-5 fix, re-checked on the 09:49 master
Garbled morph at 1:44.8 (strip 1:41.6–1:44.6, 4 fps: the old fraction slides out, then D's slides in; never two digit sets) · jump labels at 3:04.8 (sheet 2:55–2:59: "our jump" gone before the bracket slides, then "Schelling's jump: 35–50%") · ladder focal regions (kf 2:27.1, 2:45.4: thumbnails gone, A's patch in the right column, counts only as spoken) · "households (simulated start)" (kf 2:17.6) · Schelling frame (kf 2:57.7: one rules label; sheet 2:59: hatched band, our columns dimmed) · subject outline (kf 1:17.5, 1:38.4) · "this chart" (kf 1:57.7: axes drawn) · spoken columns (kf 2:05.3: ¼ mark and bright column) · counter pulse · "In the other" (whisper: "In the other, nobody minds their neighbors at all.") · 38 spoken + "38 content by their turn" (kf 0:55.4–1:06.4) · rule-town texture (kf 3:05.5, 3:13.6) · no zone pulses, towns dimmed (kf 3:31.7) · HUD centred beside the board (kf 1:06.4). All landed. Mechanics of that master: 3:43.2, 158 wpm, −14.0 LUFS / −1.7 dBTP, max silence 1.96 s, max static 3.67 s, WER 0.0 %, 0 render warnings, layout audit 0 issues in 231 checks, 0 banned phrases.

### New standard mid-revision (toolkit commit 760d507, PRODUCTION_GUIDE §13)

While this pass was under way the toolkit gained the §13 targets from 28 critic reviews: ≤ 500 words and 3:15–3:35, shaped cadence, 0.9–1.4 s after key results, no sentence over 200 wpm, deictic sync, no glyph morphs, Text ≥ 27 for labels the narration refers to, one focal point per frame. The 09:49 master failed three of them (526 words / 3:43; 6 sentences over 200 wpm; flat 0.41 s gaps with beat turns at 0.43 s). The revision therefore went further than the plan above.

### What changed

**Narration: 526 → 483 words, 3:43 → about 3:34, `CADENCE = "shaped"`** (§13.1, §13.4)
- Cut by the mute test, each one something the frame already shows or a restatement:
  - "about one in six" (0:41);
  - the second spoken "two hundred and thirty-eight" (2:22): "unhappy 238" is on the ladder, and the repeat was the report's flagged phrase;
  - the third domino step, "Then the next one, also at three eighths, tips in round three" (and its 1.1 s pause, D's ring and the early replay of C's round-3 move). A → B → C already makes the chain; a round-3 critic had called it a repeat of the first two;
  - "It traces this to reduced credit in the areas marked in red" folded into the study sentence as "…for decades, through reduced credit", the abstract's own mechanism;
  - the second "at all", "of them", "of a household's" (the report's other repeated phrase), "that suited them" → "suitable".
- Voice: every beat at 0.82–0.84 (was 0.80–0.85; the HOLC beat was 0.85, above the new 0.84 ceiling). Shaped cadence: full stops 0.47 s median, beat turns 0.67 s (were 0.41 / 0.43, "metronomic"). A 0.9 s hold after each key result: "It reads seventy-four.", "…it jumps to seventy-six.", "…that chain never starts." The ¼ prediction hold is 1.5 s (was 1.2).
- Sentences over 200 wpm: 6 → 2. "It is happy to be outnumbered two to one" joins the rule sentence ("…it moves, so it is happy…", 193 wpm); "So how does a demand of a third…" → "So how can a demand of one third…" (197); "Three eighths is more than a third" → "Three eighths beats a third" (188). The two left ("That whole town is one point on this chart", "Look again at the first town") are 6-word lines.
- Held function word: "Before round one," held its "one" 0.60 s before the comma; it is now "At the start,".
- Deictics: 15, all landing (`beat.on("these", …)` brings "? demanded" in on "these households"; the 50 % readout pulses on "Here"; the round-1 dim runs 1.4 s, through "of these").

**Frames** (§13.2)
- Labels the narration refers to are at Text 27 (34.6 px): "empty: not counted", the HUD notes ("38 content by their turn", "67 content at the start"), "random mix", "each dot: one simulated town", "households (simulated start)", "unhappy", "lose one match", "our jump". The rule inset moved 0.45 left so its label still clears the safe area.
- Schelling frame: "Schelling's jump: 35–50%" → "Schelling: 35–50%" at Text 27, and the rules label "nearest move · 25–30% empty" is gone (at 27 it does not fit left of his band, and it repeated the narration). The citation is underlined on "nearest" instead, so the rules point at their source. One label and one band on the chart.
- One focal point on the ladder: A's patch dims to 60 % (§13.2.8: a saturated hue fades only to 60 %) while the bars are the subject ("Every household at three eighths…", the ¼ prediction) and returns during the caret's slide, just before its 2/7 ≥ ¼ flip on "that chain never starts".
- Stakes beat: the rule inset stays, dimmed to 60 %, instead of leaving the lower right empty for 9 s; it returns to full on "a demand of one third" and fades with the rewind.
- The ladder baseline and the x-axis copy that becomes it use the new `AXIS` colour, the same as the chart's axes, so the line does not change shade as it starts to move.

**Motion** (the three near-empty frames found on the 09:49 master)
- 1:55: the axes start drawing halfway through the town's shrink (x-axis and y-axis first, below and left of the moving town; titles last), so the shrunken town never sits alone; its copy leaves on "whole" and lands on "point".
- 2:11: the ladder entrance is one 1.5 s move: the dot chart fades (0–0.35 s), its x-axis rises into the baseline (0.15–0.75 s), the titles fade in (0.4–1.0 s), and the bars sprout from the moving line (0.5–1.35 s). The sheet frame that used to show a bare line now shows the bars coming up.
- 3:33: our town returns to full strength while the rule town and the labels fade, so the one town left is the subject of "Look again at the first town".

**Checked before the master** (dry run of the scene with the new toolkit, no frames rendered): 0 warnings (budget, deictic, glyph morph, speed, overlap, text size), layout audit 0 issues in 220 checks, and the review kit's Narration craft section has no flagged line (483 words / 3:33.9; median sentence 167 wpm, 2 over 200; full stops 0.47 s vs beat turns 0.67 s; longest run without a breath 14.7 s; 6 numbers in the busiest 20 s).

## Round 5 revisions (continued, 2)

The previous pass rendered a master at 14:02, rebuilt the review pack (14:05), then edited scene.py (14:09) and was interrupted before rendering those edits. So the 14:02 master still showed two defects that its own report and frames exposed, and that the CHANGELOG above describes as fixed. This pass audited that master frame by frame, rendered the pending edits together with three new fixes, and checked every round-5 item again on the new master.

### Plan (written before editing)

| Dimension | BAR "9" anchor | Where the 14:02 master falls short | Upgrade |
|---|---|---|---|
| Motion / Visual | "Every motion encodes a relation"; "nothing to remove" | 1:22.6–1:23.4: the inset caption "before round 1" cross-fades into "after round 1" in place, both legible for about 0.6 s ("bafterre round 1" in a 5 fps strip), the same garble class the critics docked at 1:45 and 3:05 | `recap()` now uses the toolkit `swap()`: old caption out, then new in (already edited at 14:09, never rendered) |
| Motion | "reading time respected"; static ≤ 4 s | 2:05.2–2:09.7: the finished ladder bars sit static for 4.5 s (report FLAG) | The bars sprout one by one across the whole sentence, from "sort" to "With" (14:09 edit, never rendered) |
| Visual | "all §5 standards met" | 0:54–0:56: round-1 hops near the edges swing out over the board's frame (17 of 200 moves, up to 0.30 units; one passes next to the "simulated" tag) | Every hop now bends toward the board's centre and is clamped to the board; the dashed plan preview uses the same arc |
| Visual | "every axis and marker labelled" (§13.1) | 2:41–2:54: the random-mix dashed line returns on the Schelling chart without its label | The line stays out with its label; the chart carries only Schelling's band and the two brackets |
| Visual | §13.2.8: a saturated hue dims only to 60 % | the 14:02 master still had the stakes-beat rule example and A's ladder patch at 35 % (olive gold) | 60 % (14:09 edit, never rendered) |

### What changed (scene.py)
- **Inset caption (1:22.6, 1:38.0).** `recap()` uses the toolkit `swap()` (Succession: old out, then new in). A 5 fps strip of the new master shows "before round 1", an empty slot, then "after round 1"; likewise "after round 1" → "after round 2". The two captions are never on screen together.
- **Ladder entrance (2:03.6–2:07.7).** The dot chart fades (0.3 s), its x-axis rises into the baseline (0.1–0.7 s), the titles fade in (0.35–0.95 s), and the 14 bars sprout left to right, one about every 0.25 s, until "With". The 4.5 s static stretch is gone: the longest static stretch in the episode is now 3.8 s (2:56.4, the two-town reveal).
- **Hops stay on the board (round 1 at 0:53, rounds 2–7 at 1:42).** New `inward()` picks the arc sign that bends each hop toward the board's centre, and `play_round` clamps every in-flight position to the board's cell range. Checked offline over all 341 moves: before, 17 left the board by up to 0.30 units; now, none does. The dashed plan preview (0:46) is drawn with the same `inward()` arc, so it still traces the exact path the tile flies at 0:53. A 4 fps strip of round 1 shows no tile outside the board.
- **Schelling chart (2:41–2:54).** The random-mix dashed line is no longer restored with the dots. Its label was already gone, so it would have been an unlabelled marker. A 4 fps strip of the reverse morph and kf 2:53.3 show only the axes, the dots, the bracket, the hatched band and the two thumbnails.

### Checked on the new master (19:55)
- **Every round-5 fix still lands:**
  - The 2/7 → 3/8 change slides, with no glyph morph (B → C at 1:33).
  - Same-household digits fade out and back in (strip 1:37.0–1:39.4).
  - The jump labels go out, then the bracket slides, then the new label comes in (sheet 2:49–2:51).
  - Ladder: one focal region (kf 2:23.4; A's patch now at 60 %).
  - "households (simulated start)" is shown.
  - Schelling frame: one label and a hatched band, with our columns dimmed (kf 2:53.3).
  - Subject outline (sheet 1:15–1:41).
  - "this chart": the axes are drawn first (sheet 1:49–1:51).
  - Spoken columns are marked (sheet 1:53–1:59).
  - The counter pulses on "this".
  - Whisper hears "In the other".
  - "38 content by their turn".
  - The rule town's texture matches the Schelling town's (kf 3:01.8).
  - No zone pulses under the HOLC sentence.
  - Our town returns at full strength for the landing (sheet 3:25–3:31).
- **Mechanics:**

  | Measure | Value |
  |---|---|
  | Runtime | 3:33.8 |
  | Narration | 483 words |
  | Pace | 153 wpm over speech |
  | Loudness | −14.0 LUFS / −1.8 dBTP |
  | Longest silence | 2.08 s (the planned hold at 0:09) |
  | Longest static stretch | 3.80 s |
  | WER | 0.4 % (only "corner"/"corners") |
  | Render warnings | 0 |
  | Layout audit | 0 issues in 222 checks |
  | Glyph morphs | 0 |
  | Deictics | 15 of 15 landed |
  | Review-kit flags | 0 |

- **Facts:** nothing factual changed. The Schelling 1971 wording was re-checked against the paper's PDF text (p.155, "moves to the nearest vacant spot"; "a rapidly rising function of demands in the range from about 35% to 50%").
- **Left as is, by judgment:**
  - The right third of the frame is empty during 2:04–2:16, while the ladder builds and before A's patch arrives. It is not a half or a quadrant (§13.1), and it is the column the critics asked the thumbnails to vacate.
  - Two six-word lines run at 208 and 215 wpm ("That whole town is one point on this chart", "Look again at the first town"). The report only flags four or more.

## Round 6 revisions

Round 6 failed at 8.6 (craft) and 8.5 (substance). Neither critic found a factual error or a cap. Both said the structure was right and that their fixes would reach about 9.0. This pass applies every fix from both reviews and keeps the three "keep" items in each.

### Plan (written before editing)

| Dimension (round-6 score) | BAR "9" anchor | Where the round-6 master fell short | Upgrade |
|---|---|---|---|
| Clarity (8.5 / 8.5) | "Viewer could re-derive it after one watch" | At ¼ the ladder explained the jump only by the starting count (238 → 95). The mechanism, that a 3/8 household can now lose a match and stay, was never said or drawn: the "lose one match" arrow faded during the caret's slide. "One lost match away from it" used a pronoun that reached back a sentence. "Corner" named a patch that is not a corner. The HOLC sentence had no link to the rule-made town | Keep the arrow, land it on the now-grey 2/7 bar, add "still content", and say "Now a household at three eighths can lose a match and stay, so that chain never starts". Say "away from two sevenths". Say "block". Open the HOLC part with "Real segregation also has causes besides preference." |
| Hook (8.5 / 8.5) | "the ending resolves the opening exactly" | The two-town test was not blind: ours was the seed-3 town in the orientation watched for 90 s. The stakes line played over an unchanged frame | Turn our town a quarter turn for the test (76 % and texture are unchanged) and turn it back as it grows home on "Look again at the first town". On "real city maps", dim the inset and the meter and pulse the board's frame |
| Audio (8.5 / 8) | "pauses are intentional" | The landing line ran at 215 wpm with 0.30 s after "first town.", straight after a 14.7 s run with no breath. "That whole town is one point on this chart" ran 208 wpm. Whisper heard "Replay 1 corners" | Landing at speed 0.80, with [pause 1.2] after "first town." and [pause 0.3] after "demanded,". About 0.95 s of silence after "credit." The HOLC run is split by the new link sentence. The chart line at 0.80. "Replay one block. [pause 0.3]" |
| Visual (8.5 / 8.5) | "Every frame has one focal point" | RED rings on gold read as orange. The ladder left the right third empty for 12 s. The prediction hold had about 14 labels in three clusters. Dot clouds looked like smudges, with stray ¼ / ⅓ glyphs. The end card dissolved over the board | Rings get a 1 px background-coloured gap, and content tiles dim to 55 % while the 238 rings draw. The ladder is built centred and slides left on "including". During the prediction hold, A's patch and the arrow dim to 35 %. Dots go to 60 % opacity with ± 0.3 pp jitter, and the column marks are dropped. The end card is dropped: hold the restored opening frame, then fade to the background |
| Motion (8.5 / 9) | "reading time respected" | Rounds 2–7 ran about 0.4 s each, and the per-round moves row showed stale values ("round 3 · moves 0") | The fold and unpark move into the gap before "Now", so the rounds start on "Now". Each round gets at least 0.6 s plus 0.15 s to settle, and the moves row is cumulative (200 → 341) |
| Concision (8.5 / 8.5) | "Cutting any sentence loses something" | "these are the only shares up to sixty percent" spent 14 words on a caveat. The plan took two sentences | "shares come in steps". The plan is one sentence. "and they're tall" is cut. The words pay for the new mechanism sentence, and the total ends at 479 words |

### What changed (every round-6 fix, both critics)

| Fix (critic #) | Change | Checked on the final master |
|---|---|---|
| ¼ mechanism (craft 1, substance 1) | The "lose one match" arrow stays through the caret's slide and lands on the now-grey 2/7 bar. On "lose a match", the arrow brightens and the 2/7 bar and its 67 flash. On "stay", "lose one match" moves up a line and "still content" fades in under it. New line: "Now a household at three eighths can lose a match and stay, so that chain never starts." 2:21 is now "…one lost match away from two sevenths." | sheet 9 (2:31–2:37), kf 2:36.2 |
| Landing audio (craft 2, substance 3) | One beat at speed 0.80: "Look again at the first town. [pause 1.2] As Schelling argued, whatever you guessed its people demanded, [pause 0.3] the map alone could not have told you." The town lands on "first", the meter returns on "town", and "? demanded" is back at 76 % 0.5 s before "As", in silence. There is 0.95 s of silence after "credit." | word timings: "town" ends 204.92 s, swap done 205.64 s, "As" 206.15 s |
| End card (craft 3, substance 9) | Dropped. The restored opening frame holds 1.2 s after "told you", then fades to the background in 0.5 s. Nothing dissolves over the board. Trailing silence is 1.77 s | frames 213.6 / 214.2 / 214.45 s |
| Red rings on gold (craft 4, substance 5) | Every ring now sits outside a 1 px background-coloured gap (front stroke in BG, ring drawn as a background stroke behind the fill). Content households dim to 55 % while the 238 rings draw, and return on "Round one" | kf 0:44.3 |
| Rounds 2–7 (craft 5) | The inset folds and the town returns before "Now", so the rounds start on "Now" and run through a 1.9 s pause. Each round gets at least 0.6 s plus 0.15 s for the counts to settle before the round number advances. The "moves" row is cumulative (200 → 272 → 313 → 329 → 338 → 340 → 341), so it never shows a stale value | sheet 6 (1:39 "round 2 · 41 · 272", 1:43 "round 7 · 0 · 341") |
| Ladder composition (craft 6) | The ladder is built centred (+2.1 units). On "including" it slides left in 0.8 s, and A's patch fades in once the right-hand bars have passed its column | sheet 7 (2:01–2:05 centred), sheet 8 (2:11 slide) |
| Prediction focus (craft 7) | During "At a quarter, how many…? [pause 1.5]", A's patch, its formula and the arrow dim to 35 %, so the dashed ¼ outline with 76 and 67 is the focal point. They return during the caret's slide on "Only these two bars" | sheet 8 (2:21, 2:23) |
| Dot clouds (craft 8) | Dots at 60 % opacity with ± 0.3 pp jitter; the PURPLE ¼ / ⅓ column marks are gone. Each spoken column brightens while its thumbnail label pulses | kf 1:54.8 |
| Stakes frame (craft 9) | On "real city maps", the rule inset and meter dim to 35 % and the board's frame pulses once. The demand returns on "motives", the match on "patterns", and the inset on "a demand of one third" | sheet 2 (0:23–0:29) |
| "Replay 1 corners" (craft 10, substance 4) | "Replay one block. [pause 0.3]" and "our block's chain". Whisper now hears "Replay one block." | transcript 1:10.3 |
| Blind test (substance 2) | Our town is shown turned a quarter turn in the two-town test (the share and texture are unchanged: `avg_share(rot90)` = 0.7553). On "Look again at the first town" it turns back while it grows home: a rigid rotation of the whole board, one move | sheet 10 (2:53–2:59), frames 203.6 / 204.0 s |
| Caveat line (substance 6) | "With at most eight neighbors, shares come in steps." The highlight sweep and the 0 % / 60 % end marks arrive on "shares" | sheet 7 (2:05) |
| HOLC link (substance 7) | "Real segregation has other causes. One study finds…". The toy towns dim to 55 % under the link sentence and to 30 % across "1930s federal lending maps", so the beat is never static for 4 s | sheet 11 (3:11–3:17) |
| Chart line pace (craft 2, substance 8) | "That whole town is one point on this chart" is spoken at 0.78. There is already 1.5 s of silence before it, so no extra pause was added (it would have made a 2.2 s gap) | report: 0 sentences above 200 wpm |

### Found on the first round-6 master and fixed before the final one
- **4.5 s static stretch at 3:13 (report FLAG).** The new HOLC wording ended the towns' dim before "study", which left the frame frozen. The two-stage dim (55 %, then 30 %) removed it. The longest static stretch is now 3.8 s (the two-town prediction hold).
- **A flying ⅓ crossed the 2/7 (2:13).** The copy that flew from the caret's ⅓ into A's formula passed through "2/7 <". The formula's ⅓ now fades in while the caret's ⅓ pulses.
- **"? demanded" finished after "As Schelling" began (3:25).** The town landed on "town", so the meter and the "?" did not fit in the 1.2 s pause. It now lands on "first".
- **Two short lines over 200 wpm.** The merged "Two gold out of seven, less than a third, so now it wants out." measured 204 wpm at 0.82, and the chart line 201 wpm at 0.80. They are now at 0.80 and 0.78.
- **Runtime.** The first preview ran 3:38.5. To bring it back to 3:34.5, the beat gaps that only padded transitions were shortened (C → "Now" 0.6 → 0.3 s; the chart line's gap 1.2 → 0.9 s; Schelling 0.45 → 0.25 s), "Is it still content? [pause 1.2]" became [pause 1.0], and three phrases were cut: "at all", "Two sevenths is", and "also … besides preference" → "other causes". "In his 1971 paper" was kept, because "In 1971, … ran" would misdate runs first issued in 1969 (facts R6-9).

### Mechanics of the final master
Runtime 3:34.5, 479 words. Pace is 152 wpm over speech time, with no sentence above 200 wpm (the median sentence runs 168). Loudness is −14.0 LUFS with a −1.9 dBTP true peak. Leading silence is 0.00 s and trailing silence 1.77 s. The longest internal silence is 2.08 s (the planned holds at 0:09 and 3:03), and the longest static stretch is 3.80 s. The longest run without a breath is 13.6 s. WER is 0.2 %: whisper writes "blocks" for "block's". There are 0 render warnings, and the layout audit found 0 issues in 229 checks. There are 0 glyph morphs, 14 of 14 deictics land, review-kit flags are 0, and banned phrases are 0. The only repeated phrase the kit lists is "household at three eighths" (2:16, 2:31). It is a deliberate callback: the same rung is named before and after the demand moves.

### Left as is, by judgment
- During the ring draw (0:41–0:52), the content households dim to 55 %, so the dimmed gold reads darker. They are context for 10 s, and every household returns to full colour on "Round one".
- The ladder still has no numbered vertical axis. The counts 67, 125 and 76 sit on the bars the narration names, and a tick column would add three labels to the busiest frame of the episode.

## Round 7 revisions

Round 7 failed at 8.9 (craft) and 8.7 (substance). Neither critic found a factual error or a cap, and both said their fixes would reach 9. This pass applies every fix from both reviews (one in a different form, explained below) and keeps all the "keep" items: the "? demanded" marker sliding 76 % → ⅓ and coming back on the restored first frame, "plan predicts 0" against the live 74 and the dim-all-but-the-67 frame, the real-tile domino, the town flying into its dot, the x-axis becoming the ladder's baseline, the caret crossing exactly two bars, and the blind two-town test.

### Plan (written before editing)

| Dimension (round-7 scores) | BAR "9" anchor | Where the round-7 master fell short | Upgrade |
|---|---|---|---|
| Visual (8.5 / 8.5) | "Every frame has one focal point; all §5 standards met" | 13 prose words at 2:34.5; the ladder had no height scale; the test boards were at 5 % when "Two simulated towns" began; "our jump" floated 1.5 units above the dots it joins; the 30-town clouds read as glowing crosses, then smudges; five HUD rows under a beat about one number | "households" as the ladder's y title (11 words at most); a GRAY "256" over the tallest bar; both towns and labels fully in before "Two"; "our jump" at 82 % over our two columns with a dotted drop; solid-dot swarms with a background rim and no mean cross, dimmed by colour; "round" and "moves" dim to 35 % at the stall |
| Clarity (9 / 8.5) | "Viewer could re-derive it after one watch" | the 14.7 s Schelling sentence carried three qualifiers, two with no picture; the 125 was drawn but never used; "finds … through reduced credit" overstated the paper's "suggest" | three sentences with pauses, with "nearest move" and "25–30% empty" labels on their words; "All one hundred twenty-five households at three eighths…" with the 125 and its bar pulsing; "Its authors point to reduced credit" |
| Audio (9 / 8.5) | "pauses are intentional" | the Schelling sentence had no pause over 0.31 s for 26 words | [pause 0.4] and [pause 0.5] between its three sentences, spoken at 0.82 |
| Concision (9 / 8.5) | "Cutting any sentence loses something" | "If the plan had worked, this counter would read zero" restated the HUD row; "the other thirty-eight were content by their turn" restated the note; "both seventy-six percent" read the labels aloud | all three cut; the stall is shown live instead |
| Hook (9 / 9) | "tension rises through build and fail" | the 74 sat on screen 6 s before it was spoken | the count stalls on screen as "The unhappy count stalls at seventy-four" is spoken, then "plan predicts 0" pulses in the silence |
| Originality (9 / 8.5) | "a non-obvious angle viewers would remember" | the real-world sentence read as an appended disclaimer ("Real segregation has other causes") | "Real cities have rules too", with the rule town's "· placed by a rule" header pulsing: the study follows from the two-town test |

### What changed (every round-7 fix, both critics)

| Fix (critic #) | Change | Checked on the final master |
|---|---|---|
| Word load at 2:34 (craft 1) | Ladder y title "households" (was "households (simulated start)"): 11 prose words at the ¼ mechanism frame | ladder keyframes 2:27–2:31 |
| Near-empty frame under "Two" (craft 2) | The chart cuts out (0.6 s), then both towns, the tag and both "76% match" labels fade in (0.6 s) before the beat starts, so they are at 100 % on "Two" | sheet 10 (2:49) |
| Ladder scale (craft 3) | GRAY "256" (MathTex 32) over the ½ bar, the tallest, arriving once the highlight sweep has passed it (in the first preview it sat in the path of the bar's 1.18× stretch) | sheet 7 (2:03) |
| Breathless Schelling sentence (craft 4, substance 1) | Three sentences: "In his 1971 paper, Thomas Schelling ran this model. [pause 0.4] His households moved to the nearest square that suited them, on far emptier boards. [pause 0.5] There the jump came later, between about a third and a half." at 0.80. GRAY "nearest move" on "nearest" and "25–30% empty" on "emptier", under "Schelling: 35–50%" | sheets 9–10, Schelling keyframes |
| "both seventy-six percent" (craft 5) | Cut to "Two simulated towns. [pause 0.6]"; both "76% match" labels pulse together in the silence | sheet 10 (2:49–2:51) |
| Floating "our jump" (craft 6) | Bracket at 82 %, ends over the ¼ and ⅓ columns, with a dotted drop from its left end to the ¼ column; drawn on "model" with the box on the two towns; it rises to the top row and slides to 35–50 % on "There", on a path that bends away from his rules' text | sheets 9–10 |
| Unused 125 (substance 2) | "All one hundred twenty-five households at three eighths are one lost match from two sevenths." The 125 fades in and pulses with its bar on "one hundred twenty-five", the 3/8 rung pulses on "three eighths", the arrow draws on "lost match" | sheet 8 (2:11–2:15) |
| HOLC pivot and "finds … through" (substance 3) | "Real cities have rules too. One study finds that 1930s federal lending maps raised racial segregation for decades. Its authors point to reduced credit." The rule town's "· placed by a rule" pulses on "rules too" (about its left edge; zone lines not pulsed); the two-stage dim is kept | sheet 11 |
| Failure read out late (substance 4) | "If the plan had worked, this counter would read zero. It reads seventy-four." → "The unhappy count stalls at seventy-four." The last 12 hops of round one land one by one under "The unhappy count", so the count visibly slows (82 → 74) while "moves" ticks to 200, and freezes on "stalls"; "plan predicts 0" pulses in the 1.2 s after "seventy-four" | sheet 4 (0:55–0:57), frames 52.3–58.6 |
| 38 restated (substance 5) | "Round one: two hundred moves." The note "38 content by their turn" arrives as "moves" reaches 200 and holds ≈ 2.5 s before it gives its slot to "67 content at the start" | sheet 4 (0:57) |
| Glowing crosses (substance 6) | Each demand's 30 towns are solid dots (r 0.05, 100 %, a 1.6 px background rim, ± 1 pp spread by rank). The mean tick and whisker are gone. Dimming recolours the dots instead of lowering their opacity, so overlaps never build a brighter core. Our two towns are ringed markers on a small background disc, so they stay visible inside their columns | kf 1:50, 2:45, 2:47 |
| Busy HUD at the stall (substance 7) | "round" and "moves" dim to 35 % as the count freezes; both return at full strength for rounds 2–7 | kf 0:55, 1:02 |
| Word load counting the citation (found while checking) | Past critics counted the citation as prose (this episode, round 5: "about 22 words"). The x title is now "demanded (%)" and the "our jump" tag fades as "nearest move" arrives (bracket and drop stay), so no Schelling frame carries more than 12 words, counting the 5-word citation | Schelling keyframes |

### Found on the first round-7 master and fixed before the final one
- One sentence at 202 wpm ("There the jump came later…", at 0.82). The Schelling beat is now spoken at 0.80, as the craft critic suggested.
- The Schelling frame came to 13–14 words counting the citation (see the last table row).
- whisper wrote "a quarter" for "Demand a quarter" and repeated "happy" after "unhappy" at a segment boundary. Kokoro's own timings give "Demand" 0.39 s, and these clips are byte-identical to round 7, where whisper heard both correctly.

### Mechanics of the final master
Runtime 3:30.9 (was 3:34.5), 467 narration words (was 479). Pace is 153 wpm over speech time, with no sentence above 200 wpm (the median sentence runs 168). Loudness is −14.0 LUFS with a −1.9 dBTP true peak. Leading silence is 0.00 s and trailing silence 1.77 s. The longest internal silence is 2.09 s (the planned prediction holds) and the longest static stretch 3.63 s (the cold-open prediction hold). The longest run without a breath is 11.7 s (was 13.6 s). WER is 0.2 %: whisper writes "blocks" for "block's". There are 0 render warnings, and the layout audit found 0 issues in 232 checks. There are 0 glyph morphs, 13 of 13 deictics land, review-kit flags are 0, and banned phrases are 0.

### Left as is, by judgment
- The HOLC frame (3:09–3:20) carries the two towns' headers, the two "76% match" labels, the "simulated" tag and the 6-word citation. Counting the citation, that is about 15 words. Rounds 6 and 7 accepted it, and each label is needed there: "· placed by a rule" is what "rules too" points at, and "76% match" is what pulses on "segregation".
- "a quarter empty" (a critic's wording) was not used: "a quarter" is a demand level in this episode. The narration says "far emptier boards", and the label gives his 25–30 %.
- The critic's dashed short hop on the thumbnail for "nearest" was not drawn. At 2 units wide a one-square hop is 0.05 units, too small to see, so the rule is shown as the label "nearest move" on its word.

## Round 8 revisions

Round 8 failed at 8.9 (craft) and 8.8 (substance). Neither critic found a factual error or a cap, and both said their fixes would reach 9. This pass applies every fix from both reviews and keeps the "keep" items: the "? demanded" marker sliding 76 % → ⅓ and returning on the restored first frame, the "guess 0" row (was "plan predicts 0") against the live 74 with the dim-all-but-the-67 frame, the real-tile domino with fractions built from tile copies, the town-to-dot flight, the x-axis-to-baseline morph, the caret crossing exactly two bars to 2/7 ≥ ¼, and the blind two-town test.

### Plan (written before editing)

| Dimension (round-8 scores) | BAR "9" anchor | Where the round-8 master fell short | Upgrade |
|---|---|---|---|
| Clarity (9 / 8.5) | "Viewer could re-derive it after one watch; all numbers check out" | the ¼ side said a 3/8 household "can lose a match and stay", which is true but not why the curve jumps: 190 content households are still one lost match from tipping at ¼ (210 at ⅓). "plan" implied a planner; "stalls" implied the count was stuck | the mechanism is the spark: the two bars that change sides were the only movers with two matching neighbors (274 matches stripped at ⅓ against 62 at ¼, verified in facts R8-1); "The obvious guess: zero unhappy …"; "stops at seventy-four, not zero" with the meter pulsed |
| Visual (8.5 / 8.5) | "Every frame has one focal point; all §5 standards met" | full-strength thumbnails beside the hatched band; the "our jump" bracket unlabelled for 4 s; 15 prose words on the HOLC frame; "76 67" read as one string; the ladder silently cropped at 60 % | thumbnails dim to 35 % on "His households"; "ours" stays until the slide; "· placed by a rule" and the centre tag leave on "One study"; counts ≥ 0.32 apart; "+421 above 60%" |
| Motion (9 / 9) | "Every motion encodes a relation" | the bracket skewed mid-slide (Transform between differently shaped brackets) and grazed "25–30% empty" | one level bar (width and centre set each frame), rise then slide, rules placed so the path stays ≥ 0.25 clear; asserted over 41 samples of the path |
| Audio (9 / 9) | "each deictic lands as the element highlights" | "our household" pointed at B after the outline had moved to C | B's red ring pulses on "our household" |
