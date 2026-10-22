EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each person once per friend she has, so the average friend has avg(k²)/μ = μ + σ²/μ friends, which is more than the average person whenever friend counts vary. Epidemiologists can use that gap to see an outbreak coming.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8.5 · Motion 8.5 · Audio 8.5 · Concision 8 · Originality 8.5
WEIGHTED: 8.5 (8.45)   AFTER CEILING: 8.5 (lowest 8 + 2 = 10, so the ceiling does not bind)
CAPS: none
FINAL: 8.5   PASS: no

Reviewer: science/story editor, round 1 (independent). Evidence: review/ pack (metrics.json 00:53 is newer than final.mp4 00:51), all 13 contact sheets, keyframes at 0:07.9, 1:00.4, 1:18.6, 1:44.2, 2:04.8, 2:17.9, 2:20.1, 2:29.4, 2:47.4, 3:14.8, 3:24.1 and 3:39.8, plus frames I extracted at 0:11.5, 0:20.5, 2:50.5 (formula crop), 3:11.5 and 3:17.5. I also measured audio RMS at 57.2–58.0 s and 111–112 s.

## FACTS
I recomputed everything myself. Degrees from the edge list: Betty 1, Sue 4, Alice 4, Jane 2, Pam 3, Dale 3, Carol 2, Tina 1.

- 8 girls, every friendship between them, at "an Illinois high school" (Feld's Marketville, from Coleman's 1957–58 study of northern-Illinois schools) | Verified | Feld 1991, AJS 96(6):1464–1477, text p. 1465 and Fig. 1 ("eight girls in 'Marketville,' one of the high schools included in the study"). Coleman's 10 schools were in northern Illinois.
- Mean 2.5 friends (Σk = 20 over 8 girls) | Verified | Feld Table 1 ("Mean 2.5*"). Recomputed 20/8.
- Token average 60/20 = 3.0, Σk² = 1+16+16+4+9+9+4+1 = 60 | Verified | Feld Table 1 ("Mean 3†"; "20 friends ... having a total of 60 friends, with a mean of 3.0").
- "half a friend too low", "20% more than girls": 3 − 2.5 = 0.5, and 3/2.5 = 1.20 | Verified | computed.
- Ring: all counts 2, 32/16 = 2.0, σ² = 0 so 2 + 0/2 = 2 | Verified | computed (labelled hypothetical on screen).
- Two girls at each count 1–4. Token columns 2, 4, 6, 8. Sue holds 4 tokens, 4 × 4 = 16 | Verified | computed.
- Fulcra: girls balance at 2.5. Tokens (weight k at position k) balance at Σk²/Σk = 3 | Verified | geometry checked on kf_11 (yellow ▲ at x ≈ 646 px, midway between the count-3 nodes at 593 and 700 px).
- Divide by 8: 60/8 = 7.5 = avg(k²) and 20/8 = 2.5 = μ | Verified | computed.
- Squared distances: 2.25 four times and 0.25 four times, sum 10, σ² = 10/8 = 1.25 (population variance) | Verified | computed.
- 4² = (2.5 + 1.5)² = 2.5² + 1.5² + 2·2.5·1.5 = 6.25 + 2.25 + 7.5 = 16 | Verified | algebra.
- avg(k²) = μ² + σ² + 2μ·avg(d), with avg(d) = 0 because Σ(k − μ) = Σk − nμ = 0 (the balance condition) | Verified | re-derived. The "beam balances, so the cross terms cancel" argument is exactly right.
- Σk²/Σk = μ + σ²/μ = 2.5 + 1.25/2.5 = 3.0 | Verified | Feld p. 1469–70 gives the same identity, "mean(x) + variance(x)/mean(x)".
- Facebook 2011: average user about 190 friends | Verified | Ugander, Karrer, Backstrom & Marlow 2011, arXiv:1111.4503: "the average Facebook user in our study had around 190 Facebook friends" (68.7 B edges, 721 M users, so 2·68.7e9/721e6 = 190.6).
- Tokens average about 635 | Verified | Ugander et al.: "The expected number of friends at the end of a randomly chosen edge, ⟨k²⟩/⟨k⟩ = 635". This is the episode's token average, so the comparison is like for like.
- "A few users had thousands of friends"; 5,000 limit on screen | Verified | Ugander et al. ("many hundreds or even thousands of friends"; 5,000 cutoff).
- Spread term 445 is "more than twice the mean": 635 − 190 = 445 > 380 | Verified | computed (2.34×).
- Christakis & Fowler, Harvard, 2009 (1 Sep – 31 Dec 2009) | Verified | C&F 2010, PLoS ONE 5(9): e12948, Methods. The citation year on screen (2010) is the publication year and is correct.
- 319 random students and 425 named friends | Verified | C&F: "(N = 319) ... 'friends' sample (N = 425) composed of individuals who were named as a friend at least once".
- "Friends sit closer to everyone else in the network, so they should catch it first" | Verified as C&F's rationale (abstract and Fig. 1 caption: central individuals "are likely to be infected sooner") | C&F 2010.
- Flu diagnoses; friends' curve rises first; redrawn Fig. 3 | Verified | C&F Fig. 3 left panel (NPMLE, "diagnoses by medical staff"). The redrawn totals of 7.5 % and 7.8 % match the paper's ~8 %.
- "fitted curves put them 13.9 days ahead" | Verified | C&F abstract: 13.9 days (95 % CI 9.9–16.6), from an NLS logistic fit. The on-screen dashed curves are an honest refit with the shift held at 13.9 and are labelled "logistic refit". I measured the on-screen arrow at 140 px ≈ 13.8 days at 10.17 px/day.
- "With self-reported symptoms, the lead shrank to about three" (3.2 on screen) | Verified | C&F Results: "3.2 days, 95% C.I. 2.2–4.3".
- Five girls (Betty, Jane, Pam, Dale, Tina) have fewer friends than their friends' average, and Sue and Alice have more. Labels: 4, 3.5, 3.33, 3.33, 2, then 2.75 and 3 | Verified | Feld p. 1465 and Table 1 (4, 2.75, 3, 3.5, 3.3, 3.3, 2, 2).
- "land on a Sue four times as often as on a Betty" (4/20 vs 1/20) | Verified | computed.

