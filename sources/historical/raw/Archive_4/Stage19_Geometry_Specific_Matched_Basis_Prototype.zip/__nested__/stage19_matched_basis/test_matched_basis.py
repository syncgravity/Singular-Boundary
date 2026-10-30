import unittest
import numpy as np
from matched_basis import construct
class Tests(unittest.TestCase):
 def test_exact_bin_coupling_synthetic(self):
  def c(areas):
   n=len(areas)
   return dict(length=np.ones(n,dtype=np.int64),family=np.zeros(n,dtype=np.int64),anchor=np.arange(n),F=n,sizes=[3],area=np.array(areas,float),perimeter=np.ones(n)*5,compactness=np.ones(n)*.6,idx=np.zeros((n,1),np.int32))
  sp={'edge_vectors':np.array([[1.,0.]])}
  a,b=c([1.1,1.1,1.7]),c([1.1,1.7,1.7])
  wa,wb,r=construct(a,sp,b,sp)
  self.assertAlmostEqual(wa.sum(),1);self.assertAlmostEqual(wb.sum(),1)
  self.assertLess(r['max_joint_bin_probability_error'],1e-12)
  self.assertAlmostEqual(r['common_support_mass'],2/3)
 def test_reject_no_overlap(self):
  def c(area):
   return dict(length=np.ones(1,dtype=np.int64),family=np.zeros(1,dtype=np.int64),anchor=np.zeros(1,dtype=np.int64),F=1,sizes=[3],area=np.array([area]),perimeter=np.array([5.]),compactness=np.array([.6]),idx=np.zeros((1,1),np.int32))
  with self.assertRaises(ValueError):construct(c(1.1),{'edge_vectors':np.array([[1.,0.]])},c(3.0),{'edge_vectors':np.array([[1.,0.]])})
if __name__=='__main__':unittest.main()
