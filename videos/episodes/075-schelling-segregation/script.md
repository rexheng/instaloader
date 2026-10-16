# Episode 75 — Mild Preferences, Segregated Towns

**One idea:** in Schelling's model, households that demand only a third of their neighbors
match still build a town where three quarters match, because each departure tips a neighbor
that was content; so a segregated map cannot tell you what its people wanted.

Runtime 3:56.4 · 568 words · narrator af_heart @ 0.84 (0.80–0.85 per beat);
variable gaps: ≈ 0.25 s inside a thought, ≈ 0.9 s at beat boundaries.

(Round 1 title "Mild Preferences, Extreme Segregation" overclaimed: 76 % against a 50 % random
baseline is strong, not extreme, and Schelling himself called his one-third result "slight".)

## Palette (colour → one meaning, whole episode)

| Colour | Meaning |
|---|---|
| BLUE `#5AA9E6` | blue households |
| YELLOW `#F5C451` | gold households (and the count of gold neighbors in every fraction) |
| RED `#EF6F61` | unhappy: a ring drawn *outside* an unhappy household's tile (the tile keeps its colour), the "unhappy" counts, the share-ladder bars of unhappy households |
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
number is on screen before it is spoken. "three quarters" pulses the 76 %. On the question a
PURPLE marker "? demanded" appears at the same height. 1.5 s hold.

> In this simulated town, on average, three quarters of a household's neighbors match its
> color. How much matching do these households demand? [pause 1.5]

### 2 · Reveal + rule (0:12–0:23)
*Screen:* the marker slides from 76 % to ⅓. A white box lands on a gold household; its 3×3
flies out, magnified; the two empty squares get grey × marks and "empty: not counted";
rings on the 2 gold neighbors, "2 of 6 match".

> Just a third. Each household counts the occupied squares around it. If fewer than a third
> of them match, it moves. It is happy to be outnumbered two to one.

### 3 · Stakes (0:23–0:32)
> We read maps of real cities the same way, guessing motives from patterns. So how does a
> demand of a third build a town of three quarters?

### 4 · Naive build (0:33–0:58)
*Screen:* every tile flies back to its starting square; the meter falls 76 % → 50 %, docks;
the RED "unhappy" counter counts to 238 as RED rings draw round those tiles. One real
round-1 move is previewed as a dashed arc. The HUD under the meter is a two-column table:
labels ("unhappy", "plan predicts", "round") right-aligned on one edge, numbers right-aligned
on the meter's 100 % end, so "plan predicts 0" has its 0 directly under the count.

> Rewind to the start, a random mix. Here, on average, half of a household's neighbors
> match, well above a third. So most households are content. Only these two hundred and
> thirty-eight are not, about one in six.
>
> The obvious plan is to move each of them to a random empty square where it would be
> content. Then everyone is content, and the town stays mixed.

### 5 · Run + measured failure (0:58–1:17)
*Screen:* round 1: 200 tiles hop; the meter climbs to 64 %; the counter stops at 74, above
"plan predicts 0". On "sixty-seven": every content tile dims, the 7 outlined tiles that were
already unhappy at the start turn grey, 67 RED rings remain, and the GRAY note "67 content at
the start" appears, right-aligned on the number column.

> Round one takes two hundred moves, and the matching share jumps to sixty-four percent.
>
> If the plan had worked, this counter would read zero. It reads seventy-four, and
> sixty-seven of these were content before round one. They never moved. Their neighbors did.

