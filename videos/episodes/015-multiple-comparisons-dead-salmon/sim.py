"""Numbers for episode 15 (all recomputed here). Run: python sim.py"""
import numpy as np
from math import log10, exp, log
from scipy.stats import norm, t as tdist

COLS, ROWS = 74, 30

def fish_mask():
    """Salmon silhouette on a COLS x ROWS voxel grid (nose left, forked tail right)."""
    m = np.zeros((ROWS, COLS), bool)
    for c in range(COLS):
        x = (c + 0.5) / COLS
        for r in range(ROWS):
            y = (r + 0.5) / ROWS - 0.5          # -0.5 top .. 0.5 bottom (row order)
            if x < 0.80:
                u = x / 0.80
                # blunt snout, deepest at u~0.35, tapering to a narrow peduncle
                h = 0.40 * (u / 0.35) ** 0.5 if u < 0.35 else \
                    0.07 + 0.33 * (0.5 + 0.5 * np.cos(np.pi * (u - 0.35) / 0.65))
                yc = 0.03 * np.sin(np.pi * u)   # belly slightly deeper than back
                inside = abs(y - yc) < h
            else:
                v = (x - 0.80) / 0.20
                h = 0.07 + 0.36 * v
                notch = 0.30 * max(0.0, v - 0.35) / 0.65
                inside = abs(y) < h and abs(y) >= notch
            m[r, c] = inside
    return m

mask = fish_mask()
n0 = mask.sum()
# trim/pad deterministically to exactly 1000
SEED = 8  # chosen among seeds giving the typical outcome (about 50 / 1-2 / 0 hits); see facts.md
rng = np.random.default_rng(SEED)
cells = np.argwhere(mask)
if n0 > 1000:
    # drop cells on the outline with the highest |y| first
    edge = [tuple(c) for c in cells]
    def border(rc):
        r, c = rc
        nb = sum(mask[r+dr, c+dc] for dr, dc in ((1,0),(-1,0),(0,1),(0,-1))
                 if 0 <= r+dr < ROWS and 0 <= c+dc < COLS)
        return nb
    order = sorted(edge, key=lambda rc: (border(rc), -abs(rc[0] - ROWS/2)))
    for rc in order[: n0 - 1000]:
        mask[rc] = False
print("raw voxels", n0, "-> final", mask.sum())

M = int(mask.sum())
z = rng.standard_normal(M)          # pure noise test statistic per voxel (simulated)
p = norm.sf(z)                       # one-sided p-value, like a task>rest t-contrast
for a in (0.05, 0.001, 0.05 / M):
    print(f"alpha={a:.6g}: hits={int((p < a).sum())}, expected={M*a:.3g}")

print("0.95^1 .. ", [round(0.95**k, 4) for k in (1, 2, 3, 14)])
print("0.95^1000 =", 0.95**1000, "P(any)=", 1-0.95**1000)
print("0.999^1000 =", 0.999**1000)
lc = 130000 * log(0.999)
print("0.999^130000 = exp(%.2f) = %.3g  (10^%.2f)" % (lc, exp(lc), lc / log(10)))
print("expected false voxels 130000*0.001 =", 130000 * 0.001)
print("Bonferroni 0.05/1000 =", 0.05 / 1000, " P(any) indep =", 1 - (1 - 0.05/1000)**1000)
print("Bonferroni 0.05/130000 =", 0.05/130000)
print("t(131) one-sided p<0.001 crit:", tdist.isf(0.001, 131))
print("NeuroImage 2008 corrected 193/260 =", 193/260, " uncorrected share", 67/260)
np.savez("sim_data.npz", mask=mask, p=p)
print("z crit 0.05 / 0.00005:", norm.isf(0.05), norm.isf(0.05 / 1000))
print("power for true mean z=3:", norm.sf(norm.isf(0.05) - 3), norm.sf(norm.isf(0.05 / 1000) - 3))
# how often does the 1000-voxel fish show >=1 voxel at p<0.001? (analytic and simulated)
sims = (np.random.default_rng(0).random((20000, 1000)) < 0.001).any(axis=1).mean()
print("P(any at 0.001, m=1000): analytic", 1 - 0.999**1000, "simulated", sims)
