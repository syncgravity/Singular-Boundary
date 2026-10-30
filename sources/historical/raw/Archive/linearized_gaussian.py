"""Exact integer-derived abelianized Gaussian conditional comparison for local 36 links.
Rank and spectrum checks independent of stochastic gauge sampling.
"""
import numpy as np,json
from scipy.linalg import null_space
from pathlib import Path
z=np.load('/mnt/data/R3_local_conditional_2026_10_27/incidence.npz');D=z['d2'];Q=z['Q'];L=z['local_links'];R=np.setdiff1d(np.arange(D.shape[1]),Q);E=np.setdiff1d(np.arange(D.shape[0]),L)
blocks={};X=np.zeros((len(E),len(E)))
for name,fac in [('ret',R),('full',np.arange(D.shape[1]))]:
 A=D[np.ix_(L,fac)].T.astype(float); B=D[np.ix_(E,fac)].T.astype(float)
 ns=null_space(A.T, rcond=1e-12) # orthogonal complement in face space
 C=B.T@ns@ns.T@B;C=(C+C.T)/2
 w,V=np.linalg.eigh(C);pos=w>1e-8
 print(name,'face-count',len(fac),'A rank',np.linalg.matrix_rank(A),'residual rank',pos.sum(), 'eigs',np.round(w[pos],8))
 blocks[name]=dict(C=C,eig=w,pos=pos,V=V,ns=ns)
C0=blocks['ret']['C'];C1=blocks['full']['C'];w0,V0=np.linalg.eigh(C0);w1,V1=np.linalg.eigh(C1);pos0=w0>1e-8;pos1=w1>1e-8
H=V0[:,pos0];D0=np.diag(w0[pos0]);D1=H.T@C1@H;d0=np.linalg.eigvalsh(D0);d1=np.linalg.eigvalsh(D1)
G=np.linalg.eigvalsh(np.linalg.inv(np.diag(np.sqrt(d0))) @ (H.T@C1@H) @ np.linalg.inv(np.diag(np.sqrt(d0))))
assert np.linalg.matrix_rank(C1-C0,tol=1e-8)<=5
assert np.min(G)>=1-1e-8
assert np.linalg.norm(C0-H@H.T@C0)<1e-8 and np.linalg.norm(C1-H@H.T@C1)<1e-8
base=np.prod(G)**(-1.5)
mean=(3./2)*np.sum(G-1.)
print('generalized spectrum',G,'mean defect',mean,'gaussian E exp(-Delta)',base,'-log',-np.log(base))
certificate={'local_links':len(L),'exterior_links':len(E),'retained_residual_rank':int(pos0.sum()),'full_residual_rank':int(pos1.sum()),'equal_kernel':True,'retained_positive_eigenvalues':w0[pos0].tolist(),'full_positive_eigenvalues':w1[pos1].tolist(),'generalized_eigenvalues':G.tolist(),'gaussian_mean_defect':float(mean),'gaussian_expected_exp_minus_defect':float(base),'gaussian_free_energy_defect':float(-np.log(base)),'linearized_assumptions':'Gaussian SU2 Lie algebra about common flat configuration, normalized quadratic Wilson action; 3 independent color components. Does not prove finite-coupling nonlinear large-lambda limit when gauge holonomy moduli occur.'}
Path('/mnt/data/R3_conditional_frustration_numeric_2026_10_27/gaussian_certificate.json').write_text(json.dumps(certificate,indent=2))
np.savez_compressed('/mnt/data/R3_conditional_frustration_numeric_2026_10_27/gaussian_matrices.npz',C0=C0,C1=C1,projector=H@H.T,gen_eigenvalues=G)
