# Episode 60 — Why Your Friends Have More Friends Than You

**Idea (one sentence):** Following a friendship lands on a person once for every friend she has,
so the average friend has avg(k²)/μ = μ + σ²/μ friends (the cross terms vanish because the
distances from the balance point sum to zero), which is more than the average person whenever friend
counts vary, and epidemiologists can use this to see an outbreak coming.

Runtime 3:41 · 560 words · voice af_heart, speed 0.82, sentence gaps 0.26 s inside a beat and
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
> The guess was half a friend too low: friends average twenty percent more than girls. The tokens
> piled up unevenly: four on Sue, four on Alice, one on Betty.

Visual: the ring's friend bar and its readout fade (no count-down through 1.9); the real network
returns; twenty numbered tokens (0.30 squares, digits 30) fly; tokens on
short edges keep to the right-hand lane so no pair touches. The counter runs to 60/20 = 3.0, the
YELLOW outline overshoots the dashed guess to 3.0, fills BLUE to 2.5 and PURPLE beyond: "+0.5 · 20%".
Sue's, Alice's and Betty's tokens pulse as named. Sue's name label now sits up-left of her node.

### 5. Insight (1:06–2:24): the beam, the variance, why the cross terms vanish
> Line the girls up by friend count: two at each count, from one to four, so they balance at two
> and a half.
> The tokens stack higher on the right, one per friend, so they balance at three.
> Sue holds four tokens, each worth four: sixteen. A girl with k friends adds k squared on top, and k
> on the bottom. Sixty over twenty.
> Divide top and bottom by the eight girls: the average of k squared, seven and a half, over the
> average girl, two and a half.
> Measure each girl's distance from the balance point and square it: two and a quarter at the ends, a
> quarter in the middle. They average one and a quarter, the variance, sigma squared. *[pause]*
> Split Sue's four into the balance point, two and a half, plus her distance, one and a half.
> Squaring gives two and a half squared, her distance squared, and a cross term. *[pause]* Every
> girl splits this way, and because the beam balances, the left and right distances add to zero and
> the cross terms cancel. *[pause]*
> So the average of k squared is mu squared plus sigma squared, and friends average mu, plus sigma
> squared over mu. Here that's two and a half, plus a half: exactly the extra half friend we
> measured. The ring had no spread, so it had no gap. *[pause 1.3]*

Visual (the one picture): the girls slide onto a beam (0.8 apart), each name riding along to sit
under her node (Text 20); the beam draws once they have settled, with the BLUE fulcrum 2.5, token stacks, YELLOW fulcrum 3. On "Sue holds four
tokens" her stack is boxed and her name flashes. "sum of counts / tokens" becomes Σk²/Σk (label swaps leave upward, then the new label
rises). The divide step: Σk²÷8 / Σk÷8 = 60÷8 / 20÷8 → avg(k²)/μ = 7.5/2.5 (written `avg(k²)`,
never k̄², which would read as μ²). The variance: PURPLE distances from the BLUE fulcrum; each
girl's distance segment drops to her square's top edge, visibly shrinking to the squares' scale
(tag "square side = distance, drawn at 1/4 scale"; exactly ¼), then the square grows down from it;
the area labels 2.25 / 0.25 themselves fly into σ² = 10/8 = 1.25 (no copies, so no doubled glyphs;
the tag, beside the squares, fades before their flight crosses it). The bar panel dims to 25 %.
In the hold after "sigma squared" the token stacks, Sue's box and "4×4=16" leave, the old main row
fades out, and the whole beam picture lifts 1.6 units into the freed band (one focal point; the
lower-left band is now free).
The cross-term step (right panel, its own row): 4² = (2.5 + 1.5)² with 4 copied from Sue's node
(her name flashes) and 1.5 from her distance label; on "her distance" PURPLE "d = k − μ" is written
above the distance line, so avg(d) has a referent → 4² = 2.5² + 1.5² + 2·2.5·1.5 (cross term INK-boxed) → averaged over
the eight girls (all nodes flash): avg(k²) = μ² + σ² + 2μ·avg(d). The distance labels gain signs
(−1.5, −0.5, +0.5, +1.5); on "add to zero" the four signed labels merge into a PURPLE 0 under the
balance point, that 0 flies up to replace avg(d) and the box shrinks around 2μ·0; on "cancel" the
boxed term leaves: avg(k²) = μ² + σ².
On "So" the main row avg(k²)/μ = 7.5/2.5 = 3.0 returns where it stood and its numerators are
rebuilt from the identity (μ² + σ² copied down; 2.5 from the denominator, 1.25 from the variance
row): (μ²+σ²)/μ = (2.5²+1.25)/2.5 = 3.0, then split (the variance row leaves), μ²/μ boxed and
cancelled (box, square and denominator leave; μ slides), 2.5²/2.5 → 2.5 (the identity row leaves),
1.25/2.5 → 0.5, flashing with the PURPLE bar segment.
The ring: a 0.42× thumbnail of the 0:31 ring appears in the freed lower-left band; on "no spread"
a copy of the PURPLE distance line collapses into a point at its centre; on "no gap" the bars meet
at 2.0 and 2.0 (the PURPLE segment and "+0.5 · 20%" vanish) and μ + σ²/μ is copied beside the ring
as 2 + 0/2 = 2. In the closing pause the bars return to 2.5 and 3.0.

