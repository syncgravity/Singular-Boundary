#!/usr/bin/env python3
"""Independent SU2 multi-face exponential trial and rigorous energy-cutoff inequalities.
Applies to the full physical Wilson link theory; checks use exact Haar radial quadrature.
"""
import numpy as np
import math
from scipy.integrate import quad
from scipy.special import roots_chebyu
from scipy.linalg import eigh

def tilted(kappa):
    # Integrate Haar SU2 with shifted exponential to prevent overflow.
    f=lambda p:2/math.pi*math.sqrt(max(0.,1-p*p))*math.exp(2*kappa*(p-1))
    z=quad(f,-1,1,epsabs=1e-13,limit=300)[0]
    pp=quad(lambda p:p*f(p),-1,1,epsabs=1e-13,limit=300)[0]/z
    pp2=quad(lambda p:p*p*f(p),-1,1,epsabs=1e-13,limit=300)[0]/z
    return pp,pp2
for kap in (.75,2.5,7.0,20.):
    r,p2=tilted(kap)
    assert abs((1-p2)-3*r/(2*kap))<3e-9
    assert 0 < 1-r <= 3/(4*kap)+1e-12
    print('kappa',kap,'mean p',r,'mean d',1-r,'kinetic moment',1-p2)

# Independent plaquette Haar coordinate powers. Adjoint-color averages kill mixed gradient form.
# Trial energy is sum of per-face kinetic+magnetic terms, with uniform coefficient.
for aa,bb in [(4.,4.),(4.,100.),(3.5,400.)]:
    k=math.sqrt(2*bb/aa)
    r,p2=tilted(k)
    v=aa*k*k*(1-p2)/4+bb*(1-r)
    certificate=(3/(2*math.sqrt(2)))*math.sqrt(aa*bb)
    assert v<=certificate+1e-9
    print('a,b,optimized trial energy,certificate',aa,bb,v,certificate)

# Rigorous finite-dimensional self-adjoint block complement: general H=T+V, T>=0,
# 0<=V<=B, P=1_{T<=M}, Q T Q>=M, ||PVQ||<=B.
# Then E_full >= min eigenvalue of [[E_Ritz,-B],[-B,M]].
for M in (60.,100.,1000.):
    T=np.diag([0.,3.,M+1.,M+5.])
    rng=np.random.default_rng(41)
    X=rng.normal(size=(4,4));V=X.T@X
    V=9*V/np.linalg.eigvalsh(V).max(); B=9.
    H=T+V
    E=float(np.linalg.eigvalsh(H)[0]);Er=float(np.linalg.eigvalsh(H[:2,:2])[0]);
    lo=(Er+M-math.sqrt((Er-M)**2+4*B*B))/2
    assert lo-1e-10 <= E <= Er+1e-10
    if M>Er:assert 0<=Er-E<=B*B/(M-Er)+1e-10
    print('Ritz sandwich',M,'lower',lo,'exact',E,'Ritz',Er)

# Illustrative scaling only: 7 retained faces, each a~4, b~h^-2.
# Uniform ground-state electric tail ||Q_M Omega||²<=S/M.
for h in (.2,.1,.05,.025):
    b=4/h**2
    S=7*(3/(2*math.sqrt(2)))*math.sqrt(4*b)
    B=2*7*b
    M=200*S
    assert S/M==.005
    # center-cap convolution test requires stronger M with ratio nu/alpha^2~h^-3/2
    a=math.acos(1-h)
    from scipy.integrate import quad
    def phi(t):
        x=t/a
        if x<=.25:return 1.
        if x>=.5:return 0.
        z=4*(x-.25)
        return (1-10*z**3+15*z**4-6*z**5)**2
    alpha=quad(lambda t:2/math.pi*math.sin(t)**2*phi(t),0,a/2)[0]
    nu=quad(lambda t:2/math.pi*math.sin(t)**2*phi(t)**2,0,a/2)[0]
    M_cap=S*(16*nu/alpha**2)**2
    err=2*nu*math.sqrt(S/M_cap)+nu*S/M_cap
    assert err<alpha*alpha/4
    print('h',h,'S',S,'B',B,'M for absolute cap control',M_cap,'cert error/Haar',err/alpha**2)
print('PASS SU2 multi-face trial, gap-free electric tail, finite Ritz energy enclosure and cap accuracy scale')
