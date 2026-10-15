"""Data for episode 64. Run once: python3 simulate.py -> data.json (deterministic).

Karate club: networkx.karate_club_graph() (Zachary 1977; 'club' = club joined after the split).
All modularity values unweighted (Newman & Girvan 2004 definition)."""
import json
import networkx as nx
import numpy as np
from scipy.optimize import linear_sum_assignment

G0 = nx.karate_club_graph()
G = nx.Graph(G0.edges())
N, M = 34, 78
club = [0 if G0.nodes[i]["club"] == "Mr. Hi" else 1 for i in range(N)]   # 0 = Mr. Hi, 1 = Officer


def mod_matrix(H):
    A = nx.to_numpy_array(H, nodelist=range(N)); k = A.sum(1); m = k.sum() / 2
    return A - np.outer(k, k) / (2 * m), m


def Q(H, s):
    B, m = mod_matrix(H); s = np.asarray(s, float)
    return float(s @ B @ s / (4 * m))


def spectral(H):
    B, m = mod_matrix(H); w, v = np.linalg.eigh(B)
    return np.where(v[:, -1] >= 0, 1.0, -1.0)


def refine(H, s):
    B, m = mod_matrix(H); s = s.copy(); f = lambda s: s @ B @ s
    imp = True
    while imp:
        imp = False
        for i in range(N):
            s2 = s.copy(); s2[i] *= -1
            if f(s2) > f(s) + 1e-12:
                s, imp = s2, True
    return s


def best_bisection(H, rng, tries=30):
    B, m = mod_matrix(H); f = lambda s: s @ B @ s / (4 * m); best = -1
    for _ in range(tries):
        s = rng.choice([-1, 1], N).astype(float); imp = True
        while imp:
            imp = False
            for i in rng.permutation(N):
                q = f(s); s[i] *= -1
                if f(s) > q + 1e-12: imp = True
                else: s[i] *= -1
        best = max(best, f(s))
    return best


def orient(s):                      # +1 = the group containing member 1 (Mr. Hi)
    return s if s[0] > 0 else -s


pos = nx.kamada_kawai_layout(G)
P = np.array([pos[i] for i in range(N)])
if P[0, 0] > P[33, 0]: P[:, 0] *= -1          # Mr. Hi on the left, president on the right
P -= P.mean(0); P /= np.abs(P).max(0)

# naive: global minimum cut
cut_value, (a, b) = nx.stoer_wagner(G)
small = a if len(a) < len(b) else b
naive = [1.0 if i in small else -1.0 for i in range(N)]

found = orient(spectral(G))
wrong_found = [i for i in range(N) if (found[i] > 0) != (club[i] == 0)]
grp = [i for i in range(N) if found[i] > 0]
A = nx.to_numpy_array(G, nodelist=range(N)); k = A.sum(1)

rng = np.random.default_rng(64)
qs, twins = [], []
for r in range(300):
    H = G.copy(); nx.double_edge_swap(H, nswap=10 * M, max_tries=100000, seed=int(rng.integers(1e9)))
    qs.append(best_bisection(H, rng)); twins.append(H)

# a representative shuffled club: refined spectral Q closest to the median shuffle
med = float(np.median(qs))
cands = []
for H in twins[:60]:
    s = orient(refine(H, spectral(H))); cands.append((abs(Q(H, s) - med), H, s))
_, T, ts = min(cands, key=lambda c: c[0])
E0 = sorted(G.edges()); E1 = sorted(T.edges())
cost = np.array([[min(np.linalg.norm(P[u] - P[x]) + np.linalg.norm(P[v] - P[y]),
                      np.linalg.norm(P[u] - P[y]) + np.linalg.norm(P[v] - P[x]))
                  for (x, y) in E1] for (u, v) in E0])
r_, c_ = linear_sum_assignment(cost)
twin_edges = [None] * M
for i, j in zip(r_, c_):
    (u, v), (x, y) = E0[i], E1[j]
    d1 = np.linalg.norm(P[u] - P[x]) + np.linalg.norm(P[v] - P[y])
    d2 = np.linalg.norm(P[u] - P[y]) + np.linalg.norm(P[v] - P[x])
    twin_edges[i] = [x, y] if d1 <= d2 else [y, x]

out = dict(
    pos=P.tolist(), edges=[list(e) for e in E0], club=club, degree=k.tolist(),
    naive=naive, naive_cut=cut_value, naive_Q=Q(G, naive),
    naive_wrong=min(sum((naive[i] > 0) != (club[i] == 0) for i in range(N)),
                    sum((naive[i] > 0) != (club[i] == 1) for i in range(N))),
    found=found.tolist(), found_Q=Q(G, found), found_wrong=wrong_found,
    found_inside=int(A[np.ix_(grp, grp)].sum() / 2 + A[np.ix_([i for i in range(N) if i not in grp],
                                                             [i for i in range(N) if i not in grp])].sum() / 2),
    found_ends_A=float(k[grp].sum()),
    exact_max_bisection_Q=best_bisection(G, np.random.default_rng(1), 200),
    club_Q=Q(G, [1.0 if c == 0 else -1.0 for c in club]),
    shuffle_Q=qs, shuffle_mean=float(np.mean(qs)), shuffle_max=float(np.max(qs)),
    shuffle_min=float(np.min(qs)),
    twin_edges=twin_edges, twin_split=ts.tolist(), twin_Q=Q(T, ts),
)
json.dump(out, open("data.json", "w"))
for kk in ("naive_cut", "naive_Q", "naive_wrong", "found_Q", "found_wrong", "found_inside", "found_ends_A",
           "exact_max_bisection_Q", "club_Q", "shuffle_mean", "shuffle_min", "shuffle_max", "twin_Q"):
    print(kk, out[kk])
print("twin split sizes", sum(1 for x in ts if x > 0), "persisting edges", sum(1 for e, t in zip(E0, twin_edges) if set(e) == set(t)))
