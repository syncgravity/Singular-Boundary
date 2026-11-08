"""PF-I9 checks: exact finite cut-and-project and source operator interface."""
from __future__ import annotations
import unittest
from pathlib import Path
import sys
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from verify_source_cut_project_bridge import (
    source_import,one_case,direct_membership,WINDOW_EQ,direct_face_membership,
    topological_moments,PAR,PERP)

SRC=Path(__file__).resolve().parents[1]/'paper6_extend_local.py'
if not SRC.exists():SRC=Path(__file__).resolve().parent/'paper6_extend_local.py'

class PF_I9_Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s=source_import(SRC)
        cls.cache={ng:one_case(cls.s,ng) for ng in [7,10,12]}
    def test_source_gamma_zero(self):
        self.assertAlmostEqual(float(self.s.GAMMA_GENERIC.sum()),0.,places=13)
    def test_projection_orthogonality(self):
        self.assertLess(float(np.abs(PAR.T@PERP).max()),1e-13)
    def test_4_hypersimplex_slices(self):
        self.assertEqual(set(WINDOW_EQ),{1,2,3,4})
    def test_direct_window_recovers_all_source_labels_small(self):
        self.assertEqual(self.cache[7]['source_retained_vertices'],1550)
        self.assertTrue(self.cache[7]['small_common_disk_accepted_vertex_sets_equal'])
    def test_exact_all_local_selected_faces_missing_only_due_line_range(self):
        for ng,ex in [(7,28),(10,210),(12,234)]:
            r=self.cache[ng]
            self.assertEqual(r['missing_source_tile_faces_in_selected_disk'],ex)
            self.assertEqual(r['missing_face_crossing_levels_outside_enumeration'],ex)
    def test_all_extra_basis_edges_are_completed_rhombus_edges(self):
        for ng,extra in [(7,0),(10,62),(12,85)]:
            r=self.cache[ng]
            self.assertEqual(r['source_coupled_extra_over_truncated_tiles'],extra)
            self.assertTrue(r['all_extra_basis_bonds_have_omitted_rhombus_witness'])
            self.assertEqual(r['source_coupled_edge_count'] if 'source_coupled_edge_count' in r else
               r['source_coupled_basis_edge_count'],r['completed_window_tile_edges_on_original_source_vertices'])
            self.assertEqual(r['direct_complete_tile_edge_SHA256_on_source_vertices'],r['source_original_coupled_edge_SHA256'])
    def test_true_onepass_finite_selection_differs(self):
        self.assertEqual(self.cache[7]['direct_35pct_full_star_interior_count'],1432)
        self.assertEqual(self.cache[10]['direct_35pct_full_star_interior_count'],3032)
        self.assertEqual(self.cache[12]['direct_35pct_full_star_interior_count'],4294)
    def test_weighted_laplacian_trace_formula(self):
        for r in self.cache.values():
            for name in ['source_tile_scalar_weighted_moments','source_coupled_scalar_weighted_moments']:
                q=r[name]
                self.assertAlmostEqual(q['traceL_div_N'],q['mean_weighted_strength'],places=10)
                self.assertGreater(q['traceL2_div_N'],q['traceL_div_N']**2)
    def test_full_source_vs_direct_collars_small(self):
        a=self.cache[7];b=one_case(self.s,7,collar=6)
        keys=['direct_35pct_full_star_interior_count','direct_window_selected_tile_faces',
              'source_original_vertex_SHA256','corrected_direct_vertex_SHA256',
              'corrected_direct_all_edges_SHA256','source_coupled_extra_over_truncated_tiles']
        for key in keys:self.assertEqual(a[key],b[key],key)
    def test_original_source_coupled_matrix_entries(self):
        # Actual dense source matrix at the smallest published grid; inspect
        # edge weights and diagonal independently of summary statistics.
        t=self.s.build_penrose_tiling(7)
        ids=self.s.select_interior_vertices(t,.35)
        L,n,e,na,nb=self.s.build_coupled_z5_laplacian(t,ids)
        r=self.cache[7]
        self.assertEqual((n,e),(1550,r['source_coupled_basis_edge_count']))
        self.assertLess(float(np.abs(L.sum(axis=1)).max()),1e-10)
        self.assertAlmostEqual(float(np.trace(L)/n),r['source_coupled_scalar_weighted_moments']['traceL_div_N'],places=11)
        self.assertEqual(int(np.count_nonzero(np.triu(L,k=1))),e)
    def test_all_eight_source_graphs_true_tile_completion(self):
        import json
        rows=json.loads((Path(__file__).resolve().parent/'PF_I9_COMPLETE_WINDOW_SOURCE_COMPARISON.json').read_text())['size_rows']
        self.assertEqual([r['source_retained_vertices'] for r in rows],
                         [1550,3042,4324,6980,9950,12207,16435,19260])
        self.assertEqual([r['source_coupled_extra_over_truncated_tiles'] for r in rows],
                         [0,62,85,290,444,593,889,1066])
        for r in rows:
            self.assertTrue(r['all_extra_basis_bonds_have_omitted_rhombus_witness'])
            self.assertTrue(r['completed_window_tile_equals_all_basis_on_original_source_vertices'])
            self.assertEqual(r['source_original_coupled_edge_SHA256'],
                             r['direct_complete_tile_edge_SHA256_on_source_vertices'])
            self.assertEqual(r['missing_source_tile_faces_in_selected_disk'],
                             r['missing_face_crossing_levels_outside_enumeration'])

    def test_reported_higher_size_n_deltas_equal_source_component_nullity(self):
        import json
        rows=json.loads((Path(__file__).resolve().parent/'PF_I9_COMPLETE_WINDOW_SOURCE_COMPARISON.json').read_text())['size_rows']
        diffs=[0,0,0,1,3,1,1,5]
        nullity=[r['source_coupled_scalar_weighted_moments']['weighted_laplacian_nullity'] for r in rows]
        self.assertEqual(nullity,[1,1,1,1,3,1,1,5])
        self.assertEqual(nullity[3:],diffs[3:])
        self.assertNotEqual(nullity[:3],diffs[:3])

    def test_negative_one_source_trace_full_eight(self):
        from verify_pf_i9_negative_one_trace import compute
        import json
        s=json.loads((Path(__file__).resolve().parent/'PF_I9_COMPLETE_WINDOW_SOURCE_COMPARISON.json').read_text())
        a=compute(s,1e-4);b=compute(s,0.0)
        self.assertAlmostEqual(a['mean_R_minus_one_full_modes'],0.7370567093342758,places=12)
        self.assertAlmostEqual(b['mean_R_minus_one_full_modes'],0.7370502535994539,places=12)
        self.assertTrue(a['both_rounded_to_reported_4_decimals'])
        self.assertEqual(len(a['rows']),8)
        self.assertTrue(all(r['exact_decomposition_reconstructed'] for r in a['rows']))

    def test_source_periodic_dense_matrix_vs_analytic_trace(self):
        from verify_pf_i9_negative_one_trace import compute
        import json
        s=json.loads((Path(__file__).resolve().parent/'PF_I9_COMPLETE_WINDOW_SOURCE_COMPARISON.json').read_text())
        r=compute(s,1e-4)['rows'][0]
        L,n=self.s.build_periodic_laplacian(r['N_QC'],r['periodic_bond_weight_tavg'])
        self.assertEqual(n,r['N_periodic'])
        self.assertAlmostEqual(float(np.trace(L)/n),r['periodic_traceL_over_N'],places=12)
        self.assertEqual(int(np.count_nonzero(np.triu(L,1))),r['periodic_triangle_bond_count'])

    def test_selected_window_clearance(self):
        for r in self.cache.values():self.assertGreater(r['minimum_source_selected_vertex_window_clearance'],1e-6)

if __name__=='__main__':unittest.main(verbosity=2)
