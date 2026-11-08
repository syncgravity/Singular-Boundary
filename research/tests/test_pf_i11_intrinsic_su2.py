#!/usr/bin/env python3
"""PF-I11 tests distinguish source-dependent and source-independent claims."""
import os, sys, math, unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from verify_pf_i11_intrinsic_su2 import (
    SOURCE_SHA,Complex, qconj,qmul,unit_quaternion,q_identity,plaquette_holonomies,
    wilson_action,gauge_transform,collapse_complex,tree_forest_and_chords,
    flat_connection_witness,exact_one_face,quadrature_one_face,
    assemble_complex,source_complex,case_summary,validate_source,triangle_membership)

SRC=Path(os.environ.get('PF_I11_SOURCE_SCRIPT',''))
HAS_SOURCE=SRC.is_file()

def square_complex():
    # Purely algebraic isolated plaquette for public tests (not a source patch).
    a=(1,0,0,0,0);b=(1,1,0,0,0);c=(1,1,1,0,0);d=(1,0,1,0,0)
    f=(a,b,c,d);labels=sorted(f)
    edges=sorted({tuple(sorted((u,v))) for u,v in zip(f,f[1:]+f[:1])});eid={x:i for i,x in enumerate(edges)}
    inds=[];sign=[]
    for u,v in zip(f,f[1:]+f[:1]):
        edge=tuple(sorted((u,v)));inds.append(eid[edge]);sign.append(1 if edge==(u,v) else -1)
    return Complex(labels,edges,[f],np.array([inds],dtype=np.int32),np.array([sign],dtype=np.int8),[(0,1)],[1])

