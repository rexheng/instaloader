import numpy as np
s=0.55; mL,mR=-1.7,1.3
def p(x): return 3*np.exp(-(x-mR)**2/(2*s*s))+np.exp(-(x-mL)**2/(2*s*s))
Z=4*s*np.sqrt(2*np.pi); print("Z exact",Z)
xs=np.linspace(-4,4,100); dx=xs[1]-xs[0]; print("grid100 Z",p(xs).sum()*dx)
g=np.linspace(-4,4,200001); y=p(g); 
# valley
mask=(g>mL)&(g<mR); v=g[mask][np.argmin(y[mask])]; print("valley",v,p(v), "peaks",p(mL),p(mR))
from math import erf,sqrt
print("true share left of valley", (y[g<v].sum())/(y.sum()))
rng=np.random.default_rng(7)
def run(n,sig,x0=1.3):
    x=x0; out=np.empty(n); acc=0
    for i in range(n):
        y_=x+sig*rng.normal()
        if rng.random()<p(y_)/p(x): x=y_; acc+=1
        out[i]=x
    return out,acc/n
for sig in [0.05,1.2,1.5,25]:
    out,a=run(50000,sig); print(sig,"acc",a,"share small",(out<v).mean())
print("years 1e20/1e9", 1e20/1e9/3.156e7)
seq=[60.]
for _ in range(6): a=seq[-1]; b=120-a; seq.append(a-a/3+b)
print(seq)
def ess(x):
    x=x-x.mean(); n=len(x); f=np.fft.rfft(x,2*n); ac=np.fft.irfft(f*np.conj(f))[:n]; ac/=ac[0]
    s=0
    for k in range(1,n):
        if ac[k]<0.05: break
        s+=ac[k]
    return n/(1+2*s)
for seed in [7,8,9]:
    rng=np.random.default_rng(seed)
    out,a=run(50000,1.5); print(seed,"acc",a,"share",(out<v).mean(),"ess",ess(out))
rng=np.random.default_rng(3)
for sig in [0.05,25]:
    out,a=run(2000,sig); print(sig,a,(out<v).mean(), out.min(), out.max(), ess(out))
