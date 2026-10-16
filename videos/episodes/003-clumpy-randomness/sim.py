"""Episode 3 data: one uniform-random map (A) and one rule-based 'even' map (B).

Both: 537 points in a 24 x 24 square (unit = one square's side), counted per unit square.
A: every point uniform and independent (homogeneous Poisson-like / multinomial counts).
B: random sequential addition with a minimum spacing (no two dots closer than D_MIN).
Writes sim_data.npz used by scene.py.  Deterministic.
"""
import math
import numpy as np

N, G = 537, 24
LAM = N / G**2


def counts(pts):
    ij = np.floor(pts).astype(int).clip(0, G - 1)
    c = np.zeros((G, G), int)
    np.add.at(c, (ij[:, 0], ij[:, 1]), 1)
    return c


def hist(c, top=5):
    h = [int((c == k).sum()) for k in range(top)]
    h.append(int((c >= top).sum()))
    return h


def poisson_expected(lam=LAM, n=G**2, top=5):
    p = [math.exp(-lam) * lam**k / math.factorial(k) for k in range(top)]
    return [n * x for x in p] + [n * (1 - sum(p))]


def uniform_map(seed):
    return np.random.default_rng(seed).uniform(0, G, size=(N, 2))


def even_map(seed, d):
    rng = np.random.default_rng(seed)
    pts = []
    tries = 0
    while len(pts) < N:
        p = rng.uniform(0, G, 2)
        tries += 1
        if all((p[0] - q[0])**2 + (p[1] - q[1])**2 >= d * d for q in pts):
            pts.append(p)
        if tries > 2_000_000:
            raise RuntimeError("too dense")
    return np.array(pts)


def aimed_map(seed, k=3, sigma=2.0):
    """'Aimed' bombs: k aim points (uniform in the middle of the map), each hit normal around a
    randomly chosen aim point with s.d. sigma squares; hits off the map are re-drawn."""
    rng = np.random.default_rng(seed)
    aims = rng.uniform(4, G - 4, size=(k, 2))
    pts = []
    while len(pts) < N:
        p = aims[rng.integers(k)] + rng.normal(0, sigma, 2)
        if 0 <= p[0] < G and 0 <= p[1] < G:
            pts.append(p)
    return np.array(pts), aims


def misfit(h, exp=None):
    """Pearson chi-squared of a 0..4,5+ histogram against 576 * Poisson(537/576)."""
    exp = np.array(poisson_expected() if exp is None else exp)
    return float(((np.array(h) - exp) ** 2 / exp).sum())


def null_misfits(n=20000, seed=2026):
    """Misfit of n pure-chance maps (537 uniform hits each, counted in the 576 squares)."""
    rng = np.random.default_rng(seed)
    exp = np.array(poisson_expected())
    out = np.empty(n)
    for i in range(n):
        c = np.bincount(rng.integers(0, G * G, size=N), minlength=G * G)
        h = np.array([(c == k).sum() for k in range(5)] + [(c >= 5).sum()])
        out[i] = ((h - exp) ** 2 / exp).sum()
    return out


SEED_A, SEED_B, D_MIN = 0, 1, 0.8
SEED_AIM, SEED_NULL = 0, 2026


def save(path="sim_data.npz"):
    a = uniform_map(SEED_A)
    b = even_map(SEED_B, D_MIN)
    aim, aims = aimed_map(SEED_AIM)
    null = null_misfits(seed=SEED_NULL)
    np.savez(path, a=a, b=b, aimed=aim, aims=aims, null=null)
    return a, b


if __name__ == "__main__":
    import os
    a, b = save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sim_data.npz"))
    print("map A counts 0..5+:", hist(counts(a)), " >=3:", int((counts(a) >= 3).sum()),
          " >=2:", int((counts(a) >= 2).sum()))
    print("map B counts 0..5+:", hist(counts(b)), " min pair distance:",
          round(min(np.hypot(*(b[i] - b[j])) for i in range(len(b)) for j in range(i)), 3))
    d = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sim_data.npz"))
    print("aimed map counts 0..5+:", hist(counts(d["aimed"])), " aim points:",
          d["aims"].round(1).tolist(), " misfit", round(misfit(hist(counts(d["aimed"]))), 1))
    exp = poisson_expected()
    ca = hist(counts(a))
    parts = [(o - e) ** 2 / e for o, e in zip(ca, exp)]
    print("map A misfit per bar:", [round(x, 3) for x in parts], " total", round(sum(parts), 3))
    print("map B misfit:", round(misfit(hist(counts(b))), 1))
    nl = d["null"]
    print(f"{len(nl)} pure-chance maps: share with misfit >= 2.0 = {(nl >= 2.0).mean():.4f}"
          f"  (Monte Carlo s.e. {np.sqrt(0.75 * 0.25 / len(nl)):.4f}); max {nl.max():.1f};"
          f" share >= 16: {(nl >= 16).mean():.4f}")
    print("lambda", LAM)
    print("Poisson expected (0..4,5+):", [round(x, 2) for x in exp])
    print("expected >=3:", round(sum(exp[3:]), 2), " expected empty frac", math.exp(-LAM))
    # binomial check
    p0 = (575 / 576) ** 537
    print("binomial (575/576)^537 =", p0, " x576 =", 576 * p0, " e^-lam =", math.exp(-LAM))
    # chi2 check of Clarke table
    obs = [229, 211, 93, 35, 7, 1]
    clarke_exp = [226.74, 211.39, 98.54, 30.62, 7.14, 1.57]
    chi = sum((o - e)**2 / e for o, e in zip(obs, clarke_exp))
    from scipy.stats import chi2
    print("chi2 Clarke 6 cells", chi, "p(df=4)", chi2.sf(chi, 4))
    chi5 = sum((o - e)**2 / e for o, e in zip(obs[:4] + [8], clarke_exp[:4] + [8.71]))
    print("chi2 merged 4+:", chi5, chi2.sf(chi5, 3), chi2.sf(chi5, 4))
    print("chi2_4 tail at 2.0 (map A):", round(chi2.sf(2.0, 4), 4), " map B:", chi2.sf(271.7, 4))
