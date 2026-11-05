#!/usr/bin/env python3
"""Exact integer CG fusion multiplicity and full invariant operator dimension."""
from collections import defaultdict
def multiplicities(degrees):
    d={degrees[0]:1}
    for n in degrees[1:]:
        nxt=defaultdict(int)
        for L,v in d.items():
            for k in range(abs(L-n),L+n+1,2):nxt[k]+=v
        d=dict(nxt)
    return d
for m,N in ((3,10),(4,16),(6,36),(10,100)):
    for ell in (m-1,m+1):
        d=multiplicities([ell]+[1]*(N-1))
        dimension=(ell+1)*2**(N-1)
        invariant=sum(v*v for v in d.values())
        assert sum((L+1)*v for L,v in d.items())==dimension
        print('PASS N',N,'m',m,'ell',ell,'Fourier',dimension,'invariant',invariant,'maxmultiplicity',max(d.values()))
print('Only full invariant algebra dimensions; source-adapted compressed ranks may be smaller')
