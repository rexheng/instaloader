# Episode 7: How Much Information Is in a Letter?

**Idea (one sentence):** A character costs log₂(1/p) yes-or-no questions, so its information
depends on how predictable it is, not on how many letters exist. Averaged over English, and
using what came before, that is about one bit per character, not the 4.75 that halving the
alphabet suggests.

Runtime target is about 3:30 (≤ 500 words, PRODUCTION_GUIDE §13). Voice af_heart, speed 0.83, shaped cadence; the crux beat ("The widths add to one…") at 0.80. Beat gap 0.38 s; the four act turns (no context → context, two-letter → a person, the guess chart → the payoff line, the payoff → the landing) get 0.8 s, about twice an ordinary beat boundary.

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | probability: candidate tiles, column widths, every `p` (including the p inside 1/p), the E/Z share strips, the % braces, "×130", "1/1260", the run's probabilities (0.683 × 0.670 × 0.072 = 0.0329) |
| YELLOW | questions (= bits): the "?" box (and the run box), halving cuts and arrows, the "3.75 extra" overlay and every later "N extra" gap meter, doubling counters, `2^k`, `k`, `log₂(1/p)`, `log₂(1/q)`, `H`, every Σ p log₂(1/p) level (4.11, 0.16, 1.67, 2.81, 1.42; dimmed to 30 % when only a reference), the run's letter costs and total, E's outline at "half a question", guess counts above 1, the ghost of the price line that stops at the floor (80 %) |
| GREEN | Shannon's measurements: the ≈1 band (0.6–1.3), the first-guess tally, "1 guess" |
| PURPLE | context, the characters already read: the dim "already read" row, Q, TH, THE OTHER DA |
| GRAY | axes, ticks, titles, citations, leaders, the inset frame, the context counter, the abandoned 4.75 (the only grey level), the landing's resting "5 questions" (the abandoned halving count), the "one at a time" row of the run's bill, first-guess "1"s, the payoff tags, "upper estimate", the LLM book note, the "floor" tag, the waiting LLM marker's "?" |
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

Visual: the halving diagram clears while, in the same move, the baseline fades in at its full width (round 10: never a centred stub beside a lone 4.75) and all 27 tiles return to full strength (each will be priced); the row rises to the top, the tiles drop onto the baseline as the feet of 27 columns, the axis grows, and every column rises to the same price (yellow dashed line); the 4.75 climbs the gutter behind the column tops and settles on the line as the bars reach it. A green band at 0.6–1.3 sits behind the bars, labelled ≈1 left of the axis, centred on the band. Citation: *Shannon, 1951 · Bell System Technical Journal*. On "No compressor beats it" a ghost of the price line (80 %) is pushed down from 4.75 and stops at ≈1, where a grey **floor** appears in the right gutter and the band flashes; both leave on "guessing" (about 2.5 s on screen). On "guessing what comes next" the context boxes flash purple left to right; on "language models" an INK **LLM** tag with an arrow points into the ? box (the same tag returns at the payoff), and it leaves with the next beat.

### 4. Fail: measured, and why (0:38–0:52)
> So where do four of every five questions go? Z costs as much as E, yet E turns up a
> hundred thirty times as often.

Visual: yellow outline + hatching over the block above ≈1, double arrow, **3.75 extra (79%)**. On "Z" the hatching goes and E and Z are isolated; on "as much as E" E and the one price line flash together; every column takes its real (Brown) width at the same height, "10.3%" and "0.08%" sit on grey leaders, and a blue **×130** grows between them.

### 5. Insight (0:52–2:08)
> Split the probability, not the alphabet: is it a space, E, T, A or O? That's
> nearly half.

Gap-free re-sort by frequency; the five get a white-outline flash; a yellow cut and blue brace at 48 %.

> E starts near a tenth. Each ideal answer keeps half the probability, so E doubles its share.
> Three point three doublings fill the bar. Z, one in every twelve hundred sixty, needs ten point three.

