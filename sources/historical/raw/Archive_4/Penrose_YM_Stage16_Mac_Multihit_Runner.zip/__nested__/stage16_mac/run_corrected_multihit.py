#!/usr/bin/env python3
"""Read-only Stage 16 corrected SU(2) direct/multihit Wilson measurements.

The default reads one final gauge field per checkpoint. It does NOT reconstruct
900 historical gauge fields and is not a statistically sufficient ensemble.
"""
import argparse,hashlib,json,os,sys,time
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
STAGE16=ROOT/'ym_stage16'
STAGE7=ROOT/'ym_stage13'/'deps'/'ym_stage7'
sys.path.insert(0,str(STAGE7));sys.path.insert(0,str(STAGE16))
from stage7_large_torus import pair,assemble_vectorized
from stage16_multihit import multihit_batched

def sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for x in iter(lambda:f.read(4<<20),b''):h.update(x)
    return h.hexdigest()

def catalog(kind,n):
    matches=json.loads((STAGE16/'MATCHED_PATH_SCREEN.json').read_text())['pairs']
    name='square_path_index' if kind=='square' else 'penrose_path_index'
    indices=np.array([x[name] for x in matches[:n]],dtype=np.int64)
    with np.load(STAGE16/f'{kind}_candidate_paths.npz',allow_pickle=False) as z:
        return {k:np.asarray(z[k][indices]) for k in ('idx','sign','length','u','v','dx','r')},indices

def run(a):
    pairs=json.loads((STAGE16/'MATCHED_PATH_SCREEN.json').read_text())['pairs']
    assert len(pairs)>=a.pairs
    out=Path(a.output).resolve();out.mkdir(parents=True,exist_ok=True)
    p_geom,s_geom=pair();geoms={'square':s_geom,'penrose':p_geom}
    ref_a=(p_geom['physical_area']/p_geom['F'])**.5
    records=[]
    for kind in a.kinds:
        sp=geoms[kind]; paths,indices=catalog(kind,a.pairs)
        lat=assemble_vectorized(sp,20,3.5,ref_a)
        for seed in a.seeds:
            cp=Path(a.checkpoints).resolve()/f'{kind}_nt20_seed{seed}.npz'
            if not cp.is_file():raise FileNotFoundError(cp)
            with np.load(cp,allow_pickle=False) as z:
                links=z['links'].copy();sweeps=int(z['sweeps']); settings=json.loads(str(z['settings_json'].item()))
                if 'spatial_geometry_hash' in settings and settings['spatial_geometry_hash']!=sp['graph_hash']:
                    raise ValueError(f'geometry hash mismatch: {cp}')
                if 'beta' in settings and float(settings['beta'])!=3.5:raise ValueError('beta mismatch')
                if 'nt' in settings and int(settings['nt'])!=20:raise ValueError('Nt mismatch')
            if links.shape!=(lat['L'],4):raise ValueError(f'wrong link shape {links.shape}')
            raw=[];mh=[];times=[]
            for lag in a.lags:
                t=time.perf_counter();d,m=multihit_batched(links,lat,sp,paths,t0=0,lag=lag)
                if not(np.all(np.isfinite(d)) and np.all(np.isfinite(m))):raise ValueError('nonfinite values')
                raw.append(d);mh.append(m);times.append(time.perf_counter()-t)
            dest=out/f'{kind}_seed{seed}_sweep{sweeps}_multihit.npz'
            tmp=out/(dest.stem+'.partial.npz')
            np.savez_compressed(tmp,direct=np.stack(raw),multihit=np.stack(mh),lags=np.array(a.lags),
                matched_pair_indices=np.arange(a.pairs),candidate_path_indices=indices,
                r=paths['r'],dx=paths['dx'],source=paths['u'],target=paths['v'],
                source_checkpoint_sha256=sha(cp),sweep=np.int64(sweeps),geometry=kind,seed=np.int64(seed))
            os.replace(tmp,dest)
            rec={'kind':kind,'seed':seed,'sweeps':sweeps,'paths':a.pairs,'lags':a.lags,
                 'seconds_per_lag':times,'checkpoint_hash':sha(cp),'output':dest.name,'output_sha256':sha(dest),
                 'status':'FINAL_SNAPSHOT_ONLY_NOT_ENSEMBLE'}
            records.append(rec)
            print('SAVED',dest.name,'times',np.round(times,2),flush=True)
    (out/'MEASUREMENT_MANIFEST.json').write_text(json.dumps({'records':records,'fit_admitted':False,
       'note':'One final field per chain. Path-to-path replicas are not independent gauge samples. '
       'No string tension, scale, or plateau extraction is supported.'},indent=2))
    return records

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkpoints',default='checkpoints')
    ap.add_argument('--output',default='multihit_results')
    ap.add_argument('--pairs',type=int,default=20)
    ap.add_argument('--lags',type=int,nargs='+',default=[4,8])
    ap.add_argument('--kinds',nargs='+',choices=['square','penrose'],default=['square','penrose'])
    ap.add_argument('--seeds',nargs='+',type=int,default=[101,211,307,419])
    a=ap.parse_args()
    if not 1<=a.pairs<=600:ap.error('pairs must be 1..600')
    if not a.lags or any(not 1<=t<20 for t in a.lags):ap.error('lags must be 1..19')
    run(a)
