"""Schelling (1971) checkerboard model, as simulated in episode 75.

Rules (all stated on screen / in narration):
  * 40 x 40 board, 10 % of squares empty, the rest split evenly between blue and gold
    households, placed uniformly at random.
  * A household's neighbours are the occupied squares among the 8 around it (fewer at
    the edge; the board does not wrap).
  * A household is content if  same / occupied >= demand  (a household with no
    neighbours is content).
  * Each round: every household that is unhappy at the start of the round, in random
    order, moves (if it is still unhappy when its turn comes) to an empty square chosen
    uniformly at random among those where it would be content.
  * Stop when nobody is unhappy (or nobody can move).

Pure numpy, deterministic for a given seed.  `python sim.py` prints every number used
in the episode and writes sim_cache.json next to this file.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

N = 40
VACANCY = 0.10
EMPTY, BLUE_H, GOLD_H = 0, 1, 2
OFFS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]


def neighbour_counts(g):
    """(# blue neighbours, # gold neighbours) for every square."""
    b = np.zeros(g.shape, int)
    y = np.zeros(g.shape, int)
    pb = np.pad(g == BLUE_H, 1)
    py = np.pad(g == GOLD_H, 1)
    for dr, dc in OFFS:
        b += pb[1 + dr:1 + dr + g.shape[0], 1 + dc:1 + dc + g.shape[1]]
        y += py[1 + dr:1 + dr + g.shape[0], 1 + dc:1 + dc + g.shape[1]]
    return b, y


def same_occ(g):
    b, y = neighbour_counts(g)
    same = np.where(g == BLUE_H, b, np.where(g == GOLD_H, y, 0))
    return same, b + y


def unhappy_mask(g, t):
    same, occ = same_occ(g)
    return (g > 0) & (same < t * occ - 1e-12)


def avg_share(g):
    """Average over households (with >= 1 neighbour) of the share of neighbours that match."""
    same, occ = same_occ(g)
    m = (g > 0) & (occ > 0)
    return float((same[m] / occ[m]).mean())


def init(seed, n=N, vac=VACANCY):
    rng = np.random.default_rng(seed)
    total = n * n
    ne = int(round(vac * total))
    nb = (total - ne) // 2
    arr = np.array([EMPTY] * ne + [BLUE_H] * nb + [GOLD_H] * (total - ne - nb))
    rng.shuffle(arr)
    g = arr.reshape(n, n)
    ids = -np.ones((n, n), int)
    occ = np.argwhere(g > 0)
    for k, (r, c) in enumerate(occ):
        ids[r, c] = k
    return g, ids, rng


def _content_cells(g, col, t):
    b, y = neighbour_counts(g)
    same = b if col == BLUE_H else y
    return (g == EMPTY) & (same >= t * (b + y) - 1e-12)


def step(g, ids, t, rng):
    """One round, in place. Returns a list of moves (id, (r0, c0), (r1, c1), colour)."""
    idx = np.argwhere(unhappy_mask(g, t))
    rng.shuffle(idx)
    moves = []
    for r, c in idx:
        col = g[r, c]
        same, occ = _local(g, r, c, col)
        if same >= t * occ - 1e-12:
            continue                                  # became content before its turn
        hid = ids[r, c]
        g[r, c] = EMPTY                               # lift the mover off the board
        ok = _content_cells(g, col, t)
        ok[r, c] = False                              # it may not "move" to its own square
        cand = np.argwhere(ok)
        if len(cand) == 0:
            g[r, c] = col
            continue
        er, ec = cand[rng.integers(len(cand))]
        g[er, ec] = col
        ids[r, c] = -1
        ids[er, ec] = hid
        moves.append((int(hid), (int(r), int(c)), (int(er), int(ec)), int(col)))
    return moves


def _local(g, r, c, col):
    s = o = 0
    for dr, dc in OFFS:
        rr, cc = r + dr, c + dc
        if 0 <= rr < g.shape[0] and 0 <= cc < g.shape[1] and g[rr, cc] > 0:
            o += 1
            s += g[rr, cc] == col
    return s, o


def run(seed, t=1 / 3, max_rounds=300):
    g, ids, rng = init(seed)
    states = [(g.copy(), ids.copy())]
    rounds = []
    while len(rounds) < max_rounds:
        mv = step(g, ids, t, rng)
        rounds.append(mv)
        states.append((g.copy(), ids.copy()))
        if not unhappy_mask(g, t).any() or not mv:
            break
    return states, rounds


# ----------------------------------------------------------------------------- episode data
SEED = 3                     # the town shown in the episode (typical: 30-town mean is 0.75)
SWEEP_SEEDS = list(range(30))      # 30 towns per demand level, includes SEED
SWEEP_T = [0.0, 0.1, 0.2, 0.25, 1 / 3, 0.4, 0.5, 0.6]


def per_move_trace(g0, ids0, rounds, t):
    """Replay moves one at a time: unhappy set + average share after every move."""
    g = g0.copy()
    trace = []
    for mv in rounds:
        rt = []
        for hid, (r, c), (er, ec), col in mv:
            g[r, c] = EMPTY
            g[er, ec] = col
            rt.append({"unhappy": int(unhappy_mask(g, t).sum()), "share": avg_share(g)})
        trace.append(rt)
    return trace


def build_cache(path: Path):
    t = 1 / 3
    states, rounds = run(SEED, t)
    g0, ids0 = states[0]
    colour = {}
    pos = {}
    for (r, c) in np.argwhere(g0 > 0):
        colour[int(ids0[r, c])] = int(g0[r, c])
        pos[int(ids0[r, c])] = (int(r), int(c))
    unhappy_by_state = []
    share_by_state = []
    for g, ids in states:
        um = unhappy_mask(g, t)
        unhappy_by_state.append(sorted(int(ids[r, c]) for r, c in np.argwhere(um)))
        share_by_state.append(avg_share(g))
    final_pos = {}
    gF, idsF = states[-1]
    for (r, c) in np.argwhere(gF > 0):
        final_pos[int(idsF[r, c])] = (int(r), int(c))
    # same starting town, demand of a quarter
    q_states, q_rounds = run(SEED, 0.25)
    qF, qidsF = q_states[-1]
    q_final_pos = {int(qidsF[r, c]): (int(r), int(c)) for r, c in np.argwhere(qF > 0)}
    sweep = {}
    for tt in SWEEP_T:
        vals = []
        for s in SWEEP_SEEDS:
            st, _ = run(s, tt)
            vals.append(avg_share(st[-1][0]))
        sweep[f"{tt:.4f}"] = vals
    data = {
        "seed": SEED, "n": N, "vacancy": VACANCY,
        "colour": colour, "start_pos": pos, "final_pos": final_pos,
        "rounds": [[[m[0], m[1], m[2], m[3]] for m in mv] for mv in rounds],
        "unhappy_by_state": unhappy_by_state, "share_by_state": share_by_state,
        "trace": per_move_trace(g0, ids0, rounds, t),
        "quarter": {"final_pos": q_final_pos, "rounds": len(q_rounds),
                    "moves": sum(len(m) for m in q_rounds), "share": avg_share(qF)},
        "sweep": sweep,
    }
    path.write_text(json.dumps(data))
    return data


def load(path: Path | None = None):
    path = path or Path(__file__).with_name("sim_cache.json")
    if path.exists():
        d = json.loads(path.read_text())
    else:
        d = build_cache(path)
    for k in ("colour", "start_pos", "final_pos"):
        d[k] = {int(i): (tuple(v) if isinstance(v, list) else v) for i, v in d[k].items()}
    d["quarter"]["final_pos"] = {int(i): tuple(v) for i, v in d["quarter"]["final_pos"].items()}
    return d


CHAIN = {"A": (4, 15), "B": (4, 14), "C": (3, 13), "D": (3, 12)}   # the corner shown on screen

# ----------------------------------------------------------------------------- share ladder
def share_ladder(g):
    """{Fraction(same, occupied): number of households} for a board (households with no
    occupied neighbour are content at any demand and are left out; there are none in SEED)."""
    from collections import Counter
    from fractions import Fraction
    same, occ = same_occ(g)
    c = Counter()
    for r, cc in np.argwhere(g > 0):
        if occ[r, cc]:
            c[Fraction(int(same[r, cc]), int(occ[r, cc]))] += 1
    return c


def round1_breakdown(seed=SEED, t=1 / 3):
    """Replay round 1 and classify every household unhappy at its start: moved, became
    content before its turn (a neighbour's move fixed it), or found no acceptable square."""
    g, ids, rng = init(seed)
    idx = np.argwhere(unhappy_mask(g, t))
    rng.shuffle(idx)
    out = {"moved": 0, "content_before_turn": 0, "no_destination": 0}
    for r, c in idx:
        col = g[r, c]
        s, o = _local(g, r, c, col)
        if s >= t * o - 1e-12:
            out["content_before_turn"] += 1
            continue
        g[r, c] = EMPTY
        ok = _content_cells(g, col, t)
        ok[r, c] = False
        cand = np.argwhere(ok)
        if len(cand) == 0:
            g[r, c] = col
            out["no_destination"] += 1
            continue
        er, ec = cand[rng.integers(len(cand))]
        g[er, ec] = col
        out["moved"] += 1
    return out


# ----------------------------------------------------------------------------- zoned town
# A second, preference-free town for the two-town test: 160 squares are left empty at
# random; the board is split into irregular zones by a rule (a fine random field, cut at the
# median over the occupied squares, so the two colours get exactly 720 squares each); every
# household lives in a zone marked for its colour.  Nobody has a demand and nobody moves.
# The field's grain (ZONE_SIGMA, ZONE_NOISE) is chosen so the town's texture matches a
# Schelling town (no stray single tiles), not just its 76 %: the map alone cannot tell them
# apart (texture statistics: texture_stats(), printed by `python sim.py`).
ZONE_SEED, ZONE_SIGMA, ZONE_NOISE = 73, 1.1, 0.1


def zoned_town(seed=ZONE_SEED, sigma=ZONE_SIGMA, noise=ZONE_NOISE, n=N, vac=VACANCY):
    from scipy.ndimage import gaussian_filter
    rng = np.random.default_rng(seed)
    field = gaussian_filter(rng.standard_normal((n, n)), sigma, mode="reflect")
    field = field / field.std() + noise * rng.standard_normal((n, n))
    total = n * n
    ne = int(round(vac * total))
    empty = np.zeros(total, bool)
    empty[rng.permutation(total)[:ne]] = True
    empty = empty.reshape(n, n)
    cut = np.median(field[~empty])
    zone = np.where(field > cut, BLUE_H, GOLD_H)
    g = np.where(empty, EMPTY, zone)
    assert int((g == BLUE_H).sum()) == int((g == GOLD_H).sum()) == (total - ne) // 2
    return g, zone


def texture_stats(g):
    """Map texture: mean share, households below 1/3, single-colour clusters (8-connected),
    clusters of <= 3 households, 4-neighbour unlike pairs."""
    from scipy.ndimage import label
    same, occ = same_occ(g)
    m = (g > 0) & (occ > 0)
    s = same[m] / occ[m]
    sizes = []
    for col in (BLUE_H, GOLD_H):
        lab, k = label(g == col, structure=np.ones((3, 3)))
        sizes += list(np.bincount(lab.ravel())[1:])
    sizes = np.array(sizes)
    unlike = sum(int(((a > 0) & (b > 0) & (a != b)).sum())
                 for a, b in ((g[:, :-1], g[:, 1:]), (g[:-1, :], g[1:, :])))
    return {"share": round(float(s.mean()), 4), "below_third": round(float((s < 1 / 3).mean()), 3),
            "clusters": int(len(sizes)), "clusters_le3": int((sizes <= 3).sum()),
            "unlike_pairs": unlike}


def report_extra():
    from fractions import Fraction
    g0 = init(SEED)[0]
    lad = share_ladder(g0)
    print("share ladder at the start (fraction: households):",
          ", ".join(f"{f}: {v}" for f, v in sorted(lad.items())))
    q, th = Fraction(1, 4), Fraction(1, 3)
    print("unhappy at start: demand 1/4 ->", sum(v for f, v in lad.items() if f < q),
          "| demand 1/3 ->", sum(v for f, v in lad.items() if f < th),
          "| rungs in [1/4, 1/3):", {str(f): v for f, v in sorted(lad.items()) if q <= f < th})
    print("round 1 breakdown of the 238:", round1_breakdown())
    gz, zone = zoned_town()
    bl = int((gz == BLUE_H).sum())
    gd = int((gz == GOLD_H).sum())
    in_own = float(((gz > 0) & (gz == zone)).sum() / (gz > 0).sum())
    print(f"zoned town: share {avg_share(gz):.4f} (seed-3 town {avg_share(run(SEED)[0][-1][0]):.4f}); "
          f"blue {bl} gold {gd} empty {int((gz == 0).sum())}; living in own colour's zone {in_own:.3f}")
    print("texture, seed-3 Schelling town:", texture_stats(run(SEED)[0][-1][0]))
    print("texture, zoned town:           ", texture_stats(gz))


def verify_chain():
    """Print (colour, same, occupied) for the corner chain after each round, the round in which
    each leaves (demand 1/3), and whether any of them moves when the demand is 1/4."""
    st, rounds = run(SEED, 1 / 3)
    for k in range(5):
        g = st[k][0]
        row = {n: (int(g[rc]), *map(int, _local(g, rc[0], rc[1], g[rc]))) for n, rc in CHAIN.items()}
        print("chain after round", k, row)
    for k, mv in enumerate(rounds):
        for hid, a, b, col in mv:
            for n, rc in CHAIN.items():
                if tuple(a) == rc:
                    print(f"chain: {n} {rc} leaves in round {k + 1}")
    _, rq = run(SEED, 0.25)
    moved = {tuple(a) for mv in rq for _, a, _, _ in mv}
    print("demand 1/4: chain households that ever move:", [n for n, rc in CHAIN.items() if rc in moved])


if __name__ == "__main__":
    import time
    t0 = time.time()
    p = Path(__file__).with_name("sim_cache.json")
    d = build_cache(p)
    print(f"built in {time.time() - t0:.1f}s")
    n_h = len(d["colour"])
    print("households", n_h, "blue", sum(v == 1 for v in d["colour"].values()))
    print("share by state", [round(x, 4) for x in d["share_by_state"]])
    print("unhappy by state", [len(u) for u in d["unhappy_by_state"]])
    print("moves per round", [len(r) for r in d["rounds"]])
    u0 = len(d["unhappy_by_state"][0])
    print(f"initially unhappy {u0} = {u0 / n_h:.3f} = 1 in {n_h / u0:.2f}")
    movers1 = {m[0] for m in d["rounds"][0]}
    u1 = d["unhappy_by_state"][1]
    print("unhappy after r1", len(u1), "of which never moved in r1:", sum(h not in movers1 for h in u1),
          "never unhappy at start:", sum(h not in set(d['unhappy_by_state'][0]) for h in u1))
    print("quarter:", d["quarter"]["rounds"], "rounds", d["quarter"]["moves"], "moves, share",
          round(d["quarter"]["share"], 4))
    for k, v in d["sweep"].items():
        print("demand", k, "mean %.3f sd %.3f min %.3f max %.3f" % (np.mean(v), np.std(v), min(v), max(v)))
    verify_chain()
    report_extra()
