"""Every number shown or spoken in episode 7, recomputed from the raw sources.

    python3 data.py /path/to/brown        # writes data.json next to this file

Brown corpus (Francis & Kucera 1964; NLTK distribution, 500 tagged files ca01..cr09):
https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/brown.zip
Text is reduced to Shannon's 27-symbol alphabet: each token's letters are kept (A-Z,
upper-cased), punctuation-only tokens are dropped, and tokens are joined by one space.

Shannon (1951) guess record: Bell System Technical Journal 30(1), p. 56, display (9).
"""
from __future__ import annotations

import collections
import heapq
import json
import math
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SYM = [chr(65 + i) for i in range(26)] + [" "]

# Shannon 1951, p. 56: the passage and the number of guesses each symbol took.
RECORD_TEXT = ["THERE IS NO REVERSE ON A MOTORCYCLE A ",
               "FRIEND OF MINE FOUND THIS OUT ",
               "RATHER DRAMATICALLY THE OTHER DAY "]
RECORD_GUESSES = [
    [1, 1, 1, 5, 1, 1, 2, 1, 1, 2, 1, 1, 15, 1, 17, 1, 1, 1, 2, 1, 3, 2, 1, 2, 2, 7, 1, 1, 1, 1,
     4, 1, 1, 1, 1, 1, 3, 1],
    [8, 6, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [4, 1, 1, 1, 1, 1, 1, 11, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1],
]
# Shannon 1951, p. 64: experimental bounds (bits/letter) for N = 100 letters of context
SHANNON_BOUNDS_N100 = (0.6, 1.3)
# "The fractions add up": a real run from the record (THERE -> E R E space, after T H),
# each character priced by the two-letter-context table
RUN_CONTEXT, RUN_TEXT = "TH", "ERE "


def load_brown(d: str) -> str:
    words = []
    for f in sorted(os.listdir(d)):
        if not re.fullmatch(r"c[a-r]\d\d", f):
            continue
        for tok in open(os.path.join(d, f), encoding="latin-1").read().split():
            w = re.sub(r"[^A-Za-z]", "", tok.rsplit("/", 1)[0]).upper()
            if w:
                words.append(w)
    return " ".join(words) + " "


def entropy(ps) -> float:
    return -sum(p * math.log2(p) for p in ps if p > 0)


def next_dist(text: str, ctx: str) -> tuple[int, dict]:
    nxt = collections.Counter(text[i + len(ctx)] for i in range(len(text) - len(ctx))
                              if text.startswith(ctx, i))
    n = sum(nxt.values())
    return n, {s: nxt[s] / n for s in SYM}


def cond_entropy(text: str, k: int) -> float:
    """H(next symbol | the k symbols before it), averaged over every k-symbol context
    (each context weighted by how often it occurs)."""
    joint = collections.Counter(text[i:i + k + 1] for i in range(len(text) - k))
    ctx = collections.Counter()
    for g, c in joint.items():
        ctx[g[:k]] += c
    n = sum(joint.values())
    return -sum(c / n * math.log2(c / ctx[g[:k]]) for g, c in joint.items())


def huffman_depths(p: dict) -> dict:
    h = [(v, i, (s,)) for i, (s, v) in enumerate(p.items())]
    heapq.heapify(h)
    depth = {s: 0 for s in p}
    k = len(h)
    while len(h) > 1:
        a, b = heapq.heappop(h), heapq.heappop(h)
        for s in a[2] + b[2]:
            depth[s] += 1
        heapq.heappush(h, (a[0] + b[0], k, a[2] + b[2]))
        k += 1
    return depth


def main(brown_dir: str):
    text = load_brown(brown_dir)
    n = len(text)
    cnt = collections.Counter(text)
    p = {s: cnt[s] / n for s in SYM}
    order = sorted(SYM, key=lambda s: -p[s])
    H1 = entropy(p.values())
    huff = huffman_depths(p)
    L_huff = sum(p[s] * huff[s] for s in SYM)

    # equal-split ("halve the alphabet") tree, alphabetical, larger half first
    eq_depth = {}

    def split(g, d):
        if len(g) == 1:
            eq_depth[g[0]] = d
            return
        k = (len(g) + 1) // 2
        split(g[:k], d + 1)
        split(g[k:], d + 1)
    split(SYM, 0)
    L_eq = sum(p[s] * eq_depth[s] for s in SYM)

    nQ, pQ = next_dist(text, "Q")
    nTH, pTH = next_dist(text, "TH")

    # the run E R E _ after TH: each character's ideal cost given the two before it
    run, ctx = [], RUN_CONTEXT
    for ch in RUN_TEXT:
        n_c, d_c = next_dist(text, ctx[-2:])
        run.append({"ch": ch, "context": ctx[-2:], "n": n_c, "p": d_c[ch],
                    "cost": -math.log2(d_c[ch])})
        ctx += ch
    run_total = sum(r["cost"] for r in run)

    # why counting stops at short contexts: possible contexts vs the corpus
    grams10 = collections.Counter(text[i:i + 10] for i in range(len(text) - 10))
    once10 = sum(1 for v in grams10.values() if v == 1)

    g = sum(RECORD_GUESSES, [])
    s = "".join(RECORD_TEXT)
    assert len(g) == len(s) == 102
    gc = collections.Counter(g)
    # Shannon's own tally (p. 56): 79 first, 8 second, 3 third, 2 fourth, 2 fifth, 8 more
    assert (gc[1], gc[2], gc[3], gc[4], gc[5], sum(v for k, v in gc.items() if k > 5)) == \
        (79, 8, 3, 2, 2, 8)

    out = {
        "brown": {"characters": n, "words": text.count(" ")},
        "p": p, "order": order,
        "H0_log2_27": math.log2(27), "H1": H1,
        "huffman_avg_len": L_huff, "equal_split_avg_len": L_eq,
        "E_over_Z": p["E"] / p["Z"], "one_in_Z": 1 / p["Z"],
        "log2_inv": {s: -math.log2(p[s]) for s in SYM},
        "top5_share": sum(p[x] for x in order[:5]),
        "after_Q": {"n": nQ, "p": pQ, "H": entropy(pQ.values())},
        "after_TH": {"n": nTH, "p": pTH, "H": entropy(pTH.values())},
        # averaged over ALL contexts (Q and TH above are best cases)
        "H_given_1_prev": cond_entropy(text, 1), "H_given_2_prev": cond_entropy(text, 2),
        "record": {"text": RECORD_TEXT, "guesses": RECORD_GUESSES, "first_try": gc[1],
                   "symbols": len(g), "total_guesses": sum(g)},
        "shannon_bounds_N100": SHANNON_BOUNDS_N100,
        "run_THERE": {"context": RUN_CONTEXT, "run": RUN_TEXT, "letters": run,
                      "total": run_total, "questions": math.ceil(run_total),
                      "one_at_a_time": sum(math.ceil(r["cost"]) for r in run)},
        "contexts": {"possible_2": 27 ** 2, "possible_100_log10": 100 * math.log10(27),
                     "brown_10grams_distinct": len(grams10), "brown_10grams_seen_once": once10},
    }
    (HERE / "data.json").write_text(json.dumps(out, indent=1))
    print(f"Brown: {n:,} characters, {out['brown']['words']:,} words")
    print(f"log2 27 = {math.log2(27):.4f}   H1 = {H1:.4f}   Huffman = {L_huff:.4f}   "
          f"equal split = {L_eq:.4f}")
    print("top-5:", order[:5], f"{out['top5_share']:.4f}")
    for x in ("E", " ", "Z"):
        print(f"  {x!r}: p = {p[x]:.5f}  log2(1/p) = {-math.log2(p[x]):.3f}")
    print(f"E/Z = {p['E'] / p['Z']:.1f}   Z = 1 in {1 / p['Z']:.0f}")
    print(f"after Q (n={nQ}): U = {pQ['U']:.4f}  H = {out['after_Q']['H']:.4f}")
    print(f"after TH (n={nTH}): E = {pTH['E']:.4f}  H = {out['after_TH']['H']:.4f}")
    print(f"averaged over all contexts: H(X|1 prev) = {out['H_given_1_prev']:.4f}   "
          f"H(X|2 prev) = {out['H_given_2_prev']:.4f}")
    print(f"record: {gc[1]}/{len(g)} first try, {sum(g)} guesses")
    print("run after TH:", [(r["ch"], r["context"], round(r["p"], 4), round(r["cost"], 3)) for r in run],
          f"total {run_total:.3f} -> {math.ceil(run_total)} questions")
    print(f"10-letter strings in Brown: {len(grams10):,} distinct, {once10 / len(grams10):.1%} seen once; "
          f"27^100 = 10^{100 * math.log10(27):.2f}")


if __name__ == "__main__":
    main(sys.argv[1])
