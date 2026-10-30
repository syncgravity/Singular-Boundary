#!/usr/bin/env python3
"""Pilot of exact NONABELIAN 59-pivot flat transport under actual retained Wilson Gibbs measure.
Two cold/hot starts; not a certified stationary sampler or a theorem.
"""
import sys, json, argparse, time
from pathlib import Path
import numpy as np
from numba import njit
SRC=Path(__file__).resolve().parent;sys.path.insert(0,str(SRC))
from direct_cut_project import build
from construct_surgery import product_collar
from cavity_audit import seed_support,Q_from_seed
from relative_words import solve
ROOT=Path(__file__).resolve().parent
@njit
def qmul(a,b):
 r=np.empty(4)
 r[0]=a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3]
 r[1]=a[0]*b[1]+b[0]*a[1]+a[2]*b[3]-a[3]*b[2]
 r[2]=a[0]*b[2]+b[0]*a[2]+a[3]*b[1]-a[1]*b[3]
 r[3]=a[0]*b[3]+b[0]*a[3]+a[1]*b[2]-a[2]*b[1]
 return r
@njit
def dagger(a):
 r=a.copy();r[1:]*=-1;return r
@njit
def face_deficit(U,edges,signs,f):
 z=np.zeros(4);z[0]=1.
 for j in range(4):
  e=edges[f,j]
  if signs[f,j]>0:z=qmul(z,U[e])
  else:z=qmul(z,dagger(U[e]))
 return 1.-z[0]
@njit
def evaluate(U,edges,signs,fs):
 x=0.
 for f in fs:x+=face_deficit(U,edges,signs,f)
 return x
@njit
def seedrng(seed):np.random.seed(seed)
@njit
def sweep(U,edges,signs,adj,deg,lam,scale):
 accept=0
 for e in np.random.permutation(len(U)):
  v=np.random.normal(0.,1.,3);v/=np.sqrt((v*v).sum());theta=np.random.normal(0.,scale)
  rot=np.empty(4);rot[0]=np.cos(theta);rot[1:]=np.sin(theta)*v
  old=U[e].copy();before=0.
  for j in range(deg[e]):before+=face_deficit(U,edges,signs,adj[e,j])
  U[e]=qmul(rot,old);after=0.
  for j in range(deg[e]):after+=face_deficit(U,edges,signs,adj[e,j])
  cost=lam*(after-before)
  if cost<=0 or np.random.random()<np.exp(-cost):accept+=1
  else:U[e]=old
 return accept/len(U)
@njit
def repair(U,op_edges,offsets,w):
 V=U.copy()
 for ii in range(len(op_edges)-1,-1,-1):
  z=np.zeros(4);z[0]=1.
  for j in range(offsets[ii],offsets[ii+1]):
   t=w[j];e=abs(t)-1
   if t>0:z=qmul(z,V[e])
   else:z=qmul(z,dagger(V[e]))
  V[op_edges[ii]]=z
 return V

@njit
def geodesic_contraction(U,V, pivots,tau):
 W=U.copy()
 for e in pivots:
  theta=np.arccos(max(-1.,min(1.,np.dot(U[e],V[e]))))
  if theta<1e-7:
   r=(1.-tau)*U[e]+tau*V[e]
  elif theta>np.pi-1e-7:
   r=(1.-tau)*U[e]+tau*V[e]
  else:
   r=(np.sin((1.-tau)*theta)*U[e]+np.sin(tau*theta)*V[e])/np.sin(theta)
  W[e]=r/np.linalg.norm(r)
 return W

def arrays(words,R):
 E=np.array([[e for e,s in words[f]] for f in R],dtype=np.int64)
 S=np.array([[s for e,s in words[f]] for f in R],dtype=np.int64)
 # note face ids in array are local R indices
 n=int(E.max())+1
 incident=[[] for _ in range(n)]
 for i,face in enumerate(E):
  for e in face:incident[e].append(i)
 m=max(map(len,incident));AD=np.zeros((n,m),dtype=np.int64);deg=np.array(list(map(len,incident)),dtype=np.int64)
 for e,fs in enumerate(incident):AD[e,:len(fs)]=fs
 return E,S,AD,deg

