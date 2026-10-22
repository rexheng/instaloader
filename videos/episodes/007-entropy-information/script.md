# Episode 7: How Much Information Is in a Letter?

**Idea (one sentence):** A character costs log₂(1/p) yes-or-no questions, so its information
depends on how predictable it is, not on how many letters exist. Averaged over English, and
using what came before, that is about one bit per character, not the 4.75 that halving the
alphabet suggests.

Runtime target is about 3:30 (≤ 500 words, PRODUCTION_GUIDE §13). Voice af_heart, speed 0.83, shaped cadence.

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | probability: candidate tiles, column widths, every `p` (including the p inside 1/p), the E/Z share strips, the % braces, "×130", "1/1260" |
| YELLOW | questions (= bits): the "?" box (and the run box), halving cuts and arrows, the "3.75 extra" overlay and every later "N extra" gap meter, doubling counters, `2^k`, `k`, `log₂(1/p)`, `log₂(1/q)`, `H`, every Σ p log₂(1/p) level (4.11, 0.16, 1.67, 2.81, 1.42; dimmed to 30 % when only a reference), the run's letter costs and total, E's outline at "half a question", guess counts above 1 |
| GREEN | Shannon's measurements: the ≈1 band (0.6–1.3), the first-guess tally, "1 guess" |
| PURPLE | context, the characters already read: the dim "already read" row, Q, TH, THE OTHER DA |
| GRAY | axes, ticks, titles, citations, leaders, the inset frame, the context counter, the abandoned 4.75 (the only grey level), the landing's resting "5 questions" (the abandoned halving count), the "one at a time" row of the run's bill, first-guess "1"s, the payoff tags, "upper estimate", the LLM book note |
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
- The run E ␣ O after T H (0.5 + 0.6 + 3.8 = 4.9 → 5; one at a time 1 + 1 + 4 = 6) and the context counts: Brown, `data.py` (`run_after_TH`).
- `facts.md` covers every claim.

## Beats

### 1. Cold open (0:00–0:10)
> You've read an English sentence up to one hidden character. With yes-or-no questions,
> how many do you need, on average? *[pause 1.5]*

Visual (the frame is centred vertically; everything is there from frame 1):
- A row of 12 dim purple boxes, labelled "already read" in purple, ending in a yellow **?** box (y ≈ 1.35). On "You've read", the real letters glint through at 9 % (too faint to read) and go dark again.
- The 27 candidate tiles (A–Z, ⎵) at y ≈ 0.15, with a grey "26 letters + space" label between them and the ? box.
- On "hidden", the ? box flags and a ripple runs along the tiles (the candidates for that slot).
- *questions per character* **?** arrives on "With" (≈ 0:04) at y ≈ −1.6. Prediction hold 1.5 s.

### 2. Naive build: cut the alphabet in half (0:10–0:24)
> The natural answer is five: each answer halves what's left, and five cuts take
> twenty-seven to one. The ideal is log base two of twenty-seven: four point seven five.

Visual:
- "?" becomes "5". Yellow cuts split the tile row and the discarded halves dim; a chain 27 → 13 → 6 → 3 → 2 → 1 grows with one yellow arrow per cut, and the kept group closes on Y.
- `log₂ 27 ≈ 4.75` is built in place: the label steps left, "log₂" is written, the chain's 27 travels on a lane below the chain into its slot, "≈" is written and the 5 becomes 4.75.

### 3. Target and stakes (0:24–0:38)
> In 1951, Claude Shannon put the true figure at about one. No compressor beats it on
> average, and guessing what comes next is how language models are trained.

Visual: the halving diagram clears, the row rises to the top, the tiles drop onto a baseline as the feet of 27 columns, the axis grows, and every column rises to the same price (yellow dashed line); the 4.75 climbs the gutter behind the column tops and settles on the line as the bars reach it. A green band at 0.6–1.3 sits behind the bars, labelled ≈1 left of the axis, centred on the band. Citation: *Shannon, 1951 · Bell System Technical Journal*. On "guessing what comes next" the context boxes flash purple left to right; on "language models" an INK **LLM** tag with an arrow points into the ? box (the same tag returns at the payoff), and it leaves with the next beat.

