#!/usr/bin/env python3
"""PF-I11 exact Haar factorization for any free-face-collapsible 2-complex.

This exact mathematical result applies to the SOURCE geometry and its separate
completed-window control. It does NOT furnish a 4D interacting YM continuum.
"""
from __future__ import annotations
import json,math,argparse
from pathlib import Path
import numpy as np
from verify_pf_i11_intrinsic_su2 import exact_one_face,qconj,qmul,unit_quaternion


def finite_factorization_from_counts(faces,beta):
    if faces<0 or beta<0:raise ValueError('faces and beta must be nonnegative')
    r=exact_one_face(beta)
    # Each successful face-edge elementary collapse allows integration over
    # one SU2 Haar link used by one remaining face only, yielding z(beta).
    return {'faces':faces,'beta':beta,'single_face_Z':r['Z'],
            'single_face_mean_halftrace':r['mean_halftrace'],
            'log_partition':float(faces*math.log(r['Z'])),
            'log_partition_per_face':float(math.log(r['Z'])) if faces else 0.,
            'two_distinct_face_connected_trace_covariance_exact':0.0}


def direct_two_face_haar_montecarlo(beta1=.71,beta2=1.23,samples=120000,seed=119):
    """Independent SU2 Haar-link check on two adjacent square faces sharing edge.

    Plaquette1 link product [u0 u1 u2 u_shared], Plaquette2 product
    [u_shared^-1 v0 v1 v2]. Distinct link variables are independent Haar.
    """
    rng=np.random.default_rng(seed)
    # Only 7 distinct links, one common. This is a small CONVENTIONAL
    # algebraic control, never substituted for source cut-project geometry.
    U=unit_quaternion(rng,(samples,7))
    first=qmul(qmul(qmul(U[:,0],U[:,1]),U[:,2]),U[:,3])
    second=qmul(qmul(qmul(qconj(U[:,3]),U[:,4]),U[:,5]),U[:,6])
    x=first[:,0];y=second[:,0]
    weights=np.exp(-beta1*(1-x)-beta2*(1-y))
    Z=float(np.mean(weights));Z_se=float(np.std(weights,ddof=1)/math.sqrt(samples))
    ex=float(np.mean(weights*x)/Z);ey=float(np.mean(weights*y)/Z)
    cxy=float(np.mean(weights*x*y)/Z-ex*ey)
    zpred=exact_one_face(beta1)['Z']*exact_one_face(beta2)['Z']
    return {'sample_count':samples,'seed':seed,'beta1':beta1,'beta2':beta2,
            'direct_haar_sample_partition':Z,'direct_haar_sample_standard_error':Z_se,
            'exact_collapse_factorized_partition':zpred,
            'standardized_Z_difference':float((Z-zpred)/Z_se),
            'weighted_plaquette_halftrace_x':ex,'weighted_plaquette_halftrace_y':ey,
            'weighted_connected_plaquette_halftrace_covariance':cxy,
            'exact_connected_covariance':0.,
            'scope':'Finite algebraic two-square Monte Carlo crosscheck; exact theorem by conditional free-link Haar integration, not by MC.'}


def summary(source_file,core_file,beta=.71):
    src=json.loads(Path(source_file).read_text())['results']
    core=json.loads(Path(core_file).read_text())['results']
    assert len(src)==len(core)==8
    rows=[]
    for a,b in zip(src,core):
        for name,t in [('original_source',a),('completed_window_core',b)]:
            assert t['all_faces_collapse']
            rows.append({'Ngrid':t['Ngrid'],'selection':name,'components':t['full_components'],
                'fundamental_group_free_rank':t['free_group_rank_if_complete'],
                **finite_factorization_from_counts(t['n_faces'],beta)})
    return {'checkpoint':'PF-I11-E','exact_theorem':'Haar partition and all individual face-holonomy class-function moments factorize for any finite 2-complex admitting a complete sequence of face/free-edge collapses.',
            'status':'Exact finite 2D plaquette-only Wilson result; NO continuum 4D interacting YM or physical gap claim',
            'coupling_convention':'unit per-rhombus kappa=beta, arbitrary test coupling NOT source physical coupling',
            'source_rows':rows,'single_plaquette_example':exact_one_face(beta),
            'two_plaquette_independent_montecarlo':direct_two_face_haar_montecarlo(),
            'physical_mass_gap_proved':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source-evidence',type=Path,required=True)
    p.add_argument('--completed-evidence',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--beta',type=float,default=.71)
    a=p.parse_args();o=summary(a.source_evidence,a.completed_evidence,a.beta)
    a.output.write_text(json.dumps(o,sort_keys=True,indent=2)+'\n')
    print('factorized exact',len(o['source_rows']),'samples','single per-face logZ',math.log(exact_one_face(a.beta)['Z']))
    print('two-square Monte Carlo source deviation',o['two_plaquette_independent_montecarlo']['standardized_Z_difference'])
