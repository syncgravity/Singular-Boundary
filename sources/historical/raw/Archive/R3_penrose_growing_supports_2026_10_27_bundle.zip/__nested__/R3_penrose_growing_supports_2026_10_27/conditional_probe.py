#!/usr/bin/env python3
"""Exploratory local-conditional SU2 curvature frustration across genuine Penrose volumes.
This is numerical MCMC + local optimization only, not certified global minima / uniform theorem.
"""
import numpy as np,json,sys,collections,time,argparse
from pathlib import Path
from scipy.optimize import minimize
from numba import njit
from nested_audit import build,seed_support,embed_support,complex_3
from extended_audit import get_star_seed,get_star_Q
ROOT=Path(__file__).resolve().parent
@njit
def mul(a,b):
 z=np.empty(4,np.float64);z[0]=a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3];z[1]=a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2];z[2]=a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1];z[3]=a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0];return z
@njit
def dagger(a):
 v=a.copy();v[1:]*=-1;return v
@njit
def eye():
 z=np.zeros(4);z[0]=1.;return z
@njit
def face_cos(U,EW,SW,f):
 z=eye()
 for j in range(4):
  e=EW[f,j];z=mul(z,U[e] if SW[f,j]>0 else dagger(U[e]))
 return z[0]
@njit
def sweep(U,EW,SW,adj,deg,active,lam,step_size):
 accepted=0
 for e in np.random.permutation(len(U)):
  vec=np.random.normal(0.,1.,3);vec/=np.sqrt((vec*vec).sum());theta=np.random.normal()*step_size
  rot=np.empty(4);rot[0]=np.cos(theta);rot[1:]=np.sin(theta)*vec
  prop=mul(rot,U[e]);vold=0.;vnew=0.
  for j in range(deg[e]):
   f=adj[e,j]
   if not active[f]:continue
   vold+=face_cos(U,EW,SW,f)
  old=U[e].copy();U[e]=prop
  for j in range(deg[e]):
   f=adj[e,j]
   if not active[f]:continue
   vnew+=face_cos(U,EW,SW,f)
  delta=-lam*(vnew-vold)
  if delta<=0 or np.random.random()<np.exp(-delta):accepted+=1
  else:U[e]=old
 return accepted/len(U)
@njit
def val_grad(U,EW,SW,active,isl):
 value=0.;grad=np.zeros((len(U),4))
 for f in range(len(active)):
  if not active[f]:continue
  pre=np.zeros((5,4));post=np.zeros((5,4));vv=np.empty((4,4))
  pre[0,0]=1.;post[4,0]=1.
  for j in range(4):
   e=EW[f,j];vv[j]=U[e] if SW[f,j]>0 else dagger(U[e]);pre[j+1]=mul(pre[j],vv[j])
  for j in range(3,-1,-1):post[j]=mul(vv[j],post[j+1])
  value+=1.-pre[4,0]
  for j in range(4):
   e=EW[f,j]
   if not isl[e]:continue
   for k in range(4):
    basis=np.zeros(4);basis[k]=1. if (k==0 or SW[f,j]>0) else -1.
    grad[e,k]-=mul(mul(pre[j],basis),post[j+1])[0]
 return value,grad

def make_graph(g):
 V,E,F=len(g.labels),len(g.edges),len(g.faces);N=3*(V+E);NF=3*(E+F)
 ix={tuple(sorted(e)):i for i,e in enumerate(g.edges)}
 ew=[];sw=[];meta=[]
 for t in range(3):
  for fi,face in enumerate(g.faces):
   es=[];sign=[]
   for a,b in zip(face,face[1:]+face[:1]):es.append(t*E+ix[tuple(sorted((a,b)))]);sign.append(1 if a<b else -1)
   ew.append(es);sw.append(sign);meta.append(('s',t,fi))
 for t in range(3):
  for e,(a,b) in enumerate(g.edges):
   ew.append([t*E+e,3*E+t*V+b,((t+1)%3)*E+e,3*E+t*V+a]);sw.append([1,1,-1,-1]);meta.append(('t',t,e))
 assert len(ew)==NF
 ew=np.asarray(ew,dtype=np.int64);sw=np.asarray(sw,dtype=np.int64)
 neighbors=[[] for i in range(N)]
 for f in range(NF):
  for e in ew[f]:neighbors[e].append(f)
 maxdeg=max(map(len,neighbors));adj=np.full((N,maxdeg),-1,np.int64);deg=np.asarray(list(map(len,neighbors)),np.int64)
 for i,fs in enumerate(neighbors):adj[i,:len(fs)]=fs
 return ew,sw,adj,deg,meta

