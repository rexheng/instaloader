# Episode 7: How Much Information Is in a Letter?

**Idea (one sentence):** A character costs log₂(1/p) yes-or-no questions, so its information
depends on how predictable it is, not on how many letters exist. Averaged over English, and
using what came before, that is about one bit per character, not the 4.75 that halving the
alphabet suggests.

Runtime target is about 3:57 (~605 words). Voice af_heart, speed 0.84.

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | probability: candidate tiles, column widths, every `p` (including the p inside 1/p), the E/Z share strips, the % braces, "×130", "1/1260" |
| YELLOW | questions (= bits): the "?" box (and the run box), halving cuts and arrows, the "3.75 extra" overlay and every later "N extra" gap meter, doubling counters, `2^k`, `k`, `log₂(1/p)`, `log₂(1/q)`, `H`, every Σ p log₂(1/p) level (4.11, 0.16, 1.67, 2.81, 1.42; dimmed to 30 % when only a reference), the run's letter costs and total, E's outline at "half a question", guess counts above 1 |
| GREEN | Shannon's measurements: the ≈1 band (0.6–1.3), the first-guess tally, "1 guess" |
| PURPLE | context, the characters already read: the dim "already read" row, Q, TH, THE OTHER DA |
| GRAY | axes, ticks, titles, citations, leaders, the inset frame, the context counter, the abandoned 4.75 (the only grey level), first-guess "1"s, the LLM book note |
| INK | letters, labels, the language-model tag and marker ("LLM") |

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
- The run E R E ␣ after T H (0.5 + 3.0 + 2.6 + 1.6 = 7.7 → 8) and the context counts: Brown, `data.py`.
- `facts.md` covers every claim.

## Beats

### 1. Cold open (0:00–0:10)
> You've read an English sentence up to one hidden character. With yes-or-no questions,
> how many do you need per character, on average? *[pause 1.5]*

Visual (the frame is centred vertically; everything is there from frame 1):
- A row of 12 dim purple boxes, labelled "already read" in purple, ending in a yellow **?** box (y ≈ 1.35). On "You've read", the real letters glint through at 9 % (too faint to read) and go dark again.
- The 27 candidate tiles (A–Z, ⎵) at y ≈ 0.15, with a grey "26 letters + space" label between them and the ? box.
- On "hidden", the ? box flags and a ripple runs along the tiles (the candidates for that slot).
- *questions per character* **?** arrives on "With" (≈ 0:04) at y ≈ −1.6. Prediction hold 1.5 s.

### 2. Naive build: cut the alphabet in half (0:10–0:24)
> The natural answer is five. Each answer can cut what's left in half, and five cuts take
> twenty-seven down to one. The ideal is log base two of twenty-seven, about four point seven five.

Visual:
- "?" becomes "5". Yellow cuts split the tile row and the discarded halves dim; a chain 27 → 13 → 6 → 3 → 2 → 1 grows with one yellow arrow per cut, and the kept group closes on Y.
- `log₂ 27 ≈ 4.75` is built in place: the label steps left, "log₂" is written, the chain's 27 travels on a lane below the chain into its slot, "≈" is written and the 5 becomes 4.75.

### 3. Target and stakes (0:24–0:38)
> In 1951, Claude Shannon estimated the true figure at about one. Whatever it is, no text
> compressor can beat it on average, and guessing what comes next is how language models are
> trained.

Visual: the halving diagram clears, the row rises to the top, the tiles drop onto a baseline as the feet of 27 columns, the axis grows, and every column rises to the same price (yellow dashed line, 4.75 in the gutter). A green band at 0.6–1.3 sits behind the bars, labelled ≈1 left of the axis, centred on the band. Citation: *Shannon, 1951 · Bell System Technical Journal*. On "guessing what comes next" the context boxes flash purple left to right; on "language models" an INK **LLM** tag with an arrow points into the ? box (the same tag returns at the payoff), and it leaves with the next beat.

### 4. Fail: measured, and why (0:38–0:52)
> So where do four of every five questions go? Splitting the alphabet evenly charges every
> character the same price. Z costs as much as E, yet E turns up a hundred and thirty times as
> often.

Visual: yellow outline + hatching over the block above ≈1, double arrow, **3.75 extra (79%)**. Then E and Z are isolated, every column takes its real (Brown) width at the same height, "10.3%" and "0.08%" sit on grey leaders, and a blue **×130** grows between them.

