import zipfile,io,hashlib,json,re,numpy as np
from pathlib import Path
Z=Path('/mnt/data/stage19_pilot_results.zip'); z=zipfile.ZipFile(Z)
seeds=[101,211,307,419]; kinds=['square','penrose']; data={}; results={}; integrity=[]
for kind in kinds:
 data[kind]=[]
 for seed in seeds:
  base=f'stage19_pilot_results/{kind}_seed{seed}/'
  j=json.loads(z.read(base+'latest.json'))
  names=sorted(n for n in z.namelist() if n.startswith(base+'observations_') and n.endswith('.npz'))
  assert len(names)==5, (kind,seed,len(names))
  ss=[]; times=[]; scalar=[]; aux=[]; hashes=[]; accepted=[]; totals=[]; channels=[]
  for name in names:
   m=re.search(r'observations_(\d+)_(\d+)\.npz',name); a,b=map(int,m.groups()); ss.append((a,b))
   raw=z.read(name); hashes.append(hashlib.sha256(raw).hexdigest())
   with np.load(io.BytesIO(raw)) as x:
    scalar.append(x['scalar']); aux.append(x['aux_full_denominator']); times.extend(x['measured_sweeps'].tolist());accepted.append(int(x['accepted_anchors']));totals.append(int(x['all_anchors']));channels.append(list(x['channels'].astype(str)))
    assert x['scalar'].shape==(2,20,4) and x['aux_full_denominator'].shape==(2,20)
    assert str(x['catalogue_sha256'])==j['catalogue_sha256'] and str(x['source_sha256'])==j['source_checkpoint_sha256']
  assert ss==[(10000+20*i,10020+20*i) for i in range(5)]
  assert times==list(range(10010,10101,10))
  assert hashes[-1]==j['segment_sha256']
  assert len(set(accepted))==len(set(totals))==len(set(tuple(c) for c in channels))==1
  n=np.concatenate(scalar); au=np.concatenate(aux)
  assert np.isfinite(n).all() and np.isfinite(au).all()
  assert np.max(abs(au-n[:,:,3]*(accepted[0]/totals[0])))<1e-12
  data[kind].append(n)
  integrity.append({'kind':kind,'seed':seed,'segments':len(names),'observations':len(times),'final_sweep':times[-1],'accepted':accepted[0],'total':totals[0],'aux_mask_identity_max':float(np.max(abs(au-n[:,:,3]*(accepted[0]/totals[0])))),'channels':channels[0]})
# per chain all configurations 10x20x4, connected time-averaged correlation at lag t
# unbiased across separate gauge observations when subtracting mean for each timeslice channel (global ensemble baseline)
def connected(x):
 # x: configurations x timeslice x channels
 mean=x.mean(axis=(0,1),keepdims=True)
 y=x-mean
 return np.array([np.mean(y*np.roll(y,-t,axis=1),axis=(0,1)) for t in range(11)])
# bootstrap preserving 4 chains, 2-config blocks: five blocks per chain with replacement
rng=np.random.default_rng(19419)
for kind in kinds:
 X=np.stack(data[kind]) # chain,configuration,time,channel
 x=X.reshape(40,20,4)
 corr=connected(x)
 nboot=1800; bs=np.empty((nboot,11,4))
 for i in range(nboot):
  sel=np.concatenate([X[c].reshape(5,2,20,4)[rng.integers(5,size=5)] for c in range(4)],axis=0).reshape(40,20,4)
  bs[i]=connected(sel)
 se=bs.std(axis=0,ddof=1)
 chmean=X.mean(axis=(0,1,2)); chstd=X.std(axis=(0,1,2),ddof=1)
 pear=np.corrcoef(x.reshape(-1,4),rowvar=False)
 jack=[]
 for c in range(4):jack.append(connected(np.concatenate([X[u] for u in range(4) if u!=c])))
 # sequential t>=2 with SNR >=2 and c>0, per-channel (not prescriptive actual fits)
 snr=np.divide(corr,se,out=np.zeros_like(corr),where=se>0)
 results[kind]={'observations':40,'timeslices':20,'channel_mean':chmean.tolist(),'channel_std_timeslice':chstd.tolist(), 'correlations_timeslice':pear.tolist(),'connected':corr.tolist(),'bootstrap_se_block2':se.tolist(),'snr':snr.tolist(), 'leave_one_chain_connected':np.array(jack).tolist(),'positive_two_sigma_t2_6':(snr[2:7]>2).astype(int).tolist(),'bootstrap_replicates':nboot}
Path('/mnt/data/stage19_pilot_audit/RESULTS.json').write_text(json.dumps({'integrity':integrity,'results':results},indent=2))
print('integrity',len(integrity));
for kind in kinds:
 print(kind,'mean',np.round(results[kind]['channel_mean'],5))
 print(kind,'lag2..6 SNR:\n',np.round(np.array(results[kind]['snr'])[2:7],2))
 print(kind,'corr aux controls',np.round(np.array(results[kind]['correlations_timeslice'])[-1,:-1],3))
