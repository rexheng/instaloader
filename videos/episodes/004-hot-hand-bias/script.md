# Episode 4 — The Hidden Bias That Hid the Hot Hand

**Idea (one sentence):** If you score the flip after each heads *within* a short sequence and
then average those scores, a perfectly fair coin reads below one half (17/42 for four flips),
because each sequence gets one vote and heads-after-heads crowd into a few sequences; tails
crowd the same way, so the 1985 hot-hand test (after 3 hits − after 3 misses) reads −8 for a
random shooter, and measured from that baseline Cornell's +4 becomes +12.

Narration strings live in `narration_text.py` (one per beat, used verbatim by `scene.py`),
voice af_heart, speed 0.81. Sentence gaps vary: `[pause 0.12]` inside a thought, 0.55–0.8 s
after the beats that close a section or the densest run (`GAPS`, "across eleven."), 0.38 s
otherwise.

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| YELLOW | heads / a hit: coin faces, "hit" glyphs, yellow tiles, hᵢ, numerators |
| GRAY (hollow) | tails / a miss: coin faces, "miss" glyphs, gray tiles; also axes and secondary labels |
| BLUE | the streak test and what it reads: rings on checked flips, row scores, nᵢ, the averages 17/42 and 25/42, the random shooter's 46% / 54% and its −8 gap, the streak-length ghost ticks, the landing's shooter dot |
| RED | the bias: the −9.5-point gap, the −19-point and −8-point gaps, the "bias" arrow |
| PURPLE | the real Cornell shooters (GVT 1985 data): 49%, 45%, +4, the +12 brace |
| YELLOW dots | hits in a row (●, ●●, ●●●) flagged on the ghost ticks, with a grey "hits in a row" legend — yellow keeps its meaning, a hit |
| INK | the assumption (dashed: one half / gap 0, "the obvious guess"); the 14 equal vote outlines and the 1/14 they become |

Never red vs green; red is always labelled.

## Beats

### 1. Cold open (0:00–0:13) — *open*
> Flip a fair coin four times. After each heads, check the next flip: here, one of the two is
> heads. Do it for all sixteen sequences and average the shares. What do you get? *[pause 1.6]*

Visual: the row of four large coins flips in at the vertical centre of the frame (H H T H).
Blue arcs jump from each eligible heads to the next flip; those flips get blue rings; the
ringed heads lifts into a yellow 1, both rings into a blue 2 → "1/2". On "Do it" the row rises
and the share axis (0–100%, "checked flips that are heads") draws under it; on "all sixteen
sequences" a ghost of all 16 sequences (coin radius 0.12, 60% opacity, compact 4 × 4) deals in
under the row; on "average the shares" the ghosts collapse onto the line as one "?" (question
ends ≈ 0:11.6). Prediction hold.

### 2. Stakes (0:13–0:25) — *stakes*
> One half feels obvious, since a coin has no memory. In nineteen eighty five, a famous study
> ran this same check on basketball shots, and called the hot hand an illusion.

Visual: "?" → dashed ink line at 50%, "the obvious guess"; "every flip: 1/2 heads" (inline
MathTex, 38) under the row on "no memory"; citation (Gilovich et al., 1985 · Cognitive
Psychology) on "nineteen eighty five"; the caption clears on "basketball"; GVT's verbatim phrase
"a powerful and widely shared cognitive illusion" above the row on "illusion".

### 3. The test (0:26–0:32) — *test*
> Heads are hits. A hot shooter beats their usual rate; a random one should match it.

Visual: on "Heads are hits" each coin's letter morphs into its word (H → "hit", T → "miss") and
the axis title swaps words in place to "checked shots that are hits". "→ hot" grows right of the
dashed line (the quote clears); on "usual rate" the dashed line pulses (its label grows away from
the line, about its left edge); on "match it" the row's 1/2 pulses. No "cold" arrow: "cold" is
first spent on the measured −9.5.

### 4. Calibrate (0:32–0:41) — *calibrate*
> So first, test the test on a shooter we know is random: a fair coin. Four flips can land
> sixteen ways, all equally likely.

