#!/usr/bin/env python3
"""Idempotent, provenance-pinned finite two-scale P/Q influence overlay.

Input: v2.31-draft; output v2.32-draft. Never promotes P0--P5 gate states.
"""
from __future__ import annotations
import json
from pathlib import Path

REPORT='research/theorems/R3_EXACT_TWO_TIME_INFLUENCE_AND_DYADIC_SCALING_2026-11-06.md'
SOURCE_SHA='fa21e892ba3ad4989564360195e45453c1ca98e0'
BRANCH='audit/2026-11-06-two-scale-influence-kernel'


def attach(root:Path):
    root=Path(root);p=root/'knowledge-graph.json';g=json.loads(p.read_text(encoding='utf8'))
    if g['version']=='v2.32-draft':return g
    assert g['version']=='v2.31-draft',f'unexpected source version: {g["version"]}'
    nodes=g['nodes'];edges=g['edges'];by={n['id']:n for n in nodes}
    source={'title':'Exact cubic SU2 non-Markovian P/Q influence and same-region dyadic comparison',
        'path':REPORT,'git_blob_sha':SOURCE_SHA,
        'url':'https://github.com/syncgravity/singular-boundary/blob/'+SOURCE_SHA+'/'+REPORT}
    def chk(label,state='open',note=''):return {'label':label,'state':state,'note':note}
    def add(id,title,kind,status,stage,summary,detail,checks,tags,importance=4):
        assert id not in by,id
        n={'id':id,'title':title,'kind':kind,'status':status,'stage':stage,
           'summary':summary,'detail':detail,'checks':checks,'sources':[source],
           'tags':tags,'importance':importance,'core':False,'route':None}
        nodes.append(n);by[id]=n
    add('R-TWO-TIME-INFLUENCE','Exact continuous and discrete SU(2) two-time influence kernel',
        'result','finite','P2',
        'Full Wilson/Kogut–Susskind cubic P/Q decomposition yields exact non-Markovian Volterra evolution and a positive Feshbach self-energy; B*B=(beta² F/4)P holds on the full retained boundary space.',
        'At each fixed 3D lattice, the eliminated Q sector has memory B*exp(-tD)B and resolvent B*(D+z)^-1 B, while symmetric positive transfer has an all-step convolution recurrence. Memory itself decays with bare electric rate, but full physical gap remains unproved.',
        [chk('Gauge-invariant retained eight-link holonomy-product algebra','met','Coarse and refined spatial meshes use identical physical boundary products'),
         chk('Sharp all-coarse-state offdiagonal magnetic coupling','met','SU2 Haar orthogonality across all cubical faces'),
         chk('Exact Volterra, Feshbach and positive discrete transfer memory','met','Finite self-adjoint original-link Hamiltonian'),
         chk('Renormalized physical-time infrared exclusion','open','Finite bare memory estimates do not control the full Schur complement')],
        ['cubic','SU2','finite-influence','physical-time'])
    add('R-DYADIC-BARE-MEMORY','Two genuine cubic refinements: bare influence growth and resolvent bounds',
        'result','finite','P2',
        'On the same 2h×2h×h spatial slab, 20 plaquettes at mesh h become 128 at h/2; eight original coarse boundary holonomies are retained via fine-link products. Bare zero-time memory ratio equals (128/5)[g0(h)/g0(h/2)]^4.',
        'Sharp operator identity on the matched physical boundary space and interacting vacuum self-energy resolvent sandwich. Raw influence strength is not scale-invariant; this is NOT a renormalized divergence or a mass-gap counterexample.',
        [chk('Exact 20/128 face and 33/170 edge geometry with equal physical region','met'),
         chk('All distinct face pair orthogonality; 190 and 8128 tests','met'),
         chk('Analytic two-scale bare self-energy and full-Wilson finite resolvent bounds','met'),
         chk('Small or summably weighted physical two-scale difference','open','Existing bare triangle inequality is not small along weak-bare-coupling refinement')],
        ['cubic','SU2','dyadic-refinement','finite'])
    add('W-RENORMALIZED-INFLUENCE','Renormalized gauge-invariant influence/Schur complement across scales',
        'work','open','P2',
        'Replace bare Haar boundary projection with a physically normalized renormalized observable/effective-action dictionary and prove a summable interacting physical-time or low-energy resolvent comparison.',
        'The exact finite memory and raw dyadic ratio form a compulsory regression criterion. The large bare coefficient must be treated with running couplings, counterterms, nonlinear recoupling, and vacuum-centering; no uniform physical estimate has been proved.',
        [chk('Source-derived gauge-invariant observable map at fixed physical support'),
         chk('Higher-spin and all-time influence channels under genuine spatial refinement'),
         chk('Summable long-physical-time connected-correlation or resolvent discrepancy'),
         chk('Nontrivial 4D OS reconstruction and dense spectral probes')],
        ['renormalization','SU2','influence-kernel','open'],5)
    def link(a,b,kind,label,status='open'):
        assert a in by and b in by,(a,b)
        if not any(e['from_id']==a and e['to_id']==b and e['kind']==kind for e in edges):
            edges.append({'from_id':a,'to_id':b,'kind':kind,'label':label,'status':status})
    link('R-TEMPORAL-MEMORY','R-TWO-TIME-INFLUENCE','exact-extension','two-step memory becomes an all-time kernel','finite')
    link('R-TWO-TIME-INFLUENCE','R-DYADIC-BARE-MEMORY','two-scale-comparison','same eight physical boundary holonomies','finite')
    link('M-CUBIC','R-DYADIC-BARE-MEMORY','source-model','genuine 3D dyadic control','finite')
    link('R-TWO-TIME-INFLUENCE','W-RENORMALIZED-INFLUENCE','required-interface','bare influence not yet physically renormalized','open')
    link('R-DYADIC-BARE-MEMORY','W-RENORMALIZED-INFLUENCE','quantitative-warning','bare coefficient growth requires scale-dependent control','open')
    link('W-RENORMALIZED-INFLUENCE','W-3D-WILSON-TIME','next-mathematical-step','full physical-time influence beyond one slab','open')
    link('W-RENORMALIZED-INFLUENCE','T3-TIME-COMPARE','open-infrared-interface','uniform physical-time connected comparison missing','open')
    link('R-TWO-TIME-INFLUENCE','T2-OBSERVABLES','scoped-evidence','physical renormalized observable dictionary still open','finite')
    g['version']='v2.32-draft';g['build_date']='2026-11-06 (UTC)';g['git_branch']=BRANCH
    assert len(nodes)==108 and len(edges)==208,(len(nodes),len(edges))
    assert len([n for n in nodes if n['kind']=='dataset'])==26
    assert all(n['status']=='open' for n in nodes if n['kind'] in ('gate','goal'))
    assert all(e['from_id'] in by and e['to_id'] in by for e in edges)
    p.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf8')
    return g

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
    j=attach(ap.parse_args().root);print('PASS',j['version'],len(j['nodes']),'nodes',len(j['edges']),'edges; all continuum gates OPEN')
