"""Geometry-only independent validation of the large matched Wilson path batch."""
import unittest,json,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from stage16_matched_paths import select_matched

class TestMatchedCatalog(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.result=json.loads((HERE/'MATCHED_PATH_SCREEN.json').read_text())
  cls.s=np.load(HERE/'square_candidate_paths.npz')
  cls.p=np.load(HERE/'penrose_candidate_paths.npz')
 def test_unique_pairs_and_physical_thresholds(self):
  x=self.result['pairs']
  self.assertGreaterEqual(len(x),100)
  self.assertEqual(len({z['square_path_index'] for z in x}),len(x))
  self.assertEqual(len({z['penrose_path_index'] for z in x}),len(x))
  for z in x:
   s=z['square_path_index'];p=z['penrose_path_index']
   a=self.s['dx'][s];b=self.p['dx'][p]
   d=abs(np.linalg.norm(a)-np.linalg.norm(b))/max(np.linalg.norm(a),np.linalg.norm(b))
   angle=np.rad2deg(np.arccos(np.clip(abs(np.dot(a,b))/(np.linalg.norm(a)*np.linalg.norm(b)),-1,1)))
   self.assertLessEqual(d,.05+1e-12)
   self.assertLessEqual(angle,25+1e-12)
 def test_catalog_physical_consistency(self):
  for z in (self.s,self.p):
   self.assertEqual(len(z['idx']),1000)
   self.assertTrue(np.all(z['length']>=1))
   self.assertTrue(np.all(z['length']<=10))
   self.assertTrue(np.allclose(np.linalg.norm(z['dx'],axis=1),z['r']))

if __name__=='__main__':unittest.main()