*(Round 10: "E's share" was heard as "ease share", and the "in" of "one in twelve hundred" was swallowed.)*

The doubling strips (keep): the chart steps back to 30 % except E; E's column is copied into a strip, one cut, the kept half stretches, a yellow counter runs to 3.3; then Z's sliver ("1/1260", in with the strip) runs to 10.3: its count starts on "twelve" and lands on 10.3 as "ten point three" begins; "1/1260" steps back to 40 % once the counter passes 1.

> A character with probability p needs k questions, where p times two to the k equals one.
> *[pause 1.5]* So two to the k equals one over p, and k equals log base two of one over p.

On "In general" the strips step up 0.65 and dim to 40 % (their headers leave; the 3.3 and 10.3 counters stay bright), so the equation is built **centre stage** at font 56 (its "=" at x ≈ 0.2, y ≈ 0.75): p is copied from E's column, 2ᵏ from the counter, "= 1" flashes both full strips. It holds ≈ 2.7 s, then two legal steps on their own words (`2ᵏ = 1/p`, then `k = log₂(1/p)`: in three moves (round 10): the 2 steps down and left out of the exponent's base, shrinking to subscript size, while the fraction slides right; only once the 2 is well clear does k drop out of the exponent into its place; then the 2 runs right along a lane 0.38 below the baseline (passing under the k at speed, in about 0.1 s) and rises into the base's subscript. So k is never stacked over a resting 2 (no "k/2" frame) and never stands beside it on the baseline (no "2k" frame); "log" is written 0.3 s after the 2 lands), and k flags with both counters.

> Make each character's cost its height.

The strips leave, the chart returns to full strength, `k = log₂(1/p)` is carried up to the formula row, the 4.75 line turns into a grey ghost, and all 27 heights morph to log₂(1/p).

> The widths add to one, *[pause 0.25]* so the area is the average cost. *[pause 0.5]* Pour the
> skyline flat, and its height is that average. *(speed 0.80: the crux breathes)*

As the blue sweep adds the widths up, the ×28 inset of X J Q Z (Z = 10.3) opens beside the four hairlines; on "area" the formula is assembled from its referents (`average = Σ p log₂(1/p)`: the blue sweep line contracts into the p, the log comes from k, "k" → "average" as a cross-fade); on "Pour" the skyline pours flat (keep) and the level is born at 4.11.

> Shannon called it entropy, in bits: one bit per yes-or-no answer. For English letters: four
> point one one. *[pause 0.9]*

"average" cross-fades into H; the axis title "questions" steps out and "bits" steps in; the level value is copied into `= 4.11 bits`.

> That beats four point seven five, but it's four times Shannon's estimate: it ignores what
> came before.

The failure metric comes back as a live meter: a yellow double arrow grows from ≈1 up to the ghost 4.75, its reading riding on its top and counting up to **3.75 extra** (hidden while it is still inside the poured stack), the band back at full strength; it stands while "four point seven five" is spoken, then shrinks to 4.11 as the number counts to **3.11 extra** and the ghost fades out. On "prices every character" the meter leaves and the stack rises back into the skyline (each character priced on its own); on "came before it" the context row flashes purple.

### 6. Context (2:08–2:58)
> What comes after a Q? *[pause 1.1]* *(after a 0.8 s act turn: about 2.1 s of silence before the question and 1.5 s after it)*

Only the question changes: the box before the ? becomes a purple **Q**, the equation's value becomes a yellow **?**, the 4.11 level dims to a 30 % reference. Then a static frame for the prediction.

> It's U, ninety-eight percent of the time. U swallows the bar, and the average falls to
> point one six bits. *[pause 0.4]*

- On "It's U": U gets the outline flash, the x-axis title becomes "share after Q" (the Q flies down the right gutter), and a blue **98%** appears over U.
- On "swallows the bar": U widens to 98 % **while** its height falls (heights interpolate geometrically, so the drawn area only shrinks); a blue brace at a fixed height grows with it and the 98% rides at its centre.
- "and the average": the skyline pours (the 98 % brace leaves in its first 0.3 s), the axis zooms to 0–5.5 (the old ticks are gone before the new ones fade in), the level is born at 0.16 and copied into the slot on "one six".

