import json,tempfile,unittest
from pathlib import Path
from stage8_admission import audit
class AdmissionTests(unittest.TestCase):
 def test_fail_closed_empty(self):
  with tempfile.TemporaryDirectory() as d:
   r=audit(d)
   self.assertEqual(r['n_chains_present'],0)
   self.assertIsNone(r['mass_estimate'])
   self.assertFalse(r['requirements']['four_independent_checkpoint_states_per_geometry'])
 def test_missing_checkpoint_never_admitted(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'square_nt20_seed101_progress.json'
   p.write_text(json.dumps({'settings':{'kind':'square','seed':101,'burn':1000,'thin':10},'completed_sweeps':10000}))
   r=audit(d)
   self.assertEqual(r['n_chains_present'],0)
   self.assertEqual(r['production_samples_total'],0)
 def test_physical_gate_has_no_synthetic_estimates(self):
  with tempfile.TemporaryDirectory() as d:
   r=audit(d)
   for k in ('mass_estimate','string_tension_estimate','mass_ratio','continuum_contrast'):
    self.assertIsNone(r[k])
if __name__=='__main__':unittest.main()
