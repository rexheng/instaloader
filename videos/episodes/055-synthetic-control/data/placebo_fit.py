import pandas as pd, numpy as np, sys
from scipy.optimize import nnls
d=pd.read_csv(sys.argv[1],sep=';')
P=d.pivot(index='Year',columns='State',values='PacksPerCapita')
pre=(P.index<=1988)
def fit(y,X):
    # nnls with sum-to-one via heavy penalty row
    A=np.vstack([X,1e3*np.ones(X.shape[1])]); b=np.r_[y,1e3]
    w,_=nnls(A,b); return w
states=list(P.columns)
res={}
for s in states:
    others=[o for o in states if o!=s and not (s!='California' and o=='California')]
    X=P[others].values; y=P[s].values
    w=fit(y[pre],X[pre])
    syn=X@w; gap=y-syn
    res[s]=dict(gap=gap,pre=np.mean(gap[pre]**2),post=np.mean(gap[~pre]**2),w=dict(zip(others,w)))
ca=res['California']
print('CA outcome-only weights',{k:round(v,3) for k,v in ca['w'].items() if v>0.005})
print('CA gap 2000',ca['gap'][-1].round(1),'pre rmspe',np.sqrt(ca['pre']).round(2))
ratio={s:r['post']/r['pre'] for s,r in res.items()}
rk=sorted(ratio.items(),key=lambda x:-x[1])
print(rk[:5]); print('CA rank',[s for s,_ in rk].index('California')+1,'of',len(rk))
for k in (2,5,20):
    keep=[s for s in states if res[s]['pre']<=k*ca['pre']]
    print(k,'x cutoff: states kept incl CA',len(keep))
# Montana alone
m=P['Montana'];print('Montana gap 2000',(P['California']-m).iloc[-1],'1988',(P['California']-m).loc[1988])
print('pre rmspe each placebo', sorted([(round(np.sqrt(r['pre']),1),s) for s,r in res.items()])[-6:])
np.savez(sys.argv[2],years=P.index.values,ca=P['California'].values,
  donors=P.drop(columns='California').values,donor_names=np.array(P.drop(columns='California').columns),
  gaps=np.array([res[s]['gap'] for s in states]),gap_names=np.array(states),
  prerm=np.array([np.sqrt(res[s]['pre']) for s in states]))