### 6. General case + prediction (2:24–2:46)
> In twenty eleven, Facebook users averaged about a hundred and ninety friends. If every friendship
> sent tokens, what would the tokens average? *[pause 1.6]*
> About six hundred and thirty five. A few users had thousands of friends, so the spread term is more
> than twice the mean itself.

(round 3) As 635 lands the bar fills BLUE to 190 and PURPLE beyond ("+445"). On "A few users" four
BLUE dots ("a few users") slide along the axis past 800, through a break, toward a tick "5,000"
tagged "Facebook's limit". On "spread term" the PURPLE segment flashes and the row builds.

Visual: the beam and the algebra leave; the bar panel scales 1.25× and moves to the centre (one
focal point); μ + σ²/μ slides under it. Labels change to "average user", the axis to 0–800; the
YELLOW outline grows to 635, fills BLUE to 190 and PURPLE beyond ("+445"); the row becomes
μ + σ²/μ = 190 + 445 = 635, each number copied from its bar label.
Citation: Ugander et al., 2011 · arXiv:1111.4503.

### 7. Payoff (2:46–3:18)
> In twenty oh nine, Christakis and Fowler tested this at Harvard. Friends sit closer to everyone
> else in the network, so they should catch it first. They tracked flu diagnoses in three hundred
> nineteen random students and four hundred twenty five friends they named. The friends' curve rose
> first: fitted curves put them thirteen point nine days ahead. With self-reported symptoms, the lead
> shrank to about three.

Visual (round 3): the Facebook numbers leave with their axis; the axes build while each Facebook
bar flies straight to the origin of the curve it becomes (no legend over the Harvard chart). From
"tested" the step curves grow (BLUE → random students, YELLOW → friends) on one shared calendar;
the group labels rise in as each number is spoken (C&F Fig. 3, redrawn). Flash along the friends'
curve on "rose first". Dashed logistic fits (shared shape refit in sim.py, shift held at C&F's 13.9
days) with the raw steps dimmed; an INK arrow between the fits at 2.8 %; a copy lifts into a
read-out above the plot, "C&F fitted lead: 13.9 days" left of it. On "self-reported" a GRAY copy
drops into the row below with "self-reported:"; on "shrank" it shrinks, tip fixed, while a live
number beside it reads its length, ending at "3.2 days".
Citation: Christakis & Fowler, 2010 · PLoS ONE · Fig. 3 redrawn, logistic refit.

### 8. Landing (3:18–3:45)
> Back to the eight girls. Five have fewer friends than their friends average, and only Sue and Alice
> have more.
> Follow any friendship, yours included, and you land on a Sue four times as often as on a Betty. So
> Betty looks at her one friend and sees four. From most seats in this class, the view is the same.

Visual: the chart dissolves into the cold-open frame, now answered (friend bar 2.5 BLUE + 0.5
PURPLE, YELLOW outline, "3.0"). On "Five", INK outlines and each girl's friends' average in YELLOW
(4, 3.5, 3.33, 3.33, 2); Sue and Alice get 2.75 and 3. Then all twenty tokens fly once more; every
token except Sue's four and Betty's one dims to 30 %; on "a Sue" Sue's four pulse and a tally row
"Sue ■■■■ 4×" appears in the empty right panel, on "a Betty" Betty's one pulses and "Betty ■ 1×"
appears under it. On "Betty looks" Betty's node takes a thick INK outline; on "sees four" Sue's 4 pulses;
on "most seats" Jane, Pam, Dale and Tina take the same outline: the five seats from which friends
look more popular. End card.

## Sources
- Feld, S. L. (1991). Why your friends have more friends than you do. *American Journal of Sociology*
  96(6), 1464–1477. (Network data from Coleman, J. S., 1961, *The Adolescent Society*.)
- Ugander, J., Karrer, B., Backstrom, L., & Marlow, C. (2011). The anatomy of the Facebook social
  graph. arXiv:1111.4503.
- Christakis, N. A., & Fowler, J. H. (2010). Social network sensors for early detection of contagious
  outbreaks. *PLoS ONE* 5(9), e12948. Figure 3 redrawn under CC BY 4.0.
