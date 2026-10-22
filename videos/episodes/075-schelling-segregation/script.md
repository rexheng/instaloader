# Episode 75 — Mild Preferences, Segregated Towns

**One idea:** in Schelling's model, households that demand only a third of their neighbors
match still build a town where three quarters match, because each departure tips a neighbor
that was content; so a segregated map cannot tell you what its people wanted.

Runtime ≈ 3:34 · 483 words (budget ≤ 500, 3:15–3:35) · narrator af_heart @ 0.84 (0.82–0.84 per
beat) with CADENCE = "shaped": full stops ≈ 0.47 s, beat turns ≈ 0.67 s, a 0.9 s hold after each of
the three key results (74, 76 %, 95), prediction holds 1.5 s.

(Round 1 title "Mild Preferences, Extreme Segregation" overclaimed: 76 % against a 50 % random
baseline is strong, not extreme, and Schelling himself called his one-third result "slight".)

## Palette (colour → one meaning, whole episode)

| Colour | Meaning |
|---|---|
| BLUE `#5AA9E6` | blue households |
| YELLOW `#F5C451` | gold households (and the count of gold neighbors in every fraction) |
| RED `#EF6F61` | unhappy: a ring drawn *outside* an unhappy household's tile, after a 1 px gap of background colour (the tile keeps its colour; round 6: red right against gold read as orange), the "unhappy" counts, the share-ladder bars of unhappy households |
| PURPLE `#B394E8` | the demand: the share of matching neighbors a household insists on (marker, ⅓ / ¼, the demand line on the ladder, chart x-axis, "demanded" labels) |
| INK (off-white) | the measured outcome (average share of neighbors that match: meter, chart dots and mean ticks); focus boxes; fractions; the zone lines of the rule-made town |
| GRAY / DIM | axes, captions, "plan predicts 0", "round", notes, ladder bars of content households, the random-mix baseline, Schelling's band, citations; the end-card Ω is INK (not BLUE) |

Blue vs gold is colour-blind safe; RED never contrasts with GREEN (GREEN is unused); RED is
always a ring or a count, never a household colour.

## Beats

### 1 · Cold open (0:00–0:12): a segregated town, predict the motive
*Screen:* frame 1 is the finished 40×40 town (seed 3), centred and already tagged "simulated"
(under the board's lower-left corner).
On "simulated" it slides left as the meter enters. The meter bar is drawn already at 76 % and
the number is written on (it never counts up from a 0 % that never existed), so the puzzle's
number is on screen before it is spoken. "three quarters" pulses the 76 %. On "these households"
the PURPLE marker "? demanded" appears (deictic sync), and it pulses on "demand". 1.5 s hold.

> In this simulated town, on average, three quarters of a household's neighbors match its
> color. How much matching do these households demand? [pause 1.5]

### 2 · Reveal + rule (0:12–0:23)
*Screen:* the marker slides from 76 % to ⅓. A white box lands on a gold household; its 3×3
flies out, magnified; the two empty squares get grey × marks and "empty: not counted";
rings on the 2 gold neighbors, "2 of 6 match".

> Just a third. Each household counts the occupied squares around it. If fewer than a third
> match, it moves, so it is happy to be outnumbered two to one.

### 3 · Stakes (0:23–0:32)
*Screen (round 6):* on "real city maps" the rule inset and the meter dim to 35 % and the board's
frame pulses once (the town is read as a map); the demand marker returns on "motives", the
match readout on "patterns", the rule inset on "a demand of one third".

> We read real city maps the same way, guessing motives from patterns. So how can a demand
> of one third build a town of three quarters?

### 4 · Naive build (0:33–0:58)
*Screen:* every tile flies back to its starting square; the meter falls 76 % → 50 %, docks;
the meter docks during "half … above"; the RED "unhappy" counter arrives on "these" and counts
to 238 as RED rings draw round those tiles, while the content households dim to 55 % so the 238
stand out as a set (they return on "Round one"). The HUD sits beside the board's middle (first row
y = 0.45), four rows: unhappy, plan predicts, round, moves. One real
round-1 move is previewed as a dashed arc (the same arc it flies in round one; every hop bends toward the board's centre, so no tile ever swings out over the board's edge). The HUD under the meter is a two-column table:
labels ("unhappy", "plan predicts", "round") right-aligned on one edge, numbers right-aligned
on the meter's 100 % end, so "plan predicts 0" has its 0 directly under the count.

