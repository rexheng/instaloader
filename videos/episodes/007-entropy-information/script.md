# Episode 7: How Much Information Is in a Letter?

**Idea (one sentence):** A character costs log₂(1/p) yes-or-no questions, so its information
depends on how predictable it is, not on how many letters exist. Averaged over English, and
using what came before, that is about one bit per character, not the 4.75 that halving the
alphabet suggests.

Runtime target is about 3:56 (~600 words). Voice af_heart, speed 0.84.

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | probability: candidate tiles, column widths, every `p` (including the p inside 1/p), the E/Z share strips, the % braces, "×130", "1/1260" |
| YELLOW | questions (= bits): the "?" box (and the run of "?" boxes), halving cuts and arrows, the "3.75 extra" overlay, doubling counters, `2^k`, `k`, `log₂(1/p)`, `H`, the level line, E's outline at "half a question", guess counts above 1 |
| GREEN | Shannon's measurements: the ≈1 band (0.6–1.3), the first-guess tally, "1 guess" |
| PURPLE | context, the characters already read: the dim "already read" row, Q, TH, THE OTHER DA |
| GRAY | axes, ticks, titles, citations, leaders, the inset frame, reference levels (the abandoned 4.75, the 4.11 reference while contexts are priced, the 2.81 all-contexts average), first-guess "1"s |
| INK | letters, labels, the language-model marker |

Emphasis rules:
- A context box is emphasised with a purple flash.
- A probability column is emphasised with a white outline plus a brighter blue.
- Yellow is reserved for questions.

## Data

- Letter probabilities come from the Brown Corpus (Francis & Kučera, 1964), reduced to
  Shannon's 27 symbols: 5,751,047 characters. Computed by `data.py` (writes `data.json`).
- The guess record and bounds are from Shannon 1951, *Bell System Technical Journal* 30(1),
  pp. 56 and 64. The guess-number entropy (1.42) is computed by `scene.py` from that record.
- Average over all two-letter contexts (2.81): Brown, `data.py` (`cond_entropy`).
- Language-model figure: Valmeekam et al. 2023, arXiv:2306.04050 (LLMZip), Table IV (a 1924 book
  released on Project Gutenberg in May 2023, after the model was trained).
- `facts.md` covers every claim.

## Beats

### 1. Cold open (0:00–0:10)
> You've read this English sentence up to one hidden character. With yes-or-no questions,
> how many do you need per character, on average? *[pause 1.5]*

Visual (the frame is centred vertically; everything is there from frame 1):
- A row of 12 dim purple boxes, labelled "already read" in purple, ending in a yellow **?** box (y ≈ 1.35). On "You've read", the real letters glint through at 9 % (too faint to read) and go dark again.
- The 27 candidate tiles (A–Z, ⎵) at y ≈ 0.15, with a grey "26 letters + space" label between them and the ? box.
- On "hidden", the ? box flags and a ripple runs along the tiles (the candidates for that slot).
- *questions per character* **?** arrives on "With" (≈ 0:04) at y ≈ −1.6. The question ends at ≈ 0:08; prediction hold 1.5 s.

### 2. Naive build: cut the alphabet in half (0:10–0:25)
> The natural answer is five. Each answer can cut what's left in half, and five cuts take
> twenty-seven down to one.

> With perfect fifty-fifty splits, the ideal is log base two of twenty-seven, about four point seven five.

