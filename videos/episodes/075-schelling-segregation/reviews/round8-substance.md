EPISODE: 075 — "Mild Preferences, Segregated Towns"
IDEA: In a Schelling town, households that demand only a third of their neighbors match still sort into a 76 %-matching town, because every departure costs a content neighbor a match and tips it; so a segregated map cannot tell you what its people wanted.
SCORES: Hook 9 · Clarity 8.5 · Visual 8.5 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 8.8   AFTER CEILING: 8.8 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none
FINAL: 8.8   PASS: no

Evidence used: review/ pack (metrics.json 23:58 is newer than final.mp4 23:56), report.md, all 12 contact sheets, keyframes kf_01, 03, 10, 16, 20, 24, 26, 28, 31, 33, 36, 39 at full resolution, extra frames at 1:09.0, 2:44.8, 2:46.9, 3:03.0, transcript, narration.txt, script.md, facts.md, sim_output.txt, plus my own scratch run of sim.py (below).

FACTS: <claim> | Verified/Wrong/Unverifiable | <source>
- "three-quarters of a household's neighbors match" / 76 % meter | Verified | sim_output: final share 0.7553
- Rule: content iff same/occupied ≥ ⅓, empties not counted; "happy to be outnumbered two to one" | Verified | s/(s+d) ≥ ⅓ ⇔ d ≤ 2s; boxed example 2 of 6 (0:19)
- Random start "half the neighbors match" | Verified | 0.4992
- "these 238 are unhappy" | Verified | sim_output; sum of red ladder bars 23+15+23+11+23+76+67 = 238
- "Round one, 200 moves"; note "38 content by their turn" | Verified | round1 breakdown 200 moved / 38 content before turn / 0 stuck
- "stalls at 74" | Verified as a number (74 after round 1); the verb is loose (see fix 4) | sim_output unhappy by state [238, 74, 41, 16, 9, 2, 1, 0]
- "67 of these were content before round one. They never moved." | Verified | "never unhappy at start: 67"; only start-of-round unhappy households move
- Chain: B 3/8 → 2/7 after A leaves (r1); C 3/8 → 2/7 after B leaves (r2); 3/8 > ⅓ > 2/7 | Verified | chain states in sim_output; 0.375 > 0.333 > 0.286
- "After round seven nobody wants to move" | Verified | 7 rounds, moves 200, 72, 41, 16, 9, 2, 1
- ¼ → 58 %, ⅓ → 76 % (same start) | Verified | 0.5787, 0.7553; 30-town means 0.584 / 0.749
- Ladder counts 67 (2/7), 125 (3/8), 76 (¼ = 66 at 2/8 + 10 at 1/4), 256 (½) | Verified | share ladder line in sim_output
- "At a quarter … Only these two bars change sides. Just 95 start unhappy" | Verified | 238 − 76 − 67 = 95; shares equal to the demand are content
- "Now a household at 3/8 can lose a match and stay. So that chain never starts." | Verified as stated, but incomplete as the explanation of the jump (see fix 1) | 2/7 ≥ ¼ and 2/8 ≥ ¼; chain households never move at ¼
- Schelling 1971 ran this model; nearest satisfactory square; 25–30 % vacancies; rapid rise "from about 35% to 50%", slight at one third | Verified | Schelling, "Dynamic Models of Segregation", J. Math. Sociology 1(2):143–186 (1971); web search hit on the paper PDF (acoustique.ec-lyon.fr) shows "moves to the nearest vacant spot that surrounds him with a neighborhood that meets his demands", "rising function of demands in the range from about 35% to 50%", "the segregation that results is slight when the demand is for…"
- On-screen "Schelling, 1971 · Journal of Mathematical Sociology" | Verified | as above
- "1930s federal lending maps raised racial segregation for decades. Its authors point to reduced credit." | Verified | Aaronson, Hartley & Mazumder, "The Effects of the 1930s HOLC 'Redlining' Maps", AEJ: Economic Policy 13(4):355–92 (Nov 2021); abstract on aeaweb.org: "increased racial segregation in later decades … These results suggest … through reduced credit access and subsequent disinvestment"
- On-screen "Aaronson, Hartley & Mazumder, 2021 · AEJ: Economic Policy" | Verified | as above
- Two towns both 76 %, one with no preferences | Verified | zoned town 0.7553, 100 % in own-colour zone
- "As Schelling argued, … the map alone could not have told you" | Verified (paraphrase) | abstract: inferences about individual motives "can usually not be drawn from aggregate patterns"; the two-town test supports the stronger "could not" for this map

