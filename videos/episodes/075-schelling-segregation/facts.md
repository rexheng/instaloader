# Episode 75 — fact check

Every number on screen or in the narration, how it was verified, and its source.
Simulation numbers come from `sim.py` (this directory, numpy + scipy, deterministic);
`python sim.py` reprints them (output saved in `sim_output.txt`). scene.py re-derives the
key ones from sim.py at render time and `assert`s them (238, 95, 200/38/0, 74/67/7, the chain
fractions, 2 of 6, both towns at 76 %).

## Simulation set-up (stated on screen as "simulated")

| Item | Value | Note |
|---|---|---|
| Board | 40 × 40 squares, no wrap-around | Schelling also used a bounded board (13 × 16) |
| Empty squares | 10 % (160) | Schelling used 25–30 % |
| Households | 720 blue, 720 gold, placed uniformly at random | equal groups, as in Schelling's first runs |
| Neighbors | occupied squares among the 8 around a household (fewer at edges); empty squares are not counted | Schelling 1971 p.155: "the eight surrounding squares"; on screen: grey × on the empties + "empty: not counted" |
| Content if | same / occupied ≥ demand | demand = ⅓ in the main run |
| Move rule | each round, households unhappy at the start of the round move (in random order, if still unhappy) to a uniformly random empty square where they would be content | Schelling moved to the *nearest* such square |
| Town shown | seed 3 | chosen as typical: its final share 0.755 vs 30-town mean 0.749 |

## Claims