def experiment(radius,lambdas,samples,burn,stride,seed):
 g,_=build(radius,0);W,_=product_collar(g);Q=Q_from_seed(g,seed_support(build(5.,0)[0]));R=sorted(set(range(len(W)))-Q)
 H={e for q in Q for e,s in W[q]};A=sorted(f for f in R if any(e in H for e,s in W[f]))
 base,_=build(5.,0);ops=solve(True,optimized=True,radius=5.)['operations']
 if radius!=5:
  from classify_modes import link_key
  maplink={str(link_key(g,e)):e for e in range(3*(len(g.labels)+len(g.edges)))}
  def mp(e):return maplink[str(link_key(base,e))]
  r_ops=[{'edge':mp(o['edge']), 'replacement_word':[np.sign(t)*(mp(abs(t)-1)+1) for t in o['replacement_word']]} for o in ops]
 else:r_ops=ops
 solved={o['edge'] for o in r_ops};X={e for e in solved if e not in H}
 crossing=sorted(f for f in R if f not in A and any(e in X for e,s in W[f]));assert len(crossing)==33
 earr,sarr,adj,deg=arrays(W,R);n=3*(len(g.labels)+len(g.edges));
 assert n==len(adj)
 lookup={f:i for i,f in enumerate(R)};AF=np.asarray([lookup[f] for f in A],np.int64);CF=np.asarray([lookup[f] for f in crossing],np.int64)
 oed=np.array([o['edge'] for o in r_ops],np.int64);ww=np.array([t for o in r_ops for t in o['replacement_word']],np.int64);offset=np.array([0]+list(np.cumsum([len(o['replacement_word']) for o in r_ops])),np.int64)
 data=[]
 for lam in lambdas:
  for chain in range(2):
   seedrng(seed+chain*113+int(lam*19)+int(radius*37));U=np.zeros((n,4));U[:,0]=1.
   if chain:
    U=np.random.normal(0.,1.,size=(n,4));U/=np.linalg.norm(U,axis=1)[:,None]
   for i in range(burn+samples*stride):
    acc=sweep(U,earr,sarr,adj,deg,lam,.65/np.sqrt(max(lam/3.,1.)))
    if i>=burn and (i-burn+1)%stride==0:
     V=repair(U,oed,offset,ww)
     a=evaluate(U,earr,sarr,AF);post=evaluate(V,earr,sarr,AF)
     cross=evaluate(V,earr,sarr,CF)-evaluate(U,earr,sarr,CF)
     assert post<1e-9,('A not flat!',post)
     rec={'radius':radius,'lambda':lam,'chain':chain,'sample':(i-burn+1)//stride-1,'acceptance':float(acc),'lambda_A_before':float(lam*a),'lambda_crossing_cost':float(lam*cross),'lambda_full_action_decrease':float(lam*(a-cross)), 'lambda_cross_positive':float(lam*max(cross,0))}
     for tau in (0.1,0.25,0.5,0.75):
      Vtau=geodesic_contraction(U,V,oed,tau)
      a_t=evaluate(Vtau,earr,sarr,AF);cross_t=evaluate(Vtau,earr,sarr,CF)-evaluate(U,earr,sarr,CF)
      rec['lambda_action_decrease_tau_'+str(tau)]=float(lam*(a-a_t-cross_t))
      rec['lambda_A_after_tau_'+str(tau)]=float(lam*a_t)
      rec['lambda_crossing_cost_tau_'+str(tau)]=float(lam*cross_t)
     data.append(rec)
   print('radius',radius,'lambda',lam,'chain',chain,'n',len(data),flush=True)
 return data

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--radii',nargs='+',type=float,default=[5.,6.5]);p.add_argument('--lambdas',nargs='+',type=float,default=[8.,16.,32.]);p.add_argument('--burn',type=int,default=160);p.add_argument('--stride',type=int,default=15);p.add_argument('--samples',type=int,default=15);p.add_argument('--seed',type=int,default=20261027)
 opt=p.parse_args();out=[]
 for rad in opt.radii:
  out.extend(experiment(rad,opt.lambdas,opt.samples,opt.burn,opt.stride,opt.seed));(ROOT/'wilson_crossing_geodesic_samples.json').write_text(json.dumps({'scope':'Exploratory compact-Haar retained Wilson measure; two short cold/hot chains, not a stationary-law certificate','sampling':vars(opt),'samples':out},indent=2))
 print('DONE',len(out),'samples',flush=True)
