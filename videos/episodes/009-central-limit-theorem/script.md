# Episode 9: Why Bell Curves Are Everywhere, and When They're Not

**Idea (one sentence):** Collecting more data never makes lopsided data bell-shaped; averaging
does, because every way an average differs from the bell fades (its skewness is the piece's
over root n, its extra tail weight over n), which for an A-B test on bus waits means 1,420 per
average, not the textbook's 30, and only while no single piece can outweigh the rest (finite
variance).

Runtime 3:52.8 · about 600 words (161 wpm over speech) · voice af_heart, speed 0.86. Narration text lives in
`narration_text.py` (the scene imports it, so script and audio cannot drift). Round 3 cadence:
sentences inside a beat are 0.27 s apart, story-beat boundaries about 0.9 s (`GAP_AFTER`).

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | single pieces: raw waits, one coin flip, single lighthouse flashes, their skewness and kurtosis, skew(x), ex. kurt(x), the cubed-gap cubes |
| YELLOW | averages: the average dot, histograms of averages, skew(x-bar), ex. kurt(x-bar), one test's 95% interval around its average, the miss meter, the running average of flashes |
| GREEN | the perfect bell (normal curve with the same centre and width), its 2.5% tails (and the meter's 2.5% line, the interval the bell's true spread would give, the ring on the answer), "bell = 0" on the skewness axis |
| RED | an extreme piece that drags the average (the 25.7-minute wait, the farthest flash, infinite variance) |
| PURPLE | the median (the fix for the lighthouse) |
| GRAY / INK | axes, tick labels, sample sizes (guess chips, INK log-axis markers with gray names), the spread and spread cubed (gray bar, gray cubes), the true mean mu, the textbook rule and Kohavi's 2-3% band, citations |

## Beats

### 1. Cold open (0:00-0:14)
> A hundred waits for a bus: mostly short, with a long tail. Textbooks say the average of thirty
> is safe to treat as a bell. For these waits, does it take thirty, three hundred, or over a
> thousand? *[pause 1.5]*

Blue histogram of 100 simulated waits (a brightness sweep, never a height change). On "tail" a
gray brace labelled "tail" spans 20-45 minutes and the 0-20 min bars dim to 40%. On "Textbooks"
"Montgomery & Runger, 2010" appears bottom-left. On "average of thirty" a gray arrow labelled
"average of 30" grows toward a dashed green bell; "?"; three gray guess chips 30 / 300 / 1,000+
arrive on their words (prediction hold).

### 2. Stakes (0:14-0:20)
> A-B tests lean on that bell, and on revenue data, thirty is off by a factor of thousands.

The dashed bell flags on "bell"; on "revenue" the citation becomes "Kohavi et al., 2014 · KDD";
the 30 chip pulses on "thirty".

### 3. Naive build (0:20-0:29)
> First, look for the bell in the data itself. Collect a thousand, ten thousand, a hundred
> thousand. The bars get smoother, but the shape doesn't budge.

### 4. Fail, measured (0:29-0:43)
> Measure the lean with skewness: the average cubed gap from the mean, left gaps counting
> negative, over the spread cubed. A perfect bell scores zero. These waits for a bus score about
> two at every sample size.

Definition built term by term from a mean line and x - mu arrows; skew bars 1.90 / 1.96 / 2.00 /
1.98 against the green "bell 0" line; brace "gap ~ 2".

### 5. Fix: average (0:44-0:55)
> So average instead. *[pause 0.5]* Four bus waits: the one long wait gets diluted by three short
> ones. *[pause 0.8]* Drop that one number here. Do that ten thousand times.

Panels n = 1, 4, 16, 64 with a rotated gray "share" beside panel 1's y-axis. Four chips (25.7 in
red) become (5.2 + 1.8 + 25.7 + 5.3) / 4 = 9.5, which drops into panel 2.

### 6. Readings (0:55-1:04)
> These averages lean less: skewness one. Sixteen per average: point five. Sixty-four: point two
> five, nearly this perfect bell in green.

### 7. Insight: the formula from the readings (1:04-1:12)
> Each time the group grows four times, the skewness halves: two over root n, and two is the
> skewness of one wait.

"x4" arcs between the headers, "/2" arcs between the readings, 2/sqrt(n) under each reading
converge to one 2/sqrt(n) with skew(x-bar) = in front; on "skewness of one wait" the 1.98 reading
pulses and the 2 becomes skew(x): skew(x-bar) = skew(x)/sqrt(n). (Round 3 cut the restatement
"So the lean of an average is the lean of one piece, over root n".)

### 8. Why root n, drawn as cubes (1:13-1:27)
> The root comes from the cubes. Add four waits: their cubed gaps add up, four times one wait's.
> But the spread only doubles, so its cube grows eight times. Four over eight: half the lean. In
> general, n over n to the one and a half.

The formula opens in place: skew(x-bar) stays left, "= skew(x)/sqrt(n)" slides right (nothing is
duplicated), "=" fades in, a dashed gray box holds the empty slot, and E[(x-mu)^3]/sigma^3 is
written while skew(x) flags. One blue cube grows out of E[(x-mu)^3] and one gray cube out of
sigma^3, captioned "cubed gaps" and "spread^3". The blue cube copies to a row of four ("x4"). On
"spread" a gray bar sigma appears over the gray cube; on "doubles" it grows to 2 sigma ("x2"); on
"cube grows" the gray cube becomes a 2 x 2 x 2 cube of eight ("x8"). "Four over eight" flags both
labels and the /2 arrow between 1.98 and 0.99 flags on "half". On "In general" the labels become
x n, x root n and x n^{3/2}, and x n and x n^{3/2} fly into the dashed box as n / n^{3/2}.

