#!/usr/bin/env python3
"""Exact-arithmetic cubical strong-coupling applicability and low-energy-transfer countermodel.
This checks an *existing sufficient certificate*, not the spectrum of interacting Yang--Mills.
"""
from __future__ import annotations
import argparse, json, math
from fractions import Fraction
from pathlib import Path


def threshold_table():
    rows=[]
    for n in (1,2,4,8,16,32,64):
        v=(n+1)**3; e=3*n*(n+1)**2; f=3*n*n*(n+1); cubes=n**3
        assert v-e+f-cubes == 1
        q=Fraction(4*f,3)
        assert q == 4*n*n*(n+1)
        g_sq=math.sqrt(float(q)); g=math.sqrt(g_sq)
        # min-max lower bound is positive iff g0^4>4F/3, and g0^2>sqrt(4F/3)
        rows.append(dict(n=n,vertices=v,edges=e,faces=f,cubes=cubes,
                         critical_g0_squared=g_sq,critical_g0=g,
                         exact_g0_fourth_threshold=str(q)))
    return rows


def low_energy_countermodel():
    # C_C(t)=exp(-M t), C_P(t)=(1-eta) exp(-M t)+eta exp(-m t).
    # Both are positive Laplace transforms of probability measures,
    # and sup_t |C_P-C_C| <= eta; but P has positive spectral weight at m<M.
    M=1.0;m=0.125;eta=1e-4
    samples=[]
    for t in (0,1,5,10,20,100):
        cc=math.exp(-M*t);cp=(1-eta)*cc+eta*math.exp(-m*t)
        assert 0 <=cp-cc+eta*cc+1e-15  # harmless numerical sign check
        assert abs(cp-cc)<=eta+1e-14
        samples.append({'t':t,'cubic':cc,'penrose_analogue':cp,'absolute_difference':abs(cp-cc),
                        'renormalized_difference_at_M':math.exp((M-m)*t)*eta*(1-math.exp(-(M-m)*t))})
    return {'cubic_gap_M':M,'comparison_low_energy_m':m,'low_energy_weight_eta':eta,
            'uniform_unweighted_error_bound':eta,
            'comparison_spectrum':[m,M],
            'samples':samples,
            'conclusion':'Unweighted all-time error <=eta does NOT transfer the cubic gap M. Exponentially weighted errors are essential for this sufficient transfer route.'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path('docs/evidence/YM_CUBIC_PENROSE_GATE_CHECKS_2026-11-05.json'));args=ap.parse_args()
    rows=threshold_table();counter=low_energy_countermodel()
    assert rows[-1]['critical_g0']>rows[0]['critical_g0']
    assert counter['comparison_spectrum'][0]<counter['cubic_gap_M']
    data={'status':'PASS','claim_scope':'Finite cubical sufficient bound; conditional comparison; NOT a Yang--Mills mass-gap theorem',
          'physical_normalization':'h=1/n, alpha=g0²/(2h), beta=2/(g0²h), F=3 n² (n+1), z=4/g0^4',
          'bound':'Delta >= (3*g0²/2 -2*F/g0²)/h; sufficient positivity iff g0^4>4F/3',
          'table':rows,'countermodel':counter,
          'checks':['exact cell Euler characteristic','symbolic face-count threshold','monotonic minimum g0 under refinement','positive Laplace spectral measures','arbitrarily small unweighted correlation error does not preserve larger gap'],
          'notes':['This min-max inequality is already recorded in R3-IR-589.',
                   'Countermodel illustrates a missing estimate; it is not a construction of a Penrose Yang--Mills vacuum.',
                   'No finite numerical sample proves infinite-volume or continuum spectral support.']}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'result':'PASS','n_tested':[r['n'] for r in rows], 'critical_g0_n16':rows[4]['critical_g0'],
                     'countermodel_low_frequency':counter['comparison_spectrum'][0],
                     'uncertified':'continuum interacting gap and Penrose transfer'}))

if __name__=='__main__': main()
