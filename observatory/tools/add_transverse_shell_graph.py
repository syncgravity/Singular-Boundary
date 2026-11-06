#!/usr/bin/env python3
"""Idempotent scoped finite 3D SU2 transverse-shell additions to Observatory v2.29.
This adds research/next-step records, not a continuum theorem or certified gate closure.
"""
from pathlib import Path
import json

REPORT='research/theorems/R3_CUBIC_FIRST_TRANSVERSE_SHELL_CHARACTER_BLOCK_2026-11-06.md'
BLOB='a7d5f05a60847042c9bc0702078a88789d22728d'
REPO='https://github.com/syncgravity/singular-boundary/blob/'

def attach(root):
    root=Path(root);p=root/'knowledge-graph.json';g=json.loads(p.read_text(encoding='utf-8'))
    if g['version']=='v2.30-draft':return g
    assert g['version']=='v2.29',g['version']
    nodes=g['nodes'];edges=g['edges'];by={x['id']:x for x in nodes}
    assert all(x in by for x in ('M-CUBIC','R-P0-HK','P2','T2-OBSERVABLES'))
    source={'title':'Finite 3D cubical transverse-shell Haar/blocking audit', 'path':REPORT,
            'git_blob_sha':BLOB,'url':REPO+BLOB+'/'+REPORT}
    def check(label,state='open',note=''):return {'label':label,'state':state,'note':note}
    def add(id,title,kind,status,stage,summary,detail,checks,importance=4):
        assert id not in by
        n={'id':id,'title':title,'kind':kind,'status':status,'stage':stage,'summary':summary,'detail':detail,
           'checks':checks,'sources':[source],'tags':['cubic','SU2','finite-shell'],'importance':importance,'core':False,'route':None}
        nodes.append(n);by[id]=n
    add('R-CUBIC-3D-SHELL','Finite 3D SU(2) transverse plaquette shell', 'result','finite','P2',
        'Exact positive truncated-plaquette 2×2×1 spatial slab: 20 faces and 25 integrated links; first transverse Wilson correction λ⁸χ₁/32, vacuum cube term λ⁶/4 and exact adjoint λ¹⁶/16384.',
        'This is a finite spatial polynomial-weight character calculation, not the full Wilson exponential, heat-kernel physical-time dynamics, uniform interacting renormalization or a continuum mass gap. 2^20 face selections were exhaustively checked; remaining amplitudes bounded by an explicit sup-norm remainder.',
        [check('Parity geometry and finite SU(2) character factors','met','32 admissible subsets; embedded disk/sphere Schur coefficients and truncated-action positivity checked'),
         check('Uniform correction to normalized 3D block at fixed |λ|<1/2','met','Analytical finite-block sup-norm remainder bound'),
         check('Physical Wilson exponential and Euclidean-time interaction','open','Requires higher-spin recoupling and temporal heat-kernel transfer'),
         check('Uniform h→0 and box-size infrared estimate','open','Physical continuum problem remains open')])
    add('W-3D-WILSON-TIME','3D Wilson exponential and physical-time block transfer','work','open','P2',
        'Repeat the transverse-shell comparison with the full SU(2) Wilson exponential plus temporal heat-kernel transfer; establish real physical-time connected-correlation bounds.',
        'The polynomial λ-character model demonstrates transverse channels but does not reproduce the physical weak-bare-coupling continuum. Retain spin intertwiners and define renormalized observables before comparing h→h/2.',
        [check('Full Wilson exponential character expansion and 3D shell integration'),
         check('Same-action time transfer, gauge-invariant probes and vacuum centering'),
         check('Volume/refinement-uniform interacting physical-time comparison')],importance=5)
    def edge(a,b,kind,label,status):
        assert a in by and b in by
        if not any(x['from_id']==a and x['to_id']==b and x['kind']==kind for x in edges):
            edges.append({'from_id':a,'to_id':b,'kind':kind,'label':label,'status':status})
    edge('M-CUBIC','R-CUBIC-3D-SHELL','finite-model-evidence','spatial 3D cubical control only','finite')
    edge('R-P0-HK','R-CUBIC-3D-SHELL','different-action','temporal heat kernel vs polynomial spatial weight; not interchangeable','open')
    edge('R-CUBIC-3D-SHELL','W-3D-WILSON-TIME','next-required-interface','full 3D Wilson exponential and physical-time dynamics remain open','open')
    edge('W-3D-WILSON-TIME','P2','open-proof-obligation','uniform interacting infrared bound not established','open')
    edge('R-CUBIC-3D-SHELL','T2-OBSERVABLES','scoped-evidence','finite coarse character evidence, no continuum dictionary','finite')
    assert all(n['status']=='open' for n in nodes if n['kind'] in ('goal','gate'))
    assert len(nodes)==103 and len(edges)==194
    g['version']='v2.30-draft';g['git_branch']='audit/2026-11-06-cubic-transverse-shell'
    g['build_date']='2026-11-06 (UTC)'
    p.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
    return g

if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent);a=ap.parse_args();g=attach(a.root)
 print('finite 3D shell attached:',len(g['nodes']),'nodes,',len(g['edges']),'edges; 6 YM gates OPEN')
