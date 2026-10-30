#!/usr/bin/env python3
"""Stage 19 capped 0++ pilot; independent read-only Stage9 inputs.

Four channels: 3 unrestricted full-anchor rooted controls and 1 strict matched
auxiliary conditional on the geometry-only accepted roots. An auxiliary with
full-anchor denominator is stored separately. Neither is an exact symmetry orbit.
"""
import argparse,hashlib,json,os,sys,time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(HERE/'stage18'),str(HERE/'stage18'/'stage17_mac'),
 str(HERE/'stage18'/'stage17_mac'/'ym_stage13'/'deps'/'ym_stage7'),
 str(HERE/'stage18'/'stage17_mac'/'ym_stage13'/'deps'/'ym_stage6'/'source_stage5'),
 str(HERE/'stage19')]
from stage7_checkpointed import sweep,get_plaquettes,setup_geometry
from stage19_full import neighbors,boundary,full_catalogue
from target_first import grow
from full_anchor_targets import TARGETS,SCALE,THRESHOLD
from matched_basis import weighted_observe

SIZES=(2,3,4,5,6,7,8,9,10,12,15)
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(4<<20),b''):h.update(b)
 return h.hexdigest()
def save(p,**kw):
 p=Path(p);tmp=p.with_suffix('.partial.npz')
 with open(tmp,'wb') as f:np.savez_compressed(f,**kw);f.flush();os.fsync(f.fileno())
 os.replace(tmp,p)
def pack(paths):
 ml=max(map(len,paths));i=np.full((len(paths),ml),-1,np.int64);s=np.zeros((len(paths),ml),np.int64)
 for j,p in enumerate(paths):
  for k,(e,sg) in enumerate(p):i[j,k]=e;s[j,k]=sg
 return i,s,np.array([len(p) for p in paths],np.int64)
def construct(sp,kind,certificate):
 F=int(sp['F']);prior=np.load(certificate,allow_pickle=False)
 if kind=='penrose' and len(prior['best_size'])!=F:raise ValueError('certificate does not match geometry')
 adj=neighbors(sp);areas=np.asarray(sp['face_areas']);vv=np.asarray(sp['edge_vectors'])
 targets=np.array([[np.log(a),np.log(p),4*np.pi*a/p**2] for a,p in TARGETS])
 paths=[];roots=[];ds=[];tid=[];sizes=[];t0=time.monotonic()
 for root in range(F):
  requested=(int(prior['best_size'][root]),) if kind=='penrose' and int(prior['best_size'][root]) in SIZES else (3,5,8,10)
  best=(float('inf'),None)
  for batch in (requested,SIZES):
   seen=set()
   for nf in batch:
    for variant in range(4):
     fs=grow(adj,root,nf,variant)
     if fs is None or fs in seen:continue
     seen.add(fs);p=boundary(sp,fs)
     if p is None:continue
     edges=np.array([e for e,s in p],dtype=int);a=float(areas[list(fs)].sum());per=float(np.linalg.norm(vv[edges],axis=1).sum())
     vals=np.array([np.log(a),np.log(per),4*np.pi*a/per**2]);dd=np.linalg.norm((targets-vals)/SCALE,axis=1)
     j=int(np.argmin(dd));d=float(dd[j])
     if d<best[0]:best=(d,(p,j,nf))
   if best[0]<=THRESHOLD:break
  if best[0]<=THRESHOLD:
   p,j,nf=best[1];paths.append(p);roots.append(root);ds.append(best[0]);tid.append(j);sizes.append(nf)
  if root and root%5000==0:print('CATALOGUE',kind,root,'/',F,'seconds',int(time.monotonic()-t0),flush=True)
 idx,sign,length=pack(paths)
 if kind=='penrose':
  expected=np.flatnonzero(prior['covered'])
  if expected is not None and not np.array_equal(roots,expected):raise ValueError('strict acceptance mask differs from prior certificate')
  if len(roots)!=22658:raise ValueError(f'Penrose coverage changed: {len(roots)} != 22658')
 elif len(roots)!=F:raise ValueError('square coverage incomplete')
 ctrl=full_catalogue(sp)
 if any(np.count_nonzero(ctrl['kind']==k)!=F for k in range(3)):raise ValueError('control not full-volume')
 return {'idx':idx,'sign':sign,'length':length,'roots':np.array(roots,np.int64),'distance':np.array(ds),
         'target':np.array(tid,np.int64),'faces':np.array(sizes,np.int64),
         'cidx':ctrl['idx'].astype(np.int64),'csign':ctrl['sign'].astype(np.int64),
         'clength':ctrl['length'],'ckind':ctrl['kind'],'F':np.int64(F),'graph_hash':np.array(sp['graph_hash']),
         'threshold':np.float64(THRESHOLD)}
def catalogue(kind,g,path,cert):
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 if not path.exists():
  print('BUILDING geometry-only catalogue',kind,flush=True);save(path,**construct(g,kind,cert))
 with np.load(path,allow_pickle=False) as z: cat={k:z[k].copy() for k in z.files}
 F=int(g['F']);roots=cat['roots'];assert cat['graph_hash'].item()==g['graph_hash'] and int(cat['F'])==F
 assert np.array_equal(roots,np.unique(roots)) and np.all((roots>=0)&(roots<F))
 assert float(cat['threshold'])==THRESHOLD and np.max(cat['distance'])<=THRESHOLD
 assert all(np.sum(cat['ckind']==i)==F for i in range(3))
 assert len(roots)==(F if kind=='square' else 22658)
 return cat,sha(path)
