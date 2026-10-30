#!/usr/bin/env python3
"""Numerical differential audit of the exact S3 geodesic-contraction Haar Jacobian.
Analytic proof uses spherical coordinates, not this numerical test.
"""
import json
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent
rng=np.random.default_rng(20261027)
def contract(x,t):
 theta=np.arccos(np.clip(x[0],-1,1))
 if theta<1e-10:return x.copy()
 v=x.copy();v[1:]*=(np.sin((1-t)*theta)/np.sin(theta));v[0]=np.cos((1-t)*theta)
 return v
def jac_sphere(x,t,eps=3e-6):
 # Orthonormal source tangent basis from QR decomposition.
 seed=np.eye(4);seed[:,0]=x
 Q,_=np.linalg.qr(seed)
 basis=Q[:,1:]
 derivative=[]
 for i in range(3):
  x1=x+eps*basis[:,i];x1/=np.linalg.norm(x1)
  x2=x-eps*basis[:,i];x2/=np.linalg.norm(x2)
  derivative.append((contract(x1,t)-contract(x2,t))/(2*eps))
 D=np.stack(derivative,axis=1)
 return float(np.sqrt(np.linalg.det(D.T@D)))
rows=[]
for t in [0.1,.25,.5,.8]:
 for theta in np.linspace(.15,3.0,17):
  n=rng.normal(size=3);n/=np.linalg.norm(n)
  x=np.r_[np.cos(theta),np.sin(theta)*n]
  J=(1-t)*(np.sin((1-t)*theta)/np.sin(theta))**2
  jnum=jac_sphere(x,t)
  rows.append({'t':t,'theta':float(theta),'j_analytic':float(J),'j_num':jnum,'relative_error':abs(jnum/J-1)})
assert max(x['relative_error'] for x in rows)<3e-6
(R/'jacobian_validation.json').write_text(json.dumps({'status':'PASS; independent numeric tangent-Jacobian check; proof analytic','max_relative_error':max(x['relative_error'] for x in rows),'trials':len(rows)},indent=2))
print('PASS Jacobian',max(x['relative_error'] for x in rows),'trials',len(rows))
