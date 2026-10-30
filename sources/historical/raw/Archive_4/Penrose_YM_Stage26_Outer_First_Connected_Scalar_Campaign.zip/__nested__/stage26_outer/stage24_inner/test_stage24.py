import unittest
import numpy as np
from pathlib import Path
from stage24_inner_diagnostics import compute
from analyze_stage24 import independent_chain_connected
class TestStage24(unittest.TestCase):
    def test_reject_one_replica(self):
        with self.assertRaises(ValueError):compute('square',101,'unused','unused','unused',reps=1)
    def test_requires_independent_chains(self):
        self.assertEqual(independent_chain_connected([]),{})
    def test_pair_selector(self):
        from stage23_outer_benchmark import products_by_lag
        x=np.ones((20,4));p,d,c=products_by_lag(x,x,0)
        self.assertEqual(p.shape,(9,4,4));self.assertTrue(np.allclose(p,1));self.assertTrue(np.all(c>0))
if __name__=='__main__':unittest.main()
