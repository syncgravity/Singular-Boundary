#!/usr/bin/env python3
"""PF-I16: interacting one-rhombus spectral f-sum consistency verifier."""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal

def qminus(T):
    return (3+2*T-math.sqrt(T*(4*T+3)))/(4*(1+T))

for T in (0,0.01,0.1,1,4,16,100,10000):
    q=qminus(T)
    assert 0<q<=0.75
    assert abs((1.5-2*q)**2-4*T*q*(1-q))<1e-8*(1+T)

for a,b in ((1.,0.),(1.,0.71),(1.,1.),(0.4,2.),(2.,4.)):
    n=np.arange(45,dtype=float)
    diag=a*n*(n+2)+b
    off=np.full(44,-b/2)
    ev,V=eigh_tridiagonal(diag,off)
    psi=V[:,0]; E0=ev[0]
    P=np.diag(np.ones(44)/2,1)+np.diag(np.ones(44)/2,-1)
    pv=P@psi
    response=(diag-E0)*pv
    response[:-1]+=off*pv[1:]
    response[1:]+=off*pv[:-1]
    Q=1-float(pv@pv)
    m1=float(pv@response)
    assert abs(m1-a*Q)<1e-8
    T=max(0,float(np.dot(psi,(diag-b)*psi))/(4*a))
    assert T<=2*b/a+1e-10 and Q>=qminus(T)-1e-10
    m2=float(response@response)
    B=4*a*(0.75+math.sqrt(T))
    assert m2<=B*B+1e-8
    print(f"a={a:.2f}, b={b:.2f}, Q={Q:.10f}, Tlink={T:.10f}, m1={m1:.10f}, m2={m2:.10f}")
print("PASS: 8 algebraic and 5 interacting one-rhombus checks")
