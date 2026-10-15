"""Episode 35 simulation (all data on screen is SIMULATED).
Rule: gold if x2 > 5 + 2.2 sin(0.75 x1), x in [0,10]^2, 15% of labels flipped.
Writes data.npz used by scene.py and prints every number the script uses."""
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

NOISE, N, SEED, B = 0.15, 300, 1, 200
def truthf(X): return (X[:, 1] > 5 + 2.2 * np.sin(X[:, 0] * 0.75)).astype(int)
def make(n, rng):
    X = rng.uniform(0, 10, (n, 2)); y = truthf(X)
    return X, np.where(rng.random(n) < NOISE, 1 - y, y)

R = 400                                   # evaluation / image grid (area fraction = error)
g = (np.arange(R) + 0.5) * 10 / R
G = np.array([(a, b) for b in g for a in g]); T = truthf(G)
img = lambda v: v.reshape(R, R)[::-1]     # row 0 = top (x2 = 10)
out = {}

X, y = make(N, np.random.default_rng(SEED))
out["X"], out["y"], out["clean"] = X, y, (y == truthf(X))
tree = DecisionTreeClassifier(random_state=0).fit(X, y)
p_tree = tree.predict(G)
print("training accuracy", (tree.predict(X) == y).mean(), "leaves", tree.get_n_leaves(),
      "depth", tree.get_depth(), "mislabeled", (~out["clean"]).sum())
print("single tree error vs truth", (p_tree != T).mean())
out["tree"] = img(p_tree)
for d in (1, 2, 3, 4, 6):
    out[f"depth{d}"] = img(DecisionTreeClassifier(max_depth=d, random_state=0).fit(X, y).predict(G))

def lonely_boxes(t, Xs, ys):
    """Leaf rectangles that hold exactly one training point, and that point is mislabelled."""
    tr = t.tree_; boxes = []
    def rec(node, lo, hi):
        if tr.children_left[node] == -1:
            if tr.n_node_samples[node] == 1:
                inside = np.all((Xs >= lo) & (Xs <= hi), 1)
                i = np.flatnonzero(inside)
                if len(i) == 1 and ys[i[0]] != truthf(Xs[i])[0]:
                    boxes.append([lo[0], lo[1], hi[0], hi[1]])
            return
        f, th = tr.feature[node], tr.threshold[node]
        h2 = hi.copy(); h2[f] = th; rec(tr.children_left[node], lo, h2)
        l2 = lo.copy(); l2[f] = th; rec(tr.children_right[node], l2, hi)
    rec(0, np.zeros(2), np.full(2, 10.0))
    return np.array(boxes)

out["tree_boxes"] = lonely_boxes(tree, X, y)
print("one-point mislabelled boxes in the tree", len(out["tree_boxes"]))

# same rule, fresh samples -> the tree jumps (variance)
for k, s in enumerate((101, 102, 103)):
    Xf, yf = make(N, np.random.default_rng(s))
    out[f"fresh{k}"] = img(DecisionTreeClassifier(random_state=0).fit(Xf, yf).predict(G))
    out[f"freshX{k}"], out[f"freshy{k}"] = Xf, yf
    out[f"fresh_boxes{k}"] = lonely_boxes(DecisionTreeClassifier(random_state=0).fit(Xf, yf), Xf, yf)

# one bootstrap resample, shown explicitly
rng = np.random.default_rng(5)
idx = rng.integers(0, N, N)
cnt = np.bincount(idx, minlength=N)
out["boot_count"] = cnt
print("bootstrap: points left out", (cnt == 0).mean(), "theory", (1 - 1 / N) ** N)
out["boot_tree"] = img(DecisionTreeClassifier(random_state=0).fit(X[idx], y[idx]).predict(G))

roots = {}
def votes(mf):
    f = RandomForestClassifier(B, max_features=mf, random_state=1).fit(X, y)
    roots[mf] = np.array([[e.tree_.feature[0], e.tree_.threshold[0]] for e in f.estimators_])
    return np.array([e.predict(G) for e in f.estimators_], dtype=np.float32)
for name, mf in (("bag", None), ("rf", 1)):
    V = votes(mf)
    cum = np.cumsum(V, 0) / np.arange(1, B + 1)[:, None]
    err = ((cum > 0.5) != T).mean(1)
    out[f"{name}_err"] = err
    ind = (V != T).mean(1)
    print(name, "forest error", err[-1], "error at B=1..10", np.round(err[:10], 3),
          "B=20,50,100,150", np.round(err[[19, 49, 99, 149]], 3),
          "individual tree error mean", ind.mean())
    out[f"{name}_bits"] = np.packbits(np.array([img(v) for v in V], dtype=bool), axis=0)
    out[f"{name}_roots"] = roots[mf]
    print(name, "root split on feature 2 share", (roots[mf][:, 0] == 1).mean())
    if name == "rf":
        out["rf_tree0"] = img(V[0]); print("rf tree 0 error", ind[0])

# variance of the vote across M fresh datasets -> sigma^2, rho, formula check
M, Bv = 40, 100
gg = (np.arange(60) + 0.5) / 6; GG = np.array([(a, b) for b in gg for a in gg])
for name, mf in (("bag", None), ("rf", 1)):
    V = np.zeros((M, Bv, len(GG)), dtype=np.float32)
    for m in range(M):
        Xm, ym = make(N, np.random.default_rng(1000 + m))
        f = RandomForestClassifier(Bv, max_features=mf, random_state=m).fit(Xm, ym)
        V[m] = [e.predict(GG) for e in f.estimators_]
    s2 = V.var(axis=(0, 1)).mean()
    S, SS = V.sum(1), (V ** 2).sum(1)
    cov = ((S ** 2 - SS) / (Bv * (Bv - 1))).mean(0) - V.mean(axis=(0, 1)) ** 2
    rho = cov.mean() / s2
    bvals = np.array([1, 2, 3, 5, 10, 20, 30, 50, 75, 100])
    meas = np.array([(V[:, :b].mean(1)).var(0).mean() for b in bvals])
    pred = rho * s2 + (1 - rho) * s2 / bvals
    out[f"{name}_s2"], out[f"{name}_rho"] = s2, rho
    out[f"{name}_bvals"], out[f"{name}_meas"], out[f"{name}_pred"] = bvals, meas, pred
    print(name, "sigma2", round(s2, 4), "rho", round(rho, 3), "floor", round(rho * s2, 4))
    print("   B", bvals, "\n   measured", np.round(meas, 4), "\n   formula ", np.round(pred, 4))
np.savez_compressed("data.npz", **out)
