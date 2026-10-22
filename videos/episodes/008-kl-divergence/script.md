# Episode 8 — The Distance That Isn't Symmetric

**Idea (one sentence):** KL divergence only charges where its *first* distribution puts
its mass, so swapping the order changes the answer: with the data first, a one-bell model
must cover every hump; with the model first, it may ignore a hump but must never wander
where the data isn't.

**The episode's own picture:** one bell over the data, and under it *two bills* for that same
bell, the data-first bill and the bell-first bill, kept side by side. As the bell slides from A
to B, one bill drains while the other swells into a mountain: each order has its own closest
bell.

Runtime ≈ 3:32 · 545 words · ≈ 162 wpm over speech time · voice af_heart, speed 0.84.
Pronunciation overrides: Kullback, Leibler ("lie-bler"), Blei ("bly"), the letter A (/eɪ/, misaki
reads a lone "A" as the article), "imagines" (misaki says "im-AY-jen-eez"). Sentence gaps are
varied on purpose: ≈ 0.25 s inside a thought, ≈ 0.7–1.0 s after a payoff number or at a beat
turn, a 1.5 s hold after each of the two prediction questions.

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | the data: the 272 eruption bars, the smoothed curve, every `p`, the words "data" (and, in the payoff, the same curve standing in for a "posterior", with its spread 1.14) |
| PURPLE | the bell (the model): bells A and B, every `q`, the words "bell" / "model", their stats labels and `→ A` / `→ B` |
| RED | the divergence in bits: every "bits" number, the `log₂` term, the two shaded bills |
| YELLOW | focus: the 1 / 2 / 3 bet, the length being examined (scanner), the ×2 doublings, "?", highlight boxes and underlines, the "moves" arrow, 15 % |
| GRAY | axes, citations, the negative ("refund") part of a bill, clipped stretches and their true values |
| INK | labels |

No green; red never sits against green. Bell A is drawn dashed whenever another bell is the focus,
solid when it is a contender (the second prediction) or the focus (maximum likelihood). A and B
are always italic math letters.

## Data

- 272 Old Faithful eruption lengths, R dataset `faithful` (Härdle 1991), `faithful.csv`.
- "Data, smoothed": maximum-likelihood mixture of two normals (EM), which keeps the sample
  mean and variance exactly. Why smoothing is needed (raw points score every bell infinite,
  bell first) and how it matters are shown in beat 12 with R's own default kernel smoothing
  (`density()`, bandwidth `bw.nrd0` = 0.335 min).
- Every number: `data.py` → `data.json`; every claim: `facts.md`.

## Beats

### 1. Cold open: the bet (0:00–0:14)
> Old Faithful's eruptions. Data first, the closest bell is this one. Swap the order. If
> closeness is a distance, order can't matter: it stays at one. Or does it move to two, or
> three? *[pause 1.5]*

First frame: axes and the 272 eruption bars (faint), which brighten as the smoothed curve
draws while `D(data ‖ bell)` writes top right (data blue in the first slot, bell purple in the
second), so the order the bet is about is on screen from the first second; "272 eruptions /
curve: smoothed" in the empty right side; data citation. On "Data first" the blue "data" slot
flashes yellow; on "this one" bell A draws. On "Swap the order" the two arguments arc past each
other onto a second line, `D(bell ‖ data)`. The wrong belief is the symmetry of a distance
("order can't matter"). On "one" a yellow **1** sits on A's crown; on "two" and "three" faint
dashed narrow bells appear on the short and the long hump, numbered **2** and **3**. Prediction
hold (a three-way spatial bet the title does not answer).

### 2. Stakes (0:14–0:27)
> The D is KL divergence, named for Kullback and Leibler. Every maximum-likelihood fit shrinks
> it with the data first, and much of Bayesian machine learning shrinks it with the order
> flipped. It's often called a distance.

