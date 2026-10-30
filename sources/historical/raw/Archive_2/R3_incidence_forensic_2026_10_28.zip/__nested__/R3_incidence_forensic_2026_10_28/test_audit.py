import unittest
from audit import peel
class Tests(unittest.TestCase):
 def test_private_face(self):
  self.assertTrue(peel({'f':['a','b'],'g':['b','c']},['f'])['full_certificate'])
 def test_exterior_blocks(self):
  self.assertFalse(peel({'f':['a','b'],'g':['a','b']},['f'])['full_certificate'])
 def test_full_rank_not_sufficient(self):
  self.assertFalse(peel({'a':['x','y'],'b':['y','z'],'c':['x','z']},['a','b','c'])['full_certificate'])
 def test_partial(self):
  x=peel({'a':['x'],'b':['y','z'],'c':['y','z']},['a','b']);self.assertEqual(x['peeled_count'],1)
if __name__=='__main__':unittest.main()
