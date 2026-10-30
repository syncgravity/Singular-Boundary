"""Finite inverse-Whitney form and transported-frame covariance regression.
Requires global_whitney_11face.npz; generate from saved assembly code.
"""
import os
from pathlib import Path
import numpy as np
paths=[Path(__file__).resolve().parent/'global_whitney_11face.npz',Path('/mnt/data/global_whitney_11face.npz')]
file=next((x for x in paths if x.exists()),None)
if file is None:raise SystemExit('global_whitney_11face.npz required')
M=np.load(file)['matrix'];w=np.linalg.eigvalsh(M)
assert M.shape==(30,30) and w[0]>0
K=np.linalg.inv(M);lower=1/w[-1];upper=1/w[0]
rng=np.random.default_rng(20261030)
for _ in range(100):
 V=rng.normal(size=(30,3));rots=[]
 for i in range(30):
  r,_=np.linalg.qr(rng.normal(size=(3,3)))
  if np.linalg.det(r)<0:r[:,0]*=-1
  rots.append(r)
 D=np.einsum('eij,ej->ei',np.array(rots),V)
 energy=np.einsum('ef,ei,fi->',K,D,D);norm=np.sum(V*V)
 assert lower*norm-1e-10<=energy<=upper*norm+1e-10
 G,_=np.linalg.qr(rng.normal(size=(3,3)))
 alt=D@G.T
 assert np.isclose(energy,np.einsum('ef,ei,fi->',K,alt,alt),atol=1e-10)
print('PASS 100 inverse-Whitney and common-adjoint frame tests')
print('electric-only gap lower bound, g2 squared =1:',3/(8*w[-1]))
