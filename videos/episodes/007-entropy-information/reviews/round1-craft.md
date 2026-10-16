# Episode 7, review round 1 (craft critic: visual design, motion, A/V sync)

Evidence: `review/` pack (metrics.json 11:10 is newer than final.mp4 11:08): report.md, all 11 contact sheets, keyframes kf_01, 05, 06, 11, 16, 21, 22, 25, 27, 28, 29, 31, 33, plus extra ffmpeg frames at 0:23, 0:27, 0:41.5, 0:59.6, 1:07, 1:11, 1:39, 1:44.6, 1:57, 2:04.4, 2:08, 2:17.4–2:18.9 (0.3 s steps), 2:18–2:20.2 crops, 2:22.8, 2:23.8–2:26.2 crops (0.4 s steps), 2:25.0, 2:29, 2:57, 3:12. I also read the transcript, narration diff, script.md, facts.md and data.json.

```
EPISODE: 007 — "How Much Information Is in a Letter?"
IDEA: A character costs log2(1/p) yes/no questions, so its information depends on how predictable it is; priced with context, English needs about 1 bit per character, not the 4.75 that halving the alphabet suggests.
SCORES: Hook 8.5 · Clarity 8 · Visual 7.5 · Motion 8 · Audio 8 · Concision 8.5 · Originality 9
WEIGHTED: 8.2 (8.15)   AFTER CEILING: 8.2 (lowest 7.5 + 2 = 9.5, not binding)
CAPS: Text overlapping another element (cap 7). The blue "68%" label for E is struck through by the yellow dashed average line from about 2:24.2 to 2:25.8, about 1.5 s, while the narration says "E takes over two thirds of the bar". Frames at 2:24.2, 2:24.6, 2:25.0, 2:25.4 and 2:25.8 show the line crossing the glyphs. The same line also crosses "98%" briefly at about 2:19.0, which is a lesser instance.
FINAL: 7.0   PASS: no
FACTS:
- Hidden symbol is one of 27 (26 letters + space) | Verified | Shannon 1951 p.56 alphabet
- Five halvings take 27 to 1; chain 27→13→6→3→2→1 | Verified | arithmetic (cuts at N|O, U|V, X|Y, Z|␣, Y|Z on screen match)
- log2 27 ≈ 4.75 | Verified | 4.7549
- Shannon (1951) estimated about 1 bit/char | Verified | BSTJ 30(1) p.50, "of the order of one bit per letter"
- "That's the floor for any text compressor" | Verified (loose: the floor is the true entropy rate, of which ≈1 is an estimate) | source-coding theorem
- Next-token guessing is how LMs are trained | Verified (general knowledge, qualitative) | —
- "Four of every five questions" wasted | Verified | (4.75−1)/4.75 = 0.79
- E appears 130× as often as Z | Verified | data.json E/Z = 130.3 (Brown)
- Space+E+T+A+O ≈ half of text (48%) | Verified | data.json top5 = 0.4834
- E ≈ a tenth; 3.3 doublings | Verified | p(E) = 0.1031, log2(1/p) = 3.277
- Z is 1 in 1260, needs 10.3 | Verified | 1/p = 1263, log2 = 10.30
- p·2^k = 1 ⇒ k = log2(1/p) | Verified | algebra
- Widths sum to 1 so area = average | Verified | expectation
- H(Brown letters) = 4.11 bits | Verified | data.json H1 = 4.1111 (Shannon's own F1 = 4.03 from other tables; Brown is labelled on screen)
- "Still 4 times Shannon's estimate" | Verified | 4.11/1
- After Q, U 98 in 100 | Verified | data.json 0.9814 (n = 5,103)
- H after Q = 0.16 | Verified | facts.md 0.156; consistent with the after_Q distribution
- After TH, E > 2/3; H = 1.7 | Verified | data.json E 0.683; H 1.667
- Guessing protocol (guess until right) | Verified | Shannon 1951 pp.55–56
- Record text and per-character guess counts | Verified | matches Shannon's display on p.56 as transcribed in data.json
- 79 of 102 right on first guess | Verified | Shannon 1951 p.56
- 0.6–1.3 bits/char at N = 100 | Verified | Shannon 1951 p.64 table
- Hidden char is the Y of "THE OTHER DAY", guessed first try | Verified | record line 3
MECHANICS: runtime 3:12.6 · wpm 161 (speech time) · max silence 1.96 s · max static 3.53 s · −14.0 LUFS / −1.9 dBTP · leading 0.00 s / trailing 1.74 s · 0 banned phrases · WER 1.8 %
FIXES (highest impact first):
1. [2:24.2–2:25.8][Visual] The "68%" label sits at value ≈3.9, exactly where the dashed H line starts (4.11) and then passes as it slides to 1.67, so it is struck through for about 1.5 s. Anchor every share label for a widened column (98% at 2:13–2:21, 68% at 2:24–2:27) under the x-axis beside its letter ("E · 68%" in BLUE at y just below the letter row), or keep it at max(column top, H-line start, H-line end) + 0.35. Never place it in the band the H line sweeps through. This removes cap 7.
2. [1:41–1:57][Clarity/Motion] "the total area is the average number of questions" is said over a static skyline. The 4.11 then arrives by sliding the old 4.75 line down (1:53–1:55), not from the area. After "average number of questions", pour the skyline into one rectangle of width 1. Each column's area flows left to right in about 2 s (smooth), the top settles flat at 4.11, and the dashed yellow line is born at that top. Then TransformFromCopy that height into "= 4.11 bits". Repeat the levelling in about 1 s for the after-Q (0.16) and after-TH (1.67) states so H is visibly the skyline's "water level" every time. This is the episode's one missing "picture becomes the number" move.
3. [2:15–2:27][Visual/Clarity] Once U (2:17) and E-after-TH (2:26) flatten below 1.3, they disappear under the opaque green ≈1 band. "98%" and "68%" then float over the green band and read as labelling Shannon's band (kf_28 2:20.8, kf_29 2:26.7). Draw the band behind the bars (lower z-index) at 25–30 % fill with two thin green edge lines, and give flattened columns a 3 px BLUE outline so they stay visible. Also dim the band to 40 % between 0:55 and 1:52, when it is not being discussed. It currently tints every bar teal for about 2 minutes (0:33–2:27).
4. [2:41–2:49][Clarity] The jump from "79 of 102 first guesses" to "0.6 to 1.3 bits" is unexplained, so the viewer cannot see how guess counts become bits. Add one sentence and one visual. Collapse the record's guess counts into a 6-bar histogram (1st: 79, 2nd: 8, 3rd: 3, 4th: 2, 5th: 2, >5: 8) and say: "A subject who is right first time almost always is a peaked distribution, and Shannon turned these guess frequencies into bounds." Then TransformFromCopy the histogram into the green 0.6–1.3 band. Runtime has room (3:12 of 4:00).
5. [1:07–1:35][Visual] The "what's still possible" strips for E and Z are drawn inside the chart's plot area, spanning y ≈ 7–10 on the "questions" axis (kf_16, kf_21), so they read as plotted values. Either dim the chart to 30 % and move the strips into a clear band above it, or scale the chart down to y ∈ [−3.0, 0.5] while the strips are active and restore it at 1:35 when heights morph.
6. [0:40–0:45][Hook/Clarity] The failure is shown as an unlabelled yellow overlay (f 0:41.5) that turns the bars muddy teal and is gone by 0:45. Add a yellow brace on the right of the overlay labelled "3.75 wasted · 79 %", hold it 2 s, and keep the overlay outline (not fill) until "Z costs as much as E" begins.
7. [0:43–0:47][Audio] "Cutting the alphabet in half prices every character alike" is a garden-path sentence. The TTS groups it as "in half prices," (whisper inserts a comma after "prices"), so it sounds like "half-price". Rewrite as "Halving the alphabet charges every character the same price."
8. [2:31–2:56][Visual] In the Shannon record the two-digit counts collide with their neighbours: "11 5" reads as "115" (line 3, from 2:37) and "15 1 17" crowds on line 1 (kf_33). Lay each count in a fixed cell centred under its character (cell = character advance, at least 0.35 units) with tabular figures. Shrink two-digit counts to 80 % so they fit the cell. Also set the record in the same serif as the rest of the episode, or justify Inter as an "exhibit" face consistently.
9. [0:00–0:13, 3:01–3:11][Visual] The cold open and landing are top-heavy. The box row sits at y ≈ +1.6 and the lower 55 % of the frame is empty (kf_01, sheet 11). Centre the group vertically: the hidden row at y ≈ +1.2, the tiles at 0, "questions per character ?" at −1.2. Use the same layout on return so the landing reads as the cold-open frame re-seen.
10. [2:56–2:58][Motion] The cold-open row cross-fades in on top of the dimmed record, a double exposure of boxes over digits (f 2:57). Fade the record fully out except "THE OTHER DAY", fly that phrase into the row first, and only then bring the boxes in under it.
11. [1:37–1:41][Visual] "Rare ones narrow and tall" cannot be seen in the settled skyline. J, Q, X and Z are under a pixel wide, so the tallest visible column is about 7.5 (kf_22) and the 10.3 Z only shows during the 1 s yellow flash at 1:39. Give columns a minimum drawn width of 6 px, with a footnote "widths below 0.5 % exaggerated", or add a 3× inset of the right tail labelled "Z 10.3".
12. [0:59–1:01][Visual] The five most frequent symbols flash YELLOW (f 0:59.6), but yellow means questions or bits. Flash them with a white outline plus a BLUE brighten, and save yellow for the 48 % cut.
13. [0:27][Motion] A stray yellow dash and dot at about (300,578) px and a mark at (300,808) appear while the halving diagram is still on screen. These are the chart's dashed line and axis being created early. Start creating the chart only after the tiles start dropping, or Create the axes from the origin.
14. [1:55–2:27][Visual] The right gutter stacks "4.11", "4.75" and "≈1" within about 60 px of each other. Two labels sit at almost the same height (crops at 2:20.8 and 2:26.7), so the column is busy. Once "That beats 4.75" is said (2:00), fade the ghost 4.75 line and label to 30 %, or move the ghost label to the left of the y-axis.
REACHES 9 IF ALL FIXED: yes. The structure is right: a committed prediction by 0:11, a naive 4.75, a measured failure, the doubling-strip derivation, context as the second fix, Shannon's record as payoff, and a landing that resolves the hidden character. What is missing is execution: one hard overlap (cap), two missing picture-to-number moves (area→H levelling, guess counts→bits) and label/band hygiene on the chart. Fixes 1–6 are required; 7–14 polish Visual from 7.5 to 9.
KEEP:
- The halving chain that closes on Y at 0:21, paid off when Shannon's subject guesses that same Y first time (2:59–3:03), followed by "Five questions is the price of a letter with no past."
- The E "what's still possible" strip that doubles with a live yellow counter (1:07–1:23), then TransformFromCopy into p·2^k = 1 → k = log2(1/p) (1:25–1:33).
- U swallowing the bar and then collapsing to the floor (2:13–2:21), and the live 0→79/102 first-guess tally driven by the moving cursor (2:29–2:39).
```

