import unittest,tempfile
from pathlib import Path
import numpy as np
from stage19_mc import pack,save,sha
class TestStage19Pilot(unittest.TestCase):
 def test_pack(self):
  i,s,n=pack([[(2,1),(4,-1)],[(1,1)]])
  self.assertEqual(n.tolist(),[2,1]);self.assertEqual(i.tolist(),[[2,4],[1,-1]])
  self.assertEqual(s.tolist(),[[1,-1],[1,0]])
 def test_atomic_round_trip(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'x.npz';save(p,scalar=np.ones((2,20,4)))
   with np.load(p,allow_pickle=False) as z:self.assertEqual(z['scalar'].shape,(2,20,4))
   self.assertEqual(len(sha(p)),64)
if __name__=='__main__':unittest.main()
