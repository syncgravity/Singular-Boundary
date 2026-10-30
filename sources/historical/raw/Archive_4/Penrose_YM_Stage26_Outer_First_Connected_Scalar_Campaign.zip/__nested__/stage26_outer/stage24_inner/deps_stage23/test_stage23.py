import unittest, numpy as np
from stage22_shifted import slab_masks,shifted_pairs
from stage23_outer_benchmark import products_by_lag
class Tests(unittest.TestCase):
 def test_offsets_are_true_different_slabs(self):
  nt=20
  for offset in range(5):
   b=[(offset+5*k)%nt for k in range(4)]
   ps=shifted_pairs(nt,b)
   for lag,t,s in ps:
    def prev(x):
     for d in range(20):
      if (x-d)%20 in b:return (x-d)%20
    self.assertNotEqual(prev(int(t)),prev(int(s)))
 def test_products_constant_field(self):
  direct=np.ones((20,4));means=np.ones((20,4))*2
  for offset in range(5):
   x,y,n=products_by_lag(direct,means,offset)
   np.testing.assert_allclose(x,4);np.testing.assert_allclose(y,1)
   self.assertTrue(np.all(n>0))
 def test_masks_partition(self):
  lat={'nt':20,'E':7,'V':9,'L':20*16}
  for off in range(5):
   b,m=slab_masks(lat,off)
   self.assertEqual(len(m),4)
   self.assertEqual(len(set(b)),4)
   self.assertEqual(int(sum(q.sum() for q in m)),lat['L']-4*lat['E'])
if __name__=='__main__':unittest.main()
