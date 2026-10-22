# Episode 4 — The Hidden Bias That Hid the Hot Hand

**Idea (one sentence):** If you score the flip after each heads *within* a short sequence and
then average those scores, a perfectly fair coin reads below one half (17/42 for four flips),
because each sequence gets one vote and heads-after-heads crowd into a few sequences; tails
crowd the same way, so the 1985 hot-hand test (after 3 hits − after 3 misses) reads −8 for a
random shooter, and measured from that baseline Cornell's +4 becomes +12.

Narration strings live in `narration_text.py` (one per beat, used verbatim by `scene.py`),
voice af_heart, `CADENCE = "shaped"` (gaps follow the sense) at speed 0.82; the beats whose
short plain sentences ran above 200 wpm (`SPEEDS`: undefined, cold, crowds, mirror, observed,
landing) at 0.80. 0.9–1.0 s after each key result (`GAPS`, and `[pause 0.9]` after "minus eight points" and
"twelve points hot").

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| YELLOW | heads / a hit: coin faces, "hit" glyphs, yellow tiles, hᵢ, numerators |
| GRAY (hollow) | tails / a miss: coin faces, "miss" glyphs, gray tiles; also axes. Secondary grey *text* uses #A9AEB6 (8.1:1) |
| BLUE | the streak test and what it reads: rings on checked flips, row scores, nᵢ, the averages 17/42 and 25/42, the random shooter's 46% / 54% and its −8 gap, the streak-length ghost ticks, the test's "hot" verdict arrows (0:28 and the landing), the landing's shooter dot |
| RED | the bias: the −9.5-point gap, the −19-point and −8-point gaps, the "bias" arrow |
| PURPLE | the real Cornell shooters (GVT 1985 data): 49%, 45%, +4, the +12 brace |
| YELLOW dots | hits in a row (●, ●●, ●●●): the "after 3 hits" lane's condition and the flags on the ghost ticks, with a grey "hits in a row" legend — yellow keeps its meaning, a hit; hollow grey dots (○○○) mark the "after 3 misses" lane |
| INK | the assumption (dashed: one half / gap 0, "the obvious guess"); the 14 equal vote outlines and the 1/14 they become |

Never red vs green; red is always labelled.

## Beats

### 1. Cold open (0:00–0:13) — *open*
> Flip a fair coin four times. After each heads, check the next flip: *[pause 0.35]* here, one of
> the two is heads. *[pause 0.35]* Do this for every four flip run, and average. Below, at, or above
> one half? *[pause 1.6]*

Visual: the row of four large coins flips in at the vertical centre of the frame (H H T H).
Blue arcs jump from each eligible heads to the next flip; those flips get blue rings; while the
ringed heads pulses, a copy of its disc materialises just below the row and travels under it into a
yellow 1; both rings likewise into a blue 2 → "1/2" (each copy fades in below its coin and out
before it lands, so no copy ever crosses a coin or is seen doubled). On "Do it" the row rises
and the share axis (0–100%, "checked flips that are heads") draws under it; on "every four flip
run" a ghost of all 16 runs (coin radius 0.15, 75% opacity, compact 4 × 4) deals in under the row
while the row fades to 40%; on "and average" the ghosts collapse onto the line as one "?" and the
row returns (question ends ≈ 0:12.0). On "Below", "at", "above" the three answers "< 1/2", "= 1/2", "> 1/2" appear on
the line where they sit. Prediction hold.

### 2. Stakes (0:13–0:25) — *stakes*
> One half feels obvious, since a coin has no memory. In nineteen eighty five, a study ran this
> kind of check on basketball shots, and called the hot hand an illusion.

Visual: the "= 1/2" answer becomes "the obvious guess" while the "?" and the other two answers
fade, and the dashed ink line grows up from 50%; "every flip: 1/2 heads" (inline MathTex, 38) under the row on "no memory"; citation
(Gilovich et al., 1985 · Cognitive Psychology) on "nineteen eighty five"; the row's arcs and rings
re-trace on "this kind of check"; on "basketball shots" each coin letter morphs into its word
(H → "hit", T → "miss") and the axis title swaps to "checked shots that are hits"; GVT's verbatim
phrase "a powerful and widely shared cognitive illusion" above the row on "illusion".

### 3. The test (0:26–0:32) — *test*
> Heads are hits. A hot shooter beats their usual rate; a random one should match it.

Visual: on "Heads are hits" the three hit words pulse. "→ hot" grows right of the
dashed line (the quote clears); on "usual rate" the dashed line pulses (its label grows away from
the line, about its left edge); on "match it" the row's 1/2 pulses. No "cold" arrow: "cold" is
first spent on the measured −9.5.

