#!/usr/bin/env python3
"""Physical three-face original-link SU(2) PW matrix product and inverse tests.
Uses explicit SU(2) CG coefficients and complex off-diagonal matrices.
Finite checks are regressions, not the proof of the all-degree theorem.
Requires numpy, sympy and scipy (for SymPy CG).
"""
from itertools import product
from math import sqrt
import numpy as np
from sympy import S
from sympy.physics.wigner import clebsch_gordan

def spinops(n):
    j=n/2; m=np.arange(j,-j-1,-1)
    plus=np.zeros((n+1,n+1),complex)
    for k in range(n):
        z=m[k+1];plus[k,k+1]=sqrt((j-z)*(j+z+1))
    return ((plus+plus.conj().T)/2,(plus-plus.conj().T)/(2j),np.diag(m).astype(complex))

def cg(q,r,l):
    C=np.zeros((q+1,r+1,l+1),complex)
    for j,k,M in product(range(q+1),range(r+1),range(l+1)):
        C[j,k,M]=float(clebsch_gordan(S(q)/2,S(r)/2,S(l)/2,
                S(q-2*j)/2,S(r-2*k)/2,S(l-2*M)/2))
    return C

def pw_product(F,G,p,q,r,s,l):
    F=F.reshape(p+1,q+1,p+1,q+1)
    G=G.reshape(r+1,s+1,r+1,s+1)
    C=cg(q,r,l)
    raw=np.einsum('ajkt,ucwz->ajucktwz',F,G,optimize=True)
    H=np.einsum('juM,ajucktwz,twN->aMckNz',C,raw,C,optimize=True)
    d=(p+1)*(l+1)*(s+1)
    return H.reshape(d,d)

def input_k(p,q):
    a,b=spinops(p),spinops(q)
    ia=np.eye(p+1);ib=np.eye(q+1)
    A=[np.kron(x,ib) for x in a]
    B=[np.kron(ia,x) for x in b]
    base=p*(p+2)+q*(q+2)
    def D(x):return -sum((A[k]@x@B[k] for k in range(3)),np.zeros_like(x))
    return lambda x:base*x+2*D(x)

def output_k(p,l,s):
    a,b,c=spinops(p),spinops(l),spinops(s)
    ia=np.eye(p+1);ib=np.eye(l+1);ic=np.eye(s+1)
    A=[np.kron(np.kron(x,ib),ic) for x in a]
    B=[np.kron(np.kron(ia,x),ic) for x in b]
    C=[np.kron(np.kron(ia,ib),x) for x in c]
    base=p*(p+2)+l*(l+2)+s*(s+2)
    def D(x):return -sum((A[k]@x@B[k]+B[k]@x@C[k] for k in range(3)),np.zeros_like(x))
    return lambda x:base*x+2*D(x),D,base

def nuclear(x):return float(np.linalg.norm(x,'nuc'))

def test(p,q,r,s,seed):
    rng=np.random.default_rng(seed)
    df=(p+1)*(q+1); dg=(r+1)*(s+1)
    if seed%2:
        F=np.outer(rng.normal(size=df)+1j*rng.normal(size=df),
                   rng.normal(size=df)+1j*rng.normal(size=df))
        G=np.outer(rng.normal(size=dg)+1j*rng.normal(size=dg),
                   rng.normal(size=dg)+1j*rng.normal(size=dg))
    else:
        F=rng.normal(size=(df,df))+1j*rng.normal(size=(df,df))
        G=rng.normal(size=(dg,dg))+1j*rng.normal(size=(dg,dg))
    KF=input_k(p,q)(F);KG=input_k(r,s)(G)
    PF=df*nuclear(F);PG=dg*nuclear(G)
    P=p*(p+2);Q=q*(q+2);R=r*(r+2);T=s*(s+2)
    wF=1+max(p,q);wG=1+max(r,s)
    result=0.; product_norm=0.; max_scalar=0.
    for l in range(abs(q-r),q+r+1,2):
        H=pw_product(F,G,p,q,r,s,l)
        d=(p+1)*(l+1)*(s+1)
        product_norm+=d*nuclear(H)
        K,D,base=output_k(p,l,s)
        forcing=(pw_product(KF,G,p,q,r,s,l)
                 +pw_product(F,KG,p,q,r,s,l)-K(H))/2
        answer=np.zeros_like(forcing);term=forcing/base
        for i in range(160):
            answer+=term
            term=(-2/base)*D(term)
            if np.linalg.norm(term,'fro')<1.e-13:break
        residual=np.linalg.norm(K(answer)-forcing,'fro')
        assert residual<1.e-8*max(1,np.linalg.norm(forcing,'fro')),(p,q,r,s,l)
        result+=d*(1+max(p,l,s))*nuclear(answer)
        scalar=(1+max(p,l,s))/(wF*wG)*(.5+1.25*(P+Q+R+T)/base)
        max_scalar=max(max_scalar,scalar)
        assert scalar<6
    assert product_norm<=PF*PG*(1+1.e-9)
    ratio=result/(PF*PG*wF*wG)
    assert ratio<=max_scalar*(1+1.e-8)
    assert ratio<=6+1.e-8
    print('PASS',p,q,r,s,'observed',format(ratio,'.7f'),'envelope',format(max_scalar,'.7f'))

if __name__=='__main__':
    cases=[(1,1,1,1),(1,2,2,1),(1,3,3,1),(1,4,4,1),
           (2,3,3,2),(1,4,3,1),(2,2,3,1),(3,2,2,2),
           (2,1,2,3),(2,3,1,1),(3,1,3,1),(3,3,1,2)]
    for i,c in enumerate(cases):test(*c,seed=71+i)
    print('PASS 12 actual PW matrix original-link inverse, product, norm checks')
