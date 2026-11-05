#!/usr/bin/env python3
"""Archive metadata and two-dimensional Penrose/square provenance comparison only.
This does NOT infer spectral dimension, gravitational loop finiteness, or a mass gap.
"""
import argparse, hashlib, json, pathlib, tarfile, zipfile
import numpy as np

def sha(b): return hashlib.sha256(b).hexdigest()

def audit(root):
  names=('penrose','square'); seeds=(101,211,307,419); lags=None; rows=[]
  for geom in names:
    for seed in seeds:
      fn=f'{geom}_seed{seed}_sweep10000_multihit.npz'; path=root/fn
      with np.load(path,allow_pickle=False) as x:
        required=['direct','multihit','lags','matched_pair_indices','r','dx','geometry','seed','source_checkpoint_sha256','sweep']
        assert all(k in x for k in required),fn
        assert str(x['geometry'])==geom and int(x['seed'])==seed and int(x['sweep'])==10000,fn
        assert x['direct'].shape == x['multihit'].shape == (4,600),fn
        assert x['dx'].shape == (600,2),fn
        assert (np.isfinite(x['direct']).all() and np.isfinite(x['multihit']).all()),fn
        ls=[int(v) for v in x['lags']]
        if lags is None: lags=ls
        assert ls==lags,fn
        dat={k:np.asarray(x[k],dtype='float64').mean(axis=1).tolist() for k in ('direct','multihit')}
        source_sha=str(x['source_checkpoint_sha256'])
      compact=root/f'{geom}_seed{seed}_stage26.zip'
      with zipfile.ZipFile(compact) as z:
        assert z.testzip() is None,compact
        j=json.loads(z.read(f'{geom}_seed{seed}/latest.json'))
        assert j['source_sha256']==source_sha,(fn,'source checkpoint hash mismatch')
        assert j['kind']==geom and j['seed']==seed and j['sweep']==12000
        assert j['initial_sweep']==10000 and j['observations']==100
        # Important: sweep source metadata equals the generator-source SHA, NOT the latest record SHA.
      rows.append({'geometry':geom,'seed':seed,'lags':ls,'sweep_sha256':sha(path.read_bytes()),'compact_sha256':sha(compact.read_bytes()),
                   'input_stage9_checkpoint_sha256':source_sha,'mean_over_600_pairs':dat,
                   'input_checkpoint_lineage_metadata_verified':True,'compact_crc_pass':True})
  by_geom={}
  for geom in names:
    rr=[x for x in rows if x['geometry']==geom]
    by_geom[geom]={k:np.asarray([x['mean_over_600_pairs'][k] for x in rr]).mean(axis=0).tolist() for k in ('direct','multihit')}
  contrasts={k:(np.asarray(by_geom['penrose'][k])-np.asarray(by_geom['square'][k])).tolist() for k in ('direct','multihit')}
  with tarfile.open(root/'Sharpe_dissertation_v10.7.tar.gz','r:gz') as tar:
    papers=[{'archive_member':m.name,'sha256':sha(tar.extractfile(m).read()),'bytes':m.size} for m in tar.getmembers() if m.isfile() and '/Paper_' in m.name and m.name.endswith('.pdf') and '/._' not in m.name]
  assert len(papers)==5
  return {'scope':'Provenance and descriptive checks only; neither 600 samples nor four seed trials justify independence or uncertainty estimates without the exact simulation protocol.','lag_values':lags,'paired_seed_labels':list(seeds),'sweep_rows':rows,'overall_mean_of_four_seed_means':by_geom,'penrose_minus_square_descriptive':contrasts,'paper_sources':sorted(papers,key=lambda x:x['archive_member']),
  'critical_distinctions':['Square control sweep records and Penrose sweep records have distinct simulation source SHA-256; matching seed labels do not establish identical random streams or matched physical sites.','The sweep arrays are 2D displacement data; neither these arrays nor the compact Stage26 files certify a 3D refining regulator.','The Paper 2 spectral-zeta ratio is a different experiment and is NOT recalculated by this multihit comparison.','Internal 600-pair measurements may be dependent. Means are descriptive, not confidence intervals or tests of significance.','The source checkpoint SHA in sweeps is the INPUT Stage 9 checkpoint SHA, not Python generator source SHA and not the latest Stage26 output record SHA.']}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--data-dir',default='/mnt/data');p.add_argument('--out',default='pairing_audit.json');a=p.parse_args();v=audit(pathlib.Path(a.data_dir));pathlib.Path(a.out).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n');print('PASS: 8 sweeps, 8 compact archives, 5 dissertation papers; Stage 9 checkpoint lineage metadata and structure verified');print('lags:',v['lag_values']);print('descriptive Penrose minus square multi-hit:',v['penrose_minus_square_descriptive']['multihit'])
