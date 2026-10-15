"""Recompute every number shown or spoken in episode 48 from Matthews (2000), Table 1.

    python videos/episodes/048-confounding-dags/check_numbers.py
"""
import numpy as np
from scipy import stats

# country, area (km^2), stork pairs, humans (millions), births (thousands / yr)
TABLE = [
    ("Albania", 28750, 100, 3.2, 83), ("Austria", 83860, 300, 7.6, 87),
    ("Belgium", 30520, 1, 9.9, 118), ("Bulgaria", 111000, 5000, 9.0, 117),
    ("Denmark", 43100, 9, 5.1, 59), ("France", 544000, 140, 56, 774),
    ("Germany", 357000, 3300, 78, 901), ("Greece", 132000, 2500, 10, 106),
    ("Holland", 41900, 4, 15, 188), ("Hungary", 93000, 5000, 11, 124),
    ("Italy", 301280, 5, 57, 551), ("Poland", 312680, 30000, 38, 610),
    ("Portugal", 92390, 1500, 10, 120), ("Romania", 237500, 5000, 23, 367),
    ("Spain", 504750, 8000, 39, 439), ("Switzerland", 41290, 150, 6.7, 82),
    ("Turkey", 779450, 25000, 56, 1576),
]


def ols(y, *xs):
    X = np.column_stack([np.ones(len(y)), *xs])
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ b
    df = len(y) - X.shape[1]
    se = np.sqrt(np.diag(e @ e / df * np.linalg.inv(X.T @ X)))
    p = 2 * stats.t.sf(np.abs(b / se), df)
    return b, se, p, df


if __name__ == "__main__":
    A = np.array([r[1] for r in TABLE], float)
    S = np.array([r[2] for r in TABLE], float)
    B = np.array([r[4] for r in TABLE], float)
    r, p = stats.pearsonr(S, B)
    print(f"n = {len(TABLE)}   r(storks, births) = {r:.4f}   p = {p:.5f}   "
          f"t = {r * np.sqrt(15) / np.sqrt(1 - r * r):.3f}   1/p = {1 / p:.0f}")
    b, se, pv, df = ols(B, S)
    print(f"naive slope = {b[1]:.5f} thousand births / pair = {1000 * b[1]:.1f} births / pair; "
          f"x10,000 pairs -> +{10000 * b[1]:.0f} thousand births")
    print(f"r(area, births) = {stats.pearsonr(A, B)[0]:.4f}   r(area, storks) = {stats.pearsonr(A, S)[0]:.4f}")
    b2, se2, pv2, df2 = ols(B, S, A)
    lo, hi = b2[1] + np.array([-1, 1]) * stats.t.ppf(0.975, df2) * se2[1]
    print(f"adjusted for area: b = {1000 * b2[1]:.2f} births / pair, p = {pv2[1]:.4f} (df {df2}), "
          f"95% CI [{1000 * lo:.1f}, {1000 * hi:.1f}]")
    # Frisch-Waugh-Lovell: residualise both on area, slope of residuals == adjusted b
    cs, cb = np.polyfit(A, S, 1), np.polyfit(A, B, 1)
    rs, rb = S - np.polyval(cs, A), B - np.polyval(cb, A)
    print(f"FWL slope of residuals = {1000 * np.polyfit(rs, rb, 1)[0]:.2f} births / pair")
    t = TABLE.index(next(x for x in TABLE if x[0] == "Turkey"))
    print(f"Turkey: size predicts {np.polyval(cs, A[t]):.0f} pairs and {np.polyval(cb, A[t]):.0f} "
          f"thousand births; residual = ({rs[t]:.0f} pairs, {rb[t]:.0f} thousand births)")
