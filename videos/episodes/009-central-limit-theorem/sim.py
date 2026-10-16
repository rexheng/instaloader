"""Episode 9 data: every number shown or spoken, recomputed. Writes data.npz for scene.py.

    python videos/episodes/009-central-limit-theorem/sim.py

All "waits" are SIMULATED exponential draws (mean 10 min: buses arriving at random,
i.e. a Poisson process).  Seeds were chosen so each sample is representative (its
sample skewness is close to the exact value); the exact values are printed next to them.
"""
from pathlib import Path

import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
MEAN = 10.0                       # minutes; exponential: sd = mean = 10, skewness = 2


def skew(x) -> float:
    """Sample skewness E[(x - mean)^3] / sd^3 (same definition as Kohavi et al. 2014)."""
    x = np.asarray(x, float)
    d = x - x.mean()
    return float((d ** 3).mean() / (d ** 2).mean() ** 1.5)


def shares(x, edges) -> np.ndarray:
    """Share (fraction) of ALL draws falling in each bin (draws outside the window are
    counted in the denominator, so bars are honest shares of the whole sample)."""
    h, _ = np.histogram(x, edges)
    return h / len(x)


def main() -> dict:
    out = {}
    # ------------------------------------------------------------- raw waits, growing n
    waits = np.random.default_rng(123).exponential(MEAN, 100_000)
    src_edges = np.arange(0, 50.01, 2.5)                       # 20 bins of 2.5 min
    sizes = [100, 1_000, 10_000, 100_000]
    out["src_edges"] = src_edges
    out["src_shares"] = np.array([shares(waits[:n], src_edges) for n in sizes])
    out["src_skew"] = np.array([skew(waits[:n]) for n in sizes])
    out["src_first100"] = waits[:100]
    print("raw waits skewness by n:", dict(zip(sizes, out["src_skew"].round(3))),
          "(exact 2); max of first 100:", waits[:100].max().round(1))
    # exact exponential share per bin (the smooth 'source shape')
    out["src_exact"] = np.diff(stats.expon(scale=MEAN).cdf(src_edges))

    # ------------------------------------------------------------- averages of n waits
    rng = np.random.default_rng(1157)
    # window = mean -3.5 sd .. mean +4 sd (clamped at 0), so each bell is drawn whole
    groups = {4: (0, 30), 16: (1.25, 20), 64: (5.625, 15)}
    for n, (lo, hi) in groups.items():
        means = rng.exponential(MEAN, (10_000, n)).mean(1)
        edges = np.linspace(lo, hi, 25)                       # 24 bins = 0.25 sd each
        out[f"avg{n}_edges"] = edges
        out[f"avg{n}_shares"] = shares(means, edges)
        out[f"avg{n}_skew"] = skew(means)
        sd = MEAN / np.sqrt(n)
        out[f"avg{n}_bell"] = np.diff(stats.norm(MEAN, sd).cdf(edges))
        print(f"averages of {n:2d}: skew {skew(means):.3f} (exact {2 / np.sqrt(n):.3f}), "
              f"sd {means.std():.3f} (exact {sd:.3f}), outside window "
              f"{np.mean((means < lo) | (means > hi)):.4f}")
    # excess kurtosis ("extra tail weight") of an average of n waits: exactly 6/n
    for n in (1, 4, 16, 64):
        print(f"excess kurtosis, average of {n:2d}: {stats.gamma(n).stats('k'):.4f} (6/n = {6 / n:.4f})")
    # the landing: 10,000 simulated averages of 1,420 waits (the size the 355 s^2 rule asks for)
    rng = np.random.default_rng(2025)
    means = np.concatenate([rng.exponential(MEAN, (1000, 1420)).mean(1) for _ in range(10)])
    lo, hi = 9.0, 11.0                                        # mean -/+ 3.77 sd
    edges = np.linspace(lo, hi, 25)
    out["avg1420_edges"] = edges
    out["avg1420_shares"] = shares(means, edges)
    out["avg1420_skew"] = skew(means)
    print(f"averages of 1420: skew {skew(means):.3f} (exact {2 / np.sqrt(1420):.3f}), sd "
          f"{means.std():.4f} (exact {MEAN / np.sqrt(1420):.4f}), outside window "
          f"{np.mean((means < lo) | (means > hi)):.5f}")
    # the one worked example: four waits -> one average (first group of the n=4 run)
    ex = np.random.default_rng(83).exponential(MEAN, 4)
    out["example4"] = ex
    print("example group of 4:", ex.round(1), "mean", ex.mean().round(2))

    # ------------------------------------------------------------- lopsided coin (p = 0.1)
    p = 0.1
    coin_skew = (1 - 2 * p) / np.sqrt(p * (1 - p))
    k = np.arange(0, 17)
    out["coin_k"] = k
    out["coin_shares"] = stats.binom(64, p).pmf(k)            # exact, share of heads k/64
    out["coin_bell"] = stats.norm(64 * p, np.sqrt(64 * p * (1 - p))).pdf(k)
    out["coin_skew"] = np.array([coin_skew, coin_skew / 8])
    ck = stats.bernoulli(p).stats("k")
    print(f"coin excess kurtosis {float(ck):.3f}; mean of 64 flips {float(stats.binom(64, p).stats('k')):.4f} "
          f"(= {float(ck) / 64:.4f})")
    print(f"coin p=0.1 skew {coin_skew:.3f}; mean of 64 flips: {coin_skew / 8:.3f}; "
          f"heads beyond 16 of 64: {stats.binom(64, p).sf(16):.5f}")

    # ------------------------------------------------------------- 'how many is enough'
    # EXACT distribution of the average of n exponential waits: Gamma(n, scale 10/n).
    # Bins are 1/7 of the 95% half-width c = 1.96 sd/sqrt(n), so mean -/+ c fall on bin
    # edges; the window runs from -14 to +15 bins around the mean.
    z = stats.norm.ppf(0.975)
    for n in (30, 300, 1420):
        g = stats.gamma(n, scale=MEAN / n)
        sd = MEAN / np.sqrt(n)
        c = z * sd
        w = c / 7
        edges = MEAN + w * np.arange(-14, 16)
        out[f"tail{n}_edges"] = edges
        out[f"tail{n}_shares"] = np.diff(g.cdf(edges))
        out[f"tail{n}_bell"] = np.diff(stats.norm(MEAN, sd).cdf(edges))
        lo, hi = g.cdf(MEAN - c), g.sf(MEAN + c)
        out[f"tail{n}_tails"] = np.array([lo, hi])
        print(f"average of {n} waits: window {edges[0]:.2f}-{edges[-1]:.2f} min; KNOWN-sd 95% "
              f"interval mean +- {c:.3f}: misses {100 * lo:.2f}% low / {100 * hi:.2f}% high "
              f"(bell 2.50/2.50); skew {2 / np.sqrt(n):.4f}")
    for n in (130, 150):
        g = stats.gamma(n, scale=MEAN / n)
        c = z * MEAN / np.sqrt(n)
        print(f"  known sd, n={n}: {100 * g.cdf(MEAN - c):.2f}% / {100 * g.sf(MEAN + c):.2f}% "
              f"(already inside 2-3%: the 355 s^2 rule is for an ESTIMATED spread)")
    # What an A-B test computes: the 95% interval xbar +- 1.96 s/sqrt(n) with s the SAMPLE sd
    # (ddof = 1).  Simulated miss rates on exponential waits: 'low' = the interval lies wholly
    # below the true mean 10, 'high' = wholly above it.
    for n, reps, seed in ((30, 2_000_000, 31), (300, 1_000_000, 301), (1420, 1_000_000, 1421)):
        rng = np.random.default_rng(seed)
        low = high = 0
        chunk = max(1, 20_000_000 // n)
        for k in range(0, reps, chunk):
            m = min(chunk, reps - k)
            x = rng.exponential(MEAN, (m, n))
            xb, s = x.mean(1), x.std(1, ddof=1)
            h = z * s / np.sqrt(n)
            low += int(np.sum(xb + h < MEAN))
            high += int(np.sum(xb - h > MEAN))
        out[f"miss{n}"] = np.array([low, high]) / reps
        se = 100 * np.sqrt(0.03 * 0.97 / reps)
        print(f"SIMULATED z-interval with sample sd, n={n} ({reps:,} tests): misses "
              f"{100 * low / reps:.2f}% low / {100 * high / reps:.2f}% high (MC se ~{se:.3f} pts)")
    # one test of 30 waits with a low average (seed 219: xbar near 6.8, its sd at the median
    # sd of all tests whose average lies in 6.6-7.0 min, so its interval is the typical one)
    ex30 = np.random.default_rng(219).exponential(MEAN, 30)
    xb, s = ex30.mean(), ex30.std(ddof=1)
    out["ex30"] = np.array([xb, s, z * MEAN / np.sqrt(30), z * s / np.sqrt(30)])
    print(f"example test of 30 waits: xbar {xb:.3f}, sample sd {s:.3f}; known-sd interval "
          f"{xb - z * MEAN / np.sqrt(30):.2f}-{xb + z * MEAN / np.sqrt(30):.2f} (covers 10); "
          f"estimated-sd interval {xb - z * s / np.sqrt(30):.2f}-{xb + z * s / np.sqrt(30):.2f} (misses)")
    rng = np.random.default_rng(0)
    x = rng.exponential(MEAN, (400_000, 30))
    xb_all, s_all = x.mean(1), x.std(1, ddof=1)
    sel = (xb_all > 6.6) & (xb_all < 7.0)
    print(f"  tests of 30 with average 6.6-7.0: median sd {np.median(s_all[sel]):.3f}; "
          f"{100 * np.mean((xb_all + z * s_all / np.sqrt(30) < MEAN)[sel]):.0f}% of their "
          f"intervals miss low; corr(average, sd) = {np.corrcoef(xb_all, s_all)[0, 1]:.2f}")
    thr = 1 / np.sqrt(355)
    print(f"textbook n=30 leaves skew 2/sqrt(30) = {2 / np.sqrt(30):.3f}")
    print(f"355 s^2 rule  <=>  s/sqrt(n) <= 1/sqrt(355) = {thr:.4f}")
    print(f"  check: 1/0.053^2 = {1 / 0.053 ** 2:.1f} (so the screen shows 1/sqrt(355), "
          f"not 0.053, inside the algebra)")
    for name, s in [("waits", 2.0), ("Bing revenue/user", 17.9), ("capped at $10/wk", 5.2)]:
        print(f"  {name:18s} skew {s:5.1f} -> n >= 355 s^2 = {355 * s * s:,.0f}")

    # ------------------------------------------------------------- the lighthouse (Cauchy)
    rng = np.random.default_rng(3397)
    theta = rng.uniform(-np.pi / 2, np.pi / 2, 1000)           # beam angle from the normal
    x = np.tan(theta)                                         # landing spot, miles (d = 1)
    kk = np.arange(1, 1001)
    out["lh_x"] = x
    out["lh_mean"] = np.cumsum(x) / kk
    out["lh_median"] = np.array([np.median(x[:i]) for i in kk])
    far = int(np.abs(x).argmax())
    print(f"lighthouse: farthest {x[far]:.0f} mi at flash {far + 1}; running mean before "
          f"{out['lh_mean'][far - 1]:.2f}, after {out['lh_mean'][far]:.2f}; final mean "
          f"{out['lh_mean'][-1]:.2f}; final median {out['lh_median'][-1]:.3f}")
    q = 0.5 ** (1 / 1000)
    print(f"typical farthest of 1000 flashes (median of max|x|): {np.tan(np.pi / 2 * q):.0f} mi;"
          f" P(|x|<1) = {2 / np.pi * np.arctan(1):.2f}")
    q1, q3 = np.quantile(x, [0.25, 0.75])
    print(f"this run: middle half of single flashes {q1:.2f} .. {q3:.2f} mi; "
          f"share within 1 mile {np.mean(np.abs(x) < 1):.3f}")
    # 200 repeats of the whole run: the average of 1,000 flashes each (seed chosen so the
    # sample quartiles sit close to the exact +-1)
    avgs = np.random.default_rng(298).standard_cauchy((200, 1000)).mean(1)
    out["lh_avgs"] = avgs
    a1, a3 = np.quantile(avgs, [0.25, 0.75])
    print(f"200 averages of 1,000 flashes: middle half {a1:.2f} .. {a3:.2f} mi; share within "
          f"1 mile {np.mean(np.abs(avgs) < 1):.3f}; beyond the picture (|x| > 5.5): "
          f"{np.sum(avgs < -5.5)} left, {np.sum(avgs > 5.5)} right")
    big = np.random.default_rng(5).standard_cauchy((20_000, 1000))
    m = big.mean(1)
    print(f"20,000 averages of 1000 flashes: share within 1 mile {np.mean(np.abs(m) < 1):.3f} "
          f"(single flash: 0.500); median sd {np.median(big, 1).std():.4f} "
          f"(theory pi/(2 sqrt n) = {np.pi / 2 / np.sqrt(1000):.4f})")
    w = np.random.default_rng(6).exponential(MEAN, (20_000, 1000)).max(1)
    print(f"longest of 1000 waits: median {np.median(w):.1f} min -> /1000 = "
          f"{np.median(w) / 1000 * 60:.1f} s")
    np.savez(HERE / "data.npz", **out)
    return out


if __name__ == "__main__":
    main()
