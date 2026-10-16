# Round 1 review: substance (science and story editor)

Evidence used: `review/` pack (metrics.json 12:20 is newer than final.mp4 12:19), so no new pack was generated. I read report.md, all 11 contact sheets and keyframes kf_06, kf_08, kf_14, kf_25, kf_37 and kf_39 at full resolution. I also pulled 8 extra full-resolution frames (1:01.0, 1:12.8, 1:35.5, 1:41.5, 1:51.0, 2:17.0, 2:29.5, 2:45.0) and two 4 fps tiles (1:11–1:15 and 2:15.5–2:19). I read the transcript, script.md, facts.md, narration.txt and check_numbers.py. Every number was recomputed independently: the 16 sequences by exact enumeration, and the streak gaps by my own Monte Carlo runs (separate code and seeds from check_numbers.py). Citations were checked against the GVT 1985 PDF (colorado.edu copy) and the Miller & Sanjurjo paper (Wharton copy, JSTOR 44955325).

```
EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: Averaging the after-heads share sequence by sequence gives each sequence one vote, and heads-after-heads crowd into few sequences, so even a fair coin reads 17/42 instead of 1/2; the 1985 hot-hand test had the same bias, and measured from the right baseline (−8) Cornell's +4 becomes +12.
SCORES: Hook 8.5 · Clarity 8 · Visual 8 · Motion 8 · Audio 8 · Concision 8 · Originality 8.5
WEIGHTED: 8.1   AFTER CEILING: 8.1
CAPS: Factual/mathematical error (cap 6) → on-screen "1,000 shots: −0.75 (simulated)" and ghost marker plotted at −0.75 @ 2:28–2:34; the expected gap is −0.70 (see FACTS)
FINAL: 6.0   PASS: no
FACTS:
- 4 fair flips → 16 equally likely sequences | Verified | 2^4, enumeration
- HHTH: checked flips 2 (H) and 3 (T) → "one of the two is heads", 1/2 | Verified | enumeration
- TTTH, TTTT get no score; 14 rows scored | Verified | enumeration
- HHHT "checks three flips, two are heads" → 2/3 | Verified | enumeration
- Table h/n labels (16 rows at 0:57.7) and dot stacks: 0×6, ½×4, ⅔×1, 1×3 | Verified (every row checked in kf_14) | enumeration
- Mean of 14 row scores = 17/42 = 0.40476 ("about 40.5%", "0.405") | Verified | (3 + 2/3 + 2)/14 = 17/42
- "Reads cold by nine and a half points" (50 − 40.48 = 9.52) | Verified | arithmetic
- Pooled: 24 checked flips, 12 H / 12 T → exactly ½ | Verified | enumeration (ΣH = 12, Σn = 24)
- "Twelve heads crowd into eight rows; twelve tails across eleven" | Verified (8 yellow boxes @ 1:41.5, 11 white boxes @ 1:45) | enumeration
- Heads hold Σhᵢ/nᵢ = 17/3 of 14 votes = 17/42 | Verified | arithmetic
- GVT 1985, Cognitive Psychology 17(3):295–314; quote "a powerful and widely shared cognitive illusion" | Verified, quote verbatim | GVT 1985 Discussion (colorado.edu PDF)
- 26 Cornell players (14 men, 12 women), ~100 shots each ("up to 100") | Verified | Miller & Sanjurjo 2018 §3.1
- Cornell: .49 after 3 hits vs .45 after 3 misses → +4; GVT read it as no hot hand | Verified | M&S 2018 §3.1 ("players on average hit .49 when on a hit streak, versus .45 when on a miss streak")
- Random shooter, n = 100, p = .5: expected gap ≈ −8 points | Verified | M&S 2018 ("the expected difference (and the strength of the bias) is -8 percentage points"); my sim −7.90 (40k seqs)
- "Measured from −8, it's 12 points hot" | Verified | M&S 2018 ("+12 percentage points higher than ... a Bernoulli i.i.d. shooter")
- Miller & Sanjurjo 2018 · Econometrica 86(6):2019–2047 | Verified | JSTOR 44955325, arXiv 1902.01265
- "Longer records shrink the bias" | Verified | M&S 2018 abstract
- "1,000 shots: −0.75 (simulated)" | WRONG (small, but on screen and plotted) | Two independent 10⁶-sequence simulations (n = 1000, k = 3, p = .5, both streak types defined): −0.703 ± 0.006 and −0.708 ± 0.006; a 2×10⁵ run gives −0.689 ± 0.014. The true value is ≈ −0.70. facts.md's −0.75 comes from a 40k-rep run (s.e. 0.03), so it is Monte Carlo noise printed to two decimals and about 7 true s.e. from the target.
- "A 50% shooter who scores one half here is already running hot" | Defensible only as an average over many 4-shot records; read literally about one row (HHTH, which is on screen), it overclaims | see Fix 7
MECHANICS: runtime 3:06.3 · wpm 153 (speech time; 149 overall) · max silence 2.07 s (planned prediction hold at 0:12.3) · leading 0.00 s / trailing 1.74 s · max static 3.37 s (2:18.5, planned hold) · −14.0 LUFS / −2.1 dBTP · 0 black frames · WER 0.7%
```

