#!/usr/bin/env python3
"""Idempotent v2.30 -> v2.31 finite Wilson shell and coarse-time memory overlay.
DOES NOT certify P0-P5 or quasicrystal transfer/continuum theorems.
"""
from pathlib import Path
import argparse
import json

PATH='research/theorems/R3_FULL_WILSON_3D_SHELL_AND_TEMPORAL_MEMORY_2026-11-06.md'
BLOB='b77b6f704edc1fb95b3ecfdf056836426fb0145a'
REPO='https://github.com/syncgravity/singular-boundary/blob/'


def attach(root: Path):
    root=Path(root)
    p=root/'knowledge-graph.json'
    g=json.loads(p.read_text(encoding='utf-8'))
    if g['version']=='v2.31-draft':return g
    assert g['version']=='v2.30-draft',g['version']
    nodes=g['nodes'];edges=g['edges'];by={n['id']:n for n in nodes}
    assert len(nodes)==103 and len(edges)==194
    source={'title':'Full SU2 Wilson exponential, 3D cap and positive temporal memory',
            'path':PATH,'git_blob_sha':BLOB,'url':REPO+BLOB+'/'+PATH}
    def chk(label,state='open',note=''):
        return {'label':label,'state':state,'note':note}
    def add(id,title,kind,status,stage,summary,detail,checks,tags):
        assert id not in by
        n={'id':id,'title':title,'kind':kind,'status':status,'stage':stage,
           'summary':summary,'detail':detail,'checks':checks,
           'sources':[source],'tags':tags,'importance':4,'core':False,'route':None}
        nodes.append(n);by[id]=n
    add('R-WILSON-EXP-SHELL','Full Wilson-exponential 3D shell character cap','result','finite','P2',
        'Normalized full SU2 Wilson exponential on the 2x2x1 cubic slab: four exact five-face cap kernels, all-order bottom coupling, and a uniform explicit remainder from shell supports >=8.',
        'The first shell Taylor coefficient is (d/db + 4a0\'/a0)Z_planar/16. The same five-face support generates a seventh-order correction: its full series must be retained. Spatial Haar integration is not a closed physical-time transfer; this is a finite model calculation.',
        [chk('Exact spin-n SU2 cap convolution','met','Coefficient (a_n(s)/a0(s))^5/(n+1)^4'),
         chk('Uniform bound on higher shell supports','met','exp(8|b|) times sum k=8..16 C(16,k) [2(exp(2|s|)-1)]^k'),
         chk('Weak-bare-coupling h->0 interacting bound','open','No scale/volume uniform estimate')],
        ['cubic','SU2','full-Wilson','finite'])
    add('R-TEMPORAL-MEMORY','Positive two-step memory under spatial Haar compression','result','finite','P2',
        'At fixed 3D cubic regulator, the full Wilson potential and heat-kernel transfer satisfy P T² P-(P T P)²=P T (1-P) T P>=0; on 1 the leading memory is epsilon² F beta_h²/4.',
        'For 20 faces, F beta_h²/4=5 beta_h². Strict Jensen gives <1,T_eps 1>>exp(-eps F beta_h) for each eps>0. This is a finite temporal-blocking obstruction, not a physical continuum infrared gap or divergence theorem.',
        [chk('Same-regulator full Wilson plus positive time transfer','met','Finite symmetric heat-kernel construction'),
         chk('Exact positive two-step memory operator','met','P T Q T P=(Q T P)* (Q T P)'),
         chk('Interacting multiscale influence-kernel estimates','open','Physical-time long-distance dynamics remain unproved')],
        ['cubic','SU2','finite-time','renormalization'])

    nxt=by['W-3D-WILSON-TIME']
    nxt['summary']='Finite Wilson-exponential 3D shell and one/two-step temporal memory have now been derived. Required next: a gauge-invariant multiscale influence kernel and uniform interacting connected-time correlations.'
    nxt['detail']='Static exponential cap integration cannot be iterated as a Markovian coarse time transfer: P T² P-(P T P)²=PT(1-P)TP is positive. Retain full unresolved temporal memory, higher-spin channels and correctly renormalized physical observables.'
    nxt['checks']=[chk('Full Wilson exponential spatial first-shell character analysis','met','Finite 2x2x1 result only'),
                   chk('Positive physical-time transfer and exact first memory term','partial','Finite original-link model; no two-scale bound'),
                   chk('Uniform interacting physical-time transfer/correlations','open','Continuum P2-P4 not closed')]
    def link(a,b,kind,label,status):
        assert a in by and b in by
        assert not any(e['from_id']==a and e['to_id']==b and e['kind']==kind for e in edges)
        edges.append({'from_id':a,'to_id':b,'kind':kind,'label':label,'status':status})
    link('R-CUBIC-3D-SHELL','R-WILSON-EXP-SHELL','action-upgrade','truncated character to full Wilson exponential (finite only)','finite')
    link('R-WILSON-EXP-SHELL','R-TEMPORAL-MEMORY','same-regulator','spatial Wilson action coupled to heat-kernel temporal transfer','finite')
    link('R-P0-HK','R-TEMPORAL-MEMORY','positive-physical-time','source-qualified finite heat-kernel transfer','finite')
    link('R-TEMPORAL-MEMORY','W-3D-WILSON-TIME','unsolved-memory-control','bound the two-time influence kernel across spatial refinements','open')
    link('W-3D-WILSON-TIME','T3-TIME-COMPARE','open-interacting-infrared','uniform physical-time connected correlations remain open','open')
    link('R-WILSON-EXP-SHELL','T2-OBSERVABLES','scoped-coarse-character-evidence','no renormalized continuum dictionary','finite')
    assert len(nodes)==105 and len(edges)==200
    assert all(n['status']=='open' for n in nodes if n['kind'] in ('goal','gate'))
    assert len([n for n in nodes if n['kind']=='dataset'])==26
    g['version']='v2.31-draft'
    g['build_date']='2026-11-06 (UTC)'
    g['git_branch']='audit/2026-11-06-full-wilson-time-memory'
    p.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
    return g

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent);a=p.parse_args()
    g=attach(a.root)
    print('Full Wilson/temporal memory overlay verified:',len(g['nodes']),'nodes',len(g['edges']),'edges; six YM gates open')