### 9. Universality, and why it is a bell (1:28-1:50)
> A coin that lands heads one time in ten is just two spikes, yet its averages make the same bell,
> by the same rule. Kurtosis, the extra tail weight, fades faster, as one over n, and every finer
> difference faster still. Only the bell survives. That's the central limit theorem. It needs
> independent pieces, and one more condition.

Panel 1 becomes the coin's two spikes (its y-axis stays); panel 4 the exact share of heads in 64
flips (skew 0.33 = 2.67/sqrt(64)). A copy of the formula becomes ex. kurt(x-bar) = ex. kurt(x)/n
(excess kurtosis: a bell scores 0).

### 10. Payoff: the textbook's thirty (1:51-1:57)
> Back to the textbook's thirty. *[pause 0.5]* Two over root thirty: point three seven. Close to a
> bell, by eye.

The coin frame dissolves into the exact n = 30 panel ("share (exact)", "average
(minutes)") and the log axis "sample size" with a gray "textbook 30" marker.

### 11. Where tests live (1:58-2:15)
> But tests live in the tails: a ninety-five percent interval should miss two and a half percent
> on each side. Tests estimate the spread from the same data, so a low average gets a small spread,
> and its interval stops short. With thirty waits: seven percent low, one percent high.

The middle bars dim and the bell's tails shade green. A miss meter appears beside the panel
(header "misses (simulated)", "low" / "high", a green dashed line labelled "2.5%"). A gray dashed
mu line at 10; one simulated test (average 6.83, sample SD 6.47) appears as a yellow dot; the
interval its true spread would give (green, dashed, 3.25-10.41) shrinks to its own interval
(yellow, 4.51-9.14), whose right end stops short of mu. On "seven percent low" that interval
flows into the low bar (7.2%); the high bar rises to 1.0%.

### 12. Kohavi's rule is our formula (2:16-2:41)
> Ron Kohavi and colleagues, using Bing's data, want each side between two and three percent.
> Their rule: n at least three hundred fifty-five times the skewness squared. *[pause 0.3]* Divide
> by n and take the root: *[pause 1.0]* it's our formula: the average's skewness at most point oh
> five three. Three hundred still misses. For these waits: fourteen twenty, and both misses reach
> the band. *[pause 1.2]*

Citation: Kohavi, Deng, Longbotham & Xu, 2014 · KDD. On "each side" the tails and both meter
readings flash. "2.5%" becomes a gray "2-3%" beside a gray
band. n >= 355 · skew(x)^2 -> skew(x)^2/n <= 1/355 -> skew(x)/sqrt(n) <= 1/sqrt(355) ~ 0.053. On
"Three hundred" a gray 300 marker lands, the panel morphs to n = 300 (skew 0.12) and the meter to
3.7% / 1.7% (the low bar still above the band). On "fourteen twenty" n >= 355 · 2^2 = 1,420, the
1,420 marker, the n = 1,420 panel (skew 0.053) and the meter at 3.0% / 2.1%: on the band. On
"band" a green ring flashes around the bars and the band; the answer holds about 3 s.

### 13. Bing (2:41-2:51)
> Bing's revenue per user had a skewness near eighteen: a hundred and fourteen thousand users.
> Capping each user at ten dollars a week: under ten thousand.

The panel and meter dim on "Bing's". n >= 355 · 17.9^2 ~ 114,000, then n >= 355 · 5.2^2 ~ 9,600.

### 14. The condition: the lighthouse (2:52-3:40)
> Now the condition. A lighthouse one mile off a straight shore flashes at random angles, and each
> flash lands somewhere on the shore. Track the average landing spot. It never settles: a flash
> aimed almost along the shore lands absurdly far away, and yanks it. Among a thousand flashes,
> the farthest typically lands about nine hundred miles off. Divided by a thousand, it still drags
> the average about a mile. Half of single flashes land within a mile of the middle. Repeat the
> thousand-flash average two hundred times, and still only half do. The theorem needs finite
> variance: no single piece can outweigh the rest. Here the variance is infinite. The median
> ignores how far the extremes fly, so it homes in.

The payoff dissolves into the shore and lamp in the pause before "Now the condition" (the map
starts while the payoff is at about 30%). On "finite variance" the running-average chart dims to
30% and "1 mi" fades, leaving the condition and the red jump dot; the chart returns on "median",
when the purple median is drawn on it.

### 15. Landing (3:41-3:53)
> So the answer is over a thousand, not thirty. And collect forever: this histogram stays
> lopsided. The bell was never in the data. It's in the average.

The cold-open frame is whole before "So the answer" (dissolve in the pause, the shore line sliding
into the waits axis). The 1,000+ chip lights on "thousand"; the arrow label becomes "average of
1,420"; the "tail" brace returns on "lopsided"; on "It's in the average" 10,000 simulated averages
of 1,420 waits grow under a solid green bell (ticks 9.5 and 10.5 only).

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
