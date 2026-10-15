"""Simulated data for episode 47 (all images and numbers on screen come from here).

    python sim.py            -> writes sim.npz and prints every number used in the script

Toy 'photos': 40x40 grayscale.  Horses and cars are rasterised silhouettes with random
position, size, brightness, background texture and pixel noise.  Source A (the training
archive) stamps a small tag in the bottom-left corner of EVERY horse photo.  Source B
(new photos) has no tags.  Classifier: L2 logistic regression on raw pixels.
"""
import numpy as np
from matplotlib.path import Path

N = 40
JIT, LIGHT, NOISE, NTR = 12, 0, 0.1, 1000
TAG = (slice(33, 37), slice(2, 9))        # rows, cols: 4 x 7 = 28 pixels (1.75 % of 1600)
yy, xx = np.mgrid[0:N, 0:N] + 0.5
PTS = np.c_[xx.ravel(), yy.ravel()]


def poly(vertices, ox, oy, s):
    v = np.array(vertices, float) * s + [ox, oy]
    return Path(v).contains_points(PTS).reshape(N, N)


def ellipse(cx, cy, rx, ry):
    return ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1


# shapes in a unit box ~ [-1, 1], y grows downward (image rows)
HORSE = [(-0.85, -0.05), (-0.6, -0.25), (0.35, -0.25), (0.55, -0.75), (0.7, -0.95),
         (0.95, -0.85), (0.98, -0.7), (0.75, -0.55), (0.62, -0.05), (0.6, 0.15),
         (0.52, 0.15), (0.5, 0.75), (0.4, 0.75), (0.38, 0.2), (-0.45, 0.2), (-0.5, 0.75),
         (-0.6, 0.75), (-0.62, 0.15), (-0.75, 0.15), (-0.95, 0.35), (-1.0, 0.25),
         (-0.85, 0.0)]


def horse(rng):
    s = rng.uniform(9, 12)
    ox, oy = rng.uniform(20 - JIT, 20 + JIT), rng.uniform(19 - JIT / 2, 19 + JIT / 2)
    flip = False
    v = [(-x if flip else x, y) for x, y in HORSE]
    return poly(v, ox, oy, s)


def car(rng):
    s = rng.uniform(9, 12)
    ox, oy = rng.uniform(20 - JIT, 20 + JIT), rng.uniform(21 - JIT / 2, 21 + JIT / 2)
    body = poly([(-1, -0.15), (1, -0.15), (1, 0.35), (-1, 0.35)], ox, oy, s)
    cab = poly([(-0.55, -0.15), (-0.3, -0.6), (0.35, -0.6), (0.6, -0.15)], ox, oy, s)
    w1 = ellipse(ox - 0.55 * s, oy + 0.38 * s, 0.22 * s, 0.22 * s)
    w2 = ellipse(ox + 0.55 * s, oy + 0.38 * s, 0.22 * s, 0.22 * s)
    return body | cab | w1 | w2


def tag_pattern():
    t = np.zeros((4, 7))
    t[:, :] = 0.95
    t[1:3, 1] = 0.25            # a tiny 'c' and bar: reads as a stamp, not as a shape
    t[1, 2] = t[2, 2] = 0.95
    t[1:3, 3:6] = 0.3
    return t


TAG_PIX = tag_pattern()


def photo(rng, kind, tagged):
    horizon = rng.uniform(14, 24)
    sky = rng.uniform(0.6, 0.8)
    ground = rng.uniform(0.4, 0.6)
    img = np.where(yy < horizon, sky, ground) + rng.normal(0, NOISE, (N, N))
    img += 0.08 * np.sin(xx / rng.uniform(2, 5) + rng.uniform(0, 6)) * (yy > horizon)
    mask = horse(rng) if kind == 1 else car(rng)
    tone = rng.uniform(0.02, 0.15) if rng.random() > LIGHT else rng.uniform(0.85, 1.0)
    img = np.where(mask, tone + rng.normal(0, 0.03, (N, N)), img)
    if tagged:
        img[TAG] = TAG_PIX
    return np.clip(img, 0, 1)


def dataset(rng, n, tag_rule):
    X, y, tagged = [], [], []
    for i in range(n):
        k = i % 2                               # 1 = horse, 0 = car
        t = tag_rule(rng, k)
        X.append(photo(rng, k, t).ravel()); y.append(k); tagged.append(t)
    return np.array(X), np.array(y), np.array(tagged)


def fit_logreg(X, y, lam=1e-3, steps=3000, lr=0.5):
    w = np.zeros(X.shape[1]); b = 0.0
    for _ in range(steps):
        p = 1 / (1 + np.exp(-(X @ w + b)))
        g = p - y
        w -= lr * (X.T @ g / len(y) + lam * w)
        b -= lr * g.mean()
    return w, b