## Notes behind the scores

- **Hook 8.5.** A concrete puzzle and an explicit question by 0:11, followed by a 2.0 s prediction hold (0:11.1–0:13.1). The likely answer, 5 or 4.75, is then contradicted by Shannon's ≈1 at 0:26–0:32, and tension rises through 4.11 ("still 4×") to context. The ending resolves the opening exactly. Held back from 9 because the first frame is 12 empty grey boxes in the top third of an otherwise empty frame, and the stakes line (compressors, LLMs, 0:32–0:40) is never shown or returned to.
- **Clarity 8.** Concrete first throughout, and log2(1/p) is genuinely derived from the doubling picture. There are two steps a viewer must take on faith: area = average (fix 2) and guess counts → 0.6–1.3 bits (fix 4). The 2:17–2:27 band occlusion also makes the context bars hard to read (fix 3).
- **Visual 7.5.** The palette is semantic and held consistently: blue p, yellow questions/bits, green Shannon, purple context. Citations are bottom-left above y = −3.2 and type sizes are adequate (ticks about 25–30 px cap height at 1080p). There are more than two minor issues, though: strips inside the plot (fix 5), a long-lived band over every bar (fix 3), digit collisions (fix 8), top-heavy open and close (fix 9), invisible tall slivers (fix 11), yellow misuse (fix 12) and a crowded right gutter (fix 14). On top of these is the capped overlap (fix 1).
- **Motion 8.** Objects persist: the context row lives from 0:00 to 2:27 and the chart from 0:28 to 2:27. Most transforms carry meaning: tiles to equal columns, widths to probabilities, 4.75 heights to the log2(1/p) skyline, U widening then flattening, and record letters flying into the boxes. Deductions: the 4.11 line slides in rather than emerging from the area, there is a double-exposure cross-fade at 2:57, stray early-draw marks at 0:27, and one hard cut at 2:28, which is allowed at a beat boundary. Static never exceeds 3.53 s.
- **Audio 8.** 161 wpm, −14.0 LUFS, −1.9 dBTP, no silence over 2 s. Deictics land: E strip 1:05.6 → 1:07, five flash 0:59–1:01, "U swallows the bar" 2:13.6 → 2:13, context flash at "nothing came before it" 2:04.4, tally reaching 79 at 2:39 on "79 of 102". Deductions: the garden-path phrasing at 0:43 (fix 7), and "in a hundred" heard as "and 100" at 2:12.5, which suggests a swallowed "in a".
- **Concision 8.5.** 502 words, with almost nothing removable. The stakes sentence (0:32–0:40) is the only slack: it is asserted and never paid off.
- **Originality 9.** The hidden Y foreshadowed by the halving path and paid off with Shannon's own record is a memorable, non-obvious frame for entropy. The doubling strip is a fresh way to make log2(1/p) concrete.
