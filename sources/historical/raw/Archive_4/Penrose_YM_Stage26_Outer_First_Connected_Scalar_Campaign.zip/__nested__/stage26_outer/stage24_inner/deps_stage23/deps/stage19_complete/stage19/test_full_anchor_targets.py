import unittest
import numpy as np
from full_anchor_targets import assign, orientations, TARGETS
class TestAnchor(unittest.TestCase):
 def test_no_silent_imputation(self):
  # one matching root, one intentionally empty; uncovered root must remain uncovered
  r=(0,5,0,1.9,6.5,4*np.pi*1.9/6.5**2,0.,0.,[(0,1)])
  s,d,t,c=assign([r],np.array([0,1]));self.assertEqual(c.tolist(),[1,0]);self.assertEqual(len(s),1)
 def test_all_roots_and_target_uniqueness(self):
  r=(0,5,0,1.9,6.5,4*np.pi*1.9/6.5**2,0.,0.,[(0,1)])
  s,d,t,c=assign([r,r],np.array([0]),kmax=2)
  self.assertLessEqual(c[0],2);self.assertEqual(len(set(t)),len(t))
 def test_target_distances(self):
  r=(0,5,0,1.9,6.5,4*np.pi*1.9/6.5**2,0.,0.,[(0,1)])
  s,d,t,c=assign([r],np.array([0]));self.assertEqual(d[0],0.0)
if __name__=='__main__':unittest.main()
