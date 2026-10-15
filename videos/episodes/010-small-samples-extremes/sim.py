"""Simulated state for episode 10 (all schools identical by construction).

1,662 schools; students tested per school n ~ log-uniform on [10, 400] (rounded);
every student score ~ Normal(500, 100). Two schools are pinned at n = 16 and n = 400
for the on-screen resampling demo. "Small" = the smallest 3 % (n <= 11 students).
"""
import numpy as np

N, MU, SIGMA, SEED = 1662, 500.0, 100.0, 38
SMALL_MAX = 11


def simulate(seed: int = SEED):
    rng = np.random.default_rng(seed)
    n = np.round(np.exp(rng.uniform(np.log(10), np.log(400), N))).astype(int)
    i16 = int(np.argmin(np.abs(n - 16) + 1e-3 * np.arange(N)))
    n[i16] = 16
    i400 = int(np.argmax(n))
    n[i400] = 400
    draws16 = None
    means = np.empty(N)
    for i, k in enumerate(n):
        d = rng.normal(MU, SIGMA, k)
        means[i] = d.mean()
        if i == i16:
            draws16 = d
    order = np.argsort(-means)
    top, bot = order[:50], order[-50:]
    small = n <= SMALL_MAX
    z = (means - MU) / (SIGMA / np.sqrt(n))
    out = np.abs(z) > 2
    return dict(n=n, means=means, top=top, bot=bot, small=small, out=out, i16=i16,
                i400=i400, draws16=draws16,
                n_small=int(small.sum()), top_small=int(small[top].sum()),
                bot_small=int(small[bot].sum()), n_out=int(out.sum()),
                out_small=int(small[out].sum()))


if __name__ == "__main__":
    import sys
    for s in (range(40) if len(sys.argv) > 1 else [SEED]):
        r = simulate(s)
        print(s, {k: r[k] for k in ("n_small", "top_small", "bot_small", "n_out", "out_small")},
              "chance", round(50 * r["n_small"] / N, 2), "chance_out", round(r["n_out"] * r["n_small"] / N, 2),
              "m16", round(r["means"][r["i16"]], 1), "m400", round(r["means"][r["i400"]], 1),
              "range", round(r["means"].min()), round(r["means"].max()))
