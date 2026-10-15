"""Exact t-SNE (van der Maaten & Hinton 2008) in numpy, used to generate the episode's
simulated data. Run once: python tsne_sim.py  -> tsne_data.npz"""
import numpy as np

def sq_dists(X):
    s = (X**2).sum(1)
    return np.maximum(s[:, None] + s[None, :] - 2 * X @ X.T, 0)

def calibrate(D2, perp, tol=1e-5, iters=100):
    """Binary-search beta_i = 1/(2 sigma_i^2) so that 2^H(P_i) = perp."""
    n = D2.shape[0]; P = np.zeros_like(D2); sig = np.zeros(n)
    logU = np.log(perp)
    for i in range(n):
        d = np.delete(D2[i], i)
        lo, hi, beta = 0.0, np.inf, 1.0 / np.median(d)
        for _ in range(iters):
            p = np.exp(-(d - d.min()) * beta); sp = p.sum()
            H = np.log(sp) + beta * ((d - d.min()) * p).sum() / sp
            if abs(H - logU) < tol: break
            if H > logU: lo = beta; beta = beta * 2 if hi == np.inf else (beta + hi) / 2
            else: hi = beta; beta = (beta + lo) / 2
        P[i, np.arange(n) != i] = p / sp
        sig[i] = np.sqrt(1 / (2 * beta))
    return P, sig

def tsne(X, perp=30, n_iter=1000, seed=0, snaps=(), lr=None):
    n = len(X)
    Pc, sig = calibrate(sq_dists(X), perp)
    P = (Pc + Pc.T) / (2 * n); P = np.maximum(P, 1e-12)
    rng = np.random.default_rng(seed)
    Y = rng.normal(0, 1e-4, (n, 2)); V = np.zeros_like(Y); G = np.ones_like(Y)
    lr = lr or max(n / 12 / 4, 50)
    out = {}
    for t in range(n_iter):
        ex = 12.0 if t < 250 else 1.0
        mom = 0.5 if t < 250 else 0.8
        num = 1 / (1 + sq_dists(Y)); np.fill_diagonal(num, 0)
        Q = np.maximum(num / num.sum(), 1e-12)
        PQ = (ex * P - Q) * num
        grad = 4 * ((np.diag(PQ.sum(1)) - PQ) @ Y)
        G = (G + 0.2) * ((grad > 0) != (V > 0)) + G * 0.8 * ((grad > 0) == (V > 0))
        G = np.maximum(G, 0.01)
        V = mom * V - lr * G * grad
        Y = Y + V; Y -= Y.mean(0)
        if t in snaps: out[t] = Y.copy()
    out[n_iter] = Y.copy()
    return Y, sig, out

def spread(Z):  # RMS distance of points from their centroid
    return np.sqrt(((Z - Z.mean(0))**2).sum(1).mean())

if __name__ == "__main__":
    rng = np.random.default_rng(7)
    d, m = 50, 150
    cA = np.zeros(d); cB = np.zeros(d); cB[0] = 300; cC = np.zeros(d); cC[1] = 1500
    A = cA + rng.normal(0, 1, (m, d)); B = cB + rng.normal(0, 10, (m, d)); C = cC + rng.normal(0, 1, (m, d))
    X = np.vstack([A, B, C]); lab = np.repeat([0, 1, 2], m)
    for name, Z in zip("ABC", [A, B, C]): print("true spread", name, spread(Z))
    cen = [Z.mean(0) for Z in (A, B, C)]
    print("true gaps AB AC BC", np.linalg.norm(cen[0]-cen[1]), np.linalg.norm(cen[0]-cen[2]), np.linalg.norm(cen[1]-cen[2]))
    snaps = tuple(range(0, 1000, 5))
    Y, sig, out = tsne(X, 30, 1000, seed=1, snaps=snaps)
    for k in range(3): print("map spread", "ABC"[k], spread(Y[lab == k]), "median sigma", np.median(sig[lab == k]))
    mc = [Y[lab == k].mean(0) for k in range(3)]
    print("map gaps AB AC BC", np.linalg.norm(mc[0]-mc[1]), np.linalg.norm(mc[0]-mc[2]), np.linalg.norm(mc[1]-mc[2]))
    # noise
    N = rng.normal(0, 1, (300, d))
    Yn2, _, _ = tsne(N, 2, 1000, seed=2)
    Yn30, _, _ = tsne(N, 30, 1000, seed=2)
    traj = np.stack([out[k] for k in sorted(out)])
    np.savez("tsne_data.npz", X=X, lab=lab, Y=Y, sig=sig, traj=traj, snap_iters=np.array(sorted(out)),
             noise2=Yn2, noise30=Yn30)
