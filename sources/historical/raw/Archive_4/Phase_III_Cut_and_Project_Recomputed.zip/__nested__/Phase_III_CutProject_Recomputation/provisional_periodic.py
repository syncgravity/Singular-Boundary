"""Rational pentagrid torus approximant with exact rank-two integer period quotient.
This is a rational multigrid approximant, not a Penrose substitution supertile.
"""
import numpy as np
from itertools import combinations
from collections import Counter
from pathlib import Path
import sys
from phase2 import Complex,build_edges

GAMMA=np.array([0.073,0.197,0.313,0.439,0.613])

def periodic(q=5, offset=0):
    ang=2*np.pi*np.arange(5)/5
    irr=np.column_stack((np.cos(ang),np.sin(ang)))
    a=np.rint(q*irr).astype(int)
    if len({tuple(x) for x in a})!=5:raise ValueError('q too small')
    normals=a/q
    gamma=(GAMMA+offset*np.array([.0413,.0271,.0719,.0337,.0531]))%1
    gamma=gamma+(1.-gamma.sum())/5.  # only normalizes offsets; rational directions are NOT Penrose
    # invariant quotient labels: k ~ k + m*a[:,0]+n*a[:,1]
    A=a.astype(float)
    pinv=np.linalg.pinv(A)
    def canonical(k):
        z=pinv@k
        shift=np.floor(z+1e-8).astype(int)
        return tuple((k-a@shift).tolist())
    labels=[]; ids={};faces=[];seen=set()
    def add(k):
        key=canonical(k)
        if key not in ids:ids[key]=len(labels);labels.append(key)
        return ids[key]
    # Crossing representatives in fundamental square 0<=x,y<q.
    for i,j in combinations(range(5),2):
        inv=np.linalg.inv(normals[[i,j]])
        lims=[]
        for h in (i,j):
            vals=[float(normals[h]@[x,y]-gamma[h]) for x in (0,q) for y in (0,q)]
            lims.append(range(int(np.floor(min(vals)))-1,int(np.ceil(max(vals)))+2))
        for p in lims[0]:
            for r in lims[1]:
                x=inv@np.array([p+gamma[i],r+gamma[j]])
                if not (-1e-8<=x[0]<q-1e-8 and -1e-8<=x[1]<q-1e-8):continue
                k=np.floor(normals@x-gamma+1e-9).astype(int);k[i]=p-1;k[j]=r-1
                face=[]
                for di,dj in [(0,0),(1,0),(1,1),(0,1)]:
                    h=k.copy();h[i]+=di;h[j]+=dj;face.append(add(h))
                if len(set(face))<4:continue
                sig=tuple(sorted(face))
                if sig not in seen:faces.append(tuple(face));seen.add(sig)
    xy=np.array([np.array(v)@normals for v in labels],float)
    return Complex(labels,xy,faces,build_edges(faces)),a

def check(g):
    counts=Counter(tuple(sorted((u,v))) for f in g.faces for u,v in zip(f,f[1:]+f[:1]))
    return dict(V=len(g.labels),E=len(g.edges),F=len(g.faces),chi=len(g.labels)-len(g.edges)+len(g.faces),edge_multiplicities=dict(Counter(counts.values())),quad=all(len(set(f))==4 for f in g.faces),degree=dict(Counter(Counter(u for e in g.edges for u in e).values())))
if __name__=='__main__':
 for q in (4,5,6,8,10,13):
  try:
   g,a=periodic(q);print(q,a.tolist(),check(g),flush=True)
  except Exception as e:print('ERR',q,repr(e),flush=True)

def topology(g):
    from collections import defaultdict,deque
    byedge=defaultdict(list)
    for i,f in enumerate(g.faces):
        for u,v in zip(f,f[1:]+f[:1]):
            a,b=sorted((u,v));byedge[(a,b)].append((i,1 if (u,v)==(a,b) else -1))
    if any(len(x)!=2 for x in byedge.values()):return {'manifold':False}
    constraints=defaultdict(list)
    for pair in byedge.values():
        (i,s),(j,t)=pair;constraints[i].append((j,-s*t));constraints[j].append((i,-s*t))
    sign={};orientable=True;components=0
    for i in range(len(g.faces)):
        if i in sign:continue
        components+=1;sign[i]=1;dq=deque([i])
        while dq:
            u=dq.popleft()
            for v,rel in constraints[u]:
                desired=sign[u]*rel
                if v not in sign:sign[v]=desired;dq.append(v)
                elif sign[v]!=desired:orientable=False
    return {'manifold':True,'orientable':orientable,'face_components':components,'torus_euler':len(g.labels)-len(g.edges)+len(g.faces)==0}
