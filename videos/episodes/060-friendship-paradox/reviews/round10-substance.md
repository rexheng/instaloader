# Round 10 — science and story editor (fact-check, hook and tension, clarity, concision, slop; every dimension scored)

**Evidence used**
- `review/` pack (metrics.json 23:33 is newer than final.mp4 23:31, so reused): report.md, narration_diff.txt, all 12 contact sheets, transcript.txt.
- Full-resolution keyframes read: kf_05 (0:16.4), kf_11 (1:00.2), kf_13 (1:14.3), kf_15 (1:25.6), kf_17 (1:42.3), kf_19 (2:03.4), kf_23 (2:17.6), kf_27 (2:28.9), kf_33 (2:57.5), kf_35 (3:05.6), kf_37 (3:19.9), kf_39 (3:33.1).
- Extra frames extracted with ffmpeg into /tmp/r10sub060: 1:23.4, 1:24.2, 1:25.0, 1:26.0, 1:26.8, 1:28.0 (divide step); 2:46.6–2:47.8 (Facebook row build); 3:24.4, 3:25.4 (landing hand-off); 0:43.0, 0:43.5 (ring fade-out).
- narration.txt, script.md, facts.md, cf_fig3_digitized.json, CHANGELOG tail (only to check which round-9 fixes landed).
- Independent recomputation (Python) from the edge list Betty–Sue, Sue–Alice, Sue–Dale, Sue–Pam, Alice–Jane, Alice–Pam, Alice–Dale, Jane–Dale, Pam–Carol, Carol–Tina:
  - counts Betty 1, Sue 4, Alice 4, Dale 3, Pam 3, Jane 2, Carol 2, Tina 1; Σk = 20, Σk² = 60, μ = 2.5, σ² = 1.25 (population), avg(k²) = 7.5, Σk²/Σk = 3.0 = μ + σ²/μ;
  - token layers 20/8 = 2.5, 38/14 = 2.71, 52/18 = 2.89, 60/20 = 3.0 (the on-screen live fulcrum 2.7 / 2.9 / 3.0);
  - friends' means: Betty 4, Sue 2.75, Alice 3, Dale 3.33, Pam 3.33, Jane 3.5, Carol 2, Tina 2 → 5 below, 2 above, 1 equal (Feld p. 1465);
  - Sue: 4² = (2.5 + 1.5)² = 6.25 + 2.25 + 7.5 = 16;
  - C&F schematic: random {Betty 1, Dale 3, Carol 2} (mean 2.0) → tokens 4, 4, 4, 2, 3, 1 (mean 3.0);
  - Facebook: 2 × 68.7e9 / 721e6 = 190.6; 635 − 190.6 = 444.4 ≈ 445 > 2 × 190.6 = 381.
- Citations re-verified online today (2026-10-22):
  - Feld 1991, *AJS* 96(6):1464–77 (UVM PDF): eight Marketville girls, "a total of 20 friends, with a mean of 2.5"; Coleman 1961 data.
  - Ugander, Karrer, Backstrom & Marlow, arXiv:1111.4503 (PDF): "n = 721 million ... 68.7 billion friendship edges ... around 190 Facebook friends"; "⟨k²⟩/⟨k⟩ = 635"; "92.7% of users have less friends than the average friend count of their friends"; "clear cutoff at 5000 friends".
  - Christakis & Fowler, *PLoS ONE* 5(9):e12948, 15 Sep 2010 (journals.plos.org): Harvard College, late 2009; random N = 319, friends N = 425; "NLS estimates suggest that the friends curve for flu diagnosed by medical staff is shifted 13.9 days forward in time (95% C.I. 9.9–16.6)"; "a significant but smaller shift in self-reported flu symptoms (3.2 days, 95% C.I. 2.2–4.3)"; friend group "significantly higher measured in-degree and betweenness centrality"; "more friends means more paths to others in the network who might be infected".