class FiniteSU2WithoutSource(unittest.TestCase):
    def setUp(self):self.C=square_complex()

    def test_SU2_quaternion_associativity_and_inverse(self):
        r=np.random.default_rng(9);a,b,c=unit_quaternion(r,(3,))
        self.assertLess(np.linalg.norm(qmul(qmul(a,b),c)-qmul(a,qmul(b,c))),2e-15)
        self.assertLess(np.linalg.norm(qmul(a,qconj(a))-[1,0,0,0]),2e-15)

    def test_uniform_haar_quaternion_norm(self):
        r=np.random.default_rng(4);U=unit_quaternion(r,(2000,))
        np.testing.assert_allclose(np.sum(U*U,axis=1),1,atol=1e-14)

    def test_single_square_boundary_and_rank(self):
        T=collapse_complex(self.C)
        self.assertEqual((T['n_vertices'],T['n_edges'],T['n_faces']),(4,4,1))
        self.assertTrue(T['all_faces_collapse'])
        self.assertEqual(T['free_group_rank_if_complete'],0)

    def test_single_square_without_face_has_one_loop(self):
        C=self.C
        empty=Complex(C.labels,C.edges,[],np.empty((0,4),dtype=np.int32),np.empty((0,4),dtype=np.int8),[],[])
        T=collapse_complex(empty)
        self.assertEqual(T['free_group_rank_if_complete'],1)
        W=flat_connection_witness(empty,T)
        self.assertAlmostEqual(W['first_two_fundamental_loop_halftraces'][0],math.cos(.71),places=13)

    def test_gauge_action_and_trace_covariance_noncommuting(self):
        C=self.C;r=np.random.default_rng(13)
        U=unit_quaternion(r,(C.edge_count(),));g=unit_quaternion(r,(C.vertices_count(),))
        V=gauge_transform(C,U,g)
        self.assertAlmostEqual(wilson_action(C,U,1.3),wilson_action(C,V,1.3),places=12)
        self.assertAlmostEqual(plaquette_holonomies(C,U)[0,0],plaquette_holonomies(C,V)[0,0],places=12)
        self.assertGreater(wilson_action(C,U,1.3),0)

    def test_projected_area_weight_is_optional_positive(self):
        C=self.C;r=np.random.default_rng(8);U=unit_quaternion(r,(C.edge_count(),))
        S=wilson_action(C,U,2.,mode='projected-area')
        self.assertGreaterEqual(S,-1e-12)
        self.assertLessEqual(S,4*abs(math.sin(2*math.pi/5))+1e-12)

    def test_single_plaquette_partition_bessel_haar(self):
        for beta in [0.0,.25,.71,3.0]:
            x=exact_one_face(beta)
            y=quadrature_one_face(beta)
            self.assertAlmostEqual(x['Z'],y['Z'],places=12)
            self.assertAlmostEqual(x['mean_halftrace'],y['mean_halftrace'],places=12)
            self.assertGreater(x['Z'],0);self.assertLessEqual(x['Z'],1.)
            self.assertGreaterEqual(x['Z'],math.exp(-2*beta)-1e-14)

    def test_finite_partition_bounds_formula(self):
        # For any complex and positive face weights,
        # exp(-2 sum kappa) <= Z <= 1 from 0<= 1-cos(theta)<=2.
        for k in [0.,.3,1.5]:
            self.assertLessEqual(math.exp(-2*k),exact_one_face(k)['Z'])

    def test_face_orientation_reversal(self):
        C=self.C;r=np.random.default_rng(22);U=unit_quaternion(r,(C.edge_count(),))
        H=plaquette_holonomies(C,U)[0]
        face=(C.faces[0][0],C.faces[0][3],C.faces[0][2],C.faces[0][1])
        edge_index={x:i for i,x in enumerate(C.edges)}
        fedge=[];sign=[]
        for a,b in zip(face,face[1:]+face[:1]):
            edge=tuple(sorted((a,b)));fedge.append(edge_index[edge]);sign.append(1 if edge==(a,b) else -1)
        CC=Complex(C.labels,C.edges,[face],np.array([fedge]),np.array([sign]),C.face_families,C.face_heights)
        Hr=plaquette_holonomies(CC,U)[0]
        np.testing.assert_allclose(Hr,qconj(H),atol=1e-13)

    def test_d1_d0_zero_square(self):
        C=self.C
        # Exact integer simplicial/cellular incidence: boundary of boundary=0.
        vmap={v:i for i,v in enumerate(C.labels)}
        b0=np.zeros((C.edge_count(),C.vertices_count()),dtype=np.int32)
        for e,(a,b) in enumerate(C.edges):b0[e,vmap[a]]=-1;b0[e,vmap[b]]=1
        b1=np.zeros((C.face_count(),C.edge_count()),dtype=np.int32)
        for k,e in enumerate(C.face_edges[0]):b1[0,e]=C.face_signs[0,k]
        self.assertFalse(np.any(b1@b0))

    def test_nonabelian_independent_flat_cycles_abstract_two_loops(self):
        # 2 isolated square loops joined by one tree bridge, with no plaquettes.
        C=self.C
        a=(2,0,0,0,0);b=(2,1,0,0,0);c=(2,1,1,0,0);d=(2,0,1,0,0)
        new_edges=sorted(C.edges+[(a,b),(b,c),(c,d),(a,d),(C.labels[0],a)])
        VV=sorted(C.labels+[a,b,c,d]);Z=Complex(VV,new_edges,[],np.empty((0,4),dtype=np.int32),np.empty((0,4),dtype=np.int8),[],[])
        T=collapse_complex(Z);self.assertEqual(T['free_group_rank_if_complete'],2)
        W=flat_connection_witness(Z,T)
        self.assertLess(W['nonabelian_commutator_halftrace'],.99)


