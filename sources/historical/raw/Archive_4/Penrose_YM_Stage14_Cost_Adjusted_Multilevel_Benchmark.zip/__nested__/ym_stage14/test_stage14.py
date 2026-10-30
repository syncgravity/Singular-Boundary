import unittest,numpy as np
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'ym_stage13'))
from stage13_transport import *
class Stage14Tests(unittest.TestCase):
 def test_exact_reconstruction(self):
  sp,lat=small_square();rng=np.random.default_rng(42);q=rng.normal(size=(lat['L'],4));q/=np.linalg.norm(q,axis=1)[:,None]
  self.assertAlmostEqual(direct_rectangle(q,15,sp['E'],sp['V'],0,1,[0],[1],0,10),paired_rectangle(q,15,sp['E'],sp['V'],0,1,[0],[1],0,5),places=11)
 def test_saved_benchmark_scope(self):
  import json
  obj=json.loads((Path(__file__).parent/'BENCHMARK.json').read_text())
  self.assertEqual(len(obj['rows']),48)
  self.assertEqual({r['seed'] for r in obj['rows']},{101,211,307,419})
  self.assertFalse(obj['design']['physical_admission'])
  self.assertLess(obj['max_outer_cache_error'],1e-9)
 def test_no_fictitious_fit(self):
  import json
  obj=json.loads((Path(__file__).parent/'BENCHMARK.json').read_text())
  for d in ('8','32'):
   self.assertTrue(np.isfinite(obj['summary'][d]['conditional_mean']))
   self.assertGreater(obj['summary'][d]['mean_time_seconds'],0)
if __name__=='__main__':unittest.main()
