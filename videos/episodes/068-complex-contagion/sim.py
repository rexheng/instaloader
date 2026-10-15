"""Simulations behind every number shown in episode 68 (all SIMULATED).
Ring lattice: N=40, each person tied to 2 neighbours on each side (4 friends).
Rewiring: degree-preserving double-edge swaps; a share f of the 80 ties is swapped
(each swapped tie at most once), so everyone keeps exactly 4 friends."""
import numpy as np

def lattice(N, k=4):
    return {tuple(sorted((i, (i + d) % N))) for i in range(N) for d in range(1, k // 2 + 1)}

def rewire(E, N, rng, f=1.0):
    S = set(E); fresh = list(E); rng.shuffle(fresh)
    target = int(round(f * len(E))); done = 0; tries = 0
    pool = list(fresh)
    while done + 2 <= target and len(pool) >= 2 and tries < 20000:
        tries += 1
        a, b = rng.choice(len(pool), 2, replace=False)
        (u, v), (x, y) = pool[a], pool[b]
        if rng.random() < .5: x, y = y, x
        if len({u, v, x, y}) < 4: continue
        e1, e2 = tuple(sorted((u, x))), tuple(sorted((v, y)))
        if e1 in S or e2 in S: continue
        S -= {pool[a], pool[b]}; S |= {e1, e2}
        for i in sorted((a, b), reverse=True): pool.pop(i)
        done += 2
    return S

def adj(E, N):
    A = [set() for _ in range(N)]
    for u, v in E: A[u].add(v); A[v].add(u)
    return A

def run(A, seeds, T):
    act = set(seeds); hist = [set(seeds)]
    while True:
        new = {i for i in range(len(A)) if i not in act and len(A[i] & act) >= T}
        if not new: return hist
        act |= new; hist.append(set(act))

def connected(A):
    seen = {0}; st = [0]
    while st:
        x = st.pop()
        for y in A[x]:
            if y not in seen: seen.add(y); st.append(y)
    return len(seen) == len(A)

if __name__ == "__main__":
    N = 40
    L = adj(lattice(N), N)
    print("ring: simple rounds", len(run(L, [0], 1)) - 1,
          "| complex rounds", len(run(L, [0, 1], 2)) - 1, "reach", len(run(L, [0, 1], 2)[-1]))
    rng = np.random.default_rng(1)
    rounds, full, shared, nconn = [], [], [], 0
    for t in range(2000):
        R = adj(rewire(lattice(N), N, rng, 1.0), N)
        a = int(rng.integers(N)); b = int(rng.choice(sorted(R[a])))
        shared.append(len(R[a] & R[b]))
        full.append(len(run(R, [a, b], 2)[-1]))
        if connected(R): nconn += 1; rounds.append(len(run(R, [a], 1)) - 1)
    rounds, full, shared = map(np.array, (rounds, full, shared))
    print("random (2000 nets): connected", nconn, "| simple rounds mean %.2f" % rounds.mean(),
          np.bincount(rounds))
    print("complex: mean reach %.2f, P(stuck at 2)=%.3f, P(all 40)=%.3f, max reach %d"
          % (full.mean(), (full == 2).mean(), (full == N).mean(), full.max()))
    print("shared friends of a tied pair: mean %.3f (theory 9/38=%.3f)" % (shared.mean(), 9 / 38),
          np.bincount(shared))
    print("sweep f, mean complex reach %, mean simple rounds")
    for f in [0, .05, .1, .15, .2, .3, .4, .5, .6, .8, 1.0]:
        fs, rs = [], []
        for t in range(1000):
            R = adj(rewire(lattice(N), N, rng, f), N)
            a = int(rng.integers(N)); b = int(rng.choice(sorted(R[a])))
            fs.append(len(run(R, [a, b], 2)[-1]) / N)
            if connected(R): rs.append(len(run(R, [a], 1)) - 1)
        print(f, round(100 * np.mean(fs), 1), round(np.mean(rs), 2))
