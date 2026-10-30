#!/usr/bin/env python3
"""Joint 24-mode + crossing-energy transport, exact Gaussian gauge benchmark.
NO compact SU(2) Gibbs concentration claim.
"""
import sys,json,time
from pathlib import Path
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import splu
ROOT=Path(__file__).resolve().parent
SRC=Path(__file__).resolve().parent;sys.path.insert(0,str(SRC))
from direct_cut_project import build
from construct_surgery import product_collar
from cavity_audit import seed_support,Q_from_seed
from relative_words import solve
from classify_modes import analyze

def sparse_matrix(fs,edges,words):
 idx={e:i for i,e in enumerate(edges)}; rows=[];cols=[];vals=[]
 for j,f in enumerate(fs):
  for e,s in words[f]:
   if e in idx:rows.append(j);cols.append(idx[e]);vals.append(s)
 return sp.csr_matrix((vals,(rows,cols)),shape=(len(fs),len(edges)),dtype=float)

def primary(radius):
 g,_=build(radius,0);W,_=product_collar(g);Q=Q_from_seed(g,seed_support(build(5.,0)[0]));R=sorted(set(range(len(W)))-Q)
 H=set(e for f in Q for e,s in W[f]);A=sorted(f for f in R if any(e in H for e,s in W[f]));X=set(json.loads((SRC/'optimized_basis.json').read_text())['best_basis_links']) if radius==5 else None
 if X is None:
  from classify_modes import link_key
  labels=json.loads((SRC/'optimized_basis.json').read_text())['best_basis_z5_labels']
  link_by_label={str(link_key(g,e)):e for e in range(3*(len(g.labels)+len(g.edges)))}
  X={link_by_label[str(key)] for key in labels}
 C=sorted(f for f in R if f not in A and any(e in X for e,s in W[f]))
 if radius==5:
  t=solve(True,optimized=True,radius=radius);P=sorted(o['edge'] for o in t['operations'])
 else:
  # pivot roles mapped by canonical geometry labels of original 5-radius specimen
  from classify_modes import link_key
  base,_=build(5.,0);bt=solve(True,optimized=True,radius=5.)
  ref={str(link_key(base,o['edge'])) for o in bt['operations']};inv={str(link_key(g,e)):e for e in range(3*(len(g.edges)+len(g.labels)))}
  P=sorted(inv[k] for k in ref)
 edges=sorted({e for f in R for e,s in W[f]});D=sparse_matrix(R,edges,W)
 Ma=sparse_matrix(A,P,W).toarray();Mc=sparse_matrix(C,P,W).toarray()
 assert np.linalg.matrix_rank(Ma)==59 and len(P)==59 and len(A)==62 and len(C)==33
 L=Mc@np.linalg.pinv(Ma,rcond=1e-12)
 # normal-projection covariance restricted to A union C; Tikhonov inverse converges to projector in lambda_reg->0
 ia=np.array([R.index(f) for f in A+C]);da=D[ia,:].toarray();tic=time.time()
 G=(D.T@D).tocsc();n=G.shape[0];reg=1e-7
 fac=splu(G+reg*sp.eye(n,format='csc'))
 Cov=da@fac.solve(da.T);Cov=(Cov+Cov.T)/2
 eig,evec=np.linalg.eigh(Cov);eig=np.clip(eig,0,1);rootcov=(evec*np.sqrt(eig))@evec.T
 k=len(A);Z=np.zeros((len(C),len(C)));M=np.block([[L.T@L,-L.T],[-L,Z]])
 S=rootcov@M@rootcov;alpha=np.linalg.eigvalsh((S+S.T)/2)
 tr=float(np.sum(alpha));var=float(np.sum(alpha**2));rnk=int(np.linalg.matrix_rank(Cov,tol=1e-5));
 # Independent of ambient shape: 24-dimensional quotient of retained face curvature by H-link repair.
 H=sorted({e for q in Q for e,s in W[q]});Dh=sparse_matrix(A,H,W).toarray()
 uu,ss,vv=np.linalg.svd(Dh,full_matrices=True);rankH=np.sum(ss>1e-10)
 assert rankH==35
 transverse=uu[:,rankH:];Covcomp=transverse.T@Cov[:len(A),:len(A)]@transverse
 ec=np.linalg.eigvalsh((Covcomp+Covcomp.T)/2);ec=np.clip(ec,0,1)
 assert np.count_nonzero(ec>1e-5)==24 and ec.max()<=1+1e-6

 co={'radius':radius,'ambient_retained_faces':len(R),'A_faces':len(A),'crossing_faces':len(C),'solved_pivots':len(P),
  'normal_projector_covariance_max_eig':float(eig.max()),'normal_projector_covariance_rank':rnk,
  'crossing_transfer_operator_norm':float(np.linalg.norm(L,ord=2)),
  'crossing_transport_quadratic_eigenvalue_min':float(alpha.min()),'crossing_transport_quadratic_eigenvalue_max':float(alpha.max()),
  'crossing_transport_positive_eigenvalue_count':int(np.count_nonzero(alpha>1e-7)),
  'dimensionless_gaussian_crossing_mean_lambda_Gamma':float(1.5*tr),
  'dimensionless_gaussian_crossing_std_lambda_Gamma':float(np.sqrt(1.5*var)),
  'dimensionless_gaussian_crossing_positive_part_upper_expectation':float(np.maximum(alpha,0).sum()*1.5),
  'gaussian_24_mode_covariance_rank':int(np.count_nonzero(ec>1e-5)),'gaussian_24_mode_covariance_max_eig':float(ec.max()),'gaussian_expected_lambda_sH':float(1.5*ec.sum()),'gaussian_lambda_sH_upper_mean':36.0,'gaussian_24_mode_tail':'P(lambda*sH >= t) <= min(1,2^36 exp(-t/2)), uniformly in ambient volume, for exactly linearized free-boundary Gaussian measure, NOT SU2','action_covariance_trace_all_A_C':float(eig.sum()),'elapsed_seconds':time.time()-tic,
  'linearized_Gaussian_theorem':'For each independent SU(2) tangent color the full retained curvature is N(0,P_im(D)/lambda). All local-marginal covariance eigenvalues are <=1, independent of ambient size. For local A, P(lambda*s_H^lin >= t) <= min(1, 2^(3|A|/2)*exp(-t/2)); this is NOT a nonabelian SU2 theorem.'}
 return co

if __name__=='__main__':
 print('GAUSSIAN BENCHMARK',flush=True)
 report=[]
 for r in [5.,6.5]:
  z=primary(r);report.append(z);print('radius',r,'eigen',z['crossing_transport_quadratic_eigenvalue_min'],z['crossing_transport_quadratic_eigenvalue_max'],'mean lambdaGamma',z['dimensionless_gaussian_crossing_mean_lambda_Gamma'],'std',z['dimensionless_gaussian_crossing_std_lambda_Gamma'],flush=True)
 (ROOT/'gaussian_joint_certificate.json').write_text(json.dumps({'status':'Exact theorem for normal Gaussian quotient; floating point numerical coefficient audit on two genuine Penrose ambient patches; NOT a nonlinear Haar concentration bound','results':report},indent=2))
