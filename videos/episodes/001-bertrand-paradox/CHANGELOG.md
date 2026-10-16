# Episode 1 — changelog

## Round 1 revisions

Round 1 review: craft 8.2, substance 7.9; neither passed. Both critics named the same two structural gaps, and both are now visual beats.

**Structure**
- **The invariance test is shown, not asserted** (craft 1, substance 1). The payoff floor now holds a big circle and a smaller, off-centre circle inside it. Straws give 0.50 on both. Each program's chords are then rained on the big circle and judged on the small one, and a scoreboard fills row by row: midpoints 0.25 ≠ 0.41, endpoints 0.33 ≠ 0.47, radius 0.50 = 0.50, which matches the straws row. The numbers come from `sim.py` (seeded samples within 0.002 of a 2M-line check) and are recorded in facts.md.
- **A data-science consequence with real data** (craft 2, substance 2). The spinner beat is gone. A new class-size beat follows it: bars of 10, 10 and 100. Counting each class once gives a mean of 40. As each bar widens in proportion to its students, the mean line rises continuously to 85. Then come the real figures: Stony Brook, 1974, 737 classes, 40 per class vs 147 per student (Feld & Grofman 1977, *Research in Higher Education* 6(3):215–222, checked against the paper's PDF). I used the class-size paradox rather than the friendship paradox because episode 60 covers the latter. The stakes line now reads "Every poll and every simulation has to decide what they mean". The closing line points back to the class-size beat ("…the same way forty and a hundred and forty-seven are both right").

**Fixes**
- The (r/2)/r = 1/2 and π(r/2)²/πr² = 1/4 equations are now built in the tally row, from the radius halves and from the two disks' outlines dropping straight down. No more blob crossing labels (craft 7, substance 3). The histograms no longer have to vanish to make room. The 1/2 stays up through the whole endpoint beat and folds into the tally at the next beat (craft 3). The 1/4 is up for ≥ 4 s.
- The endpoint recipe's 1/3 is now derived: its five gold histogram bars stack into one column labelled 0.334, then the 1/3 flags (substance 6).
- The histogram caption sits as two lines directly over the purple histogram until the green one appears, then moves to the middle of the row (craft 8).
- Panel transition: the sweep and question fade first, then the panel moves, then the tally moves, and the exact 1/3 travels over from the arc equation. Every caption change is a fade, not a glyph morph (craft 6).
- Settled chord rains dim to 30 % (craft 13). Panel 2 enlarges ink-only, with no rain, label or tally (substance 10).
- The Bertrand quote is split into two lines, and the recipe labels dim while it is up (substance 8). Narration now says "twenty-five percentage points" and the brace reads "25 points" (craft 9, substance 5).
- "Rim, radius, area": a fresh thick green radius draws on "radius" (craft 10).
- The Jaynes beat opens with the scoreboard slot ("–") and the citation already up (craft 12).
- "128 real tosses" is now "128 straws crossed it", and the narration says "the hundred and twenty-eight that crossed it" (substance 4; Jaynes §6 counts 128 *successful* tosses).
- Skilled tosser: the real-experiment labels and the radius row dim to 30 %, and a "simulated" tag sits beside the climbing tally (craft 5, substance 9).
- The "Change the machine" line is gone, along with its swallowed word (craft 11, substance 7).
- Landing: the marker sweep reveals 1/4, 1/3 and 1/2 as it passes them. The final frame holds 1.5 s after the last word. No end card, so trailing silence stays under 2 s (craft 4).

**Found in my own frame review (not in the round 1 reviews)**
- 0:45, the 120°/360° build: the circle-to-glyph morph made a filled grey blob. Both disk-to-equation builds now go outline → shrink to icon → travel → cross-fade into the term (`drop_into`).
- 1:13–1:21: the number line now sits lower, so the two-line quote and the "25 points" label clear the error bars and the tallies by ≥ 0.15.
- Transitions are sequenced, so nothing fades in on top of something still moving: the tally lands before its ≈ appears, a derivation fades before its result slides into the tally row, the quote leaves before the brace grows, the old caption leaves before the new one arrives, and the failed scoreboard rows leave before the radius row moves up.
- Skilled tosser: the pull finishes before "answers", so 1.00 holds for about 1 s. The class beat now opens on the chart frame plus its real-data header and citation, with no blank frame. The per-student label only appears once its line has cleared the 40 line.

**Mechanics (review/report.md):** 3:43.3, 160 wpm in speech, −14.0 LUFS / −1.6 dBTP, longest silence 1.92 s, longest static 2.80 s, trailing silence 1.90 s, 0 render warnings, 0 banned phrases, WER 2.3 % (homophones only: chord/cord, poll/pole, Jaynes/Janes).

## Round 2 revisions

Round 2 review: craft 8.4, substance 8.6; no caps, no factual errors. Both critics said every fix together reaches about 9.0, and both named the class-size beat as the main gap: it was attached, not welded. Each critic's other fixes are below.

**Plan for the climb (BAR §12.2), per dimension scored below 9**
- *Clarity (8.5/8.5; 9 = "viewer could re-derive it after one watch; assumptions stated").* The class beat never said "at random", the toy data sat under the real header, bar width was unlabelled, the Jaynes test skipped its premise, the stacked 1/3 column sat on the wrong bin, and "fit that prediction" overstated Jaynes. → All of these now say or show their link.
- *Visual (8/8.5; 9 = "one focal point per frame; nothing to remove").* The invariance frame was cluttered, the small circle's gold rule was lost under the chords, there was a dangling "≈", 147 sat on the toy scale, and the landing incircle drew as a wedge. → Dim or clear context in sequence, add a halo, give the real data its own block, and draw outline then fill.
- *Motion (8.5/8.5; 9 = "every motion encodes a relation; reading time respected").* The 0:46 equation held 0.6 s, the icon shrink flew in about 0.4 s, the tally and 1/3 drifted apart from their panel, and the disk passed over the tally. → Hold ≥ 3.2 s, one 0.85 s lift per term, move the tally and 1/3 with the panel, and keep fades and moves from overlapping.
- *Audio (8.5/8.5).* "forty and a hundred and forty-seven" was heard as three numbers. → "a hundred forty-seven", checked with Whisper.
- *Hook, Originality, Concision (8.5–9).* The class beat played like an appendix. → It now reuses the episode's own picture (dots = what is spread evenly) and the stakes line's "two words", and the closing numbers stay on screen. "Jaynes also named the limit:" is cut.

**Class-size beat, rebuilt (craft 1, 2, 8; substance 1, 2, 6, 7)**
- Narration: "Surveys hide the same two words. … Pick a class at random, and the average size is forty. Pick a student at random, and it's eighty-five. At Stony Brook in nineteen seventy-four, that was forty for a random class, and a hundred forty-seven for a random student."
- The chart opens as the toy only, with a grey italic "example" tag, "class size (students)" and the citation. On "the same two words", the stakes beat's italic "at random" returns in its old place, and it flags on "Pick a class at random". "Pick a class at random" puts one dot under each equal-width bar. On "Pick a student at random" each class dot splits into its students (10, 10, 100 dots, the midpoints' dot style), every bar widens to its students' width ("width = students" appears), and the mean line rises continuously from "random class 40" to "random student 85".
- On "Stony Brook" the example dims to 30 % and loses its word labels. A separate framed block appears ("Stony Brook, 1974 · 737 classes"), then "- - - random class 40" on "forty" and "—— random student 147" on "forty-seven". The line glyphs match the example's two lines, and the block is not on the example's scale. A 1.0 s pause holds the finished frame.
- Landing: the Stony Brook block clears first. Then 40 and 147 travel, untouched by any label, to a dimmed grey "40 · 147" pair under the 0–1 line, right of 1/2, and they brighten on "forty". The closing clause now names numbers that are on screen.

