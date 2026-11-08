import math,unittest
from pathlib import Path
from verify_pf_i11_intrinsic_su2 import collapse_complex
from verify_pf_i11_plaquette_factorization import (
    finite_factorization_from_counts,direct_two_face_haar_montecarlo,summary)
from test_pf_i11_intrinsic_su2 import square_complex

class PlaquetteFactorizationTests(unittest.TestCase):
    def test_haar_factorization_base_case(self):
        C=square_complex();self.assertTrue(collapse_complex(C)['all_faces_collapse'])
        q=finite_factorization_from_counts(1,.71)
        self.assertAlmostEqual(math.exp(q['log_partition']),q['single_face_Z'],places=13)

    def test_exact_two_face_factor_and_trace_covariance(self):
        f=finite_factorization_from_counts(2,.71)
        self.assertAlmostEqual(math.exp(f['log_partition']),f['single_face_Z']**2,places=13)
        self.assertEqual(f['two_distinct_face_connected_trace_covariance_exact'],0)

    def test_independent_haar_two_plaquette_monte_carlo(self):
        q=direct_two_face_haar_montecarlo(samples=100000)
        self.assertLess(abs(q['standardized_Z_difference']),4.5)
        self.assertLess(abs(q['weighted_connected_plaquette_halftrace_covariance']),.02)

    def test_original_and_completed_all_eight_analytically_solvable(self):
        p=Path(__file__).resolve().parent
        a=p/'PF_I11_EIGHT_SIZE_SOURCE_GAUGE_COMPLEX.json';b=p/'PF_I11_COMPLETED_WINDOW_CORE_CONTROL.json'
        if not a.is_file() or not b.is_file():self.skipTest('Full source geometry evidence not present')
        q=summary(a,b)
        self.assertEqual(len(q['source_rows']),16)
        self.assertEqual(len({round(x['log_partition_per_face'],13) for x in q['source_rows']}),1)
        orig=[x for x in q['source_rows'] if x['selection']=='original_source']
        self.assertEqual([x['fundamental_group_free_rank'] for x in orig],[0,0,0,0,0,6,10,10])

if __name__=='__main__':unittest.main()
