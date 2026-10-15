"""Builds data.json for episode 81 (run once; scene.py only reads data.json).

English: NLTK's copy of the Brown Corpus (Francis & Kucera 1961/1967), tokens lower-cased,
pure-punctuation tokens dropped.  Monkey: simulated random typing, seed 7, 26 equally likely
letters, space bar ends a word with probability 1/5 after each letter (no empty words),
as many words as the Brown Corpus.

    python make_data.py /path/to/nltk_data/corpora/brown
"""
import collections, json, os, re, sys
import numpy as np

d = sys.argv[1]
c = collections.Counter()
for f in sorted(os.listdir(d)):
    if not re.match(r"c[a-r]\d\d$", f):
        continue
    for tok in open(os.path.join(d, f)).read().split():
        w = tok.rsplit("/", 1)[0]
        if re.search(r"[A-Za-z0-9]", w):
            c[w.lower()] += 1
eng = c.most_common()
N = sum(k for _, k in eng)
fe = np.array([k for _, k in eng])

rng = np.random.default_rng(7)
q = 0.2
L = rng.geometric(q, size=N)
letters = rng.integers(0, 26, size=int(L.sum()))
s = "".join(chr(97 + i) for i in letters)
m = collections.Counter()
p = 0
for l in L:
    m[s[p:p + l]] += 1
    p += l
mon = m.most_common()
fm = np.array([k for _, k in mon])
stream = " ".join(s[sum(L[:i]):sum(L[:i]) + L[i]] for i in range(60))


def sample(f, rmax, extra=()):
    rmax = min(rmax, len(f))
    rs = set(np.unique(np.round(np.logspace(0, np.log10(rmax), 700)).astype(int)))
    rs |= set(range(1, 40)) | {r for r in extra if r <= rmax} | {rmax}
    rs = sorted(rs)
    return [[int(r), int(f[r - 1])] for r in rs]


def fit(f, lo, hi):
    r = np.arange(lo, hi + 1)
    return [float(v) for v in np.polyfit(np.log10(r), np.log10(f[lo - 1:hi]), 1)]


out = dict(
    N=int(N), types=len(eng), top=[[w, int(k)] for w, k in eng[:12]],
    eng=sample(fe, 100000), mon=sample(fm, 100000, extra=(26, 27, 702, 703, 18278, 18279)),
    mon_types=len(mon), mon_top=[[w, int(k)] for w, k in mon[:30]],
    fit_eng=fit(fe, 1, 1000), fit_mon=fit(fm, 1, 1000), stream=stream,
    eng_hapax=int((fe == 1).sum()),
)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json"), "w"))
print({k: v for k, v in out.items() if k not in ("eng", "mon", "mon_top")})
print(out["mon_top"][:3], out["mon_top"][25:28])
