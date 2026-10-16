EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: If you score the flip after each heads row by row and then average the rows, a fair coin reads below one half (17/42), because every row gets one vote and checked heads crowd into a few rows. The same bias puts a random shooter at −8 points on the 1985 hot-hand test, so Cornell's +4 is really +12.
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 8 · Audio 8.5 · Concision 8 · Originality 8
WEIGHTED: 8.1   AFTER CEILING: 8.1 (lowest 8 + 2 = 10, so the ceiling does not bind)
CAPS: none. Checked each one: no runtime, pace, loudness, silence or static violation; layout audit 0 issues over 198 frames; no typos or broken LaTeX found in 40 keyframes plus 25 extra extracted frames; 0 banned phrases; every empirical claim has an on-screen citation.
FINAL: 8.1   PASS: no

Reviewer: craft critic (visual design, motion, A/V sync), round 1. Evidence: the review/ pack (metrics.json is newer than final.mp4, so no regeneration was needed). I read all 11 contact sheets and 12 full-resolution keyframes (kf_03, 06, 08, 14, 17, 21, 24, 25, 33, 36, 40 and others via the sheets), plus 25 extra frames I extracted with ffmpeg at 1:44.5–1:52.8, 2:07.5, 2:11, 2:18.5, 2:20.5, 2:35.5, 2:42.5, 2:44, 2:55, 3:01–3:02, 3:13–3:14.9. Contrast was measured on pixels.

## FACTS
| Claim | Status | Source |
|---|---|---|
| 4 flips → 16 equally likely sequences | Verified | 2^4; check_numbers.py |
| HHTH: the flips after a heads are H, T → 1/2 (0:04.6) | Verified | enumeration |
| HHHT "checks three flips, two are heads" → 2/3 (0:41.5; the boxed row at 0:43 is HHHT) | Verified | enumeration |
| TTTT, TTTH get no score; 14 scored rows | Verified | enumeration |
| Score distribution 0×6, ½×4, ⅔×1, 1×3; mean 17/42 = 40.5% | Verified | recomputed: (3 + 2/3 + 2)/14 = 17/42 |
| "Cold by nine and a half points" | Verified | 50 − 40.48 = 9.52 |
| Pooled: 24 checked flips, 12 H, 12 T | Verified | enumeration |
| 12 heads in 8 rows; 12 tails across 11 rows | Verified | enumeration |
| After a tails: 25/42; gap of the two averages −19 points | Verified | 17/42 − 25/42 = −4/21 = −19.05 |
| GVT 1985, Cognitive Psychology; "a powerful and widely shared cognitive illusion" | Verified | GVT 1985 17(3):295–314, quoted in Miller & Sanjurjo 2018 |
| 26 Cornell players, up to 100 shots, from a distance where they hit ~50% | Verified | GVT Study 4 via M&S §3.1 and Table 2 (three players took 90/75/50) |
| Random shooter, n = 100, k = 3: 46% / 54%, gap ≈ −8 | Verified | M&S 2018 §3.2; exact DP in check_numbers.py (0.4603 / 0.5397, −7.94) |
| Bias grows with streak length and shrinks with record length (ghost ticks −1.0, −3.1, −8; −0.7 at 1,000 shots) | Verified | M&S abstract; DP output |
| Cornell 49% after 3 hits, 45% after 3 misses, +4; measured from −8 it is +12 | Verified | M&S 2018 §3.2–3.3 |
| The gym result does not establish the effect in defended games | Verified (fair hedge) | M&S §3.1, fn. 22 |
| Miller & Sanjurjo 2018, Econometrica | Verified | Econometrica 86(6):2019–2047 |

No wrong or fabricated claims. One wording problem (not a factual error) is listed under Clarity, fix 2.

## MECHANICS
runtime 3:15.1 · wpm 154 (speech time; 149 overall) · max silence 2.07 s (0:11.7–0:13.8, the planned prediction pause) · max static 3.87 s (0:10.0–0:13.8, the same pause) · −14.0 LUFS / −2.1 dBTP · leading silence 0.00 s, trailing 0.89 s · WER 0.6% · 0 black frames · 0 layout-audit issues.

## Dimension notes (evidence)

**Hook 8.5.** The concrete object is on screen at 0:00 (HHTH flipping in). The arcs and rings make the procedure visible at 0:02–0:07. The 16-row ghost collapses into a "?" on the axis while "What do you get?" is spoken at 0:11.9, followed by a 2 s hold, so the viewer commits by 0:12. The stakes ("called the hot hand an illusion", with the verbatim quote) land at 0:25. The landing re-uses the cold-open frame and answers the "?" with 17/42 at 3:05–3:07, which is an exact resolution. What keeps it from 9: tension sags at 2:07–2:21. Cornell's design is read out over two empty lanes with "?" values (see Visual).

