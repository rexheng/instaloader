"""Deterministic 36-person towns for the on-screen illustration (simulated)."""
import numpy as np

W, H = 5.0, 4.0          # panel size in scene units


def build(seed=3, n_side=6, late=4, n_purple=18):
    rng = np.random.default_rng(seed)
    g = np.array([(i, j) for i in range(n_side) for j in range(n_side)], float)
    pos = (g + 0.5) / n_side * [W, H] - [W / 2, H / 2]
    pos += rng.uniform(-0.22, 0.22, pos.shape) * [W / n_side, H / n_side]
    N = len(pos)
    purple = np.zeros(N, bool); purple[rng.choice(N, n_purple, replace=False)] = True
    # hidden appetite: purple high, gray low, except `late` grays that are high
    z = np.where(purple, rng.uniform(0.65, 1.0, N), rng.uniform(0.0, 0.35, N))
    grays = np.flatnonzero(~purple)
    late_ids = rng.choice(grays, late, replace=False)
    z[late_ids] = rng.uniform(0.7, 0.9, late)
    d = np.linalg.norm(pos[:, None] - pos[None], axis=2); np.fill_diagonal(d, 1e9)
    edges = set()
    for i in range(N):
        for j in np.argsort(d[i])[:2]:
            edges.add((min(i, j), max(i, j)))
    edges = sorted(edges)
    return pos, purple, z, late_ids, edges, d


def rewire(pos, z, edges, d, thr=0.3, dmax=1.5):
    """Town A: a tie between dissimilar (hidden-trait) people is dropped, and one of the two
    re-ties to the nearest similar person within reach (positions never change)."""
    cur = set(edges); moves = []
    for (i, j) in edges:
        if abs(z[i] - z[j]) <= thr:
            continue
        cur.discard((i, j))
        best = None
        for mover, other in ((i, j), (j, i)):
            for k in np.argsort(d[mover]):
                if d[mover, k] > dmax:
                    break
                e = (min(mover, k), max(mover, k))
                if k not in (mover, other) and abs(z[k] - z[mover]) <= thr and e not in cur:
                    if best is None or d[mover, k] < best[0]:
                        best = (d[mover, k], mover, e)
                    break
        if best is None:
            moves.append(((i, j), None, None))
        else:
            cur.add(best[2]); moves.append(((i, j), best[2], best[1]))
    return sorted(cur), moves


def repaint(purple, edges, rounds=3):
    """Town B: each round, people adopt the colour most of their friends have (ties keep)."""
    N = len(purple); nb = [[] for _ in range(N)]
    for i, j in edges:
        nb[i].append(j); nb[j].append(i)
    states = [purple.copy()]
    c = purple.copy()
    for _ in range(rounds):
        new = c.copy()
        for i in range(N):
            if not nb[i]:
                continue
            m = np.mean(c[nb[i]])
            if m > 0.5: new[i] = True
            elif m < 0.5: new[i] = False
        c = new; states.append(c.copy())
    return states


def match(colors, edges):
    return np.mean([colors[i] == colors[j] for i, j in edges])


if __name__ == "__main__":
    for seed in range(40):
        pos, purple, z, late, edges, d = build(seed)
        ea, moves = rewire(pos, z, edges, d)
        sb = repaint(purple, edges)
        print(seed, len(edges), "start %.2f" % match(purple, edges), "A %.2f" % match(purple, ea),
              "B %.2f" % match(sb[-1], edges), "purpB", sb[-1].sum(), "lost", sum(m[1] is None for m in moves),
              "late-in-A-purple-ties", [sum(purple[k] for e in ea for k in e if l in e and k != l) for l in late])


def relayout(pos, edges, iters=60, seed=1):
    """Town A after rewiring: redraw with a spring layout so ties are short (layout only)."""
    import networkx as nx
    G = nx.Graph(); G.add_nodes_from(range(len(pos))); G.add_edges_from(edges)
    p = nx.spring_layout(G, pos={i: tuple(pos[i]) for i in range(len(pos))}, iterations=iters,
                         seed=seed, k=0.55)
    q = np.array([p[i] for i in range(len(pos))])
    q -= q.mean(0)
    q = q / np.abs(q).max(0) * [W / 2, H / 2]
    return q
