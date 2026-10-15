"""Simulation + exact numbers for episode 12 (confidence intervals). Run: python sim.py"""
import numpy as np
from scipy import stats
MU, SIGMA, N, RUNS = 0.25, 0.13, 5, 100
Z, T = 1.96, stats.t.ppf(0.975, N - 1)

def intervals(rng, k):
    x = rng.normal(MU, SIGMA, size=(k, N))
    return x, x.mean(1), x.std(1, ddof=1)

if __name__ == "__main__":
    print("t crit df=4:", T)
    print("exact z-coverage with n=5:", 2 * stats.t.cdf(Z, N - 1) - 1)
    print("exact t-coverage:", 2 * stats.t.cdf(T, N - 1) - 1)
    big = np.random.default_rng(0)
    _, m, s = intervals(big, 1_000_000)
    hz = np.abs(m - MU) <= Z * s / np.sqrt(N); ht = np.abs(m - MU) <= T * s / np.sqrt(N)
    print("1e6 sim z:", hz.mean(), " t:", ht.mean())
    print("mean t width:", (2 * T * s / np.sqrt(N)).mean(), "median", np.median(2*T*s/np.sqrt(N)))
    good = []
    for seed in range(4000):
        x, m, s = intervals(np.random.default_rng(seed), RUNS)
        hz = np.abs(m - MU) <= Z * s / np.sqrt(N); ht = np.abs(m - MU) <= T * s / np.sqrt(N)
        lo, hi = (m - T * s / np.sqrt(N)).min(), (m + T * s / np.sqrt(N)).max()
        if hz.sum() == 88 and ht.sum() == 95 and hz[:4].all() and lo > -0.02 and hi < 0.52:
            good.append((seed, lo, hi))
    print(len(good), good[:10])
