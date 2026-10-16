# Episode 2 — When a 99% Accurate Test Says You're Sick

**Idea (one sentence):** A positive result doesn't hand you the test's 99%; it shrinks the
sample space to everyone who tested positive, and when the condition is rare that crowd is
mostly false alarms, which is all Bayes' theorem (and a model's *precision*) says.

Runtime target ≈ 3:40 · ≈ 520 words · voice af_heart, speed 0.84 (cold open 0.86; the reveal
sentences and the two insight sentences 0.80; 0.2 s pauses inside a thought).

Premise: **1 in 500** sick, the test catches **99 %** and wrongly flags **1 %** of the
healthy → per 10,000 people, 20 sick → 19.8 positive, 9,980 healthy → 99.8 positive →
P(sick∣+) = 16.6 % (**17 %**, "six times too high"). Accuracy is 99 % (9,900 of 10,000 right);
a test that calls everyone healthy scores 99.8 %.

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| RED | has the condition the test looks for: sick, or a face on a police watch list (nodes, people, counts, the red share of the meter, *sick* in formulas, the 71 listed squares in the Cardiff crowd, "173 right", "watch-listed: ≤ 1,200") |
| BLUE | does not have it: healthy, not on a list (same roles; the Cardiff crowd is blue like the 10,000 people) |
| YELLOW | a positive result, the evidence: the + badge, the test beam, the outline of the positive crowd / the alerts, the rings on the squares the camera flags, the + in P(·∣+), the box around the denominator |
| GREEN | the correct answer (doctors and students who chose it: 23 %, Manrai et al. 2014) |
| GRAY | the naive rule: its 99 % marker, the 44 % of doctors who answered with the test's own accuracy (95 %), and accuracy (the naive score: both accuracy bars); also secondary labels, citations, other wrong answers, the evaluators' 3 % / 46 % tick labels |
| INK | text, and the closing "recall" / "precision" tags |
| low opacity | ruled out (tested negative, or cleared by the camera) / context (the table once its numbers are used) |

Emphasis is a colour-preserving scale pulse (never the yellow flash), because yellow already
means "tested positive". The meter title always sits above its bar, and the meter is never
untitled: titles change fade-out-then-fade-in, and the fill is emptied before a new quantity grows.

## Beats

### 1. Cold open + commit (0:00–0:20)
> One in five hundred people has this disease. A test catches ninety-nine percent of cases and
> wrongly flags one percent of the healthy. If yours says positive, what's the chance you're
> sick? *[0.3]* Pick a number. *[1.6 s hold]*
> Most doctors and medical students given a problem like this got it wrong.

Visual: frame 1 holds red "sick" node with "1 in 500", blue "healthy" node, and the empty meter
"chance you're sick ?" ghosted at 30 % on the right. The arrows grow to a yellow + as the rates
are spoken; a ring "you" closes on "yours says positive"; the meter brightens on the question;
the "?" pulses on "Pick a number"; hold. Only then, on "Most doctors", a 10 × 10 waffle builds
under the meter (23 green = "23% right", "doctors & students", "1 dot = 1%") with the citation
*Manrai et al., 2014 · JAMA Intern. Med.*

### 2. The tempting answer (0:20–0:27)
> Their most common answer was the test's own accuracy, here ninety-nine percent: you'd start
> treatment today.

Visual: on "most common answer" the 44 grey dots that said 95 % brighten (the others dim) and
"44% said 95%" appears; both rates pulse on "accuracy"; on "ninety-nine percent" a copy of the
"99%" rises, travels above the meter title and drops onto a dashed grey marker at 99 % ("naive");
the waffle clears. "you" pulses on "treatment".

### 3. Naive build: it works when half are sick (0:27–0:45)
> Check that rule by counting. Here are ten thousand people, and suppose half of them are sick.
> Test everyone. Ninety-nine percent of the sick light up, and one percent of the healthy.
> Of the five thousand who lit up, ninety-nine percent are sick. Here, the rule holds.

Visual: the diagram straightens into a counting table in three stages; a 100 × 100 grid
("10,000 people · expected counts"); 5,000 turn red; a yellow beam sweeps; negatives dim; counts
tick to 4,950 and 50; the meter fills to 99 % on the naive marker.