- Round-9 fixes confirmed on the master:
  1. Divide in two states: the ÷ 8 row is fully in by 1:23.4 and holds to ~1:26.4 (~3 s), then every term pinches in place to avg(k²)/μ = 7.5/2.5 (1:26.8–1:28.0).
  2. Cold open breaths: silences 0:04.4–0:05.0 and 0:08.0–0:08.8 now separate the three sentences.
  3. "Measure each girl's distance from the balance point" (heard cleanly at 1:36.0).
  4. C&F draw is {Betty, Dale, Carol}; tokens 4, 4, 4, 2, 3, 1 (kf_35).
  5. Squares and "sides at 1/4 scale" leave together (2:21 → 2:23, sheet 8).
  6. Fits begin at each group's first case (kf_37, day ≈ 3.5).

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each person once per friend she has, so the friend average is avg(k²)/μ = μ + σ²/μ (the cross term vanishes because distances from the balance point sum to zero), which beats the person average whenever counts vary, and that is why the friends students name are an early-warning sample for flu.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 9 · Audio 9 · Concision 9 · Originality 9
WEIGHTED: 9.0 (135 + 225 + 135 + 135 + 90 + 90 + 90 = 900 / 100)   AFTER CEILING: 9.0 (lowest 9 + 2 = 11, does not bind)
CAPS: none. 0 banned phrases or patterns (my own sweep of transcript and narration agrees with the kit). Every empirical claim carries an on-screen citation (Feld/Coleman 0:00–2:30, Ugander 2:31–2:58, C&F 2:59–3:24). No wrong or fabricated claim. All mechanics in range. Layout audit 0/218; no overlap or clipping in any settled frame I read.
FINAL: 9.0   PASS: yes
FACTS:
- Eight girls at an Illinois high school, every friendship among them | Verified | Feld 1991 Fig. 1 ("Marketville"); Coleman 1961, northern Illinois
- Counts 1,4,4,2,3,3,2,1; "two and a half friends" | Verified | recomputed; Feld p. 1467
- Ring "everyone has 2 (hypothetical)": 32/16 = 2.0; "the guess holds" | Verified | computed, labelled hypothetical
- Real class: tokens read 1–4, 60/20 = 3.0; "+0.5 · 20%"; "fell short by half a friend" | Verified | Feld Table 1; 0.5/2.5 = 20 %
- Mid-flight counters 15/5 (0:47), 58/19 (0:49) | Verified | consistent partial sums
- "four on Sue, four on Alice, one on Betty" | Verified | degrees
- Two girls at each count; girls balance at 2.5; tokens at 3; live fulcrum 2.7 / 2.9 / 3.0 | Verified | layer sums recomputed; pairs sit symmetrically about each tick, so the offsets do not move either balance point
- "Sue holds four tokens, each worth four: sixteen"; k² on top, k on bottom; (60÷8)/(20÷8) = 7.5/2.5 | Verified | algebra
- Distances 1.5 / 0.5; areas 2.25 / 0.25; σ² = 10/8 = 1.25 | Verified | population variance, computed
- 4² = (2.5 + 1.5)² = 2.5² + 1.5² + 2·2.5·1.5 | Verified | 6.25 + 2.25 + 7.5 = 16
- avg(k²) = μ² + σ² + 2μ·avg(d), avg(d) = 0 because the beam balances | Verified | Σ(k − μ) = 0 by definition of μ; complete proof
- (μ² + σ²)/μ → μ + σ²/μ = 2.5 + 0.5 = 3.0; ring 2 + 0/2 = 2 | Verified | computed
- Facebook 2011: about 190 friends; a few had thousands; 5,000 limit | Verified | Ugander et al. 2011 (May 2011 snapshot)
- Tokens average about 635 | Verified | Ugander: ⟨k²⟩/⟨k⟩ = 635, exactly the token (edge-end) average
- 190 + 445 = 635; "spread term is more than twice the mean" | Verified | 444.4 vs 381
- "93% of users had fewer friends than their friends averaged" (92.7 % on screen, "below their own friends' average") | Verified | Ugander, per-user statistic, correctly kept distinct from 635
- Christakis & Fowler at Harvard; random students vs the friends they named; 319 / 425 | Verified | C&F 2010 Methods
- "Named friends have more friends, so they sit closer to everyone else, and should catch flu first" | Verified as C&F's rationale | C&F: higher in-degree and betweenness; "more friends means more paths"
- Raw steps = C&F Fig. 3 redrawn (colours remapped to the series palette); dashed curves a disclosed logistic refit with the shift held at 13.9 d | Verified as disclosed | on screen "Fig. 3 redrawn, logistic refit"; arrow length measured on kf_37 = 140 px at 10.1 px/day ≈ 13.8 d
- "Fitted curves put them 13.9 days ahead" | Verified | C&F Results (NLS, diagnoses by medical staff)
- "With self-reported symptoms, the lead shrank to about three" (3.2 days on screen) | Verified | C&F Results
- "Betty looks at her one friend, Sue, and sees four. Most of us are Betty." | Verified as a fair per-person reading | Feld 5 of 8; Ugander 92.7 %
MECHANICS: runtime 3:34.5 · wpm 153 (speech time; 138 overall) · max silence 2.22 s (planned, 3:29.0–3:31.2 after "sees four"; 2.0 s after "Pick one" and after the Facebook question) · max static 3.5 s (0:53.1–0:56.6) · −14.0 LUFS / −2.1 dBTP · lead 0.00 s / trail 1.80 s · WER 2.6 % (number formatting only)
FIXES (highest impact first; all are nitpicks, none needed to pass):
1. [2:12–2:20][Motion] The two algebra rows after "So" hold a little under the §5 reading time.
   - The rebuilt row (μ² + σ²)/μ = (2.5² + 1.25)/2.5 = 3.0 (7 terms, target ≈ 4.8 s) holds ≈ 4 s, 2:12.3 → split on "mu" ≈ 2:16.4.
   - The split row μ²/μ + σ²/μ = 2.5²/2.5 + 1.25/2.5 = 3.0 (9 terms, target ≈ 5.6 s) holds ≈ 3.8 s, 2:16.5 → collapse on "two and a half" ≈ 2:20.3.
   - Change: in narration.txt, raise the pause after "plus sigma squared over mu" from [pause 1.2] to [pause 1.8]. Fund it by cutting the [pause 1.0] after "With no spread, the ring had no gap" to [pause 0.4], so runtime stays 3:34.5.
