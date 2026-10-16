"""Episode 3 real data: V-1 impact sites inside the London County Council boundary.

Source: L. Shaw (2025), "V1 and V2 impact sites in London", Zenodo,
doi:10.5281/zenodo.14883986 (CC-BY 4.0), file V1-impacts.csv (887 rows, md5
6fc152898e06207014322ca4481ccbf6), digitised from the LCC bomb damage maps (Ward 2015) and
analysed in Shaw & Shaw, "The flying bomb and the actuary", Significance 16(5) (2019).

Coordinates are British National Grid metres.  Writes real_data.npz used by scene.py and
prints every number the episode quotes from this file.  Deterministic.
"""
import csv
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
# Shaw & Shaw's rectangle re-creating Clarke's 144 km2 south-London area (Zenodo record)
CLARKE_BOX = (525000, 543000, 172000, 180000)        # 18 km x 8 km = 576 squares of 500 m
# A same-shape comparison area north of the Thames, wholly inside the county
NORTH_BOX = (526000, 535000, 181000, 186000)          # 9 km x 5 km = 45 km2
STEP = 500


def load():
    rows = list(csv.DictReader(open(os.path.join(HERE, "v1_impacts.csv"), encoding="utf-8")))
    return np.array([[float(r["easting"]), float(r["northing"])] for r in rows])


def inside(p, b):
    return (p[:, 0] > b[0]) & (p[:, 0] < b[1]) & (p[:, 1] > b[2]) & (p[:, 1] < b[3])


def grid_counts(p, b, step=STEP):
    q = p[inside(p, b)]
    nx, ny = int((b[1] - b[0]) / step), int((b[3] - b[2]) / step)
    c = np.zeros((nx, ny), int)
    np.add.at(c, (((q[:, 0] - b[0]) // step).astype(int), ((q[:, 1] - b[2]) // step).astype(int)), 1)
    return c


def thames():
    """Thames centreline (OS Open Rivers, BNG m), extracted by thames.py."""
    rows = list(csv.DictReader(open(os.path.join(HERE, "thames_os_open_rivers.csv"))))
    return np.array([[float(r["easting"]), float(r["northing"])] for r in rows])


def area_km2(b):
    return (b[1] - b[0]) * (b[3] - b[2]) / 1e6


if __name__ == "__main__":
    from scipy.stats import binomtest, chi2, poisson
    p = load()
    th = thames()
    np.savez(os.path.join(HERE, "real_data.npz"), pts=p, clarke_box=CLARKE_BOX, north_box=NORTH_BOX,
             thames=th)
    seg = th[(th[:, 0] >= NORTH_BOX[0]) & (th[:, 0] <= NORTH_BOX[1])]
    print(f"Thames: {len(th)} vertices; highest northing under the north box {seg[:, 1].max():.0f} m"
          f" (box starts at {NORTH_BOX[2]} m, so the box is wholly north of the river)")
    print("V-1 sites in file:", len(p))
    print("extent E", p[:, 0].min(), p[:, 0].max(), " N", p[:, 1].min(), p[:, 1].max())
    nc, nn = int(inside(p, CLARKE_BOX).sum()), int(inside(p, NORTH_BOX).sum())
    dc, dn = nc / area_km2(CLARKE_BOX), nn / area_km2(NORTH_BOX)
    print(f"Clarke-area box: {nc} hits / {area_km2(CLARKE_BOX):.0f} km2 = {dc:.2f} per km2")
    print(f"north box:       {nn} hits / {area_km2(NORTH_BOX):.0f} km2 = {dn:.2f} per km2"
          f"  (ratio {dn / dc:.2f})")
    print(f"Clarke's own count: 537 / 144 km2 = {537 / 144:.2f} per km2")
    bt = binomtest(nn, nn + nc, area_km2(NORTH_BOX) / (area_km2(NORTH_BOX) + area_km2(CLARKE_BOX)))
    print("one-density test (binomial, north share of the two boxes): p =", f"{bt.pvalue:.1e}")
    c = grid_counts(p, CLARKE_BOX)
    h = [int((c == k).sum()) for k in range(5)] + [int((c >= 5).sum())]
    lam = c.sum() / c.size
    e = [c.size * poisson.pmf(k, lam) for k in range(5)]
    e.append(c.size - sum(e))
    x2 = sum((o - x) ** 2 / x for o, x in zip(h, e))
    print("Clarke-area box histogram 0..5+:", h, " lambda", round(lam, 4),
          " chi2", round(x2, 2), " p(df4)", round(chi2.sf(x2, 4), 2))
