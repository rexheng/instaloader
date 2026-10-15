# Episode 35 — Why a Forest of Bad Trees Beats One Good Tree

**One idea:** averaging trees only cancels the part of their wobble they don't share, so the vote's variance is rho sigma squared plus (1 − rho) sigma squared over B; random forests win by pushing rho down, not by adding trees.

All data on screen is simulated (sim.py, numbers in sim_output.txt and facts.md): 300 training points, rule "gold above x₂ = 5 + 2.2 sin(0.75 x₁)", 15 % of labels flipped. "Wrong" = share of the plane where the model disagrees with the true rule.

## Palette (colour -> one meaning)

| colour | meaning |
|---|---|
| BLUE | class "blue": points and the regions a model gives to them |
| YELLOW | class "gold": points and regions |
| RED | wrong: where a model disagrees with the true rule, and every error number |
| PURPLE | shared wobble: correlation rho, the rho sigma squared floor |
| GREEN | a tree's own wobble: the (1 − rho) sigma squared part that averaging cancels |
| INK / GRAY / DIM | text, the true-rule dashed curve, focus boxes / axes / context |

## Beats

**Cold open (0:00–0:13)**
1. This decision tree sorts all three hundred training points perfectly. Yet on new points from the same rule, it's wrong about eighteen percent of the time.
   *(points land; regions carve split by split; "training 300 / 300"; the dashed true rule and the red disagreement area appear; RED 18.4 %)*
2. Now two hundred worse trees, each wrong about twenty one percent of the time, take a vote. Guess the error of their vote. [pause 1.5]
   *(three offset mini-planes "× 200", "each ≈ 21 % wrong", "vote: ? %")*

**Naive build (0:13–0:45)**
3. The obvious crowd is two hundred copies of the best tree.
   *(copies stack out of the tree; tree counter 1 → 200)*
4. Their vote is wrong eighteen point four percent of the time, exactly as before, because copies make the same mistakes, so no copy is ever outvoted.
   *(red area unchanged; error curve flat at 18.4)*
5. So where do the mistakes come from? Draw a fresh sample of three hundred points from the same rule, and grow the tree again.
   *(points and regions swap to fresh samples, three times)*
6. These little boxes around single mislabeled points land somewhere new every time. That wobble from one dataset to the next is the tree's variance, sigma squared.
   *(focus box on a one-point box; σ² label)*

**Fix 1, and its measured stall (0:45–1:22)**
7. We have one dataset, but we can fake fresh ones by resampling it with replacement. About a third of the points drop out, some count twice, and each tree comes out different. That's bagging.
   *(left-out dots dim to 30 %, doubled dots get a ring; "36 % left out"; tree re-grows)*
8. Two hundred bagged trees, voting. Watch the boxes blur.
   *(vote image accumulates tree by tree; live error curve drops)*
9. The error falls to eleven point six percent, then stalls. After fifty trees, more trees change nothing.
   *(flat tail of the RED curve highlighted)*

**Insight (1:22–2:20)**
10. To see why, give every pair of trees a cell in a grid. The variance of the vote is the average of all the cells.
11. A diagonal cell pairs a tree with itself, so it holds the full sigma squared. Two different trees learned from the same data, so they wobble together: their cell holds only a share, rho.
12. The purple layer covers every cell, so it averages to rho sigma squared. The green sits on only B of the B squared cells, so it averages to one minus rho, sigma squared, over B.
13. Add trees, and the green shrinks toward zero. The purple floor stays.
14. Now the copies. For copies, rho is one. What does that leave? [pause 1.5] Just sigma squared: the B cancels, and copying buys nothing.
15. Bagged trees here have rho of about point two two. Measured over forty simulated datasets, the vote's variance follows this curve right down to the floor.

**Fix 2 (2:20–2:45)**
16. So the lever is rho. The random forest fix: at every split, a tree may look at only a random subset of the features. Here, one of the two.
17. Each tree gets a little worse, but rho drops to point one seven, and the floor drops with it. The vote is wrong nine point nine percent of the time. That's the number you guessed.

**Payoff (2:45–3:15)**
18. Leo Breiman proved in two thousand one that adding trees can't make a forest overfit. Its error settles to a limit set by how strong the trees are and how correlated.
19. Kinect's body tracker ran on three randomized trees, each trained on different random images, labelling every pixel of a frame in under five milliseconds.
20. What's left in red is what the trees get wrong together, and no number of trees outvotes it.

**Landing (3:15–3:25)**
21. So the first tree didn't lose for being bad. It lost for being alone: none of its mistakes could ever be outvoted.

## Sources
- Breiman, L. (2001). Random Forests. *Machine Learning* 45(1), 5–32. Theorem 1.2 (no overfitting as trees are added), Theorem 2.3 (PE* ≤ ρ̄(1 − s²)/s²).
- Breiman, L. (1996). Bagging predictors. *Machine Learning* 24(2), 123–140.
- Hastie, Tibshirani & Friedman (2009). *The Elements of Statistical Learning*, 2nd ed., eq. 15.1.
- Shotton et al. (2011). Real-Time Human Pose Recognition in Parts from Single Depth Images. *CVPR 2011*, 1297–1304.
