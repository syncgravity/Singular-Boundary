#!/usr/bin/env python3
"""PF-I14 exact Sturmian/translation/reflection and finite source gauge checks."""
from __future__ import annotations
import os
from pathlib import Path
from fractions import Fraction
import unittest
import numpy as np
from verify_pf_i14_decorated_hull import (
    QuadraticPhase,FibonacciDecoration,mechanical,floor_quadratic,
    ceil_quadratic,exact_word_involution_certificate,exact_semidirect_certificate,
    theta_complex,finite_covariance,finite_translation_covariance,
    translated_label,theta_label)
from verify_pf_i11_intrinsic_su2 import assemble_complex,validate_source
from verify_pf_i9_source_cut_project_bridge import direct_membership,PAR

ROOT=Path(__file__).resolve().parent
PRIVATE=ROOT/'source'
SNAPS=PRIVATE/'private_snapshots'
SOURCE=PRIVATE/'paper6_extend_local.py'


def toy_complex():
    # Direct hypersimplex WINDOW acceptance, not de Bruijn crossing code.
    g=np.array([(j*np.sqrt(2)+j*j*np.sqrt(3))%1 for j in range(5)])
    g-=g.mean();g[4]=-g[:4].sum()
    labels=[]
    from itertools import product
    for m in product(range(-2,3),repeat=5):
        if 1<=sum(m)<=4 and np.linalg.norm(np.array(m)@PAR)<3.4 and direct_membership(m,g)[0]:
            labels.append(m)
    C=assemble_complex(labels,g)
    assert len(C.faces)>0
    return C,g


class ExactWordTests(unittest.TestCase):
    def test_source_matches_original_floor_word_all_levels(self):
        from verify_pf_i9_source_cut_project_bridge import fib_type
        dec=FibonacciDecoration.source()
        for j in range(5):
            for k in range(-100,101):
                self.assertEqual(dec.type(j,k),1 if fib_type(j,k)=='A' else 0)

    def test_exact_integer_surd_floor_and_ceil(self):
        import decimal
        ctx=decimal.getcontext();ctx.prec=65
        sq5=decimal.Decimal(5).sqrt();alph=(sq5-1)/2
        for p in [Fraction(0),Fraction(1,7),Fraction(-11,13),Fraction(2,3)]:
            for b in range(-70,71):
                d=QuadraticPhase(p,b);v=decimal.Decimal(p.numerator)/decimal.Decimal(p.denominator)+b*alph
                flo=int(v.to_integral_value(rounding=decimal.ROUND_FLOOR))
                cei=int(v.to_integral_value(rounding=decimal.ROUND_CEILING))
                self.assertEqual(floor_quadratic(d),flo)
                self.assertEqual(ceil_quadratic(d),cei)

    def test_word_involution_with_singular_boundary(self):
        a=exact_word_involution_certificate(1000)
        self.assertEqual(a['singular_reflected_lower_word_mismatch_levels_source_index'],[-1,0])
        self.assertEqual(a['validated_integer_source_cases'],20010)

    def test_upper_lower_swapped_exact(self):
        for p in [QuadraticPhase(),QuadraticPhase(Fraction(1,7),-3),QuadraticPhase(Fraction(-1,5),4)]:
            for upper in [False,True]:
                for k in range(-400,401):
                    self.assertEqual(mechanical(k,p,upper),mechanical(-k,p.reflect(),not upper))

    def test_decoration_reflection_squares_identity(self):
        d=FibonacciDecoration(tuple(QuadraticPhase(Fraction(j,7),j-2) for j in range(5)),(True,False,True,True,False))
        self.assertEqual(d.reflect().reflect(),d)

    def test_semidirect_relation(self):
        p=exact_semidirect_certificate()
        self.assertIn('R T_a R',p['exact_group_relation'])
        self.assertTrue(p['five_separate_word_phase_coordinates_necessary_for_full_Lambda0_covariance'])

    def test_zero_sum_reindexing_restricts_height(self):
        d=FibonacciDecoration.source()
        with self.assertRaises(ValueError):d.translate((1,0,0,0,0))
        with self.assertRaises(ValueError):d.translate((0,0,0,0,0,0))

class FiniteCovarianceTests(unittest.TestCase):
    def test_toy_window_reflection(self):
        C,g=toy_complex();row=finite_covariance(C,g,seed=30)
        self.assertEqual(row['edge_hopping_type_mismatches_under_decorated_theta'],0)
        self.assertLess(row['Wilson_face_action_absolute_difference'],1e-10)
        self.assertTrue(row['nonabelian_two_face_action']['pair_penalty_max_absolute_discrepancy']<1e-10)

    def test_toy_window_height_preserving_translation(self):
        C,g=toy_complex();r=finite_translation_covariance(C,g,seed=77)
        self.assertEqual(r['translated_Wilson_action_absolute_difference'],0)

    def test_toy_theta_twice_vertex_face_maps(self):
        C,g=toy_complex();C2,e1,f1=theta_complex(C,g);C3,e2,f2=theta_complex(C2,-g)
        self.assertEqual(C.labels,C3.labels)
        self.assertEqual(C.edges,C3.edges)
        self.assertEqual(C.faces,C3.faces)
        self.assertTrue(np.array_equal(np.arange(len(C.edges)),e2[e1]))
        self.assertTrue(np.array_equal(np.arange(len(C.faces)),f2[f1]))

    @unittest.skipUnless(SOURCE.exists() and (SNAPS/'PF_I11_original_source_7.npz').exists(),
                         'original unpublished source not available; public derived test')
    def test_source_snapshot_7_reflection(self):
        from verify_pf_i12_two_sector_coupling import snapshot_complex
        g=validate_source(SOURCE).GAMMA_GENERIC
        C=snapshot_complex(SNAPS/'PF_I11_original_source_7.npz')
        r=finite_covariance(C,g,seed=1461)
        self.assertEqual((r['V'],r['E'],r['F']),(1550,3017,1468))
        self.assertEqual(r['singular_lower_lower_mismatch_edges'],488)
        self.assertEqual(r['same_fixed_hopping_word_mismatch_count'],1864)

    @unittest.skipUnless(SOURCE.exists() and (SNAPS/'PF_I11_original_source_25.npz').exists(),
                         'original unpublished source not available; public derived test')
    def test_source_snapshot_25_reflection(self):
        from verify_pf_i12_two_sector_coupling import snapshot_complex
        g=validate_source(SOURCE).GAMMA_GENERIC
        C=snapshot_complex(SNAPS/'PF_I11_original_source_25.npz')
        r=finite_covariance(C,g,seed=1461)
        self.assertEqual((r['V'],r['E'],r['F']),(19260,38139,18874))
        self.assertEqual(r['singular_lower_lower_mismatch_edges'],1714)
        self.assertEqual(r['same_fixed_hopping_word_mismatch_count'],27350)

    @unittest.skipUnless(SOURCE.exists() and (SNAPS/'PF_I11_original_source_25.npz').exists(),
                         'original unpublished source not available; public derived test')
    def test_source_snapshot_translation(self):
        from verify_pf_i12_two_sector_coupling import snapshot_complex
        g=validate_source(SOURCE).GAMMA_GENERIC
        C=snapshot_complex(SNAPS/'PF_I11_original_source_25.npz')
        r=finite_translation_covariance(C,g,seed=11)
        self.assertTrue(r['all_edge_and_face_Fibonacci_couplings_transport'])

if __name__=='__main__':unittest.main()
