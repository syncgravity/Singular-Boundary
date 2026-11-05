#!/usr/bin/env python3
"""Read-only structure/provenance audit of user-supplied dissertation and Stage26 data.
Metadata consistency is NOT identity to external source or physical regulator certification.
"""
import hashlib,io,json,os,tarfile,zipfile
from pathlib import Path
import numpy as np
root=Path('/mnt/data')
def sha(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()
result={'dissertation_tar':{'bytes':(root/'Sharpe_dissertation_v10.7.tar.gz').stat().st_size,'sha256':sha(root/'Sharpe_dissertation_v10.7.tar.gz')},'archives':[],'full_archive':{},'whitney':{}}
with tarfile.open(root/'Sharpe_dissertation_v10.7.tar.gz','r:gz') as tf:
 result['dissertation_tar']['pdfs']=[m.name for m in tf if m.isfile() and m.name.endswith('.pdf')]
for kind in ('square','penrose'):
 for seed in (101,211,307,419):
  archive=root/f'{kind}_seed{seed}_stage26.zip'
  sweep=root/f'{kind}_seed{seed}_sweep10000_multihit.npz'
  with zipfile.ZipFile(archive) as z:
   names=[n for n in z.namelist() if n.endswith('.npz')]
   sweeps=[]; dims=[]; sources=set()
   for name in names:
    with np.load(io.BytesIO(z.read(name)),allow_pickle=False) as d:
     sweeps.append(int(d['sweep']))
     dims.append((d['direct_timeslice'].shape,d['conditional'].shape))
     sources.add(str(d['source_sha256']))
   assert len(names)==100
   assert len(set(sweeps))==100
   assert len(set(map(str,dims)))==1
   valid_archive=z.testzip() is None
  with np.load(sweep,allow_pickle=False) as d:
   assert str(d['geometry'])==kind and int(d['seed'])==seed
   assert d['dx'].ndim==2 and d['dx'].shape[1]==2
   assert int(d['sweep'])==10000
   assert len(sources)==1
   assert str(d['source_checkpoint_sha256'])==next(iter(sources))
   sdict={'sweep':int(d['sweep']),'lag_count':len(d['lags']),'spatial_displacements_shape':list(d['dx'].shape),'source_checkpoint_metadata_matches_stage26_10000':True}
  result['archives'].append({'geometry':kind,'seed':seed,'sha256_stage_zip':sha(archive),'sha256_sweep_npz':sha(sweep),'zip_crc_passed':valid_archive,'checkpoint_count':len(names),'checkpoint_sweep_min_max':[min(sweeps),max(sweeps)],'checkpoint_direct_timeslice_shape':list(dims[0][0]),'checkpoint_conditional_shape':list(dims[0][1]),'sweep_dataset':sdict})
with np.load(root/'global_whitney_11face.npz',allow_pickle=False) as w:
 result['whitney']={'sha256':sha(root/'global_whitney_11face.npz'),'matrix_shape':list(w['matrix'].shape),'edge_ids_shape':list(w['edge_ids'].shape),'eigenvalues_shape':list(w['eigenvalues'].shape)}
full=root/'penrose_seed101_stage26_full.zip'
with zipfile.ZipFile(full) as z:
 result['full_archive']={'sha256':sha(full),'entries':len(z.namelist()),'contains_restart':any(n.endswith('restart.npz') for n in z.namelist()),'crc_passed':z.testzip() is None}
with open('attached_source_manifest.json','w') as f:json.dump(result,f,indent=2)
print(json.dumps({'archives_checked':len(result['archives']),'total_checkpoints':sum(x['checkpoint_count'] for x in result['archives']),'spatial_displacement_dim':2,'full_archive_crc':result['full_archive']['crc_passed'],'all_sweep_metadata_agree':all(a['sweep_dataset']['source_checkpoint_metadata_matches_stage26_10000'] for a in result['archives']),'manifest_file':'attached_source_manifest.json'},indent=2))