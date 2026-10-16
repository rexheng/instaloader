"""Recompute every number episode 2 shows or speaks (round 2 premise: 1 in 500, 99 %, 1 %).
Run: python3 videos/episodes/002-base-rate-fallacy/check.py"""
from fractions import Fraction as F

import numpy as np

prev, sens, fpr = F(1, 500), F(99, 100), F(1, 100)


def ppv(p):
    return p * sens / (p * sens + (1 - p) * fpr)


P = ppv(prev)
print("PPV exact", P, f"{float(P):.4f}", " naive/ppv", f"{float(sens / P):.2f}")
N = 10000
print("expected counts: sick", N * prev, "-> +", float(N * prev * sens),
      "; healthy", N * (1 - prev), "-> +", float(N * (1 - prev) * fpr))
print("count picture 20/120 =", f"{20 / 120:.4f}")
print("before rounding 19.8/(19.8+99.8) =", f"{19.8 / (19.8 + 99.8):.4f}")
print("table route (20*0.99)/(20*0.99+9980*0.01) =", f"{(20 * 0.99) / (20 * 0.99 + 9980 * 0.01):.4f}")
print("shares route (0.002*0.99)/(0.002*0.99+0.998*0.01) =",
      f"{(0.002 * 0.99) / (0.002 * 0.99 + 0.998 * 0.01):.4f}")
print("20/10000 =", 20 / 10000, " 9980/10000 =", 9980 / 10000)
print("half sick:", 5000 * 0.99, 5000 * 0.01, 4950 / 5000)
print("strip 24 x 5 =", 24 * 5, " red columns 4/24 =", f"{4 / 24:.4f}", "(meter red share 20/120)")
# Monte Carlo
rng = np.random.default_rng(7)
n = 10_000_000
sick = rng.random(n) < 1 / 500
pos = np.where(sick, rng.random(n) < 0.99, rng.random(n) < 0.01)
print("MC P(sick|+) =", f"{sick[pos].mean():.4f}")
# landing sweep and flows
for k in (500, 100, 2):
    print(f"prior 1/{k} -> P(sick|+) = {float(ppv(F(1, k))):.4f}")
W = 0.45
print("flow widths at 1/500:", round(W * float(P), 4), round(W * (1 - float(P)), 4),
      "(ratio 19.8 : 99.8)")
# Cardiff 2017 (South Wales Police figures via BBC News, 4 May 2018)
alerts, wrong = 2470, 2297
print("Cardiff right:", alerts - wrong, " precision", f"{(alerts - wrong) / alerts:.4f}",
      " press '92%' is really", f"{wrong / alerts:.4f}", " raster 26 x 95 =", 26 * 95)
crowd, squares = 170_000, 100 * 100
print("crowd: 1 square =", crowd / squares, "people; lit squares 2470/17 =", f"{2470 / 17:.1f}",
      "-> 145 squares =", 145 * 17, "alerts at that scale; blocks 29 x 5 =", 29 * 5)
print("watch lists ~1,200 of 170,000 =", f"{1200 / 170000:.4%}", "(upper bound on listed share)")
# ---- round 4: cold-open baseline is Manrai et al. 2014 (JAMA Intern Med 174(6):991-993)
# 61 respondents; prevalence 1/1000, false-positive rate 5 %, perfect sensitivity assumed
m_right, m_95, m_n = 14, 27, 61
m_other = m_n - m_right - m_95
per100 = [round(100 * k / m_n) for k in (m_right, m_95, m_other)]
print("Manrai: right", m_right, "/", m_n, "=", f"{m_right / m_n:.3f}", "; said 95%", m_95, "=",
      f"{m_95 / m_n:.3f}", "; other", m_other, "; per 100 dots", per100, "sum", sum(per100),
      "; wrong", m_n - m_right, "=", f"{(m_n - m_right) / m_n:.3f}")
p_m = F(1, 1000)
print("Manrai correct answer:", f"{float(p_m / (p_m + (1 - p_m) * F(5, 100))):.4f}",
      "; that test's accuracy (TP+TN)/N:", f"{float(p_m + (1 - p_m) * F(95, 100)):.4f}")
# ---- round 3 additions
# accuracy (the title's "99 % accurate") and the always-"healthy" test, per 10,000 people
tp, fn = 20 * 0.99, 20 * 0.01
fp, tn = 9980 * 0.01, 9980 * 0.99
print("accuracy: right =", round(tp + tn, 1), "of 10,000 =", f"{(tp + tn) / 10000:.4f}",
      "; says 'healthy' to everyone: right =", 9980, "=", f"{9980 / 10000:.4f}",
      "(recall 0)")
# Cardiff crowd picture: listed squares, flagged squares, red share of the flagged
import math
print("listed squares: ceil(1200/17) =", math.ceil(1200 / 17), "(1200/17 =", f"{1200 / 17:.1f})",
      "; flagged red: 173/17 =", f"{173 / 17:.1f}", "-> 10 ; red share of 145 flagged =",
      f"{10 / 145:.4f}", "vs 173/2470 =", f"{173 / 2470:.4f}")
print("listed share of crowd (upper bound): 71/10000 =", 71 / 10000, " 1200/170000 =",
      f"{1200 / 170000:.4f}")
# Davies et al. 2018: Champions League (all watch lists incl. blue) 78 true of 2,632 = 3 %;
# Six Nations 2018 (non-police) 22 judged true of 48 = 46 %
print("Davies CL:", f"{78 / 2632:.3f}", " Six Nations:", f"{22 / 48:.3f}")
# landing sweep: label and meter computed from the same rounded prevalence
for n in (74, 100, 15, 5, 2, 394, 500):
    print(f"  1 in {n}: P(sick|+) = {float(ppv(F(1, n))):.3f}")
# ---- round 4: derivation states and markers
print("stage 2a (transient) 20*0.99/(20*0.99+100) =", f"{19.8 / 119.8:.4f}", "-> 17%")
print("evaluators' tick at the final: 78/2632 =", f"{78 / 2632:.4f}", "-> 3%")
