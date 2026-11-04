#!/usr/bin/env python3
"""CG reconstruction, physical original-link K and all-spin trace-word regression.
Requires numpy, scipy, sympy. Finite checks supplement the analytic all-degree proof.
The archived companion ZIP contains this full checker, logs and SHA-256 manifest.
"""
from itertools import product
from math import sqrt
import numpy as np
from scipy.linalg import expm,svdvals
from sympy import S
from sympy.physics.wigner import clebsch_gordan

def spinops(n):
    j=n/2; m=np.arange(j,-j-1,-1); up=np.zeros((n+1,n+1),complex)
    for k in range(n):
        a=m[k+1];up[k,k+1]=sqrt((j-a)*(j+a+1))
    return ((up+up.conj().T)/2,(up-up.conj().T)/(2j),np.diag(m).astype(complex))
def cg(n,m,l,i,k,M):
    return float(clebsch_gordan(S(n)/2,S(m)/2,S(l)/2,
                 S(n-2*i)/2,S(m-2*k)/2,S(l-2*M)/2))
def coeff(n,m,l):
    dn=n+1;dm=m+1;dl=l+1;d=dn*dm*dl
    X=np.zeros((d,d),complex)
    for i,j,k,z,M,N in product(range(dn),range(dn),range(dm),
                                range(dm),range(dl),range(dl)):
        c=cg(n,m,l,j,k,M)*cg(n,m,l,i,z,N)
        if c:
            row=np.ravel_multi_index((j,N,k),(dn,dl,dm))
            col=np.ravel_multi_index((i,M,z),(dn,dl,dm))
            X[row,col]+=c
    return X
def physical(n,m,l):
    a,b,c=spinops(n),spinops(l),spinops(m)
    ia=np.eye(n+1);ib=np.eye(l+1);ic=np.eye(m+1)
    A=[np.kron(np.kron(a[k],ib),ic) for k in range(3)]
    B=[np.kron(np.kron(ia,b[k]),ic) for k in range(3)]
    C=[np.kron(np.kron(ia,ib),c[k]) for k in range(3)]
    base=n*(n+2)+l*(l+2)+m*(m+2)
    def d12(x):return -sum((A[k]@x@B[k] for k in range(3)),np.zeros_like(x))
    def d23(x):return -sum((B[k]@x@C[k] for k in range(3)),np.zeros_like(x))
    def K(x):return base*x+2*d12(x)+2*d23(x)
    return K,d12,d23,base
def randrep(n,seed):
    rng=np.random.default_rng(seed);axis=rng.normal(size=3)
    axis/=np.linalg.norm(axis);theta=.3+.07*seed;J=spinops(n)
    return expm(1j*theta*sum(axis[k]*J[k] for k in range(3)))
def check(n,m):
    U=randrep(n,1);Vn=randrep(n,2)
    Vm=randrep(m,2);W=randrep(m,3)
    value=np.trace(U@Vn)*np.trace(Vm@W)
    reconstructed=0j;ratio_num=0.;zero_middle=None
    for l in range(abs(n-m),n+m+1,2):
        H=coeff(n,m,l);Vl=randrep(l,2)
        reconstructed+=np.trace(H@np.kron(np.kron(U,Vl),W))
        K,d12,d23,b=physical(n,m,l)
        lam=1.5*(n*(n+2)+m*(m+2))
        T=(lam*H-K(H))/2
        R=np.zeros_like(T);step=T/b
        for _ in range(120):
            R+=step;step=-2*(d12(step)+d23(step))/b
            if np.linalg.norm(step,'fro')<3e-14:break
        assert np.linalg.norm(K(R)-T,'fro')<2e-9
        assert np.linalg.norm(R,'nuc')<=2*np.linalg.norm(H,'nuc')+1e-8
        d=(n+1)*(l+1)*(m+1)
        ratio_num+=d*np.linalg.norm(R,'nuc')*(1+max(n,l,m))
        if l==0:zero_middle=np.trace(R@np.kron(U,W))
    assert abs(reconstructed-value)<1e-9
    Pn=(n+1)**5;Pm=(m+1)**5
    ratio=ratio_num/(Pn*Pm)
    assert ratio<=2+1e-9
    if n==m:
        target=np.trace(U@W.conj().T)/(4*(n+1))
        assert abs(zero_middle-target)<1e-9
    print('PASS',n,m,'PW L1 ratio',round(ratio,10))
if __name__=='__main__':
    for n,m in [(1,1),(1,2),(2,1),(2,2),(1,3),(3,1),(2,3),(3,2),(3,3)]:
        check(n,m)
    print('PASS all CG reconstructions, physical Fourier inverse blocks, and zero-middle channels')
