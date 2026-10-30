"""Independent window construction, dual-method crosscheck, gauge invariance, restart."""
import sys,unittest,tempfile,json
from pathlib import Path
import numpy as np
from direct_cut_project import build, validate, face_label_sets, internal_window
from phase2 import links, verify,laplacian,holonomies
from phase2_extended import sparse_laplacian
from checkpoint_wilson import run_one

from audited_penrose import build as pentagrid_build

class DirectWindowTests(unittest.TestCase):
    def test_complex_incidence_and_heights(self):
        for r in (5.,6.5,8.,10.):
            for o in (0,1,2):
                g,gamma=build(r,o)
                out=validate(g,gamma)
                self.assertEqual(out['euler'],1)
                self.assertEqual(out['height_classes'],[1,2,3,4])
                self.assertLessEqual(out['max_degree'],7)
                self.assertAlmostEqual(out['gamma_sum'],1.,places=12)
    def test_agrees_with_independent_pentagrid_method_in_same_disk(self):
        for o in (0,1,2):
            direct,gamma=build(9.,o)
            independent,gg,_=pentagrid_build(radius=7.,offset=o)
            self.assertTrue(np.allclose(gg,gamma))
            pentagrid_faces={frozenset(independent.labels[i] for i in face)
                for face in independent.faces
                if all(np.linalg.norm(independent.xy[i]) <= 9.+1e-9 for i in face)}
            self.assertSetEqual(face_label_sets(direct),pentagrid_faces)
    def test_exact_second_moment(self):
        g,gm=build(5.)
        U=links(g,2026)
        H=sparse_laplacian(g,U)
        moment=np.real(H.multiply(H.transpose()).sum())/(2*len(g.labels))
        self.assertAlmostEqual(float(moment),validate(g,gm)['exact_normalized_m2'],10)
    def test_gauge_covariance(self):
        g,gm=build(5.)
        v=verify(g,links(g,2026))
        self.assertLess(v['hermiticity_error'],1e-10)
        self.assertLess(v['gauge_covariance_error'],1e-10)
        self.assertLess(v['wilson_gauge_error'],1e-10)
        self.assertGreater(v['min_eigenvalue'],-1e-9)
    def test_flat_connection_and_independent_haar(self):
        from haar_sampler import haar_su2
        from phase2_extended import low_spectrum
        g,gm=build(5.)
        U={e:np.eye(2,dtype=complex) for e in g.edges}
        ev=low_spectrum(g,U,k=2)['eigenvalues']
        self.assertLess(max(abs(x) for x in ev),1e-8)
        self.assertTrue(np.allclose(holonomies(g,U),1))
        rng=np.random.default_rng(432)
        for _ in range(20):
            u=haar_su2(rng)
            self.assertTrue(np.allclose(u@u.conj().T,np.eye(2),atol=1e-12))
            self.assertAlmostEqual(float(np.linalg.det(u).real),1.,places=12)

    def test_restart_identical_to_unsplit(self):
        with tempfile.TemporaryDirectory() as a,tempfile.TemporaryDirectory() as b:
            kw=dict(radius=5.,offset=1,beta=1.,chain=0,burn=3,thin=2,target=4)
            run_one(directory=a,module_sweeps=11,**kw)
            run_one(directory=b,module_sweeps=4,**kw)
            run_one(directory=b,module_sweeps=7,**kw)
            fn='R5.0_o1_b1.0_c0.json'
            x=json.loads((Path(a)/fn).read_text());y=json.loads((Path(b)/fn).read_text())
            self.assertEqual(x['rng_state'],y['rng_state'])
            self.assertEqual(x['links'],y['links'])
            
            for xx, yy in zip(x['measurements'], y['measurements']):
                self.assertEqual(xx['sweep'], yy['sweep'])
                self.assertAlmostEqual(xx['plaquette'], yy['plaquette'],places=13)
                for col in ('lambda0','lambda2','gap'):
                    self.assertLess(abs(xx[col]-yy[col]),1e-9)

if __name__=='__main__':unittest.main(verbosity=2)
