# Round 3 review: substance (science and story editor)

Evidence: `review/` pack (metrics.json 19:53 is newer than final.mp4 19:52), all 13 contact sheets, keyframes kf_05, kf_12, kf_21, kf_24, kf_29, kf_30, kf_34, kf_36, and extra ffmpeg frames at 0:02.0, 0:43.0, 1:44.6, 1:45.0, 1:45.6, 1:46.2 and 2:48.5. I also read script.md, facts.md, narration.txt, transcript.txt and narration_diff.txt. Sources were checked against the PLoS ONE full text, the arXiv PDF of Ugander et al. (grepped), and secondary summaries of Feld 1991.

```
EPISODE: 060 — "Why Your Friends Have More Friends Than You"
IDEA: Following a friendship lands on each person once per friend she has, so the friend average is avg(k²)/μ = μ + σ²/μ, which exceeds the person average whenever friend counts vary. Flu researchers exploit that gap.
SCORES: Hook 8.5 · Clarity 8.5 · Visual 8 · Motion 8.5 · Audio 8.5 · Concision 8.5 · Originality 8.5
WEIGHTED: 8.4   AFTER CEILING: 8.4 (lowest 8 + 2 = 10, not binding)
CAPS: none. No factual errors, 0 banned phrases, every empirical claim cited on screen, mechanics in range, layout audit clean. The overlaps I saw are transitional only (1:45.0, 2:48.5).
FINAL: 8.4   PASS: no
```

## FACTS

| Claim | Verdict | Source / check |
|---|---|---|
| Eight girls, "an Illinois high school", every (reciprocated) friendship | Verified | Feld 1991 Fig. 1 ("Marketville", Coleman 1961, northern Illinois schools). Psychology Today's summary of Feld confirms Betty's only friend is Sue and Sue's friends are Betty, Alice, Pam and Dale. |
| Counts 1,4,4,2,3,3,2,1; mean 2.5 | Verified | Recomputed from the edge list: Σk = 20, 20/8 = 2.5 |
| 20 tokens sum to 60, friends average 3 | Verified | Σk² = 1+16+16+4+9+9+4+1 = 60. I counted the 20 tokens in kf_12 by edge: 5+7+7+5+6+8+7+7+5+3 = 60. Each token sits at the correct end. |
| "half a friend too low", "20% more" | Verified | 3 − 2.5 = 0.5; 3/2.5 = 1.20 |
| Ring: every token reads 2, 32/16 = 2 | Verified | 8 nodes and 8 edges give 16 tokens |
| Beam balances at 2.5 (girls) and 3 (tokens) | Verified | I measured node x-positions in kf_21. The token-weighted mean x = 12439/20 = 622 px against the yellow fulcrum at about 621 px, so the drawn beam is physically honest. |
| Sue: 4 tokens × 4 = 16; k² on top, k on bottom; 60/20 | Verified | arithmetic |
| ÷8: avg(k²) = 7.5 over μ = 2.5 | Verified | 60/8, 20/8 |
| Squared distances 2.25 (×4) and 0.25 (×4); σ² = 10/8 = 1.25 | Verified | population variance; 6.25 + 1.25 = 7.5 |
| 4² = (2.5 + 1.5)² = 2.5² + 1.5² + 2·2.5·1.5 | Verified | 6.25 + 2.25 + 7.5 = 16 |
| Cross terms cancel because the distances sum to 0 (the beam balances) | Verified | Σ(k − μ) = 0 by the definition of μ. On screen: −1.5, −0.5, +0.5, +1.5, two girls each. |
| avg(k²) = μ² + σ²; friends average μ + σ²/μ = 2.5 + 0.5 | Verified | re-derived |
| "The ring had no spread, so it had no gap" | Verified | σ² = 0, so the gap σ²/μ is 0 |
| Facebook 2011: average about 190 friends | Verified | Ugander, Karrer, Backstrom & Marlow, arXiv:1111.4503: "around 190 Facebook friends" |
| Token average about 635 | Verified | Same paper: "The expected number of friends at the end of a randomly chosen edge, ⟨k²⟩/⟨k⟩ = 635" |
| "A few users had thousands of friends" | Verified | Same paper: "a much smaller population have many hundreds or even thousands of friends" |
| Spread term (445) "more than twice the mean" | Verified | 635 − 190.6 = 444.4 > 380 |
| Christakis & Fowler, Harvard, 2009 | Verified | PLoS ONE 5(9): e12948 (2010): flu monitored Sept 1 – Dec 31, 2009 |
| 319 random students, 425 named friends | Verified | PLoS ONE Methods (from 6,650 undergraduates) |
| Fitted curves put friends 13.9 days ahead | Verified | Abstract and Results: medical-staff diagnoses, 13.9 d (95% CI 9.9–16.6) |
| Self-reported symptoms: lead about 3 | Verified | Results: 3.2 d (95% CI 2.2–4.3) |
| Five girls have fewer friends than their friends' average; only Sue and Alice have more | Verified | Recomputed: Betty 1<4, Jane 2<3.5, Pam 3<3.33, Dale 3<3.33, Tina 1<2. Sue 4>2.75, Alice 4>3, Carol 2=2. |
| Sue landed on 4× as often as Betty; Betty "sees four" | Verified | 4/20 against 1/20; Betty's only friend is Sue |
| "More friends means more ways to catch flu, so friends should get sick first" | Verified (loose) | C&F's stated rationale is centrality, which means earlier infection. "More ways to catch flu" also suggests more infection overall, but the redrawn totals are equal (7.5% vs 7.8%). See fix 6. |