## Transcript and slop scan

- §4 banned phrases: 0. Patterns: no "not just X", no rhetorical-question chains (the questions at 0:11 and 2:18 each stand alone and are followed by a hold), no fake colon reveals, no empty superlatives. The ending reframes the cold open and is not a recap list. "One half is what a fair coin does. Seventeen out of forty two is what this test sees." restates, but it earns its place by re-seeing the 0:00 frame.
- Hook: the commit lands at 0:11.3 ("What do you get?") with a "?" over the 0–1 line, a 2.1 s hold, and then the stake (GVT 1985 + quote) at 0:18–0:27. That is on template.
- Script vs audio: only "nine and a half" heard as "9.5" and "a hundred" heard as "100", which is harmless. Sanjurjo and Cornell are transcribed correctly, so pronunciation is fine.
- Deictics land: "This row checks three flips" puts a box on HHHT at 0:49. "This row's three heads" boxes HHHH and its first vote segment at 1:35. "this lone tails" boxes HTTT and its segment at 1:39.

## Dimension notes (evidence)

- **Hook 8.5.** The concrete puzzle is on screen in frame 1 and the viewer commits by 0:12. The ending re-sees the opening (3:02, HHTH with 17/42 vs the dashed guess). Deduction: the first 12 s are pure procedure ("After every heads, check the next flip… Average that share over every possible sequence"), which is abstract on first hearing, and the reason to care arrives only at 0:18.
- **Clarity 8.** The mechanism is canonical and correct: one vote per row, and checked heads come in crowds. The derivation is concrete first: 16 rows, 14 dots, balance point, then the strip and then the formula. The skipped step is the jump from the 4-flip P(H | H) vs ½ demo to the 100-shot "after 3 hits − after 3 misses" gap (2:04–2:28). The viewer is never told that the same crowding pushes the after-misses rate *up* (E ≈ .54) while the after-hits rate drops (E ≈ .46), which is why the gap is −8 and why 100 shots is "not long". They cannot re-derive −8. The closing line is also ambiguous (Fix 7).
- **Visual 8.** The semantic palette is consistent: yellow is H, blue is the test, red is the bias, purple is Cornell. Each frame has a clear focal point and charts are labelled. Issues: "cold −9.5 points" is readable for only about 1.5 s and ends about 15 px from the blue 0.405 line (1:12.8–1:14.7). The ghost label at 2:29.5 is centred about 2.3 units right of its marker and is low-contrast grey. The axis title renders the subtraction as an em-dash ("after 3 hits — after 3 misses", 2:19–2:51). The HHHH highlight box top sits at y ≈ 47 px, outside title-safe (1:35.5). In "1/14 Σᵢ" (1:53.9) the 1/14 and i use a heavier white weight than hᵢ/nᵢ.
- **Motion 8.** Objects persist and transform well: ringed coins fly into 24 tiles, the strip regroups into 14 equal votes, and the yellow parts slide onto 0.405 (1:47). The row scores also fly from the table into the formula (1:51). Deduction: the axis change at 2:16.7–2:17.4 is a crossfade, not the scripted re-scale. For about 0.75 s, old and new tick labels and both axis titles are superimposed ("0.75+10", "share of checked flips that are heads" over "after 3 hits…"), and the blue line cuts through "random shooter" (frame 2:17.0).
- **Audio 8.** Pace is 153 wpm, loudness is on target, silences are intentional, and deictics are in sync. The synthetic cadence is acceptable. With no audible evidence of a defect beyond normal TTS flatness, this stays at 8.
- **Concision 8.** 17/42 is spoken four times. Two of those come within 4 s of each other: "heads hold seventeen out of forty two" (1:48) and "Averaging the fourteen row scores gives seventeen out of forty two" (1:52). The 1:50–1:57 pair of sentences re-announces results already shown at 1:03 and 1:16. Otherwise it is tight.
- **Originality 8.5.** The resized-votes strip, where HHHH's three heads are squeezed into one vote and a lone tails is stretched to a whole one, is a non-obvious picture I have not seen in the NYT or Numberphile treatments. The coin-flip frame is intrinsic to the Miller–Sanjurjo result rather than lazy.

