#!/usr/bin/env python3
"""Exact local-environment proof checker for the H-3D Z5 model set.

Candidate displacements, window thresholds, phase partition, boundedness,
Voronoi vertices, facet incidences and covering-radius bound are checked in
Q(sqrt(5), sin(pi/5)) using exact rational arithmetic. NumPy/SciPy only propose
vertices and facets; every proposed item is reconstructed and checked exactly.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations, product
from math import sqrt
import numpy as np
import scipy
from scipy.spatial import ConvexHull, HalfspaceIntersection, QhullError

class Q5:
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o): o=q5(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(-q5(o))
    def __mul__(self,o):
        o=q5(o); return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=q5(o); den=o.a*o.a-5*o.b*o.b
        if den==0: raise ZeroDivisionError
        return Q5((self.a*o.a-5*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __eq__(self,o): o=q5(o); return self.a==o.a and self.b==o.b
    def sign(self):
        a,b=self.a,self.b
        if b==0:return (a>0)-(a<0)
        if a==0:return (b>0)-(b<0)
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        d=a*a-5*b*b; sd=(d>0)-(d<0)
        return sd if a>0 else -sd
    def val(self): return float(self.a)+float(self.b)*sqrt(5)
    def key(self): return (self.a.numerator,self.a.denominator,self.b.numerator,self.b.denominator)
    def __repr__(self): return f"({self.a})+({self.b})sqrt5"

def q5(x): return x if isinstance(x,Q5) else Q5(x,0)

S2=Q5(F(5,8),F(-1,8))
PHI=Q5(F(1,2),F(1,2))
class Q5S:
    """A + sin(pi/5)*C, with A,C in Q(sqrt(5))."""
    def __init__(self,a=0,c=0): self.a,self.c=q5(a),q5(c)
    def __add__(self,o): o=q5s(o); return Q5S(self.a+o.a,self.c+o.c)
    __radd__=__add__
    def __neg__(self): return Q5S(-self.a,-self.c)
    def __sub__(self,o): return self+(-q5s(o))
    def __mul__(self,o):
        o=q5s(o)
        return Q5S(self.a*o.a+S2*self.c*o.c,self.a*o.c+self.c*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=q5s(o); den=o.a*o.a-S2*o.c*o.c
        if den==0: raise ZeroDivisionError
        return Q5S((self.a*o.a-S2*self.c*o.c)/den,(self.c*o.a-self.a*o.c)/den)
    def __eq__(self,o): o=q5s(o); return self.a==o.a and self.c==o.c
    def sign(self):
        sa,sc=self.a.sign(),self.c.sign()
        if sa==0:return sc
        if sc==0:return sa
        if sa==sc:return sa
        cmp=(self.a*self.a-S2*self.c*self.c).sign()
        return cmp if sa>0 else -cmp
    def val(self): return self.a.val()+sqrt((5-sqrt(5))/8)*self.c.val()
    def key(self): return (self.a.key(),self.c.key())
    def __repr__(self): return f"({self.a})+s({self.c})"

def q5s(x): return x if isinstance(x,Q5S) else Q5S(x,0)
def cmp_exact(a,b): return (a-b).sign()
def zero(x): return x==Q5S(0,0)
def dot(a,b):
    z=Q5S(0,0)
    for x,y in zip(a,b): z=z+x*y
    return z

def solve(A,b):
    """Exact Gaussian elimination over Q(sqrt(5),sin(pi/5))."""
    n=len(A); M=[[q5s(x) for x in row]+[q5s(y)] for row,y in zip(A,b)]
    for k in range(n):
        pivot=next((i for i in range(k,n) if not zero(M[i][k])),None)
        if pivot is None:return None
        if pivot!=k:M[k],M[pivot]=M[pivot],M[k]
        p=M[k][k]; M[k]=[x/p for x in M[k]]
        for i in range(n):
            if i==k:continue
            f=M[i][k]
            if zero(f):continue
            M[i]=[x-f*y for x,y in zip(M[i],M[k])]
    return [M[i][-1] for i in range(n)]

C72=Q5(F(-1,4),F(1,4))
C144=Q5(F(-1,4),F(-1,4))

def invariants(d):
    norm1=Q5(sum(x*x for x in d),0)
    for j in range(5):
        for k in range(j+1,5):
            cc=C72 if (j-k)%5 in (1,4) else C144
            norm1=norm1+2*d[j]*d[k]*cc
    re2=Q5(d[0],0)+C144*(d[1]+d[4])+C72*(d[2]+d[3])
    b_int=Q5(d[1]-d[4],0)+PHI*(d[3]-d[2])
    v2=S2*b_int*b_int
    phys2=Q5(F(2,5),0)*(norm1+re2*re2)
    b_phys=PHI*(d[1]-d[4])+(d[2]-d[3])
    q=(Q5S(Q5(d[0],0)+C72*(d[1]+d[4])+C144*(d[2]+d[3]),0),
        Q5S(0,b_phys),Q5S(re2,0))
    qnorm=norm1+re2*re2
    return phys2,v2,b_int,q,qnorm

def candidate_displacements():
    out=[]; cutoff=Q5(F(6561,2500),0); vint=Q5(4,0)*PHI*PHI
    full_norm_bound=Q5(F(5,2),0)*cutoff+vint
    assert (full_norm_bound-Q5(25,0)).sign()<0
    for a,b,c,d in product(range(-4,5),repeat=4):
        e=-(a+b+c+d)
        if abs(e)>4:continue
        v=(a,b,c,d,e)
        if not any(v):continue
        p2,v2,B,q,norm=invariants(v)
        if (p2-cutoff).sign()<=0 and (v2-vint).sign()<=0:
            out.append((v,B,q,norm,p2))
    return sorted(out,key=lambda x:x[0])

def phase_partition(D):
    endpoints=[Q5S(-PHI,0),Q5S(PHI,0)]
    for _,B,_,_,_ in D:
        for A in (-PHI,PHI):
            t=Q5S(A,-B)
            if cmp_exact(t,endpoints[0])>0 and cmp_exact(t,endpoints[1])<0:
                endpoints.append(t)
    endpoints=sorted(endpoints,key=cmp_to_key(cmp_exact))
    unique=[]
    for t in endpoints:
        if not unique or t!=unique[-1]:unique.append(t)
    phases=list(unique)
    phases.extend((a+b)/Q5S(2,0) for a,b in zip(unique[:-1],unique[1:]))
    phases=sorted(phases,key=cmp_to_key(cmp_exact))
    return unique,phases

def accepted_neighbors(t,D):
    out=[]
    for d,B,q,norm,p2 in D:
        shifted=t+Q5S(0,B)
        if cmp_exact(shifted,Q5S(-PHI,0))>=0 and cmp_exact(shifted,Q5S(PHI,0))<=0:
            out.append((d,q,norm,p2))
    return out

def boundedness_witness(neighbors):
    qs=[x[1] for x in neighbors]
    for inds in combinations(range(len(qs)),4):
        A=[[qs[i][k] for i in inds] for k in range(3)]
        A.append([Q5S(1,0)]*4)
        lam=solve(A,[Q5S(0,0),Q5S(0,0),Q5S(0,0),Q5S(1,0)])
        if lam is not None and all(x.sign()>0 for x in lam):
            return inds,lam
    return None

def local_cell(neighbors):
    witness=boundedness_witness(neighbors)
    if witness is None:raise AssertionError("no positive tetrahedral normal witness")
    qs=[x[1] for x in neighbors]; norms=[x[2] for x in neighbors]
    qf=np.asarray([[x.val() for x in q] for q in qs],dtype=float)
    nf=np.asarray([x.val() for x in norms],dtype=float)
    halfspaces=np.column_stack([2*qf,-nf])
    try:
        approximate=HalfspaceIntersection(halfspaces,np.zeros(3))
        hull=ConvexHull(approximate.intersections)
    except QhullError as exc:
        raise AssertionError(f"Qhull failed despite exact boundedness witness: {exc}")
    vertices=[]
    for x0 in approximate.intersections:
        active=[i for i in range(len(qs)) if abs(2*np.dot(qf[i],x0)-nf[i])<1e-7]
        exact=None
        for inds in combinations(active,3):
            if abs(np.linalg.det(2*qf[list(inds)]))<1e-8:continue
            A=[[Q5S(2,0)*qs[i][k] for k in range(3)] for i in inds]
            b=[Q5S(norms[i],0) for i in inds]
            candidate=solve(A,b)
            if candidate is None:continue
            if all((Q5S(2,0)*dot(q,candidate)-Q5S(n,0)).sign()<=0 for q,n in zip(qs,norms)):
                xf=np.asarray([z.val() for z in candidate])
                if np.linalg.norm(xf-x0)<1e-7:
                    exact=candidate;break
        if exact is None:raise AssertionError("Qhull vertex failed exact reconstruction/feasibility")
        vertices.append(exact)
    unique={tuple(x.key() for x in v):v for v in vertices}
    V=list(unique.values())
    if len(V)!=len(approximate.intersections):raise AssertionError("duplicate Qhull vertices")
    for simplex in hull.simplices:
        tri=[V[int(i)] for i in simplex]
        if not any(all((Q5S(2,0)*dot(q,x)-Q5S(n,0)).sign()==0 for x in tri)
                   for q,n in zip(qs,norms)):
            raise AssertionError("convex-hull facet is not an original constraint plane")
    radius2=[Q5S(F(2,5),0)*(x[0]*x[0]+x[1]*x[1]+x[2]*x[2]) for x in V]
    maxr2=radius2[0]
    for r in radius2[1:]:
        if (r-maxr2).sign()>0:maxr2=r
    if (maxr2-Q5S(F(6561,10000),0)).sign()>=0:
        raise AssertionError(f"circumradius bound 0.81 failed: {maxr2}")
    facets=0
    for q,n in zip(qs,norms):
        on=[x for x in V if (Q5S(2,0)*dot(q,x)-Q5S(n,0)).sign()==0]
        if len(on)<3:continue
        found=False
        for i,j in combinations(range(1,len(on)),2):
            a=[on[i][k]-on[0][k] for k in range(3)]
            b=[on[j][k]-on[0][k] for k in range(3)]
            cross=(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
            if any(not zero(z) for z in cross):found=True;break
        if found:facets+=1
    return len(V),facets,maxr2,witness[0]

def main():
    D=candidate_displacements()
    assert len(D)==30,len(D)
    assert max(max(map(abs,d)) for d,_,_,_,_ in D)==1
    minp2=D[0][4]
    for *_,p2 in D:
        if (p2-minp2).sign()<0:minp2=p2
    expected=Q5(2,F(-4,5))
    assert minp2==expected,(minp2,expected)
    endpoints,phases=phase_partition(D)
    assert len(endpoints)==20 and len(phases)==39,(len(endpoints),len(phases))
    neighbor_counts=[];vertex_hist=Counter();facet_hist=Counter();joint_hist=Counter();maxr2=None;witnesses=0
    exact_r2=Q5S(Q5(F(173,200),F(-1,10)),0)
    for t in phases:
        N=accepted_neighbors(t,D);neighbor_counts.append(len(N))
        nv,nf,r2,wit=local_cell(N)
        assert r2==exact_r2,(t,r2,exact_r2)
        vertex_hist[nv]+=1;facet_hist[nf]+=1;joint_hist[(nf,nv)]+=1;witnesses+=1
        if maxr2 is None or (r2-maxr2).sign()>0:maxr2=r2
    assert min(neighbor_counts)==14 and max(neighbor_counts)==18
    assert vertex_hist==Counter({18:29,12:6,20:2,22:2}),vertex_hist
    assert facet_hist==Counter({12:28,8:6,14:5}),facet_hist
    print("P0-H3D exact local Voronoi certificate: PASS")
    print(f"numpy={np.__version__}; scipy={scipy.__version__} (used only to propose vertices/facets; exact checks follow)")
    print("exact displacement classes=30; exact window thresholds=20; exact phases=39")
    print(f"possible accepted neighbour count={min(neighbor_counts)}..{max(neighbor_counts)}")
    print(f"exact global separation squared >= {minp2}; distance >= sqrt(2-4*sqrt(5)/5)")
    print("exact global Voronoi covering-radius squared = 173/200 - sqrt(5)/10")
    print(f"exact Voronoi circumradius squared <= {maxr2} < 6561/10000 = (0.81)^2")
    print(f"exact facet histogram across phases={dict(sorted(facet_hist.items()))}")
    print(f"exact vertex histogram across phases={dict(sorted(vertex_hist.items()))}")
    print(f"joint facet/vertex histogram={dict(sorted(joint_hist.items()))}")
    print(f"boundedness witnesses={witnesses}/39 (positive tetrahedral combinations)")
    print("SCOPE: geometry of alternative H-3D model set only; no SU(2) dynamics or mass gap")

if __name__=="__main__":main()
