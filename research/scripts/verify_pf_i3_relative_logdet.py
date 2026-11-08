#!/usr/bin/env python3
"""PF-I3 second source audit: Paper4 relative logdet and Paper2 mode counts.

Proves exact finite eigenvalue formulas; performs ONE-calibrated-conductance finite
P3 versus triangular control. Does NOT replicate Paper2 or Paper4 original code.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from verify_pf_i3_spectral_moments import p3_matrices,control_patch

SOURCE_NGRID=[7,10,12,15,18,20,23,25]
SOURCE_PAPER2_NINT=[1550,3042,4324,6980,9950,12207,16435,19260]
SOURCE_PAPER4_ZPRIME_N=[1550,3042,4324,6979,9947,12206,16434,19255]
SOURCE_PAPER4_GAMMA_REL_RATIOS={'0.0001':0.959,'0.01':0.927,'1':0.816,'100':0.739}
SOURCE_PAPER4_ZPRIME_RATIO=0.646
SOURCE_PAPER2_RM1=0.7371
PAPER1_M2=1e-4


def spec_positive(L,tol=1e-9):
    eig=eigh(L,eigvals_only=True,check_finite=False,driver='evr')
    assert eig[0]>-tol
    pos=eig[eig>tol]
    return pos,int(len(eig)-len(pos))


def gamma_relative(eig,m2):
    assert m2>0 and len(eig)>0
    return float(np.log1p(eig/m2).mean()/2)


def gamma_from_source_paper4_equation(eig,m2):
    zprime=-np.log(eig+m2).mean()
    z0=1.0
    return float(-zprime/2-z0*math.log(m2)/2)


def one_patch(radius,nmax,m2fit=PAPER1_M2):
    q=p3_matrices(radius,nmax); t=control_patch(q['n'],'triangle')
    # EXACTLY one fitted scalar, period-control conductance alpha, based only
    # on P2's R(-1)=0.7371. Not fitted to the 4 P4 mass-flow ratios.
    alpha=((q['mean_weighted_degree']+m2fit)/SOURCE_PAPER2_RM1-m2fit)/t['mean_degree']
    eq,nzero_q=spec_positive(q['weighted_strength']);ep,nzero_p=spec_positive(alpha*t['lap'])
    assert nzero_q==nzero_p==1
    samples={}; maxerr=0
    for s,source_ratio in SOURCE_PAPER4_GAMMA_REL_RATIOS.items():
        m2=float(s)
        gq=gamma_relative(eq,m2);gp=gamma_relative(ep,m2)
        q_from_paper4=gamma_from_source_paper4_equation(eq,m2)
        p_from_paper4=gamma_from_source_paper4_equation(ep,m2)
        assert abs(gq-q_from_paper4)<1e-11, (m2,gq,q_from_paper4)
        assert abs(gp-p_from_paper4)<1e-11, (m2,gp,p_from_paper4)
        pred=gq/gp;maxerr=max(maxerr,abs(pred-source_ratio))
        samples[s]={'paper4_reported':source_ratio,'conditional_P3_control':pred,
                    'difference':pred-source_ratio,'P3_gamma_rel_per_mode':gq,
                    'triangle_gamma_rel_per_mode':gp}
    src_zpr_q=float(-np.log(eq+m2fit).mean());src_zpr_p=float(-np.log(ep+m2fit).mean())
    return {
        'n':q['n'],'p3_edges':q['e'],'periodic_edges':t['e'],'p3_zero_modes_removed':nzero_q,
        'periodic_zero_modes_removed':nzero_p,'positive_eigenvalue_count_each':len(eq),
        'single_periodic_conductance_calibrated_at_Paper2_R_minus1':alpha,
        'full_mode_trace_R_minus1_used_for_calibration':SOURCE_PAPER2_RM1,
        'paper4_gamma_mass_flow':samples,
        'maximum_absolute_difference_vs_Paper4_table':maxerr,
        'zeta_prime_ratio_at_Paper1_m2':src_zpr_q/src_zpr_p,
        'paper4_reported_eight_size_mean_zeta_prime_ratio':SOURCE_PAPER4_ZPRIME_RATIO,
        'm2_to_infinity_relative_gamma_ratio_limit':float(eq.mean()/ep.mean()),
        'm2_to_zero_relative_gamma_ratio_limit':1.0,
        'original_Paper2_or_Paper4_generator_reproduced':False
    }


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    diffs=[p2-p4 for p2,p4 in zip(SOURCE_PAPER2_NINT,SOURCE_PAPER4_ZPRIME_N)]
    assert diffs==[0,0,0,1,3,1,1,5]
    rows=[]
    for r,nmax in [(6.5,11),(12.,12)]:rows.append(one_patch(r,nmax))
    j={
        'date':'2026-11-07','proof_scope':'exact finite relative logdet asymptotics and nonunique calibrated P3 source-equation control',
        'paper4_reference':'Sharpe Paper4 §§2-3, 7.2,10.1; original report not independent reproduction',
        'source_Paper2_Ngrid':SOURCE_NGRID,'source_Paper2_Nint':SOURCE_PAPER2_NINT,
        'source_Paper4_zeta_prime_N':SOURCE_PAPER4_ZPRIME_N,
        'N_difference_Paper2_minus_Paper4_zeta_prime':diffs,
        'N_difference_is_automatically_zero_mode_count':False,
        'source_Paper4_reported_zeta_prime_mean':SOURCE_PAPER4_ZPRIME_RATIO,
        'source_Paper4_reported_Gamma_relative_table':SOURCE_PAPER4_GAMMA_REL_RATIOS,
        'paper4_Gamma_formula_exact':'1/(2N) sum log(1+lambda/m2), with m2>0 and positive-mode exclusion',
        'paper4_mass_flow_endpoints_generic_not_unique_to_Z5':True,
        'candidate_control_calibration_uses_Paper2_R_minus1_only':True,
        'candidate_control_results':rows,
        'Yang_Mills_mass_gap_or_gravity_UV_proved':False
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(j,indent=2,sort_keys=True)+'\n')
    print(json.dumps({
        'N_discrepancies':diffs,
        'P4_source_flow':SOURCE_PAPER4_GAMMA_REL_RATIOS,
        'control':[{'n':r['n'],'calibration':r['single_periodic_conductance_calibrated_at_Paper2_R_minus1'],
                    'predicted':{k:round(v['conditional_P3_control'],6) for k,v in r['paper4_gamma_mass_flow'].items()},
                    'max_abs_error':r['maximum_absolute_difference_vs_Paper4_table'],
                    'zeta_prime_ratio':r['zeta_prime_ratio_at_Paper1_m2']}
                   for r in rows]},indent=2))
if __name__=='__main__':main()
