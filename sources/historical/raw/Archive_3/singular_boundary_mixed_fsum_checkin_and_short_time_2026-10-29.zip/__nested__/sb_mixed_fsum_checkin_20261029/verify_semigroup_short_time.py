#!/usr/bin/env python3
"""Finite center-even diffusion regression of rigorous mixed heat-response bounds."""
import numpy as np
from scipy.linalg import eigh
for z in (.25,.0625,.015625,.00390625):
    c=[1.,1.,z,1.,1.];L=np.zeros((6,6))
    for i,w in enumerate(c):
        L[i,i]+=w;L[i+1,i+1]+=w;L[i,i+1]-=w;L[i+1,i]-=w
    E,V=eigh(L);vac=np.ones(6)/np.sqrt(6.)
    src=np.eye(6)[0]*vac[0]-vac/6
    drv=np.eye(6)[2]*vac[2]-vac/6
    v=V.T@src;w=V.T@drv
    m1=float(np.sum(E*v*w));m3o=float(np.sum(E**3*v*v));m1o=float(np.sum(E*v*v));m1w=float(np.sum(E*w*w))
    assert abs(m1)<1e-12
    c0=float(np.dot(v,w))
    for t in (.01,.1,1.,5.):
        ct=float(np.sum(v*w*np.exp(-t*E)))
        assert abs(ct-c0)<=t*np.sqrt(m1o*m1w)+1e-11
        assert abs(ct-c0+t*m1)<=.5*t*t*np.sqrt(m3o*m1w)+1e-11
    inverse=float(np.sum(v[1:]*w[1:]/E[1:]))
    assert abs(inverse-(1/(24*z)-1/27))<1e-9
    print(f'epsilon={z:g} M1={m1:.2e} M-1={inverse:.8f} short-time bounds PASS')
print('PASS: exact finite-time Taylor bounds; inverse response remains unbounded as gap closes')
