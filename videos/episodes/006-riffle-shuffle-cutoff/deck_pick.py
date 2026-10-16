"""Pick the on-screen example decks (seeded, reproducible). Writes decks.json.

Forward GSR riffles: cut ~ Binomial(52, 1/2); every interleaving of the two packets that keeps
each packet's order is equally likely (equivalent to dropping cards with probability
proportional to packet size).  Deck lists card numbers 1..52 from top (left) to bottom."""
import json
import numpy as np

N = 52


def riffle(deck, rng):
    c = int(rng.binomial(N, 0.5))
    top_slots = np.sort(rng.choice(N, c, replace=False))
    mask = np.zeros(N, bool)
    mask[top_slots] = True
    new = np.empty(N, int)
    new[mask] = deck[:c]
    new[~mask] = deck[c:]
    return new, c, mask


def rising(deck):
    pos = np.empty(N + 1, int)
    pos[deck] = np.arange(N)
    return 1 + int(np.sum(pos[2:] < pos[1:-1]))


def runs(deck):
    """List of rising sequences, each a list of card numbers."""
    pos = np.empty(N + 1, int)
    pos[deck] = np.arange(N)
    out, cur = [], [1]
    for x in range(2, N + 1):
        if pos[x] > pos[x - 1]:
            cur.append(x)
        else:
            out.append(cur)
            cur = [x]
    out.append(cur)
    return out


want = [2, 4, 8, 14]
for seed in range(20000):
    rng = np.random.default_rng(seed)
    deck = np.arange(1, N + 1)
    hist, cuts, masks, Rs = [deck.tolist()], [], [], []
    ok = True
    for k in range(10):
        deck, c, m = riffle(deck, rng)
        hist.append(deck.tolist()); cuts.append(c); masks.append(m.tolist()); Rs.append(rising(deck))
        if k < 4 and Rs[-1] != want[k]:
            ok = False
            break
    if not ok:
        continue
    if not (cuts[0] in (25, 26, 27) and 19 <= Rs[4] <= 21 and 22 <= Rs[5] <= 24 and 24 <= Rs[6] <= 26 and Rs[9] >= 25):
        continue
    if hist[4][0] == 1:            # avoid the old top card on top (keeps the top-card beat clean)
        continue
    print("seed", seed, "cuts", cuts, "R", Rs)
    break

rng2 = np.random.default_rng(12345)
for t in range(1000):
    rnd = rng2.permutation(np.arange(1, N + 1))
    if rising(rnd) == 26:
        break
print("random deck R", rising(rnd))

# a second, different 4-riffle GSR deck with the same count (14): the theorem beat shows that
# it has exactly the same chance, C(16 + 52 - 14, 52) / 16^52 = 1431 / 2^208 = 3.5e-60
for seed2 in range(1, 20000):
    rng3 = np.random.default_rng(10_000 + seed2)
    d2 = np.arange(1, N + 1)
    for _ in range(4):
        d2, _, _ = riffle(d2, rng3)
    if rising(d2) == 14 and d2.tolist() != hist[4] and d2[0] != 1:
        break
print("alt 14-sequence deck from seed", 10_000 + seed2)
json.dump({"seed": seed, "decks": hist, "cuts": cuts, "masks": masks, "R": Rs,
           "runs": [runs(np.array(h)) for h in hist],
           "random": rnd.tolist(), "random_runs": runs(rnd),
           "alt14": d2.tolist(), "alt14_runs": runs(d2), "alt14_seed": 10_000 + seed2},
          open("decks.json", "w"))
