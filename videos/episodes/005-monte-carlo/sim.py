"""Episode 5 data: every number shown or spoken comes from here (writes data.json).

Test rig: points uniform in the unit cube [0,1]^d.  The target is the "corner ball"
{x : x1^2 + ... + xd^2 <= r_d^2}, with r_d chosen so the ball covers exactly HALF the cube
in every dimension (the true answer is always 1/2).
  d = 2: r^2 = 2/pi exactly;  d = 3: r^3 = 3/pi exactly (r < 1, the ball fits in the cube);
  d >= 4: r > 1, solved numerically from the exact CDF of sum U_i^2 (characteristic-function
  inversion, checked against Monte Carlo).

Grid ("naive"): n = floor(N^(1/d)) midpoints (i + 1/2)/n per axis, N = 1,000,000 budget;
its estimate (exact lattice count via dynamic programming on integer sums).
Darts: N = 1,000,000 uniform random points per dimension (seeded, "simulated" on screen).

    python sim.py      # ~1 min, writes data.json next to this file
"""
from __future__ import annotations

import json
import math
import warnings
from math import factorial, gamma, pi
from pathlib import Path

import numpy as np
from scipy import integrate, optimize
from scipy.special import fresnel

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
DIMS = [2, 3, 6, 10, 20, 100]
BUDGET = 10 ** 6


# ------------------------------------------------------------ exact CDF of sum U_i^2
def phi1(t: float) -> complex:
    """E exp(i t U^2), U ~ U(0,1)."""
    if t == 0:
        return 1.0 + 0j
    a = abs(t)
    S, C = fresnel(math.sqrt(2 * a / pi))
    k = math.sqrt(pi / (2 * a))
    return complex(k * C, k * S * np.sign(t))


def cdf_sum_sq(x: float, d: int) -> float:
    """P(U_1^2 + ... + U_d^2 <= x) by Gil-Pelaez inversion."""
    f = lambda t: (np.exp(-1j * t * x) * phi1(t) ** d).imag / t
    T = 4000 if d < 6 else 400
    edges = np.linspace(0, T, 801)
    tot = sum(integrate.quad(f, a, b, limit=200)[0] for a, b in zip(edges[:-1], edges[1:]))
    return 0.5 - tot / pi


def half_radius_sq(d: int) -> float:
    if d == 2:
        return 2 / pi
    if d == 3:
        return (3 / pi) ** (2 / 3)
    return optimize.brentq(lambda x: cdf_sum_sq(x, d) - 0.5, d / 3 - 1.5, d / 3 + 0.5, xtol=1e-12)


# ------------------------------------------------------------ grid estimate (exact count)
def grid_estimate(d: int, n: int, r2: float) -> float:
    sq = [(2 * i + 1) ** 2 for i in range(n)]          # ((i+1/2)/n)^2 * 4n^2
    lim = r2 * 4 * n * n
    dist = {0: 1}
    for _ in range(d):
        new: dict[int, int] = {}
        for s, c in dist.items():
            for q in sq:
                new[s + q] = new.get(s + q, 0) + c
        dist = new
    inside = sum(c for s, c in dist.items() if s <= lim + 1e-9)
    return inside / n ** d


def ball_share(d: int, r: float = 1.0) -> float:
    """Share of [0,1]^d within distance r <= 1 of the corner = V_d r^d / 2^d."""
    return pi ** (d / 2) / gamma(d / 2 + 1) * r ** d / 2 ** d


