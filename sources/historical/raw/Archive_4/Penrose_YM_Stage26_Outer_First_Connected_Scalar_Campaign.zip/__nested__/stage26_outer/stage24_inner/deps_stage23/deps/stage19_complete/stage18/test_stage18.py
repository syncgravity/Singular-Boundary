import tempfile,unittest
from pathlib import Path
import numpy as np
from stage18_scalar_run import atomic_npz,scalar_measure
class ScalarTests(unittest.TestCase):
 def test_atomic(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'a.npz';atomic_npz(p,x=np.arange(3));self.assertTrue(np.array_equal(np.load(p)['x'],[0,1,2]))
 def test_assembly(self):
  # Exact concatenation of three scalar channels for every smearing level.
  from unittest.mock import patch
  l=np.zeros((4,4));g={'E':2,'spatial_kind':'square_torus'};loops={'idx':0,'sign':0,'length':0,'kind':0}
  with patch('stage18_scalar_run.ape_spatial',side_effect=lambda *a: np.ones((4,4))*a[-1]),patch('stage18_scalar_run.measure_scalar_groups',side_effect=lambda a,*rest: np.ones((20,3))*a[0,0]):
   s=scalar_measure(l,g,[0,2,6,12],.4,loops,(1,2,3));self.assertEqual(s.shape,(20,12));self.assertTrue(np.array_equal(s[0],[0,0,0,2,2,2,6,6,6,12,12,12]))
if __name__=='__main__':unittest.main()
