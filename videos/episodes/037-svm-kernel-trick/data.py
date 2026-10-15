"""Simulated ring data + every number shown in episode 37 (deterministic)."""
import numpy as np

N_IN, N_OUT = 40, 40
R_IN, R_OUT = (0.0, 1.0), (1.5, 2.3)


def make_points(seed=7):
    rng = np.random.default_rng(seed)

    def ring(n, r0, r1):
        r = np.sqrt(rng.uniform(r0 ** 2, r1 ** 2, n))      # uniform over area
        t = rng.uniform(0, 2 * np.pi, n)
        return np.c_[r * np.cos(t), r * np.sin(t)]
    X = np.r_[ring(N_IN, *R_IN), ring(N_OUT, *R_OUT)]
    y = np.r_[np.ones(N_IN), -np.ones(N_OUT)]                # +1 purple (inside), -1 blue (ring)
    return X, y


def mistakes(w, b, F, y):
    return int(np.sum(np.sign(F @ w + b) * y <= 0))


def perceptron(F, y, n_updates, seed=3, w0=None, b0=0.0):
    """Classic perceptron: pick a random misclassified point, nudge toward it.
    Returns a list of (w, b, mistakes, index_nudged)."""
    rng = np.random.default_rng(seed)
    w = np.zeros(F.shape[1]) if w0 is None else np.array(w0, float)
    b = b0
    hist = [(w.copy(), b, mistakes(w, b, F, y), None)]
    for _ in range(n_updates):
        wrong = np.flatnonzero(np.sign(F @ w + b) * y <= 0)
        if len(wrong) == 0:
            break
        i = rng.choice(wrong)
        w = w + y[i] * F[i]
        b = b + y[i]
        hist.append((w.copy(), b, mistakes(w, b, F, y), i))
    return hist


def lift(X):
    return np.c_[X, (X ** 2).sum(1)]


def kernel(A, B):
    """phi(a).phi(b) for phi(x,y) = (x, y, x^2+y^2)."""
    return A @ B.T + np.outer((A ** 2).sum(1), (B ** 2).sum(1))


if __name__ == "__main__":
    X, y = make_points()
    r = np.linalg.norm(X, axis=1)
    print("purple max r", r[y > 0].max(), "z", (r[y > 0] ** 2).max())
    print("blue min r", r[y < 0].min(), "z", (r[y < 0] ** 2).min())
    h2 = perceptron(X, y, 5000, w0=[0.6, 0.8], b0=0.3)
    m = [h[2] for h in h2]
    print("2D: updates", len(h2) - 1, "final", m[-1], "best", min(m), "worst", max(m))
    print("2D first 30 mistakes:", m[:31])
    # best possible straight line (brute force over directions/offsets)
    best = 99
    for th in np.linspace(0, np.pi, 721):
        d = np.array([np.cos(th), np.sin(th)])
        p = X @ d
        for c in np.r_[p - 1e-9, p + 1e-9]:
            for s in (1, -1):
                best = min(best, int(np.sum(np.sign(s * (p - c)) * y <= 0)))
    print("best possible line mistakes", best)
    F = lift(X)
    h3 = perceptron(F, y, 5000, w0=[0.6, 0.8, 0.0], b0=0.3)
    print("3D: updates", len(h3) - 1, "mistakes", [h[2] for h in h3])
    w, b = h3[-1][0], h3[-1][1]
    print("3D plane w,b", w, b)
    # kernel identity check
    a, c = X[0], X[50]
    print("kernel check", lift(a[None]) @ lift(c[None]).T, kernel(a[None], c[None]))
    from sklearn.svm import SVC
    K = kernel(X, X)
    svm = SVC(kernel="precomputed", C=1e6).fit(K, y)
    print("SVM support vectors", svm.support_, "n", len(svm.support_), "train err",
          np.mean(svm.predict(K) != y))
    alpha = np.zeros(len(y)); alpha[svm.support_] = svm.dual_coef_[0]
    W = alpha @ F; B = svm.intercept_[0]
    print("SVM primal w", W, "b", B, "margin", 2 / np.linalg.norm(W))
    print("SVM circle center", -W[:2] / (2 * W[2]), "r^2", (W[0]**2 + W[1]**2) / (4 * W[2]**2) - B / W[2])
    from math import comb
    print("deg-7 monomials in 256 vars:", comb(263, 7))
