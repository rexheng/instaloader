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

## Round 1 revisions (review cycle 2)

Reviews: `reviews/round1-craft.md` (8.4) and `reviews/round1-substance.md` (8.4). No caps and no factual
errors claimed. Both say every fix together reaches about 9.0, narrowly, with no structural rebuild.

### Climb plan (written before editing)

| Dimension (score) | BAR "9" anchor | Where it falls short | Upgrade |
|---|---|---|---|
| Visual 8 / 8.5 | one focal point per frame; nothing to remove | fail beat weights the 20 sick (big rings) over the 100 false alarms (6 px); bird-shaped brace; 3 precision figures on one bar; dim crowd, empty right half; 6x brace reads as measuring nothing | every positive gets the same yellow ring and the same 3x size (100 blue visibly outnumber 20 red); straight brackets everywhere (6x bracket runs 17 % -> 99 %); police 7 % alone on the main bar, evaluators on their own bar; brighter, larger crowd with legend under the meter on the right |
| Clarity 8.5 | re-derive after one watch; numbers like-for-like | "44% said 95%" next to a 99 % test; 3 % vs 7 % unexplained; "forty-six" without unit; no 5,000 / 120 on screen | narration names the doctors' test as 95 % accurate and morphs 95 % into our 99 %; evaluators counted only logbook-confirmed alerts (Davies et al. 2018, Champions League Final section: "Operator logs were then used…", re-read); "forty-six percent"; column sums 5,000 and 120 |
| Concision 8 | cutting any sentence loses something | /10,000 sub-beat 14 s; landing with three moves | /10,000 in about 9 s, table and formula change together on each number; accuracy paradox cut (it is episode 44's whole topic) |
| Motion 8.5 | every motion encodes a relation | cold-open diagram falls apart before the table forms; near-empty frame on "police watch list" | one 1.5 s morph (node+label -> row, arrow + rate -> row arrow, + -> header); the 120-dot strip spreads into the Cardiff crowd while the meter retitles |
| Hook 8.5 | commit by 0:12; ending resolves the opening | question ends 0:13.4 | cold open at speed 0.88, no pause before "Pick a number"; a "your guess" marker slides along the empty meter during the hold |
| Audio 8.5 | deictics land | "watch list" had nothing to land on | red "on a watch list" legend lands on the words |
| Originality 8 / 8.5 | an image viewers would remember | Cardiff base rate never shown | "≤ 1 in 140" under the watch-list legend; evaluators' bar visibly sheds false alarms 3 % -> 46 % |

### What changed

**Facts (no error was claimed; one proposed wording was checked and not used).**
- I re-read Davies, Innes & Dawson (2018). Their 3 % comes from "Operator logs … used to clarify whether
  or not these matches were accurate … 3% (N=78) were 'true positives' (confirmed by the operators)",
  across 2,632 alerts that include the police-officer test list, with many decisions never logged.
  So the narration now gives the real reason their count is below the force's 7 %: "Cardiff
  University's evaluators counted only alerts the logbooks confirmed: three percent." The substance
  critic's suggested "checking every alert themselves" does not describe their method, so it is not
  used (facts.md §C records the quote).
- Six Nations 2018: 22 of 48 judged true (46 %), 22 false, 4 missing; "Months later, a new algorithm,
  better photos and practised operators thinned out the false alarms, and their count rose to
  forty-six percent." Davies et al. credit the new algorithm and operator familiarity with the
  settings, and after the final only high-standard custody photos were enrolled.
- "≤ 1 in 140" = 1,200 / 170,000 = 1 in 141.7, an upper bound. It is *more* common than the hook's
  1 in 500 (the critic's aside that the targets are rarer is not right), so no comparison is drawn.
- The accuracy paradox (99.8 % for a test that calls everyone healthy) is cut: it is the whole topic of
  episode 44 ("99.8% Accurate and Completely Useless"), and both critics wanted a one-move landing.
  check.py and facts.md are updated (99 ÷ 17 = 5.82, sums 5,000 and 120, 7 px crowd cells).

**Fail beat (craft 1, 10; substance 5).** Every person who tests positive is now a vector square: the
20 sick grow 3× on "twenty sick" (no ring); as the beam passes, every positive gets the same yellow
ring and the 100 healthy positives grow 3×, so 100 ringed blue squares visibly outnumber 20 ringed red
ones. On "one percent" only those 100 pulse; on "nearly everyone" the 9,980. A grey rule and "5,000"
appear under the positives column on "five thousand", and "120" on "a hundred and twenty". The 6×
brace is now a grey bracket from the meter's 17 % fill edge to the naive 99 % marker, labelled
"99 ÷ 17 ≈ 6×".

**Brackets (craft 2).** All four braces (strip "20"/"100", Cardiff "173 right"/"2,297 wrong") are
straight brackets: a rule with two 0.12 end ticks, stroke 4, drawn with Create.

**Evaluators on their own bar (craft 3; substance 1).** The main bar keeps only the police 7 %
("police count" to its right). A thin red/blue "university evaluators" bar below fills to 3 % ("2017
final"), the tag becomes "Six Nations 2018" on "Months later", and from "photos" to "alarms" its blue
share shrinks while red grows to 46 % (smooth, ≈ 2.5 s). "forty-six percent" is spoken with its unit.

**Stakes (craft 4; substance 6).** "Their most common answer was their test's own accuracy:
ninety-five percent. For our test, that's ninety-nine: you'd start treatment today." A grey "their test:
95% accurate" sits under "44% said 95%" for ≈ 4 s, and on "ninety-nine" a copy of the "95%" turns into
"99%" in the first 40 % of its trip, then travels round the right end of the meter onto the naive marker.

**÷ 10,000 (craft 5; substance 3).** "Divide everything by the ten thousand. Counts become shares: two
in a thousand sick, nine hundred ninety-eight healthy. The share can't change." (9.4 s, was 13.9 s; the
third "nine thousand nine hundred eighty" is gone). The table and the formula change together on each
spoken number (20 → 0.002 in the people column and both 20s in the formula in one move, then 9,980 →
0.998).

**Into Cardiff (craft 6, 7; substance 7, 8).** One staged move on "Swap the disease for a police watch
list": the algebra clears and the meter empties and retitles in place, then the meter goes to the top
right while the strip's 120 people spread out into the crowd (the 20 sick become 20 of the listed
faces) and the crowd fades in around them; the red legend "■ on a watch list" lands on "watch list".
The crowd is larger (700 px, 7 px cells with 5 px squares) at 80 % opacity, the listed squares are
11 px, and every flagged square grows to 11 px with a yellow ring as the beam passes. The legend moved
under the meter on the right and now reads "on a watch list / ≤ 1,200 faces · ≤ 1 in 140 / = 17
people · illustration"; "≤ 1 in 140" pulses on "error rate per face". A grey dateline "Cardiff · 3 June
2017" sits over "≈ 170,000 people" from "Champions League final". The two citations share one line so
nothing crowds the crowd.

**Diagram → table (craft 8).** One 1.5 s morph: each node + label becomes its row's bullet + label
(labels arc over their nodes, which they pass), each arrow becomes its row arrow with its rate riding
along (the 1 % now sits under its arrow in the table, as in the diagram), the + travels in a straight
line just ahead of the arrow tips into the positives' header, and the meter steps down out of the way.
Only "1 in 500", "you" and the ring fade, as they have no row.

**Hook (substance 4).** No pause before "Pick a number", "of the sick", cold open at speed 0.88: the
question ends at 0:11.7 (was 0:12.6). A hollow grey "your guess" marker slides once along the empty
meter during the 1.6 s hold.

**Landing (craft 9; substance 2, 9).** "Back to your test" (the alerts collapse into the + while the
diagram re-forms around it and the meter slides back, in one overlapping move) → the 17 % grows back on
"seventeen percent" → the prevalence sweep → the chiasmus. "recall" is written as the red flow pulses;
the two-tag frame is complete from "precision" and holds ≈ 3.5 s to the end card. The landing runs
≈ 30 s (was 39 s) with two moves and ends on one line.

**Kept (all three keep items from both reviews):** the persistent meter docked on the 24 × 5 strip with
its 17 % red segment over the 4 red columns, and again over the 2,470-cell raster at 7 %; the
derivation built from the picture (brackets → 20 / (20 + 100), table → 20 × 0.99 and 9,980 × 0.01,
Bayes form with the yellow and red boxes); the half-sick control case; the raster collapsing into the +;
the landing sweep with one updater, "1 in 100 · 50%" held while spoken and the naive marker at 1 in 2.

### Self-check (review kit on the final 1080p master)

- Runtime 3:36.2 (was 3:42.9). 152 wpm on speech time; 516 words by the review kit's count (was 536).
- −14.1 LUFS / −2.3 dBTP. Leading silence 0.0 s, trailing 1.86 s, longest internal silence 2.16 s
  (the planned "Pick a number" hold). Longest static stretch 3.3 s (2:51.0, under the evaluators' line).
- WER 2.2 % (only "a hundred" heard as "one hundred", "logbooks"/"log books", "practised"/"practiced").
  0 banned phrases, 0 flags, 0 render warnings. Layout audit: 0 issues in 205 checks.
- I looked at all 12 contact sheets, the keyframes at 0:21, 1:12, 2:29, 2:55, and frames every
  0.14–0.2 s through every changed transition: the 95 → 99 trip (0:25.9–0:27.3), the diagram → table
  morph (0:29.4–0:31.1), the grid's arrival, the fail-beat beam, the meter's two-axis move (1:25.6–1:27),
  the ÷ 10,000 swaps (1:52–1:55), the strip → crowd move (2:12.3–2:14.5), the evaluators' bar
  (2:48–3:04) and the landing rebuild (3:05.9–3:08.3).
- These passes caught and fixed: the "+" and "1 %" crossing the meter title mid-morph (the + now travels
  just ahead of the arrow tips; the meter steps lower, earlier); the ring lingering as a loose circle
  (fades early); the travelling glyph still reading "95%" (the 95 → 99 change now finishes in the first
  40 % of the trip); black holes in the crowd where the later listed faces would be; the rightmost
  column of positives not finishing its growth (the beam's tracker now runs 3 % past the edge); the
  "Six Nations 2018" tag running into "university evaluators" (tags now sit right of their bars); a
  4.3 s static stretch in the evaluators' line (the bar now moves from "photos" to "alarms"); a
  near-empty frame on "Back to your test" (the diagram now re-forms while the alerts collapse); three
  clearance warnings (grid header vs a top-row ring, citation vs crowd bottom and beam).

Honest estimate against BAR §3: Hook 9, Clarity 9, Visual 9, Motion 9, Audio 9, Concision 9,
Originality 8.5 → weighted 8.95, i.e. 8.9–9.0. The binding risk remains Originality: the core example is the
canonical one, and the Cardiff act (crowd → alerts raster → police vs evaluators bars) carries the
episode's own image.

## Round 5 revisions

Reviews: `reviews/round5-craft.md` and `reviews/round5-substance.md` (8.4 / 8.4). They are the same texts as
`reviews/round1-*.md` (review cycle 2): no caps and no factual errors claimed, and every fix in them was
already applied in "Round 1 revisions (review cycle 2)" above (final.mp4 3:36.2, rendered after the reviews).
So this round re-checks that each fix landed, audits the current cut frame by frame as a fresh critic would
(sheets, keyframes and 2–10 fps sweeps through every transition), and climbs on what is left. Facts were
re-checked against facts.md; nothing was claimed wrong, so nothing changes there except the record of the
new landing numbers.

### Climb plan (written before editing)

| Dimension (cycle-2 score) | BAR "9" anchor | Where the current cut still falls short | Upgrade |
|---|---|---|---|
| Hook 8.5 / Originality 8–8.5 | "the ending resolves the opening exactly"; "a non-obvious image viewers would remember" | the landing rebuilds the cold-open diagram with thin arrows, and the people-width flows only appear 4 s later, on "Symptoms"; the counts 20 / 100 appear only after the sweep, in silence | the first frame is re-seen at once: on "Back to your test" the two arrows swell into people-width flows (a thin red flow of 20, a fat blue flow of 100) in the pause, so the 1 % arrow is visibly the one that fills the +; the counts stay live through the prevalence sweep (99 / 99 at 1 in 100; 4,950 / 50 at 1 in 2, the half-sick table of the naive build) |
| Visual 8 / 8.5 | "all §5 standards met; nothing to remove" | "≈" and "≤" in the Cardiff header and legend fall back to a heavier sans font (CMU Serif has no glyph for them: checked with fontTools) | typeset both with LaTeX (MathTex at the matching cap height) |
| Motion 8.5 | "every motion encodes a relation"; no near-empty frame | on "Back to your test" everything fades in the first 30 % and the diagram only starts at 35 %, so ≈ 0.5 s shows a lone meter and a ring (3:06.5); the end card cross-fades over the closing frame, so "Ω Sample Space" prints over "chance you're sick" for ≈ 0.4 s | the diagram starts re-forming while the Cardiff picture is still leaving (overlapping windows); the closing frame fades out before the card fades in |
| Audio 8.5 | pauses intentional | the 1.0 s pause after "Back to your test" carries no new picture | the pause (1.6 s) is where the arrows become people-width flows |
| Clarity 8.5 | numbers like-for-like, re-derivable | the landing's 20 / 100 have no unit | a small grey "per 10,000 people" under "you" when the counts appear |

### What changed

**Facts.** No error was claimed and none was found. Re-checked: BBC News (4 May 2018), the Guardian
(5 May 2018) and WalesOnline all give 2,470 potential matches and 2,297 incorrect (173 right, 7 %); the
Manrai, Davies et al. and Six Nations rows in facts.md stand as written. New on screen are the landing's
live counts per 10,000 people: 10,000/N × 0.99 and (10,000 − 10,000/N) × 0.01, i.e. 20 / 100 at 1 in 500,
99 / 99 at 1 in 100 (50 %) and 4,950 / 50 at 1 in 2 (99 %). They are recomputed in check.py (last block)
and recorded in facts.md §A.

**Landing: the first frame, re-seen (Hook, Originality, Audio).** "Back to your test" now gets a 1.6 s
pause that carries the picture. The alerts still collapse into the + (kept), the cold-open diagram
re-forms, and in the pause both arrows swell into flows as wide as the people they carry. The thin 99 %
flow is labelled "20" and the fat 1 % flow "100", with a grey "per 10,000 people" in the wedge between
them. So the frame the viewer committed on is shown again, and now the 1 % arrow is visibly the one that
fills the +. The 17 % fills on "seventeen percent" as before. On "Symptoms" the naive 99 % marker returns
as the target of the climb. One updater then drives the label, both flows, both counts and the meter:
"1 in 100 · 99 / 99 · 50 %" on its words, then "1 in 2 · 4,950 / 50 · 99 %" on "ninety-nine", which are
the numbers of the half-sick table where the rule held. The return to 1 in 500 runs in the pause, and the
recall / precision chiasmus is unchanged. (The counts used to appear only after the sweep, in silence.)

**No empty frame on "Back to your test" (Motion).** The diagram now cross-fades in (8–60 % of the move)
while the Cardiff picture fades out (0–42 %), and the meter's ride starts at 20 % instead of 35 %. At
3:06.6 the frame shows the nodes, labels, ring and meter; before, it showed a lone meter and ring.

**End card (Visual).** The closing frame fades out (0.3 s) before the card fades in (0.3 s), so
"Ω Sample Space" no longer prints over "chance you're sick". The finished two-tag frame holds about 2.5 s.

**Glyphs (Visual).** "≈ 170,000 people" and "≤ 1,200 faces · ≤ 1 in 140" are typeset in LaTeX at the
matching cap height (MathTex 38 / 36 ≈ Text 28 / 26). CMU Serif has no ≈ or ≤ (checked with fontTools),
so Pango had drawn them in a heavier sans fallback. {\le} is set as an ordinary symbol, so both bounds get
the same spacing.

**Kept:** all three keep items from both reviews, namely the meter docked on the 24 × 5 strip and on the
2,470-cell raster, the derivation built from the picture, the half-sick control, the raster collapsing into
the +, and the landing sweep (one updater, "1 in 100 · 50 %" held while spoken, naive marker at 1 in 2).

### Self-check (review kit on the final 1080p master)

- render.sh: 0 warnings, layout audit 0 issues in 207 checks. The preview pass had caught two problems,
  both now fixed: the naive marker was built while the meter still had its Cardiff geometry (so it sat
  mid-bar), and "per 10,000 people" was 0.11 from the widest red flow. Clearance from both flows at every
  prevalence is now ≥ 0.23, by computed geometry.
- Runtime 3:36.9. 152 wpm on speech time, 515 words. −14.1 LUFS / −2.3 dBTP. Leading silence 0.0 s,
  trailing 1.93 s. Longest internal silences: 2.16 s (the planned "Pick a number" hold) and 2.1 s (the new
  "Back to your test" pause). Longest static stretch 3.3 s (2:51); the closing two-tag frame holds 3.1 s.
  0 banned phrases, 0 flags.
- WER 2.2 %. In the full-file transcript "Police" is heard as "This" (2:40) and "Your" as "Or" (3:09), both
  at segment starts. Re-transcribing just those stretches with the same model gives "Police counted 173
  as right, 7%" and "Your 17% assumes a random screen", so these are segmentation misses, not
  pronunciation.
- Looked at all 12 contact sheets and keyframes kf_28 (legend glyphs), kf_36 (the re-seen first frame),
  kf_38 (1 in 2 · 4,950 / 50 · 99 %) and kf_39 (back at 1 in 500). Also stepped through frames at 4–5 fps
  over 3:05.9–3:09.5 (collapse, cross-fade, arrows swelling into flows) and 3:33.8–3:36.9 (fade out, then
  card), plus a 2 fps sweep of the whole landing in the preview. Nothing overlaps and no frame is empty.

Honest estimate against BAR §3: Hook 9, Clarity 9, Visual 9, Motion 9, Audio 9, Concision 9,
Originality 8.5–9, so weighted 8.95–9.0. Originality is still the binding dimension, because the core
example is the canonical one. The episode's own images now sit at both ends of act 2 and at the close:
the strip under the meter, the Cardiff crowd collapsing into the raster, and the people-width flows that
re-read frame one.

## Round 6 revisions

Reviews: `reviews/round6-craft.md` (8.5, reaches 9 "only just") and `reviews/round6-substance.md`
(8.5, "reaches 9 if fixed: no" — Originality held at 8 by the canonical spine; it names a Cardiff cold
open, or, as the cheaper route, making the half-sick → rare transition one continuous prevalence slide
with the meter falling live). No caps, no factual errors; one source conflict (4-day alert count shown as
one match-day crowd) and two nits (images vs faces; the 46 % is the operators' initial judgment).

### Climb plan (written before editing)

Structure. The substance critic says polish cannot reach 9, so the fail beat is restructured rather than
polished. A Cardiff cold open was considered and rejected: the title promises a medical test, both critics'
keep items hang on the cold-open diagram being re-seen at the landing, and the Cardiff case has no premise
a viewer could compute from (its precision also depends on who counts). The restructure keeps every keep
item and replaces the recolour with the episode's own image: **the same test, a prevalence slider and a
meter that falls live**. The half-sick case is drawn as a block (the left 50 columns), so the beam lights
almost all of the left half and a sprinkle of the right; then "Now make the disease rarer, down to yours"
drains the block from its right edge while the table's prevalence label ("1 in 2", carried in from the cold
open's "1 in 500") ticks to 1 in 500, the counts tick as expected counts, and the meter slides from 99 % to
17 % away from the naive marker. The failure is measured as it happens; the counting then names the cause.

| Dimension (craft / substance) | BAR "9" anchor | Where the cut falls short | Upgrade |
|---|---|---|---|
| Originality 8 / 8 | "a non-obvious angle or image viewers would remember" | canonical example; the fresh parts are secondary | the live prevalence slide (above); the two meters share one word: "precision" morphs from the alert meter's title and a ghost of the disease meter's 17 % appears tagged "precision too"; the 3 % → 46 % rise is tied to the blue term of Bayes' denominator ("P(+ ∣ not listed) ↓") |
| Clarity 8.5 / 8.5 | "viewer could re-derive it after one watch; all numbers check; sources correct" | numbers → symbols by cross-fade, no mapping; "these/these" point at nothing; stale positives under "÷ 10,000"; 4-day count shown as one day | per-term transforms 0.002 → P(sick) etc. with "≈ 17 %" kept; grey braces "how common" / "how often" grow on the spoken words and stretch with their terms; the positives column is divided too; "Over four days", "final week" everywhere, Davies table row in facts.md |
| Visual 8.5 / 8.5 | "every frame has one focal point; all §5 standards met" | moiré half-sick grid; overlapping 3× squares; ~22 words in the Cardiff frame; dead band; olive badge; small "your guess"; mixed bar-label grammar | block layout; every positive ≥ 5 cells from every other; ghosted meter title, dateline fades, 2-line legend docked 0.5 under the meter; badge never dimmed; "your guess" Text 26; both bars tagged the same way (who / which alerts, on the right) |
| Motion 8.5 / 9 | "every motion encodes a relation" | cross-fade into Bayes; lumpy outline → disk; 145 squares arrive as a jumble | per-term morphs (lag 0.3, numerator first); outline → disk as one rounded rectangle whose corners grow into a circle, ring after landing; the 145 file into their blocks in order, red first |
| Audio 8.5 / 8.5 | "each deictic lands as the element highlights" | the two "these"; "nine thousand nine hundred eighty" spoken twice; soft onsets at "Police" / "Your" | braces on the words; "every healthy person"; 80 ms pre-roll on those two beats |
| Concision 8.5 / 8.5 | "cutting any sentence loses something" | 22 s of mechanical substitution | the two "unrounded" sentences merge into one move |
| Hook 8.5 / 8.5 | "ending resolves the opening exactly" | the close never says the title's word back | "The title's ninety-nine percent is the test's recall" |

### What changed

**Facts (substance fix 1 and both nits; all accepted after re-reading the sources on 2026-10-22).**
Davies et al.'s deployment table reads "Champions League (4 days) | extremely large | 2632 | 78 (3%)", and
Wired UK (4 May 2018) puts the 2,470 alerts in "Champions League Final week"; only the BBC says "on the day
of the final". The narration now says "Over four days, they raised two thousand four hundred and seventy
alerts", the dateline reads "Cardiff · Champions League final week, 2017" (and fades once read), and the
evaluators' tag reads "final week · 2,632 alerts". "Twelve hundred faces" became "twelve hundred photos"
(Davies: "around 1200 images", including the police "friendlies" list) and the 1,200 is no longer written
on screen; only the bound it implies is ("≤ 1 in 140"). The Six Nations 46 % is the operators' logbook
judgment, the same method as the final's 3 %; facts.md now records that intervention teams later found 7
of those 22 false (at most 15 / 48 = 31 %, still ten times 3 %) and the tag shows the small base, "48
alerts". facts.md §A/§C, script.md sources and check.py (last block) carry the new rows.

**Fail beat, restructured (substance "reaches 9: no"; Originality).** The recolour is gone. The half-sick
case is now a block (the left 50 columns: no moiré; the beam lights almost all of the left half and a
sprinkle of the right). The cold open's "1 in 500" rides into the table's header in the diagram → table
morph and rolls to "1 in 2" on "half". Then one slider, on "Now keep the same test, and make the disease
rarer and rarer, down to yours: one in five hundred": the label runs 1 in 2 → 1 in 500 (log-spaced), the
block drains from its right edge (the 50 false-alarm people in it stay lit as they turn blue), the table
ticks as expected counts (1 in 5: 2,000 → 1,980 / 8,000 → 80; 1 in 100: 100 → 99 / 9,900 → 99), and the
meter falls live from 99 % to 17 % away from the naive marker. The failure is measured as it happens;
"About twenty sick people light up, plus one percent of the 9,980 healthy ones: about a hundred" then
names the cause as the 20 and the 100 grow into ringed squares on their own words. Every positive is ≥ 5
cells from every other, so all 120 rings are distinct (craft 7, substance 4). The landing's sweep is now
this slider run backwards.

**Numbers → Bayes (craft 1, 2, 3, 6; substance 6).** The two "unrounded" sentences are one ("the red
count is twenty sick people times ninety-nine percent, and the blue, every healthy person times one
percent"), one layout change with each term arriving on its words; 9,980 is no longer spoken twice. On
"Divide everything" each row of the table divides on its spoken number, positives too (19.8 → 0.00198,
99.8 → 0.00998), so nothing under "÷ 10,000" is stale, the "1 in 500" label leaves, and nothing yellow is
dimmed. Grey braces "how common" (under 0.002 and 0.998) and "how often" (under 0.99 and 0.01) grow on
those words; on "Name them, and you have Bayes' theorem" each number turns into its name in place
(0.002 → P(sick), 0.99 → P(+∣sick), 0.998 → P(healthy), 0.01 → P(+∣healthy); numerator first, lag 0.3),
the braces stretch with their terms, "≈ 17 %" stays on the right, and the labelled form holds until the
braces hand over to the yellow box on "shrink".

**Cardiff (craft 4, 5, 9, 10; substance 2, 3, 9).** The meter waits ghosted at 30 % (title, track, "?")
until "Shrink to the alerts", like the cold open's meter. The legend is two lines docked 0.5 under the
meter ("■ watch list · ≤ 1 in 140", "■ = 17 people · illustration"); about 10 words of prose at most. The
145 flagged squares file into the raster one by one in block order (red first, then left to right, each
move ≥ 0.5 s). On "precision" the alert meter's title turns into the word, a small ghost of the disease
meter (17 %, "your test") appears beside it and the word is copied above it: "precision too". Both bars are
tagged the same way on the right ("police count / 2,470 alerts", "evaluators' count / final week · 2,632
alerts" → "Six Nations 2018 · 48 alerts"). The rise to 46 % is tied to the formula: "…thinned out the false
alarms, the blue term in Bayes' denominator…", with a blue "P(+ ∣ not listed) ↓" appearing under the
shrinking blue segment; the shrink starts on "a new algorithm".

**Landing and hook (craft 8; substance 5, 8).** The raster's outline stays one convex shape (a rounded
rectangle whose sides shrink and corners grow into the badge's circle), the disk grows inside it at full
opacity, the cross arrives once it has landed, and "you" closes round the badge only then. The close is
"The title's ninety-nine percent is the test's recall…", so the last lines re-read the title. "The police
counted…" and "Your seventeen percent…" start with 80 ms of silent pre-roll; the full-file whisper
transcript now hears "The police counted" and "Your 17% assumes". "your guess" is Text 26 and sits 0.1
lower; its slide stops inside the safe area.

**Kept:** the 120 survivors lining up into the 24 × 5 strip under the 17 % meter, red columns under the red
segment; the unbroken object chain (cold-open diagram → table, now with its "1 in 500" → grid → strip →
crowd → raster → + badge → cold-open diagram with flows); the half-sick control and the bracketed 6×; the
landing's live sweep on one updater and the recall / precision tags on the opening frame's 99 % and 17 %.

### Self-check and second pass (same round, continued after an interruption)

The edits above had been rendered (final.mp4 09:42) but never reviewed. The review kit was re-run on
that master (0 warnings, 0 layout issues, 3:40.7) and every contact sheet and the keyframes at each
fixed timestamp were read, plus 4–15 fps strips through the slider (0:47–0:55), the numbers → names
step (2:01–2:05), the strip → crowd hand-off (2:09–2:13), the 145 squares filing in (2:32–2:36), the
precision ghost (2:46–2:50) and the raster → + badge (3:08–3:12). All the round-6 fixes had landed.
Midway through this pass the toolkit gained PRODUCTION_GUIDE §13 ("the systemic 9-blockers") and a
"Narration craft" section in the review kit, which flagged this cut for length (508 words, 3:40.7),
a metronomic cadence and an 18 s breathless run. Those are now critic-visible, so this pass also
follows §13.7.

**Defects found in the frames and fixed.**
- *Raster → badge (3:09.5).* The outline was eased twice (`smooth` inside a window that is already
  smooth), so it lagged and then raced the shrinking raster, and the raster poked out of it for
  ≈ 0.2 s. Both now run on one clock; the raster stays inside the outline until it is the disk.
- *"precision" copy (2:48.7).* TransformFromCopy started on top of the title at full strength (a
  double strike). It is now a Flight that starts invisible just above the title; "too" arrives last.
- *Live meters vs displayed counts.* During the fail-beat slider and the landing sweep the meter
  showed the exact P(sick∣+) at N while the table showed rounded whole people, so a paused frame could
  disagree by a point (sheet 0:53: "1 in 388 · 26 / 100 → 126" with "20 %", but 26/126 = 20.6 %). This
  happened at 59 of the 499 integer N. Both meters are now driven from the displayed counts (red ÷
  column sum), so every frame re-derives; the spoken N (500, 100, 2) are unchanged (check.py, facts.md).
- *"1 in 500" over "0 sick" (0:33).* The head counts appeared with the empty grid, under the cold
  open's "1 in 500". They now arrive only once the label has rolled to "1 in 2".
- *A false equation mid-build (1:46).* "Divide everything" changed the sick and healthy rows in two
  moves, so for a moment the formula mixed shares and counts (0.002 × 0.99 / (… + 9,980 × 0.01)
  ≈ 17 %). It is one move now, so the formula is true at every frame.
- *Glyph morphs.* "95%" → "99%" interpolated the 5 into a 9 (a smeared glyph at 0:25.9); the alert
  meter's title morphed glyph by glyph into "precision"; the numbers → names step was a per-glyph
  ReplacementTransform. Now: the travelling label cross-fades (the 9 and % stay put), the title rolls
  out and "precision" rolls in, and each number rolls out towards its name's slot while the name rolls
  in from there (numerator first, braces stretching), so no two strings are ever legible at once.
  The render's glyph-morph lint reports 0.
- *Type floors.* The bar tags' second lines (Text 18 = 23 px) are Text 21; "Six Nations 2018 / 48
  alerts" is two lines so it stays inside the safe area; "your test" is Text 24.

**§13 budget and voice (Concision, Audio).** `CADENCE = "shaped"` (sense-following gaps; "hundred and
twenty" read "hundred twenty"), the cold open at 0.84 instead of 0.88, a 0.3 s breath after the hook
question, 0.9 s after the thesis, and 38 fewer words (508 → 470) by the mute test:
- "Check that rule by counting: ten thousand people, half of them sick." (was 18 words, now 12);
- "Test everyone, and watch who lights up." (the beam and the ticking counts show the 99 % / 1 %; the
  spoken rates repeated the cold open word for word);
- "…plus one percent of everyone else: about a hundred." (the 9,980 is on the table; no longer
  spoken, and no repeat of "percent of the healthy");
- "Divide everything by ten thousand: counts become shares. The share can't change." (was 22 words;
  §13.4's example of a ÷ 10,000 step narrated for 14 s);
- "Symptoms raise the one in five hundred: at one in a hundred…" (the label rises on those words).
"Shrink to the alerts. Take the red share." is two short sentences (it ran at 214 wpm); "and these
are how often…" no longer holds "these" for 0.67 s; the "red share" sentence is at 0.80.

**Deictics.** "this disease" pulses the sick node, "a problem like this" pulses the problem's three
numbers, "Here, the rule holds" lands on the meter at the naive marker, and the second "these" grows
its braces, and "here it's one percent" starts the pulse of the 100 false alarms (the render's
deictic check had listed all five).

**Kept:** everything in the round-6 keep lists (strip under the meter, the unbroken object chain, the
half-sick control and the 6× bracket, the live slider and sweep, the recall/precision tags).
