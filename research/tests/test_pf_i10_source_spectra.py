#!/usr/bin/env python3
"""Regression tests for PF-I10; use PF_I10_PRIVATE_SOURCE for private author-script tests."""
import json, math, os, sys, unittest
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.linalg import eigvalsh
HERE=Path(__file__).resolve().parent
SCRIPT_DIR=HERE if (HERE/'verify_pf_i10_source_spectral.py').is_file() else HERE.parent/'scripts'
sys.path.insert(0,str(SCRIPT_DIR))
from verify_pf_i10_source_spectral import (source_import, periodic_sparse, build_sparse,
                                            SOURCE_SHA, TAVG, slq_one)
from verify_pf_i10_multimass import same_graph_uniform,slq_mass
from verify_pf_i10_tile_cutoff import source_tile_sparse,one_case

class PF_I10_ProofTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        summary_path=HERE/'PF_I10_EIGHT_SIZE_SPECTRAL_SUMMARY.json'
        if not summary_path.is_file():
            summary_path=HERE.parent/'evidence'/'PF_I10_EIGHT_SIZE_SPECTRAL_SUMMARY_2026_11_08.json'
        cls.summary=json.loads(summary_path.read_text())
        cls.srcpath=Path(os.environ['PF_I10_PRIVATE_SOURCE']) if 'PF_I10_PRIVATE_SOURCE' in os.environ else None
        cls.source=source_import(cls.srcpath) if cls.srcpath is not None else None

    def test_source_script_is_sha_pinned(self):
        self.assertEqual(SOURCE_SHA,'86ce0bf4e0688899a2f1c9dba980cb6d996c3fef59889807ee8376d6e62369da')

    def test_periodic_exact_source_edge_count(self):
        for q in [3,7,39]:
            L,m=periodic_sparse(q*q)
            self.assertEqual(m['edges'],(q-1)*(3*q-1))
            self.assertEqual(m['components'],1)
            self.assertAlmostEqual(float(L.diagonal().mean()),m['trace_over_n'],places=12)

    def test_periodic_coupling_not_unit(self):
        self.assertAlmostEqual(TAVG,(1+(2/(1+np.sqrt(5)))**2)/2,places=12)
        self.assertNotEqual(TAVG,1)

    def test_sparse_uniform_same_edge_support_and_zero_rows(self):
        A=sparse.csr_matrix([[1.4,-0.4,-1],[ -0.4,0.4,0],[-1,0,1.]])
        U=same_graph_uniform(A)
        self.assertTrue(np.allclose(U.sum(axis=1),0))
        self.assertEqual((U.nnz-A.nnz),0)
        self.assertAlmostEqual(float(U.diagonal().mean()),4*TAVG/3,places=12)

    def test_lanczos_quadrature_exact_for_two_point_matrix(self):
        L=sparse.csr_matrix([[1.,-1.],[-1.,1.]])
        val=slq_one(L,np.array([1.,-1.]),10,1e-4)
        self.assertAlmostEqual(val['sqrt'],math.sqrt(2.0001),places=10)
        self.assertAlmostEqual(val['log'],math.log(2.0001),places=10)
        self.assertAlmostEqual(val['first'],2.,places=10)

    def test_positive_modes_and_zero_mode_depend_on_components(self):
        L=sparse.block_diag((sparse.csr_matrix([[1.,-1.],[-1.,1.]]),sparse.csr_matrix([[1.,-1.],[-1.,1.]])))
        e=eigvalsh(L.toarray())
        self.assertEqual(sum(x<1e-10 for x in e),2)
        m2=1e-4
        full=np.sqrt(np.maximum(e,0)+m2).mean()
        positive=np.sqrt(e[e>1e-10]+m2).mean()
        recovered=(4*full-2*math.sqrt(m2))/(4-2)
        self.assertAlmostEqual(positive,recovered,places=12)

    def test_psd_added_edges_monotone_unfiltered_functionals(self):
        # Exactly the source Tile vs Coupled situation in a 3-vertex fragment.
        tile=np.zeros((3,3));coupled=np.array([[1.,-1.,0.],[-1.,2.,-1.],[0.,-1.,1.]])
        d=coupled-tile
        self.assertGreaterEqual(float(eigvalsh(d).min()),-1e-12)
        for f in [lambda a:np.sqrt(a+1e-4), lambda a:np.log(a+1e-4)]:
            self.assertGreater(np.sum(f(np.maximum(eigvalsh(coupled),0))),np.sum(f(np.maximum(eigvalsh(tile),0))))

    def test_exact_three_sizes_match_graph_source_reference(self):
        expected={7:0.8338194850588261,10:0.8303487155220399,12:0.8354604886394673}
        rows=self.summary['rows']
        for r in rows[:3]:
            self.assertEqual(r['spectral_method'],'exact_dense_eigvalsh')
            self.assertAlmostEqual(r['source_weighted_spectra']['0.0001']['sqrt']['ratio_positive_modes'],expected[r['Ngrid']],places=12)

    def test_all_eight_sizes_and_gates_unchanged(self):
        self.assertEqual([r['Ngrid'] for r in self.summary['rows']],[7,10,12,15,18,20,23,25])
        self.assertEqual(sum(x['spectral_method']=='exact_dense_eigvalsh' for x in self.summary['rows']),3)
        self.assertEqual(sum(x['spectral_method'].startswith('stochastic') for x in self.summary['rows']),5)
        self.assertFalse(self.summary['proof_gates']['interacting_4D_SU2_Yang_Mills_existence'])
        self.assertFalse(self.summary['proof_gates']['continuum_positive_mass_gap'])

    def test_eight_size_sqrt_and_log_means_reproduce_rounding(self):
        s=self.summary['eight_size_spectral_means']
        self.assertAlmostEqual(s['sqrt']['arithmetic_mean'],.8331846869573367,places=12)
        self.assertAlmostEqual(s['log']['arithmetic_mean'],.6463577401075136,places=12)
        self.assertAlmostEqual(s['relative_log']['arithmetic_mean'],.9587136627121045,places=12)

    def test_four_mass_flow(self):
        expected=[.959,.927,.816,.739]
        vals=[self.summary['eight_size_relative_logdet_mass_flow'][m]['arithmetic_mean'] for m in ['0.0001','0.01','1.0','100.0']]
        self.assertTrue(all(abs(a-b)<.001 for a,b in zip(vals,expected)))

    def test_same_graph_factorization_not_interaction(self):
        for r in self.summary['rows']:
            factor=r['uniform_same_graph_ratio']['sqrt']*r['uniform_to_periodic_ratio']['sqrt']
            self.assertAlmostEqual(factor,r['source_weighted_spectra']['0.0001']['sqrt']['ratio_positive_modes'],places=12)
        self.assertGreater(self.summary['eight_size_same_graph_fibonacci_uniform_mean']['sqrt'],1)
        self.assertLess(self.summary['eight_size_uniform_topology_vs_periodic_mean']['sqrt'],1)

    def test_fixed_probe_lanczos_convergence(self):
        step=self.summary['N25_160_to_240_step_fixed_probe_convergence']['0.0001']
        self.assertLess(step['sqrt']['absolute_difference'],1e-6)
        self.assertLess(step['log']['absolute_difference'],4e-5)
        self.assertLess(step['relative_log']['absolute_difference'],1e-5)

    def test_tile_coupled_psd_addition_exact_source_metadata(self):
        data=self.summary['original_tile_cutoff_components_from_exact_source']
        self.assertEqual(data['25']['components_tile'],111)
        self.assertEqual(data['25']['components_coupled'],5)
        self.assertEqual(data['25']['source_coupled_minus_tile_edges'],1066)
        self.assertEqual(data['10']['components_tile'],51)
        self.assertEqual(data['10']['components_coupled'],1)
        self.assertAlmostEqual(data['7']['trace_Delta_L_over_N'],0,places=12)
        self.assertGreater(data['25']['trace_Delta_L_over_N'],0)

    def test_slq_probes_are_conditional_not_rigorous(self):
        self.assertTrue(any('Stochastic trace samples' in q for q in self.summary['limitations']))

    @unittest.skipUnless(os.environ.get('PF_I10_PRIVATE_SOURCE'),'Requires unpublished source script')
    def test_private_source_matrix_one_to_one_at_n7(self):
        s=self.source
        til=s.build_penrose_tiling(7)
        iv=s.select_interior_vertices(til,.35)
        original,n,*_=s.build_coupled_z5_laplacian(til,iv)
        rebuilt,md,_=build_sparse(s,7)
        self.assertEqual(n,1550)
        self.assertTrue(np.allclose(original,rebuilt.toarray(),atol=1e-12))
        self.assertEqual(md['edges'],3017)

    @unittest.skipUnless(os.environ.get('PF_I10_PRIVATE_SOURCE'),'Requires unpublished source script')
    def test_private_tile_cutoff_source_distinct_at_n10(self):
        r=one_case(self.source,10)
        self.assertEqual((r['tile_edges'],r['coupled_edges']), (5865,5927))
        self.assertEqual(r['source_coupled_minus_tile_edges'],62)
        self.assertEqual((r['components_tile'],r['components_coupled']), (51,1))

    @unittest.skipUnless(os.environ.get('PF_I10_PRIVATE_SOURCE'),'Requires unpublished source script')
    def test_private_largest_source_matrix_components_and_edges(self):
        L,md,_=build_sparse(self.source,25)
        self.assertEqual((md['n'],md['edges'],md['components']), (19260,38139,5))
        self.assertTrue(np.allclose(L.sum(axis=1),0,atol=1e-10))

if __name__=='__main__':unittest.main(verbosity=2)
