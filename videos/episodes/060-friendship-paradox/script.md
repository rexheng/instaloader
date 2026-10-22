# Episode 60 — Why Your Friends Have More Friends Than You

**Idea (one sentence):** Following a friendship lands on a person once for every friend she has,
so the average friend has avg(k²)/μ = μ + σ²/μ friends (the cross terms vanish because the
distances from the balance point sum to zero), which is more than the average person whenever friend
counts vary, and epidemiologists can use this to see an outbreak coming.

Runtime 3:3x · 510 words · voice af_heart, speed 0.80, sentence gaps 0.26 s inside a beat and
0.7 s at section boundaries; 0.6 s holds after each new equation row in the algebra (round 3).
Pronunciation override: Christakis → /kɹɪstˈɑkɪs/.

## Palette (one meaning each, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | a person counted once: the girls, the girl average μ, Facebook's average user, the random-student group |
| YELLOW | reached by following a friendship: tokens, the friend average, avg(k²), named friends, the friends' flu curve |
| PURPLE | the spread: distances from the balance point, their squares, σ², σ²/μ (+0.5 for the girls, +445 on Facebook) |
| GRAY | the naive guess (dashed), edges, axes; text-grade gray #9EA5AF (7.3:1) for names, ticks, citations |
| INK | numbers, neutral symbols, emphasis outlines (boxes, the closing outlines) |

The average-friend bar is a YELLOW outline (the friend average) filled BLUE up to μ and PURPLE
beyond it (σ²/μ), so every bar segment has the colour of its term in μ + σ²/μ.

## Beats

### 1. Cold open (0:00–0:13)
> Eight girls at an Illinois high school, and every friendship between them.
> On average, each girl has two and a half friends.
> How many friends does the average friend have? Pick one. *[pause 2.0]*

Visual: frame 0 shows the eight girls (Feld 1991, Fig. 1) at 70 %; they brighten and the
friendships draw in. Counts fly into the BLUE bar "average girl 2.5". The "average friend ?" row
appears; on "average friend" a dashed line drops from the end of the girl bar (2.5) and two ghost
drop lines appear above the axis ticks 3 and 4, each with its candidate written under it in YELLOW
(2.5, 3, 4). On "Pick one" the three candidates pulse in turn, then the hold. The question asks for
a number, so the title's "more" does not answer it.
Citation: Feld, 1991 · Am. J. Sociology · data: Coleman, 1961.

### 2. Stakes (0:13–0:22)
> It matters to health researchers choosing whom to watch for flu: random students, or the friends
> those students name.

Visual: a BLUE ring "random" on Jane; a YELLOW arrow along her friendship to Alice, "named friend".

### 3. Naive build: the guess works on an easy case (0:22–0:44)
> The natural guess is two and a half again: every friend is one of these same eight girls.
> Check that on a rewired class where every girl has two friends. Send a token both ways along every
> friendship.
> Each token reads the friend count where it lands, here always two. Both averages are two: the guess
> holds.

Visual: a GRAY dashed "guess" box grows to 2.5; the ghost lines leave. The girls glide into a ring
labelled "what if: / everyone has 2 / (hypothetical)"; each count rides with its node and changes
2→ without a crossfade. Sixteen tokens fly in 2.5 s (lag 0.04); the counter reads 32/16 = 2.0; the
friend bar fills BLUE exactly to the girl bar.

### 4. Fail (0:44–1:06)
> Now restore the real friendships and send the tokens again. They read one, two, three, or four.
> Twenty tokens add up to sixty: friends average three.
> The guess was half a friend too low. The tokens piled up unevenly: four on Sue, four on Alice,
> one on Betty.

Visual: the ring's friend bar and its readout fade (no count-down through 1.9); the real network
returns while the girl read-out holds 2.0; then the girl bar grows to 2.5 (its read-out swaps while
invisible, so no transient 2.4), the guess tick follows it and the dashed box re-opens leftward from
the tick ("guess ?"). Twenty numbered tokens (0.30 squares, digits 30) fly; tokens on
short edges keep to the right-hand lane so no pair touches. The counter runs to 60/20 = 3.0, the
YELLOW outline overshoots the guess to 3.0 while the dashed box closes onto its right edge, one dashed
tick at 2.5 (no doubled outline); the bar fills BLUE to the tick and PURPLE beyond: "+0.5 · 20%".
(The same collapse happens on the ring at 2.0, where the bar ends exactly on the tick.)
Sue's, Alice's and Betty's tokens pulse as named. Sue's name label now sits up-left of her node.

