# Episode 23 fact sheet

Every number shown or spoken, how it was checked, and its source. Simulation numbers are recomputed by `python3 plane_model.py` / the snippet at the end (numpy, seeded); the scene imports the same module, so screen = computation.

## Real-world claims

| Claim (as narrated / shown) | Verification | Source |
|---|---|---|
| "In the Second World War, the military's instinct was to protect the parts that came back with the most hits." | Wallis: "The military was inclined to provide protection for those parts that on returning planes showed the most hits. Wald assumed, on good evidence, that hits in combat were uniformly distributed over the planes..." | W. A. Wallis, rejoinder to the discussion of "The Statistical Research Group, 1942–1945", *JASA* 75(370), June 1980; quoted verbatim in B. Casselman, "The Legend of Abraham Wald", AMS Feature Column (June 2016), and in Conversable Economist (2020). On screen: "Wallis, 1980 · JASA". |
| Armor is heavy; it impairs the mission. | M&S §2: "Reinforcement means, of course, that the aircraft is heavier, and this impairs its mission." | Mangel & Samaniego 1984. |
| Abraham Wald worked out this comparison in 1943, in memos for the Statistical Research Group at Columbia. | Eight SRG memoranda (1943), "A Method of Estimating Plane Vulnerability Based on Damage of Survivors"; SRG was at Columbia; reprinted by Center for Naval Analyses as CRC 432 (1980). Casselman: five memos on survival given hits, one on vulnerability of different sections. | DTIC ADA091073 (CNA reprint record); Casselman 2016; Mangel & Samaniego 1984. |
| "His method also handled planes hit many times." | Wald's basic equation Σ a_j/(q_1…q_j) = 1 − a_0 uses planes returning with j = 1…5 hits; his region formula is q(i) = δ(i)·q/γ(i) (holes share ÷ area share × overall per-hit survival). | M&S 1984 §3.1, §3.5 (eqs. 3.3, 3.24). |
| Worked example: engine hit survived 59 % of the time, fuselage 94 %. | M&S Table 4 (hypothetical data: 400 planes, 380 return; holes engines 19, fuselage 39, fuel 18, other 26; area shares .269/.346/.154/.231; q = .851): engine .588, fuselage .940, fuel system .973, others .939. Recomputed: .186×.851/.269 = .588; .382×.851/.346 = .940. | Mangel & Samaniego, "Abraham Wald's Work on Aircraft Survivability", *JASA* 79(386):259–267, 1984. The data are illustrative (M&S: "A Hypothetical Set of Data"), so the narration says "the example Mangel and Samaniego worked through", not combat data. |
| Wald assumed hits land evenly; proposed firing dummy bullets at real planes to check. | Wallis (above): "Wald assumed, on good evidence, that hits in combat were uniformly distributed". M&S §3.5: γ "can be experimentally determined by firing dummy bullets at real aircraft." | Wallis 1980; M&S 1984. |
| (Not claimed) Wald personally decided where armor went. | Casselman: memos "say nothing about what the military should do". The script never says Wald recommended armoring engines; it says he "worked out this comparison". | Casselman 2016. |
| The famous red-dot bomber image | Not used. Our plane is our own drawing, labelled "simulated". (Commons: that image is a modern "illustration of hypothetical damage pattern", 2016/2021.) | Wikimedia Commons, File:Survivorship-bias.svg. |

## Simulation (labelled "simulated" on screen throughout the build)

Model: stylised top-view bomber (plane_model.py). One hit per plane, uniform over the silhouette. Area shares (Monte Carlo, 400 000 points; 2 000 000-point check agrees to ±0.001): engines 0.174, fuselage 0.251, wings 0.463, tail 0.111. Per-hit survival: engines 0.59, fuselage 0.94, wings 0.97, tail 0.94 (M&S Table 4 values rounded; their "fuel system" → our wings, "others" → our tail; this mapping is a modelling choice, said on screen only as "borrowed those numbers").

| Shown / said | Value | Check |
|---|---|---|
| Sorties | 400, each hit once | campaign(seed=25) |
| Holes on returning planes | engines 42, fuselage 91, wings 181, tail 42 (sum 356) | np.bincount(reg[survived]) |
| Planes lost, first campaign | 44 | 400 − 356 |
| Their holes (red) | engines 27, fuselage 8, wings 7, tail 2 | np.bincount(reg[~survived]) |
| All hits incl. lost | engines 69, fuselage 99, wings 188, tail 44 | ≈ expected 69.6 / 100.5 / 185.4 / 44.5 ("covers the plane evenly") |
| "Engines are seventeen percent of the area, so about seventy of the four hundred hits" | 400 × 0.174 = 69.6 ≈ 70 | |
| "Forty two out of seventy … sixty percent" | 42 / 69.6 = 0.603 | |
| Wings: "181 seen out of 185 expected … ninety eight percent" | 181 / 185.4 = 0.976 → 0.98 | |
| Other ratios on screen | fuselage 91/100.5 = 0.905 → 0.91; tail 42/44.5 = 0.944 → 0.94 | "every other part comes home more than ninety percent of the time" ✓ (0.91, 0.98, 0.94) |
| Next campaign (seed 121, same fire for each option; armor = hits there are survived) | no armor 40, armored wings 36, armored engines 12 | campaign(121, armored=…) |
| "Four planes saved out of forty" | 40 − 36 = 4 | |
| "Losses fall from forty to twelve" | 40 → 12 | |
| "If fire avoided the engines … the same 42 holes would look harmless" | expected slides 70 → 46; 42/46 = 0.91 (same as other parts) | illustrative what-if, stated as conditional |
| Expected losses (sanity check of the seeds) | E[lost] = 400·Σ γ(1−q) = 42.8; seeds 25 (44) and 121 (40) are typical, not extreme | |

Note on the estimator: with exactly one hit per plane, seen/expected = (N·γ·q)/(N·γ) = q exactly in expectation. With multiple hits per plane Wald's formula q(i) = δ(i)q/γ(i) is needed; the narration flags "his method also handled planes hit many times".
