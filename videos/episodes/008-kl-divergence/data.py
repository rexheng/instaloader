"""Episode 8 data: every number shown or spoken, recomputed from the raw data.

    python3 videos/episodes/008-kl-divergence/data.py      # -> data.json

Data: R's `faithful` dataset (272 Old Faithful eruptions; column `eruptions` = length in
minutes), source W. Haerdle (1991), *Smoothing Techniques with Implementation in S*.
CSV copied from https://vincentarelbundock.github.io/Rdatasets/csv/datasets/faithful.csv.

"Smoothed data" P = maximum-likelihood mixture of two normals (EM).  At the MLE the
mixture has exactly the sample mean and (1/n) variance, so the data-first best bell
(moment matching) is the ordinary maximum-likelihood normal fit.
All divergences are in bits: D(W||V) = integral of w * log2(w / v) dx.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.special import logsumexp
from scipy.stats import norm

HERE = Path(__file__).resolve().parent
LN2 = np.log(2.0)

e = np.array([float(r["eruptions"]) for r in csv.DictReader(open(HERE / "faithful.csv"))])
n = len(e)

# ---------------------------------------------------------------- 2-normal mixture by EM
pi, mu, sd = np.array([.5, .5]), np.array([2.0, 4.3]), np.array([.3, .4])
for _ in range(20000):
    d = pi * norm.pdf(e[:, None], mu, sd)
    r = d / d.sum(1, keepdims=True)
    nk = r.sum(0)
    pi_new, mu_new = nk / n, (r * e[:, None]).sum(0) / nk
    sd_new = np.sqrt((r * (e[:, None] - mu_new) ** 2).sum(0) / nk)
    done = np.allclose([pi, mu, sd], [pi_new, mu_new, sd_new], atol=1e-13, rtol=0)
    pi, mu, sd = pi_new, mu_new, sd_new
    if done:
        break

X = np.linspace(-8, 15, 460001)
DX = X[1] - X[0]


def logp(x):
    x = np.asarray(x, float)
    return logsumexp(np.log(pi) + norm.logpdf(x[..., None], mu, sd), axis=-1)


LP = logp(X)


def kl_bits(lw, lv):
    w = np.exp(lw)
    return float(np.sum(w * (lw - lv)) * DX / LN2)


def fwd(m, s):                       # D(data || bell)
    return kl_bits(LP, norm.logpdf(X, m, s))


def rev(m, s):                       # D(bell || data)
    return kl_bits(norm.logpdf(X, m, s), LP)


mA, sA = float(e.mean()), float(e.std())          # MLE normal = data-first optimum
ra = minimize(lambda t: fwd(t[0], np.exp(t[1])), (3.0, 0.0), method="Nelder-Mead",
              options=dict(xatol=1e-9, fatol=1e-13, maxiter=20000))
rb = minimize(lambda t: rev(t[0], np.exp(t[1])), (4.3, np.log(.44)), method="Nelder-Mead",
              options=dict(xatol=1e-9, fatol=1e-13, maxiter=20000))
rc = minimize(lambda t: rev(t[0], np.exp(t[1])), (2.0, np.log(.24)), method="Nelder-Mead",
              options=dict(xatol=1e-9, fatol=1e-13, maxiter=20000))
mB, sB = float(rb.x[0]), float(np.exp(rb.x[1]))

# ---------------------------------------------------------------- descent path A -> B (bell first)
# plain gradient descent on (mu, log sigma), recorded for the animation
th = np.array([mA, np.log(sA)])
path = [(mA, sA, rev(mA, sA))]
step, h = 0.02, 1e-5
for it in range(20000):
    f0 = rev(th[0], np.exp(th[1]))
    g = np.array([(rev(th[0] + h, np.exp(th[1])) - rev(th[0] - h, np.exp(th[1]))) / (2 * h),
                  (rev(th[0], np.exp(th[1] + h)) - rev(th[0], np.exp(th[1] - h))) / (2 * h)])
    th = th - step * g
    path.append((float(th[0]), float(np.exp(th[1])), rev(th[0], np.exp(th[1]))))
    if np.linalg.norm(g) < 1e-6:
        break
path = np.array(path)
# resample by arc length in (mu, log sigma) so the animation moves at an even pace
seg = np.r_[0, np.cumsum(np.hypot(np.diff(path[:, 0]), np.diff(np.log(path[:, 1]))))]
u = np.linspace(0, seg[-1], 121)
path_rs = np.c_[np.interp(u, seg, path[:, 0]), np.interp(u, seg, path[:, 1])]
path_rs = np.c_[path_rs, [rev(m, s) for m, s in path_rs]]

# ---------------------------------------------------------------- point values
def at(x0, m, s):
    p0, q0 = float(np.exp(logp(x0))), float(norm.pdf(x0, m, s))
    return {"p": p0, "q": q0, "log2_p_over_q": float(np.log2(p0 / q0))}


# ---------------------------------------------------------------- heavier smoothing (beat 11)
H_HEAVY = 0.36                      # Gaussian kernel bandwidth, minutes (R's default is 0.335)
LPH = logsumexp(norm.logpdf(X[:, None], e[None, :], H_HEAVY), axis=1) - np.log(n)


def rev_h(m, s):
    return kl_bits(norm.logpdf(X, m, s), LPH)


rh = minimize(lambda t: rev_h(t[0], np.exp(t[1])), (mB, np.log(sB)), method="Nelder-Mead",
              options=dict(xatol=1e-9, fatol=1e-13, maxiter=20000))
th = np.array([mB, np.log(sB)])
hpath = [(mB, sB, rev_h(mB, sB))]
for it in range(20000):
    g = np.array([(rev_h(th[0] + h, np.exp(th[1])) - rev_h(th[0] - h, np.exp(th[1]))) / (2 * h),
                  (rev_h(th[0], np.exp(th[1] + h)) - rev_h(th[0], np.exp(th[1] - h))) / (2 * h)])
    th = th - step * g
    hpath.append((float(th[0]), float(np.exp(th[1])), rev_h(th[0], np.exp(th[1]))))
    if np.linalg.norm(g) < 1e-6:
        break
hpath = np.array(hpath)
seg = np.r_[0, np.cumsum(np.hypot(np.diff(hpath[:, 0]), np.diff(np.log(hpath[:, 1]))))]
u = np.linspace(0, seg[-1], 81)
hpath_rs = np.c_[np.interp(u, seg, hpath[:, 0]), np.interp(u, seg, hpath[:, 1])]
hpath_rs = np.c_[hpath_rs, [rev_h(m, s) for m, s in hpath_rs]]

# ---------------------------------------------------------------- R's default smoothing (beat 12)
# density(faithful$eruptions) uses bw.nrd0 = 0.9 * min(sd, IQR/1.34) * n^(-1/5) (R quantile type 7
# = numpy's default "linear")
q75, q25 = np.percentile(e, [75, 25])
H_RDEF = float(0.9 * min(e.std(ddof=1), (q75 - q25) / 1.34) * n ** -0.2)
LPR = logsumexp(norm.logpdf(X[:, None], e[None, :], H_RDEF), axis=1) - np.log(n)


def rev_r(m, s):
    return kl_bits(norm.logpdf(X, m, s), LPR)


rr_wide = minimize(lambda t: rev_r(t[0], np.exp(t[1])), (mA, np.log(sA)), method="Nelder-Mead",
                   options=dict(xatol=1e-9, fatol=1e-13, maxiter=20000))
rr_narrow = minimize(lambda t: rev_r(t[0], np.exp(t[1])), (mB, np.log(sB)), method="Nelder-Mead",
                     options=dict(xatol=1e-9, fatol=1e-13, maxiter=20000))


def descend(fun, m0, s0, max_it=20000):
    """Plain gradient descent on (mu, log sigma); returns the raw path [(mu, sd, D)]."""
    th = np.array([m0, np.log(s0)])
    out = [(m0, s0, fun(m0, s0))]
    for it in range(max_it):
        g = np.array([(fun(th[0] + h, np.exp(th[1])) - fun(th[0] - h, np.exp(th[1]))) / (2 * h),
                      (fun(th[0], np.exp(th[1] + h)) - fun(th[0], np.exp(th[1] - h))) / (2 * h)])
        th = th - step * g
        out.append((float(th[0]), float(np.exp(th[1])), fun(th[0], np.exp(th[1]))))
        if np.linalg.norm(g) < 1e-6:
            break
    return np.array(out)


def resample(p, k, fun):
    seg = np.r_[0, np.cumsum(np.hypot(np.diff(p[:, 0]), np.diff(np.log(p[:, 1]))))]
    u = np.linspace(0, seg[-1], k)
    rs = np.c_[np.interp(u, seg, p[:, 0]), np.interp(u, seg, p[:, 1])]
    return np.c_[rs, [fun(m, s) for m, s in rs]]


# plain gradient descent from A under R's default smoothing: where does the same slide stop?
rpath = descend(rev_r, mA, sA)
rdef_descent_from_A = [float(rpath[-1, 0]), float(rpath[-1, 1]), float(rpath[-1, 2])]
rpath_rs = resample(rpath, 81, rev_r)

# ---------------------------------------------------------------- cross-validated smoothing (beat 12)
# leave-one-out likelihood cross-validation of the Gaussian kernel bandwidth
def loo(hh):
    L = norm.logpdf(e[:, None], e[None, :], hh)
    np.fill_diagonal(L, -np.inf)
    return float(np.sum(logsumexp(L, axis=1) - np.log(n - 1)))


HS = np.round(np.arange(0.050, 0.4001, 0.001), 3)
LOO = np.array([loo(hh) for hh in HS])
H_CV = float(HS[np.argmax(LOO)])
LPC = logsumexp(norm.logpdf(X[:, None], e[None, :], H_CV), axis=1) - np.log(n)


def rev_c(m, s):
    return kl_bits(norm.logpdf(X, m, s), LPC)


rc_from_A = minimize(lambda t: rev_c(t[0], np.exp(t[1])), (mA, np.log(sA)), method="Nelder-Mead",
                     options=dict(xatol=1e-9, fatol=1e-13, maxiter=20000))
rc_from_B = minimize(lambda t: rev_c(t[0], np.exp(t[1])), (mB, np.log(sB)), method="Nelder-Mead",
                     options=dict(xatol=1e-9, fatol=1e-13, maxiter=20000))
# the slide shown on screen: from the wide R-default fit, descend on the cross-validated curve
cpath = descend(rev_c, rdef_descent_from_A[0], rdef_descent_from_A[1])
cpath_rs = resample(cpath, 81, rev_c)
# stability of the bell-first optimum across bandwidths (narrated: R's default tips it)
BW_SCAN = {}
for hh in (0.10, 0.15, 0.20, 0.25, 0.30, 0.3348, 0.36):
    lph = logsumexp(norm.logpdf(X[:, None], e[None, :], hh), axis=1) - np.log(n)
    f = lambda m, s, lph=lph: kl_bits(norm.logpdf(X, m, s), lph)
    ra_ = minimize(lambda t: f(t[0], np.exp(t[1])), (mA, np.log(sA)), method="Nelder-Mead",
                   options=dict(xatol=1e-8, fatol=1e-12, maxiter=20000))
    rb_ = minimize(lambda t: f(t[0], np.exp(t[1])), (mB, np.log(sB)), method="Nelder-Mead",
                   options=dict(xatol=1e-8, fatol=1e-12, maxiter=20000))
    BW_SCAN[str(hh)] = {"from_A": [float(ra_.x[0]), float(np.exp(ra_.x[1])), float(ra_.fun)],
                        "from_B": [float(rb_.x[0]), float(np.exp(rb_.x[1])), float(rb_.fun)],
                        "gap_share": float(np.sum(np.exp(lph)[(X >= 2.5) & (X < 3.5)]) * DX)}

# ---------------------------------------------------------------- the unweighted log-ratio (beat 6)
XL = np.linspace(0.0, 7.0, 7001)
LR = (logp(XL) - norm.logpdf(XL, mA, sA)) / LN2           # log2(p/q_A) on the plotted range
gap = (XL > 2.3) & (XL < 3.7)
below = LR < -1.0
clip_runs = XL[np.flatnonzero(np.diff(below.astype(int)))].tolist()

counts, edges = np.histogram(e, bins=np.arange(1.5, 5.25 + 1e-9, 0.25))
P_X = np.exp(LP)
neg_entropy = float(np.sum(P_X * LP) * DX)        # -h(P), nats

out = {
    "n": n,
    "eruptions": sorted(e.tolist()),
    "hist_edges": edges.tolist(), "hist_counts": counts.tolist(),
    "mix": {"pi": pi.tolist(), "mu": mu.tolist(), "sd": sd.tolist()},
    "mix_mean": float((pi * mu).sum()),
    "mix_sd": float(np.sqrt((pi * (sd ** 2 + mu ** 2)).sum() - (pi * mu).sum() ** 2)),
    "neg_entropy_nats": neg_entropy,
    "A": {"mu": mA, "sd": sA, "fwd": fwd(mA, sA), "rev": rev(mA, sA),
          "numerical_fwd_opt": [float(ra.x[0]), float(np.exp(ra.x[1])), float(ra.fun)]},
    "B": {"mu": mB, "sd": sB, "fwd": fwd(mB, sB), "rev": rev(mB, sB)},
    "C_local_min_short_hump": {"mu": float(rc.x[0]), "sd": float(np.exp(rc.x[1])),
                               "rev": float(rc.fun)},
    "at_2min": {"A": at(2.0, mA, sA), "B": at(2.0, mB, sB)},
    "at_3min": {"A": at(3.0, mA, sA), "B": at(3.0, mB, sB)},
    "share_data_under_3": float((e < 3).mean()), "count_data_under_3": int((e < 3).sum()),
    "count_data_2p5_3p5": int(((e >= 2.5) & (e < 3.5)).sum()),
    "share_P_2p5_3p5": float(np.sum(P_X[(X >= 2.5) & (X < 3.5)]) * DX),
    "share_A_2p5_3p5": float(norm.cdf(3.5, mA, sA) - norm.cdf(2.5, mA, sA)),
    "share_A_outside_1_6": float(norm.cdf(1, mA, sA) + norm.sf(6, mA, sA)),
    "share_B_under_3": float(norm.cdf(3.0, mB, sB)),
    "ratio_rev_A_over_fwd_A": None,
    "descent_path": path_rs.tolist(),
    "descent_raw_steps": len(path),
    "heavy": {"h": H_HEAVY, "rev_opt": [float(rh.x[0]), float(np.exp(rh.x[1])), float(rh.fun)],
              "fwd_opt_sd": float(np.sqrt(sA ** 2 + H_HEAVY ** 2)),
              "share_2p5_3p5": float(np.sum(np.exp(LPH)[(X >= 2.5) & (X < 3.5)]) * DX),
              "path_from_B": hpath_rs.tolist(), "raw_steps": len(hpath)},
    "rdef": {"h": H_RDEF, "iqr": float(q75 - q25), "sd_n1": float(e.std(ddof=1)),
             "wide": [float(rr_wide.x[0]), float(np.exp(rr_wide.x[1])), float(rr_wide.fun)],
             "narrow_local": [float(rr_narrow.x[0]), float(np.exp(rr_narrow.x[1])),
                              float(rr_narrow.fun)],
             "descent_from_A": rdef_descent_from_A, "path_from_A": rpath_rs.tolist(),
             "raw_steps_from_A": len(rpath),
             "share_2p5_3p5": float(np.sum(np.exp(LPR)[(X >= 2.5) & (X < 3.5)]) * DX)},
    "log2_p_over_qA": {"at_0": float(LR[0]), "at_7": float(LR[-1]),
                       "gap_min": [float(XL[gap][np.argmin(LR[gap])]), float(LR[gap].min())],
                       "crosses_minus1_at": clip_runs},
    "cv": {"h": H_CV, "loo_at_h": float(LOO.max()), "loo_at_rdef": loo(H_RDEF),
           "fit_from_A": [float(rc_from_A.x[0]), float(np.exp(rc_from_A.x[1])), float(rc_from_A.fun)],
           "fit_from_B": [float(rc_from_B.x[0]), float(np.exp(rc_from_B.x[1])), float(rc_from_B.fun)],
           "path_from_wide": cpath_rs.tolist(), "raw_steps": len(cpath),
           "share_2p5_3p5": float(np.sum(np.exp(LPC)[(X >= 2.5) & (X < 3.5)]) * DX)},
    "bandwidth_scan": BW_SCAN,
    "naive": {"shift": -0.8, "stretch": 1.8, "fwd_shifted": fwd(mA - 0.8, sA),
              "fwd_stretched": fwd(mA, 1.8 * sA)},
    "p_at_A_pm_sd": [float(np.exp(logp(mA - sA))), float(np.exp(logp(mA + sA)))],
    "mix_peaks": [float(np.exp(logp(mu[0]))), float(np.exp(logp(mu[1])))],
    "qB_peak": float(norm.pdf(mB, mB, sB)), "qA_peak": float(norm.pdf(mA, mA, sA)),
    "var_ratio_B_over_A": float((sB / sA) ** 2),
    "A_pm_sd": [mA - sA, mA + sA], "B_pm_sd": [mB - sB, mB + sB],
}
out["ratio_rev_A_over_fwd_A"] = out["A"]["rev"] / out["A"]["fwd"]
out["ratio_sdB_over_sdA"] = sB / sA
(HERE / "data.json").write_text(json.dumps(out, indent=1))
for k, v in out.items():
    if k not in ("eruptions", "descent_path", "heavy", "rdef", "cv"):
        print(k, v)
print("heavy", {k: v for k, v in out["heavy"].items() if k != "path_from_B"})
print("rdef", {k: v for k, v in out["rdef"].items() if k != "path_from_A"})
print("cv", {k: v for k, v in out["cv"].items() if k != "path_from_wide"})
print("cv path ends", out["cv"]["path_from_wide"][-1], "monotone",
      bool(np.all(np.diff(cpath_rs[:, 2]) <= 1e-9)))
print("rdef path ends", out["rdef"]["path_from_A"][-1], "monotone",
      bool(np.all(np.diff(rpath_rs[:, 2]) <= 1e-9)))
print("heavy path ends", out["heavy"]["path_from_B"][-1], "monotone",
      bool(np.all(np.diff(hpath_rs[:, 2]) <= 1e-9)))
