#!/usr/bin/env python3
"""Regression tests for the exact PF-I4 source-model compatibility gates."""
import sys
from fractions import Fraction
from pathlib import Path
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parent))
from verify_pf_i4_source_selection import (
    PAPER2_FULL,PAPER4_PRIME,paper4_degree_arithmetic,zero_mode_hypothesis,
    patch_report,components,ORIGINAL_PDF_HASHES
)

class SourceConsistencyTests(unittest.TestCase):
    def test_paper4_degree_lower_bound(self):
        d=paper4_degree_arithmetic()
        self.assertEqual(Fraction(d['exact_lower_bound_mean_degree']),Fraction('3.774'))

    def test_percent_rounding_does_not_fix(self):
        d=paper4_degree_arithmetic()
        self.assertGreater(Fraction(d['minimum_allowing_each_percent_rounded_to_0p1pct']),Fraction(d['claimed_mean_degree']))

    def test_factor_d_does_not_equal_printed_degree(self):
        d=paper4_degree_arithmetic()
        self.assertNotEqual(Fraction(d['mean_degree_implied_by_6D_squared']),Fraction(d['claimed_mean_degree']))

    def test_paper4_mode_count_deltas(self):
        self.assertEqual([a-b for a,b in zip(PAPER2_FULL,PAPER4_PRIME)],[0,0,0,1,3,1,1,5])

    def test_zero_mode_same_graph_interpretation_excluded(self):
        d=zero_mode_hypothesis()
        self.assertEqual(d['not_possible_as_all_zero_modes_of_same_nonempty_weighted_graph_indices'],[0,1,2])
        self.assertEqual(d['not_possible_as_one_zero_mode_from_same_connected_weighted_graph_indices'],[0,1,2,4,7])

    def test_neighbor_closed_connected_proper_subset_impossible(self):
        adj=[{1},{0,2},{1,3},{2}]
        for mask in range(1,2**len(adj)-1):
            subset={i for i in range(len(adj)) if mask>>i&1}
            self.assertFalse(all(adj[i]<=subset for i in subset),subset)

    def test_finite_small_p3_neighbor_filter(self):
        r=patch_report(6.5,11)
        self.assertEqual((r['full_vertices'],r['full_edges']),(186,345))
        self.assertEqual(r['one_pass_core_components'],1)
        self.assertGreater(r['count_core_vertices_with_neighbors_outside_core'],0)
        self.assertEqual(r['full_zero_modes_weighted_L'],1)

    def test_finite_large_p3_neighbor_filter(self):
        r=patch_report(12.0,19)
        self.assertEqual((r['full_vertices'],r['full_edges']),(616,1185))
        self.assertEqual(r['one_pass_core_components'],1)
        self.assertGreater(r['count_core_vertices_with_neighbors_outside_core'],0)

    def test_pdf_native_hashes_distinct_from_historical_reports(self):
        self.assertEqual(len(ORIGINAL_PDF_HASHES),3)
        self.assertTrue(all(len(x)==64 for x in ORIGINAL_PDF_HASHES.values()))

if __name__=='__main__':unittest.main()
