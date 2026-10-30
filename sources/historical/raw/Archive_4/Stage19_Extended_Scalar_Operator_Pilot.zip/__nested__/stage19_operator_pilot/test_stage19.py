import unittest
import numpy as np
from stage19_pilot import boundary, catalogue, measurement

class TestStage19(unittest.TestCase):
 def test_boundary_single_face(self):
  sp={'face_idx':np.array([[0,1,2,3]]),'face_sign':np.ones((1,4),dtype=int),
      'edges':np.array([[0,1],[1,2],[2,3],[3,0]])}
  self.assertEqual(boundary(sp,[0]),[(0,1),(1,1),(2,1),(3,1)])
 def test_boundary_adjacent_faces(self):
  sp={'face_idx':np.array([[0,1,2,3],[4,5,6,1]]),'face_sign':np.array([[1,1,1,1],[-1,1,1,-1]]),
      'edges':np.array([[0,1],[1,2],[2,3],[3,0],[4,1],[4,5],[5,2]])}
  # Adjacent, coherently oriented faces yield a single six-edge boundary.
  self.assertEqual(len(boundary(sp,[0,1])),6)
 def test_empty_cycle_rejected(self):
  sp={'face_idx':np.array([[0,1,2,3],[0,1,2,3]]),'face_sign':np.array([[1,1,1,1],[-1,-1,-1,-1]]),
      'edges':np.array([[0,1],[1,2],[2,3],[3,0]])}
  self.assertIsNone(boundary(sp,[0,1]))
if __name__=='__main__':unittest.main()
