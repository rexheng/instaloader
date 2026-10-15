import numpy as np
from sim import ranks
S, W = 48, 8
def run(q, s, rng, N):
    d = np.zeros(S)
    for _ in range(N):
        w = q * (d + 1) ** s
        d[rng.choice(S, p=w / w.sum())] += 1
    return d
q = np.linspace(1.0, 0.1, S)
N=3000
for seed in range(6):
  out=[]
  for s in [0,1]:
    rng = np.random.default_rng(seed)
    D = np.array([run(q, s, rng, N) for _ in range(W)])
    R = np.array([ranks(d) for d in D])
    spread = (R.max(0)-R.min(0))
    out.append((spread.mean(), sorted(R[:,25].tolist()), [int(np.argmax(d))+1 for d in D]))
  print(seed, ["%.1f %s %s"%o for o in out])
