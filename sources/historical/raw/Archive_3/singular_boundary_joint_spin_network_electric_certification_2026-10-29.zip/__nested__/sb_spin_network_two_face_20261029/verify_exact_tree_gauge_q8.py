#!/usr/bin/env python3
"""Exact nonabelian Q8 control of spanning-tree gauge reduction on the minimal
8-face connected 3x3-minus-corner rhombus patch.

This finite-group test checks the algebra of the *continuous SU2* exact gauge
reduction, but Q8 is NOT SU2 and no physical SU2 8-face spectrum is computed.
"""
from collections import defaultdict, deque
from random import Random
import math

# quaternion group Q8: (sign bit, axis), axis 0=1, 1=i,2=j,3=k
# integer encoding 2*axis + sign bit
AX={ (1,2): (3,1), (2,3):(1,1), (3,1):(2,1),
     (2,1): (3,-1), (3,2):(1,-1), (1,3):(2,-1)}
def mul(x,y):
    a,sa=divmod(x,2); b,sb=divmod(y,2); sign=(-1)**(sa+sb)
    if a==0: z=b
    elif b==0: z=a
    elif a==b: z=0;sign=-sign
    else: z,sg=AX[a,b];sign*=sg
    return z*2+(0 if sign>0 else 1)
def inv(x):
    a,s=divmod(x,2)
    return x if a==0 else x^1
ONE=0; NEGONE=1
S=(2,3,4,5,6,7)
assert all(mul(x,inv(x))==ONE for x in range(8))
assert all(mul(mul(x,y),z)==mul(x,mul(y,z)) for x in range(8) for y in range(8) for z in range(8))
def char(x):
    if x==0:return 1.
    if x==1:return -1.
    return 0.

