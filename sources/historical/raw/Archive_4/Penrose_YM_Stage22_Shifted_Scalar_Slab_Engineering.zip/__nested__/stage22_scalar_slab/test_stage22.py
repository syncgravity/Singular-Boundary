import unittest,numpy as np
from stage22_shifted import slab_masks,shifted_pairs
class TestMasks(unittest.TestCase):
 def test_disjoint_and_boundary(self):
  for o in range(5):
   lat={'nt':20,'E':7,'V':5,'L':240}
   b,m=slab_masks(lat,o)
   self.assertEqual(sum(x.sum() for x in m),212)
   self.assertTrue(all(np.sum([x[i] for x in m])==0 for t in b for i in range(t*7,(t+1)*7)))
 def test_all_offsets_time_pairs(self):
  lags=set()
  for o in range(5):
   b,_=slab_masks({'nt':20,'E':7,'V':5,'L':240},o)
   pairs=shifted_pairs(20,b)
   self.assertTrue(all(t not in b and s not in b for lag,t,s in pairs))
   lags.update(pairs[:,0].tolist())
  self.assertEqual(lags,set(range(2,11)))
if __name__=='__main__':unittest.main()
