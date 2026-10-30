#!/usr/bin/env python3
"""One-face-per-prism local Bianchi repair: explicit integer H certificate."""
import json,numpy as np
from pathlib import Path
root=Path(__file__).resolve().parent
z=np.load('/mnt/data/R3_local_conditional_2026_10_27/incidence.npz')
D2=z['d2'].astype(int);B2=z['spatial_d2'].astype(int)
n=3;d3=np.zeros((n*16,n*4),dtype=int)
for t in range(n):
 nxt=(t+1)%n
 for f in range(4):
  d3[4*n+12*t:4*n+12*(t+1),4*t+f]=B2[:,f]
  d3[4*n*0+4*nxt+f,4*t+f]+=1
  d3[4*t+f,4*t+f]-=1
assert not np.any(D2@d3)
# Choose inserted temporal plaquettes so that each prism cell touches <=1.
inc=[set(np.flatnonzero(d3[f])) for f in range(12,48)]
Q=[]
for f in list(range(12,48)):
 if len(Q)>=5:break
 if all(inc[f-12].isdisjoint(inc[q-12]) for q in Q):Q.append(f)
Q=np.array(Q,dtype=int)
assert len(Q)>=3
R=np.setdiff1d(np.arange(D2.shape[1]),Q)
Hr=np.zeros((len(R),len(Q)),dtype=int)
choices=[]
for qi,q in enumerate(Q):
 cells=np.flatnonzero(d3[q])
 assert len(cells)>=1
 cell=int(cells[0]); s=int(d3[q,cell]);
 # sum_faces d3[f,c] D2[:,f] = 0; solve for inserted q.
 for f in np.flatnonzero(d3[:,cell]):
  if f==q:continue
  assert f not in Q
  ri=int(np.flatnonzero(R==f)[0]);Hr[ri,qi]=-s*int(d3[f,cell])
 choices.append({'face':int(q),'cell':cell,'other_retained_faces':[int(f) for f in np.flatnonzero(d3[:,cell]) if f!=q]})
assert np.array_equal(D2[:,Q],D2[:,R]@Hr)
rowmax=int(np.max(np.sum(np.abs(Hr),axis=1)));colmax=int(np.max(np.sum(np.abs(Hr),axis=0)))
measured_norm2=float(np.linalg.norm(Hr,2)**2)
assert colmax<=5 and rowmax<=2 and measured_norm2<=10+1e-8
report={'prism_count':12,'spatial_complex':'four-quadrilateral disk with three periodic temporal intervals; not Penrose-extracted','isolated_Q':Q.tolist(),'local_face_fillings':choices,'signed_face_boundary_equality_verified':True,'one_face_per_prism_verified':True,'repair_integer_matrix_H_shape':list(Hr.shape),'repair_col_sum_max':colmax,'repair_row_sum_max':rowmax,'schur_upper_bound_norm_H_squared':colmax*rowmax,'measured_norm_H_squared':measured_norm2,'gaussian_C1_le_11C0':'follows from D_Q=D_R H and ||H||²<=10 for every choice of local links','nonlinear_bianchi':'d(W_q) <= 5 sum_{p in chosen prism cell except q} d(W_p), with conjugations along transport paths. Total V_Q <=10 gamma/beta_min * retained local action under equal or uniformly comparable weights. Does NOT directly prove insertion free-energy lower bound.'}
(root/'bianchi_certificate.json').write_text(json.dumps(report,indent=2))
np.savez_compressed(root/'bianchi_operator.npz',d3=d3,H=Hr,Q=Q,R=R)
print(json.dumps(report,indent=2))
