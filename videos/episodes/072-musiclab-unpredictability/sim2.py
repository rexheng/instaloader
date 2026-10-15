import numpy as np
from sim import gini, unpred, ranks
S, W = 48, 8
def run(q, s, rng, N):
    d = np.zeros(S)
    for _ in range(N):
        w = q * (d + 1) ** s
        d[rng.choice(S, p=w / w.sum())] += 1
    return d
q = np.linspace(1.0, 0.35, S)
for N in [700, 1000]:
  for s in [0, 1]:
    rng = np.random.default_rng(7)
    D = np.array([run(q, s, rng, N) for _ in range(W)])
    R = np.array([ranks(d) for d in D])
    from scipy.stats import spearmanr
    rho = np.mean([spearmanr(-np.arange(S), d).correlation for d in D])
    print(N, s, "gini", round(np.mean([gini(d) for d in D]),3), "U", round(unpred(D),4), "rho", round(rho,2),
          "song26 ranks", sorted(R[:,25]), "winners", [int(np.argmax(d))+1 for d in D],
          "top share", [round(d.max()/d.sum(),3) for d in D])
