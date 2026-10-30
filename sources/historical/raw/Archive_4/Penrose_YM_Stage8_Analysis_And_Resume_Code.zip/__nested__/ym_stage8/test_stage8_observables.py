import unittest,numpy as np
from stage8_observable_gates import correlation_per_configuration,audit_chains
class TestObservables(unittest.TestCase):
 def test_constant_field_zero_after_global_centering(self):
  x=np.full((3,12,9),2.25)
  self.assertTrue(np.array_equal(correlation_per_configuration(x),np.zeros((3,7,9))))
 def test_lag0_variance_and_symmetry(self):
  rng=np.random.default_rng(1999)
  x=rng.normal(size=(6,20,3))
  C=correlation_per_configuration(x,tmax=10)
  self.assertTrue(np.all(C[:,0,:]>=0))
  self.assertTrue(np.allclose(C[:,0,:],np.mean((x-x.mean(axis=(0,1),keepdims=True))**2,axis=1)))
 def test_reject_empty(self):
  import tempfile
  with tempfile.TemporaryDirectory() as d:
   self.assertFalse(audit_chains(d,'square')['admitted'])
if __name__=='__main__': unittest.main()
