"""Fail-closed progress and physics-admission audit.

No mass or string-tension fit is attempted absent accepted individual-chain
spectroscopy and scale-setting evidence. Chain startup/burn-in is never data.
"""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
SEEDS=(101,211,307,419)
KINDS=('square','penrose')

def audit(root, seeds=SEEDS, check_npz=True):
    root=Path(root); chains=[]
    for kind in KINDS:
        for seed in seeds:
            stem=f'{kind}_nt20_seed{seed}'
            cp=root/(stem+'.npz'); meta=root/(stem+'_progress.json')
            if not (cp.exists() and meta.exists()):
                chains.append({'kind':kind,'seed':seed,'present':False,'sweeps':0,'production_samples':0})
                continue
            doc=json.loads(meta.read_text());sett=doc['settings']
            if sett['kind']!=kind or sett['seed']!=seed:raise ValueError('settings mismatch '+stem)
            sweeps=doc['completed_sweeps']; burn=sett['burn']; thin=sett['thin']
            if doc['n_postburn_samples'] > max(0,(sweeps-burn)//thin):
                raise ValueError('Impossible sample count '+stem)
            if doc['cache_error'] is None or doc['cache_error']>=1e-9:
                raise ValueError('Plaquette cache not certified '+stem)
            row={'kind':kind,'seed':seed,'present':True,'sweeps':sweeps,
                 'burn_threshold':burn,'production_samples':doc['n_postburn_samples'],
                 'cache_error':doc['cache_error'],'checkpoint_bytes':cp.stat().st_size}
            if check_npz:
                if hashlib.sha256(cp.read_bytes()).hexdigest()!=doc['checkpoint_sha256']:
                    raise ValueError('checkpoint SHA mismatch '+stem)
                with np.load(cp,allow_pickle=False) as z:
                    if int(z['sweeps'])!=sweeps:raise ValueError('mismatched sweeps')
                    if len(z['measured_sweeps'])!=row['production_samples']:
                        raise ValueError('mismatched measurements')
                    if np.any(z['measured_sweeps']<=burn):raise ValueError('burn-in leakage')
                    if np.any((z['measured_sweeps']-burn)%thin):raise ValueError('thinning mismatch')
                    if len(z['rng'])!=2:raise ValueError('missing RNG')
                    if z['observables_scalar'].shape!=(row['production_samples'],sett['nt'],9):
                        raise ValueError('scalar shape')
                    if z['observables_flux'].shape!=(row['production_samples'],sett['nt'],6):
                        raise ValueError('flux shape')
                    if z['observables_wilson'].shape!=(row['production_samples'],3,100,sett['nt']//2):
                        raise ValueError('Wilson shape')
            chains.append(row)
    nready=sum(int(r['present']) for r in chains)
    nprod=sum(r['production_samples'] for r in chains)
    # No unverified or placebo physics evidence is accepted.
    requirements={
     'four_independent_checkpoint_states_per_geometry': all(sum(r['kind']==k and r['present'] for r in chains)>=4 for k in KINDS),
     'four_converged_production_chains_per_geometry':False,
     'all_chains_postburn_sampling':all(r['production_samples']>0 for r in chains),
     'sampling_precision_Rhat_less_1p01_ESS400':False,
     'scalar_multi_time_covariance_stable_fit':False,
     'confinement_multi_distance_or_winding_fit':False,
     'renormalized_coupling_and_anisotropy_match':False,
     'finite_volume_and_orientation_stability':False,
     'multiple_cutoffs_approximants_and_offsets':False,
     'joint_bootstrap_ratio':False,
     'continuum_extrapolated_contrast':False
    }
    reasons={k:('passed' if v else 'not established') for k,v in requirements.items()}
    report={'status':'NOT A PHYSICAL MASS OR STRING TENSION RESULT',
        'n_chains_present':nready,'production_samples_total':nprod,
        'requirements':requirements,'decision':reasons,
        'mass_estimate':None,'string_tension_estimate':None,'mass_ratio':None,
        'continuum_contrast':None,'chains':chains}
    return report

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--root',default='checkpoints');ap.add_argument('--output',default='stage8_admission.json');ap.add_argument('--skip-npz',action='store_true');args=ap.parse_args()
 obj=audit(args.root,check_npz=not args.skip_npz)
 Path(args.output).write_text(json.dumps(obj,indent=2))
 print('admission: chains',obj['n_chains_present'],'production',obj['production_samples_total'],
       'mass',obj['mass_estimate'],'sigma',obj['string_tension_estimate'])
