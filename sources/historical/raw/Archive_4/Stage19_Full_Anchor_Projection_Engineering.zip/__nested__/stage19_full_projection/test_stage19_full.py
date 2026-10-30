import unittest
import numpy as np
from stage19_full import setup_geometry,full_catalogue, boundary
from area_orientation import groups
class FullProjectionTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.square,_=setup_geometry('square',20,3.5)
  cls.penrose,_=setup_geometry('penrose',20,3.5)
 def test_full_coverage(self):
  for g in (self.square,self.penrose):
   c=full_catalogue(g)
   for k in range(3):
    ix=np.flatnonzero(c['kind']==k)
    self.assertEqual(len(ix),int(g['F']))
    np.testing.assert_array_equal(c['anchor'][ix],np.arange(int(g['F'])))
 def test_deterministic(self):
  a=full_catalogue(self.square);b=full_catalogue(self.square)
  for k in ('idx','sign','length','area','orientation','anchor','kind'):
   np.testing.assert_array_equal(a[k],b[k])
 def test_strata_cover_every_root(self):
  for g in (self.square,self.penrose):
   c=full_catalogue(g);inv,keys,count=groups(c)
   self.assertEqual(int(count.sum()),3*int(g['F']))
   self.assertTrue(np.all(count>0))
   self.assertTrue(np.all(np.isfinite(c['area'])))
 def test_closed_paths(self):
  for g in (self.square,self.penrose):
   c=full_catalogue(g)
   for i in (0,1,10,100,len(c['length'])-1):
    edges=g['edges'];ids=c['idx'][i,:c['length'][i]];sign=c['sign'][i,:c['length'][i]]
    oriented=[tuple(map(int,edges[e])) if s==1 else tuple(map(int,edges[e][::-1])) for e,s in zip(ids,sign)]
    self.assertTrue(all(oriented[j][1]==oriented[(j+1)%len(oriented)][0] for j in range(len(oriented))))
if __name__=='__main__':unittest.main()
