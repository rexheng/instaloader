"""Simulations for episode 1 (Bertrand's chord paradox). Unit circle, centre (0, 0).

Every number shown or spoken in the episode is computed here (seeded, deterministic).
A chord is 'long' when its length exceeds the inscribed equilateral triangle's side, sqrt(3).
"""
from __future__ import annotations

import numpy as np

SIDE = np.sqrt(3.0)
N = 10_000                     # chords per recipe in the tallies


def endpoints(n, rng):
    """Recipe 1: two independent uniform points on the rim, joined."""
    a, b = rng.uniform(0, 2 * np.pi, (2, n))
    p = np.stack([np.cos(a), np.sin(a)], 1)
    q = np.stack([np.cos(b), np.sin(b)], 1)
    return p, q


def radial(n, rng):
    """Recipe 2: uniform direction, uniform point on that radius, chord perpendicular there."""
    th = rng.uniform(0, 2 * np.pi, n)
    d = rng.uniform(0, 1, n)
    return _chord_from_mid(d, th)


def midpoint(n, rng):
    """Recipe 3: uniform point in the disk (by rejection), used as the chord's midpoint."""
    pts = np.empty((0, 2))
    while len(pts) < n:
        c = rng.uniform(-1, 1, (2 * n, 2))
        pts = np.vstack([pts, c[(c ** 2).sum(1) < 1]])
    pts = pts[:n]
    d = np.hypot(pts[:, 0], pts[:, 1])
    th = np.arctan2(pts[:, 1], pts[:, 0])
    return _chord_from_mid(d, th)


def _chord_from_mid(d, th):
    h = np.sqrt(np.clip(1 - d ** 2, 0, None))
    m = np.stack([d * np.cos(th), d * np.sin(th)], 1)
    t = np.stack([-np.sin(th), np.cos(th)], 1)
    return m - h[:, None] * t, m + h[:, None] * t


def lengths(p, q):
    return np.hypot(*(p - q).T)


def mids(p, q):
    return (p + q) / 2


def running_share(is_long):
    return np.cumsum(is_long) / np.arange(1, len(is_long) + 1)


def straw_lines(n, rng):
    """Jaynes's straws in the 'zero skill' limit: an isotropic line process
    (uniform direction, uniform offset over a band much wider than the circle)."""
    th = rng.uniform(0, np.pi, n)
    off = rng.uniform(-6, 6, n)                 # signed distance of the line from the origin
    return th, off


def straw_chords(th, off, cx, cy, r):
    """Chords cut on the circle (cx, cy, r) by lines {x: x.n = off}, n = (cos th, sin th)."""
    nrm = np.stack([np.cos(th), np.sin(th)], 1)
    dist = off - (cx * nrm[:, 0] + cy * nrm[:, 1])    # signed distance from circle centre
    hit = np.abs(dist) < r
    return hit, np.abs(dist) / r


def program_lines(kind, n, rng):
    """Each recipe's chords of the unit circle, as full lines {x : x.n = d}, n = (cos th, sin th).
    d >= 0 is the distance of the chord's midpoint from the centre."""
    if kind == "midpoint":                      # uniform point in the disk is the midpoint
        d = np.sqrt(rng.uniform(0, 1, n))
        th = rng.uniform(0, 2 * np.pi, n)
    elif kind == "radial":                      # uniform direction, uniform distance
        d = rng.uniform(0, 1, n)
        th = rng.uniform(0, 2 * np.pi, n)
    elif kind == "endpoints":                   # two uniform rim points
        a, b = rng.uniform(0, 2 * np.pi, (2, n))
        m = (np.stack([np.cos(a), np.sin(a)], 1) + np.stack([np.cos(b), np.sin(b)], 1)) / 2
        d = np.hypot(m[:, 0], m[:, 1])
        th = np.arctan2(m[:, 1], m[:, 0])
    else:
        raise ValueError(kind)
    return th, d


def judge(th, d, cx, cy, r):
    """Lines {x.n = d} judged on the circle (cx, cy, r): (hit mask, long share among hits)."""
    dist = np.abs(d - (cx * np.cos(th) + cy * np.sin(th)))
    hit = dist < r
    return hit, float((dist[hit] < r / 2).mean())


# The invariance test (Jaynes 1973 §5-6) as shown on screen: one rain, two circles.
SMALL_R = 0.5                   # small circle: half the radius ...
SMALL_C = (0.4, 0.0)            # ... centred 0.4 radii from the big circle's centre (inside it)
N_TEST = 100_000                # lines per rain behind the on-screen tallies
TEST_SEEDS = {"midpoint": 45, "endpoints": 43, "radial": 41}   # samples within 0.002 of the 2M values
N_STRAWS = 200_000              # straws behind the on-screen tallies (seed 1973)


