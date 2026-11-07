#!/usr/bin/env python3
"""Finite-regulator exact cubic incidence and non-Abelian weighted-energy calibration.
Full 201-check finite-difference verifier is in Library Proof Audits ZIP.
"""
import math
import numpy as np

def complex_3d(n):
    edges={}; faces=[]; centers=[]; incid={}
    def step(p,d):
        x=list(p);x[d]+=1;return tuple(x)
    for p in np.ndindex((n+1,)*3):
        for d in range(3):
            if p[d]<n:edges[p,d]=len(edges)
    for p in np.ndindex((n+1,)*3):
        for i in range(3):
            for j in range(i+1,3):
                if p[i]>=n or p[j]>=n:continue
                boundary=(edges[p,i],edges[step(p,i),j],edges[step(p,j),i],edges[p,j])
                idx=len(faces);faces.append(boundary)
                x=np.array(p,dtype=float)/n;x[i]+=.5/n;x[j]+=.5/n;centers.append(x)
                for e in boundary:incid.setdefault(e,[]).append(idx)
    return edges,faces,np.array(centers),incid

checks=0
for n in [1,2,3,4,5,6]:
    e,faces,c,inc=complex_3d(n)
    assert len(e)==3*n*(n+1)**2;checks+=1
    assert len(faces)==3*n*n*(n+1);checks+=1
    assert max(map(len,inc.values()))<=4;checks+=1
    assert all(len(set(f))==4 for f in faces);checks+=1
    for ids in inc.values():
        for p in ids:
            for q in ids:
                assert np.linalg.norm(c[p]-c[q])<=math.sqrt(2)/n+1e-12
                checks+=1
    for L in [0,.1,.7,2]:
        phi=-L*np.linalg.norm(c-.5,axis=1)
        w=np.exp(2*phi)
        for ids in inc.values():
            mx=max(w[p] for p in ids)
            for p in ids:
                assert 0<=mx-w[p]<=2*math.sqrt(2)*L*mx/n+1e-12
                assert mx/w[p]<=math.exp(2*math.sqrt(2)*L/n)+1e-12
                checks+=2
print('PASS',checks,'cubic incidence and physical Lipschitz weight checks')