| # | Claim (narration / screen) | Value | Verification | Source |
|---|---|---|---|---|
| 0 | "If fewer than a third of them match, it moves" (round 3; replaces "Every household … is free to move") | rule | every household may move whenever it is unhappy (move rule above). Round 1 wording "Everyone … chose where to live" was replaced: only 341 moves happen, so ≥ 1,099 of 1,440 households never left their random start (critic right) | sim.py |
| 1 | "In this simulated town, on average, three quarters of a household's neighbors match its color"; meter drawn at 76 % (round 3: it no longer counts up from 0 %) | 0.7553 | sim, final state of seed 3 (mean over households of same / occupied neighbors) | sim.py |
| 2 | "Each household counts the occupied squares around it. If fewer than a third match, it moves" (round 5 cont.; was "a third of them") | rule | definition of the simulation; empties excluded (denominator = occupied neighbors); content iff same/occupied ≥ ⅓, so it moves iff the share is < ⅓ | sim.py `same_occ` |
| 3 | "…so it is happy to be outnumbered two to one" | ⅓ same ⇔ 2:1 | same/(same+diff) ≥ 1/3 ⇔ diff ≤ 2·same. Boxed example: gold household at row 15, col 15 of the final town has 2 gold, 4 blue, 2 empty neighbors → "2 of 6 match" (asserted in scene.py) | sim.py |
| 4 | Random start: on average half of neighbors match; meter 50 % | 0.4992 | sim, seed 3 initial state | sim.py |
| 5 | "Still, these two hundred thirty-eight are unhappy" (round 5 cont.: "about one in six" cut for the word budget; 238/1440 = 16.5 % is no longer spoken; cycle 2: "So most households are content" cut as a restatement); RED counter counts to 238 as the rings draw | 238 / 1440 = 16.5 % (1 in 6.05) | sim | sim.py |
| 6 | "Round one takes two hundred moves; the other thirty-eight were content by their turn." (round 5: "The matching share jumps to sixty-four percent" cut; the meter still climbs to 64 % live) HUD row "moves" counts live to 200; GRAY note "38 content by their turn" on "thirty-eight" (cycle 2, substance fix 5: the 238 vs 200 gap is now spoken, so the note no longer competes with the narration) | 200; 38; 0.6441 | `round1_breakdown()`: of the 238, 200 moved, **38 were content when their turn came** (other households' moves had changed their neighborhood), 0 found no acceptable square; asserted in scene.py | sim.py |
| 7 | After round one the unhappy counter reads 74, not 0 ("plan predicts 0") | 74 | sim | sim.py |
| 8 | "sixty-seven of these were content before round one. They never moved."; on screen 67 RED rings kept, 7 turn grey, "67 content at the start" | 67 of 74 | 67 of the 74 were content at the start; only households unhappy at the start of a round move in it, so none of the 67 moved in round 1 (asserted in scene.py). The other 7 were unhappy at the start (6 moved and are unhappy again, 1 was fixed before its turn and tipped again) | sim.py |
| 9 | Gold household B (row 4, col 14): 3 gold of 8 before round 1 → 2 gold of 7 after neighbor A (row 4, col 15) leaves; nothing else in its neighborhood changes | 3/8 = 0.375 ≥ 0.333; 2/7 = 0.286 < 0.333 | sim, checked square by square (patch changes per round: r1 A leaves; r2 B leaves, a blue household arrives at A's old square, outside C's and D's neighborhoods; r3 C leaves; r4 D leaves) | sim.py |
| 10 | B leaves in round 2; C (row 3, col 13) goes 3/8 → 2/7 ("In round two, our household leaves, and this one drops to two sevenths"). Round 5 cont.: the third step was cut from narration and screen; for the record: "Then the next one, also at three eighths, tips in round three" (round 5 wording; round 3 had "Then the next one, at three eighths, [pause] tips"): D (row 3, col 12) has 3 gold of 8 after round 2, C leaves in round 3, D goes 3/8 → 2/7 (leaves in round 4) | — | `verify_chain()` ("after round 2: D (2, 3, 8)", "after round 3: D (2, 2, 7)") | sim.py |
| 10a | The board's corner replays in step with the inset (round 2: B → (28, 37), household 1144 from (31, 34) into A's old square (4, 15); round 3: C → (32, 1)) | real moves | `rounds[1]`, `rounds[2]` filtered to the patch: exactly these 3 moves touch rows 2–5 × cols 11–15 in rounds 2–3; both destinations were empty at the start of their round, so showing them early never overlaps a tile (asserted in scene.py) | sim.py |
| 11 | "Now run the whole town. After round seven, nobody wants to move." (cycle 2: "Round after round, the tipping spreads" and "Seventy-six percent, the town we started with" cut; the rounds play in a 1.8 s pause and the meter shows 76 %) ; HUD "moves" shows each round's moves live | moves per round 200, 72, 41, 16, 9, 2, 1; unhappy after each round 74, 41, 16, 9, 2, 1, 0; 0.7553 | sim (round 7 still has 1 mover, so "after round seven" is exact) | sim.py |
| 12 | Chart: 30 simulated towns per demand (on screen: "each dot: one simulated town"; cycle 2 cut the spoken "Thirty towns at each demand, from zero to sixty percent"); INK tick = mean, GRAY whisker = min–max. On "a quarter" / "a third" the PURPLE ¼ / ⅓ fly from the thumbnail labels to their columns, which brighten while the others dim to 40 % | 0 → 0.500; 0.1 → 0.514; 0.2 → 0.569; ¼ → 0.584 (0.565–0.613); ⅓ → 0.749 (0.716–0.781); 0.4 → 0.822; 0.5 → 0.867; 0.6 → 0.965 | sim, seeds 0–29 | sim.py |
| 13 | Same starting town at demand ¼: "barely sorts: fifty-eight percent" | 0.5787, 6 rounds, 105 moves | sim | sim.py |
| 14 | Share ladder: "Sort the random start by each household's share of matching neighbors. With at most eight neighbors, these are the only shares up to sixty percent." Bars at every share that occurs, 0–60 %, with the ends marked "0%" and "60%" (round 3: the old "only these values occur" ignored the cut at 60 %) | 0: 23, 1/8: 15, 1/7: 23, 1/6: 11, 1/5: 23, 1/4: 76, 2/7: 67, 1/3: 47, 3/8: 125, 2/5: 38, 3/7: 138, 1/2: 256, 4/7: 129, 3/5: 48 | `share_ladder(init(3))`. With n ≤ 8 occupied neighbors a share is k/n; the 14 distinct values k/n ≤ 0.6 are exactly the 14 bars (every one occurs). No household of seed 3 has 0 occupied neighbors | sim.py |
| 14a | "At a third, everyone left of it is unhappy"; on screen "unhappy 238" (round 5 cont.: the number is no longer spoken a second time) | 238 | sum of the bars with share < ⅓ (= claim 5) | sim.py |
| 14a′ | Counts shown above bars: 67 (2/7), 125 (3/8), 76 (¼) | 67, 125, 76 | `share_ladder(init(3))`; asserted in scene.py | sim.py |
| 14a″ | "Every household at three eighths is one lost match away from it" (it = two sevenths); GRAY arrow 3/8 → 2/7 "lose one match" (shown only while the demand is ⅓; it fades out as the demand slides to ¼) | 3/8 → 2/7 | arithmetic: 3 matching of 8 occupied; one matching neighbor leaves and its square is empty → 2 of 7 (exactly the chain's steps B, C, D). If an unlike household later moves into that square it is 2/8 = ¼; both 2/7 and ¼ are < ⅓ (unhappy) and ≥ ¼ (content), so the arrow's meaning holds either way. Not claimed: that nobody is one lost match from unhappiness at ¼ (2/7 → 1/6 still tips at ¼); the narration only speaks of the 3/8 rung | arithmetic |
| 14b | "including the neighbor that started our corner's chain, at two sevenths"; patch 2/7 < ⅓ built from A's 3×3 at the start (2 gold, 5 blue, 1 empty) | A = (4, 15): 2 gold of 7 | `verify_chain()` row "after round 0": A (2, 2, 7); asserted in scene.py | sim.py |
| 14c | Prediction "At a quarter, how many would start unhappy?" (counts 238 / 67 / 76 on screen), then "Only these two bars change sides, and they're tall: now just ninety-five start unhappy" ("rungs" was never defined: round 3) | rungs in [¼, ⅓): ¼ (76 = 66 at 2/8 + 10 at 1/4) and 2/7 (67); 238 − 76 − 67 = 95 | arithmetic + `report_extra()`: "unhappy at start: demand 1/4 -> 95 / demand 1/3 -> 238; rungs in [1/4, 1/3): 1/4: 76, 2/7: 67". A share equal to the demand is content (≥), so at ¼ the ¼ rung is content | sim.py |
| 14d | "and that chain never starts"; A's formula flips to 2/7 ≥ ¼ | 0.286 ≥ 0.25 | re-running the same start at ¼: none of A, B, C, D ever moves (`verify_chain()`: "demand 1/4: chain households that ever move: []") | sim.py |
| 14e | Transitional formula states never show a stale or false inequality | — | every departure (A, B, C) and the "?" + 30 %-dimmed numbers are one animation; the new fraction resolves on the narration cue; at ¼ the threshold and relation change together | scene.py `pending()` / `resolve_to()` |
| 15 | "In his 1971 paper, Thomas Schelling ran this model" (round 2's "by hand, on a checkerboard" was cut for concision; still true) | — | JMS 1971 p.154: "divide the area into squares like a checkerboard"; p.155: "what is reported here has all been done by hand and eye". His version differs (nearest move, more vacancies), as the next sentence says. The narration does not say he *first* ran it in 1971: the paper's footnote (p.143) says it was issued as RAND memo RM-6014-RC in May 1969 | Schelling 1971, *J. Math. Sociology* 1(2):143–186 |
| 16 | "His households moved to the nearest suitable square, on emptier boards" (round 5 cont.; the on-screen rules label "nearest move · 25–30% empty" was cut: it repeated the narration and does not fit at the Text-27 label floor) | nearest satisfactory square; "25 % to 30 % vacancies" (ours: 10 %, random destination) | JMS 1971 pp.154–155: "moves to the nearest vacant spot that surrounds him with a neighborhood that meets his demands"; "25 % to 30 % vacancies allows fair freedom of movement" | Schelling 1971 |
| 17 | "and there the jump came later, between about a third and a half"; GRAY bracket "our jump" over ¼–⅓ (our step: 58 → 75 %) slides to the band "Schelling: 35–50%" (round 5 cont.; was "Schelling's jump: 35–50%") (cycle 2: the band is hatched and our dots dim to 35 % while it shows, so it reads as his result, not ours; his rules are one label, "nearest move · 25–30% empty") | — | JMS 1971 p.159: segregation is "a rapidly rising function of demands in the range from about 35 % to 50 %"; at about one-third the segregation "is slight". Our own check (scratch, not shown): nearest-square moves with 30 % empty give 0.64 at ⅓, 0.71 at 0.4, 0.78 at ½ (vs 0.75 at ⅓ with random moves), consistent with his milder, later rise | Schelling 1971 |
| 18 | (Round 3: the spoken quote "He wrote that inferences about individual motives can usually not be drawn from aggregate patterns" was cut for concision; its source now carries the landing, claim 22.) Abstract text: "inferences about individual motives can usually not be drawn from aggregate patterns" | verbatim | JMS 1971 abstract, p.143 | Schelling 1971 |
| 19 | The test: "Two simulated towns, both seventy-six percent. In one town, households demand a third. In the other, nobody minds their neighbors at all." (cycle 2: "In the other" was rushed and whisper dropped "other"; the new split was synthesized and transcribed correctly by whisper on its own clip). Reveal: right = our seed-3 town ("⅓ demanded"), left = "0 demanded · placed by a rule", zone lines drawn; "The other was placed by a rule, with no preferences at all"; GRAY "simulated" between the towns | 0.7553 vs 0.7553 → both 76 % | `zoned_town()` (cycle 2 rule, seed 73): 160 empty squares at random; a fine random field (Gaussian σ = 1.1 squares plus 0.1 white noise) cut at its median over the occupied squares marks each square for one colour (exactly 720 / 720); **every household lives in a zone of its colour**. Nobody has a demand and nobody moves. The grain was chosen so the *texture* matches a Schelling town, not just the 76 % (substance fix 3: the old rule, 92 % compliance on coarse zones, left stray single tiles and smooth blobs a viewer could spot). `texture_stats()`: Schelling town 11 clusters, 0 of ≤ 3 households, 582 unlike pairs, 0 % below ⅓; rule town 26 clusters, 4 of ≤ 3 households, 519 unlike pairs, 3.1 % below ⅓ (the old rule: 53 clusters, 41 of ≤ 3, 6.6 % below ⅓). It is a toy rule, labelled simulated; it is *not* a model of HOLC, only a demonstration that a 76 % map needs no preference at all | sim.py |
| 20 | "In real cities, one study finds that 1930s federal lending maps increased racial segregation for decades, through reduced credit." (round 5 cont.: one sentence; "through reduced credit" is the abstract's own mechanism, "through reduced credit access and subsequent disinvestment". Before: "…for decades. It traces this to reduced credit in the areas marked in red.") (round 3: two sentences, subject next to its verb; the mechanism is attributed to the study, "It traces this to…") | — | Abstract (re-read on aeaweb.org, Oct 2026): "The maps led to reduced home ownership rates, house values, and rents and increased racial segregation in later decades … These results suggest the HOLC maps had meaningful and lasting effects on the development of urban neighborhoods through reduced credit access and subsequent disinvestment." The D grade was drawn in red ("redlining"). The mechanism is now stated (credit), and the toy rule is no longer described as "a rule about where each color could buy", which wrongly implied the maps assigned residence by race (substance critic, round 2: right). HOLC = Home Owners' Loan Corporation, a federal agency. Attributed to "one study" because the size of the maps' own causal role is debated (e.g. Fishback et al. argue HOLC itself lent in red-graded areas); the claim is exactly the cited paper's finding On screen (cycle 2, substance fix 4): the zone-line pulses on "increased" and "credit" were removed, because they equated the toy rule with the HOLC mechanism; on "1930s" both toy towns dim to 30 %, the "76% match" labels pulse on "decades", and the citation is underlined on "traces" | Aaronson, Hartley & Mazumder 2021, *AEJ: Economic Policy* 13(4):355–92, doi:10.1257/pol.20190414 |
| 21 | Plan preview arc | round-1 move #34: gold household (23,18) → (21,34) | a real move from the simulation, drawn as the dashed preview and later flown on the same arc | sim.py |
| 22 | "Look again at the first town. As Schelling argued, whatever you guessed its people demanded, the map alone could not have told you." | — | "As Schelling argued" paraphrases claim 18 (abstract: inferences about individual motives "can usually not be drawn from aggregate patterns"); the specific "could not" for this map is what the two-town test shows (claim 19: the same 76 % map, with a matching texture, arises from demand ⅓ and from demand 0; substance fix 3 asked for exactly this or a weaker line, and the rule town was regenerated); claim 1 | Schelling 1971; sim |

## Round 1 critic claims, re-verified (Oct 2026)

| Critic claim | Verdict | Action |
|---|---|---|
| "Everyone … chose where to live" is imprecise (≥ 1,099 never moved) | right | narration now "Every household … is free to move" |
| Stale "3/8 ≥ 1/3" beside a patch already showing 2/7 (B→C and C→D steps) | right | departure + "?" + dimmed numbers are one animation (claim 14e) |
| "Why the jump" explained by one chain only; 95 vs 238 initially unhappy | right (95 and 238 reproduced) | new share-ladder beat (claims 14–14d) |
| "Extreme Segregation" overclaims | right | title "Mild Preferences, Segregated Towns" |
| 238 unhappy vs 200 moves unexplained | right (38 fixed before their turn, 0 stuck) | GRAY note "38 fixed by neighbors' moves" (claim 6) |
| "thirties" transcribed as "thirty s" | not a mispronunciation | whisper writes "1930s" (round 1 and round 2 transcripts); the review kit normalizes "1930s" to "nineteen thirty s", which mismatched the script word "thirties". The narration text now writes "1930s" (misaki reads it "nineteen thirties"), so script and transcript normalize identically |

## Round 2 critic claims, re-verified (Oct 2026)

| Critic claim | Verdict | Action |
|---|---|---|
| Rung labels "1/4" and "2/7" touch or cross the x-axis; "2/7" sits between two bars (both critics, cap 7) | right | Rung fractions now sit in a row under the axis, ≥ 0.17 below the axis and the ticks. Counts sit centred above their own bars (`next_to(bar, UP, buff=0.15)`), and scene.py asserts ≥ 0.15 between neighbouring labels. The demand is a short tick, so no label shares a column with a tall line |
| Ladder bars read against the % y-axis and the PURPLE "demanded" x title (both) | right | % y-axis, its title, the x numbers, the dots and the random-mix line fade to 0; the x title becomes INK "share of neighbors matching"; all are restored for the Schelling beat |
| HOLC bridge implies the maps were a rule about where each color could buy (substance) | right | new sentence with the credit mechanism (claim 20) |
| "until round seven, when nobody wants to move" is off by one (substance) | right | "and after round seven, nobody wants to move" (claim 11) |
| Board focus box stale during the replay (both) | right | the board's corner replays with the real tiles and moves (claim 10a) |
| Every number otherwise verified (both critics re-ran sim.py) | — | unchanged |

**Transcript note (this revision's review kit, WER 0.4 %).** Two whisper slips are not pronunciation errors:
- **"aggregating" for "aggregate" (3:14).** misaki tags "aggregate" here as an adjective (JJ) and phonemizes it /ˈæɡɹəɡət/, not as the verb /ˈæɡɹəɡˌAt/. The same sentence's audio transcribed correctly in round 2.
- **"be." (2:46).** This is a 20 ms token (166.58–166.60 s) inside the planned 1.2 s prediction silence.

## Round 3 critic claims, re-verified (Oct 2026)

No factual errors were claimed. Both critics recomputed every number (238, 95, 200/38, 74/67, the chain fractions, the sweep) and verified Schelling 1971 and Aaronson et al. 2021 by web search. Points of precision that changed:

| Critic point | Verdict | Action |
|---|---|---|
| "only these values occur" overstates: the ladder stops at 3/5 (substance 7) | right: 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8 and 1 also occur above 60 % | "these are the only shares up to sixty percent", with "0%" and "60%" marked at the ends (claim 14) |
| After the slide to ¼ the 3/8 → 2/7 arrow lands on a grey bar and implies nobody is one loss from tipping (substance 2) | right about the implication (at ¼ the 2/7 rung is one loss from 1/6 or 2/8, and 1/6 < ¼) | the arrow and its label fade out during the slide (claim 14a″) |
| The HOLC sentence garden-paths (both) | right (prosody, not fact) | claim 20 rewritten; Kokoro word timings show no internal break (0.05 s max gap inside each sentence) |

## Deliberately not claimed
- That Schelling found strong segregation at a demand of one third (his hand runs at about
  one third gave only slight segregation; the narration says his jump came later).
- That mild preferences cause real-world segregation (the two-town test and claim 20 are the
  counterweight); that the toy zoning rule models HOLC.
- The 2005 Nobel prize (awarded to Schelling and Aumann for game theory of conflict and
  cooperation, not specifically for this model) — omitted.
- Exact positions of the tipping point: they depend on vacancy, move rule, neighborhood size
  and board size; the chart is labelled "simulated" and its rules are in narration/beat 4.

## Round 1 critic claims, second review cycle (Oct 2026)

Neither critic claimed a factual error; both re-ran sim.py and verified Schelling 1971 (35–50 %, "slight" at one third, nearest move, 25–30 % vacancies) and Aaronson, Hartley & Mazumder 2021 by web search. Precision points:

| Critic point | Verdict | Action |
|---|---|---|
| "the map alone could not have told you" overclaims: the rule town's smooth blobs and stray tiles differ from the Schelling town (substance 3) | right about the old rule town | rule regenerated to match the texture (claim 19, `texture_stats()`); the landing line is kept |
| Zone-line pulses on "increased" / "credit" equate the toy rule with HOLC (substance 4) | right | pulses removed; towns dim under the HOLC sentence (claim 20) |
| 238 unhappy vs 200 moves never explained (substance 5) | right | spoken clause + live "moves" row + note (claim 6) |
| "other" dropped by whisper at 3:15 (both) | likely rushed prosody | line re-split and re-synthesized; whisper transcribes "In the other, nobody minds" (claim 19) |
| Schelling's band over our dots reads as his data (both) | right | hatched band, our dots at 35 % (claim 17) |

## Round 5 (Oct 2026): re-verification and transcript notes

The round-5 reviews (identical to the second cycle's round-1 reviews) claimed no factual error;
both critics re-ran sim.py and verified both citations. Nothing factual changed. Wording changes:

| Change | Check |
|---|---|
| "Then the next one, also at three eighths, tips in round three" | `verify_chain()`: D (row 3, col 12) has 3 gold of 8 after round 2 ("after round 2: D (2, 3, 8)") and 2 of 7 after round 3, when C leaves ("after round 3: D (2, 2, 7)"); so D tips (becomes unhappy) in round three and leaves in round 4. "also" refers to C, which had 3/8 too (claim 10). The on-screen caption at that moment is "after round 3" |
| Cut "The matching share jumps to sixty-four percent" | the meter still shows 64 % (0.6441) after round 1; no number is spoken any more |
| On screen: the two "76% match" labels pulse on "segregation" (was "decades") | the labels are the segregation measure of the two toy towns; the towns stay dimmed, so the pulse ties the study's word to our measure without equating the toy rule with the maps (claim 20) |

**Transcript slips that are whisper's, not the voice's.** The first round-5 master's full-track
whisper (Groq whisper-large-v3-turbo) wrote "3 is more than a third" for "Three eighths is more
than a third" (1:23) and "It ips" for a pause-isolated "tips" (1:48). Kokoro's own timings place
"eighths" at 0.35 s (83.52–83.87 s). Re-synthesized on their own and sent to the same whisper,
both lines transcribe word for word ("…out of eight. Three eighths is more than a third, so it
stayed." and "…Then the next one, at three eighths. Tips."). "tips" was still rewritten so it
never starts a clip after a pause (the new line transcribes as "…also at 3 eighths, tips in round
three.").

**Round 5, continued (Oct 22).** The narration was cut from 526 to about 483 words for the new
concision budget (PRODUCTION_GUIDE §13: ≤ 500 words, 3:15–3:35); claims 2, 3, 5, 10, 14a, 16, 17
and 20 above record each wording change. No number, simulation result or citation changed. The Aaronson, Hartley & Mazumder
abstract was re-read on aeaweb.org (doi 10.1257/pol.20190414): "The maps led to reduced home
ownership rates, house values, and rents and increased racial segregation in later decades", as
claim 20 says.

**Round 5, continued (2).** No narration, number or citation changed. On screen, the random-mix
dashed line no longer returns on the Schelling chart (it had lost its label there), and round-one
hops stay on the board. Schelling 1971 was re-checked once more against the paper's PDF text
(p.155: a dissatisfied household "moves to the nearest vacant spot that surrounds him with a
neighborhood that meets his demands"; segregation is "a rapidly rising function of demands in the
range from about 35% to 50%"), as claims 16 and 17 say.

## Round 6 (Oct 2026): re-verification and new wording

Neither round-6 critic claimed a factual error. Both recomputed the numbers from `sim_output.txt` and checked Schelling 1971 (35–50 %, "slight" at about one third, nearest move, 25–30 % vacancies) and Aaronson, Hartley & Mazumder 2021 by web search. The wording and screen changes below were checked against `sim.py` again (scratch run, Oct 22).

| # | New or changed claim (narration / screen) | Value | Verification | Source |
|---|---|---|---|---|
| R6-1 | "Every household at three eighths is one lost match away from two sevenths." (was "… away from it": the pronoun reached back a sentence) | 3/8 → 2/7 | arithmetic, as claim 14a″ | arithmetic |
| R6-2 | "Only these two bars change sides: just ninety-five start unhappy. Now a household at three eighths can lose a match and stay, so that chain never starts." On screen the 3/8 → 2/7 arrow stays through the caret's slide to ¼, lands on the now-grey (content) 2/7 bar, and gains the label "still content" under "lose one match" | 2/7 = 0.286 ≥ ¼; 2/8 = ¼ ≥ ¼ | One lost match takes a 3/8 household to 2/7 (the matching neighbour's square is left empty) or, if an unlike household later fills that square, to 2/8. Both are ≥ ¼, so content at a demand of ¼ (a share equal to the demand is content). At ⅓ both are < ⅓ (unhappy), which is exactly the B → C link. Re-running the same start at ¼: none of A, B, C, D ever moves (`verify_chain()`: "chain households that ever move: []"). "and they're tall" was cut: the count falling 238 → 95 shows it. Still not claimed: that no household at ¼ is one loss from unhappiness (2/7 → 1/6 tips at ¼); the line speaks only of the 3/8 rung | sim.py, arithmetic |
| R6-3 | "With at most eight neighbors, shares come in steps." (was "… these are the only shares up to sixty percent") | 14 rungs up to 3/5 | a share is k/n with n ≤ 8, so it takes only discrete values; the ladder shows the 14 that occur up to 60 %, with the ends marked "0%" and "60%" (claim 14) | sim.py |
| R6-4 | HUD "moves" row is cumulative: 200 after round one, then 272, 313, 329, 338, 340, 341 | 341 | `sim.run(3, 1/3)`: moves per round 200, 72, 41, 16, 9, 2, 1 (sum 341); asserted in scene.py. Not spoken. For reference, the same start at ¼ makes 105 moves (82, 16, 3, 2, 1, 1) | sim.py |
| R6-5 | The blind test: our town is shown turned a quarter turn (90°) and turns back as it grows home on "Look again at the first town"; both towns still "76% match" | 0.7553 rotated = 0.7553 | the 8-square neighbourhood and the square board are symmetric under a 90° turn, so every household keeps the same neighbours: `avg_share(np.rot90(gF))` = 0.75534 = `avg_share(gF)` (checked, also for −90°) | sim.py |
| R6-6 | "Real segregation has other causes. One study finds that 1930s federal lending maps increased racial segregation for decades, through reduced credit." (was "In real cities, one study finds …") | — | the new first sentence ("other" = other than the preferences the model is about; it follows "with no preferences") is the episode's own framing of the cited result (a non-preference mechanism, credit, raised segregation); it does not say the toy rule models the maps, and the toy towns dim under it. The study sentence is unchanged (claim 20) | Aaronson, Hartley & Mazumder 2021 |
| R6-7 | "Replay one block." / "… our block's chain" (was "corner": the patch, rows 2–5 × cols 11–15 of 40, is not a board corner; whisper heard "corners") | — | patch coordinates in scene.py (`PATCH_R`, `PATCH_C`) | scene.py |
| R6-8 | "The obvious plan is to move each one to a random empty square where it would be content, so the town stays mixed." (merged; "Then everyone is content" cut) | — | the HUD row "plan predicts 0" (unhappy) now arrives on "content"; claim 7 unchanged | sim.py |
| R6-9 | "In his 1971 paper, Thomas Schelling ran this model." kept as it was | — | a shorter "In 1971, Thomas Schelling ran this model" was considered and rejected: it would date the runs to 1971, but the paper was first issued as RAND memo RM-6014-RC in May 1969 (claim 15) | Schelling 1971 |
| R6-10 | Dot chart: the 30-town dots are drawn at 60 % opacity with ± 0.3 pp horizontal jitter (was 38 %, ± 0.6 pp); the small PURPLE ¼ / ⅓ column marks are gone | — | display only; the jitter is horizontal and only separates overlapping dots of one column (all dots of a column share the same demand) | sim.py |
| R6-11 | "Two gold out of seven, less than a third, so now it wants out." (was "Two gold out of seven. Two sevenths is less than a third, …"); "In the other, nobody minds their neighbors." (was "… at all") | 2/7 = 0.286 < 0.333 | claim 9; cut for the runtime budget (the fraction 2/7 < ⅓ is on screen) | sim.py |

## Round 7 (Oct 2026): re-verification and new wording

Neither round-7 critic claimed a factual error (both recomputed every number from `sim_output.txt` and checked both citations by web search). The substance critic flagged one wording nit: "finds … through reduced credit" turned the abstract's "suggest" into a finding. That is right and is fixed (R7-6). The two citations were re-checked on Oct 22 2026: the Schelling 1971 PDF (copies at pdodds.w3.uvm.edu and acoustique.ec-lyon.fr) reads "moves to the nearest vacant spot that surrounds him with a neighborhood that meets his demands" and "25% to 30% vacancies allows fair freedom of movement without making the board too empty"; the aeaweb.org abstract of Aaronson, Hartley & Mazumder (doi 10.1257/pol.20190414) reads "The maps led to reduced home ownership rates, house values, and rents and increased racial segregation in later decades. These results suggest the HOLC maps had meaningful and lasting effects on the development of urban neighborhoods through reduced credit access and subsequent disinvestment."

| # | New or changed claim (narration / screen) | Value | Verification | Source |
|---|---|---|---|---|
| R7-1 | "Round one: two hundred moves. The unhappy count stalls at seventy-four." (replaces "Round one takes two hundred moves; the other thirty-eight were content by their turn" and "If the plan had worked, this counter would read zero. It reads seventy-four."). On screen the last 12 hops of round one land one by one; the RED count reads 82 after move 188 and then 81, 80, 78, 76, 75, 76, 75, 75, 74, 74, 74, 74; it freezes at 74 as "moves" reaches 200. The GRAY note "38 content by their turn" is kept, now unspoken | 200 moves; 74 | unhappy count after each round-1 move, recomputed from `sim.run(3, 1/3)` (scratch, Oct 22): it falls roughly linearly from 238 and the last four moves leave it at 74. "Stalls" describes round one: the plan promised 0 after it (claim 7); later rounds still lower the count (41, 16, 9, 2, 1, 0, claim 11) | sim.py |
| R7-2 | "All one hundred twenty-five households at three eighths are one lost match from two sevenths." (was "Every household at three eighths is one lost match away from two sevenths.") | 125 at 3/8 | `share_ladder(init(3))`: 3/8 → 125. Every such household has 3 matching neighbours, so each can lose one; with the square left empty it is at 2/7 (if an unlike household later fills it, 2/8 = ¼; both < ⅓), as claim 14a″ | sim.py, arithmetic |
| R7-3 | Ladder: GRAY count "256" above the ½ bar (the height scale); y title "households" (was "households (simulated start)") | 256 | `share_ladder(init(3))`: ½ → 256, the tallest bar among the 14 shares ≤ 3/5 (asserted in scene.py). The board is tagged "simulated" from frame 1 and the narration calls the ladder "the random start" | sim.py |
| R7-4 | "His households moved to the nearest square that suited them, on far emptier boards." On screen GRAY "nearest move" (on "nearest") and "25–30% empty" (on "emptier"), under "Schelling: 35–50%" | his 25–30 % vacancies vs our 10 % (160 of 1,600 squares) | Schelling 1971 (PDF text above). "Far emptier": 25–30 % is 2.5–3 × our 10 %. "a quarter empty" was not used: "a quarter" is a demand level in this episode | Schelling 1971 |
| R7-5 | "There the jump came later, between about a third and a half." (now its own sentence; claim 17 unchanged) | 35–50 % | as claim 17 | Schelling 1971 |
| R7-6 | "Real cities have rules too. One study finds that 1930s federal lending maps raised racial segregation for decades. Its authors point to reduced credit." (was "Real segregation has other causes. One study finds … increased racial segregation for decades, through reduced credit.") | — | "raised … for decades" = the abstract's "increased racial segregation in later decades"; "Its authors point to reduced credit" = "These results suggest … through reduced credit access and subsequent disinvestment" (critic right: the mechanism is suggested, not found). "Rules" means institutional rules (the federal maps graded neighbourhoods for mortgage lending); it does not say the maps assigned households to places, and the toy rule town is not presented as a model of them (only its header pulses on "rules too"; the towns dim under the study) | Aaronson, Hartley & Mazumder 2021 |
| R7-7 | "Two simulated towns." (was "Two simulated towns, both seventy-six percent."); the two "76% match" labels are on screen before "Two" and pulse together after "towns" | 0.7553 / 0.7553 | claim 19 | sim.py |
| R7-8 | Dot chart: each demand's 30 towns are drawn as solid dots (r 0.05, 100 %, background rim), spread ± 1 pp horizontally by rank; no mean tick or min–max whisker. Our two towns are ringed markers at (25, 57.9) and (33.3, 75.5). "our jump" bracket at 82 % from 25 to 33.3 with a dotted drop to the ¼ column | — | display only: the spread is horizontal, inside each column; every dot keeps its town's exact share on the vertical axis (claim 12). Our ⅓ column's highest town is 78.1 %, under the 82 % bracket | sim.py |