The ghosts, numbers and data label leave; the D flags. "KL divergence" label; citation
*Kullback & Leibler, 1951 · Annals of Mathematical Statistics*; "maximum-likelihood fit" pinned
above bell A's crown by a dashed leader; flash along the bell; on "Bayesian" the flipped line
lights with a grey "variational inference" tag and the Blei citation; "a distance?" (yellow).

### 3. Naive build (0:27–0:40)
> So treat it as one. Data first, this bell is point seven six bits away. Shift it or stretch
> it, and that number only grows, so this is bell A: three and a half minutes, give or take one
> point one. *[0.8 s]*

"a distance?" loses its "?"; "KL divergence" dims; the "variational inference" tag and the Blei
citation leave with their topic. `= 0.76 bits` (red, live). The bell shifts
0.8 min left (the number climbs to 1.12 and flashes yellow during a 0.5 s hold) and back, then
widens ×1.8 (1.11, flash) and back. The dashed mean line completes the pin; the pinned label
becomes `A: 3.49 ± 1.14 min`.

### 4. Fail (0:40–0:55)
> But a distance reads the same both ways. Put the bell first, and the same two curves are one
> point seven bits apart, more than twice as far. *[0.75 s]* Only the order changed, so the
> order must be built into the formula.

The A label dims. `D(bell ‖ data) = 1.69 bits`, yellow `×2.2`. On "order changed" both whole
D-lines are boxed (unfilled boxes, 0.12 clear of every glyph).

### 5. Insight: one length (0:55–1:13)
> To see why, open it up at one real eruption, two minutes long. The data's curve gives that
> length a height, p. The bell gives it q, about a quarter as much. Double q twice and you reach
> p, so log base two of p over q is about two: two doublings, or two bits.

The numbers fade first, then the chart shrinks left and `D(data ‖ bell)` heads the right column.
The axis number 2 flags; scanner at 2.0 min. The blue bar `p` grows and is pulled out, same
baseline and scale, into the right side (p = 0.59); likewise the purple `q` (q = 0.15). In the
pull-out a copy of q stacks on itself (yellow ×2), then two copies (×2) until it meets the dashed
line at p's top. `log₂(p/q) = 1.98` is assembled: the p swings up from the pulled-out p bar
around the outside, the q drops in from its readout.

### 6. Every length, weighted (1:13–1:30)
> *[1.0 s]* Do that at every length. *[0.9 s]* Then weight each one by how often eruptions last
> that long, which is p, and add it all up. Where the bell rises above the data, the grey dips pay a little back.
> That's the divergence: point seven six bits.

