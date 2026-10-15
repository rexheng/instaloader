# Episode 62 — facts and verification

All network numbers recomputed with NetworkX 3.7 (`nx.florentine_families_graph()`, the
Padgett marriage network as published by Breiger & Pattison 1986; NetworkX drops the isolated
Pucci family, which we draw separately as an isolate, so the full set is 16 families, 20 marriage ties).

| # | Claim (as said / shown) | Verification | Source |
|---|---|---|---|
| 1 | The marriage network of 16 elite Florentine families; 20 ties | `G.number_of_edges() == 20`, 15 nodes + isolated Pucci | Breiger & Pattison 1986, *Social Networks* 8(3):215–256 (NetworkX docstring); UCINET PADGM/PADGB dataset page |
| 2 | Net wealth 1427 (thousand lira): Strozzi 146, Medici 103; Strozzi richest of the 16 | UCINET PADGW attribute table (Borgatti MGT780 exercise page lists WEALTH: Strozzi 146, Medici 103, next highest Barbadori 55) | analytictech.com/mgt780/exercises/xstrength.htm; UCINET "Padgett Florentine Families" page ("each family's net wealth in 1427 (in thousands of lira)") |
| 3 | Palla Strozzi was the richest man in Florence in 1427 | Wikipedia "Palla Strozzi" (gross taxable assets 162,925 florins in 1427 catasto); Gregory, *A Florentine Family in Crisis* | en.wikipedia.org/wiki/Palla_Strozzi |
| 4 | Medici degree 6, Strozzi 4, Guadagni 4 | `G.degree()` | computed |
| 5 | Ratio 6:4 = 1.5 | arithmetic | — |
| 6 | Removing the Strozzi: every family in the web can still reach every other (0 pairs cut off) | remove node → one component of 14 | computed |
| 7 | Removing the Medici: three pieces (Acciaiuoli alone; Salviati+Pazzi; 11 others); 35 pairs lose every connection | components sizes 1, 2, 11 → C(14,2)=91 minus (55+1)=35 | computed |
| 8 | Pazzi–Acciaiuoli: one shortest chain, Pazzi–Salviati–Medici–Acciaiuoli | `all_shortest_paths` → 1 path, length 3 | computed |
| 9 | Albizzi–Tornabuoni: two equally short chains, via Medici and via Guadagni | `all_shortest_paths` → [Albizzi, Medici, Tornabuoni], [Albizzi, Guadagni, Tornabuoni] | computed |
| 10 | Betweenness C_B(v) = Σ over pairs σ_st(v)/σ_st (unnormalised, each unordered pair once) | Freeman's definition; NetworkX `betweenness_centrality(normalized=False)` for undirected graphs counts each unordered pair once | Freeman 1977, "A set of measures of centrality based on betweenness", *Sociometry* 40(1):35–41 |
| 11 | 105 pairs of other families (15 choose 2, incl. Pucci, whose pairs score 0) | C(15,2)=105 | arithmetic |
| 12 | Betweenness: Medici 47.5, Guadagni 23.17 (said "about twenty-three", shown 23.2), Strozzi 9.33 ("nine and a third") | `betweenness_centrality(normalized=False)`; Medici = 45 pairs with every shortest path through Medici + 5 pairs at ½ | computed |
| 13 | Medici:Strozzi betweenness ratio ≈ 5.1 ("about five to one") | 47.5 / 9.333 = 5.089 | computed |
| 14 | Medici's six partners form 15 possible pairs; only 1 pair (Ridolfi–Tornabuoni) is married | computed | computed |
| 15 | Strozzi's four partners: 2 of 6 pairs married (Castellani–Peruzzi, Peruzzi–Bischeri) | computed | computed |
| 16 | Padgett & Ansell, "Robust Action and the Rise of the Medici, 1400–1434", *AJS* 98(6):1259–1319, 1993 | AJS page, doi 10.1086/230190 | journals.uchicago.edu/doi/abs/10.1086/230190 |
| 17 | P&A analysed 92 families, marriage and economic ties; Medici partisans connected to each other "almost solely through the Medici themselves"; oligarchs "densely interconnected" | direct quotes from the paper ("Within this 92-family data set…", "Medici partisans were connected to other Medici partisans almost solely through the Medici themselves", "Only the Medici family itself linked the segments") | home.uchicago.edu/~jpadgett/papers/published/robust.pdf |
| 18 | Centrality is only part of their argument: they also used economic/loan ties, social class, neighbourhood, and the political history | P&A tables on prestige, wealth, neighbourhood (San Giovanni) and the narrative of 1433–34 | same PDF |
| 19 | 1434: Cosimo de' Medici recalled from exile; Palla Strozzi exiled, permanently (died in Padua 1462) | P&A ("Cosimo was recalled from Venice in triumph, and Cosimo's oligarchic enemies were exiled, this time for good"); Oxford Reference "Strozzi family": "Palla Strozzi (1372–1462)… was exiled in 1434 to Padua" | PDF; oxfordreference.com |

Wording choices for accuracy
- "The Medici will rule": the Medici dominated Florence from 1434 (curriculum pitfall: they also lead in degree; the script says so).
- We never claim the Medici were poor; they were second-richest of the 16 (103 vs 146).
- The 16-family marriage network is a slice of Padgett & Ansell's 92-family data; said on screen and in narration.
- Betweenness counts each unordered pair once (no factor of 2), matching NetworkX's undirected unnormalised convention.