### 6 · Insight: the domino (1:16–1:51)
*Screen:* "Replay one corner": the board parks at the left edge at 0.7 scale and dims to 30 %
except the corner; the HUD and the meter's 64 % readout fade out completely (only "⅓ demanded"
stays, the source of the formula's ⅓). A white box lands on the corner, and the corner
**rewinds**: household A flies home from where round 1 sent it, and the rings return to the
start state. The corner's 4×5 squares fly out into a large inset (675 px wide), formula to its
right, state caption ("before round 1", "after round 2"…) under the formula. The board's corner and the inset stay
in step for the whole replay, using the real tiles and the real moves: A flies out to its
round-1 square, B to its round-2 square while a blue household flies into A's old square, and
C to its round-3 square, each in the same animation as the inset departure and the "?".
Rings appear on the board when they appear in the inset.
The formula is built from the tiles: square copies of the 3 gold neighbors fly to the YELLOW
3 and fade into it (copies of all 8 do the same for the 8), then ≥, then PURPLE ⅓ copied from
the demand marker. Each fraction state holds ≥ 1.5 s: C's 2/7 < ⅓ through a 1 s pause, D's
3/8 ≥ ⅓ through "the next one, also at three eighths", D's 2/7 < ⅓ into the next beat.

> Replay one corner. Before round one, this gold household had three gold neighbors out of
> eight. Three eighths is more than a third, so it stayed.
>
> Then this neighbor moved away. Is it still content? [pause 1.2]
>
> Two gold out of seven. Two sevenths is less than a third, so now it wants out.
>
> Its neighbor here also has three eighths. In round two, our household leaves, and this one
> drops to two sevenths. [pause 0.7] Then the next one, at three eighths, tips.

### 7 · The cascade completes (1:51–2:02)
*Screen:* on "whole town" the inset fades, the board grows back to full size and strength,
the HUD returns, and rounds 2–7 run
(the replayed movers are already home, so they do not move twice). The counter reaches 0 by
"nobody".

> Now run the whole town. Round after round, the tipping spreads, and after round seven,
> nobody wants to move. Seventy-six percent, the town we started with.

### 8 · Generalise: the tipping curve (2:03–2:18)
*Screen:* the HUD leaves first; then, as the narration starts, the town shrinks into its
thumbnail slot, and the axes draw while a copy of it lands as the dot (33.3, 75.5) on "point". 30 simulated towns per demand: dots r = 0.05 at 38 %
opacity, ±0.6 pp jitter, INK mean tick and GRAY min–max whisker per column. The same starting
town re-run at ¼ sorts in the lower thumbnail ("¼ → 58 %").

> That whole town is one point on this chart. Thirty towns at each demand, from zero to sixty
> percent.
>
> Demand a quarter, and the same starting town barely sorts: fifty-eight percent. Demand a
> third, and it jumps to seventy-six.

### 9 · Why the jump: the share ladder (2:12–2:45)
*Screen:* the ladder is its own chart, about 1.3× the dot chart and 0.8 units higher. On "sort",
the dot chart leaves completely (dots, y-axis, its title, the x numbers and ticks, the
random-mix line) while its x-axis line moves up and stretches into the ladder's GRAY baseline
and the x title cross-fades to INK "share of neighbors matching". Only then do the bars grow
from the baseline, one per share a household of the random start actually has (k of n,
n ≤ 8). Title: "households by share (simulated start)". On "these" a highlight sweeps along
the bars; on "sixty percent" the ends are marked "0%" and "60%".

The rung fractions sit in one row under the baseline. GRAY counts (MathTex 32) sit centred
above their own bars: "2/7" and "67" on "two sevenths", "3/8" and "125" on "three eighths".
The demand is a PURPLE caret between the baseline and the fraction row, plus a PURPLE outline
round the threshold bar; its fraction is in the row under the caret. Every bar left of it
turns RED, and "unhappy 238" sits above the red group. A curved GRAY arrow "lose one match"
runs from the 3/8 count down to the 2/7 count. Household A (2 gold of 7 at the start) appears
between the thumbnails, with 2/7 < ⅓ built from its tiles (its ⅓ copied from "⅓ → 76%").

The prediction: a 50 % caret, a dashed PURPLE outline on the ¼ bar, its "¼" and the count "76"
appear, so all three counts are visible; 1.2 s hold. The ⅓ outline and label lift off, the
caret slides to ¼ and crosses exactly two bars, 2/7 (67) and ¼ (76: 66 at 2/8, 10 at 1/4).
They turn grey, the arrow and its label fade with the slide, the count falls 238 → 171 → 95,
the dashed outline turns solid, and A's formula flips to 2/7 ≥ ¼.

