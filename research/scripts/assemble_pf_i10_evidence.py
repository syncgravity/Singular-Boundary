#!/usr/bin/env python3
"""Canonical, timing-free PF-I10 spectral summary; preserve source/data provenance."""
from pathlib import Path
import json,math,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parent
FILES=['PF_I10_MULTIMASS_FIRST4.json','PF_I10_MULTIMASS_LAST4.json',
       'PF_I10_MULTIMASS_N23.json','PF_I10_MULTIMASS_N25.json']
ROWS={r['Ngrid']:r for f in FILES for r in json.loads((ROOT/f).read_text())['rows']}
assert sorted(ROWS)==[7,10,12,15,18,20,23,25]
EXACT={r['Ngrid']:r for r in json.loads((ROOT/'PF_I10_EXACT_THREE_SIZES.json').read_text())['rows']}
TILE={r['Ngrid']:r for f in ['PF_I10_TILE_SPECTRAL_7_10_12.json','PF_I10_TILE_SPECTRAL_25.json']
          for r in json.loads((ROOT/f).read_text())['rows']}
SEP={'sqrt':'sqrt','log':'zeta_prime','relative_log':'relative_logdet'}
MASSES=['0.0001','0.01','1.0','100.0']
out=[]
for n in sorted(ROWS):
 r=ROWS[n];row={'Ngrid':n,'vertices':r['QC']['n'],'source_basis_edges':r['QC']['edges'],
  'QC_components':r['QC']['components'],'periodic_vertices':r['periodic']['n'],
  'periodic_edges':r['periodic']['edges'],'periodic_weight':r['periodic']['weight'],
  'source_zeta_negative_one_trace':float(r['QC']['trace_over_n']+1e-4)/(r['periodic']['trace_over_n']+1e-4),
  'spectral_method':'exact_dense_eigvalsh' if n in EXACT else 'stochastic_Lanczos_trace_control',
  'slq_probes':r['source_slq']['probes'],'slq_steps':r['source_slq']['steps'],
  'source_weighted_spectra':{},'uniform_same_graph_ratio':{},'uniform_to_periodic_ratio':{}}
 for m in MASSES:
  row['source_weighted_spectra'][m]={}
  for func,field in SEP.items():
   estimate=r['ratios'][m][func]['trace_control']
   if n in EXACT:
    q=EXACT[n]['ratios'][m][field]['source_over_periodic'];SE=0.
    fibuni=EXACT[n]['ratios'][m][field]['source_over_uniform']
    uniper=EXACT[n]['ratios'][m][field]['uniform_over_periodic']
   else:
    q=estimate['positive'];SE=estimate['positive_SE_independent']
    fibuni=r['fib_over_same_graph_uniform'][m][func]['trace_control']['positive']
    uniper=r['same_graph_uniform_over_periodic'][m][func]['trace_control']['positive']
   if abs(q-fibuni*uniper)>5e-5:raise AssertionError(('bad factor',n,m,func,q,fibuni*uniper))
   row['source_weighted_spectra'][m][func]={'ratio_positive_modes':q,'conditional_probe_standard_error':SE,
                                             'comparison':field}
   if m=='0.0001':
    row['uniform_same_graph_ratio'][func]=fibuni
    row['uniform_to_periodic_ratio'][func]=uniper
 if n in TILE:
  row['original_truncated_tile_graph']={k:v for k,v in TILE[n].items() if k not in ('exact_tile_eigenvalues','exact_periodic_eigenvalues')}
 out.append(row)

def summarize(m,f):
 vals=[r['source_weighted_spectra'][m][f]['ratio_positive_modes'] for r in out]
 ses=[r['source_weighted_spectra'][m][f]['conditional_probe_standard_error'] for r in out]
 return {'arithmetic_mean':float(np.mean(vals)),'sample_standard_deviation_across_eight_sizes':float(np.std(vals,ddof=1)),
         'conditional_standard_error_of_mean_from_independent_probes_only':float(math.hypot(*ses)/8),
         'n_exact':3,'n_stochastic':5}
