"""Recomputes every number shown in episode 34 (simulated quadratic valley)."""
import math
import numpy as np

def run(k, eta, beta=0.0, x0=(-5, 0.7), tol=1e-3, maxit=200000):
    H = np.array([1.0, k]); x = np.array(x0, float); prev = x.copy(); d0 = np.linalg.norm(x)
    for i in range(1, maxit + 1):
        xn = x - eta * H * x + beta * (x - prev); prev = x; x = xn
        d = np.linalg.norm(x)
        if d <= tol * d0: return i
        if d > 1e6 * d0: return -i
    return None

if __name__ == "__main__":
    print("round bowl eta=1:", run(1, 1.0))
    for k in (25, 100):
        print(f"k={k} best fixed eta={2/(k+1):.4f}: {run(k, 2/(k+1))} steps; shrink {(k-1)/(k+1):.4f};"
              f" theory {math.log(1000)/math.log((k+1)/(k-1)):.1f}")
        s = math.sqrt(k); a = 4/(1+s)**2; b = ((s-1)/(s+1))**2
        print(f"   heavy ball alpha={a:.4f} beta={b:.4f}: {run(k, a, b)} steps")
    print("k=25 eta=0.005:", run(25, 0.005), " eta=0.1:", run(25, 0.1))
    x = np.array([-5, 0.7])
    for i in range(5):
        x = x - 0.1 * np.array([1, 25]) * x; print("  diverge step", i + 1, x)
