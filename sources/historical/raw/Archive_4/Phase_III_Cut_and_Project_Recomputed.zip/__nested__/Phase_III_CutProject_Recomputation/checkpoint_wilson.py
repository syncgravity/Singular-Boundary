"""Reproducible, checkpointed Wilson action run on independently window-built Z^5 P3 patches.

Each checkpoint includes exact gauge links, numpy RNG state, step counter,
measurements, graph fingerprint. Atomic overwrite permits resuming by module.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse, hashlib, json, time
from pathlib import Path
import numpy as np
from direct_cut_project import build,validate
from phase2 import random_su2, holonomies
from phase2_extended import face_adjacencies, sparse_laplacian, metropolis_sweep

def fingerprint(g,gamma):
    raw = json.dumps({'labels': g.labels, 'faces':g.faces,'edges':g.edges,
            'gamma':gamma.tolist()},sort_keys=True,separators=(',',':')).encode('utf8')
    return hashlib.sha256(raw).hexdigest()

def store(path,payload):
    tmp=path.with_suffix('.inprogress')
    with open(tmp,'w') as f:
        json.dump(payload,f);f.flush();os.fsync(f.fileno())
    os.replace(tmp,path)

def run_one(radius=5.,offset=0,beta=1.,chain=0,burn=100,thin=3,target=200,step=.65,
            module_sweeps=150,directory='chains'):
    g,gamma=build(radius,offset)
    geom=validate(g,gamma)
    sha=fingerprint(g,gamma)
    key=f'R{radius}_o{offset}_b{beta}_c{chain}'
    path=Path(directory)/f'{key}.json'
    path.parent.mkdir(exist_ok=True,parents=True)
    setup=dict(radius=radius,offset=offset,beta=beta,chain=chain,burn=burn,thin=thin,
               target=target,step=step,graph_sha256=sha,eigensolver='dense-Hermitian-v1')
    if path.exists():
        s=json.loads(path.read_text())
        for k,v in setup.items():
            if s['setup'][k]!=v:raise ValueError(f'checkpoint mismatch {key} {k}: {s["setup"][k]} vs {v}')
        rng=np.random.default_rng(); rng.bit_generator.state=s['rng_state']
        U={e:np.asarray(z)[:,:,0]+1j*np.asarray(z)[:,:,1] for e,z in zip(g.edges,s['links'])}
    else:
        seed=934071+100000*int(beta)+2000*int(round(radius*10))+157*offset+chain*1009
        rng=np.random.default_rng(seed)
        U={e:random_su2(rng,1) for e in g.edges}
        s={'setup':setup,'seed':seed,'geometry':geom,'sweeps':0,'accept_sum':0.,'measurements':[]}
    adj=face_adjacencies(g)
    start=time.perf_counter()
    end=min(s['sweeps']+module_sweeps,burn+thin*target)
    while s['sweeps']<end:
        accepted=metropolis_sweep(g,U,beta,rng,step,adj)
        s['sweeps']+=1;s['accept_sum']+=accepted
        t=s['sweeps']
        if t>burn and (t-burn)%thin==0:
            ev=np.linalg.eigvalsh(sparse_laplacian(g,U).toarray())[:4]
            if max(abs(ev[0]-ev[1]),abs(ev[2]-ev[3]))>2e-9:
                raise ArithmeticError('SU(2) eigenvalue doublet failed verification')
            s['measurements'].append({'sweep':t,'plaquette':float(np.mean(holonomies(g,U))),
                                      'lambda0':float(ev[0]),'lambda2':float(ev[2]),
                                      'gap':float(ev[2]-ev[0])})
    s['rng_state']=rng.bit_generator.state
    s['links']=[np.stack((U[e].real,U[e].imag),axis=-1).tolist() for e in g.edges]
    s['last_module_s']=time.perf_counter()-start
    store(path,s)
    return {'key':key,'sweeps':s['sweeps'],'measurements':len(s['measurements']),
            'done':s['sweeps']>=burn+thin*target,'last_module_s':round(s['last_module_s'],3)}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--radius',type=float,default=5.);p.add_argument('--offset',type=int,default=0)
    p.add_argument('--beta',type=float,default=1.);p.add_argument('--chain',type=int,default=0)
    p.add_argument('--burn',type=int,default=100);p.add_argument('--thin',type=int,default=3)
    p.add_argument('--target',type=int,default=200);p.add_argument('--step',type=float,default=.65)
    p.add_argument('--module-sweeps',type=int,default=150);p.add_argument('--directory',default='chains')
    a=p.parse_args();print(json.dumps(run_one(**vars(a))),flush=True)
