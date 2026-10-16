# Episode 8 — The Distance That Isn't Symmetric

**Idea (one sentence):** KL divergence only charges where its *first* distribution puts
its mass, so swapping the order changes the answer: with the data first, a one-bell model
must cover every hump; with the model first, it may ignore a hump but must never wander
where the data isn't.

**The episode's own picture:** one bell over the data, and under it *two bills* for that same
bell, the data-first bill and the bell-first bill, kept side by side. As the bell slides from A
to B, one bill drains while the other swells into a mountain: each order has its own closest
bell.

Runtime 3:27 · 544 words · 164 wpm over speech time (157 overall) · voice af_heart, speed 0.84.
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
  mean and variance exactly. Sensitivity to the smoothing is shown in beat 12 with R's own
  default kernel smoothing (`density()`, bandwidth `bw.nrd0` = 0.335 min) and with the
  bandwidth chosen by leave-one-out likelihood cross-validation (0.103 min).
- Every number: `data.py` → `data.json`; every claim: `facts.md`.

## Beats

### 1. Cold open: the bet (0:00–0:14)
> Old Faithful's eruptions. With the data first, the closest bell curve is this one. Put the
> bell first, and if closeness works both ways, it stays at one. Or does it move to two, or
> three? *[pause 1.5]*

First frame: axes and the 272 eruption bars (faint), which brighten as the smoothed curve
draws; "272 eruptions / curve: smoothed" in the empty right side; data citation. On "data first"
`D(data ‖ bell)` writes top right (data blue in the first slot, bell purple in the second); on
"this one" bell A draws. On "bell first" the two arguments arc past each other onto a second
line, `D(bell ‖ data)`, so the notation is read as nothing more than an order. On "one" a yellow
**1** sits on A's crown; on "two" and "three" faint dashed narrow bells appear on the short and
the long hump, numbered **2** and **3**. Prediction hold (a three-way spatial bet the title does
not answer).

### 2. Stakes (0:14–0:27)
> The D stands for KL divergence, named for Kullback and Leibler. Every maximum-likelihood fit
> is the closest model by it, and it's often called a distance between distributions.

The ghosts, numbers and data label leave; the D flags. "KL divergence" label; citation
*Kullback & Leibler, 1951 · Annals of Mathematical Statistics*; "maximum-likelihood fit" pinned
above bell A's crown by a dashed leader; flash along the bell; "a distance?" (yellow).

### 3. Naive build (0:27–0:40)
> So treat it as one. Data first, this bell is point seven six bits away. Shift it or stretch
> it, and that number only grows, so this is bell A: three and a half minutes, give or take one
> point one.

"a distance?" loses its "?"; "KL divergence" dims. `= 0.76 bits` (red, live). The bell shifts
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
> Do that at every length. Then weight each one by how often eruptions last that long, which is
> p, and add it all up. Where the bell rises above the data, the grey dips pay a little back.
> That's the divergence: point seven six bits.

Two panels: chart on top, the bill underneath (shared x labels 1–6 and "eruption length
(minutes)" under the bottom panel; "bits", later "bits/min", inside the panel's top-left
corner). The scanner sweeps drawing log₂(p/q); where it runs off the panel floor the line is
faint with grey true depths (↓ −45, ↓ −6.2, ↓ −20); `log₂(p/q)` flies into the formula row. The
curve is multiplied by p; the readout's p swings round the left of the readouts into the weight
(the flash runs along the humps); ∫ and dx write; the area fills left to right while
`= 0.76 bits` counts up. On "grey dips" a grey "refund" tag sits under the largest dip. On
"divergence" `D(data ‖ bell)` lands on top of the formula block, which is centred on the bill.

### 7. A bell that skips a hump (1:30–1:46)
> Try a bell that ignores the short eruptions and sits on the long hump. At two minutes, it falls
> short by eighteen and a half doublings. More than a third of all eruptions are short ones like
> this, so the bill comes to five point eight bits.

A stays as a dashed ghost, labelled on its own left tail. The bell slides to B; the q readout
switches to scientific notation, `q = 1.6×10⁻⁶`, so `log₂(p/q) = 18.52` never looks like a division
by zero; the bill grows into a clipped red mountain with a live "peak ≈ 11"; total 5.77. Box over
the short hump, "36%".

### 8. Keep that bill, swap for a second one (1:46–1:59)
> Now keep that bill, and swap the order for a second one. Every p trades places with q. The bell
> supplies the lengths, and the data judges them. Which bell wins now? *[pause 1.5]*

The readouts leave first; then the panels make room: chart and the data-first bill move up, a
second (bell-first) bill panel appears underneath at 30 %, the shared x labels move to the new
bottom. A copy of the formula block drops in beside the new panel, and in it the arguments arc
past each other (`D(bell ‖ data)`), the weight p becomes q and the fraction's p and q swap places
(`= ∫ q log₂(q/p) dx = ?`). During the question A and B are both solid, unfilled, equally
bright, both labels lit (no hint of the answer); the data-first bill still shows B's 5.77.
"supplies": both bells flash; "judges": the data curve flashes. Prediction hold.

