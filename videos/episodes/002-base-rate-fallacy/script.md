# Episode 2 — When a 99% Accurate Test Says You're Sick

**Idea (one sentence):** A positive result doesn't hand you the test's 99%; it shrinks the
sample space to everyone who tested positive, and when the condition is rare that crowd is
mostly false alarms, which is all Bayes' theorem (and a model's *precision*) says.

Runtime target ≈ 3:35 · ≈ 500 words · voice af_heart, speed 0.84 (cold open 0.88; the reveal
sentences and the two insight sentences 0.80; 0.2 s pauses inside a thought).

Premise: **1 in 500** sick, the test catches **99 %** and wrongly flags **1 %** of the
healthy → per 10,000 people, 20 sick → 19.8 positive, 9,980 healthy → 99.8 positive →
P(sick∣+) = 16.6 % (**17 %**, "six times too high"). Accuracy is 99 % (9,900 of 10,000 right).
(The accuracy paradox, 99.8 % for a test that calls everyone healthy, is episode 44's topic and is
not used here.)

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| RED | has the condition the test looks for: sick, or a face on a police watch list (nodes, people, counts, the red share of the meter and of the evaluators' bar, *sick* in formulas, the 71 listed squares in the Cardiff crowd, "173 right", "on a watch list", "≤ 1,200 faces · ≤ 1 in 140") |
| BLUE | does not have it: healthy, not on a list (same roles; the Cardiff crowd is blue like the 10,000 people) |
| YELLOW | a positive result, the evidence: the + badge, the test beam, the same ring on every person who tests positive (sick or not) and on every square the camera flags, the outline of the positive crowd / the alerts, the + in P(·∣+), the box around the denominator |
| GREEN | the correct answer (doctors and students who chose it: 23 %, Manrai et al. 2014) |
| GRAY | the naive rule: its 99 % marker, the 44 % of doctors who answered with the test's own accuracy (95 %, "their test: 95% accurate"), the "your guess" marker; also secondary labels, column sums, brackets that measure (6×), citations, other wrong answers, bar titles and tags ("police count", "university evaluators", event tags) |
| INK | text, and the closing "recall" / "precision" tags |
| low opacity | ruled out (tested negative, or cleared by the camera) / context (the table once its numbers are used) |

Emphasis is a colour-preserving scale pulse (never the yellow flash), because yellow already
means "tested positive". The meter title always sits above its bar, and the meter is never
untitled: titles change fade-out-then-fade-in, and the fill is emptied before a new quantity grows.

## Beats

### 1. Cold open + commit (0:00–0:18)
> One in five hundred people has this disease. A test catches ninety-nine percent of the sick and
> wrongly flags one percent of the healthy. If yours says positive, what's the chance you're sick?
> Pick a number. *[1.6 s hold]*
> Most doctors and medical students given a problem like this got it wrong.

Visual: frame 1 holds red "sick" node with "1 in 500", blue "healthy" node, and the empty meter
"chance you're sick ?" ghosted at 30 % on the right. The arrows grow to a yellow + as the rates
are spoken; a ring "you" closes on "yours says positive"; the meter brightens on the question;
the "?" pulses on "Pick a number" and a hollow grey "your guess" marker slides once along the
empty scale during the hold. On "Most doctors" it fades and a 10 × 10 waffle builds under the
meter (23 green = "23% right", "doctors & students", "1 dot = 1%") with the citation
*Manrai et al., 2014 · JAMA Intern. Med.*

### 2. The tempting answer (0:18–0:27)
> Their most common answer was their test's own accuracy: ninety-five percent. For our test,
> that's ninety-nine: you'd start treatment today.

Visual: on "most common answer" the 44 grey dots that said 95 % brighten (the others dim) and
"44% said 95%" appears; "their test: 95% accurate" under it on "their test's own accuracy"; both
95 %s pulse on "ninety-five"; our arrows' rates pulse on "our test"; on "ninety-nine" a copy of
the "95%" morphs into "99%" as it travels round the right end of the meter onto a dashed grey
marker at 99 % ("naive"); the waffle clears. "you" pulses on "treatment".

### 3. Naive build: it works when half are sick (0:27–0:45)
> Check that rule by counting. Here are ten thousand people, and suppose half of them are sick.
> Test everyone. Ninety-nine percent of the sick light up, and one percent of the healthy.
> Of the five thousand who lit up, ninety-nine percent are sick. Here, the rule holds.

Visual: one 1.5 s morph turns the diagram into a counting table (each node + label → row bullet +
label, each arrow → row arrow with its rate riding along, the + → the positives' column header;
the meter steps down out of the way). A 100 × 100 grid ("10,000 people · expected counts");
5,000 turn red; a yellow beam sweeps; negatives dim; counts tick to 4,950 and 50; a grey rule and
"5,000" appear under the positives column on "five thousand"; the meter fills to 99 % on the naive
marker.

### 4. Fail: make it rare (0:45–1:17)
> Now make the disease rare, like yours: one in five hundred. That leaves twenty sick people.
> Run the same test. About twenty sick people light up, plus one percent of the nine thousand
> nine hundred eighty healthy ones. That's about a hundred.
> So of a hundred and twenty positives, only twenty are sick. **Seventeen percent.** *[1 s]*
> **The rule said ninety-nine. Six times too high.** *[1 s]*
> One percent sounds small, but here it's one percent of nearly everyone.

Visual: 4,980 red people turn blue; the 20 sick grow to 3× on "twenty sick". The same beam: every
person it lights gets the same yellow ring, and the 100 healthy positives grow to 3× as it passes,
so 100 ringed blue squares visibly outnumber 20 ringed red ones. Counts tick to 20 and 100; "120"
under the column; meter 17 %; a grey bracket from the 17 % fill edge to the naive marker,
"99 ÷ 17 ≈ 6×"; on "one percent" only the 100 ringed blue squares pulse, on "nearly everyone"
the 9,980.

### 5. Insight: shrink the sample space (1:17–2:04)
> *(0.80)* Your positive result ruled out everyone who tested negative. *[0.6]*
> *(0.80)* What's left is a smaller sample space: these hundred and twenty people.
> Your chance of being sick is the red share of this crowd. Twenty, out of twenty plus a
> hundred. *[1.1, the 17 % flies in silently]*
> Unrounded, the red count is twenty sick people times ninety-nine percent. *[0.6]* The blue
> count is nine thousand nine hundred eighty healthy people times one percent.
> Divide everything by the ten thousand. Counts become shares: two in a thousand sick, nine
> hundred ninety-eight healthy. The share can't change.
> These are how common each group is, and these, how often each group tests positive: Bayes'
> theorem.
> All it does is shrink the sample space to what the evidence allows, then take the share. *[0.8]*

Visual (the one picture): the negatives vanish, the 120 ringed survivors become dots, the header
swaps to "120 people who tested +"; they line up in a 24 × 5 strip, the meter rises to the strip's
row and slides onto it, the yellow outline closes on "these", and the pair rises: the four red
columns sit under the 17 % red segment. The formula is built from the picture:
1. P(sick∣+) from the meter's title; straight brackets count "20" and "100"; their labels fly into
   20 / (20 + 100); the meter's 17 % flies in to "≈ 17%".
2. "twenty sick people times ninety-nine percent": the 20 flies out of the table's people column
   and the 0.99 off the red arrow → 20 × 0.99 (the denominator repeats it in place); the table's
   rounded 20 positives become 19.8. Then 9,980 × 0.01 replaces the 100, and the table's 100
   becomes 99.8.
3. ÷ 10,000: the people column's header becomes "÷ 10,000" (the rest of the table dims); on "two
   in a thousand" the table's 20 and both 20s in the formula become 0.002 in one move, on "nine
   hundred ninety-eight" the 9,980s become 0.998; the 17 % pulses on "the share can't change".
4. Pulses on "how common" (priors, and the table's shares) and "how often" (rates, and the arrows);
   one change to the named form on "Bayes' theorem". A yellow box on the denominator on "shrink",
   a red box on the numerator on "take the share"; the strip's outline pulses in the 0.8 s pause.

### 6. Consequence: precision, Cardiff 2017 (2:04–3:02)
> Swap the disease for a police watch list.
> At the twenty seventeen Champions League final, about a hundred and seventy thousand people were
> in Cardiff. The watch lists held about twelve hundred faces, so even a small error rate per face
> would swamp the real matches.
> Face-recognition cameras scanned the crowd. *[0.3]* They raised two thousand four hundred and
> seventy alerts.
> Shrink to the alerts, and take the red share. Police counted a hundred and seventy-three as
> right: seven percent.
> In machine learning, the share of alerts that are right is called precision.
> Cardiff University's evaluators counted only alerts the logbooks confirmed: three percent.
> Months later, a new algorithm, better photos and practised operators thinned out the false
> alarms, and their count rose to forty-six percent.

Visual: the formula and table clear while the meter empties and is retitled in place ("chance an
alert is right ?"); in one move the meter goes to the top right while the strip's 120 people
spread out into a 100 × 100 crowd that fades in around them (the 20 red become listed faces);
the red legend "■ on a watch list" lands on "watch list". "Cardiff · 3 June 2017" on "Champions
League final", "≈ 170,000 people" over the crowd, "■ = 17 people · illustration" on "Cardiff"; on
"twelve hundred faces" the other 51 listed squares appear (71 in all) and "≤ 1,200 faces · ≤ 1 in
140"; the crowd brightens and "≤ 1 in 140" pulses on "error rate per face"; the 71 pulse on
"swamp". The yellow beam sweeps: every square it flags grows to the listed squares' size with a
yellow ring (145, 10 of them red); cleared listed squares dim. The 10 red flagged pulse; the
legend steps aside and all 145 fly, rings on, into the blocks of a 26 × 95 raster of exactly 2,470
alerts under a bar of the same width. "Shrink to the alerts": the crowd fades out and the meter +
raster move to the centre; straight red/blue brackets on "red share"; "173 right" / "2,297 wrong";
the meter fills to 7 %, its red segment over the red columns. On "precision" the title becomes
"precision". Then a second, thin bar below: "university evaluators" (and "police count" over the
main bar); it fills to 3 % on "three percent" (tag "2017 final"), the tag becomes "Six Nations
2018" on "Months later", and on "thinned out the false alarms" its blue share shrinks while red
grows to 46 % in 1.5 s. Citations: BBC (police figures) for the whole beat, Davies et al. beside it
from the watch-list sentence on.

### 7. Landing: the opening, re-seen (3:02–3:33)
> Back to your test. *[1.0]*
> Your seventeen percent assumes a random screen. Symptoms raise the one in five hundred, and the
> answer climbs: at one in a hundred, fifty percent; at one in two, ninety-nine, where the rule
> held. *[1.2]*
> Ninety-nine percent is the test's recall: how often the sick test positive. Seventeen percent
> is its precision: how often the positive are sick.

Visual: the raster's outline becomes the + badge's disk while the raster shrinks into it; the
cross fades in once the disk has landed; the meter empties in place and is retitled "chance you're
sick", slides back while the cold-open diagram re-forms around the +, and grows its 17 % on
"seventeen percent". The arrows become flows whose widths are the shares of the people reaching +;
the prevalence label goes live (one updater drives label, flows and meter from the same rounded N):
"1 in 100" as it is spoken, 50 % through "fifty percent", "1 in 2 · 99 %" on "ninety-nine", on the
returning "naive 99%" marker; in the pause it returns to 1 in 500 and "20" / "100" appear outside
their flows. "recall" is written beside the arrow's 99 % as the red flow pulses, "precision" under
the meter on its word, size 34, each underlined; the finished two-tag frame holds ≈ 4 s (from
"precision" to the end card). End card.

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
  images only after the final); Champions League section ("Operator logs were then used to clarify whether
  or not these matches were accurate … 3% (N=78) were 'true positives' (confirmed by the operators)").
  Both on screen on the evaluators' own bar.
- All other numbers are computed from the stated premises; see facts.md and check.py.
