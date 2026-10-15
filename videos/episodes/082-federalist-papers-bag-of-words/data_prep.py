"""Recompute every number in episode 82 from the Project Gutenberg text of The Federalist.

    curl -sSL -o /tmp/fed.txt https://www.gutenberg.org/cache/epub/18/pg18.txt
    python data_prep.py /tmp/fed.txt          # writes data.json next to this file

Attribution follows the standard (Adair 1944 / Mosteller & Wallace) split:
Hamilton 51 known, Madison 14 known, disputed 49-58, 62, 63 (Gutenberg labels 58
"MADISON"; we treat it as disputed). Rates = uses per 1,000 tokens ([a-z]+ after
lower-casing, body text after "To the People of the State of New York:", up to PUBLIUS).
Poisson model: lambda = pooled author rate x essay length (no smoothing).
"""
import json, re, sys
from math import exp, factorial, log
from pathlib import Path

t = open(sys.argv[1], encoding="utf-8").read()
t = t[:t.find("*** END OF")]
parts = re.split(r"\n(?:THE FEDERALIST\.\n)?No\. ([IVXLC]+)\.\n", t)


def rom(s):
    v = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
    return sum(-v[c] if i + 1 < len(s) and v[s[i + 1]] > v[c] else v[c] for i, c in enumerate(s))


papers = {}
for i in range(1, len(parts), 2):
    n, body = rom(parts[i]), parts[i + 1]
    if n in papers:
        continue                                   # Gutenberg prints No. 70 twice
    m = re.search(r"\n(HAMILTON|MADISON|JAY|HAMILTON OR MADISON|HAMILTON AND MADISON)\s*\n", body)
    k = body.find("To the People of the State of New York")
    txt = body[k + 39:] if k >= 0 else body
    p = txt.rfind("PUBLIUS")
    papers[n] = (m.group(1) if m else "?", txt[:p] if p > 0 else txt)

D = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63]
H = sorted(n for n, (a, _) in papers.items() if a == "HAMILTON")
M = sorted(n for n, (a, _) in papers.items() if a == "MADISON" and n not in D)
assert len(H) == 51 and len(M) == 14
tok = {n: re.findall(r"[a-z]+", papers[n][1].lower()) for n in papers}
rate = lambda n, w: 1000 * tok[n].count(w) / len(tok[n])
pooled = lambda ns, w: sum(tok[n].count(w) for n in ns) / sum(len(tok[n]) for n in ns)
WORDS = ["upon", "by", "on", "to", "there"]


def log10_odds(n, Hs, Ms):                         # log10 P(counts | Madison) / P(counts | Hamilton)
    L, out = len(tok[n]), {}
    for w in WORDS:
        k, lh, lm = tok[n].count(w), pooled(Hs, w) * L, pooled(Ms, w) * L
        out[w] = (-lm + k * log(lm) + lh - k * log(lh)) / log(10)
    return out


def best_cut(w):                                   # rule: rate > cut -> Hamilton
    h, m = [rate(n, w) for n in H], [rate(n, w) for n in M]
    cuts = sorted(set(h + m + [-1.0]))
    return min((sum(x <= c for x in h) + sum(x > c for x in m), c) for c in cuts)


loo_wrong = [n for n in H + M
             if (sum(log10_odds(n, [x for x in H if x != n], [x for x in M if x != n]).values()) > 0) != (n in M)]
L54 = len(tok[54])
lh, lm = pooled(H, "upon") * L54, pooled(M, "upon") * L54
pois = lambda k, l: exp(-l) * l ** k / factorial(k)
out = {
    "H": {n: {w: rate(n, w) for w in ("war", "liberty", "upon")} for n in H},
    "M": {n: {w: rate(n, w) for w in ("war", "liberty", "upon")} for n in M},
    "D": {n: {w: rate(n, w) for w in ("war", "liberty", "upon")} for n in D},
    "best_cut": {w: best_cut(w) for w in ("war", "liberty", "upon")},
    "pooled_upon": {"H": 1000 * pooled(H, "upon"), "M": 1000 * pooled(M, "upon")},
    "len54": L54, "lam54": {"H": lh, "M": lm},
    "pmf54": {"H": [pois(k, lh) for k in range(13)], "M": [pois(k, lm) for k in range(13)]},
    "odds54_words": log10_odds(54, H, M),
    "log10_odds": {n: sum(log10_odds(n, H, M).values()) for n in D},
    "loo_wrong": loo_wrong,
    "war_counts": {n: tok[n].count("war") for n in (8, 78, 79, 80, 81, 82, 83)},
    "upon_counts_D": {n: tok[n].count("upon") for n in D},
    "len51": len(tok[51]),
}
Path(__file__).with_name("data.json").write_text(json.dumps(out, indent=1))
print(json.dumps({k: out[k] for k in ("best_cut", "pooled_upon", "lam54", "odds54_words",
                                      "log10_odds", "loo_wrong", "war_counts", "upon_counts_D")}, indent=1))
print("P(2|H)", out["pmf54"]["H"][2], "P(2|M)", out["pmf54"]["M"][2])