> To see why that happens, sort the random start by each household's share of matching
> neighbors. With at most eight neighbors, these are the only shares up to sixty percent.
>
> At a third, everyone left of it is unhappy, two hundred and thirty-eight, including the
> neighbor that started our corner's chain, at two sevenths.
>
> Every household at three eighths is one lost match away from it.
>
> At a quarter, how many would start unhappy? [pause 1.2]
>
> Only these two bars change sides, and they're tall: now just ninety-five start unhappy,
> and that chain never starts.

### 10 · Payoff + honest limits (2:45–3:01)
*Screen:* the 2:12 morph in reverse: the bars sink into the baseline and the ladder labels
fade (0.6 s); the baseline shrinks back into the x-axis while the x title returns to PURPLE
"demanded (% of neighbors)" (0.7 s); only then do the dots, y-axis and random-mix line return
(0.6 s). Citation "Schelling, 1971 · Journal of Mathematical Sociology" appears on "paper",
and a box flashes the two towns on "model". A GRAY "our jump" bracket over ¼–⅓ appears on
"His households", its label on the bracket's own row to its left. "his rules: nearest square"
and "25–30% empty (ours: 10%)" appear on their words, right-aligned under that row. On "came
later" the bracket slides to 35–50 % and "Schelling's jump: 35–50%" takes the row, so his
label, his rules and his band read as one block. The band (GRAY, 18 %) sweeps from 35 to 50
exactly on "between about a third and a half".

> In his 1971 paper, Thomas Schelling ran this model. His households moved to the nearest
> square that suited them, on emptier boards, and there the jump came later, between about a
> third and a half.

(Round 3 cut the quote sentence "He wrote that inferences about individual motives can usually
not be drawn from aggregate patterns": the thesis was stated three times in 45 s. Its source
now carries the landing.)

### 11 · The test: two towns, one picture (3:16–3:47)
*Screen:* a cross-fade to two simulated towns side by side, both "76% match", with nothing to
say which is which (ours is on the right). One GRAY "simulated" tag sits centred in the gap, on
the row of the "76% match" labels. The two candidate labels "⅓ demanded" and "0 demanded" wait
unassigned in the gap with a "?". Prediction hold 1.5 s.

Reveal: a box goes on the right town, and "⅓ demanded" travels up the empty gap, then sideways
above the towns, never over tiles. "0 demanded" does the same to the left town while its zone
lines draw on. "· placed by a rule" appears only after it lands. Both headers are centred on
their boards, with "demanded" on one baseline 0.25 above the boards. The zone lines pulse on
"increased" and again on "credit"; the two "76% match" labels pulse on "decades". Citation
"Aaronson, Hartley & Mazumder, 2021 · AEJ: Economic Policy".

> Two simulated towns, both seventy-six percent. In one, households demand a third; in the
> other, nobody minds their neighbors at all. Which one wanted a third? [pause 1.5]
>
> This one. The other was placed by a rule, with no preferences at all. In real cities, one
> study finds that 1930s federal lending maps increased racial segregation for decades. It
> traces this to reduced credit in the areas marked in red.

### 12 · Landing (3:48–3:56)
*Screen:* the rule-made town fades. Ours grows back into the opening position, the meter and
the "simulated" tag return, and the PURPLE marker goes back to "?" at 76 %: the exact opening
frame.

> Look again at the first town. As Schelling argued, whatever you guessed its people demanded,
> the map alone could not have told you.

## Sources
- Schelling, T. C. (1971). Dynamic models of segregation. *Journal of Mathematical Sociology*
  1(2), 143–186. doi:10.1080/0022250X.1971.9989794 (first issued as RAND RM-6014-RC, May 1969).
- Aaronson, D., Hartley, D., & Mazumder, B. (2021). The effects of the 1930s HOLC "redlining"
  maps. *American Economic Journal: Economic Policy* 13(4), 355–392. doi:10.1257/pol.20190414
- All town numbers: `sim.py` in this directory (seeded, deterministic; see facts.md).
