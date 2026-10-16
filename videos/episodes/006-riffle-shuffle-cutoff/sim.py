"""Exact numbers for episode 6 (riffle-shuffle cutoff), plus a Monte-Carlo cross-check.

Gilbert-Shannon-Reeds (GSR) model.  k riffle shuffles of an n-card deck = one 2^k-shuffle.
Bayer & Diaconis (1992), Thm 1: after an a-shuffle, a permutation with r rising sequences
has probability C(a + n - r, n) / a^n.  The number of permutations of n with r rising
sequences is the Eulerian number A(n, r-1) (r-1 descents).  So the whole distribution is
a function of r, and the total-variation distance to uniform equals the TV distance between
the two distributions of r.

Run:  python3 sim.py            (writes data.json next to this file)
"""
from __future__ import annotations

import json
from fractions import Fraction
from math import comb, factorial, log2, sqrt
from pathlib import Path

import numpy as np

N = 52


def eulerian(n: int) -> list[int]:
    """E[r] = # permutations of n with exactly r rising sequences (r = 1..n); index 0 unused."""
    A = [1]                                   # n = 1: one permutation, 0 descents
    for m in range(2, n + 1):
        B = [0] * m
        for d in range(m):
            B[d] = (d + 1) * (A[d] if d < len(A) else 0) + (m - d) * (A[d - 1] if d >= 1 else 0)
        A = B
    return [0] + A                            # r = d + 1


def rising_pmf_shuffled(n: int, k: int, E: list[int]) -> list[Fraction]:
    a = 2 ** k
    return [Fraction(0)] + [Fraction(E[r] * comb(a + n - r, n), a ** n) for r in range(1, n + 1)]


def rising_pmf_uniform(n: int, E: list[int]) -> list[Fraction]:
    f = factorial(n)
    return [Fraction(0)] + [Fraction(E[r], f) for r in range(1, n + 1)]


def tv(p, q) -> Fraction:
    return sum(abs(x - y) for x, y in zip(p, q)) / 2


def mean(p) -> float:
    return float(sum(r * x for r, x in enumerate(p)))


def sd(p) -> float:
    m = mean(p)
    return sqrt(float(sum((r - m) ** 2 * x for r, x in enumerate(p))))


def main():
    E = eulerian(N)
    assert sum(E) == factorial(N)
    U = rising_pmf_uniform(N, E)
    out = {"n": N, "uniform": {"pmf": [float(x) for x in U], "mean": mean(U), "sd": sd(U)}}
    print(f"uniform: mean rising sequences {mean(U):.4f}  sd {sd(U):.4f}  "
          f"(theory (n+1)/2 = {(N + 1) / 2}, sqrt((n+1)/12) = {sqrt((N + 1) / 12):.4f})")
    cdf = 0
    for r in range(1, 25):
        cdf += U[r]
        if r in (16, 18, 19, 20, 21, 22):
            print(f"  P_uniform(R <= {r}) = {float(cdf):.3e}   (1 in {float(1 / cdf):,.0f})")
    rows = []
    for k in range(1, 13):
        P = rising_pmf_shuffled(N, k, E)
        assert sum(P) == 1
        d = tv(P, U)
        g = mean(U) - mean(P)
        approx = N * N / (12 * 2 ** k)
        rows.append({"k": k, "tv": float(d), "mean": mean(P), "sd": sd(P), "gap": g,
                     "gap_approx": approx, "pmf": [float(x) for x in P],
                     "max_r": min(N, 2 ** k)})
        print(f"k={k:2d}  TV={float(d):.4f}  mean R={mean(P):7.3f}  sd={sd(P):.3f}  "
              f"gap={g:7.3f}  n^2/(12*2^k)={approx:7.3f}  gap/sd_U={g / sd(U):6.2f}")
    out["shuffled"] = rows
    # the best test after 4 shuffles: "say 'shuffled 4 times' iff r <= 16"
    cdf16 = float(sum(U[1:17]))
    out["p_uniform_le16"] = cdf16
    print(f"P_uniform(R<=16) = {cdf16:.3e}")
    # cutoff estimate from gap = sd
    a_star = N ** 1.5 / sqrt(12)
    print(f"gap = sd at 2^k = n^1.5/sqrt(12) = {a_star:.1f}  ->  k = {log2(a_star):.2f};  "
          f"1.5 log2 n = {1.5 * log2(N):.2f}")
    # naive test: which card ends on top?  Forward a-shuffle = inverse of "give every card a
    # uniform digit 0..a-1 and stable-sort by digit".  Card 1 sits first among its digit group,
    # so the card that ends on top is card 1 + Bin(n-1, D/a), D uniform on 0..a-1.
    top = []
    for k in range(1, 13):
        a = 2 ** k
        p = [sum(Fraction(comb(N - 1, j)) * Fraction(d, a) ** j * (1 - Fraction(d, a)) ** (N - 1 - j)
                 for d in range(a)) / a for j in range(N)]
        assert sum(p) == 1
        d_top = sum(abs(x - Fraction(1, N)) for x in p) / 2
        top.append({"k": k, "tv": float(d_top), "pmf": [float(x) for x in p]})
        print(f"top card k={k:2d}: TV={float(d_top):.4f}  accuracy={50 + 50 * float(d_top):.1f}%  "
              f"P(card 1 on top)={float(p[0]):.4f}")
    out["top_card"] = top
    Path(__file__).with_name("data.json").write_text(json.dumps(out, indent=1))


def simulate(k: int, trials: int, rng) -> np.ndarray:
    """Forward GSR riffle shuffles of 0..N-1; returns decks (trials x N), top first."""
    decks = np.tile(np.arange(N), (trials, 1))
    for _ in range(k):
        cut = rng.binomial(N, 0.5, size=trials)
        # uniform interleaving of top packet (first cut cards) and bottom packet:
        # choose which positions take top-packet cards uniformly at random
        keys = rng.random((trials, N))
        # positions for top packet = the `cut` smallest keys' positions, in order
        order = np.argsort(keys, axis=1)
        is_top = np.zeros((trials, N), dtype=bool)
        rows = np.arange(trials)[:, None]
        rank = np.empty_like(order)
        rank[rows, order] = np.arange(N)[None, :]
        is_top = rank < cut[:, None]
        new = np.empty_like(decks)
        for t in range(trials):
            c = cut[t]
            new[t, is_top[t]] = decks[t, :c]
            new[t, ~is_top[t]] = decks[t, c:]
        decks = new
    return decks


def rising(deck: np.ndarray) -> int:
    pos = np.empty(N, dtype=int)
    pos[deck] = np.arange(N)
    return 1 + int(np.sum(pos[1:] < pos[:-1]))


if __name__ == "__main__":
    main()
