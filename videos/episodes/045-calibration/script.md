# 045 — When 90% Confident Isn't 90% Right

**One idea:** a model's confidence is honest only if, among the cases where it says p, it is right a fraction p of the time; dividing the logits by one number (a temperature) can fix that without changing a single prediction.

## Palette (one meaning each, whole episode)
| Colour | Meaning |
|---|---|
| BLUE | the modern / big network: its accuracy, its probabilities, its "right" cases |
| PURPLE | the old / small network |
| RED | wrong cases and the confidence gap (calibration error) |
| YELLOW | the temperature T and whatever is being pointed at |
| INK (dashed) | the honest diagonal: "says = is right" |
| GRAY / DIM | axes, citations, de-emphasised context |

## Beats (narration exactly as spoken)

**1 · Cold open (0:00)** — two cards, real numbers, citation.
> Two networks take the same test: small photos in a hundred categories. A design from nineteen ninety-eight gets fifty-five percent right. A design from twenty sixteen gets sixty-nine percent.

**2 · Prediction (≈0:11)** — a confidence slot "says: ?" under each card.
> Each one also tells you how sure it is. Whose confidence would you trust? [pause 1.5]

**3 · Stakes** — one confidence track 0 → 1 with a hand-over threshold; the question becomes an equation.
> That number decides when a car stops trusting its camera, or when a diagnosis goes to a human doctor. So the precise question is this. When a network says ninety percent, is it right ninety percent of the time?

**4 · Naive build** — simulated stand-in, one prediction's ten bars.
> To check, we simulated a stand-in network: ten classes, ten thousand test cases. For one case it outputs these ten probabilities. The tallest bar, point eight four, is its confidence.

**5** — 10×10 tiles.
> One answer can't show whether that is honest. So gather every case where it said between eighty and ninety percent, about thirteen hundred of them. Out of every hundred, sixty-three are right.

**6** — tiles collapse into a column in a reliability diagram.
> Stack that sixty-three percent as a column above its confidence. An honest network would reach this diagonal. Now do every confidence range.

**7 · Fail, measured**
> Every column falls short. Weight each red gap by how many cases it holds, average them, and you get the calibration error: point one five. On average, it claims fifteen points more than it delivers.

**8 · Naive fix, fails differently** — purple columns.
> The obvious fix is a smaller network. Its columns sit on the diagonal, with an error of point oh one. But its accuracy drops from sixty-nine percent to fifty-four. That is the nineteen ninety-eight trade.

**9 · Insight** — back to the one prediction; the softmax is built from its bars.
> Go back to the big network's one answer. Its tallest bar is the right class; it is just too tall. These probabilities come from raw scores called logits. Raise e to each score, then divide by the total.

**10** — T enters the formula. Prediction pause.
> Now divide every score by one number, T, the temperature. Turn T up. What happens to the accuracy? [pause 1.5]

**11** — T knob turns; bars flatten; accuracy counter stays.
> Nothing. Dividing by T pulls every score toward zero, so the bars flatten, but the tallest bar stays tallest. Every prediction is unchanged. Only the confidence drops.

**12** — reliability columns rise onto the diagonal as T goes 1 → 2.
> On the diagram, the columns climb onto the diagonal. Fit T on held-out cases, and a temperature of about two takes the error from point one five to point oh one.

**13 · Payoff (real)** — Guo et al. 2017 numbers.
> Guo, Pleiss, Sun and Weinberger reported this at ICML in twenty seventeen. Their hundred-and-ten-layer network, the twenty sixteen design, had a calibration error of sixteen and a half percent. One temperature cut it to one point three, with accuracy untouched.

**14 · Honest limit** — simulated shift, columns sag again; Ovadia et al. 2019.
> The temperature is fit on data like the training data. When the inputs shift, Ovadia and colleagues found that this calibration does not hold.

**15 · Landing** — back to the two cards.
> So, the two networks. The old one's confidence was honest; the new one's was inflated. Divide the new one's scores by a single number, and it keeps its sixty-nine percent, and its ninety percent means ninety.

## Sources
- Guo, Pleiss, Sun & Weinberger (2017). On Calibration of Modern Neural Networks. ICML, PMLR 70. Fig. 1, Table 1, §4.2.
- Ovadia et al. (2019). Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift. NeurIPS.
- Simulation: `sim.py` (seed 45); see facts.md.
