"""Four final chain checkpoints per geometry: large M55 multihit path screen.
Not a replacement for the 900 measured observations per chain.
"""
from pathlib import Path
import sys,json,time
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'ym_stage13/deps/ym_stage7'))
from stage7_large_torus import pair,assemble_vectorized
from stage16_multihit import multihit_batched

def load_subcatalog(path,indices):
    z=np.load(path)
    return {k:z[k][indices] for k in ('idx','sign','length','u','v','dx','r')}

def run(checkpoint_dir=None):
    checkpoint_dir=Path(checkpoint_dir) if checkpoint_dir is not None else HERE.parent
    matched=json.loads((HERE/'MATCHED_PATH_SCREEN.json').read_text())
    inds_square=[p['square_path_index'] for p in matched['pairs']]
    inds_penrose=[p['penrose_path_index'] for p in matched['pairs']]
    gP,gS=pair();r=[]
    for kind,sp,indices in [('square',gS,inds_square),('penrose',gP,inds_penrose)]:
        start=time.perf_counter()
        p=load_subcatalog(HERE/f'{kind}_candidate_paths.npz',indices)
        a=(sp['physical_area']/sp['F'])**.5
        lat=assemble_vectorized(sp,20,3.5,a)
        for seed in (101,211,307,419):
            filename=checkpoint_dir/f'{kind}_nt20_seed{seed}.npz'
            with np.load(filename,allow_pickle=False) as z:
                U=z['links'].copy();sw=int(z['sweeps'])
            if U.shape!=(lat['L'],4):raise AssertionError('gauge field and geometry mismatch')
            for lag in (4,8):
                begin=time.perf_counter();d,m=multihit_batched(U,lat,sp,p,lag=lag)
                r.append({'geometry':kind,'seed':seed,'lag':lag,'npaths':len(d),'sweeps_of_snapshot':sw,
                     'runtime_seconds':time.perf_counter()-begin,
                     'direct_batch_mean':float(np.mean(d)), 'multihit_batch_mean':float(np.mean(m)),
                     'direct_raw_sd_among_paths':float(np.std(d,ddof=1)),
                     'multihit_raw_sd_among_paths':float(np.std(m,ddof=1)),
                     'all_finite':bool(np.isfinite(m).all()),
                     'note':'one final snapshot per chain; paths correlated; not full ensemble measurement'})
        print(kind,'measured selected paths',len(p['u']),'4 final chain fields elapsed',round(time.perf_counter()-start,2),flush=True)
    out={'status':'IMPLEMENTATION_SCREEN_ONLY','matching_reference':'MATCHED_PATH_SCREEN.json',
       'all_physical_results_admitted':False,'outer_independent_samples_per_geometry':4,
       'measurements':r}
    (HERE/'LARGE_SNAPSHOT_SCREEN.json').write_text(json.dumps(out,indent=2))
    return out
if __name__=='__main__':
    import argparse
    cli=argparse.ArgumentParser(description='Stage 16 matched-path large-gauge snapshot screening')
    cli.add_argument('--checkpoints',default=str(HERE.parent),help='directory with 8 Stage 9 final .npz checkpoints')
    args=cli.parse_args()
    print(json.dumps(run(args.checkpoints),indent=2))
