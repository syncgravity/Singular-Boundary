"""Independent checks for corrected-open-Penrose 2+1D pilot.
Run under PYTHONPATH from bundled source archives; see README_NEXT.md.
"""
import unittest
import numpy as np
from corrected_2p1_pilot import (geometry,extrude_open,make_paths,face_cluster_loops,
    rect_path,trace_closed_path,loop_scalar_obs,run_chain,corr_operators)
from wilson_torus import mul, face_trace_scalar


def random_su2(rng,n):
    x=rng.normal(size=(n,4));return x/np.linalg.norm(x,axis=1)[:,None]


def gauge_links(links,gauges,ends):
    arr=np.empty_like(links)
    for i,(u,v) in enumerate(ends):
        inv=gauges[v].copy();inv[1:]*=-1
        arr[i]=mul(mul(gauges[u],links[i]),inv)
    return arr

class CorrectedPilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sp=geometry(3.5,0)
        cls.lat=extrude_open(cls.sp,6,1.7)
        cls.lo=face_cluster_loops(cls.sp)
        cls.paths=make_paths(cls.sp)

    def test_cut_and_project_geometry_and_open_boundary(self):
        s,l=self.sp,self.lat
        self.assertEqual((s['V'],s['E'],s['F']), (50,84,35))
        self.assertEqual(s['stats']['euler'],1)
        self.assertTrue(np.any(l['degree'][:6*s['E']]==3))
        self.assertTrue(np.any(l['degree'][:6*s['E']]==4))
        self.assertEqual(l['boundary_spatial_links'],6*s['stats']['boundary_edges'])
        self.assertEqual(l['P'],6*(s['F']+s['E']))

    def test_identity_config_and_multidistance_paths(self):
        s,l,lo,pa=self.sp,self.lat,self.lo,self.paths
        links=np.zeros((l['L'],4));links[:,0]=1.
        for f in range(l['P']):
            self.assertAlmostEqual(face_trace_scalar(f,links,l['fi'],l['sg']),1.,places=13)
        obs=loop_scalar_obs(links,6,s['E'],lo['idx'],lo['sign'],lo['length'],lo['kind'])
        np.testing.assert_allclose(obs,0,atol=1e-13)
        self.assertTrue(set(pa['length'])=={1,2,3})
        for j in range(len(pa['length'])):
            self.assertAlmostEqual(rect_path(links,6,s['E'],s['V'],pa['idx'][j],pa['sign'][j],
               pa['length'][j],pa['u'][j],pa['v'][j],0,2),1.,places=13)

    def test_gauge_covariance_all_plaquettes_operators_and_paths(self):
        s,l,lo,pa=self.sp,self.lat,self.lo,self.paths
        rng=np.random.default_rng(402)
        links=random_su2(rng,l['L'])
        gt=random_su2(rng,6*s['V'])
        updated=gauge_links(links,gt,l['ends'])
        for f in range(l['P']):
            self.assertLess(abs(face_trace_scalar(f,links,l['fi'],l['sg'])-face_trace_scalar(f,updated,l['fi'],l['sg'])),3e-13)
        orig=loop_scalar_obs(links,6,s['E'],lo['idx'],lo['sign'],lo['length'],lo['kind'])
        trans=loop_scalar_obs(updated,6,s['E'],lo['idx'],lo['sign'],lo['length'],lo['kind'])
        np.testing.assert_allclose(orig,trans,atol=3e-13)
        for j in range(len(pa['length'])):
            for t in (0,3):
                for lag in (1,2):
                    a=rect_path(links,6,s['E'],s['V'],pa['idx'][j],pa['sign'][j],pa['length'][j],
                                pa['u'][j],pa['v'][j],t,lag)
                    b=rect_path(updated,6,s['E'],s['V'],pa['idx'][j],pa['sign'][j],pa['length'][j],
                                pa['u'][j],pa['v'][j],t,lag)
                    self.assertAlmostEqual(a,b,places=12)

    def test_one_edge_rectangle_agrees_with_temporal_plaquette(self):
        s,l,pa=self.sp,self.lat,self.paths
        rng=np.random.default_rng(577)
        links=random_su2(rng,l['L'])
        for j in np.flatnonzero(pa['length']==1):
            e=int(pa['idx'][j,0]);
            for t in (0,2,5):
                rect=rect_path(links,6,s['E'],s['V'],pa['idx'][j],pa['sign'][j],1,
                               pa['u'][j],pa['v'][j],t,1)
                fp=t*(s['F']+s['E'])+s['F']+e
                self.assertAlmostEqual(rect,face_trace_scalar(fp,links,l['fi'],l['sg']),places=12)

    def test_boundary_edge_metropolis_delta_exact(self):
        l=self.lat
        rng=np.random.default_rng(841)
        links=random_su2(rng,l['L'])
        original=np.array([face_trace_scalar(f,links,l['fi'],l['sg']) for f in range(l['P'])])
        for eid in (0,5,21,l['L']-1):
            trial=links.copy();trial[eid]=random_su2(rng,1)[0]
            updated=np.array([face_trace_scalar(f,trial,l['fi'],l['sg']) for f in range(l['P'])])
            exact=np.dot(l['beta'],updated-original)
            fs=l['adj'][eid,:l['degree'][eid]]
            local=np.dot(l['beta'][fs],updated[fs]-original[fs])
            self.assertAlmostEqual(exact,local,places=11)

    def test_tiny_sampler_and_connected_shape(self):
        l=self.lat
        snaps,act,acc,err=run_chain(l['fi'],l['sg'],l['beta'],l['adj'],l['degree'],l['L'],
                                    seed=107,burn=2,steps=4,thin=2,angle=.8)
        self.assertEqual(snaps.shape,(2,l['L'],4))
        self.assertLess(err,1e-10)
        self.assertTrue(0<acc<1)
        self.assertEqual(act.shape,(2,))
        rng=np.random.default_rng(99)
        C=corr_operators(rng.normal(size=(10,6,3)))
        self.assertEqual(C.shape,(4,3,3))
        np.testing.assert_allclose(C[0],C[0].T,atol=1e-12)

if __name__=='__main__':unittest.main(verbosity=2)
