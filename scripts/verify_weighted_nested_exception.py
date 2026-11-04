#!/usr/bin/env python3
"""Exact weighted-exception Casimir history combinatorics, κ=log(4).
Does NOT test the inherited SU(2) coefficientwise PW operator estimates.
"""
from fractions import Fraction as F
from random import Random
def edges(i,j):
    return ({("top",k) for k in range(i,j+1)}
            |{("bot",k) for k in range(i,j+1)}
            |{("vert",k) for k in range(i,j+2)})
def check():
    rng=Random(20261104);checks=0
    for N in range(1,29):
        outer=edges(1,N)
        Jset=[(a,b) for a in range(1,N+1) for b in range(a,N+1)]
        Es={J:edges(*J) for J in Jset}
        for _ in range(20):
            n={e:rng.randrange(7) for e in outer}
            qe={e:F(k*(k+2),4) for e,k in n.items()}
            q=sum(qe.values(),F(0))
            if not q:continue
            W={J:F(rng.randrange(1,20),rng.randrange(10,70)) for J in Jset}
            G=max((sum((W[J] for J in Jset if J[0]<=x<=J[1]),F(0))
                  for x in range(1,N+1)),default=F(0))
            Q={J:sum((qe[e] for e in Es[J]),F(0)) for J in Jset}
            for e in outer:
                weighted=sum((F(1,2**(J[1]-J[0]+1))*W[J]
                              for J in Jset if e in Es[J]),F(0))
                assert weighted<=G
                checks+=1
            charge=sum((Q[J]*F(1,2**(J[1]-J[0]+1))*W[J] for J in Jset),F(0))
            assert charge<=q*G
            exc=[J for J in Jset if 2*Q[J]>q]
            half=sum((F(1,2**(J[1]-J[0]+1))*W[J] for J in exc),F(0))
            assert half<=2*G
            cost=sum((F(3*(J[1]-J[0]+1)+1,4**(J[1]-J[0]+1))*W[J]
                      for J in exc),F(0))
            assert cost<=4*G
            checks+=3
    for m in range(1,10001):
        assert F(3*m+1,2**m)<=2
        checks+=1
    assert checks==36600,checks
    print("PASS",checks,"exact-rational incidence, weighted energy and exception checks")
    print("κ=log4 gives Hκ=2, nested constants R and 4C0")
if __name__=="__main__":check()
