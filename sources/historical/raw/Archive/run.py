#!/usr/bin/env python3
"""Retained-cavity SU2 Monte Carlo and conditional Riemannian action minima.
Experiments conditional on constructed 3-step 12-prism complex only.
Matrix-free analytic quaternion gradient; NO continuum or ambient-uniform theorem.
"""
import numpy as np, json, argparse, time
from pathlib import Path
from scipy.optimize import minimize
from numba import njit
SOURCE=Path('/mnt/data/R3_local_conditional_2026_10_27/incidence.npz')
OUT=Path('/mnt/data/R3_conditional_frustration_numeric_2026_10_27')
z=np.load(SOURCE);D1=z['d1'];D2=z['d2'];Q=z['Q'];L=z['local_links'];R=np.setdiff1d(np.arange(D2.shape[1]),Q)
# all plaquettes have four links, prescribed compatible directed cyclic products
words=[]
for f in range(D2.shape[1]):
 edges=list(map(int,np.flatnonzero(D2[:,f])));ends={}
 for e in edges:
  ends[e]=(int(np.flatnonzero(D1[:,e]==-1)[0]),int(np.flatnonzero(D1[:,e]==1)[0]))
 cur=min(v for a,b in ends.values() for v in (a,b));word=[]
 while len(word)<len(edges):
  cand=[]
  for e in edges:
   if e in [t[0] for t in word]:continue
   a,b=ends[e];sign=int(D2[e,f]);
   if (sign==1 and cur==a):cand.append((e,1,b))
   if (sign==-1 and cur==b):cand.append((e,-1,a))
  assert len(cand)==1,(f,cur,cand)
  e,s,cur=cand[0];word.append((e,s))
 assert cur==min(v for a,b in ends.values() for v in (a,b))
 words.append(word)
EW=np.array([[p[0] for p in w] for w in words],dtype=np.int64)
SW=np.array([[p[1] for p in w] for w in words],dtype=np.int64)
assert EW.shape==(48,4)
ISQ=np.zeros(48,dtype=np.bool_);ISQ[Q]=True
ISLOCAL=np.zeros(63,dtype=np.bool_);ISLOCAL[L]=True
FACES_BY_EDGE=np.full((63,8),-1,dtype=np.int64)
for e in range(63):
 adj=np.flatnonzero(np.any(EW==e,axis=1));assert len(adj)<=8;FACES_BY_EDGE[e,:len(adj)]=adj
@njit

def mult(a,b):
 out=np.empty(4);out[0]=a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3]
 out[1]=a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2]
 out[2]=a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1]
 out[3]=a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0]
 return out
@njit
def adjoint(a):
 out=a.copy();out[1:]*=-1;return out
@njit
def identity():
 q=np.zeros(4);q[0]=1;return q
@njit
def facecos(U,f):
 p=identity()
 for i in range(4):
  e=EW[f,i];v=U[e] if SW[f,i]==1 else adjoint(U[e]);p=mult(p,v)
 return p[0]
@njit
def total_energy(U,lam,include_q):
 ret=0.
 for f in range(48):
  if include_q or not ISQ[f]: ret+=lam*(1-facecos(U,f))
 return ret
@njit
def grad_energy(U,lam,include_q):
 val=0.;grad=np.zeros((63,4))
 for f in range(48):
  if not include_q and ISQ[f]:continue
  v=np.empty((4,4));pre=np.empty((5,4));post=np.empty((5,4));pre[0]=identity();post[4]=identity()
  for j in range(4):
   e=EW[f,j];v[j]=U[e] if SW[f,j]==1 else adjoint(U[e]);pre[j+1]=mult(pre[j],v[j])
  for j in range(3,-1,-1):post[j]=mult(v[j],post[j+1])
  val+=lam*(1-pre[4,0])
  for j in range(4):
   e=EW[f,j]
   if not ISLOCAL[e]:continue
   for k in range(4):
    b=np.zeros(4);b[k]=1. if (k==0 or SW[f,j]==1) else -1.
    grad[e,k]-=lam*mult(mult(pre[j],b),post[j+1])[0]
 return val,grad
