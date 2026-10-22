# Episode 7 changelog

## Round 1 revisions

Round 1 scored craft 7 and substance 6, both capped. This round fixes both caps and works through every listed fix.

**Caps removed**
- **Factual (cap 6).** "Five questions is the price of a letter with no past" contradicted the episode's own 4.11. It is now "Splitting the alphabet took five", which is true of the Y and the 27→1 chain on screen (facts #33). "That's the floor for any text compressor" became "Whatever it is [the true figure], no text compressor can beat it on average" (facts #6).
- **Overlap (cap 7).** The H line used to slide through the 68 % and 98 % labels. The average line no longer slides at all: every level is born after a *pour* (below). The 98 % and 68 % call-outs are now blue braces parked above the column's tallest state, which is always above both levels.

**Clarity (picture becomes the number)**
- **Area to H.** After "the total area is the average", the skyline pours flat. Each column becomes a full-width slab of the same area, the stack height is H, and the yellow level line is born on its top. Width and height interpolate geometrically, so every piece keeps its area at every frame while it flows. The value is copied into "= 4.11 bits". The same pour is repeated for after-Q (0.16) and after-TH (1.67).
- **Guess counts to bits.** The record's guess counts fly into a guess-number skyline (width = share, height = log₂(1/share)). It pours to 1.42 bits, Shannon's eq. 17 upper bound recomputed from his own record, with "a better guesser could only lower it". The 1.42 then joins the 0–5 line next to Shannon's 0.6–1.3.
- **Language-model stake paid off.** LLaMA-7B + arithmetic coding at 0.71 bits/char on 27-symbol text8, inside the band. Cited *Valmeekam et al., 2023 · arXiv:2306.04050 (LLMZip)*; the training-overlap caveat is recorded in facts #30.
- **Fair cold open.** The cold open now says "You've read this English sentence up to one hidden character", and the boxes are dim purple, labelled "already read".
- **Formula derivation.** `p·2ᵏ=1 → k=log₂(1/p)` now rearranges glyph by glyph. In `average = Σ p log₂(1/p)`, p comes from the width sweep and "average" from k.
- **Narration.** "With perfect fifty-fifty splits, the ideal is…", "So k equals…", "Splitting the alphabet evenly charges every character the same price" (the old line was a garden path; "halving" was avoided because it sounds like "having"), and "out of a hundred". One "X, not Y" antithesis was removed.

**Visual / motion**
- **Band label.** Shannon's band is labelled ≈1 like an axis value, left of the y-axis. In the right gutter it read "1.67 ≈1" as an equation. The % braces leave before each pour.
- **Band.** Shannon's band sits behind the bars with thin edges on top. It is dimmed to 40 % while it is not discussed. Flattened columns get a 3 px blue outline, and hairline columns lose their dark edge so they stay visible.
- **Fail beat.** A yellow double arrow and the label "3.75 extra (79%)" are held at least 2 s. The overlay keeps its outline until "Z".
- **Doubling strips.** The chart opens at a tall scale (0–6.5 axis) so it fills the frame. When the strips arrive it rescales down and dims to 30 %, and the strips sit in the clear band above its axis. The axis grows to 11 only when costs need it.
- **Tail inset.** X J Q Z are drawn ×32 wide at true heights, with "10.3" on Z, during "rare ones narrow and tall".
- **Top-5 flash.** It uses a white outline and blue brighten (yellow stays for questions). Every p in the formulas is blue, including the one inside 1/p.
- **Chart entrance.** The halving diagram clears before the axes grow, so there are no stray early marks. The ghost 4.75 label moves inside the plot and dims to 30 % after "That beats 4.75".
- **Cold open and landing.** Both are centred vertically, with the same layout. In the landing, THE OTHER DAY flies into the row first and the boxes come in under it, with no double exposure.
- **Record.** It uses fixed 0.32 cells in the episode serif, with two-digit counts at 80 % size (no "115" collision).
- **Context timing.** TH goes straight from the after-Q state to the after-TH state, with no reset to no-context.
- **Static stretches.** The two near-static stretches now have motion that matches the narration. On "one bit per yes-or-no answer", the level line flashes. On "prices every character", the stack's slabs flash bottom-up. The longest static stretch is now under 4 s.
- **Mechanics.** 3:43, 0 render warnings, −14 LUFS, longest static stretch 3.6 s, WER 1.9 %. The mini skyline sits higher, so its axis title no longer shares a line with the citation.

## Round 2 revisions

