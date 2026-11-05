#!/usr/bin/env python3
"""P-71: exact SU2 fusion multiplicities for actual N=4 CG output degrees.
The companion verified ZIP supplies full corrected-source and invariant K-inverse code.
"""
from collections import defaultdict
def multiplicities(degrees):
 dp={degrees[0]:1}
 for n in degrees[1:]:
  nxt=defaultdict(int)
  for L,count in dp.items():
   for out in range(abs(L-n),L+n+1,2):nxt[out]+=count
  dp=dict(nxt)
 return dp
for m,channels in [(3,[(2,{1:3,3:3,5:1},19),(4,{1:1,3:3,5:3,7:1},20)]),
                    (4,[(3,{0:1,2:3,4:3,6:1},20),(5,{2:1,4:3,6:3,8:1},20)])]:
 for ell,want,dim in channels:
  deg=[ell,1,1,1]
  d=multiplicities(deg)
  assert d==want,(m,ell,d,want)
  assert sum(v*v for v in d.values())==dim
  assert sum((L+1)*v for L,v in d.items())==(ell+1)*8
  print('PASS m',m,'ell',ell,'twice-spin multiplicities',d,
        'corrected physical invariant superoperator dimension',dim)
print('Reference full-source numerics independently computed in companion archive:')
print('N=4 m=3 R=0.1291250095339979, N=4 m=4 R=0.1169833273515')
print('These values are floating-point, not interval-certified or joint N~m² limits.')