MECHANICS: runtime 3:30.9 · 153 wpm (speech time; 137 overall) · max silence 2.09 s (0:09.1, planned prediction hold) · max static 3.63 s (0:03.9) · −14.0 LUFS / −1.9 dBTP · leading 0.00 s, trailing 1.77 s · WER 0.2 % ("block's" heard as "blocks") · 0 banned phrases · 0 layout issues · 13/13 deictics land

## Dimension notes

**Hook 9.** Frame 1 (0:00) is the finished town with "76% match"; "How much matching do these households demand?" lands at 0:06.7–0:08.9 with a 2.1 s hold and "? demanded" on screen (sheet 1, 0:09), so the viewer commits before the reveal at 0:10.8. "So how can a demand of one-third build a town of three-quarters?" (0:26.8) is the one driving question, and 3:21–3:30 restores the exact opening frame with "? demanded" (kf 3:30.2 against kf 0:06.6). This is the anchor for a 9. A small nit in the build: "The obvious plan is to move each one…" (0:43) implies a planner the model does not have.

**Clarity 8.5.** Every number checks out (above), and the domino (1:05–1:33) is exemplary: real tiles, real moves, 3/8 → 2/7 built from the squares. The deduction is for the insight beat itself, 2:10–2:33. The narration and the arrow "lose one match → still content" (kf 2:32.5) explain the ⅓-vs-¼ jump by the robustness of the tall 3/8 rung ("All 125 households at 3/8 are one lost match from 2/7… Now a household at 3/8 can lose a match and stay"). Each sentence is true. As an explanation of *why the curve jumps*, though, it is selective. I recomputed it on seed 3's start with sim.py's own `init`/`same_occ`:
- Content households one vacated match away from tipping: **210 at ⅓** (1/3: 47, 3/8: 125, 2/5: 38) against **190 at ¼** (1/4: 76, 2/7: 67, 1/3: 47). At ¼ the fragile edge moves down a rung and is almost as large. "That chain never starts" holds for our chain, but the 2/7 and ¼ rungs now play the 3/8 rung's role.
- The real difference is the spark. At ⅓ the 238 first movers include the two tall bars (2/7, ¼), households that each have one or two matching neighbors, so their leaving strips **274** matches from content same-color neighbors and would tip **70** of them outright. At ¼ the 95 movers are near-loners (≤ 1/5): **62** matches stripped, **21** tipped. The total cascade agrees: 341 moves for 238 initial movers at ⅓ against 105 for 95 at ¼.

A viewer who re-derives the episode's argument would conclude "at ¼ nobody is one loss from tipping", which is false: 190 are. The chain beat already shows the right mechanism (A, at 2/7, *had* gold neighbors to lose), so the ladder should land on that.

**Visual 8.5.** The palette is disciplined: purple is always demand, red always unhappy, ink always outcome. The single-focus frames are strong (kf 0:16.1, 1:24.1, 2:08.6). Two misses against §5:
- (a) The HOLC frame (3:09–3:20, kf 3:10.6) carries 15 prose words: "0 demanded · placed by a rule" (5), "⅓ demanded" (1), "76% match" ×2 (2), "simulated" (1), and the citation (6). The limit is 12.
- (b) From 2:42 to 2:46 the "our jump" bracket sits unlabeled at 82 % (frame 2:44.8) after its tag fades on "nearest". For about 3 s it is an anonymous mark, and it then slides away.

