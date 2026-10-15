# Episode 18 · Fact sheet

Primary source: L. D. Stone, C. M. Keller, T. M. Kratzke, J. P. Strumpfer (2014),
"Search for the Wreckage of Air France Flight AF 447", *Statistical Science* 29(1):69–80,
doi:10.1214/13-STS420 (arXiv:1405.4720). Read in full (PDF text); page refs below are to the arXiv reprint.

| # | Claim (as used in the episode) | Verification | Source |
|---|---|---|---|
| 1 | AF 447 disappeared over the Atlantic in June 2009 (June 1), Rio → Paris | Abstract, p.1 | Stone et al. 2014 |
| 2 | 228 passengers and crew aboard (spoken in stakes beat) | Abstract: "carrying 228 passengers and crew"; Wikipedia: 216 passengers + 12 crew | Stone et al. 2014; Wikipedia "Air France Flight 447" |
| 3 | Wreck had to lie within 40 NM of the last known position (the circle) | §1, §3.1: "the location of the wreckage was within the 40 NM circle … with probability 1" | Stone et al. 2014 |
| 4 | Ships listened for the recorders' underwater locator beacons for 31 days, along the intended flight path, and heard nothing | §1: "search began on June 10, 2009 and lasted 31 days … searched extensively along the intended flight path, but the beacons were not detected"; §4.3 | Stone et al. 2014 |
| 5 | "Two ships" | §1/§4.3: "performed by two ships employing passive acoustic sensors" | Stone et al. 2014 |
| 6 | August 2009: sonar searched a patch the listening ships had not covered; unsuccessful | §1: "active acoustic search with side-looking sonar … in August 2009 south of the last known position in an area not covered by the passive acoustic search … also unsuccessful"; §4.4 "chosen because it … had not been searched before" | Stone et al. 2014 |
| 7 | A larger sonar search in 2010 (April–May, "next spring") also found nothing | §1: 2010 searches by US Navy/Phoenix and WHOI, rectangle then extended south and west, "also unsuccessful" | Stone et al. 2014 |
| 8 | Analysts put the chance the ships would have heard the beacons (wreck within range) at 0.77 | §4.3: P_D = 0.92 (independent beacon survival) or 0.72 (dependent); weighted 0.25/0.75 → P̄_D = 0.77; failure factor 1 − P̄_D = 0.23. Recomputed: 0.25·0.9216 + 0.75·0.72 = 0.7704 | Stone et al. 2014 |
| 9 | 0.77 = a ~90% chance of hearing a working beacon, discounted for beacons destroyed in the crash | §4.3: sensors "probability at least 0.9 of detecting the beacons within lateral range 1730 m"; "accounted for the possibility that one or both of the beacons were destroyed in the crash", survival 0.8 each from past crash data | Stone et al. 2014 |
| 10 | Bayes update for a failed search: w̃ ∝ (1 − p_d)·w | Eq. (4.1) | Stone et al. 2014 |
| 11 | Two-region form: P(zone given miss) = p(1−d)/(1−pd) | Derived: numerator p(1−d); total remaining p(1−d) + (1−p) = 1 − pd | algebra |
| 12 | With p = 0.5, d = 0.77: 0.5·0.23/(1 − 0.385) = 0.115/0.615 = 0.187 ≈ 19% | Computed exactly (python) | — |
| 13 | d = 0 ⇒ posterior = prior (0.5) | formula | — |
| 14 | In 2010 (July) the BEA tasked the authors (Metron, Inc.; Lawrence Stone chief scientist) to build a probability map accounting for all previous search | §1: "In July 2010 we were tasked by the BEA…"; author affiliations | Stone et al. 2014 |
| 15 | Doubts about the beacons led them to also compute a posterior that assumes the beacons did not function | §4.6: "doubts about the beacons compelled us to produce the alternate posterior shown in Figure 8, which assumes the beacons did not function" | Stone et al. 2014 |
| 16 | 2011 search started near the centre (of the distribution / of the circle) and found the wreck within one week | Abstract "found with one week of undersea search"; §5 "the 2011 search commenced in the center of the distribution and quickly found the wreckage"; BEA director quote "near the center of the Circle … after one week of exploration". WHOI release: Alucia on site 25 March, found ~2–3 April 2011 | Stone et al. 2014; WHOI press release Apr 2011 |
| 17 | Found by underwater robots (sonar) | WHOI: REMUS 6000 autonomous underwater vehicles with side-scan sonar | WHOI press release "WHOI-led team locates Air France wreckage" (2011) |
| 18 | Wreck lay inside the area the listening ships had covered | §5: "the wreckage is located in an area thoroughly covered by the passive search (see Figure 5)" | Stone et al. 2014 |
| 19 | Wreck lay in a high-probability area of the beacons-failed map | §4.6 / §5 | Stone et al. 2014 |
| 20 | The recovered beacon, connected to a fully charged battery, produced no signal | §4.6: "Testing by the BEA showed that when the beacon was connected to a fully charged battery, it did not produce a signal" | Stone et al. 2014 |
| 21 | Bayes did not find the plane: the AUV sonar search did; the map told them where to start, and it rests on subjective inputs (detection probabilities, scenario weights) | §2: subjective probabilities; §4.3: "detection estimates … tend to be optimistic" | Stone et al. 2014; WHOI |
| 22 | Wreck marker position on map | Wreck 3°03′57″N 30°33′42″W (Wikipedia, citing BEA); LKP 2.98°N 30.59°W (paper §3.1). Offset: 5.15 NM north, 1.70 NM east → 5.4 NM (≈10 km), bearing ≈18°. Placed accordingly on the map; distance not spoken | Wikipedia; Stone et al. 2014 |

## Simulated elements (labelled "simulated" on screen)
- **Prior map**: 30×30 grid of 2.67 NM cells clipped to the 40 NM circle. Mixture of 0.5 × uniform-in-circle (paper's D1) and 0.5 × circular normal, sd 8 NM, centred on the last known position (paper's D2). The paper's third component (reverse drift of bodies, D3, weight 0.3) is omitted; this is a teaching simplification, not the paper's map.
- **Listening zone**: simplified as a strip ±9 NM either side of the planned route (route bearing ≈30° true near the LKP; initial great-circle bearing Rio→Paris region). The real search tracks (paper Fig. 5) were a lattice designed to cover the expected flight path within 1730 m lateral range. The prior is rescaled within/outside the strip so the zone holds exactly 0.50 (unrescaled value 0.507; change ≤ 1.5%).
- Under that prior: zeroing gives 0; d = 0.77 gives 0.187; d = 0 gives 0.50 (recomputed in `scene.py` from the grid).

## Claims deliberately avoided
- That the BEA "zeroed" searched areas: we only state where the August 2009 sonar went (true) and attribute the zeroing logic to the viewer's choice.
- The authors' claim that a Bayesian approach "delayed the discovery by up to one year" is not used.
- No claim that our map reproduces their Figure 7 or 8.