def opt(U,EW,SW,Q,L,lam,insert,start=None,maxiter=180):
 isl=np.zeros(len(U),dtype=np.bool_);isl[L]=True
 # Include only faces touching any local link. Other face energies cancel between minima.
 active=np.zeros(len(EW),dtype=np.bool_)
 active[np.unique(np.flatnonzero(np.isin(EW,L).any(axis=1)))]=True
 if not insert:active[Q]=False
 xx=U[L].ravel() if start is None else start[L].ravel()
 def fgrad(x):
  zz=x.reshape((-1,4));nn=np.linalg.norm(zz,axis=1);Qloc=zz/nn[:,None]
  V=U.copy();V[L]=Qloc
  v,g=val_grad(V,EW,SW,active,isl)
  g=g[L];g=(g-np.sum(g*Qloc,axis=1)[:,None]*Qloc)/nn[:,None]
  return lam*v,(lam*g).ravel()
 sol=minimize(fgrad,xx,method='L-BFGS-B',jac=True,options={'maxiter':maxiter,'ftol':1e-11,'gtol':1e-6})
 result=U.copy();vec=sol.x.reshape((-1,4));result[L]=vec/np.linalg.norm(vec,axis=1)[:,None]
 return float(sol.fun),result,{'success':bool(sol.success),'grad':float(np.linalg.norm(sol.jac,ord=np.inf)),'iter':int(sol.nit)}

def run(r,lam,samples,burn,stride,chains,seed,maxiter):
 g,_=build(r,0);ew,sw,adj,deg,meta=make_graph(g)
 src,_=build(5.,0);s14=seed_support(src);s8=get_star_seed(src)
 _,supp14=embed_support(s14,g);supp8=get_star_Q(g,s8)
 supports={'overlapping14':supp14,'star8':supp8};q={name:np.array([i for i,m in enumerate(meta) if m[0]=='t' and (m[1],m[2]) in supp],np.int64) for name,supp in supports.items()}
 L={name:np.unique(ew[qv].ravel()) for name,qv in q.items()}
 records=[];now=time.monotonic()
 for name in ('overlapping14','star8'):
  active=np.ones(len(ew),np.bool_);active[q[name]]=False
  for chain in range(chains):
   np.random.seed(seed+chain*1789+int(r*1000)+int(lam*101)+(0 if name=='overlapping14' else 31013))
   U=np.zeros((len(deg),4));U[:,0]=1.
   if chain%2:
    U=np.random.normal(size=U.shape);U/=np.linalg.norm(U,axis=1)[:,None]
   for i in range(burn+samples*stride):
    acc=sweep(U,ew,sw,adj,deg,active,lam,.75/np.sqrt(max(lam/3.,1.)))
    if i>=burn and (i-burn+1)%stride==0:
     rec={'r':r,'lambda':lam,'support':name,'chain':chain,'sample':(i-burn+1)//stride-1,'acc':float(acc)}
     e0,u0,di0=opt(U,ew,sw,q[name],L[name],lam,False,maxiter=maxiter)
     e1,u1,di1=opt(U,ew,sw,q[name],L[name],lam,True,start=u0,maxiter=maxiter)
     e1b,u1b,di1b=opt(U,ew,sw,q[name],L[name],lam,True,start=U,maxiter=maxiter)
     if e1b<e1:e1=e1b;u1=u1b
     e0b,_,di0b=opt(U,ew,sw,q[name],L[name],lam,False,start=u1,maxiter=maxiter)
     e0=min(e0,e0b)
     rec.update(defect=float(max(0,e1-e0)),optgrad=max(di0['grad'],di1['grad'],di1b['grad'],di0b['grad']),
           maxiter_hit=int(max(di0['iter'],di1['iter'],di1b['iter'],di0b['iter'])>=maxiter),
           min_diff_warning=bool(e1-e0<-1e-5))
     records.append(rec)
   print('radius',r,'λ',lam,'support',name,'chain',chain,'totalrecords',len(records),'elapsed',round(time.monotonic()-now,1),flush=True)
 return records

def main():
 p=argparse.ArgumentParser();p.add_argument('--radii',nargs='+',type=float,default=[5.,6.5,8.,10.]);p.add_argument('--lambdas',nargs='+',type=float,default=[8.]);p.add_argument('--samples',type=int,default=5);p.add_argument('--burn',type=int,default=130);p.add_argument('--stride',type=int,default=20);p.add_argument('--chains',type=int,default=2);p.add_argument('--seed',type=int,default=20261027);p.add_argument('--maxiter',type=int,default=110)
 args=p.parse_args();R=[]
 for lam in args.lambdas:
  for r in args.radii:
   R.extend(run(r,lam,args.samples,args.burn,args.stride,args.chains,args.seed,args.maxiter));(ROOT/'conditional_samples.json').write_text(json.dumps({'metadata':vars(args),'results':R,'scope':'exploratory MCMC and local nonconvex optimizer, not a theorem or certified minima'},indent=2))
 print('saved',len(R),'records',flush=True)
if __name__=='__main__':main()
