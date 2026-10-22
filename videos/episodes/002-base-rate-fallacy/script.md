# Episode 2 — When a 99% Accurate Test Says You're Sick

**Idea (one sentence):** A positive result doesn't hand you the test's 99%; it shrinks the
sample space to everyone who tested positive, and when the condition is rare that crowd is
mostly false alarms, which is all Bayes' theorem (and a model's *precision*) says.

Runtime target ≤ 3:35 · ≈ 475 words · voice af_heart, speed 0.84, `CADENCE = "shaped"` (gaps follow
the sense; "hundred and twenty" is read "hundred twenty"); the reveal sentences and the two insight
sentences 0.80, the "red share" sentence 0.81; 1.0 s after "Seventeen percent" and "Six times too
high", 0.9 s after the thesis (PRODUCTION_GUIDE §13).

Premise: **1 in 500** sick, the test catches **99 %** and wrongly flags **1 %** of the
healthy → per 10,000 people, 20 sick → 19.8 positive, 9,980 healthy → 99.8 positive →
P(sick∣+) = 16.6 % (**17 %**, "six times too high"). Accuracy is 99 % (9,900 of 10,000 right).
(The accuracy paradox, 99.8 % for a test that calls everyone healthy, is episode 44's topic and is
not used here.)

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| RED | has the condition the test looks for: sick, or a face on a police watch list (nodes, people, counts, the red share of the meter and of the evaluators' bar, *sick* in formulas, the 71 listed squares in the Cardiff crowd, "173 right", "watch list · ≤ 1 in 140") |
| BLUE | does not have it: healthy, not on a list (same roles; the Cardiff crowd is blue like the 10,000 people; "P(+ ∣ not listed) ↓", the false alarms' term) |
| YELLOW | a positive result, the evidence: the + badge, the test beam, the same ring on every person who tests positive (sick or not) and on every square the camera flags, the outline of the positive crowd / the alerts, the + in P(·∣+), the box around the denominator |
| GREEN | the correct answer (doctors and students who chose it: 23 %, Manrai et al. 2014) |
| GRAY | the naive rule: its 99 % marker, the 44 % of doctors who answered with the test's own accuracy (95 %, "their test: 95% accurate"), the "your guess" marker; also secondary labels, column sums, brackets that measure (6×), citations, other wrong answers, bar tags ("police count / 2,470 alerts", "evaluators' count / …"), the "how common" / "how often" braces, the ghost meter's "your test" |
| INK | text, and the "precision" / "precision too" / "recall" tags |
| low opacity | ruled out (tested negative, or cleared by the camera) / a meter still waiting for its number (30 %, as in the cold open and the Cardiff build-up) |

Emphasis is a colour-preserving scale pulse (never the yellow flash), because yellow already
means "tested positive". The meter title always sits above its bar, and the meter is never
untitled: titles change fade-out-then-fade-in, and the fill is emptied before a new quantity grows.

## Beats

### 1. Cold open + commit (0:00–0:18)
> One in five hundred people has this disease. A test catches ninety-nine percent of the sick and
> wrongly flags one percent of the healthy. If yours says positive, what's the chance you're sick?
> *[0.3]* Pick a number. *[1.6 s hold]*
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
> Check that rule by counting: ten thousand people, half of them sick.
> Test everyone, and watch who lights up.
> Of the five thousand who lit up, ninety-nine percent are sick. Here, the rule holds.

Visual: one 1.5 s morph turns the diagram into a counting table (each node + label → row bullet +
label, each arrow → row arrow with its rate riding along, the + → the positives' column header,
"1 in 500" → the table's header above the sick row; the meter steps down out of the way). A 100 × 100
grid ("10,000 people · expected counts"); on "half" the left 50 columns fill with red (a block, no
moiré) and the header's "500" rolls to "2"; a yellow beam sweeps: almost all of the left half stays lit,
the right half dims but for a sprinkle of 50; counts tick to 4,950 and 50; a grey rule and a live sum
"5,000" under the positives column on "five thousand"; the meter fills to 99 % on the naive marker.

### 4. Fail: the same test, a rarer disease (0:45–1:17)
> Now keep the same test, and make the disease rarer and rarer, down to yours: one in five hundred.
> About twenty sick people light up, plus one percent of the healthy ones: about a hundred.
> So of a hundred and twenty positives, only twenty are sick. **Seventeen percent.** *[1 s]*
> **The rule said ninety-nine. Six times too high.** *[1 s]*
> One percent sounds small, but here it's one percent of nearly everyone.

Visual (the episode's own image): the rates 99 % / 1 % pulse on "same test"; then ONE slider. The
table's "1 in 2" runs to "1 in 500" (log-spaced), the red block drains from its right edge (the 50
false-alarm people inside it stay lit as they turn blue), the table's counts and sum tick as expected
counts, and the meter falls live away from the naive marker: 99 → 92 → 67 → 50 → 17 %. The failure is
measured before it is explained. Then the 20 sick grow to 3× with a yellow ring on "twenty sick", the
100 healthy positives on "one percent of …" (left to right); no two rings touch. "120" pulses; the 17 %
pulses; a grey bracket from the 17 % fill edge to the naive marker, "99 ÷ 17 ≈ 6×"; on "one percent"
only the 100 ringed blue squares pulse, on "nearly everyone" the 9,980.

### 5. Insight: shrink the sample space (1:17–2:10)
> *(0.80)* Your positive result ruled out everyone who tested negative. *[0.6]*
> *(0.80)* What's left is a smaller sample space: these hundred and twenty people.
> Your chance of being sick is the red share of this crowd. Twenty, out of twenty plus a
> hundred. *[1.1, the 17 % flies in silently]*
> Unrounded, the red count is twenty sick people times ninety-nine percent, and the blue, every
> healthy person times one percent.
> Divide everything by ten thousand: counts become shares. *[0.4]* The share can't change.
> These are how common each group is, and these, how often each group tests positive. Name them,
> and you have Bayes' theorem.
> All it does is shrink the sample space to what the evidence allows, then take the share. *[0.9]*

Visual (the one picture): the negatives vanish, the 120 ringed survivors become dots, the header
swaps to "120 people who tested +"; they line up in a 24 × 5 strip, the meter rises to the strip's
row and slides onto it, the yellow outline closes on "these", and the pair rises: the four red
columns sit under the 17 % red segment. The formula is built from the picture:
1. P(sick∣+) from the meter's title; straight brackets count "20" and "100"; their labels fly into
   20 / (20 + 100); the meter's 17 % flies in to "≈ 17%".
2. One move, one sentence: the layout opens once; on "twenty sick people times ninety-nine percent"
   the 20 flies out of the table's people column and the 0.99 off the red arrow (the denominator
   repeats the term in place; the table's 20 positives become 19.8); on "every healthy person times
   one percent" the 9,980 and the 0.01 arrive the same way and the table's 100 becomes 99.8.
3. ÷ 10,000: the people column's header becomes "÷ 10,000"; on "counts" the sick row
   (20 → 0.002, 19.8 → 0.00198) and both 20s in the formula change in one move; on "shares" the
   healthy row (9,980 → 0.998, 99.8 → 0.00998) and the formula's 9,980 (each number rolls out and
   its share rolls in; nothing morphs glyph by glyph). No number in
   the table is left undivided. The 17 % pulses on "the share can't change".
4. Grey braces grow on the spoken words: "how common" under 0.002 and 0.998, "how often" under 0.99
   and 0.01. On "Name them" each number turns into its name in place (0.002 → P(sick), 0.99 →
   P(+∣sick), 0.998 → P(healthy), 0.01 → P(+∣healthy); numerator first; each number's box grows into
   its name's box as one fades into the other, so no glyph is ever half-morphed), the braces stretch with their
   terms and "≈ 17 %" stays at the right end. "Bayes' theorem" above the left side. The braces leave;
   a yellow box on the denominator on "shrink", a red box on the numerator on "take the share"; the
   strip's outline pulses in the 0.9 s pause.

### 6. Consequence: precision, Cardiff 2017 (2:10–3:05)
> Swap the disease for a police watch list.
> For the twenty seventeen Champions League final, about a hundred and seventy thousand people came
> to Cardiff. The watch lists held about twelve hundred photos, so even a small error rate per face
> would swamp the real matches.
> Face-recognition cameras scanned the crowds. *[0.3]* Over four days, they raised two thousand four
> hundred and seventy alerts.
> Shrink to the alerts. Take the red share. The police counted a hundred and seventy-three as
> right: seven percent.
> In machine learning, the share of alerts that are right is called precision.
> Cardiff University's evaluators counted only alerts the logbooks confirmed: three percent.
> Months later, a new algorithm, better photos and practised operators thinned out the false
> alarms, the blue term in Bayes' denominator, and their count rose to forty-six percent.

Visual: the formula and table clear while the meter empties and is retitled in place ("chance an
alert is right ?", ghosted at 30 % like the cold open's meter until it gets its number); in one move the
meter goes to the top right while the strip's 120 people spread out into a 100 × 100 crowd that fades
in around them (the 20 red become listed faces); the legend, docked 0.5 under the meter, starts with
"■ watch list" on "watch list". The grey dateline "Cardiff · Champions League final week, 2017" on
"Champions League final" (it fades once read), "≈ 170,000 people" over the crowd, "■ = 17 people ·
illustration" on "Cardiff"; on "twelve hundred photos" the other 51 listed squares appear (71 in all)
and "· ≤ 1 in 140" joins the first legend line; the crowd brightens and "≤ 1 in 140" pulses on "error
rate per face"; the 71 pulse on "swamp". The yellow beam sweeps: every square it flags grows to the
listed squares' size with a yellow ring (145, 10 of them red); cleared listed squares dim. The 10 red
flagged pulse; the legend steps aside and the 145 file, rings on, one by one into the blocks of a 26 ×
95 raster of exactly 2,470 alerts (red first, then left to right). "Shrink to the alerts": the crowd
fades out, the meter + raster move to the centre and the meter comes up to full strength; straight
red/blue brackets on "red share"; "173 right" / "2,297 wrong"; the meter fills to 7 %, its red segment
over the red columns. On "precision" the title rolls out and "precision" rolls in, a small ghost of the disease
meter appears beside it ("your test", 17 %) and the word is copied under it: "precision too". Then the
ghost leaves, the main bar is tagged "police count / 2,470 alerts", and a second, thin bar below is
tagged the same way, "evaluators' count / final week · 2,632 alerts"; it fills to 3 % on "three
percent", its second tag line becomes "Six Nations 2018 · 48 alerts" on "Months later", and on
"thinned out the false alarms" its blue share shrinks while red grows to 46 %, with a blue
"P(+ ∣ not listed) ↓" appearing under the shrinking blue segment on "the blue term". Citations: BBC
(police figures) for the whole beat, Davies et al. beside it from the watch-list sentence on.

### 7. Landing: the opening, re-seen (3:05–3:36)
> Back to your test. *[1.6, the first frame is re-seen in silence]*
> Your seventeen percent assumes a random screen. Symptoms raise the one in five hundred: at one in
> a hundred, fifty percent; at one in two, ninety-nine, where the rule held. *[1.2]*
> The title's ninety-nine percent is the test's recall: how often the sick test positive. Seventeen
> percent is its precision: how often the positive are sick.

Visual: the raster's outline stays one convex shape while it becomes the + badge's disk (a rounded
rectangle whose sides shrink and corners grow into the circle) and the raster shrinks into it; the
disk fills, then the cross; "you" closes round the landed badge. The meter empties in place and is
retitled "chance you're sick" and slides back while the cold-open diagram re-forms around the + (it
starts re-forming while the Cardiff picture is still leaving, so no frame is empty). In the pause the
first frame is re-seen: each arrow swells into a flow as wide as the people it carries into the +, the
thin 99 % flow labelled "20", the fat 1 % flow "100", with "per 10,000 people" between them. The meter
grows its 17 % on "seventeen percent". On "Symptoms" the naive 99 % marker returns as the climb's target
and the prevalence label goes live: one updater drives label, flows, counts and meter from the same
rounded N: "1 in 100 · 99 / 99 · 50 %" as it is spoken, "1 in 2 · 4,950 / 50 · 99 %" on
"ninety-nine" (the half-sick table of the naive build), on the marker; in the pause it returns to
1 in 500 (20 / 100, 17 %). The fail beat's slider, run backwards. "recall" is written beside the
arrow's 99 % as the red flow pulses, "precision" under the meter on its word, size 34, each underlined;
the finished two-tag frame holds ≈ 2.5 s, fades out, then the end card fades in (they never overprint).

The beats "The police counted…" and "Your seventeen percent…" start with 80 ms of silent pre-roll
(their first word follows a pause).

## Sources
- Manrai, A. K., Bhatia, G., Strymish, J., Kohane, I. S., & Jain, S. H. (2014). Medicine's
  uncomfortable relationship with math: calculating positive predictive value. *JAMA Internal
  Medicine*, 174(6), 991–993. doi:10.1001/jamainternmed.2014.1059 (61 respondents; 14 right; most
  common answer 95 %, 27 of 61).
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
  Both on screen on the evaluators' own bar.
- All other numbers are computed from the stated premises; see facts.md and check.py.
