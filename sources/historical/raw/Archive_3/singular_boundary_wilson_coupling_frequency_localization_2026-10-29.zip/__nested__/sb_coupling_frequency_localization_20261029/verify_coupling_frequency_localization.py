#!/usr/bin/env python3
"""Deterministic continuous SU2 rotor nonlinear local response audit.
Rotor has A=4, H(x)=n(n+2)+x(1-p), and is a benchmark, NOT a Penrose patch.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import eval_chebyu
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss
from math import sqrt
A=4.0; c0=3/(2*sqrt(2))
N=128
n=np.arange(N,dtype=float)
D=n*(n+2)
quad_nodes,quad_weights=leggauss(28)

def spectrum(x):
    en,v=eigh_tridiagonal(D+x,np.full(N-1,-x/2))
    ground=v[:,0]
    pground=np.zeros(N)
    pground[:-1]+=.5*ground[1:]
    pground[1:]+=.5*ground[:-1]
    # driver b(1-p), mixed excited amplitude -b * <excited|p|ground>
    coef=v[:,1:].T@pground
    eps=en[1:]-en[0]
    chi=float(np.sum(coef*coef/eps))
    m1=float(np.sum(coef*coef*eps))
    pp=float(np.dot(ground,pground))
    assert abs(m1-(A/4)*(1-(np.dot(pground,pground))))<1e-7  # p² expectation as ||p psi||²
    return chi, pp, coef*coef, eps

def gaussint(fn,low,high):
    x=(quad_nodes+1)*(high-low)/2+low
    return float(sum(w*fn(z) for z,w in zip(x,quad_weights))*(high-low)/2)

def intervals(b):
    a=[0.,.5,1.,2.,4.,8.,16.,32.,64.,128.,256.,512.,1024.,2048.,4096.]
    return [(lo,min(hi,b)) for lo,hi in zip(a,a[1:]) if lo<b]

def calc(b,C,L=1.):
    h=b**(-.5);lam=L*h**(-11/8)
    # finite u: x=ub. spectral amplitude W=b(1-p), chi_WW(u)=b² chi_pp(x)
    total=early=hi=0.
    for lo,up in intervals(b):
        def fchi(x): return spectrum(x)[0]
        total+=gaussint(fchi,lo,up)
        if lo<C: early+=gaussint(fchi,lo,min(up,C))
        def uv(x):
            chi,p,z,eps=spectrum(x)
            return np.sum(z[eps>lam]/eps[eps>lam])
        hi+=gaussint(uv,lo,up)
    # multiply by b to convert 0^1 b² chi(x)du=b∫0^b chi(x)dx
    total*=b; early*=b; hi*=b
    p1=spectrum(b)[1]
    theoretical=b*p1/2
    abs_err=abs(total-theoretical)
    eta=c0*sqrt(A/C)
    # integrated source high energy upper using m1 bound, A=4
    highub=(3/(4*sqrt(2)))*A**1.5*b**1.5/(lam*lam)
    lower=b/2*(1-eta)-highub
    assert abs_err < 5e-6*b
    assert early>=b/2*(1-eta)-1e-8*b
    assert hi<=highub+1e-8*b
    assert early-hi>=lower-1e-8*b
    print(f'b={b:<6} C={C:<5} total={total:.8f} exact={theoretical:.8f} early_fraction={early/total:.8f} high_fraction={hi/total:.8f} guaranteed_early_fraction={1-eta:.6f}')
for b,C in [(100.,25.),(400.,25.),(1600.,25.),(1600.,64.)]:
    calc(b,C)
chi,p,z,eps=spectrum(0)
assert abs(chi-1/(3*A))<1e-12
# The exact SU(2) heat kernel at time 1 has a strictly positive global
# min/max ratio. This supplies a volume-free one-link conditional minorant.
def heat_one(theta):
    x=np.cos(theta)
    return sum((i+1)*np.exp(-i*(i+2)/4)*eval_chebyu(i,x) for i in range(40))
theta=np.linspace(0,np.pi,401)
vals=np.array([heat_one(v) for v in theta])
m=float(np.min(vals));M=float(np.max(vals))
assert m>0 and M>=m
norm=quad(lambda t:2/np.pi*np.sin(t)**2*heat_one(t),0,np.pi,epsabs=1e-12)[0]
assert abs(norm-1)<1e-10
print(f'SU2 heat kernel k1: min={m:.9f}, max={M:.9f}, Haar norm={norm:.9f}, positivity ratio={m/M:.9e}')
print('PASS: SU2 exact full-time susceptibility, bridge boundary-layer localization, spectral UV fsum, Haar heat kernel')