def main():
    rng = np.random.default_rng(47)
    source_a = lambda r, k: k == 1                  # every horse photo is stamped
    no_tag = lambda r, k: False
    fixed = lambda r, k: r.random() < 0.5           # stamp half of ALL photos at random
    Xtr, ytr, _ = dataset(rng, NTR, source_a)
    Xnew, ynew, _ = dataset(rng, 1000, no_tag)
    Xte, yte, _ = dataset(rng, 1000, source_a)
    w, b = fit_logreg(Xtr, ytr)
    acc = lambda w, b, X, y: ((X @ w + b > 0) == y).mean()
    sig = lambda z: 1 / (1 + np.exp(-z))
    out = {}
    out["v1_test"] = acc(w, b, Xte, yte)
    out["v1_new"] = acc(w, b, Xnew, ynew)
    out["v1_new_horses"] = acc(w, b, Xnew[ynew == 1], ynew[ynew == 1])
    out["v1_new_cars"] = acc(w, b, Xnew[ynew == 0], ynew[ynew == 0])
    xbar = Xtr.mean(0)
    tm = np.zeros((N, N), bool); tm[TAG] = True; tm = tm.ravel()
    sh = [(w * (x - xbar))[tm].sum() / (w * (x - xbar)).sum() for x in Xte[yte == 1]]
    out["tag_share_median"] = float(np.median(sh))
    # heroes: a tagged horse that flips to car without its tag; a car that flips to horse
    hero = None
    for seed in range(400):
        h = photo(np.random.default_rng(seed), 1, True).ravel()
        h0 = photo(np.random.default_rng(seed), 1, False).ravel()
        R = w * (h - xbar)
        if sig(h @ w + b) > 0.97 and sig(h0 @ w + b) < 0.1 and abs(R[tm].sum() / R.sum() - out["tag_share_median"]) < 0.03:
            hero = seed; break
    for seed in range(1000, 1400):
        c = photo(np.random.default_rng(seed), 0, False).ravel()
        ct = photo(np.random.default_rng(seed), 0, True).ravel()
        if sig(c @ w + b) < 0.03 and sig(ct @ w + b) > 0.9:
            carseed = seed; break
    h = photo(np.random.default_rng(hero), 1, True).ravel()
    h0 = photo(np.random.default_rng(hero), 1, False).ravel()
    c = photo(np.random.default_rng(carseed), 0, False).ravel()
    ct = photo(np.random.default_rng(carseed), 0, True).ravel()
    R = w * (h - xbar)
    out.update(hero=hero, car=carseed, p_h=sig(h @ w + b), p_h0=sig(h0 @ w + b),
               p_c=sig(c @ w + b), p_ct=sig(ct @ w + b), s_h=h @ w + b, s_bar=xbar @ w + b,
               R_tag=R[tm].sum(), R_rest=R[~tm].sum(), R_total=R.sum(),
               hero_share=R[tm].sum() / R.sum())
    # v2: tag stamped on half of all photos at random
    Xtr2, ytr2, _ = dataset(np.random.default_rng(5), NTR, fixed)
    w2, b2 = fit_logreg(Xtr2, ytr2)
    Xte2, yte2, _ = dataset(np.random.default_rng(6), 1000, fixed)
    xbar2 = Xtr2.mean(0)
    R2 = w2 * (h - xbar2)
    out.update(v2_test=acc(w2, b2, Xte2, yte2), v2_test_archive=acc(w2, b2, Xte, yte), v2_new=acc(w2, b2, Xnew, ynew),
               v2_hero_share=R2[tm].sum() / R2.sum(), v2_p_h0=sig(h0 @ w2 + b2),
               v2_p_ct=sig(ct @ w2 + b2), v2_p_h=sig(h @ w2 + b2))
    wscr = np.random.default_rng(99).permutation(w)      # sanity check: scrambled weights
    Rscr = wscr * (h - xbar)
    for k, v in out.items():
        print(f"{k:18s} {v}")
    gal = np.r_[Xte[yte == 1][:6], Xte[yte == 0][:6]]
    newg = np.r_[Xnew[ynew == 1][:6], Xnew[ynew == 0][:6]]
    np.savez_compressed(__file__.replace("sim.py", "sim.npz"), w=w, b=b, w2=w2, b2=b2,
                        xbar=xbar, xbar2=xbar2, h=h, h0=h0, c=c, ct=ct, R=R, R2=R2, Rscr=Rscr,
                        gal=gal, gal_pred=(gal @ w + b > 0), newg=newg,
                        new_pred=(newg @ w + b > 0), new_pred2=(newg @ w2 + b2 > 0),
                        **{k: np.array(v) for k, v in out.items()})


if __name__ == "__main__":
    main()
