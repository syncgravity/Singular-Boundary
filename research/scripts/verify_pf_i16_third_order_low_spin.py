#!/usr/bin/env python3
"""PF-I16 exact SU(2) character low-spin score, orders 1–8; numerical check."""
from fractions import Fraction as F
from collections import defaultdict
from math import pi
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh_tridiagonal

def add(a,b,z=F(1)):
    d=defaultdict(F,a)
    for k,v in b.items():d[k]+=z*v
    return {k:v for k,v in d.items() if v}
def mul(a,b):
    d=defaultdict(F)
    for i,v in a.items():
        for j,w in b.items():
            for k in range(abs(i-j),i+j+1,2):d[k]+=v*w
    return {k:v for k,v in d.items() if v}

P=[{0:F(1)}]; energy={}
for n in range(1,9):
    r={k:v/2 for k,v in mul({1:F(1)},P[-1]).items()}
    for j in range(2,n):r=add(r,P[n-j],energy[j])
    if n>=2:energy[n]=-r.get(0,F(0))
    P.append({k:v/F(k*(k+2)) for k,v in r.items() if k})
L=[]
for n in range(1,9):
    poly={0:{0:F(1)}}; s={}
    for m in range(1,n+1):
        nxt={}
        for degree,A in poly.items():
            for j in range(1,n-degree+1):
                v=degree+j
                nxt[v]=add(nxt.get(v,{}),mul(A,P[j]))
        poly=nxt
        s=add(s,poly.get(n,{}),F((-1)**(m+1),m))
    L.append(s)
assert L[0][1]==F(1,6)
assert L[1][2]==-F(1,288)
assert L[2]=={1:-F(1,648),3:F(1,6480)}
assert L[4][1]==F(7,124416)
assert L[6][1]==-F(311,111974400)
x,w=leggauss(1000)
theta=(x+1)*pi/2
hw=w*np.sin(theta)**2
n=np.arange(36)
characters=np.sin((n[:,None]+1)*theta)/np.sin(theta)
for b in (.2,.1,.05,.02):
    _,V=eigh_tridiagonal(n*(n+2)+b,-b/2*np.ones(len(n)-1))
    phi=(V[:,0]/V[0,0])@characters
    s=np.log(phi)
    c1=float(hw@(s*characters[1]))
    c3=float(hw@(s*characters[3]))
    assert abs(c1-(b/6-b**3/648))<.00007*b**5
    assert abs(c3-b**3/6480)<.00001*b**5
    print(f'b={b:.3g} log_chi1={c1:.12g} log_chi3={c3:.12g}')
print('PASS 8 rational orders; low-spin at orders 3/5/7; 4 Jacobi/Haar checks')