summary={
 'schema':'singular-boundary.pf-i10.source-spectra.v1','scope':'finite scalar source cut-project; first 3 exact and last 5 stochastic, no gauge gap',
 'source_script_sha256':'86ce0bf4e0688899a2f1c9dba980cb6d996c3fef59889807ee8376d6e62369da',
 'all_spectra_original_source_retained_vertices':True,
 'completed_window_recomputed_core_used_in_spectra':False,
 'coupled_basis_graph_equals_completed_tile_edges_on_same_original_retained_labels':True,
 'source_operator':'L=D_weight-W, original source Fibonacci t_j(level)',
 'comparison':'source finite zigzag triangular periodic, q=floor(sqrt N), tavg=(1+phi^-2)/2',
 'zero_filter':'eigenvalues > 1e-10; in stochastic calculations subtract exactly c zero modes using component count before normalizing',
 'mass_squared_values':[0.0001,0.01,1.0,100.0],
 'source_claims_provisional_unpublished':{'R_s_minus_half_eight_size_mean':0.8332,'zeta_prime_mean_approx':0.646,
             'relative_logdet_mass_flow':[0.959,0.927,0.816,0.739]},
 'eight_size_spectral_means':{f:summarize('0.0001',f) for f in SEP},
 'eight_size_relative_logdet_mass_flow':{m:summarize(m,'relative_log') for m in MASSES},
 'eight_size_same_graph_fibonacci_uniform_mean':{f:float(np.mean([r['uniform_same_graph_ratio'][f] for r in out])) for f in SEP},
 'eight_size_uniform_topology_vs_periodic_mean':{f:float(np.mean([r['uniform_to_periodic_ratio'][f] for r in out])) for f in SEP},
 'N25_160_to_240_step_fixed_probe_convergence':{},
 'original_tile_cutoff_components_from_exact_source':{},
 'proof_gates':{'finite_scalar_source_spectral_reproduction':'three_exact_plus_five_stochastic','interacting_4D_SU2_Yang_Mills_existence':False,
                'continuum_positive_mass_gap':False,'gravitational_UV_finiteness':False},
 'limitations':['Stochastic trace samples and SE do not give deterministic quadrature or thermodynamic error bounds',
                'm2=1e-4 fixed; paper source and manuscript number not assumed authoritative',
                'physical-dimensional Yang-Mills operator and gauge measure not constructed',
                'eight-size arithmetic means are not continuum limits'],
 'rows':out}
L=json.loads((ROOT/'PF_I10_MULTIMASS_N25.json').read_text())['rows'][0]
H=json.loads((ROOT/'PF_I10_MULTIMASS_N25_CONVERGENCE240.json').read_text())['rows'][0]
for m in MASSES:
 summary['N25_160_to_240_step_fixed_probe_convergence'][m]={}
 for f in SEP:
  a=L['ratios'][m][f]['trace_control']['positive'];b=H['ratios'][m][f]['trace_control']['positive']
  summary['N25_160_to_240_step_fixed_probe_convergence'][m][f]={
    'lanczos_160':a,'lanczos_240':b,'absolute_difference':abs(a-b),
    'same_source_random_seed_probes':True}
for r in json.loads((ROOT/'PF_I10_TILE_CUTOFF_EXACT_EVIDENCE.json').read_text())['rows']:
 summary['original_tile_cutoff_components_from_exact_source'][str(r['Ngrid'])]={k:r[k] for k in ['tile_edges','coupled_edges','source_coupled_minus_tile_edges','components_tile','components_coupled','trace_Delta_L_over_N']}
(ROOT/'PF_I10_EIGHT_SIZE_SPECTRAL_SUMMARY.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
# Full source model numeric evidence, deterministic by omitting timing fields
raw_files=FILES+['PF_I10_EXACT_THREE_SIZES.json','PF_I10_TILE_CUTOFF_EXACT_EVIDENCE.json',
         'PF_I10_TILE_SPECTRAL_7_10_12.json','PF_I10_TILE_SPECTRAL_25.json',
         'PF_I10_MULTIMASS_N25_CONVERGENCE240.json']
def strip_nonreplayable(o):
 if isinstance(o,dict):return {k:strip_nonreplayable(v) for k,v in o.items() if k not in ('elapsed_sec','duration_sec','elapsed_s')}
 if isinstance(o,list):return [strip_nonreplayable(v) for v in o]
 return o
all_raw={name:strip_nonreplayable(json.loads((ROOT/name).read_text())) for name in raw_files}
(ROOT/'PF_I10_COMPLETE_SPECTRAL_REPLAY_EVIDENCE.json').write_text(json.dumps(all_raw,indent=2,sort_keys=True)+'\n')
print('source-hybrid means',json.dumps({f:summary['eight_size_spectral_means'][f]['arithmetic_mean'] for f in SEP},indent=2))
print('source-hybrid mass flow',json.dumps({m:summary['eight_size_relative_logdet_mass_flow'][m]['arithmetic_mean'] for m in MASSES},indent=2))
print('summary JSON size', (ROOT/'PF_I10_EIGHT_SIZE_SPECTRAL_SUMMARY.json').stat().st_size)
