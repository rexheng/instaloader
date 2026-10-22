# Episode 9: Why Bell Curves Are Everywhere, and When They're Not

**Idea (one sentence):** Collecting more data never makes lopsided data bell-shaped; averaging
does, because every way an average differs from the bell fades (its skewness is the piece's
over root n, its extra tail weight over n), which for an A-B test on bus waits means 1,420 per
average before the bell's 2.5% tails can be trusted, not the textbook's 30, and for data where
one piece can outweigh the rest (infinite variance) no number is enough.

Runtime about 3:34 (round 5) · 490 words · voice af_heart, speed 0.83 (landing 0.80),
`CADENCE = "shaped"`. Narration text lives in `narration_text.py` (the scene imports it, so script
and audio cannot drift); explicit pauses only at the prediction (1.6 s) and after the key results,
beat turns about 0.7 s against 0.48 s full stops (`GAP_AFTER`).

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | single pieces: raw waits, single lighthouse flashes, their skewness and excess kurtosis, skew(x), the cubed-gap cubes |
| YELLOW | averages: the average dot, histograms of averages, skew(x-bar) and the excess kurtosis of averages, one test's 95% interval around its average ("own spread"), the miss meter, the running average of flashes |
| GREEN | the perfect bell (normal curve with the same centre and width), its 2.5% tails (cold open and payoff; the meter's 2.5% line, the interval the bell's true spread would give, "true spread", the ring on the answer), "bell = 0" on the skewness axis |
| RED | an extreme piece that drags the average (the 25.7-minute wait, the 902-mile flash, infinite variance, "never" on the sample-size axis) |
| GRAY / INK | axes, tick labels, sample sizes (guess chips, INK log-axis markers with gray names), the spread and spread cubed (gray bar, gray cubes), the true mean mu, the textbook rule and Kohavi's 2-3% band, citations |

(Round 5: PURPLE is gone with the median.)

## Glossary (one name per quantity)

- **wait**: one simulated bus wait (minutes). **average** (x-bar): the mean of n waits.
- **skewness** = "the lean": E[(x - mu)^3] / sigma^3; skew(x) for one wait, skew(x-bar) for an average.
- **spread** = sigma (true) or the sample SD a test computes ("own spread").
- **ex. kurt** = excess kurtosis = "the extra tail weight".
- **misses** = the share of 95% intervals wholly below ("low") or above ("high") the true mean.

## Beats

### 1. Cold open (0:00-0:15)
> A hundred waits for a bus: mostly short, with a long tail. Textbooks say the average of thirty
> is safe to treat as a bell. For these waits, does it take thirty, three hundred, or over a
> thousand? *[pause 1.6]*

Blue histogram of 100 simulated waits (a brightness sweep, never a height change). On "tail" a
gray "tail" brace spans 20-45 min and the 0-20 min bars dim; the brace steps back to 40% and
stays until the first chip. "Montgomery & Runger, 2010" on "Textbooks". On "average" a gray arrow
"average of 30" grows; a dashed green bell is drawn until "these", when the waits flash and a "?"
lands on the bell; three gray chips 30 / 300 / 1,000+ arrive on their words (prediction hold).

### 2. Stakes and the criterion (0:15-0:22)
> A-B tests lean on that bell's tails, and on revenue data, thirty is off by a factor of thousands.

The dashed bell flags on "bell's"; on "tails" its two tails beyond 1.96 SD shade green, "2.5%"
each. "Kohavi et al., 2014 · KDD" on "revenue"; the 30 chip pulses on "thirty".

### 3. Naive build (0:22-0:29)
> Maybe thirty means collecting enough waits. Collect a hundred thousand: smoother bars, same shape.

On "hundred" the 100 waits become 100,000 (the counter swaps in place); the bars glow on
"smoother"; the exact exponential curve is drawn on "same shape".

### 4. Fail, measured (0:29-0:43)
> Measure the lean with skewness: the average cubed gap from the mean, left gaps counting
> negative, over the spread cubed. A perfect bell scores zero. These waits score about two, at
> every size.

Definition built term by term from a mean line and x - mu arrows; on "These waits" the histogram
flashes; skew bars 1.90 / 1.96 / 2.00 / 1.98 at 10^2..10^5 waits against the green "bell 0" line;
brace "gap ~ 2".

### 5. Fix: average (0:44-0:55)
> So average instead. *[pause 0.5]* Four bus waits: one long wait, diluted by three short ones.
> *[pause 0.8]* Drop the average here. Do that ten thousand times.

