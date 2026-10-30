"""Replay recorded Markov chains with dense Hermitian spectrum to handle SU(2) degeneracy.

Original global-ARPACK solver may miss degenerate partners; it does not alter the
independent numpy Generator driving the Markov chain. Rebuild every configuration
from seed, and assert final links/RNG state exactly equal saved checkpoint.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,hashlib,json,math,time
from pathlib import Path
import numpy as np
from direct_cut_project import build,validate
from phase2 import random_su2,holonomies
from phase2_extended import metropolis_sweep,face_adjacencies,sparse_laplacian
from checkpoint_wilson import fingerprint
base=Path(__file__).parent

def replay(path,output_dir=None):
    p=Path(path)
    old=json.loads(p.read_text()); cfg=old['setup']
    g,gm=build(cfg['radius'],cfg['offset'])
    assert fingerprint(g,gm)==cfg['graph_sha256']
    rng=np.random.default_rng(old['seed'])
    U={e:random_su2(rng,1) for e in g.edges}
    adj=face_adjacencies(g)
    m=[]
    for sweep in range(1,old['sweeps']+1):
        metropolis_sweep(g,U,cfg['beta'],rng,cfg['step'],adj)
        if sweep>cfg['burn'] and (sweep-cfg['burn'])%cfg['thin']==0:
            H=sparse_laplacian(g,U).toarray()
            vals=np.linalg.eigvalsh(H)[:4]
            assert abs(vals[0]-vals[1])<2e-9 and abs(vals[2]-vals[3])<2e-9, (cfg,sweep,vals)
            m.append({'sweep':sweep,'plaquette':float(np.mean(holonomies(g,U))),
                      'lambda0':float(vals[0]),'lambda2':float(vals[2]),'gap':float(vals[2]-vals[0])})
    assert len(m)==len(old['measurements'])
    assert rng.bit_generator.state == old['rng_state']
    links=[np.stack((U[e].real,U[e].imag),axis=-1).tolist() for e in g.edges]
    assert links == old['links'], 'replayed final link state differs from saved checkpoint'
    x=np.array([z['lambda0'] for z in old['measurements']]); xx=np.array([z['lambda0'] for z in m])
    y=np.array([z['lambda2'] for z in old['measurements']]); yy=np.array([z['lambda2'] for z in m])
    assert max(abs(a['plaquette']-b['plaquette']) for a,b in zip(old['measurements'],m))<1e-12
    result={'setup':cfg,'seed':old['seed'],'sweeps':old['sweeps'],'accept_sum':old['accept_sum'],'geometry':old['geometry'],
            'measurements':m, 'certification':{
            'old_checkpoint_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
            'final_rng_exact':True,'final_link_state_exact':True,
            'eigen_solver':'numpy.linalg.eigvalsh complete Hermitian eigenspectrum',
            'doublet_tolerance_abs':2e-9,
            'lambda0_old_max_abs_error':float(np.max(np.abs(x-xx))),
            'lambda2_old_max_abs_error':float(np.max(np.abs(y-yy))),
            'lambda0_old_discrepant_draws_at_1e-7':int(np.sum(np.abs(x-xx)>1e-7)),
            'lambda2_old_discrepant_draws_at_1e-7':int(np.sum(np.abs(y-yy)>1e-7))}}
    output_dir=Path(output_dir) if output_dir else base/'chains_dense'
    output_dir.mkdir(exist_ok=True)
    (output_dir/p.name).write_text(json.dumps(result,indent=1))
    return p.name, result['certification']

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--glob',default='R*.json');parser.add_argument('--output-dir',default=str(base/'chains_dense'))
    a=parser.parse_args()
    t=time.perf_counter()
    files=sorted((base/'chains').glob(a.glob))
    for p in files:
        fn,result=replay(p,a.output_dir)
        print(fn,'errors',result['lambda0_old_discrepant_draws_at_1e-7'],result['lambda2_old_discrepant_draws_at_1e-7'], 'wall',round(time.perf_counter()-t,2),flush=True)
    print('done',len(files),'wall_seconds',round(time.perf_counter()-t,3),flush=True)
