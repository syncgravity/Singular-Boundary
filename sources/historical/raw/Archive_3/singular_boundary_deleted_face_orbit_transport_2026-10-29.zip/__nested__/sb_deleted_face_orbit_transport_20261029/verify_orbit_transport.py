#!/usr/bin/env python3
"""Deterministic SU(2) gauge-orbit dual-path transport certificate.
No sampling; fixed irrational-angle link matrices and exact graph incidence.
"""
import numpy as np
from collections import defaultdict, deque
from itertools import permutations, combinations

sigmax=np.array([[0,1],[1,0]],complex)
sigmay=np.array([[0,-1j],[1j,0]],complex)
sigmaz=np.array([[1,0],[0,-1]],complex)
I=np.eye(2,dtype=complex)

def su2(k):
    axis=np.array([np.sin(0.73+k),np.cos(1.21+2*k),np.sin(0.61+3*k)],float)
    axis=axis/np.linalg.norm(axis)
    th=0.21+0.057*(k%13)
    return np.cos(th)*I+1j*np.sin(th)*(axis[0]*sigmax+axis[1]*sigmay+axis[2]*sigmaz)

def build(faces):
    faces=[list(f) for f in faces]
    edgemap=defaultdict(list); edge_set=set()
    for idx,face in enumerate(faces):
        for a,b in zip(face,face[1:]+face[:1]):
            e=tuple(sorted((a,b)))
            edge_set.add(e); edgemap[e].append(idx)
    for e,inc in edgemap.items():assert len(inc)<=2
    return faces,sorted(edge_set),edgemap

def word(face,links):
    P=I.copy()
    for a,b in zip(face,face[1:]+face[:1]):
        e=tuple(sorted((a,b))); P=P@(links[e] if (a,b)==e else links[e].conj().T)
    return P

def solve_adjust_edge(face,edge,W_original,links):
    edges=[(tuple(sorted((a,b))),(a,b)==tuple(sorted((a,b)))) for a,b in zip(face,face[1:]+face[:1])]
    j=next(k for k,(e,_) in enumerate(edges) if e==edge)
    A=I.copy();B=I.copy()
    for e,forward in edges[:j]:A=A@(links[e] if forward else links[e].conj().T)
    for e,forward in edges[j+1:]:B=B@(links[e] if forward else links[e].conj().T)
    X=A.conj().T@W_original@B.conj().T
    links[edge]=X if edges[j][1] else X.conj().T

def transport(faces,edge_faces,links,path,R):
    """path = faces [target, next, ..., last, None] ending at exterior."""
    originals=[word(f,links) for f in faces]
    out={e:U.copy() for e,U in links.items()}
    crossed=[]
    for i in range(len(path)-1):
        a,b=path[i:i+2]
        if b is None: candidates=[e for e,inc in edge_faces.items() if inc==[a]]
        else: candidates=[e for e,inc in edge_faces.items() if sorted(inc)==sorted([a,b])]
        assert len(candidates)>0,(a,b)
        e=candidates[0]
        crossed.append(e)
        if i==0:out[e]=R@out[e]
        else:solve_adjust_edge(faces[a],e,originals[a],out)
    assert len(set(crossed))==len(crossed)
    errors=[np.linalg.norm(word(f,out)-originals[j]) for j,f in enumerate(faces)]
    assert max(e for i,e in enumerate(errors) if i!=path[0])<4e-12,errors
    for e in edge_faces:
        if e not in crossed:assert np.linalg.norm(out[e]-links[e])<1e-14
    return out,crossed,errors

def dual_distance(edgemap,nf,target):
    graph=defaultdict(set)
    outside=nf
    for e,inc in edgemap.items():
        if len(inc)==2:a,b=inc
        else:a,b=inc[0],outside
        graph[a].add(b);graph[b].add(a)
    q=deque([(target,0)]);seen={target}
    while q:
        u,d=q.popleft()
        if u==outside:return d
        for v in graph[u]:
            if v not in seen:seen.add(v);q.append((v,d+1))
    raise ValueError('disconnected dual')

def grid(n):
    faces=[]
    for i in range(n):
        for j in range(n):
            faces.append([(i,j),(i,j+1),(i+1,j+1),(i+1,j)])
    return faces

def penrose_seed():
    raw=[
    [(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
    [(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
    [(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
    def adjacent(a,b):return sum(abs(x-y) for x,y in zip(a,b))==1
    out=[]
    for f in raw:
        for perm in permutations(f[1:]):
            seq=[f[0],*perm]
            if all(adjacent(a,b) for a,b in zip(seq,seq[1:]+seq[:1])):
                out.append(seq);break
        else:raise ValueError('no perimeter')
    return out

# The center twists are all the fixed -I left/right multiplications:
for label,n,face_list,path in [('grid3',3,grid(3),[4,1,None]),('grid5',5,grid(5),[12,7,2,None]),('grid7',7,grid(7),[24,17,10,3,None]),('penrose3',0,penrose_seed(),[0,1,None])]:
    faces,edges,inc=build(face_list)
    links={e:su2(i) for i,e in enumerate(edges)}
    assert len(edges)==(2*n*(n+1)) if n else len(edges)==10
    if not n:assert len(faces)==3
    for Rtag,R in [('noncentral',su2(41)),('center',-I)]:
        moved,crossed,errors=transport(faces,inc,links,path,R)
        d=dual_distance(inc,len(faces),path[0]);assert d<=len(crossed)
        if n:assert d==n//2+1
        if Rtag=='center':
            assert all(np.linalg.norm(moved[e]+links[e])<2e-12 for e in crossed)
        print(label,Rtag,'faces',len(faces),'edges',len(edges),'dual minimum',d,
              'path',len(crossed),'non-target holonomy max residual',round(max(err for k,err in enumerate(errors) if k!=path[0]),14))

# Exact noncentral electric-isometry obstruction: z^{-1}R^{-1}zy depends on z.
X=1j*sigmax;R=su2(42)
yprime0=R.conj().T
comm=R.conj().T@X-X@R.conj().T
assert np.linalg.norm(comm)>0.1
assert np.linalg.norm((-I)@X-X@(-I))<1e-13
print('noncentral electric derivative obstruction Frobenius norm:',round(np.linalg.norm(comm),8))
print('PASS SU2 nonabelian dual-path, preserved other holonomies, dual minimal length, center parity and electric obstruction')
# Infinitesimal SU2 collective transport: each crossed edge has one unit-speed group rotation.
faces,edges,inc=build(grid(7));links={e:su2(k) for k,e in enumerate(edges)}
path=[24,17,10,3,None];eps=1.e-6
Plus,crossed,_=transport(faces,inc,links,path,np.cos(eps)*I+1j*np.sin(eps)*sigmaz)
Minus,_,_=transport(faces,inc,links,path,np.cos(eps)*I-1j*np.sin(eps)*sigmaz)
for e in crossed:
  deriv=(Plus[e]-Minus[e])/(2*eps)
  assert abs(np.linalg.norm(deriv)-np.sqrt(2))<1e-7,(e,np.linalg.norm(deriv))
print('PASS collective path generator has one SU2 generator per crossed edge')
