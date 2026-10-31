"""R3-IR-550 reproducibility: local fiber fluctuation comparison.
Requires numpy and scipy; no original binary data needed.
"""
import numpy as np
from scipy.special import roots_jacobi
from math import exp, log
ys,weights=roots_jacobi(96,.5,.5)
weights/=weights.sum()
p=np.linspace(-1,1,301)
def certificate(lam,eta,tau):
    F=np.exp(-lam*p[:,None]**2-eta*ys[None,:]**2+tau*p[:,None]*ys[None,:])
    q=F@weights
    s=F**2@weights
    r=s/q**2
    Bq=log(q.max()/q.min())
    Br=log(r.max()/r.min())
    cert=exp(-2*Bq-Br)
    haar=2/np.pi*np.sqrt(np.maximum(0,1-p**2))
    density=s/np.trapezoid(s*haar,p)
    assert np.min(density)>=cert-1e-9
    return Bq,Br,cert,float(density.min())
print('coupled',certificate(.7,.9,.5))
for eta in (0.,1.,5.,20.):
    Bq,Br,cert,actual=certificate(.7,eta,0.)
    assert abs(Br)<1e-11
    assert abs(cert-exp(-1.4))<1e-10
    print('spectator eta',eta,'certificate',cert,'relative minimum',actual)
print('PASS: local comparison insensitive to noninteracting spectator concentration')
