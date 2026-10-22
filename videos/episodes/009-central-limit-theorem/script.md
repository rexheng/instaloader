# Episode 9: Why Bell Curves Are Everywhere, and When They're Not

**Idea (one sentence):** Collecting more data never makes lopsided data bell-shaped; averaging
does, because every way an average differs from the bell fades (its skewness is the piece's
over root n, its extra tail weight over n), which for an A-B test on bus waits means 1,420 per
average before the bell's 2.5% tails can be trusted, not the textbook's 30, and for data where
one piece can outweigh the rest (infinite variance) no number is enough.

Runtime about 3:55 (round 5) · about 590 words · voice af_heart, speed 0.86. Narration text lives in
`narration_text.py` (the scene imports it, so script and audio cannot drift). Round 3 cadence:
sentences inside a beat are 0.27 s apart, story-beat boundaries about 0.9 s (`GAP_AFTER`).

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | single pieces: raw waits, single lighthouse flashes, their skewness and excess kurtosis, skew(x), the cubed-gap cubes |
| YELLOW | averages: the average dot, histograms of averages, skew(x-bar) and the excess kurtosis of averages, one test's 95% interval around its average ("own spread"), the miss meter, the running average of flashes |
| GREEN | the perfect bell (normal curve with the same centre and width), its 2.5% tails (cold open and payoff; the meter's 2.5% line, the interval the bell's true spread would give, "true spread", the ring on the answer), "bell = 0" on the skewness axis |
| RED | an extreme piece that drags the average (the 25.7-minute wait, the farthest flash, infinite variance, "never" on the sample-size axis) |
| PURPLE | the median (the fix for the lighthouse) |
| GRAY / INK | axes, tick labels, sample sizes (guess chips, INK log-axis markers with gray names), the spread and spread cubed (gray bar, gray cubes), the true mean mu, the textbook rule and Kohavi's 2-3% band, citations |

## Beats

### 1. Cold open (0:00-0:14)
> A hundred waits for a bus: mostly short, with a long tail. Textbooks say the average of thirty
> is safe to treat as a bell. For these waits, does it take thirty, three hundred, or over a
> thousand? *[pause 1.5]*

Blue histogram of 100 simulated waits (a brightness sweep, never a height change). On "tail" a
gray brace labelled "tail" spans 20-45 minutes and the 0-20 min bars dim to 40%; the brace holds
about 2.2 s, then steps back to 40% and stays until the first guess chip. On "Textbooks"
"Montgomery & Runger, 2010" appears bottom-left. On "average of thirty" a gray arrow labelled
"average of 30" grows toward a dashed green bell; "?"; three gray guess chips 30 / 300 / 1,000+
arrive on their words (prediction hold).

### 2. Stakes and the criterion (0:14-0:20)
> A-B tests lean on that bell's tails, and on revenue data, thirty is off by a factor of thousands.

The dashed bell flags on "bell's"; on "tails" its two tails beyond 1.96 SD shade green, each
labelled "2.5%" (what "safe" has to mean for a test). On "revenue" the citation becomes "Kohavi
et al., 2014 · KDD"; the 30 chip pulses on "thirty".

### 3. Naive build (0:20-0:30)
> Maybe thirty just means collecting enough waits. Collect a thousand, ten thousand, a hundred
> thousand. The bars get smoother, but the shape doesn't budge.

### 4. Fail, measured (0:30-0:44)
> Measure the lean with skewness: the average cubed gap from the mean, left gaps counting
> negative, over the spread cubed. A perfect bell scores zero. These waits for a bus score about
> two at every sample size.

Definition built term by term from a mean line and x - mu arrows; skew bars 1.90 / 1.96 / 2.00 /
1.98 against the green "bell 0" line; brace "gap ~ 2".

### 5. Fix: average (0:44-0:55)
> So average instead. *[pause 0.5]* Four bus waits: the one long wait gets diluted by three short
> ones. *[pause 0.8]* Drop that one number here. Do that ten thousand times.