### 4. Fail: measured, and why (0:38–0:52)
> So where do four of every five questions go? Z costs as much as E, yet E turns up a
> hundred thirty times as often.

Visual: yellow outline + hatching over the block above ≈1, double arrow, **3.75 extra (79%)**. On "Z" the hatching goes and E and Z are isolated; on "as much as E" E and the one price line flash together; every column takes its real (Brown) width at the same height, "10.3%" and "0.08%" sit on grey leaders, and a blue **×130** grows between them.

### 5. Insight (0:52–2:08)
> Instead, split the probability, not the alphabet: is it a space, E, T, A or O? That's
> nearly half.

Gap-free re-sort by frequency; the five get a white-outline flash; a yellow cut and blue brace at 48 %.

> E starts near a tenth. Each ideal answer keeps half the probability, so E's share doubles.
> Three point three doublings fill the bar. Z, one in twelve hundred sixty, needs ten point three.

The doubling strips (keep): the chart steps back to 30 % except E; E's column is copied into a strip, one cut, the kept half stretches, a yellow counter runs to 3.3; then Z's sliver ("1/1260") runs to 10.3.

> A character with probability p needs k questions, where p times two to the k equals one.
> *[pause 1.5]* So two to the k equals one over p, and k equals log base two of one over p.

On "In general" the strips step up 0.65 and dim to 40 % (their headers leave; the 3.3 and 10.3 counters stay bright), so the equation is built **centre stage** at font 56 (its "=" at x ≈ 0.2, y ≈ 0.75): p is copied from E's column, 2ᵏ from the counter, "= 1" flashes both full strips. It holds ≈ 2.7 s, then two legal steps on their own words (`2ᵏ = 1/p`, then `k = log₂(1/p)`), and k flags with both counters.

> Now make each character's cost its height.

The strips leave, the chart returns to full strength, `k = log₂(1/p)` is carried up to the formula row, the 4.75 line turns into a grey ghost, and all 27 heights morph to log₂(1/p).

> The widths add to one, so the area is the average cost. Pour the skyline flat, and its
> height is that average.

As the blue sweep adds the widths up, the ×28 inset of X J Q Z (Z = 10.3) opens beside the four hairlines; on "area" the formula is assembled from its referents (`average = Σ p log₂(1/p)`: the blue sweep line contracts into the p, the log comes from k, "k" → "average" as a cross-fade); on "Pour" the skyline pours flat (keep) and the level is born at 4.11.

> Shannon called it entropy, in bits: one bit per yes-or-no answer. For English letters: four
> point one one. *[pause 0.9]*

"average" cross-fades into H; the axis title "questions" steps out and "bits" steps in; the level value is copied into `= 4.11 bits`.

> That beats four point seven five, but it's four times Shannon's estimate: it ignores what
> came before.

The failure metric comes back as a live meter: a yellow double arrow grows from ≈1 up to the ghost 4.75, its reading riding on its top and counting up to **3.75 extra** (hidden while it is still inside the poured stack), the band back at full strength; it stands while "four point seven five" is spoken, then shrinks to 4.11 as the number counts to **3.11 extra** and the ghost fades out. On "prices every character" the meter leaves and the stack rises back into the skyline (each character priced on its own); on "came before it" the context row flashes purple.

### 6. Context (2:08–2:58)
> What comes after a Q? *[pause 1.6]*

Only the question changes: the box before the ? becomes a purple **Q**, the equation's value becomes a yellow **?**, the 4.11 level dims to a 30 % reference. Then a static frame for the prediction.

> It's U, ninety-eight percent of the time. U swallows the bar, and the average falls to
> point one six bits. *[pause 0.9]*

- On "It's U": U gets the outline flash, the x-axis title becomes "share after Q" (the Q flies down the right gutter), and a blue **98%** appears over U.
- On "swallows the bar": U widens to 98 % **while** its height falls (heights interpolate geometrically, so the drawn area only shrinks); a blue brace at a fixed height grows with it and the 98% rides at its centre.
- "and the average": the skyline pours (the 98 % brace leaves in its first 0.3 s), the axis zooms to 0–5.5 (the old ticks are gone before the new ones fade in), the level is born at 0.16 and copied into the slot on "one six".

> After TH, E takes two thirds of the bar, and costs about half a question.

