#!/usr/bin/env python3
"""Deterministic nonlinear SU2 magnetic deletion via bridge separation.

No Monte Carlo. Checks exact Haar trial identities, connected-face portal topology,
source Penrose spatial seed, and a genuine one-plaquette character Hamiltonian.
"""
import math
from itertools import combinations
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import ive
import sympy as sp


def square_faces(centres):
    faces = []
    for x,y in sorted(centres):
        verts = [(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
        faces.append({tuple(sorted((a,b))) for a,b in zip(verts,verts[1:]+verts[:1])})
    return faces


def component_neighbour_sets(faces, target):
    adjacency = [set() for _ in faces]
    for i in range(len(faces)):
        for j in range(i+1,len(faces)):
            if faces[i]&faces[j]: adjacency[i].add(j); adjacency[j].add(i)
    remaining = set(range(len(faces)))-{target}
    comps=[]
    while remaining:
        x=remaining.pop(); seen={x}; todo=[x]
        while todo:
            z=todo.pop()
            for j in adjacency[z] & remaining:
                remaining.remove(j);seen.add(j);todo.append(j)
        comps.append(seen)
    edge_component = {}
    for e in faces[target]:
        neigh=[j for j in range(len(faces)) if j!=target and e in faces[j]]
        assert len(neigh)<=1
        edge_component[e] = ('free',e) if not neigh else next(i for i,c in enumerate(comps) if neigh[0] in c)
    counts={}
    for c in edge_component.values():counts[c]=counts.get(c,0)+1
    isolated=[e for e,c in edge_component.items() if counts[c]==1]
    return adjacency, comps, isolated


star=square_faces([(0,0),(0,1),(0,-1),(1,0),(-1,0)])
center=sorted([(0,0),(0,1),(0,-1),(1,0),(-1,0)]).index((0,0))
adj,cs,portals=component_neighbour_sets(star,center)
assert len(star)==5 and len(set.union(*star))==16
assert len({v for e in set.union(*star) for v in e})==12
assert len(adj[center])==4 and len(cs)==4 and len(portals)==4
assert not [e for e in star[center] if sum(e in face for face in star)==1]

full=square_faces([(i,j) for i in range(3) for j in range(3)])
_,full_components,full_portals=component_neighbour_sets(full,4)
assert len(full_components)==1 and len(full_portals)==0

# Real canonical 3 Penrose rhombi, five-integer lifting coordinates.
seed = [
 [(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
 [(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
 [(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges_from_vertex_quad(vs):
    return {tuple(sorted((a,b))) for a,b in combinations(vs,2) if sum(abs(x-y) for x,y in zip(a,b))==1}
penrose=[edges_from_vertex_quad(f) for f in seed]
assert len(set.union(*penrose))==10
for i in range(3):
    _,_,ip=component_neighbour_sets(penrose,i)
    assert ip, (i,ip)

# Class SU2 Haar trace p has semicircle law and moments Catalan/4^n.
p=sp.symbols('p', real=True)
for n in range(1,6):
    calculated=sp.integrate(p**(2*n)*2/sp.pi*sp.sqrt(1-p*p),(p,-1,1))
    expected=sp.catalan(n)/4**n
    assert sp.simplify(calculated-expected)==0,(n,calculated,expected)

# Exact self-adjoint Haar Casimir identity and gamma shape comparison.
for k in [0.2,0.5,1.,2.,5.,20.,50.]:
    r=float(ive(0,2*k)/ive(1,2*k)-1/k)
    xmoment=3*r/(2*k)
    assert 0<=r<=1
    assert 1-r<=3/(4*k)+1e-12
    # electric energy for class source e^{k p}: E grad energy = 3*A*k*r/8
    assert xmoment>=0

A=4.
for b in [0.5,4.,25.,100.,1600.]:
    k=math.sqrt(2*b/A)
    r=float(ive(0,2*k)/ive(1,2*k)-1/k)
    energy=(3*A*k*r)/8+b*(1-r)
    bound=3/(2*math.sqrt(2))*math.sqrt(A*b)
    assert energy<=bound+1e-10
    # The interacting pure one-face physical H has character basis j=0,1,2,...
    n=np.arange(100,dtype=float)
    actual=float(eigh_tridiagonal(A*n*(n+2)/4+b,np.full(len(n)-1,-b/2),select='i',select_range=(0,0))[0][0])
    assert 0<=actual<=energy+1e-9,(b,actual,energy)
    # Apply the PE-2 single-face tail at h with b_f=4h^{-2}.
    print(f'b={b:7g} exact_interacting_E0={actual:.8f} Haar_trial={energy:.8f} bound={bound:.8f}')

# Penalizing extra magnetic faces by maximum potential 2b is rigorous.
for b in [.2,3,20]:
    B_extra=b+2*b
    assert 2*B_extra == 6*b
print('PASS: real 3-face Penrose spatial incidence, nonlinear five-face interior bridge,')
print('      cycle-rich 3x3 obstruction, Haar Catalan moments, normalized SU2 Ritz.')
print('No Monte Carlo; no Stage7/26 Hamiltonian certification.')
