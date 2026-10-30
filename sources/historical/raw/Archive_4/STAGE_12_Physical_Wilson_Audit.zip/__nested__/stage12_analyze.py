import numpy as np,json
from pathlib import Path
rng=np.random.default_rng(12012)
root=Path('/mnt/data')
bins=np.array([0.5,.9,1.2,1.5,1.8,2.1,2.4,2.7,3.0])
out={}
for kind in ('square','penrose'):
 pp=np.load(root/f'STAGE12_{kind}_paths.npz'); r=pp['r']; dx=pp['dx']; phi=np.arctan2(dx[:,1],dx[:,0])%np.pi
 W=np.stack([np.load(root/f'{kind}_nt20_seed{s}.npz')['observables_wilson'][:,1,:,:] for s in (101,211,307,419)]) # (4,900,100,10)
 # bootstrap all paths bin averaged, with complete within-chain blocks of 20
 print(kind,'shape',W.shape,'finite',np.isfinite(W).all(),flush=True)
 blocks=W.reshape(4,45,20,100,10).mean(axis=2)
 results=[]
 for i in range(len(bins)-1):
  mask=(r>=bins[i])&(r<bins[i+1]); n=int(mask.sum())
  if n<2:continue
  # each chain block = within-block averaged paths, preserving all correlations
  b=blocks[:,:,mask,:].mean(axis=2)
  mean=b.mean(axis=(0,1)); nb=4*45
  bs=np.empty((500,10))
  for k in range(500):
   ids=rng.integers(0,45,size=(4,45));bs[k]=b[np.arange(4)[:,None],ids].mean(axis=(0,1))
  se=bs.std(axis=0,ddof=1)
  energies={}
  for t in range(2,9): # W index t-1
   x=mean[t-1];y=mean[t]; valid=(bs[:,t-1]>0)&(bs[:,t]>0)
   ev=np.log(x/y) if x>0 and y>0 else None
   gev=np.log(bs[valid,t-1]/bs[valid,t]) if valid.sum()>=400 else None
   energies[str(t)]={'value':ev,'se':float(np.std(gev,ddof=1)) if gev is not None else None,'valid_fraction':float(valid.mean())}
  results.append({'bin':[float(bins[i]),float(bins[i+1])],'n_paths':n,'mean_r':float(r[mask].mean()),'r_min':float(r[mask].min()),'r_max':float(r[mask].max()),'mean_cos2phi':float(np.cos(2*phi[mask]).mean()),'mean_w':mean.tolist(),'se_w':se.tolist(),'snr':(mean/(se+1e-100)).tolist(),'energies_lattice':energies,'by_chain_t4':b.mean(axis=1)[:,3].tolist()})
 out[kind]=results
 for z in results:
  print('bin',z['bin'],'N',z['n_paths'],'r',round(z['mean_r'],3),'SNR t4,6,8',*(round(z['snr'][j],1) for j in (3,5,7)),'Veff t4:5', z['energies_lattice']['4']['value'],flush=True)
(root/'STAGE12_PHYSICAL_WILSON_AUDIT.json').write_text(json.dumps(out,indent=2))
