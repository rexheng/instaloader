# Episode 44 — 99.8% Accurate and Completely Useless

**One idea:** when positives are rare, a tiny false-alarm *rate* on the huge negative class
outnumbers the true positives, so accuracy and ROC look excellent while precision collapses;
the class ratio N/P is exactly the term ROC never sees.

## Palette (colour -> one meaning, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | honest (legitimate) transactions, everywhere: squares, score curve, bar segment, equation terms |
| RED | fraud transactions, everywhere |
| YELLOW | the threshold line / current operating point / the class ratio 578 being pointed at |
| PURPLE | the ROC curve and anything ROC "sees" |
| GREEN | precision: the precision readout and the precision-recall curve |
| INK / GRAY / DIM | text / axes and sources / context |

## Beats (narration as spoken)

**B0 · Cold open (0:00–0:12)** — waffle of 579 squares (578 blue, 1 red) on screen from frame 1; "accuracy = 99.8%"; "frauds caught = ?".
> This model is ninety-nine point eight percent accurate on real credit card data. Of the four hundred ninety-two frauds in it, how many did it catch? [pause 1.5]

**B1 · Naive model (0:12–0:27)** — "?" becomes 0; a box labels the whole grid "predicted: honest"; the fraction 578/579 is pulled out of the squares. Citation: Dal Pozzolo et al., 2015 · IEEE SSCI.
> None. It calls every transaction honest. Each square here is about four hundred ninety-two transactions, and the model is wrong only on this red one. Five hundred seventy-eight right for every one wrong is ninety-nine point eight percent.

**B2 · Naive build (0:27–0:45)** — the squares melt into two score curves (simulated), drawn to equal height; yellow threshold line.
> A useful model has to hand investigators a short list of alerts. So it gives every transaction a fraud score. Here are the scores, simulated, with each group drawn to the same height. It flags everything to the right of this line.

**B3 · ROC (0:45–1:00)** — threshold sweeps; purple ROC curve traces; live readouts "caught", "flagged"; AUC = 0.995.
> Slide the line, and track two rates: the share of fraud caught, and the share of honest purchases flagged. Together they trace the ROC curve. It hugs the top-left corner, with an area of point nine nine five.

**B4 · Prediction (1:00–1:13)** — line parks at caught 90%, flagged 1%.
> Park the line here. It catches ninety percent of fraud and flags only one percent of honest purchases. When this model raises an alert, what is the chance it is really fraud? [pause 2]

**B5 · Fail (1:13–1:21)** — precision = 13% (green) appears; both peaks flagged as equal height.
> Thirteen percent. That is the model's precision, and the picture hid the reason. I drew both groups at the same height.

**B6 · Insight, true scale (1:21–1:40)** — red hill flattens by 578×; shaded tails pulled out into a stacked "alerts" bar: 2,843 blue over 443 red.
> At true scale, the honest group is five hundred seventy-eight times bigger, so the fraud hill flattens into this sliver. Past the line, one percent of the honest mountain is two thousand eight hundred forty-three false alarms. Ninety percent of the sliver is only four hundred forty-three frauds.

**B7 · Formula from the bar (1:40–1:58)** — precision = 443/(443+2843) → rates × counts → 1/(1 + (0.01/0.90)·578), brace "6.4 false alarms per fraud".
> Precision is this red part over the whole bar. Write each part as a rate times a count. Divide through, and the ratio of the counts, five hundred seventy-eight, multiplies the false-alarm rate, giving more than six false alarms for every fraud.

**B8 · General form (1:58–2:08)** — numbers become words: flagged/caught boxed purple ("ROC sees"), honest/fraud boxed yellow.
> The ROC curve plots only the two rates, flagged and caught. The ratio of the counts never enters it, which is why it looked so good.

**B9 · Fix: precision-recall (2:08–2:22)** — ROC and PR axes side by side, the line sweeps again, green PR curve sags; the random baseline drops from 0.5 to 0.17%.
> So plot precision against fraud caught instead. Slide the line again. Where the ROC curve hugged its corner, this one sags, and a random model would sit at point one seven percent, not fifty.

**B10 · Trade-off (2:22–2:36)** — operating point moves to caught 70%, precision 55%.
> Every point is a trade. Raise the line, and you catch seventy percent of fraud, but now more than half the alerts are real. The right point depends on what a missed fraud costs, against an investigator's hour.

**B11 · Payoff (2:36–2:54)** — bars 22/33 (purple) and 4/33 (green); citation Saito & Rehmsmeier, 2015 · PLoS ONE.
> Saito and Rehmsmeier made this case in Plos One in twenty fifteen. Of thirty-three genome-wide studies with imbalanced data that they reviewed, twenty-two judged their models by ROC, and only four by precision-recall. ROC is not wrong. It measures ranking, and ranking ignores how rare the positives are.

**B12 · Landing (2:54–3:05)** — the waffle returns; "accuracy" relabels to "share honest".
> Back to the red square. Ninety-nine point eight percent never described the model. It described how rare fraud is.

## Sources
- Dal Pozzolo, Caelen, Johnson & Bontempi (2015), "Calibrating Probability with Undersampling for Unbalanced Classification", IEEE SSCI, pp. 159–166 — the ULB/Worldline credit-card dataset (284,807 transactions, 492 frauds, two days, Sept 2013).
- Saito & Rehmsmeier (2015), "The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets", PLoS ONE 10(3): e0118432.
- Scores are simulated (binormal, honest N(0,1), fraud N(3.61,1)); see facts.md.
