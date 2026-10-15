"""Episode 61 data: every number shown on screen is computed here (seeded, deterministic).

    python3 sim.py            # prints the numbers and writes data.npz next to this file
"""
from pathlib import Path

import numpy as np
from scipy import optimize, special, stats

HERE = Path(__file__).resolve().parent
N, M = 10_000, 2


def grow_ba(n=N, m=M, seed=61):
    """Barabasi-Albert growth: each newcomer brings m links, each attached to an existing
    node with probability proportional to its degree (sampling from the endpoint list)."""
    rng = np.random.default_rng(seed)
    edges = [(0, 1), (1, 2), (0, 2)]                     # seed triangle
    ends = [0, 1, 1, 2, 0, 2]
    for v in range(3, n):
        targets = set()
        while len(targets) < m:
            targets.add(ends[rng.integers(len(ends))])
        for t in targets:
            edges.append((v, t))
            ends += [v, t]
    deg = np.bincount(np.array(ends), minlength=n)
    return deg, edges


def lognormal_counts(n=N, mu=-1.0, sigma=2.0, seed=7):
    """'Opening' data: whole-number counts floor(X), X log-normal(mu, sigma) conditioned on
    X >= 1 (inverse-CDF sampling). No growth, no preferential attachment."""
    rng = np.random.default_rng(seed)
    lo = stats.norm.cdf((0 - mu) / sigma)
    u = rng.uniform(lo, 1, size=n)
    return np.floor(np.exp(mu + sigma * stats.norm.ppf(u))).astype(int)


EDGES = np.array([1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512,
                  768, 1024, 1536])


def logbin(d):
    """Log-binned histogram: fraction of nodes per unit k in bins [a, b) of growing width,
    plotted at the geometric centre of the integers in the bin."""
    c, _ = np.histogram(d, bins=EDGES)
    w = np.diff(EDGES)
    cen = np.sqrt(EDGES[:-1] * (EDGES[1:] - 1))
    dens = c / (len(d) * w)
    m = c > 0
    return cen[m], dens[m], c[m]


def binned_line(d):
    """Naive test: least-squares line through the log-binned log-log histogram."""
    cen, dens, _ = logbin(d)
    X, Y = np.log10(cen), np.log10(dens)
    b, a = np.polyfit(X, Y, 1)
    return b, a, np.corrcoef(X, Y)[0, 1] ** 2


def hist(k):
    vals, counts = np.unique(k, return_counts=True)
    return vals, counts / len(k)


def ls_slope(vals, frac):
    """Naive: least-squares line through the raw log-log histogram."""
    X, Y = np.log10(vals), np.log10(frac)
    b, a = np.polyfit(X, Y, 1)
    r2 = np.corrcoef(X, Y)[0, 1] ** 2
    return b, a, r2


def mle_alpha(k, kmin):
    """CSN 2009 eq. 3.7: alpha ~= 1 + n / sum ln(k / (kmin - 1/2))."""
    t = k[k >= kmin]
    d = np.log(t / (kmin - 0.5))
    return 1 + 1 / d.mean(), d.mean(), len(t)


def mle_alpha_exact(k, kmin):
    t = k[k >= kmin]
    s = np.log(t).sum()
    nll = lambda a: len(t) * np.log(special.zeta(a, kmin)) + a * s
    return optimize.minimize_scalar(nll, bounds=(1.01, 6), method="bounded").x


def pl_logpmf(t, a, kmin):
    return -a * np.log(t) - np.log(special.zeta(a, kmin))


def ln_logpmf_fit(t, kmin):
    """Discrete log-normal truncated at kmin (mass of [k, k+1) of the continuous one),
    fitted by maximum likelihood."""
    def logpmf(mu, s):
        cdf = lambda x: stats.norm.cdf((np.log(x) - mu) / s)
        tail = 1 - cdf(kmin)
        return np.log(np.maximum(cdf(t + 1) - cdf(t), 1e-300)) - np.log(tail)
    res = optimize.minimize(lambda p: -logpmf(p[0], np.exp(p[1])).sum(), x0=[1.0, 0.0],
                            method="Nelder-Mead", options=dict(maxiter=4000, xatol=1e-6, fatol=1e-8))
    mu, s = res.x[0], np.exp(res.x[1])
    return logpmf(mu, s), mu, s


def vuong(t, a, kmin):
    lpl = pl_logpmf(t, a, kmin)
    lln, mu, s = ln_logpmf_fit(t, kmin)
    d = lln - lpl
    R = d.sum()
    z = R / (np.sqrt(len(t)) * d.std())
    p = 2 * stats.norm.sf(abs(z))
    return R, p, mu, s


def ks_kmin(k, cands):
    """CSN: choose kmin minimising the KS distance between data and fitted power law."""
    best = None
    for kmin in cands:
        t = np.sort(k[k >= kmin])
        if len(t) < 50:
            break
        a = mle_alpha_exact(k, kmin)
        kk = np.arange(kmin, t.max() + 1)
        pmf = np.exp(pl_logpmf(kk, a, kmin))
        cdf_model = np.cumsum(pmf)
        cdf_emp = np.searchsorted(t, kk, side="right") / len(t)
        D = np.max(np.abs(cdf_emp - cdf_model))
        if best is None or D < best[1]:
            best = (kmin, D, a)
    return best


def race(t, kmin):
    """Per-point log-likelihood ratio (log-normal minus power law), cumulated in order of k."""
    a = mle_alpha_exact(np.concatenate([t]), kmin)
    lpl = pl_logpmf(t, a, kmin)
    lln, mu, s = ln_logpmf_fit(t, kmin)
    d = lln - lpl
    order = np.argsort(t, kind="stable")
    return np.cumsum(d[order]), t[order]


def small_network(n=34, m=2, seed=3):
    deg, edges = grow_ba(n=n, m=m, seed=seed)
    import networkx as nx
    g = nx.Graph(edges)
    pos = nx.kamada_kawai_layout(g)
    P = np.array([pos[i] for i in range(n)])
    return deg, np.array(edges), P


KMIN = 10
SEED_BA = 7

if __name__ == "__main__":
    deg, _ = grow_ba(seed=SEED_BA)
    x = lognormal_counts()
    out = {}
    for name, d in (("ba", deg), ("ln", x)):
        cen, dens, cnt = logbin(d)
        b, a, r2 = binned_line(d)
        al, dm, nt = mle_alpha(d, KMIN)
        ex = mle_alpha_exact(d, KMIN)
        t = d[d >= KMIN]
        R, p, mu, sg = vuong(t, ex, KMIN)
        cum, ks = race(t, KMIN)
        print(f"{name}: n={len(d)} max={d.max()} bins={len(cen)} slope={b:.3f} r2={r2:.4f} "
              f"| tail n={nt} mean d={dm:.4f} alpha~={al:.4f} exact={ex:.4f} "
              f"| R(LN-PL)={R:.2f} p={p:.2g} LN mu={mu:.2f} s={sg:.2f}")
        out.update({f"{name}_cen": cen, f"{name}_dens": dens, f"{name}_line": np.array([b, a, r2]),
                    f"{name}_mle": np.array([al, dm, nt, ex]), f"{name}_race": np.array([R, p]),
                    f"{name}_cum": cum, f"{name}_tail": np.sort(t)})
    v, f = hist(deg)
    print("raw-histogram LS slope (BA):", round(ls_slope(v, f)[0], 3))
    sd, se, sp = small_network()
    print("small network degrees:", sd.tolist())
    out.update(small_deg=sd, small_edges=se, small_pos=sp)
    np.savez(HERE / "data.npz", **out)
