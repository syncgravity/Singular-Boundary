#!/usr/bin/env python3
"""PF-I16 exact 50-sector four-face C2222 reduction; independent and linked controls."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from functools import lru_cache

Z=(0,0,0,0); T=(2,2,2,2)
A=[x for x in product(range(3),repeat=4) if sum(x)<=4]
assert len(A)==50 and Counter(map(sum,A))=={0:1,1:4,2:10,3:16,4:19}
assert len([x for x in product(range(5),repeat=4) if sum(x)<=4])==70
def px(a):
    o={}
    for n,v in a.items():
        o[n+1]=o.get(n+1,F(0))+v/2
        if n:o[n-1]=o.get(n-1,F(0))+v/2
    return o
one=[{0:F(1)}]; e={}
for j in range(1,5):
    rhs=px(one[-1]);e[j]=-rhs.get(0,F(0))
    for k in range(2,j):
        for n,v in one[j-k].items():rhs[n]=rhs.get(n,F(0))+e[k]*v
    rhs[0]=rhs.get(0,F(0))+e[j]
    one.append({n:v/F(n*(n+2)) for n,v in rhs.items() if n and v})
assert one[1]=={1:F(1,6)}
assert one[2]=={2:F(1,96)}
assert one[3]=={1:-F(5,1728),3:F(1,2880)}
assert one[4]=={2:-F(37,138240),4:F(1,138240)}
@lru_cache(None)
def psi(a):
    d={Z:F(1)}
    for i,j in enumerate(a):
        nd={}
        for v,c in d.items():
            for n,w in one[j].items():
                z=list(v);z[i]=n;z=tuple(z)
                nd[z]=nd.get(z,F(0))+c*w
        d=nd
    return d
def dot(a,b):return sum(c*b.get(v,F(0)) for v,c in a.items())
def K(a):return {v:c*sum(n*(n+2) for n in v) for v,c in a.items()}
def p(a,i):
    d={}
    for v,c in a.items():
        for s in (-1,1):
            if v[i]+s>=0:
                z=list(v);z[i]+=s;z=tuple(z)
                d[z]=d.get(z,F(0))+c/2
    return d
def comp(a,t=T):
    b=tuple(x-y for x,y in zip(t,a))
    return b if min(b)>=0 else None
K8=W8=D6=F(0);nW=0
for a in A:
    b=comp(a)
    if b is None or b not in A:continue
    if sum(a)==sum(b)==4:
        K8+=dot(psi(a),K(psi(b)))
        for i in range(4):
            c=list(b);c[i]-=1
            if c[i]>=0:
                W8+=dot(psi(a),p(psi(tuple(c)),i));nW+=1
    if sum(a)+sum(b)==6:D6+=dot(psi(a),psi(b))
assert nW==52
N8=K8-2*W8
E2D6=F(0)
for i in range(4):
    t=list(T);t[i]-=2;t=tuple(t)
    for a in A:
        b=comp(a,t)
        if b is not None and b in A and sum(a)+sum(b)==6:
            E2D6-=dot(psi(a),psi(b))/12
assert N8==E2D6==-F(1,139968)
# Original-link 2-face positive control: K(xy)=13/2 xy - z/2, Kz=9/2 z.
u,v=F(4,39),F(4,351)
assert F(13,2)*u==F(2,3) and -u/2+F(9,2)*v==0
C22=-F(2,3)*(u+v)/16+F(1,216)
assert C22==-F(1,8424)
print('PASS: 50 retained sectors, 19 kinetic and 52 Wilson pairings')
print('PASS: exact independent-face C2222=0 via',N8,'-',E2D6)
print('PASS: exact source shared-edge C22=',C22)