**Other fixes**
- 0:41–0:53 (craft 4, 10; substance 11).
  - A copy of the gold arc flies straight into "120°" (0.85 s), then a copy of the whole rim (it turns blue) flies into "360°". There is no icon shrink. Each copy shrinks before it travels, so nothing large crosses the caption, and the fraction bar and terms arrive together.
  - A 1.5 s pause after "a third of the rim" holds the equation and the arc unchanged through "Case closed" (≈ 3.5 s).
  - On "a second way" only the question, the caption and "120°/360° =" fade (0.35 s). Then one 0.95 s move:
    - the circle shrinks into panel 1 and its triangle turns back upright;
    - the sweep chord and the arc shrink with it as they fade;
    - its label arcs over the circle, its tally dips under it, and the exact 1/3 travels with them.
  - Each tally now drops a plain dot onto the shared number line, instead of morphing its digits into a dot over the tally.
- 1:25 / 1:43 (craft 9). The number line, error bars and brace fade before the enlarge starts. Panel 2's label and tally return only after the circle has landed.
- Dangling "≈" (craft 6). The ≈ now arrives in the same animation as the π(r/2)² and r/2 numerators. The disk outlines use the same one-move lift as the arc.
- Endpoint stack (substance 3). TransformFromCopy copies of the five gold bars stack in their own column left of the axis origin, with no tick and labelled 0.334. The originals stay in place at 35 %, so the histogram still shows the rim pile-up.
- Invariance test (craft 3, 7; substance 4, 9).
  - New premise line: "One rain lands on both circles at once, so a program that matches the straws must score the same on both." This is the substance critic's premise. It states the pass criterion and drops the mechanism sentence, which the picture already shows, and it is 1.5 s shorter than the suggested wording. The other straws dim, one straw is followed, and dots mark where it crosses each rim. The straws row (0.50 = 0.50) flags on "matches the straws".
  - All three program rows appear with "–" cells, and each turns into live numbers only when its own rain starts.
  - On "same" the big triangle leaves and the big incircle dims to 20 %.
  - Small-circle chords are drawn at 70 %, under the small incircle (stroke 4.5 on a dark halo).
  - On "like the straws" the failed rows dim and the program chords clear. The small circle and the failed rows leave before the straws return.