@njit
def per_link_delta(U,e,proposal,lam):
 cur=0.;new=0.;old=U[e].copy()
 for f in FACES_BY_EDGE[e]:
  if f<0:break
  if ISQ[f]:continue
  cur+=facecos(U,f)
 U[e]=proposal
 for f in FACES_BY_EDGE[e]:
  if f<0:break
  if ISQ[f]:continue
  new+=facecos(U,f)
 U[e]=old
 return -lam*(new-cur)
@njit
def seed_numba(seed):
 np.random.seed(seed)
@njit
def sweep(U,lam,proposal_scale):
 count=0
 for e in np.random.permutation(63):
  rv=np.random.normal(0,1,3);n=np.sqrt((rv*rv).sum());angle=np.random.normal()*proposal_scale
  v=np.empty(4);v[0]=np.cos(angle);v[1:]=rv*np.sin(angle)/n
  prop=mult(v,U[e]);difference=per_link_delta(U,e,prop,lam)
  if difference<=0 or np.random.random()<np.exp(-difference):U[e]=prop;count+=1
 return count/63.
def gradfun(x, U_ext, lam, include_q):
 X=x.reshape((len(L),4));n=np.sqrt((X*X).sum(axis=1));US=X/n[:,None]
 U=U_ext.copy();U[L]=US
 val,raw=grad_energy(U,lam,include_q)
 g=raw[L];g=(g-np.sum(g*US,axis=1)[:,None]*US)/n[:,None]
 return val,g.ravel()
def optimize(U,lam,include_q,start=None,maxiter=400):
 init=U.copy() if start is None else start.copy(); x0=init[L].ravel()
 ret=minimize(gradfun,x0,args=(U,lam,include_q),jac=True,method='L-BFGS-B',
  options={'maxiter':maxiter,'gtol':1.e-7,'ftol':5.e-13,'maxls':25})
 res=U.copy(); x=ret.x.reshape((-1,4));res[L]=x/np.linalg.norm(x,axis=1)[:,None]
 return float(ret.fun),res,{'nit':int(ret.nit),'success':bool(ret.success),'gradient_inf':float(np.max(abs(ret.jac))),'message':str(ret.message)}