> Rewind to the start, a random mix. Here, on average, half the neighbors match, well above
> a third. Still, these two hundred thirty-eight are unhappy.
>
> The obvious plan is to move each one to a random empty square where it would be
> content, so the town stays mixed.

("plan predicts 0" arrives on "content". Round 6 merged "Then everyone is content" into the plan.)

### 5 · Run + measured failure (0:58–1:17)
*Screen:* round 1: 200 tiles hop (each arc bent toward the board's centre and kept on the board) while the GRAY "moves" row counts live to 200; the meter
climbs to 64 %; the counter stops at 74, above "plan predicts 0". On "thirty-eight" the GRAY note
"38 content by their turn" appears. The counter pulses on "this counter". On "sixty-seven": every
content tile dims, the 7 outlined tiles that were already unhappy at the start turn grey, 67 RED
rings remain, and the 38 note gives its slot to "67 content at the start" (out, then in).

> Round one takes two hundred moves; the other thirty-eight were content by their turn.

(Round 5 cut "The matching share jumps to sixty-four percent": the meter climbs to 64 % live
during the round, so the sentence only read the screen aloud.)
>
> If the plan had worked, this counter would read zero. It reads seventy-four. [pause 0.9]
> Sixty-seven of these were content before round one. They never moved. Their neighbors did.

### 6 · Insight: the domino (1:16–1:51)
*Screen:* "Replay one block" (round 6: "corner" was wrong, the patch sits mid-top): the board parks at the left edge at 0.7 scale and dims to 30 %
except the corner; the HUD and the meter's 64 % readout fade out completely (only "⅓ demanded"
stays, the source of the formula's ⅓). A white box lands on the corner, and the corner
**rewinds**: household A flies home from where round 1 sent it, and the rings return to the
start state. The corner's 4×5 squares fly out into a large inset (675 px wide), formula to its
right, state caption ("before round 1", "after round 2"…) under the formula; each caption change is
a sequential swap (old out, then new in), never a cross-fade. The inset flies
out of the corner box while the corner rewinds (one move). The subject household carries a white
inner outline (B, then C); A's ring stays at 50 % until "Then this neighbor moved away". The board's corner and the inset stay
in step for the whole replay, using the real tiles and the real moves: A flies out to its
round-1 square, and B to its round-2 square while a blue household flies into A's old square,
each in the same animation as the inset departure and the "?".
Rings appear on the board when they appear in the inset.
The formula is built from the tiles: square copies of the 3 gold neighbors fly to the YELLOW
3 and fade into it (copies of all 8 do the same for the 8), then ≥, then PURPLE ⅓ copied from
the demand marker. Each fraction state holds ≥ 1.5 s; C's 2/7 < ⅓ holds through a 0.9 s pause
into the next beat.

> Replay one block. [pause 0.3] At the start, this gold household had three gold neighbors out of
> eight. Three eighths beats a third, so it stayed.
>
> Then this neighbor moved away. Is it still content? [pause 1.0]
>
> Two gold out of seven, less than a third, so now it wants out. (speed 0.80)
>
> Its neighbor here also has three eighths. In round two, our household leaves, and this one
> drops to two sevenths. [pause 0.9]

(Round 5, continued: the third step, "Then the next one, also at three eighths, tips in round
three", was cut for the concision budget. Two links, A → B → C, already make the chain, and a
round-3 critic had called the third step a repeat of the first two.)

(A new subject household (B → C): the old fraction and relation slide out to the left and
fade, then the new household's slide in from the right; the ⅓ stays. The same household's numbers
(3/8 → 2/7) fade out, then the new digits fade in, in place, each half ≥ 0.3 s. No glyph morph.)

### 7 · The cascade completes (1:51–2:02)
*Screen (round 6):* in the gap before "Now" the inset folds away (0.35 s) and the board grows
back to full size and strength while the HUD returns, so rounds 2–7 start on "Now" and run
through the 1.9 s pause, each at least 0.6 s plus 0.15 s for its counts to settle before the
round number advances. The "moves" row is cumulative (200 → 272, 313, 329, 338, 340, 341), so
it never shows a stale per-round value (the replayed movers are already home, so they do not
move twice). The counter reaches 0 on "nobody"; the 76 % pulses after "move".

> Now run the whole town. [pause 1.9] After round seven, nobody wants to move.

### 8 · Generalise: the tipping curve (2:03–2:18)
*Screen:* the HUD fades (0.4 s) while the town shrinks into its thumbnail slot; the axes start
drawing halfway through the shrink (x-axis and y-axis first, below and left of the moving town;
titles last, after it lands), so the chart is complete before the line starts and the frame
never holds a lone thumbnail. A copy of the town leaves on "whole" and lands as the dot
(33.3, 75.5) on "point". After "chart" the
30-town clouds fade in under the note "each dot: one simulated town" (no narration), and only then
does "⅓ → 76 %" appear beside the thumbnail (round 5: the flying copy used to pass over it while
it faded in; likewise "→ 58 %" arrives after the ¼ town's copy has landed as its dot). On "a
quarter" the lower thumbnail's PURPLE ¼ pulses while its column brightens and the others dim to
40 %; on "a third" the ⅓ does the same from the upper label (round 6: the small PURPLE ¼ / ⅓
marks inside the plot read as stray glyphs beside "random mix" and are gone; each column is also
the one our own town's dot lands in). 30 simulated towns per demand: dots r = 0.05 at 60 %
opacity, ±0.3 pp jitter (round 6; were 38 % and ±0.6, "smudges"), INK mean tick and GRAY min–max whisker per column. The same starting
town re-run at ¼ sorts in the lower thumbnail ("¼ → 58 %").

> That whole town is one point on this chart. (speed 0.78; it ran 208 wpm at 0.84)
>
> Demand a quarter, and the same starting town barely sorts: fifty-eight percent. Demand a
> third, and it jumps to seventy-six. [pause 0.9]

### 9 · Why the jump: the share ladder (2:12–2:45)
*Screen:* the ladder is its own chart, about 1.3× the dot chart and 0.8 units higher, built
centred (round 6: its right third used to sit empty for 12 s); on "including" it slides left
(0.8 s) to make room for household A's patch, which fades in only once the right-hand bars have
passed its column. On "sort",
one move that runs from "sort" to "With": the two thumbnails and their labels leave with the dot
chart (one focal region), and the dot chart leaves completely (dots, y-axis, its title, the x
numbers and ticks, the random-mix line; 0–0.3 s); its x-axis line rises and stretches into the
ladder's baseline (0.1–0.7 s); both ladder titles fade in (0.35–0.95 s, after the old x title
has left); and the bars sprout from the line, left to right, standing on it, one every ≈ 0.25 s
across "by each household's share of matching neighbors" (from 0.25 s to "With"). The frame is
never a bare line and never static for 4 s (round 5 cont.: the 09:49 cut showed the bare line for
about 0.9 s, and a first fix left the finished bars static for 4.5 s before "these"). One bar per
share a household of the random start actually has (k of n, n ≤ 8). The vertical is named where a y-axis title sits: INK "households (simulated start)". On "shares come in steps" a
highlight sweeps along the bars and the ends are marked "0%" and "60%".

The rung fractions sit in one row under the baseline. GRAY counts (MathTex 32) sit centred
above their own bars: "2/7" and "67" on "two sevenths", "3/8" and "125" on "three eighths".
The demand is a PURPLE caret between the baseline and the fraction row, plus a PURPLE outline
round the threshold bar; its fraction is in the row under the caret. Every bar left of it
turns RED, and "unhappy 238" sits above the red group. A curved GRAY arrow "lose one match"
runs from the 3/8 count down to the 2/7 count. Household A (2 gold of 7 at the start) appears
in the right column the thumbnails vacated, beside the bars' middle, with 2/7 < ⅓ built from its
tiles (its ⅓ appears as the caret's ⅓ pulses; round 6: a copy flying from the caret crossed the
2/7 on its way).

The prediction: a 50 % caret, a dashed PURPLE outline on the ¼ bar, its "¼" and the count "76"
appear, so all three counts are visible, while A's patch, its formula and the arrow dim to 35 %
(round 6: one focal point, the dashed ¼ outline with 76 and 67); 1.5 s hold. The ⅓ outline and
label lift off, the caret slides to ¼ and crosses exactly two bars, 2/7 (67) and ¼ (76: 66 at
2/8, 10 at 1/4), and the dimmed context returns. The two bars turn grey and flash, the count
falls 238 → 171 → 95, the dashed outline turns solid, and A's formula flips to 2/7 ≥ ¼.
Round 6, the mechanism: the "lose one match" arrow stays. On "three eighths" the 3/8 rung
pulses; on "lose a match" the arrow brightens and its target, the now-grey 2/7 bar, flashes; on
"stay" "lose one match" moves up a line and "still content" fades in under it; on "never
starts" A's 2/7 ≥ ¼ flashes.

> To see why, sort the random start by each household's share of matching neighbors. With
> at most eight neighbors, shares come in steps.
>
> At a third, everyone left of it is unhappy, including the neighbor that started our
> block's chain, at two sevenths.
>
> Every household at three eighths is one lost match away from two sevenths.
>
> At a quarter, how many would start unhappy? [pause 1.5]
>
> Only these two bars change sides: just ninety-five start unhappy. Now a household at three
> eighths can lose a match and stay, so that chain never starts. [pause 0.9]

(Round 6: both critics found that the ¼ side explained the jump by the starting count alone.
The new sentence names the mechanism: 2/7 ≥ ¼, so the 3/8 → 2/7 step that drove A → B → C no
longer tips anyone. "and they're tall" was cut; the count falling 238 → 95 shows it.)

### 10 · Payoff + honest limits (2:45–3:01)
*Screen:* the 2:12 morph in reverse: the bars sink into the baseline and the ladder labels
fade while the two thumbnails return to their column (0.5 s); the baseline shrinks back into the
x-axis while the x title returns to PURPLE "demanded (% of neighbors)" (0.6 s); only then do the
dots and y-axis return (0.7 s; the random-mix line and its label stay out, so the chart carries no unlabelled marker). Citation "Schelling, 1971 · Journal of Mathematical Sociology" appears on "paper",
and a box flashes the two towns on "model". A GRAY "our jump" bracket over ¼–⅓ appears on
"His households", its label on the bracket's own row to its left. On "nearest" the citation is underlined: his rules come from his paper (round 5, continued:
the rules label "nearest move · 25–30% empty" was cut; at the new Text-27 label floor it did not
fit left of his band, and it repeated the narration). On "the jump": "our jump" fades out
(0.3 s), then the bracket slides to 35–50 % (0.6 s), then "Schelling: 35–50%" fades in once it
has stopped. The band
(a light GRAY hatch, fill 7 %) sweeps from 35 to 50 exactly on "between about a third and a half"
while our 30-town dots and mean ticks dim to about 30 %, so it reads as his model's result. Our
two towns' dots (¼ → 58 %, ⅓ → 76 %) stay at full strength: they are the ends of "our jump", left
of his band, and the two thumbnails they belong to are still on screen.

> In his 1971 paper, Thomas Schelling ran this model. His households moved to the nearest
> suitable square, on emptier boards, and there the jump came later, between about a third
> and a half.

(Round 3 cut the quote sentence "He wrote that inferences about individual motives can usually
not be drawn from aggregate patterns": the thesis was stated three times in 45 s. Its source
now carries the landing.)

### 11 · The test: two towns, one picture (3:16–3:47)
*Screen:* a cross-fade to two simulated towns side by side, both "76% match", with nothing to
say which is which (ours is on the right, turned a quarter turn: round 6, so the test is blind;
the viewer has watched the unturned town for 90 s, and a 90° turn changes neither the 76 % nor the
texture). One GRAY "simulated" tag sits centred in the gap, on
the row of the "76% match" labels. The two candidate labels "⅓ demanded" and "0 demanded" wait
unassigned in the gap with a "?". Prediction hold 1.5 s.

Reveal: a box goes on the right town, and "⅓ demanded" travels up the empty gap, then sideways
above the towns, never over tiles. "0 demanded" does the same to the left town while its zone
lines draw on. "· placed by a rule" appears only after it lands. Both headers are centred on
their boards, with "demanded" on one baseline 0.25 above the boards. Citation "Aaronson, Hartley
& Mazumder, 2021 · AEJ: Economic Policy" on "study"; both toy towns dim to 30 % slowly across
"Real segregation has other causes" to 55 %, then to 30 % across "1930s federal lending maps"
(the toy rule is not a model of the 1930s maps, so the zone lines no longer pulse); the two "76% match" labels, the segregation measure,
pulse on the study's "segregation"; the citation is underlined on "credit". No stretch of this beat is static for more than about 2.2 s. The rule town's grain matches a
Schelling town's texture (no stray tiles), so the picture cannot give the answer away.

> Two simulated towns, both seventy-six percent. In one town, households demand a third. In the
> other, nobody minds their neighbors. Which one wanted a third? [pause 1.5]
>
> This one. The other was placed by a rule, with no preferences. Real segregation has other
> causes. One study finds that 1930s federal lending maps increased racial segregation for
> decades, through reduced credit.

(Round 6: the link sentence ties the rule-made town to the study, and splits a 14.7 s run with
no breath. About 0.95 s of silence follows "credit.")

### 12 · Landing (3:48–3:56)
*Screen:* the rule-made town and every label fade first (0.45 s; round 5: the growing town no
longer passes over fading labels) while ours returns to full strength, so the one town left is the
focus of "Look again at the first town", not a dim leftover. Ours then turns back its quarter
turn while it grows into the opening position (one move, landing on "first"), the meter and the
"simulated" tag return on "town", and in the 1.2 s pause the PURPLE marker goes back to "?" at
76 %: the exact opening frame, seen in silence. The "? demanded" marker pulses on "guessed" and the board's
frame on "map". The frame holds 1.2 s after the last word, then fades to the background (round
6: no series card dissolving over the board; trailing silence under 2 s).

> Look again at the first town. [pause 1.2] As Schelling argued, whatever you guessed its people
> demanded, [pause 0.3] the map alone could not have told you. (speed 0.80; it ran 215 wpm)

## Sources
- Schelling, T. C. (1971). Dynamic models of segregation. *Journal of Mathematical Sociology*
  1(2), 143–186. doi:10.1080/0022250X.1971.9989794 (first issued as RAND RM-6014-RC, May 1969).
- Aaronson, D., Hartley, D., & Mazumder, B. (2021). The effects of the 1930s HOLC "redlining"
  maps. *American Economic Journal: Economic Policy* 13(4), 355–392. doi:10.1257/pol.20190414
- All town numbers: `sim.py` in this directory (seeded, deterministic; see facts.md).