2. [0:42.8–0:43.5][Visual] The ring's YELLOW friend-bar outline, its "2.0", and "32/16 = 2.0" fade through olive/brown. The full-res frame at 0:43.0 shows the colours plainly. This breaks the episode's own rule that YELLOW never dims, which holds everywhere else.
   - Change: shrink the outline, "2.0", "32" and "16" out at full colour (the same treatment as the C&F tokens), or cap their opacity ramp at 0.2 s.
3. [1:26.6–1:27.0][Motion] The pinch hand-over in the divide step briefly overlaps old and new glyphs at 45 % size. At 1:26.8 "60" and "7.5" sit on top of each other, as do "Σk ÷ 8" and "μ".
   - Change: set the cross to 0 s, so the old term reaches zero size before the new one starts growing. Alternatively, run the numerator and denominator relabels as one TransformMatchingTex.
4. [0:00–0:24][Hook] The series title ("…More Friends Than You") already refutes the 2.5 candidate. So "The natural guess is two and a half again" (0:21.3) voices a belief the title has broken, and the live choice is really 3 vs 4.
   - Change, at no word cost: replace "The natural guess is two and a half again: every friend is one of these eight girls." with "Every friend is one of these eight girls, so two and a half sounds right." It reads as the viewer's own reasoning rather than a strawman.
   - Optional, if the producer wants a cited misconception: Zuckerman & Jost 2001, *Social Psychology Quarterly* 64:207–223, found most people believe they have more friends than their friends do. It is already in C&F's references.
5. [1:05–1:35][Visual] In kf_13 and kf_15, a ~180 px empty band sits between the beam (y ≈ 548) and the count ruler (y ≈ 728), so the ruler reads as detached from the girls it measures.
   - Change: during the stacking beat, raise the ruler to 0.35 units under the fulcrum labels. It can drop back to its current lane spacing when the distances are drawn at 1:38.
6. [3:15–3:24][Visual] Both dashed fits start well above their raw step at the first case (yellow ≈ 0.8 % vs 0.2 % at day 3.5; kf_37).
   - Change: start each fit at its group's second case, or clip the first 3 days of each curve, so no curve sits visibly off its own data at the origin.
