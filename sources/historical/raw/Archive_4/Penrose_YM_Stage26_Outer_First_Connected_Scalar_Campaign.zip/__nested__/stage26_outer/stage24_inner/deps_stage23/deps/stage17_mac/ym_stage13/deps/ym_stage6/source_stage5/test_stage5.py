import unittest, tempfile, numpy as np
from stage5_square_production import setup,block_indices,bootstrap_correlators,diagnostic_az
from stage4_smearing_flux import staple_structure,ape_spatial,oriented_windings,square_scalar_basis
from wilson_torus import face_trace_scalar

class Stage5Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.sp,cls.lat,cls.cal,cls.paths,cls.flux,cls.scalar,cls.staple=setup(20,3.5)
 def test_geometry(self):
  s=self.sp
  self.assertEqual((s['V'],s['E'],s['F']),(182,364,182))
  self.assertEqual(s['V']-s['E']+s['F'],0)
  self.assertEqual(self.lat['L'],20*(s['V']+s['E']))
 def test_weak_field(self):
  np.testing.assert_allclose(self.cal['eig'],[1,1],atol=1e-11)
 def test_spatial_holonomies(self):
  self.assertEqual(len(self.scalar['counts']),3)
  self.assertTrue(np.all(self.scalar['length']>=4))
 def test_winding_deck(self):
  d,res=oriented_windings(self.sp)
  self.assertLess(res,1e-10)
  self.assertEqual(len(self.flux['direction']),48)
 def test_ape_identity_connection(self):
  L=self.lat['L'];u=np.zeros((L,4));u[:,0]=1
  v=ape_spatial(u,20,self.sp['E'],*self.staple,.4,2)
  np.testing.assert_allclose(v,u,atol=2e-15)
 def test_bootstrap_chain_blocks(self):
  for i in block_indices(4,20,5,6):
   self.assertEqual(len(i),80)
   self.assertEqual(np.unique(i//20).size,4)
 def test_connected_constant(self):
  a=np.zeros((80,20,3))
  c,b=bootstrap_correlators(a,5,5)
  self.assertTrue(np.allclose(c,0))
  self.assertTrue(np.allclose(b,0))
 def test_bootstrap_equivalent_to_direct(self):
  from stage4_smearing_flux import connected_corr
  rng=np.random.default_rng(1414)
  x=rng.normal(size=(80,20,3))
  C,B=bootstrap_correlators(x,5,4)
  np.testing.assert_allclose(C,connected_corr(x),rtol=0,atol=2e-14)
 def test_time_slices(self):
  self.assertEqual(self.lat['fi'].shape[0],20*(self.sp['E']+self.sp['F']))
  self.assertEqual(self.paths['idx'].shape[0],len(self.paths['meta']))
 def test_winding_physical_period(self):
  for j in range(2):
   seq=[x for x in self.flux['meta'] if x['direction']==j]
   self.assertEqual(len(seq),24)
   self.assertAlmostEqual(seq[0]['length'],np.linalg.norm(self.sp['periods'][:,j]),places=10)
if __name__=='__main__':unittest.main()
