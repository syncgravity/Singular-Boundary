#!/usr/bin/env python3
"""Scoped v2.37 graph overlay: flat-field physical-time curvature heat control,
periodic Fourier comparison, isolated-plaquette nonlinear warning.
No P0-P5 / Penrose / gravity gate closure.
"""
from pathlib import Path
import argparse, json

SOURCE_PATH='research/theorems/R3_FIXED_PHYSICAL_RADIUS_LINEARIZED_CUBIC_FLOW_2026-11-05.md'
SOURCE_SHA='c7d2384ba72e4c8ad2f18a8b1b99f15c949cd1af'
BRANCH='audit/2026-11-05-physical-radius-linearized-cubic-flow'


def attach(root:Path):
    root=Path(root);p=root/'knowledge-graph.json';g=json.loads(p.read_text())
    if g['version']=='v2.37-draft':return g
    assert g['version']=='v2.36-draft',g['version']
    n=g['nodes'];edges=g['edges'];by={x['id']:x for x in n}
    assert len(n)==124 and len(edges)==260
    source={'title':'Exact flat-field cubic physical flow and nonlinear isolated-plaquette countercheck',
            'path':SOURCE_PATH,'git_blob_sha':SOURCE_SHA,
            'url':f'https://github.com/syncgravity/singular-boundary/blob/{SOURCE_SHA}/{SOURCE_PATH}'}
    def chk(label,state='open',note=''):return {'label':label,'state':state,'note':note}
    def add(id,title,kind,status,stage,summary,detail,checks,tags,importance=4):
        assert id not in by,id
        x=dict(id=id,title=title,kind=kind,status=status,stage=stage,summary=summary,
            detail=detail,checks=checks,sources=[source],tags=tags,importance=importance,core=False,route=None)
        n.append(x);by[id]=x
    def link(a,b,kind,label,status='open'):
        assert a in by and b in by,(a,b)
        assert not any(z['from_id']==a and z['to_id']==b and z['kind']==kind for z in edges)
        edges.append(dict(from_id=a,to_id=b,kind=kind,label=label,status=status))

    add('R-LINEAR-CUBIC-PHYSFLOW',
        'Flat-field SU(2) cubical curvature heat flow at fixed physical radius',
        'result','finite','P2',
        'Exact linearization of spatial Wilson link-gradient flow gives F_h(tau)=exp[-tau d1 d1*/(4h²)]F_h(0). Its curvature heat smoothing bounds are uniform in mesh and open-box volume for every fixed tau>0.',
        'Three independent su(2) colors and original-link oriented d1,d0 with d1d0=0. The quadratic curvature energy h³||F||² is linearized-gauge invariant; the result does not control nonlinear commutators, interacting-vacuum probability or quantum physical-time correlations.',
        [chk('Flat-connection Wilson Hessian equals (d1*d1)/4','met','Exact finite Lie-algebra quadratic term'),
         chk('Uniform h,R linearized physical-curvature smoothing','met','Spectral theorem for positive d1d1*/h²'),
         chk('Nonlinear gauge-covariant physical-radius flow bound','open','Cannot inherit a linearized spectral estimate automatically')],
        ['SU2','cubic','linearized','finite','fixed-physical-flow'],5)
    add('R-PERIODIC-FLOW-FOURIER',
        'Periodic cubic Fourier control: O(h²) physical-flow multiplier error',
        'result','finite','P2',
        'For fixed nonzero transverse Fourier modes, lambda_h=4h^-2 sum_j sin²(pi k_j h), with zero-to-continuum discrepancy at most (4pi⁴h²/3)sum_j k_j⁴; physical heat multipliers converge at O(h²).',
        'This is a separate periodic, flat-field, linearized reference. Zero/longitudinal gauge modes are not the transverse curvature branch. It is not a periodic-to-Penrose, interacting-cubic, or physical 4D quantum-field universality theorem.',
        [chk('Exact periodic cubical curl/Hodge Fourier symbol','met'),
         chk('Rigorous fixed-mode O(h²) eigen/multiplier errors','met'),
         chk('Uniform nonlinear interacting measure over all modes','open','Modewise convergence is not Schwinger-function convergence')],
        ['cubic','periodic','Fourier','linearized','finite'],4)
    add('R-NONLINEAR-PLAQUETTE-FLOW-ESCAPE',
        'Nonlinear isolated plaquette: normalized flowed trace escapes to ultraviolet',
        'result','obstruction','P2',
        'One exact SU2 four-link plaquette under Haar/free-electric vacuum has Var(x_s)~4sqrt2 epsilon^(3/2), Dirichlet~sqrt2 epsilon^(1/2)/4, epsilon=1-tanh(s); normalized first moment~alpha/(4epsilon), and positive-time correlations vanish as s grows.',
        'Only an isolated four-link spatial gradient-flow control, not a fixed-physical-size loop, interacting cubic Wilson vacuum, or Yang–Mills counterexample. Shows that deterministic over-flow plus variance normalization can generate rare-event UV spectral escape despite unit variance.',
        [chk('Exact nonlinear SU2 isolated-plaquette flow and Haar endpoint asymptotics','met'),
         chk('Normalized Haar free-electric positive-time correlation collapses','met','Weak L²→0 and compact heat semigroup, not interacting vacuum'),
         chk('Behavior of actual cubic Wilson ground state at fixed physical flow radius','open','Unknown')],
        ['SU2','nonlinear','Haar','counterexample','physical-time'],4)
    add('W-NONLINEAR-PHYS-RADIUS',
        'Nonlinear fixed-physical-radius Wilson field and full interacting Schur criterion',
        'work','open','P2',
        'Upgrade the uniform flat-field 3D smoothing to physical 4D gauge-covariant flow and nontrivial true-vacuum covariance, then control complete interacting physical-time shorted forms across h→0 and spatial volume.',
        'Required: source-defined 4D regulator, nonlinear curvature estimates stable at s=tau/h², gauge-covariant observable dictionary at fixed physical support, nonvanishing renormalized variance, and long-time/energy-dependent Schur and OS continuum limits. A tight UV spectral moment does not exclude infrared soft states.',
        [chk('Full nonlinear gauge curvature/tangent estimate uniform at fixed physical radius'),
         chk('Nonzero renormalized true-vacuum covariance of fixed-support 4D flowed Wilson field'),
         chk('Complete Schur / positive-time connected estimates uniform in h,R'),
         chk('Nontrivial OS and positive physical spectral gap independently')],
        ['SU2','renormalization','open','4D-flow','Schur'],5)

    link('M-CUBIC','R-LINEAR-CUBIC-PHYSFLOW','source-model','Finite 3D open cubic linearized gauge-field control','finite')
    link('R-CUBIC-SPATIAL-WILSON-FLOW','R-LINEAR-CUBIC-PHYSFLOW','exact-flat-linearization','Physical flow heat semigroup on cubical cochains','finite')
    link('R-LINEAR-CUBIC-PHYSFLOW','R-PERIODIC-FLOW-FOURIER','boundary-control-only','Different periodic cubic reference; same flat linearization','finite')
    link('R-LINEAR-CUBIC-PHYSFLOW','W-NONLINEAR-PHYS-RADIUS','open-nonlinear-extension','Linear spectral smoothing does not bound interacting nonlinear flow','open')
    link('R-PERIODIC-FLOW-FOURIER','T2-OBSERVABLES','linear-control-only','Per-mode UV control not a renormalized interacting field','finite')
    link('R-PERIODIC-FLOW-FOURIER','T0-QC-3D','distinct-model','Periodic cubic symbols do not prove quasicrystalline three-space','open')
    link('R-GROUP-HEAT-WILSON-NOGO','R-NONLINEAR-PLAQUETTE-FLOW-ESCAPE','distinct-operations','Deterministic field flow unlike group heat measurement smoothing','finite')
    link('R-CUBIC-SPATIAL-WILSON-FLOW','R-NONLINEAR-PLAQUETTE-FLOW-ESCAPE','exact-one-plaquette-control','Large lattice flow produces rare-event normalized spectral escape','obstruction')
    link('R-NONLINEAR-PLAQUETTE-FLOW-ESCAPE','W-NONLINEAR-PHYS-RADIUS','non-uniformity-warning','Nonlinear reference has no uniform normalized positive-time control','open')
    link('R-NONLINEAR-PLAQUETTE-FLOW-ESCAPE','T3-TIME-COMPARE','cannot-transfer','Haar reference not the 3D interacting long-time theory','open')
    link('W-NONLINEAR-PHYS-RADIUS','W-PHYSICAL-FLOWED-SCHUR','refines-open-criterion','Need fixed-radius interacting covariance and full Schur dynamics','open')
    link('W-NONLINEAR-PHYS-RADIUS','T2-OBSERVABLES','observable-dictionary-open','No nontrivial 4D renormalized Wilson field','open')
    link('W-NONLINEAR-PHYS-RADIUS','T3-TIME-COMPARE','interacting-time-open','Uniform connected physical-time bound missing','open')
    link('W-NONLINEAR-PHYS-RADIUS','I-UV-COUPLING','constructive-UV-open','No asymptotically free nonlinear interacting estimate','open')
    link('W-NONLINEAR-PHYS-RADIUS','G-GRAV','distinct-scientific-goals','YM smearing does not establish gravitational UV finiteness','open')

    g.update(version='v2.37-draft',build_date='2026-11-05 (America/Denver)',git_branch=BRANCH,
      scope='Exact flat-field 3D cubic fixed-physical-radius smoothing and periodic Fourier O(h²) control; nonlinear isolated SU2 plaquette rare-event countercheck. Full nonlinear interacting 4D gap and gravity still OPEN.')
    assert len(n)==128 and len(edges)==275 and len({x['id'] for x in n})==128
    assert len([x for x in n if x['kind']=='dataset'])==26
    assert all(x['status']=='open' for x in n if x['kind'] in ('gate','goal'))
    p.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
    (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n')
    return g

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
    j=attach(ap.parse_args().root)
    print('PASS physical radius linearized overlay',j['version'],len(j['nodes']),len(j['edges']),'all P0-P5 and gravity OPEN')