### 5. Insight (1:06–2:24): the beam, the variance, why the cross terms vanish
> Line the girls up by friend count: two at each count, from one to four, so they balance at two
> and a half.
> The tokens stack higher on the right, one per friend, so they balance at three.
> Sue holds four tokens, each worth four: sixteen. A girl with k friends adds k squared on top, and k
> on the bottom.
> Divide top and bottom by the eight girls: the average of k squared, seven and a half, over the
> average count, two and a half.
> Measure each girl's distance from the balance point and square it: two and a quarter at the ends, a
> quarter in the middle. They average one and a quarter, the variance, sigma squared. *[pause]*
> Split Sue's count, four, into the balance point, two and a half, plus her distance, one and a half.
> Squaring gives two and a half squared, her distance squared, and a cross term. *[pause]* Every
> girl splits this way, and because the beam balances, the left and right distances add to zero and
> the cross terms cancel. *[pause]*
> So the average of k squared is mu squared plus sigma squared, and friends average mu, plus sigma
> squared over mu. Here that's two and a half, plus a half: exactly the extra half friend we
> measured. The ring had no spread, so it had no gap. *[pause 1.3]*

Visual (the one picture): the girls slide onto a beam (0.8 apart), each name riding along to sit
under her node (Text 20); the beam draws once they have settled, with the BLUE fulcrum 2.5.
"The tokens stack": the tokens grow out of their girl layer by layer. Layer 1 is one token per girl,
so it balances where the girls do; from layer 2 a copy of the BLUE fulcrum slides right along the beam,
turning YELLOW, with a live read-out that stops at 2.7 (38/14), 2.9 (52/18) and 3.0 (60/20) as each
layer lands, so the moving balance point is the proof; "three" flashes it with the bar's 3.0.
On "Sue holds four tokens" her stack is boxed and her name flashes. "sum of counts / tokens" becomes
Σk²/Σk. The divide step: Σk²÷8 / Σk÷8 = 60÷8 / 20÷8 → avg(k²)/μ = 7.5/2.5.
Variance (second cycle layout): on "Measure", the stacks leave, the bar panel and the citation go to 0,
the main row parks at 30 % at the bottom centre, and the beam picture moves up and right so the balance
point sits at x = 0: one centred column, picture on top, rows below. PURPLE distances from the BLUE
fulcrum; each girl's distance segment drops to her square's top edge, shrinking to the squares' scale
(tag "sides at 1/4 scale", GRAY Text 18, directly under the squares), then the square grows down from
it; the area labels 2.25 / 0.25 fly along the tag's row into σ² = 10/8 = 1.25, which sits beside the
squares it averages.
The cross-term step (centred row under the picture): 4² = (2.5 + 1.5)²; Sue's 4 flies down from her
node (threading between the labels and squares) and 1.5 from her distance label; on "her distance"
PURPLE "d = k − μ" is written beside the beam → 4² = 2.5² + 1.5² + 2·2.5·1.5 (cross term INK-boxed) →
averaged over the eight girls (all nodes flash): avg(k²) = μ² + σ² + 2μ·avg(d). The distance labels gain
signs; on "add to zero" they merge into a PURPLE 0 under the balance point, that 0 drops between the
middle squares to replace avg(d) and the box shrinks around 2μ·0; on "cancel" the boxed term leaves.
On "So" the parked main row brightens and its numerators are rebuilt from the identity (μ² + σ² copied
down; 2.5 from the denominator, 1.25 from the variance row). From here every row is typeset by TeX as
one formula, so μ sits on TeX's baseline. The split moves each term to exactly one place; the second
bar and denominator rise in after (no stacked copies). μ²/μ is boxed and cancelled, 2.5²/2.5 → 2.5,
1.25/2.5 → 0.5.
On "exactly the extra half friend we measured" the picture moves back left, the bars and citation
return, the result row moves under the bars, and its 0.5 flashes with the PURPLE bar segment.
The ring: the class picture, the row and the bars dim to 30 %; a 0.55× thumbnail of the 0:31 ring
(digits 32) appears lower left; on "no spread" a copy of the PURPLE distance line collapses into a
point at its centre; on "no gap" μ + σ²/μ is copied beside it as 2 + 0/2 = 2. The bars never change
(round 1 showed 2.0 / 2.0 beside a beam reading 2.5 and 3). Everything brightens in the closing pause.

