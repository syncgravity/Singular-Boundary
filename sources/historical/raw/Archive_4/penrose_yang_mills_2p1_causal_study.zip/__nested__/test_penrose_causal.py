import numpy as np
from numpy.testing import assert_allclose
from penrose_causal_study import Approximant, local_agreements, pentagon_window_audit,face_orientation_audit, saturation_index
from wilson_torus import penrose_faces,square_faces,prepare_cellulation,mul,face_trace_scalar


def test_periodic_cellulations():
    for m in (5,8,13,21):
        primitive=Approximant(m,primitive_periods=True)
        assert saturation_index(primitive.t1,primitive.t2)==1
        assert primitive.stats()['euler_torus']==0
    for m in (5,8,13,21):
        a=Approximant(m)
        s=a.stats()
        assert s['euler_torus']==0
        assert set(s['edge_face_incidence'])=={2}
        assert all(3 <= deg <=7 for deg in a.degrees)
        assert face_orientation_audit(a)['all_opposite']


def test_canonical_windows_are_pentagons():
    for m in (5,13,34):
        assert pentagon_window_audit(Approximant(m)) == {1:5,2:5,3:5,4:5}


def test_exact_area_coverage():
    for m in (5,13,21):
        a=Approximant(m)
        v=a.Qpar@np.eye(5)
        faceareas=sum(abs(np.linalg.det(v[:,[f[4],f[5]]])) for f in a.faces)
        cellarea=abs(np.linalg.det(np.stack([a.Qpar@a.t1,a.Qpar@a.t2],axis=1)))
        assert_allclose(faceareas,cellarea,rtol=1e-12,atol=1e-10)


def test_local_model_set_convergence():
    a=Approximant(55)
    out=local_agreements(a,max_k=6)
    assert all(x['match'] for x in out['balls'].values())


def test_oriented_wilson_cellulations():
    for fidx,sgn,E in (square_faces(34,40),penrose_faces(Approximant(13))):
        adj=prepare_cellulation(fidx,sgn,E)
        assert adj.shape==(E,2)
        links=np.zeros((E,4));links[:,0]=1.
        assert_allclose([face_trace_scalar(f,links,fidx,sgn) for f in range(len(fidx))],1.)


def test_penrose_wilson_gauge_invariance():
    a=Approximant(5)
    fidx,sgn,E=penrose_faces(a)
    rng=np.random.default_rng(123)
    links=rng.normal(size=(E,4));links=links/np.linalg.norm(links,axis=1)[:,None]
    vtx=rng.normal(size=(len(a.nodes),4));vtx=vtx/np.linalg.norm(vtx,axis=1)[:,None]
    before=np.array([face_trace_scalar(f,links,fidx,sgn) for f in range(len(fidx))])
    new=links.copy()
    for i,(u,v,d) in enumerate(a.edges):
        reverse=vtx[v]*[1.,-1.,-1.,-1.]
        new[i]=mul(mul(vtx[u],links[i]),reverse)
    after=np.array([face_trace_scalar(f,new,fidx,sgn) for f in range(len(fidx))])
    assert_allclose(before,after,atol=1e-12)
