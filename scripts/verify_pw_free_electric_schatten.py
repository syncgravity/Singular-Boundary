#!/usr/bin/env python3
"""Finite original-link three-face PW free-electric nuclear inverse regression."""
from itertools import product
from math import sqrt
import numpy as np
def spin(n):
    j=n/2;m=np.arange(j,-j-1,-1);up=np.zeros((n+1,n+1),complex)
    for k in range(n):
        x=m[k+1];up[k,k+1]=sqrt((j-x)*(j+x+1))
    return ((up+up.conj().T)/2,(up-up.conj().T)/(2j),np.diag(m).astype(complex))
def check():
    rng=np.random.default_rng(211);count=0
    for n in product(range(4),repeat=3):
        if not any(n):continue
        d=int(np.prod([x+1 for x in n]));id=[np.eye(x+1) for x in n]
        mat=[spin(x) for x in n]
        J=[]
        for i in range(3):
            J.append([])
            for a in range(3):
                v=[mat[i][a] if k==i else id[k] for k in range(3)]
                J[i].append(np.kron(np.kron(v[0],v[1]),v[2]))
        D=sum(x*(x+2) for x in n)
        S=sum(sqrt(n[i]*(n[i]+2)*n[i+1]*(n[i+1]+2)) for i in range(2))/4
        assert 2*S<=D/2+1e-12
        def cross(X):
            return -sum((J[i][a]@X@J[i+1][a] for i in range(2) for a in range(3)),np.zeros_like(X))
        def K(X):return D*X+2*cross(X)
        for _ in range(2):
            X=rng.standard_normal((d,d))+1j*rng.standard_normal((d,d))
            out=np.zeros_like(X);step=X/D
            for k in range(140):
                out+=step;step=-2*cross(step)/D
                if np.linalg.norm(step,'fro')<1e-13:break
            assert np.linalg.norm(K(out)-X,'fro')<1e-9*max(1,np.linalg.norm(X,'fro'))
            assert np.linalg.norm(out,'nuc')<=2*np.linalg.norm(X,'nuc')/D+1e-9
            count+=1
    print('PASS',count,'random original-link face-sector Fourier inverse and nuclear checks')
if __name__=='__main__':check()
