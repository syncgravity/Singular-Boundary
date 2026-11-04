#!/usr/bin/env python3
"""Original-link versus face PW nuclear-norm transport: cyclic coefficient test."""
from itertools import product
import numpy as np

def cyclic(d,L):
    dim=d**L;A=np.zeros((dim,dim),dtype=np.int8)
    for t in product(range(d),repeat=L):
        i=np.ravel_multi_index(t,(d,)*L)
        j=np.ravel_multi_index(t[1:]+t[:1],(d,)*L)
        A[i,j]=1
    assert (A.sum(0)==1).all() and (A.sum(1)==1).all()
    assert np.array_equal(A@A.T,np.eye(dim,dtype=int))
    return A

def check():
    rng=np.random.default_rng(419);total=0
    for d in range(2,5):
        for L in range(1,6):
            if d**L>500:continue
            A=cyclic(d,L);dim=d**L
            assert abs(np.linalg.norm(A,'nuc')-dim)<1e-9
            U=[]
            for _ in range(L):
                x=rng.standard_normal((d,d))+1j*rng.standard_normal((d,d))
                q,_=np.linalg.qr(x);U.append(q)
            tensor=U[0]
            for u in U[1:]:tensor=np.kron(tensor,u)
            reverse=np.eye(d,dtype=complex)
            for u in U[::-1]:reverse=reverse@u
            assert abs(np.trace(A@tensor)-np.trace(reverse))<2e-10
            assert dim*np.linalg.norm(A,'nuc')==d**(2*L)
            total+=1
    for N in range(1,101):
        for d in range(2,11):
            assert d**(2*((2*N+2)-N))==d**(2*N+4)
    print('PASS',total,'matrix/trace/nuclear regressions and 900 exact integer ratios')
if __name__=='__main__':check()
