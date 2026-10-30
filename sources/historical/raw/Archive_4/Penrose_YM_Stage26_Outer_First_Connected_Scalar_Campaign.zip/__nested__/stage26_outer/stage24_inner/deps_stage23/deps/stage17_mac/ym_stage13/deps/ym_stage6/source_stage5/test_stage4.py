import unittest
import numpy as np
from stage3_periodic_pilot import square_torus
from stage2_rational_torus import build_torus
from stage4_smearing_flux import staple_structure,ape_spatial,winding_paths,measure_winding,measure_scalar_groups,connected_corr,gevp_diagnostics,trace_spatial_path
from stage3_periodic_pilot import _basis
from wilson_torus import mul


def qdag(q):
    q=q.copy();q[1:]*=-1;return q

class Stage4Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sp=square_torus(6,7,42.0)
        cls.pen=build_torus(5)
        cls.nt=4
        cls.rng=np.random.default_rng(922)
        L=cls.nt*(cls.sp['E']+cls.sp['V'])
        x=cls.rng.normal(size=(L,4));cls.U=x/np.linalg.norm(x,axis=1)[:,None]

    def test_staples_each_torus_edge_has_two(self):
        z=staple_structure(self.sp)
        self.assertTrue(np.all(z[3]==2))
        self.assertTrue(np.all(z[2]>0))

    def test_square_scalar_basis_is_complete_and_closed(self):
        from stage4_smearing_flux import square_scalar_basis
        b=square_scalar_basis(self.sp)
        self.assertEqual(b['counts'],{'plaquette':42,'rectangle_1x2':84,'square_2x2':42})
        self.assertEqual(set(b['length']),{4,6,8})
        identity=np.zeros_like(self.U);identity[:,0]=1
        x=measure_scalar_groups(identity,self.nt,self.sp['E'],b['idx'],b['sign'],b['length'],b['kind'])
        self.assertLess(np.max(abs(x)),1e-14)

    def test_ape_unitary_and_temporal_unchanged(self):
        z=staple_structure(self.sp)
        w=ape_spatial(self.U,self.nt,self.sp['E'],*z,.35,2)
        self.assertLess(np.max(abs(np.linalg.norm(w,axis=1)-1)),1e-12)
        self.assertTrue(np.array_equal(w[self.nt*self.sp['E']:],self.U[self.nt*self.sp['E']:]))

    def test_alpha_zero_is_identity(self):
        z=staple_structure(self.sp)
        w=ape_spatial(self.U,self.nt,self.sp['E'],*z,0.,2)
        self.assertLess(np.max(abs(w-self.U)),1e-13)

    def test_ape_gauge_covariance(self):
        V,E,nt=self.sp['V'],self.sp['E'],self.nt
        G=self.rng.normal(size=(nt*V,4));G/=np.linalg.norm(G,axis=1)[:,None]
        ug=self.U.copy()
        for t in range(nt):
            for e,(u,v) in enumerate(self.sp['edges']):
                ug[t*E+e]=mul(mul(G[t*V+u],self.U[t*E+e]),qdag(G[t*V+v]))
            for u in range(V):
                ug[nt*E+t*V+u]=mul(mul(G[t*V+u],self.U[nt*E+t*V+u]),qdag(G[((t+1)%nt)*V+u]))
        z=staple_structure(self.sp)
        w1=ape_spatial(self.U,nt,E,*z,.4,2)
        w2=ape_spatial(ug,nt,E,*z,.4,2)
        expected=w1.copy()
        for t in range(nt):
            for e,(u,v) in enumerate(self.sp['edges']):
                expected[t*E+e]=mul(mul(G[t*V+u],w1[t*E+e]),qdag(G[t*V+v]))
        self.assertLess(np.max(abs(expected[:nt*E]-w2[:nt*E])),3e-12)
        basis,_=_basis(self.sp)
        a=measure_scalar_groups(w1,nt,E,basis['idx'],basis['sign'],basis['length'],basis['kind'])
        b=measure_scalar_groups(w2,nt,E,basis['idx'],basis['sign'],basis['length'],basis['kind'])
        self.assertLess(np.max(abs(a-b)),1e-11)
        loops=winding_paths(self.sp,nanchors=3)
        x=measure_winding(w1,nt,E,loops['idx'],loops['sign'],loops['length'],loops['direction'])
        y=measure_winding(w2,nt,E,loops['idx'],loops['sign'],loops['length'],loops['direction'])
        self.assertLess(np.max(abs(x-y)),1e-11)
        from corrected_2p1_pilot import measure_wilson_paths
        from stage3_periodic_pilot import periodic_paths
        paths=periodic_paths(self.sp,max_steps=2,per_size=3)
        z1=measure_wilson_paths(w1,nt,E,V,paths['idx'],paths['sign'],paths['length'],paths['u'],paths['v'],2)
        z2=measure_wilson_paths(w2,nt,E,V,paths['idx'],paths['sign'],paths['length'],paths['u'],paths['v'],2)
        self.assertLess(np.max(abs(z1-z2)),1e-11)

    def test_winding_both_geometries(self):
        for sp in (self.sp,self.pen):
            p=winding_paths(sp,nanchors=3)
            self.assertLess(p['deck_residual'],1e-10)
            for x in p['meta']:
                self.assertGreater(x['edges'],2)
                self.assertGreater(x['length'],0)
                self.assertLess(x['edges'],80)
            self.assertEqual(set(p['direction']),{0,1})

    def test_closed_loop_gauge_scalar(self):
        loops=winding_paths(self.sp,nanchors=2)
        identity=np.zeros_like(self.U);identity[:,0]=1
        vals=measure_winding(identity,self.nt,self.sp['E'],loops['idx'],loops['sign'],loops['length'],loops['direction'])
        self.assertLess(np.max(abs(vals-1)),1e-14)

    def test_winding_center_charge_on_both_tori(self):
        from stage4_smearing_flux import oriented_windings
        from wilson_torus import face_trace_scalar
        for sp in (self.sp,self.pen):
            nt=4;E=sp['E'];V=sp['V']
            arr=self.rng.normal(size=(nt*(E+V),4));arr/=np.linalg.norm(arr,axis=1)[:,None]
            gauge=arr.copy();dw,_=oriented_windings(sp)
            for t in range(nt):
                for e in range(E):
                    if dw[e,0]%2: gauge[t*E+e]*=-1
            for t in range(nt):
                for j in range(sp['F']):
                    fi=sp['face_idx'][j]+t*E
                    before=face_trace_scalar(0,arr,fi[None,:],sp['face_sign'][j][None,:])
                    after=face_trace_scalar(0,gauge,fi[None,:],sp['face_sign'][j][None,:])
                    self.assertAlmostEqual(before,after,places=11)
            winding=winding_paths(sp,nanchors=2)
            before=measure_winding(arr,nt,E,winding['idx'],winding['sign'],winding['length'],winding['direction'])
            after=measure_winding(gauge,nt,E,winding['idx'],winding['sign'],winding['length'],winding['direction'])
            self.assertLess(np.max(abs(before[:,0]+after[:,0])),1e-10)
            self.assertLess(np.max(abs(before[:,1]-after[:,1])),1e-10)

    def test_connected_corr_constant_zero(self):
        x=np.ones((8,4,9));self.assertLess(np.max(abs(connected_corr(x))),1e-14)

    def test_gevp_rejects_indefinite(self):
        C=np.zeros((3,3,3));C[1]=np.diag([1,-1,1]);C[2]=np.eye(3)*.1
        self.assertFalse(gevp_diagnostics(C)['metric_positive'])

if __name__=='__main__':unittest.main()
