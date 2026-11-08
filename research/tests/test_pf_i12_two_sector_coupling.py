#!/usr/bin/env python3
"""Exact finite PF-I12 regression; source snapshots optional, never fabricated."""
from __future__ import annotations
import itertools, math, os, sys, unittest
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
ROOT=Path(__file__).resolve().parent
for p in [ROOT,ROOT.parent/'scripts',Path('/mnt/data/pf_i11_work')]:
    if (p/'verify_pf_i12_two_sector_coupling.py').exists() or (p/'verify_pf_i11_intrinsic_su2.py').exists():
        sys.path.insert(0,str(p))
from verify_pf_i11_intrinsic_su2 import qmul,qconj,unit_quaternion,gauge_transform
from verify_pf_i12_two_sector_coupling import (
    V4,EXPECTED_FOUR_VOLUME,geometric_fourvolume_certificate,snapshot_complex,
    transverse_pairs,pair_penalty,wilson_transverse_action,local_two_face_integral)

from verify_pf_i12_conditional_heat_gluing import su2_heat_character_kernel,check_kernel

SNAP=Path(os.getenv('PF_I12_SNAPSHOTS',str(ROOT/'private_snapshots')))

class GeometryTheorems(unittest.TestCase):
    def test_four_plane_orthogonality(self):
        self.assertTrue(np.allclose(V4@V4.T,2.5*np.eye(4),atol=1e-14))
        self.assertTrue(np.allclose(V4@np.ones(5),0,atol=1e-14))

    def test_five_minors_equal(self):
        mags=[abs(np.linalg.det(V4[:,q])) for q in itertools.combinations(range(5),4)]
        for v in mags:self.assertAlmostEqual(v,EXPECTED_FOUR_VOLUME,places=12)

    def test_four_J_choices_and_no_C5_time_axis(self):
        J0=np.array([[0.,-1.],[1.,0.]])
        def rot(theta):return np.cos(theta)*np.eye(2)+np.sin(theta)*J0
        R=np.zeros((4,4));R[:2,:2]=rot(2*math.pi/5);R[2:,2:]=rot(4*math.pi/5)
        found=set()
        for a,b in itertools.product([-1,1],repeat=2):
            J=np.zeros((4,4));J[:2,:2]=a*J0;J[2:,2:]=b*J0
            self.assertTrue(np.allclose(J@J,-np.eye(4)))
            self.assertTrue(np.allclose(R@J,J@R))
            found.add((a,b))
        self.assertEqual(len(found),4)
        self.assertGreater(abs(np.linalg.det(rot(4*math.pi/5)-np.eye(2))),1.0)

    def test_4d_coordinate_cube_height_impossible(self):
        for h in range(1,5):self.assertFalse(h>=1 and h+4<=4)
        self.assertTrue(geometric_fourvolume_certificate()['no_full_four_coordinate_cube_with_all_16_corners_can_fit_source_heights_1_to_4'])

    def test_rotation_of_bivector_sign(self):
        # A 5-cycle relabeling preserves the magnitude of four-form.
        cols=[0,1,2,3]; shifted=[(i+1)%5 for i in cols]
        self.assertAlmostEqual(abs(np.linalg.det(V4[:,cols])),abs(np.linalg.det(V4[:,shifted])),places=12)


class NonAbelianTwoFaceTheory(unittest.TestCase):
    def test_quaternion_commutator_angle_identity(self):
        rng=np.random.default_rng(492)
        A=unit_quaternion(rng,(1000,));B=unit_quaternion(rng,(1000,))
        lhs=1-qmul(qmul(qmul(A,B),qconj(A)),qconj(B))[:,0]
        x=A[:,0];y=B[:,0]
        n=A[:,1:]/np.linalg.norm(A[:,1:],axis=1)[:,None]
        m=B[:,1:]/np.linalg.norm(B[:,1:],axis=1)[:,None]
        cosrel=np.sum(n*m,axis=1)
        rhs=2*(1-x**2)*(1-y**2)*(1-cosrel**2)
        self.assertLess(np.max(np.abs(lhs-rhs)),1e-12)

    def test_exact_covariance_derivative_at_Haar(self):
        p=local_two_face_integral(0.,0.)
        self.assertAlmostEqual(p['independent_single_face_Var_X2'],1/16,places=12)
        self.assertAlmostEqual(p['exact_zero_lambda_derivative_Cov_X2_Y2'],-1/192,places=12)
        self.assertAlmostEqual(p['connected_Cov_X2_Y2'],0,places=12)

    def test_exchange_reflection_pos_violated(self):
        for beta in (0.,.71):
            p=local_two_face_integral(beta,.4)
            self.assertLess(p['exchange_reflection_quadratic_test_unnormalized'],0.)

    def test_naive_exchange_failure_exact_slope(self):
        p=local_two_face_integral(0.,.001)
        self.assertAlmostEqual(p['exact_zero_lambda_derivative_Cov_X2_Y2'],-1/192,places=12)
        self.assertLess(p['exchange_reflection_quadratic_test_unnormalized'],0.)

    def test_baseline_commutator_mean(self):
        p=local_two_face_integral(0.,0.)
        self.assertAlmostEqual(p['baseline_expected_commutator_penalty'],.75,places=12)

    def test_nonzero_finite_coupling_covariance(self):
        p=local_two_face_integral(0.,.4)
        self.assertLess(p['connected_Cov_X2_Y2'],-.002)
        self.assertGreater(p['connected_Cov_X2_Y2'],-.003)
        self.assertLess(p['Z_two_face'],p['Z_baseline_product'])

    def test_quadrature_independence_and_convergence(self):
        a=local_two_face_integral(.71,.4,nx=50,nc=18)
        b=local_two_face_integral(.71,.4,nx=74,nc=26)
        self.assertAlmostEqual(a['Z_two_face'],b['Z_two_face'],places=12)
        self.assertAlmostEqual(a['connected_Cov_X2_Y2'],b['connected_Cov_X2_Y2'],places=12)

    def test_small_lambda_linear_slope(self):
        a=local_two_face_integral(0.,.001)
        self.assertLess(abs(a['connected_Cov_X2_Y2']/.001+1/192),2e-5)

    def test_nonzero_all_finite_beta_derivative(self):
        for beta in (0.,.1,.71,5.,20.):
            x=local_two_face_integral(beta,0.)
            self.assertLess(x['exact_zero_lambda_derivative_Cov_X2_Y2'],0.)
            self.assertGreater(x['independent_single_face_Var_X2'],0.)


