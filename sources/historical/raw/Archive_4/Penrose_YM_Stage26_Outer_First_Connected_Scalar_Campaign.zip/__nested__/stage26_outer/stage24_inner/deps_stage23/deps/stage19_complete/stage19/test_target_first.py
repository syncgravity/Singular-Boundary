import unittest, numpy as np
from target_first import match,pack,features
class TargetTests(unittest.TestCase):
 def setUp(self):
  self.row=lambda root,n,area,per:(root,n,0,area,per,4*np.pi*area/per**2,0.,1.,[(0,1)]*n)
 def test_deterministic(self):
  a=[self.row(0,3,1.4,5.5),self.row(1,5,2.5,8)]
  b=[self.row(0,4,1.41,5.52),self.row(1,6,2.51,8.02)]
  x,_,_=match(a,b,3);y,_,_=match(a,b,3)
  self.assertEqual(x,y)
  self.assertTrue(any(a[i][1]!=b[j][1] for i,j,d in x))
 def test_packed(self):
  p=pack([self.row(0,3,1.4,5.5)],[0]);self.assertEqual(p['idx'].shape,(1,3))
  self.assertEqual(features([self.row(0,3,1.4,5.5)]).shape,(1,3))
if __name__=='__main__':unittest.main()
