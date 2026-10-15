"""Episode 32 data: one simulated dataset (seed 0) + a 200-dataset check that it is typical.
Run:  python3 sim.py   -> writes sim_data.npz, prints every number used on screen."""
import numpy as np, warnings, sys
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.model_selection import KFold
warnings.filterwarnings("ignore")
n, p, sigma = 60, 50, 1.0
beta = np.zeros(p); idx = [3, 14, 25, 36, 47]; beta[idx] = [2.0, -1.5, 1.5, -1.0, 1.0]

def run(seed):
    rng = np.random.default_rng(seed)
    X = rng.standard_normal((n, p)); y = X @ beta + sigma * rng.standard_normal(n)
    Xt = rng.standard_normal((10000, p)); yt = Xt @ beta + sigma * rng.standard_normal(10000)
    kf = KFold(10, shuffle=True, random_state=0)
    fits = {"ols": LinearRegression(fit_intercept=False).fit(X, y),
            "ridge": RidgeCV(alphas=np.logspace(-2, 3, 60), fit_intercept=False, cv=kf).fit(X, y),
            "lasso": LassoCV(alphas=np.logspace(-3, 0, 60), fit_intercept=False, cv=kf,
                             max_iter=100000).fit(X, y)}
    out = {}
    for k, m in fits.items():
        c = m.coef_
        out[k] = dict(c=c, train=np.mean((X @ c - y) ** 2), test=np.mean((Xt @ c - yt) ** 2),
                      zeros=int(np.sum(c == 0)), true_kept=int(np.sum(c[idx] != 0)),
                      alpha=getattr(m, "alpha_", None))
    return out

if __name__ == "__main__":
    r = run(0)
    for k, v in r.items():
        print(k, "train %.3f test %.3f zeros %d true_kept %d alpha %s min|c| %.4f max|c| %.3f"
              % (v["train"], v["test"], v["zeros"], v["true_kept"], v["alpha"],
                 np.abs(v["c"]).min(), np.abs(v["c"]).max()))
    np.savez("sim_data.npz", beta=beta, ols=r["ols"]["c"], ridge=r["ridge"]["c"], lasso=r["lasso"]["c"],
             tests=np.array([r[k]["test"] for k in ("ols", "ridge", "lasso")]),
             trains=np.array([r[k]["train"] for k in ("ols", "ridge", "lasso")]))
    if "--check" in sys.argv:
        R = [run(s) for s in range(200)]
        for k in ("ols", "ridge", "lasso"):
            t = [q[k]["test"] for q in R]; z = [q[k]["zeros"] for q in R]
            print(k, "200 datasets: test median %.2f IQR %.2f-%.2f; zeros median %d range %d-%d; all 5 kept in %d/200"
                  % (np.median(t), *np.percentile(t, [25, 75]), np.median(z), min(z), max(z),
                     sum(q[k]["true_kept"] == 5 for q in R)))
