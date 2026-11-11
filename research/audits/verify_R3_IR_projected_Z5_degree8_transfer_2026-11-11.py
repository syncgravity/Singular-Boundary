#!/usr/bin/env python3
"""Rational lower-bound verifier for the r=8 projected-Z5 finite 2-skeleton."""
from fractions import Fraction as F
from math import sqrt, exp, pi

S1=F(333528,10**9)
S2=F(194619,10**12)
T=F(250292,10**9)
h=F(166813,10**9)
rho=F(6,5)

def certified(r):
    q=S1+S2
    B=F(r,2)*S1
    c=F(1,2)-2*r*rho*q
    # exp(-x)>=1-x and pi<22/7
    ctr=F(3,4)*(1-F(88,7)*B)
    ell=B*B  # c_tr<=3/4
    C3=2*rho*42*r*T  # sqrt(1728)<42
    CH=6*r*h*(2+3*r*(1+rho))
    CR=F(3,4)*B  # sqrt(2)/2<3/4
    CG=C3+CR
    a=c-ell
    b=ctr-CH
    lower=min(a,b)-CG/2
    return B,c,ctr,ell,C3,CH,CR,CG,a,b,lower

def diagnostic(r):
    q=float(S1+S2); B=r*float(S1)/2
    c=.5-2*r*float(rho)*q
    ctr=.75*exp(-4*pi*B)
    ell=4*ctr*B*B/3
    C3=2*float(rho)*sqrt(1728)*r*float(T)
    CH=6*r*float(h)*(2+3*r*(1+float(rho)))
    CR=sqrt(2)*B/2; CG=C3+CR
    a=c-ell; b=ctr-CH
    return (a+b-sqrt((a-b)**2+CG**2))/2

if __name__=="__main__":
    for r in (4,8):
        v=certified(r)
        print("r",r)
        print("B,c,ctr_lower,ell_upper,C3_upper,CH_upper,CR_upper,CG_upper,a_lower,b_lower,lambda_lower")
        print(" ".join(f"{float(x):.15g}" for x in v))
        print("diagnostic lambda",f"{diagnostic(r):.12f}")
        assert v[-1]>0
    assert certified(8)[-1]>F(197,1000)
    print("PASS: conservative rational r=8 full-Hessian energy bound remains positive")