## MECHANICS

```
MECHANICS: runtime 3:37.2 · wpm 159 (speech) · max silence 2.08 s (planned prediction holds at 0:10.6 and 2:35.9) · max static 3.43 s (0:58.4–1:01.8) · −14.0 LUFS / −2.1 dBTP · leading 0.00 s / trailing 1.75 s · WER 0.9% · 0 banned phrases
```

## Transcript and slop audit

- §4 banned phrases: 0. Banned patterns: none. There is one question per prompt (0:08 and 2:31), no question chains, no "it's not just" constructions, no fake-reveal colons, and no recap ending.
- Signposting: "Now restore…" once, which is allowed.
- Script versus transcript: the only differences are number normalization ("twenty oh nine" heard as "2009") and "Sue's" heard as "sues". No term sounds mispronounced; "Christakis" transcribes correctly.
- Hook: the network is on screen in frame 0. The question "How many friends does the average friend have?" lands at 0:08.1–0:10.6, followed by a 2.1 s hold. Stakes come at 0:12.7. Both are inside 0:15.

## Story

The structure is the strongest part of this episode. The cold-open number leads to the naive guess voiced as reasonable (0:21). The guess is then confirmed on a hypothetical ring (0:27–0:42), the SMH "it works at first" beat. On the real network it fails by a measured 0.5, or 20% (0:53–0:59). The cause is named: tokens pile up unevenly. One picture, the token beam, turns into the formula. The ring then explains its own success ("no spread, no gap", 2:23). The episode generalizes to Facebook with a prediction pause, pays off with C&F and states their honest limit (self-report, 3.2 days), and returns to the eight girls from Betty's seat. Tension rises through the ring check and the failure. The weak spots are the opening commitment, since the title already says "more" and the ? floats over three unlabelled candidates, and the 8 s of empty C&F axes at 2:48–2:56.

## FIXES (highest impact first)

1. **[2:47–2:56][Visual/Clarity]** The C&F axes are empty for about 8 s. Meanwhile the Facebook numbers ("average user 190", "average friend 635", kf_30) sit as a legend above a chart of Harvard flu data, so two datasets share one frame and the 190/635 numbers seem to describe Harvard. **Change:**
   - Strip the numbers from the legend when it parks, and relabel its two bars at once as "random person" (BLUE) and "named friend" (YELLOW).
   - Start growing the step curves on "tested this at Harvard" (about 2:50.5), not on "sick first" (2:55), so the chart is never empty for more than 2 s.
