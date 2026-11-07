#!/usr/bin/env python3
"""Conditional scalar-Laplacian comparison control only.
NOT the dissertation's coupled-Z5 operator, NOT a gauge-invariant Yang–Mills gap.
Requires NumPy/SciPy. Run: python research/scripts/verify_pf_scalar_spectral_control_2026_11_07.py
"""
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigsh
checks=0
for n in (5,7,10,14,19,25):
    N=n*n
    L=lil_matrix((N,N),dtype=float)
    for x in range(n):
        for y in range(n):
            i=x*n+y
            for xx,yy in ((x+1,y),(x,y+1)):
                if xx<n and yy<n:
                    j=xx*n+yy
                    L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    L=L.tocsr()
    eig=np.sort(eigsh(L,k=3,which="SM",return_eigenvectors=False,tol=1e-10))
    lam=float(eig[1])
    exact=2*(1-np.cos(np.pi/n))
    assert abs(lam-exact)<2e-8,(n,lam,exact);checks+=1
    t=max(1,n//4);theta=t/n;delta=(n-2*t+1)/(n-1);R=n-1
    # D=4, c+=a=1. Elementary two-slab Rayleigh estimate.
    upper=4/(2*theta*theta*delta*delta*R*R)
    assert lam<=upper+1e-10,(n,lam,upper);checks+=1
    assert lam*n*n<10.5;checks+=1
assert checks==18
print("PASS",checks,"scalar controls only; PF coupled-Z5 3D operator NOT constructed")
