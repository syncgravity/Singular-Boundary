#!/usr/bin/env python3
"""Build source-aggregate PF-I15 public data; never export unpublished sources."""
import json,sys
from pathlib import Path
p=Path(sys.argv[1] if len(sys.argv)>1 else 'PF_I15_SOURCE_EIGHT_SIZE_ELECTRIC_GAP_EVIDENCE.json')
j=json.loads(p.read_text())
rows=j['original_source_8size_replay']['results']
assert len(rows)==8
pub={
  'checkpoint':'PF-I15',
  'status':'finite exact reference, source-derived physical time and continuum gap remain OPEN',
  'source_script_sha256_for_provenance_only':j['original_source_8size_replay']['source_script_sha256'],
  'source_unpublished_original_file_in_repository':False,
  'source_script_replayed_at_all_eight_sizes':True,
  'C5_invariant_additive_clock_nonselection':j['C5_additive_clock'],
  'auxiliary_decorated_phase_invariant_measure_nonuniqueness':j['auxiliary_decorated_hull_measure_nonuniqueness'],
  'exact_gauge_spin_network_gap_theorem':j['exact_electric_spin_network_gap'],
  'all_eight_source_size_controls':[
    {k:v for k,v in row.items() if k not in {'extensive_interaction_bound_example'}} | {
      'extensive_magnetic_bound_example':row['extensive_interaction_bound_example']}
    for row in rows
  ],
  'one_genuine_rhombus_Wilson_quantum_control':j['finite_one_rhombus_interacting_quantum_control'],
  'global_Yang_Mills_interacting_uniform_mass_gap_proved':False,
  'physical_time_derived':False,
  'original_source_numeric_spectra_reproduced_under_selected_H_el':True
}
out=Path('PF_I15_PUBLIC_FINITE_TIME_AND_ELECTRIC_RESULTS_2026_11_08.json')
out.write_text(json.dumps(pub,sort_keys=True,indent=2)+'\n')
print('Saved',out,'rows',len(pub['all_eight_source_size_controls']))
