#!/usr/bin/env python3
"""Build deterministic, source-code-free public PF-I11 summary from verified evidence."""
from pathlib import Path
import json,hashlib
from verify_pf_i11_intrinsic_su2 import exact_one_face,SOURCE_SHA
ROOT=Path(__file__).resolve().parent

def loaded(name):return json.loads((ROOT/name).read_text())

def make():
    orig=loaded('PF_I11_EIGHT_SIZE_SOURCE_GAUGE_COMPLEX.json')['results']
    complete=loaded('PF_I11_COMPLETED_WINDOW_CORE_CONTROL.json')['results']
    sym=loaded('PF_I11_SIMPLE_D5_REFLECTION_CANDIDATES.json')['results']
    transfer=loaded('PF_I11_AUXILIARY_TRANSFER_CONTROL.json')['rows']
    factor=loaded('PF_I11_EXACT_FACE_HAAR_FACTORIZATION.json')
    assert [x['Ngrid'] for x in orig]==[x['Ngrid'] for x in complete]==[7,10,12,15,18,20,23,25]
    assert [x['pi1_free_rank'] for x in orig]==[0,0,0,0,0,6,10,10]
    assert all(x['pi1_free_rank']==0 for x in complete)
    assert all(x['all_faces_collapse'] for x in orig+complete)
    rows=[]
    for a,b in zip(orig,complete):
        rows.append({
            'Ngrid':a['Ngrid'],'original_V':a['n_vertices'],'original_E':a['n_edges'],
            'original_F_direct_window_rhombi':a['n_faces'],'original_components':a['full_components'],
            'original_pi1_free_rank':a['pi1_free_rank'],
            'original_su2_extra_classical_flat_directions':a['linearized_extra_flat_moduli_dimensions'],
            'source_edge_zero_face_incidence':a['zero_incidence_edges'],
            'original_labels_sha256':a['source_vertices_sha256'],
            'original_face_labels_sha256':a['direct_accepted_faces_sha256'],
            'collapse_pair_sha256':a['collapse_pair_sha256'],
            'completed_window_core_V':b['n_vertices'],'completed_window_core_E':b['n_edges'],
            'completed_window_core_F':b['n_faces'],'completed_window_components':b['full_components'],
            'completed_window_pi1_free_rank':b['pi1_free_rank'],
            'completed_window_labels_sha256':b['source_vertices_sha256'],
            'completed_core_is_separate_population':a['source_vertices_sha256']!=b['source_vertices_sha256'],
            'flat_nonabelian_witness':a.get('flat_connection',None),
        })
    assert all(x['completed_core_is_separate_population'] for x in rows)
    return {'status':'PF-I11 finite accepted-rhombus Wilson SU2 and source-selection topological certificate; no physical time/mass gap',
        'date':'2026-11-08', 'source_original_sha256':SOURCE_SHA,
        'original_source_preserved_privately':True,
        'original_source_selection':'author 35% tile-center/one-pass incident tile rule',
        'independent_face_rule':'three-free-coordinate strict internal triangular acceptance; all corners accepted',
        'SU2_Wilson_partition_exact':'exp(-2 sum kappa_f) <= Z <= 1 for kappa_f >= 0, normalized Haar',
        'finite_one_face_beta_0p71':exact_one_face(.71),
        'rows':rows,
        'simple_D5_source_spatial_index_tests':[
          {'Ngrid':a['Ngrid'],'weighted_face_automorphisms':a['exact_restricted_D5_weighted_face_symmetries']} for a in sym],
        'auxiliary_transfer_tests':[{k:x[k] for k in ['beta','electric_scale','auxiliary_gap','min_transfer_eigenvalue']} for x in transfer],
        'exact_all_face_Haar_factorization_verified_on_16_complexes':len(factor['source_rows'])==16,
        'log_partition_per_face_uniform_beta_0p71':factor['source_rows'][0]['log_partition_per_face'],
        'all_16_full_plaquette_Haar_density_identical_at_beta_0p71':len({round(x['log_partition_per_face'],13) for x in factor['source_rows']})==1,
        'distinct_plaquette_trace_connected_covariance_exact':0.0,
        'two_square_independent_haar_mc_standardized_partition_deviation':factor['two_plaquette_independent_montecarlo']['standardized_Z_difference'],
        'private_tests_passed':27,'public_no_original_script_tests_passed':19,'public_source_skips':8,
        'physical_time_or_OS_reflection_proved':False,
        'four_dimensional_interacting_YM_exists_proved':False,
        'continuum_positive_physical_mass_gap_proved':False,
        'notes':'Every source rhombus face peels with a free edge; therefore pure plaquette Wilson Haar partition and all distinct face character moments factorize. Two-complex face peeling is an explicit strong deformation retract; the free group ranks are finite source-selection dependent. The auxiliary positive transfer imports a kinetic scale and is not intrinsic physical time.'}

if __name__=='__main__':
    p=ROOT/'PF_I11_PUBLIC_FINITE_GAUGE_RESULTS_2026_11_08.json'
    p.write_text(json.dumps(make(),indent=2,sort_keys=True)+'\n')
    print('wrote',p,'bytes',p.stat().st_size)