REACHES 9 IF ALL FIXED: yes. It is already 9.0. These fixes would turn the remaining nitpicks into a clean 9 with margin; no structural change is needed. The episode has a committed three-way prediction by 0:13 and a case where the guess holds (the ring). The failure is measured (+0.5 · 20 %) and its cause is named. The token beam becomes the formula through a complete cross-term proof. Two correctly cited payoffs follow, with an honest limit (3.2 days), and the landing accounts for every cold-open candidate.
KEEP: (1) The token-weighted beam, whose YELLOW fulcrum slides 2.5 → 2.7 → 2.9 → 3.0 as each layer lands, and the signed distances sliding into the PURPLE 0 that kills the cross term (1:06–2:09). (2) The friend bar as a YELLOW outline filled BLUE to μ and PURPLE beyond, carried unchanged from 2.5 + 0.5 to 190 + 445 = 635, with the "+0.5 ?" target held top-right through the derivation. (3) The fact discipline: 635 is exactly the token definition, 92.7 % is worded as a per-user statistic, the 13.9-day lead is disclosed as a fit, and the 3.2-day self-report is the stated limit.
```

## Notes by dimension (evidence)

**Hook 9.**
- Frame 0 (sheet 1, 0:01) already shows the network and "average friend ?".
- By 0:11 the YELLOW candidates 2.5 / 3 / 4 hang from drop lines (kf_05). "Pick one" (0:12.1–0:12.8) is followed by a 2.0 s hold, so the viewer commits by about 0:13.
- The stakes line (0:14.8–0:21.3) is paid off at 2:59 with the same Jane → Alice picture.
- The landing (3:25.7–3:34.5) re-forms the cold-open frame. Betty's token lands on Sue reading 4, and the bar grows to the ringed 3 (kf_39).
- Residual: the title pre-refutes 2.5 (fix 4). I did not dock it, because the 3-vs-4 choice is genuine and the 4 is paid off.

**Clarity 9.**
- Concrete before abstract throughout:
  - the guess holds on the ring (0:27–0:42);
  - it then fails by a measured amount (kf_11, "+0.5 · 20%");
  - the cause is named in plain words ("piled up unevenly") before any symbol;
  - Σk²/Σk is read off a balance;
  - the variance is built from areas, and the cross term is cancelled by the balance condition, not asserted.
- Every number recomputes (see FACTS).
- The round-9 reading-time defect in the divide step is fixed: the ÷ 8 row holds about 3 s.
- The general step "Every girl splits this way" (2:00.9–2:03) is fast but is carried by every node flashing as the row generalises. I could follow it on one watch.

**Visual 9.**
- The semantic palette holds in every settled frame I read: BLUE counted once, YELLOW reached by following a friendship, PURPLE the spread, grey axes and guess.
- Each settled frame has one focal point (kf_13, kf_19, kf_23, kf_33, kf_37). The dimmed context sits at about 35 %.
- Type is above the floor in every frame, and word blocks are 5 words or fewer ("below their own friends' average").
- Only nits remain: the olive fade at 0:43 (fix 2), the detached ruler (fix 5), and the fit start points (fix 6).

**Motion 9.**
- Objects persist and transform:
  - counts fly into the bar (0:07);
  - nodes ride into the ring (0:29) and onto the beam in nested arcs (1:01–1:03);
  - the fulcrum is live;
  - distances drop and become squares (1:39–1:43);
  - the signed distances merge into 0 (2:05–2:07);
  - the collapse lands on the baseline (2:19–2:23);
  - 190 / 445 / 635 drop out of their segments (2:46.6–2:47.8);
  - the BLUE bar splits into the eight nodes (2:58–2:59);
  - the groups shrink into the curve origins (3:07).
- 0 glyph morphs; max static 3.5 s.
- Remaining items are a slightly short hold on the two post-"So" rows (fix 1) and a 0.13 s glyph overlap in the pinch (fix 3).

**Audio 9.**
- Loudness and pace are on target: −14.0 LUFS and −2.1 dBTP, 153 wpm on speech time, no sentence above 200 wpm.
- The cold open now breathes (0.6 s and 0.8 s). Planned holds follow "Pick one" (2.0 s), "sigma squared" (1.2 s), the Facebook question (2.0 s) and "sees four" (2.2 s).
- "Christakis" is transcribed correctly, and the "girl's / girls'" homophone is gone.
- The WER residue is number formatting only ("½", "¼").
- Not docked: the held "one" in "Pick one" (0.55 s) reads as intended emphasis.

**Concision 9.**
- 495 words in 3:34.5, every beat load-bearing:
  - the ring is both the "works at first" case and the 2:26 callback;
  - Facebook is the general case and the prediction;
  - C&F is the stakes payoff with its limit.
- The eight "two and a half"s each read a number off the screen. There is no recap and no preamble.
- The tightest candidate for a cut, "Odds are, that includes you." (2:55.5), ties the 92.7 % to the title's "You", so I would keep it.

**Originality 9.**
- The examples (Feld's eight girls, Facebook 635, the Harvard flu sensors) are this topic's standard trio. The angle is not standard: tokens become a weighted beam whose balance point visibly slides from 2.5 to 3, and the gap is the variance seen as squares around the fulcrum.
- §4 sweep, 0 hits:
  - no "it turns out", no "now let's look at";
  - no question chains: the three questions at 0:08.8, 1:32.9 and 2:37.9 each stand alone with a visual answer;
  - no fake reveals, no lesson-list ending.