Everything else is clean: no overlaps, citations bottom-left above y = −3.2, and the y-title "neighbors matching (%)" is intact (kf 1:42.6; the contact sheet's timestamp badge hides its first letters).

**Motion 9.** Objects persist and transform throughout. Tiles fly home on "Rewind" (0:33–0:35). The round-1 hops land one by one into the stall (0:52–0:56). The real corner rewinds into the inset (1:05–1:09). The town flies into its chart dot (1:41–1:43). The chart's x-axis becomes the ladder baseline (1:55–1:57). The caret slides across exactly two bars (2:19–2:23), and the band sweeps on "between … a half" (2:46.9 → 2:48.7). Nothing I saw is decorative.

**Audio 9.** Pace is 153 wpm, loudness −14.0 LUFS, peak −1.9 dBTP, and all 13 deictics land within the window. The pauses are shaped: 2.1 s after the prediction question, 1.5 s before "Only these two bars", 1.2 s before the last sentence. The only transcript slip is "blocks" for "block's" (2:07.6), which is an apostrophe, not a mispronunciation.

**Concision 9.** 467 words in 3:31 with no recap, and each sentence is pointed at a visible object. The only lines I would rewrite rather than cut are the two mechanism sentences (fix 1).

**Originality 9.** Three choices make this episode its own. The blind two-town test (2:49–3:06) turns Schelling's abstract into something the viewer fails. The real-tile domino replay is the second, and the town that literally becomes one point on the chart is the third. None of them is stock.

FIXES (highest impact first):
1. [2:10–2:33][Clarity] The ladder explains the ⅓-vs-¼ jump by the 3/8 rung's fragility, but at ¼ there are 190 content households one lost match from tipping (1/4, 2/7, 1/3 rungs) against 210 at ⅓, so fragility is not what changes. What changes is who moves first and how many matches they take with them (274 stripped / 70 tipped at ⅓ against 62 / 21 at ¼, seed 3, departures left empty). Keep "All 125 … one lost match from two sevenths" (2:10–2:16) as the ⅓ picture. Then replace 2:20.9–2:32.9 ("Only these two bars change sides: just ninety-five start unhappy. Now a household at three eighths can lose a match and stay, so that chain never starts.") with: "Only these two bars change sides: just ninety-five start unhappy. And these two bars were the movers with matches to lose. At a quarter they stay, so their neighbors keep their matches, and our chain never starts." On screen, on "matches to lose", flash the two bars (2/7, ¼) and the two gold neighbors in A's patch. On "stay", A's 2/7 ≥ ¼ flashes (already built). Re-point the grey arrow from the 2/7 bar to the 3/8 bar and relabel it "keeps its match" (drop "still content", which implies the whole fragile edge is safe). Optionally add one GRAY count pair under the ladder, "matches taken: 274 → 62". Verify 274/62 in sim.py first (my scratch: for every content household, count its same-color neighbors that are unhappy at the start; sum). Raises Clarity to 9.
2. [3:09.0–3:20.0][Visual] 15 prose words on the HOLC frame (kf 3:10.6) against the 12-word limit. On "One study" (≈3:09.0), fade "· placed by a rule" (it has already pulsed on "rules too") and the centre "simulated" tag (both towns were tagged simulated at 2:49) to 0 over 0.4 s. That leaves 9 words. Together with fix 3 this raises Visual to 9.
3. [2:41.5–2:46.0][Visual] The "our jump" bracket sits unlabeled at 82 % for about 3 s (frame 2:44.8). Keep the tag "our jump" visible until the bracket starts to slide on "There" (2:44.6). To keep the frame at ≤ 12 words, shorten the rules label pair to "nearest move · 25–30% empty" on one line, or drop "Journal of" from the citation to read "Schelling, 1971 · J. Math. Sociology" (the venue stays identifiable).
4. [0:54.1–0:58.0][Clarity] "The unhappy count stalls at seventy-four." The count does not stall over the run: it falls 238 → 74 in round one and on to 0 by round seven (1:37). The failure is "not zero, and not mixed". Change it to "The unhappy count stops at seventy-four, not zero." and keep the live landing of the last 12 hops. Also pulse the 64 % meter on "not zero", so the second half of the plan's failure ("the town stays mixed": 50 % → 64 %) is pointed at, not just visible.
5. [0:43.2–0:51.6][Hook] "The obvious plan is to move each one…" implies a planner; in the model the households move themselves. Change it to "The obvious guess: each one moves to a random empty square where it would be content, and the town stays mixed." The word count is unchanged and the "plan predicts 0" row can read "guess: 0".

REACHES 9 IF ALL FIXED: yes. Fixes 1–3 lift Clarity and Visual to 9, which gives weighted 9.0 with no caps. Fix 1 is the one that matters: it is a story-level correction to the insight beat, not polish, and it should be re-verified in sim.py before it is spoken.

KEEP:
- The opening frame and its exact return: "? demanded" on the 76 % meter at 0:09 and again at 3:21–3:30.
- The real-tile domino (1:05–1:33): the corner rewinds into the inset, and 3/8 → 2/7 is built from the actual squares, in step with the board.
- The blind two-town test (2:49–3:06) as the bridge to Aaronson, Hartley & Mazumder and to the landing line.