### 4. Fail: make it rare (0:45–1:17)
> Now make the disease rare, like yours: one in five hundred. That leaves twenty sick people.
> Run the same test. About twenty sick people light up, plus one percent of the nine thousand
> nine hundred eighty healthy ones. That's about a hundred.
> So of a hundred and twenty positives, only twenty are sick. **Seventeen percent.** *[1 s]*
> **The rule said ninety-nine. Six times too high.** *[1 s]*
> One percent sounds small, but here it's one percent of nearly everyone.

Visual: 4,980 red people turn blue, the 20 sick get rings, the same beam, counts tick to 20 and
100, meter 17 %, brace "6× too high", the dimmed healthy crowd brightens on "nearly everyone".

### 5. Insight: shrink the sample space (1:17–2:10)
> *(0.80)* Your positive result ruled out everyone who tested negative. *[0.6]*
> *(0.80)* What's left is a smaller sample space: these hundred and twenty people.
> Your chance of being sick is the red share of this crowd. Twenty, out of twenty plus a
> hundred. *[1.1, the 17 % flies in silently]*
> Unrounded, the red count is twenty sick people times ninety-nine percent. *[0.6]* The blue
> count is nine thousand nine hundred eighty healthy people times one percent.
> Divide top and bottom by the ten thousand we started with. Twenty people become two in a
> thousand, and nine thousand nine hundred eighty become nine hundred ninety-eight in a thousand.
> The share can't change.
> These are how common each group is, and these, how often each group tests positive: Bayes'
> theorem.
> All it does is shrink the sample space to what the evidence allows, then take the share. *[0.8]*

Visual (the one picture): the negatives vanish, the 120 survivors swell, the header swaps to
"120 people who tested +"; they line up in a 24 × 5 strip, the meter slides onto it, the yellow
outline closes on "these", and the pair rises: the four red columns sit under the 17 % red segment.
The formula is built from the picture and changes only four times, each at least 5 s after the last:
1. Built: P(sick∣+) from the meter's title; braces count "20" and "100"; their labels fly into
   20 / (20 + 100); the meter's 17 % flies in to "≈ 17%".
2. "twenty sick people times ninety-nine percent": the 20 flies out of the table's people column
   and the 0.99 off the red arrow → 20 × 0.99 (the denominator repeats it in place); the table's
   rounded 20 positives become 19.8. Then "nine thousand nine hundred eighty … one percent":
   9,980 × 0.01 replaces the 100, and the table's 100 becomes 99.8.
3. The ÷ 10,000 step has its own picture: the people column's header becomes "÷ 10,000" (the rest
   of the table dims), 20 → 0.002 on "two in a thousand", 9,980 → 0.998 on "nine hundred
   ninety-eight"; on "the share can't change" the shares fly into the formula and the 17 % pulses.