### 4. Calibrate (0:32–0:41) — *calibrate*
> First, test the test on a shooter we know is random: a fair coin. Four flips can land
> sixteen ways, all equally likely.

Visual: arrow and citation clear; "hit/miss" morph back into H/T (and the title back to
flips/heads) on "a fair coin"; on "Four
flips" the big row shrinks into its slot of the 4 × 4 table and the other fifteen deal in.
Table coins are radius 0.185 at pitch 0.49, so each blue check ring clears its neighbours.

### 5. Fail (0:41–1:07) — *score*, *undefined*, *average*, *cold*
> This row checks three flips, and two are heads. *[pause 1.0]*
> Two rows show no heads before the last flip, so they get no score.
> Drop the other fourteen scores onto the line. Their average is seventeen out of forty two.
> On a fair coin, the test reads cold, by nine and a half points.

Visual: HHHT worked slowly: its 3 rings are drawn one by one and flash as "/3" is written, then
the two ringed heads pulse as the "2" is written (nothing flies through the tight row); the rest
score in a silent cascade (round 7: "Score every row the same way" is cut); TTTH and
TTTT dim with "–". Each of the 14 scores shrinks into a blue dot in place, then the dots fall onto
the line (six at 0, four at ½, one at ⅔, three at 1); a blue marker slides from 50% to its balance
point with a live "40.5%", settling on "seventeen", and "17/42 =" is written to the left of the
readout ("17/42 = 40.5%") while the fraction is spoken; it rides left with the axis at 1:05 and
leaves at "Gather". Red arrow from 50% to the marker; "cold" on "reads cold", "−9.5 points"
on "nine".

### 6. Insight: one vote per row (1:07–1:50) — *pool*, *votes*, *crowds*, *lineup*, *formula*
> Yet no flip is biased. Gather all twenty four checked flips: twelve heads, twelve tails. Total
> heads over total flips: exactly half.
> The skew comes from scoring row by row: each row gets one vote, however many flips it checked.
> Checked heads come in crowds, since a heads gets the next flip checked too. Here, three heads
> share a single vote, while this lone tails gets a whole one.
> Twelve heads crowd into eight rows. Twelve tails spread across eleven.
> Crowded heads split their votes. *[1.2 s]*
> Line them up: *[pause 0.8]* the heads hold five and two thirds of the fourteen votes.
> *[pause 1.0]* That's seventeen out of forty two. *[1.6 s]*
> So the test takes an average of ratios, one per row, instead of the ratio of totals.

Visual (the one picture): during "Yet no flip is biased" the line and its markers slide left to
open the right column, and the blue 40.5% marker shortens to the vote lane (top 0.15 above the
vote strip), so the pooled strip is read only against the dashed 50% line. The discs of the 24 ringed coins become a strip of 24 equal tiles (the
letters stay in the table); only once they have landed do the yellow tiles fly into "12" and all
24 into "24" (12/24, boundary on the dashed 50%). On "Total heads over total flips" 12/24 restacks
and the table's 14 numerators pulse in place while Σᵢhᵢ is written, then the 14 denominators while
Σᵢnᵢ is written; the "=" joins only on
"exactly half", so Σᵢhᵢ/Σᵢnᵢ = 12/24 sits beside the pooled strip from 1:17 on. A copy regroups row by row, then every row is
resized to one equal vote (1/14): HHHH's three heads squeeze into one vote, HTTT's lone tails
stretches to a whole one (row and segment boxed together). While the tiles regroup, the "40.5%"
and "the obvious guess" labels step back to 25% (nothing crosses them at full strength). The 8 rows
holding heads are boxed while the other rows, the pooled strip, its formula and "the obvious guess"
dim; then the 11 rows holding tails (dimming swaps); counts "12 heads · 8 rows" (yellow) and "12
tails · 11 rows" (grey) in the right column. On "Crowded heads split their votes" only HHHH and
HHHT stay bright and their five third-of-a-vote heads slices pulse with their 3/3 and 2/3. On
"Line them up" the table dims and the yellow parts slide left and stop exactly on the blue 40.5%
marker; its label hands over to "5⅔ votes" over the packed yellow, whose 5⅔ travels to the right
column as a numerator; on "fourteen" "8⅓ votes" appears over the grey and the 14 vote outlines fly
into the denominator 14; on "That's" the "=" and then 17/42 slide in to the right of 5⅔/14 (no copy flies: a cross-fade of
5⅔/14 into 17/42 read as glyph soup). That working then steps aside
(17/42 stays). On "an average" the 14 vote outlines fly into the ink 1/14 (the Σ joins);
on "of ratios" HHHH's own 3/3 travels whole, at table size, comes down onto the sum's empty slot
from above (clear of 1/14 and Σ) and is gone before hᵢ/nᵢ appears there; on "one per row" all 14 row ratios
flash in the table and the "=" joins it to 17/42. Both formulas are
displaystyle at one size with their "=" signs on one vertical. On "instead" the 1/14 Σ pulses, on
"ratio of totals" the two Σ inside the pooled fraction pulse. The table fades out.