Visual:
- "?" becomes "5". Yellow cuts split the tile row and the discarded halves dim.
- A chain 27 → 13 → 6 → 3 → 2 → 1 grows with one yellow arrow per cut. The kept group closes on Y.
- `log₂ 27 ≈ 4.75`, built in order: the label steps left so the finished line will be centred at x = 0 (the 5 waits in the answer's slot); "log₂" is written; the chain's 27 travels on a lane *below* the chain and above the label, then drops into its slot; "≈" is written and the 5 becomes 4.75.

### 3. Target and stakes (0:25–0:39)
> In 1951, Claude Shannon estimated the true figure at about one. Whatever it is, no text
> compressor can beat it on average, and guessing what comes next is how language models are
> trained.

Visual, in order:
1. The halving diagram and the "26 letters + space" label clear, the row rises to the top, and 4.75 steps right into the gutter at its own height.
2. The baseline grows; each tile drops onto it as the short foot of its column; then the vertical axis grows. The "questions" axis is short at first, running 0–6.5, at a tall scale so the chart fills the frame.
3. All 27 columns rise together to the same price while 4.75 rides up the gutter with their tops, and the yellow dashed line is born on the flat top.
4. A green band at 0.6–1.3 sits *behind* the bars, with thin edges. It is labelled ≈1 like an axis value, left of the y-axis. Citation: *Shannon, 1951 · Bell System Technical Journal*.
5. The band is flagged on "compressor".
6. On "guessing what comes next", the context boxes flash purple from left to right into the ? box.

### 4. Fail: measured, and why (0:39–0:53)
> So where do four of every five questions go? Splitting the alphabet evenly charges every
> character the same price. Z costs as much as E, yet in real text E turns up a hundred and thirty
> times as often.

Visual:
- A yellow outline with 45° yellow hatching (no fill, so the bars stay blue) covers the block above ≈1, with a yellow double arrow and the label **3.75 extra (79%)** above the chart.
- On "Splitting" the hatching goes and only the outline stays. The flat top is flagged on "same price".
- On "Z" the overlay goes, and E and Z are isolated (everything else, columns and letters, at 25–30 %).
- Every column then takes its real width (Brown Corpus); E and Z stay the only bright columns, and Z, now a hairline, keeps its own axis letter. "10.3%" and "0.08%" sit on short grey leaders above their own columns; on "thirty", a blue **×130** grows between them. The x-axis "share of text" appears. Heights do not change, because every character costs the same.

### 5. Insight (0:53–2:13)
> Instead, ask questions that split the probability, not the alphabet. Is it a space, E, T,
> A, or O? Those five make up nearly half of all text.

Columns re-sort by frequency without ever leaving a gap: each column pours from its old slot into its new one, the sorted block growing from the left (most frequent first) while the rest stays packed against it, so every frame tiles 0–100 %. The five get a white-outline flash. A yellow cut appears at 48 %. The band dims to 40 % until it is needed again.

> E starts near a tenth of the bar. Each ideal answer keeps half the probability, so E
> doubles its share of what's left. Three point three doublings, and E fills the whole bar.

The chart steps back: it rescales to a smaller unit and everything in it except E's column and E's letter (the strip's referent) dims to 30 %: columns, letters, % ticks, axis title, the yellow 4.75 line and its label, the band. In the clear band above its short axis, E's column is copied into a strip ("what's still possible"). One yellow cut dims the far half, and the kept half stretches: E doubles. A yellow counter runs to 3.3 as E fills the strip.

> Z starts at one in twelve hundred and sixty, and needs ten point three.

Z's sliver goes into a second strip; on "one in", a blue "1/1260" appears under the sliver, and it fades as the counter runs to 10.3.

> In general, a character with probability p needs k questions, where p times two to the k
> equals one. *[pause 1.5]* So two to the k equals one over p, and k equals log base two of
> one over p.

`p · 2ᵏ = 1` is built from E's column (p) and the counter (2ᵏ, with both counters flagged). On "one" the two full strips flash: 1 is the whole bar. The complete equation holds ≈ 2.7 s. Then two legal steps, each on its own words:
- "two to the k equals one over p": p drops under the 1 (`2ᵏ = 1/p`);
- "k equals log base two": k comes down from the exponent and the 2 becomes the base (`k = log₂(1/p)`), with k staying yellow;
- k flags together with the 3.3 and 10.3 counters.

> Now give each character its own cost as a height. Common characters sit wide and low,
> rare ones narrow and tall.

The strips leave, the chart returns to full strength, its axis title returns and the axis grows to 11. The yellow 4.75 line turns into a grey ghost. All 27 heights morph from 4.75 to log₂(1/p), forming a skyline. Space and E get the outline flash. On "rare", a thin grey box closes around the four hairlines at 100 %, dashed leaders run to a framed inset 0.43 units clear of the axis, and the inset shows X J Q Z at ×28 width (with small gaps, so their letters never crowd) and true heights on its own baseline; Z is labelled 10.3.

> The widths add up to one, so the total area is the average number of questions per
> character. Then pour the skyline flat, and its height is that average.

- A blue line sweeps the axis from 0 to 100 %.
- On "area" the columns flash and the formula is assembled from its referents: k becomes "average", the sweep becomes p, and Σ is written. The result is `average = Σ p log₂(1/p)`.
- On "pour", every column becomes a full-width slab of the same area. Stacked, the slabs reach 4.11.
- The yellow level line is born on that top.

> Shannon called that average the entropy, counted in bits, one bit per yes-or-no answer.
> For English letters, it's four point one one.

"average" becomes H, the axis title "questions" becomes "bits", and the level value is copied into `= 4.11 bits`.

> That beats four point seven five, but it's still four times Shannon's estimate: it prices
> every character as if nothing came before it.

The ghost line is flagged, then dims to 30 %. The band returns to full strength. The context row flashes purple.

### 6. Context (2:13–2:49)
> What comes after a Q? *[pause 1.3]*

The box before the ? becomes a purple **Q**. The equation's value turns into a yellow **?** (`H = … = ? bits`), and the 4.11 level stays as a 30 % grey reference. Prediction hold; the stack rises back into the plain skyline, top slab first.

> It's U, ninety-eight times out of a hundred. U swallows the bar, its cost drops to almost
> nothing, and the average falls to point one six bits. *[pause 0.45]*

- On "U", U widens to 98 % at its old height, and a blue **98%** brace widens *with* it (it spans U in every frame, readable by "ninety-eight", complete by "out of a hundred"). U gets the outline flash on "swallows". The x-axis title follows the context: "share" stays put, "of text" drops away and "after Q" arrives, with the purple Q flying over the row and down the right gutter (x ≈ 6.1), never across a column or tick label.
- On "its cost drops", U flattens to the floor.
- On "and the average", the brace and letters leave and the skyline pours into a thin slab. Everything left is a level under 4.2, so **the y-axis zooms to 0–5.5 during the pour** (ticks 0, 2, 4; the band and the 4.11 reference ride along).
- The level line is born at 0.16 on "falls", and the 0.16 is copied into the equation's ? slot as "one six" is spoken. It holds ≈ 2 s before the next context.

> After TH, E takes two thirds of the bar, and its cost shrinks to about half a question.

The context becomes T H (they fly to the axis title by the same gutter route), the 0.16 level leaves and the equation shows ? again. The stack rises into the TH-weighted skyline, and since costs up to 10.4 are back, the axis zooms back out to 0–11. E is 68 % wide, with a brace marked **68%** above its tallest state. E's cost re-prices to 0.55, and on "half" E gets a yellow outline (its height is the cost).

> Half a question sounds impossible, but a compressor asks about long runs of letters, and the
> fractions add up. Here they average one point seven.

- "Half a question sounds impossible": E flashes yellow.
- "long runs of letters": the ? box widens into a run of four ? boxes — one question about the whole run.
- "the fractions add up": the brace leaves and the TH skyline pours into stacked slabs (the fractions adding up), with the axis zooming back in to 0–5.5.
- "Here they average one point seven": the level is born at 1.67 and copied into the equation.

> Q and TH are the easy cases. Averaged over every two-letter context, it's still two point
> eight.

The T H boxes flash and the run closes back into the single ? box. A grey dashed level grows at 2.81 with "all two-letter contexts" above it, and 2.81 in the gutter (Brown, recomputed in `data.py`). On the zoomed axis the ladder reads 4.11 (no context) > 2.81 (two letters) > 1.67 (TH) > 0.16 (Q), with Shannon's band at ≈1. This is why Shannon needed long context.

### 7. Payoff (2:49–3:40)
> Shannon measured this with a person, who read a passage one character at a time, guessing
> each next one until right. Seventy-nine of a hundred and two came on the first guess.

A cross-fade to Shannon's own record (p. 56), THERE IS NO REVERSE ON A MOTORCYCLE … THE OTHER DAY:
- The whole passage fades in at 20 % while the chart leaves, centred vertically, so the frame is never empty.
- Each character sits in a fixed cell (pitch 0.32; the three two-digit counts get 0.44 cells, so "11 5" never reads as "115"), with its guess count centred under it. The 1s are grey and the rest yellow.
- The record is revealed at full strength under a moving cursor.
- A green tally counts first guesses to 79 / 102.

> A twin who guesses the same way could rebuild the passage from these counts alone. Treat
> each guess count as a symbol, and the same skyline pours flat at about one point four bits.
> A better guesser could only lower it.

On "twin", the letters fade to 12 % and only the counts remain (the tally leaves). On "rebuild", the letters come back left to right, written from the counts. On "counts alone" the letters step back to 30 %. On "Treat", the record steps up 1.2 units and the guess counts fly down into a small skyline: the width is the share of guesses (1st 77 %, 2nd 8 %, 3rd+ the tail; axis ticks 0 % and 100 %) and the height is log₂(1/share). It pours flat to a yellow level of 1.42, and a down arrow appears beside it on "lower".

> Shannon's tests, with a hundred letters of context, put English between point six and one
> point three bits per character.

A 0–5 "bits per character" line appears:
- markers for 4.75 and 2.81 (grey), 4.11 and 1.42 (yellow; the 1.42 flies in from the mini skyline);
- on "a hundred letters of context" the 2.81 marker (two letters of context) flags;
- a green band at 0.6–1.3, labelled under the line.

Citation: Shannon 1951.

> In twenty twenty-three, a language model compressing part of a new book in the same
> twenty-seven symbols needed point eight four bits, inside that range.

On "a language model" an INK "LLM" marker appears at the 4.75 end on a track above the other labels. Across "compressing a book…" it slides down the line, and on "point eight four" it drops onto the line, with 0.84 on the value row and "LLM" stacked above it, inside the band. Citation: *Valmeekam et al., 2023 · arXiv:2306.04050 (LLMZip), Table IV*. (0.84 is their result on a 100,000-token extract of a book released after the model was trained; their text8 figure, 0.71, is "likely optimistic" by their own account.)

### 8. Landing (3:40–3:56)
> The hidden character from the start is the Y at the end of the other day. Shannon's
> subject got it on the first guess, a single yes-or-no question. Splitting the alphabet took
> five. In English, almost no letter arrives without a past.

1. Everything fades except THE OTHER DAY.
2. That phrase flies into the cold-open row: THE OTHER DA becomes purple, and the Y goes into the ? box.
3. Only then do the boxes come in under it, and the 27 candidate tiles (Y highlighted) return below: frame one, re-seen.
4. "1 guess" appears in green.
5. On "a single yes-or-no question", the 27→1 chain and "5 questions" return to their cold-open places.
6. On "five", "5 questions" and the chain flag.
7. On "In English", these dim while the purple context flashes.
8. No end card: the re-seen cold-open frame holds to the end.

## Sources
- C. E. Shannon, "Prediction and Entropy of Printed English", *Bell System Technical Journal*
  30(1): 50–64, 1951.
- W. N. Francis & H. Kučera, *Brown Corpus*, Brown University, 1964 (NLTK distribution).
- C. S. K. Valmeekam, K. Narayanan, D. Kalathil, J.-F. Chamberland, S. Shakkottai, "LLMZip:
  Lossless Text Compression using Large Language Models", arXiv:2306.04050, 2023 (Table IV;
  ref. [7]: J. F. Dobie, *Legends of Texas*, 1924, Project Gutenberg ebook 70859, 25 May 2023).
