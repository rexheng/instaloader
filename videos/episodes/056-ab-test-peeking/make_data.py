"""Simulated A/A tests for episode 56 (all data shown on screen is simulated).
1000 tests, two identical buttons with true click rate 10 %, 500 visitors per button per day,
20 daily looks, pooled two-proportion z-test."""
import numpy as np

P, N_DAY, DAYS, T = 0.10, 500, 20, 1000
Z_CRIT = 1.959964
t = np.arange(1, DAYS + 1)


def run(seed):
    rng = np.random.default_rng(seed)
    a = rng.binomial(N_DAY, P, (T, DAYS)).cumsum(1)
    b = rng.binomial(N_DAY, P, (T, DAYS)).cumsum(1)
    n = N_DAY * t
    pa, pb = a / n, b / n
    pool = (a + b) / (2 * n)
    se = np.sqrt(pool * (1 - pool) * 2 / n)
    return (pb - pa) / se


def obf_c():
    rng = np.random.default_rng(0)
    S = rng.standard_normal((1_000_000, DAYS)).cumsum(1)
    Z = S / np.sqrt(t)
    lo, hi = 1.9, 2.5
    for _ in range(40):
        c = (lo + hi) / 2
        r = (np.abs(Z) > c * np.sqrt(DAYS / t)).any(1).mean()
        lo, hi = (c, hi) if r > 0.05 else (lo, c)
    return (lo + hi) / 2


def first_cross(Z, bound):
    cr = np.abs(Z) > bound
    return np.where(cr.any(1), cr.argmax(1), -1)


if __name__ == "__main__":
    C = obf_c()
    obf = C * np.sqrt(DAYS / t)
    print("OBF c", C)
    for seed in range(400):
        Z = run(seed)
        f = first_cross(Z, Z_CRIT)
        peek = (f >= 0).sum()
        once = (np.abs(Z[:, -1]) > Z_CRIT).sum()
        fo = first_cross(Z, obf)
        ob = (fo >= 0).sum()
        d1, d2 = (f == 0).sum(), (f == 1).sum()
        # hero: first crossing upward on day 7, finishes well inside
        hero = [i for i in range(T) if f[i] == 6 and Z[i, 6] > 0 and abs(Z[i, -1]) < 0.8
                and Z[i, 6] < 2.4 and np.abs(Z[i, :6]).max() < 1.7]
        if 244 <= peek <= 252 and 47 <= once <= 53 and 47 <= ob <= 53 and 45 <= d1 <= 55 \
                and 28 <= d2 <= 38 and hero:
            print("seed", seed, "peek", peek, "once", once, "obf", ob, "d1", d1, "d2", d2, "hero", hero[:3])
            np.savez("data.npz", Z=Z, first=f, first_obf=fo, obf=obf, hero=hero[0], seed=seed, C=C)
            print("slices", [(f == k).sum() for k in range(DAYS)])
            print("obf slices", [(fo == k).sum() for k in range(DAYS)])
            print("hero z", np.round(Z[hero[0]], 2))
            break
