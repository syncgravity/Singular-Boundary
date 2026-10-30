import unittest
import numpy as np
from stage21_scalar_multilevel import boundary_mask,conditional_pair
class TestConditionalDesign(unittest.TestCase):
 def test_boundary_link_mask(self):
  d={'nt':20,'E':3,'V':5,'L':160}
  mask=boundary_mask(d)
  self.assertEqual(int((~mask).sum()),12)
  self.assertTrue(np.all(~mask[0:3]))
  self.assertTrue(np.all(~mask[15:18]))
  self.assertTrue(np.all(mask[60:]))
 def test_products_of_conditional_means(self):
  x=np.arange(4*20*4,dtype=float).reshape(4,20,4)
  r=conditional_pair(x,x)
  self.assertEqual(r.shape,(6,4,4))
  np.testing.assert_array_equal(r[0],np.outer(x[:,2].mean(axis=0),x[:,7].mean(axis=0)))
 def test_no_forbidden_same_slab_pair(self):
  self.assertEqual(len(conditional_pair(np.zeros((2,20,4)),np.zeros((2,20,4)))),6)
if __name__=='__main__':unittest.main()
