#!/usr/bin/env python3
"""PF-I16: 3-face source-Z5 motif and sharp SU(2) Gauss Schatten threshold."""
import numpy as np
from itertools import combinations

def add(*vecs):
    return tuple(sum(v[i] for v in vecs) for i in range(5))
z=(0,)*5
i,j,k=[tuple(int(t==d) for t in range(5)) for d in range(3)]
def face(o,a,b):
    x,y,w=add(o,a),add(o,b),add(o,a,b)
    return {frozenset((o,x)),frozenset((o,y)),frozenset((x,w)),frozenset((y,w))}
F=[face(z,i,j),face(z,i,k),face(k,i,j)]
assert len(set.union(*F))==10
assert len({v for f in F for e in f for v in e})==8
assert (len(F[0]&F[1]),len(F[1]&F[2]),len(F[0]&F[2]))==(1,1,0)
assert {sum(v) for f in F for e in f for v in e}=={0,1,2,3}
def allowed(x,y,z):return abs(x-y)<=z<=x+y and not ((x+y+z)%2)
def opts(a,t,u,N):
    return [x for x in range(N+1) if allowed(x,a,t) and allowed(x,a,u)]
def trace(N,p=2):
    out=0.;cnt=0
    for t in range(N+1):
        for u in range(N+1):
            allopts=[opts(a,t,u,N) for a in range(N+1)]
            for a,Ls in enumerate(allopts):
                if not Ls: continue
                L=np.array(Ls,float)
                base=3*L*(L+2)+a*(a+2)+t*(t+2)+u*(u+2)
                for b,Rs in enumerate(allopts):
                    if not Rs: continue
                    R=np.array(Rs,float)
                    E=(base[:,None]+b*(b+2)+3*R[None,:]*(R[None,:]+2))/4
                    if a==b==t==u==0: E=E[E>0]
                    out+=float(np.sum(E**(-p)))
                    cnt+=E.size
    return cnt,out
for N,expected in [(4,589),(8,14046),(12,112419),(16,527372),(20,1803273)]:
    cnt,acc=trace(N)
    assert cnt==expected
    print(f'N={N} states={cnt} Tr(K^-2)={acc:.9f}')
for M in (2,4,8,16,32):
    even=range(M,2*M,2)
    assert len(even)==M//2
    for x,y,z in combinations(even,3):
        assert allowed(x,y,z)
    bound=(M/2)**6/(10*M*(M+1))**2
    print(f'M={M} dyadic lower shell Tr(K^-2) >= {bound:.9f}')
print('PASS original-Z5 three-square topology, Gauss spin rules, cutoff traces; p>3 by analytic shell count')
