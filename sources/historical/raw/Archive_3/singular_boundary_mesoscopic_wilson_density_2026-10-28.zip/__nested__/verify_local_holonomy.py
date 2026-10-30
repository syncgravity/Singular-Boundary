#!/usr/bin/env python3
"""Read-only exact rational checks for small Penrose Wilson boundaries.

No historical configuration changes, random fields, Monte Carlo or fit.
The three original canonical Q14 spatial seed rhombi are the fixture.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import json

faces_z5 = [
    [[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
    [[-1,-1,-1,-1,-1],[-1,-1,0,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1]],
    [[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]],
]

def adjacency_edges(vertices):
    vv=list(map(tuple,vertices))
    return {tuple(sorted((x,y))) for x,y in combinations(vv,2)
            if sum(abs(a-b) for a,b in zip(x,y))==1}

faces=[adjacency_edges(z) for z in faces_z5]
assert [len(f) for f in faces]==[4,4,4]
all_edges=sorted(set().union(*faces))
assert len(all_edges)==10
assert len(faces[0] & faces[1]) == len(faces[0] & faces[2]) == 1
assert not (faces[1] & faces[2])

# Enumerate all connected face sets. Their boundary edges form simple cycles.
connected=[]
for mask in range(1,1<<3):
    ids=[i for i in range(3) if mask>>i&1]
    found={ids[0]}
    while True:
        expand=found | {i for i in ids if any(faces[i]&faces[j] for j in found)}
        if expand==found:break
        found=expand
    if len(found)!=len(ids):continue
    edge_count=Counter(e for i in ids for e in faces[i])
    boundary={e for e,c in edge_count.items() if c==1}
    degree=Counter(v for e in boundary for v in e)
    assert set(degree.values())=={2}
    assert len(boundary)==2*len(ids)+2
    connected.append((ids,boundary))
assert len(connected)==6

zero=F(0); one=F(1)
def qmul(x,y):
    a,u=x[0],x[1:];b,v=y[0],y[1:]
    c=(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
    return (a*b-sum((w*z for w,z in zip(u,v)),zero),)+tuple(a*z+b*w-t for w,z,t in zip(u,v,c))

def qinv(q):return (q[0],)+tuple(-t for t in q[1:])
def d(q):return one-q[0]
E=(one,zero,zero,zero); X=(zero,one,zero,zero);Y=(zero,zero,one,zero);Z=(zero,zero,zero,one)
Q=[E,X,Y,Z,(F(3,5),F(4,5),zero,zero), (F(5,13),zero,F(12,13),zero)]
assert all(sum((w*w for w in q),zero)==1 for q in Q)

def cycle_holonomy(edges, assignment):
    ne=Counter(v for e in edges for v in e)
    assert len(edges)>0 and set(ne.values())=={2}
    # walk unique simple connected boundary cycle, starting at lex first vertex
    start=min(ne)
    cur=start; prev=None; word=E;steps=0
    while True:
        neighbors=sorted((b if a==cur else a) for a,b in edges if cur==a or cur==b)
        assert len(neighbors)==2
        nxt=next(v for v in neighbors if v!=prev) if prev is not None else neighbors[0]
        e=tuple(sorted((cur,nxt)))
        val=assignment[e]
        word=qmul(word,val if (cur,nxt)==e else qinv(val))
        steps+=1
        prev,cur=cur,nxt
        if cur==start:break
        assert steps <=len(edges)
    assert steps==len(edges)
    return word

max_gap=F(-100)
tests=0
for case in range(7):
    field={edge:Q[(ix*(case+1)+case*case+2*ix*ix)%len(Q)] for ix,edge in enumerate(all_edges)}
    ds=[d(cycle_holonomy(face,field)) for face in faces]
    assert all(F(0)<=z<=F(2) for z in ds)
    for ids,boundary in connected:
        actual=d(cycle_holonomy(boundary,field))
        upper=len(ids)*sum((ds[j] for j in ids),zero)
        assert actual <= upper, (case,ids,actual,upper)
        tests+=1
        max_gap=max(max_gap,actual-upper)

# The anchored-root incidence bound is finite graph combinatorics, independent of SU2.
patches=[{0,1},{0,1},{0,2}]
coverage=Counter(j for patch in patches for j in patch)
assert max(coverage.values())==3 <= 2*3**(2-1)-1
assert sum(len(p) for p in patches)==6

output={
    'canonical_seed_faces':3,'canonical_seed_links':10,'connected_disk_patches':len(connected),
    'boundary_lengths':{','.join(map(str,i)):len(b) for i,b in connected},
    'exact_rational_SU2_boundary_inequalities_checked':tests,
    'all_checks_passed':True,'max_actual_minus_upper':str(max_gap),
    'anchored_two_face_root_coverage':dict(coverage),
    'general_deficit_bound':'d(W_partial_Q) <= |Q| sum_{f in Q} d_f',
    'mesoscopic_GNS_norm_bound':'||(Wbar_D-1) Omega||^2 <= 2 k (2*3^(k-1)-1) delta_D',
    'any_monte_carlo':False,'any_nontrivial_spectral_gap_proved':False
}
print(json.dumps(output,indent=2))
