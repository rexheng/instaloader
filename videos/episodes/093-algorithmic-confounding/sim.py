"""Simulation for episode 93 (deterministic). Two copies of the same random network;
each person adds new friends either (A) uniformly at random or (B) by accepting a
friend-of-a-friend suggestion. Nobody has any preference for triangles in (A).
Reports average local clustering (networkx definition, degree<2 nodes count as 0)."""
import numpy as np, networkx as nx

def base_graph(n, m, rng):
    g = nx.empty_graph(n)
    while g.number_of_edges() < m:
        a, b = rng.choice(n, 2, replace=False)
        g.add_edge(int(a), int(b))
    return g

def step(g, rule, rng, order):
    added = []
    n = g.number_of_nodes()
    for i in order:
        i = int(i)
        cand = None
        if rule == "fof":
            fr = list(g.neighbors(i))
            fof = sorted({m for j in fr for m in g.neighbors(j)} - set(fr) - {i})
            if fof:
                # pick a friend uniformly, then one of their friends (path-weighted)
                rng.shuffle(fr)
                for j in fr:
                    opts = [m for m in g.neighbors(j) if m != i and not g.has_edge(i, m)]
                    if opts:
                        cand = (int(rng.choice(opts)), j)
                        break
        if cand is None:
            opts = [m for m in range(n) if m != i and not g.has_edge(i, m)]
            cand = (int(rng.choice(opts)), None)
        g.add_edge(i, cand[0])
        added.append((i, cand[0], cand[1]))
    return added

def run(n, m0, rounds, seed):
    rng = np.random.default_rng(seed)
    g0 = base_graph(n, m0, rng)
    out = {"base": nx.average_clustering(g0)}
    res = {}
    for rule in ("random", "fof"):
        r2 = np.random.default_rng(seed + 1000)
        g = g0.copy()
        traj = [nx.average_clustering(g)]
        adds = []
        for _ in range(rounds):
            order = r2.permutation(n)
            for e in step_one_by_one(g, rule, r2, order):
                adds.append(e); traj.append(nx.average_clustering(g))
        res[rule] = (g, traj, adds)
    return g0, res

def step_one_by_one(g, rule, rng, order):
    for i in order:
        yield step(g, rule, rng, [i])[0]

if __name__ == "__main__":
    import sys
    for (n, m0, rounds) in [(40, 40, 1), (40, 40, 2), (48, 60, 1), (60, 90, 1), (36, 36, 2)]:
        rs, fs, bs = [], [], []
        for s in range(200):
            g0, res = run(n, m0, rounds, s)
            bs.append(res["random"][1][0]); rs.append(res["random"][1][-1]); fs.append(res["fof"][1][-1])
        print(n, m0, rounds, "base %.3f  random %.3f [%.3f-%.3f]  fof %.3f [%.3f-%.3f]" % (
            np.mean(bs), np.mean(rs), *np.percentile(rs, [5, 95]), np.mean(fs), *np.percentile(fs, [5, 95])))
