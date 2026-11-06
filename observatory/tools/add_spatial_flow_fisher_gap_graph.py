#!/usr/bin/env python3
"""Idempotent source-scoped v2.36 overlay.
Five model-qualified physics nodes; no continuum theorem gate promotion.
Requires the v2.35-draft local Wilson Fisher graph.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

SOURCE_PATH='research/theorems/R3_GAUGE_COVARIANT_SPATIAL_FLOW_AND_FISHER_GAP_OBSTRUCTION_2026-11-06.md'
SOURCE_SHA='24c44fb008adafd4a5e7df420c37c726fd241f61'
BRANCH='audit/2026-11-06-wilson-spatial-flow-fisher-gap'


def attach(root: Path):
    root=Path(root)
    p=root/'knowledge-graph.json'
    g=json.loads(p.read_text())
    if g['version']=='v2.36-draft':return g
    assert g['version']=='v2.35-draft',g['version']
    nodes=g['nodes'];edges=g['edges'];by={n['id']:n for n in nodes}
    assert len(nodes)==119 and len(edges)==245
    source={'title':'Finite gauge-equivariant spatial Wilson flow, exact SU2 density gap counterexample and observable Rayleigh test',
            'path':SOURCE_PATH,'git_blob_sha':SOURCE_SHA,
            'url':f'https://github.com/syncgravity/singular-boundary/blob/{SOURCE_SHA}/{SOURCE_PATH}'}
    def ck(label,state='open',note=''):return {'label':label,'state':state,'note':note}
    def add(id,title,kind,status,stage,summary,detail,checks,tags,importance=4):
        assert id not in by,id
        n={'id':id,'title':title,'kind':kind,'status':status,'stage':stage,
           'summary':summary,'detail':detail,'checks':checks,'sources':[source],
           'tags':tags,'importance':importance,'core':False,'route':None}
        nodes.append(n);by[id]=n
    def edge(a,b,kind,label,status='open'):
        assert a in by and b in by,(a,b)
        assert not any(e['from_id']==a and e['to_id']==b and e['kind']==kind for e in edges)
        edges.append({'from_id':a,'to_id':b,'kind':kind,'label':label,'status':status})
    add('R-SU2-FISHER-GAP-COUNTER',
        'SU(2) Fisher and Wilson variance do not imply a spectral gap',
        'result','obstruction','P4',
        'Exact smooth positive class-rotor countermodel: uniformly bounded Fisher H1≤3/4 and nonzero fundamental trace variance≥1, yet the positive weighted class-sector spectral gap ≤epsilon→0.',
        'Density rho_e=(x²+epsilon²)/(1/4+epsilon²), x=tr(U)/2; an explicit smooth class potential gives a genuine positive SU2 rotor. This is NOT the cubic Wilson magnetic Hamiltonian, and is NOT a counterexample to YM mass gap.',
        [ck('Analytic Haar SU2 trace moments, variance and Fisher bound','met','Exact class density'),
         ck('Smooth positive finite class rotor with gap upper bound epsilon','met','Explicit Rayleigh test and ground-state potential'),
         ck('Transfer low-gap example to cubic Wilson vacuum','open','No such transfer or claim; different potential')],
        ['SU2','class-rotor','counterexample','Fisher','infrared'],5)
    add('R-GROUP-HEAT-WILSON-NOGO',
        'Single-holonomy heat smoothing leaves normalized fundamental Wilson trace unchanged',
        'result','finite','P2',
        'SU2 group heat convolution multiplies chi1 by e^(−3s/4); centering and variance normalization cancel the factor exactly at every finite s.',
        'Convolution of the observed probability density can supply a uniform noise-smoothed law, but that is an auxiliary random readout and cannot replace the interacting physical-time Wilson observable.',
        [ck('Exact Peter–Weyl character eigenvalue','met','Casimir chi1=3/4'),
         ck('Normalized deterministic observable invariant under group heat smearing','met','Any interacting loop marginal with nonzero variance'),
         ck('Physical gauge-field and time smoothing equivalence','open','Group readout heat smoothing is a different operation')],
        ['SU2','group-heat','no-go','normalization'])
    add('R-CUBIC-SPATIAL-WILSON-FLOW',
        'Finite gauge-equivariant spatial Wilson flow with factorial locality',
        'result','finite','P2',
        'Full 3D original-link spatial Wilson-action gradient flow exists and is gauge-equivariant; ||Hess S||≤4, ||D Phi_s||≤e^(4s), and exterior influence decays by a Poisson factorial tail at fixed lattice flow time.',
        'A true gauge-field observable, unlike independent heat noise. The bound is volume-independent for fixed s but is NOT uniform at fixed physical radius s=t_phys/h²; this is only 3D spatial flow, not 4D quantum Wilson flow.',
        [ck('SU2 cubical 3D link incidence and exact gauge covariance','met','Finite open cubical complex'),
         ck('Uniform-in-volume Hessian and Poisson-distance influence bound','met','Four distinct links per face; each link degree≤4'),
         ck('Uniform bound at physical flow time s=t_phys/h²','open','Naive e^(4s) estimate degenerates')],
        ['cubic','SU2','Wilson-flow','quasilocal','finite'],5)
    add('I-FLOWED-WILSON-DIRICHLET',
        'Physical-time spectral first moment as a covariance–Dirichlet matrix quotient',
        'interface','conditional','P2',
        'For any finite smooth gauge-invariant flowed Wilson family, −C_a′(0)=alpha_h(aᵀG_h a)/(aᵀS_h a), with S interacting covariance and G electric-gradient Dirichlet matrix.',
        'An h-uniform bound on this quotient would give UV first-moment tightness for the selected normalized states; it neither excludes soft energies nor establishes the interacting full Schur form or 4D OS theory.',
        [ck('Finite ground-state-transform Dirichlet identity','met','Exact matrix quotient'),
         ck('Uniform interacting covariance and Dirichlet comparison','open','Unknown true Wilson vacuum at weak bare coupling'),
         ck('Physical time and nontrivial continuum field','open','Not supplied by initial-time tightness')],
        ['cubic','gauge-invariant','Dirichlet','physical-time','conditional'],5)
    add('W-PHYSICAL-FLOWED-SCHUR',
        'Uniform physical-radius gauge-flowed Wilson fields and complete Schur dynamics',
        'work','open','P2',
        'Construct genuine physically normalized gauge-invariant flowed or smeared Wilson fields across h→h/2, with nonzero variance, uniform interacting covariance/Dirichlet bounds and full energy-dependent Schur/long-time estimates.',
        'The finite 3D spatial flow is only a candidate. Physical flow time scales like t_phys/h², and current factorial locality and e^(8s) derivative bounds are not uniform; positive spectral exclusion and OS reconstruction remain open.',
        [ck('Source-compatible 4D gauge-field flow and fixed physical support'),
         ck('Nontrivial renormalized interacted vacuum covariance and initial moments'),
         ck('Complete shorted Schur form / connected long-physical-time comparison uniform in h,R'),
         ck('Nontrivial 4D OS and quasicrystal transfer')],
        ['cubic','SU2','renormalization','physical-flow','open'],5)
    edge('R-LOCAL-WILSON-FISHER','R-SU2-FISHER-GAP-COUNTER','logical-obstruction',
         'Even a uniform local Fisher bound need not imply a gap','obstruction')
    edge('R-SU2-FISHER-GAP-COUNTER','P4','does-not-imply',
         'Positive local variance and static regularity cannot exclude low energy','obstruction')
    edge('R-WILSON-FIXED-LOOP-MOMENT','R-GROUP-HEAT-WILSON-NOGO','invariant-under-noise',
         'Group heat multiplier cancels in normalized Wilson first moment','finite')
    edge('R-GROUP-HEAT-WILSON-NOGO','W-PHYSICAL-FLOWED-SCHUR','different-operation',
         'Single-holonomy group heat noise does not construct physical gauge flow','open')
    edge('M-CUBIC','R-CUBIC-SPATIAL-WILSON-FLOW','source-model',
         'Finite full 3D spatial cubic Wilson functional','finite')
    edge('R-CUBIC-SPATIAL-WILSON-FLOW','I-FLOWED-WILSON-DIRICHLET','candidate',
         'Gauge-equivariant flowed test observables exist at each finite regulator','finite')
    edge('I-FLOWED-WILSON-DIRICHLET','W-PHYSICAL-FLOWED-SCHUR','open-uniform-test',
         'True covariance/Dirichlet estimates unknown along weak-bare-coupling refinements','open')
    edge('W-PHYSICAL-FLOWED-SCHUR','T2-OBSERVABLES','open-renormalized-bridge',
         'A physical observable dictionary and nontrivial continuum field are missing','open')
    edge('W-PHYSICAL-FLOWED-SCHUR','T3-TIME-COMPARE','open-long-time-dynamics',
         'Complete Schur and infrared time-correlation estimates remain open','open')
    edge('R-CUBIC-SPATIAL-WILSON-FLOW','T0-QC-3D','model-transfer-missing',
         'A real 3D quasicrystalline gauge-field flow needs its own geometry','open')
    edge('R-GROUP-HEAT-WILSON-NOGO','I-FLOWED-WILSON-DIRICHLET','scope-guard',
         'Noise scalar and full 3D flowed observable are different','finite')
    edge('I-FLOWED-WILSON-DIRICHLET','R-WILSON-THERMO-SUBSEQ','sufficient-for-uv-tightness',
         'Uniform first moment gives subsequential high-energy tightness, not IR gap','conditional')
    edge('W-STATE-SCHUR-UNIFORM','W-PHYSICAL-FLOWED-SCHUR','source-obligation',
         'Physical vacuum shorted form is still required','open')
    edge('I-UV-COUPLING','W-PHYSICAL-FLOWED-SCHUR','asymptotic-freedom-interface',
         'Current fixed lattice-flow-time bounds degenerate at fixed physical radius','open')
    edge('R-SU2-FISHER-GAP-COUNTER','W-UV-UNIFORM-LOCAL-WILSON','necessary-warning',
         'Static UV regularity alone cannot provide spectral exclusion','obstruction')
    g.update(version='v2.36-draft',git_branch=BRANCH,build_date='2026-11-06 (UTC)',
         scope='Finite gauge-equivariant spatial Wilson flow, covariance/Dirichlet test, heat noise no-go and exact SU2 Fisher-gap counterexample; continuum YM/Penrose/gravity remain OPEN.')
    assert len(nodes)==124 and len(edges)==260
    assert len({x['id'] for x in nodes})==124
    assert len([x for x in nodes if x['kind']=='dataset'])==26
    assert all(n['status']=='open' for n in nodes if n['kind'] in ('goal','gate'))
    p.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
    (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n')
    return g

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
    g=attach(a.parse_args().root)
    print('PASS finite Wilson-flow/Fisher-gap graph',len(g['nodes']),'nodes',len(g['edges']),'edges; YM gates OPEN')
