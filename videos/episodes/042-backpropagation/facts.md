# Episode 42 fact sheet: How a Network Learns: Passing the Blame Backward

All toy-network numbers were recomputed in Python (see the bottom of this file). The toy network is a worked example. It is not real data, and the screen labels it "toy network".

| # | Claim (as narrated / shown) | Verification | Source |
|---|---|---|---|
| 1 | Finite differences need one extra run of the network per weight: n weights need n + 1 runs per gradient (forward differences). A million weights need 1,000,001 runs. | Definition of the forward-difference gradient: one base evaluation plus one per perturbed coordinate. | Standard numerical analysis; Baydin et al. 2018 §2 (numerical differentiation needs O(n) evaluations for a gradient of n inputs) |
| 2 | Toy network: x1 = 2, x2 = 1, w1 = 1, w2 = 0.5, z = w1 x1 + w2 x2 = 2.5, h = ReLU(z) = 2.5, v = 2, y = v h = 5, target 3, loss (y-3)^2 = 4. | Python: f(1, .5, 2) = 4.0 | computed |
| 3 | Nudging w1 by 0.01 gives a loss of 4.1616 and a slope estimate of 16.16. The same nudge gives 8.04 for w2 and 10.06 for v (exactly 10.0625). | Python: 4.1616, 16.16; 8.04; 10.0625 | computed |
| 4 | Exact gradients by the backward pass are dL/dy = 2(y-3) = 4, dL/dh = 4·v = 8, dL/dv = 4·h = 10, dL/dz = 8·ReLU'(2.5) = 8·1 = 8, dL/dw1 = 8·x1 = 16, dL/dw2 = 8·x2 = 8. | Hand computation, matching the finite-difference limits (16.16 → 16 and so on as the nudge shrinks). | computed |
| 5 | Chain rule: dL/dw1 = dL/dy · dy/dh · dh/dz · dz/dw1 = 4·2·1·2 = 16. The first three factors (= 8 = dL/dz) are shared with w2. | Calculus | — |
| 6 | The backward pass costs about twice the forward pass, so the whole gradient costs about three forward runs. | Kaplan et al. 2020, §2.1: "Accounting for the backwards pass (approximately twice the compute as the forwards pass), we then define the estimated non-embedding compute as C ≈ 6N floating point operators per training token" (forward = 2N per token). This agrees with Baydin et al. 2018, which gives reverse-mode cost as c·ops(f) with "c < 6 and typically c ∼ [2, 3]". | Kaplan et al., "Scaling Laws for Neural Language Models", arXiv:2001.08361 (2020); Baydin, Pearlmutter, Radul & Siskind, "Automatic Differentiation in Machine Learning: a Survey", JMLR 18(153), 2018 |
| 7 | LLM training budgets use about 6 operations (FLOPs) per weight per token: 2 forward and 4 backward. | Kaplan et al. 2020 §2.1 (quoted above): C_forward ≈ 2N per token; training C ≈ 6N per token. | Kaplan et al. 2020 |
| 8 | Reverse mode was published by Linnainmaa in 1970. | Baydin et al. 2018 §3.3: "the work by Linnainmaa (1970, 1976) is often cited as the first published description of the reverse mode" (Helsinki master's thesis, 1970; BIT 1976). The narration says "published by Linnainmaa in 1970" and the screen gives "first published description". | Baydin et al. 2018; Griewank 2012, "Who invented the reverse mode of differentiation?", Documenta Math. Extra Vol. ISMP |
| 9 | Werbos applied it to neural networks (1974 thesis; 1982 NN application). | Baydin et al. 2018 §3.3 credits Werbos (1974, Harvard PhD thesis "Beyond Regression") with the formal discrete-time version. Schmidhuber 2015 (Neural Networks 61) credits Werbos 1982 with the first NN-specific application in today's form. The screen shows "Werbos 1974 · 1982". | Baydin et al. 2018; Schmidhuber 2015 |
| 10 | Rumelhart, Hinton & Williams (1986, Nature 323:533–536) made it famous; their hidden units learned useful features. | Bibliographic record (ADS 1986Natur.323..533R), whose abstract says hidden units "come to represent important features of the task domain". Baydin et al.: "brought to fame by Rumelhart et al. (1986)". Not credited as the inventors. | Nature 323(6088):533–536, doi:10.1038/323533a0 |
| 11 | The cost is memory: the backward pass needs forward values (v's blame = 4·h uses h = 2.5), so every forward intermediate must be stored until the backward pass reaches it. | Baydin et al. 2018 §3.2: "The advantages of reverse mode AD, however, come with the cost of increased storage requirements growing (in the worst case) proportionally to the number of operations in the evaluated function." | Baydin et al. 2018 |
| 12 | "Training repeats this step thousands of times." | A deliberately conservative generic claim. For example, 90 ImageNet epochs at batch 256 are about 450k steps. No specific study is implied. | general knowledge; conservative |

Cut or avoided: the claim that backprop was invented in 1986 (pitfall); any wall-clock time for a million runs (it depends on hardware); vanishing gradients (a second idea, cut for focus).

```python
def f(w1,w2,v,x1=2,x2=1,t=3):
    z=w1*x1+w2*x2; h=max(z,0); y=v*h; return (y-t)**2
f(1,.5,2) = 4.0 ; f(1.01,.5,2) = 4.1616 -> 16.16 ; f(1,.51,2) = 4.0804 -> 8.04 ; f(1,.5,2.01) = 4.100625 -> 10.0625
```