Panels n = 1, 4, 16, 64 with a rotated gray "share (%)" and y ticks (10 and 20 on panel 1, 10 on
the others). Four chips (25.7 in red) become (5.2 + 1.8 + 25.7 + 5.3) / 4 = 9.5, which drops into
panel 2.

### 6. Readings (0:55-1:05)
> These averages lean less: skewness one. Sixteen per average: point five. Sixty-four: point two
> five, nearly this perfect bell in green.

The n = 4 bell is drawn whole: its part below 0 minutes (no average gets there) is dimmed.

### 7. Insight: the formula from the readings (1:05-1:13)
> Each time the group grows four times, the skewness halves: two over root n, and two is the
> skewness of one wait.

"x4" arrows between the headers on "grows four times", "/2" arrows between the readings on
"halves"; 2/sqrt(n) is written under each reading while that panel's n pulses (nothing flies
through the panels); the four 2/sqrt(n) become one, then "skew(x-bar) =" arrives in the cleared
space; on "skewness of one wait" the 1.98 reading pulses and the 2 becomes skew(x).

### 8. Why root n, drawn as cubes (1:14-1:29)
> The root comes from the cubes. Add four bus waits: their cubed gaps add up to four times one
> wait's. But the spread only doubles, so its cube grows eight times. Four over eight: half the
> lean. In general, n over n to the one and a half.

The formula opens in place (dashed slot); one blue cube grows out of E[(x-mu)^3] and one gray
cube out of sigma^3 ("cubed gaps", "spread^3"); four blue cubes ("x4"); sigma -> 2 sigma ("x2");
2 x 2 x 2 gray cube ("x8"); x n and x n^{3/2} fly into the slot. In the pause after the beat the
proof closes back to skew(x-bar) = skew(x)/sqrt(n) and the cubes leave, so the next beat starts
from one formula and the panels.

### 9. Why it is a bell (1:30-1:45)
> Kurtosis, the extra tail weight, fades faster: it quarters each time. Every finer difference
> fades faster still. Only the bell survives. That's the central limit theorem. It needs
> independent pieces, and one more condition.

The skew row dims to 40%. Under it: "ex. kurt = 6" (blue, under 1.98), one wait's tail bars
glow on "tail weight", then 1.5 / 0.375 / 0.094 (yellow, exact 6/n) with "÷4" arrows on
"quarters". On "Every finer difference" the three green bells pulse in turn; on "Only the bell"
the n = 64 bars glow. "central limit theorem" (with "independent pieces + one condition" under
it) appears bottom-left beside the formula.

### 10. Payoff: the textbook's thirty (1:46-1:52)
> Back to the textbook's thirty. *[pause 0.5]* Two over root thirty: point three seven. Close to a
> bell, by eye.

Everything but the n = 16 panel leaves; that panel grows into the exact n = 30 panel ("n = 30",
"exact" beside it, "average (minutes)"); the formula moves to the top right; the log axis
"sample size" with a gray "textbook 30" marker fades in.

### 11. Where tests live (1:53-2:13)
> But tests live in the tails: a ninety-five percent interval should miss two and a half percent
> on each side. Tests estimate the spread from the same data. With lopsided waits, a low average
> comes with a small spread, so its interval stops short. *[pause 0.8]* With thirty waits: seven
> percent low, one percent high.

On "tails" the middle bars dim and the bell's tails shade green, while the formulas and the
log axis step back to 35%. A miss meter appears ("misses (simulated)", "low" / "high", a green
dashed line "2.5%"). A gray dashed mu line; one simulated test (average 6.83, sample SD 6.47):
the interval the true spread would give (green, dashed, 3.25-10.41, "true spread") covers mu; on
"small spread" its own interval (yellow, 4.51-9.14, "own spread") is drawn just above it and
stops short of mu; both stay labelled through the pause. On "seven" the yellow interval flows
into the low bar (7.2%); the high bar rises to 1.0%.

