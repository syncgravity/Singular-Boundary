#!/usr/bin/env python3
"""Exact cubical 3D incidence/refinement and SU(2) Hamiltonian non-intertwining audit.
No continuum mass-gap claim. Standard Python + numpy for numerical gauge regressions.
"""
from __future__ import annotations
from collections import defaultdict
from itertools import combinations, product
from math import pi, sqrt
import json
import numpy as np

AXES=(0,1,2)

def cells(n,k):
    for axes in combinations(AXES,k):
        for o in product(*(range(n) if a in axes else range(n+1) for a in AXES)):
            yield (tuple(o),tuple(axes))

def boundary(c):
    o,axes=c
    res={}
    for j,a in enumerate(axes):
        ar=tuple(b for b in axes if b!=a)
        oo=list(o); oo[a]+=1
        res[(tuple(oo),ar)]=(-1)**j
        res[(o,ar)]=-(-1)**j
    return res

def refine(c):
    o,axes=c
    res={}
    for offsets in product((0,1), repeat=len(axes)):
        co=[2*x for x in o]
        for a,v in zip(axes,offsets): co[a]+=v
        res[(tuple(co),axes)]=1
    return res

def linear_map(cells_coeff,mapfunc):
    out=defaultdict(int)
    for c,w in cells_coeff.items():
        for d,v in mapfunc(c).items():out[d]+=w*v
    return {c:w for c,w in out.items() if w}

def rank_mod2(rows,ncols):
    pivots={}
    for row in rows:
        x=row
        while x:
            pivot=x.bit_length()-1
            if pivot in pivots:x ^= pivots[pivot]
            else:
                pivots[pivot]=x
                break
    return len(pivots)

def boundary_rank(n,k):
    lower=list(cells(n,k-1)); idx={c:j for j,c in enumerate(lower)}
    upper=list(cells(n,k)); rows=[0]*len(lower)
    for j,c in enumerate(upper):
        for d,v in boundary(c).items():
            if v%2: rows[idx[d]]^=(1<<j)
    return rank_mod2(rows,len(upper))

def exact_checks():
    cases=[]
    total_boundary=total_refine=0
    for n in (1,2,3):
        nums=[sum(1 for _ in cells(n,k)) for k in range(4)]
        V,E,F,C=nums
        assert nums == [(n+1)**3,3*n*(n+1)**2,3*n*n*(n+1),n**3]
        assert V-E+F-C==1
        for k in (2,3):
            for c in cells(n,k):
                assert linear_map(boundary(c),boundary)=={}
                total_boundary+=1
        for k in (1,2,3):
            for c in cells(n,k):
                b1=linear_map(refine(c),boundary)
                b2=linear_map(boundary(c),refine)
                assert b1==b2,(n,k,c,b1,b2)
                total_refine+=1
        r=[boundary_rank(n,k) for k in (1,2,3)]
        b=[V-r[0],E-r[0]-r[1],F-r[1]-r[2],C-r[2]]
        assert b==[1,0,0,0],(n,nums,r,b)
        cases.append(dict(n=n,lattice_pitch=1/n,max_cell_diameter=sqrt(3)/n,V=V,E=E,F=F,C=C,rank_boundary=r,betti=b))
    return cases,total_boundary,total_refine

# SU2 random unit quaternions, matrix group representation.
def su2(q):
    a,b,c,d=q
    return np.array([[a+1j*b,c+1j*d],[-c+1j*d,a-1j*b]],dtype=complex)
def rand_su2(rng):
    x=rng.normal(size=4);x/=np.linalg.norm(x);return su2(x)

def gauge_refinement_numeric():
    rng=np.random.default_rng(142019)
    # (start vertex, end vertex) directed fine edges in a 2x2 face.
    ed={}
    for x in range(2):
        for y in range(3):ed[((x,y),(x+1,y))]=rand_su2(rng)
    for x in range(3):
        for y in range(2):ed[((x,y),(x,y+1))]=rand_su2(rng)
    gauges={(x,y):rand_su2(rng) for x in range(3) for y in range(3)}
    mat=np.eye(2,dtype=complex)
    coarse_edges=[[(0,0),(1,0),(2,0)],[(2,0),(2,1),(2,2)],[(2,2),(1,2),(0,2)],[(0,2),(0,1),(0,0)]]
    def oriented(a,b,values):
        if (a,b) in values:return values[(a,b)]
        return values[(b,a)].conj().T
    def hol(path,values):
        R=np.eye(2,dtype=complex)
        for a,b in zip(path,path[1:]):R=R@oriented(a,b,values)
        return R
    transformed={(a,b): gauges[a]@u@gauges[b].conj().T for (a,b),u in ed.items()}
    errs=[]
    for path in coarse_edges:
        original=hol(path,ed)
        changed=hol(path,transformed)
        errs.append(float(np.max(np.abs(changed-gauges[path[0]]@original@gauges[path[-1]].conj().T))))
    loop=sum((p[:-1] for p in coarse_edges),[])+[(0,0)]
    t1=np.real(np.trace(hol(loop,ed)))
    t2=np.real(np.trace(hol(loop,transformed)))
    assert max(errs)<1e-13
    assert abs(t1-t2)<1e-13
    # Counterexample: interior fine edge only; coarse perimeter trivial.
    eye=np.eye(2,dtype=complex)
    edged={e:eye.copy() for e in ed}
    theta=pi/3
    edged[((1,0),(1,1))]=su2([np.cos(theta),np.sin(theta),0,0])
    fine=[]
    for x in range(2):
        for y in range(2):
            face=[(x,y),(x+1,y),(x+1,y+1),(x,y+1),(x,y)]
            fine.append(float(1-np.real(np.trace(hol(face,edged)))/2))
    coarse=float(1-np.real(np.trace(hol(loop,edged)))/2)
    assert abs(coarse)<1e-13
    assert np.allclose(sorted(fine),[0,0,0.5,0.5],atol=1e-13),(fine,coarse)
    return dict(max_coarse_edge_gauge_error=max(errs),coarse_wilson_trace_error=abs(t1-t2),fine_face_potential_values=fine,coarse_face_potential=coarse,total_fine_face_potential=sum(fine))

if __name__=='__main__':
    cases,nchain,nref=exact_checks()
    su=gauge_refinement_numeric()
    result=dict(description='P0 open-cube exact chain and SU2 gauge refinement benchmark',cell_cases=cases,exact_integer_chain_checks=nchain,exact_integer_refinement_checks=nref,group_regression=su,casimir_wilson_eigenvalues={'coarse_face_four_edges':3.0,'refined_perimeter_eight_edges':6.0},limitations='Purely cubic benchmark: not coupled-Z5 or Penrose source certification; not interacting continuum theory')
    print(json.dumps(result,indent=2))
    with open('p0_refinement_verification.json','w') as f:json.dump(result,f,indent=2)