> After TH, E takes two thirds of the bar, and costs about half a question.

T H fly to the title; the stack rises into the TH-weighted skyline (axis zooms out); on "two thirds" the **68%** brace appears and E is re-priced at once, dropping to 0.55; on "half" E gets a yellow outline.

> Half a question sounds impossible, but a compressor asks about runs of letters. Their
> probabilities multiply, so their costs add: *[pause 0.6]* five questions for these three, not
> six. *[pause 0.8]* After TH, it averages one point seven.

- E flashes yellow; the ? box flags on "impossible".
- "compressor": the ? box widens into a run of three holding a real run from Shannon's passage, **E ␣ O** (THE OTHER, after T H). The after-TH skyline **and its whole chart** step out (axes, ticks, titles, band, the 4.11 reference: 0 %; only the Brown citation stays), so the bill is never read against axes it is not on. The run's bill is laid out one column per letter: the letter (flashing in the row as its copy appears), a tag naming its two-letter context (**after TH**, **after HE**, **after E␣**: grey "after", purple letters), its probability given those two letters (blue, **0.683, 0.670, 0.072**) and its cost log₂(1/p) (yellow, **0.55, 0.58, 3.80**); MathTex 40, centred in the frame the chart has left. As each column appears, a purple bracket under the context row slides one box to the right, over that letter's two-letter window, and the window flashes purple.
- "Their probabilities multiply": the product is built left to right (each p pulsing as the × after it is written), **= 0.0329**; then, to its right, the run's own price as one symbol, **log₂(1/0.0329) = 4.93**, written while the formula's log₂(1/p) flags.
- "so their costs add": the sum is built the same way, **= 4.93**; the two 4.93s flag together (the costs add because the probabilities multiply). On "five questions", **→ 5 questions**.
- "these three, not six": under each cost, as it pulses, its whole-question count drops in: grey **1 + 1 + 4 = 6 · one at a time**, its "=" under the "=" of the row above and the 6 in the 4.93's column (units under units), "one at a time" left-aligned under "questions" (which sits on the 5's baseline); the 6 is in place as "six" is spoken. In the 0.8 s pause the 5 and the 6 flag together (white), and the complete bill holds about 1.6 s (round 10).
- "TH" (of "After TH"): the bill leaves completely first (0.45 s; only the run box and its letters step back to 30 % in the row), so no cost is ever read against the returning axes; then the chart returns (the 4.11 reference waits for the next beat) and the TH skyline pours, its columns fading in as they flow, landing on "one point seven", where the level is born at 1.67 and copied into the equation.

> But averaged over every two-letter context, it's still two point eight.

The run closes back into the ? box; the TH stack dims to 26 % (the band behind it drops to a faint fill with its green edges, so blue over green never mixes to teal) while the axis zooms in to 0–5.5, its 1.67 gets a purple **TH** tag, the 4.11 reference returns at 60 %. On "every two-letter context" a yellow dashed level grows at 2.81 ("all two-letter contexts", 2.81 in the gutter) and the gap meter measures it once, growing from ≈1 straight to it (**1.81 extra**, the reading hidden until it is 0.15–0.3 clear of the TH level, so it never grazes the 1.67 line); 2.81 is copied into the equation (the copy leaves the gutter to the right and rises outside the 4.11 label), and a note under the slot says what it is: **H averaged over contexts** (H yellow, the rest grey). A 0.8 s act turn follows.

### 7. Payoff (2:58–3:53)
> Hundred-letter contexts need more text than any corpus holds, so Shannon asked a person who
> knows English.