- Tyler (substance 5): "…matched the radius program's spread of chord lengths." The radius row flags on "radius program's".
- Limit (substance 8): "A skilled tosser, Jaynes noted, could produce other answers."
- Landing incircle (craft 5, substance 10): the outline is drawn first (0.8 s), then the fill fades in (0.4 s).

**Found in my own frame review (not in the round 2 reviews)**
- Spacing. The toolkit's new layout audit found 26 places where text sat under 0.15 from another object: histogram ticks, the "25 points" label, the bar highlight boxes, the "simulated" tag, the class-bar labels, the r/2 label, and the π(r/2)² numerator against panel 3's dots. All were re-spaced. The tally row moved down 0.07, and the boxes now stop at the baseline. The audit now reports 0 issues.
- Transients found in 0.3 s frame sweeps:
  - At 0:51 the moving label clipped the shrinking circle. It now arcs over it.
  - At 0:52 the tally-to-dot morph garbled the digits. Each tally now drops a plain dot instead.
  - At 3:39 the 40 crossed the fading "random student" label. The block now clears first.
  - At 3:28 the "random student" label faded in too close to the 40 label.
- The three class dots were left behind after the split. They now hand over to the 120 student dots.

**Mechanics (review/report.md):** 3:49.3, 163 wpm in speech, −14.1 LUFS / −1.7 dBTP, longest silence 1.92 s, longest static 3.5 s (the planned hold on the finished Stony Brook frame), trailing silence 1.78 s. 0 render warnings, 0 layout-audit issues, 0 banned phrases, 0 flags. WER 3.7 %, homophones and number formatting only (chord/cord, Jaynes/Janes, "a hundred" → "100"). Whisper hears "147" both times.

## Round 3 revisions