Visual: arrow and citation clear; "hit/miss" morph back into H/T (and the title back to
flips/heads) on "a fair coin"; on "Four
flips" the big row shrinks into its slot of the 4 × 4 table and the other fifteen deal in.
Table coins are radius 0.185 at pitch 0.49, so each blue check ring clears its neighbours.

### 5. Fail (0:41–1:07) — *score*, *undefined*, *average*, *cold*
> This row checks three flips, and two of them are heads. Score every row the same way.
> Two rows never show a heads before the last flip, so they get no score.
> Drop the other fourteen scores onto the line. Their average is seventeen out of forty two:
> about forty point five percent.
> On a perfectly fair coin, the test reads cold, by nine and a half points.

Visual: HHHT worked slowly (3 rings, 2/3 built from them), the rest score in a cascade; TTTH and
TTTT dim with "–". Each of the 14 scores shrinks into a blue dot in place, then the dots fall onto
the line (six at 0, four at ½, one at ⅔, three at 1); a blue marker slides from 50% to its balance
point with a live "40.5%". Red arrow from 50% to the marker; "cold" on "reads cold", "−9.5 points"
on "nine".

### 6. Insight: one vote per row (1:07–1:50) — *pool*, *votes*, *crowds*, *lineup*, *formula*
> Yet no flip is biased. Gather all twenty four checked flips: twelve heads, twelve tails. Exactly half.
> The skew comes from scoring row by row, because each row gets one vote, however many flips it checked.
> And checked heads come in crowds, since a heads gets the next flip checked too. This row's three
> heads share a single vote, while this lone tails gets a whole one.
> Twelve heads crowd into eight rows. Twelve tails spread across eleven. Line up the votes, and heads
> hold seventeen out of forty two.
> That's one vote per row. Count all the flips together first, and you get one half.

Visual (the one picture): during "Yet no flip is biased" the line and its markers slide left to
open the right column, and the blue 40.5% marker shortens to the vote lane (top 0.15 above the
vote strip), so the pooled strip is read only against the dashed 50% line. The discs of the 24 ringed coins become a strip of 24 equal tiles (the
letters stay in the table); only once they have landed do the yellow tiles fly into "12" and all
24 into "24" (12/24, boundary on the dashed 50%). A copy regroups row by row, then every row is
resized to one equal vote (1/14): HHHH's three heads squeeze into one vote, HTTT's lone tails
stretches to a whole one (row and segment boxed together). The 8 rows holding heads, then the 11
holding tails, are outlined; the yellow parts slide left and stop exactly on the blue 40.5% marker;
the packed yellow, as one block, flies into "17/42". On "That's" the 14 numerators fly into hᵢ
and the 14 denominators into nᵢ (two grouped flights, no glyph shatter); on "vote per row" 14
equal ink outlines draw over the strip and fly into the ink 1/14. On "Count all the flips" 12/24
restacks piece by piece (12 → numerator, slash → bar, 24 → denominator), then the numerators fly
into Σhᵢ and the denominators into Σnᵢ. The table
fades out while "one half" is still sounding.

### 7. The mirror (1:50–2:07) — *mirror*, *gap*
> Tails crowd the same way. Swap heads and tails, and the strip flips over one half. So after a
> tails, the test reads hot: twenty five out of forty two.
> Subtract the two averages, and a fair coin shows a gap of minus nineteen points.

Visual: on "Tails crowd" the pooled strip and both formulas fade out in place (0.5 s, drifting
up 0.3), and only then does the whole picture rise 1 unit (no empty top
half): the vote strip takes the top lane ("after heads", 17/42 in the right column) and its blue
marker becomes that lane's cursor. A copy drops, unchanged, into the bottom lane (0.8 s). On
"Swap heads and tails" its tiles recolour in place (yellow ↔ grey). On "the strip flips over one
half" it turns a half turn about the dashed 50% line (1.6 s, one sine ease) while the dashed line
thickens as the mirror axis: its heads part now ends at 59.5%. "after tails" + cursor on "So after a
tails"; the heads part, as one block, flies into "25/42". A red arrow from the after-tails cursor
to the after-heads cursor: "−19 points".