4. Pulses on "how common" (priors, and the table's shares) and "how often" (rates, and the arrows);
   one change to the named form on "Bayes' theorem". A yellow box on the denominator on "shrink",
   a red box on the numerator on "take the share" (≥ 0.15 clear of the bar), the strip's outline
   pulses in the 0.8 s pause.

### 6. Consequence: precision, Cardiff 2017 (2:10–3:00)
> Swap the disease for a police watch list.
> At the twenty seventeen Champions League final, about a hundred and seventy thousand people were
> in Cardiff. The watch lists held about twelve hundred faces, so even a small error rate per face
> would swamp the real matches.
> Face-recognition cameras scanned the crowd. *[0.3]* They raised two thousand four hundred and
> seventy alerts.
> Shrink to the alerts, and take the red share. Police counted a hundred and seventy-three as
> right: seven percent.
> In machine learning, the share of alerts that are right is called precision.
> The university's evaluators counted three percent here. After a new algorithm and better photos
> cut the false alarms, they counted forty-six at the Six Nations.

Visual: the formula, table and strip clear while the meter empties and is retitled in place
("chance an alert is right ?"); then in one move the meter goes to the top right while a blue 100 × 100
crowd fades in at its final place on the left ("≈ 170,000 people"; legend "■ = 17 people ·
illustration"). On "twelve hundred faces" 71 squares turn red ("■ watch-listed: ≤ 1,200"); the crowd
brightens on "error rate per face"; the 71 pulse on "swamp". The yellow beam sweeps and stops;
cleared squares dim; 145 squares stay lit with yellow rings. A beat later the 10 red ones among them
pulse, rings on; then all 145 fly, rings on, into the blocks of a 26 × 95 raster of exactly 2,470
alerts under a bar of the same width, the 10 red ones in the first columns. "Shrink to the alerts":
the crowd fades out and the meter + raster move to the centre; braces grow under the red and blue
columns on "red share"; "173 right" / "2,297 wrong" on "hundred and seventy-three"; the meter fills to
7 %, its red segment over the red columns. On "precision" the title becomes "precision". The title
lifts; dashed ink ticks: 3 % "evaluators: 3%" on "three percent", 46 % "Six Nations 2018: 46%" on
"forty-six" (both the evaluators' own counts); the 2,297 pulse on "false alarms". Citations: BBC
(police figures) for the whole beat, Davies et al. from the watch-list sentence on.

### 7. Landing: the opening, re-seen (3:00–3:40)
> Back to your test. *[0.9]* The title's ninety-nine percent accuracy is real. But a test that
> calls everyone healthy scores ninety-nine point eight: more accurate, and useless.
> Your seventeen percent assumes a random screen. Symptoms raise the one in five hundred, and the
> answer climbs: at one in a hundred, fifty percent; at one in two, ninety-nine, where the rule
> held. *[1.2]*
> Ninety-nine percent is the test's recall: how often the sick test positive. Seventeen percent
> is its precision: how often the positive are sick.

Visual: the raster's outline becomes the + badge's disk (both closed shapes) while the raster
shrinks into it; the cross fades in once the disk has landed; the meter empties in place and is
retitled "chance you're sick", slides back, and grows its 17 % from zero; the cold-open diagram
re-forms around the +. Under the meter two grey bars: "accuracy" fills to 99 % on "real";
on "calls everyone healthy" the second bar appears and both flows drain, their rates read 0 % and the
+ dims (nothing reaches it); "calls everyone healthy" fills to 99.8 %; both values pulse on "more
accurate"; the red 0 % pulses on "useless". Then the flows refill, the rates return, the bars leave;
the arrows become flows whose widths are the shares of the people reaching +; the prevalence label
goes live (one updater drives label, flows and meter from the same rounded N): it reaches "1 in 100"
as it is spoken and holds 50 % through "fifty percent", then reaches "1 in 2 · 99 %" on
"ninety-nine", on the returning "naive 99%" marker; in the pause it returns to 1 in 500 and "20" /
"100" appear outside their flows, silently. The closing chiasmus writes "recall" beside the arrow's
99 % and "precision" under the meter, each on its spoken word, size 34, each underlined as it is
written. End card.

## Sources
- Manrai, A. K., Bhatia, G., Strymish, J., Kohane, I. S., & Jain, S. H. (2014). Medicine's
  uncomfortable relationship with math: calculating positive predictive value. *JAMA Internal
  Medicine*, 174(6), 991–993. doi:10.1001/jamainternmed.2014.1059 (61 respondents; 14 right; most
  common answer 95 %, 27 of 61).
- BBC News (4 May 2018), "2,000 wrongly matched with possible criminals at Champions League"
  (South Wales Police data: about 170,000 people in Cardiff; 2,470 alerts, 2,297 wrong; police
  blamed poor-quality images from UEFA and Interpol).
- Davies, B., Innes, M., & Dawson, A. (2018). *An Evaluation of South Wales Police's Use of
  Automated Facial Recognition.* Universities' Police Science Institute, Cardiff University, p. 10
  (around 1,200 images on the Champions League watch lists); key findings (true positives 3 % at the
  Champions League final → 46 % at the 2018 Six Nations, with the new algorithm; high-standard custody
  images only after the final). Both on screen as the evaluators' ticks.
- All other numbers are computed from the stated premises; see facts.md and check.py.
