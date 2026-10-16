# Review, round 2: substance critic (facts, story, clarity, concision, slop; all dimensions scored)

Evidence: I used the existing `review/` pack. metrics.json (15:43) is newer than final.mp4 (15:40), so no new pack was needed. I read:
- report.md, all 13 contact sheets, transcript.txt and the word timings, narration.txt / narration.json, script.md, facts.md and CHANGELOG.md;
- full-resolution keyframes kf_04 (0:08.5), kf_11 (1:04.5) and kf_24 (2:20.5);
- frames I extracted at 1:41.0, 2:03.0, 2:07.0, 2:13.0, 2:46.0, 3:17.0 and 3:36.0;
- a 4× crop of Sue's label at 1:04.5;
- 5 fps tiles of the equation area at 1:39.8–1:42.2 and 2:06.0–2:08.4.

Primary sources I read myself:
- Feld 1991, AJS 96(6), full text (uvm.edu mirror): Fig. 1 and Table 1, pp. 1465–1468.
- Ugander et al. 2011, arXiv:1111.4503, full PDF text.
- Christakis & Fowler 2010, PLoS ONE 5(9): e12948 (journals.plos.org).

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each person once per friend she has, so the average friend has Σk²/Σk = μ + σ²/μ friends, which is more than the average person whenever friend counts vary, and the friends of random students therefore catch flu earlier.
SCORES: Hook 8 · Clarity 8 · Visual 7.5 · Motion 8 · Audio 8 · Concision 8 · Originality 8.5
WEIGHTED: 8.0 (797.5/100)   AFTER CEILING: 8.0 (lowest 7.5 + 2 = 9.5, so the ceiling does not bind)
CAPS: Text overlapping another element → max 7. The "4" token at Sue's end of the Sue–Dale edge covers the lower right of the "e" in the "Sue" label (4× crop @ 1:04.5; also visible @ 3:36.0). It is a held state at 0:55–1:13 and 3:29–3:39, not a transition.
FINAL: 7.0   PASS: no
FACTS:
- 8 girls in "Marketville", reciprocated friendships, names fictitious, data from Coleman's The Adolescent Society | Verified | Feld 1991 p.1465 ("eight girls in 'Marketville,' one of the high schools included in the study. The names are fictitious")
- "an Illinois high school" | Verified (minor) | Coleman's schools were in northern Illinois. Note: Feld says Coleman studied "12 high schools", while facts.md says 10. Neither number is on screen, so this is harmless.
- Counts Betty 1, Sue 4, Alice 4, Jane 2, Pam 3, Dale 3, Carol 2, Tina 1; the edge list reproduces them | Verified | Feld Fig. 1 labels "4(2.75) Sue, 4(3) Alice, 3(3.3) Pam/Dale, 2(3.5) Jane, 2(2) Carol, 1(2) Tina", plus Betty 1(4); recomputed from the 10 edges
- μ = 20/8 = 2.5; 20 tokens sum to 60; friends average 3 | Verified | Feld p.1467: "a total of 20 friendships, with a mean of 2.5. The friends have a total of 60 friends, with a mean of 3.0"; Σk² = 1+16+16+4+9+9+4+1 = 60
- "half a friend too low, off by 20%" | Imprecise, not wrong | 3 − 2.5 = 0.5. As a share of the guess that is 20%; as a share of the true value it is 16.7%. "The guess was … too low, off by 20%" most naturally reads as an error relative to the truth (a guess 20% too low would be 2.4). The on-screen "+0.5 · 20%" sits on the friend bar's excess, where it correctly means "3 is 20% more than 2.5". See fix 3.
- Ring: 16 tokens, 32/16 = 2 = μ, σ² = 0 | Verified | arithmetic
- Two girls at each count 1–4; beam balances at 2.5, token stacks (2, 4, 6, 8) at (2+8+18+32)/20 = 3 | Verified | arithmetic. Pixel check on f_2:03: pair centres at 211/416/621/827 px, 205 px per friend. The BLUE ▲ is at 519 px (2.5) and the YELLOW ▲ at 622 px (3.0).
- Sue 4 × 4 = 16; Σk²/Σk = 60/20 | Verified
- 60/8 = 7.5, 20/8 = 2.5; distances 1.5 and 0.5; squares 2.25 and 0.25; total 10; σ² = 10/8 = 1.25 (population variance) | Verified | recomputed
- 7.5 = 2.5² + 1.25; (μ²+σ²)/μ = μ + σ²/μ = 2.5 + 0.5 = 3 | Verified | re-derived: Σk²/n = μ² + σ² with population σ²
- 5 of 8 below their friends' average (Betty, Jane, Pam, Dale, Tina); only Sue and Alice above; labels 4, 3.5, 3.33, 3.33, 2 / 2.75, 3 | Verified | Feld p.1465 text and Fig. 1
- "Sue is on four friend lists, Betty on one … four times as often" | Verified | P(edge end = Sue) = 4/20 vs 1/20
- Facebook, May 2011: average user about 190 friends | Verified | Ugander et al.: "721 million active users … 68.7 billion friendship edges … around 190 Facebook friends"
- Their friends averaged about 635 | Verified | Ugander et al.: "The expected number of friends at the end of a randomly chosen edge, ⟨k²⟩/⟨k⟩ = 635". This is the edge-end (token) average, which is the episode's definition. A per-user "average of friends' averages" would be a different number (Ugander Fig. 6a; Feld's 2.99 vs 3.0), so the spoken question should name the token average (fix 9).
- "A few users had thousands of friends" | Verified | "a much smaller population have many hundreds or even thousands of friends"
- "spread term more than twice the mean": 635 − 190 = 445 > 380 | Verified | arithmetic
- C&F, Harvard, 2009; 319 random students; 425 named friends | Verified | PLoS ONE 5(9): e12948: "chosen randomly from the 6,650 Harvard undergraduates (N = 319)", "friends sample (N = 425)", 1 Sept – 31 Dec 2009
- "Steps are flu diagnoses by medical staff" | Verified | Fig. 3; Results: "the friends curve for flu diagnosed by medical staff is shifted 13.9 days forward in time"
- "fitted curves put the friends 13.9 days ahead" | Verified | Abstract: 13.9 days (95% C.I. 9.9–16.6); Methods: cumulative logistic fitted by NLS
- Self-reported lead about 3 days (screen: 3.2) | Verified | "a significant but smaller shift in self-reported flu symptoms (3.2 days, 95% C.I. 2.2–4.3)"
- Citations on screen: "Feld, 1991 · Am. J. Sociology · data: Coleman, 1961"; "Ugander et al., 2011 · arXiv:1111.4503 (Facebook, May 2011)"; "Christakis & Fowler, 2010 · PLoS ONE · redrawn from Fig. 3" | Verified | authors, years and venues all correct
MECHANICS: runtime 3:39.6 · 150 wpm (speech; 529 words) · max silence 2.09 s (planned holds at 0:12.0 and 2:33.0) · lead 0.00 s / trail 1.74 s · max static 3.57 s (3:16.1) · −14.0 LUFS / −2.1 dBTP · WER 1.6 % (the diffs are ASR number formatting; the "on on" at 3:37.3 is a Whisper duplicate, since the TTS word list has a single "on" at 217.19 s) · 0 banned phrases · 0 black frames
FIXES (highest impact first):
1. [0:55–1:13 and 3:29–3:39][Visual] The "4" token at Sue's end of the Sue–Dale edge covers the "e" of "Sue" (crop @ 1:04.5, frame @ 3:36.0). This alone triggers cap 7. Move Sue's name label to the LEFT of her node, `next_to(sue_node, LEFT, buff=0.15).shift(UP*0.35)`, which is the empty region above the Betty edge. Then add an assert over every parked token position: for each name label L and token T, `L.get_right()[0] + 0.15 < T.get_left()[0]` or their y-spans are disjoint. Check Betty's label against the Betty–Sue tokens in the same pass. Removes the cap (final → 8.0).
2. [2:03.9–2:10.6][Clarity] "Seven and a half is exactly two and a half squared, plus that variance" is presented as a numerical coincidence, then generalized to μ + σ²/μ. The beam already holds the reason, and the episode doesn't use it. The cross terms vanish *because the beam balances at μ*. Insert ≈8 s after "the variance, sigma squared":
   - On Sue's column, write 4² = (2.5 + 1.5)² = 2.5² + 2·2.5·1.5 + 1.5², with the middle term in an INK box.
   - Flash the signed distances on the PURPLE line: −1.5, −1.5, −0.5, −0.5, +0.5, +0.5, +1.5, +1.5. Sum them to 0 under the BLUE ▲.
   - TransformMatchingTex the row into avg(k²) = μ² + σ².
   - Narration (≈20 words): "Every girl's k squared is two and a half squared, plus her distance squared, plus a cross term, and the cross terms cancel because the beam balances."
   This makes the formula re-derivable after one watch, and it is the episode's most memorable possible image: the same fulcrum is why the identity holds. Clarity → 9.
