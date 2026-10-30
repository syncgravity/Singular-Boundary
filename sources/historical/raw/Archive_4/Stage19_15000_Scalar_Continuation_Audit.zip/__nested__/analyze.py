import os,zipfile,io,re,json,hashlib,numpy as np
from pathlib import Path
BASE=Path('/mnt/data'); OUT=BASE/'stage19_15k_audit';OUT.mkdir(exist_ok=True)
seeds=[101,211,307,419]; kinds=['square','penrose']; data={}; integrity={}
for kind in kinds:
 for seed in seeds:
  name=f'{kind}_seed{seed}'; path=BASE/(name+'.zip')
  with zipfile.ZipFile(path) as z:
   infos=[]; records=[]; names=[p for p in z.namelist() if re.search(r'observations_\d{8}_\d{8}\.npz$',p)];names.sort()
   latest=json.loads(z.read(f'{name}/latest.json'))
   for n in names:
    m=re.search(r'observations_(\d{8})_(\d{8})\.npz$',n)
    start,end=map(int,m.groups());a=np.load(io.BytesIO(z.read(n)),allow_pickle=False)
    obs=a['scalar']; sw=a['measured_sweeps']; full=a['aux_full_denominator'];na=int(a['accepted_anchors']); nt=int(a['all_anchors']); cat=str(a['catalogue_sha256'])
    assert obs.shape==(2,20,4) and np.isfinite(obs).all() and np.isfinite(full).all()
    assert np.allclose(full,obs[:,:,3]*na/nt,rtol=1e-12,atol=1e-12)
    assert np.array_equal(sw,[start+10,end]) and end-start==20
    infos.append((start,end,cat,na,nt));records.append(obs)
   assert len(infos)==245,(name,len(infos))
   assert infos[0][0]==10100 and infos[-1][1]==15000
   assert all(infos[i][1]==infos[i+1][0] for i in range(len(infos)-1))
   assert len(set((x[2],x[3],x[4]) for x in infos))==1
   assert latest['to_sweep']==15000 and latest['catalogue_sha256']==infos[0][2]
   joined=np.concatenate(records);assert joined.shape==(490,20,4)
   data[(kind,seed)]=joined
   integrity[name]={'segments':len(infos),'measurements':joined.shape[0],'first_sweep':10110,'last_sweep':15000,'accepted_anchors':na,'all_anchors':nt,'catalogue_sha256':cat,'zip_test_bad_file':z.testzip(),'latest_matches':True,'channels':list(a['channels'])}
 print(kind,'loaded')

def corr(series):
 # configuration ensemble connected circular correlator: mean_t O(t)O(t+lag) minus ensemble vacuum expectation squared
 mean=series.mean(axis=(0,1))
 return np.array([np.mean(series*np.roll(series,-t,axis=1),axis=(0,1))-mean**2 for t in range(11)]).T # (channel,time)

def boot(kind,block,reps=500,seed=30):
 rng=np.random.default_rng(seed+block); n=490
 features=[]
 for sd in seeds:
  c=data[(kind,sd)]
  means=c.mean(axis=1)
  products=np.stack([(c*np.roll(c,-t,axis=1)).mean(axis=1) for t in range(11)],axis=1)
  features.append(np.concatenate([means,products.reshape(n,-1)],axis=1))
 bs=[]
 for i in range(reps):
  sums=np.zeros(48)
  for f in features:
   starts=rng.integers(0,n,size=int(np.ceil(n/block)))
   inds=(starts[:,None]+np.arange(block)[None,:])%n
   sums+=f[inds.reshape(-1)[:n]].mean(axis=0)
  m=sums[:4]/4; prod=(sums[4:]/4).reshape(11,4)
  bs.append((prod-m[None,:]**2).T)
 return np.array(bs)
results={}
for kind in kinds:
 pooled=np.concatenate([data[(kind,s)] for s in seeds]); c=corr(pooled)
 single=np.stack([corr(data[(kind,s)]) for s in seeds]); residual=[]
 for block in (10,20,40,80):
  b=boot(kind,block)
  stderr=b.std(axis=0,ddof=1)
  snr=np.divide(c,stderr,out=np.full_like(c,np.nan),where=stderr>0)
  successes=[{'channel':int(i),'t':int(t),'snr':float(snr[i,t])} for i in range(4) for t in range(2,7) if snr[i,t]>2]
  trip=[{'channel':i,'start_t':t} for i in range(4) for t in range(2,5) if np.all(snr[i,t:t+3]>2)]
  residual.append({'block':block,'SE':stderr.tolist(),'SNR':snr.tolist(),'positive_two_sigma':successes,'three_time_windows':trip})
 results[kind]={'channels':['full_3face','full_5face','full_8face','strict_complete_aux'], 'mean_connected':c.tolist(),'per_chain_connected':single.tolist(),'blocks':residual,'timeslice_correlation':np.corrcoef(pooled.reshape(-1,4),rowvar=False).tolist(),'mean_operator_values':pooled.mean(axis=(0,1)).tolist()}
 print(kind,'t2-6 40block SNR',np.round(np.array(residual[2]['SNR'])[:,2:7],2))
result={'integrity':integrity,'analysis':results,'method':'Connected circular correlator C(t)=mean_{cfg,time}[O(time) O(time+t)]-(mean_{cfg,time} O)^2. Stationary block bootstrap resamples configurations with circular contiguous blocks within each of four independent chains. 600 replicates per block size; descriptive only.','caveats':['Four chains per geometry; finite sample autocorrelations remain uncertain.','Mass fit requires stable positive later-time correlators and model/window robustness.','Legacy masked and complete auxiliary datasets are not pooled.','Stage19 chains are descendants of Stage9 and not independent of Stage17/18 descendants.']}
(OUT/'RESULTS.json').write_text(json.dumps(result,indent=2))
print('wrote',OUT/'RESULTS.json')
