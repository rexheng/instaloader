# Episode 62 — How the Medici Won Florence Without Being the Richest

**One idea:** counting a node's ties (degree) misses brokerage; betweenness — the share of
shortest routes between other pairs that run through you — shows that the Medici's position in
the Florentine marriage network was about five times the Strozzi's, not one and a half.

## Palette (colour → one meaning)
- YELLOW → the Medici (node, bar, formula's v)
- PURPLE → the Strozzi (node, bar)
- BLUE → marriage ties (edges)
- GREEN → shortest routes (path highlights, route counts σ)
- RED → damage: pairs of families cut off
- INK text · GRAY other families, axes, secondary labels · DIM context

## Narration (beat by beat)

**Cold open (0:00–0:12)** — network of 16 families on screen from frame 1; wealth bars grow.
1. Florence, fourteen twenty-seven. The Strozzi are richer, but the Medici will rule.
2. Count their marriages: the Medici have six, the Strozzi four. How much stronger is the Medici position? Make a guess. [pause 1.5]

**Stakes + naive build** — panel bars morph wealth → degree; node sizes scale by degree.
3. Pick the wrong measure of importance, and you misread who holds power. The obvious measure is degree: count each family's ties.
4. By degree, the Medici lead, with the Strozzi and the Guadagni tied behind them at four. Six to four is one and a half to one.

**Fail** — remove nodes; red counter of pairs cut off.
5. Now test that ranking. Remove the Strozzi, and every family in the web can still reach every other through some chain of marriages.
6. Put them back, and remove the Medici instead. The web breaks into three pieces, and thirty-five pairs of families lose every connection.
7. Degree called it six to four. The damage is thirty-five to zero. Counting ties misses which ties nobody else can replace.

**Insight** — green routes, points fly to a tally, formula built from the ½.
8. So score routes instead. The Pazzi and the Acciaiuoli are joined by one shortest chain, through the Salviati and the Medici. The Medici sit on it, so they score one point.
9. The Albizzi and the Tornabuoni have two equally short chains, one through the Medici and one through the Guadagni. Each family gets half a point.
10. That half is the routes through the Medici, one, over all the shortest routes, two. Add those fractions over every pair of families, and you get betweenness.
11. Freeman wrote it down in nineteen seventy-seven. Now run it on all one hundred and five pairs that leave the Medici out.
12. The Medici collect forty-seven and a half points. The Guadagni, about twenty-three. The Strozzi, nine and a third. Against the Strozzi, the lead is about five to one, not one and a half.

**Payoff** — Padgett & Ansell 1993 · AJS on screen; partner pairs.
13. Padgett and Ansell found this structure in the marriage and business ties of ninety-two elite families. The Medici's allies were tied to each other almost only through the Medici.
14. Even in this slice, the Medici's six partners form fifteen possible pairs, and just one of those pairs is married. Among the Strozzi's four partners, two of six pairs are.
15. Centrality is only part of their argument. They also traced business, class and neighborhood, and this web holds sixteen of their ninety-two families.

**Landing** — back to the wealth bars from the opening, then to betweenness.
16. In fourteen thirty-four, Cosimo de' Medici returned from exile, and Palla Strozzi, the richest man in Florence, left it for good.
17. The Strozzi owned more of Florence. The Medici stood between more of it.

## Sources
- Padgett, J. F. & Ansell, C. K. (1993). Robust Action and the Rise of the Medici, 1400–1434. *American Journal of Sociology* 98(6):1259–1319.
- Breiger, R. L. & Pattison, P. E. (1986). Cumulated social roles. *Social Networks* 8(3):215–256 (16-family marriage network; wealth attribute from Padgett's data, UCINET PADGW).
- Freeman, L. C. (1977). A set of measures of centrality based on betweenness. *Sociometry* 40(1):35–41.
- Oxford Reference, "Strozzi family" (Palla Strozzi exiled 1434 to Padua).
