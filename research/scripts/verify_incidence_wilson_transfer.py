#!/usr/bin/env python3
"""Non-Abelian SU(2) incidence-weighted Wilson-flow transfer checks.

Finite non-Abelian tests: oriented tetrahedral surface + six faces of cube;
quaternion holonomies, signed face edges, left-invariant gradients via exact
quaternion tangent derivative (not a scalar/link-decoupled replacement).
This is a finite-regulator incidence control, NOT PF 3D SU(2) construction.
"""
import itertools
import math
import numpy as np

rng=np.random.default_rng(20261107)

def qm(a,b):
    return np.array([a[0]*b[0]-a[1:]@b[1:], *(a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:]))])

def conj(q):return q*np.array([1.,-1.,-1.,-1.])

def random_q():
    q=rng.normal(size=4)
    return q/np.linalg.norm(q)

def make_complex(verts,faces):
    e={}
    words=[]
    for f in faces:
        seq=[]
        for a,b in zip(f,f[1:]+f[:1]):
            key=tuple(sorted((a,b)))
            if key not in e:e[key]=len(e)
            seq.append((e[key],1 if a<b else -1))
        words.append(seq)
    edges=list(e)
    centers=np.array([np.mean(np.array([verts[x] for x in f],dtype=float),axis=0) for f in faces])
    return edges,words,centers

def eval_l_g(Q,words):
    F=len(words);E=len(Q)
    ell=np.zeros(F);grad=np.zeros((F,E,3));identity=np.array([1.,0.,0.,0.]);gen=np.eye(4)[1:,:]/2
    for p,word in enumerate(words):
        factors=[Q[e] if sign>0 else conj(Q[e]) for e,sign in word]
        pref=[identity]
        for x in factors:pref.append(qm(pref[-1],x))
        suff=[None]*(len(factors)+1);suff[-1]=identity
        for i in range(len(factors)-1,-1,-1):suff[i]=qm(factors[i],suff[i+1])
        ell[p]=1-pref[-1][0]
        for k,(edge,sign) in enumerate(word):
            for a,g in enumerate(gen):
                # left multiplication Q -> exp(t g) Q.
                d=qm(g,Q[edge])
                if sign<0:
                    # inverse(exp(t g)Q)=Q^{-1}exp(-t g)
                    d=-qm(conj(Q[edge]),g)
                grad[p,edge,a]+= -qm(qm(pref[k],d),suff[k+1])[0]
    return ell,grad

def one_trial(vertices,faces,h):
    edges,words,centers=make_complex(vertices,faces)
    P=len(words);E=len(edges)
    d=max(sum(any(j==e for j,_ in w) for w in words) for e in range(E))
    m=max(len(w) for w in words)
    kappa=max(np.linalg.norm(centers[p]-centers[q]) for p in range(P) for q in range(P) if p!=q and set(e for e,_ in words[p])&set(e for e,_ in words[q]))/h
    for iteration in range(100):
        Q=np.array([random_q() for _ in range(E)])
        ell,g=eval_l_g(Q,words)
        assert np.all(ell>=-1e-12) and np.all(ell<=2+1e-12)
        for p,w in enumerate(words):
            for e,_ in w:
                assert abs(g[p,e]@g[p,e] - ell[p]*(2-ell[p])/4)<5e-12,(p,e,g[p,e],ell[p])
        L=float(rng.uniform(.05,2.5))
        direction=rng.normal(size=3);direction/=np.linalg.norm(direction)
        # phi = L directional distance, exactly Lipschitz L
        w=np.exp(2*L*(centers@direction));ap=np.ones(P) if iteration%2==0 else rng.uniform(.15,2.0,size=P)
        F=np.einsum('p,pej->ej',ap,g);G=np.einsum('p,pej->ej',ap*w,g)
        we=np.array([max(w[p] for p,ww in enumerate(words) if any(x==e for x,_ in ww)) for e in range(E)])
        diss=-np.sum(G*F);dirichlet=.5*np.sum(we[:,None]*F*F)
        q=1-math.exp(-2*L*kappa*h)
        amax=max(sum(ap[p] for p,word in enumerate(words) if any(j==e for j,_ in word)) for e in range(E))
        exact_rhs=q*q*amax*m*math.exp(2*L*kappa*h)/4*np.sum(ap*w*ell)
        rhs=amax*m*kappa*kappa*L*L*h*h*math.exp(2*L*kappa*h)*np.sum(ap*w*ell)
        assert diss+dirichlet<=exact_rhs+1e-9,(diss,dirichlet,exact_rhs)
        assert exact_rhs<=rhs+1e-9
    return len(edges),P,d,m,round(kappa,8)

tetra={0:(0.,0.,0.),1:(1.,0.,0.),2:(0.,1.,0.),3:(0.,0.,1.)}
tetra_faces=[[0,2,1],[0,1,3],[0,3,2],[1,2,3]]
# All six faces of a unit cube, oriented boundaries; each edge belongs to 2 faces.
cube={i:tuple(float(z) for z in xyz) for i,xyz in enumerate(itertools.product((0,1),repeat=3))}
cube_faces=[]
for axis in range(3):
    for val in (0,1):
        group=[i for i,v in cube.items() if v[axis]==val]
        a,b=[q for q in range(3) if q!=axis]
        order=sorted(group,key=lambda i: { (0,0):0,(1,0):1,(1,1):2,(0,1):3 }[(int(cube[i][a]),int(cube[i][b]))])
        cube_faces.append(order)
print('tetra',one_trial(tetra,tetra_faces,h=1))
print('cube',one_trial(cube,cube_faces,h=1))
print('PASS 200 random noncommuting SU(2) surface configurations, every edge gradient, weighted flow bounds; PF physical regulator OPEN')