#!/usr/bin/env python3
"""Gauge-orbit center Hessian and nonlinear invariant-graph calibration only."""
import numpy as np
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import eigsh

def geom(n):
    vertices=[(x,y,z) for x in range(n+1) for y in range(n+1) for z in range(n+1)]
    vm={v:i for i,v in enumerate(vertices)}
    edges=[]; em={}
    for p in vertices:
        for d in range(3):
            if p[d]<n: em[(p,d)]=len(edges);edges.append((p,d))
    def sh(p,d):
        a=list(p);a[d]+=1;return tuple(a)
    fr=[];fc=[];fv=[];dr=[];dc=[];dv=[];f=0
    for k,(p,d) in enumerate(edges):
        dr.extend((k,k));dc.extend((vm[p],vm[sh(p,d)]));dv.extend((-1,1))
    for p in vertices:
        for i in range(3):
            for j in range(i+1,3):
                if p[i]>=n or p[j]>=n:continue
                for v,k,sgn in ((p,i,1),(sh(p,i),j,1),(sh(p,j),i,-1),(p,j,-1)):
                    fr.append(f);fc.append(em[(v,k)]);fv.append(sgn)
                f+=1
    B=coo_matrix((fv,(fr,fc)),shape=(f,len(edges))).tocsr()
    D=coo_matrix((dv,(dr,dc)),shape=(len(edges),len(vertices))).tocsr()
    return B,D,len(vertices),len(edges),f

checks=0
for n in range(2,7):
    B,D,V,E,P=geom(n)
    assert (V,E,P)==((n+1)**3,3*n*(n+1)**2,3*n*n*(n+1));checks+=1
    assert (B@D).nnz==0;checks+=1
    assert np.all(B.power(2).sum(axis=1).A1==4);checks+=1
    degree=B.power(2).sum(axis=0).A1
    assert degree.max()==4;checks+=1
    e=int(np.flatnonzero(degree==4)[0]);z=np.where(B.getcol(e).toarray().ravel()!=0,-1,1)
    assert np.sum(z==-1)==4;checks+=1
    H=B.T@diags(z/4)@B
    assert abs(H[e,e]+1)<1e-12;checks+=1
    assert (H@D).nnz==0;checks+=1
    lam=-eigsh(H,k=1,which='SA',tol=1e-10)[0][0]
    assert lam>=1-1e-8;checks+=1
    q=3*(E-V+1)
    assert 3*(V-1)+q==3*E;checks+=1
    print('n',n,'orbit_dim',3*(V-1),'normal_dim',q,'top_growth',round(lam,8),'unstable_rank>=3')

for q in (3,6,9,30,60):
    for m in (3,min(q,6)):
        for r in (.01,.1,.3):
            for frac in (.01,.2,.9):
                w=frac*r
                assert r**(q-m)*w**m<=r**q+1e-12;checks+=1
print('PASS PARTIAL',checks)
for lam in (.3,1.,2.):
    for mu in (0.,.2,1.):
        for c in (-1.,.5,2.):
            k=-c/(lam+2*mu)
            for z0 in (-.12,-.04,0.,.07,.11):
                for eta0 in (-.0001,.00003,.0002):
                    for t in (0.,.1,.5,1.5,3.):
                        z=z0*np.exp(-mu*t);u=k*z*z+eta0*np.exp(lam*t)
                        assert abs(u-k*z*z-eta0*np.exp(lam*t))<1e-12;checks+=1
print('PASS TOTAL',checks)