Round-7 focus rule for this beat: from "each row gets one vote" the table, the pooled strip,
Σᵢhᵢ/Σᵢnᵢ = 12/24 and "the obvious guess" step back to 30%, the 40.5% readout to 25% (the vote strip is
the one subject); a table row returns to full only while it is named: HHHH from "since a heads
gets the next flip checked too" to "lone", HTTT on "this lone tails", the 8 heads rows on "Twelve
heads", the 11 tails rows on "Twelve tails", HHHH and HHHT on "split"; the 14 denominators flash on
"however many flips it checked"; the readout comes back as the heads pack onto its marker; the
pooled strip and its formula come back to full on "the ratio of totals" (never removed, so no
third equation arrives). The 14 outlines are counted in place (each answers in turn) as "14" is
written; on "an average" the outlines themselves (no copies, right-most first) lift off at 40%, run right between the
strips and become 1/14 and Σ. 5⅔ / 14 = 17/42 is held complete ≥ 3.2 s. The HHHH and HTTT boxes
take the rings in, 0.13 clear of them.

### 7. The mirror (1:50–2:07) — *mirror*, *gap*
> Now score the flip after each tails. Swap heads and tails, and the strip flips over one half:
> the test reads high, twenty five out of forty two.
> Subtract the averages: a fair coin shows a gap of minus nineteen points.

Visual: on "score" the pooled strip, its formula and the left side of the row-average formula fade
out in place (0.5 s, drifting up 0.3); the whole picture rises 1 unit while the formula's 17/42
moves up to become the "after heads" lane value: the vote strip takes the top lane and its blue
marker becomes that lane's cursor. A copy drops, unchanged, into the bottom lane (0.8 s). On
"Swap heads and tails" its tiles recolour in place (yellow ↔ grey). On "the strip flips over one
half" it turns a half turn about the dashed 50% line (1.6 s, one sine ease) while the dashed line
thickens as the mirror axis: its heads part now ends at 59.5%. "after tails" + cursor on "after a
tails"; on "twenty five" the heads part answers in place (a vertical flash) and "25/42" is
written beside "after tails" (round 7: no copy crosses the strip). A red arrow from the after-tails cursor
to the after-heads cursor: "−19 points".

### 8. Payoff (2:07–3:00) — *cornell*, *minus8*, *observed*, *hot*
> The nineteen eighty five study ran the same comparison on twenty six Cornell players: up to a
> hundred shots each, from where they'd hit about half. After three hits, versus after three misses.
> For a random shooter, the same crowding pulls after hits down to forty six percent on average,
> and after misses up to fifty four. Miller and Sanjurjo's twenty eighteen paper *[pause 0.5]* puts
> the gap at about minus eight points. *[pause 0.9]* Longer records shrink it, *[pause 0.5]* but a
> hundred shots isn't long.
> The Cornell players hit forty nine percent after three hits, and forty five after three misses.
> The study found plus four, too close to zero to count, so no hot hand.
> Measured from minus eight, it's twelve points hot. *[pause 0.9]* That's evidence for a hot hand
> in a gym, not proof it survives defenders in a game.

