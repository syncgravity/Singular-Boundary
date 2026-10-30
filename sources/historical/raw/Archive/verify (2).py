import numpy as np
from sympy import Matrix
from scipy.special import ive
from pathlib import Path
base=Path('/mnt/data/R3_two_prism_certified_2026_10_27/incidence.npz')
z=np.load(base,allow_pickle=True)
D=Matrix(z['d2'].T.tolist())
full=D.rank()
records=[]
for p in range(D.rows):
    reduced=D.copy(); reduced.row_del(p)
    records.append({'face':p,'full_rank':full,'retained_rank':reduced.rank(), 'retained_determines_deleted':reduced.rank()==full})
assert full==9 and all(x['retained_determines_deleted'] for x in records)
print('Incidence rank certificate: full rank',full, '; one-face-deleted retained ranks:',[r['retained_rank'] for r in records])
for lam in (10,100,1000):
 a=ive(2,lam)/ive(1,lam)
 theta=np.pi/2
 parts=100
 j=np.arange(parts)
 expected_steps=lam*a*(np.cos(j*theta/parts)-np.cos((j+1)*theta/parts))
 total=lam*a*(1-np.cos(theta))
 assert np.allclose(expected_steps.sum(),total)
 print('lambda',lam,'total entropy/action penalty',float(total),'steps telescope',float(expected_steps.sum()))