```
FIXES (highest impact first):
1. [2:28–2:34][Clarity/correctness] "1,000 shots: −0.75 (simulated)" and its ghost marker are wrong; E[gap] at n = 1000, k = 3, p = .5 is −0.70 (two 10⁶-sequence sims: −0.703, −0.708, s.e. 0.006) → relabel "1,000 shots: about −0.7 (simulated)", move the marker to −0.70, raise reps in check_numbers.py to ≥ 10⁶ and update facts.md row 18. Removes cap 6.
2. [2:18–2:28][Clarity] −8 appears with no mechanism linking it to the coin demo → after the 1.5 s hold, slide two small blue markers: "after 3 hits" from 50 to 46 and "after 3 misses" from 50 to 54 (M&S / own sim: .460 and .539), and say "The same crowding drags the after-hits score down and pushes the after-misses score up, so the gap opens to about minus eight." Then the gap marker lands on −8. Pay for the ~5 s with Fix 4.
3. [2:16.6–2:17.5][Motion] Crossfade of the 0–1 axis into the −10…+15 axis superimposes both tick sets and both axis titles, and the blue line crosses "random shooter" → first FadeOut the 0–1 ticks, title and "0.405 random shooter" (0.4 s), then ReplacementTransform the dashed ½ line into the dashed 0 line ("the obvious guess" carries over), then Write the new ticks and title. No frame should show two label sets at once.
4. [1:50–1:57][Concision] "Averaging the fourteen row scores gives seventeen out of forty two. Pooling the counts first gives one half." repeats 1:48 and 1:16 → replace with one line over the two formula builds: "Score rows first, you get seventeen forty-seconds; pool flips first, you get one half." Or build the formulas silently under the existing 1:48 sentence. Saves about 4 s.
5. [1:12–1:16][Visual] "cold −9.5 points" finishes writing after it is spoken and dims at about 1:14.7 (readable ≈ 1.5 s, below the 2.0 s needed for 4 words), and its last glyph is about 15 px from the blue 0.405 line → start the Write on "reads cold", hold until 1:16.2, and place the label under the red arrow with buff ≥ 0.2.
6. [2:28–2:34][Visual] Ghost label is centred about 2.3 units right of its marker and drawn in dim grey (below 4.5:1) → put it directly above the −0.7 marker, left of the dashed 0 line, at ≥ 4.5:1 contrast; or drop the marker and keep only the spoken "longer records shrink the bias".
7. [3:00–3:05][Clarity] "A fifty percent shooter who scores one half here is already running hot" literally calls one 4-shot row (HHTH, on screen) hot → "A fifty percent shooter whose rows average one half here is already running hot." The arrow animation stays as is.
8. [0:00–0:12][Hook] The cold open is a procedure with no stakes until 0:18 → make line 4 concrete and visible: "Do it for all sixteen possible sequences and average." Flash the 16-row grid ghosted at 15% behind the "?" so "every possible sequence" points at something. Optionally move "the test that 'proved' the hot hand an illusion" into the 0:12–0:14 hold.
9. [2:19–2:51][Visual] Axis title "after 3 hits — after 3 misses (points)" shows an em-dash where a minus is meant, and "points" is ambiguous → MathTex "after 3 hits − after 3 misses (percentage points)" with a true minus sign.
10. [1:35–1:38][Visual] The HHHH highlight box (with arcs) reaches y ≈ 47 px, outside 5% title-safe → shift the 16-row table down 0.1 units or reduce the box buff.
11. [1:53–2:51][Visual] In "1/14 Σᵢ hᵢ/nᵢ" the 1/14 and the i subscript are in a heavier white weight than the rest → render the whole expression in one MathTex with the series math style, with 1/14 in the neutral ink colour.
REACHES 9 IF ALL FIXED: yes, narrowly. Fix 1 removes the cap, which leaves 8.1 on the dimension scores. Fix 2 (the after-misses half of the mechanism) is the one that lifts Clarity, the 25-weight dimension, to 9. Fixes 3–6 lift Motion and Visual to about 8.5–9, and Fix 4 lifts Concision to 9. The structure (commit, naive test, measured failure, one picture, real payoff, re-seen open) already matches the template, so no structural change is needed.
KEEP: (1) the one-vote strip, 1:27–1:49: HHHH's three tiles squeezed into one vote, the lone tails stretched to one, and the yellow sliding exactly onto 0.405. (2) The landing back on the HHTH row with 17/42 vs the dashed "obvious guess" (2:53–3:05). (3) The honest payoff: verbatim GVT quote, real +4 measured from −8 with the +12 brace, and "evidence, not proof".
```
