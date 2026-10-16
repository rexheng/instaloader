# Episode 60 — fact sheet

Every number spoken or shown, how it was checked, and where it comes from. `sim.py` recomputes the
network numbers exactly (fractions); `cf_fig3_digitized.json` holds the redrawn Harvard data.

## The eight girls (cold open, naive build, insight, landing)

| Claim | Check | Source |
|---|---|---|
| The network is real: 8 girls, 10 reciprocated friendships, in "Marketville", one of the high schools in Coleman's study. Names are Feld's (fictitious). | Read in the paper: "the set of relationships depicted in figure 1, found among eight girls in 'Marketville,' one of the high schools included in the study. The names are fictitious." Fig. 2 caption: "Network of reciprocated friendships among Marketville girls ... (From *The Adolescent Society* by James S. Coleman, 1961)". | Feld, S. L. (1991). Why your friends have more friends than you do. *American Journal of Sociology* 96(6): 1464–1477. |
| Edges: Betty–Sue, Sue–Alice, Sue–Dale, Sue–Pam, Alice–Jane, Alice–Pam, Alice–Dale, Jane–Dale, Pam–Carol, Carol–Tina. | Reconstructed from Feld's text ("Betty's only friend, Sue"; "Jane's two friends, Dale and Alice"; "Dale's three friends, Sue, Alice, and Jane"; "Sue's friends, Dale, Alice, Pam, and Betty") and Table 1 (each girl's count and her friends' total). The reconstruction reproduces every row of Table 1 exactly (sim.py). | Feld 1991, Fig. 1, Table 1 |
| Friend counts 1,4,4,2,3,3,2,1 (Betty, Sue, Alice, Jane, Pam, Dale, Carol, Tina); 20 friend slots; mean **2.5**. | Table 1: total 20, "Mean 2.5* (*for eight girls)". sim.py: 20/8 = 5/2. | Feld 1991, Table 1 |
| Average over friends = **3** (60 over 20). | Table 1: friends' friends total 60, "Mean 3† († for 20 friends)". Text: "a total of 20 friends ... having a total of 60 friends, with a mean of 3.0 friends per friend." sim.py: Σk² = 60, Σk = 20. | Feld 1991, p. 1467 |
| Feld's general formula: mean friends of friends = Σx²/Σx = mean + variance/mean. | Quoted from Feld p. 1469–70 and footnote 4. Derivation: Σk²/Σk = (Σk²/n)/(Σk/n) = (μ² + σ²)/μ with population variance σ² = Σk²/n − μ². | Feld 1991 |
| "Divide top and bottom by the eight girls": 60/20 → (60÷8)/(20÷8) → 7.5/2.5; the bottom is the girl average μ = 2.5, the top is the average of k², 7.5. | 60/8 = 7.5, 20/8 = 2.5 (sim.py). | computed |
| Variance as a picture: each girl's distance from the balance point 2.5 is 1.5 (counts 1 and 4) or 0.5 (counts 2 and 3); squared, 2.25 for the four girls at the ends, 0.25 for the four in the middle; they sum to 10 and average 10/8 = **1.25** = σ² (population variance). On screen the squares are drawn at 0.43 units per friend of distance (a separate scale from the beam); areas are labelled. | sim.py "squared distances" line: sum 10, mean 5/4; check 2.5² + 1.25 = 15/2 = mean of k² = 60/8. | computed |
| "seven and a half is exactly two and a half squared, plus that variance"; 2.5 + 1.25/2.5 = 2.5 + 0.5 = 3. | 6.25 + 1.25 = 7.5; 1.25/2.5 = 0.5. Displayed chain: (μ²+σ²)/μ = (2.5²+1.25)/2.5 → μ²/μ + σ²/μ = 2.5²/2.5 + 1.25/2.5 → μ + σ²/μ = 2.5 + 0.5 = 3.0, every state exact. | computed |
| The naive guess (2.5) is "half a friend too low, off by twenty percent". | 3 − 2.5 = 0.5; 0.5/2.5 = 20 %. | computed |
| Two girls at each count 1, 2, 3, 4; token columns 2, 4, 6, 8. | sim.py histogram {1:2, 2:2, 3:2, 4:2}; k·n_k = {2,4,6,8}. | computed |
| "Sue holds four tokens, each worth four: sixteen." | Sue has 4 friends, so she is named on 4 lists; 4 × 4 = 16. | computed |
| Five girls (Betty, Jane, Pam, Dale, Tina) have fewer friends than the average among their own friends; Sue and Alice have more; Carol is equal. | Feld: "Of the eight girls, five (Betty, Jane, Pam, Dale, and Tina) have fewer friends than the average among their friends, while only two (Sue and Alice) have more ... one (Carol) has as many". sim.py reproduces it. | Feld 1991, p. 1465 |
| Landing labels (YELLOW, "her friends' average"): Betty 4, Jane 3.5, Pam 3.33, Dale 3.33, Tina 2; Sue 2.75, Alice 3. | sim.py per-girl friends' mean: Betty 4/1; Jane (4+3)/2 = 3.5; Pam (4+4+2)/3 = 10/3; Dale (4+4+2)/3 = 10/3; Tina 2/1; Sue (1+4+3+3)/4 = 2.75; Alice (4+2+3+3)/4 = 3; Carol (3+1)/2 = 2 (equal, not labelled). A round-1 critic suggested 2.5 and 3.25 for Sue and Alice; those are wrong, the recomputed 2.75 and 3 are shown. 10/3 is shown rounded as 3.33. | Feld 1991 Fig. 1 / Table 1, recomputed |
| "Sue is on four friend lists, Betty on one. Follow any friendship ... you land on a Sue four times as often as on a Betty." | Following a uniformly random friendship end lands on a girl with probability k/Σk: Sue 4/20, Betty 1/20, a ratio of 4. Each girl receives one token per friend (4 on Sue, 1 on Betty), which is what the tokens show. | computed |
| "an Illinois high school" (narration since round 1; the era was cut to bring the prediction forward, the date context stays in the on-screen "data: Coleman, 1961") | Coleman's survey covered 10 high schools in northern Illinois, data collected 1957–1958 (GESIS archive ZA1196: "schoolchildren in 10 selected High Schools in Northern Illinois", 1957–1958); Marketville is one of the study's schools. Round 2 re-check (a critic noted Feld's text mentions 12 schools): the review of the book in *Psychoanalytic Quarterly* 32 (PEP, PAQ.032.0126A) says "Ten high schools in northern Illinois", and Brookings' 2017 Brown Center Report says "In the fall of 1957, James Coleman began surveying students in 10 high schools in northern Illinois". The count is not spoken or shown; "an Illinois high school" is true either way. | Coleman 1961; GESIS ZA1196; PEP review; Brookings 2017 |
| "every friendship between them" | Feld's networks are *reciprocated* (mutual) choices (Fig. 2 caption); Fig. 1 shows all ties among the eight. | Feld 1991 |

The ring ("rewire the class so every girl has two friends") is a hypothetical, labelled "what if" on
screen: 8 nodes, 8 edges, every count 2, Σk²/Σk = 32/16 = 2 = μ, σ² = 0.

Pitfall respected: the paradox is about **averages**. The script says "friends average three" and, at
the end, that five of eight have fewer friends than their friends' average while Sue and Alice have
more, so it never claims every individual is outnumbered.

## Facebook (general case, prediction pause)

| Claim | Check | Source |
|---|---|---|
| "On Facebook in twenty eleven, users averaged about a hundred and ninety friends." | arXiv text: measurements in May 2011, ~721 million active users, 68.7 billion friendship edges, "so the average Facebook user in our study had around 190 Facebook friends." 2 × 68.7e9 / 721e6 = 190.6. | Ugander, Karrer, Backstrom & Marlow (2011), *The Anatomy of the Facebook Social Graph*, arXiv:1111.4503 |
| Their friends averaged "about six hundred and thirty five". | arXiv text: "The expected number of friends at the end of a randomly chosen edge, ⟨k²⟩/⟨k⟩ = 635". This is exactly the token average of the episode (Σk²/Σk). | Ugander et al. 2011 |
| "A few users had thousands of friends." | arXiv text: "a much smaller population have many hundreds or even thousands of friends"; 5,000-friend cap. | Ugander et al. 2011 |
| "the spread term is more than twice the mean itself"; 190 + 445 = 635 on screen. | σ²/μ = 635 − 190.6 = 444.4 ≈ 445 > 2 × 190 = 380. Implied σ² ≈ 84,700, σ ≈ 291 (not shown). | computed from the paper's numbers |

## Harvard flu sensors (payoff)

| Claim | Check | Source |
|---|---|---|
| Christakis and Fowler, study run at Harvard in 2009 (Sept 1 – Dec 31). | PLoS ONE full text. | Christakis, N. A. & Fowler, J. H. (2010). Social Network Sensors for Early Detection of Contagious Outbreaks. *PLoS ONE* 5(9): e12948. doi:10.1371/journal.pone.0012948 |
| "More friends means more ways to catch flu, so the friends should get sick first." (the mechanism, added in round 1) | C&F's own rationale: Fig. 1 caption, "central individuals are likely to be infected sooner because they lie a shorter number of steps (on average) from all other individuals in the network"; the introduction motivates the friend sample by the friendship paradox (friends of random people have more contacts, so are more central). Re-read on journals.plos.org, Oct 2026. | C&F 2010, Introduction and Fig. 1 caption |
| 319 randomly chosen students; 425 friends those students named. | "(1) a sample chosen randomly from the 6,650 Harvard undergraduates (N = 319), and (2) a 'friends' sample (N = 425) composed of individuals who were named as a friend at least once by a member of this random sample." | C&F 2010, Methods |
| "The steps are flu diagnoses by medical staff." | Fig. 3 left panel: NPMLE of cumulative flu incidence "based on diagnoses by medical staff". Redrawn by digitizing the published figure (PLoS ONE is CC BY 4.0): step heights quantize exactly to whole cases (1/425 and 1/319). Totals: friends 32/425 = 7.5 %, random 25/319 = 7.8 %, overall 57/744 = 7.7 %, matching the paper's "cumulative incidence ... 8% based on diagnoses". Day positions ±1 day. | C&F 2010, Fig. 3 (left) |
| "the fitted curves put the friends thirteen point nine days ahead" (on screen: "fitted lead: 13.9 days") | Abstract: "the progression of the epidemic in the friend group occurred 13.9 days (95% C.I. 9.9–16.6) in advance of the randomly chosen group"; Methods: "we fit the observed probability of flu to a cumulative logistic function via nonlinear least squares (NLS)". **Round 1 change:** the arrow is no longer drawn on the raw steps at a chosen height (a round-1 critic correctly noted the raw gap varies from about 30 days to about 1 day with height). The dashed curves are a cumulative logistic c/(1+e^(−(t−m)/s)) with shared c and s and the random group shifted by the published 13.9 days; c = 8.320 %, m = 52.79 d, s = 21.86 d are least-squares fitted to the redrawn step curves (sim.py). Letting the shift float in the same fit gives 14.5 days, inside C&F's 95 % CI, so the redrawn data agree with the published fit. Because the two fits are a pure shift, their horizontal gap is 13.9 days at every height; the arrow sits at 2.8 % (fits at day 38.0 and 51.9), the height where it clears the raw steps by ≥ 0.2 units. The raw steps are dimmed to 45 % when the fits appear. | C&F 2010; refit in sim.py |
| "With self-reported symptoms, the lead shrank to about three." | "a significant but smaller shift in self-reported flu symptoms (3.2 days, 95% C.I. 2.2–4.3)". | C&F 2010, Results |
| Friends are more central (why the curve moves). | "The friend group was observed to have significantly higher measured in-degree and betweenness centrality than the random group." | C&F 2010, Fig. 3 caption |

Note: the arXiv preprint (1004.4792) reports 14.7 days; the peer-reviewed PLoS ONE number, 13.9, is
the one used. C&F also caution that "the amount of lead time will depend on features of the outbreak
and the network at hand"; the episode's honest limit is the self-report result.

## On-screen presentation checks (round 1)

- Text-grade gray for names, ticks, axis titles and citations is #9EA5AF, 7.3:1 on the background (the series GRAY #8B939E, 5.8:1, is kept for lines only).
- The ring is labelled "what if: / everyone has 2 / (hypothetical)" and the Feld/Coleman citation is dimmed to 25 % while it is on screen, restored when the real friendships return.
- Colour semantics of the bars: the average-friend bar is a YELLOW outline (the friend average) filled BLUE up to the girl average μ and PURPLE beyond it (σ²/μ), so μ is blue in both the bar and the equation; the same holds for Facebook (190 blue + 445 purple = 635 yellow).

## Round 2 additions (every new number and claim)

| Claim (spoken or on screen) | Check | Source |
|---|---|---|
| Hook: "How many friends does the average friend have?" with candidate stops 2.5, 3, 4 | "The average friend" is Feld's average over the 20 friend slots (Table 1, "Mean 3†, † for 20 friends"), i.e. the token average Σk²/Σk = 60/20 = 3.0. The candidates are the naive answer (2.5) and two alternatives; 3 is the answer paid off at 1:0x. | Feld 1991, Table 1 |
| "The guess was half a friend too low: friends average twenty percent more than girls." (round 1 said "off by twenty percent", whose baseline was ambiguous: 0.5/3 = 16.7 %) | 3.0/2.5 = 1.20, so the friend average is 20 % more than the girl average; on screen "+0.5 · 20%" sits on the purple excess over the 2.5 fill. | computed |
| "the average of k squared" is written avg(k²) on screen (round 1 used an overline on k², which reads like k̄² = μ²) | avg(k²) = 60/8 = 7.5; μ² = 6.25; they differ by σ² = 1.25. | computed |
| Squares "at ¼ scale" | Beam: 1.52 units per friend. Squares: SQ_SCALE = 1.52/4 = 0.38 units per friend of distance, so the 1.5 distance becomes a 0.57-unit side and the 0.5 distance a 0.19-unit side. Each distance segment is copied down and visibly shrinks to that length before its square grows. Areas are labelled in friends² (2.25, 0.25). | scene.py |
| "Split Sue's four into the balance point, two and a half, plus her distance, one and a half." On screen 4² = (2.5 + 1.5)² | 2.5 + 1.5 = 4. | computed |
| "Squaring gives two and a half squared, her distance squared, and a cross term." On screen 4² = 2.5² + 1.5² + 2·2.5·1.5 | 6.25 + 2.25 + 7.5 = 16 = 4². | computed |
| "Every girl splits this way": avg(k²) = μ² + σ² + 2μ·avg(d) | For each girl k = μ + d with d = k − μ, so k² = μ² + d² + 2μd. Averaging over the 8 girls: avg(k²) = μ² + avg(d²) + 2μ·avg(d), and avg(d²) is the population variance σ² (the squares just averaged). | algebra |
| "because the beam balances, the left and right distances add to zero and the cross terms cancel." On screen the distance labels become −1.5, −0.5, +0.5, +1.5 and a 0 appears under the balance point; avg(d) → 0. | Two girls at each count: 2(−1.5 − 0.5 + 0.5 + 1.5) = 0. In general Σ(k − μ) = Σk − nμ = 0 by the definition of μ, which is exactly the condition for the beam (equal weights at positions k) to balance at μ. Hence avg(k²) = μ² + σ² = 6.25 + 1.25 = 7.5 ✓. | algebra; sim.py |
| Main row: (μ² + σ²)/μ = (2.5² + 1.25)/2.5 = 3.0 → μ²/μ + σ²/μ → μ + σ²/μ = 2.5 + 0.5 = 3.0 | 7.5/2.5 = 3; 6.25/2.5 = 2.5; 1.25/2.5 = 0.5. Every displayed state is exact. | computed |
| "If every friendship sent tokens, what would the tokens average?" → "About six hundred and thirty five" (round 1 asked "How many friends did their friends average?", which could mean the per-user average of friends' averages, a different statistic) | A token sent along each direction of each edge reads the receiver's degree; the token average is Σk²/Σk = ⟨k²⟩/⟨k⟩, which Ugander et al. report as "The expected number of friends at the end of a randomly chosen edge, ⟨k²⟩/⟨k⟩ = 635". | Ugander et al. 2011 |
| On screen: μ + σ²/μ = 190 + 445 = 635 | 190 + 445 = 635; σ²/μ = 635 − 190.6 = 444.4 ≈ 445 with the paper's rounded 190. | computed |
| C&F read-out: "fitted lead: 13.9 days" beside an arrow 13.9 days long; "self-reported: 3.2 days" beside an arrow 3.2 days long | Both read-out arrows are drawn at the chart's own day scale (units per day from the x axis), tips aligned, so their lengths compare honestly; the 13.9-day one is a copy of the arrow drawn between the two fits at 2.8 %. 13.9 (95 % CI 9.9–16.6) for diagnosed flu; 3.2 (95 % CI 2.2–4.3) for self-reported symptoms. | C&F 2010, Abstract and Results |
| "So Betty looks at her one friend and sees four." | Betty's only friend is Sue (Feld: "Betty's only friend, Sue"), and Sue has 4 friends. | Feld 1991 |
| "From most seats in this class, the view is the same." Five nodes (Betty, Jane, Pam, Dale, Tina) take thick outlines | 5 of the 8 girls have fewer friends than the average among their own friends (Feld p. 1465); "most" = 5/8. | Feld 1991 |
| Closing "4×" and "1×" | Sue receives 4 of the 20 tokens, Betty 1: a uniformly random friendship end is Sue with probability 4/20 and Betty with 1/20, a ratio of 4. | computed |

Layout (round 2 cap): `scene.py` now calls `assert_token_clearance()` before rendering (and `python
scene.py` runs it alone). It places every token at its parked position (both directions of all 10
real edges and all 8 ring edges) and fails if any token is within 0.15 units of a name label,
within 0.05 of a node circle, within 0.04 of another token, or crossed by an edge it does not
belong to. With round 2's placement (Sue's name above her node) it reports "token Dale->Sue is
0.000 from label 'Sue'", the overlap the critics saw; Sue's label now sits up-left of her node.
With this revision's larger tokens (0.30 units, digits 30) Carol's old left-hand label would sit 0.013
from the Pam->Carol token, so it moved below her node. Tokens on short edges keep to a right-hand
lane. A per-beat audit in the scene also logs any text within 0.12 units of other text or of a
small shape. The closing "4×" / "1×" are a tally in the empty right-hand panel (Sue: four tokens,
Betty: one token), not tags beside the nodes, where they read as labels of the wrong girl.

## Round 3 additions (every new number and claim)

| Claim (spoken or on screen) | Check | Source |
|---|---|---|
| Hook: "How many friends does the average friend have? Pick one." with YELLOW candidates 2.5, 3, 4 under the drop lines | The candidates are values of the friend average (YELLOW = reached by following a friendship). 2.5 is the naive answer, 3 is Feld's friend mean (Table 1, "Mean 3, for 20 friends"), 4 is the largest count. Nothing on screen claims which is right until 0:5x. | Feld 1991, Table 1 |
| "Friends sit closer to everyone else in the network, so they should catch it first." (replaces round 2's "More friends means more ways to catch flu", which suggested friends get sick *more often*; the redrawn totals are level, 32/425 = 7.5 % vs 25/319 = 7.8 %) | C&F, Fig. 1 caption: "central individuals are likely to be infected sooner because they lie a shorter number of steps (on average) from all other individuals in the network". Fig. 3 caption: "The friend group was observed to have significantly higher measured in-degree and betweenness centrality than the random group." | Christakis & Fowler 2010, PLoS ONE 5(9): e12948 |
| Facebook picture of "A few users had thousands of friends": four BLUE dots slide past 800 through a break in the axis toward a tick "5,000", tagged "Facebook's limit"; the dots are labelled "a few users" | Ugander et al., arXiv text (re-read Oct 2026): "a much smaller population have many hundreds or even thousands of friends" and "The distribution shows a clear cutoff at 5000 friends, a limit imposed by Facebook on the number of friends at the time of our measurements." The dots are schematic (no values are claimed for them); the "≈"-style break marks the compressed stretch from 800 to 5,000. | Ugander, Karrer, Backstrom & Marlow 2011, arXiv:1111.4503 |
| d is named on screen: "d = k − μ" (PURPLE d, BLUE μ) above the distance line, written on "her distance" | Sue: d = 4 − 2.5 = 1.5, the 1.5 copied into (2.5 + 1.5)². The distance labels are \|d\| until "left and right", then signed d (−1.5, −0.5, +0.5, +1.5). | definition |
| "the left and right distances add to zero": the four signed labels merge into the 0 under the balance point, and that 0 replaces avg(d) | Two girls at each count: Σd = 2(−1.5 − 0.5 + 0.5 + 1.5) = 0, so avg(d) = 0/8 = 0 and 2μ·avg(d) = 0. In general Σ(k − μ) = Σk − nμ = 0. | algebra |
| Scale tag: "square side = distance, drawn at 1/4 scale" (round 2: "squares at ¼ scale", which a critic read as areas at ¼) | Beam: 1.6 units per friend (girls now 0.8 apart, so each name fits under its node). Squares: SQ_SCALE = 1.6/4 = 0.4 units per friend of distance, so sides are exactly ¼ of the beam distances (0.6 and 0.2 units) and drawn areas 1/16. The labels give the true areas in friends², 2.25 and 0.25. | scene.py |
| Fulcra still exact after the respacing | Girls sit at BX(k) ± 0.4 with BX linear in k, two per count, so the girls' mean x is BX(2.5); each pair is symmetric about BX(k), so the token-weighted mean x is BX(Σk²/Σk) = BX(3). | geometry |
| Ring callback: thumbnail of the 0:31 ring, its PURPLE distance line collapses to a point, the bars meet at 2.0 and 2.0 (no PURPLE), and the row reads 2 + 0/2 = 2 | The ring: every count 2, μ = 2, σ² = 0, so μ + σ²/μ = 2 + 0/2 = 2, as measured at 0:40 (32/16 = 2.0). The bars then return to the real class, 2.5 and 3.0. | computed |
| C&F read-out: "C&F fitted lead: 13.9 days"; citation "Christakis & Fowler, 2010 · PLoS ONE · Fig. 3 redrawn, logistic refit" | The 13.9-day shift is C&F's published estimate (Abstract: 13.9 days, 95 % CI 9.9–16.6). The dashed curves are a refit of the curve shape to the redrawn steps with that shift held at 13.9; letting the shift float gives 14.5 days, inside C&F's CI (sim.py). The label now says whose number it is. | C&F 2010; sim.py |
| Self-reported read-out: "self-reported:" appears with a GRAY copy of the 13.9-day arrow; on "shrank" a live number reads the arrow's length as it shrinks, ending at 3.2 days | C&F Results: "a significant but smaller shift in self-reported flu symptoms (3.2 days, 95% C.I. 2.2–4.3)". The number is the arrow's length in days at the chart's scale (dpu from the x axis), so it ends at exactly 3.2; intermediate values are the moving ruler, not claims. | C&F 2010 |
| 0:42 reset: the ring's friend bar and its "2.0" fade out instead of counting down | Round 2 showed "1.9" on the friend readout while the girl bar read 2.0, a false momentary claim. | presentation |

## Considered and cut

- A simulated SIR outbreak on a synthetic school: in configuration-model simulations friends mostly
  got sick *more often*, with only a small timing shift, which would have added a second idea. Replaced
  by the real Harvard curves.
- Marketville's whole network (146 girls; mean 2.7 vs 3.4 among friends; 80 fewer vs 41 more) is
  verified in Feld but not used, to keep one example.
- Facebook's "92.7 % of users have fewer friends than their friends' average" (verified) is a
  separate individual-level claim; not used.

## Second review cycle, round 1 additions (every new number and claim)

| Claim (spoken or on screen) | Check | Source |
|---|---|---|
| The token fulcrum slides as the token layers land; its live read-out stops at 2.5, 2.7, 2.9, 3.0 | Layer j holds the j-th token of every girl with more than j friends; tokens sit on their girl's column, at position k. Layer 1: 8 tokens, positions summing to 20, balance 20/8 = 2.5 (one token per girl, so it balances where the girls do). Layer 2: +6 tokens (Sue, Alice, Jane, Pam, Dale, Carol), +18, so 38/14 = 2.714 → "2.7". Layer 3: +4 (Sue, Alice, Pam, Dale), +14, so 52/18 = 2.889 → "2.9". Layer 4: +2 (Sue, Alice), +8, so 60/20 = 3.0. Computed exactly with fractions. Between layers the read-out is the moving fulcrum's position (each landing token is weighted by how far it has landed), not a claim. | computed |
| "Named friends have more friends, so they sit closer to everyone else, and should catch flu first." | Re-read on journals.plos.org (Oct 2026). Results: "The friend group was observed to have significantly higher measured in-degree and betweenness centrality than the random group." In-degree is the number of times a student was named as a friend. Abstract: "monitoring the friends of randomly selected individuals. Such individuals are known to be more central." Fig. 1 caption: central individuals "are likely to be infected sooner because they lie a shorter number of steps (on average) from all other individuals". | Christakis & Fowler 2010, PLoS ONE 5(9): e12948 |
| "over the average count, two and a half" | μ = 20/8 = 2.5 is the average friend count over the eight girls (round 1 said "the average girl", which a critic noted is a person, not a count). | Feld 1991, Table 1 |
| Landing: "Seat by seat, five have fewer friends than their friends average; only Sue and Alice have more." | Unchanged fact (Feld p. 1465); "seat by seat" now names the switch from the friend average (3.0, over 20 friendship ends) to a per-girl comparison. | Feld 1991 |
| Closing line: "Two and a half counts the girls; three counts the friendships." The friend bar grows to 3 (BLUE to 2.5, PURPLE beyond), the candidate 3 is ringed | 2.5 = 20/8 averages friend counts over the 8 girls, each counted once. 3 = 60/20 averages over the 20 friendship ends (each of the 10 friendships followed from both sides), which is how "the average friend" is defined (Feld Table 1, "Mean 3, for 20 friends"). | Feld 1991, Table 1 |
| Ring callback: the bars stay at 2.5 / 3.0 (dimmed); the ring thumbnail carries 2 + 0/2 = 2 | Round 1 switched the bars to 2.0 / 2.0 while the beam still showed 2.5 and 3. The ring: μ = 2, σ² = 0, μ + σ²/μ = 2. | computed |
| Facebook: a BLUE brace labelled "a few users" spans the broken stretch of the axis from just past 800 to the 5,000 tick ("Facebook's limit") | It marks a range, with no values claimed (round 1's four dots read as plotted data). Ugander et al.: "a much smaller population have many hundreds or even thousands of friends"; "a clear cutoff at 5000 friends, a limit imposed by Facebook". | Ugander et al. 2011, arXiv:1111.4503 |
| Cut from the narration | "friends average twenty percent more than girls" (muddled: the friends are girls; "+0.5 · 20%" stays on screen, on the PURPLE excess over the BLUE 2.5) and "Sixty over twenty" (the fraction is on screen). The landing's second token flight and 4× / 1× tally are cut. | presentation |
