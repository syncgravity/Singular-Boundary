#!/usr/bin/env python3
"""Finite-volume a posteriori spectral gap / cap certificate, abstract matrix check.
The theorem applies to H=T+V, positive bounded V; the test matrix is not an 8-face Wilson calculation.
"""
import numpy as np,math
from scipy.linalg import eigh
rng=np.random.default_rng(716)
for M in (40.,80.,200.,600.):
    T=np.diag([0.,6.,M+5.,M+12.])
    A=np.array([[.7,.3,-.1,.05],[.3,.6,.12,-.08],[-.1,.12,.4,.1],[.05,-.08,.1,.45]])
    V=A.T@A
    H=T+V
    v,W=eigh(H)
    P=H[:2,:2];val,U=eigh(P)
    er0,er1=val[:2];phi=np.r_[U[:,0],np.zeros(2)]
    rho=np.linalg.norm(V[2:,:2],2);res=np.linalg.norm(V[2:,:2]@U[:,0])
    theta=rho*rho/(M-er1)
    d=er1-er0-theta
    assert d>0
    assert v[1]-v[0]>=d-1e-10
    assert np.linalg.norm((np.eye(4)-np.outer(W[:,0],W[:,0]))@phi)<=res/d+1e-10
    O=np.diag([.8,.15,.35,.5]);nu=np.linalg.norm(O,2)
    exact=W[:,0]@O@W[:,0];ritz=phi@O@phi
    err=2*math.sqrt(2)*nu*res/d
    assert abs(exact-ritz)<=err+1e-12
    print('M',M,'certified gap',d,'true gap',v[1]-v[0], 'certified cap error',err,'actual error',abs(exact-ritz))
print('PASS certified finite Ritz gap and ground-state observable control, not an SU2 8-face spectrum')