On "need" the equation (and its note), the gap meter and "all two-letter contexts" step out and the whole chart steps back to 25 % (0.5 s; only the Brown citation stays bright), and then, in the equation's place, grey: **possible contexts: 27² = 729 → 27¹⁰⁰ ≈ 10¹⁴³** is written over the quiet chart, so the arithmetic is the one focal point, then **Brown Corpus: 5.75 M characters** (the Brown citation and 10¹⁴³ flag). On "so" the chart fades out completely, and T H leave with it (the row is blank again, as in the cold open); the arithmetic stays above while Shannon's passage (0.3 lower than before, to leave it room) fades in at 40 % (letters only: no guess exists yet). On "a person" a yellow reading cursor locks onto its first letter while the text-so-far row flashes purple; on "knows English" the arithmetic leaves.

> His subject read a passage, guessing each next letter until right: seventy-nine of a hundred
> two on the first guess. *[pause 0.6]*

Shannon's own record (p. 56), glyphs 12 % larger (pitch 0.33, two-digit counts in 0.45 cells), revealed under a moving cursor: the unread letters step back to 15 % as it starts, and each guess count appears only as the cursor passes its letter; the 1s are grey and the rest yellow; a green tally counts first guesses to 79 / 102. The context row reads along: its 12 boxes hold the last 12 symbols read (purple), and the ? box is the symbol being guessed.

> A twin guessing the same way could rebuild the passage from these counts. Treat each
> count as a symbol: *[pause 1.0]* the same skyline, *[pause 0.7]* poured flat, sits at about one point four bits.
>
> That caps the text; more context or a better guesser could only lower it. *(its own beat; then a 0.8 s act turn)*

Twin: letters fade to 12 % and return left to right. Then the letters and the context row leave (the record returns for the landing), the three rows of counts close up at the top of the frame (in order, none crossing another), and the guess chart's baseline is drawn below them once they have risen clear of it, centred and full width (x −4 to 4, y −1.05; ticks 0, 2, 4, 6 bits before the pour). On "Treat" the counts are sorted into their columns one row at a time, bottom row first, so no count ever passes over one still at rest: each drops straight down to its group's lane (1s lowest, 2s above, each 3+ count its own lane), runs along it to its column, and drops straight into the column's foot, which widens as its counts land (width = share of guesses). The labels 1st/2nd/3rd+ and "share of guesses" are the sort's destinations: they come in under the axis as the first counts fly (round 10), so the labelled chart is read for about 4 s before it pours. Then every column rises to its cost (height = log₂(1/share)) as the vertical axis and "bits" grow, as the letter columns did at 0:24, and yellow **log₂(1/q) =** is written as they rise, high over the low 1st column (y 2.2, above where the zoomed stack will reach). On "same skyline" **3.67** is written on a grey leader to the 2nd-guess column, which flashes white-edged, brighter blue. On "poured" it pours flat: the 1st/2nd/3rd+ labels and the leader leave in the first 0.4 s, but the formula stays through the pour and the zoom (it prices what is pouring) and steps out only as the 1.42 level is born, on "one point four" (complete on screen about 4 s; round 10). The axis zooms to 0–2.1 (the chart now fills the lower two-thirds), the stack's separators step back to 25 % and Shannon's ≈1 band is drawn over the stack as two 5 px green edges running 0.25 past the axis (no fill); the level is labelled **≈ 1.42**, with grey **one passage, context 0–101** under it. As "That caps the text" begins, the yellow gap meter grows from ≈1 to the level, counting **0.42 extra**; on "caps" a down arrow and a grey **upper estimate**; on "more context" the note flags; on "lower" the arrow flags.

> Shannon's tests, with a hundred letters of context, put English between point six and one
> point three bits.

