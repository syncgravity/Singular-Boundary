"""Exact relative deleted-face cap feasibility audit for the original Whitney matrix."""
import hashlib, math, numpy as np
from pathlib import Path
p=Path(__file__).resolve().parent/"global_whitney_11face.npz"
expected="d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf"
assert hashlib.sha256(p.read_bytes()).hexdigest()==expected
z=np.load(p); ids=list(map(int,z["edge_ids"])); M=z["matrix"]
m=float(M[ids.index(13),ids.index(13)])
b=3/32000; gamma=3/(8*m);rho=b/gamma
def cap(d):
 t=math.acos(1-d)
 return 2/math.pi*(t-(1-d)*math.sqrt(2*d-d*d))
def cap_inverse(target):
 lo,hi=0.,1.
 for _ in range(100):
  mid=(lo+hi)/2
  if cap(mid)<target:lo=mid
  else:hi=mid
 return (lo+hi)/2
print("rho",rho,"critical delta",cap_inverse(rho/(1-rho)))
for d in (.1,.01,.001):
 c=cap(d)
 print("delta",d,"Haar cap",c,"threshold rho",c/(1+c))
for h in (1.,.5,.25,.125,.0625,.03125,.015625):
 r=rho/(h*h);eps=r/(1-r) if r<1 else float("inf")
 d=cap_inverse(eps) if eps<1 else float("nan")
 print("illustrative h",h,"rho",r,"delta_min",d,"delta.1 lower",max(0,cap(.1)-eps))
assert abs(cap(.1)-.037386073468498655)<1e-13
print("PASS exact original-matrix relative-cap threshold audit")
