#!/usr/bin/env python3
"""Exact one-face SU(2) CG Poisson multiplier and arbitrary-matrix regressions.
This is a local certificate, NOT a full nonlinear history-tame theorem.
"""
from fractions import Fraction as F
from itertools import product
import numpy as np
from sympy import S
from sympy.physics.wigner import clebsch_gordan
def scalar(m,n,l):
    if l==0:return F(0)
    em=m*(m+2);en=n*(n+2);el=l*(l+2)
    return F(l+1,(m+1)*(n+1))*abs(F(em+en-el,2*el))
def cg(m,n,l):
    C=np.zeros(((m+1)*(n+1),l+1),complex)
    for i,j,k in product(range(m+1),range(n+1),range(l+1)):
        C[i*(n+1)+j,k]=float(clebsch_gordan(S(m)/2,S(n)/2,S(l)/2,
            S(m-2*i)/2,S(n-2*j)/2,S(l-2*k)/2))
    return C
count=0
for m in range(1,101):
    for n in range(1,101):
        for l in range(abs(m-n),m+n+1,2):
            assert scalar(m,n,l)<=F(2,3),(m,n,l)
            count+=1
assert count==348350
rng=np.random.default_rng(20261104);blocks=0
for m,n in product(range(1,6),repeat=2):
    for rankone in (False,True):
        A=rng.normal(size=(m+1,m+1))+1j*rng.normal(size=(m+1,m+1))
        B=rng.normal(size=(n+1,n+1))+1j*rng.normal(size=(n+1,n+1))
        if rankone:
            A=np.outer(A[:,0],A[0,:]);B=np.outer(B[:,0],B[0,:])
        input_norm=(m+1)*(n+1)*np.linalg.norm(A,'nuc')*np.linalg.norm(B,'nuc')
        output=0
        for l in range(abs(m-n),m+n+1,2):
            C=cg(m,n,l);H=C.conj().T@np.kron(A,B)@C
            assert np.linalg.norm(C.conj().T@C-np.eye(l+1))<1e-9
            multiplier=(m*(m+2)+n*(n+2)-l*(l+2))/(2*l*(l+2)) if l else 0
            output+=(l+1)*np.linalg.norm(multiplier*H,'nuc')
            blocks+=1
        assert output<=(2/3)*input_norm*(1+1e-10)
print("PASS",count,"exact one-face scalar CG channels")
print("PASS",blocks,"dense/rank-one complex CG matrix output blocks")