The skewness chart fades first; one wait's 1.98 drops straight out of it and slides along the
readings row to sit under panel 1 once the shrinking histogram has risen above that row ("skew ="
fades in on arrival). Panels n = 1, 4, 16, 64 with "share (%)" ticks. Four chips (25.7 in red)
come out of their bars and become (5.2 + 1.8 + 25.7 + 5.3) / 4 = 9.5, which drops into panel 2 on
"here"; 10,000 averages grow.

### 6. Readings (0:55-1:04)
> These averages lean less: skewness one. Sixteen: point five. Sixty-four: point two five, nearly
> this perfect bell.

On "These averages" the n = 4 bars flash; each panel's bars grow while its size is said and its
reading lands on the value; the green bells are drawn on "this" (the n = 4 bell whole, its part
below 0 minutes dimmed).

### 7. Insight: the formula from the readings (1:05-1:13)
> Each time n grows four times, the skewness halves: two over root n, and two is the skewness of
> one wait.

"x4" arrows between the headers, "/2" arrows between the readings; 2/sqrt(n) is written under
each reading while that panel's n pulses, held about 1.6 s; on "skewness of" the four collapse
into one and "skew(x-bar) =" arrives; on "one wait" the 1.98 reading pulses and the 2 becomes
skew(x).

### 8. Why root n, drawn as cubes (1:13-1:29)
> The root comes from the cubes: add four bus waits, and the cubed gaps add up, four times one
> wait's. But the spread only doubles, so its cube grows eight times. Four over eight: half the
> lean. In general, n, over n to the one and a half.

The formula opens in place (dashed slot); one blue cube grows out of E[(x-mu)^3] and one gray
cube out of sigma^3 ("cubed gaps", "spread^3"); four blue cubes ("x4"); sigma -> 2 sigma ("x2");
2 x 2 x 2 gray cube ("x8"); x n and x n^{3/2} fly into the slot. Then the cubes and the middle of
the expansion leave first, and the two ends close up into skew(x-bar) = skew(x)/sqrt(n).

### 9. Why it is a bell (1:30-1:44)
> Kurtosis, the extra tail weight, quarters each time. Every finer difference fades faster
> still, until only the bell survives. That's the central limit theorem: independent pieces,
> plus one condition.

The skew row dims to 40%. "ex. kurt = 6" (blue, under 1.98); one wait's tail bars glow on
"tail"; on "quarters" 1.5 / 0.375 / 0.094 (exact 6/n) arrive one by one, each with its "÷4"
arrow. On "Every finer difference" the green bells pulse in turn; on "only the bell" the n = 64
bars glow. "central limit theorem" with "independent pieces" + "+ one condition" under it.

### 10. Payoff: the textbook's thirty (1:45-1:51)
> Back to the textbook's thirty. *[pause 0.3]* Two over root thirty is point three seven: close to
> a bell, by eye.

Everything but the n = 16 panel leaves; it grows into the exact n = 30 panel ("n = 30", "exact",
"average (minutes)"); the formula moves to the top right; its copy becomes 2/sqrt(30) = 0.37; the
log axis "sample size" with a gray "textbook 30" marker fades in.

### 11. Where tests live (1:52-2:12)
> But tests live in the tails: a ninety-five percent interval should miss two and a half percent
> each side. *[pause 0.4]* A test estimates the spread from its own data. With lopsided waits, a low
> average comes with a small spread, so its interval stops short. *[pause 0.8]* At thirty: seven
> percent low, one percent high. *[pause 0.5]*

