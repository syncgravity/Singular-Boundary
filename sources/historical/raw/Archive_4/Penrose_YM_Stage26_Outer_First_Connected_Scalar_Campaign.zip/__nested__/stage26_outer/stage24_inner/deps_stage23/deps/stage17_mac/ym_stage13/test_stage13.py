import unittest,numpy as np
from stage13_transport import *
class TestTransport(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.sp,cls.lat=small_square();cls.nt=15;cls.E=cls.sp['E'];cls.V=cls.sp['V']
  cls.u=identity_field(cls.lat)
  rng=np.random.default_rng(1203);q=rng.normal(size=cls.u.shape);cls.random=q/np.linalg.norm(q,axis=1)[:,None]
 def test_flat(self):
  u=self.u
  self.assertAlmostEqual(direct_rectangle(u,15,self.E,self.V,0,1,[0],[1],0,10),1.,places=12)
  self.assertAlmostEqual(paired_rectangle(u,15,self.E,self.V,0,1,[0],[1],0,5),1.,places=12)
 def test_random_exact(self):
  for u in (self.random,self.u):
   d=direct_rectangle(u,15,self.E,self.V,0,1,[0],[1],0,10)
   p=paired_rectangle(u,15,self.E,self.V,0,1,[0],[1],0,5)
   self.assertAlmostEqual(d,p,places=11)
 def test_factorization(self):
  locked,allowed,group,bb=slab_partition(15,self.E,self.V,5)
  self.assertTrue(assert_slab_factorization(self.lat,group,locked,15,self.E,self.V,5))
 def test_conditional_identity(self):
  # No dynamics: conditional estimator must preserve normalization and boundaries.
  out=conditioned_rectangle(self.u,self.lat,self.sp,0,1,[0],[1],inner=3,warm=1,spacing=1)
  self.assertTrue(out['frozen_exact']);self.assertLess(out['cache_error'],1e-11)
  self.assertTrue(np.isfinite(out['conditional']))
if __name__=='__main__':unittest.main()

class TestModelSetTransport(unittest.TestCase):
 def test_m5_geometry_and_algebra(self):
  from stage2_rational_torus import build_torus
  from stage2_ym_calibration import assemble
  sp=build_torus(5)
  lat,_=assemble(sp,15,3.5,1.,1.)
  E,V=sp['E'],sp['V'];locked,allowed,group,bounds=slab_partition(15,E,V,5)
  self.assertTrue(assert_slab_factorization(lat,group,locked,15,E,V,5))
  rng=np.random.default_rng(450);q=rng.normal(size=(lat['L'],4));u=q/np.linalg.norm(q,axis=1)[:,None]
  a,b=map(int,sp['edges'][0]);s=1
  self.assertAlmostEqual(direct_rectangle(u,15,E,V,a,b,[0],[s],0,10),paired_rectangle(u,15,E,V,a,b,[0],[s],0,5),places=11)