# 3x3 patch with corner (0,0) removed: 8 plaquettes; f=(1,1) interior
F=sorted([(x,y) for x in range(3) for y in range(3) if (x,y)!=(0,0)])
TARGET=(1,1)
def fvs(f):
    x,y=f
    return [(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
ED=set()
for f in F:
    vs=fvs(f)
    for a,b in zip(vs,vs[1:]+vs[:1]): ED.add(tuple(sorted((a,b))))
ED=sorted(ED);V=sorted({p for a,b in ED for p in (a,b)})
assert len(F)==8 and len(ED)==22 and len(V)==15
EID={e:i for i,e in enumerate(ED)}
A=defaultdict(list)
for a,b in ED:
    A[a].append(b);A[b].append(a)
root=(3,3);parent={root:None};queue=deque([root])
while queue:
    v=queue.popleft()
    for w in sorted(A[v]):
        if w not in parent:
            parent[w]=v;queue.append(w)
assert set(parent)==set(V)
TREE={tuple(sorted((v,p))) for v,p in parent.items() if p is not None}
CHORDS=[e for e in ED if e not in TREE]
assert len(TREE)==14 and len(CHORDS)==8
CHIDX={e:i for i,e in enumerate(CHORDS)}

def path_holonomies(U):
    P={root:ONE}
    q=deque([root])
    while q:
        v=q.popleft()
        for w in A[v]:
            if parent.get(w)!=v:continue
            e=tuple(sorted((v,w)));u=U[EID[e]]
            step=u if e==(v,w) else inv(u)
            P[w]=mul(P[v],step);q.append(w)
    return P

def reduction(U):
    P=path_holonomies(U)
    return tuple(mul(mul(P[a],U[EID[(a,b)]]),inv(P[b])) for a,b in CHORDS)

def make_link_state(X):
    return [ONE if e in TREE else X[CHIDX[e]] for e in ED]

def word_p(f,X):
    U=make_link_state(X);h=ONE
    v=fvs(f)
    for a,b in zip(v,v[1:]+v[:1]):
        e=tuple(sorted((a,b)));u=U[EID[e]]
        h=mul(h,u if e==(a,b) else inv(u))
    return h

def fullword(f,U):
    h=ONE;v=fvs(f)
    for a,b in zip(v,v[1:]+v[:1]):
        e=tuple(sorted((a,b)));u=U[EID[e]]
        h=mul(h,u if e==(a,b) else inv(u))
    return h

def gauge(U,g):
    return [mul(mul(g[a],U[EID[(a,b)]]),inv(g[b])) for a,b in ED]

def sub(v):
    return {w for w in V if w==v or any(parent.get(z)==w for z in [])} # replaced below

def descendants(v):
    out={v}
    for w in V:
        z=w
        while z!=root:
            if z==v:out.add(w);break
            z=parent[z]
    return out

def tree_predict(X,e,q):
    a,b=e
    child = a if parent.get(a)==b else b
    assert parent.get(child)==(b if child==a else a)
    p=parent[child]
    G=q if e==(p,child) else inv(q)
    Z=descendants(child)
    out=[]
    for s,t in CHORDS:
        x=X[CHIDX[(s,t)]]
        if s in Z:x=mul(G,x)
        if t in Z:x=mul(x,inv(G))
        out.append(x)
    return tuple(out)

def move_on_link(X,e,q):
    U=make_link_state(X)
    U[EID[e]]=mul(q,U[EID[e]])
    return reduction(U)

rng=Random(811)
# Validate gauge invariance and tree/chord generator conjugations.
for i in range(80):
    U=[rng.randrange(8) for _ in ED]
    g={v:rng.randrange(8) for v in V}
    X=reduction(U)
    Y=reduction(gauge(U,g))
    assert Y==tuple(mul(mul(g[root],x),inv(g[root])) for x in X)
    for f in F:
        assert char(fullword(f,U))==char(word_p(f,X))

for i in range(40):
    X=tuple(rng.randrange(8) for _ in CHORDS)
    for e in ED:
        for q in S:
            actual=move_on_link(X,e,q)
            if e in TREE:
                pred=tree_predict(X,e,q)
            else:
                pred=list(X);pred[CHIDX[e]]=mul(q,pred[CHIDX[e]])
                pred=tuple(pred)
            assert actual==pred,(e,q,actual,pred)

def phi(X):
    # independent traces of retained plaquette words + genuine connected products
    v=[char(word_p(f,X)) for f in F]
    return (0.17*sum((j+1)*z for j,z in enumerate(v))+
            0.031*v[1]*v[4]+0.08*v[2]*v[6]*v[7])

def reduced_kinetic(X):
    # Exact finite-Q8 analogue of sum_e a_e (-Delta_e) in tree gauge
    summ=0.
    for index,e in enumerate(ED):
        a=.65+(index%7)*.12
        summ+=a*(phi(X)-sum(phi(move_on_link(X,e,q)) for q in S)/len(S))
    return summ

# Original-link kinetic acting on gauge-invariant pullback Phi(U)=phi(reduction(U)).
for i in range(35):
    X=tuple(rng.randrange(8) for _ in CHORDS)
    U=make_link_state(X)
    orig=0.
    for index,e in enumerate(ED):
        a=.65+(index%7)*.12
        terms=[]
        for q in S:
            U2=U.copy();U2[EID[e]]=mul(q,U2[EID[e]])
            terms.append(phi(reduction(U2)))
        orig+=a*(phi(reduction(U))-sum(terms)/len(S))
    assert abs(orig-reduced_kinetic(X))<1e-10

# Exact target-center flux: choose dual path (center -> top center -> exterior).
center_flip=[tuple(sorted(z)) for z in [((1,2),(2,2)),((1,3),(2,3))]]
for i in range(50):
    X=tuple(rng.randrange(8) for _ in CHORDS)
    U=make_link_state(X)
    Uf=U.copy()
    for e in center_flip: Uf[EID[e]]=mul(NEGONE,Uf[EID[e]])
    changed=[]
    for f in F:
        p=char(fullword(f,U));pp=char(fullword(f,Uf))
        if abs(pp-p)>1e-9:changed.append(f)
    # For imaginary Q8 elements p=0, so test group-valued center flip directly.
    for f in F:
        h=fullword(f,U);hf=fullword(f,Uf)
        assert hf==(mul(NEGONE,h) if f==TARGET else h)

print('PASS: 8-face nonabelian gauge-fixed tree model',len(V),'vertices,',len(ED),'edges,',len(CHORDS),'independent Q8 coordinates')
print('PASS: complete local kinetic generator exact after gauge reduction (22 edges); magnetic Wilson words; target center string')
print('LIMITATION: Q8 is a finite SU2 subgroup, not SU2 Haar or a nonperturbative solution of the eight-face SU2 spectral problem.')
