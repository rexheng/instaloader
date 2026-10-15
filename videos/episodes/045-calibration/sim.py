"""Simulated data for episode 45 (all on-screen 'simulated' numbers come from here).
A 10-class problem. True label probabilities = softmax(u), u = v + w.
 * big network: sees all of u but reports softmax(A*u)  -> accurate, overconfident
 * small network: sees only v, reports the calibrated E[softmax(v+w) | v] -> honest, less accurate
"""
import numpy as np

K, N, NVAL = 10, 10_000, 5_000
SIG_V, SIG_W, A = 2.9, 1.5, 2.0
BINS = np.linspace(0, 1, 11)


def softmax(z, T=1.0):
    z = z / T
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)


def make(n, rng):
    v = rng.normal(0, SIG_V, (n, K))
    w = rng.normal(0, SIG_W, (n, K))
    u = v + w
    p = softmax(u)
    y = (p.cumsum(1) > rng.random((n, 1))).argmax(1)
    return v, u, y


def small_probs(v, rng, m=400):
    out = np.zeros_like(v)
    for _ in range(m):
        out += softmax(v + rng.normal(0, SIG_W, v.shape))
    return out / m


def reliability(P, y):
    conf, pred = P.max(1), P.argmax(1)
    right = pred == y
    rows = []
    ece = 0.0
    for lo, hi in zip(BINS[:-1], BINS[1:]):
        m = (conf > lo) & (conf <= hi)
        if m.sum() == 0:
            rows.append((lo, hi, 0, np.nan, np.nan)); continue
        acc, c = right[m].mean(), conf[m].mean()
        ece += m.mean() * abs(acc - c)
        rows.append((lo, hi, int(m.sum()), acc, c))
    return right.mean(), ece, rows


def nll(P, y):
    return -np.log(P[np.arange(len(y)), y] + 1e-12).mean()


def _report():
    rng = np.random.default_rng(45)
    v, u, y = make(N, rng)
    vv, uv, yv = make(NVAL, rng)
    z, zv = A * u, A * uv          # the big network's logits
    acc, ece, rows = reliability(softmax(z), y)
    print(f"BIG T=1: acc={acc:.3f} ece={ece:.3f}")
    for r in rows: print("  ", r)
    Ts = np.linspace(0.5, 5, 451)
    Tbest = Ts[np.argmin([nll(softmax(zv, T), yv) for T in Ts])]
    acc2, ece2, rows2 = reliability(softmax(z, Tbest), y)
    print(f"BIG T*={Tbest:.2f}: acc={acc2:.3f} ece={ece2:.3f}")
    for r in rows2: print("  ", r)
    for T in (1.0, 1.5, 2.0, 2.5, 3.0):
        a_, e_, _ = reliability(softmax(z, T), y); print(f"   T={T}: acc={a_:.3f} ece={e_:.3f}")
    Ps = small_probs(v, rng)
    acc3, ece3, rows3 = reliability(Ps, y)
    print(f"SMALL: acc={acc3:.3f} ece={ece3:.3f}")
    for r in rows3: print("  ", r)
    # top bin detail
    P = softmax(z); conf = P.max(1); right = P.argmax(1) == y
    m = conf > 0.9
    print("top bin n", m.sum(), "acc", right[m].mean(), "mean conf", conf[m].mean())


def episode_data():
    """Everything the scene draws. Deterministic (seed 45)."""
    rng = np.random.default_rng(45)
    v, u, y = make(N, rng)
    vv, uv, yv = make(NVAL, rng)
    z, zv = A * u, A * uv
    Ts = np.round(np.arange(0.5, 5.0001, 0.01), 2)
    T_star = float(Ts[np.argmin([nll(softmax(zv, T), yv) for T in Ts])])
    sweep = {}
    for T in np.round(np.arange(1.0, 2.5001, 0.01), 2):
        acc, ece, rows = reliability(softmax(z, T), y)
        sweep[float(T)] = (acc, ece, [r[3] for r in rows], [r[2] for r in rows], [r[4] for r in rows])
    Ps = small_probs(v, rng)
    small = reliability(Ps, y)
    # distribution shift: noisier inputs (larger hidden part), same T*
    sv_shift = (SIG_V * 0.6)
    v2 = rng.normal(0, sv_shift, (N, K)); w2 = rng.normal(0, SIG_W, (N, K))
    u2 = v2 + w2
    y2 = (softmax(u2).cumsum(1) > rng.random((N, 1))).argmax(1)
    # the network still reads the shifted inputs at its old scale (it does not know
    # its features got weaker): logits = A * (u2 scaled back up to the training spread)
    scale = np.sqrt(SIG_V**2 + SIG_W**2) / np.sqrt(sv_shift**2 + SIG_W**2)
    shift = reliability(softmax(A * u2 * scale, T_star), y2)
    # one example from the 0.8-0.9 bin whose top class is right
    P = softmax(z)
    conf = P.max(1)
    cand = np.where((conf > 0.84) & (conf < 0.86) & (P.argmax(1) == y))[0]
    ex = int(cand[0])
    return dict(z=z[ex], y=int(y[ex]), T_star=T_star, sweep=sweep, small=small, shift=shift)


if __name__ == "__main__":
    d = episode_data()
    print("T*", d["T_star"], "example z", np.round(d["z"], 2), "label", d["y"],
          "p", np.round(softmax(d["z"]), 3))
    for T in (1.0, 1.5, d["T_star"]):
        a, e, accs, ns, cs = d["sweep"][T]; print(T, round(a, 4), round(e, 4), np.round(accs, 2), ns)
    print("small", round(d["small"][0], 4), round(d["small"][1], 4))
    print("shift", round(d["shift"][0], 4), round(d["shift"][1], 4), [(r[2], None if r[2]==0 else round(r[3],2)) for r in d["shift"][2]])