No wrong, fabricated or uncited claims. Every empirical beat has an on-screen citation.

Note, no deduction: C&F's friend sample is "named at least once by a random student". That sample is degree-biased like the tokens, but it is not the same distribution as a uniformly random friendship end. The narration never claims they are identical, so this is not an error.

## MECHANICS
runtime 3:41.4 · wpm 160 (speech time; 153 overall) · max silence 2.23 s (the planned prediction pause, 0:11.7–0:14.0) · leading 0.00 s / trailing 1.49 s · max static 2.5 s · −14.0 LUFS / −2.1 dBTP · 0 black frames · layout audit 0 issues · WER 1.5 %. No cap triggered.

Transcript notes:
- 0:57.9: "friends" is missing from the transcript. RMS shows speech at 57.5–57.9 s before "average", so the word is spoken and Whisper dropped it. Not a defect.
- 1:51.3: "Sue's four" was heard as "sus four", which points to a slurred possessive (see fix 6).
- 3:40.8: "Thank you" over the 1.5 s trailing silence and the end card is a Whisper hallucination, not narration.

Banned phrases and §4 patterns: none found. No question chains, no "it turns out", no fake reveals, no lesson-list ending. The narration is clean and specific.

## FLIPBOOK / BEATS
- 0:00–0:13 cold open: the real network, counts fly into "average girl 2.5", and the candidates 2.5 / 3 / 4 appear. The viewer commits on "Pick one" at 0:11 with a 2.2 s hold.
- 0:14–0:22 stakes: the random/named-friend arrow is on Jane → Alice.
- 0:22–0:44 naive build: the ring, 32/16 = 2.0, "the guess holds".
- 0:44–1:06 fail: 60/20 = 3.0, the purple +0.5 · 20 %, and the Sue/Alice/Betty pulses.
- 1:06–2:30 insight: beam, token stacks, Σk²/Σk, divide by 8, distance squares to σ², cross-term cancellation via the balance point, μ + σ²/μ, ring callback.
- 2:30–2:51 Facebook prediction pause with the 635 payoff.
- 2:51–3:19 C&F redrawn curves.
- 3:19–3:41 landing on the cold-open frame.

The structure matches §6 almost beat for beat, and the build → fail → measure chain is real.

Sync is good throughout: "four on Sue … one on Betty" pulses at 1:03–1:05, "her distance" writes d = k − μ at 1:55, "add to zero" merges the signed labels into 0 at 2:09, and "the friends' curve rose first" flashes at 3:09.

## WHAT HOLDS IT BELOW 9 (evidence)
1. **2:51–3:00, Clarity.** "In 2009, Christakis and Fowler tested *this* at Harvard. Friends sit closer to everyone else in the network, so they should catch *it* first."
   - "it" has no antecedent. Flu was last mentioned at 0:16, 2.5 minutes earlier, and the previous 20 s were about Facebook friend counts.
   - The step from "friends have more friends" (everything the video proved) to "friends sit closer to everyone else" (the mechanism C&F rely on) is never stated.
   - This is the single place where the payoff does not follow from the insight.
2. **3:19–3:40, Clarity/Hook.** The landing silently switches statistic.
   - The whole derivation is about the friend average (3.0). The landing's "five have fewer friends than their friends' average" is a per-girl comparison, a different quantity (Feld separates them; the mean of the per-girl means is 2.99).
   - Feld notes that μ + σ²/μ does not by itself guarantee a majority. Juxtaposing it with "Follow any friendship, yours included" invites the viewer to think the formula proves it.
   - The 4×/1× tally (3:29–3:35) repeats the "four on Sue … one on Betty" beat from 1:03.
   - The final line, "From most seats in this class, the view is the same", is soft. It does not re-see the opening question ("How many friends does the average friend have?") as sharply as the bar wants.
