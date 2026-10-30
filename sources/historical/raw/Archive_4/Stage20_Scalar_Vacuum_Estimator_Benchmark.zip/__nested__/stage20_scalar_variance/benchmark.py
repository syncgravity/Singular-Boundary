"""Stage20: cross-chain-disconnected scalar benchmark on Stage19 observations.

This is NOT a multilevel gauge estimator. Assumes independent chains share stationary law.
"""
import io, json, zipfile, hashlib, argparse
from pathlib import Path
import numpy as np
SEEDS=(101,211,307,419); GEOMS=('square','penrose')

def read_chain(root,g,s):
 zpath=root/f'{g}_seed{s}.zip'; seq=[]; steps=[]; sha=set(); nfiles=0
 with zipfile.ZipFile(zpath) as z:
  names=sorted(n for n in z.namelist() if 'observations_' in n and n.endswith('.npz'))
  for n in names:
   with np.load(io.BytesIO(z.read(n)),allow_pickle=False) as f:
    seq.append(f['scalar'].astype(np.float64)); steps.extend(f['measured_sweeps'].tolist()); sha.add(str(f['catalogue_sha256']))
   nfiles+=1
 a=np.concatenate(seq);steps=np.asarray(steps)
 assert a.shape==(490,20,4) and np.array_equal(steps,np.arange(10110,15001,10))
 assert len(sha)==1 and np.isfinite(a).all()
 # per-config timeslice mean, and timeslice paired products
 m=a.mean(axis=1)
 p=np.stack([(a*np.roll(a,-t,axis=1)).mean(axis=1) for t in range(8)],axis=1)
 return m,p,{'zip':pstr(pth=zpath),'segments':nfiles,'catalogue_sha256':next(iter(sha)),'start':int(steps[0]),'end':int(steps[-1])}

def pstr(pth):return pth.name

def estimators(m,p):
 # m (chains,configs,channels), p(chains,configs,t,channels)
 mu=m.mean(axis=1); mu_all=mu.mean(axis=0)
 raw=p.mean(axis=(0,1))
 plugin=raw-mu_all[None,:]**2
 cross=(np.sum(mu,axis=0)**2-np.sum(mu**2,axis=0))/(len(mu)*(len(mu)-1))
 cross=raw-cross[None,:]
 return plugin,cross,mu

def boot(m,p,block,reps=400,seed=0):
 rng=np.random.default_rng(seed); nch,ncfg,k=m.shape; nb=(ncfg+block-1)//block
 off=np.arange(block)
 plug=np.empty((reps,8,k)); cross=np.empty_like(plug)
 for r in range(reps):
  idx=(rng.integers(ncfg,size=(nch,nb))[:,:,None]+off[None,None,:])%ncfg
  idx=idx.reshape(nch,-1)[:,:ncfg]
  mb=np.take_along_axis(m,idx[:,:,None],axis=1)
  pb=np.take_along_axis(p,idx[:,:,None,None],axis=1)
  plug[r],cross[r],_=estimators(mb,pb)
 return plug,cross

def audit(root,out,reps=400):
 result={'method':{'data':'Stage19 complete-strict auxiliary and three full-volume scalar controls; independent chain identities','assumptions':'four chains independent and drawn from same stationary equilibrium distribution; nonstationarity and finite effective sample remain possible','plug_in':'E[xy]-E_sample[x]E_sample[y] over same ensemble','cross_chain':'E[xy] - average_{c != d}(mu_c * mu_d), exactly separates vacuum estimates by independent chains','cross_chain_unbiasedness':'For independent stationary chains with common mean, cross-chain disconnected estimator is unbiased even with within-chain autocorrelation. Ensemble product estimator also unbiased under stationarity.','bootstrap':'circular moving block within each chain; resampling joint per-configuration means and products; does not establish thermalization','scientific_gate':'three consecutive positive 2 SE points t=2..6 in same channel across all bootstrap blocks 10,20,40,80; not mass alone'},'geometries':{},'sources':{}}
 for g in GEOMS:
  records=[read_chain(root,g,s) for s in SEEDS]
  m=np.stack([r[0] for r in records]);p=np.stack([r[1] for r in records]);
  result['sources'][g]={str(s):r[2] for s,r in zip(SEEDS,records)}
  plug,cross,mu=estimators(m,p)
  gobj={'channel_names':['3_face_full','5_face_full','8_face_full','strict_complete_aux'],'observed':{'plugin':plug.tolist(),'cross_chain':cross.tolist(),'difference':(cross-plug).tolist()},'chain_vacuum_means':mu.tolist(),'bootstrap':{}}
  for b in (10,20,40,80):
   bp,bc=boot(m,p,b,reps,seed=20261018+b)
   tmp={}
   for name,obs,draws in [('plugin',plug,bp),('cross_chain',cross,bc)]:
    se=draws.std(axis=0,ddof=1); z=np.divide(obs,se,out=np.zeros_like(obs),where=se>0)
    passed=[{'channel':int(k),'start_t':int(t)} for k in range(4) for t in (2,3,4) if np.all(z[t:t+3,k]>=2)]
    tmp[name]={'se':se.tolist(),'snr':z.tolist(),'three_consecutive_t2_6':passed,'maximum_t2_6_snr':float(z[2:7].max())}
   diff=bc-bp
   tmp['estimator_difference']={'mean':(cross-plug).tolist(),'bootstrap_se':diff.std(axis=0,ddof=1).tolist(),'within_bootstrap_correlation_t2':np.array([np.corrcoef(bp[:,2,k],bc[:,2,k])[0,1] for k in range(4)]).tolist()}
   gobj['bootstrap'][str(b)]=tmp
  result['geometries'][g]=gobj
  print(g,'means at t2',cross[2], 'SNR at t2', np.asarray(gobj['bootstrap']['40']['cross_chain']['snr'])[2],flush=True)
 out.mkdir(parents=True,exist_ok=True)
 (out/'RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False))
 return result

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path('/mnt/data'));ap.add_argument('--out',type=Path,default=Path('/mnt/data/stage20_scalar_variance'));ap.add_argument('--reps',type=int,default=400); a=ap.parse_args();audit(a.root,a.out,a.reps)
