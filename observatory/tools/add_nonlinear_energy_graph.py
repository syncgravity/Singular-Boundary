#!/usr/bin/env python3
"""Proof Atlas v2.38: exact classical 3D SU2 Wilson-flow energy and its limits.

Finite classical flow / fixed-regulator vacuum variance only. No continuum mass gap.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path

SOURCE_PATH='research/theorems/R3_NONLINEAR_CUBIC_PHYSICAL_ENERGY_DISSIPATION_2026-11-06.md'
SOURCE_SHA='0e7b7e4a4525a7fcf3d9ad2556de903102556172'
BRANCH='audit/2026-11-06-nonlinear-cubic-physical-energy'

def attach(root:Path):
    root=Path(root);p=root/'knowledge-graph.json';g=json.loads(p.read_text())
    if g['version']=='v2.38-draft':return g
    assert g['version']=='v2.37-draft',g['version']
    nodes=g['nodes'];edges=g['edges'];by={n['id']:n for n in nodes}
    assert len(nodes)==128 and len(edges)==275
    source=dict(title='Nonlinear 3D cubic SU2 physical-action dissipation and curvature concentration',
                path=SOURCE_PATH,git_blob_sha=SOURCE_SHA,
                url=f'https://github.com/syncgravity/singular-boundary/blob/{SOURCE_SHA}/{SOURCE_PATH}')
    def chk(label,state='open',note=''):return dict(label=label,state=state,note=note)
    def add(id,title,kind,status,stage,summary,detail,checks,tags,importance=4):
        assert id not in by,id
        n=dict(id=id,title=title,kind=kind,status=status,stage=stage,
               summary=summary,detail=detail,checks=checks,sources=[source],
               tags=tags,importance=importance,core=False,route=None)
        nodes.append(n);by[id]=n
    def edge(a,b,kind,label,status='open'):
        assert a in by and b in by,(a,b)
        assert not any(e['from_id']==a and e['to_id']==b and e['kind']==kind for e in edges)
        edges.append(dict(from_id=a,to_id=b,kind=kind,label=label,status=status))

    add('R-NONLINEAR-PHYS-ACTION',
        'Full nonlinear SU(2) cubic spatial physical-action dissipation',
        'result','finite','P2',
        'For finite 3D open cubic Wilson gradient flow, E_h=8S_h/h satisfies the exact nonperturbative energy/physical-flow-force balance E_h(tau)+8 integral_0^tau h^-3 ||grad S_h||² dt=E_h(0).',
        'Gauge equivariant at every finite flow time. Conditional on a uniformly bounded total initial classical curvature energy, evolved energy and integrated force are uniform in mesh. This is NOT a pointwise nonlinear curvature smoothing, interacting-vacuum energy bound or 4D mass-gap result.',
        [chk('Exact nonlinear product-SU2 Wilson action chain rule','met','No linearized or small-field assumption'),
         chk('Finite gauge-equivariant flow at fixed physical tau','met','s=tau/h²; compact configuration manifold'),
         chk('Uniform physical energy and integrated force under uniform classical initial E','conditional','The initial bound is a separate classical hypothesis'),
         chk('Uniform true-vacuum quantum flowed covariance and Schur/IR','open','No interacting field-measure limit')],
        ['SU2','cubic','nonlinear','classical','physical-flow'],5)
    add('R-PLAQUETTE-HOLONOMY-ADMISSIBILITY',
        'Conditional small-plaquette holonomy and energy-measure compactness',
        'result','conditional','P2',
        'If total classical E_h(0)≤M on a fixed physical box, every flowed plaquette angle obeys theta_p(tau)≤(pi/2)sqrt(Mh); positive face-energy measures have weak subsequences for each fixed physical tau.',
        'Only an O(sqrt h) plaquette-angle bound, not the O(h²) curvature-angle scale, physical curvature derivative regularity, uniqueness or diffuse energy density. Local energy concentration is possible.',
        [chk('Exact link-plaquette energy positivity and angle inequality','met'),
         chk('Uniform classical initial total energy across h','conditional','Not established for quantum Wilson ground-state samples'),
         chk('Continuous curvature-energy density and unique continuum limit','open','Positive Radon measures may be atomic')],
        ['SU2','cubic','classical','curvature-measure'],4)
    add('R-CUBIC-CURVATURE-ATOMIC',
        'One-link curvature concentration defeats pointwise nonlinear inference',
        'result','obstruction','P2',
        'A genuine SU(2) cubical configuration with one link exp(sqrt h T3) has E_h→4, plaquette curvature angle/h²=h^-3/2, and gauge-invariant face-energy measure converging to 4 delta at the spatial center.',
        'Exact initial-flow-time nonlinear configuration respecting original-link incidence. It refutes the implication bounded physical classical action ⇒ diffuse energy measure / pointwise curvature. It does NOT refute positive-time nonlinear smoothing or a YM continuum mass gap.',
        [chk('Four incident plaquettes of an interior edge','met','Bianchi/incidence satisfied by original SU2 links'),
         chk('Energy bounded, principal-angle/h² diverges','met','E_h=32(1−cos(sqrt h/2))/h→4'),
         chk('Curvature defect survives a fixed positive physical flow time','open','Not established; counterexample is at tau=0')],
        ['SU2','cubic','counterexample','energy-concentration'],4)
    add('R-FINITE-FLOWED-VACUUM',
        'Finite true-Wilson-vacuum variance after nonlinear spatial flow',
        'result','finite','T2',
        'For every fixed finite cubic regulator and finite physical flow time, the nonlinear flowed fundamental Wilson loop remains a nonconstant gauge-invariant function; strict positivity/full support of the interacting ground-state law gives strictly positive variance.',
        'Finite-time spatial flow is a diffeomorphism; variance positivity follows with no quantitative h,R lower bound. Exact expectation-level nonlinear energy dissipation holds for the true finite vacuum but its initial raw physical energy is not known uniformly bounded.',
        [chk('Nonconstant flowed Wilson loop under finite smooth diffeomorphism','met'),
         chk('Strict finite interacting-vacuum variance','met','Positive finite Wilson ground state has full Haar support'),
         chk('Uniform nonzero renormalized covariance in physical continuum','open','Not proved: variance may vanish on refinement')],
        ['SU2','cubic','finite-quantum-vacuum','observable'],4)

    old=by['W-NONLINEAR-PHYS-RADIUS']
    assert old['status']=='open'
    old['summary']='A full nonlinear 3D classical physical-action balance is now exact under bounded initial energy, but gauge curvature derivative smoothing, physical interacting-vacuum covariance and 4D long-time Schur estimates remain OPEN.'
    old['detail']='Finite nonlinear Wilson flow preserves classical physical energy and integrated force; these estimates permit curvature concentration and have no proved uniform initial quantum-vacuum energy hypothesis. Next: genuine positive-physical-radius nonlinear smoothing beyond integrated force, and a renormalized nontrivial 4D interacting observable/Schur comparison.'
    old['checks'][0]['state']='partial'
    old['checks'][0]['note']='Exact nonlinear physical-action dissipation and conditional small plaquette holonomy; no pointwise physical curvature derivative smoothing or 4D quantum estimate.'

    edge('M-CUBIC','R-NONLINEAR-PHYS-ACTION','finite-3d-model','Open original-link cubical SU2 spatial Wilson','finite')
    edge('R-CUBIC-SPATIAL-WILSON-FLOW','R-NONLINEAR-PHYS-ACTION','nonlinear-physical-scale','Exact classical Wilson gradient flow at tau=h²s','finite')
    edge('R-LINEAR-CUBIC-PHYSFLOW','R-NONLINEAR-PHYS-ACTION','distinct-scopes','Classical nonlinear energy balance is weaker than derivative smoothing','finite')
    edge('R-NONLINEAR-PHYS-ACTION','R-PLAQUETTE-HOLONOMY-ADMISSIBILITY','conditional-consequence','Uniform initial classical energy implies small Wilson plaquettes','conditional')
    edge('R-PLAQUETTE-HOLONOMY-ADMISSIBILITY','R-CUBIC-CURVATURE-ATOMIC','obstruction-to-inference','Haar-invariant positive energy may concentrate at tau=0','obstruction')
    edge('R-CUBIC-CURVATURE-ATOMIC','W-NONLINEAR-PHYS-RADIUS','regularity-still-open','No pointwise field/curvature bounds from energy alone','open')
    edge('R-NONLINEAR-PHYS-ACTION','W-NONLINEAR-PHYS-RADIUS','partial-classical-checkpoint','Time-integrated force only; true vacuum assumptions unknown','open')
    edge('R-NONLINEAR-PHYS-ACTION','R-FINITE-FLOWED-VACUUM','same-finite-flow','Nonlinear gauge-equivariant diffeomorphism at finite regulator','finite')
    edge('R-FINITE-FLOWED-VACUUM','T2-OBSERVABLES','finite-not-continuum','Strict variance at fixed h does not imply nontrivial OS field','finite')
    edge('R-FINITE-FLOWED-VACUUM','W-PHYSICAL-FLOWED-SCHUR','uniformity-missing','Actual interacting covariance and long-time Schur remain unproved','open')
    edge('R-NONLINEAR-PLAQUETTE-FLOW-ESCAPE','R-CUBIC-CURVATURE-ATOMIC','distinct-obstructions','Over-flow variance vs initial curvature concentration','obstruction')
    edge('W-NONLINEAR-PHYS-RADIUS','T3-TIME-COMPARE','no-infrared-certificate','Classical time integral not quantum physical-time decay','open')
    edge('R-NONLINEAR-PHYS-ACTION','G-GRAV','distinct-goal','Classical cubic gauge flow does not establish gravitational UV theory','open')

    g.update(version='v2.38-draft',build_date='2026-11-06',git_branch=BRANCH,
      scope='Exact nonlinear classical 3D Wilson physical-action dissipation, conditional small plaquette holonomies, curvature-energy atomic concentration, and strictly finite interacting-vacuum flowed variance. No physical nonlinear smoothing derivative, 4D YM gap or gravity UV proof.')
    assert len(nodes)==132 and len(edges)==288
    assert len({x['id'] for x in nodes})==132
    assert sum(x['kind']=='dataset' for x in nodes)==26
    assert all(x['status']=='open' for x in nodes if x['kind'] in ('goal','gate'))
    assert by['G-GRAV']['status']=='open'
    p.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
    (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n')
    return g

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
    g=attach(parser.parse_args().root)
    print('PASS nonlinear physical energy overlay',g['version'],len(g['nodes']),len(g['edges']),'P0–P5 OPEN')