### 5. Insight (0:52–2:08)
> Instead, ask questions that split the probability, not the alphabet. Is it a space, E, T,
> A, or O? Those five make up nearly half of all text.

Gap-free re-sort by frequency; the five get a white-outline flash; a yellow cut and blue brace at 48 %.

> E starts near a tenth of the bar. Each ideal answer keeps half the probability, so E
> doubles its share of what's left. Three point three ideal doublings, and E fills the whole bar.
> Z starts at one in twelve hundred and sixty, and needs ten point three.

The doubling strips (keep): the chart steps back to 30 % except E; E's column is copied into a strip, one cut, the kept half stretches, a yellow counter runs to 3.3; then Z's sliver ("1/1260") runs to 10.3.

> In general, a character with probability p needs k questions, where p times two to the k
> equals one. *[pause 1.5]* So two to the k equals one over p, and k equals log base two of
> one over p.

On "In general" the strips step up 0.65 and dim to 40 % (their headers leave; the 3.3 and 10.3 counters stay bright), so the equation is built **centre stage** at font 56 (its "=" at x ≈ 0.2, y ≈ 0.75): p is copied from E's column, 2ᵏ from the counter, "= 1" flashes both full strips. It holds ≈ 2.7 s, then two legal steps on their own words (`2ᵏ = 1/p`, then `k = log₂(1/p)`), and k flags with both counters.

> Now give each character its own cost as a height.

The strips leave, the chart returns to full strength, `k = log₂(1/p)` is carried up to the formula row, the 4.75 line turns into a grey ghost, and all 27 heights morph to log₂(1/p).

> The widths add up to one, so the total area is the average number of questions per
> character. Pour the skyline flat, and its height is that average.

As the blue sweep adds the widths up, the ×28 inset of X J Q Z (Z = 10.3) opens beside the four hairlines; on "area" the formula is assembled from its referents (`average = Σ p log₂(1/p)`, "k" → "average" as a cross-fade); on "Pour" the skyline pours flat (keep) and the level is born at 4.11.

> Shannon called that average the entropy, counted in bits, one bit per yes-or-no answer.
> For English letters, it's *[pause 0.3]* four point one one.

"average" cross-fades into H; the axis title "questions" steps out and "bits" steps in; the level value is copied into `= 4.11 bits`.

> That beats four point seven five, but it's still four times Shannon's estimate: it prices
> every character as if nothing came before it.

The failure metric comes back as a live meter: a yellow double arrow from ≈1 up to the ghost 4.75 with **3.75 extra**, the band back at full strength; it shrinks to 4.11 as the number counts to **3.11 extra** and the ghost fades out. On "prices every character" the meter leaves and the stack rises back into the skyline (each character priced on its own); on "came before it" the context row flashes purple.

### 6. Context (2:08–2:58)
> What comes after a Q? *[pause 1.6]*

Only the question changes: the box before the ? becomes a purple **Q**, the equation's value becomes a yellow **?**, the 4.11 level dims to a 30 % reference. Then a static frame for the prediction.

> It's U, ninety-eight times out of a hundred. U swallows the bar, its cost drops to almost
> nothing, and the average falls to point one six bits. *[pause 0.45]*

- On "It's U": U gets the outline flash, the x-axis title becomes "share after Q" (the Q flies down the right gutter), and a blue **98%** appears over U.
- On "swallows the bar": U widens to 98 % **while** its height falls (heights interpolate geometrically, so the drawn area only shrinks); a blue brace at a fixed height grows with it and the 98% rides at its centre.
- "its cost drops to almost nothing": the flattened U flashes. "and the average": the skyline pours, the axis zooms to 0–5.5 (the old ticks are gone before the new ones fade in), the level is born at 0.16 and copied into the slot on "one six".

> After TH, E takes two thirds of the bar, and its cost shrinks to about half a question.

T H fly to the title; the stack rises into the TH-weighted skyline (axis zooms out); on "two thirds" the **68%** brace appears and E is re-priced at once, dropping to 0.55; on "half" E gets a yellow outline.

> Half a question, like three point three doublings, sounds impossible, but a compressor asks
> about long runs of letters, and the fractions add up. After TH, the average is one point seven.

- E flashes yellow.
- "long runs of letters": the ? box widens into a run of four holding a real run from Shannon's passage, **E R E ␣** (THERE, after T H), and each letter's cost given the two before it appears under it in yellow: **0.5, 3.0, 2.6, 1.6** (Brown, `data.py`).
- "the fractions add up": the four costs flow into one total, **7.7 → 8 questions** (for four letters).
- "After TH, the average…": the TH skyline pours (axis zooms in) and the level is born at 1.67 and copied into the equation.

