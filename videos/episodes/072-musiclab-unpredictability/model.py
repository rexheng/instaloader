"""Simulated market used on screen (labelled 'simulated'). Deterministic."""
import numpy as np
S, W, N = 48, 8, 3000
Q = np.linspace(1.0, 0.1, S)          # index 0 = best song
TRACK = 25                             # "song 26"
K = 150                                # snapshots along the run

def run(s, seed):
    """Returns snapshots (W, K+1, S) of download counts and final counts (W, S)."""
    rng = np.random.default_rng(seed)
    snaps = np.zeros((W, K + 1, S))
    picks = np.zeros((W, N), dtype=int)
    for w in range(W):
        d = np.zeros(S)
        for n in range(N):
            p = Q * (d + 1) ** s
            i = rng.choice(S, p=p / p.sum())
            picks[w, n] = i
            d[i] += 1
            if (n + 1) % (N // K) == 0:
                snaps[w, (n + 1) // (N // K)] = d
    return snaps, picks

def ranks(d):
    return (-d).argsort(kind="stable").argsort() + 1

def gini(d):
    m = d / d.sum()
    return np.abs(m[:, None] - m[None, :]).sum() / (2 * len(m))

if __name__ == "__main__":
    import sys
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    for s in (0, 1):
        snaps, picks = run(s, seed)
        F = snaps[:, -1]
        R = np.array([ranks(f) for f in F])
        t = R[:, TRACK]
        print(f"s={s} track ranks {t.tolist()} worst miss {np.abs(t-26).max()}")
        print("  gini", np.round([gini(f) for f in F], 2), "max share", np.round(F.max(1) / N, 3))
        print("  top5 rank range", R[:, :5].min(), R[:, :5].max(), " bottom5 range", R[:, -5:].min(), R[:, -5:].max())
        print("  mid (11-38) range", R[:, 10:38].min(), R[:, 10:38].max())
        print("  first picks world0", picks[0, :8] + 1)
        print("  winners", (F.argmax(1) + 1).tolist(), "mean spread", (R.max(0) - R.min(0)).mean())