### 8. Payoff (2:07–3:00) — *cornell*, *minus8*, *observed*, *hot*
> The nineteen eighty five study ran the same comparison on twenty six Cornell players: up to a
> hundred shots each, from where they'd hit about half. After three hits, versus after three misses.
> For a random shooter, the same crowding pulls those to forty six and fifty four percent. Miller and
> Sanjurjo's twenty eighteen paper puts the gap at about minus eight points. Longer streaks grow the
> bias. *[pause 0.9]* Longer records shrink it, *[pause 0.5]* but a hundred shots isn't long.
> Cornell's players hit forty nine percent after three hits, and forty five after three misses. The
> study took that plus four to mean no hot hand.
> Measured from minus eight, it's twelve points hot. That's evidence for a hot hand in a gym, not
> proof it survives defenders in a game.

Visual: header "Cornell, 1985 · 26 players · up to 100 shots" builds phrase by phrase. The strips
fade to two thin lanes ("sliders"); both cursors glide back to 50% (the obvious guess), values
become "?"; the old tick labels fade out *before* the line is rescaled to 40–60% (5 ticks, "next-shot
hit rate"). On "about half" the dashed 50% line and its tick pulse (each shooter stood where they hit
~50%). Lane labels become "after 3 hits" / "after 3 misses"; the header details dim to 30%,
"Cornell, 1985" stays. On "the same crowding" the after-3-hits cursor slides 50 → 46% and the
after-3-misses cursor 50 → 54%, the red arrow growing between them; values 46% / 54%. A blue
"random" column head is written over the right column on "For a random shooter", before any number
lands in it, and the M&S citation comes in on "the same crowding" (GVT's dims on "Miller"). On
"gap": the percent labels fade out, the pair slides left until the after-misses cursor sits on the
dashed line, and the same tick marks are relabelled −10 … +10 ("after-hits − after-misses (points)",
one line): the after-hits cursor is now the blue random-shooter marker at −8, the arrow the red
"bias"; the right column dims to 30% (no lanes left to label). On "Longer streaks grow the bias"
three dim blue ghost ticks slide out of zero to −1.0, −3.1 and −8 (the last lands exactly under the
−8 marker); each carries a flag of yellow hit dots (●, ●●, ●●●) hung on the left of its own tick top
by an updater, and a grey "hits in a row" legend sits above ●●; the picture holds ≈ 1.8 s. On
"Longer records shrink it" the 1- and 2-hit ghosts step aside and the 3-hit ghost slides with its
flag to its 1,000-shot position (−0.7, labelled "1,000 shots"), held ≈ 2.2 s; on "isn't" it slides
back under −8 and "up to 100 shots" in the header flashes. Cornell: the last ghost clears, the
header details fade (the title re-centres), the right column returns with a purple "Cornell" column
head beside "random", and purple 49% / 45% appear under it, then fly (arced clear of the other
labels) into a purple marker at +4 ("+4"); the dashed 0 pulses on "no hot hand". A purple brace
from −8 to +4 above the two marker tops; "+12 points" fades down onto it as the brace finishes
(right column dims). On "evidence" the title and citations dim to 30%; on "in a gym" a grey "no
defenders" tag appears under +4 and pulses on "defenders".

### 9. Landing (3:00–3:14) — *landing*
> One half is what a fair coin does. Seventeen out of forty two is what this test sees. A fifty
> percent shooter *[pause 0.3]* who averages one half on this test *[pause 0.2]* is already running hot.

Visual: the payoff fades out (0.5 s), then the cold-open frame fades in (0.8 s): H H T H with its
1/2, the 0–100% line with the dashed "the obvious guess" at 50%. On "Seventeen" the ghost of the
sixteen rows returns left of the line and collapses onto 40.5%, where the blue 17/42 marker draws:
the cold-open question, answered on its own image. HHTH's own 1/2 stays put. On "A fifty percent
shooter" the dashed 50% line pulses; on "averages one half" a blue dot (the shooter's average)
grows on it; on "already running hot" an arrow grows from the 17/42 marker to it: "hot". Hold ≈ 0.8 s on that frame; no end card over it.

## Sources (on screen)
- Gilovich, Vallone & Tversky, 1985 · Cognitive Psychology 17(3):295–314 (shown as "Gilovich et al., 1985 · Cognitive Psychology")
- Miller & Sanjurjo, 2018 · Econometrica 86(6):2019–2047

See `facts.md` for every number, `check_numbers.py` to recompute them.
