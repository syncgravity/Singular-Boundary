#!/usr/bin/env python3
"""Conditional finite SU2 link heat seam on genuine source rhombus pairs."""
import unittest
from pathlib import Path
from test_pf_i14_decorated_hull import toy_complex
from verify_pf_i14_gauge_projected_gluing import heat_gram,local_pair_link_model
from verify_pf_i12_two_sector_coupling import snapshot_complex
from verify_pf_i11_intrinsic_su2 import unit_quaternion
import numpy as np

SRC=Path(__file__).resolve().parent/'source/private_snapshots/PF_I11_original_source_7.npz'

class GaugeProjectedTests(unittest.TestCase):
    def test_positive_heat_gram_in_small_actual_link_set(self):
        q=unit_quaternion(np.random.default_rng(333),(9,3))
        for t in [.45,.85,1.5]:
            G=heat_gram(q,t)
            self.assertGreaterEqual(float(np.linalg.eigvalsh(G).min()),-1e-8)

    def test_toy_actual_link_gauge_projected_nonabelian(self):
        C,g=toy_complex()
        result=local_pair_link_model(C,seed=99,beta=.3,lam=.4,nconfigs=7,gauge_samples=7)
        self.assertEqual(result['actual_source_link_variables'],8)
        self.assertEqual(result['actual_source_vertices_in_local_patch'],7)
        self.assertGreater(result['two_sided_finite_gauge_averaged_heat_Gram_min_eigen'],-1e-7)
        self.assertGreater(result['difference_under_independent_half_gauge'],1e-4)
        self.assertFalse(result['global_original_source_OS_positive_proved'])

    @unittest.skipUnless(SRC.exists(),'original unpublished source link data unavailable')
    def test_original_source_actual_link_gluing(self):
        C=snapshot_complex(SRC)
        result=local_pair_link_model(C,seed=1415,beta=.3,lam=.4,nconfigs=10,gauge_samples=9)
        self.assertEqual(result['source_Ngrid'],7)
        self.assertEqual(result['local_pair_face_families'],[[0,1],[2,3]])
        self.assertGreater(result['two_sided_finite_gauge_averaged_heat_Gram_min_eigen'],-1e-7)
        self.assertFalse(result['source_physical_t_derived'])

if __name__=='__main__':unittest.main()
