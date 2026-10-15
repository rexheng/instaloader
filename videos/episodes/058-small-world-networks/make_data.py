"""Precompute every number shown in episode 58 (simulated). Run: python3 make_data.py"""
import networkx as nx, numpy as np, json
n, k = 200, 4

def ring():
    G = nx.Graph(); G.add_nodes_from(range(n))
    for i in range(n):
        for d in (1, 2):
            G.add_edge(i, (i + d) % n)
    return G

def rewire(G, m, rng):
    """Unhook m distinct lattice links; keep endpoint u, reattach other end to a random node."""
    H = G.copy(); edges = sorted(G.edges()); idx = rng.choice(len(edges), m, replace=False)
    moved = []
    for j in idx:
        u, v = edges[j]
        if rng.random() < 0.5: u, v = v, u
        while True:
            w = int(rng.integers(n))
            if w != u and not H.has_edge(u, w): break
        H.remove_edge(u, v); H.add_edge(u, w); moved.append(((u, v), (u, w)))
    return H, moved

def stats(H):
    return nx.average_shortest_path_length(H), nx.average_clustering(H), nx.diameter(H)

G = ring(); L0, C0, D0 = stats(G)
print("ring", L0, C0, D0)
# expected effect of 8 rewirings over many seeds
Ls, Cs = [], []
for s in range(400):
    H, _ = rewire(G, 8, np.random.default_rng(10_000 + s))
    if nx.is_connected(H):
        a, b, _ = stats(H); Ls.append(a); Cs.append(b)
print("8 rewired, mean over", len(Ls), "L", np.mean(Ls), np.median(Ls), np.percentile(Ls, [10, 90]), "C", np.mean(Cs))

# pick the on-screen 8-shortcut graph: typical L and C
best = None
for s in range(300):
    H, moved = rewire(G, 8, np.random.default_rng(s))
    if not nx.is_connected(H): continue
    a, b, d = stats(H)
    spans = [min((w - u) % n, (u - w) % n) for (_, (u, w)) in moved]
    score = abs(a - np.mean(Ls)) + 3 * abs(b - np.mean(Cs)) + (0.2 if min(spans) < 15 else 0)
    if best is None or score < best[0]: best = (score, s, a, b, d, moved, spans)
_, seed8, L8, C8, D8, moved8, spans = best
print("chosen seed", seed8, L8, C8, D8, spans)
H8, _ = rewire(G, 8, np.random.default_rng(seed8))
# fully random: rewire all 400
Lr, Cr = [], []
for s in range(100):
    R, _ = rewire(G, 400, np.random.default_rng(50_000 + s))
    if nx.is_connected(R):
        a, b, _ = stats(R); Lr.append(a); Cr.append(b)
print("all rewired mean", np.mean(Lr), np.mean(Cr), len(Lr))
bestR = None
for s in range(100):
    R, mv = rewire(G, 400, np.random.default_rng(50_000 + s))
    if not nx.is_connected(R): continue
    a, b, d = stats(R); sc = abs(a - np.mean(Lr)) + 5 * abs(b - np.mean(Cr))
    if bestR is None or sc < bestR[0]: bestR = (sc, s, a, b, d)
print("chosen random", bestR)
R, _ = rewire(G, 400, np.random.default_rng(50_000 + bestR[1]))
# BFS hop distances from node 0
src = 0
d_ring = nx.single_source_shortest_path_length(G, src)
d_8 = nx.single_source_shortest_path_length(H8, src)
print("max hops ring", max(d_ring.values()), "8:", max(d_8.values()), "mean from src", np.mean(list(d_8.values())))
# triangle-survival check: expected fraction of lattice triangles intact
tri0 = sum(nx.triangles(G).values()) / 3
tri8 = [sum(nx.triangles(rewire(G, 8, np.random.default_rng(20_000 + s))[0]).values()) / 3 for s in range(400)]
print("triangles", tri0, np.mean(tri8) / tri0, 0.98 ** 3)
# Watts-Strogatz curve (standard per-edge rewiring, connected realisations)
ps = np.logspace(-3, 0, 16)
Lc, Cc = [], []
for p in ps:
    a, b = [], []
    for s in range(100):
        W = nx.connected_watts_strogatz_graph(n, k, p, tries=1000, seed=int(1000 * p) * 100 + s)
        a.append(nx.average_shortest_path_length(W)); b.append(nx.average_clustering(W))
    Lc.append(np.mean(a) / L0); Cc.append(np.mean(b) / C0)
    print(f"p={p:.4f} L/L0={Lc[-1]:.3f} C/C0={Cc[-1]:.3f}")
json.dump({"L0": L0, "C0": C0, "D0": D0, "seed8": int(seed8), "L8": L8, "C8": C8, "D8": D8,
           "shortcuts": [[int(u), int(w)] for (_, (u, w)) in moved8],
           "removed": [[int(a), int(b)] for ((a, b), _) in moved8],
           "Lr": bestR[2], "Cr": bestR[3], "random_edges": [list(map(int, e)) for e in R.edges()],
           "hops_ring": [d_ring[i] for i in range(n)], "hops_8": [d_8[i] for i in range(n)],
           "ps": ps.tolist(), "Lc": Lc, "Cc": Cc, "L8_mean": float(np.mean(Ls)), "C8_mean": float(np.mean(Cs))},
          open("data.json", "w"))
