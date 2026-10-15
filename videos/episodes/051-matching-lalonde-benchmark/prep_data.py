"""Rebuild data.npz and print every number used in episode 51 from the public NSW / PSID files.

Data: Rajeev Dehejia's public copies of the LaLonde (1986) / Dehejia-Wahba (1999) files,
    https://users.nber.org/~rdehejia/data/nsw_dw.dta        (185 treated, 260 controls)
    https://users.nber.org/~rdehejia/data/psid_controls.dta (PSID-1, 2,490 men)
    https://users.nber.org/~rdehejia/data/nsw.dta           (LaLonde's 297 / 425 sample)
Usage:  python prep_data.py <dir with the three .dta files> [out.npz]
Earnings are in 1982 dollars (as in both papers).
"""
import sys

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

D = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else "data.npz"
dw = pd.read_stata(f"{D}/nsw_dw.dta")
ps = pd.read_stata(f"{D}/psid_controls.dta").reset_index(drop=True)
la = pd.read_stata(f"{D}/nsw.dta")
tr = dw[dw.treat == 1].reset_index(drop=True)
ct = dw[dw.treat == 0]

print("experimental benchmark (DW subsample):", tr.re78.mean() - ct.re78.mean())        # 1794.34
print("experimental benchmark (LaLonde sample):",
      la[la.treat == 1].re78.mean() - la[la.treat == 0].re78.mean())                    # 886.30
print("mean 1978 earnings: trainees", tr.re78.mean(), "PSID", ps.re78.mean())            # 6349 / 21554
print("naive difference:", tr.re78.mean() - ps.re78.mean())                              # -15204.8
print("1975 earnings ratio PSID/trainees:", ps.re75.mean() / tr.re75.mean())             # 12.4
print("age: trainees", tr.age.mean(), "PSID", ps.age.mean())                             # 25.8 / 34.9


def features(df, re74=True):
    """Dehejia & Wahba (1999) Table 3 note (e): PSID-1 logit specification."""
    cols = {"age": df.age, "age2": df.age ** 2, "ed": df.education, "ed2": df.education ** 2,
            "married": df.married, "nodeg": df.nodegree, "black": df.black, "hisp": df.hispanic,
            "re75": df.re75 / 1e3, "re75sq": (df.re75 / 1e3) ** 2}
    if re74:
        cols.update({"re74": df.re74 / 1e3, "re74sq": (df.re74 / 1e3) ** 2,
                     "u74black": (df.re74 == 0) * 1.0 * df.black})
    return pd.DataFrame(cols).values


def scores(re74):
    df = pd.concat([tr, ps])
    X = features(df, re74)
    mu, sd = X.mean(0), X.std(0)
    m = LogisticRegression(C=1e8, max_iter=50000, tol=1e-10).fit((X - mu) / sd, df.treat.values)
    p = m.predict_proba((X - mu) / sd)[:, 1]
    return p[:len(tr)], p[len(tr):]


out = {}
for re74 in (True, False):
    pt, pc = scores(re74)
    idx = np.array([np.argmin(np.abs(pc - v)) for v in pt])     # 1-NN on the score, with replacement
    tag = "1" if re74 else "0"
    print(f"--- score {'with' if re74 else 'without'} 1974 earnings")
    print("  PSID men below the lowest trainee score:", (pc < pt.min()).sum())  # 1344 (DW: 1,333)
    print("  score > 0.8: trainees", (pt > 0.8).sum(), "PSID", (pc > 0.8).sum())  # 98 / 7 (DW: 98 / 7)
    print("  distinct PSID men used by 1-NN matching:", len(np.unique(idx)))     # 55 (DW Table 4: 56)
    print("  1-NN matching estimate (our run):", np.mean(tr.re78.values - ps.re78.values[idx]))
    out.update({f"pt{tag}": pt, f"pc{tag}": pc, f"idx{tag}": idx})

q = ps.re75 < 500
print("PSID men with 1975 earnings < $500:", q.sum(), "of whom 1974 earnings > $10k:",
      (q & (ps.re74 > 10000)).sum())                                                     # 255 / 45
print("trainees with zero earnings in both 1974 and 1975:",
      ((tr.re74 == 0) & (tr.re75 == 0)).mean())                                         # 0.589
np.savez(OUT, tr_re74=tr.re74.values, tr_re75=tr.re75.values, tr_re78=tr.re78.values,
         ps_re74=ps.re74.values, ps_re75=ps.re75.values, ps_re78=ps.re78.values, **out)
