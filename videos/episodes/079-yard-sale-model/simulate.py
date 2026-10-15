"""Simulated data for episode 79 (yard-sale model). Deterministic; writes sim.npz.

Room: N=500 agents, $100 each. Each round everyone is paired at random once and a fair
coin picks the winner.
  fixed : loser pays $10 (if the loser has it)                  [naive build]
  yard  : stake = 1/5 of the poorer player's wealth              [Chakraborti 2002 / Hayes 2002]
  tax   : yard rule, then each round w <- 0.99 w + 0.01 mean(w)  [redistribution]
"""
import numpy as np

N, F = 500, 0.2


def run(mode, rounds, seed, w0=None, tax=0.0, stake=10.0):
    rng = np.random.default_rng(seed)
    w = np.full(N, 100.0) if w0 is None else w0.copy()
    out = [np.sort(w)]
    for _ in range(rounds):
        perm = rng.permutation(N)
        a, b = perm[:N // 2], perm[N // 2:]
        a_wins = rng.random(N // 2) < 0.5
        if mode == "fixed":
            loser = np.where(a_wins, w[b], w[a])
            d = np.where(loser >= stake, stake, 0.0)
        else:
            d = F * np.minimum(w[a], w[b])
        sg = np.where(a_wins, 1.0, -1.0)
        w[a] += sg * d
        w[b] -= sg * d
        if tax:
            w = (1 - tax) * w + tax * w.mean()
        out.append(np.sort(w))
    return w, np.array(out)


def gini(w):
    w = np.sort(w); n = len(w); i = np.arange(1, n + 1)
    return 2 * np.sum(i * w) / (n * w.sum()) - (n + 1) / n


if __name__ == "__main__":
    _, fixed = run("fixed", 1000, seed=1)
    wy, yard = run("yard", 1000, seed=1)
    _, taxed = run("tax", 600, seed=11, w0=wy, tax=0.01)
    np.savez_compressed("sim.npz", fixed=fixed, yard=yard, taxed=taxed)
    half = lambda h: h[:, :N // 2].sum(axis=1)
    for name, h in (("fixed", fixed), ("yard", yard), ("taxed", taxed)):
        hh = half(h)
        print(name, "poorer half $ at", [(r, round(hh[r], 2)) for r in (0, 50, 100, 200, 300, 500, len(h) - 1)])
        print("   max wealth at", [(r, round(h[r, -1])) for r in (0, 50, 100, 150, 200, 300, 500, len(h) - 1)])
        print("   top5 share end", round(h[-1, -5:].sum() / 5e4, 3), "gini end", round(gini(h[-1]), 3),
              "n>100", int((h[-1] > 100).sum()), "median", h[-1, 249:251].mean())
