"""Archived M5 Wilson edge-center symmetry and conditional SU2 Haar moments.
Run after restoring actual_m5_two_tree_forms.py and original matrix from Library.
"""
import numpy as np, contextlib, io, sys
with contextlib.redirect_stdout(io.StringIO()):
 sys.path.insert(0, "/mnt/data")
 import actual_m5_two_tree_forms as m
rng=np.random.default_rng(551)
e=m.edge_index[13]
assert 13 not in m.T1
assert [f for f in m.F if 13 in m.fi[f]]==[0,10]
err=0.
for _ in range(6):
 U=rng.normal(size=(30,4)); U/=np.linalg.norm(U,axis=1)[:,None]
 J=U.copy(); J[e]*=-1
 for f in m.F:
  target=-m.face_p(f,U) if f in (0,10) else m.face_p(f,U)
  assert abs(m.face_p(f,J)-target)<1e-12
 assert max(np.linalg.norm(x-y) for x,y in zip(m.transports(m.T1,U),m.transports(m.T1,J)))<1e-12
 a,bvec=[],[]
 for f,target in [(0,a),(10,bvec)]:
  for k in range(4):
   X=U.copy();X[e]=np.eye(4)[k];target.append(m.face_p(f,X))
 a=np.array(a);bvec=np.array(bvec)
 assert abs(np.linalg.norm(a)-1)<1e-12 and abs(np.linalg.norm(bvec)-1)<1e-12
 c=float(a@bvec)
 for p in (-.8,-.2,.2,.8):
  Z=rng.normal(size=(20000,4));Z-=np.outer(Z@a,a);Z/=np.linalg.norm(Z,axis=1)[:,None]
  z=(p*a+np.sqrt(1-p*p)*Z)@bvec
  mean=c*p;second=c*c*p*p+(1-c*c)*(1-p*p)/3
  err=max(err,abs(z.mean()-mean),abs((z*z).mean()-second))
  assert abs(z.mean()-mean)<.014 and abs((z*z).mean()-second)<.014
print("PASS original M5 Wilson parity and Haar conditional first/second moments; max MC error",err)
