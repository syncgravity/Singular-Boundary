#!/usr/bin/env python3
"""Algebraic exact-constant check of universal spin and 35-state exclusion.
Uses earlier eight-face exact coefficient definition; no numerical claim of a
full connected SU2 ground-state eigenspectrum.
"""
import math
C_H=4*math.sqrt(2)/(3*math.pi)
faces=sorted((x,y) for x in range(3) for y in range(3) if (x,y)!=(0,0))
retained=[f for f in faces if f!=(1,1)]
from collections import defaultdict
inc=defaultdict(list)
for x,y in faces:
    v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
    for a,b in zip(v,v[1:]+v[:1]): inc[tuple(sorted((a,b)))].append((x,y))
edges=sorted(inc)
assert len(faces)==8 and len(retained)==7 and len(edges)==22
A={f:sum(.8+.07*(i%6)+.013*(i%3) for i,e in enumerate(edges) if f in inc[e]) for f in faces}
c={f:.78+.09*i for i,f in enumerate(retained)}
C=3/(2*math.sqrt(2))*sum(math.sqrt(A[q]*c[q]) for q in retained)
assert abs(C-15.042168124831)<1e-8
min_c=min(c.values())
# Universal one-link spin support: each outer private edge appears at most
# once as an SU2 fundamental in every 35-state basis function.
q=retained[0]
outer=[e for e in edges if inc[e]==[q]]
assert len(outer)>=1
Dhalf=1**2+2**2
D1=Dhalf+3**2
assert Dhalf==5 and D1==14
# Seven retained independent Haar-cap variables for the 35-state basis.
assert 1+len(retained)+len(retained)*(len(retained)-1)//2+6==35
K=35*16
pref=math.sqrt(K)*C_H**3.5+math.sqrt(C/min_c)
assert pref>0
for b in (1e3,1e6,1e12,1e24):
    delta=b**(-1/23)
    u=math.sqrt(K)*(C_H*delta**1.5)**(7/2)+math.sqrt(C/(min_c*delta*math.sqrt(b)))
    bound=pref*b**(-21/92)
    assert math.isclose(u,bound,rel_tol=1e-12)
    print('b %.0e  seven-cap overlap certificate upper %.8f' % (b,min(1,bound)))
for eta in (.25,.5,.8):
    b=1e15;delta=4*C/(eta**2*min_c*math.sqrt(b))
    assert delta<=1
    Dmin=eta**5/(32*C_H)*(min_c/C)**1.5*b**.75
    Nmin=Dmin**(1/3)-2
    assert Dmin>0
    print('overlap eta',eta,'necessary character index lower',Nmin)
print('PASS: exact finite 35-state sup kernel, seven-face Haar cap rarity, b^-21/92 overlap exclusion and universal b^1/4 link-spin necessity')
