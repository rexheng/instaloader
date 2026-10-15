"""Exact check of every simulated number shown in episode 077 (run: python3 model_check.py).

Model (simulated, labelled on screen): one pasture, 10 herders.
Grass regrows logistically, dG/dt = rG(1 - G/K) - eCG; its steady state is
G*/K = 1 - eC/r.  With r/e = 100 cows, grass left = 1 - C/100, and milk per cow
= 20 L/day x grass left = 20 - 0.2 C.  Herders best-respond one cow at a time
(add if it strictly raises their own milk, net of any fine).
"""
from fractions import Fraction as F


def milk(C):
    return max(F(0), F(20) - F(1, 5) * C)


def run(start, saints=(), fine=None, cap=5):
    h = list(start)
    for _ in range(500):
        changed = False
        for i in range(10):
            if i in saints:
                continue
            others = sum(h) - h[i]

            def u(n):
                p = n * milk(others + n)
                if fine is not None:
                    p -= fine * max(0, n - cap)
                return p
            if u(h[i] + 1) > u(h[i]):
                h[i] += 1; changed = True
            elif h[i] > 0 and u(h[i] - 1) > u(h[i]):
                h[i] -= 1; changed = True
        if not changed:
            break
    C = sum(h)
    return h, C, milk(C), C * milk(C)


best = max(range(101), key=lambda C: C * milk(C))
print("village optimum:", best, "cows ->", best * milk(best), "L/day; grass", 1 - F(best, 100))
h, C, m, T = run([5] * 10)
print("no rules:", h, C, "cows; grass", 1 - F(C, 100), "; milk", T, "L/day")
h, C, m, T = run([5] * 10, saints=(0, 1, 2))
print("3 saints:", h, C, "cows; saint earns", 5 * m, "; others", [x * m for x in h[3:]])
h, C, m, T = run([5] * 10, fine=9)
print("fine 9 L per cow over 5:", h, C, "cows; milk", T)
print("51st cow: gain", milk(51), "damage", 50 * F(1, 5), "his share (5/50)",
      F(5, 50) * 50 * F(1, 5), "net to him", 6 * milk(51) - 5 * milk(50),
      "net to village", 51 * milk(51) - 50 * milk(50))
print("91st cow: gain", milk(91), "damage", 90 * F(1, 5), "his share (9/90)",
      F(9, 90) * 90 * F(1, 5), "net to him", 10 * milk(91) - 9 * milk(90))
