EPISODE: 004 — "The Hidden Bias That Hid the Hot Hand"
IDEA: If you average "share of heads after a heads" row by row over short sequences, a fair coin reads 17/42 instead of 1/2, because each row gets one vote and checked heads crowd into a few rows. The same bias puts a random shooter at −8 points on the 1985 after-3-hits minus after-3-misses test, so Cornell's +4 is really about +12.
SCORES: Hook 9 · Clarity 9 · Visual 9 · Motion 8.5 · Audio 9 · Concision 8.5 · Originality 9
WEIGHTED: 8.9 (15·9 + 25·9 + 15·9 + 15·8.5 + 10·9 + 10·8.5 + 10·9 = 887.5 → 8.875, rounded half-up)   AFTER CEILING: 8.9 (lowest score 8.5; 8.5 + 2 = 10.5, so the ceiling does not bind)
CAPS: none. I checked each one:
- Runtime 3:31.0.
- Pace 150 wpm over speech time.
- Loudness −14.1 LUFS and −2.1 dBTP.
- Longest internal silence 2.17 s, the planned prediction hold at 0:12.7–0:14.8.
- Longest static stretch 3.53 s, at 3:06.6–3:10.2.
- 0 black frames and 0 banned phrases. No rhetorical-question chain: the opening question is one question.
- The layout audit passed 227 settled frames.
- Both studies are cited on screen whenever they are used.
- 7 of 7 deictic words land within the window.
- I found no settled overlap or clipping in any keyframe I read.
- The 2:41–2:43.6 cursor/label mismatch (fix 1) is a motion and clarity defect, not cap 6. Its labels state correct values, and the move is a visibly rigid slide of the pair toward the zero line. But it is the closest thing to a plotted-data error in the cut, and it must go.
FINAL: 8.9   PASS: no

