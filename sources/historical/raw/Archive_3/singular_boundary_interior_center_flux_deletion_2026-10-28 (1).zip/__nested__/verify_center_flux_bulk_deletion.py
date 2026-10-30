#!/usr/bin/env python3
"""Center-vortex parity, physical SU2 Ritz, uniform Gaussian bulk deletion.
Deterministic exact finite-dimensional audits. No Monte Carlo.
"""
import itertools
from collections import defaultdict, deque
import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal


def edge(a,b):
    return tuple(sorted((a,b)))

def grid_faces(n):
    return [[(i,j),(i+1,j),(i+1,j+1),(i,j+1)] for i in range(n) for j in range(n)]

def penrose_seed():
    return [
       [(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
       [(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
       [(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)],
    ]

def directed_face(vertices):
    if len(vertices[0])==2:
        return vertices
    for perm in itertools.permutations(vertices[1:]):
        cyc=[vertices[0],*perm]
        if all(sum(abs(a-b) for a,b in zip(u,v))==1 for u,v in zip(cyc,cyc[1:]+cyc[:1])):
            return cyc
    raise AssertionError("face cannot be cyclically ordered")

def incidence(faces):
    cyc=[directed_face(face) for face in faces]
    E=sorted({edge(a,b) for f in cyc for a,b in zip(f,f[1:]+f[:1])})
    lookup={e:i for i,e in enumerate(E)}
    B=np.zeros((len(cyc),len(E)),dtype=int)
    for fi,f in enumerate(cyc):
        for u,v in zip(f,f[1:]+f[:1]):
            key=edge(u,v);B[fi,lookup[key]]=1 if (u,v)==key else -1
    return E,B

def dual_shortest_path(face_index,B):
    F,E=B.shape
    incident=[list(np.flatnonzero(B[:,j])) for j in range(E)]
    assert max(map(len,incident))<=2
    adj=defaultdict(list)
    for j,fl in enumerate(incident):
        if len(fl)==2:u,v=fl
        else:u,v=fl[0],F # exterior
        adj[u].append((v,j));adj[v].append((u,j))
    parent={face_index:None}; queue=deque([face_index])
    while queue and F not in parent:
        u=queue.popleft()
        for v,j in adj[u]:
            if v not in parent:parent[v]=(u,j);queue.append(v)
    assert F in parent
    path=[];cur=F
    while cur!=face_index:
        prev,j=parent[cur];path.append(j);cur=prev
    twist=np.zeros(E,dtype=int);twist[path]=1
    assert np.array_equal((abs(B)@twist)%2,np.eye(F,dtype=int)[face_index]);
    return len(path),twist

for faces,name in [(penrose_seed(),"Penrose Z5 spatial seed"),(grid_faces(5),"5x5 interior grid"),(grid_faces(10),"10x10 interior grid")]:
    E,B=incidence(faces);F=len(faces)
    assert len(E)==(10 if name.startswith('Penrose') else (2*int(F**.5)*(int(F**.5)+1)))
    idx=(int(F**.5)//2)*int(F**.5)+(int(F**.5)//2) if F>3 else F//2
    dist,twist=dual_shortest_path(idx,B)
    assert dist==(3 if F==25 else 5 if F==100 else 1) or F==3
    if F>3:
        assert np.count_nonzero(abs(B[idx]))==4
        assert all(np.count_nonzero(abs(B[:,j]))==2 for j in np.flatnonzero(B[idx]))
    print(f"PASS {name}: {F} faces, {len(E)} edges, center twist length {dist}")
    # A discrete center vortex is physical, not a vertex gauge transformation.
    assert np.count_nonzero((abs(B)@twist)%2)==1

b,a,v=sp.symbols('b a v',positive=True)
g=a*(1-v) # a here denotes A_f/4
R=b+(g/v-sp.sqrt((g/v)**2+4*b*b*v))/2
assert sp.simplify(R.subs(v,sp.Rational(1,4))- (b+(3*a-sp.sqrt(9*a*a+b*b))/2))==0
assert sp.simplify((2*v*v/g)-(2*v*v/(a*(1-v))))==0
print('PASS symbolic center-odd Ritz and susceptibility')

for bc in [0.1,1.0,5.0,20.0,100.0]:
    n=70;j=np.arange(n)
    # One face: four link electric coefficients a=1 -> -Delta_class coefficient 4
    # SU2 chars chi_(j/2) eigenvalue j(j+2)/4, so E_n=j(j+2)
    Eplus,_=eigh_tridiagonal(j*(j+2)+bc,np.full(n-1,-bc/2),select='i',select_range=(0,0))
    Eminus,_=eigh_tridiagonal(j*(j+2),np.full(n-1,+bc/2),select='i',select_range=(0,0))
    ground=float(Eplus[0]);even_shift=float(Eplus[0]-bc)
    assert abs(even_shift-float(Eminus[0]))<1e-10
    ritz=bc+(3-np.sqrt(9+bc*bc))/2
    assert 0<ground<=ritz+1e-9
    print(f'PASS nonlinear SU2 one-face b={bc:6.1f}: E0={ground:.9f}, Ritz={ritz:.9f}')

for n in [3,25,100]:
    faces=penrose_seed() if n==3 else grid_faces(round(n**.5))
    E,B=incidence(faces);F=B.shape[0]
    ae=0.6+0.25*(1+np.sin(np.arange(len(E))*.31))  # deterministic nonuniform weights
    M=(B*ae)@B.T
    assert np.linalg.eigvalsh(M)[0]>0
    weights=2.0+np.cos(np.arange(F)*.24)**2
    f=F//2
    base=(np.sqrt(M).shape[0] if False else 0) # no matrix elementwise sqrt used
    def energy(mags):
        w,U=np.linalg.eigh(M)
        root=(U*np.sqrt(w))@U.T
        Q=(root*mags[np.newaxis,:]/8)@root
        return 3*sum(np.sqrt(np.maximum(np.linalg.eigvalsh(Q),0)))
    Eall=energy(weights)
    reduced=weights.copy();reduced[f]=0.
    Edelete=energy(reduced)
    d=Eall-Edelete
    bound=3/np.sqrt(8)*np.sqrt(weights[f]*M[f,f])
    assert -1e-8<=d<=bound+1e-8
    print(f'PASS Gaussian {F}-face BULK deletion: increment={d:.9f}, bound={bound:.9f}')
print('PASS ALL deterministic physical center-flux / Gaussian rank-one checks; no Monte Carlo')