2. **[1:44.6–1:45.8][Motion/Visual]** The eight area labels are copied on top of the originals before they fly. For about 0.5 s the doubled glyphs read as "2225" and bold "0.25" (frame 1:45.0). **Change:** dim the original labels to 40% in the same `AnimationGroup` as the copies lifting, and give each copy a +0.25 y offset before the flight to the σ² row. Alternatively, fly the originals and leave the squares labelled only by size.
3. **[2:01–2:09][Visual]** The right column shows four rows at once: σ², the expansion or identity, the dimmed main row "avg(k²)/μ = 7.5/2.5 = 3.0", and the dimmed bar panel. That gives the boxed cross term three competitors (kf_21). **Change:** fade the old main row to 0% at 1:49 (it is rebuilt from the identity at 2:09 anyway), and keep the bar panel at 25%. That leaves only the σ² row, the identity row and the beam's signed distances.
4. **[0:42.7–0:43.6][Clarity]** During the reset, the friend-bar readout counts down through "1.9" while the girl bar still reads 2.0 (frame 0:43.0). For about 0.5 s the screen claims friends average less than girls. **Change:** `FadeOut` the ring's friend fill and readout (or set them to empty instantly) instead of animating the value down.
5. **[1:57–2:05][Clarity]** "avg(d)" appears on screen but "d" is never named, either aloud or on screen. **Change:** when the 1.5 distance label is copied into (2.5 + 1.5)² at about 1:53, attach a small PURPLE tag "d" under the distance ruler ("d = distance"), and keep it until 2:09.
6. **[2:51–2:56][Clarity/Correctness]** "More ways to catch flu" predicts that friends get sick more often, but the redrawn curves end level (friends 7.5%, random 7.8%) and the claim is about timing. **Change** the narration to C&F's own mechanism, keeping the word count: "Friends sit closer to everyone else in the network, so they should catch it first."
7. **[0:08–0:12.7][Hook]** The title already answers "more", and the "?" glides over unlabelled ghost lines, so the viewer has no clear choice to commit to. **Change:**
   - During the hold, show the three candidates as YELLOW numbers "2.5 · 3 · 4" under the friend row, at the ghost lines.
   - Extend the hold from 1.6 s to 2.0 s.
   - Make the line ask for a number: "How many friends does the average friend have? Pick one."

   The viewer then commits to a number, and the 0:53 payoff ("half a friend too low") lands against that choice.
8. **[1:37–1:47][Clarity]** "squares at ¼ scale" is ambiguous: the sides are at ¼, so the areas are at 1/16. **Change** the tag to "side = distance (¼ scale)", and label the first square "1.5² = 2.25" so the viewer reads area as distance squared.
9. **[3:07–3:10][Clarity/Honesty]** The dashed fits are the producer's refit with the shift forced to C&F's 13.9 days; a free refit gives 14.5. **Change** the read-out to "C&F fitted lead: 13.9 days", or add "(shape refit, shift from C&F)" to the citation line.
10. **[2:48.0–2:49.0 and the held legend][Visual]** While the legend shrinks, "average user" touches its bar (frame 2:48.5), and the held gap is about 7 px. **Change:** set the label-to-bar buff to ≥ 0.15 units (20 px) throughout the shrink.

REACHES 9 IF ALL FIXED: yes, narrowly, and with no structural change. Fixes 1–4 lift Visual and Motion to 9, fixes 5, 6 and 8 lift Clarity to 9, and fix 7 lifts Hook to 9. That gives about 15·9 + 25·9 + 15·9 + 15·9 + 10·8.5 + 10·9 + 10·8.5 = 8.9 to 9.0. If fix 7 is skipped, the episode stays near 8.8. Originality is held at 8.5 because the eight-girl example and the Harvard flu study are the canonical pair used in almost every friendship-paradox explainer. The token beam is what makes this version distinct.

KEEP:
- The token beam with physically exact fulcra (2.5 blue, 3 yellow). The cross terms cancel *because the beam balances*, and that is the one picture: the right idea, honestly drawn.
- The ring "what if" that works first and is explained at the end ("no spread, no gap"): naive build, fail, then the cause.
- The YELLOW-outline / BLUE / PURPLE friend bar reused for Facebook (190 + 445 = 635), and the redrawn C&F curves with the self-report caveat.
