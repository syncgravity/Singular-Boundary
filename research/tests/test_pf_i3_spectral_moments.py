"""Independent regression checks for PF-I3 conditional spectral source interface.

Tests do NOT reproduce the unpublished numerical generator in Sharpe Paper 2.
"""
import math
import unittest
import sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
for loc in (HERE, HERE.parent/"scripts"):
    if (loc/"verify_pf_i3_spectral_moments.py").is_file():
        sys.path.insert(0,str(loc));break
else:
    raise RuntimeError("PF-I3 verifier must be available alongside or in research/scripts")
from verify_pf_i3_spectral_moments import (
    p3_matrices, control_patch, check_trace, spectral, exact_source_constraints,
    SOURCE_PAPER1_IR_M2 as M2)

class PFI3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p3=p3_matrices(6.5,11)
        cls.tri=control_patch(cls.p3['n'],'triangle')
        cls.sw=spectral(cls.p3['weighted_strength'],M2)
        cls.sc=spectral(cls.p3['count_minus_weight'],M2)
        cls.st=spectral(cls.tri['lap'],M2)

    def test_original_p3_counts(self):
        self.assertEqual((self.p3['n'],self.p3['e']), (186,345))

    def test_weighted_laplacian_annihilates_constant(self):
        self.assertLess(np.max(np.abs(self.p3['weighted_strength']@np.ones(self.p3['n']))),1e-10)

    def test_count_diag_not_same_kinetic_operator(self):
        self.assertGreater(self.sc['minimum_eigenvalue'],0.49)
        self.assertAlmostEqual(self.sw['minimum_eigenvalue'],0,places=8)

    def test_trace_identities_weighted_and_count(self):
        for name in ['weighted_strength','count_minus_weight','same_graph_uniform_mean_weight']:
            L=self.p3[name]
            mu1,mu2=check_trace(L,len(L),M2)
            s=spectral(L,M2)
            self.assertAlmostEqual(s['zeta']['-1'],mu1+M2,places=10)
            self.assertAlmostEqual(s['zeta']['-2'],mu2+2*M2*mu1+M2**2,places=9)

    def test_equal_n_periodic_control_conductance(self):
        self.assertEqual(self.tri['n'],self.p3['n'])
        self.assertEqual(self.tri['e'],507)

    def test_reported_source_ratio_is_conditional_mismatch(self):
        s=exact_source_constraints(M2)
        self.assertAlmostEqual(s['strict_count_degree_triangular_unit_edges_predicted_ratio_s_minus1'],.650005833236,places=10)
        self.assertGreater(s['source_report_minus_prediction'],.087)

    def test_reproduction_at_one_s_not_enough(self):
        half=self.sc['zeta']['-0.5']/self.st['zeta']['-0.5']
        one=self.sc['zeta']['-1']/self.st['zeta']['-1']
        self.assertLess(abs(half-.8332),.003)
        self.assertGreater(abs(one-.7371),.05)

    def test_identity_at_s_zero(self):
        self.assertEqual(self.sw['zeta']['0'],1)
        self.assertEqual(self.st['zeta']['0'],1)

    def test_normalization_makes_big_difference(self):
        a=self.sw['zeta']['-0.5']/self.st['zeta']['-0.5']
        b=self.sc['zeta']['-0.5']/self.st['zeta']['-0.5']
        self.assertGreater(b-a,.1)

    def test_trace_matching_changes_zeta_ratio(self):
        a=self.sw; tri=self.tri['lap']
        scale=a['mean_L']/self.st['mean_L']
        matched=spectral(scale*tri,M2)
        self.assertAlmostEqual(a['zeta']['-1']/matched['zeta']['-1'],1,places=10)
        self.assertGreater(a['zeta']['-0.5']/matched['zeta']['-0.5'],.97)

    def test_logdet_not_negative_half_zeta(self):
        a=np.array([1.,9.]);b=np.array([4.,4.])
        self.assertEqual(np.sqrt(a).mean(),np.sqrt(b).mean())
        self.assertGreater(abs(np.log(a).mean()-np.log(b).mean()),.28)

    def test_spectral_ratio_not_determinant_ratio(self):
        self.assertLess(self.sw['zeta']['-0.5']/self.st['zeta']['-0.5'],.71)
        self.assertLess(self.sw['mean_log_L_plus_m2']-self.st['mean_log_L_plus_m2'],-.7)

if __name__ == '__main__': unittest.main(verbosity=2)
