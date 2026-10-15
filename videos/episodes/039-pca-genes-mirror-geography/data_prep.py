"""Simulated genotypes for episode 39 (deterministic). Writes data.npz.

Model (simulated, not real data): N people placed around 16 rough country centre points;
M SNPs, each with a base allele frequency p ~ U(0.1, 0.9) that tilts linearly across the
map (gradient ~ N(0, 0.025) per 1000 km in each direction); genotypes ~ Binomial(2, f).
Coastline: Natural Earth 1:50m land (public domain) via world-atlas@2.0.2 land-50m.json.
    python3 data_prep.py /path/to/land-50m.json
"""
import json
import sys

import numpy as np

C = {"PT": (39.6, -8.0), "ES": (40.3, -3.7), "FR": (46.6, 2.4), "UK": (52.6, -1.6),
     "IE": (53.2, -8.0), "NL": (52.2, 5.6), "DE": (51.0, 10.3), "CH": (46.8, 8.2),
     "IT": (42.8, 12.6), "PL": (52.1, 19.4), "CZ": (49.8, 15.5), "HU": (47.1, 19.5),
     "RO": (45.9, 24.9), "GR": (39.5, 22.0), "SE": (59.5, 15.5), "NO": (61.0, 9.5)}
N, M, AMP, SEED = 1000, 10000, 0.025, 7
LAT0, LON0 = 49.0, 9.0
KX, KY = np.cos(np.radians(48)) * 111.0, 111.0


def proj(lon, lat):
    return (np.asarray(lon) - LON0) * KX, (np.asarray(lat) - LAT0) * KY


def coast(path, lon0=-12, lon1=32, lat0=35.5, lat1=64, minlen=12, step=2):
    t = json.load(open(path))
    sc, tr = t["transform"]["scale"], t["transform"]["translate"]
    lines = []
    for a in t["arcs"]:
        a = np.cumsum(np.array(a, float), 0) * sc + tr
        ins = (a[:, 0] >= lon0) & (a[:, 0] <= lon1) & (a[:, 1] >= lat0) & (a[:, 1] <= lat1)
        cur = []
        for p, i in zip(a, ins):
            if i:
                cur.append(p)
            else:
                if len(cur) >= minlen:
                    lines.append(np.array(cur))
                cur = []
        if len(cur) >= minlen:
            lines.append(np.array(cur))
    out = []
    for l in lines:
        l = np.vstack([l[::step], l[-1:]])
        x, y = proj(l[:, 0], l[:, 1])
        out.append(np.c_[x, y])
    return out


def main(land):
    rng = np.random.default_rng(SEED)
    codes = list(C)
    cid = rng.integers(0, len(codes), N)
    lat = np.array([C[codes[i]][0] for i in cid]) + rng.normal(0, 0.7, N)
    lon = np.array([C[codes[i]][1] for i in cid]) + rng.normal(0, 1.0, N)
    X, Y = proj(lon, lat)
    sx, sy = (X - X.mean()) / 1000, (Y - Y.mean()) / 1000
    p = rng.uniform(0.1, 0.9, M)
    gx, gy = rng.normal(0, AMP, M), rng.normal(0, AMP, M)
    f = np.clip(p[None] + sx[:, None] * gx[None] + sy[:, None] * gy[None], 0.01, 0.99)
    G = rng.binomial(2, f).astype(float)

    def fit_err(F):
        A = np.c_[np.ones(N), F]
        bx = np.linalg.lstsq(A, X, rcond=None)[0]
        by = np.linalg.lstsq(A, Y, rcond=None)[0]
        return float(np.median(np.hypot(A @ bx - X, A @ by - Y)))

    base = float(np.median(np.hypot(X - X.mean(), Y - Y.mean())))
    two = G[:, [0, 1]]
    e_two = fit_err(two)
    s = G.sum(1)
    e_sum = fit_err(s[:, None])
    halves = np.c_[G[:, :M // 2].sum(1), G[:, M // 2:].sum(1)]
    e_half = fit_err(halves)
    q = G.mean(0) / 2
    Z = (G - G.mean(0)) / np.sqrt(2 * q * (1 - q))       # centre + scale, as smartpca does
    U, S, Vt = np.linalg.svd(Z, full_matrices=False)
    ev = S ** 2
    frac = ev / ev.sum()
    PC = U[:, :2] * S[:2]
    e_pc = fit_err(PC)
    # orthogonal Procrustes (rotation/reflection + scale) onto the map, for display only
    P0 = PC - PC.mean(0)
    T0 = np.c_[X - X.mean(), Y - Y.mean()]
    u, sv, vt = np.linalg.svd(P0.T @ T0)
    R = u @ vt
    scale = sv.sum() / (P0 ** 2).sum()
    PCmap = scale * P0 @ R + [X.mean(), Y.mean()]
    ang = np.degrees(np.arctan2(R[0, 1], R[0, 0]))
    # how much one SNP's frequency changes from SW to NE corner (the "tilt")
    j = 0
    # signed tilt of each SNP along latitude (per 1000 km) for the sign illustration
    print(f"half {e_half:.0f} base {base:.0f}  two {e_two:.0f}  sum {e_sum:.0f}  pc {e_pc:.0f}  "
          f"frac {100*frac[0]:.2f}% {100*frac[1]:.2f}% {100*frac[2]:.2f}%  rot {ang:.1f} det {np.linalg.det(R):+.0f}")
    print("snp0 p", p[0], "gx gy", gx[0], gy[0], " snp1", p[1], gx[1], gy[1])
    print("frac of SNPs with gy>0:", (gy > 0).mean())
    lines = coast(land)
    np.savez_compressed("data.npz", X=X, Y=Y, cid=cid, codes=np.array(codes), two=two, s=s,
                        PC=PC, PCmap=PCmap, frac=frac, base=base, e_two=e_two, e_sum=e_sum, halves=halves, e_half=e_half,
                        e_pc=e_pc, gx=gx, gy=gy, p=p,
                        coast=np.array(lines, dtype=object), allow_pickle=True)


if __name__ == "__main__":
    main(sys.argv[1])
