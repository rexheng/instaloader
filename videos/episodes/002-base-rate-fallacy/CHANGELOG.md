# Episode 2 changelog

## Round 1 revisions

Reviews: `reviews/round1-craft.md` (7.9) and `reviews/round1-substance.md` (7.9). Neither critic
claimed a factual error. Both put Originality at 6 because the hook numbers and the
independent-retest-to-91 % beat follow Veritasium's *The Bayesian Trap* (2017), and the ceiling
rule then capped the score at 8. So this round is a restructure, not a polish pass. Every new
claim was checked against its source before use (facts.md §B, §C).

**Structure (both critics' fix 1)**
- Cold open: the viewer now commits against a real baseline. "Most doctors given a problem like
  this got it wrong. Pick a number." A ghosted 10 × 10 waffle of gynecologists (21 green =
  "21% got it right") appears with the Gigerenzer et al. 2007 citation. The empty meter is ghosted
  at 30 % from frame 1 and brightens on the question (craft 10), so the first frame is balanced.
- The retest-to-91 % beat is deleted. In its place, in the same strip-and-meter picture, is a
  data-science consequence. At the 2017 Champions League final in Cardiff, face-recognition
  cameras raised 2,470 alerts and only 173 were right, which is 7 % (South Wales Police figures,
  BBC News 2018). The 110-person strip becomes a 26 × 95 raster of the 2,470 alerts under a bar of
  exactly the same width, so its 173 red cells sit on the meter's 7 %. A legend redefines
  red/blue as on / not on the watch list. The meter title goes "chance you're on the list" →
  "precision". Fraud (craft's example) was not used because episode 44 covers fraud and class
  imbalance.
- The landing's single 1-in-100 jump is now a live prior sweep (substance 1b). The prevalence
  label counts from 1 in 1,000 to 1 in 100 (meter 50 %) to 1 in 2 (meter 99 %, on the returning
  "naive 99%" marker), which explains why the half-sick check worked. Then it returns. The arrows
  are flows whose widths track the share reaching +.
- Gigerenzer stays as the payoff, introduced with "Back to those gynecologists" as a callback to
  the cold open.

**Insight beat**
- When the negatives vanish, the 110 survivors swell to dots of radius 0.082 in the same animation,
  and the ten sick keep their rings (craft 2).
- The strip now hangs *under* the meter bar, so the title "chance you're sick" sits above the bar
  in every scene (substance 8).
- Braces under the strip count "10" (red columns) and "100" (blue columns) before the fraction is
  built. The fraction's terms fly from those labels, not from the dots (no smear). "≈ 9%" flies
  from the meter's value label on the newly spoken "about nine percent" (craft 7, substance 2).
- 10 vs 9.9: the table's results morph to 9.9 and 99.9 as "nine point nine" and "ninety-nine
  point nine" are spoken (substance 3).
- After the counts are used, the table dims to 30 % and the "people" header goes (craft 5).
- The names come in two flagged steps: 0.001 / 0.999 → P(sick) / P(healthy), with the table's head
  counts flashing, then 0.99 / 0.01 → P(+∣sick) / P(+∣healthy), with the table's arrows flashing.
  The numeric form holds about 5 s first (craft 4). "Bayes' theorem" sits under the left-hand side,
  not floating above it (craft 5).

**Fail beat**
- The 4,990-dot recolour starts on "Now make the disease rare" (2.4 s). The counter reads
  10 / 9,990 before "That leaves ten sick people" (substance 6).
- The 99 % copy to the meter flies only its label, on an upward arc, so the copy never overlaps
  its source (craft 7, substance 7).

**Payoff**
- The gynecologist waffle ("per 100 gynecologists") replaces the decorative white dots. Each
  answer's dots line up in its row, one dot per 1 %, and become the bar: the 21 green on
  "twenty-one", then 47 / 13 / 19 on "most common" (craft 6, substance 4). The waffle label fades
  before the axis title writes (craft 8).
- Values ride 0.2 units right of their bar ends and move with them through before → after. The
  25 % guessing line is up only while it is the comparison, and the values step clear of it
  (craft 9). The mini diagram keeps "cancer" / "no cancer". The citation clears the axis title.
- There is no blank frame before the landing. The chart fades while the mammography diagram
  slides into the cold-open position and morphs: 1 in 100 → 1 in 1,000, 90 % → 99 %, 9 % → 1 %,
  cancer/no cancer → sick/healthy. It is introduced by "Their problem is yours with different
  numbers" (craft 3).

**Audio**
- Pauses inside a thought are now 0.2 s. "That's nine percent", "The rule said ninety-nine.
  Eleven times too high" and "Only twenty-one percent chose it…" are their own beats at speed 0.80,
  each followed by a 1 s pause (craft 11).
- The stakes line is concrete: "At ninety-nine percent, you'd start treatment today" (substance
  5). It does not give the 9 % away before the count.
- The "scan scan" ASR artefact can't recur: the line now reads "the mammogram catches ninety
  percent" (substance 9).

**Other**
- The end card's Ω is in ink, not blue, because blue means "healthy" here (substance 10).
- facts.md has new sections for the cold-open baseline, the Cardiff figures (including that the
  press's "92 %" is really 93.0 %; the video shows counts and 7 % instead) and the prior sweep.
  check.py recomputes the new numbers.

**Self-check after the revision** (review kit on the 1080p master): runtime 3:46.5, 155 wpm on
speech time, −14.0 LUFS / −2.1 dBTP, longest silence 2.06 s (the planned prediction hold), longest
static stretch 2.9 s, WER 2.7 %, no banned phrases, 0 render or layout warnings. Two passes on the
preview and the master caught and fixed these:
- the 25 % line crossing the 13 % and 19 % values;
- the "99%" label sitting on the widest flow during the sweep (rate labels moved out to 0.68 units,
  total flow width 0.45);
- the waffle label reading as one line with "cancer";
- a 4.0 s still frame before the Cardiff alerts (citation now on "twenty seventeen", dissolve on
  "Cardiff");
- mixed MathTex/Text baselines in "173 right" / "2,297 wrong" / "2,470 camera alerts";
- the chart overlapping the diagram mid-morph (the chart now clears in the first 30 % of the move,
  and "100" morphs in place into "1,000").

## Round 2 revisions

Reviews: `reviews/round2-craft.md` (8.4) and `reviews/round2-substance.md` (8.4). Neither critic
found a factual error. The substance critic said polish alone tops out at about 8.8 because both
anchor examples belong to the reference channels: the hook numbers are Veritasium's (1 in 1,000,
99 %, 9 %) and the payoff is 3Blue1Brown's Gigerenzer replay. So this round restructures the hook
numbers and the payoff, and rebuilds the Cardiff beat around the shrink it was missing.

### Plan of the climb (written before editing; guide §12)

| Dim | BAR "9" anchor | Where round 2 fell short | Upgrade |
|---|---|---|---|
| Hook 8.5 | commit to a likely-wrong prediction by 0:12 | "Pick a number" at 0:16, after the "most doctors got it wrong" spoiler and the 21 % waffle; numbers are the Bayesian Trap's | Question, then "Pick a number" at about 0:12 with a 1.6 s hold; the doctors' waffle only after the hold. Fresh premise: 1 in 500, same 99 % / 1 % test (title kept), answer 17 % (20 of 120) |
| Clarity 8.5 | re-derive after one watch; assumptions stated; sources correct | Cardiff asserted the base rate over a stale 9 % meter, never mentioned the poor photos; the strip's "10" became "10 people" in 10 × 0.99 | Cardiff shows the base rate as data (170,000 people vs about 1,200 watch-list photos, Davies et al. 2018) and collapses the scanned crowd into the alerts; meter resets with the title; police's poor-photo explanation on screen; 20 → 19.8 → 20 × 0.99 built from the table's people column |
| Visual 8.5 | one focal point; nothing to remove | dead 2:38–2:45 frame; waffle inside the plot area; landing counts stacked in the wedge; 18 words in the cold open | payoff chart deleted; waffle callback at 2× beside the strip; landing shifted down 0.6 with counts outside the flows; merged labels, shorter citation |
| Motion 8.5 | every motion encodes a relation | 99 % copy collisions; strip→raster dissolve without correspondence; "nearly everyone" pointed at a table row | copy flies on a raised Bézier path, "naive" written after it lands; each lit crowd square becomes one ≈17-alert block of the raster; the dimmed grid itself pulses on "nearly everyone" |
| Audio 8.5 | deictics land; pauses intentional | insight sentence at bookkeeping pace | both insight sentences at speed 0.80 with a 0.6 s pause |
| Concision 8 | cutting any sentence loses something | 9 % said twice; mammography problem re-read; "most common answer" line; "Those counts came from this table" | all cut; Gigerenzer becomes one sentence over the cold-open waffle (21 → 87 green); target runtime ≤ 3:30 |
| Originality 7–8 | an angle viewers would remember | both anchors borrowed | fresh numbers; 3b1b payoff gone; Cardiff crowd-to-alerts collapse with real watch-list size; closing chiasmus labels the two numbers "recall" and "precision" |

### What changed

**Structure (substance fixes 1 and 2; craft fix 3)**
- New premise: 1 in 500 sick, the same 99 % / 1 % test (the title's promise), so the answer is
  20 of 120 = 17 % ("six times too high") instead of the Bayesian Trap's 1 in 1,000 → 9 %.
  Every number, the 24 × 5 strip, the formula stages, the sweep and the flows were recomputed
  (`check.py`, facts.md §A).
- The 3Blue1Brown-style payoff is gone: no mammography re-read, no answer chart, no "fewer than
  blind guessing", no "most common answer was 90 %". One sentence over the cold-open waffle
  replaces it: "As for those gynecologists: after one session turning percentages into counts of
  women, the way we just counted people, eighty-seven percent got it right." The waffle comes back
  from its cold-open spot at 2× beside the strip, which pulses on "the way we just counted
  people". Then 66 grey dots turn green (21 → 87). This also fixes the dead 2:38–2:45 frame and
  the waffle sitting inside the plot area (craft 2, 5; substance 8).
- Order is now insight → trained doctors → Cardiff → landing, so the "recall / precision"
  labels in the last line come straight after the precision beat.
- Cut: the second spoken "about nine percent" (the "≈ 17%" now flies in silently, its source
  dimmed to 40 %); "Those counts came from this table". Runtime 3:46 → 3:35, 568 → 530 words.

**Hook (craft 6, substance 3, 11)**
- "…what's the chance you're sick? Pick a number." at 0:12.6, a 2.1 s hold, and only then "Most
  doctors given a problem like this got it wrong" with the waffle. Labels merged to
  "gynecologists / 21% right"; citation shortened to "Gigerenzer et al., 2007 · Psychol. Sci.
  Public Interest".

**Cardiff, rebuilt around the shrink (craft 1, 10; substance 4, 9, 10)**
- On "Swap the disease…" the meter slides right, empties to "?" and is retitled "chance an alert
  is right" in the same move, while the strip gives way to a grey 100 × 100 crowd. No stale 9 %
  frame.
- The base rate is now data, not assertion: "about 170,000 people" (BBC) against "watch lists:
  about 1,200 faces". The second figure is newly sourced from Davies, Innes & Dawson 2018, the
  Cardiff University evaluation, p. 10, and is cited on screen. The mechanism is said before the
  result: "so even a small error rate per face would swamp the real matches."
- The same yellow beam sweeps the crowd. The 145 squares it flags turn yellow (2,470 ÷ 17 per
  square), fly right and become the 145 blocks of the 26 × 95 raster of exactly 2,470 alerts.
  The cleared crowd stays at 30 % as context. This replaces the strip→raster cross-dissolve, and
  the outline is created with the raster, so nothing spills.
- Honest limit, spoken and held on screen about 7 s: "Police also blamed poor-quality photos" (BBC).

**Insight (substance 5, 6, 12; craft 9)**
- One glyph, one quantity: "Before rounding, these are nineteen point eight and ninety-nine
  point eight". The equation's 20 / 100 and the table's results become 19.8 / 99.8. Each is then
  replaced by people × rate, with the 20 and 9,980 flying from the table's people column and
  0.99 / 0.01 from its arrows.
- "Your positive result ruled out everyone who tested negative" and "What's left is a smaller
  sample space" are at speed 0.80, with a 0.6 s pause, and the negatives vanish over the first.
- The "120 people who tested +" label steps aside before the brace labels fly into the fraction,
  so nothing flies through it.

**Motion / visual polish (craft 4, 7, 8; substance 7)**
- The "99%" copy rises off the arrow on a Bézier path above the meter title and drops onto the
  marker, fading in as it leaves (no double-struck glyph). "naive" is written 0.3 s after it
  lands, 0.18 to its left.
- "Nearly everyone": the dimmed crowd of healthy negatives brightens 22 % → 62 % → 22 % with the
  9,980 and the 100.
- Landing is 0.6 lower; rate labels moved toward the nodes. "20" sits outside the red flow and
  "100" outside the blue one at size 44, clear of "you". Grey "recall" beside 99 % and
  "precision" under the meter's 17 % are written on the two closing sentences.
- Meter titles change by fade-out-then-fade-in (no half-second of overlapping titles).

**Kept (both critics' keep lists):** the strip under the meter with its red columns under the
red share and the staged formula; the half-sick check where the rule holds, then the measured
"6× too high"; the landing sweep back onto the naive marker and the closing chiasmus over
people-width flows.

**Facts:** no factual errors were claimed. New claims were checked against primary sources: the
BBC (170,000; 2,470 / 2,297; the poor-quality images quote) and the Davies et al. 2018 PDF
(≈ 1,200 watch-list images; repeat matches). facts.md is rewritten for the new premise and has a
"not claimed" list (no per-face error rate, no count of listed people present).

### Self-check (review kit on the final 1080p master)

Runtime 3:34.6 (was 3:46.5). 154 wpm on speech time, 530 words. −14.1 LUFS / −2.2 dBTP.
Longest silence 2.08 s (the planned "Pick a number" hold). Longest static stretch 3.6 s.
WER 2.1 %, 0 banned phrases, 0 flags, 0 render warnings. Layout audit: 0 issues in 187 checks.

Two passes on the preview and three on the master caught and fixed these:
- the crowd label crossing the left safe edge;
- a 5 s near-empty frame before the crowd appeared (the crowd now arrives with "Swap the disease");
- the 99 % copy double-striking its source (it now leaves fast and fades in);
- "100" reading as "100 you" in the landing;
- the dimmed crowd vanishing into a black square (it now stays at 30 %);
- about 30 words in the final Cardiff frame (crowd labels dimmed, scale note removed after the
  collapse);
- half-second title crossfades;
- the collapsing raster crossing the moving meter and its own braces;
- a "nineteen" sync miss;
- the new toolkit audit's 19 clearance findings: fraction-bar spacing, brace labels, rate labels,
  stacked citations and the crowd beam, all now at least 0.15.

## Round 3 revisions

Reviews: `reviews/round3-craft.md` (8.5) and `reviews/round3-substance.md` (8.5). Neither critic
found a factual error or a cap; both said the structure reaches 9 only narrowly, with Originality
the binding dimension (fix 1 in each review). Every fix from both reviews is applied below.

### Plan of the climb (written before editing; guide §12)

| Dim | BAR "9" anchor | Where round 3 fell short | Upgrade |
|---|---|---|---|
| Hook 9 | ending resolves the opening exactly | the title's "99% accurate" never paid off | landing names accuracy: 9,900 of 10,000 right, but "calls everyone healthy" scores 99.8 % ("More accurate, and useless"), drawn as two grey bars under the meter |
| Clarity 8.5 | re-derive after one watch; sources correct | Cardiff base rate only a text label; 7 % presented as purely base rate and as fact; "recall" never spoken; 12 s algebra sentence | 71 red listed squares in the crowd; "Police counted…"; Davies et al.'s later 46 % (new algorithm, better photos → fewer false alarms per face); recall and precision both spoken; algebra in three sentences |
| Visual 8.5 | one focal point; all §5 standards | grey slab with moiré; tiny dim payoff tags; stale header; 24 words at 2:55; legend 15 px from grid; waffle without a unit | blue crowd on the pixel lattice, never scaled; tags at size 30 in ink; header swapped as negatives vanish; crowd labels and "2,470 alerts" leave once counted; legend with swatches 0.3 from the crowd; "1 dot = 1%" |
| Motion 8.5 | every motion encodes a relation | four transitions crossfaded layers (0:27, 1:23, 2:27, 3:04); in-flight collisions (20 +100, 9,980 double strike, denominator hole); ghost glyphs in naming; meter lag in the sweep | each transition staged (old leaves, then move, then new arrives); routed flights that fade in off their source; one-move rebuilds with in-place denominator swaps; swap() never overprints; one driver updates meter and label from the same N |
| Audio 8.5 | each deictic lands; pauses intentional | four quantities in one 12 s sentence; 0.002 one second late; "this plus sign" not flagged | split into three sentences; 0.002 / 0.998 timed to land on their words; ring and badge pulse on "this plus" |
| Concision 8.5 | cutting any sentence loses something | stakes said the naive answer twice; "Now give each number its name"; third full 20 / 100 sentence | merged stakes line; naming intro cut; shorter flow line |
| Originality 7.5–8 | an image viewers would remember | Cardiff crowd was a grey slab; the paradox itself is the canonical example | the Cardiff crowd now carries its own tiny red base rate, the camera lights 145 squares of which 10 are red, and those 10 become the raster's red columns: the same shrink as the strip, on real data, with an honest second number (46 %) and the accuracy trap |

### What changed

**Facts re-verified (substance fix 2).** I re-read Davies, Innes & Dawson (2018) in full. Their own
logbook analysis gives 3 % true positives at the Champions League final (78 of 2,632 alerts, all watch
lists) and 46 % at the 2018 Six Nations (22 of 48 judged true). They credit the new M20 algorithm and
operator familiarity with the settings, and they note that only high-standard custody photos were used
after the final and that the threshold went from .55 to .59. The video now says "Police counted a
hundred and seventy-three as right" (the force's own figure) and adds the honest limit as a sentence
and a dashed meter marker: "Later, a new algorithm and better photos cut the false alarms, and
forty-six percent of alerts were judged right" ("Six Nations 2018: 46%", Davies citation held).
facts.md §C is rewritten with the quotes, and check.py recomputes 3 %, 46 %, 71 squares and the
accuracy figures.

**Cardiff crowd (craft fixes 1, 10; substance fixes 4, 10).** The crowd is now blue (not on a list),
like the 10,000 people. On "twelve hundred faces" 71 squares turn red (⌈1,200 / 17⌉, an upper bound,
legend "■ watch-listed: ≤ 1,200"). The crowd brightens on "error rate per face" and the 71 pulse on
"swamp". The beam leaves 145 squares lit with yellow rings, 10 of them red. They fly into the raster
keeping their colour, the 10 red ones landing in its first columns, so the 7 % is visible before it
is measured. The raster sits on the pixel lattice (600 px, integer pitch) and is never scaled, which
removes the moiré (the old moiré came from scale pulses on the raster image). The legend has swatches,
sits 0.3 from the crowd and says "= 17 people · illustration". Once the alerts are counted, the crowd
labels and "2,470 alerts" leave, so the precision frame has 9 words of prose.

**Accuracy payoff (substance fix 1).** "Back to your test. The title's ninety-nine percent accuracy is
real. But a test that calls everyone healthy scores ninety-nine point eight: more accurate, and
useless." Two grey bars under the meter ("accuracy" 99 %, "calls everyone healthy" 99.8 %). Grey is
the naive rule's colour, and accuracy is the naive score.

**Transitions staged, never layered (craft fixes 2a–d, 3, 4, 5, 8, 11).**
- Diagram → table: labels, rates and the "you" ring leave first (Uncreate). Then nodes, arrows and the
  + travel, with no text in motion (the + on an arc above everything). Then row labels and rates
  appear beside the parts that have landed.
- Shrink: the header swaps (fade out, then in) to "120 people who tested +" as the negatives vanish,
  and the rings fade with them. The 120 line up in the empty lower half, the meter slides left along
  an empty row to sit on them (crossing nothing), the outline closes on "these", and the pair rises.
- To Cardiff: the waffle, strip and braces clear, then the meter empties and is retitled in place,
  then it slides right while the crowd fades in behind it.
- Back to the test: the meter empties and is retitled "chance you're sick" in place (no 7 % → 17 %
  tween), slides back, and grows 17 % from zero. Rate labels fade in, not Write.

**Formula motion (craft fixes 5, 7, 8; substance fixes 5, 7).**
- Every glyph change is an odometer swap: the old glyph rolls up and out, the new one rolls up in, so
  there is never a cross-fade ghost.
- Copies start invisible beside their source and fade in along routed paths. The 100 comes round the
  right of the fraction and slides in from the right, never over the "+". The 20 and 0.99 leave the
  table through the gap between its rows and the gap beside the strip. The 9,980 drops between the
  numerator and the tail and rises into its slot. The 17 % goes down the left edge and across the open
  band.
- 19.8 → 20 × 0.99 is one move: the old 19.8s stay until their replacements arrive, the denominator
  repeats the numerator's term in place, and the bar stretches once. No hole.
- 0.002 lands on "two in a thousand" and 0.998 on "nine hundred ninety-eight". In-formula pulses are
  at most 1.12× so nothing grows into its neighbour. The 9,980 keeps the denominator's baseline.

**Sweep (craft fix 9; substance fix 3).** One driver sets the meter from the same rounded N that the
"1 in N" label shows, before anything that reads it is drawn. Frames now agree, e.g. "1 in 59 · 63%",
"1 in 333 · 23%". The return to 1 in 500 takes 2.5 s with smooth easing. The ring and badge
scale-pulse (1.15×, 0.6 s) on "this plus".

**Narration (craft fixes 4, 6, 12; substance fix 11).**
- The algebra sentence is three sentences.
- Stakes merged into "The tempting answer is the test's own hit rate, ninety-nine percent: you'd
  start treatment today."
- "Now give each number its name" is cut.
- The flow line is "On a random screen, twenty reach this plus along the red, a hundred along the
  blue."
- The ending names both terms: "Ninety-nine percent is the test's recall: how often the sick test
  positive. Seventeen percent is its precision: how often the positive are sick." Each tag ("recall",
  "precision") is written on its word in ink at size 30.

**Small:** "1 dot = 1%" under both waffles (substance fix 8). The P(sick∣+) left-hand side arrives
while the meter title pulses, with no double-struck copy over the title. The 46 % marker is drawn in
ink so it reads over the bar.

**Kept (both keep lists):** the 120-dot strip hanging under the meter with its red columns under
the 17 % segment, and the formula built braces → table → ÷ 10,000 → names; the half-sick check, then
the measured "6× too high"; the landing diagram with people-width flows, the sweep onto the naive
marker, and the 99 % / 17 % chiasmus; the Cardiff beam → 2,470-cell raster → 7 % bar.

### Self-check (review kit on the final 1080p master)

- Runtime 3:49.8 (was 3:34.6), because of the accuracy payoff and the Six Nations limit. 153 wpm on
  speech time, 544 words spoken.
- −14.0 LUFS / −1.7 dBTP. Longest silence 2.08 s (the planned "Pick a number" hold). Longest static
  stretch 3.3 s.
- WER 2.0 %, 0 banned phrases, 0 flags, 0 render warnings. Layout audit: 0 issues in 210 checks.
- I checked frames every 0.25 s through every staged transition and every flight: 0:25–0:28,
  1:16–1:27, 1:26–1:34, 1:38–1:46, 2:22–2:27, 2:43–2:48, 3:05–3:08.

These passes caught and fixed:
- the title's copy double-striking as it became P(sick∣+);
- formula pulses growing into their neighbours (now ≤ 1.12×);
- the numerator reading "20 19.8" mid-swap;
- the 9,980 copy grazing the tail;
- the 0.01 copy cut by the fraction bar;
- flying alert squares crossing the legend text;
- a 1.5 s near-empty frame before the crowd appeared;
- a play-level rate function that kept the old header visible during the rise;
- the 46 % marker vanishing into the bar;
- a 3.8 s static stretch in the crowd beat (the legend now arrives on "Cardiff").

Honest estimate: Hook 9, Clarity 9, Visual 9, Motion 9, Audio 9, Concision 8.5, Originality 8.5–9
→ about 8.9–9.0. The remaining risk is length: 3:50, and the landing now carries three ideas
(accuracy, prevalence, recall/precision).

## Round 4 revisions

Reviews: `reviews/round4-craft.md` (8.6) and `reviews/round4-substance.md` (8.5). Neither critic found a
factual error or a cap. Craft says all fixes reach about 9.0. Substance says polish alone reaches 8.9 and
that 9 needs a more original act 2, because the spine (a medical test plus the Gigerenzer gynecologists) is
the same as 3Blue1Brown's *The medical test paradox*. So this round restructures as well as polishing.

### Climb plan (written before editing)

| Dimension (low score) | BAR "9" anchor | Where it falls short | Upgrade |
|---|---|---|---|
| Originality 8 / 8.5 | a non-obvious angle or image viewers would remember | the cold-open baseline and the training payoff are 3b1b's Gigerenzer example; Cardiff reads as an epilogue | replace Gigerenzer with Manrai et al. 2014 (JAMA Intern Med: 14 of 61 right, most common answer 95 %, the test's own accuracy), which ties the cold open to the landing's accuracy line; cut the training payoff; act 2 now applies the viewer's move ("Shrink to the alerts, and take the red share"), the 10 flagged watch-listed squares are pulsed in the crowd before they fly, and the crowd leaves as the sample space shrinks |
| Clarity 8.5 | could re-derive after one watch; all numbers like-for-like | 8 equation states in 32 s; ÷10,000 is the rewind; 7 % vs 46 % compares two measures; 99 % vs 99.8 % bars look the same | 4 formula changes, at least 5 s apart (20 → 20 × 0.99, 100 → 9,980 × 0.01, shares, names); ÷10,000 happens first in the table's people column, then flies in; evaluators' 3 % tick beside their 46 %; the useless test drains both arrows to 0 % so "useless" has a picture |
| Visual 8.5 | one focal point per frame | dead dim crowd slab 2:50–3:06; meter parks top-left; closing tags same weight as neighbours | crowd fades out once the alerts land and the precision picture re-centres; crowd fades in at its final place while the meter makes one move; tags size 34 with underlines |
| Motion 8.5 | every motion encodes a relation | mangled "+" morph and a one-frame crowd pop at 3:06; beam still sweeping while squares fly; rings lost in flight | outline → disk, raster shrinks into the + and the cross fades in after; beam ends, 0.5 s hold, red pulse, then the flight with rings kept |
| Audio 8.5 | deictics land, pauses intentional | sweep leaves "1 in 100" while it is spoken; no air after the thesis | narration reordered to "at one in a hundred, fifty percent; at one in two, ninety-nine" so each number has its own frame; 0.8 s pause after the thesis with the outline pulsing |
| Concision 8 / 8.5 | cutting any sentence loses something | third 20 / 100 statement; "Before rounding…"; 11 s gynecologist callback | flow line cut (labels arrive silently); unrounding folded into the people-times-rate sentences; training beat cut |

### What changed

**Facts.** No factual error was claimed. Both critics flagged the 7 % vs 46 % comparison as mixing two
measures; that is fixed on screen and in narration (below). New source verified in full text: Manrai
et al. 2014, *JAMA Intern Med* 174(6):991–993 (61 doctors and students at a Boston-area hospital; 14
right; most common answer 95 %, 27 of 61). facts.md §B is rewritten for it, check.py recomputes the
per-100 waffle (23 / 44 / 33) and the "95 % = that test's accuracy" claim, and the Gigerenzer training
result is no longer claimed anywhere. The Met Police "one error in 1,000 faces" vs Essex 8-of-42 story
was checked and recorded in facts.md §D but not used (it would mix two forces in one act).

**Originality / hook (substance fix 7, structure).**
- Cold-open baseline: "Most doctors and medical students given a problem like this got it wrong" over a
  waffle of Manrai's respondents (23 % right). The stakes line now uses their real most common answer:
  "Their most common answer was the test's own accuracy, here ninety-nine percent: you'd start
  treatment today." The 44 grey dots that said 95 % light up, labelled "44% said 95%", before the 99 %
  flies to the naive marker. The landing's "The title's ninety-nine percent accuracy is real" now
  answers that exactly.
- The gynecologist training beat (11 s) is cut: Bayes → thesis → 0.8 s pause → police watch list, with
  the meter retitling as the act-2 question.
- Act 2 applies the move: "Shrink to the alerts, and take the red share." The crowd fades out on
  "shrink" and the meter + alert raster take the centre, so the precision picture is one focal point
  (craft fix 2).

**Derivation (substance fixes 1, 6, 9).** Four formula changes, each ≥ 5 s apart:
"Unrounded, the red count is twenty sick people times ninety-nine percent" (20 → 20 × 0.99 from the
people column and the red arrow; the table's 20 positives become 19.8) · "The blue count is nine
thousand nine hundred eighty healthy people times one percent" (100 → 9,980 × 0.01; table 100 → 99.8)
· ÷ 10,000 gets its own picture: the people column's header becomes "÷ 10,000" (rest of the table
dims), 20 → 0.002 and 9,980 → 0.998 in place on their spoken words, then on "The share can't change"
the layout opens and the shares fly in · one naming change on "Bayes' theorem" after pulses on "how
common" and "how often". "Before rounding…", "That's twenty sick people…" and "That's seventeen
percent" are gone ("Seventeen percent."). The 9,980 and 0.998 copies go round the right of the tail and
rise into their slots, so no copy crosses the bar; old terms leave only as new ones arrive.
The named form has 0.3 between bar and terms and the boxes pad 0.12, so both boxes clear the bar by
≥ 0.18 (substance fix 8); "Bayes' theorem" sits ≥ 0.22 under the yellow box.

**Thesis pause (craft fix 5).** "[pause 0.8]" after "…then take the share."; the strip's yellow outline
pulses once in it.

**Cardiff (craft fixes 3, 7; substance fix 3; craft fix 6).**
- On "Swap the disease…" the old picture clears while the meter empties and is retitled in place, then
  the meter makes one move to the top right and the crowd fades in at its final place as the meter
  clears it (no parking top-left, no empty frame on "police watch list").
- The beam finishes, a beat later the 10 flagged watch-listed squares pulse (2.2×, red, rings on), then
  all 145 fly with their yellow rings kept until they land. Flagged squares are 5 px with 10 px rings.
- Like-for-like: "The university's evaluators counted three percent here. After a new algorithm and
  better photos cut the false alarms, they counted forty-six at the Six Nations." Two dashed ink ticks:
  "evaluators: 3%" (label left of its tick) and "Six Nations 2018: 46%" (right of its tick); the title
  lifts to make room. The 7 % fill stays the force's count and is attributed to police in narration.

**Landing (craft fixes 1, 4, 8; substance fixes 2, 4, 5).**
- The alerts collapse into the +: the raster's outline becomes a circle outline (two closed curves),
  the raster shrinks into it, then the circle fills and the cross fades in. No glyph is interpolated,
  and the crowd is already gone (no pop).
- "Calls everyone healthy": both flows drain, their rates read 0 % and the + dims (nothing reaches it),
  as the 99.8 % bar fills; the red 0 % pulses on "useless". They refill as the next beat starts.
- Sweep re-timed with the narration reordered: "at one in a hundred, fifty percent; at one in two,
  ninety-nine". The label reaches 1 in 100 on "one in a hundred", holds through "fifty percent", and
  reaches 1 in 2 on "ninety-nine".
- The flow line ("On a random screen, twenty reach this plus…") is cut; "20" / "100" fade in outside
  their flows during the silent return to 1 in 500.
- Closing tags "recall" / "precision" are size 34 and each is underlined as it is written.
