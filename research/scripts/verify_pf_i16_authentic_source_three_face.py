#!/usr/bin/env python3
"""PF-I16: reproduce all eight ORIGINAL source population counts, accepted-face incidence, and genuine three-face witness.
Independent reimplementation from indexed private paper6_extend_local.py and public PF-I11 verifier.
The original SHA-pinned private source bytes are NOT directly executed here.
"""
import itertools
from collections import defaultdict, Counter
import numpy as np
from scipy.spatial import ConvexHull
TH=2*np.pi*np.arange(5)/5
PAR=np.stack((np.cos(TH),np.sin(TH)),axis=1)
PERP=np.stack((np.cos(2*TH),np.sin(2*TH)),axis=1)
gamma=np.array([(j*np.sqrt(2)+j*j*np.sqrt(3))%1 for j in range(5)])
gamma-=gamma.mean(); gamma[4]=-gamma[:4].sum()
U=np.eye(5,dtype=int)
TR={}
for j,k in itertools.combinations(range(5),2):
    free=[a for a in range(5) if a not in (j,k)]
    for h in (1,2):
        pts=np.array([PERP[list(c)].sum(axis=0) for c in itertools.combinations(free,h)])
        TR[j,k,h]=ConvexHull(pts).equations
def accepted(m,j,k):
    h=sum(m)
    if h not in (1,2):return False
    eq=TR[j,k,h]; x=(np.asarray(m)+gamma)@PERP
    return np.max(x@eq[:,:2].T+eq[:,2])<-1e-9
def replay(N):
    vd={};tiles=[]
    for j,k in itertools.combinations(range(5),2):
        a,b=PAR[j],PAR[k];det=a[0]*b[1]-a[1]*b[0]
        for nj in range(-N,N+1):
            for nk in range(-N,N+1):
                bj=nj+gamma[j];bk=nk+gamma[k]
                point=np.array([(bj*b[1]-bk*a[1])/det,(a[0]*bk-bj*b[0])/det])
                base=[0]*5
                for f in range(5):
                    if f not in (j,k):
                        base[f]=int(np.ceil(point@PAR[f]-gamma[f]-1e-9))
                corners=[]
                for dj in (0,1):
                    for dk in (0,1):
                        m=base.copy();m[j]=nj+dj;m[k]=nk+dk
                        corners.append(tuple(m))
                if any(not 1<=sum(m)<=4 for m in corners):continue
                for m in corners:vd.setdefault(m,np.asarray(m)@PAR)
                tiles.append((corners[0],corners[2],corners[3],corners[1]))
    center=np.mean(list(vd.values()),axis=0)
    centers=np.array([np.mean([vd[m] for m in t],axis=0) for t in tiles])
    dist=np.linalg.norm(centers-center,axis=1)
    interior=set(np.flatnonzero(dist<.35*dist.max()))
    vtiles=defaultdict(list)
    for idx,t in enumerate(tiles):
        for v in t:vtiles[v].append(idx)
    selected={v for v,ix in vtiles.items() if all(i in interior for i in ix)}
    E=sum(tuple(np.asarray(m)+U[j]) in selected for m in selected for j in range(5))
    faces=[];counts=Counter()
    for m in sorted(selected):
        a=np.asarray(m)
        for j,k in itertools.combinations(range(5),2):
            b=tuple(a+U[j]);c=tuple(a+U[j]+U[k]);d=tuple(a+U[k])
            if not (b in selected and c in selected and d in selected):continue
            if not accepted(m,j,k):continue
            v=(m,b,c,d);faces.append((m,j,k))
            for x,y in zip(v,v[1:]+v[:1]):counts[frozenset((x,y))]+=1
    witness=[((0,1,0,0,0),2,3),((0,1,0,0,0),3,4),((0,1,0,0,1),0,3)]
    assert set(witness)<=set(faces)
    assert max(counts.values())<=2
    return len(selected),E,len(faces),max(counts.values())
if __name__=='__main__':
    ref={7:(1550,3017,1468),10:(3042,5927,2886),12:(4324,8468,4145),
         15:(6980,13779,6800),18:(9950,19593,9646),20:(12207,24091,11879),
         23:(16435,32582,16138),25:(19260,38139,18874)}
    for N,target in ref.items():
        result=replay(N)
        assert result[:3]==target,(N,result,target)
        print('N=',N,'V,E,F=',target,'max genuine faces/original link=',result[3],flush=True)
    print('PASS: all eight original source counts; accepted trivalent witness; incidence at most two')
