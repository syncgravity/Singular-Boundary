#!/usr/bin/env python3
"""Reproducible finite SU2 vacuum Harnack/spectral sum rule overlay.
Input v2.33-draft, output v2.34-draft. All continuum gates remain OPEN.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

SOURCE='research/theorems/R3_FINITE_WILSON_MARGINAL_HARNACK_AND_TWO_SCALE_SUM_RULE_2026-11-06.md'
SOURCE_SHA='0252ebfd73b2e9870717393be5fcd5114bb8cf0f'
BRANCH='audit/2026-11-06-marginal-harnack-loop-sumrule'


def attach(root:Path):
    root=Path(root);p=root/'knowledge-graph.json';g=json.loads(p.read_text(encoding='utf-8'))
    if g['version']=='v2.34-draft':return g
    assert g['version']=='v2.33-draft',f'Unexpected input: {g["version"]}'
    nodes=g['nodes'];edges=g['edges'];by={n['id']:n for n in nodes}
    src={'title':'Finite SU2 vacuum marginal bound, fixed-physical Wilson moment and source-response circularity',
         'path':SOURCE,'git_blob_sha':SOURCE_SHA,
         'url':'https://github.com/syncgravity/singular-boundary/blob/'+SOURCE_SHA+'/'+SOURCE}
    def chk(label,state='open',note=''):return {'label':label,'state':state,'note':note}
    def add(id,title,kind,status,stage,summary,detail,checks,tags,importance=4):
        assert id not in by,id
        obj={'id':id,'title':title,'kind':kind,'status':status,'stage':stage,
             'summary':summary,'detail':detail,'checks':checks,'sources':[src],
             'tags':tags,'importance':importance,'core':False,'route':None}
        nodes.append(obj);by[id]=obj
    add('R-WILSON-MARGINAL-HARNACK',
        'Finite interacting SU(2) vacuum marginal Harnack certificate',
        'result','finite','P2',
        'For the genuine finite cubic Wilson vacuum Ω² dHaar, every coarse-loop marginal obeys exp(−2Λ)≤ρ≤exp(2Λ), Λ=64F/g₀⁴+E log(101/99). Positive Wilson variance is explicit.',
        'The proof uses SU2 heat-kernel Peter–Weyl tails and Feynman–Kac positivity. Λ grows with the entire lattice and inverse bare coupling; this is NOT a uniform local-marginal or ultraviolet estimate.',
        [chk('Finite SU2 heat-kernel uniform minorization at time αt=8','met','δ8<0.01 from explicit character-series bound'),
         chk('Real interacting vacuum marginal pointwise bounds','met','Feynman–Kac; depends on all E and F'),
         chk('Finite normalized Wilson loop variance certificate','met','Variance ≥exp(−2Λ)'),
         chk('Volume/mesh independent local-marginal Harnack','open','Global bound grows as exp(O(F/g₀⁴))')],
        ['SU2','cubic','finite','ground-state','marginal'],5)
    add('R-WILSON-FIXED-LOOP-MOMENT',
        'Physical Wilson loop: exact first spectral moment on every cubic refinement',
        'result','finite','P4',
        'For a simple loop of L distinct original links, −C′(0)=α L Eρ(1−W²/4)/Varρ(W). On fixed physical perimeter ℓ, α L=g₀²ℓ/(2h²).',
        'The formula is an ultraviolet spectral sum rule, not infrared exclusion. A positive spectral toy measure exhibits diverging first moment with a fixed positive gap.',
        [chk('Original-link gradient/Casimir identity','met','|∇χfund|²=1−χfund²/4'),
         chk('Same physical contour has twice as many fine edges','met','Unit-square perimeter 4: L=4n'),
         chk('First moment controls the physical infrared mass gap','open','False in general: high-energy spectral tail counterexample')],
        ['SU2','cubic','finite','ultraviolet','moment'],4)
    add('I-WILSON-STATIC-TIME-NORM',
        'Conditional two-scale marginal matching versus physical-time normalization',
        'interface','conditional','P2',
        'If |log(ρf/ρc)|≤δ on the same physical loop, its unsmeared normalized first-moment ratio lies in k exp(±2δ), k=4 g₀(h/2)²/g₀(h)².',
        'This is conditional on an unproved ratio bound. With slowly running bare coupling and δ small, the raw initial-slope ratio tends toward four; matching static laws does not supply a common physical-time renormalized observable.',
        [chk('Source-certified common physical-loop holonomy dictionary','met','Fine holonomy is ordered product, not a new loop'),
         chk('True interacting relative-marginal log ratio δ uniformly small','open','Not obtained for cubic Wilson ground states'),
         chk('Renormalized/smeared physical-time loop observable','open','Raw first spectral moments need not converge')],
        ['SU2','cubic','comparison','conditional'],5)
    add('W-LOCAL-MARGINAL-UV',
        'Noncircular local marginal and renormalized Wilson–Schur estimates',
        'work','open','P2',
        'Replace the global Ω Harnack estimate by a boundary-local volume-uniform estimate; construct a renormalized gauge-invariant loop and control the entire energy-dependent Schur form across refinements.',
        'A bounded-source response estimate ||∂θ sqrtρ||≤sqrt Var(F)/Δ depends on the finite interacting gap Δ, so assuming it uniform to prove the same gap is circular. Seek a localized, source-independent estimate along the actual g₀(h) and R→∞.',
        [chk('Volume-independent local conditional-marginal estimate without a gap assumption'),
         chk('Physical-time normalization for a nontrivial smeared Wilson observable'),
         chk('Uniform conditional-score variance and full shorted Schur comparison'),
         chk('Nontrivial 4D OS continuum and dense physical probes')],
        ['SU2','cubic','renormalization','open','noncircular'],5)
    # Preserve parent gate/status; annotate the scope of the existing open work only.
    work=by['W-STATE-SCHUR-UNIFORM']
    work['checks'][1]['note']='An explicit global Harnack bound for ρ now exists, but grows with F/g₀⁴ and E; a local uniform score/Schur estimate remains OPEN.'
    def edge(a,b,kind,label,status='open'):
        assert a in by and b in by,(a,b)
        assert not any(x['from_id']==a and x['to_id']==b and x['kind']==kind for x in edges)
        edges.append({'from_id':a,'to_id':b,'kind':kind,'label':label,'status':status})
    edge('R-VACUUM-WEIGHTED-BLOCK','R-WILSON-MARGINAL-HARNACK','finite-quantification','actual Ω² local marginal is bounded nonuniformly','finite')
    edge('M-CUBIC','R-WILSON-MARGINAL-HARNACK','source-model','original-link 3D cubic SU2 Wilson','finite')
    edge('R-WILSON-MARGINAL-HARNACK','R-WILSON-FIXED-LOOP-MOMENT','quantified-variance','variance strictly positive at finite regulator','finite')
    edge('R-WILSON-FIXED-LOOP-MOMENT','I-WILSON-STATIC-TIME-NORM','conditional-two-scale','factor four from diffusion and edge counts','conditional')
    edge('I-WILSON-STATIC-TIME-NORM','W-LOCAL-MARGINAL-UV','requires-renormalization','raw Wilson first moment not physically time-matched','open')
    edge('R-WILSON-MARGINAL-HARNACK','W-LOCAL-MARGINAL-UV','nonuniform-bound','global exp(F/g₀⁴) loses volume/UV control','open')
    edge('W-STATE-SCHUR-UNIFORM','W-LOCAL-MARGINAL-UV','refines-open-gate','noncircular local estimate still needed','open')
    edge('W-LOCAL-MARGINAL-UV','T2-OBSERVABLES','open-physical-probe','smearing/renormalization and density missing','open')
    edge('W-LOCAL-MARGINAL-UV','T3-TIME-COMPARE','open-dynamics','complete Schur/long-time comparison missing','open')
    edge('R-WILSON-FIXED-LOOP-MOMENT','P4','uv-not-ir','high spectral first moment does not prove mass gap','open')
    edge('W-LOCAL-MARGINAL-UV','P2','missing-uniform-interaction','physical continuum interacting estimates remain OPEN','open')
    edge('R-WILSON-MARGINAL-HARNACK','I-UV-COUPLING','weak-coupling-degradation','Harnack constant grows as g₀^−4','open')
    edge('I-WILSON-STATIC-TIME-NORM','T2-OBSERVABLES','renormalized-dictionary','marginal match alone insufficient for physical time','open')
    g['version']='v2.34-draft';g['build_date']='2026-11-06 (UTC)';g['git_branch']=BRANCH
    assert len(nodes)==115 and len(edges)==231,(len(nodes),len(edges))
    assert len([n for n in nodes if n['kind']=='dataset'])==26
    assert all(n['status']=='open' for n in nodes if n['kind'] in ('gate','goal'))
    assert all(e['from_id'] in by and e['to_id'] in by for e in edges)
    p.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
    (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n')
    return g

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
    g=attach(a.parse_args().root);print('PASS',g['version'],len(g['nodes']),'physics nodes,',len(g['edges']),'typed edges; six YM gates OPEN')