**Clarity 8.** The order is concrete first (one row, then 16 rows, then the scores, then the line). The failure is measured (−9.5 points). The mechanism (one vote per row) gets its own picture, and the gym-versus-game limit is stated. Deductions:
- At 1:56–2:00, "So after a tails, the test reads **hot**". "Hot" was defined at 0:27–0:30 as beating your usual rate *after hits*. Calling the after-tails reading "hot" uses the episode's key word for a different quantity, at exactly the moment the viewer has to keep two lanes apart.
- 1:33.9–1:43.3: "Twelve heads crowd into eight rows. Twelve tails spread across eleven. Line up the votes…" The counts 8 and 11 do not visibly produce 17/42. The causal step (fewer rows means fewer votes per heads) is left for the viewer to infer while three things animate at once. This took me a rewatch.
- The only general formula, (1/14)Σhᵢ/nᵢ = 17/42 against Σhᵢ/Σnᵢ = 12/24, is on screen for about 3 s and never returns (see Motion). The viewer cannot re-derive what it says after one watch.

**Visual 8.** One flat background and a strict semantic palette that I checked across the whole episode: yellow = heads/hit, grey = tails/miss, blue = what the test reads, red = bias, purple = Cornell. The 1/2 is split yellow over blue at 0:07, and that split carries through every score in the table, which is excellent. Type sizes clear the minimums at full resolution, and everything sits inside the safe area. Deductions:
- 1:41–1:50 (kf_24 at 1:48.2): six competing elements are in one frame. The full 16-row table, the pooled strip, the vote strip, "40.5%", "the obvious guess" and two stacked equations at the right edge. There is no single focal point at the climax of the insight.
- 2:09–2:21 (frame at 2:11.0): the frame is nearly empty. Two grey hairlines, the blue cursors stacked on the dashed line (hiding it), an axis with no tick labels for about 3 s, and "?" values. The header "Cornell, 1985" is built left-of-centre (x ≈ 430–755 px) with the right half empty, and re-centres only later. The lane labels still read "after heads / after tails" until about 2:18, while the narration has been about basketball since 2:07.
- Contrast: the secondary grey text (axis titles, ticks, both citations, "every flip: 1/2 heads") measures 6.1–6.5:1 against the background (pixel 145,150,158 on 20,21,26). The bar is 7:1.
- 2:21–2:41: the purple "Cornell, 1985" header stays at full strength over a chart that holds only the random-shooter baseline. Purple means Cornell data, and none is on screen until 2:41.

**Motion 8.** Objects persist almost throughout. The big HHTH row shrinks into its slot of the 4×4 table (0:37–0:41). Scores become dots, the dots fall onto the line, and the marker slides to its balance point with a live 40.5% (0:53–1:00). Checked coins become tiles and the tiles become 12/24 (1:10–1:15). Each row is resized to one vote, and the yellow parts slide left and stop exactly on the 40.5% marker (1:18–1:41), so here the animation really is the proof. The copy flips about the 50% line (1:53–1:56). The two-lane chart is relabelled into the difference axis by sliding (2:31–2:33). Deductions:
- 1:43–1:50: the equations are built from swarms of glyphs flying out of the table (stray "2", "0 1" fragments mid-flight at 1:46.5). Σhᵢ/Σnᵢ = 12/24 is complete at about 1:47.5 and fading by 1:50.3, a hold of roughly 2.5–3 s. The §5 rule is 2 s + 0.4 s per term, about 3.6 s. Then the equations are gone for good.
- 0:17–0:32: about 15 s on one composition where the only events are text appearing (citation, quote, "→ hot"). The coin → hit/miss morph comes at 0:26.3 on "Heads are hits", but "basketball shots" (0:21.7) gets no visual change.
- 2:11–2:21: about 10 s where the only motion is header phrases writing on and one pulse on the 50% tick.

**Audio 8.5.** 154 wpm, −14.0 LUFS, −2.1 dBTP, WER 0.6%. Deictics land: "Here, one of the two" at 0:04.6 coincides with the rings; "This row" at 0:41.5 gets its box by 0:42.5; "this row's three heads" at 1:28.1 is boxed at 1:29; "this lone tails" at 1:31.1 is boxed on HTTT, with its segment boxed in the strip, by 1:32.5. Pauses are placed on purpose (0:11.7 prediction, 2:35.7 and 3:00.5 section breaks). Whisper heard "Sanjorjo's" at 2:27.9, which is probably a slightly off vowel in "Sanjurjo" (the Spanish is roughly "san-HOOR-ho"). Minor.

**Concision 8.** Most lines earn their place. There is one double explanation. 1:15.9–1:21.0, "each row gets one vote, however many flips it checked", is restated at 1:43.3–1:45.5 as "That's one vote per row." "Tails crowd the same way" (1:49.1) and "Swap heads and tails" (1:51.7) also say the same thing twice in a row.