def main():
    out: dict = {"budget": BUDGET, "dims": DIMS}
    R2 = {d: half_radius_sq(d) for d in DIMS}
    out["r2"] = {str(d): R2[d] for d in DIMS}
    out["cdf_check"] = {str(d): cdf_sum_sq(R2[d], d) for d in DIMS if d >= 4}

    # grid at a fixed million-point budget
    grid = {}
    for d in DIMS:
        n = int(math.floor(BUDGET ** (1 / d) + 1e-9))
        g = grid_estimate(d, n, R2[d])
        grid[str(d)] = {"per_axis": n, "points_used": n ** d, "estimate": g,
                        "error_points": abs(g - 0.5) * 100}
    out["grid"] = grid

    # the fairest rescue at d = 20: two values (1/4, 3/4) on 19 axes and the centre on the
    # 20th = 2^19 = 524,288 points (2^20 would exceed the budget); exact count by k = #(3/4)
    r2 = R2[20]
    inside = sum(math.comb(19, k) for k in range(20) if (19 - k) / 16 + 9 * k / 16 + 1 / 4 <= r2)
    est = inside / 2 ** 19
    out["rescue20"] = {"points_used": 2 ** 19, "estimate": est, "error_points": abs(est - 0.5) * 100}

    # darts: one million uniform points per dimension
    rng = np.random.default_rng(2024)
    darts = {}
    for d in DIMS:
        hits = 0
        for _ in range(10):
            U = rng.random((BUDGET // 10, d))
            hits += int(((U * U).sum(1) <= R2[d]).sum())
        est = hits / BUDGET
        darts[str(d)] = {"hits": hits, "estimate": est, "error_points": abs(est - 0.5) * 100}
    out["darts"] = darts
    out["darts_typical_error_points"] = 0.5 / math.sqrt(BUDGET) * 100

    # 2-D build: 10x10 midpoint grid and 100 darts
    r2 = R2[2]
    mids = (np.arange(10) + 0.5) / 10
    gx, gy = np.meshgrid(mids, mids)
    gin = (gx ** 2 + gy ** 2 <= r2)
    out["grid2d"] = {"x": gx.ravel().tolist(), "y": gy.ravel().tolist(),
                     "inside": gin.ravel().astype(int).tolist(), "count": int(gin.sum())}
    # dart #1 is the cold-open 100-D dart's first two coordinates (it persists on screen)
    v = np.random.default_rng(7).random(100)
    P = np.vstack([v[:2], np.random.default_rng(9).random((99, 2))])
    din = (P ** 2).sum(1) <= r2
    out["darts2d"] = {"x": P[:, 0].tolist(), "y": P[:, 1].tolist(),
                      "inside": din.astype(int).tolist(), "count": int(din.sum())}

    # the cold-open 100-D dart, plus 99 more: one 100-dart experiment in 100-D
    out["dart100"] = {"x": v.tolist(), "sum_sq": float((v * v).sum()),
                      "inside": bool((v * v).sum() <= R2[100])}
    W = np.vstack([v, np.random.default_rng(110).random((99, 100))])
    win = (W * W).sum(1) <= R2[100]
    out["darts100d"] = {"x": W.tolist(), "inside": win.astype(int).tolist(),
                        "count": int(win.sum())}

    # "shadows alone aren't the fix": a million evenly spaced points on the main diagonal
    # (t, ..., t), t = (i + 1/2)/N, give every axis a million distinct values, but the point is
    # inside iff 100 t^2 <= r_100^2, so the estimate is the share of t below sqrt(r^2/100)
    tmax = math.sqrt(R2[100] / 100)
    k = int(math.floor(tmax * BUDGET - 0.5)) + 1          # #{i : (i + 1/2)/N <= tmax}
    out["diag100"] = {"t_max": tmax, "estimate": k / BUDGET, "error_points": abs(k / BUDGET - 0.5) * 100}
    out["dart2d_sum_sq"] = float(P[0, 0] ** 2 + P[0, 1] ** 2)

    # repeated experiments: 300 runs of n darts, in 2-D and 100-D
    rng = np.random.default_rng(5)
    hist = {}
    first = {2: out["darts2d"]["count"] / 100, 100: out["darts100d"]["count"] / 100}
    for n in (100, 400):
        for d in (2, 100):
            U = rng.random((300, n, d))
            e = ((U * U).sum(2) <= R2[d]).mean(1)
            if n == 100:
                e[0] = first[d]          # run 1 is the experiment shown on screen
            hist[f"{n}_{d}"] = {"estimates": e.tolist(), "mean": float(e.mean()),
                                "sd": float(e.std(ddof=1)), "theory_sd": 0.5 / math.sqrt(n)}
    out["hist"] = hist

    # payoff illustration after Bergstra & Bengio (2012) Fig. 1: f(x, y) = g(x) + h(y) ~ g(x)
    # seed chosen so that the nine x-values (drawn at 0.06 + 0.88 x) are >= 0.06 apart on screen
    # (nine visibly distinct shadows on the score curve) and x, y are uncorrelated (r = 0.00), so the
    # points look like what they are: independent uniform draws (the panel is labelled schematic)
    xs = np.random.default_rng(119736).random((9, 2))
    out["bb"] = {"grid": [[(i + 0.5) / 3, (j + 0.5) / 3] for j in range(3) for i in range(3)],
                 "random": xs.tolist()}

    # honest limit: radius-one ball's share of the cube vs dimension
    out["ball_r1"] = {str(d): ball_share(d) for d in range(2, 31)}
    out["two_pow_100"] = f"{2 ** 100:,}"
    out["root20"] = BUDGET ** (1 / 20)
    out["fact52"] = float(factorial(52))

    (HERE / "data.json").write_text(json.dumps(out, indent=1))
    for d in DIMS:
        print(d, f"r={math.sqrt(R2[d]):.4f}", grid[str(d)], darts[str(d)])
    for k, h in hist.items():
        print(k, round(h["mean"], 4), round(h["sd"], 4), h["theory_sd"])
    print("grid2d", out["grid2d"]["count"], "darts2d", out["darts2d"]["count"])
    print("dart100 inside", out["dart100"]["inside"], out["dart100"]["sum_sq"],
          "100-D batch count", out["darts100d"]["count"], "dart #1 in 2-D", out["darts2d"]["inside"][0])
    print("ball r1 share d=30", out["ball_r1"]["30"], "d=17", out["ball_r1"]["17"])


if __name__ == "__main__":
    main()
