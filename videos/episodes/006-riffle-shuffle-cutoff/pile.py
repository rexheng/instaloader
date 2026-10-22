"""Seeded sample for the 'pile decks onto their counts' beat (writes pile.json).

40 decks of each kind, counted by rising sequences: our two on-screen decks (4 riffles: 14;
perfect: 26) plus 39 more of each -- forward GSR riffles (4 of them, from a sorted deck) and
uniformly random permutations.  Labelled "40 simulated decks each" on screen; the stacks then
morph into the exact distributions (Bayer & Diaconis Thm 1 / Eulerian numbers)."""
import json
from collections import Counter

import numpy as np

N = 52
data = json.load(open("data.json"))
P4 = np.array(data["shuffled"][3]["pmf"][1:])
U = np.array(data["uniform"]["pmf"][1:])


def riffle(deck, rng):
    c = int(rng.binomial(N, 0.5))
    top_slots = np.sort(rng.choice(N, c, replace=False))
    mask = np.zeros(N, bool)
    mask[top_slots] = True
    new = np.empty(N, int)
    new[mask] = deck[:c]
    new[~mask] = deck[c:]
    return new


def rising(deck):
    pos = np.empty(N + 1, int)
    pos[deck] = np.arange(N)
    return 1 + int(np.sum(pos[2:] < pos[1:-1]))


def sample(seed):
    rng = np.random.default_rng(seed)
    r4, ru = [14], [26]
    for _ in range(39):
        d = np.arange(1, N + 1)
        for _ in range(4):
            d = riffle(d, rng)
        r4.append(rising(d))
        ru.append(rising(rng.permutation(np.arange(1, N + 1))))
    return r4, ru


best = None
for seed in range(1, 400):
    r4, ru = sample(seed)
    c4, cu = Counter(r4), Counter(ru)
    if max(c4.values()) > 15 or max(cu.values()) > 7:
        continue
    # closeness of the 40-deck histograms to the exact pmfs (L1 distance)
    e4 = sum(abs(c4.get(r, 0) / 40 - P4[r - 1]) for r in range(1, N + 1))
    eu = sum(abs(cu.get(r, 0) / 40 - U[r - 1]) for r in range(1, N + 1))
    if best is None or e4 + eu < best[0]:
        best = (e4 + eu, seed, r4, ru)
_, seed, r4, ru = best
print("seed", seed, "riffled", sorted(Counter(r4).items()), "perfect", sorted(Counter(ru).items()))
json.dump({"seed": seed, "riffled4": r4, "perfect": ru}, open("pile.json", "w"))
