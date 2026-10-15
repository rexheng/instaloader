"""Precompute data for scene.py -> data.json (all simulated)."""
import json, numpy as np
from sim import lattice, rewire, adj, run, connected
N = 40
# 1) the right-hand network for the cold open
rng = np.random.default_rng(2024)
while True:
    E = rewire(lattice(N), N, rng, 1.0); R = adj(E, N)
    if not connected(R): continue
    a = int(rng.integers(N)); b = int(rng.choice(sorted(R[a])))
    if len(run(R, [a], 1)) - 1 == 4 and len(R[a] & R[b]) == 0 and len(run(R, [a, b], 2)[-1]) == 2:
        break
# relabel: a -> 0, b -> 1
perm = list(range(N)); perm[a], perm[0] = perm[0], perm[a]
pos_b = perm.index(b); perm[pos_b], perm[1] = perm[1], perm[pos_b]
inv = {old: new for new, old in enumerate(perm)}
E2 = sorted(tuple(sorted((inv[u], inv[v]))) for u, v in E)
R2 = adj(E2, N)
assert len(run(R2, [0], 1)) - 1 == 4 and len(R2[0] & R2[1]) == 0 and 1 in R2[0]
# 2) sweep
fs = [0, .025, .05, .075, .1, .15, .2, .3, .4, .5, .6, .7, .8, .9, 1.0]
reach, rounds = [], []
for f in fs:
    r1, r2 = [], []
    for t in range(2000):
        R = adj(rewire(lattice(N), N, rng, f), N)
        x = int(rng.integers(N)); y = int(rng.choice(sorted(R[x])))
        r1.append(len(run(R, [x, y], 2)[-1]) / N)
        if connected(R): r2.append(len(run(R, [x], 1)) - 1)
    reach.append(float(np.mean(r1))); rounds.append(float(np.mean(r2)))
    print(f, reach[-1], rounds[-1], flush=True)
json.dump({"N": N, "random_edges": E2, "sweep_f": fs, "sweep_reach": reach,
           "sweep_rounds": rounds}, open("data.json", "w"))