3. [1:02–1:06][Clarity] "The guess was half a friend too low, off by twenty percent." Relative to the true 3.0, the guess is 16.7% low. Change the narration to "The guess was half a friend too low: the friends average twenty percent more than the girls." Keep the on-screen "+0.5 · 20%" on the PURPLE excess, where it is correct.
4. [1:43–2:10][Clarity/Visual] The derivation hinges on avg(k²) ≠ (avg k)², but it is typeset as \overline{k^2}. On screen (frame @ 2:03) that is a short overbar over k², easily read as k̄², which is μ², the very quantity it must be distinguished from 15 s later. Write it as `\text{avg}(k^2)` (or ⟨k²⟩) in all three rows. On "two and a half squared" at 2:05, show "7.5 vs 2.5² = 6.25" side by side for 1.5 s before the "+ 1.25" lands.
5. [1:51–2:05][Visual/Clarity] The squares are not squares of the drawn distances. The PURPLE distance line uses the beam scale (1.5 friends = 307 px, f_2:03), while the 2.25 square's side is ≈ 88 px, so the narration's "measure each girl's distance … and square it" does not match what is drawn. For each column, `TransformFromCopy(distance_segment, square.bottom_edge)` and let the copy visibly shrink to the square scale while it drops (0.8 s, smooth), then grow it into the square. Or add a 26-pt GRAY tag "squares at ¼ scale" under the row.
6. [2:46.5–2:58][Visual/Clarity] The parked Facebook bars "190" and "635" sit inside the flu chart's plot area at y ≈ 6–7 % and x ≈ 12–45 days (f_2:46), with their row labels gone. For ~11 s they read as data plotted on "% diagnosed vs days". Park them outside the axes (above the plot frame, right of the y-axis title, at 60 % opacity). On "319 random students" / "425 friends", TransformFromCopy each bar into its curve's start point before the steps draw.
7. [1:40.5–1:42, 2:06–2:08, 2:20.5–2:22][Motion] Crossfades double-expose glyphs for 0.4–0.8 s: "Σ÷k²8" and a ghosted "60÷8" (tile @ 1:40.6–1:41.2); "σ̸²", "1.2̸5", "μ̸²/μ", "2.5̸³" (f_2:07.0); and "σ²/0⁄2" (sheet @ 2:21). Where only "÷ 8" is appended, use TransformMatchingTex with the shared terms isolated, so the old terms stay put and only "÷ 8" fades in. Elsewhere use `Succession(FadeOut(old, shift=UP*0.12, run_time=0.35), FadeIn(new, shift=UP*0.12, run_time=0.45))`.
8. [0:00–0:14][Hook] The title already says friends have *more*, so "more, fewer, or the same?" asks the viewer to commit to something the title gave away. Commit to magnitude instead. Narration: "On average, each girl has two and a half friends. Pick a girl's friend at random: how many friends does she have, on average?" Have the "?" stop on three faint candidate ticks at 2.5 / 3 / 4 before the 1.6 s hold. The fail beat then pays off a number (3.0), not a direction.
9. [2:30–2:33][Clarity] "How many friends did their friends average?" is ambiguous, since a per-user average of friends' averages is a different statistic from Ugander's ⟨k²⟩/⟨k⟩ = 635. Say instead: "If every friendship sent a token, what would the tokens average?" That is exactly the 635 and reuses the episode's own mechanic.
10. [3:15–3:20][Motion/Clarity] "the lead shrank to about three" appears only as the text "self-reported: 3.2 days" (f_3:17). On "shrank", Transform a copy of the 13.9-day arrow into a 3.2-day GRAY arrow (≈ 32 px at this scale) just below it, label it buff 0.15, and move "fitted lead: 13.9 days" next_to its own arrow. Today that label floats ≈ 200 px to the right of the arrow.
11. [3:27.8–3:39][Hook/Visual] The closing frame has no focal point. At 3:36 all 20 tokens are equally bright and Sue's four are indistinguishable from the rest. The line restates the mechanism; it does not re-see the cold open.
   - On "Follow any friendship", dim every token except Sue's four and Betty's one to 30 %. Pulse Sue's four (scale 1.3) on "a Sue" and Betty's one on "a Betty".
   - Replace the last sentence with one that re-sees the opening question from inside the network: "Betty looks at her one friend and sees four. From most seats in this class, the view is the same."
