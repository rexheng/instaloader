# Episode 077 — fact sheet

Every claim spoken or shown, how it was checked, and the source. "Simulated" numbers
come from `model_check.py` (exact rational arithmetic) and are labelled "simulated" on screen.

## Real-world claims

| # | Claim (as used) | Verification | Source |
|---|---|---|---|
| 1 | Törbel (Valais, Swiss Alps) has managed its high pasture as a commons for more than five hundred years; villagers formed an association to regulate the alp on 1 Feb 1483. | Two independent secondary sources agree on 1483; written rules go back further (13th c.). "More than five hundred years" is safe (2026 − 1483 = 543). | Gardner & Stern, *Environmental Problems and Human Behavior*, ch. 6 prologue (citing Netting 1976, 1981); swissinfo.ch, "Törbel und Elinor Ostrom" (2025); Ostrom 1990, ch. 3 |
| 2 | Törbel rule: "no one is permitted to send more cows to the alps than he can [feed in] winter". On screen paraphrased "No more cows on the alp than you can feed through winter". | Quoted by Gardner & Stern from Netting (1981, p. 61). Year of the rule is reported as 1517 (Netting/Ostrom) but the Swiss Historical Dictionary dates the alp statute 1507, so **no year is stated** for the rule in the video. | Netting, R. McC. (1981) *Balancing on an Alp*, Cambridge UP, p. 61 |
| 3 | An elected local official fines rule-breakers; cows are counted when they go up to the alp. | Gardner & Stern: "A local official is authorized to levy fines on those who violate the rules against overgrazing… The official, in turn, is elected at the annual meeting"; "The cows are sent to the alp all at once, and are immediately counted". | Netting 1981 via Gardner & Stern ch. 6 |
| 4 | Garrett Hardin, 1968, *Science*: "Freedom in a commons brings ruin to all." Herdsman's gain from one more animal "nearly +1", his share of overgrazing "only a fraction of −1". | Verbatim text checked (ion.sdsu.edu extract). Citation: Science 162(3859):1243–1248, 13 Dec 1968. Hardin applied the argument to pastures, ocean fisheries ("the oceans of the world continue to suffer from the survival of the philosophy of the commons") and pollution. | Hardin 1968, Science 162:1243 |
| 5 | Elinor Ostrom, *Governing the Commons* (1990, Cambridge UP) uses Törbel as a founding case; 2009 Nobel Memorial Prize in Economic Sciences (shared with Oliver Williamson); first woman to win it. | swissinfo (Törbel is "the first, foundational case study" of the 1990 book; 2009 prize). First woman: Nobel Prize website / widely documented. | Ostrom 1990; nobelprize.org |
| 6 | Fehr & Gächter: anonymous groups of four, 20 tokens each round, every token in the shared pot returns 0.4 to each member; fixed ("partner") groups; final round mean contribution 3.2 tokens without punishment vs 18.2 with the option to pay to fine others. Spoken as "about three" and "about eighteen" tokens of twenty. | Read from Table 4 ("Mean contributions in the Partner-treatments", final period: 3.2 vs 18.2) and §C (y = 20, n = 4, a = 0.4) of the paper's working-paper version (CESifo WP 183), whose design and data are those published in the AER. Punishing was costly to the punisher (Table 2: 1–30 tokens). | Fehr & Gächter (2000) "Cooperation and Punishment in Public Goods Experiments", AER 90(4):980–994, doi:10.1257/aer.90.4.980 |

## Simulated model (on screen: "simulated")

Steady state of logistic regrowth with grazing proportional to cows: G*/K = 1 − eC/r. With r/e = 100 cows: grass left = 1 − C/100, milk per cow = 20 L/day × grass left = 20 − 0.2C (each extra cow cuts every cow's milk by 0.2 L).

| Number shown/spoken | Exact value | Check |
|---|---|---|
| 20 L per cow on fresh grass; −0.2 L per cow per added cow | model parameters | — |
| Village milk peaks at 50 cows, 500 L/day, grass 50 % | C(20 − 0.2C) max at C = 50 → 50 × 10 = 500 | model_check.py |
| No rules, each herder adds while it pays: 90 cows (9 each), grass 10 %, 180 L/day | best-response dynamics from 5 each | model_check.py |
| 3 "saints" fixed at 5 cows: herd settles at 89; saints earn 11 L/day, others 22–24.2 L/day ("about half") | best-response | model_check.py |
| 51st cow: gain 9.8 L; damage 50 × 0.2 = 10 L; his share 5/50 → 1 L; net to him +8.8 L; net to village −0.2 L | exact | model_check.py |
| He stops when damage = N × gain: 91st cow gain 1.8 L, damage 18 L, his share 1.8 L, net 0 | exact (tie → does not add) | model_check.py |
| Fine of 9 L per cow over 5 (= the 9 of 10 damage slices that fall on others): herd stays at 50, 500 L/day | gain − share − fine = 9.8 − 1 − 9 < 0 | model_check.py |
| Formula: add a cow iff gain > damage / N (equal herds); with fine = damage·(N−1)/N, iff gain > damage | algebra | — |

## Cut / hedged
- The year 1517 for the winter rule (conflicts with 1507 in the HLS) — not stated.
- Antisocial punishment (Herrmann, Thöni & Gächter 2008) — cut for length; the honest limit given is the monitoring requirement ("a fine only works if someone counts"), which is the logical condition of the model and one of Ostrom's design principles (monitoring).