### 9. Bell first, scored (1:59–2:17)
> Take bell B first. It almost never imagines a short eruption, so ignoring them costs it nothing.
> It pays point six two. Bell A imagines eruptions in the gap and out in the tails, lengths the
> data almost never shows. That costs one point seven bits.

A returns to dashed, B fills; the bell-first panel comes to full strength and its bill fills left
to right, total counting to 0.62 (dashed box: nothing over the short hump). The bell moves back to
A: the bell-first bill grows over the gap and both tails (boxes; grey refunds under the humps)
to 1.69 while the data-first bill above falls from 5.77 to 0.76 — both totals live.

### 10. Slide downhill: one bill drains, the other swells (2:17–2:33)
> Now start from A, and let the bell slide downhill on the bell-first bill. As that bill drains,
> the other one swells, and the bell settles on the long hump, less than half as wide. Flip the
> order, and the closest bell moves to three.

Gradient descent on D(bell ‖ data) from A (precomputed path): the bell narrows and slides right;
the bell-first bill drains 1.69 → 0.62 while the data-first bill swells into the mountain,
0.76 → 5.77, its live "peak ≈" counting up to 11. The two D-lines flag on "drains" / "swells".
`B: 4.27 ± 0.44 min` pinned to B's crown by a dashed leader (B's letter label yields to it). On
"Flip" a yellow **1** at A's crown and an arrow to a yellow **3** at B's crown: the cold-open bet,
answered on the same image.

### 11. Payoff (2:33–2:58)
> Maximum likelihood puts the data first, so its fits stretch over every hump. Variational
> inference approximates a Bayesian posterior with the model first, so it settles on one hump.

> Blei and colleagues note that variational inference generally underestimates posterior
> variance. Here, bell B keeps only fifteen percent of the posterior's variance.

The bills' labels and fills leave first, then the chart returns to full size. Legend row 1
`D(data ‖ model)  maximum likelihood → A` (citation *Bishop, 2006 · Pattern Recognition and
Machine Learning, §10.1*), a blue "data" tag right of the long hump; on "stretch over every
hump" A turns solid with a fill sweeping across both humps while B dims to 30 %. On "Bayesian
posterior" the bars dim to 25 %, the x-axis title to 30 %, "data" fades and "posterior" writes
with a grey "same curve, as a stand-in" note; row 2 `D(model ‖ posterior)  variational inference
→ B`. On "settles on one hump" B returns solid with its fill sweeping across the long hump, A
back to dashed. Citation *Blei et al., 2017 · J. American Statistical Association*. On
"underestimates" a blue ±1 SD bracket on the posterior curve (2.35–4.63 min, low, labelled 1.14)
and a purple one on B above the blue crown (3.83–4.71 min, labelled 0.44); on "Here" the labels
fly into `(0.44 / 1.14)² = 15%` (0.44 purple, 1.14 blue).

### 12. Honest limit (2:58–3:16)
> Settling on one hump needs that gap to be nearly empty. Smooth the data with R's default
> setting, and the gap fills enough that the best bell-first fit comes out wide. Smoothing
> chosen by cross-validation keeps the gap nearly empty, and the fit on one hump.

Legend, brackets, ratio and citation are removed (not dimmed); the tag returns to "data". Box over
the gap. The smoothed curve morphs into R's default kernel smoothing (tag "R's default
smoothing"; footnote in the citation slot, set in math: "With raw points, D(bell ‖ data) = ∞ for
every bell"). B stays as a faint 25 % reference; the fit starts from A (where a slide from A
really ends under this smoothing) and descends to the wide fit, pinned "best bell-first fit:
3.55 ± 0.99 min" with a dashed leader — never called B. On "cross-validation" the curve morphs
into the cross-validated kernel smoothing (tag "cross-validated smoothing") and the fit slides
back onto the long hump: "best bell-first fit: 4.28 ± 0.39 min".

### 13. Landing (3:16–3:28)
> So closeness depends on which curve goes first. Bell A never misses an eruption that happens.
> Bell B almost never imagines one that doesn't.

The fit label and tags leave; the smoothing returns to the original curve and the fit settles
into B. The two cold-open lines return in their cold-open place with answers: `D(data ‖ bell) → A`,
`D(bell ‖ data) → B`; a yellow underline under each first argument only. The bars brighten under A;
B fills, sitting inside the long hump. The last two lines are spoken as a pair. End card.

## Sources

- Kullback, S. & Leibler, R. A. (1951). On Information and Sufficiency. *Annals of Mathematical
  Statistics* 22(1): 79–86.
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer. §1.6.1 (eq. 1.119,
  KL and maximum likelihood), §10.1.2 and Fig. 10.3 (mode covering vs mode seeking).
- Blei, D. M., Kucukelbir, A. & McAuliffe, J. D. (2017). Variational Inference: A Review for
  Statisticians. *J. American Statistical Association* 112(518): 859–877.
- Härdle, W. (1991). *Smoothing Techniques with Implementation in S*. Springer (R `faithful`).
- R Core Team, `stats::bw.nrd0` / `density()` documentation (Silverman's rule of thumb,
  0.9·min(sd, IQR/1.34)·n^(−1/5)); leave-one-out likelihood cross-validation of a Gaussian
  kernel bandwidth (e.g. Silverman 1986, *Density Estimation*, §3.4.4), computed in `data.py`.