@unittest.skipUnless(HAS_SOURCE,'Original unpublished source script not mounted; private source-dependent test skipped')
class SourceDefinedC11(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src=validate_source(SRC)
        cls.small=source_complex(SRC,7)
        cls.large=source_complex(SRC,20)

    def test_first_source_complex_counts_and_topology(self):
        C=self.small;T=collapse_complex(C)
        self.assertEqual((len(C.labels),len(C.edges),len(C.faces)),(1550,3017,1468))
        self.assertEqual(T['free_group_rank_if_complete'],0)
        self.assertTrue(T['all_faces_collapse'])

    def test_exact_source_face_membership_height(self):
        C=self.small
        for face, (j,k) in zip(C.faces,C.face_families):
            self.assertTrue(triangle_membership(face[0],j,k,C.gamma))
        self.assertEqual(set(C.face_heights),{1,2})

    def test_original_source_complex_chain_identity_exact(self):
        C=self.small
        vmap={v:i for i,v in enumerate(C.labels)}
        b0=np.zeros((len(C.edges),len(C.labels)),dtype=np.int8)
        for e,(a,b) in enumerate(C.edges):b0[e,vmap[a]]=-1;b0[e,vmap[b]]=1
        # Avoid dense F x E: each face's four signed row sums telescope.
        for fe,sign in zip(C.face_edges,C.face_signs):
            self.assertFalse(np.any(np.einsum('i,ij->j',sign,b0[fe])))

    def test_source_random_gauge_invariance(self):
        C=self.small;r=np.random.default_rng(33)
        U=unit_quaternion(r,(C.edge_count(),));g=unit_quaternion(r,(C.vertices_count(),))
        B=gauge_transform(C,U,g)
        self.assertAlmostEqual(wilson_action(C,U,.67),wilson_action(C,B,.67),places=9)
        self.assertAlmostEqual(wilson_action(C,U,.67,mode='projected-area'),wilson_action(C,B,.67,mode='projected-area'),places=9)
        np.testing.assert_allclose(plaquette_holonomies(C,U)[:,0],plaquette_holonomies(C,B)[:,0],rtol=0,atol=1e-12)

    def test_large_source_flat_nonabelian_witness(self):
        C=self.large;T=collapse_complex(C)
        self.assertEqual(T['free_group_rank_if_complete'],6)
        W=flat_connection_witness(C,T)
        self.assertLess(W['max_identity_holonomy_error'],1e-10)
        self.assertLess(abs(W['flat_action_beta1']),1e-9)
        self.assertLess(W['nonabelian_commutator_halftrace'],.99)
        self.assertLess(W['first_two_fundamental_loop_halftraces'][0],.99)
        # Random gauge transformation preserves a nontrivial flat sector.
        r=np.random.default_rng(33)
        G=unit_quaternion(r,(C.vertices_count(),))
        B=gauge_transform(C,W['links'],G)
        self.assertLess(abs(wilson_action(C,B,1.)),1e-9)

    def test_source_completed_core_removes_all_loop_moduli(self):
        from verify_pf_i11_completed_core import one_corrected
        for n in [20,25]:
            r=one_corrected(self.src,n)
            self.assertTrue(r['all_faces_collapse'])
            self.assertEqual(r['free_group_rank_if_complete'],0)
            self.assertEqual(r['linearized_extra_flat_moduli_dimensions'],0)

    def test_source_field_linearized_flat_mode_dimensions(self):
        r=case_summary(self.large)
        self.assertEqual(r['linearized_extra_flat_moduli_dimensions'],18)
        self.assertEqual(r['linearized_flat_tangent_dimensions_total']-r['linearized_gauge_tangent_dimensions'],18)

    def test_all_source_eight_size_topology_table(self):
        import json
        p=Path(__file__).resolve().parent/'PF_I11_EIGHT_SIZE_SOURCE_GAUGE_COMPLEX.json'
        if not p.exists():self.skipTest('full source evidence not in public checkout')
        j=json.loads(p.read_text())
        self.assertEqual([x['free_group_rank_if_complete'] for x in j['results']],[0,0,0,0,0,6,10,10])
        self.assertTrue(all(x['all_faces_collapse'] for x in j['results']))

if __name__=='__main__':unittest.main(verbosity=2)