### 6. General case + prediction (2:24–2:46)
> In twenty eleven, Facebook users averaged about a hundred and ninety friends. If every friendship
> sent tokens, what would the tokens average? *[pause 1.6]*
> About six hundred and thirty five. A few users had thousands of friends, so the spread term is more
> than twice the mean itself.

As 635 lands the bar fills BLUE to 190 and PURPLE beyond ("+445"). On "A few users" the axis
breaks and runs on to a "5,000" tick tagged "Facebook's limit", and a BLUE brace labelled "a few users"
spans that stretch (a range, not plotted dots). On "spread term" the PURPLE segment flashes and the row
builds.

Visual: the beam and the algebra leave; the bar panel scales 1.25× and moves to the centre (one
focal point); μ + σ²/μ slides under it. Labels change to "average user", the axis to 0–800; the
YELLOW outline grows to 635, fills BLUE to 190 and PURPLE beyond ("+445"); the row becomes
μ + σ²/μ = 190 + 445 = 635, each number copied from its bar label.
Citation: Ugander et al., 2011 · arXiv:1111.4503.

### 7. Payoff
> In twenty oh nine, Christakis and Fowler put this to work at Harvard. Named friends have more
> friends, so they sit closer to everyone else, and should catch flu first. They tracked flu diagnoses
> in three hundred nineteen random students and four hundred twenty five friends they named. The
> friends' curve rose first: fitted curves put them thirteen point nine days ahead. With self-reported
> symptoms, the lead shrank to about three.

Visual: the Facebook numbers leave with their axis; the axes build while each Facebook bar flies to
the origin of the curve it becomes. The calendar starts on "work". "friends they named" (YELLOW) rises
in on "Named friends" and flashes on "more friends"; "319 random students" and the "425" arrive as
spoken (C&F Fig. 3, redrawn). Flash along the friends' curve on "rose first". Dashed logistic fits
(shared shape refit in sim.py, shift held at C&F's 13.9 days) with the raw steps dimmed; an INK arrow
between the fits at 2.8 %; a copy arcs up into the read-out above the plot, "C&F fitted lead: 13.9
days" left of it (0.3 below and 0.4 left of round 1's spot, off the safe edge). On "self-reported" a
GRAY copy drops into the row below; on "shrank" it shrinks, tip fixed, while a live number reads its
length, ending at "3.2 days".
Citation: Christakis & Fowler, 2010 · PLoS ONE · Fig. 3 redrawn, logistic refit.

### 8. Landing
> Back to the eight girls. Seat by seat, five have fewer friends than their friends average; only Sue
> and Alice have more.
> Betty looks at her one friend and sees four. Two and a half counts the girls; three counts the
> friendships.

Visual: the chart dissolves into the cold-open frame itself: the network, "average girl 2.5", and
"average friend ?" with the drop lines and the YELLOW candidates 2.5 / 3 / 4 from 0:11. On "Seat by
seat", INK outlines and each girl's friends' average in YELLOW (4, 3.5, 3.33, 3.33, 2); Sue and Alice
get 2.75 and 3. On "Betty looks" the other labels leave, Betty's 4 stays; on "sees four" the Betty–Sue
edge brightens and Sue's 4 pulses. "Two and a half counts the girls": the girl bar, its 2.5 and the
2.5 candidate flash BLUE. "three counts the friendships": every friendship flashes, the "?" and drop
lines leave, the friend bar grows (YELLOW outline, BLUE to 2.5, PURPLE beyond) to the 3, which slides
to the bar's end and is ringed; the 4 dims. End card. (Second cycle: no second token flight, no 4× / 1×
tally.)

## Sources
- Feld, S. L. (1991). Why your friends have more friends than you do. *American Journal of Sociology*
  96(6), 1464–1477. (Network data from Coleman, J. S., 1961, *The Adolescent Society*.)
- Ugander, J., Karrer, B., Backstrom, L., & Marlow, C. (2011). The anatomy of the Facebook social
  graph. arXiv:1111.4503.
- Christakis, N. A., & Fowler, J. H. (2010). Social network sensors for early detection of contagious
  outbreaks. *PLoS ONE* 5(9), e12948. Figure 3 redrawn under CC BY 4.0.
