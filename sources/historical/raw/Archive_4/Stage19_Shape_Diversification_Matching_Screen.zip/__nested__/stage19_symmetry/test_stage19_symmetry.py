import unittest
import numpy as np
from stage19_symmetry import setup_geometry,many_shapes,weights,strata
class Stage19SymmetryTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.a=many_shapes(setup_geometry('square',20,3.5)[0],variants=2)
  cls.b=many_shapes(setup_geometry('penrose',20,3.5)[0],variants=2)
 def test_every_anchor(self):
  for c in (self.a,self.b):
   for k in range(3):
    x=c['anchor'][c['family']==k]
    self.assertTrue(np.all(np.bincount(x,minlength=c['F'])>=1))
 def test_root_weights(self):
  for c in (self.a,self.b):
   w=weights(c)
   for k in range(3):
    ix=np.where(c['family']==k)[0]
    np.testing.assert_allclose(np.bincount(c['anchor'][ix],weights=w[ix],minlength=c['F']),1/c['F'],atol=1e-15)
 def test_geometry_descriptor(self):
  for c in (self.a,self.b):
   self.assertTrue(np.all(c['area']>0)); self.assertTrue(np.all(c['perimeter']>0))
   self.assertTrue(np.all((c['compactness']>0)&(c['compactness']<1.1)))
 def test_matching_no_false_full(self):
  r=strata(self.a,self.b)
  self.assertLess(r['penrose_covered_root_weight'],0.8)
  self.assertGreater(len(r['strata']),0)
if __name__=='__main__':unittest.main()