12. [0:18–3:34][Audio] Every sentence is followed by an almost identical 0.4–0.5 s pause (60+ entries in the silence list), which gives a metronomic TTS cadence. Cut intra-paragraph sentence gaps to 0.2–0.3 s, and keep 0.6–0.8 s only at beat boundaries (0:23, 0:49, 1:12, 2:23, 2:44, 3:19).
13. [0:30–0:49][Concision] The ring "easy case" runs 19 s to show 2 = 2. Cut "And in an easy case, the guess holds." Run the 16 ring tokens with lag_ratio 0.04 over 2.5 s. Keep the ring, because the 2:21 "no spread, no gap" callback needs it. Saves ≈ 5 s.
REACHES 9 IF ALL FIXED: yes, narrowly. Fix 1 removes the cap (→ 8.0). Fixes 2–5 and 9 make the derivation re-derivable and unambiguous (Clarity 9). Fixes 5–7 and 10–11 give every frame one focal point and every change a motion (Visual 9, Motion 9). Fix 8 makes the commitment real (Hook 9). Fixes 12–13 lift Audio and Concision to 8.5–9. With Originality at 9 (fix 2's "the balance point is why the cross terms cancel"), the estimate is ≈ 8.9–9.0. No structural change is needed: the misconception is voiced (0:23), the failure is measured (+0.5, 0:57–1:06), the one picture becomes the formula (1:12–2:23), there are two correctly cited real payoffs with an honest limit (3.2 days), and the landing returns to the opening network.
KEEP: (1) the token-balance beam: girls balancing at 2.5, token stacks at 3, both fulcra geometrically exact, with the purple distances hanging off the same fulcrum; (2) the friend bar as a YELLOW outline filled BLUE to μ and PURPLE beyond, reused for Facebook (190 + 445 = 635); (3) the redrawn C&F step curves with shared-shape fits and the self-report caveat. Every number in the episode checks out against the primary sources.
```

## Notes by dimension

**Hook (8).** Frame 0 shows the real network (sheet 1 @ 0:01). The question lands at 0:08.7–0:12.0, then a 2 s hold with the "?" keyed to "more / fewer / same". The stakes line follows at 0:14 (watch random students or their named friends), drawn as Jane → Alice. The misconception is voiced fairly at 0:23 ("every friend is one of these same eight girls"). Two things keep it below 9: the title gives away the direction of the answer, and the stakes set up at 0:14 pay off only at 2:44.

**Clarity (8).** The chain token → Σk²/Σk → ÷8 → avg(k²)/μ → variance squares → μ + σ²/μ is concrete-first and every number checks out. The remaining issues:
- The identity avg(k²) = μ² + σ² is shown as a coincidence for this one case, then used as a law (fix 2).
- \overline{k^2} is visually confusable with μ² at the exact point where the two must be told apart (fix 4).
- The square sides are not the drawn distances (fix 5).
- "Off by 20%" uses an unstated baseline (fix 3).
- The Facebook question is ambiguous about which average it means (fix 9).

None of these is a factual error under BAR §3, but together they mean a viewer could not yet re-derive the formula after one watch.

**Visual (7.5).** The palette is strictly semantic: BLUE = person counted once, YELLOW = reached by a friendship, PURPLE = spread. Dimming hierarchy works (1:51–2:18), citations sit bottom-left, and word load is low. Deductions:
- the held label/token overlap at Sue (cap);
- the Facebook bars inside the flu axes (2:46–2:58);
- during the Facebook beat (2:23–2:44), the dimmed beam fills the left 55 % of the frame;
- the square-scale mismatch;
- a closing frame with no focal point.

**Motion (8).** Most motion carries meaning: counts fly into the μ bar (0:07), tokens travel edges and show the count they read, the YELLOW outline overshoots the dashed guess (1:01), girls slide onto the beam (1:13–1:19), area labels travel into σ² (2:00), and denominators rise into μ² (2:07). Deductions: glyph double-exposure crossfades in three places, and the 3.2-day result is text only.

**Audio (8).** Pace is 150 wpm, loudness is on target, pronunciation is clean ("Christakis" is transcribed correctly; WER diffs are number formatting only). Deictics land: "Four on Sue, four on Alice, one on Betty" (1:09–1:12) pulse the right tokens; "Sue holds four tokens" (1:29) draws the box; "only Sue and Alice" (3:24.6) gets outlines at ~3:26, within ±2 s. Deduction: uniform post-sentence pauses give a mechanical rhythm (fix 12).

**Concision (8).** There is little slack, but the ring beat (0:30–0:49) is a long demonstration of an identity. The Facebook beat (21 s) earns its place as the general case and second prediction. About 5 % is removable.

**Originality / non-slop (8.5).** No banned phrases, no question chains, no "it turns out", no empty superlatives. The prose is nouns and numbers that point at the screen. The token/beam device and the real redrawn Harvard curves are fresh and specific. Fix 2 (the balance point is *why* the cross terms cancel) would be the shareable, non-obvious image that lifts this to 9.
