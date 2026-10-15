"""Simulation behind episode 36. ALL DATA SIMULATED.  Run: python sim.py
Points uniform on the 10 x 10 square; label +1 (blue) inside the disc of area 50
centred at (5, 5), -1 (purple) outside.  Training set: 20 inside + 20 outside.
Weak learner: axis-aligned decision stump (one straight cut) minimising weighted error.
"""
import numpy as np

R = np.sqrt(50 / np.pi)          # disc covers exactly half the square
N = 40
SEED = 3

def label(X):
    return np.where(((X - 5) ** 2).sum(1) < R * R, 1, -1)

def make_train(n=N, seed=SEED):
    rng = np.random.default_rng(seed)
    X, y = [], []
    while len(y) < n:
        p = rng.uniform(0.3, 9.7, 2)
        c = 1 if ((p - 5) ** 2).sum() < R * R else -1
        if sum(1 for v in y if v == c) < n // 2:
            X.append(p); y.append(c)
    return np.array(X), np.array(y)

def make_fresh(n=5000, seed=99):
    X = np.random.default_rng(seed).uniform(0, 10, size=(n, 2))
    return X, label(X)

def best_stump(X, y, w):
    best = None
    for f in (0, 1):
        xs = np.unique(X[:, f]); ths = (xs[:-1] + xs[1:]) / 2
        for t in ths:
            for s in (1, -1):
                pred = np.where(X[:, f] < t, s, -s)
                err = w[pred != y].sum()
                if best is None or err < best[0] - 1e-12:
                    best = (float(err), f, float(t), s)
    return best

def stump_pred(st, X):
    _, f, t, s = st
    return np.where(X[:, f] < t, s, -s)

def adaboost(X, y, T):
    n = len(y); w = np.full(n, 1 / n); out = []; ws = [w.copy()]
    for _ in range(T):
        st = best_stump(X, y, w); eps = st[0]
        a = 0.5 * np.log((1 - eps) / eps)
        p = stump_pred(st, X)
        w = w * np.exp(-a * y * p); w /= w.sum()
        out.append((st, a, eps)); ws.append(w.copy())
    return out, ws

def vote(stumps, X, k=None):
    k = len(stumps) if k is None else k
    F = sum(a * stump_pred(st, X) for st, a, _ in stumps[:k])
    return np.where(F >= 0, 1, -1)

def bagging(X, y, B=100, seed=500):
    rng = np.random.default_rng(seed); n = len(y); out = []
    for _ in range(B):
        idx = rng.integers(0, n, n)
        out.append(best_stump(X[idx], y[idx], np.full(n, 1 / n)))
    return out

def noisy_track(idx=6, T=100):
    """Flip one label (index 6: a point inside the circle) and return its weight per round."""
    X, y = make_train(); yn = y.copy(); yn[idx] *= -1
    _, ws = adaboost(X, yn, T)
    return np.array([w[idx] for w in ws])

if __name__ == "__main__":
    X, y = make_train(); Xf, yf = make_fresh()
    print("fresh share inside", (yf == 1).mean())
    st0 = best_stump(X, y, np.full(N, 1 / N))
    p0 = stump_pred(st0, X)
    print("best stump", st0, "right", (p0 == y).sum(), "/", N, "fresh", (stump_pred(st0, Xf) == yf).mean())
    bag = bagging(X, y)
    Fb = sum(stump_pred(s, X) for s in bag)
    print("bagging: distinct cuts", len({(s[1], round(s[2], 2), s[3]) for s in bag}),
          "vote right", (np.where(Fb >= 0, 1, -1) == y).sum(), "/", N)
    from collections import Counter
    print(Counter((s[1], round(s[2], 2), s[3]) for s in bag).most_common(6))
    stumps, ws = adaboost(X, y, 100)
    for k in (1, 2, 3, 4, 5, 10, 20, 30, 40, 47, 50, 100):
        print(k, "right", (vote(stumps, X, k) == y).sum(), "fresh %.3f" % (vote(stumps, Xf, k) == yf).mean())
    for i, (st, a, e) in enumerate(stumps[:5]):
        print("round", i + 1, "eps %.4f alpha %.4f" % (e, a), st)
    # after reweighting, previous stump has weighted error exactly 1/2
    w1 = ws[1]; print("prev stump error on new weights", w1[p0 != y].sum())
    # label noise: flip 4 labels
    rng = np.random.default_rng(11)
    flip = np.array(sorted(rng.choice(N, 4, replace=False)))
    yn = y.copy(); yn[flip] *= -1
    sn, wn = adaboost(X, yn, 100)
    print("noise flips", flip, "share of weight on flipped after 100:", wn[-1][flip].sum(),
          "fresh clean %.3f noisy %.3f" % ((vote(stumps, Xf) == yf).mean(), (vote(sn, Xf) == yf).mean()))
    tr = noisy_track(); print("flipped point weight: start %.3f peak %.3f (round %d) end %.3f" % (tr[0], tr.max(), tr.argmax(), tr[-1]))
