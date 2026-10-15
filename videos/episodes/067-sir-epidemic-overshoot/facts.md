# Facts: Episode 67, "Why Epidemics Overshoot Herd Immunity"

Model shown everywhere on screen: deterministic SIR (well-mixed), R0 = 2.5, lasting immunity, no
interventions, started from 1 infected in 400 (simulated; labelled "simulated" on screen).
All numbers recomputed with scipy (`solve_ivp`, rtol 1e-10; `brentq` on the final-size equation).

| # | Claim (narration / screen) | Verification | Source |
|---|---|---|---|
| 1 | Classical herd-immunity threshold for R0 = 2.5 is 60% | 1 - 1/R0 = 1 - 0.4 = 0.6 | Standard; restated as h_C = 60% for R0 = 2.5 in Britton et al. 2020, Table 1 |
| 2 | Without depletion, each new case comes with 0.4 recoveries; the (caught-it, sick-now) path is a straight line of slope 0.6 | Linear model dI = beta I dt - gamma I dt, dx = beta I dt, so dI/dx = 1 - gamma/beta = 1 - 1/R0 = 0.6 | Derivation |
| 3 | Effective cases per case = R0 x S; recoveries per new case = 1/(R0 S); slope of the SIR path = 1 - 1/(R0 S) | dI/dx with x = 1 - S: (beta S I - gamma I)/(beta S I) | Derivation |
| 4 | Curve is flat (I peaks) at S = 40%, i.e. when 60% have caught it | 1 - 1/(2.5 S) = 0 -> S = 0.4. ODE: peak at S = 0.3999, ever-infected 0.6001 | Simulation |
| 5 | Final share ever infected is 89% (357 of 400) | Final-size equation 1 - z = exp(-2.5 z): z = 0.8926. ODE with I0 = 1/400: 0.8927 -> 357.1 people | Simulation + exact |
| 6 | Missed by 29 points | 89.26 - 60 = 29.3 | Arithmetic |
| 7 | A third of all infections happen after the threshold | (0.8926 - 0.6)/0.8926 = 0.328; 117/357 = 0.328 | Arithmetic |
| 8 | 93 people sick at the peak (23%) | I_max = 1 - (1 + ln R0)/R0 = 0.2335; x 400 = 93.4 | Exact |
| 9 | 240 caught it before the turn, 117 after | 0.6001 x 400 = 240; 357 - 240 = 117 | Simulation |
| 10 | R0 = 1.5: turn at 33%, landing 58% | 1 - 1/1.5 = 0.333; final size 0.5828 | Exact |
| 11 | R0 = 4: turn at 75%, landing 98% | 0.75; final size 0.9802 | Exact |
| 12 | R0 below 1: curve never rises | slope at start = 1 - 1/R0 < 0 | Derivation |
| 13 | 400 people in a country of 60 million: each dot is 150,000 people | 60,000,000 / 400 = 150,000 | Arithmetic (hypothetical country) |
| 14 | The model is the simplest form of Kermack & McKendrick (1927) | W. O. Kermack & A. G. McKendrick, "A Contribution to the Mathematical Theory of Epidemics", Proc. R. Soc. Lond. A 115(772):700-721, doi:10.1098/rspa.1927.0118. Their model is more general (a renewal equation); SIR with constant rates is its simplest special case, so the narration says "simplest form". | royalsocietypublishing.org; Diekmann et al. arXiv:2505.01621 review |
| 15 | Britton, Ball & Trapman (2020): R0 = 2.5, population with age and activity structure; disease-induced herd immunity about 43% vs 60% classical; "an illustration" rather than an estimate | Science 369(6505):846-849, doi:10.1126/science.abc6810. Table 1: homogeneous 60.0%, age 55.8%, activity 46.3%, age+activity 43.0%. Activity groups: 50% normal, 25% half, 25% double contacts, so the most active have 4x the contacts of the least active. Authors: results "should be interpreted as an illustration". | pmc.ncbi.nlm.nih.gov/articles/PMC7331793 |
| 16 | "The busiest catch it first" | Paper's mechanism: infection, and therefore immunity, concentrates in the most socially active groups | Britton et al. 2020 |

Limits stated in narration: homogeneous mixing (Kermack-McKendrick beat), heterogeneity lowers the threshold
(Britton). Assumptions on screen with the model: "SIR, R0 = 2.5, simulated".

Not used: the 1978 BMJ boarding-school outbreak. Its 512/763 counts boys confined to bed, not infections,
so it cannot be read as a final size and would not cleanly illustrate overshoot.
