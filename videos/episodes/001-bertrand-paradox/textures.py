"""Chord-density textures for episode 1: each recipe's chords rasterised into RGBA stages.

Lines are accumulated as hit counts (0.5 px sampling, light blur), so overlapping chords
add up the way ink would; gold = long chords, grey = short.  stage k shows the first
n_k chords with an exposure that follows n so the picture converges like the tally does.
"""
from __future__ import annotations

import numpy as np

GOLD = np.array([0xF5, 0xC4, 0x51], float) / 255
SHORT = np.array([0x9A, 0xA3, 0xAE], float) / 255
MARGIN = 1.03                     # image spans [-MARGIN, MARGIN] in circle units


def _hist(p, q, size):
    """Accumulated line counts on a size x size grid (each line ~1 per pixel crossed)."""
    scale = size / (2 * MARGIN)
    a = (p + MARGIN) * scale
    b = (q + MARGIN) * scale
    L = np.hypot(*(b - a).T)
    k = np.maximum(2, np.ceil(L * 2).astype(int))          # 0.5 px spacing
    idx = np.repeat(np.arange(len(p)), k)
    t = (np.arange(k.sum()) - np.repeat(np.cumsum(k) - k, k)) / np.repeat(k - 1, k)
    pts = a[idx] + (b - a)[idx] * t[:, None]
    h, _, _ = np.histogram2d(pts[:, 1], pts[:, 0], bins=size, range=[[0, size], [0, size]])
    return h * 0.5                                            # 2 samples per px of length


def _blur(h):
    k = np.array([0.25, 0.5, 0.25])
    h = np.apply_along_axis(lambda r: np.convolve(r, k, mode="same"), 0, h)
    return np.apply_along_axis(lambda r: np.convolve(r, k, mode="same"), 1, h)


def stages(p, q, is_long, ns, size, gain=1.0):
    """RGBA uint8 arrays (flipped so +y is up) for cumulative chord counts ns."""
    out = []
    hg = np.zeros((size, size))
    hs = np.zeros((size, size))
    prev = 0
    disk_px = np.pi * (size / (2 * MARGIN)) ** 2
    total_len = 0.0
    for n in ns:
        sl = slice(prev, n)
        lg = is_long[sl]
        if lg.any():
            hg += _blur(_hist(p[sl][lg], q[sl][lg], size))
        if (~lg).any():
            hs += _blur(_hist(p[sl][~lg], q[sl][~lg], size))
        total_len += np.hypot(*(q[sl] - p[sl]).T).sum() * size / (2 * MARGIN)
        prev = n
        cbar = total_len / disk_px                    # mean lines per pixel inside the disk
        # exposure: one line on its own reads clearly; the full set averages ~45 % alpha
        expo = gain * min(1.3, 0.8 / max(cbar, 1e-9))
        ag = 1 - np.exp(-hg * expo)
        as_ = 0.5 * (1 - np.exp(-hs * expo))
        a = ag + as_ * (1 - ag)
        rgb = (GOLD[None, None] * ag[..., None] + SHORT[None, None] * (as_ * (1 - ag))[..., None])
        rgb = rgb / np.maximum(a, 1e-6)[..., None]
        img = np.dstack([rgb, a])
        out.append((np.clip(img, 0, 1) * 255).astype(np.uint8)[::-1])
    return out


def stage_counts(n_total=10_000, first=8, count=46):
    """Geometric schedule of cumulative chord counts after the first hand-drawn chords."""
    g = np.unique(np.round(np.geomspace(first + 1, n_total, count)).astype(int))
    return list(g)
