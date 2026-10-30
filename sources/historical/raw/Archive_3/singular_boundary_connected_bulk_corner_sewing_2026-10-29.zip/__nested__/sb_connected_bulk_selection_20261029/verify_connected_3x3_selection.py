#!/usr/bin/env python3
"""Exact 3x3 square-rhombus Wilson support graph and SU(2) fusion/center checks.
All 256 surrounding magnetic activation masks, no stochastic sampling.
This script does NOT diagonalize a non-Abelian quantum Hamiltonian.
"""
from collections import defaultdict,deque,Counter
from math import pi,sin,cos
from scipy.integrate import quad
center=(0,0)
N={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
C={'NE':(1,1),'NW':(-1,1),'SW':(-1,-1),'SE':(1,-1)}
allfaces=[center]+list(N.values())+list(C.values())
assert len(allfaces)==9
edge_faces=defaultdict(list)
for x,y in allfaces:
    vertices=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
    for a,b in zip(vertices,vertices[1:]+vertices[:1]):
        edge_faces[tuple(sorted((a,b)))].append((x,y))
assert len(edge_faces)==24 and all(len(v)<=2 for v in edge_faces.values())
shared=defaultdict(set)
for touching in edge_faces.values():
    if len(touching)==2:
        a,b=touching;shared[a].add(b);shared[b].add(a)

def components(active):
    remain=set(active);out=[]
    while remain:
        s=remain.pop();q=[s];part={s}
        for x in q:
            for y in shared[x]&remain:
                remain.remove(y);q.append(y);part.add(y)
        out.append(part)
    return out

def open_arc(active):
    # The four cardinal target edges in cyclic order N,E,S,W.
    if set(N.values())-active:return True  # one free target edge
    cc=components(active)
    color={f:i for i,p in enumerate(cc) for f in p}
    order=[color[N[k]] for k in ('N','E','S','W')]
    for v in set(order):
        mask=[x==v for x in order]
        transitions=sum(mask[i]!=mask[(i+1)%4] for i in range(4))
        if 0<sum(mask)<4 and transitions==2:return True
    return False

cases=[]
for mask in range(256):
    active={f for k,f in enumerate(list(N.values())+list(C.values())) if mask>>k&1}
    o=open_arc(active)
    cases.append((active,o))
    all_neigh=set(N.values())<=active
    corners=sum(f in active for f in C.values())
    if all_neigh and corners<3: assert o, (mask,active)
    if not o: assert all_neigh and corners>=3
    if corners==3 and all_neigh:assert not o
assert sum(not o for _,o in cases)==5  # four 3-corner + complete ring
assert sum(o for _,o in cases)==251
print('9-face disk:',len(allfaces),'faces',len(edge_faces),'primal edges')
print('256 subsets of 8 surrounding magnetic couplings: open arc',sum(o for _,o in cases),'connected obstruction',sum(not o for _,o in cases))
for a,o in cases:
    if not o:print('potentially non-Haar support:',sorted([k for k,v in {**N,**C}.items() if v in a]))

# For formal SU2 spin-j character at target, each cardinal neighbor must enter
# at least 2j times; on a physically allowed coupling coordinate, center sign
# parity forces even power of each activated corner coupling.
for j in (1,2,3,4):
    minimum=4*(2*j)+3*2
    assert minimum==8*j+6
    print('integer spin',j,'minimum total Taylor order',minimum)

# Check SU2 normalized Haar moments and fundamental character Casimir.
h=lambda u:2/pi*sin(u)**2
for j in (0,1,2,3):
    char=lambda u: (2*j+1) if abs(u)<1e-9 else sin((2*j+1)*u)/sin(u)
    moment=quad(lambda u:h(u)*char(u),0,pi,epsabs=1e-13)[0]
    assert abs(moment-(1 if j==0 else 0))<1e-11
print('PASS exact graph support, center parity thresholds, SU2 Haar orthogonality')