On "tails" the middle bars dim and the bell's tails shade green; the formulas and the axis step
back to 35%. The miss meter ("misses (simulated)", "low" / "high", green dashed "2.5%"). A gray
dashed mu line rising past both intervals; the long tail bars glow on "lopsided"; one simulated
test (average 6.83, sample SD 6.47): the interval its true spread would give (green, dashed,
3.25-10.41, "true spread") covers mu; on "small" its own interval (yellow, 4.51-9.14, "own
spread") is drawn just above and stops short of mu. Both ride just above the histogram, their
labels (Text 26) left-aligned at the panel's edge. On "seven" the yellow interval flows into the
low bar (7.2%); the high bar rises to 1.0%.

### 12. Kohavi's rule is our formula (2:12-2:39)
> Ron Kohavi and colleagues want each side within two to three percent. Their rule: n at least
> three hundred fifty-five times the skewness, squared. *[pause 0.3]* Divide by n and take the
> root: *[pause 1.0]* it's our formula, the average's skewness at most point oh five three. At
> three hundred, the lean is point one two: still too much. For these waits, fourteen twenty, and
> both misses reach the band. *[pause 1.2]*

Citation: "Kohavi et al., 2014 · KDD; rule from Boos & Hughes-Oliver, 2000". On "each side" the
tails and both readings flash; "2.5%" becomes a gray "2-3%" beside a gray band. On "Their rule"
the panel dims to 35% and 2/sqrt(30) leaves; then skew(x-bar) = 0.37 moves to sit right above the
meter while the meter's title steps back for the 0.8 s it is crossed. The rule is written; a copy
becomes skew(x)^2/n <= 1/355, then skew(x)/sqrt(n) <= 1/sqrt(355) ~ 0.053. On "our formula" the
top formula lights up and comes down into the line: skew(x-bar) = skew(x)/sqrt(n) <= 0.053 (never
more than two equations). On "At three hundred" a gray 300 marker lands, the panel morphs to
n = 300, the readout rolls to 0.12 and the meter to 3.7% / 1.7%. On "these waits" the rule becomes
n >= 355 · 2^2 = 1,420; on "fourteen" the 1,420 marker, the panel, the readout 0.053 and the meter
3.0% / 2.1%. On "band" a green ring flashes around the bars and the band. Every changed number
rolls (old out upward, then new in), so no frame shows two numbers printed over each other.

### 13. Bing, and the third answer (2:40-2:51)
> Bing's revenue per user had a skewness near eighteen: a hundred fourteen thousand users. And for
> some data, no number on this axis is enough.

On "Bing's" the panel, meter, readout and inequality leave first; then the sample-size axis rises
to mid-frame and the rule to the top: n >= 355 · 17.9^2 ~ 114,000 (marker "Bing revenue"). On "no
number" a bright sweep runs along the whole axis and off its end into a red dashed extension and
a red "never" marker, which flags on "enough".

### 14. The condition: the lighthouse (2:52-3:21)
> A lighthouse a mile off a straight shore flashes at random angles, landing somewhere on the
> shore. Track the average landing spot: it never settles. One flash, aimed almost along the
> shore, lands nine hundred miles away. Repeat the thousand-flash average two hundred times: still
> as spread out as one flash. The theorem needs finite variance: no single piece can outweigh the
> rest. Here, it's infinite.

Everything but the sample-size axis line fades; the line becomes the shore while the lamp
appears ("1 mi" drop line). Flashes land as blue dots; the running-average trace lurches through
840 flashes; flash 841's beam turns red and leaves the picture ("902 mi ->"), and a red dot marks
the jump on the trace. Then 200 averages of 1,000 flashes fall onto a second line ("12 more" off
each end); on "spread" their middle half is bracketed from its quartile dots ("average of 1,000"),
on "one flash" the single flashes' middle half ("one flash", "middle half"): the same width. On
"finite variance" the chart steps back and "variance < infinity" is written; the red jump dot
flags on "single piece"; on "Here" it turns into a red "variance = infinity".

### 15. Landing (3:22-3:34)
> So the answer is over a thousand, not thirty. The bell was never in the data. *[pause 0.3]* It's
> in the average.

The lighthouse fades first, then the shore slides into the waits axis as the whole cold-open
frame returns (dashed bell, its 2.5% tails, chips). The 1,000+ chip lights on "thousand"; the
arrow label becomes "average of 1,420" on "not thirty"; on "never" the "?" and the chips leave and
the guessed bell dims; on "data" the lopsided histogram flashes; on "It's in the average" 10,000
simulated averages of 1,420 waits grow under a solid green bell (ticks 9.5 and 10.5).

## Sources
- Kohavi, R., Deng, A., Longbotham, R., Xu, Y. (2014). Seven Rules of Thumb for Web Site
  Experimenters. KDD '14, 1857-1866. doi:10.1145/2623330.2623341 (Rule #7; table corrected
  Jan 2015).
- Montgomery, D. C. & Runger, G. C. (2010). Applied Statistics and Probability for Engineers,
  5th ed. (n >= 30 rule, as quoted by Kohavi et al.).
- Deng, A. (2021, book draft). Causal Inference and Its Applications in Online Industry, ch. 8.5
  (355 s^2 is the unknown-variance threshold; known variance gives about 123 s^2).
- Boos, D. D. & Hughes-Oliver, J. M. (2000). How Large Does n Have to Be for Z and t
  Intervals? The American Statistician 54(2):121-128 (origin of the 355 s^2 rule).
- Gull, S. F. (1988). Bayesian inductive inference and maximum entropy; Sivia, D. S. &
  Skilling, J. (2006). Data Analysis: A Bayesian Tutorial, 2nd ed., OUP (lighthouse problem).