T H fly to the title; the stack rises into the TH-weighted skyline (axis zooms out); on "two thirds" the **68%** brace appears and E is re-priced at once, dropping to 0.55; on "half" E gets a yellow outline.

> Half a question sounds impossible, but a compressor asks about long runs of letters, and the
> fractions add up: five questions for these three, not six. After TH, it averages one point seven.

- E flashes yellow; the ? box flags on "impossible".
- "asks about long runs of letters": the ? box widens into a run of three holding a real run from Shannon's passage, **E ␣ O** (THE OTHER, after T H); the after-TH skyline leaves the chart (0 %: it prices only the first letter) and the 68 % brace leaves. Over the empty chart the run's bill is laid out one column per letter: the letter (flashing in the row as its copy appears), a tag naming its two-letter context (**after TH**, **after HE**, **after E␣**: grey "after", purple letters), and its cost given those two letters, in yellow MathTex 36: **0.5, 0.6, 3.8**. As each column appears, a purple bracket under the context row slides one box to the right, over that letter's two-letter window, and the window flashes purple.
- "the fractions add up": the sum is built left to right, each cost pulsing as the "+" after it is written; "= 4.9" arrives once every term is in, then **→ 5 questions** on "five questions".
- "these three, not six": under each cost, as it pulses, its whole-question count drops in: grey **1 + 1 + 4 = 6 · one at a time**, with 6 under 5; 5 flags.
- "After TH": the chart returns to full strength and the TH skyline pours (the bill stays); on "the average" the level is born at 1.67, the bill and run box step back to 30 %, and 1.67 is copied into the equation.

> But averaged over every two-letter context, it's still two point eight.

The run closes back into the ? box and the bill leaves; the TH stack dims to 26 % while the axis zooms in to 0–5.5, its 1.67 gets a purple **TH** tag, the 4.11 reference rises to 60 %. The gap meter grows from ≈1 to 4.11, its reading counting up to 3.11 with the arrow (hidden until it clears the TH stack); a yellow dashed level grows at 2.81 ("all two-letter contexts", 2.81 in the gutter), and the meter shrinks to 2.81 (**1.81 extra**) while 2.81 is copied into the equation (the copy leaves the gutter to the right and rises outside the 4.11 label).

### 7. Payoff (2:58–3:53)
> Hundred-letter contexts need more text than any corpus holds, so Shannon used a predictor
> that knows English: a person.

On "need" the equation steps out and, in its place, grey: **possible contexts: 27² = 729 → 27¹⁰⁰ ≈ 10¹⁴³** (the gap meter and "all two-letter contexts" leave as it is written, so the arithmetic is the one focal point), then **Brown Corpus: 5.75 M characters** (the Brown citation flags). The chart fades out completely (0.5 s), and T H leave with it (the row is blank again, as in the cold open); Shannon's passage fades straight in at 40 % on "already knows English" (letters only: no guess exists yet), so no frame is empty. On "a person" a yellow reading cursor locks onto its first letter while the text-so-far row flashes purple.

> His subject read a passage letter by letter, guessing each next one until right:
> seventy-nine of a hundred two on the first guess. *[pause 0.9]*

Shannon's own record (p. 56), glyphs 12 % larger (pitch 0.33, two-digit counts in 0.45 cells), revealed under a moving cursor: the unread letters step back to 15 % as it starts, and each guess count appears only as the cursor passes its letter; the 1s are grey and the rest yellow; a green tally counts first guesses to 79 / 102. The context row reads along: its 12 boxes hold the last 12 symbols read (purple), and the ? box is the symbol being guessed.

> A twin guessing the same way could rebuild the passage from these counts. Treat each
> count as a symbol: *[pause 1.2]* the same skyline pours flat at about one point four bits.
>
> A better guesser could only lower it. *(its own beat, speed 0.80)*