**Originality 8.** The vote strip (HHHH's three heads squeezed into one vote and HTTT's lone tails stretched to a whole one) is a memorable image I have not seen in the Upshot or Numberphile-style treatments of Miller–Sanjurjo. The ghost ticks with ●/●●/●●● flags are also good. The topic itself is well covered elsewhere, and the 2:07–2:21 setup reads like a generic chart.

## FIXES (highest impact first)
1. [1:43–1:51][Motion + Clarity] The episode's only formula pair lives for about 3 s and vanishes before "Tails crowd the same way". Change: complete (1/14)Σhᵢ/nᵢ = 17/42 by 1:46 and Σhᵢ/Σnᵢ = 12/24 by 1:47.5, then hold both untouched for at least 3.6 s. During that hold, Indicate (≤ 1 s) the "1/14 Σ" and the "Σ…/Σ" so the one structural difference flashes. When the mirror opens, don't fade them. TransformMatchingTex the 17/42 into the "after heads 17/42" lane label, and bring a compact "(1/14)Σ hᵢ/nᵢ" back next to the 17/42 marker in the landing (3:05). That raises Motion and Clarity.
2. [1:56–2:00][Clarity] Replace "So after a tails, the test reads hot: twenty five out of forty two" with "So after a tails, the test reads high: twenty five out of forty two." Keep "hot" for after-hits readings only, which matches the definition at 0:27.
3. [2:07–2:21][Visual + Motion + Hook] Replace the empty-lane stretch with the episode's own grammar at basketball scale. On "twenty six Cornell players: up to a hundred shots each", deal one strip of 100 small hit/miss tiles above the lanes, labelled "one simulated 100-shot record". On "After three hits", put blue rings on the shots that follow each ●●● run, reusing the cold-open arc and ring style. On "versus after three misses", ring the shots after each ○○○. Then collapse the strip into the two lanes as the cursors move 50 → 46 / 54. Also: relabel the lanes to "after 3 hits / after 3 misses" at 2:07.6 (not at 2:18–2:20), keep the 40–60% tick labels visible throughout, and build the header centred from its first phrase.
4. [1:41–1:50][Visual] Give the climax one focal point. Once the 11 tails rows' outlines finish (about 1:41), dim the table to 30%. Fade the text "the obvious guess" (keep the dashed line), and move the two equations into the space the dimmed table frees (top right), at least 0.15 units clear of the pooled strip.
5. [1:33.9–1:43.3][Clarity] Make "crowding" quantitative where it is said. When the 8 heads rows are outlined, write a yellow "12 heads ÷ 8 votes" beside them, and for the tails rows a grey "12 tails ÷ 11 votes". Then "Line up the votes" visibly follows from the split. (facts.md already has 0.47 vs 0.69 votes per checked flip, if a number is wanted.)
6. [0:21.7–0:27][Motion] Move the H → "hit" / T → "miss" morph (and the axis retitle) to "basketball shots" at 0:21.7, so the picture changes when basketball is named. "Heads are hits" at 0:26.3 then gets a pulse on the morphed row instead of a fresh event.
7. [whole episode][Visual] Raise the secondary grey (axis titles, ticks, citations) from about #91969E to about #A6ABB3 so it measures at least 7:1 on the background. Re-check the "the obvious guess" contrast hierarchy afterwards.
8. [1:43.3–1:45.5][Concision] Cut "That's one vote per row." (it repeats 1:18), and let the 14 outlines draw and fly into the ink 1/14 under "Count all the flips together first…". Also merge "Tails crowd the same way. Swap heads and tails, and…" into "Swap heads and tails, and the strip flips over one half."
9. [2:21–2:41][Visual] Dim the purple "Cornell, 1985" header to 30% while only the random-shooter baseline is shown, and restore it to full on "Cornell's players" (2:41.2), so purple appears exactly when Cornell data does.
10. [2:27.9][Audio] Respell "Sanjurjo" phonetically in narration_text.py for Kokoro (for example "San-hoor-ho") and re-check the transcript.

REACHES 9 IF ALL FIXED: yes. The structure is right: commit-able hook by 0:12, a measured failure (−9.5), one transforming picture (the vote strip), a cited payoff with an honest limit, and a landing that answers the opening frame. What remains is craft. Fixes 1, 3 and 4 move Motion and Visual to 9, fixes 1, 2 and 5 move Clarity to 9, and fix 3 also removes the mid-episode sag in Hook. With those, the weighted score is about 8.9–9.1.

KEEP:
- The vote strip (1:18–1:41). Each row resized to one equal vote, HHHH squeezed and HTTT stretched, then the yellow sliding left and stopping exactly on the 40.5% marker.
- The mirror. The after-tails copy turns a half turn about the dashed 50% line (1:53–1:56), and the two-lane chart slides into the difference axis (2:31–2:33).
- The landing returns to the exact cold-open frame and answers its "?" with the 17/42 marker (3:02–3:15). The yellow-over-blue 1/2 colour code runs through every score.
