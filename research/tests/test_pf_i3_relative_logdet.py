"""Paper4 determinant-source regression tests (finite candidate, not original replication)."""
import math
import sys
import unittest
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
for p in (HERE,HERE.parent/'scripts'):
    if (p/'verify_pf_i3_relative_logdet.py').is_file():
        sys.path.insert(0,str(p));break
else:raise RuntimeError('PF-I3 relative logdet verifier missing')
from verify_pf_i3_relative_logdet import (
    SOURCE_PAPER2_NINT,SOURCE_PAPER4_ZPRIME_N,one_patch,
    gamma_relative,gamma_from_source_paper4_equation)

class TestPFI3Paper4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.small=one_patch(6.5,11)
        cls.big=one_patch(12,12)

    def test_source_table_mode_count_differences(self):
        self.assertEqual([a-b for a,b in zip(SOURCE_PAPER2_NINT,SOURCE_PAPER4_ZPRIME_N)],
                         [0,0,0,1,3,1,1,5])

    def test_exact_relative_determinant_identity(self):
        vals=np.array([0.2,1.3,4.5])
        for m2 in [.0001,.01,1,100]:
            self.assertAlmostEqual(gamma_relative(vals,m2),
                                   gamma_from_source_paper4_equation(vals,m2),places=12)

    def test_m2_small_limit_generic(self):
        a=np.array([1.,9.]);b=np.array([4.,4.]);m2=1e-50
        self.assertLess(abs(gamma_relative(a,m2)/gamma_relative(b,m2)-1),.02)

    def test_m2_large_limit_first_moment(self):
        a=np.array([1.,9.]);b=np.array([4.,4.]);m2=1e9
        self.assertAlmostEqual(gamma_relative(a,m2)/gamma_relative(b,m2),a.mean()/b.mean(),places=7)

    def test_one_scalar_calibration_not_four(self):
        for r in [self.small,self.big]:
            self.assertGreater(r['single_periodic_conductance_calibrated_at_Paper2_R_minus1'],0)
            self.assertLess(r['maximum_absolute_difference_vs_Paper4_table'],.004)
            self.assertTrue(r['original_Paper2_or_Paper4_generator_reproduced'] is False)

    def test_source_calculation_already_exists(self):
        self.assertEqual(self.small['paper4_reported_eight_size_mean_zeta_prime_ratio'],.646)
        self.assertAlmostEqual(self.big['zeta_prime_ratio_at_Paper1_m2'],.6540123010689,places=8)

    def test_mode_zero_removal(self):
        for r in [self.small,self.big]:
            self.assertEqual(r['p3_zero_modes_removed'],1)
            self.assertEqual(r['periodic_zero_modes_removed'],1)
            self.assertEqual(r['positive_eigenvalue_count_each'],r['n']-1)

if __name__=='__main__':unittest.main(verbosity=2)
