"""Simulated survey for episode 27 (all data simulated; seeds fixed).

300 people, age uniform 20-65, income ($k) = 18 + 0.9*(age-20) + N(0, 11), floored at 8.
Three erasers each remove exactly 90 people (30%), sampled without replacement with
probability proportional to a skip propensity:
  MCAR  constant
  MAR   logistic(-0.15*(age-20) + c)      (young skip more)
  MNAR  logistic( 0.16*(income-mean) + c) (high earners skip more)
c is set so the mean propensity is 0.30.  The "age fix" fits OLS income~age on the
survivors and fills each blank with line(age) + N(0, residual sd) (stochastic regression
imputation).  Run this file to print every number used in the episode.
"""
import numpy as np

N, K = 300, 90


def logistic(z):
    return 1 / (1 + np.exp(-z))


def calib(score, target=0.3):
    lo, hi = -20.0, 20.0
    for _ in range(80):
        m = (lo + hi) / 2
        if logistic(score + m).mean() > target:
            hi = m
        else:
            lo = m
    return logistic(score + m), m


def build():
    rng = np.random.default_rng(27)
    age = rng.uniform(20, 65, N)
    inc = np.maximum(18 + 0.9 * (age - 20) + rng.normal(0, 11, N), 8.0)
    T = inc.mean()
    p_mar, c_mar = calib(-0.15 * (age - 20))
    p_mnar, c_mnar = calib(0.16 * (inc - T))
    props = {"MCAR": np.full(N, 0.3), "MAR": p_mar, "MNAR": p_mnar}
    # skip propensity as a function of position (for drawing the eraser's fog)
    out_fog = {"MCAR": lambda a, y: 0.3,
               "MAR": lambda a, y: logistic(-0.15 * (a - 20) + c_mar),
               "MNAR": lambda a, y: logistic(0.16 * (y - T) + c_mnar)}
    seeds = {"MCAR": 9, "MAR": 71, "MNAR": 150}
    out = {"age": age, "inc": inc, "T": T, "fog": out_fog}
    for k, p in props.items():
        r = np.random.default_rng(seeds[k])
        idx = r.choice(N, K, replace=False, p=p / p.sum())
        miss = np.zeros(N, bool)
        miss[idx] = True
        obs = ~miss
        b, a = np.polyfit(age[obs], inc[obs], 1)
        resid = np.std(inc[obs] - (a + b * age[obs]))
        rr = np.random.default_rng(100 + seeds[k])
        fill = a + b * age[miss] + rr.normal(0, resid, miss.sum())
        imp = inc.copy()
        imp[miss] = fill
        out[k] = dict(p=p, miss=miss, a=a, b=b, fill=fill, cc=inc[obs].mean(),
                      imp=imp.mean())
    b, a = np.polyfit(age, inc, 1)
    out["true_line"] = (a, b)
    return out


if __name__ == "__main__":
    d = build()
    print("true mean %.2f  min %.1f max %.1f" % (d["T"], d["inc"].min(), d["inc"].max()))
    print("true line a=%.2f b=%.3f" % d["true_line"])
    for k in ("MCAR", "MAR", "MNAR"):
        m = d[k]
        print(k, "deleted-mean %.2f err %+.2f | filled-mean %.2f err %+.2f | line a=%.2f b=%.3f"
              " | p %.2f-%.2f | blanks mean age %.1f mean inc %.1f" % (
                  m["cc"], m["cc"] - d["T"], m["imp"], m["imp"] - d["T"], m["a"], m["b"],
                  m["p"].min(), m["p"].max(), d["age"][m["miss"]].mean(), d["inc"][m["miss"]].mean()))
        print("   fill range %.1f-%.1f" % (m["fill"].min(), m["fill"].max()))