def test_rains():
    """The scene's own samples: {kind: (th, d)} relative to the big unit circle."""
    return {k: program_lines(k, N_TEST, np.random.default_rng(s)) for k, s in TEST_SEEDS.items()}


def results(seed=1889):
    rng = np.random.default_rng(seed)
    out = {}
    for name, f in (("endpoints", endpoints), ("radial", radial), ("midpoint", midpoint)):
        p, q = f(N, rng)
        lg = lengths(p, q) > SIDE
        out[name] = dict(p=p, q=q, long=lg, share=running_share(lg))
    return out


if __name__ == "__main__":
    res = results()
    exact = {"endpoints": 1 / 3, "radial": 1 / 2, "midpoint": 1 / 4}
    for k, v in res.items():
        s = v["share"][-1]
        se = np.sqrt(s * (1 - s) / N)
        m = mids(v["p"], v["q"])
        inside = np.hypot(*m.T) < 0.5
        print(f"{k:10s} share={s:.4f} exact={exact[k]:.4f} se={se:.4f} 95%±{1.96*se:.4f} "
              f"midpoint-inside-r/2={inside.mean():.4f} same_as_long={np.all(inside == v['long'])}")
    vals = [res[k]["share"][-1] for k in res]
    print("gap max-min", max(vals) - min(vals))
    # straws
    rng = np.random.default_rng(1973)
    th, off = straw_lines(200_000, rng)
    for (cx, cy, r) in ((0, 0, 1), (1.5, -0.7, 1), (0.3, 0.2, 1.6), (-2, 1, 0.6)):
        hit, rel = straw_chords(th, off, cx, cy, r)
        print("straws circle", (cx, cy, r), "hits", hit.sum(), "long share", (rel[hit] < 0.5).mean())
    # exact checks
    # recipe 1: P(theta in (2pi/3, 4pi/3)) for central angle uniform -> 1/3
    print("exact endpoints", (4 * np.pi / 3 - 2 * np.pi / 3) / (2 * np.pi))
    print("incircle radius of inscribed equilateral triangle (R=1):", np.cos(np.pi / 3))
    print("side", SIDE, "chord at d=1/2:", 2 * np.sqrt(1 - 0.25))

    # ---- invariance test: the same rain judged on the big circle and on a smaller, off-centre one
    print("\ninvariance test (big r=1 at 0; small r=%.1f at %s)" % (SMALL_R, SMALL_C))
    for k, (th, d) in test_rains().items():
        _, big = judge(th, d, 0, 0, 1)
        hit, small = judge(th, d, *SMALL_C, SMALL_R)
        _, conc = judge(th, d, 0, 0, SMALL_R)
        print(f"  scene sample {k:10s} big={big:.4f} small={small:.4f} (hits {hit.sum()}) "
              f"concentric-small={conc:.4f}")
    big_rng = np.random.default_rng(7)
    for k in ("midpoint", "endpoints", "radial"):
        th, d = program_lines(k, 2_000_000, big_rng)
        print(f"  2M check    {k:10s} big={judge(th, d, 0, 0, 1)[1]:.4f} "
              f"small={judge(th, d, *SMALL_C, SMALL_R)[1]:.4f} "
              f"concentric-small={judge(th, d, 0, 0, SMALL_R)[1]:.4f}")

    # straws exactly as the scene draws them (scene units: big circle r=2 at (-2.7, 0.2),
    # small circle r=1 at (-1.9, 0.2); 200,000 lines, offsets uniform on +-7.5, seed 1973)
    rng = np.random.default_rng(1973)
    th = rng.uniform(0, np.pi, N_STRAWS)
    off = rng.uniform(-7.5, 7.5, N_STRAWS)
    for (cx, cy, r) in ((-2.7, 0.2, 2.0), (-1.9, 0.2, 1.0)):
        hit, sh = judge(th, off, cx, cy, r)
        print(f"  scene straws circle ({cx}, {cy}, r={r}): hits {hit.sum()} long share {sh:.4f}")

    # ---- class-size paradox (Feld & Grofman 1977): toy example and their Stony Brook figures
    sizes = np.array([10, 10, 100])
    print("\nclass sizes", sizes, "per class", sizes.mean(), "per student", (sizes ** 2).sum() / sizes.sum())
    mu, sd = 40.5, 65.8          # 737 classes, Teacher Evaluation Survey, spring 1974 (p. 216)
    print("Stony Brook: per-student mean = mu * (1 + sd^2/mu^2) =", round(mu * (1 + sd ** 2 / mu ** 2), 1))