> But averaged over every two-letter context, it's still two point eight.

The run closes back into the ? box, the TH stack dims to 30 % and its 1.67 gets a purple **TH** tag, the 4.11 reference rises to 60 %. A yellow dashed level grows at 2.81 ("all two-letter contexts", 2.81 in the gutter), and the gap meter returns at 4.11 (3.11 extra) and shrinks to 2.81 (**1.81 extra**) while 2.81 is copied into the equation.

### 7. Payoff (2:58–3:53)
> Long contexts need more text than any corpus holds, so Shannon used a predictor that already
> knows English: a person.

On "need" the equation steps out and, in its place, grey: **possible contexts: 27² = 729 → 27¹⁰⁰ ≈ 10¹⁴³**, then **Brown Corpus: 5.75 M characters** (the Brown citation flags). The chart fades out completely; then Shannon's record fades in at 15 % on "a person".

> His subject read a passage letter by letter, guessing each next one until right.
> Seventy-nine of a hundred and two came on the first guess.

Shannon's own record (p. 56), glyphs 12 % larger (pitch 0.33, two-digit counts in 0.45 cells), revealed under a moving cursor (unread lines at 15 %); the 1s are grey and the rest yellow; a green tally counts first guesses to 79 / 102.

> A twin who guesses the same way could rebuild the passage from these counts alone. Treat
> each guess count as a symbol, and the same skyline pours flat at about one point four bits.
> A better guesser could only lower it.

Twin: letters fade to 12 % and return left to right. The record steps up; the counts fly down into the guess skyline (width = share of guesses, height = log₂(1/share)); beside the 2nd-guess column, yellow **log₂(1/q) = 3.67**. It pours flat; the small axis zooms to 0–2.1 with Shannon's ≈1 band; the level is labelled **≤ 1.42**; on "better guesser" a yellow double arrow measures **0.42 extra**; on "lower" a down arrow.

> Shannon's tests, with a hundred letters of context, put English between point six and one
> point three bits per character.

A 0–5 "bits per character" line: 4.75 (grey), 4.11, 2.81 and 1.42 (all yellow; 1.42 flies in from the mini skyline); 2.81 flags on "a hundred letters of context"; the green 0.6–1.3 band. Citation: Shannon 1951.

> In twenty twenty-three, a language model compressing part of a book that reached Project
> Gutenberg after its training, in the same twenty-seven symbols, needed point eight four bits,
> inside that range.

The Shannon citation fades out completely, then *Valmeekam et al., 2023 · arXiv:2306.04050 (LLMZip), Table IV* fades in. On "a language model" the INK **LLM** marker is born from the 1.42 (human guesser) triangle and waits on a track above it; on "book" a grey note **1924 book · on Gutenberg May 2023** appears beside it; on "needed point eight four" it moves only 1.42 → 0.84, into the band, with 0.84 on the value row.

### 8. Landing (3:53–4:00)
> The hidden character from the start is the Y at the end of the other day. Shannon's
> subject got it on the first guess, a single yes-or-no question. Splitting the alphabet took
> five. In English, almost no letter arrives without a past.

1. As the record fades, the cold-open row (12 boxes, the ? box) fades in at 30 % in its old place, and THE OTHER DAY comes to full strength.
2. THE OTHER DA flies straight into its boxes and the Y drops into the ? box on the spoken "Y".
3. The boxes come to full strength and the 27 candidate tiles (Y highlighted) return: frame one, re-seen.
4. "1 guess" in green; on "a single yes-or-no question" the 27→1 chain and "5 questions" return; they flag on "five" and dim on "In English" while the context flashes. The frame holds to the end.

## Sources
- C. E. Shannon, "Prediction and Entropy of Printed English", *Bell System Technical Journal*
  30(1): 50–64, 1951.
- W. N. Francis & H. Kučera, *Brown Corpus*, Brown University, 1964 (NLTK distribution).
- C. S. K. Valmeekam, K. Narayanan, D. Kalathil, J.-F. Chamberland, S. Shakkottai, "LLMZip:
  Lossless Text Compression using Large Language Models", arXiv:2306.04050, 2023 (Table IV;
  ref. [7]: J. F. Dobie, *Legends of Texas*, 1924, Project Gutenberg ebook 70859, 25 May 2023).
