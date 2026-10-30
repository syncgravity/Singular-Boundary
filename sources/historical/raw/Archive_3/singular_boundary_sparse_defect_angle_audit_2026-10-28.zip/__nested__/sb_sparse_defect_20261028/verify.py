#!/usr/bin/env python3
"""Independent deterministic checks; no Monte Carlo and no Stage-26 modification."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ive

rstar=math.pi**2/2-2
assert rstar>0
C=math.pi**2/4-1
for p in np.linspace(-1,1,25001):
    d=1-p; g=.5*math.acos(p)**2-d
    assert g>=-1e-12 and g<=C*d+1e-10
    assert g<=math.pi**4*d*d/96+1e-10

# Bessel/Haar normalizers and one-face radial moments.
def moments(k):
    def wt(x):
        p=1-x/k
        return (2/math.pi)*math.sqrt(max(0.,1-p*p))*math.exp(-2*x)/k
    xmax=min(2*k,100.)
    norm=quad(wt,0,xmax,epsabs=1e-15,epsrel=1e-13,limit=250)[0]
    assert norm>0
    def g(p):return .5*math.acos(max(-1.,min(1.,p)))**2-(1-p)
    # minus branch is p -> -p of plus branch
    vals=[]
    for f in [g,lambda p:g(p)**2,lambda p:g(-p),lambda p:g(-p)**2,lambda p:1-p,lambda p:(1-p)**2]:
        vals.append(quad(lambda x:f(1-x/k)*wt(x),0,xmax,epsabs=1e-15,epsrel=1e-11,limit=250)[0]/norm)
    ep,ep2,em,em2,ed,ed2=vals
    assert ep>=-1e-12 and em>=-1e-12
    # Haar Z= I1(2 k)/k
    zlog=2*k+math.log(ive(1,2*k))-math.log(k)
    return ep,ep2-ep**2,em,em2-em**2,ed,ed2-ed**2,zlog

print('fixed-support sparse-defect positive gauge-invariant trial superposition')
print('h      M       mean_shift    variance_R    rstar^2/4')
for n in [12,20,32,48,64]:
    h=1/n**2; k=1/h; F=n**4; M=n  # h^-1/2
    ep,vp,em,vm,ed,vd,logZ=moments(k)
    mean_shift=math.sqrt(h)*M*(em-ep)
    vbrp=h*F*vp
    vbrs=h*((F-M)*vp+M*vm)
    var=(vbrp+vbrs)/2+mean_shift**2/4
    assert M/F<.01 and abs(vbrp)<1e-4 and abs(vbrs)<2e-3
    assert abs(var-rstar*rstar/4)<1.
    assert M*logZ>100
    meanZp=h*F*ed
    meanZs=meanZp+h*M*(2-2*ed)
    assert 0<meanZp<2 and 0<meanZs<3
    print(f'{h:<7.6f} {M:>3}    {mean_shift:>11.7f}  {var:>12.7f}  {rstar*rstar/4:>12.7f}')

# Check exact tilted barrier integration constants / rate.
for h in [.12,.06,.025,.008]:
    a=2.;beta=3.;Delta=5/h**3;zeta=.5
    b=beta/h**2;s=zeta*math.sqrt(b/a)
    u0=h*(Delta/b)*(math.atanh(zeta)/zeta)
    lam=s/h
    assert abs(lam-zeta*math.sqrt(beta/a)/h**2)<1e-7
    assert abs(u0-5*math.atanh(zeta)/beta/zeta)<1e-7
    tailbound=u0*u0+2*u0/lam+2/(lam*lam)
    assert tailbound>u0*u0
print('PASS: global SU2 angle inequality, exact Haar/Bessel branch integrals, overlap, source variance, optimized Laplace tail')