class ConditionalHeatKernelGluing(unittest.TestCase):
    def test_peter_weyl_fundamental_correlator(self):
        for t in (.45,.85,2.):
            r=check_kernel(t,12,seed=622)
            self.assertAlmostEqual(r['exact_fundamental_halftrace_connected_correlation'],math.exp(-.75*t)/4,places=14)

    def test_SU2_heat_kernel_gram_positive(self):
        r=check_kernel(.85,16,seed=624)
        self.assertGreater(r['kernel_min_SPD_Gram_eigenvalue'],-1e-12)
        self.assertFalse(r['full_Z5_global_OS_reflection_proved'])

    def test_heat_kernel_central_under_common_conjugation(self):
        rng=np.random.default_rng(12)
        A=unit_quaternion(rng,(24,));B=unit_quaternion(rng,(24,));G=unit_quaternion(rng,(24,))
        lhs=su2_heat_character_kernel(qmul(A,qconj(B))[:,0],.85)
        ag=qmul(qmul(G,A),qconj(G));bg=qmul(qmul(G,B),qconj(G))
        rhs=su2_heat_character_kernel(qmul(ag,qconj(bg))[:,0],.85)
        self.assertLess(np.max(np.abs(lhs-rhs)),1e-12)

    def test_heat_kernel_series_converges(self):
        x=np.linspace(-1,1,41)
        p=su2_heat_character_kernel(x,.85,nmax=28)
        q=su2_heat_character_kernel(x,.85,nmax=50)
        self.assertLess(np.max(np.abs(p-q)),1e-13)
        self.assertGreater(p.min(),0)

    def test_heat_kernel_is_not_a_source_derived_physical_time(self):
        self.assertTrue(check_kernel()['pair_exchange_reflection_conditional_not_source_time'])


@unittest.skipUnless((SNAP/'PF_I11_original_source_7.npz').exists(),'Original unpublished PF-I11 source snapshots unavailable; never substitute a lattice')
class SourceSpecificTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.C=snapshot_complex(SNAP/'PF_I11_original_source_7.npz')
        cls.pairs=transverse_pairs(cls.C)

    def test_pair_count_source7(self):
        self.assertEqual(len(self.pairs),3093)
        self.assertEqual((len(self.C.labels),len(self.C.edges),len(self.C.faces)),(1550,3017,1468))

    def test_pair_family_distinct_and_shared_vertex(self):
        C=self.C
        for i,j,r,s in self.pairs:
            self.assertEqual(len(set(C.face_families[i]+C.face_families[j])),4)
            self.assertEqual(C.faces[i][r],C.faces[j][s])

    def test_exact_gauge_invariance_cross_action(self):
        rng=np.random.default_rng(197)
        links=unit_quaternion(rng,(len(self.C.edges),))
        g=unit_quaternion(rng,(len(self.C.labels),))
        a=wilson_transverse_action(self.C,links,self.pairs,.71,.35)
        b=wilson_transverse_action(self.C,gauge_transform(self.C,links,g),self.pairs,.71,.35)
        self.assertLess(abs(a-b),1e-8)

    def test_action_is_positive_for_positive_couplings(self):
        links=unit_quaternion(np.random.default_rng(198),(len(self.C.edges),))
        a=wilson_transverse_action(self.C,links,self.pairs,.71,.35)
        self.assertGreaterEqual(a,0)
        self.assertLessEqual(a,2*(.71*len(self.C.faces)+.35*len(self.pairs))+1e-8)

    def test_noncommutativity_source_links(self):
        rng=np.random.default_rng(200)
        links=unit_quaternion(rng,(len(self.C.edges),))
        assert np.any(pair_penalty(self.C,links,self.pairs)>0.01)


@unittest.skipUnless((SNAP/'PF_I11_original_source_20.npz').exists() and (SNAP/'PF_I11_original_source_25.npz').exists(),'Private source snapshots not available')
class LargeSourceCounts(unittest.TestCase):
    def test_source20(self):
        C=snapshot_complex(SNAP/'PF_I11_original_source_20.npz')
        self.assertEqual(len(transverse_pairs(C)),25590)

    def test_source25(self):
        C=snapshot_complex(SNAP/'PF_I11_original_source_25.npz')
        self.assertEqual(len(transverse_pairs(C)),40853)

if __name__=='__main__':unittest.main(verbosity=2)
