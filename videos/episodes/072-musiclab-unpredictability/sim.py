import numpy as np
S, N, W = 48, 700, 8
def gini(d):
    m = d / d.sum(); return np.abs(m[:,None]-m[None,:]).sum()/(2*S*m.sum())
def run(q, s, rng):
    d = np.zeros(S)
    for _ in range(N):
        w = q * (d + 1) ** s
        d[rng.choice(S, p=w / w.sum())] += 1
    return d
def unpred(D):
    M = D / D.sum(1, keepdims=True); W=len(D)
    return np.mean([np.abs(M[j]-M[k]).mean() for j in range(W) for k in range(j+1,W)])
def ranks(d):  # 1 = most downloads
    return (-d).argsort(kind='stable').argsort() + 1
if __name__ == "__main__":
    q = np.linspace(1.0, 0.35, S)     # song 0 best
    for s in [0, 0.25, 0.5, 0.75, 1.0]:
        G, U, T5 = [], [], []
        for rep in range(5):
            rng = np.random.default_rng(100 + rep)
            D = np.array([run(q, s, rng) for _ in range(W)])
            G.append(np.mean([gini(d) for d in D])); U.append(unpred(D))
            T5.append(np.mean([np.isin(np.argsort(-d)[:5], range(5)).mean() for d in D]))
        print(f"s={s}: gini {np.mean(G):.3f}  U {np.mean(U):.4f}  top5 {np.mean(T5):.2f}")
