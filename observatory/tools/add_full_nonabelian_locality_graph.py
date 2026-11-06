#!/usr/bin/env python3
"""Proof Atlas v2.40-draft: exact finite nonabelian locality and OPEN signed-covariant bridge.

An executable verifier is NOT a continuum proof. The positive propagation bound
exp(3*tau/h^2) does NOT give h-uniform physical curvature regularity.
"""
from __future__ import annotations
import json,argparse
from pathlib import Path
SOURCE_PATH='research/theorems/R3_FULL_NONABELIAN_CUBIC_PLAQUETTE_INFLUENCE_AND_MAXIMUM_OBSTRUCTION_2026-11-06.md'
SOURCE_SHA='14c4d732a8678c7dc626f134cb17d26839eac75f'
BRANCH='audit/2026-11-06-full-nonabelian-locality-and-index'

def attach(root:Path):
    root=Path(root);src=root/'knowledge-graph.json';g=json.loads(src.read_text())
    if g['version']=='v2.40-draft':
        assert len(g['nodes'])==139 and len(g['edges'])==314
        return g
    assert g['version']=='v2.39-draft' and len(g['nodes'])==136 and len(g['edges'])==302
    ns=g['nodes'];es=g['edges'];by={n['id']:n for n in ns}
    source={'title':'Exact all-configuration finite SU2 cubic plaquette-influence and nonlinear maximum countercheck',
            'path':SOURCE_PATH,'git_blob_sha':SOURCE_SHA,
            'url':f'https://github.com/syncgravity/singular-boundary/blob/{SOURCE_SHA}/{SOURCE_PATH}'}
    def chk(label,state='open',note=''):return {'label':label,'state':state,'note':note}
    def add(id,title,kind,status,stage,summary,detail,checks,tags,importance=5):
        assert id not in by
        n=dict(id=id,title=title,kind=kind,status=status,stage=stage,summary=summary,
               detail=detail,checks=checks,sources=[source],tags=tags,importance=importance,core=False,route=None)
        ns.append(n);by[id]=n
    def edge(a,b,kind,label,status='open'):
        assert a in by and b in by
        assert not any(e['from_id']==a and e['to_id']==b and e['kind']==kind for e in es)
        es.append(dict(from_id=a,to_id=b,kind=kind,label=label,status=status))
    add('R-FULL-NONABELIAN-PLAQUETTE-INFLUENCE',
        'Exact all-configuration SU(2) cubic original-link plaquette influence',
        'result','finite','P2',
        'For a_p=sqrt(1-Re U_p) in full finite cubic SU2 Wilson gradient flow, D_s^+a_p <= -(2-ell_p)a_p/2 + sum_{q ne p} N_pq a_q/4. Hence a(s)<=exp(s A)a(0), ||a(s)||inf<=exp(3s)||a0||inf.',
        'N_pq counts actual shared physical links; A=N_off/4 with maximum row sum 3. Exact gauge invariant and genuinely noncommuting. At fixed physical tau=h²s, exp(3tau/h²) is NOT mesh-uniform curvature smoothing. The signed covariant cancellation needed to improve it remains OPEN.',
        [chk('Exact one-link SU2 plaquette character derivative','met','||grad_e ell_p||²=ell_p(2−ell_p)/4'),
         chk('Original-link shared incidence comparison and self-dissipation','met','True for arbitrary finite SU2 link configuration'),
         chk('Uniform physical-time h->0 curvature bound','open','Absolute-value comparison grows exponentially in tau/h²'),
         chk('Interacting Wilson-vacuum moment bound','open','Classical deterministic inequality only')],
        ['SU2','cubic','nonabelian','finite','classical','locality'])
    add('R-FULL-NONABELIAN-MAX-COUNTER',
        'Noncommuting cubic example: largest local plaquette defect initially increases',
        'result','obstruction','P2',
        'An explicitly stored reproducible finite SU2 original-link quaternion witness has a strict largest plaquette defect ell_p≈1.9147924 with initial derivative≈+0.0577442, while total Wilson action decreases.',
        'Verified numerical witness near a large class angle. This rules out an unconditional maximum principle for max_p ell_p, not a small-field theorem, physical-time quantum spectral estimate or a counterexample to Yang–Mills existence.',
        [chk('Finite analytic-force exact-differential numerical witness','met','Seed and full quaternions preserved with strict margin'),
         chk('Analytic symbolic exact-rational witness','open','Only numerical floating-point certificate with margin'),
         chk('Near-flat noncommutative maximum principle obstruction','open','Not inferred from high-angle witness')],
        ['SU2','cubic','counterexample','numerical','finite'],4)
    add('W-FULL-NONABELIAN-SIGNED-COVARIANT-HEAT',
        'Signed non-Abelian covariant curvature heat estimate through physical refinement',
        'work','open','P2',
        'Replace exp(3tau/h²) positive absolute-value locality by physical-scale covariant heat bounds retaining link transport, signed plaquette couplings, noncommutative Bianchi cancellations and interacting-vacuum state control.',
        'Requires exact discrete non-Abelian curvature transport/covariant Bochner identity and appropriately gauge-invariant quantity under genuine SU2 fluctuations, plus a source-justified weak-coupling probability/renormalization estimate. No continuum or infrared Schur closure.',
        [chk('Exact nonlinear discrete covariant curvature flow and Bianchi identity'),
         chk('h-uniform positive-physical-time non-Abelian regularity with quantified assumptions'),
         chk('Conditions verified for true interacting Wilson vacuum and nonvanishing renormalized covariance'),
         chk('Complete physical-time Schur, OS continuum and spectral gap')],
        ['SU2','cubic','nonabelian','open','physical-time','Schur'])
    edge('M-CUBIC','R-FULL-NONABELIAN-PLAQUETTE-INFLUENCE','model','Full 3D open original-link cubic SU2 configuration space','finite')
    edge('R-NONLINEAR-PHYS-ACTION','R-FULL-NONABELIAN-PLAQUETTE-INFLUENCE','same-flow','Exact nonlinear classical physical action and local defect rates','finite')
    edge('R-PLANAR-CARTAN-EMBED','R-FULL-NONABELIAN-PLAQUETTE-INFLUENCE','strict-extension-in-fields','All-configurations bound removes Cartan restriction but loses uniform physical-time smoothing','finite')
    edge('R-LINEAR-CUBIC-PHYSFLOW','R-FULL-NONABELIAN-PLAQUETTE-INFLUENCE','distinct-inference','Linear physical heat structure cannot be inferred by absolute-link bounds','finite')
    edge('R-FULL-NONABELIAN-PLAQUETTE-INFLUENCE','R-FULL-NONABELIAN-MAX-COUNTER','local-maximum-warning','Global Wilson action decay does not force individual face-monotonicity','obstruction')
    edge('R-FULL-NONABELIAN-PLAQUETTE-INFLUENCE','W-FULL-NONABELIAN-SIGNED-COVARIANT-HEAT','nonuniform-physical-time','exp(3tau/h²) fails uniform refinement control','open')
    edge('R-FULL-NONABELIAN-PLAQUETTE-INFLUENCE','W-FULL-NONABELIAN-PHYS-SMOOTHING','partial-noncommuting-control','True nonabelian finite locality, not positive-time uniform smoothing','open')
    edge('R-FULL-NONABELIAN-MAX-COUNTER','W-FULL-NONABELIAN-SIGNED-COVARIANT-HEAT','unconditional-max-principle-fails','High-angle local max grows despite total action decay','open')
    edge('W-FULL-NONABELIAN-SIGNED-COVARIANT-HEAT','W-FULL-NONABELIAN-PHYS-SMOOTHING','refines-open-criterion','Need covariant cancellations and true vacuum support','open')
    edge('W-FULL-NONABELIAN-SIGNED-COVARIANT-HEAT','T2-OBSERVABLES','nontrivial-covariance-open','Curvature transport does not supply renormalized interacting field','open')
    edge('W-FULL-NONABELIAN-SIGNED-COVARIANT-HEAT','T3-TIME-COMPARE','physical-time-open','Spatial classical flow cannot bound quantum physical-time decay','open')
    edge('W-FULL-NONABELIAN-SIGNED-COVARIANT-HEAT','G-GRAV','separate-objective','Nonabelian YM regularity does not establish gravitational UV operator','open')
    g.update(version='v2.40-draft',build_date='2026-11-06',git_branch=BRANCH,
       scope='Exact all-configuration finite noncommuting cubic SU2 plaquette influence and verified high-curvature local-max warning. The exp(3tau/h²) bound is non-uniform at physical radius; full covariant non-Abelian/quantum smoothing and P0–P5 remain OPEN.')
    assert len(ns)==139 and len(es)==314
    assert len({n['id'] for n in ns})==139 and sum(n['kind']=='dataset' for n in ns)==26
    assert all(n['status']=='open' for n in ns if n['kind'] in ('gate','goal'))
    src.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
    (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n')
    return g
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
    g=attach(a.parse_args().root)
    print('PASS',g['version'],len(g['nodes']),len(g['edges']),'all continuum gates OPEN')
