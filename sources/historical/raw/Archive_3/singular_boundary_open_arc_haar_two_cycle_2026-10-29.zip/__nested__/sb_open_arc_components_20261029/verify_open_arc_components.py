#!/usr/bin/env python3
"""Exact planar face-component/open-arc topology audit and finite-group Haar orbit check.
Does not diagonalize an SU(2) Hamiltonian; the open-arc theorem is analytic.
"""
from collections import defaultdict, deque
from itertools import product
from fractions import Fraction

CENT=(0,0)
def geometry(squares):
    assert CENT in squares
    fs={};eds=defaultdict(list)
    for c in squares:
        x,y=c; v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
        fs[c]=v
        for a,b in zip(v,v[1:]+v[:1]):eds[tuple(sorted([a,b]))].append(c)
    for e,inc in eds.items():assert len(inc)<=2,(e,inc)
    graph={c:set() for c in squares}
    for inc in eds.values():
        if len(inc)==2:
            a,b=inc;graph[a].add(b);graph[b].add(a)
    assert len(graph[CENT])==4,'central face must have four neighbors'
    remain={c for c in squares if c!=CENT}
    components=[]
    while remain:
        origin=min(remain);q=[origin];remain.remove(origin);cc={origin}
        for a in q:
            for b in graph[a]:
                if b in remain:remain.remove(b);cc.add(b);q.append(b)
        components.append(cc)
    f=fs[CENT];colors=[]
    for e0,e1 in zip(f,f[1:]+f[:1]):
        inc=eds[tuple(sorted([e0,e1]))];assert len(inc)==2
        neigh=[c for c in inc if c!=CENT][0]
        colors.append(next(i for i,comp in enumerate(components) if neigh in comp))
    arcs=[]
    for i,comp in enumerate(components):
        support=[k for k,c in enumerate(colors) if c==i]
        if support and len(support)<4:
            # Count transitions in the cyclic binary mask; a proper contiguous arc has exactly two.
            mask=[c==i for c in colors]
            transitions=sum(mask[k]!=mask[(k+1)%4] for k in range(4))
            if transitions==2:arcs.append(support)
    bridges=[]
    for near in graph[CENT]:
        q=[CENT];seen={CENT}
        for a in q:
            for b in graph[a]:
                if (a==CENT and b==near) or (a==near and b==CENT):continue
                if b not in seen:seen.add(b);q.append(b)
        if near not in seen:bridges.append(near)
    return components,colors,arcs,bridges,len(eds)

plus={CENT,(1,0),(-1,0),(0,1),(0,-1)}
seven=plus|{(1,1),(-1,-1)}
full={(x,y) for x in (-1,0,1) for y in (-1,0,1)}
for name,config in [('five-face star',plus),('seven-face two-cycle',seven),('full three-by-three',full)]:
    comps,colors,arcs,bridges,nedge=geometry(config)
    print(name,'faces',len(config),'edges',nedge,'remaining components',len(comps),
          'target colors',colors,'open arcs',arcs,'incident dual bridges',bridges)
    if name=='seven-face two-cycle':
        assert len(comps)==2 and len(arcs)==2
        assert sorted(len(a) for a in arcs)==[2,2]
        assert not bridges, 'strict extension beyond dual-bridge cases'
    if name=='full three-by-three':
        assert len(comps)==1 and len(arcs)==0 and len(bridges)==0
    if name=='five-face star':
        assert len(comps)==4 and len(arcs)==4 and len(bridges)==4

# Exact non-Abelian quaternion group Q8: verify product of any independent Haar
# variable with an arbitrary other factor is Haar, and a gauge-open-path orbit is transitive.
mult=[[0]*8 for _ in range(8)]
for a,b in product(range(8),repeat=2):
    ia,ib=a//2,b//2;sa=(-1)**(a%2);sb=(-1)**(b%2)
    if ia==0:ic=ib;sg=1
    elif ib==0:ic=ia;sg=1
    elif ia==ib:ic=0;sg=-1
    elif (ia,ib) in [(1,2),(2,3),(3,1)]:ic=6-ia-ib;sg=1
    else:ic=6-ia-ib;sg=-1
    mult[a][b]=2*ic+int(sa*sb*sg<0)
inv=[0,1,3,2,5,4,7,6]
for a,b,c in product(range(8),repeat=3):assert mult[mult[a][b]][c]==mult[a][mult[b][c]]
for a in range(8):assert mult[a][inv[a]]==0
for right in range(8):
    assert sorted(mult[left][right] for left in range(8))==list(range(8))
# A nontrivial positive, gauge-invariant closed-loop weight depending on non-Abelian holonomy.
weights={w:Fraction(1)+Fraction(1,3)*(w==0)+Fraction(1,5)*(w==1) for w in range(8)}
# UV is an open 2-edge arc and W closes it; integrated loop weight cannot depend on UV.
arc_weight={x:sum((weights[mult[x][w]] for w in range(8)),Fraction(0)) for x in range(8)}
assert len(set(arc_weight.values()))==1
print('Q8 non-Abelian Haar path orbit: eight values equiprobable after integrating closed-loop environment')
print('PASS: exact face incidence, two-cycle non-bridge extension, open-arc Haar transport')
