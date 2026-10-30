import numpy as np
from penrose_2p1_study import paired_spatial,extrude,geometric_weights
from wilson_torus import mul,face_trace_scalar

def full_link_endpoints(sp,nt):
    V=sp['V'];E=sp['E']
    edges=np.empty((nt*(E+V),2),dtype=np.int64)
    for t in range(nt):
        for e,(u,v) in enumerate(sp['edges']):
            edges[t*E+e]=t*V+u,t*V+v
        for u in range(V):
            edges[nt*E+t*V+u]=t*V+u,((t+1)%nt)*V+u
    return edges

def test_3d_volume_and_plaquettes():
    for M in [5,8]:
        p,s=paired_spatial(M)
        assert np.isclose(p['area'],s['area'])
        for sp in [p,s]:
            nt=4;lat=extrude(sp,nt,3,np.sqrt(p['area']/p['F']),np.sqrt(p['area']/p['F']))
            assert lat['L']==nt*(sp['E']+sp['V'])
            assert lat['P']==nt*(sp['E']+sp['F'])
            assert len(lat['fi'])==len(lat['beta'])
            assert np.all(lat['beta']>0)
            assert np.all(lat['degree'][:nt*sp['E']]==4)
            assert np.all(lat['degree'][nt*sp['E']:]>=3)
            ends=full_link_endpoints(sp,nt)
            for face,sign in zip(lat['fi'],lat['sg']):
                sources=np.where(sign==1,ends[face,0],ends[face,1])
                dest=np.where(sign==1,ends[face,1],ends[face,0])
                assert np.array_equal(dest,np.roll(sources,-1))

def test_square_beta_isotropic():
    p,s=paired_spatial(5)
    a_ref=np.sqrt(p['area']/p['F'])
    x,y=geometric_weights(s,3.0,a_ref,a_ref)
    assert np.allclose(y,3)
    assert np.allclose(x,3*s['F']/p['F'])

def test_3d_gauge_invariance():
    p,s=paired_spatial(5)
    for sp in [p,s]:
        nt=3
        a_ref=np.sqrt(p['area']/p['F'])
        lat=extrude(sp,nt,2.5,a_ref,a_ref)
        rng=np.random.default_rng(130)
        links=rng.normal(size=(lat['L'],4));links/=np.linalg.norm(links,axis=1)[:,None]
        gauges=rng.normal(size=(sp['V']*nt,4));gauges/=np.linalg.norm(gauges,axis=1)[:,None]
        ends=full_link_endpoints(sp,nt)
        new=np.empty_like(links)
        for e,(u,v) in enumerate(ends):
            q=gauges[v].copy();q[1:]*=-1
            new[e]=mul(mul(gauges[u],links[e]),q)
        selected=np.unique(np.linspace(0,lat['P']-1,50,dtype=int))
        for f in selected:
            assert abs(face_trace_scalar(f,links,lat['fi'],lat['sg'])-face_trace_scalar(f,new,lat['fi'],lat['sg']))<2e-13

def test_rectangular_loop_gauge_invariance():
    from penrose_2p1_study import rect_trace
    p,_=paired_spatial(5)
    nt=4;V=p['V'];E=p['E']
    rng=np.random.default_rng(233)
    links=rng.normal(size=(nt*(E+V),4));links/=np.linalg.norm(links,axis=1)[:,None]
    gauges=rng.normal(size=(nt*V,4));gauges/=np.linalg.norm(gauges,axis=1)[:,None]
    ends=full_link_endpoints(p,nt)
    transformed=np.empty_like(links)
    for e,(u,v) in enumerate(ends):
        q=gauges[v].copy();q[1:]*=-1
        transformed[e]=mul(mul(gauges[u],links[e]),q)
    for t in [0,1,3]:
        for e in [0,23,167]:
            for lag in [1,2,3]:
                orig=rect_trace(links,nt,E,V,p['edges'],e,t,lag)
                new=rect_trace(transformed,nt,E,V,p['edges'],e,t,lag)
                assert abs(orig-new)<2e-13

def test_temporal_rectangle_one_is_temporal_plaquette():
    from penrose_2p1_study import rect_trace
    p,s=paired_spatial(5)
    for sp in [p,s]:
        nt=4;V=sp['V'];E=sp['E'];F=sp['F']
        lat=extrude(sp,nt,2.5,np.sqrt(p['area']/p['F']),np.sqrt(p['area']/p['F']))
        rng=np.random.default_rng(919)
        links=rng.normal(size=(lat['L'],4));links/=np.linalg.norm(links,axis=1)[:,None]
        for t in [0,1,nt-1]:
            for e in [0,10,E-1]:
                f=t*(F+E)+F+e
                a=face_trace_scalar(f,links,lat['fi'],lat['sg'])
                b=rect_trace(links,nt,E,V,sp['edges'],e,t,1)
                assert abs(a-b)<1e-13


def test_metropolis_local_action_change():
    p,s=paired_spatial(5)
    sp=p;nt=3
    ar=np.sqrt(p['area']/p['F'])
    lat=extrude(sp,nt,2.75,ar,ar)
    rng=np.random.default_rng(171)
    links=rng.normal(size=(lat['L'],4));links/=np.linalg.norm(links,axis=1)[:,None]
    for eid in [0,sp['E']-1,nt*sp['E'],nt*sp['E']+37]:
        trial=rng.normal(size=4);trial/=np.linalg.norm(trial)
        before=np.array([face_trace_scalar(f,links,lat['fi'],lat['sg']) for f in range(lat['P'])])
        new=links.copy();new[eid]=trial
        after=np.array([face_trace_scalar(f,new,lat['fi'],lat['sg']) for f in range(lat['P'])])
        actual=float(np.dot(lat['beta'],after-before))
        local=float(sum(lat['beta'][f]*(after[f]-before[f])
                        for f in lat['adj'][eid,:lat['degree'][eid]]))
        assert abs(actual-local)<1e-12
