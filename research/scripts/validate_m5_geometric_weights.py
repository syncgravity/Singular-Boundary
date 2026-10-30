"""Open-disk geometric weights from archived periodic M5 rhombi.
Set PENROSE_STUDY_SRC to the location of the archived Python modules.
"""
import os,sys
import numpy as np
from collections import Counter
if os.environ.get("PENROSE_STUDY_SRC"):
 sys.path.insert(0,os.environ["PENROSE_STUDY_SRC"])
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
m=Approximant(M=5);fi,sg,E=penrose_faces(m)
v=m.Qpar@np.eye(5)
lengths=np.linalg.norm(v,axis=0)
area=np.array([abs(np.linalg.det(v[:,[int(f[4]),int(f[5])]])) for f in m.faces])
assert len(area)==188 and len(m.edges)==376
assert sorted(Counter(np.round(area,9)).values())==[24,24,28,52,60]
D=(0,1,3,2,4,154,150,11,10,7,8)
incident={}
for f in D:
 for e in fi[f]:incident.setdefault(int(e),[]).append(f)
assert len(incident)==30
factor={}
for e,fs in incident.items():
 ell=lengths[int(m.edges[e][2])]
 dual=sum(area[f]/(2*ell) for f in fs)
 factor[e]=ell/dual
 assert dual>0 and factor[e]>0
assert Counter(len(fs) for fs in incident.values())=={1:16,2:14}
for k in (1,2):
 x=[factor[e] for e,fs in incident.items() if len(fs)==k]
 print("incident",k,"electric factor",min(x),max(x))
print("PASS 11 faces, 30 links, 5 area classes, diagonal weights and h scaling")
