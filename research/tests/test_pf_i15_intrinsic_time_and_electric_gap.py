#!/usr/bin/env python3
"""PF-I15 regression tests: theorem-level finite graph and illustrative source replay."""
import json
import math
import os
from pathlib import Path
import unittest
import numpy as np
from verify_pf_i15_intrinsic_time_and_electric_gap import (
    PHI,WEAK,NGRID,C5_orbit,clock_certificate,decorated_hull_measure_nonuniqueness,spin_electric_gap,
    weighted_gap_by_min_cycle_min_edge,jacobi,independent_Haar_quadrature,
    interacting_one_face,mass_scale_certificate,source_finite_replay)

class PF_I15_Test(unittest.TestCase):
    def test_C5_orbit_average_exact_zero_height(self):
        for a in [(1,-1,0,0,0),(2,0,-3,0,1),(1,2,3,4,-10)]:
            self.assertEqual(tuple(sum(row[j] for row in C5_orbit(a)) for j in range(5)),(0,)*5)

    def test_clock_constraints(self):
        a=clock_certificate()
        self.assertTrue(a['Lambda0_invariant_additive_real_clock_is_zero'])
        self.assertFalse(a['physical_time_from_geometry_proved'])

    def test_decorated_hull_invariant_probabilities_not_unique(self):
        p=decorated_hull_measure_nonuniqueness()
        self.assertTrue(p['two_symmetry_invariant_measures_distinct'])
        self.assertGreater(p['example_B_fourier_modulus'],.1)
        self.assertFalse(p['unique_physical_vacuum_selected'])

    def test_pure_electric_girth4_exact_gap(self):
        self.assertEqual(spin_electric_gap(4),3)
        self.assertEqual(spin_electric_gap(4,epsilon=2),6)
        self.assertEqual(spin_electric_gap(3),2.25)

    def test_fibonacci_weak_gap(self):
        a=weighted_gap_by_min_cycle_min_edge(1,1)
        self.assertAlmostEqual(a['electric_epsilon_equals_source_scalar_Fibonacci_weights_gap'],3*PHI**-2)
        self.assertEqual(a['electric_epsilon_equals_inverse_scalar_Fibonacci_weights_gap'],3)

    def test_one_rhombus_zero_potential_spectrum(self):
        e=np.linalg.eigvalsh(jacobi(8,0,1))
        self.assertTrue(np.array_equal(e[:5],np.array([0.,3.,8.,15.,24.])))

    def test_one_rhombus_character_fusion_tridiagonal(self):
        m=jacobi(7,kappa=.71)
        self.assertAlmostEqual(m[0,1],-.71/2)
        self.assertAlmostEqual(m[1,2],-.71/2)
        self.assertEqual(m[0,2],0)

    def test_independent_Haar_quadrature(self):
        r=independent_Haar_quadrature(6,.71,500)
        self.assertLess(r['Haar_orthogonality_max_error'],1e-12)
        self.assertLess(r['Wilson_potential_matrix_max_error'],1e-12)

    def test_finite_quantum_interaction_not_just_beta0(self):
        r=interacting_one_face(.71)
        self.assertGreater(r['stable_gap_at_kappa'],3)
        self.assertLess(r['stable_gap_at_kappa'],4)

    def test_uniform_step_vs_physical_scale(self):
        p=mass_scale_certificate(1550,1468)
        q=mass_scale_certificate(19260,18874)
        self.assertLess(q['pure_electric_per_step_transfer_gap_1_minus_lambda1'],p['pure_electric_per_step_transfer_gap_1_minus_lambda1'])
        self.assertEqual(p['pure_electric_energy_gap_dividing_by_assumed_step'],3)
        self.assertLess(q['finite_interacting_minmax_lower_bound_3_minus_kappa_F'],0)
        self.assertGreater(p['finite_interacting_minmax_lower_bound_3_minus_kappa_F'],0)

    def test_positive_kappa_finite_electric_matrix(self):
        e=np.linalg.eigvalsh(jacobi(14,.71))
        self.assertGreater(e[1]-e[0],0)
        self.assertGreater(e[0],0)

    def test_gap_scales_with_aux_electric_energy(self):
        for epsilon in (.01,.2,1.):
            self.assertAlmostEqual(spin_electric_gap(4,epsilon),3*epsilon)

    def test_fundamental_spin_network_support_needs_cycle(self):
        from itertools import combinations
        # A source rhombus plus a pendant tree edge; valence-one fundamental
        # spin cannot be gauge invariant. All nonempty Z2-closed supports
        # must contain the genuine four-edge plaquette.
        links=[(0,1),(1,2),(2,3),(3,0),(0,4)]
        valid=[]
        for mask in range(1,1<<len(links)):
            degrees={v:0 for e in links for v in e}
            for i,(u,v) in enumerate(links):
                if mask>>i&1:degrees[u]+=1;degrees[v]+=1
            if all(d%2==0 for d in degrees.values()):
                valid.append(mask)
        self.assertEqual(valid,[15])
        self.assertEqual(sum(bool(valid[0]>>i&1) for i in range(len(links))),4)


    @unittest.skipUnless(os.getenv('PFI15_PRIVATE_SOURCE') and os.getenv('PFI15_PFI11_REFERENCE'),'Original private source unavailable')
    def test_all_eight_original_source_cutproject_girth_and_weak_faces(self):
        r=source_finite_replay(os.environ['PFI15_PRIVATE_SOURCE'],os.environ['PFI15_PFI11_REFERENCE'])
        self.assertEqual([x['Ngrid'] for x in r['results']],NGRID)
        self.assertTrue(all(x['all_weak_four_edge_rhombi']>0 for x in r['results']))
        self.assertTrue(all(x['girth_exact']==4 for x in r['results']))
        self.assertTrue(all(x['electric_epsilon_equals_source_scalar_Fibonacci_weights_gap']==3*WEAK for x in r['results']))

if __name__=='__main__':unittest.main()
