import unittest,numpy as np
from stage15_batch import small_square,paths_x,batched_measure
from stage13_transport import identity_field,direct_rectangle
class Tests(unittest.TestCase):
 def setUp(self):self.sp,self.lat=small_square();self.paths=paths_x(self.sp)
 def test_paths(self):
  self.assertEqual([p['physical_r'] for p in self.paths],[1.,2.,3.])
  for p in self.paths:self.assertEqual(len(p['path']),p['length'])
 def test_identity_batched(self):
  U=identity_field(self.lat)
  r=batched_measure(U,self.lat,self.sp,self.paths,(2,4),warm=2,spacing=1,seed=13)
  self.assertTrue(r['frozen']);self.assertLess(r['cache_error'],1e-9)
  self.assertTrue(np.all(np.isfinite(r['values'][4])))
 def test_direct_identity(self):
  U=identity_field(self.lat)
  for p in self.paths:
   self.assertAlmostEqual(direct_rectangle(U,self.lat['nt'],self.sp['E'],self.sp['V'],p['u'],p['v'],p['path'],p['sg'],0,10),1.)
if __name__=='__main__':unittest.main()

class Equivalence(unittest.TestCase):
 def test_single_path_matches_legacy_same_seed(self):
  from stage13_transport import conditioned_rectangle
  from corrected_2p1_pilot import run_chain
  sp,lat=small_square();paths=paths_x(sp)
  obs,_,_,_=run_chain(lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],lat['L'],1234,12,1,1,.95)
  p=paths[0];seed=41
  b=batched_measure(obs[0],lat,sp,[p],(4,),warm=4,spacing=2,seed=seed)
  original=conditioned_rectangle(obs[0],lat,sp,p['u'],p['v'],p['path'],p['sg'],slab=5,inner=4,warm=4,spacing=2,seed=seed)
  self.assertAlmostEqual(b['values'][4][0],original['conditional'],places=12)
