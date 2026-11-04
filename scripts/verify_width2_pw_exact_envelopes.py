#!/usr/bin/env python3
"""Exact finite-regression interface for the fixed-width SU(2) PW Poisson theorem.
Mathematical all-degree arguments are in research/audits/
TWOFACE_SINGLETON_AND_WIDTH2_PW_2026-11-04.md.
Full physical Fourier matrix regressions are in the companion conversation ZIP.
"""
from itertools import product
from fractions import Fraction as F
from random import Random

nested=0;maximum=(F(0),None)
for a,n,r in product(range(1,25),repeat=3):
    A=1+max(a,n);B=1+r;P=a*(a+2);N=n*(n+2);R=r*(r+2)
    for l in range(abs(n-r),n+r+1,2):
        W=1+max(a,l);L=l*(l+2)
        e=F(W,A*B)*(F(1,2)+F(5*(P+N)+4*R,4*(P+L)))
        assert e<8,(a,n,r,l,e)
        if e>maximum[0]:maximum=(e,(a,n,r,l))
        nested+=1
assert nested==131424
print("PASS",nested,"rational two-face/singleton CG multipliers; maximum:",maximum)

self_count=0
for p,q,r,s in product(range(10),repeat=4):
    if (p==q==0) or (r==s==0):continue
    A=1+max(p,q);B=1+max(r,s)
    energy=p*(p+2)+q*(q+2)+r*(r+2)+s*(s+2)
    for l,t in product(range(abs(p-r),p+r+1,2),range(abs(q-s),q+s+1,2)):
        if l==t==0:continue
        out=l*(l+2)+t*(t+2);W=1+max(l,t)
        e=F(W,A*B)*(F(1,2)+F(5*energy,4*out))
        assert e<12,(p,q,r,s,l,t,e)
        self_count+=1
assert self_count==147927
print("PASS",self_count,"rational equal-history two-face fusion multipliers")

# Exact analytic exterior joining correction: D-2S_internal-7S_boundary
# = Q[(x-1/4)^2+(y-7/8)^2+11/64], x=sqrt(P/Q), y=sqrt(R/Q).
assert F(1,16)+F(49,64)+F(11,64)==1
rng=Random(20261104);anchors=0
for width in range(2,49):
    intervals=[(a,a+1) for a in range(1,width)]
    for _ in range(30):
        f={I:F(rng.randrange(1,41),rng.randrange(41,101)) for I in intervals}
        g={j:F(rng.randrange(1,41),rng.randrange(41,101)) for j in range(1,width+1)}
        fn=max(sum((f[I] for I in intervals if I[0]<=x<=I[1]),F()) for x in range(1,width+1))
        gn=max(g.values())
        for x in range(1,width+1):
            out=F()
            for I,v in f.items():
                for j,w in g.items():
                    if not I[0]-1<=j<=I[1]+1:continue
                    if min(I[0],j)<=x<=max(I[1],j):
                        out+=v*w*(F(2) if j in I else F(1,5))
            assert out<=(F(4)+F(4,5))*fn*gn
            anchors+=1
assert anchors==35250
print("PASS",anchors,"exact anchored two-face/singleton weights at κ=log4")
print("FINAL: nested 8 e^-κ; exterior joining 1/5; self-overlap 12 e^-2κ")
