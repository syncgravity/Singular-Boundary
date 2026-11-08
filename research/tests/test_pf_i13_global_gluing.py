#!/usr/bin/env python3
"""PF-I13 regression tests: unconditional exact theorems and conditional source replay."""
import os,sys,unittest,math
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
SCRIPTS=HERE if (HERE/'verify_pf_i13_global_gluing.py').exists() else HERE.parent/'scripts'
sys.path.insert(0,str(SCRIPTS))
sys.path.insert(0,str(HERE/'source'))
from verify_pf_i13_global_gluing import (
    petersen_type_graph,face_pair_graph,verify_phason_height_inversion,
    conditional_seam_kernel,hopping_inversion_mismatch)
from verify_pf_i12_two_sector_coupling import snapshot_complex
from verify_pf_i9_source_cut_project_bridge import direct_membership
from verify_pf_i11_intrinsic_su2 import PAR,PERP

class TestPFI13(unittest.TestCase):
    def test_family_graph_10_types_15_edges(self):
        j=petersen_type_graph();self.assertEqual((len(j['types']),j['family_transverse_type_edges']),(10,15))
    def test_petersen_graph_degree(self):
        self.assertEqual(petersen_type_graph()['type_degrees'],[3]*10)
    def test_petersen_no_triangles(self):
        self.assertFalse(petersen_type_graph()['has_type_triangles'])
    def test_petersen_odd_cycle(self):
        self.assertEqual(len(petersen_type_graph()['exhibited_odd_family_cycle']),5)
    def test_chromatic_three_exact(self):
        j=petersen_type_graph();self.assertEqual(j['family_graph_chromatic_number_exactly'],3)
        self.assertEqual(len(set(j['explicit_three_coloring'].values())),3)
    def test_paired_height_and_phason_linear_identity(self):
        g=np.array([(j*math.sqrt(2)+j*j*math.sqrt(3))%1 for j in range(5)])
        g-=g.mean();g[4]=-sum(g[:4]);m=np.array([2,-3,2,1,0]);n=np.ones(5,dtype=int)-m
        self.assertEqual(sum(m)+sum(n),5)
        np.testing.assert_allclose((n-g)@PERP,-(m+g)@PERP,atol=1e-13)
        np.testing.assert_allclose(n@PAR,-m@PAR,atol=1e-13)
    def test_height_bounded_not_unbounded_time(self):
        self.assertTrue(all(h+5 not in {1,2,3,4} for h in (1,2,3,4)))
    def test_C5_no_commuting_single_axis_reflection(self):
        rot=lambda th:np.array([[math.cos(th),-math.sin(th)],[math.sin(th),math.cos(th)]])
        g=np.zeros((4,4));g[:2,:2]=rot(2*math.pi/5);g[2:,2:]=rot(4*math.pi/5)
        for a in [-1,1]:
            for b in [-1,1]:
                R=np.diag([a,a,b,b]);self.assertAlmostEqual(np.linalg.norm(R@g-g@R),0,places=13)
                self.assertIn(int(np.sum(np.diag(R)<0)),[0,2,4])
        hyperplane=np.diag([-1,1,1,1]);self.assertGreater(np.linalg.norm(hyperplane@g-g@hyperplane),0.1)
    def test_central_inversion_4d_orientation(self):
        self.assertEqual(round(np.linalg.det(-np.eye(4))),1)
    def test_auxiliary_matched_heat_positive(self):
        j=conditional_seam_kernel();self.assertGreater(j['two_face_matched_seam_kernel_min_eigenvalue'],0)
    def test_auxiliary_local_commutator_within_halves_positive(self):
        j=conditional_seam_kernel(lam=0.4);self.assertGreater(j['doubled_side_interacting_matched_seam_min_eigenvalue'],0)
    def test_heat_pair_swap_fails(self):
        j=conditional_seam_kernel();self.assertLess(j['cross_swapped_seam_kernel_min_eigenvalue'],-0.01)
    def test_exact_swap_quadratic_sign(self):
        j=conditional_seam_kernel(t=.85)
        self.assertAlmostEqual(j['exact_continuous_Haar_antisymmetric_character_Q_swap'],-2*math.exp(-.75*.85))
        self.assertAlmostEqual(j['exact_continuous_Haar_antisymmetric_character_Q_matched'],2*math.exp(-.75*.85))
    def test_sampled_antisymmetric_character_sign(self):
        j=conditional_seam_kernel();self.assertLess(j['antisymmetric_character_test_Q_cross_swap'],0)
        self.assertGreater(j['antisymmetric_character_test_Q_matched'],0)
    def test_original_source_snapshot_7_family_chromatic(self):
        p=HERE/'source/private_snapshots/PF_I11_original_source_7.npz'
        if not p.exists():self.skipTest('private original source snapshot not present')
        C=snapshot_complex(p);j=face_pair_graph(C)
        self.assertEqual((j['faces'],j['transverse_pair_edges']),(1468,3093))
        self.assertTrue(j['chromatic_number_exactly_three']);self.assertEqual(j['odd_cycle_length'],5)
    def test_original_source_snapshot_20_family_chromatic(self):
        p=HERE/'source/private_snapshots/PF_I11_original_source_20.npz'
        if not p.exists():self.skipTest('private original source snapshot not present')
        C=snapshot_complex(p);j=face_pair_graph(C)
        self.assertEqual((j['faces'],j['transverse_pair_edges']),(11879,25590));self.assertTrue(j['chromatic_number_exactly_three'])
    def test_original_source_snapshot_25_family_chromatic(self):
        p=HERE/'source/private_snapshots/PF_I11_original_source_25.npz'
        if not p.exists():self.skipTest('private original source snapshot not present')
        C=snapshot_complex(p);j=face_pair_graph(C)
        self.assertEqual((j['faces'],j['transverse_pair_edges']),(18874,40853));self.assertTrue(j['chromatic_number_exactly_three'])
    def test_private_phase_flip_acceptance_and_face_map(self):
        p=HERE/'source/private_snapshots/PF_I11_original_source_7.npz'
        src=HERE/'source/paper6_extend_local.py'
        if not (p.exists() and src.exists()):self.skipTest('private original source not present')
        from verify_pf_i11_intrinsic_su2 import validate_source
        C=snapshot_complex(p);gamma=validate_source(src).GAMMA_GENERIC
        j=verify_phason_height_inversion(C,gamma)
        self.assertEqual(j['reflected_vertices_accepted_under_minus_gamma'],1550)
        self.assertEqual(j['all_reflected_faces_accepted_under_minus_gamma'],1468)
        self.assertLess(j['reflected_vertices_accepted_under_same_gamma'],1550)
    def test_private_hopping_word_not_reflection_invariant(self):
        p=HERE/'source/private_snapshots/PF_I11_original_source_7.npz'
        if not p.exists():self.skipTest('private original source not present')
        j=hopping_inversion_mismatch(snapshot_complex(p))
        self.assertEqual(j['source_hopping_types_changed_after_geometric_inversion'],1864)
    def test_private_20_hopping_word_not_reflection_invariant(self):
        p=HERE/'source/private_snapshots/PF_I11_original_source_20.npz'
        if not p.exists():self.skipTest('private source not present')
        j=hopping_inversion_mismatch(snapshot_complex(p))
        self.assertEqual(j['source_hopping_types_changed_after_geometric_inversion'],17194)

if __name__=='__main__':unittest.main(verbosity=2)
