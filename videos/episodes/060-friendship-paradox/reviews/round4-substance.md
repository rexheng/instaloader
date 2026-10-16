# Round 4 review: substance (science and story editor; every dimension scored)

**Evidence used**
- `review/` pack: metrics.json (00:53) is newer than final.mp4 (00:51), so I used it as is. I read report.md, transcript.txt, transcript_words.tsv and narration_diff.txt.
- All 13 contact sheets.
- Full-resolution keyframes: kf_01 (0:00.3), kf_03 (0:07.9), kf_06 (0:36.7), kf_09 (1:00.4), kf_13 (1:35.1), kf_17 (1:48.0), kf_19 (2:04.8), kf_21 (2:13.1), kf_30 (2:47.4), kf_34 (3:14.8), kf_35 (3:21.1) and kf_38 (3:32.4).
- Extra frames I pulled with ffmpeg: 0:45.0, 1:03.8, 1:04.8, 1:55.4, 2:17.0, 2:44.8 and 3:23.5. I also ran a 5 fps pixel-diff over 1:00–1:07 to check the Sue, Alice and Betty pulses (they fire at 63.2–63.8, 64.2–64.8 and 65.2–65.8 s, each inside its spoken word), and ran volumedetect on the end card.
- Sources:
  - script.md, narration.txt and facts.md.
  - Every network number recomputed from the edge list in Python with exact fractions.
  - Ugander et al. arXiv PDF: direct quotes for 190, ⟨k²⟩/⟨k⟩ = 635, the 5,000 cap and 92.7 %.
  - Christakis & Fowler, PLoS ONE full text: abstract, 319/425, 13.9 d (CI 9.9–16.6), 3.2 d.
  - Feld 1991 bibliographic record: AJS 96(6):1464–1477, doi 10.1086/229693.

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each girl once per friend she has, so the average friend has avg(k²)/μ = μ + σ²/μ friends (the cross terms vanish because the distances from the balance point sum to zero). That beats the average person whenever friend counts vary, and friends of random Harvard students caught a real flu outbreak early.
SCORES: Hook 8.5 · Clarity 9 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.6 (862.5/100)   AFTER CEILING: 8.6 (lowest 8.5 + 2 = 10.5, not binding)
CAPS: none. I found no factual or mathematical error. The transcript has 0 banned phrases and no banned patterns. Every empirical claim has an on-screen citation (Feld/Coleman, Ugander, C&F). Runtime, pace, loudness, silences and static stretches are all in range. The layout audit is clean, and the overlaps I saw are transitional only (1:55, 2:17).
FINAL: 8.6   PASS: no
```

## FACTS

| Claim | Verdict | Source / check |
|---|---|---|
| Eight girls at an Illinois high school, every (reciprocated) friendship between them | Verified | Feld 1991 Fig. 1 ("Marketville", Coleman 1961 northern-Illinois study) |
| Counts 1,4,4,2,3,3,2,1; "each girl has two and a half friends" | Verified | Edge list → Σk = 20, μ = 5/2 |
| Ring: 16 tokens, 32/16 = 2.0, "both averages are two" | Verified | 8 nodes, 8 edges |
| "Twenty tokens add up to sixty. Friends average three." | Verified | Σk² = 60, 60/20 = 3 (Feld Table 1: "Mean 3.0 for 20 friends") |
| "half a friend too low", "twenty percent more" | Verified | 3 − 2.5 = 0.5; 3/2.5 = 1.20 |
| Four tokens on Sue, four on Alice, one on Betty | Verified | k = 4, 4, 1. The kf_09 token positions are at the receiving end. |
| Balance points 2.5 (girls) and 3 (tokens) | Verified | Equal weights at k give μ. Token weights k at position k give Σk²/Σk = 3. |
| "Sue holds four tokens, each worth four: sixteen"; k² on top, k on the bottom | Verified | arithmetic |
| ÷8 → avg(k²) = 7.5 over μ = 2.5 | Verified | 60/8, 20/8 |
| Squared distances 2.25 (×4), 0.25 (×4); σ² = 10/8 = 1.25 | Verified | population variance; 7.5 − 6.25 = 1.25 |
| 4² = (2.5 + 1.5)² = 2.5² + 1.5² + 2·2.5·1.5 | Verified | 6.25 + 2.25 + 7.5 = 16 |
| Cross terms cancel because the beam balances (Σd = 0) | Verified | Σ(k − μ) = Σk − nμ = 0. Signed labels −1.5, −0.5, +0.5, +1.5 (×2). |
| avg(k²) = μ² + σ²; friends average μ + σ²/μ = 2.5 + 0.5 | Verified | re-derived |
| "The ring had no spread, so it had no gap"; 2 + 0/2 = 2 | Verified | σ² = 0 |
| Facebook 2011, users averaged about 190 friends | Verified | Ugander et al. 2011, arXiv:1111.4503: "the average Facebook user in our study had around 190 Facebook friends" (2·68.7e9/721e6 = 190.6) |
| Tokens average about 635 | Verified | Same paper: "The expected number of friends at the end of a randomly chosen edge, ⟨k²⟩/⟨k⟩ = 635" |
| "A few users had thousands of friends"; tick "5,000, Facebook's limit" | Verified | Same paper: "a clear cutoff at 5000 friends, a limit imposed by Facebook" |
| 190 + 445 = 635; "spread term more than twice the mean" | Verified | 635 − 190.6 = 444.4 ≈ 445; 445/190 = 2.34 |
| Christakis & Fowler, Harvard, 2009 (study); PLoS ONE 2010 (citation) | Verified | PLoS ONE 5(9):e12948, monitoring from Sept 1 to Dec 31, 2009 |
| 319 random students; 425 friends they named | Verified | Methods: "N = 319" and "N = 425" |
| "Friends sit closer to everyone else, so they should catch it first" | Verified (as C&F's rationale) | Abstract: "individuals near the center … are likely to be infected sooner"; friends "are known to be more central" |
| Fitted lead 13.9 days | Verified | Abstract: "13.9 days (95% C.I. 9.9–16.6)" |
| Self-reported symptoms: lead "about three" (3.2 on screen) | Verified | Results: "3.2 days, 95% C.I. 2.2–4.3" |
| Dashed curves are a logistic refit with the shift held at 13.9 | Verified (labelled) | Citation reads "Fig. 3 redrawn, logistic refit"; the read-out says "C&F fitted lead" |
| Five girls have fewer friends than their friends' average; only Sue and Alice have more | Verified | Recomputed: Betty 4, Jane 3.5, Pam 3.33, Dale 3.33, Tina 2 > own; Sue 2.75 and Alice 3 < own; Carol equal (Feld p. 1465) |
| "land on a Sue four times as often as on a Betty"; "Betty … sees four" | Verified | 4/20 vs 1/20. Betty's only friend is Sue (k = 4). |

## MECHANICS

runtime 3:41.4 · 160 wpm (speech time; 566 words) · max internal silence 2.23 s (0:11.7–0:14.0, the planned "Pick one" hold) · leading 0.00 s / trailing 1.49 s · max static 2.50 s · −14.0 LUFS / −2.1 dBTP · WER 1.5 %. The "Thank you" at 3:40.8 is a Whisper hallucination over the silent end card; volumedetect shows no speech after 3:39.9.

## Transcript and story

- **§4 search:** 0 banned phrases. I found no rhetorical-question chain (each of the two questions stands alone and is followed by a hold), no "not just X" construction, no empty superlatives and no recap ending. "Here that's…" and "Back to the eight girls" are ordinary signposts, each used once.
- **Hook:** the first frame shows the eight real girls with a citation, and "How many friends does the average friend have? Pick one." lands at 0:08–0:11, followed by a 2.2 s hold over YELLOW candidates 2.5 · 3 · 4. Stakes follow at 0:14. The hook arrives by 0:12. The weakness is that the title already says friends have *more*, so a viewer who read it picks 3 or 4. The prediction is not likely to be wrong, and the naive "2.5" is voiced by the narrator at 0:22 rather than held by the viewer.
- **Beats:** the structure follows §6 cleanly:
  - Naive build: the ring, where the guess holds, 0:28–0:44.
  - Fail: real friendships, 3.0 vs 2.5, measured as "+0.5 · 20%", 0:44–1:06.
  - Insight: beam, variance squares, cross-term cancellation, then μ + σ²/μ, 1:06–2:28.
  - General case: Facebook, with a prediction pause, 2:30–2:51.
  - Payoff with honest limit: C&F 13.9 days, shrinking to 3.2 for self-report.
  - Landing: back on the cold-open frame.
- **Sag:** the insight runs 82 s, which is 37 % of the runtime and well over the template's 50 s. Tension flattens there, between 1:38 and 2:11.
- **Script vs transcript:** two possible slurs. "Sue's four" at 1:51.3 is heard as "sus 4 four", which suggests the possessive is clipped. "friends" at 0:57.4 is not transcribed: there is 0.5 s of audio between 57.4 and 57.94 s but no recognised word, so it is likely under-articulated. Christakis is transcribed correctly, so the override works.
- **Symbol never spoken at its entrance:** μ appears on screen as the denominator of avg(k²)/μ at 1:37 (sheet 6, 1:37.0), but the narration calls it "the average girl" and first says "mu" at 2:12. For 35 s the viewer holds a Greek letter that no one has named.
- **Missing bridge:** at 2:56 "Friends sit closer to everyone else in the network" is asserted. The episode has proved that friends have more *friends*, not that they are more *central*. One clause would connect the two.
- **Landing:** the line "From most seats in this class, the view is the same" resolves the opening, but it stays in Marketville. The title says *your* friends, and the only nod to the viewer is "yours included" inside a re-explanation of tokens. The episode has a verified, cited number that would land the title on the viewer (Ugander et al.: "92.7% of users have less friends than the average friend count of their friends"), and facts.md lists it as cut.
- **Repetition:** the token-landing mechanism is explained three times: 0:57–1:05 ("piled up unevenly … four on Sue … one on Betty"), 1:13–1:18 ("one per friend") and 3:26.8–3:33.8 ("land on a Sue four times as often as on a Betty"). The third repeats rather than reframes.

## Visual and motion notes (cited)

- **Strong:**
  - The token, beam and squares chain.
  - Colour semantics held throughout. BLUE μ, YELLOW friend average and PURPLE σ² match in the bar segments and the equation terms (kf_09, kf_21).
  - The ring thumbnail callback at 2:27–2:29.
  - The Harvard step curves growing on one calendar (sheet 10–11).
  - The live arrow ruler that shrinks from 13.9 to 3.2 (3:15–3:19).
- **2:16.6–2:18.0 [Motion]:** the split μ²+σ² over μ → μ²/μ + σ²/μ morphs messily. Frame 2:17.0 shows doubled "μ μ" and "2.5 2.5" denominators with a scrambled "1.25" glyph. This is the one transform in the episode that reads as mush rather than correspondence.
- **1:55.0–1:55.4 [Motion]:** the flying "4" passes over the σ² row ("1⁴σ²" at 1:55 in sheet 7). It is brief, but it crosses a live equation.
- **3:22–3:26 [Visual]:** the legend "her friends' average" sits at bottom-left (x ≈ 100–515, y ≈ 860 in frame 3:23.5), 300–700 px from the five numbers it labels. That breaks "label next to its referent", and Betty's "4" reads at first as a stray count.
- **1:06–2:28 [Visual]:** the beam name labels (Text 20) measure about 29 px cap height in kf_13 ("Betty", "Carol"), under the 34 px primary-label minimum. Only Sue and Betty are named in the narration.
- **3:13–3:19 [Visual]:** the 13.9 d / 3.2 d read-out sits in the top-right corner, detached from the chart by the y-axis title. Its arrow runs to x ≈ 1843 px, past the 1824 px safe line (kf_34).
- **0:41 and 0:45 [Clarity, nit]:** transient readouts. The friend bar shows "0.0" while the narration says "Both averages are two", and the girl bar shows "2.4" during the restore (frame 0:45.0).

## FIXES (highest impact first)

1. **[0:00–0:28][Hook]** The title spoils the answer, so the viewer's committed prediction is not likely to be wrong. **Change:** reframe the cold open as a paradox the title cannot defuse by moving the naive argument *before* the question:
   - New cold open: "Eight girls at an Illinois high school, and every friendship between them. On average, each girl has two and a half friends. Every friend is one of these same eight girls. So how many friends does the average friend have? Pick one."
   - At 0:22, replace "The natural guess is two and a half again: every friend is one of these same eight girls." with "Same girls, same friendships: two and a half looks forced."
   - The net word count is unchanged. The viewer is pushed toward 2.5 by an argument that seems airtight, so the 0:55 "half a friend too low" breaks *their* answer rather than the narrator's. Hook → 9.
2. **[3:26.8–3:40][Hook/Concision/Originality]** The third explanation of token landing replaces a reframe, and the ending never reaches the viewer. **Change:**
   - Cut "Follow any friendship, yours included, and you land on a Sue four times as often as on a Betty."
   - New close: "So Betty looks at her one friend and sees four. On Facebook in twenty eleven, ninety-three percent of users were Betty."
   - On "Betty", keep her thick outline. On "ninety-three percent", a citation "Ugander et al., 2011 · arXiv:1111.4503" fades in bottom-left for ≥ 3 s, and a YELLOW "92.7% of users" tag appears under Betty.
   - Drop the "Sue ■■■■ 4× / Betty ■ 1×" tally, which only illustrates the cut line.
   - This turns the title onto the viewer with a verified number. Source: Ugander et al. 2011, "92.7% of users have less friends than the average friend count of their friends". That is an individual-level statistic, the same kind as "five of eight".
3. **[1:29–1:38][Clarity]** μ appears on screen at 1:37 but is first spoken at 2:12. **Change** "over the average girl, two and a half" to "over the average count, mu, two and a half". Flash the BLUE μ as "mu" is spoken.
4. **[2:16.6–2:18.0][Motion]** The split transform doubles the denominators and scrambles "1.25". **Change:** do it in two clean steps of 1 s each:
   - (a) `TransformFromCopy` the denominator μ (and 2.5) once under each numerator term while the original bar splits.
   - (b) Move "1.25" as a whole mobject: pass it through a `key_map`, or exclude it from `TransformMatchingTex` and `.animate.move_to` its new slot.
   - Hold the split state ≥ 2.4 s (2 s + 0.4 s per term) before cancelling μ²/μ.
5. **[2:56–3:00][Clarity]** "sit closer to everyone else" is asserted without a link to what was proved. **Change** to "Named friends have more friends, so they sit closer to everyone else, and should catch it first." (+5 words). On "more friends", flash the YELLOW "425 friends they named" label.
6. **[1:06–2:28][Concision]** The insight runs 82 s. **Change:**
   - Merge "Line the girls up by friend count: two at each count, from one to four, so they balance at two and a half." into "Line the girls up by friend count: they balance at two and a half." The two-per-count fact is visible.
   - Shorten the post-"cancel" pause (2:11.0–2:12.1) to 0.6 s.
   - Target ≤ 72 s for the beat and ≤ 3:30 total.
7. **[3:22–3:26][Visual]** The "her friends' average" legend is far from its numbers. **Change:**
   - Write it as a tag directly right of Betty's "4" ("4 ← her friends' average", Text 22, buff 0.2), visible for 2 s, then shrink it to 40 % opacity.
   - Remove the bottom-left legend.
8. **[1:51.3, 0:57.4][Audio]** Possible slurs: "Sue's" is heard as "sus", and "friends" is dropped from the transcript. **Change:**
   - "Split Sue's four into…" → "Split Sue's count, four, into…".
   - "too low: friends average twenty percent more" → "too low. The friends average twenty percent more than the girls."
   - Re-run the review kit and confirm both words appear in the transcript.
9. **[1:06–2:28][Visual]** The beam name labels are about 29 px cap height (below 34 px). **Change:** keep only "Sue" and "Betty" (the narrated girls) under the beam at Text 26, and drop the other six names. The counts inside the nodes carry the information and the row gets lighter.
10. **[3:13–3:19][Visual]** The read-out arrows are detached in the top-right corner, and the arrow passes the x safe line. **Change:** park the read-out block inside the plot's empty lower-right region (x ∈ [2.0, 6.2], y ≈ −1.2, under the curves after day 90), with arrow tips aligned at x ≤ 6.2.
11. **[1:53–1:55.4][Motion]** The flying "4" crosses the σ² row. **Change:** route the copy along an arc above the σ² row (`path_arc=-0.6`), or start the (2.5 + 1.5)² row first and fly into it from the right.
12. **[0:41, 0:45][Clarity, nit]** The transient readouts "0.0" and "2.4" contradict the narration for about 0.5 s. **Change:**
    - Grow the friend fill from the guess box's right edge with its readout fixed at "2.0".
    - Hide the girl readout during the restore and fade it in at "2.5".

REACHES 9 IF ALL FIXED: yes, narrowly, with no structural change. Fixes 1–2 move Hook to 9, and fix 2 also moves Originality to 9 (the episode would end on a memorable, cited number about the viewer). Fixes 4, 7, 9, 10 and 11 move Visual and Motion to 9, fixes 2 and 6 move Concision to 9, and fix 8 moves Audio to about 9. That gives 15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·9 + 10·9 = 9.0. Without fixes 1 and 2 the ceiling is about 8.8. The beam derivation is already at the bar, so the remaining gap is in story and finish, not explanation.

KEEP:
- The ring control (0:28–0:44) and its callback "The ring had no spread, so it had no gap" with the 2 + 0/2 = 2 thumbnail (2:25–2:29). That is the SMH build-fail-measure move and the honest limit in one image.
- The token → beam → squares → "distances add to zero" chain, with BLUE μ / YELLOW friend average / PURPLE σ² matched between the bar segments and the equation terms.
- The Harvard redraw with the live arrow ruler shrinking 13.9 → 3.2 days, labelled "C&F fitted lead" and "logistic refit".
