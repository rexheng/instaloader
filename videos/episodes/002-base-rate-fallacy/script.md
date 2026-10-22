# Episode 2 — When a 99% Accurate Test Says You're Sick

**Idea (one sentence):** A positive result doesn't hand you the test's 99%; it shrinks the
sample space to everyone who tested positive, and when the condition is rare that crowd is
mostly false alarms, which is all Bayes' theorem (and a model's *precision*) says.

Runtime target ≤ 3:37 · ≈ 485 words · voice af_heart, speed 0.84, `CADENCE = "shaped"` (gaps follow
the sense); the reveal sentences and the two insight sentences 0.80; 1.0 s after "Seventeen percent",
"Six times too high" and the Cardiff answer "seven percent", 0.9 s after the thesis (PRODUCTION_GUIDE §13).

Structure (round 7): the episode **opens on a real case** (Cardiff 2017: 2,470 face-recognition alerts,
"How many were right? Pick a number"), turns each alert into a positive test result (the raster
collapses into the + badge), builds and breaks the naive rule on a test the viewer can count, derives
Bayes from the picture, then answers the opening question on the same raster (173 right: 7 %, precision)
and ends on the test: "Your test didn't say you're sick. It said you're in this crowd."

Premise of the countable case: **1 in 500** sick, the test catches **99 %** and wrongly flags **1 %** of
the healthy → per 10,000 people, 20 sick → 19.8 positive, 9,980 healthy → 99.8 positive →
P(sick∣+) = 16.6 % (**17 %**, "six times too high"). Accuracy is 99 % (9,900 of 10,000 right), and so
are recall (sensitivity) and specificity: the landing calls the arrow's 99 % "recall" (it is
P(+ ∣ sick)), and says it "describes the test".

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| RED | has the condition the test looks for: sick, or a face on a police watch list (nodes, people, counts, the red share of every meter and bar, *sick* in formulas, the 71 listed squares in the Cardiff crowd, "173 right", "watch list · ≤ 1 in 140") |
| BLUE | does not have it: healthy, not on a list (same roles; the Cardiff crowd is blue like the 10,000 people; "P(+ ∣ not listed) ↓", the false alarms' term) |
| YELLOW | a positive result, the evidence: the + badge, the test beam, the same ring on every person who tests positive and on every square the camera flags, the outline of the positive crowd / the alerts, the + in P(·∣+), the box around the denominator (and its ghost) |
| GREEN | the correct answer (doctors and students who chose it: 23 %, Manrai et al. 2014) |
| GRAY | the naive rule: its 99 % marker, the 44 % who answered with their test's own accuracy, "your guess"; also the cold open's unchecked alerts (grey cells: nobody knows yet which are right), secondary labels, column sums, brackets that measure (6×), citations, other wrong answers, bar tags, braces, "7 of 22 later proved false" |
| INK | text, and the "precision" / "recall" tags |
| low opacity | ruled out (tested negative, or passed by the camera) / a meter still waiting for its number (30 %) / context (the police raster at 35 % while the evaluators' bar is read) |

Emphasis is a colour-preserving scale pulse (never the yellow flash), because yellow already
means "tested positive". The meter title always sits above its bar, and the meter is never
untitled: titles change fade-out-then-fade-in, and the fill is emptied before a new quantity grows.

## Beats

### 1. Cold open: Cardiff, commit (0:00–0:12)
> In twenty seventeen, police cameras in Cardiff raised two thousand four hundred seventy watch-list
> alerts. How many were right? *[0.3]* Pick a number. *[1.6 s hold]*

Visual: frame 1 holds the yellow-outlined 26 × 95 raster (its first columns of grey, unchecked cells)
under the empty meter "chance an alert is right ?" ghosted at 30 %; the cells pile up column by column
to 2,470 as the sentence runs; the dateline "Cardiff · Champions League final week, 2017" and the BBC
citation fade in; "2,470 alerts" lands under the raster. The meter brightens on "How many"; the "?"
pulses on "Pick a number" and a hollow grey "your guess" marker slides once along the empty scale.

### 2. The same question, countable (0:12–0:27)
> Each alert is a positive test result. *[0.4]* One in five hundred people has this disease. A test
> catches ninety-nine percent of the sick and wrongly flags one percent of the healthy. If yours says
> positive, what's the chance you're sick?

Visual: on "positive" the raster collapses into the + badge (the outline stays one convex shape and
becomes the disk; the cells shrink into it), the meter is retitled "chance you're sick" and slides to
the right; then the disease diagram forms around the +: the sick / healthy nodes and "1 in 500" on
"One in five hundred", the arrows and their rates on their words, the ring "you" on "yours".

### 3. The tempting answer (0:27–0:42)
> At one Boston-area hospital, doctors and students given a problem like this most often answered with
> their test's own accuracy: ninety-five percent. For ours, that's ninety-nine: you'd start treatment today.

Visual: a 10 × 10 waffle under the meter (23 green "23% right", "doctors & students", "1 dot = 1%",
*Manrai et al., 2014 · JAMA Intern. Med.*); the 44 grey dots that said 95 % brighten, "44% said 95%",
and under it what the respondents were told: "their test: 5% false alarms"; on "ninety-nine" the "95%"
turns into "99%" as it travels round the meter onto a dashed grey "naive 99%" marker.

### 4. Naive build: it works when half are sick (0:42–0:57)
> Check that rule by counting: ten thousand people, half of them sick.
> Test everyone, and watch who lights up.
> Of the five thousand who lit up, ninety-nine percent are sick. Here, the rule holds.

Visual: unchanged from round 6 (diagram → counting table in one morph; 100 × 100 grid at the header's own
1 in 500; the left 50 columns flood red on "half"; the beam; 4,950 / 50; the meter fills onto the marker).

### 5. Fail: the same test, a rarer disease (0:57–1:29)
> Now keep the same test, and make the disease rarer and rarer, down to yours: one in five hundred.
> About twenty sick people light up, plus one percent of everyone else: about a hundred.
> So of a hundred twenty positives, only twenty are sick. **Seventeen percent.** *[1 s]*
> **The rule said ninety-nine. Six times too high.** *[1 s]*
> One percent sounds small, but here it's one percent of nearly everyone.

Visual (the episode's own image): ONE prevalence slider, 1 in 2 → 1 in 500, drains the block from its
right edge while the table ticks and the meter falls live from the naive marker to 17 %. When it stops,
the 20 sick left inside the old block each cross-fade, in place, with a healthy person elsewhere, so
the rare sick sit anywhere in the grid (counts and meter unchanged). Then the 20 and the 100 are ringed
on their words, "99 ÷ 17 ≈ 6×", and the 100 false alarms pulse on "one percent of nearly everyone".

### 6. Insight: shrink the sample space (1:29–2:21)
Unchanged narration, except "The share stays the same. *[0.6]*": on those words the formula's fraction
bar, its "≈ 17 %" and the meter's 17 % pulse together and the frame holds, so the unchanged ratio is on
screen while every count around it has just become a share.

### 7. Payoff: back to Cardiff, precision (2:21–3:13)
> Swap the disease for a police watch list.
> About a hundred seventy thousand people came for the final, and the watch lists held about twelve
> hundred photos. *[0.3]* Even a small error rate per face would swamp the real matches.
> For four days, face-recognition cameras scanned the crowds. *[0.3]* Every face they flagged joined the alerts.
> Shrink to the alerts. Take the red share.
> The police counted a hundred seventy-three as right: seven percent. *[1.0]*
> In machine learning, that share is called precision. *[0.6]*
> Cardiff University's evaluators counted only alerts the logbooks confirmed: three percent. *[0.6]*
> Months later, a new algorithm and better photos thinned out the false alarms. *[0.4]*
> That's the blue term in Bayes' denominator. *[0.3]* Their count rose to forty-six percent. *[0.8]*

Visual: the formula and table clear; the 24 × 5 strip shrinks, as one block, into the 24 × 5 squares at
the centre of a 100 × 100 crowd (■ = 17 people, illustration) that fades in around it, the 20 sick
turning blue as they land (red now means "listed"); the meter travels to the right column, ghosted and
retitled "chance an alert is right ?". "≈ 170,000 people", the scale legend, the dateline; the 71
listed squares appear scattered on "twelve hundred photos" with "· ≤ 1 in 140" and Davies et al.'s
citation; the crowd brightens on "error rate per face", the 71 pulse on "swamp". The beam flags 145
squares (10 red), every square it passes without flagging dims to the same 35 %, listed or not; the
ghosted meter title fades further while the 145 file into the 26 × 95 raster of 2,470 alerts (the
cold open's raster, now coloured). "Shrink to the alerts": the crowd leaves, meter + raster take the
centre, brackets, "173 right / 2,297 wrong", the meter fills to 7 %, the opening question answered.
"precision" rolls in as the title. The lever: the raster dims to 35 %, its labels leave, the police bar
is tagged "police count / 2,470 alerts" and the evaluators' bar takes the labels' row ("evaluators' count
/ final week · 2,632 alerts"), filling to 3 %; "Six Nations 2018 · 48 alerts" on "Months later"; a ghost
of the boxed Bayes denominator fades into its own band on "false alarms"; on "blue term" its blue
P(healthy)P(+∣healthy) pulses and rises into "P(+ ∣ not listed) ↓" under the bar's blue segment (≥ 0.6
clear of the tag column), the rest of the ghost fading; on "rose" the blue share shrinks and the red
grows to 46 %, and "7 of 22 later proved false" joins the tags.

### 8. Landing: your test (3:13–3:36)
> Back to your test. *[1.6]*
> Symptoms raise the one in five hundred: at one in a hundred, fifty percent; at one in two,
> ninety-nine, where the rule held. *[1.0]*
> That ninety-nine percent describes the test: its recall, how often the sick test positive. *[0.3]*
> Seventeen percent describes your result: its precision. *[0.4]*
> Your test didn't say you're sick. *[0.3]* It said you're in this crowd.

Visual: in the first 0.5 s every Cardiff tag, bar and citation fades out; only the raster → + badge
collapse runs across the gap, and the diagram's nodes fade in after it. Each arrow swells into a flow as
wide as the people it carries (20 / 100 "per 10,000 people") and the meter grows its 17 % again. The
prevalence slider runs backwards (1 in 100 · 50 %, 1 in 2 · 99 % on the naive marker, back to 1 in 500).
"recall" is written beside the arrow's 99 % as the red flow pulses, "precision" under the meter. On
"you're sick" the "you" ring pulses; on "this crowd" both flows into the + swell once. The frame holds
0.8 s and fades out (no end card): the last frame is the opening question, answered.

## Sources
- Manrai, A. K., Bhatia, G., Strymish, J., Kohane, I. S., & Jain, S. H. (2014). Medicine's
  uncomfortable relationship with math: calculating positive predictive value. *JAMA Internal
  Medicine*, 174(6), 991–993. doi:10.1001/jamainternmed.2014.1059 (61 respondents; prevalence 1/1000 and a 5 %
  false-positive rate given; 14 right; most common answer 95 %, 27 of 61; on screen "their test: 5% false
  alarms").
- BBC News (4 May 2018), "2,000 wrongly matched with possible criminals at Champions League"
  (South Wales Police data: about 170,000 people in Cardiff; 2,470 alerts, 2,297 wrong; police
  blamed poor-quality images from UEFA and Interpol).
- Wired UK (4 May 2018), "Facial recognition tech used by UK police is making a ton of mistakes"
  ("During the UEFA Champions League Final week … there were 2,470 alerts"), and Davies et al.'s
  deployment table ("Champions League (4 days)"): the alerts cover four days, not the match day.
- Davies, B., Innes, M., & Dawson, A. (2018). *An Evaluation of South Wales Police's Use of
  Automated Facial Recognition.* Universities' Police Science Institute, Cardiff University, p. 10
  (around 1,200 images on the Champions League watch lists, including the police "friendlies" list); key findings (true positives 3 % at the
  Champions League final → 46 % at the 2018 Six Nations, with the new algorithm; high-standard custody
  images only after the final); Champions League section ("Operator logs were then used to clarify whether
  or not these matches were accurate … 3% (N=78) were 'true positives' (confirmed by the operators)").
  Both on screen on the evaluators' own bar. Six Nations section: "Of the initial 22 'true positives' …
  32% (n=7) were stopped but turned out to be false positives according to Intervention Teams" (on screen:
  "7 of 22 later proved false").
- All other numbers are computed from the stated premises; see facts.md and check.py.
