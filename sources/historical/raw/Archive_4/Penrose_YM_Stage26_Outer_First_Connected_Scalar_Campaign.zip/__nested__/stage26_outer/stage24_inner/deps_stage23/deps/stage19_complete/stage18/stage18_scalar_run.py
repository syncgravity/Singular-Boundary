#!/usr/bin/env python3
"""Independent, restartable Stage18 scalar continuation. Never modifies inputs.

Each segment's observations are committed before the restart state; running the
same CLI again resumes from the committed state. Original Stage9 files stay read-only.
A separate output root MUST be used, never the actively running Stage17 output.
"""
import argparse,hashlib,json,os,sys,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
DEPS=HERE/'stage17_mac'
sys.path[:0]=[str(DEPS),str(DEPS/'ym_stage13'/'deps'/'ym_stage7'),str(DEPS/'ym_stage13'/'deps'/'ym_stage6'/'source_stage5')]
from stage7_checkpointed import sweep,get_plaquettes,setup_geometry
from stage4_smearing_flux import staple_structure,ape_spatial,measure_scalar_groups,square_scalar_basis
from corrected_2p1_pilot import face_cluster_loops

def digest(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for block in iter(lambda:f.read(4<<20),b''):h.update(block)
 return h.hexdigest()

def atomic_npz(p,**arrays):
 p=Path(p);temp=p.with_name(p.stem+'.partial.npz')
 with open(temp,'wb') as f:
  np.savez_compressed(f,**arrays);f.flush();os.fsync(f.fileno())
 os.replace(temp,p)

def scalar_setup(g,weight):
 loops=square_scalar_basis(g) if g['spatial_kind']=='square_torus' else face_cluster_loops(g)
 return loops,staple_structure(g,weight)

def scalar_measure(links,g,levels,alpha,loops,staples):
 nt=20;E=int(g['E']);series=[]
 for level in levels:
  v=links if level==0 else ape_spatial(links,nt,E,*staples,alpha,level)
  series.append(measure_scalar_groups(v,nt,E,loops['idx'],loops['sign'],loops['length'],loops['kind']))
 return np.concatenate(series,axis=1)

def validate_inputs(kind,seed,settings,g):
 if (settings.get('kind'),settings.get('seed'),settings.get('nt'),settings.get('beta'))!=(kind,seed,20,3.5):
  raise ValueError('source checkpoint parameters mismatch')
 if settings.get('spatial_geometry_hash')!=g['graph_hash']:raise ValueError('source geometry mismatch')

def run(kind,seed,inputs,output,chunk,thin,target,levels,alpha,weight):
 if chunk<1 or thin<1 or target<10000 or len(set(levels))!=len(levels) or not levels or min(levels)<0 or not 0<=alpha<1:raise ValueError('invalid settings')
 inp=Path(inputs)/f'{kind}_nt20_seed{seed}.npz'
 if not inp.is_file():raise FileNotFoundError(inp)
 root=Path(output).resolve();od=root/f'{kind}_seed{seed}';od.mkdir(parents=True,exist_ok=True)
 if od.resolve()==inp.parent.resolve():raise ValueError('output overlaps source directory')
 origin=digest(inp);origin_file=od/'source_sha256.txt'
 if origin_file.exists():
  if origin_file.read_text().strip()!=origin:raise ValueError('input checkpoint has changed')
 elif any(od.iterdir()):raise ValueError('output directory has files but no provenance marker')
 else:origin_file.write_text(origin+'\n')
 config={'levels':list(levels),'alpha':alpha,'weight':weight,'thin':thin,'nt':20,'beta':3.5}
 g,lat=setup_geometry(kind,20,3.5)
 state=od/'restart.npz';prev=''
 if state.exists():
  with np.load(state,allow_pickle=False) as z:
   links=z['links'].copy();pf=z['plaquette_trace'].copy();rng=z['rng'].copy()
   start=int(z['sweeps']);prev=str(z['last_segment_sha256'].item());cfg=json.loads(str(z['measurement_config'].item()))
   if str(z['source_checkpoint_sha256'].item())!=origin:raise ValueError('source digest mismatch in state')
  if cfg!=config:raise ValueError('cannot change configuration while resuming')
  if prev:
   segments=sorted(od.glob('observations_*.npz'))
   if not segments or digest(segments[-1])!=prev:raise ValueError('committed observation segment missing/mismatched')
 else:
  with np.load(inp,allow_pickle=False) as z:
   settings=json.loads(str(z['settings_json'].item()))
   validate_inputs(kind,seed,settings,g)
   links=z['links'].copy();pf=z['plaquette_trace'].copy();rng=z['rng'].copy();start=int(z['sweeps'])
  if start<10000:raise ValueError('Stage9 initial chain must be post-10000')
 if links.shape!=(lat['L'],4) or pf.shape!=(lat['P'],):raise ValueError('field/cache shape mismatch')
 err=float(np.max(np.abs(get_plaquettes(links,lat['fi'],lat['sg'])-pf)))
 if err>1e-9:raise ValueError('initial plaquette cache mismatch')
 if start>=target:
  print(json.dumps({'kind':kind,'seed':seed,'sweeps':start,'target':target,'status':'target_reached'}));return None
 end=min(start+chunk,target)
 loops,staples=scalar_setup(g,weight)
 times=[];data=[];ts=time.monotonic()
 for k in range(start+1,end+1):
  sweep(links,pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],rng,.95)
  if (k-10000)%thin==0:
   data.append(scalar_measure(links,g,levels,alpha,loops,staples));times.append(k)
 err=float(np.max(np.abs(get_plaquettes(links,lat['fi'],lat['sg'])-pf)))
 if err>1e-9:raise ValueError('final plaquette cache mismatch')
 dest=od/f'observations_{start:08d}_{end:08d}.npz'
 atomic_npz(dest,observables_scalar=np.asarray(data,np.float64).reshape((-1,20,3*len(levels))),
  measured_sweeps=np.asarray(times,np.int64),levels=np.asarray(levels,np.int64),alpha=np.float64(alpha),
  weight=np.array(weight),kind=np.array(kind),seed=np.int64(seed),source_checkpoint_sha256=np.array(origin),
  spatial_geometry_hash=np.array(g['graph_hash']))
 segsha=digest(dest)
 atomic_npz(state,links=links,plaquette_trace=pf,rng=rng,sweeps=np.int64(end),
  last_segment_sha256=np.array(segsha),measurement_config=np.array(json.dumps(config)),
  source_checkpoint_sha256=np.array(origin))
 report={'kind':kind,'seed':seed,'start':start,'end':end,'target':target,'measurements':len(times),
  'segment':dest.name,'segment_sha256':segsha,'restart_sha256':digest(state),
  'source_checkpoint_sha256':origin,'max_plaquette_cache_error':err,
  'duration_seconds':round(time.monotonic()-ts,2),'mass_fit_admitted':False}
 tmp=od/'latest.json.partial';tmp.write_text(json.dumps(report,indent=2));os.replace(tmp,od/'latest.json')
 print('SAVED',json.dumps(report),flush=True)
 return report

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--kind',required=True,choices=['square','penrose']);p.add_argument('--seed',type=int,required=True)
 p.add_argument('--inputs',required=True);p.add_argument('--output',required=True)
 p.add_argument('--chunk',type=int,default=100);p.add_argument('--thin',type=int,default=10)
 p.add_argument('--target-sweeps',type=int,default=12000)
 p.add_argument('--levels',type=int,nargs='+',default=[0,2,6,12]);p.add_argument('--alpha',type=float,default=.4)
 p.add_argument('--weight',choices=['inverse_area','uniform'],default='inverse_area')
 a=p.parse_args();run(a.kind,a.seed,a.inputs,a.output,a.chunk,a.thin,a.target_sweeps,a.levels,a.alpha,a.weight)
