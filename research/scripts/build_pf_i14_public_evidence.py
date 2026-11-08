#!/usr/bin/env python3
"""Consolidate source-verified PF-I14 finite aggregate data; raw labels stay private."""
import json
from pathlib import Path
root=Path(__file__).resolve().parent
s=json.loads((root/'evidence/PF_I14_EIGHT_SIZE_SOURCE_COVARIANCE.json').read_text())
c=json.loads((root/'evidence/PF_I14_TWO_COMPLETED_CORE_COVARIANCE.json').read_text())
h=json.loads((root/'evidence/PF_I14_GAUGE_PROJECTED_FINITE_SEAM.json').read_text())
rows=[]
for n,x in sorted(s['source_finite'].items(),key=lambda e:int(e[0])):
 rows.append({
  'Ngrid':int(n),'original_vertices':x['V'],'original_basis_edges':x['E'],'original_rhombi':x['F'],
  'PF_I11_vertex_digest':x['source_vertex_SHA256'],'PF_I11_face_digest':x['source_face_SHA256'],
  'fixed_source_same_word_mismatch':x['same_fixed_hopping_word_mismatch_count'],
  'reflected_phase_but_wrong_lower_convention_mismatch':x['singular_lower_lower_mismatch_edges'],
  'wrong_lower_affected_levels':x['singular_lower_lower_level_histogram'],
  'correct_phase_and_upper_convention_mismatch':x['edge_hopping_type_mismatches_under_decorated_theta'],
  'reflected_incidence_faces_exact':x['all_reflected_source_faces_match_exactly'],
  'weighted_laplacian_vertex_permutation_equivalence':x['source_weighted_operator_unitarily_equivalent_by_vertex_permutation'],
  'local_gauge_action_intertwines':x['gauge_action_intertwines_exact_source_vertex_map'],
  'Wilson_action_absolute_difference':x['Wilson_face_action_absolute_difference'],
  'transverse_pairs':x['nonabelian_two_face_action']['transverse_pair_count'],
  'paired_commutator_max_absolute_difference':x['nonabelian_two_face_action']['pair_penalty_max_absolute_discrepancy'],
 })
completed=[]
for n,x in sorted(c['results'].items(),key=lambda e:int(e[0])):
 completed.append({
  'Ngrid':int(n),'completed_window_vertices':x['V'],'completed_window_edges':x['E'],
  'completed_window_rhombi':x['F'],'PF_I11_completed_SHA_matches':x['PF_I11_completed_reference_SHA256_verified'],
  'fixed_source_same_word_mismatch':x['same_fixed_hopping_word_mismatch_count'],
  'phase_shift_without_upper_mismatch':x['singular_lower_lower_mismatch_edges'],
  'correct_decorated_reflection_mismatch':x['edge_hopping_type_mismatches_under_decorated_theta'],
  'completed_original_population_not_interchanged':x['original_source_not_replaced'],
 })
out={
 'milestone':'PF-I14','date':'2026-11-08',
 'scope':'exact mathematical extension of unpublished source hopping and finite paired-hull gauge covariance; NOT physical time/OS/continuum proof',
 'original_source_script_private_SHA256':'86ce0bf4e0688899a2f1c9dba980cb6d996c3fef59889807ee8376d6e62369da',
 'exact_sturmian_reversal':s['sturmian_certificate'],
 'height_preserving_group_action':s['semidirect_group_certificate'],
 'all_eight_original_source_rows':rows,
 'source_height_preserving_translation_tests':s['source_translations'],
 'separate_two_completed_window_controls':completed,
 'auxiliary_actual_link_gauge_projected_heat_seam':h,
 'source_original_chosen_hopping_fixed_under_geometric_inversion':False,
 'decorated_reflection_covariance_of_mathematical_extended_hull_proved':True,
 'gauge_projected_link_heat_transfer_positive_conditionally':True,
 'source_physical_time_proved':False,
 'source_authorized_Fibonacci_phason_dynamics_proved':False,
 'original_YM_global_OS_reflection_positive_proved':False,
 'nontrivial_interacting_continuum_mass_gap_proved':False,
}
path=root/'PF_I14_PUBLIC_SOURCE_COVARIANCE_RESULTS_2026_11_08.json'
path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('derived public evidence',path, path.stat().st_size)
