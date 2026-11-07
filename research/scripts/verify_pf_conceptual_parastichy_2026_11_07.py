#!/usr/bin/env python3
"""Golden-angle 34/55 consequence controls: NOT authentic coupled-Z5 Conway/3D observer."""
import math
from collections import Counter
import numpy as np
from scipy.spatial import Delaunay

phi=(1+math.sqrt(5))/2
alpha=phi**-2
F=[0,1]
for k in range(2,17):F.append(F[-1]+F[-2])
checks=0
for k in range(3,15):
 assert abs(F[k]*alpha-F[k-2]-(-1)**k*phi**-k)<2e-13
 checks+=1
assert F[9]==34 and F[10]==55
assert math.sin(2*math.pi*34*alpha)<0 and math.sin(2*math.pi*55*alpha)>0
checks+=2
n=np.arange(1,1601)
phases={'golden':n*alpha,'irrational_complement':n/phi,
 'rational_H3':n*(8/13),
 'phase_shuffled':np.random.default_rng(101).permutation((n*alpha)%1)}
results={}
for key,p in phases.items():
 xy=np.c_[np.sqrt(n)*np.cos(2*np.pi*p),np.sqrt(n)*np.sin(2*np.pi*p)]
 e=set()
 for t in Delaunay(xy).simplices:
  for a,b in ((t[0],t[1]),(t[1],t[2]),(t[2],t[0])):
   e.add(tuple(sorted((int(a),int(b)))))
 for lo,hi in ((200,400),(400,800),(800,1300)):
  c=Counter(b-a for a,b in e if lo<=a<hi and lo<=b<hi)
  results[key,lo,hi]=c.most_common(6)
  checks+=1
assert [k for k,v in results['golden',400,800][:3]]==[34,55,89]
assert [k for k,v in results['irrational_complement',400,800][:3]]==[34,55,89]
assert set(k for k,v in results['rational_H3',400,800][:3])=={5,8,13}
checks+=3
for k in (34,55):
 assert len({i%k for i in range(100,500)})==k
 checks+=1
for a in (3,5,8):
 x=(a*np.arange(52))%13
 assert len(set(x[:13]))==13 and np.array_equal(x[:13],x[13:26])
 checks+=1
for k in (34,55):
 assert np.sign(np.sin(2*np.pi*k*alpha))==-np.sign(np.sin(2*np.pi*k*(1-alpha)))
 checks+=1
assert .002<abs(8/13-1/phi)<.003
checks+=1
assert checks==37,checks
for name in phases:print(name,results[name,400,800][:3])
print('PASS',checks,'toy golden-angle / rational-pitch / shuffled controls; source-Z5 observer OPEN')