Twin: letters fade to 12 % and return left to right. Then the letters and the context row leave (the record returns for the landing), the three rows of counts close up at the top of the frame (in order, none crossing another), and the guess chart's baseline is drawn below them, centred and full width (x −4.6 to 3.4). On "Treat" the counts are sorted into their columns one row at a time, bottom row first, so no count ever passes over one still at rest: each drops straight down to its group's lane (1s lowest, 2s above, each 3+ count its own lane), runs along it to its column, and drops straight into the column's foot, which widens as its counts land (width = share of guesses). Then every column rises to its cost (height = log₂(1/share)) as the vertical axis grows, as the letter columns did at 0:24. Only then do "bits", "share of guesses" and 1st/2nd/3rd+ appear (each label ≥ 0.25 clear of the next), and yellow **log₂(1/q) = 3.67** is written over the low 1st column on a grey leader to the 2nd-guess column, which flashes white-edged, brighter blue. It pours flat, and the label leaves with the columns it describes; the axis zooms to 0–2.1 (the chart now fills the lower two-thirds) and Shannon's ≈1 band is drawn over the stack; the level is labelled **≈ 1.42**, with grey **one passage, context 0–101** under it. On "better guesser" the yellow gap meter grows from ≈1 to the level, counting **0.42 extra**; on "lower" a down arrow and a grey **upper estimate**.

> With a hundred letters of context, Shannon's tests put English between point six and one
> point three bits.

The guess skyline leaves. A 0–5 "bits per character" line across the middle of the frame (y ≈ 0.25, 12 units wide): 4.75 (grey), 4.11, 2.81 and 1.42 (all yellow; 1.42 flies in from the guess chart, over the top of the frame), each with a grey tag under the axis: **halving**, **no context**, **2-letter context**, **person** (with **102 letters** under it); 2.81 flags on "a hundred letters of context"; the green 0.6–1.3 band, its label in the tag row. Citation: Shannon 1951.

> In twenty twenty-three, a language model compressed part of a book *[pause 0.3]* posted to
> Project Gutenberg after the model was trained. *[pause 0.4]* It needed point eight four bits,
> inside that range. *[pause 0.3]*

The Shannon citation fades out completely, then *Valmeekam et al., 2023 · arXiv:2306.04050 (LLMZip), Table IV* fades in. On "a language model" the INK **LLM** marker is born from the 1.42 (person) triangle and waits on a track above it; on "book", "Gutenberg" and "trained" a grey note **1924 book · on Gutenberg May 2023 · 27 symbols** (Text 26) builds above its name; on "needed" the marker, name and note slide left together (nothing crosses), and on "point eight four" the marker drops onto 0.84, into the band, with 0.84 on the value row.

### 8. Landing (3:53–4:00)
> The hidden character from the start *[pause 0.4]* is the Y in the other day. *(its own beat, speed 0.80)*
>
> Shannon's subject needed one guess: *[pause 0.3]* is it Y? Splitting the alphabet took five.
> In English, almost no letter arrives without a past.

0. The bits-per-character line fades over about 0.65 s; the person's 1.42 marker (and its tags) stays about 0.4 s longer and fades last, and only then Shannon's record comes back in its reading position (letters at 22 %), with THE OTHER DAY at full strength.
1. As the record fades, the cold-open row (12 boxes, the ? box) fades in at 30 % in its old place.
2. THE OTHER DA steps under its boxes (the Y under the ? box) as the record goes, then rises straight into them; the Y lands in the ? box on the spoken "Y".
3. The boxes come to full strength and the 27 candidate tiles (Y highlighted) return, with the 27→1 chain and a grey "5 questions" faint under them: frame one (as at 0:17), re-seen.
4. "1 guess" in green on "one guess"; on "is it Y" the ? box with its Y flags yellow; on "Splitting" the chain and "5 questions" come to full strength (yellow) and flag on "five", and step back (chain 30 %, "5 questions" grey) on "In English" while the context flashes. The frame holds to the end.

## Sources
- C. E. Shannon, "Prediction and Entropy of Printed English", *Bell System Technical Journal*
  30(1): 50–64, 1951.
- W. N. Francis & H. Kučera, *Brown Corpus*, Brown University, 1964 (NLTK distribution).
- C. S. K. Valmeekam, K. Narayanan, D. Kalathil, J.-F. Chamberland, S. Shakkottai, "LLMZip:
  Lossless Text Compression using Large Language Models", arXiv:2306.04050, 2023 (Table IV;
  ref. [7]: J. F. Dobie, *Legends of Texas*, 1924, Project Gutenberg ebook 70859, 25 May 2023).
