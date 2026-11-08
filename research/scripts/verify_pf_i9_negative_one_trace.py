#!/usr/bin/env python3
"""PF-I9: exact finite zeta(-1) trace from source-weighted graph dictionaries.

No eigenvalue calculation or fitted conductance. Triangular comparator follows
paper6_extend_local.py build_periodic_laplacian: finite (floor sqrt N)^2,
triangular zigzag bond pattern, every edge at tavg=(1+phi^-2)/2.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np


def compute(src, mass2):
    phi=(1+math.sqrt(5))/2
    tavg=(1+phi**-2)/2
    rows=[]
    for row in src['size_rows']:
        ng=row['Ngrid'];n=row['source_retained_vertices'];q=row['source_coupled_scalar_weighted_moments'];
        side=math.isqrt(n)
        nper=side*side
        edge_per=(side-1)*(3*side-1)
        mean_per=2*edge_per*tavg/nper
        mean_qc=q['traceL_div_N'];zeros=q['weighted_laplacian_nullity']
        # Full N-mode regularized finite spectral moment; no eigenvectors.
        full=(mean_qc+mass2)/(mean_per+mass2)
        # Source positive-mode-only convention renormalizes each retained set.
        positive=(mean_qc*n/(n-zeros)+mass2)/(mean_per*nper/(nper-1)+mass2)
        # Pure hopping factor on the SAME QC accepted graph.
        uniform_qc=tavg*q['mean_degree'];
        hop_ratio=(mean_qc+mass2)/(uniform_qc+mass2)
        topo_ratio=(uniform_qc+mass2)/(mean_per+mass2)
        assert abs(hop_ratio*topo_ratio-full)<1e-12
        rows.append({'Ngrid':ng,'N_QC':n,'N_periodic':nper,
            'periodic_lattice_side':side,'periodic_triangle_bond_count':edge_per,
            'periodic_bond_weight_tavg':tavg,
            'QC_component_count_exact':zeros,
            'QC_traceL_over_N':mean_qc,'periodic_traceL_over_N':mean_per,
            'R_s_minus_one_full_modes':full,
            'R_s_minus_one_positive_modes_only':positive,
            'same_graph_fibonacci_over_uniform_factor_at_minus_one':hop_ratio,
            'uniform_QC_over_periodic_factor_at_minus_one':topo_ratio,
            'exact_decomposition_reconstructed':True})
    vals=np.asarray([r['R_s_minus_one_full_modes'] for r in rows]);p=np.asarray([r['R_s_minus_one_positive_modes_only'] for r in rows]);
    return {'mass_squared_assumed':mass2,'not_used_to_fit_any_parameter':True,
            'formula':'zeta_{L,m}(-1)=m2 + 2 * sum_edge_weights / N, finite symmetric weighted-strength L',
            'source_periodic_unit_bond_assumption':False,
            'periodic_as_implemented':'triangular finite open patch floor(sqrt N)^2, t_avg=(1+phi^-2)/2',
            'source_reported_mean_R_minus_one':0.7371,
            'mean_R_minus_one_full_modes':float(vals.mean()),
            'sample_sd_full_modes':float(vals.std(ddof=1)),
            'mean_R_minus_one_positive_modes_only':float(p.mean()),
            'both_rounded_to_reported_4_decimals':round(float(vals.mean()),4)==round(float(p.mean()),4)==0.7371,
            'source_mass_squared_and_zero_filter_not_identifiable_from_4decimal_mean_alone':True,
            'rows':rows}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();data=json.loads(args.input.read_text())
    out={'scope':'exact source-operator trace, not source full spectrum or continuum YM',
         'full_unregulated':compute(data,0.0),'full_mass2_1e_minus4':compute(data,1e-4)}
    args.output.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'unregulated':out['full_unregulated']['mean_R_minus_one_full_modes'],
                      'mass_squared_1e_minus4':out['full_mass2_1e_minus4']['mean_R_minus_one_full_modes'],
                      'positive_mode_only':out['full_mass2_1e_minus4']['mean_R_minus_one_positive_modes_only']},indent=2))