Visual (round 6: no simulated record, no zoom). On "nineteen eighty five" the strips clear to two
thin lanes on the same 0–100% axis, both cursors glide back to 50% and the values become "?", while
the grey header "1985 design" and the GVT citation come in. On "the same comparison" the lane labels
become "after 3 hits" / "after 3 misses" (axis title "checked shots that are hits") and each lane
gets its condition at its left end (●●● yellow hits, ○○○ hollow grey misses). "· 26 players" and
"· up to 100 shots" join the header phrase by phrase, kept centred, each only once the header has
slid aside to make room for it. On "about half" the dashed 50%
line and its tick pulse and "the obvious guess" (ink, as in the cold open) labels its top: what the
1985 test assumed a random shooter reads. On "After three hits" / "after three misses" each lane's
glyph and label pulse (the header details dim). On "For a random shooter" a blue "random" column head; the M&S
citation on "the same crowding"; on "pulls after hits down" the top cursor slides 50 → 46% (value
46%), on "after misses up" the bottom one 50 → 54%, the red arrow growing between them. On "gap"
the pair slides until after-misses sits on the dashed line, then the same tick marks are relabelled
−10 … +10 (each % label hands over to its point label in place, so the axis is never unlabeled):
the after-hits cursor stretches out into the blue random-shooter marker at −8, the arrow becomes
the red "bias"; "the obvious guess" rides down with the dashed line, now the zero gap; the right
column dims to 30%. Silent 0.8 s on the −8 picture. Ghost ticks as
before (1, 2, 3 hits in a row → −1.0, −3.1, −8; the 3-hit one slides to its 1,000-shot place −0.7
and back). Cornell: the ghost clears, the grey header fades and then the purple "Cornell, 1985"
fades in (never superposed), the GVT citation returns to full and M&S dims; the column head "random" becomes "Cornell" and
on the spoken numbers 46% → 49% and 54% → 45% in the same slots. After "three misses" whole copies
of 49 and 45 travel to the right of where Cornell's marker will stand and "49 − 45" is written; on
"plus four" "= +4" lands as the purple marker grows up from the axis; the dashed 0 and "the obvious
guess" pulse on "no hot hand" (GVT measured +4 from zero), then a silent 0.9 s. On "Measured from minus eight" the right column leaves (its "Cornell" head travels to tag
the +4 marker, mirroring "random shooter" at −8), "the obvious guess" leaves, the chart re-centres
under its title (+1.4 units), carrying "49 − 45 = +4" beside its marker; a purple brace from −8 to +4
grows, "+12 points" on "twelve". On "in a gym" a grey "no defenders" tag under "49 − 45 = +4", pulsing on
"defenders". Citations stay at full strength.

### 9. Landing (3:00–3:14) — *landing*
> One half *[pause 0.15]* is what a fair coin does. *[pause 0.9]* Seventeen out of forty two is what this test
> sees. A fifty percent shooter *[pause 0.3]* who averages one half on this test *[pause 0.2]* is
> already running hot.

Visual: one 1.3 s move: the payoff fades (in its first third) except its number line, tick marks
and dashed zero line, which drop into the cold open's 0–100% share axis and its dashed one-half guess (the re-centred
chart already sits where the cold-open axis sits) while H H T H with its 1/2 fades back in. On "fair"
the cold open's ghost of the sixteen runs returns in the cold open's place and size (coin radius
0.15, 60%) while the row fades to 40% and the guess label leaves; held ≈ 1 s. On "Seventeen" its
fourteen scored rows fly into (1/14) Σᵢ hᵢ/nᵢ while the blue marker draws at 40.5%, and "= 17/42"
slides out of the marker to the left as the marker flashes: the cold-open question, answered on its own image, with the test's formula.
On "A fifty percent shooter" the row becomes hit/hit/miss/hit and the axis title "checked shots
that are hits"; on "averages one half on this test" the row dims to 30% and a blue dot grows on the
one-half line at the formula's height, tagged in grey "its rows average 1/2"; on "already running
hot" a thick blue arrow grows from the 17/42 marker to it: "hot". Hold ≈ 2.2 s on that frame; no
end card over it.

Round-7 payoff changes: on "twenty eighteen paper" the pair slides until after-misses sits on the
dashed 50% line; on "puts the gap" the red gap between the cursors gets its number, blue "−8", at
the end that moved; on "at about minus eight points" the axis zooms ×5 about the dashed line
(2.0 s, smooth): the 0/25/75/100% ticks run outward and leave, −10/−5/+5/+10 grow out of the
centre onto the same five tick positions, "50%" hands over to "0", the cursor rides the zoom to −8
carrying its "−8", the red gap stretches into the "bias" arrow, the right column dims. The
streak-length ghosts are cut: on "Longer records" one ghost of the −8 marker slides to −0.7
("1,000 shots") and back on "isn't". On "too close to zero" the dashed zero line pulses and grey
"vs 0: p = .49" appears under "49 − 45 = +4" (M&S's replication of GVT's paired t-test; both
citations at full); it leaves as the chart re-centres. On "Measured from minus eight" the purple
header "Cornell, 1985" itself travels (right, then down, clear of the marker) to tag the +4
marker, and the column head "Cornell" leaves, so "Cornell" is printed once. Landing: the ghost of
the sixteen runs deals in on "is what a fair coin does" at 75% while the dashed guess steps back
to 25%, is held ≈ 1.8 s, and on "Seventeen" its fourteen rows fly one after another (lag 0.06)
into (1/14) Σᵢ hᵢ/nᵢ; then the marker draws and "= 17/42" slides out of it; the dashed line comes
back to full on "A fifty percent shooter".

## Sources (on screen)
- Gilovich, Vallone & Tversky, 1985 · Cognitive Psychology 17(3):295–314 (shown as "Gilovich et al., 1985 · Cognitive Psychology")
- Miller & Sanjurjo, 2018 · Econometrica 86(6):2019–2047

See `facts.md` for every number, `check_numbers.py` to recompute them.
