"""Recompute every number shown or spoken in episode 4 (run: python check_numbers.py).

Sections
  1. the 16 four-flip sequences, exact (17/42, 12/24, 8 vs 11 rows, after-tails 25/42)
  2. exact expected streak proportions by dynamic programming (no sampling noise):
     E[P(hit | k hits) | defined] for n = 4, n = 100 (GVT's design target) and n = 1000,
     k = 1, 2, 3 (the ghost ticks in the payoff: n = 1000 takes about a minute)
  3. the expected per-player DIFFERENCE  P(hit|3 hits) - P(hit|3 misses), which needs both
     streak types in the same record: Monte Carlo with 1,000,000 sequences (seeded)
  4. Cornell's numbers (49 - 45 = +4, and +4 - (-8) = +12)
  (round 6: the simulated 100-shot record is no longer shown, so its section was removed)
"""
from fractions import Fraction as F
from itertools import product
import sys

import numpy as np

# ---- 1. all 16 four-flip sequences, exact -----------------------------------------
def share_rows(face):
    rows = []
    for seq in product("HT", repeat=4):
        s = "".join(seq)
        checked = [s[i] for i in range(1, 4) if s[i - 1] == face]
        h, n = checked.count("H"), len(checked)
        rows.append((s, h, n))
    return rows


rows = share_rows("H")
scored = [(s, h, n) for s, h, n in rows if n > 0]
shares = [F(h, n) for s, h, n in scored]
mean = sum(shares) / len(shares)
print("== after a heads (4 flips) ==")
print("scored rows:", len(scored), " undefined:", [s for s, h, n in rows if n == 0])
for s, h, n in rows:
    print(f"  {s}: {h}/{n}" if n else f"  {s}: -")
print("mean of shares =", mean, "=", float(mean))
H = sum(h for _, h, _ in scored); N = sum(n for _, _, n in scored)
print("pooled =", H, "/", N, "=", F(H, N))
print("gap vs 1/2 (points) =", 100 * (0.5 - float(mean)))
print("share distribution:", {str(k): shares.count(k) for k in sorted(set(shares))})
rows_with_h = sum(1 for s, h, n in scored if h > 0)
rows_with_t = sum(1 for s, h, n in scored if n - h > 0)
print("rows holding a checked heads:", rows_with_h, " rows holding a checked tails:", rows_with_t)

# votes held (round 6, on screen "5 2/3 votes" / "8 1/3 votes", then 5 2/3 / 14 = 17/42)
votes_h = sum(F(h, n) for _, h, n in scored)
votes_t = sum(F(n - h, n) for _, h, n in scored)
assert votes_h == F(17, 3) and votes_t == F(25, 3) and votes_h + votes_t == 14
assert votes_h / 14 == F(17, 42)
print("votes held by heads:", votes_h, "= 5 2/3", " by tails:", votes_t, "= 8 1/3", " of", len(scored),
      "->", votes_h, "/ 14 =", votes_h / 14)
# the five thinnest heads slices (a third of a vote each): HHHH's three and HHHT's two
thin = [(s, h, n) for s, h, n in scored if n == 3 and h > 0]
print("rows that check 3 flips:", [s for s, _, _ in thin], " heads among them:", sum(h for _, h, _ in thin))

rows_t = share_rows("T")
scored_t = [(s, h, n) for s, h, n in rows_t if n > 0]
mean_t = sum(F(h, n) for _, h, n in scored_t) / len(scored_t)
print("== after a tails (4 flips) ==")
print("scored rows:", len(scored_t), " mean share of heads =", mean_t, "=", float(mean_t))
print("difference of the two averages =", mean - mean_t, "=", 100 * float(mean - mean_t), "points")
both = [(a, b) for a, b in zip(rows, rows_t) if a[2] and b[2]]
per_row = sum(F(a[1], a[2]) - F(b[1], b[2]) for a, b in both) / len(both)
print("(for reference: per-row mean of the difference over the", len(both),
      "rows where both are defined =", per_row, ")")


# ---- 2. exact expected proportions after k hits (dynamic programming) ---------------
def exact_after_hits(n, k, p=0.5):
    """E[ #hits after k hits / #shots after k hits | at least one such shot ] exactly."""
    q = 1 - p
    P = np.zeros((k + 1, n + 1, n + 1))            # [current hit run (capped k), m, s]
    P[0, 0, 0] = 1.0
    for _ in range(n):
        Q = np.zeros_like(P)
        for r in range(k + 1):
            A = P[r]
            if r == k:                               # this shot follows k hits: selected
                Q[k, 1:, 1:] += p * A[:-1, :-1]      # hit
                Q[0, 1:, :] += q * A[:-1, :]         # miss
            else:
                Q[min(r + 1, k)] += p * A
                Q[0] += q * A
        P = Q
    D = P.sum(0)
    m = np.arange(n + 1)[:, None]
    s = np.arange(n + 1)[None, :]
    ratio = np.where(m > 0, s / np.maximum(m, 1), 0.0)
    return float((D * ratio).sum() / D[1:, :].sum())


print("== exact expectations, fair shooter (after k misses = 1 - after k hits, by symmetry) ==")
e4 = exact_after_hits(4, 1)
assert abs(e4 - 17 / 42) < 1e-12
for n, k in [(4, 1), (100, 1), (100, 2), (100, 3), (1000, 1), (1000, 2), (1000, 3)]:
    e = exact_after_hits(n, k)
    print(f"n={n:4d} k={k}: after {k} hits {e:.4f}  after {k} misses {1 - e:.4f}  "
          f"difference of averages {100 * (2 * e - 1):+.2f} pts")

# ---- 3. expected per-record difference (both streak types defined), simulated -------
rng = np.random.default_rng(7)


def diff_stats(n, k, reps, chunk=10_000, p=0.5):
    tot, tot2, cnt = 0.0, 0.0, 0
    for _ in range(reps // chunk):
        x = rng.random((chunk, n)) < p
        allhit = np.ones((chunk, n - k), bool)
        allmiss = np.ones((chunk, n - k), bool)
        for j in range(k):
            allhit &= x[:, j:n - k + j]
            allmiss &= ~x[:, j:n - k + j]
        nxt = x[:, k:]
        nh, nm = allhit.sum(1), allmiss.sum(1)
        hh, mh = (allhit & nxt).sum(1), (allmiss & nxt).sum(1)
        ok = (nh > 0) & (nm > 0)
        d = hh[ok] / nh[ok] - mh[ok] / nm[ok]
        tot += d.sum(); tot2 += (d * d).sum(); cnt += ok.sum()
    mu = tot / cnt
    se = np.sqrt((tot2 / cnt - mu * mu) / cnt)
    return mu, se


reps = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000
for n in (100, 1000):
    d, se = diff_stats(n, 3, reps)
    print(f"simulated ({reps:,} sequences, seed 7) n={n}, k=3: "
          f"E[P(hit|3 hits) - P(hit|3 misses)] = {100 * d:+.2f} pts (s.e. {100 * se:.3f})")

# ---- 4. Cornell numbers (Miller & Sanjurjo 2018, Table 2, reproducing GVT Table 4) ----
print("Cornell: after 3 hits .49, after 3 misses .45 -> 49 - 45 =", 49 - 45,
      "pts; measured from the random baseline -8:", (49 - 45) - (-8), "pts")
