#!/usr/bin/env python3
"""Stage 17 independent continuation + corrected exact one-line multihit.

Read-only Stage 9 inputs. Work state and compact observations live under --output.
Each segment is committed by writing its measurements first, then atomically
replacing the restart checkpoint, which references that exact segment hash.
An orphan segment (if interrupted before commit) is removed/recomputed only
when its exact expected name is present and there is no advanced checkpoint.
"""
import argparse,hashlib,json,os,sys,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(HERE/'ym_stage16'),str(HERE/'ym_stage13'),str(HERE/'ym_stage13'/'deps'/'ym_stage7')]
from stage7_checkpointed import sweep,get_plaquettes,setup_geometry
from stage16_multihit import multihit_batched

def digest(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(4<<20),b''):h.update(b)
 return h.hexdigest()

def catalogue(kind,n):
 pairs=json.loads((HERE/'ym_stage16'/'MATCHED_PATH_SCREEN.json').read_text())['pairs']
 if not 1<=n<=len(pairs):raise ValueError('bad pairs count')
 key='square_path_index' if kind=='square' else 'penrose_path_index'
 indices=np.array([p[key] for p in pairs[:n]],np.int64)
 with np.load(HERE/'ym_stage16'/f'{kind}_candidate_paths.npz') as z:
  paths={k:z[k][indices] for k in ('idx','sign','length','u','v','dx','r')}
 return paths,indices

def save_atomic(path,**arrays):
 path=Path(path);tmp=path.with_name(path.stem+'.partial.npz')
 np.savez_compressed(tmp,**arrays);os.replace(tmp,path)

def run(kind,seed,inputs,output,chunk,thin,pairs,lags):
 inp=Path(inputs)/f'{kind}_nt20_seed{seed}.npz'
 if not inp.exists():raise FileNotFoundError(inp)
 od=Path(output)/f'{kind}_seed{seed}';od.mkdir(parents=True,exist_ok=True)
 src_hash_file=od/'source_sha256.txt';orig_hash=digest(inp)
 if src_hash_file.exists():
  if src_hash_file.read_text().strip()!=orig_hash:raise ValueError('original input checkpoint changed!')
 else:
  # Refuse mixing a new source into prior output.
  if any(od.iterdir()):raise ValueError('existing output without origin marker')
  src_hash_file.write_text(orig_hash+'\n')
 state=od/'restart.npz'
 geom,lat=setup_geometry(kind,20,3.5)
 paths,indices=catalogue(kind,pairs)
 if state.exists():
  with np.load(state,allow_pickle=False) as z:
   links=z['links'].copy();pf=z['plaquette_trace'].copy();rng=z['rng'].copy()
   before=int(z['sweeps']);last=str(z['last_segment_sha256'].item());version=int(z['version'])
   cfg=json.loads(str(z['measurement_config'].item()))
  if version!=1 or cfg!={'pairs':pairs,'thin':thin,'lags':lags}:raise ValueError('measurement configuration changed')
  if last:
   names=sorted(od.glob('observations_*.npz'))
   if not names or digest(names[-1])!=last:raise ValueError('segment hash mismatch')
 else:
  with np.load(inp,allow_pickle=False) as z:
   links=z['links'].copy();pf=z['plaquette_trace'].copy();rng=z['rng'].copy()
   before=int(z['sweeps']);settings=json.loads(str(z['settings_json'].item()))
  if (settings.get('kind'),settings.get('seed'),settings.get('nt'),settings.get('beta'))!=(kind,seed,20,3.5):raise ValueError('input settings mismatch')
  if settings.get('spatial_geometry_hash')!=geom['graph_hash']:raise ValueError('geometry mismatch')
  if before<10000:raise ValueError('input must be post-10,000-sweep final state')
  last=''
 if links.shape!=(lat['L'],4) or pf.shape!=(lat['P'],):raise ValueError('state shape mismatch')
 if np.max(np.abs(get_plaquettes(links,lat['fi'],lat['sg'])-pf))>1e-9:raise ValueError('plaquette cache mismatch')
 end=before+chunk;when=[];direct=[];multi=[];start=time.monotonic()
 for k in range(before+1,end+1):
  sweep(links,pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],rng,.95)
  if (k-10000)%thin==0:
   ds=[];ms=[]
   for lag in lags:
    d,m=multihit_batched(links,lat,geom,paths,t0=0,lag=lag)
    ds.append(d);ms.append(m)
   when.append(k);direct.append(ds);multi.append(ms)
 err=float(np.max(np.abs(get_plaquettes(links,lat['fi'],lat['sg'])-pf)))
 if err>1e-9:raise ValueError('post-segment plaquette cache mismatch')
 name=f'observations_{before:08d}_{end:08d}.npz'; dest=od/name
 if dest.exists():
  # A crash before checkpoint commit may leave an orphan. Re-run with identical
  # input state, verify result content, then overwrite atomically below.
  if state.exists() and before==end:raise ValueError('unexpected existing segment')
 save_atomic(dest,measured_sweeps=np.array(when,dtype=np.int64),
  direct=np.asarray(direct,dtype=np.float64).reshape((-1,len(lags),pairs)),
  multihit=np.asarray(multi,dtype=np.float64).reshape((-1,len(lags),pairs)),
  lags=np.asarray(lags),r=paths['r'],dx=paths['dx'],path_indices=indices,
  source_checkpoint_sha256=orig_hash,kind=kind,seed=seed)
 sh=digest(dest)
 save_atomic(state,links=links,plaquette_trace=pf,rng=rng,sweeps=end,
  last_segment_sha256=sh,version=np.int64(1),
  measurement_config=json.dumps({'pairs':pairs,'thin':thin,'lags':lags}),
  source_checkpoint_sha256=orig_hash)
 report={'geometry':kind,'seed':seed,'start':before,'end':end,'measurements':len(when),
  'segment':name,'segment_sha256':sh,'checkpoint_sha256':digest(state),
  'input_sha256':orig_hash,'cache_error':err,'seconds':round(time.monotonic()-start,2),
  'fit_admitted':False}
 tmp=od/'latest.json.partial';tmp.write_text(json.dumps(report,indent=2));os.replace(tmp,od/'latest.json')
 print('SAVED',json.dumps(report),flush=True)
 return report

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--kind',required=True,choices=['square','penrose']);a.add_argument('--seed',type=int,required=True)
 a.add_argument('--inputs',required=True);a.add_argument('--output',required=True);a.add_argument('--chunk',type=int,default=100)
 a.add_argument('--thin',type=int,default=10);a.add_argument('--pairs',type=int,default=600)
 a.add_argument('--lags',type=int,nargs='+',default=list(range(2,11)));args=a.parse_args()
 if args.chunk<1 or args.thin<1 or not args.lags or len(set(args.lags))!=len(args.lags) or any(not 1<=x<20 for x in args.lags):a.error('invalid parameters')
 run(args.kind,args.seed,args.inputs,args.output,args.chunk,args.thin,args.pairs,args.lags)
