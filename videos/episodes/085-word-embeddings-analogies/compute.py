"""Reproduce every number in episode 85 from the word2vec GoogleNews vectors.

Inputs (not committed, 360 MB): the first 300,000 rows (frequency-sorted) of
GoogleNews-vectors-negative300.bin, saved as vecs300k.npy / words300k.txt, and
questions-words.txt (the Google analogy test set, github.com/tmikolov/word2vec).
    python compute.py <dir with those files>
Writes data.json next to this file (the only data scene.py reads)."""
import json, sys, collections
from pathlib import Path
import numpy as np

d = sys.argv[1]
V = np.load(d + "/vecs300k.npy"); W = open(d + "/words300k.txt").read().split("\n")
V /= np.linalg.norm(V, axis=1, keepdims=True)
idx = {}
for i, w in enumerate(W):
    idx.setdefault(w, i)
v = lambda w: V[idx[w]]
out = {}

def rank(a, b, c, k=6):
    """b - a + c, cosine with every word, no exclusion."""
    r = v(b) - v(a) + v(c)
    s = V @ r / np.linalg.norm(r)
    top = np.argsort(-s)[:k]
    return [[W[i], round(float(s[i]), 4)] for i in top]

out["king_rank"] = rank("man", "king", "woman")
out["doctor_rank"] = rank("man", "doctor", "woman")
out["programmer_rank"] = rank("man", "computer_programmer", "woman")
r = v("king") - v("man") + v("woman")
out["sum_norm"] = float(np.linalg.norm(r))
out["terms"] = {x: [float(v(x) @ v("king")), float(v(x) @ v("man")), float(v(x) @ v("woman"))]
                for x in ("king", "queen")}
# exact plane through king and the step (woman - man)
e1 = v("king"); step = v("woman") - v("man")
along = float(step @ e1); perp = float(np.linalg.norm(step - along * e1))
out["plane"] = {"step_along_king": along, "step_perp": perp, "step_len": float(np.linalg.norm(step))}
out["strips"] = {w: [round(float(x), 4) for x in v(w)] for w in ("king", "queen")}

# Google analogy test: "a b c d" means d = b - a + c  (c = the start word, like king)
qs = []
for line in open(d + "/questions-words.txt"):
    if line.startswith(":"):
        continue
    a, b, c, e = line.split()
    if all(w in idx for w in (a, b, c, e)):
        qs.append((idx[a], idx[b], idx[c], idx[e]))
qs = np.array(qs)
ok_rule = 0; no_rule = collections.Counter()
for s0 in range(0, len(qs), 512):
    Q = qs[s0:s0 + 512]
    R = V[Q[:, 1]] - V[Q[:, 0]] + V[Q[:, 2]]
    S = R @ V.T
    t = S.argmax(1)
    for j, (a, b, c, e) in enumerate(Q):
        no_rule["correct" if t[j] == e else "start" if t[j] == c else "other"] += 1
        S[j, [a, b, c]] = -np.inf
    ok_rule += int((S.argmax(1) == Q[:, 3]).sum())
n = len(qs)
out["test"] = {"n_total": 19544, "n_used": n, "rule_correct": ok_rule / n,
               **{f"norule_{k}": no_rule[k] / n for k in ("correct", "start", "other")}}
Path(__file__).with_name("data.json").write_text(json.dumps(out))
print(json.dumps({k: v for k, v in out.items() if k != "strips"}, indent=1))
