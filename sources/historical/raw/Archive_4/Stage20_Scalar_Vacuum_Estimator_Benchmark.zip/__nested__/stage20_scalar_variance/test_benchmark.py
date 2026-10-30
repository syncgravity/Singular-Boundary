import unittest
import numpy as np
from benchmark import estimators

class TestVacuumEstimator(unittest.TestCase):
 def test_equal_constant_signal(self):
  m=np.full((4,8,2),3.0)
  p=np.full((4,8,8,2),9.0)
  plug,cross,_=estimators(m,p)
  np.testing.assert_allclose(plug,0,atol=1e-14)
  np.testing.assert_allclose(cross,0,atol=1e-14)
 def test_between_chain_covariance_correction(self):
  rng=np.random.default_rng(17)
  m=rng.normal(1,0.4,(4,15,2)); p=rng.normal(1,0.1,(4,15,8,2))
  plugin,cross,mu=estimators(m,p)
  muall=mu.mean(0)
  np.testing.assert_allclose(cross-plugin, np.broadcast_to(muall**2-(np.sum(mu,axis=0)**2-np.sum(mu**2,axis=0))/12, cross.shape))
 def test_exact_independent_chain_expectation(self):
  # Deliberately perfectly autocorrelated within each chain.
  # Distinct chains are independent draws, so cross-chain vacuum term is unbiased.
  rng=np.random.default_rng(42); nrep=60000
  values=rng.normal(2,0.5,(nrep,4)); vac=np.mean((np.sum(values,axis=1)**2-np.sum(values**2,axis=1))/12)
  self.assertLess(abs(vac-4),0.012)
  plug=np.mean(values.mean(axis=1)**2)
  self.assertGreater(plug,4.04)
if __name__=='__main__':unittest.main()