Round 3 review: craft 8.6, substance 8.6; no caps, no factual errors. Both critics said every fix together lands at about 9.0, and both put the remaining defects in the story logic of the Jaynes test and in the last 35 s.

**Plan for the climb (BAR §12.2), per dimension scored below 9**
- *Clarity (8.5/8.5; 9 = "viewer could re-derive it after one watch").* The test asked programs to "match the straws", but the simulated straws are the radius program by construction (circular). The step "a program's chords are judged on the small circle" was hidden. The midpoint pivot was announced, and each recipe had three names. → Invariance itself is the criterion: the straws row reads "? = ?" (unknown, but the same on both circles), one program chord is judged on both circles before its rain, the real 128 tosses are the arbiter, the pivot is motivated ("One point sets a chord's length: its midpoint"), and the names are unified (panel "random radius point"; rows "midpoint / endpoints / radius" exactly as spoken).
- *Visual (8.5/8.5; 9 = "every frame has one focal point; nothing to remove").* Orphan toy 85/40 beside Stony Brook, "40 · 147" read as axis values, a near-empty survey opening with an oversized "at random", an empty scoreboard void, a misaligned "r" tick. → Remove or re-seat each of these.
- *Motion (8.5/9).* A fade to near-black opened the survey beat and parts were left behind at 3:29. → Cross-fade straight into "at random" and grow the chart with its bars; nothing left behind.
- *Audio (8.5/8.5).* Every gap was the TTS default 0.4 s. → Planned pauses after the thesis line (1.0 s), after the limit line (0.8 s), after each scoreboard row (0.75 s) and after the result (1.0 s).
- *Hook (9/8.5).* The last line erased Jaynes's resolution. → "Name the way, and only one is", shown on the opening image: the green 1/2 gets a "straws" tag and the other two dim; the Stony Brook pair sits in its own row as "random class 40 / random student 147". The stakes line now says "survey", which pays off at "Surveys hide the same two words".
- *Concision (8.5/8.5).* → Jaynes setup rewritten as one sentence (−1.6 s), Tyler line trimmed (−1.2 s), "like the straws" dropped; the spent time buys the planned pauses.

