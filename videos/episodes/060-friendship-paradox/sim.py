"""Episode 60 numbers: Feld (1991) Fig. 1 network, the ring, the formula, a small
simulated outbreak, and the Facebook check.  Run: python sim.py"""
import numpy as np
from fractions import Fraction as F

NAMES = ["Betty", "Sue", "Alice", "Jane", "Pam", "Dale", "Carol", "Tina"]
# Feld 1991, Fig. 1 / Table 1 (reciprocated friendships, Marketville girls, Coleman 1961)
EDGES = [("Betty", "Sue"), ("Sue", "Alice"), ("Sue", "Dale"), ("Sue", "Pam"),
         ("Alice", "Jane"), ("Alice", "Pam"), ("Alice", "Dale"), ("Jane", "Dale"),
         ("Pam", "Carol"), ("Carol", "Tina")]
nbr = {n: [] for n in NAMES}
for a, b in EDGES:
    nbr[a].append(b); nbr[b].append(a)
k = {n: len(nbr[n]) for n in NAMES}

def stats(k, nbr, label):
    ks = np.array([k[n] for n in nbr])
    mu = F(int(ks.sum()), len(ks))
    var = F(int((ks**2).sum()), len(ks)) - mu**2
    pooled = F(int((ks**2).sum()), int(ks.sum()))
    per = [F(sum(k[m] for m in nbr[n]), len(nbr[n])) for n in nbr]
    print(f"--- {label}")
    print(" degrees", dict(k))
    print(" sum k", ks.sum(), " sum k^2", (ks**2).sum(), " n", len(ks), " edges", ks.sum() // 2)
    print(" mu", mu, float(mu), " var", var, float(var), " sd", float(var) ** .5)
    print(" pooled friend mean sum k^2/sum k =", pooled, float(pooled))
    print(" mu + var/mu =", mu + var / mu, " gap", var / mu, " rel gap", float(var / mu / mu))
    print(" mean of per-person friend means", float(sum(per) / len(per)))
    for n in nbr:
        fm = F(sum(k[m] for m in nbr[n]), len(nbr[n]))
        rel = "fewer" if k[n] < fm else ("more" if k[n] > fm else "equal")
        print(f"   {n:6s} k={k[n]} friends' mean={float(fm):.3f} -> {rel}")
    print(" histogram n_k", {d: int((ks == d).sum()) for d in sorted(set(ks))})
    print(" friend-slot histogram k*n_k", {d: int(d * (ks == d).sum()) for d in sorted(set(ks))})

stats(k, nbr, "Feld Fig. 1 (real)")

# ring of the same eight girls (hypothetical): each has exactly two friends
ring = {n: [NAMES[(i - 1) % 8], NAMES[(i + 1) % 8]] for i, n in enumerate(NAMES)}
stats({n: 2 for n in NAMES}, ring, "ring (hypothetical)")

# Facebook, Ugander et al. 2011: 68.7e9 edges, 721e6 users
mu_fb = 2 * 68.7e9 / 721e6
print("--- Facebook: mean degree", mu_fb, " friend mean 635 -> var/mu", 635 - mu_fb,
      " implied var", (635 - mu_fb) * mu_fb, " sd", ((635 - mu_fb) * mu_fb) ** .5,
      " ratio 635/190", 635 / 190)

# Marketville whole school (Feld): mean 2.7 vs 3.4 -> implied variance
print("--- Marketville 146 girls: implied var = (3.4-2.7)*2.7 =", (3.4 - 2.7) * 2.7)

# ---------------------------------------------------------------- simulated outbreak
# discrete-time SI: a random girl is infected on day 0; each day every sick girl infects
# each healthy friend independently with probability p.  Record the day each girl falls ill.
def outbreak(p, runs, rng):
    idx = {n: i for i, n in enumerate(NAMES)}
    A = [[idx[m] for m in nbr[n]] for n in NAMES]
    T = np.zeros((runs, 8))
    for r in range(runs):
        t = np.full(8, np.inf); s = rng.integers(8); t[s] = 0; day = 0
        while np.isinf(t).any():
            day += 1
            sick = np.where(t < day)[0]
            new = []
            for i in sick:
                for j in A[i]:
                    if np.isinf(t[j]) and rng.random() < p:
                        new.append(j)
            for j in new:
                t[j] = day
        T[r] = t
    return T

rng = np.random.default_rng(7)
for p in (0.2, 0.3, 0.5):
    T = outbreak(p, 20000, rng)
    mean_day = T.mean(axis=0)
    # random girl sensor: uniform over girls.  named friend: random girl names a random friend
    w_friend = np.zeros(8)
    for i, n in enumerate(NAMES):
        for m in nbr[n]:
            w_friend[NAMES.index(m)] += 1 / (8 * len(nbr[n]))
    w_edge = np.array([k[n] for n in NAMES]) / 20
    print(f"--- SI p={p}: mean sick day per girl", dict(zip(NAMES, mean_day.round(2))))
    print(f"    random girl {mean_day.mean():.2f}   named friend {w_friend @ mean_day:.2f}"
          f"   edge-end {w_edge @ mean_day:.2f}")
    print("    friend weights", dict(zip(NAMES, w_friend.round(3))))

# ---------------------------------------------------------------- variance as squared distances
# (the picture under the beam): distance of each girl from the balance point 2.5, squared
dev2 = {n: F(2 * k[n] - 5, 2) ** 2 for n in NAMES}
print("--- squared distances from 2.5:", {n: float(v) for n, v in dev2.items()},
      " sum", sum(dev2.values()), " mean", sum(dev2.values()) / 8,
      " check 2.5^2 + 1.25 =", F(5, 2) ** 2 + sum(dev2.values()) / 8, "= mean k^2 =", F(60, 8))

# ---------------------------------------------------------------- Christakis & Fowler fits
# Cumulative logistic c / (1 + exp(-(t - m - shift*[random]) / s)) with shared c and s,
# least squares on the redrawn NPMLE step curves (0.5-day grid, days 0-125.5).
import json
from pathlib import Path
from scipy.optimize import least_squares

CF = json.loads((Path(__file__).resolve().parent / "cf_fig3_digitized.json").read_text())


def step(group, t):
    lev = np.zeros_like(t)
    for d, c in CF[group]["steps_day_cases"]:
        lev[t >= d] = 100 * c / CF[group]["n"]
    return lev


t = np.arange(0, 126, 0.5)
yf, yr = step("friends", t), step("random", t)


def resid(c, m, s, shift):
    return np.r_[c / (1 + np.exp(-(t - m) / s)) - yf, c / (1 + np.exp(-(t - m - shift) / s)) - yr]


free = least_squares(lambda p: resid(*p), [7.7, 60, 15, 14]).x
fixed = least_squares(lambda p: resid(*p, 13.9), [7.7, 60, 15]).x
print("--- C&F logistic, shift free: c=%.3f m=%.2f s=%.2f shift=%.1f days" % tuple(free))
print("    shift fixed at the published 13.9: c=%.3f m=%.2f s=%.2f  (used on screen)" % tuple(fixed))
ay = 2.8
tf = fixed[1] + fixed[2] * np.log(ay / (fixed[0] - ay))
print(f"    arrow at {ay}%: friends fit day {tf:.1f}, random fit day {tf + 13.9:.1f}")