3. **2:27–2:30, Clarity/Visual.** During the ring callback (kf_27 at 2:29.4) the bar panel reads "average girl 2.0 / average friend 2.0" with no ring tag. On the same frame, the beam still shows the 2.5 and 3 fulcra and the main row reads "= 2.5 + 0.5 = 3.0". That is three focal points with contradictory numbers for about 3 s.
4. **0:55–1:06 and 1:27–1:31, Concision.** The gap is stated twice in one breath ("half a friend too low: friends average twenty percent more than girls"), and the "+0.5 · 20%" label already shows both. The 60/20 fraction is spoken at 0:51 and again at 1:28 ("Sixty over twenty") while it sits on screen. With the tally repeat in the landing, about 10–12 s of 221 s is removable, and the runtime sits high in the window at 3:41.
5. **2:17, Motion.** The μ²/μ + σ²/μ split crossfades and leaves doubled glyphs for about 1 s (sheet 8, 2:17.0: "μ μ", "2.5 2.5" and a ghost "1.25" stacked). Everything else in the algebra moves cleanly.
6. **1:51, Audio.** "Split Sue's four" was transcribed "sus four", which suggests a swallowed possessive on the name that anchors the cross-term step.
7. **2:45–2:51, Visual.** The four BLUE "a few users" dots on the broken axis toward 5,000 are schematic but look like plotted data. The script admits "no values are claimed".
8. **1:33–1:37, Clarity (nit).** "over the average girl, two and a half": μ is the average girl's friend count, not a girl.

## FIXES (highest impact first)
1. [2:51–3:00][Clarity] Payoff does not follow from the insight, and "it" has no antecedent. Replace the two sentences with: "In twenty oh nine, Christakis and Fowler put this to work at Harvard. Named friends have more friends, so they sit closer to everyone else, and should catch flu first." On "more friends", flash the YELLOW friends' label beside the chart axis title. Raises Clarity.
2. [3:19–3:40][Hook+Clarity+Concision] Rewrite the landing to name the statistic switch and end on the opening question.
   - Proposed: "Back to the eight girls. Seat by seat, five have fewer friends than their friends' average; only Sue and Alice have more. Betty looks at her one friend and sees four. She asked how many friends the average friend has: two and a half was never the answer, because every count she sees comes from someone who was counted extra."
   - Visual: cut the 4×/1× tally (3:29–3:35, already made at 1:03). In its place, bring back the cold-open "average friend ? 2.5 3 4" row from 0:11 and ring the 3, dimming 2.5 to 30 %, so the last frame re-sees the first.
   - Keep it ≤ 15 s.
3. [2:27–2:30][Clarity+Visual] Ring callback shows contradictory numbers. While the ring plays, dim the beam, the squares and the "μ + σ²/μ = 2.5 + 0.5 = 3.0" row to 30 %, and put a GRAY "ring" tag (Text ≥ 26) left of the bar labels. Alternatively, leave the main bars at 2.5 / 3.0 and draw two mini bars (2.0 / 2.0) beside the ring thumbnail. Restore everything at 2:30.5.
4. [0:55–1:06][Concision] Cut "friends average twenty percent more than girls" from the narration; the "+0.5 · 20%" label carries it. [1:27–1:29] Cut "Sixty over twenty" (the fraction is on screen). With fix 2, this saves about 10 s, bringing the runtime to about 3:30.
5. [2:16–2:18][Motion] Doubled glyphs during the split. Replace the crossfade with per-term moves: TransformMatchingTex with an explicit key_map, or ReplacementTransform of each numerator/denominator part, so the left μ², σ², μ and the right 2.5², 1.25, 2.5 each slide to one target with no overlapping copies.
6. [1:51][Audio] "Sue's" is slurred. Rephrase to "Split Sue's count, four, into …", or respell for Kokoro ("Sooz"), and confirm with Whisper that the name comes back as "Sue's".
7. [2:45–2:51][Visual] Schematic dots read as data. Replace the four dots with one BLUE bracket over the broken stretch labelled "a few users, up to 5,000 (Facebook's limit)", or add "(schematic)" under "a few users".
8. [1:33–1:37][Clarity] Change "over the average girl, two and a half" to "over the average count, two and a half" (μ is a count).

REACHES 9 IF ALL FIXED: yes, narrowly.
- The structure, facts and central picture are already at the bar.
- Fixes 1–3 lift Clarity and Hook to 9 and fixes 4–5 lift Concision and Motion, which gives a weighted score of about 9.0 even with Originality held at 8.5.
- Originality stays at 8.5 because Feld's eight girls and the Facebook 190/635 pair are also the examples in Strogatz's 2012 NYT column "Friends You Can Count On". The tokens-and-beam picture is the episode's own contribution and should be made more prominent, not less.

KEEP:
- The balance beam: girls balance at 2.5, tokens at 3, and the same balance makes avg(d) = 0, which kills the cross term (1:06–2:12). This is the one picture, and it proves the identity.
- The naive build and fail on concrete data: the ring passes at 32/16 = 2.0, then the real class fails by a measured +0.5 · 20 % with token-by-token arithmetic (0:28–1:06).
- The honest payoff: C&F Fig. 3 redrawn from real data, the "C&F fitted lead: 13.9 days" read-out, and the shrink to 3.2 days with self-report (3:01–3:19).