Two panels: the chart's own x labels fade first, the chart rises (the scanner rides along back to
0.3 min, the p/q readouts dim to 30 %), and only then does the bill's panel draw underneath it
(shared x labels 1–6 and "eruption length (minutes)" under the bottom panel; "bits", later
"bits/min", inside the panel's top-left corner): nothing slides through the panel. Over "every
length" and the pause after it (≈ 1.9 s) the scanner sweeps drawing log₂(p/q); where it runs off the panel floor the line is
faint with grey true depths (↓ −45, ↓ −6.2, ↓ −20); `log₂(p/q)` flies into the formula row. The
curve is multiplied by p; the readout's p swings round the left of the readouts into the weight
(the flash runs along the humps); ∫ and dx write; the area fills left to right while
`D(data ‖ bell) = 0.76 bits` counts up (the D-line faint, so the running total has its subject).
On "grey dips" a grey "refund" tag sits under the largest dip. On "divergence" the D-line comes
to full strength; the block is centred on the bill.

### 7. A bell that skips a hump (1:30–1:46)
> Try a bell that ignores the short eruptions and sits on the long hump. At two minutes, it falls
> short by eighteen and a half doublings. More than a third of all eruptions are short ones like
> this, so the bill comes to five point eight bits. *[1.0 s]* (spoken at speed 0.80: the densest
> stretch)

The p/q/log₂ readouts, dimmed to 30 % while the scanner swept away from 2 min in beat 6, return
to full strength with the scanner at 2.00 min before the bell moves (so log₂(p/q) starts at 1.98).
A stays as a dashed ghost, labelled on its own left tail. The bell slides to B; the q readout
switches to scientific notation, `q = 1.6×10⁻⁶`, so `log₂(p/q) = 18.52` never looks like a division
by zero; the bill grows into a clipped red mountain with a live "peak ≈ 11" (arrow stops short of
the plateau's shoulder); total 5.77. Box over the short hump, "36%".

### 8. Keep that bill, swap for a second one (1:46–1:59)
> Now keep that bill, and swap the order for a second one. Every p trades places with q. The bell
> supplies the lengths, and the data judges them. Which bell wins now? *[pause 1.5]*

The readouts leave first; then the panels make room. The chart (the subject) grows to 2.85
units tall on top; the data-first bill moves under it; a bell-first bill panel waits hidden
until the question. Each bill panel carries its order in its top-right corner, "**data** first" /
"**bell** first", and its unit "bits / per min" top-left (two short lines, clear of the mountain); the shared x labels sit under the lowest panel.
The second formula block drops in already reading `= ?`; in one move the arguments arc past each
other (`D(bell ‖ data)`), the weight p becomes q and the fraction's p and q swap places
(`= ∫ q log₂(q/p) dx = ?`). No frame pairs the new order with the old integrand or number. During
the question A and B are both solid and equally bright. "supplies": both bells pulse (stroke +
fill); "judges": the data curve pulses. On "Which" the bell-first panel fades in at 30 %.
Prediction hold.

### 9. Bell first, scored (1:59–2:17)
> Take bell B first. It almost never imagines a short eruption, so ignoring them costs it nothing.
> It pays point six two. Bell A imagines eruptions in the gap and out in the tails, lengths the
> data almost never shows. That costs one point seven bits.

The "?" fades out before the number arrives. A returns to dashed, B fills; the bell-first panel
comes to full strength and its bill fills left to right, total counting to 0.62 (dashed box:
nothing over the short hump). The bell moves back to A: the bell-first bill grows over the gap and
both tails (boxes; grey refunds under the humps) to 1.69 while the data-first bill above falls
from 5.77 to 0.76 — both totals live.

### 10. Slide downhill: one bill drains, the other swells (2:17–2:34)
> Now start from A, and let the bell slide downhill on the bell-first bill. As that bill drains,
> the other one swells, and the bell settles on the long hump, less than half as wide. Flip the
> order, and the closest bell moves to three. *[pause 1.2]*

Both integrals have now been read, so each block collapses to its D-line and total, centred on
its own bill: the frame is the bell and its two bills. Gradient descent on D(bell ‖ data) from A
(precomputed path): the bell narrows and slides right; the bell-first bill drains 1.69 → 0.62
while the data-first bill swells into the mountain, 0.76 → 5.77, its live "peak ≈" counting up to
11. The two D-lines flag on "drains" / "swells". `B: 4.27 ± 0.44 min` pinned to B's crown by a
dashed leader. On "Flip" the cold-open picture returns (dashed ghosts 2 and 3, yellow 1 on A's
crown), an arrow runs 1 → 3, and B sits exactly in ghost 3: the bet, answered on the same image.

### 11. Payoff (2:34–3:00)
> Maximum likelihood puts the data first, so a one-bell fit stretches over every hump.
> Variational inference approximates a Bayesian posterior with the model first, so it tends to
> settle on one hump.

> Blei and colleagues note that variational inference generally underestimates posterior
> variance. In a real ad-conversion model, its average for one effect matched MCMC, but its
> spread was only a fifth as wide.

The bills, blocks and their labels fade first (the yellow **3** stays on B's crown and rides it
while the chart grows back to full size, until "settle on one hump"). Legend top right, left edge
at x = −1.0, clear of the y-axis title: row 1 `D(data ‖ bell)  maximum likelihood → A` (citation
*Bishop, 2006 · Pattern Recognition and Machine Learning, §10.1*) with a blue "data" tag; on
"stretches over every hump" A turns solid with a fill sweeping across both humps while B dims.
On "posterior" the bars and axis titles dim, the tag becomes "if this were a posterior", row 2
`D(bell ‖ posterior)  variational inference → B` lands and row 1 dims to 30 %. On "settle on one
hump" B returns solid with its fill sweep, A back to dashed. On "Blei" the 3 leaves and the Blei
citation replaces Bishop's; on "underestimates" ±1 SD brackets: "±1.14" on the curve (blue) and
"±0.44" on B (purple), and A steps out. On "real" the legend and the toy brackets leave and a measured case comes in
top right, above B's crown: "real ad-conversion model"; on "average" MCMC (blue) and VI (purple)
brackets on one shared mean line, on "matched" their values `0.110 ± 0.020` and `0.110 ± 0.004`
(the mean line flags); on "a fifth" five copies of the VI spread tile the
MCMC spread. Citation *Giordano, Broderick & Jordan, 2018 · JMLR, Tables 2–3*.

### 12. Honest limit (3:00–3:13)
> Against raw points, every bell-first score is infinite, so the data must be smoothed. Smooth it
> more heavily, the gap partly fills, and the best bell-first fit spreads wide, almost back to A.

The panel, brackets and tag leave. On "raw points" the curve and bars dim and the 272 eruptions
appear as blue ticks on the length axis ("272 raw points"); on "infinite" `D(bell ‖ data) = ∞`
writes in its cold-open place. On "smoothed" the ticks leave and the curve returns. On "Smooth it
more heavily" the curve morphs into R's default kernel smoothing (tag "R's default smoothing",
citation *Silverman, 1986 · Density Estimation (R's default bandwidth)*); a box marks the gap. On
"best" the bell moves from B to the best bell-first fit under that smoothing, pinned "best
bell-first fit: 3.55 ± 0.99 min"; on "back to A" dashed A returns beside it (3.49 ± 1.14). One
morph out, one back (beat 13); no fourth curve.

### 13. Landing (3:13–3:22)
> *[pause 1.2]* Bell A never misses an eruption that happens. Bell B almost never imagines one
> that doesn't.

During the pause the smoothing returns to the original curve, the fit returns to B and the tags
leave. On "Bell A" `D(data ‖ bell) → A` writes in its cold-open place, the yellow **1** returns
to A's crown, A turns solid and its fill sweeps across both humps (underline under "data"). On
"Bell B" `D(bell ‖ data) → B` writes below it, the yellow **3** returns to B's crown, A goes back
to dashed and B's fill sweeps over its one hump (underline under "bell"). The last two lines are
spoken as a pair. End card.

## Sources

- Kullback, S. & Leibler, R. A. (1951). On Information and Sufficiency. *Annals of Mathematical
  Statistics* 22(1): 79–86.
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer. §1.6.1 (eq. 1.119,
  KL and maximum likelihood), §10.1.2 and Fig. 10.3 (mode covering vs mode seeking).
- Blei, D. M., Kucukelbir, A. & McAuliffe, J. D. (2017). Variational Inference: A Review for
  Statisticians. *J. American Statistical Association* 112(518): 859–877.
- Härdle, W. (1991). *Smoothing Techniques with Implementation in S*. Springer (R `faithful`).
- Giordano, R., Broderick, T. & Jordan, M. I. (2018). Covariances, Robustness, and Variational
  Bayes. *Journal of Machine Learning Research* 19(51): 1–49. §5.3, Tables 2–3 (Criteo GLMM).
- Silverman, B. W. (1986). *Density Estimation for Statistics and Data Analysis*. Chapman & Hall
  (eq. 3.31, the rule of thumb behind R's default `bw.nrd0` = 0.9·min(sd, IQR/1.34)·n^(−1/5)).
