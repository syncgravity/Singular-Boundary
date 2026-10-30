import os,glob,zipfile,io,json,re,hashlib
import numpy as np
D='/mnt/data/stage18_audit'; seeds=[101,211,307,419]; kinds=['square','penrose']
X={}; integrity=[]
for kind in kinds:
 for seed in seeds:
  path=f'/mnt/data/{kind}_scalar_seed{seed}.zip'; vals=[]; sweeps=[]
  with zipfile.ZipFile(path) as z:
   prefix=f'{kind}_seed{seed}/'; latest=json.loads(z.read(prefix+'latest.json'))
   names=sorted(n for n in z.namelist() if re.search(r'observations_\d+_\d+\.npz$',n))
   intervals=[]; hashes=[]
   for n in names:
    m=re.search(r'observations_(\d+)_(\d+)\.npz$',n); a,b=map(int,m.groups());intervals.append((a,b)); raw=z.read(n); hashes.append(hashlib.sha256(raw).hexdigest()); arr=np.load(io.BytesIO(raw),allow_pickle=False)
    assert str(arr['kind'])==kind and int(arr['seed'])==seed
    assert arr['observables_scalar'].shape==(10,20,12)
    assert np.array_equal(arr['levels'],[0,2,6,12])
    ss=arr['measured_sweeps']; assert np.array_equal(ss,np.arange(a+10,b+1,10))
    vals.append(arr['observables_scalar']);sweeps.append(ss)
   assert len(names)==20 and intervals==[(10000+i*100,10100+i*100) for i in range(20)]
   assert latest['end']==12000 and hashes[-1]==latest['segment_sha256']
   X[kind,seed]=np.concatenate(vals)
   integrity.append(dict(kind=kind,seed=seed,segments=len(names),n=len(np.concatenate(sweeps)),start=int(np.concatenate(sweeps)[0]),end=int(np.concatenate(sweeps)[-1]),cache_error=latest['max_plaquette_cache_error'],verified_latest_sha=True))
print('loaded',[(k,v.shape) for k,v in X.items()])

def corr(y,maxlag=8):
 # y: (ncfg, nt, nop), calculate ensemble mean subtraction, with circular timeslice average
 avg=y.mean(axis=(0,1),keepdims=True); a=y-avg
 return np.array([np.mean(a*np.roll(a,-t,axis=1),axis=(0,1)) for t in range(maxlag+1)])

def se_boot(y, block=20,reps=600,seed=127):
 rng=np.random.default_rng(seed); N=y.shape[0]; nb=N//block; assert nb>=4
 chunk=y[:nb*block].reshape(nb,block,y.shape[1],y.shape[2]); result=np.empty((reps,9,y.shape[2]))
 for i in range(reps):
  ix=rng.integers(0,nb,size=nb); result[i]=corr(chunk[ix].reshape(-1,y.shape[1],y.shape[2]))
 return np.std(result,axis=0,ddof=1),np.percentile(result,[2.5,97.5],axis=0)

results={'integrity':integrity,'analysis':{}}
for kind in kinds:
 y=np.concatenate([X[kind,s] for s in seeds]); c=corr(y); stderr={};cis={}
 for b in [5,10,20,40]:
  # four chains independently sampled blocks -- balanced
  chunks=np.array([X[kind,s].reshape(200//b,b,20,12) for s in seeds])
  rng=np.random.default_rng(700+b); reps=400; bt=np.empty((reps,9,12))
  for i in range(reps):
   samples=[]
   for j in range(4):
    ids=rng.integers(0,200//b,size=200//b)
    samples.append(chunks[j,ids].reshape(200,20,12))
   bt[i]=corr(np.concatenate(samples))
  stderr[str(b)]=np.std(bt,axis=0,ddof=1);cis[str(b)]=np.percentile(bt,[2.5,97.5],axis=0)
 snr=c/(stderr['20']+1e-100)
 report={'n':len(y),'levels':[0,2,6,12],'corr':c.tolist(),'se_by_block':{b:err.tolist() for b,err in stderr.items()}, 'snr20':snr.tolist(),'positive_2sigma_t2_6':(snr[2:7]>2).sum(axis=0).tolist(),'max_consecutive_positive2sigma_t2_6':[],'leave_one_chain_out_corr_t2_5':{str(s):corr(np.concatenate([X[kind,t] for t in seeds if t!=s]))[2:6].tolist() for s in seeds}}
 for op in range(12):
  ok=(snr[2:7,op]>2); mx=cur=0
  for v in ok: cur=cur+1 if v else 0;mx=max(mx,cur)
  report['max_consecutive_positive2sigma_t2_6'].append(mx)
 results['analysis'][kind]=report
 print(kind,'t2-6 best SNR',[round(float(np.max(snr[t])),2) for t in range(2,7)])
 print('counts t2-6',[(t,int(np.sum(snr[t]>2))) for t in range(2,7)],'maxseq',max(report['max_consecutive_positive2sigma_t2_6']))
 print('new level 12',[(t,[round(float(v),2) for v in snr[t,9:12]]) for t in range(2,7)])
with open(D+'/RESULTS.json','w') as f:json.dump(results,f,indent=2,allow_nan=False)
