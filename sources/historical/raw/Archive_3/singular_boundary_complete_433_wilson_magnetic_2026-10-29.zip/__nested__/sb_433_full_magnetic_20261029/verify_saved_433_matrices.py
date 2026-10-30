#!/usr/bin/env python3
"""Independent checks of complete first-shell SU(2) matrices and Ritz data.

Kinematic Haar moments checked via binary quaternion 3-design; full 433
matrices independently tested for symmetry, parity, residual and energy scales.
"""
from pathlib import Path
import numpy as np
from scipy.sparse import load_npz,diags
from scipy.sparse.linalg import eigsh,norm
from math import sqrt
p=Path(__file__).resolve().parent
Z=np.load(p/'basis.npz');masks=Z['occupancies'];subs=Z['face_subsets'];kin=Z['electric']
assert len(masks)==433 and len(np.unique(subs))==256
faces=sorted((x,y) for x in range(3) for y in range(3) if (x,y)!=(0,0));targetidx=faces.index((1,1))
retained=[i for i in range(8) if i!=targetidx]
M=[load_npz(p/f'magnetic_{i}.npz') for i in range(8)];C=load_npz(p/'target_spin1.npz')
parity=(-1.)**((subs>>targetidx)&1)
for i,T in enumerate(M):
 assert norm(T-T.T)<1e-12
 assert np.max(np.abs(T.data))<=.500000000001
 # Source face f anticommutes with target center flux; retained faces commute.
 P=diags(parity)
 comm=norm(P@T@P-((-1 if i==targetidx else 1)*T))
 assert comm<1e-11,(i,comm)
 assert abs(np.linalg.norm(T[:,0].toarray())-.5)<1e-10
 # Haar fusion toggles exactly the activated face occupancy bit.
 rr,cc=T.nonzero()
 assert all((subs[a]^subs[b])==(1<<i) for a,b in zip(rr,cc))
assert norm(C-C.T)<1e-10 and norm(diags(parity)@C@diags(parity)-C)<1e-10
assert abs(eigsh(C,k=1,which='LA')[0][0]-1)<1e-8
assert abs(eigsh(C,k=1,which='SA')[0][0]+1/3)<1e-8
print('PASS 433-dimensional SU2 Wilson magnetic matrices, link-spin XOR and center parity')
# Exact 2nd Haar moments of every SU2 fundamental matrix element, using the
# eight-element quaternion subgroup (a spherical 3-design in S^3).
sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]],complex);sz=np.diag([1.,-1.])
unitaries=[s*Q for Q in [np.eye(2),1j*sx,1j*sy,1j*sz] for s in (-1,1)]
eps=np.array([[0,1],[-1,0]])
for a in range(2):
 for b in range(2):
  for c in range(2):
   for d in range(2):
    mixed=sum(np.conj(U[a,b])*U[c,d] for U in unitaries)/8
    same=sum(U[a,b]*U[c,d] for U in unitaries)/8
    assert abs(mixed-((a==c)*(b==d)/2))<1e-12
    assert abs(same-eps[a,c]*eps[b,d]/2)<1e-12
print('PASS exact fundamental SU2 Haar quadratic moments against Q8 3-design')
coeff=np.array([.78+.09*i for i in range(7)])
for b in (1,4,16,64):
 H=diags(kin+b*coeff.sum())
 for j,ci in zip(retained,coeff): H=H-b*ci*M[j]
 ev,V=eigsh(H,k=4,which='SA',tol=1e-11)
 v=V[:,0];gap=ev[1]-ev[0]
 assert np.linalg.norm(H@v-ev[0]*v)<1e-7
 z=np.load(p/f'ritz_b_{b}_c1.npz')
 assert abs(ev[0]-z['evals'][0])<1e-8
 assert abs(float(v@C@v)-z['chi1'])<1e-8
 # Exact seven out-of-shell spin-one Wilson channels.
 floor2=0.
 for j,ci in zip(retained,coeff):
  ix=np.where(subs==1<<j)[0]
  assert len(ix)==1
  floor2+=(b*ci*v[ix[0]]/2)**2
 assert abs(sqrt(floor2)-np.load(p/f'ritz_b_{b}.npz')['residual_lower'])<1e-7
 wt=z['target_four_weight'].item()
 assert abs(float(v@C@v))<=wt+1e-10 # exact norm of compressed chi1 is 1
 p2=0.25*(1+float(v@C@v))
 print(f'b={b:<3} E0={ev[0]:.8f} Ritz gap={gap:.8f} residual floor={sqrt(floor2):.8f} c1={float(v@C@v):.3e} target weight={wt:.8f} p_f2={p2:.8f}')
print('PASS projected eigenvalue residuals, full target spin-one operator and witness-consistent cap expansion')
