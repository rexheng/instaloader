"""Data prep for episode 26 (run once; writes iowa_data.json next to this file).

    python prep.py /path/to/us-atlas-3.0.1/counties-10m.json

1. Real geometry: Iowa's 99 county outlines (us-atlas 3.0.1, Census cartographic boundaries),
   projected equirectangular at 42 deg N, plus queen-free rook adjacency from shared arcs.
2. SIMULATED county values (shown on screen as "simulated"): two smooth spatial fields
   combined so the county-level Pearson r equals 0.346, the real Iowa value reported by
   Openshaw (1984, Table 7).
3. Zonings into six contiguous regions: east-west bands, north-south strips, an
   Openshaw-style automated zoning procedure (AZP: move one border county at a time,
   keep every region connected, keep the move if r improves) run to maximise and to
   minimise the regional r, and 10,000 random contiguous zonings.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
R_COUNTY = 0.346
K = 6
MIN_SIZE = 5


def decode(topo):
    sx, sy = topo["transform"]["scale"]
    tx, ty = topo["transform"]["translate"]
    arcs = []
    for a in topo["arcs"]:
        x = y = 0
        pts = []
        for dx, dy in a:
            x += dx
            y += dy
            pts.append((x * sx + tx, y * sy + ty))
        arcs.append(pts)
    return arcs


def ring(arcs, idx):
    pts = []
    for i in idx:
        a = arcs[i] if i >= 0 else arcs[~i][::-1]
        pts.extend(a if not pts else a[1:])
    return pts


def main(path):
    topo = json.load(open(path))
    arcs = decode(topo)
    geoms = [g for g in topo["objects"]["counties"]["geometries"] if g["id"].startswith("19")]
    geoms.sort(key=lambda g: g["id"])
    assert len(geoms) == 99
    cosl = np.cos(np.radians(42.0))
    polys, arcsets, names = [], [], []
    for g in geoms:
        rings = g["arcs"] if g["type"] == "Polygon" else [r for p in g["arcs"] for r in p]
        outer = max((ring(arcs, r) for r in rings), key=len)
        polys.append([(lon * cosl, lat) for lon, lat in outer])
        arcsets.append({(i if i >= 0 else ~i) for r in rings for i in r})
        names.append(g["properties"]["name"])
    # normalise to a box centred on 0
    allp = np.array([p for poly in polys for p in poly])
    lo, hi = allp.min(0), allp.max(0)
    c = (lo + hi) / 2
    polys = [[(x - c[0], y - c[1]) for x, y in poly] for poly in polys]
    n = 99
    adj = [set() for _ in range(n)]
    owner = defaultdict(list)
    for i, s in enumerate(arcsets):
        for a in s:
            owner[a].append(i)
    for a, os_ in owner.items():
        for i in os_:
            for j in os_:
                if i != j:
                    adj[i].add(j)
    cen = np.array([np.mean(p, axis=0) for p in polys])

    # ---------------- simulated values: smooth fields, exact county r
    rng = np.random.default_rng(SEED)
    W = np.zeros((n, n))
    for i in range(n):
        for j in adj[i]:
            W[i, j] = 1
    def smooth(z, it):
        for _ in range(it):
            z = 0.5 * z + 0.5 * (W @ z) / W.sum(1)
        return z
    trend = cen @ rng.normal(size=2)
    z1 = smooth(rng.normal(size=n), 6) + 0.25 * trend / trend.std()
    z2 = smooth(rng.normal(size=n), 6) + 0.25 * (cen @ rng.normal(size=2)) / trend.std()
    z1 = (z1 - z1.mean()) / z1.std()
    z2 = z2 - z2.mean()
    z2 -= (z2 @ z1) / (z1 @ z1) * z1
    z2 /= z2.std()
    zy = R_COUNTY * z1 + np.sqrt(1 - R_COUNTY ** 2) * z2
    x = 15.5 + 2.4 * z1          # % aged 60+   (simulated)
    y = 55.0 + 7.0 * zy           # % Republican (simulated)
    assert abs(np.corrcoef(x, y)[0, 1] - R_COUNTY) < 1e-9

    def regional_r(assign):
        mx = np.array([x[assign == k].mean() for k in range(K)])
        my = np.array([y[assign == k].mean() for k in range(K)])
        return float(np.corrcoef(mx, my)[0, 1])

    def connected(members):
        members = set(members)
        if not members:
            return False
        start = next(iter(members))
        seen, stack = {start}, [start]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v in members and v not in seen:
                    seen.add(v)
                    stack.append(v)
        return len(seen) == len(members)

    def quantile_zoning(coord):
        order = np.argsort(coord)
        a = np.zeros(n, int)
        for k, chunk in enumerate(np.array_split(order, K)):
            a[chunk] = k
        return a

    bands = quantile_zoning(-cen[:, 1])     # north to south
    strips = quantile_zoning(cen[:, 0])     # west to east
    for a in (bands, strips):
        assert all(connected(np.where(a == k)[0]) for k in range(K))

    def azp(start, sign, rng):
        a = start.copy()
        cur = sign * regional_r(a)
        traj = [a.copy()]
        improved = True
        while improved:
            improved = False
            for i in rng.permutation(n):
                src = a[i]
                if (a == src).sum() <= MIN_SIZE:
                    continue
                best, best_k = cur, None
                rest = np.where(a == src)[0]
                if not connected(rest[rest != i]):
                    continue
                for k in {a[j] for j in adj[i]} - {src}:
                    a[i] = k
                    v = sign * regional_r(a)
                    a[i] = src
                    if v > best + 1e-12:
                        best, best_k = v, k
                if best_k is not None:
                    a[i] = best_k
                    cur = best
                    traj.append(a.copy())
                    improved = True
        return a, traj

    # random contiguous zonings (seeded region growing)
    rng3 = np.random.default_rng(11)
    rand_r, rand_a = [], []
    while len(rand_r) < N_RAND:
        a = -np.ones(n, int)
        seeds = rng3.choice(n, K, replace=False)
        a[seeds] = np.arange(K)
        free = n - K
        while free:
            k = rng3.integers(K)
            front = [j for i in np.where(a == k)[0] for j in adj[i] if a[j] < 0]
            if not front:
                if all(not [j for i in np.where(a == q)[0] for j in adj[i] if a[j] < 0] for q in range(K)):
                    break
                continue
            a[front[rng3.integers(len(front))]] = k
            free -= 1
        if free:
            continue
        rand_r.append(regional_r(a))
        if len(rand_a) < 6:
            rand_a.append(a.copy())
    rand_r = np.array(rand_r)
    if QUICK:
        return {"seed": SEED, "r_bands": regional_r(bands), "r_strips": regional_r(strips),
                "rand_r_mean": rand_r.mean(), "rand_r_sd": rand_r.std(),
                "rand_r_p": np.percentile(rand_r, [2.5, 97.5]).round(2).tolist()}

    # AZP, best of several starting zonings (Openshaw used the best of five)
    rng2 = np.random.default_rng(3)
    starts = [bands, strips] + rand_a[:3]
    runs = [azp(s0, +1, rng2) for s0 in starts]
    amax, tmax = max(runs, key=lambda t: regional_r(t[0]))
    if regional_r(runs[0][0]) > regional_r(amax) - 0.005:      # prefer the climb from bands
        amax, tmax = runs[0]
    runs = [azp(s0, -1, rng2) for s0 in [amax] + starts]
    amin, tmin = min(runs, key=lambda t: regional_r(t[0]))
    if regional_r(runs[0][0]) < regional_r(amin) + 0.005:      # prefer the descent from amax
        amin, tmin = runs[0]

    def sub(traj, m):
        idx = np.unique(np.linspace(0, len(traj) - 1, min(m, len(traj))).round().astype(int))
        return [traj[i].tolist() for i in idx]

    def decomposition(a):
        """Sum-of-products identity: total = within + between (exact)."""
        mx = np.array([x[a == k].mean() for k in range(K)])
        my = np.array([y[a == k].mean() for k in range(K)])
        tot = np.sum((x - x.mean()) * (y - y.mean()))
        wit = sum(np.sum((x[a == k] - mx[k]) * (y[a == k] - my[k])) for k in range(K))
        btw = sum((a == k).sum() * (mx[k] - x.mean()) * (my[k] - y.mean()) for k in range(K))
        assert abs(tot - wit - btw) < 1e-6 * abs(tot)
        return {"total": tot, "within": wit, "between": btw}

    def proj(pts):
        return [(lon * cosl - c[0], lat - c[1]) for lon, lat in pts]
    shared = {}
    outline = []
    for a, os_ in owner.items():
        if len(os_) == 2:
            i, j = sorted(os_)
            shared.setdefault(f"{i}-{j}", []).append(proj(arcs[a]))
        elif len(os_) == 1:
            outline.append(proj(arcs[a]))

    out = {
        "shared": shared, "outline": outline,
        "traj_max_dec": [decomposition(np.array(t)) for t in sub(tmax, 40)],
        "traj_min_dec": [decomposition(np.array(t)) for t in sub(tmin, 40)],
        "seed": SEED, "names": names, "polys": polys, "centroids": cen.tolist(),
        "adj": [sorted(s) for s in adj], "x": x.tolist(), "y": y.tolist(),
        "r_county": float(np.corrcoef(x, y)[0, 1]),
        "bands": bands.tolist(), "strips": strips.tolist(),
        "r_bands": regional_r(bands), "r_strips": regional_r(strips),
        "amax": amax.tolist(), "amin": amin.tolist(),
        "r_max": regional_r(amax), "r_min": regional_r(amin),
        "traj_max": sub(tmax, 40), "traj_min": sub(tmin, 40),
        "traj_max_r": [regional_r(np.array(t)) for t in sub(tmax, 40)],
        "traj_min_r": [regional_r(np.array(t)) for t in sub(tmin, 40)],
        "rand_r_mean": float(rand_r.mean()), "rand_r_sd": float(rand_r.std()),
        "rand_hist": np.histogram(rand_r, bins=20, range=(-1, 1))[0].tolist(),
        "rand_r_p": np.percentile(rand_r, [2.5, 50, 97.5]).tolist(),
        "dec": {nm: decomposition(np.array(a)) for nm, a in
                (("bands", bands), ("strips", strips), ("amax", amax), ("amin", amin))},
        "sizes": {nm: np.bincount(np.array(a), minlength=K).tolist() for nm, a in
                  (("bands", bands), ("strips", strips), ("amax", amax), ("amin", amin))},
    }
    return out


QUICK = False
N_RAND = 10000
if __name__ == "__main__":
    SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    if sys.argv[-1] == "quick":
        QUICK, N_RAND = True, 1500
        print(main(sys.argv[1]))
        sys.exit()
    o = main(sys.argv[1])
    for kk in ("seed", "r_county", "r_bands", "r_strips", "r_max", "r_min", "rand_r_mean",
               "rand_r_sd", "rand_r_p", "sizes"):
        print(kk, o[kk])
    print("dec", {k: {a: round(b / v["total"], 3) for a, b in v.items()} for k, v in o["dec"].items()})
    print("traj lens", len(o["traj_max"]), len(o["traj_min"]))
    if len(sys.argv) > 3:
        json.dump(o, open(HERE / "iowa_data.json", "w"))
