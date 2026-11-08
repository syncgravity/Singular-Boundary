#!/usr/bin/env python3
"""PF-I12 conditional SU2 heat-kernel reflection-positive TWO-FACE control.

The pair-exchange positive kernel is an EXISTENCE CONTROL, not an intrinsic
physical temporal involution on the aperiodic Z5 source complex. The heat
parameter t>0 is NOT derived from the user's 2+2 field geometry.
"""
import argparse,json,math
from pathlib import Path
import numpy as np
from verify_pf_i11_intrinsic_su2 import qmul,qconj,unit_quaternion


def su2_heat_character_kernel(halftrace,t,nmax=64):
    """Central SU2 heat kernel K_t(g)=sum_(n>=0)(n+1)e^(-t n(n+2)/4) U_n(x)."""
    if t<=0:raise ValueError('Strictly positive auxiliary heat parameter required')
    x=np.asarray(halftrace,dtype=float)
    if np.any(np.abs(x)>1+1e-9):raise ValueError('SU2 halftrace must lie in [-1,1]')
    x=np.clip(x,-1,1)
    prev=np.ones_like(x);curr=2*x
    z=prev.copy()
    for n in range(1,nmax+1):
        if n==1:un=curr
        else:
            un=2*x*curr-prev
            prev,curr=curr,un
        z+=(n+1)*np.exp(-t*n*(n+2)/4)*un
    return z


def check_kernel(t=.85,num=16,seed=622):
    rng=np.random.default_rng(seed)
    q=unit_quaternion(rng,(num,))
    a=q[:,None,:];b=q[None,:,:]
    rel=qmul(a,qconj(b))[...,0]
    gram=su2_heat_character_kernel(rel,t)
    evals=np.linalg.eigvalsh(gram)
    pred=np.exp(-.75*t)/4
    assert np.max(np.abs(gram-gram.T))<1e-12
    assert evals.min()>=-1e-11
    return {'t_auxiliary':t,'sample_count':num,'seed':seed,
            'kernel_min_SPD_Gram_eigenvalue':float(evals.min()),
            'kernel_hermitian_symmetry_error':float(np.max(np.abs(gram-gram.T))),
            'one_pair_heat_reflection_Peter_Weyl':'nonnegative expansion d_j exp(-t*j(j+1)), giving positive definite kernel K_t(A B^-1)',
            'pair_exchange_reflection_conditional_not_source_time':True,
            'exact_fundamental_halftrace_connected_correlation':pred,
            'exact_Z_two_face_under_Haar':1.0,
            'lambda_or_heat_time_not_source_selected':True,
            'full_Z5_global_OS_reflection_proved':False,
            'continuum_YM_mass_gap_proved':False}


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--t',type=float,default=.85)
    a=p.parse_args();out=check_kernel(a.t)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out)
if __name__=='__main__':main()
