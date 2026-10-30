import unittest,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
sys.path.insert(0,str(HERE/'stage24_inner'/'deps_stage23'))
from stage22_shifted import shifted_pairs
from stage26_outer import config
class Tests(unittest.TestCase):
 def test_all_offsets_have_every_lag(self):
  for offset in range(5):
   pairs=shifted_pairs(20,[(offset+5*j)%20 for j in range(4)])
   self.assertEqual(set(pairs[:,0]),set(range(2,11)))
 def test_cross_slab_exclusion(self):
  for offset in range(5):
   bs={(offset+5*j)%20 for j in range(4)}
   for lag,t,s in shifted_pairs(20,sorted(bs)):
    self.assertNotIn(int(t),bs);self.assertNotIn(int(s),bs)
 def test_config_frozen(self):
  from argparse import Namespace
  a=Namespace(kind='square',seed=101,stride=20,burn=96,depth=32,thin=3,reps=2)
  self.assertEqual(config(a)['burn'],96)
if __name__=='__main__':unittest.main()
