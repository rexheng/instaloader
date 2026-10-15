"""Simulated towns for episode 65 (all numbers on screen labelled 'simulated').

Town A (latent homophily, ZERO influence): hidden trait z ~ N(0,1); each person is tied to the
4 people nearest to them in z; each period, a person without the trait acquires it with
probability sigmoid(-2.4 + 1.0 z), independent of friends.
Town B (contagion, NO homophily): 4 random ties per person on average; each period
P(acquire) = 1 - (1-0.077)(1-0.042)^(# friends who acquired it last period).
Test (the 'standard' lagged comparison): among people without the trait at t-1, P(acquire at t)
when >= 1 friend acquired it at t-1, vs when none did.  Periods t = 2..5.
"""
import numpy as np


def lagtest(adj, traj):
    T, N = traj.shape
    a = [0, 0]; b = [0, 0]
    for t in range(2, T):
        new_prev = traj[t - 1] & ~traj[t - 2]
        for i in range(N):
            if traj[t - 1, i]:
                continue
            ex = any(new_prev[j] for j in adj[i])
            (a if ex else b)[0] += traj[t, i]
            (a if ex else b)[1] += 1
    pa, pb = a[0] / a[1], b[0] / b[1]
    rr = pa / pb
    se = np.sqrt(1 / a[0] - 1 / a[1] + 1 / b[0] - 1 / b[1])
    return dict(p_exposed=pa, p_unexposed=pb, excess=rr - 1,
                ci=(rr * np.exp(-1.96 * se) - 1, rr * np.exp(1.96 * se) - 1))


def town_a(N, rng, k=4, b=1.0, base=-2.4, T=6):
    z = rng.normal(size=N)
    order = np.argsort(z); rank = np.empty(N, int); rank[order] = np.arange(N)
    adj = [set() for _ in range(N)]
    for i in range(N):
        for d in range(1, k // 2 + 1):
            for rr in (rank[i] - d, rank[i] + d):
                if 0 <= rr < N:
                    j = order[rr]; adj[i].add(j); adj[j].add(i)
    p = 1 / (1 + np.exp(-(base + b * z)))
    traj = np.zeros((T, N), bool); traj[0] = rng.random(N) < p
    for t in range(1, T):
        traj[t] = traj[t - 1] | (rng.random(N) < p)
    return lagtest(adj, traj)


def town_b(N, rng, k=4, q0=0.077, q1=0.042, T=6):
    adj = [set() for _ in range(N)]
    for i in range(N):
        for j in rng.choice(N, k // 2, replace=False):
            if j != i:
                adj[i].add(j); adj[j].add(i)
    traj = np.zeros((T, N), bool); traj[0] = rng.random(N) < q0
    for t in range(1, T):
        new_prev = traj[t - 1] & ~(traj[t - 2] if t >= 2 else np.zeros(N, bool))
        n = np.array([sum(new_prev[j] for j in adj[i]) for i in range(N)])
        traj[t] = traj[t - 1] | (rng.random(N) < 1 - (1 - q0) * (1 - q1) ** n)
    return lagtest(adj, traj)


if __name__ == "__main__":
    for N in (2000, 200000):
        for name, f in (("A", town_a), ("B", town_b)):
            r = f(N, np.random.default_rng(65))
            print(name, N, {k: (np.round(v, 4) if not isinstance(v, tuple) else tuple(np.round(v, 3)))
                            for k, v in r.items()})
