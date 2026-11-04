#!/usr/bin/env python3
"""Physical original-link two-face × singleton PW matrix test.
Checks both overlap orientations and independently reproduces a prior
exact quaternion/PW source. Requires numpy and sympy.
"""
from itertools import product
from math import sqrt
import numpy as np
from sympy import S
from sympy.physics.wigner import clebsch_gordan

def spin(n):
    j=n/2;m=np.arange(j,-j-1,-1);up=np.zeros((n+1,n+1),complex)
    for k in range(n):
        z=m[k+1];up[k,k+1]=sqrt((j-z)*(j+z+1))
    return ((up+up.conj().T)/2,(up-up.conj().T)/(2j),np.diag(m).astype(complex))

def cg(n,r,l):
    T=np.zeros((n+1,r+1,l+1),complex)
    for j,k,m in product(range(n+1),range(r+1),range(l+1)):
        T[j,k,m]=float(clebsch_gordan(S(n)/2,S(r)/2,S(l)/2,
                                      S(n-2*j)/2,S(r-2*k)/2,S(l-2*m)/2))
    return T

def product_block(F,G,p,n,r,l,left):
    C=cg(n,r,l)
    if left:
        A=F.reshape(n+1,p+1,n+1,p+1)
        X=np.einsum('ajkt,uv,auM,kvN->MjNt',A,G,C,C,optimize=True)
    else:
        A=F.reshape(p+1,n+1,p+1,n+1)
        X=np.einsum('ajkt,uv,juM,tvN->aMkN',A,G,C,C,optimize=True)
    d=(p+1)*(l+1)
    return X.reshape(d,d)

def physical(a,b):
    x,y=spin(a),spin(b);ix=np.eye(a+1);iy=np.eye(b+1)
    X=[np.kron(t,iy) for t in x];Y=[np.kron(ix,t) for t in y]
    energy=a*(a+2)+b*(b+2)
    def D(v):return -sum((X[k]@v@Y[k] for k in range(3)),np.zeros_like(v))
    return (lambda v:energy*v+2*D(v)),D,energy

rng=np.random.default_rng(307);cases=0
for p,n,r in product(range(1,4),repeat=3):
    for left in (False,True):
        dim=(p+1)*(n+1)
        F=rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim))
        G=rng.normal(size=(r+1,r+1))+1j*rng.normal(size=(r+1,r+1))
        inputnorm=(p+1)*(n+1)*(r+1)*np.linalg.norm(F,'nuc')*np.linalg.norm(G,'nuc')
        KF=physical(n,p)[0](F) if left else physical(p,n)[0](F)
        total=0.
        for l in range(abs(n-r),n+r+1,2):
            H=product_block(F,G,p,n,r,l,left)
            K,D,E=physical(l,p) if left else physical(p,l)
            source=(product_block(KF,G,p,n,r,l,left)+r*(r+2)*H-K(H))/2
            answer=np.zeros_like(source);step=source/E
            for _ in range(128):
                answer+=step;step=-2*D(step)/E
                if np.linalg.norm(step,'fro')<1.e-13:break
            assert np.linalg.norm(K(answer)-source,'fro')<1e-9*max(1,np.linalg.norm(source,'fro'))
            total+=(p+1)*(l+1)*(1+max(p,l))*np.linalg.norm(answer,'nuc')
        ratio=total/(inputnorm*(1+max(p,n))*(r+1))
        assert ratio<8
        cases+=1
print('PASS',cases,'complex two-face × singleton physical original-link matrix cases')
F=np.eye(4,dtype=complex);G=np.eye(2,dtype=complex);KF=physical(1,1)[0](F)
Pnorm=0.;L1=0.
for l in (0,2):
    H=product_block(F,G,1,1,1,l,True);K,D,E=physical(l,1)
    source=(product_block(KF,G,1,1,1,l,True)+3*H-K(H))/2
    ans=np.zeros_like(source);step=source/E
    for _ in range(100):
        ans+=step;step=-2*D(step)/E
    d=2*(l+1);v=np.linalg.norm(ans,'nuc')
    Pnorm+=d*v;L1+=d*(1+max(l,1))*v
assert abs(Pnorm-43/6)<1e-9 and abs(L1-35/2)<1e-9
print('PASS exact prior nested regression P0=43/6, L1=35/2')
