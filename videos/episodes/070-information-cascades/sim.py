"""Exact + simulated numbers for episode 70 (information cascades). Run: python3 sim.py"""
import numpy as np
from math import comb
p, q = 2/3, 1/3          # P(ball points to the true urn)

def cascade_wrong(n):
    """Exact P(person n guesses wrong) in the BHW/Anderson-Holt line (tie -> own ball). Truth = B."""
    st = {0: 1.0}
    for i in range(1, n + 1):
        new, wrong = {}, 0.0
        for d, pr in st.items():          # d = (#B said) - (#A said) among informative guesses
            if abs(d) == 2:
                new[d] = new.get(d, 0) + pr
                wrong += pr if d == -2 else 0
                continue
            new[d + 1] = new.get(d + 1, 0) + pr * p
            new[d - 1] = new.get(d - 1, 0) + pr * q
            wrong += pr * q
        st = new
        if i == n:
            return wrong

def pooled_wrong(n):
    """Person n sees all n draws (announce balls): majority, tie -> own ball."""
    w = 0.0
    for k in range(n + 1):                  # k = # blue (correct) among n draws
        pk = comb(n, k) * p**k * q**(n - k)
        if 2 * k < n: w += pk
        elif 2 * k == n: w += pk * (n - k) / n   # tie: own ball is purple with prob (n-k)/n by exchangeability
    return w

def simulate(lines, n, rng):
    draws = rng.random((lines, n)) < p      # True = blue (correct)
    wrong = np.zeros(lines, bool)
    d = np.zeros(lines, int)
    for i in range(n):
        free = np.abs(d) < 2
        guess_blue = np.where(free, draws[:, i], d > 0)
        d = np.where(free, d + np.where(draws[:, i], 1, -1), d)
        wrong = ~guess_blue
    return wrong.mean(), draws

print("exact cascade P(100th wrong) =", cascade_wrong(100))
print("limit q^2/(p^2+q^2) =", q*q/(p*p+q*q))
print("pooled P(100th wrong) =", pooled_wrong(100))
rng = np.random.default_rng(70)
m, _ = simulate(100_000, 100, rng)
print("simulated 100,000 lines, 100th wrong:", m)
print("two steps: BB", p*p, "AA", q*q, "mixed", 2*p*q)
# the shown line: first two purple, third blue
rng = np.random.default_rng(7)
for t in range(10000):
    dr = rng.random(100) < p
    if not dr[0] and not dr[1] and dr[2] and dr.sum() == 67:
        print("seed-7 trial", t, "blue count", dr.sum()); np.save("line.npy", dr); break