FACTS:
- 4 flips give 16 equally likely sequences | Verified | 2^4 = 16 (my own enumeration)
- In HHTH, the checked flips are H and T, so 1/2 | Verified | enumeration
- HHHT checks 3 flips and 2 are heads | Verified | enumeration
- TTTH and TTTT have no score, so 14 rows are scored | Verified | enumeration
- Dot stacks at 0:59.6 (kf_14): 0 ×6, ½ ×4, ⅔ ×1, 1 ×3 | Verified | enumeration
- The average is 17/42 = 40.5%, so it "reads cold by 9.5 points" | Verified | my own enumeration gives 17/42, and 50 − 40.48 = 9.52
- 24 checked flips (12 H, 12 T), so the pooled share is exactly ½ | Verified | Σh = 12, Σn = 24, recomputed
- 12 heads sit in 8 rows and 12 tails in 11 rows | Verified | recomputed: 8 and 11
- Heads hold 5⅔ of the 14 votes; 5⅔/14 = 17/42; tails hold 8⅓ | Verified | Σhᵢ/nᵢ = 17/3, recomputed
- After a tails the reading is 25/42; the gap is −19 points | Verified | recomputed 25/42 and −19.05
- GVT 1985, *Cognitive Psychology*: "a powerful and widely shared cognitive illusion" | Verified | GVT 17(3):295–314; the quote as reproduced in M&S 2018 fn. 8 (facts.md 13)
- 26 Cornell players, up to 100 shots each, from where they would hit about half | Verified | M&S 2018 §3.1 and Table 2
- A random shooter (n = 100, k = 3) scores 46% after 3 hits and 54% after 3 misses, a gap of about −8 points | Verified | M&S 2018 §3.2 ("−8 percentage points"); the exact DP in check_numbers.py
- Cornell: 49% after 3 hits and 45% after 3 misses, so +4, "too close to zero to count" (on screen "vs 0: p = .49") | Verified | M&S 2018 §3.1 (GVT's paired t-test, replicated at p = .49)
- Longer records shrink the bias; the 1,000-shot ghost sits at about −0.7 | Verified | M&S abstract; facts.md 18 (the 10⁶-rep simulation gives −0.71)
- Measured from −8, the +4 is +12 | Verified | arithmetic
- "Evidence for a hot hand in a gym, not proof it survives defenders in a game" | Verified (stated as a limit) | M&S §3.1
- Miller & Sanjurjo 2018, *Econometrica* | Verified | 86(6):2019–2047

MECHANICS: runtime 3:31.0 · wpm 150 (speech time) · max silence 2.17 s (planned) · max static 3.53 s · −14.1 LUFS / −2.1 dBTP · leading 0.00 s, trailing 1.74 s · WER 1.1%
- The transcript differences are all benign:
  - "a half" was heard as "point five" (1:01).
  - "a" was heard as "one" (2:22, 2:48).
  - "two-thirds thirds" at 1:44.3 is a whisper token split. The word timings overlap (104.20–104.62 and 104.35–104.63), which is not a stutter.

## Evidence read
- **Pack:** I used the `review/` pack. metrics.json (18:59) is newer than final.mp4 (18:57).
- **Documents:** report.md, all 12 contact sheets, transcript.txt, transcript_words.tsv (1:40–1:52), narration.txt, script.md, the facts.md head, the round-7 craft review, and the round-7 CHANGELOG.
- **Full-resolution keyframes:** kf_04 (0:11.1), kf_06 (0:24.3), kf_14 (0:59.6), kf_19 (1:31.0), kf_23 (1:46.9), kf_25 (1:58.2), kf_28 (2:05.7), kf_32 (2:42.6), kf_34 (2:51.8), kf_35 (3:09.3), kf_38 (3:25.5) and kf_40 (3:31.0).
- **Frame strips** extracted with ffmpeg into /tmp/ep4r8:
  - zoom: 2:40.5–2:46.5 at 3 fps
  - regroup: 1:16–1:20.5 at 3 fps
  - mirror gap label: 2:11.5–2:14.5 at 4 fps
  - Σ build: 1:50.5–1:53.5 at 4 fps
  - landing: 3:18.5–3:23.5 at 3 fps
- **Numbers:** I recomputed every coin number by enumeration in Python: 17/42, 17/3, 12/12, 8/11, 25/42, −19.05 and 9.52.

## What changed since round 7, and whether it worked
- **Focal point at 1:19–1:35: fixed.** From "each row gets one vote" (1:19) the table, the pooled strip, Σh/Σn and "the obvious guess" sit at about 30%. Only the vote strip plus the named row is bright: HHHH at 1:27, HTTT at 1:31 (kf_19), the 8 heads rows at 1:35 and the 11 tails rows at 1:37. This now reads like a 3b1b frame.
- **17/42 shown when spoken: fixed.** "17/42 = 40.5%" is beside the marker from 0:57 (kf_14).
- **Hidden rescale at 2:44: mostly fixed.** The zoom is now visible (strip 2:43.8–2:45.2). The 0/25/75/100 ticks run out and −10…+10 grow in on the same marks, and the −8 cursor rides out. But the slide that comes before it introduced a new defect (fix 1).
- **Equation cadence: fixed.** 5⅔/14 = 17/42 is complete from about 1:47.3 and holds through 1:51 (sheet 7). The Σ build follows about 3 s later, and the pooled formula brightens instead of arriving (1:57).
- **Lineup run-on: fixed.** The silences are 1:40.0–1:41.0, 1:41.9–1:42.8, 1:46.0–1:47.1 and 1:49.3–1:50.9.
- **Cut lines:** "Score every row the same way" and "Longer streaks grow the bias" are both gone.
- **No copy crosses the after-tails strip:** confirmed by the 2:05.7 frame (kf_28) and sheet 8.
- **Landing ghost: fixed.** It is up at 75% (3:17), the dashed guess steps back, and it is held, then the rows fly one at a time (strip 3:18.5–3:20.5).
- **Cornell printed once at the end: fixed** from 3:05 on (kf_35). Between 2:51 and 3:04 it is still printed twice (fix 4).

## What I saw, beat by beat
- **0:00–0:15 Cold open.**
  - HHTH, the blue check arcs and the rings are on screen from 0:01. The yellow 1 and blue 2 build "1/2" from the disc and the rings (0:05–0:07).
  - The ghost of the 16 runs deals in under the dimmed row (0:09) and collapses to "?".
  - The three answers appear where they sit on the axis (0:11–0:13), followed by a 2.2 s hold.
  - The viewer commits by 0:12.8.
- **0:15–0:32 Stakes and test.**
  - "= 1/2" becomes "the obvious guess" with the dashed line (0:17). The GVT citation arrives on "1985" (0:19).
  - H/T morph to hit/miss on "basketball shots" (0:23, kf_06). The verbatim quote appears on "illusion" (0:25–0:27).
  - "→ hot" appears on "beats their usual rate" (0:29).
- **0:32–1:05 Fail.**
  - The big row shrinks into its slot in the 4×4 table (0:37–0:39).
  - HHHT is boxed on "This row" (0:43) and its 2/3 written as "heads" lands (0:45).
  - TTTH and TTTT are boxed and dimmed on "no score" (0:47–0:51).
  - The dots fall onto the line (0:53). The marker slides 46.5% → 40.5% with "17/42 =" (0:55–0:57).
  - Red "cold −9.5 points" appears on "nine" (1:01–1:03).
  - This is a measured failure, shown on screen.
- **1:05–1:58 Insight.**
  - The pooled 24-tile strip lands on the dashed 50% (1:07–1:09). The tile counts become 12/24, and Σh/Σn is written from the table digits (1:11–1:13).
  - The regroup into the one-vote strip is in motion at 1:16.7–1:18.4 (strip).
  - The boxes are in focus (see above).
  - The decisive move is the yellow packing onto the 40.5% marker (1:43, sheet 6). "5⅔ votes" and "8⅓ votes" are labelled over the strip, and 5⅔/14 = 17/42 is built in the right column (1:45–1:49).
  - The 14 outlines lift off and fly into 1/14 Σ, and all 14 row ratios flash as hᵢ/nᵢ is written (1:51–1:54). The pooled formula returns on "ratio of totals" (1:57, kf_25: two formulas aligned on their "=").
  - The animation is the proof here.
- **1:58–2:15 Mirror.**
  - The vote strip becomes the "after heads" lane with 17/42. A copy drops, recolours, and turns a half turn about the dashed line (2:01–2:05).
  - "25/42" is written in place (2:09). A red L-arrow between the cursors carries "−19 points" (2:13–2:15).
- **2:15–3:15 Payoff.**
  - The lanes clear to "?" under "1985 design". "26 players" and "up to 100 shots" join on the words (2:19–2:23).
  - The ●●● and ○○○ conditions appear (2:19). "the obvious guess" sits on 50% (2:27).
  - "random" heads the column. The cursors move to 46% and then 54% on the spoken numbers (2:33–2:39), and the M&S citation is in by 2:33.
  - The pair slides (2:41.3), the axis zooms (2:43.8–2:45.2), and −8 becomes "bias" (2:45). The 1,000-shot ghost slides on "Longer records" (2:47–2:49).
  - Cornell: the purple header appears, and 49/45 replace 46/54 in the same slots (2:51–2:57). "49 − 45 = +4" grows with the purple marker (2:59–3:01), then "vs 0: p = .49" (3:01–3:03).
  - The chart re-centres, and the +12 brace grows on "twelve" (3:05–3:07). "no defenders" appears on "in a gym" (3:11).
- **3:15–3:31 Landing.**
  - The cold-open row, the axis and the dashed guess return (3:15). The ghost is up at 75% (3:17).
  - The rows fly into (1/14)Σhᵢ/nᵢ, and the blue marker and "= 17/42" appear (3:20–3:23).
  - The row becomes hit/miss (3:25). A blue dot appears on ½ with "its rows average 1/2" (3:27), then the blue arrow to it, "hot" (3:29).
  - The 1.7 s hold ends the video. The last frame (kf_40) re-sees the first frame exactly.

## Deductions (evidence)
- **Motion, −0.5**
  - **2:41.3–2:43.6 (zoom strip, frames 3–9; kf_32): positions contradict their labels on a labelled axis.**
    - On "twenty eighteen paper" the cursor pair slides left until after-misses sits on the dashed line.
    - The axis still reads 0%…100% with the title "checked shots that are hits". So for about 2.3 s the after-hits cursor stands at about 42% (x ≈ 673 px in kf_32; 0% is at 163 and 100% at 1378). The after-misses cursor stands at 50%.
    - Meanwhile the right column, in the same blue, reads "46%" and "54%".
    - This is the one frame in the episode where the chart says something false. A viewer pausing at 2:42 reads "46% plotted at 42%". It also spends the slide before the zoom that explains it, so the motion carries no relation the viewer can read at the time.
  - **2:44.0–2:44.3 (strip frame 11): the axis is briefly unlabelled.** The % tick labels and title have left and the new labels have not yet arrived, so the axis carries no labels at all for about 0.3 s. This is a nitpick.
  - **3:19.6–3:20.3 (landing strip frames 4–5): the ghost rows bunch in flight.** The rows cross each other and the dashed line as an unreadable 0.6 s cluster on their way into the formula. This is a nitpick, but it is the episode's final transform.
- **Concision, −0.5**
  - **1:37.6–1:40.0: "Crowded heads split their votes."** It restates 1:25.6–1:31.8 ("three heads share a single vote, while this lone tails gets a whole one") and 1:32.6 ("Twelve heads crowd into eight rows"). The pulse of the five third-of-a-vote slices it accompanies could run under "Line them up" with no loss. With its 1.0 s gap, about 3.4 s is slack.
  - **"out of forty two" is spoken 4 times** (0:56, 1:48, 2:08 as 25/42, 3:20). The 1:48 and 3:20 uses are deliberate (the derivation lands on the measured number; the landing callback), so I make no further deduction. I note it because the kit flags it.
  - **Runtime 3:31.** This is within budget, and the rest of the script earns its time.
- **Visual: no deduction below 9, but these are the residual nitpicks.**
  - 2:51–3:04 (kf_34): "Cornell" is printed twice, in the purple header "Cornell, 1985" and the purple column head "Cornell".
  - 2:17–2:41 (sheets 8–9): on the 0–100% lanes, the key 46↔54 gap is 0.72 units wide. The frame's most legible numbers live in the side column, not on the chart, until the zoom.
  - 0:41–1:05 (kf_14): the table coin letters are at the 24 px floor. Colour carries H/T, so this is acceptable.
- **No deduction to Clarity.** Every number recomputes, the assumptions are stated (fair coin, a gym, no defenders), and the significance logic is shown ("vs 0: p = .49"). The single exception is the 2:41–2:43 frame, scored under Motion. Fixing it also protects Clarity.
- **No deduction to Audio.**
  - The lineup now breathes, at 1.0, 0.9, 1.1 and 1.6 s.
  - The pauses after −9.5, −19, −8 and +12 are each 1.0–1.7 s (silence list).
  - The 7 deictic words all land on screen events: "Here" at 0:04.8, "This row" at 0:41.7, "Here, three heads" at 1:25.6, "this lone tails" at 1:30, "Line them up" at 1:41.
  - The kit's cadence line still shows a 0.35 s median full stop, so cadence is not at the 10 level.

FIXES (highest impact first):
1. [2:41.3–2:43.6][Motion/Clarity] The cursor pair slides to 42%/50% on an axis still labelled 0–100% while the column reads 46%/54% (kf_32). Reorder the move so the zoom happens first, with no slide:
   - On "twenty eighteen paper", leave the cursors at 46/54. Draw the red gap with its "−8" between them. Then, on "puts the gap", run the ×5 zoom about the 50% line, carrying both cursors (46 → 30% and 54 → 70% in screen terms). Fade the % labels to 0 in the first 0.4 s.
   - Only once the % labels are gone, slide the pair right by the after-misses offset (0.8 s, smooth) while −10…+10 grow in, so after-misses lands on 0 and after-hits on −8.
   - Alternatively, keep the current order but fade the % tick labels and the axis title to 0 over 0.4 s *before* the slide starts, and put a grey "gap from 0" label on the dashed line during the slide.
   - Either way, no frame shows a cursor at a % its label contradicts.
2. [1:37.6–1:40.0][Concision] Cut "Crowded heads split their votes." and its 1.0 s gap. Move the HHHH/HHHT third-of-a-vote pulse to start with "Line them up:" (it already has a [pause 0.8] for the pack). This saves about 3.4 s, giving about 3:27.6, and removes the double explanation.
3. [3:19.6–3:20.3][Motion] The landing ghost rows bunch in flight. Raise the row lag from 0.06 to 0.12, path each row up and over the formula's left edge (arc, path_arc = −0.6), and fade each row to 40% as it leaves its slot, so at most 3 rows are in flight at once and none crosses the dashed line.
4. [2:51–3:04][Visual] "Cornell" is printed twice (header plus column head, kf_34). Keep the column head as the source of truth: make the header read "1985 data" (grey), or drop the column head and let the purple header label the column by moving it to the column's top (x ≈ 5.0). This mirrors the 3:05 fix, which already prints it once.
5. [2:44.0–2:44.3][Motion] The axis is unlabelled for about 0.3 s mid-zoom. Start growing −10…+10 0.3 s earlier, overlapping the outgoing % labels (both ≤ 40% opacity during the overlap), and keep the axis title cross-fading rather than gone. With fix 1 this may fall out naturally.

REACHES 9 IF ALL FIXED: yes. Fix 1 lifts Motion to 9 (with fix 3) and fix 2 lifts Concision to 9: 15·9 + 25·9 + 15·9 + 15·9 + 10·9 + 10·9 + 10·9 = 900 → 9.0. No structural change is needed. The hook, failure beat, one-picture insight, payoff and landing are all in place.
KEEP: the yellow vote slices packing exactly onto the 40.5% marker and turning into 5⅔/14 = 17/42 (1:41–1:49); the half-turn mirror of the vote strip about the 50% line into −19 (2:01–2:15); the landing that re-sees the cold-open row and answers its question with (1/14)Σhᵢ/nᵢ = 17/42 and the blue "hot" arrow (3:15–3:31).
