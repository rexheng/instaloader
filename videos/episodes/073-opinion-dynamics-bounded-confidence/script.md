# 073 · How Open-Minded People Split Into Camps

**One idea:** if people only average with others within a listening range epsilon, the web of who-hears-whom tears itself apart, so a population of pure compromisers freezes into about one-over-two-epsilon camps instead of reaching consensus.

All opinion data on screen is **simulated** (`sim.py` -> `data.json`, seed 32 for the 100-person run). Labelled "simulated" on screen.

## Palette (colour -> one meaning)

| Colour | Meaning |
|---|---|
| BLUE | people under the listening-range rule (dots, threads, camps, our measured counts) |
| PURPLE | people in DeGroot's fixed-web model |
| YELLOW | epsilon, the listening range, and everything sized by it (windows, two-epsilon bands, the one-over-two-epsilon rule) |
| RED | gaps between camps that nobody can hear across |
| INK / GRAY | text, axes; INK rings = Hegselmann & Krause's published runs |

## Narration (beat by beat)

**1 · Cold open (0:00-0:14)** *100 dots on a horizontal opinion line 0..1; a yellow window of +-0.1 around one person; an arrow to the window's average.*
A hundred people, with opinions from zero to one. Each round, everyone moves to the average of everyone within point one of them. Repeat until nobody moves. How many different opinions survive? [pause 1.5]

**2 · Stakes (0:14-0:24)** *The line swings upright into an opinion axis; two copies, two panels.*
Nobody here is stubborn, and nobody is extreme. Rules like this are how modelers ask when a group that keeps compromising reaches consensus, and when it splits into camps.

**3 · Naive build (0:24-0:44)** *Left panel, purple braid; live spread number; citation DeGroot 1974.*
The obvious answer is one. In nineteen seventy four, Morris DeGroot proved that people who keep averaging over a fixed web of trust that links everyone always reach consensus. Here it is, simulated: each person trusts five random others, plus themselves. The spread, from the highest opinion to the lowest, shrinks every round to almost nothing.

**4 · Fail (0:44-0:58)** *Right panel, blue braid from the same start; spread freezes at 0.74; brace "4 camps".*
Now run our rule on the same hundred starting opinions. The spread falls from point nine nine to point seven four, and freezes. Four camps, and they never move again. We predicted one. We got four.

**5 · Cause (0:58-1:18)** *Right panel grows; red gap markers 0.20, 0.23, 0.31 between final camps; yellow window around a camp.*
The difference is the web. DeGroot's is fixed. Here, who you listen to depends on where you stand. Every gap between these final camps is wider than point one, so no one in one camp can hear anyone in the next. If any gap were narrower, those two camps would still be pulling on each other.

**6 · Insight (1:18-1:52)** *Each camp's threads traced back to round zero; yellow brackets for its starting band; the 0..1 axis cut into bands of width two epsilon; formula built from the axis and one band; citation Deffuant 2000.*
So how many camps should you expect? Call the listening range epsilon. Trace each camp back to where its members started. Each one gathered a band about two epsilon wide: roughly everyone within epsilon of its centre, on either side. Cut the line from zero to one into bands of width two epsilon, and you get one over two epsilon camps. Here, that predicts five. [pause 0.8] We counted four.

**7 · Measure (1:52-2:25)** *Log-log chart: yellow line one over two epsilon; blue dots, simulated means; the 0.25 point flagged.*
Is that close enough? Here are listening ranges from point oh one to point three, each run twenty times with six hundred and twenty five simulated people. Both axes are logarithmic, so the rule is this straight yellow line. The real counts run parallel, at about three quarters of the rule, because most camps gather a bit more than two epsilon. And at point two five, the rule still promises two camps, while almost every run ends in one.

**8 · Payoff (2:25-2:55)** *Three INK rings on the chart; citation Hegselmann & Krause 2002 · JASSS.*
That set-up is Hegselmann and Krause's, from two thousand two: six hundred and twenty five random opinions. With a range of point oh one, thirty eight opinions survived. At point one five, two camps. At point two five, consensus. Each of their single runs falls inside what our twenty runs produced. These are models, and how closely real people update this way is still thinly tested.

**9 · Landing (2:55-3:10)** *Back to the opening line; dots slide to their four final opinions; a yellow window around each camp reaches no one else.*
Back to the first picture. Every one of these hundred people compromised, every round. The four camps were settled the moment we chose how far they would listen.

## Sources
- DeGroot, M. H. (1974). Reaching a Consensus. *JASA* 69(345):118-121.
- Hegselmann, R. & Krause, U. (2002). Opinion Dynamics and Bounded Confidence: Models, Analysis and Simulation. *JASSS* 5(3):2.
- Deffuant, G., Neau, D., Amblard, F. & Weisbuch, G. (2000). Mixing beliefs among interacting agents. *Advances in Complex Systems* 3:87-98 (origin of the "1/2d rule", named in Weisbuch 2001, arXiv:cond-mat/0111494).
