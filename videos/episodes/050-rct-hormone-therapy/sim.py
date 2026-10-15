"""Simulated population for episode 50 (all on-screen sim numbers come from here).

Model (simulated, not real data):
  hidden heart health h = 0.6*m + 0.8*u, m = measured (blood-pressure-like), u = unmeasured, both N(0,1)
  baseline 5-year heart-attack risk  r0 ∝ exp(-0.7 h)   (scaled so users' baseline = 100 per 10,000)
  observational world: P(take hormones) = logistic(-0.5 + C1*h), C1 tuned so head start = 0.50
  the pill multiplies every woman's risk by 1.3 (true effect)
  trial world: fair coin decides who takes the pill
Run: python sim.py  -> prints the numbers and writes sim_display.npz (200 women shown on screen)
"""
import numpy as np

N, RR, C1 = 2_000_000, 1.3, 1.2812329
rng = np.random.default_rng(50)
m, u = rng.normal(size=N), rng.normal(size=N)
h = 0.6 * m + 0.8 * u
T = rng.random(N) < 1 / (1 + np.exp(-(-0.5 + C1 * h)))
r = np.exp(-0.7 * h); r *= 0.0100 / r[T].mean()
C = rng.random(N) < 0.5

users, non = RR * r[T].mean() * 1e4, r[~T].mean() * 1e4
q = np.quantile(m, np.linspace(0, 1, 21)); s = np.clip(np.searchsorted(q, m, side="right") - 1, 0, 19)
num = den = 0.0
for k in range(20):
    i = s == k; w = i.mean(); num += w * RR * r[i & T].mean(); den += w * r[i & ~T].mean()
tu, tc = RR * r[C].mean() * 1e4, r[~C].mean() * 1e4
print(f"observational: users {users:.1f}  non-users {non:.1f}  ratio {users/non:.3f}  head start {100/non:.3f}")
print(f"adjusted for measured m: ratio {num/den:.3f}  (head start {num/den/RR:.3f})")
print(f"coin flip: users {tu:.1f}  non-users {tc:.1f}  ratio {tu/tc:.3f}  head start {r[C].mean()/r[~C].mean():.3f}")
print(f"share choosing hormones {T.mean():.3f}; mean hidden health users {h[T].mean():.2f} vs {h[~T].mean():.2f}")
rng2 = np.random.default_rng(7)
idx = rng2.choice(N, 200, replace=False)
np.savez("sim_display.npz", h=h[idx], T=T[idx], C=C[idx])
print("display sample: users", int(T[idx].sum()), " coin-flip treated", int(C[idx].sum()))