def run(lams,samples,burn,stride,chains,seed,maxiter=300,skipseed=0):
 rng=np.random.default_rng(seed);
 for _ in range(skipseed):rng.integers(1,2147483647)
 records=[];diag=[];states=[];now=time.monotonic()
 # Multi-chain independent cold + hot start; local gauge and Wilson gauge invariant observables.
 for lam in lams:
  for chain in range(chains):
   chainseed=int(rng.integers(1,2147483647));seed_numba(chainseed);np.random.seed(chainseed)
   U=np.zeros((63,4));U[:,0]=1
   if chain%2:
    U=np.random.normal(size=(63,4));U/=np.linalg.norm(U,axis=1)[:,None]
   accepted=[];local_energies=[]
   for step in range(burn+samples*stride):
    acc=sweep(U,lam,0.75/np.sqrt(max(1,lam/3)))
    if step>=burn and (step-burn+1)%stride==0:
     val0,r0,d0=optimize(U,lam,False,maxiter=maxiter)
     val1,r1,d1=optimize(U,lam,True,start=r0,maxiter=maxiter)
     # separately minimize full starting from Gibbs sample, safeguard local minima
     val1_alt,r1_alt,d1_alt=optimize(U,lam,True,start=U,maxiter=maxiter)
     spread1=abs(val1_alt-val1)
     if val1_alt<val1:val1,r1,d1=val1_alt,r1_alt,d1_alt
     # optimize cavity using all-coupled minimizer in case local minima differ
     val0_alt,r0_alt,d0_alt=optimize(U,lam,False,start=r1,maxiter=maxiter)
     spread0=abs(val0_alt-val0)
     if val0_alt<val0:val0,r0,d0=val0_alt,r0_alt,d0_alt
     defect=max(0.,val1-val0)
     states.append(U.copy())
     records.append({'lam':lam,'chain':chain,'sample':len(local_energies),'defect':defect,'E0':val0,'E1':val1,
      'cavity_action_sample':total_energy(U,lam,False),'raw_Q_action_sample':total_energy(U,lam,True)-total_energy(U,lam,False),
      'acc':acc,'opt0_grad_inf':d0['gradient_inf'],'opt1_grad_inf':d1['gradient_inf'],
      'opt0_success':d0['success'],'opt1_success':d1['success'],'optimizer_spread0':spread0,'optimizer_spread1':spread1,'opt0_iters':d0['nit'],'opt1_iters':d1['nit'],
      'minima_inconsistency':float(val1-val0)<-1e-5})
     accepted.append(acc);local_energies.append(defect)
     if len(local_energies)%5==0:
      print('λ',lam,'chain',chain,'n',len(local_energies),'defect median',float(np.median(local_energies)), 'elapsed',round(time.monotonic()-now,1),flush=True)
   diag.append({'lam':lam,'chain':chain,'acceptance_last':float(np.mean(accepted)),'defect_mean':float(np.mean(local_energies))})
   save(records,diag,states,meta={'sample_count_per_chain':samples,'chains':chains,'burn_sweeps':burn,'stride_sweeps':stride,'seed':seed,'maxiter':maxiter,'elapsed_seconds':time.monotonic()-now})
 save(records,diag,states,meta={'sample_count_per_chain':samples,'chains':chains,'burn_sweeps':burn,'stride_sweeps':stride,'seed':seed,'maxiter':maxiter,'elapsed_seconds':time.monotonic()-now})
 return records,diag
def save(records,diag,states,meta):
 (OUT/'raw_samples.json').write_text(json.dumps({'metadata':meta,'samples':records,'chains':diag},indent=2))
 def arr(field):return np.array([r[field] for r in records],dtype=float)
 np.savez_compressed(OUT/'sampled_gauge_configurations.npz',links=np.asarray(states),lam=arr('lam'),chain=np.array([r['chain'] for r in records],dtype=int),sample=np.array([r['sample'] for r in records],dtype=int),local_link_ids=L,exterior_link_ids=np.setdiff1d(np.arange(63),L))
 np.savez_compressed(OUT/'samples.npz',lam=arr('lam'),defect=arr('defect'),E0=arr('E0'),E1=arr('E1'),rawQ=arr('raw_Q_action_sample'),acc=arr('acc'),chain=np.array([r['chain'] for r in records],dtype=int))
def test_gradient():
 rng=np.random.default_rng(99);U=rng.normal(size=(63,4));U/=np.linalg.norm(U,axis=1)[:,None]
 for flag in (False,True):
  x=U[L].ravel().copy();v,g=gradfun(x,U,3.5,flag);i=20;eps=2.e-6;xp=x.copy();xm=x.copy();xp[i]+=eps;xm[i]-=eps
  fd=(gradfun(xp,U,3.5,flag)[0]-gradfun(xm,U,3.5,flag)[0])/(2*eps)
  print('gradient check',flag,v,g[i],fd,abs(g[i]-fd));assert abs(g[i]-fd)<1.e-7
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--lams',nargs='+',type=float,default=[1.,4.,12.,30.]);p.add_argument('--samples',type=int,default=18);p.add_argument('--burn',type=int,default=280);p.add_argument('--stride',type=int,default=15);p.add_argument('--chains',type=int,default=2);p.add_argument('--seed',type=int,default=20261027);p.add_argument('--maxiter',type=int,default=300);p.add_argument('--skipseed',type=int,default=0)
 a=p.parse_args();test_gradient();run(a.lams,a.samples,a.burn,a.stride,a.chains,a.seed,a.maxiter,a.skipseed)
