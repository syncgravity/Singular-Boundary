#!/usr/bin/env python3
"""Certify a model-independent, η-regularized Gaussian rank-update bound.
The exterior ηI reference is NOT the physical SU(2) Haar measure.
"""
import numpy as np,json
from pathlib import Path
from scipy.linalg import null_space
root=Path(__file__).resolve().parent
D=np.load('/mnt/data/R3_local_conditional_2026_10_27/incidence.npz')['d2']
qsets=[np.load(root/'effective_forms.npz')['good_Q'],np.load(root/'effective_forms.npz')['bad_Q'],np.load(root/'bianchi_operator.npz')['Q']]
rng=np.random.default_rng(242424)
for cnt in [1,2,4,6,8,12,20]:
 for _ in range(5):qsets.append(np.sort(rng.choice(np.arange(12,48),cnt,replace=False)))

def form(Q,S,L,E):
 A=D[np.ix_(L,S)].T.astype(float);B=D[np.ix_(E,S)].T.astype(float)
 ns=null_space(A.T,rcond=1e-11);R=ns.T@B
 return R.T@R
normD=float(np.linalg.norm(D.astype(float),2)**2)
face_length=int(np.abs(D).sum(axis=0).max());valence=int(np.abs(D).sum(axis=1).max())
assert normD<=face_length*valence+1e-10
records=[]
for Q in qsets:
 L=np.flatnonzero(np.any(D[:,Q]!=0,axis=1));E=np.setdiff1d(np.arange(D.shape[0]),L);R=np.setdiff1d(np.arange(D.shape[1]),Q)
 C0=form(Q,R,L,E);C1=form(Q,np.arange(D.shape[1]),L,E);delta=(C1-C0);delta=(delta+delta.T)/2
 ed=np.linalg.eigvalsh(delta)
 r=int((ed>1e-8).sum());assert ed.min()>-1e-8
 assert r<=len(Q) and ed.max()<=normD+1e-8
 lamb=300.;eta=1.
 l0=np.linalg.eigvalsh(C0);l1=np.linalg.eigvalsh(C1)
 h=1.5*(sum(np.log1p(lamb*v/eta) for v in l1 if v>1e-8)-sum(np.log1p(lamb*v/eta) for v in l0 if v>1e-8))
 bound=1.5*len(Q)*np.log1p(lamb*face_length*valence/eta)
 assert -1e-6<=h<=bound+1e-6,(h,bound)
 records.append({'Q':list(map(int,Q)),'Q_faces':len(Q),'local_links':len(L),'perturbation_rank':r,'perturbation_norm':float(ed.max()),'regularized_frustration_at_lambda300':float(h),'universal_bound_at_lambda300':float(bound)})
report={'model':'three-step quadrilateral-prism combinatorial Gaussian','samples_checked':len(records),'incidence_face_length_bound':face_length,'incidence_link_valence_bound':valence,'combinatorial_operator_norm_squared_bound':face_length*valence,'measured_operator_norm_squared':normD,'theorem':'For any Q, eta>0, lambda>=0: H_eta(lambda)=(3/2)logdet((etaI+lambda C1)/(etaI+lambda C0)) <= (3/2)|Q| log(1+lambda p nu/eta). Works irrespective of rank preservation, for η-regularized Gaussian model only.','records':records,'limitations':'Finite linearized Gaussian with isotropic exterior regularization; nonlinear SU2 Wilson Haar Gibbs model not proved.'}
(root/'uniform_gaussian_certificate.json').write_text(json.dumps(report,indent=2))
print('PASS',len(records),'supports, p*nu=',face_length*valence,'max norm',normD,'max rank ratio',max(x['perturbation_rank']/x['Q_faces'] for x in records))
