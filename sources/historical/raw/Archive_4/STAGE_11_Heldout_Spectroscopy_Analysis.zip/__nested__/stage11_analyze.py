import numpy as np,json
from pathlib import Path
ROOT=Path('/mnt/data'); output={}
for geom in ('square','penrose'):
 x=[];f=[];w=[]
 for seed in (101,211,307,419):
  with np.load(ROOT/f'{geom}_nt20_seed{seed}.npz',allow_pickle=False) as z:
   x.append(z['observables_scalar'].copy());f.append(z['observables_flux'].copy());w.append(z['observables_wilson'].copy())
 x=np.array(x); f=np.array(f); w=np.array(w)
 # select operator via train chains only; evaluate held-out chain 419 without reselecting
 train=x[:3];held=x[3:]
 def matrices(tensor):
  mu=tensor.mean(axis=(0,1,2));a=tensor-mu
  return np.array([.5*(np.einsum('cnti,cntj->ij',a,np.roll(a,-lag,axis=2))/(np.prod(tensor.shape[:3]))+np.einsum('cntj,cnti->ij',a,np.roll(a,-lag,axis=2))/(np.prod(tensor.shape[:3]))) for lag in range(6)])
 ct=matrices(train); eig=np.linalg.eigvalsh(ct[1]);
 # candidates: scalar diagonal index with largest C(1)/C(0), subject to C(1)>0 and C(0)>0
 ratios=np.diag(ct[1])/np.diag(ct[0]);ind=int(np.argmax(np.where(np.diag(ct[1])>0,ratios,-np.inf)))
 # also greedy principal C0 top eigenvectors, projection directions selected on train only
 val,vec=np.linalg.eigh(ct[0]); rank3=vec[:,-3:]; proj_candidates=[('selected_single',np.eye(9)[:,ind]),('C0_top_eigenvector',vec[:,-1])]
 def block_signal(tensor,vec,block=20):
  mu=tensor.mean(axis=(0,1,2));a=np.einsum('cnti,i->cnt',tensor-mu,vec)
  z=np.array([(a*np.roll(a,-lag,axis=2)).mean(axis=2) for lag in range(1,6)]) # lag,chain,draw
  bs=z.reshape(5,len(tensor),900//block,block).mean(axis=-1).reshape(5,-1)
  m=bs.mean(axis=1);se=bs.std(axis=1,ddof=1)/np.sqrt(bs.shape[1]);return {'values':m.tolist(),'se':se.tolist(),'snr':(m/se).tolist()}
 reduced={}
 for name,vec_ in proj_candidates:
  reduced[name]={'train':block_signal(train,vec_), 'heldout':block_signal(held,vec_)}
 # Reduced coordinate submatrices min eig per lag on heldout; fixed selection of top variance 3 directions
 ctheld=matrices(held)
 reduced['C0_top3_heldout_eig_C1']=np.linalg.eigvalsh(rank3.T@ctheld[1]@rank3).tolist()
 # Wilson path geometry unspecified: per-path time series, average by step count assumed plan enumerates blocks of 20 paths
 # estimate signal/noise, no potential fit; window t=4:8 and 2-sweep APE
 wb=w[:,:,1,:,:].mean(axis=2) # chain,draw,10 per-config avg over all paths (mixed separations)
 bins=w[:,:,1,:,:].reshape(4,900,5,20,10).mean(axis=3) # 5 path-length groups
 wr=[]
 for q in range(5):
  signal=bins[:,:,q,:].reshape(4,45,20,10).mean(axis=2).reshape(180,10)
  avg=signal.mean(axis=0); se=signal.std(axis=0,ddof=1)/np.sqrt(180)
  wr.append({'length_group':q+1,'means_t1_10':avg.tolist(),'snr_t1_10':(avg/se).tolist()})
 # flux block s/e on heldout
 def flux_signal(tensor):
  zz=np.array([(tensor*np.roll(tensor,-lag,axis=2)).mean(axis=2) for lag in range(1,6)]) # lag,chain,900,6
  zz=zz.reshape(5,len(tensor),45,20,6).mean(axis=3).reshape(5,-1,6)
  mean=zz.mean(axis=1);se=zz.std(axis=1,ddof=1)/np.sqrt(zz.shape[1]);return (mean/se).tolist()
 output[geom]={'train_operator':ind,'train_c1_diag_over_c0':ratios.tolist(),'train_c1_eigenvalues':eig.tolist(),'heldout_reduced_scalar':reduced,'flux_heldout_snr':flux_signal(f[3:]),'wilson_groups':wr}
 print(geom,'selected scalar',ind,'heldout scalar snr',np.round(reduced['selected_single']['heldout']['snr'],2),'PCA',np.round(reduced['C0_top_eigenvector']['heldout']['snr'],2),'wilson t4/t8 snr',[(round(z['snr_t1_10'][3],1),round(z['snr_t1_10'][7],1)) for z in wr],flush=True)
ROOT.joinpath('STAGE_11_DIAGNOSTICS.json').write_text(json.dumps(output,indent=2))
