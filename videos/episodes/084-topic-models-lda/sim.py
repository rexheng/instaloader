"""Toy corpus for episode 84 (all data SIMULATED, labelled so on screen).

Six "speeches", eight words each, vocabulary of six words.  Ground-truth theme of a token
is fixed by the word (money words vs war words).  We:
  1. cluster whole speeches with k-means (k=2) on word counts  -> one label per speech;
  2. run collapsed Gibbs sampling for LDA (K=2) -> one label per word.
Writes sim.json, which scene.py reads.  Run:  python sim.py
"""
import json
from pathlib import Path

import numpy as np
from sklearn.cluster import KMeans

VOCAB = ["tax", "budget", "deficit", "troops", "war", "army"]
THEME = [0, 0, 0, 1, 1, 1]              # 0 = money words, 1 = war words
COUNTS = np.array([
    [3, 3, 2, 0, 0, 0],                 # speech 1
    [2, 3, 3, 0, 0, 0],                 # speech 2
    [0, 0, 0, 3, 3, 2],                 # speech 3
    [0, 0, 0, 2, 3, 3],                 # speech 4
    [1, 2, 1, 1, 2, 1],                 # speech 5: half and half
    [1, 1, 1, 2, 2, 1],                 # speech 6: 3 money, 5 war
])
ALPHA, BETA, K, SWEEPS = 0.5, 0.1, 2, 20


def tokens():
    d_of, w_of = [], []
    for d, row in enumerate(COUNTS):
        for w, c in enumerate(row):
            d_of += [d] * c
            w_of += [w] * c
    return np.array(d_of), np.array(w_of)


def kmeans_labels():
    km = KMeans(n_clusters=2, n_init=20, random_state=0).fit(COUNTS)
    lab = km.labels_.copy()
    if lab[0] != 0:                      # name cluster 0 the one holding speech 1 (money)
        lab = 1 - lab
    return lab


def gibbs(seed):
    rng = np.random.default_rng(seed)
    D, W = tokens()
    n = len(D)
    z = rng.integers(0, K, n)
    ndk = np.zeros((len(COUNTS), K)); nkw = np.zeros((K, len(VOCAB))); nk = np.zeros(K)
    for i in range(n):
        ndk[D[i], z[i]] += 1; nkw[z[i], W[i]] += 1; nk[z[i]] += 1
    states = [z.copy()]
    # probe: the conditional for the first "war" token of speech 5, at the random start
    i = int(np.where((D == 4) & (W == VOCAB.index("war")))[0][0])
    d, w, k = D[i], W[i], z[i]
    a = ndk[d].copy(); a[k] -= 1
    b = nkw[:, w].copy(); b[k] -= 1
    c = nk.copy(); c[k] -= 1
    p = (a + ALPHA) * (b + BETA) / (c + len(VOCAB) * BETA)
    probe = dict(i=i, ndk=a.tolist(), nkw=b.tolist(), nk=c.tolist(), p=(p / p.sum()).tolist(),
                 z_before=int(k), others_in_doc=int(a.sum()))
    for s in range(SWEEPS):
        for i in range(n):
            d, w, k = D[i], W[i], z[i]
            ndk[d, k] -= 1; nkw[k, w] -= 1; nk[k] -= 1
            p = (ndk[d] + ALPHA) * (nkw[:, w] + BETA) / (nk + len(VOCAB) * BETA)
            k = rng.choice(K, p=p / p.sum())
            z[i] = k
            ndk[d, k] += 1; nkw[k, w] += 1; nk[k] += 1
        states.append(z.copy())
    return D, W, states, probe


def main():
    D, W, _, _ = gibbs(0)
    truth = np.array([THEME[w] for w in W])
    lab = kmeans_labels()
    km_wrong = int(np.sum(lab[D] != truth))
    best = None
    for seed in range(200):
        _, _, states, probe = gibbs(seed)
        fin = states[-1]
        # topic naming: topic that holds most money tokens is "blue" (0)
        flip = np.mean(fin[truth == 0] == 0) < 0.5
        st = [(1 - s) if flip else s for s in states]
        wrong = [int(np.sum(s != truth)) for s in st]
        # want: a messy start (~half wrong), monotone-ish settling, exact at the end
        if wrong[-1] == 0 and wrong[0] >= 20 and all(w == 0 for w in wrong[-6:]):
            score = sum(1 for a, b in zip(wrong, wrong[1:]) if b > a)
            pp = probe["p"][::-1] if flip else probe["p"]
            zb = (1 - probe["z_before"]) if flip else probe["z_before"]
            nice = 0 if (zb == 0 and 0.6 < pp[1] < 0.75) else 1   # blue now, leaning purple
            cand = (score + nice, -wrong[0], seed)
            if best is None or cand < best[0]:
                best = (cand, seed, st, wrong, probe, flip)
    _, seed, st, wrong, probe, flip = best
    if flip:   # express the probe in display colours (0 = blue, 1 = purple)
        for key in ("ndk", "nkw", "nk", "p"):
            probe[key] = probe[key][::-1]
        probe["z_before"] = 1 - probe["z_before"]
    fin = st[-1]
    theta = [[float((np.sum(fin[D == d] == k) + 0) / np.sum(D == d)) for k in range(K)]
             for d in range(len(COUNTS))]
    out = dict(vocab=VOCAB, theme=THEME, counts=COUNTS.tolist(), alpha=ALPHA, beta=BETA,
               kmeans_labels=lab.tolist(), kmeans_wrong=km_wrong, n_tokens=int(len(D)),
               seed=seed, D=D.tolist(), W=W.tolist(), states=[s.tolist() for s in st],
               wrong=wrong, probe=probe, theta_final=theta)
    Path(__file__).with_name("sim.json").write_text(json.dumps(out))
    print("kmeans labels", lab.tolist(), "wrong", km_wrong, "/", len(D))
    print("seed", seed, "wrong per sweep", wrong)
    print("probe", probe)
    print("theta final", theta)


if __name__ == "__main__":
    main()