### 12. Kohavi's rule is our formula (2:14-2:41)
> Ron Kohavi and colleagues want each side between two and three percent. Their rule: n at least
> three hundred fifty-five times the skewness squared. *[pause 0.3]* Divide by n and take the
> root: *[pause 1.0]* it's our formula: the average's skewness at most point oh five three. At
> three hundred, the lean is point one two: still too much. For these waits: fourteen twenty,
> lean point oh five three, and both misses reach the band. *[pause 1.2]*

Citation: "Kohavi, Deng, Longbotham & Xu, 2014 · KDD (rule after Boos & Hughes-Oliver, 2000)".
On "each side" the tails and both meter readings flash; "2.5%" becomes a gray "2-3%" beside a
gray band. On "Their rule" the panel dims to 35% and skew(x-bar) = 0.37 moves from the right
column to sit right above the meter (the meter's driver). The rule n >= 355 · skew(x)^2 is
written on the lower row; a copy arcs up and becomes skew(x)^2/n <= 1/355 ("Divide by n"), then
skew(x)/sqrt(n) <= 1/sqrt(355) ~ 0.053 ("take the root"). On "our formula" the dimmed formula at
the top lights up with the matching side and comes down into the line, which now reads
skew(x-bar) = skew(x)/sqrt(n) <= 0.053: never more than two equations. On "At three hundred"
the axis returns, a gray 300 marker lands, the dimmed panel morphs to n = 300, the readout
becomes 0.12 (flagged with the 0.053 bound on "point one two") and the meter 3.7% / 1.7%. On
"these waits" the rule becomes n >= 355 · 2^2 = 1,420; on "fourteen" the 1,420 marker, the panel
and the readout 0.053 (flagged with the bound on "lean"), the meter at 3.0% / 2.1%. On "band" a
green ring flashes around the bars and the band; the answer holds about 2.5 s.

### 13. Bing, and the third answer (2:42-2:57)
> Bing's revenue per user had a skewness near eighteen: a hundred and fourteen thousand users.
> Capping each user at ten dollars a week: under ten thousand. And for some data, no number on
> this axis is enough.

On "Bing's" the panel, meter, readout and inequality leave; the sample-size axis rises to the
middle of the frame and the rule moves to the top centre. n >= 355 · 17.9^2 ~ 114,000 (marker),
then n >= 355 · 5.2^2 ~ 9,600 (the dot travels to "capped"). On "no number" a bright sweep runs
along the whole axis; on "enough" a red dashed extension and a red "never" marker appear past
its end.

### 14. The condition: the lighthouse (2:58-3:43)
> A lighthouse one mile off a straight shore flashes at random angles, and each flash lands
> somewhere on the shore. Track the average landing spot. It never settles: a flash aimed almost
> along the shore lands absurdly far away, and yanks it. Among a thousand flashes, the farthest
> typically lands about nine hundred miles off. Divided by a thousand, it still drags the average
> about a mile. Half of single flashes land within a mile of the middle. Repeat the
> thousand-flash average two hundred times, and still only half do. The theorem needs finite
> variance: no single piece can outweigh the rest. Here the variance is infinite. The median
> ignores how far the extremes fly, so it homes in.

In the pause everything but the sample-size axis line fades; the line then slides down and
becomes the shore while the lamp appears. The 200 averages' overflow is counted under the ends
of the strip: "← 12 more" / "12 more →". "simulated" sits top right. On "finite variance" the
running-average chart dims to 30%; on "infinite" (cue moved earlier) the condition turns red.

### 15. Landing (3:44-3:55)
> So the answer is over a thousand, not thirty. Collect forever: still lopsided. The bell was
> never in the data. It's in the average.

In the pause the lighthouse fades first, then the shore slides into the waits axis as the whole
cold-open frame returns (dashed bell, its 2.5% tails, chips). The 1,000+ chip lights on
"thousand"; the arrow label becomes "average of 1,420"; the "tail" brace returns on "lopsided";
on "It's in the average" 10,000 simulated averages of 1,420 waits grow under a solid green bell
(ticks 9.5 and 10.5 only).

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
