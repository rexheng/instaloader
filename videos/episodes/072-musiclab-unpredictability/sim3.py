import numpy as np
from sim import gini, unpred, ranks
S, W = 48, 8
def run(q, s, rng, N):
    d = np.zeros(S)
    for _ in range(N):
        w = q * (d + 1) ** s
        d[rng.choice(S, p=w / w.sum())] += 1
    return d
for lo in [0.2, 0.1]:
  q = np.linspace(1.0, lo, S)
  for N in [700, 2000, 4000]:
    for s in [0, 1]:
      rng = np.random.default_rng(7)
      D = np.array([run(q, s, rng, N) for _ in range(W)])
      R = np.array([ranks(d) for d in D])
      err = np.abs(R - np.arange(1, S+1)).mean()
      print(lo, N, s, "gini %.2f"%np.mean([gini(d) for d in D]), "err %.1f"%err, "winners", [int(np.argmax(d))+1 for d in D], "top5share %.2f"%np.mean([np.sort(d)[-5:].sum()/d.sum() for d in D]))