def measure(links,g,cat):
 F=int(cat['F']);n=len(cat['roots']);E=int(g['E'])
 aux=weighted_observe(links,20,E,cat['idx'],cat['sign'],cat['length'],
                     np.ones(n),np.zeros(n,np.int64),1)[:,0]
 controls=weighted_observe(links,20,E,cat['cidx'],cat['csign'],cat['clength'],
                          np.ones(len(cat['clength'])),cat['ckind'],3)
 return np.column_stack([controls,aux]),aux*(n/F)
def run(kind,seed,inputs,output,cache,certificate,target,chunk,thin):
 if target<10000 or chunk<1 or thin<1:raise ValueError('invalid target/chunk/thin')
 src=Path(inputs)/f'{kind}_nt20_seed{seed}.npz';origin=sha(src)
 od=Path(output).resolve()/f'{kind}_seed{seed}';od.mkdir(parents=True,exist_ok=True)
 marker=od/'source_sha256.txt'
 if marker.exists():
  if marker.read_text().strip()!=origin:raise ValueError('checkpoint source hash changed')
 elif list(od.iterdir()):raise ValueError('nonempty output lacking source marker')
 else:marker.write_text(origin+'\n')
 g,lat=setup_geometry(kind,20,3.5)
 cat,catsha=catalogue(kind,g,Path(cache)/f'{kind}_strict_catalogue.npz',certificate)
 cfg={'kind':kind,'seed':seed,'thin':thin,'catalogue_sha256':catsha,'source_sha256':origin,'beta':3.5,'nt':20,'threshold':THRESHOLD}
 state=od/'restart.npz'
 if state.exists():
  with np.load(state,allow_pickle=False) as z:
   links=z['links'].copy();pf=z['plaquette_trace'].copy();rng=z['rng'].copy();start=int(z['sweeps']);previous=str(z['last_segment_sha256'].item());old=json.loads(str(z['config'].item()))
  if old!=cfg:raise ValueError('resume config mismatch')
  segments=sorted(od.glob('observations_*.npz'))
  if previous and (not segments or sha(segments[-1])!=previous):raise ValueError('segment checksum mismatch')
 else:
  with np.load(src,allow_pickle=False) as z:
   settings=json.loads(str(z['settings_json'].item()))
   if settings['spatial_geometry_hash']!=g['graph_hash'] or settings['kind']!=kind or int(settings['seed'])!=seed or int(settings['nt'])!=20 or float(settings['beta'])!=3.5:raise ValueError('source incompatible')
   links=z['links'].copy();pf=z['plaquette_trace'].copy();rng=z['rng'].copy();start=int(z['sweeps'])
 if start>=target:print('TARGET ALREADY REACHED',kind,seed,start);return
 if not np.allclose(get_plaquettes(links,lat['fi'],lat['sg']),pf,atol=1e-9,rtol=0):raise ValueError('plaquette cache mismatch')
 end=min(start+chunk,target);times=[];series=[];missing=[];tic=time.monotonic()
 for k in range(start+1,end+1):
  sweep(links,pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],rng,.95)
  if (k-10000)%thin==0:
   measured,uncond=measure(links,g,cat);series.append(measured);missing.append(uncond);times.append(k)
 if not np.allclose(get_plaquettes(links,lat['fi'],lat['sg']),pf,atol=1e-9,rtol=0):raise ValueError('final plaquette cache mismatch')
 dest=od/f'observations_{start:08d}_{end:08d}.npz'
 save(dest,scalar=np.asarray(series).reshape((-1,20,4)),aux_full_denominator=np.asarray(missing).reshape((-1,20)),
      measured_sweeps=np.array(times,np.int64),channels=np.array(['full_3face','full_5face','full_8face','strict_aux_conditional']),
      catalogue_sha256=np.array(catsha),source_sha256=np.array(origin),accepted_anchors=np.int64(len(cat['roots'])),all_anchors=np.int64(cat['F']))
 d=sha(dest)
 save(state,links=links,plaquette_trace=pf,rng=rng,sweeps=np.int64(end),config=np.array(json.dumps(cfg)),last_segment_sha256=np.array(d))
 report={'kind':kind,'seed':seed,'from_sweep':start,'to_sweep':end,'measurements':len(times),
         'catalogue_sha256':catsha,'segment_sha256':d,'source_checkpoint_sha256':origin,
         'accepted_anchors':len(cat['roots']),'all_anchors':int(cat['F']),
         'runtime_seconds':time.monotonic()-tic,'physical_mass_admitted':False}
 tmp=od/'latest.json.partial';tmp.write_text(json.dumps(report,indent=2));os.replace(tmp,od/'latest.json')
 print('SAVED',json.dumps(report),flush=True)
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--kind',choices=['square','penrose'],required=True);p.add_argument('--seed',type=int,required=True)
 p.add_argument('--inputs',required=True);p.add_argument('--output',required=True)
 p.add_argument('--cache',default='stage19_catalogues');p.add_argument('--certificate',default=str(HERE/'all_anchors_strict_min_distance.npz'))
 p.add_argument('--target-sweeps',type=int,default=10100);p.add_argument('--chunk',type=int,default=100);p.add_argument('--thin',type=int,default=10)
 a=p.parse_args();run(a.kind,a.seed,a.inputs,a.output,a.cache,a.certificate,a.target_sweeps,a.chunk,a.thin)
if __name__=='__main__':main()