**Story fixes (substance 1, 2, 3, 5, 8)**
- *The test is no longer circular* (substance 1). Narration: "One rain lands on both circles at once, so an honest program must score the same on both." The simulated straws are drawn as lines only, never tallied in the test, and their row reads "straws ? = ?" (unknown, but equal on both circles). The "? = ?" flags on "the same on both" and again with the radius row's "=" on "on both". The real 128 tosses (Tyler beat) are the arbiter, and the radius row flags on "radius program's". The simulated straws are judged and tallied only in the "skilled tosser" moment, where the "?" hands over to a live share with a "simulated" tag. "Like the straws" is gone.
- *The ending keeps Jaynes's resolution* (substance 2, craft 2). "So whatever number you picked, some way of drawing chords makes it right. Name the way, and only one is. Forty and a hundred forty-seven are both right, once you say who's picked." On "Name the way" a "straws" tag appears beside the green 1/2, which flags; on "only one is" 1/4 and 1/3 dim to 30 %. The Stony Brook pair is no longer a grey "40 · 147" under the axis. Its two rows ("- - - random class 40", "—— random student 147") step down, dimmed, into their own rows left-aligned with "P(" and 0.6+ below the 1/3 label. They brighten in INK on "Forty", their numbers flag on "both right", and their labels flag on "who's picked". The 0–1 line is drawn before the sweep, with ticks only at 0 and 1.
- *The midpoint pivot is motivated* (substance 3): "One point sets a chord's length: its midpoint." The chord draws on "length", then the midpoint dot on "midpoint". I used a shorter line than the suggested one (+1.2 s instead of +3.5 s).
- *Jaynes setup in one sentence* (substance 5): "…Edwin Jaynes said a physical process picks one: straws tossed from a standing height can't be aimed, so the answer can't depend on where the circle sits or how big it is." (−1.6 s). Tyler line: dropped "then" and "on the floor" (−1.2 s).
- *Stakes* (substance 8): "Every survey and every simulation…", which pays off at "Surveys hide the same two words".

**Craft fixes**
- *Orphan toy numbers* (craft 1, substance 4). On "Stony Brook" the toy's line labels leave with their numbers (40 and 85). Only the dimmed lines remain, so the only bright numbers are Stony Brook's.
- *Breaths* (craft 3, substance 6). [pause 1.0] after "At random never said which" (the flagged labels hold still, and the panels clear after it). [pause 0.75] after each failed scoreboard row. [pause 1.0] after "a half on both" (the finished board holds ≈ 2.3 s before "Jaynes and Charles Tyler"). [pause 0.8] after "could produce other answers" (the 1.00 holds). The arc pause went from 1.5 to 1.2 s and the Stony Brook pause from 1.0 to 0.6 s, to pay for them.
- *How a program is judged on the small circle* (craft 4). Before the midpoint rain, one line of that rain is shown judged twice. Its chord of the big circle is drawn grey (0.59 R from the centre, so short there). Then the piece of the same line inside the small circle turns gold (0.39 r from its centre, so long there): same line, two verdicts. The small circle lies inside the big one, so the big chord already runs through it and no extension is needed.
- *Survey opening* (craft 5). There is no fade to an empty frame and no empty baseline. The floor clears and the stakes beat's "at random" is written large, as the frame's one subject, on "the same two words". On "Take classes" it travels up to become a 70 % caption above the chart title, right-aligned to the chart, and the title fades in. The baseline draws with the first bar. The caption flags on each spoken "at random" and leaves on "Stony Brook".
- *Scoreboard void* (craft 6). The label column now starts at x = 1.63 (≈ 1180 px, 0.7 from the floor box) and the number columns moved left with it. The "straws" row label is up from the first frame at 40 %, with its dash.
- *One name per recipe* (craft 7). Panel 2 is "random radius point". The rows read "midpoint / endpoints / radius", and the narration says "Midpoint gives…", "Endpoints give…", "the radius program", "the endpoints program".
- *"Piles them against the rim"* (substance 7). On "rim", panel 1's outer ring (0.9r–r) and the last histogram bar (0.284) light up blue together for 1 s.
- *Tick baseline* (craft 8). "0", "r/2" and "r" now share one baseline on all three histograms.

**Found in my own frame review (not in the round 3 reviews)**
- The first survey opening I built (a small caption written on an empty frame) left the frame nearly empty for about 2 s. "At random" now arrives at the stakes beat's size as the frame's one subject, then travels to its caption slot. The chart title fades in only after it has passed, because a 3:19 frame sweep showed the moving words crossing the end of the title.
- The demo chord first ran 1.2 s, too fast to read. It now draws for 0.6 s, its inner piece for 0.6 s, and it holds for 0.25 s. The midpoint rain runs to just after "quarter", so it still gets about 2 s.
- The closing flags on "both right" and "who's picked" scaled the two Stony Brook rows as one group, which pushed the labels into their glyphs and numbers (3:49). Each item now flags on its own.
- The "?" to simulated-share handoff in the skilled-tosser moment cross-faded into an overprinted "0.?50" (3:11). The "?" now leaves before the number arrives.
- The audit flagged two clearance problems. The rim highlight box sat too close to the histogram caption, so the bar itself now turns blue. "At random" sat too close to the chart title, so it is now Text 28, shifted right.

**Mechanics (review/report.md):** 3:51.3, 161 wpm in speech (152 overall), −14.0 LUFS / −1.6 dBTP. Longest silence 1.92 s, the planned "Pick a number" hold. Longest static 3.0 s. Trailing silence 1.81 s, no black frames. 0 render warnings, 0 layout-audit issues in 252 checks, 0 banned phrases, 0 flags. WER 2.0 %: homophones and number formatting only (chord/cord, Jaynes/Janes, "a hundred" → "one hundred").