Round 2 scored craft 8.5 (no cap) and substance 6.0, capped by one on-screen maths error. This round removes the cap, fixes every listed item from both critics, and keeps the three "keep" items (the four pours, the doubling strips with live counters, and Shannon's record → guess skyline → landing).

**Plan: where each dimension stood against the BAR "9" anchor, and the upgrade**
- **Clarity (7.5 / 8.5).** The 9 anchor is "all numbers check out; assumptions stated". The equation showed a stale H over a new skyline; the contexts were best cases with no average; the LLM figure carried an unstated caveat; the key equation was held for under 1 s. Upgrade: a "?" slot, a 2.81 average, the 0.84 book figure, and a two-step derivation with a 2.7 s hold.
- **Visual (8 / 8).** The 9 anchor is "every frame has one focal point; all §5 standards met". There were sub-20 px gaps, a crowded top band, a double-exposed axis title, a muddy overlay, a hidden baseline and a near-empty reset frame. Each is fixed below.
- **Motion (8 / 8.5).** The 9 anchor is "every motion encodes a relation; reading time respected". There was glyph soup at 1:35, a messy chart entrance and a 3.6 s static LLM beat. Upgrade: sequential legal algebra steps, a staged entrance, and a sliding LLM marker.
- **Audio (8 / 8.5).** The 9 anchor is "pauses are intentional". Upgrade: a planned 1.8 s hold after the equation; 0.9 s gaps at four beat boundaries; 0.2 s gaps inside two continuing thoughts; "guess number" became "guess count".
- **Hook (8.5).** The puzzle was not assembled until 0:11. Now the tiles are in by 0:04.5 and the question line by 0:07, and the first frame shows the real letters faintly.
- **Concision (8.5).** The one slack, misleading sentence is cut.

**Cap removed (factual, cap 6)**
- **Stale H.** On "What comes after a Q?" and "After TH" the equation's value morphs into a yellow "?" (`H = Σ p log₂(1/p) = ? bits`). Only after each pour is the newborn level value copied up into the slot (0.16, then 1.67). The no-context 4.11 stays as a 30 % grey reference line at its level until "the easy cases". No frame now pairs a skyline with another distribution's H.

**Substance**
- **"None of these numbers depends on what the words mean"** was cut: misleading, since 1.42, 0.6–1.3 and the LLM figure come from predictors that use meaning.
- **Honest limits.** New line: "Q and TH are the easy cases. Averaged over every two-letter context, it's still two point eight." A grey dashed level at 2.81, labelled "all two-letter contexts", grows over the poured TH stack. The same 2.81 joins the bits-per-character line and flags on "a hundred letters of context". It is recomputed in `data.py` (`cond_entropy`: H(X∣1 prev) = 3.38, H(X∣2 prev) = 2.81, matching the critic).
- **LLM figure.** It is now LLMZip's 0.8426 bits/char on a book: Table IV, J. F. Dobie's *Legends of Texas* (1924), released on Project Gutenberg on 25 May 2023, after LLaMA was trained, with the same 27-symbol preprocessing. The 0.71 text8 figure, which the authors call "likely optimistic" (Wikipedia was in the training data), is gone. The citation now names Table IV. facts.md #30 quotes the paper. The narration says only "a book" and does not claim the model never saw it.

**Derivation (p·2ᵏ = 1)**
- The narration adds `[pause 1.8]` after "equals one", and on "one" the two full strips flash (1 = the whole bar). The complete equation is readable for about 2.7 s.
- It then moves in two legal steps, each on its own words. "So two to the k equals one over p": p dips under the "=" to sit under the 1. "and k equals log base two": the 2 arcs over the "=" into the log base while k drops out of the exponent. The "=" never moves (all three forms are aligned on it), so no glyphs pile up. k stays yellow and flags with the 3.3 and 10.3 counters, and the counters also flag on "two to the k".

**Visual / motion**
- **Chart entrance.** The diagram clears and the 4.75 steps straight right into the gutter at its own height. The baseline grows; each tile drops onto it as a short foot; only then does the vertical axis grow (it no longer cuts through the tile row). All 27 columns then rise to the same price while the 4.75 rides up the gutter with their tops and the line is born. 4.75 never passes through a column.
- **Strips.** The y-axis title fades out while the strips work (it read as a third strip row) and returns with the skyline morph.
- **Top band.** The context row is raised 0.15 and the top formula drops from 48 to 44, so the formula clears the boxes by 0.21 and the 10-tick by 0.19.
- **Axis title.** "share" stays put, "of text" drops away, "after" fades in, and the purple Q (later T H) flies down from its context box. There is no cross-fade double exposure.
- **Fail overlay.** Yellow outline plus 45° yellow hatching, with no fill, so the bars stay blue. The hatching leaves on "Splitting" and the outline stays until "Z".
- **Baseline.** The x-axis has z-index 1, so it is never hidden under flashed columns.
- **Bottom band (new overlap audit).** The chart sits 0.15 higher (unit 0.345 keeps the top unchanged). The symbol letters, the % tick labels and the axis title/citation are now three rows at least 0.15 apart. The doubling headers, the 48 %/68 %/98 % brace labels, "10.3", the LLM labels and the number-line tick and band labels are spaced to ≥ 0.15. The sweep line runs on the axis. The render's overlap audit reports 0 overlaps. Three deliberately tight groups are declared with reasons in narration.json: the alphabet tile row (letters in their own tiles, 0.06 apart), Shannon's fixed-pitch record, and its reading cursor.
- **Record.** The whole passage fades in at 20 % while the chart leaves, so there is no empty frame. It is centred vertically during the reveal, then steps up 1.2 units as the guess skyline enters, and the tally leaves at that point. Two-digit counts are full size, in 0.36 cells.
- **Guess skyline.** It has 0 % and 100 % ticks, a two-row label layout (1st/2nd/3rd+; then 0 % · share of guesses · 100 %) and clears the citation.
- **Bits-per-character line.** The band label "0.6–1.3" sits under the band. On "a language model" the LLM marker enters at the 4.75 end on a higher track, slides down the line across "compressing a book…", and drops onto the line at 0.84 with "LLM" stacked over its value. That removes the 3.6 s static stretch, and the label never crosses another one.
- **Hook.** The tiles cascade in on "hidden character" and are complete by "twenty-six"; "questions per character ?" arrives on "With" (≈0:06.5). For 0.6 s at the start the real context letters show at 9 % (too faint to read) and go dark.
- **Mechanics.** Runtime 3:52.4 (+9.6 s for the held equation, the two-step derivation and the 2.8 line, net of the cut). 162 wpm over speech time, −14.0 LUFS / −2.1 dBTP, longest internal silence 1.95 s, longest static stretch 3.1 s, WER 2.1 % ("guess count" now transcribes correctly), 0 banned phrases, 0 render warnings. Layout audit: 0 issues in 204 checks.

## Round 3 revisions

Round 3 scored craft 8.6 and substance 8.4, with no caps and no factual errors (both critics recomputed every number and checked LLMZip on arXiv). This round applies all 14 craft fixes and all 14 substance fixes and keeps the three "keep" items: the doubling strips with live counters and the one-step-per-clause derivation; the pour, reused for after-Q and after-TH with the "? bits" slot; and Shannon's record → guess skyline → bits line → THE OTHER DAY landing.

**Plan: where each dimension stood against the BAR "9" anchor, and the upgrade**
- **Clarity (8.5 / 8).** The 9 anchor is "viewer could re-derive it after one watch; assumptions stated". Two steps were asserted, not argued: why a character can cost *half* a question (the hook asks about yes/no questions per character), and why guess counts measure the text. Upgrade: a sentence and picture for each (runs of letters; Shannon's identical twin), the spoken "130 times" and "1 in 1260" put on screen, and "0.08%" anchored to Z itself.
- **Visual (8.5 / 8).** The 9 anchor is "every frame has one focal point". The dimmed chart still competed with the strips, 70 % of the context plot was empty, and the tail inset read as columns past 100 %. Upgrade: everything but E at 30 % behind the strips; the axis zooms to 0–5.5 whenever only poured levels are drawn; the inset gets a gap, frame, baseline and dashed leaders; two-digit record cells widened.
- **Motion (8.5).** The 9 anchor is "every motion encodes a relation". Upgrade: a gap-free re-sort (columns pour from old slot to new), a staged log₂27 build with the 27 routed below the chain, the 98 % brace widening *with* U, the context letters routed through the gutter, and no end-card flash.
- **Hook (8.5).** Upgrade: the whole puzzle (row, tiles, "26 letters + space") is on screen in frame 1, and the question ends at 0:08 (was 0:13).
- **Audio (8.5).** Upgrade: "questions" is no longer sentence-final ("questions per character"), which measured 7 dB stronger; 0.16 lands as it is spoken and holds 2 s.
- **Concision (8.5).** Upgrade: cut "one of twenty-six letters, or a space", "In the Brown Corpus", "exactly", "because", "From tests like this"; four 0.9 s beat gaps became 0.45 s. This pays for the two new sentences.

**Clarity (both critics' top fixes)**
- **Fractions of a question.** New beat after "about half a question": "Half a question sounds impossible, but a compressor asks about long runs of letters, and the fractions add up. Here they average one point seven." E's flattened column takes a yellow outline (its height is the cost) and flashes on "half a question"; on "long runs of letters" the yellow ? box widens into a run of four ? boxes; "the fractions add up" is the TH pour itself. Evidence in facts #21c (block/arithmetic coding; LLMZip is LLaMA + arithmetic coding).
- **Why guess counts measure the text.** New sentence before "Treat each guess count as a symbol": "A twin who guesses the same way could rebuild the passage from these counts alone." On "twin" the letters fade to 12 % and only the counts remain; on "rebuild" the letters come back left to right; on "counts alone" they step back to 30 %. Quoted from Shannon p. 55 in facts #24a.
- **130× and 1 in 1260 on screen.** At real widths E and Z stay the only bright columns (others and their letters at 25–30 %), Z keeps its own axis letter, "10.3%" and "0.08%" sit on 0.4-unit grey leaders above their own columns, and a blue "×130" grows between them on "hundred and thirty". A blue "1/1260" sits under Z's starting sliver and fades in the first fifth of the counter.
- **0.16 held and in sync.** The level is born on "falls" and its value lands in the equation on "one six"; it holds about 2 s before the TH switch.
- **Wording.** "part of a new book" (a 100,000-token extract, released after the model was trained); "In the Brown Corpus" cut (citation on screen); "questions per character".

**Visual**
- **Strips stage.** Everything in the chart except E's column and E's letter dims to 30 % (letters, % ticks, x title, y ticks, the yellow 4.75 line and its label, the band) and returns on "Now give each character its own cost".
- **Context axis.** The y-axis zooms to 0–5.5 (ticks 0, 2, 4) whenever only poured levels are drawn (after Q, after TH), with the band, the 4.11 reference and its label riding along, and zooms back out when the TH skyline needs 0–11. The final frame of the beat reads 4.11 > 2.81 > 1.67 with the band at ≈1, using the whole plot.
- **Tail inset.** The main chart moved 0.15 left; the inset (×28, with small gaps so X J Q Z never crowd) sits 0.38 units clear of the axis, in its own thin grey frame on its own baseline, with a thin box around the four hairlines and two dashed leaders to the frame.
- **Record.** Two-digit counts get 0.44 cells, so "11 5" can no longer read "115".
- **68 % brace.** Parked above the grey 4.11 reference as well as above E's tallest state, so no line crosses it.
- **Landing.** The context boxes and the 27 tiles return together (frame one, re-seen) right after THE OTHER DAY lands; chain and "5 questions" return on "a single yes-or-no question", flag on "five" and dim on "In English". No end card: the landing frame holds to the end.

**Motion**
- **Re-sort without gaps.** Each column pours from its old slot into its new one (most frequent first): the sorted block grows from the left and the rest stays packed against it, so every frame tiles 0–100 % with no gaps or overlaps (`tile_columns`).
- **log₂27.** The label steps left so the finished line is centred at x = 0; "log₂" is written; the chain's 27 travels on a lane below the chain and above the label, then drops into its slot; "≈" is written and the 5 cross-fades into 4.75.
- **98 % brace.** It spans U in every frame of the widening (readable by "ninety-eight", complete by "out of a hundred"); U flashes on "swallows".
- **Context letters.** Q, then T and H, fly over the row and down the right gutter (x ≈ 6.1) to the axis title, never across a column or tick label; the old title tail fades out before the new one fades in.
- **Ident.** Dropped.

**Audio**
- "questions" is no longer sentence-final ("…the average number of questions per character"); the word measured about 7 dB louder in the synthesized clip and whisper now transcribes it. "Then pour the skyline flat" gives "pour" a consonant lead-in (whisper had heard "or").

**Verification and mechanics.** The final master is 3:54.6 at 160 wpm over speech time, with −14.0 LUFS / −1.9 dBTP, 0.00 s lead and 1.24 s trail, a longest internal silence of 1.96 s and a longest static stretch of 3.6 s (the closing hold). WER is 2.0 %, with "questions" and "pour" both transcribed. There are 0 banned phrases and 0 scene warnings, and the layout audit reports 0 issues in 218 checks with no allowances. Besides all 13 contact sheets and the keyframes, frames were swept at 0.25–0.5 s across the log₂27 build, the re-sort, the after-Q and after-TH beats (brace, gutter route, title swap, zooms, equation slot) and the landing. Two bugs were caught and fixed this way. The record's letters failed to lift with their counts because an `.animate` target was built before the twin fades. In the landing, THE OTHER DAY vanished for 1 s because the fade list matched the record group by identity, not by family.

## Round 1 revisions (review cycle 2)

Cycle-2 round 1 scored craft 8.0 and substance 8.6, with no caps and no factual errors (both critics recomputed every number; LLMZip 0.8426 checked on arXiv). Every listed fix from both critics is applied, plus three cheap items from the earlier round-4 reviews of the same cut (no chart/record superimposition, the guess skyline zoomed so its level is readable, the landing row present through the reveal). The keep items survive unchanged: the doubling strips with live counters, the skyline pour (now four times), and Shannon's record → twin → guess skyline → landing.

**Plan: where each dimension stood against the BAR "9" anchor, and the upgrade**
- **Clarity (8 / 8.5).** Anchor: "viewer could re-derive it after one watch". Two hinges were asserted: why half a question is possible, and why Shannon switched to a person. Upgrade: a real four-letter run with its costs adding to a whole number of questions, and a sentence plus an on-screen count of possible contexts.
- **Hook (8 / 8.5).** Anchor: "tension rises through build and fail". The 3.75 gap never came back. Upgrade: a live gap meter (3.75 → 3.11 → 1.81, then 0.42), band at full strength while it shows.
- **Visual (8 / 8.5).** Anchor: "every frame has one focal point". Upgrade: the main equation built centre stage at 56, the run's frame with the skyline dimmed, the record glyphs 12 % larger, citations never superimposed, the landing played into its own boxes, palette fixed (2.81 yellow; grey is only the abandoned 4.75).
- **Motion (8 / 8.5).** Anchor: "every motion encodes a relation". Upgrade: the LLM marker born from 1.42 and moved only to 0.84; U and E re-weighted and re-priced together; the prediction pause left still; tick swaps that never mix two scales; cross-fades instead of glyph soup.
- **Audio (8 / 8.5).** A 0.3 s pause before "four point one one"; the clipped "TH" sentence is gone.
- **Concision (8 / 8.5).** Cut "With perfect fifty-fifty splits", "Common characters sit wide and low, rare ones narrow and tall", "Q and TH are the easy cases" and "in real text"; this pays for the two new sentences.

**Clarity and substance**
- **Fractions add up (craft 1).** On "long runs of letters" the ? box widens into four boxes holding E R E ␣ (THERE, after T H) and each letter's cost given the two before it appears in yellow (0.5, 3.0, 2.6, 1.6; `data.py` → `run_THERE`). On "the fractions add up" the four costs flow into "7.7 → 8 questions". The skyline dims to 40 % meanwhile, so the run is the focus.
- **Why a person (substance 1).** New line: "Longer contexts need more text than any corpus holds, so Shannon used a predictor that already knows English: a person." On screen: "possible contexts: 27² = 729 → 27¹⁰⁰ ≈ 10¹⁴³" and "Brown Corpus: 5.75 M characters" (facts 21f quotes Shannon's own reason, p. 54).
- **"New book" (substance 2).** Now "part of a book that reached Project Gutenberg after its training", with a grey note "1924 book · on Gutenberg May 2023 · 27 symbols" that builds word by word. We avoid "first put online" (facts 30).
- **Gap meter (substance 3).** The fail beat's double arrow returns: 3.75 → 3.11 on "That beats four point seven five", 3.11 → 1.81 at the two-letter average, and 0.42 on the zoomed guess skyline (which now shows Shannon's ≈1 band).
- **Two-letter average (craft 7).** The TH stack dims to 30 %, 1.67 gets a purple TH tag, and 2.81 is copied into the equation. Shannon's setup is tightened to "His subject read a passage letter by letter…".
- **Guess skyline (craft 8).** Yellow "log₂(1/q) = 3.67" beside the 2nd-guess column; the poured level reads "≤ 1.42".
- **Wording.** "an English sentence", "three point three ideal doublings", "Half a question, like three point three doublings, sounds impossible", "After TH, the average is one point seven", "The ideal is log base two of twenty-seven".

**Visual and motion**
- **Equation (craft 4).** On "In general" the strips step up 0.65 and dim to 40 % (counters stay bright), and p·2ᵏ = 1 → 2ᵏ = 1/p → k = log₂(1/p) is built centred at font 56. The strips clear before the formula rises to the top row; E's 3.3 reappears as its new height.
- **LLM (craft 2, 9).** The INK "LLM" tag points into the ? box during "how language models are trained". At the payoff the marker is a TransformFromCopy of the 1.42 triangle, waits above it, and moves only 1.42 → 0.84.
- **Prediction pause (craft 3).** The unpour now happens on "it prices every character as if nothing came before it"; "What comes after a Q?" only swaps in the Q and the "?" and holds still (pause 1.6 s).
- **Re-pricing (craft 6, substance 4).** `tile_morph`: widths move linearly (the bar always tiles 0–100 %), heights geometrically, so U widens to 98 % while its cost falls (on "U swallows the bar") and E re-prices on "two thirds". The 98% label is shown over U on "ninety-eight" and rides a fixed-height brace.
- **Citations (craft 10, substance 5).** `Succession(FadeOut(Shannon), FadeIn(Valmeekam))`.
- **Record (craft 11).** Glyphs 27/24 pt (12 % larger; pitch 0.33, the widest line just fits the safe area), line spacing 1.12, unread lines at 15 %. The chart fades out completely before the record fades in, and the text-so-far row stays through the change, so no frame is empty.
- **Landing (craft 5).** The cold-open boxes and ? box fade in at 30 % as the record fades; THE OTHER DA flies straight into them and the Y lands in the ? box on the spoken "Y"; then the boxes come to full strength and the tiles return.
- **Ticks (substance 6).** In every zoom the old ticks are gone in the first 30 %, the new ones fade in at their places in the last 35 %.
- **Palette (substance 7).** 2.81 is yellow everywhere (level, gutter, bits line); the dimmed 4.11 reference is yellow at 30 %, not grey.
- **Glyph soup (substance 12).** "k" → "average", "average" → "H" and "questions" → "bits" are cross-fades.
- **Small items.** ≈1 centred on the band (substance 14); the inset opens with the width sweep (the "wide and low" sentence is cut, substance 10); the ? box flags on "sounds impossible"; the LLM note builds in three parts, so no static stretch over 4 s.

## Round 5 revisions

The round-5 reviews (craft 8.0, substance 8.6, no caps, no factual errors) are the same files as the cycle-2 round-1 reviews. The section above applied every fix from both, but that pass was cut short after its master render (the review pack was older than final.mp4, and no frames had been checked). This round regenerated the pack for that master, swept every transition at 4 fps, and fixed what the sweep found. The narration did not change. All three keep items survive: the doubling strips, the skyline pour, and the record-to-landing chain.

**Plan: dimensions still below 9 against the BAR "9" anchor**
- **Visual ("every frame has one focal point; nothing to remove").** kf_29 (2:53) was a near-empty frame (only the context row) for about 3 s while the narration said "already knows English: a person". The guess-count landing at 3:11 drew long blue streaks across the record. Fix: no empty frame and no streaks (below).
- **Motion ("every motion encodes a relation; reading time respected").** "log₂(1/q) = 3.67" stayed for 2 s over a skyline that had already poured. The 3.75 meter started shrinking as soon as it appeared (a 2 s frame read "3.74 extra"). Fix: hold each state while it is true, and remove a label when its referent goes.
- **Clarity ("all numbers check out").** Twice the equation's arriving value ran into "bits" ("1.67bits" at 2:41, "0.16bits" at 2:20). Fix: "bits" steps aside first.

**Changes**
- **No empty frame before the record (2:52–2:55).** The chart fades out in 0.5 s. Shannon's passage then fades straight in at 40 % on "already knows English", letters only, because no guess exists yet. On "a person", a yellow reading cursor locks onto its first letter while the text-so-far row flashes. When reading starts, the unread letters step back to 15 %, and each guess count appears only as the cursor passes its letter. The empty stretch is now 0.25 s mid-transition (it was about 3 s).
- **Counts drop into their columns (3:10–3:12).** "Treat each guess count as a symbol" used to morph three lines of digits into rectangles, which left streaks. Now every count falls into the foot of its own column, spread across the column's width (all 79 ones across the 1st column), and shrinks away as that column grows from its base.
- **"log₂(1/q) = 3.67" leaves with its columns.** The value lands at about 3:12.5 and holds about 1.5 s, until "flat". The pour starts on "flat", and the label and the 1st/2nd/3rd+ labels fade in its first 40 %. The level and "≤ 1.42" arrive on "one point four bits".
- **The 3.75 meter holds while it is true (1:58–2:00).** It stands at 3.75 through "four point seven five", then shrinks to 3.11 on "but it's still".
- **Equation values never hit "bits".** In each eq_known (0.16, 1.67, 2.81), "bits" steps aside and the old value leaves in the first 35 %. The copied value then flies in (ease-out), so the "0.16bits" and "1.67bits" frames are gone.
- **The widths become p (1:40).** The blue sweep along the axis no longer morphs into the glyph "p" (a wavy line across the bars, mid-flight). It contracts and rises onto the p's place, and the p appears there.
- **Landing (3:41–3:43).** As the record goes, THE OTHER DA steps under its own boxes at the boxes' pitch, with the Y under the ? box, 0.39 below the row; it was 0.10 under the boxes. It then rises straight in; the Y lands on the spoken "Y".

**Verification.** Master 3:57.7, 157 wpm over speech time, −14.1 LUFS / −2.2 dBTP, lead 0.00 s, trail 1.04 s, longest internal silence 2.09 s (the planned prediction hold), longest static stretch 3.5 s (the closing hold), WER 1.7 %, 0 banned phrases. The render printed 0 [sample_space] warnings, and the layout audit found 0 issues in 220 checks with nothing allowed. I read all 14 contact sheets and the new keyframes (kf_17, 20, 30, 33). I also swept every changed transition at 4 fps: 1:39.5–1:42.5, 1:57.5–2:01.5, 2:38.5–2:46.5, 2:51.5–2:56.5, 3:09.75–3:17.5 and 3:40.75–3:44.75. The narration diff's "longer → other" at 2:47 is a whisper segment-boundary artifact: re-transcribing the 9 s around it alone gives "Longer contexts need more text…".

## Round 6 revisions

Round 6 scored craft 8.8 and substance 8.6, with no caps and no factual errors; both critics said the fixes would reach 9. Every fix from both reviews is applied below, one of them in a corrected form (the 9-vs-8 comparison; see Clarity). The keep items are unchanged: the skyline pour (4.11 / 0.16 / 1.67 / 1.42), the persistent context row with the Y landing, and the gap meter with Shannon's record under a cursor.

**Plan: dimensions below 9 against the BAR "9" anchor**
- **Clarity (substance 8.5).** Anchor: "viewer could re-derive it after one watch". The fractional-question demo showed a total (7.7 → 8) with nothing to beat, the payoff markers were bare numbers, and the context row said "T H" during a passage that has nothing to do with TH. Upgrade: a run's bill with a real one-at-a-time comparison, tags on every marker, and a context row that reads along with the subject.
- **Visual (8.5 / 8.5).** Anchor: "every frame has one focal point". The run costs (30 px) were wedged top-right and competed with the newborn 1.67, the payoff line sat in the bottom third under a dimmed record, and the inset and book note were undersized. Upgrade: the bill moves into the empty chart at MathTex 36 and steps back to 30 % when the level is born, the record leaves for the summary line, and every small label is at least Text 26.
- **Motion (8.5 / 8.5).** Anchor: "every motion encodes a relation". Four glyph collisions: 3.3 → 2ᵏ, 2.81's copy, the count flight, and the LLM label crossing its note. Upgrade: copies leave their source before cross-fading, routes go around labels, counts fly by guess number, and the LLM marker and note move rigidly together.
- **Audio / Concision (8.5).** "Like three point three doublings" pointed at nothing; cut. The time pays for "five questions for these three, not six", "is it Y?" and an 0.8 s pause before the guess skyline pours. The voice runs at 0.85 instead of 0.84 so the master stays under 3:58.

**Clarity**
- **What 5 questions beat (substance 1).** The run is now **E ␣ O** from THE OTHER, after T H. The ? box widens into three boxes, the chart steps back to 25 %, and the run's bill is laid out in the empty top of the chart at MathTex 36. Each letter flashes in the row as its copy appears over its cost: 0.5, 0.6, 3.8. The sum is built term by term with a running tally (0.5, then 1.1, then 4.9), and the "=" is written only once every term is in, so the line never shows an equation that is not yet true. Then "→ 5 questions", and under it in grey, built by each cost dropping into its whole-question count, **1 + 1 + 4 = 6 · one at a time**, with 6 under 5. Narration: "…and the fractions add up: five questions for these three, not six." **Why not the critic's 1 + 3 + 3 + 2 = 9 for E R E ␣:** it is only the rounded-up costs. The best one-letter-at-a-time trees (Huffman per context) put R∣HE at depth 2, so they also need 8 on that run, and "8, not 9" would have been misleading. On E ␣ O, rounding up and Huffman both give 1 + 1 + 4 = 6 (`data.py` asserts it; facts 21e).
- **Payoff markers tagged (both critics).** The bits-per-character line is now the only thing in the middle of the frame: the record fades to 0 as the line builds (it comes back for the landing). The line is 12 units wide, the values are MathTex 40 and the markers larger, and grey Text 28 tags sit under the axis: **halving** (4.75), **no context** (4.11), **2-letter context** (2.81), **person** (1.42). LLM keeps its INK name. The band's "0.6–1.3" sits in the same row, under the band.
- **The context row reads along (substance 5).** T H leave with the chart at "already knows English", so the row is blank again, as in the cold open. While the cursor reads, the row's 12 boxes hold the last 12 symbols read (purple), and the ? box is the symbol being guessed.
- **Wording.** "Contexts of a hundred letters need more text than any corpus holds" (substance 8). "…a single yes-or-no question: is it Y?", with the ? box and its Y flagging on "is it Y" (substance 9). "≈ 1.42" plus a grey **upper estimate** on "could only lower it" (substance 10).

**Visual and motion**
- **Count flight (both critics).** As the record lifts, its letters drop to 12 % and the new axes are drawn without titles. The counts then fly by guess number: all 79 ones into the 1st column (1.1 s, lag 0.012), then the 2s (0.6 s), then the rest (0.8 s). Each count first dips under its own row, then curves down, shrinking, into the foot of its column, and each column grows as its counts land. "bits", "share of guesses", 1st/2nd/3rd+ and "log₂(1/q) =" arrive after the flight; the formula now sits right of the tail columns, out of every flight path. The time comes from an 0.8 s pause after "symbol".
- **Run bill vs 1.67 (craft 4).** The bill stays at full strength through the pour. On "the average" the 1.67 level is born and the bill and run box step back to 30 %, so only one yellow number is the focus. The axis zoom moved to "But averaged…", where the bill leaves, the run closes back into the ? box and the TH stack dims.
- **Copies leave their source (craft 5, 6; substance 7).** `fly_morph`: a copy travels a route and cross-fades into its target. It is invisible while it still overlaps its source, so nothing stacks. 3.3 → 2ᵏ leaves to the right of the counter, passes right of and under Z's 10.3, and lands in 2ᵏ; it now starts on "times" (1.4 s, not 0.9 s). 2.81's copy leaves the gutter to the right, rises outside the 4.11 label and comes up into the slot from below, clear of "bits".
- **LLM and its note (substance 11, 12; craft 2).** The note "1924 book · on Gutenberg May 2023 · 27 symbols" is Text 26 and builds in three parts above the waiting LLM name, on "book", "Gutenberg" and "same". On "needed", marker, name and note slide left together, so nothing crosses, and on "point eight four" they drop onto 0.84.
- **Inset (craft 7).** It moved 0.1 left with 0.05 gaps; the frame's right edge is now at x = 6.37 and "10.3" ends at 6.2. "×28 wide" is Text 26. The mini chart's axis titles and 1st/2nd/3rd+ are Text 26.

**Audio and concision**
- "Like three point three doublings" is cut (craft 3, substance 4). The voice speed is 0.85 instead of 0.84, so the added words keep the runtime under 3:58.

### Round 6 revisions, verification pass

The first round-6 pass was interrupted after its 09:27 render. This pass re-rendered the current scene and swept the frames during motion with 4–6 fps strips at every fixed timestamp, then fixed what was still wrong. No narration and no claim changed.

- **The run's sum (substance 1, 6; BAR §11.1).** In the 09:27 render the running tally rolled through 0.7, 1.2, 2.7 and 4.8 between the true partial sums, so for a few frames the bill showed sums of nothing on screen. A trial "costs flow into the total" version stacked half-faded copies of 4.9, so it was dropped too. The sum is now built left to right: each cost pulses as the "+" after it is written, then "= 4.9" arrives once every term is in. 0.5 + 0.6 + 3.8 = 4.9 holds as displayed (asserted in `scene.py`). The whole-question row no longer cross-fades "0.5" into "1" in one spot ("0̶1̶5̶"). Each whole number drops in under its own cost as that cost pulses.
- **Copies never stack (craft 5, 6; substance 7).** `fly_morph` keeps a copy invisible until its box is clear of the source's box. The old rule (opacity grows with distance) still showed a half-strength 2.81 on top of the gutter's 2.81 at 2:44. When the copy changes glyph (3.3 → 2ᵏ), the old glyph now dims out completely before the new one brightens, so the two are never superimposed.
- **Count flight (craft 1, substance 3).** Each count's path was a spline through a waypoint 0.3 under its start, and it overshot: the right-hand counts of each row first rose over their own row. Each path is now a cubic Bézier that leaves straight down and lands straight down into its column.
- **Value swaps.** "0.16 → ?" and "1.67 → ?" (the context changes) and "average → H" were cross-fades in place, which stacked the two glyphs for about 0.3 s, and the sliding "=" passed over the fading "average". Now the old term leaves upward first, and the rest of the formula slides only once it is almost gone.
- **One baseline per label row.** The payoff tags and the green 0.6–1.3 sat on their centres, so "person" (a descender and no ascender) rode about 5 px high. The LLM note's "1924 book" also sat 5 px below "· on Gutenberg May 2023". Each row now shares a measured baseline.
- **Landing, 3:41.** The bits-per-character line faded out before Shannon's record faded back in, which left about a second of near-empty frame under "The hidden character from the start". The two now overlap, so THE OTHER DAY is already bright as the line leaves.

### Round 6 revisions, narration budget (PRODUCTION_GUIDE §13)

Both round-6 critics docked Concision (8.5) and Audio (8.5). The substance critic noted the 3:57.7 runtime ("only 2.3 s under 4:00"), and the craft critic called the delivery tight. The toolkit's §13 now spells out the "9" pattern for these dimensions: ≤ 500 words, 3:15–3:35, voice 0.82–0.84 with shaped pauses, and no glyph morphs.
- **Plan.** *Concision 9* ("cutting any sentence loses something"). The mute test cut every sentence that restates the frame. *Audio 9* ("pauses are intentional"). The voice is slower and pauses come after the key results. Nothing on screen or in the argument was removed.
- **Words 602 → 496.** Cut: "Splitting the alphabet evenly charges every character the same price" (the one price line shows it, and it now flashes on "as much as E"); "its cost drops to almost nothing" (U flattens on screen); "in the same twenty-seven symbols" (the note on screen says "27 symbols"); "Whatever it is"; "In general"; "counted"; "the whole"; "ideal" (second use); "of all text". Shortened: the landing (45 → 35 words, one move: "Shannon's subject needed one guess: is it Y? Splitting the alphabet took five."), "That beats 4.75, but it's four times Shannon's estimate: it ignores what came before", and "Hundred-letter contexts…".
- **Voice.** `SPEED` 0.85 → 0.83 with `CADENCE = "shaped"` (beat gap 0.45 s). There is now a 0.9 s pause after the 4.11, 0.16 and 79/102 results, the hold before the guess skyline pours is 1.0 s, and the 1.5 s and 1.6 s prediction holds stay.
- **Re-cued.** Every animation is driven by the new word timings. The doubling cuts land on "halves"; the 4.75 is written on "four"; the even-split hatching now leaves on "Z"; the after-Q pour starts right after U swallows the bar (the 98 % brace leaves inside it); the number line is built by "context"; the LLM note's last part arrives on "training"; and the landing's chain returns on "Splitting". The glyph-morph lint's one hit ("?" → "5" at 0:11) is now `swap()`. Tick labels carry `ss_role = "tick"`, and the inset letters are Text 20 (they were 23 px, under the 24 px floor).

### Round 6 revisions, final pass (motion sweep)

The 14:37 master from the narration-budget pass had never been frame-checked. This pass swept every transform at 3–4 fps (`ffmpeg … fps=4`, BAR §11.6), fixed what the sweep found, and re-rendered and re-checked. No claim changed. Every round-6 fix stays in, and so do the keep items: the pour, the context row with the Y landing, and the gap meter with Shannon's record.

- **Glyph soup removed (craft 5–6, substance 6–7; §13.2.6).** Five transforms still interpolated unlike outlines. Each one showed up in a 2 s sheet frame or a 4 fps strip.
  - 0:20.8: "5" → "4.75" was a `FadeTransform` in place, and the two were superimposed in sheet frame 0:21. It is now `swap()`: the 5 steps up and out before 4.75 steps in.
  - 0:24.5–0:25.3: 4.75 riding into the gutter was a `ReplacementTransform` between MathTex objects of different structure ("4.ℤ5"). It now moves and scales as itself.
  - 1:26.5: "k" faded out while Σ was written on the same spot. Now k leaves first, Σ is written after it, and "=" slides only once k is gone.
  - 1:59.5 and 2:20.3: the 0.16 and 1.67 copies grew on top of their gutter labels (`TransformFromCopy`), giving "1̶.67". Every level copy now takes the route 2.81 already used: out of the gutter to the right, up outside the chart, and into the slot from below. It stays invisible while it overlaps its source.
  - 3:01.1: the mini 1.42 → payoff-line 1.42 `ReplacementTransform` garbled ("1̶4̶2"). It now moves as itself.
- **The live meter reads in front of the lines.** At 2:25.0, "2.41 extra" was struck through by the 4.11 dashed line while the meter shrank. The reading now has an opaque BG backing, so the dashes pass behind it. Its digits are re-raised above the backing on every frame, because `set_value` rebuilds them at z 0.
- **Landing frame (§13.1 composition).** From 3:22 to 3:28 the lower half was empty while the narration ran. Now the halving chain and its "5 questions" come back faint with the tiles, so the frame is the 0:17 frame re-seen. On "Splitting" they come up to full strength and flag. Afterwards "5 questions" rests in grey (the abandoned method, like the 4.75 ghost) instead of 30 % yellow, which reads as olive. The record's letters are now gone before the row's boxes come up over its last line.
- **Narration (whisper, §13.3).**
  - "Five halvings" was heard as "havings": misaki says /hˈævɪŋz/, a homophone. It is now "five cuts", which names the yellow cuts on screen.
  - "Ninety-eight times in a hundred" was heard as "times and a hundred". It is now "ninety-eight percent of the time", matching the 98 % on screen.
  - WER fell from 2.4 % to 1.4 %. The remaining diffs are number formatting and "Y" heard as "why".
- **Budget.** `BEAT_GAP` went from 0.55 to 0.51. Runtime is now 3:34.2, inside the 3:35 budget; the 3:35.5 overrun was the render's one warning. Beat turns are 0.67 s against 0.40 s full stops.
- **Labels.** "LLM" (0:32) and "TH" (2:23) went from Text 24 to Text 28, and "26 letters + space" from 24 to 26.

**Verification.**
- Master: 3:34.2, 152 wpm over speech time, −14.0 LUFS / −2.1 dBTP, lead 0.00 s, trail 0.88 s.
- Longest internal silence 2.23 s (the Q prediction hold). Longest static stretch 3.3 s (the closing hold).
- 0 render warnings. Layout audit: 0 issues in 218 checks, nothing allowed. 0 glyph morphs, 0 unlanded deictics, 0 banned phrases.
- I read all 12 contact sheets. I re-swept, at 4 fps, 0:20–0:22, 0:23.7–0:25.7, 1:25.6–1:27.6, 1:57.8–2:00.8, 2:18.3–2:21.3, 2:23.5–2:26.5, 2:59.6–3:01.6 and 3:19.6–3:22.1.
