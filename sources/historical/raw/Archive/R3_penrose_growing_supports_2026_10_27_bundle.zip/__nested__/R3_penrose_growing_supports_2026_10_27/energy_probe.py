"""Exploratory SU(2) Wilson retained-plaquette energy diagnostic; finite MCMC only.
Physical SU2 quaternion links and Metropolis updates. Fixed support from original Penrose labels.
"""
import sys,json,csv,time,argparse
from pathlib import Path
import numpy as np
from numba import njit
SRC=Path(__file__).resolve().parent;sys.path.insert(0,str(SRC))
from nested_audit import build,seed_support,embed_support
from conditional_probe import make_graph,sweep,face_cos
OUT=Path(__file__).resolve().parent
@njit
def seed_numba(s):np.random.seed(s)
@njit
def energies(U,EW,SW,active):
 allsum=0.;actsum=0.;n=0
 for f in range(len(active)):
  d=1.-face_cos(U,EW,SW,f)
  if active[f]:actsum+=d;n+=1
  allsum+=d
 return actsum/n
@njit
def tagged_energy(U,EW,SW,indices):
 arr=np.empty(len(indices))
 for k,f in enumerate(indices):arr[k]=1.-face_cos(U,EW,SW,f)
 return arr

def sample(radius,lam,burn,stride,measures,chains,seed,mode):
 g,_=build(radius,0);gg,_=build(5,0);Qseed=seed_support(gg);_,Qedges=embed_support(Qseed,g)
 ew,sw,adj,degree,meta=make_graph(g)
 Q=[i for i,m in enumerate(meta) if m[0]=='t' and (m[1],m[2]) in Qedges]
 active=np.ones(len(ew),dtype=np.bool_);active[Q]=False
 face_centres=np.array([g.xy[list(f)].mean(axis=0) for f in g.faces]);p0=int(np.argmin(np.linalg.norm(face_centres,axis=1)))
 # time-slice 0, one selected spatial face and nearest four retained temporal faces not in Q
 selected=[p0]
 additional=[i for i,m in enumerate(meta) if m[0]=='t' and active[i] and np.linalg.norm(g.xy[list(g.edges[m[2]])].mean(axis=0))<1.8]
 selected+=additional[:4]
 rows=[]
 for ch in range(chains):
  seed_numba(seed+ch*10091+round(radius*100)+round(lam*89))
  U=np.zeros((len(degree),4));U[:,0]=1.
  if ch%2:
   U=np.random.normal(size=U.shape);U/=np.linalg.norm(U,axis=1)[:,None]
  vals=[];accs=[]
  for i in range(burn+stride*measures):
   acc=sweep(U,ew,sw,adj,degree,active,lam,.75/np.sqrt(max(lam/3.,1.)))
   if i>=burn and (i-burn+1)%stride==0:
    vals.append([energies(U,ew,sw,active),*tagged_energy(U,ew,sw,np.asarray(selected,np.int64))]);accs.append(acc)
  a=np.array(vals)
  for j,name in enumerate(['all_retained_mean','anchored_spatial_plaquette']+['nearby_retained_temporal_'+str(k) for k in range(len(selected)-1)]):
   rows.append({'radius':radius,'lambda':lam,'chain':ch,'observable':name,'sample_count':measures,'mean_d':float(a[:,j].mean()),'lambda_mean_d':float(lam*a[:,j].mean()),'within_chain_sd':float(a[:,j].std(ddof=1)),'mean_acceptance':float(np.mean(accs))})
 return rows

def main():
 p=argparse.ArgumentParser();p.add_argument('--radii',nargs='+',type=float,default=[5.,6.5,8.,10.]);p.add_argument('--lambdas',nargs='+',type=float,default=[2.,4.,8.,16.]);p.add_argument('--burn',type=int,default=180);p.add_argument('--stride',type=int,default=9);p.add_argument('--samples',type=int,default=24);p.add_argument('--chains',type=int,default=2)
 a=p.parse_args(); rows=[];tic=time.time()
 for lam in a.lambdas:
  for r in a.radii:
   rows.extend(sample(r,lam,a.burn,a.stride,a.samples,a.chains,20261027,None)); print('lambda',lam,'radius',r,'elapsed',round(time.time()-tic,1),flush=True)
   with (OUT/'energy_probe.csv').open('w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 with (OUT/'energy_probe.csv').open('w',newline='') as fh:
  w=csv.DictWriter(fh,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (OUT/'energy_probe_metadata.json').write_text(json.dumps({'scope':'Exploratory retained-cavity MCMC, not certified equilibrium or uniform energy estimate','configuration':vars(a),'rows':len(rows)},indent=2))
if __name__=='__main__':main()
