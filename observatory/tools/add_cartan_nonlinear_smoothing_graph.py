#!/usr/bin/env python3
"""Source-pinned finite Cartan/Abelian planar nonlinear positive-time smoothing overlay.

Research-only: invariant subset is Haar-null in full SU2 configuration space.
Does not change continuum Yang--Mills or gravity gate statuses.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

SOURCE_PATH='research/theorems/R3_EMBEDDED_CARTAN_NONLINEAR_POSITIVE_RADIUS_SMOOTHING_2026-11-06.md'
SOURCE_SHA='e4fa23a492245068b7f3115ede3dc2272a34115f'
BRANCH='audit/2026-11-06-cartan-positive-time-cubic-smoothing'


def attach(root: Path):
    root=Path(root)
    fp=root/'knowledge-graph.json'
    g=json.loads(fp.read_text())
    if g['version']=='v2.39-draft':
        assert len(g['nodes'])==136 and len(g['edges'])==302
        return g
    assert g['version']=='v2.38-draft',g['version']
    nodes=g['nodes'];edges=g['edges']
    assert len(nodes)==132 and len(edges)==288
    by={n['id']:n for n in nodes}
    source=dict(title='Exact finite nonlinear planar Cartan cubic physical-flow smoothing and Nash certificate',
                path=SOURCE_PATH,git_blob_sha=SOURCE_SHA,
                url=f'https://github.com/syncgravity/singular-boundary/blob/{SOURCE_SHA}/{SOURCE_PATH}')
    def check(label,state='open',note=''):return dict(label=label,state=state,note=note)
    def add(id,title,kind,status,stage,summary,detail,checks,tags,importance=4):
        assert id not in by
        obj=dict(id=id,title=title,kind=kind,status=status,stage=stage,summary=summary,
                 detail=detail,checks=checks,sources=[source],tags=tags,importance=importance,
                 core=False,route=None)
        nodes.append(obj);by[id]=obj
    def link(a,b,kind,label,status='open'):
        assert a in by and b in by,(a,b)
        assert not any(e['from_id']==a and e['to_id']==b and e['kind']==kind for e in edges)
        edges.append(dict(from_id=a,to_id=b,kind=kind,label=label,status=status))

    add('R-PLANAR-CARTAN-EMBED',
        'Exact invariant SU(2) Cartan-planar cubic nonlinear Wilson flow',
        'result','finite','P2',
        'The full 3D open cubic SU2 spatial Wilson gradient flow preserves a same-Cartan, z-independent xy-link configuration with identity vertical links; lifted curvature satisfies q_s=-(1/4)BB* sin(q).',
        'A true finite-dimensional nonlinear invariant SU2 solution class with all xz/yz plaquettes identity. It is Abelian, and the fixed Cartan subset has zero Haar probability under the actual strictly positive finite Wilson vacuum. Not generic noncommutative cubic or 4D quantum Yang-Mills.',
        [check('Full 3D original-link force reduces exactly','met','Analytic 3D incidence; two independent full SU2 quaternion tests'),
         check('Non-winding flux lift |q(0)|<pi/2','conditional','Required to keep sine monotone'),
         check('True interacting Wilson-vacuum positive-probability estimate','open','Fixed commuting subgroup is Haar-null')],
        ['cubic','SU2','Cartan','finite','nonlinear'],5)
    add('R-CARTAN-POSITIVE-FLOW-SMOOTH',
        'Positive-physical-time nonlinear curvature smoothing from 3D action',
        'result','conditional','P2',
        'On the invariant Cartan-planar cubic sector with an admissible flux lift, uniform initial 3D classical action M implies ||F_h(tau)||infinity <= (pi/2)sqrt(2 C_N M/(kappa tau)), tau>0, uniformly in h and spatial mesh, kappa bounded below for fine h.',
        'Exact nonlinear positive-time curvature bound from the 2D Dirichlet Nash inequality and dynamically varying symmetric conductances c_e in [cos(delta),1]. Also H_h(tau)+kappa/4 int ||B*F_h||² <=H_h(0). No gap assumption, but it applies only to a Haar-null Abelian subset with an explicit admissibility condition.',
        [check('Uniform discrete Nash inequality on planar dual grid','met','Zero extension to Z²'),
         check('Nonlinear positive-time L2-to-Linfinity bound','met','Time-dependent conductances and duality'),
         check('Uniform bounded classical initial 3D energy and flux lift','conditional','Not established for actual interacting Wilson vacuum'),
         check('Full 3D noncommuting SU2 regularity at physical radius','open','Missing commutator and quantum-vacuum estimates')],
        ['SU2','cubic','conditional','nonlinear-smoothing','classical'],5)
    add('R-CARTAN-ALLTIME-L2',
        'All-time O(h²) nonlinear-to-linear Cartan curvature comparison',
        'result','conditional','P2',
        'Within the invariant admissible planar sector, ||F_nl(tau)-exp[-tau BB*/(4h²)]F_0||_(2,h) <= (1-cos(delta))/sqrt(2cos(delta)) ||F_0||_(2,h) for every tau>=0. Bounded initial 3D action gives delta=O(h) and O(h²) error.',
        'A genuine all-time discrete nonlinear perturbation bound, including realizable initially concentrated curvatures. For bounded initial sup curvature K, a separate L-infinity bound tau h² K³/12 holds. No nonabelian curvature transport estimate or physical-time interacting Schur comparison follows.',
        [check('Exact relative scalar conductance bound','met','1-cos(delta) controls all edge coefficients'),
         check('Uniform all-time L2 error from energy/Young inequality','met','Independent concentrated defect and smooth numerical tests'),
         check('Actual 4D interacting nonabelian continuum observables','open','Abelian classical sector is Haar-null')],
        ['SU2','cubic','Cartan','conditional','O(h²)'],5)
    add('W-FULL-NONABELIAN-PHYS-SMOOTHING',
        'Full non-Abelian physical-radius curvature and quantum Schur estimates',
        'work','open','P2',
        'Transfer conditional nonlinear positive-time curvature smoothing beyond the fixed Cartan sector to generic, noncommuting SU2 cubic fields under hypotheses supported by the true weak-coupling Wilson vacuum; then establish renormalized covariance and physical-time Schur estimates.',
        'Requires control of noncommutative Bianchi, covariant Laplacian and commutator terms, concentration/instantonic channels, probability under Omega_h² Haar rather than a Haar-null invariant subset, and nontrivial 4D OS reconstruction with dense infrared probes. No continuum gate closed.',
        [check('Noncommuting covariant curvature diffusion with h-uniform positive-time bounds'),
         check('Positive-probability true interacting Wilson-vacuum admissibility and renormalized moments'),
         check('Full energy-dependent Schur/connected long-time estimates uniform in h,R'),
         check('Nontrivial 4D OS Yang-Mills reconstruction and positive spectral gap')],
        ['SU2','cubic','nonabelian','open','4D'],5)

    link('M-CUBIC','R-PLANAR-CARTAN-EMBED','exact-restricted-subsector','Same original-link three-dimensional SU2 cubic action, commuting planar links only','finite')
    link('R-NONLINEAR-PHYS-ACTION','R-PLANAR-CARTAN-EMBED','same-classical-flow','Full nonlinear Wilson energy law restricts to exact Cartan planar invariant sector','finite')
    link('R-PLANAR-CARTAN-EMBED','R-CARTAN-POSITIVE-FLOW-SMOOTH','nonlinear-invariant-reduction','Scalar graph sine diffusion and Dirichlet Nash smoothing','conditional')
    link('R-PLAQUETTE-HOLONOMY-ADMISSIBILITY','R-CARTAN-POSITIVE-FLOW-SMOOTH','extra-admissibility','Bounded energy plus no-winding Cartan lift yields uniform ellipticity','conditional')
    link('R-CUBIC-CURVATURE-ATOMIC','R-CARTAN-POSITIVE-FLOW-SMOOTH','distinct-positive-time-result','Initial concentration need not prevent positive-time smoothing in the restricted sector','conditional')
    link('R-LINEAR-CUBIC-PHYSFLOW','R-CARTAN-ALLTIME-L2','nonlinear-perturbation','Flat Cartan heat used as comparison at identical physical flow time','finite')
    link('R-CARTAN-POSITIVE-FLOW-SMOOTH','R-CARTAN-ALLTIME-L2','energy-to-comparison','Bounded initial action yields h² relative nonlinear perturbation','conditional')
    link('R-CARTAN-ALLTIME-L2','R-PERIODIC-FLOW-FOURIER','distinct-linear-controls','Open planar Dirichlet vs periodic cubic transverse Fourier; no universality','finite')
    link('R-PLANAR-CARTAN-EMBED','W-FULL-NONABELIAN-PHYS-SMOOTHING','Haar-null-restriction','Fixed maximal torus has zero true-Wilson-vacuum probability','open')
    link('R-CARTAN-POSITIVE-FLOW-SMOOTH','W-FULL-NONABELIAN-PHYS-SMOOTHING','missing-commutators','Scalar uniformly elliptic diffusion not established for generic SU2','open')
    link('R-CARTAN-ALLTIME-L2','W-FULL-NONABELIAN-PHYS-SMOOTHING','missing-nonabelian-error','O(h²) Abelian Maxwell comparison does not transfer interacting SU2','open')
    link('W-FULL-NONABELIAN-PHYS-SMOOTHING','W-NONLINEAR-PHYS-RADIUS','refines-open-regularity','Nonlinear classical positive-time regularity in full nonabelian sector unproved','open')
    link('W-FULL-NONABELIAN-PHYS-SMOOTHING','T3-TIME-COMPARE','quantum-time-open','Full physical time Schur/spectral exclusion remains open','open')
    link('W-FULL-NONABELIAN-PHYS-SMOOTHING','T0-QC-3D','distinct-geometry','Cubic fixed Cartan result does not construct Penrose 3D gauge regulator','open')

    g.update(version='v2.39-draft',git_branch=BRANCH,build_date='2026-11-06',scope='Exact 3D SU2 Cartan-planar invariant nonlinear flow: conditional positive-time physical curvature Nash estimate from bounded classical energy and all-time O(h²) Maxwell L2 comparison. Restricted Haar-null commuting sector, no generic SU2 quantum or gravity theorem.')
    assert len(nodes)==136 and len(edges)==302
    assert len({n['id'] for n in nodes})==136 and len([n for n in nodes if n['kind']=='dataset'])==26
    assert all(n['status']=='open' for n in nodes if n['kind'] in ('gate','goal'))
    assert by['G-GRAV']['status']=='open'
    fp.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
    (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n')
    return g

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
    result=attach(ap.parse_args().root)
    print('PASS Cartan nonlinear physical smoothing',result['version'],len(result['nodes']),len(result['edges']),'continuum gates OPEN')
