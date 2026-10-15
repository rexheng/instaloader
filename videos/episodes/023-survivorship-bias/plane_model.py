"""Geometry of the stylised bomber + the simulated campaigns (episode 23).
Plane-local units, nose up. Everything is deterministic (seeded)."""
import numpy as np
from matplotlib.path import Path

def _round_rect(x0, x1, y0, y1, r, n=8):
    pts = []
    for cx, cy, a0 in ((x1 - r, y1 - r, 0), (x0 + r, y1 - r, 90), (x0 + r, y0 + r, 180), (x1 - r, y0 + r, 270)):
        for a in np.linspace(a0, a0 + 90, n):
            t = np.radians(a); pts.append((cx + r * np.cos(t), cy + r * np.sin(t)))
    return np.array(pts)

def fuselage():
    # nose rounded at top, tapering tail
    top = [(0.36 * np.cos(t), 2.45 + 0.55 * np.sin(t)) for t in np.linspace(0, np.pi, 14)]
    pts = top + [(-0.36, 1.2), (-0.36, -0.6), (-0.26, -2.3), (-0.12, -2.75), (0.12, -2.75), (0.26, -2.3), (0.36, -0.6), (0.36, 1.2)]
    return np.array(pts[::-1])

def wing(side):
    s = side
    return np.array([(s * 0.36, 0.95), (s * 4.7, 0.62), (s * 4.85, 0.45), (s * 4.75, 0.12), (s * 0.36, -0.45)])

ENGINE_X = (-2.75, -1.45, 1.45, 2.75)
def engine(x):
    return _round_rect(x - 0.22, x + 0.22, -0.05, 1.5, 0.18)

def tailplane(side):
    s = side
    return np.array([(s * 0.26, -1.85), (s * 1.75, -2.05), (s * 1.8, -2.3), (s * 1.7, -2.5), (s * 0.2, -2.5)])

REGIONS = ["engines", "fuselage", "wings", "tail"]
def region_polys():
    return {"engines": [engine(x) for x in ENGINE_X], "fuselage": [fuselage()],
            "wings": [wing(-1), wing(1)], "tail": [tailplane(-1), tailplane(1)]}

def classify(xy):
    """region index per point (priority engines > fuselage > wings > tail), -1 outside."""
    polys = region_polys(); out = np.full(len(xy), -1)
    for k, r in enumerate(REGIONS):
        m = np.zeros(len(xy), bool)
        for p in polys[r]:
            m |= Path(p).contains_points(xy)
        out[(out == -1) & m] = k
    return out

def area_shares(n=400_000, seed=1):
    rng = np.random.default_rng(seed)
    xy = rng.uniform([-5, -2.9], [5, 3.1], size=(n, 2))
    c = classify(xy); c = c[c >= 0]
    return np.bincount(c, minlength=4) / len(c)

SURVIVE = np.array([0.59, 0.94, 0.97, 0.94])   # per-hit survival (Wald / Mangel-Samaniego worked example)

def hits(n, rng):
    pts = []
    while len(pts) < n:
        xy = rng.uniform([-5, -2.9], [5, 3.1], size=(4 * n, 2))
        c = classify(xy); xy = xy[c >= 0]
        pts.extend(xy.tolist())
    xy = np.array(pts[:n]); return xy, classify(xy)

def campaign(seed, armored=None, n=400):
    rng = np.random.default_rng(seed)
    xy, reg = hits(n, rng)
    q = SURVIVE.copy()
    if armored is not None:
        q[REGIONS.index(armored)] = 1.0
    survived = rng.random(n) < q[reg]
    return xy, reg, survived

if __name__ == "__main__":
    sh = area_shares(); print("area shares", dict(zip(REGIONS, sh.round(4))))
    print("expected per 400:", (400 * sh).round(1))
    print("expected lost", 400 * (sh * (1 - SURVIVE)).sum(), "armor wings", 400*(sh*(1-SURVIVE)).sum()-400*sh[2]*0.03, "armor engines", 400*(sh*(1-SURVIVE)).sum()-400*sh[0]*.41)
    for seed in range(12):
        xy, reg, s = campaign(seed)
        seen = np.bincount(reg[s], minlength=4); lost = np.bincount(reg[~s], minlength=4)
        print(seed, "seen", seen, "lost hits", lost, "lost", (~s).sum(), "ratio", (seen / (400 * sh)).round(2))

def scan():
    sh = area_shares()
    for seed in range(60):
        xy, reg, s = campaign(seed)
        seen = np.bincount(reg[s], minlength=4)
        r = seen / (400 * sh)
        if r.max() < 1.0 and abs(r[0]-0.59) < 0.04 and abs(r[1]-.94)<.04 and abs(r[2]-.97)<.03 and abs(r[3]-.94)<.05:
            print(seed, seen, (~s).sum(), r.round(3))
