#!/usr/bin/env python3
"""Exact-Haar-Jacobian, bounded-multiplicity, 59-link partial geodesic surgery.
Full retained action never increases by construction. No uniform s_H coercivity claim.
"""
import sys,json,math
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
SRC=Path(__file__).resolve().parent;sys.path.insert(0,str(SRC))
from direct_cut_project import build
from construct_surgery import product_collar
from cavity_audit import seed_support,Q_from_seed
from relative_words import solve
from wilson_geodesic_probe import repair,geodesic_contraction,evaluate,arrays

TAUS=(0.,.1,.25,.5)

def input_data():
 g,_=build(5.,0);W,_=product_collar(g);Q=Q_from_seed(g,seed_support(g));R=sorted(set(range(len(W)))-Q)
 H={e for f in Q for e,s in W[f]};A=sorted(f for f in R if any(e in H for e,s in W[f]));ops=solve(True,optimized=True,radius=5.)['operations']
 P=[op['edge'] for op in ops];X=set(P)-H;C=sorted(f for f in R if f not in A and any(e in X for e,s in W[f]))
 arr,sgn,_,_=arrays(W,R);lookup={f:i for i,f in enumerate(R)};AF=np.asarray([lookup[f] for f in A],np.int64);CF=np.asarray([lookup[f] for f in C],np.int64)
 oed=np.array(P,np.int64);ww=np.array([int(t) for op in ops for t in op['replacement_word']],np.int64);offsets=np.array([0]+list(np.cumsum([len(op['replacement_word']) for op in ops])),np.int64)
 return g,arr,sgn,AF,CF,oed,ww,offsets

def action(U,EA,SG,A,C):return float(evaluate(U,EA,SG,A)+evaluate(U,EA,SG,C))

def surgery(U,arrays):
 g,ea,sg,A,C,p,w,offs=arrays
 target=repair(U,p,offs,w);base=action(U,ea,sg,A,C)
 results=[(base,0.,U.copy())]
 for t in TAUS[1:]:
  V=geodesic_contraction(U,target,p,t);results.append((action(V,ea,sg,A,C),t,V))
 score,t,V=min(results,key=lambda x:x[0]);return t,V,base-score,target

def jacobian(U,target,p,t):
 if t==0:return 1.,0.
 angles=np.arccos(np.clip(np.sum(U[p]*target[p],axis=1),-1.,1.))
 assert np.max(angles)<np.pi-1e-8,'antipodal null set'
 logj=np.log1p(-t)*len(p)
 for theta in angles:
  if theta<1e-5:
   logj+=2*np.log1p(-t)
  else:logj+=2*(np.log(np.sin((1.-t)*theta))-np.log(np.sin(theta)))
 assert logj>=3*len(p)*math.log1p(-t)-1e-8
 return math.exp(logj),float(logj)

def main():
 data=input_data();g,ea,sg,A,C,p,w,offs=data;n=3*(len(g.labels)+len(g.edges))
 rng=np.random.default_rng(240821);rows=[]
 for category in ['flat','near_flat','haar_random','center_defect']:
  U=np.tile(np.array([1.,0,0,0]),(n,1))
  if category=='near_flat':
   x=rng.normal(size=(n,3));x/=np.linalg.norm(x,axis=1)[:,None];angle=rng.normal(0.,.08,size=n)
   U[:,0]=np.cos(angle);U[:,1:]=x*np.sin(angle)[:,None]
  elif category=='haar_random':
   U=rng.normal(size=(n,4));U/=np.linalg.norm(U,axis=1)[:,None]
  elif category=='center_defect':
   U[p[::6]]*=-1
  target=repair(U,p,offs,w)
  # Prove computationally the target is independent of all original solved pivot values.
  W=U.copy();uu=rng.normal(size=(len(p),4));uu/=np.linalg.norm(uu,axis=1)[:,None];W[p]=uu
  second=repair(W,p,offs,w)
  independence=float(np.max(np.abs(target[p]-second[p])))
  assert independence<1e-12
  t,V,drop,target=surgery(U,data)
  assert drop>=-1e-10
  assert evaluate(target,ea,sg,A)<1e-9
  _,logj=jacobian(U,target,p,t)
  far=np.max(np.abs(V[np.array([i for i in range(n) if i not in set(p)])]-U[np.array([i for i in range(n) if i not in set(p)])]))
  assert far<1e-12
  rows.append({'configuration':category,'chosen_tau':t,'full_retained_action_decrease':drop,'target_independence_error':independence,'log_Haar_Jacobian':logj,'far_link_change_error':float(far),'target_A_energy':float(evaluate(target,ea,sg,A))})
 sample=json.loads((ROOT/'wilson_crossing_geodesic_samples.json').read_text())['samples'];stats=[]
 for lam in sorted({s['lambda'] for s in sample}):
  s=[x for x in sample if x['lambda']==lam]
  ds=np.array([[0.,x['lambda_action_decrease_tau_0.1'],x['lambda_action_decrease_tau_0.25'],x['lambda_action_decrease_tau_0.5']] for x in s]);picks=np.argmax(ds,axis=1)
  stats.append({'lambda':lam,'samples':len(s),'mean_best_lambda_action_decrease':float(np.mean(np.max(ds,axis=1))),'median_best_lambda_action_decrease':float(np.median(np.max(ds,axis=1))),'fraction_strict_improvement':float(np.mean(np.max(ds,axis=1)>1e-7)),'chosen_tau_histogram':{str(t):int(np.count_nonzero(picks==j)) for j,t in enumerate(TAUS)}})
 cert={'map':'For each solved pivot p, conditional geodesic contraction U_p-> Exp_target[(1-tau)Log_target U_p]. Target depends exclusively on remaining links (verified). Choose tau from {0,0.1,0.25,0.5} minimizing all affected full retained plaquettes.',
 'proof':'Each branch is a diffeomorphism a.e. onto geodesic ball radius (1-tau)π centered at target, with Haar Jacobian j=(1-tau)[sin((1-tau)θ)/sinθ]^2 >= (1-tau)^3. All targets independent of the original pivot links. At most four inverse branches. Include identity to ensure full-action nonincrease. This alone does not force decrease proportional to s_H.',
 'pivots':len(p),'affected_A_faces':len(A),'crossing_faces':len(C),'grid':TAUS,'max_inverse_multiplicity':len(TAUS),'global_branch_J_lower_bound':float((1-max(TAUS))**(3*len(p))), 'negative_log_J_lower_bound':float(-3*len(p)*math.log(1-max(TAUS))),
 'direct_checks':rows,'Wilson_MCMC_diagnostic':stats,'caveat':'No proof that adaptive decrease controls the absolute local minimum under the full SU2 Gibbs law. Short MCMC tests are exploratory, not equilibration certificates.'}
 (ROOT/'adaptive_surgery_certificate.json').write_text(json.dumps(cert,indent=2));print(json.dumps({'checks':rows,'stats':stats,'lower_log_jacobian':cert['negative_log_J_lower_bound']},indent=2))
if __name__=='__main__':main()