The line is **built**, in story order. In the silent act turn (0.8 s) the guess chart leaves (its "upper estimate" last), the person's 1.42 rises over the top of the frame and waits above its own place, and a 0–5 axis grows left to right across the middle of the frame (y ≈ 0.25, 12 units wide), each tick appearing as the line reaches it. Then the three estimates drop in, each with its value and its grey tag (lag 0.35, 0.5 s each; triangle and value drop 0.3 from above, the tag only settles 0.08 so it never passes through the tick numbers): 4.75 (grey) **halving**, 4.11 **no context**, 2.81 **2-letter context**; the 1.42 drops onto its marker last with **person** / **102 letters**; then the axis title **bits per character** (Text 28) in its own row, centred under the whole axis below the tags, so it is never read as a tag's second line. On "hundred letters of context" Shannon's green band grows outward from 1.0 to 0.6–1.3, and **0.6–1.3** is written in the tag row on "point six and one point three". Citation: Shannon 1951.

> A language model compressed part of a book *[pause 0.3]* posted to Project Gutenberg after
> the model was trained. *[pause 0.4]* It needed point eight four bits,
> inside that range. *(then a 0.8 s act turn)*

The Shannon citation fades out completely, then *Valmeekam et al., 2023 · arXiv:2306.04050 (LLMZip), Table IV · 27 symbols* fades in. On "a language model" the INK **LLM** marker is born from the 1.42 (person) triangle and at once rises up and left (under the 1.42 label, then up) to wait **above its own place**, over the band: the final layout lifted 0.9, with a grey **?** in its value slot and the triangle at 40 % (fill only; it turns from the person's yellow to the model's ink as it leaves), so nothing reads LLM = 1.42. On "book" and "Gutenberg" a grey note **1924 book · Gutenberg, May 2023** (Text 26) builds above its name, and on "book" the tags the LLM's story does not need (halving, no context, 2-letter context) step back to 30 % (person / 102 letters, 0.6–1.3 and the axis title stay bright); on "needed" the marker drops straight down onto 0.84, into the band (the ? leaves as it starts, 0.84 lands on "four").

### 8. Landing (3:53–4:00)
> The hidden character from the start *[pause 0.4]* is the Y in the other day. *(its own beat, speed 0.80)*
>
> Shannon's subject needed one guess: *[pause 0.3]* is it Y? Splitting the alphabet took five.
> In English, almost no letter arrives without a past.

0. (Round 10: a continuous handover.) The whole bits-per-character line fades at once (0.45 s, the person's 1.42 marker with it), and in the same move the cold-open row returns, faint (boxes at 40 %, the ? box and its ? at 55 %), where it last stood, at the top of the frame where it read along with the subject; so the row is on screen before "from the start" is spoken. Shannon's record comes back under it (letters at 22 %) with THE OTHER DAY at full strength once the line is gone.
1. The rest of the record goes; THE OTHER DA steps up under its boxes (the Y under the ? box).
2. The phrase rises straight into the waiting boxes; the ? leaves and the Y lands in the ? box on the spoken "Y".
3. The row comes to full strength and moves down to its frame-one place as the 27 candidate tiles (the Y at full blue with a white outline, to the end) return, with the 27→1 chain and a grey "5 questions" faint under them: frame one (as at 0:17), re-seen; the Y flags.
4. "1 guess" in green on "one guess"; on "is it Y" the ? box with its Y flags yellow; on "Splitting" the chain and "5 questions" come to full strength (yellow) and flag on "five", and step back (chain 30 %, "5 questions" grey; the Y tile keeps its highlight) on "In English" while the context flashes. The frame holds to the end.

## Sources
- C. E. Shannon, "Prediction and Entropy of Printed English", *Bell System Technical Journal*
  30(1): 50–64, 1951.
- W. N. Francis & H. Kučera, *Brown Corpus*, Brown University, 1964 (NLTK distribution).
- C. S. K. Valmeekam, K. Narayanan, D. Kalathil, J.-F. Chamberland, S. Shakkottai, "LLMZip:
  Lossless Text Compression using Large Language Models", arXiv:2306.04050, 2023 (Table IV;
  ref. [7]: J. F. Dobie, *Legends of Texas*, 1924, Project Gutenberg ebook 70859, 25 May 2023).
