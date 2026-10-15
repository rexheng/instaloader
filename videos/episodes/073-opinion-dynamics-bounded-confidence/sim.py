"""Simulations behind episode 73 (all data shown on screen is simulated).
Run:  python sim.py   -> writes data.json
"""
import json
import numpy as np

EPS = 0.1
N = 100
SEED = 32


def hk_step(x, eps):
    d = np.abs(x[:, None] - x[None, :]) <= eps + 1e-12
    return (d * x[None, :]).sum(1) / d.sum(1)


def hk(x, eps, max_rounds=2000):
    traj = [x.copy()]
    for _ in range(max_rounds):
        xn = hk_step(x, eps)
        traj.append(xn)
        if np.max(np.abs(xn - x)) < 1e-10:
            break
        x = xn
    return np.array(traj)


def clusters(x, tol=1e-4):
    s = np.sort(x)
    groups = np.split(s, np.where(np.diff(s) > tol)[0] + 1)
    return [(float(g.mean()), len(g)) for g in groups]


def main():
    x0 = np.sort(np.random.default_rng(SEED).uniform(0, 1, N))
    tr = hk(x0, EPS)
    rounds = 10
    hk_tr = np.vstack([tr] + [tr[-1:]] * (rounds + 1 - len(tr)))[: rounds + 1]
    final = tr[-1]
    camps = clusters(final)
    labels = [int(np.argmin([abs(f - c) for c, _ in camps])) for f in final]
    catch = [(float(x0[np.array(labels) == k].min()), float(x0[np.array(labels) == k].max()))
             for k in range(len(camps))]
    # DeGroot: fixed trust web, each person trusts self + 5 random others equally
    rng = np.random.default_rng(100 + SEED)
    W = np.zeros((N, N))
    trust = []
    for i in range(N):
        js = rng.choice([j for j in range(N) if j != i], 5, replace=False)
        trust.append([int(j) for j in js])
        W[i, i] = 1
        W[i, js] = 1
    W /= W.sum(1, keepdims=True)
    dg = [x0.copy()]
    for _ in range(rounds):
        dg.append(W @ dg[-1])
    dg = np.array(dg)
    # sweep: 625 people, 20 runs per epsilon (as in Hegselmann & Krause 2002 set-up)
    sweep = []
    for eps in (0.01, 0.02, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2, 0.25, 0.3):
        n = [len(clusters(hk(np.random.default_rng(7000 + s).uniform(0, 1, 625), eps)[-1]))
             for s in range(20)]
        sweep.append({"eps": eps, "mean": float(np.mean(n)), "min": int(min(n)), "max": int(max(n)),
                      "rule": 1 / (2 * eps)})
    out = {
        "x0": x0.tolist(), "hk": hk_tr.tolist(), "hk_rounds_to_freeze": len(tr) - 1,
        "degroot": dg.tolist(), "trust": trust, "camps": camps, "labels": labels, "catchments": catch,
        "spread_hk": (hk_tr.max(1) - hk_tr.min(1)).tolist(),
        "spread_dg": (dg.max(1) - dg.min(1)).tolist(),
        "sweep": sweep,
    }
    json.dump(out, open("data.json", "w"))
    print("rounds to freeze", len(tr) - 1)
    print("camps", [(round(c, 3), n) for c, n in camps])
    print("gaps", np.round(np.diff([c for c, _ in camps]), 3))
    print("catchments", [(round(a, 3), round(b, 3), round(b - a, 3)) for a, b in catch])
    print("spread hk", np.round(out["spread_hk"], 3))
    print("spread dg", np.round(out["spread_dg"], 3))
    for s in sweep:
        print(s)
    # sanity: every pair of distinct final opinions is more than EPS apart
    u = sorted(set(np.round(final, 8)))
    print("min final gap", min(np.diff(u)))
    # the cold-open demo person
    i = 47
    win = np.abs(x0 - x0[i]) <= EPS
    print("demo person", i, x0[i], "window count", win.sum(), "mean", x0[win].mean())


if __name__ == "__main__":
    main()
