#!/usr/bin/env python3
"""Idempotent, source-pinned finite true-vacuum conditional RG overlay.

Input v2.32-draft; output v2.33-draft. No continuum gates are closed.
"""
from __future__ import annotations
import json
from pathlib import Path

SOURCE='research/theorems/R3_VACUUM_WEIGHTED_OBSERVABLE_MAP_AND_SCHUR_FORM_2026-11-06.md'
SOURCE_SHA='06e22ced09c9e6cdb9ebb091ef03a3c80f9492ae'
BRANCH='audit/2026-11-06-vacuum-weighted-schur-form'


def attach(root: Path):
    root=Path(root);p=root/'knowledge-graph.json';g=json.loads(p.read_text(encoding='utf8'))
    if g['version']=='v2.33-draft':return g
    assert g['version']=='v2.32-draft',f'Unexpected input: {g["version"]}'
    nodes=g['nodes'];edges=g['edges'];by={n['id']:n for n in nodes}
    source={'title':'Finite interacting-vacuum SU2 conditional projection and energy-dependent Schur form',
            'path':SOURCE,'git_blob_sha':SOURCE_SHA,
            'url':'https://github.com/syncgravity/singular-boundary/blob/'+SOURCE_SHA+'/'+SOURCE}
    def chk(label,state='open',note=''):return {'label':label,'state':state,'note':note}
    def add(id,title,kind,status,stage,summary,detail,checks,tags,importance=4):
        assert id not in by,id
        row={'id':id,'title':title,'kind':kind,'status':status,'stage':stage,
             'summary':summary,'detail':detail,'checks':checks,'sources':[source],
             'tags':tags,'importance':importance,'core':False,'route':None}
        nodes.append(row);by[id]=row
    add('R-VACUUM-WEIGHTED-BLOCK',
        'Interacting-vacuum SU(2) conditional observable and Schur form',
        'result','finite','P2',
        'Each finite cubic Wilson Hamiltonian has a strictly positive gauge-invariant ground state. Ω²-weighted conditional expectation preserves the vacuum, defines an exact fixed-physical-support Wilson observable and induces a weighted coarse diffusion plus full variational Schur form.',
        'Unlike bare Haar P/Q projection, true-vacuum offdiagonal mixing vanishes on 1; on other coarse excitations it is exactly four times a conditional variance of the vacuum logarithmic score. Coarse kinetic weight is a=mα; the entire time-dependent Schur form still requires renormalized scale comparison.',
        [chk('Finite positive SU2 Wilson ground state and gauge covariance','met','Compact product-group ellipticity and positivity-improving semigroup'),
         chk('Vacuum-weighted local cylinder algebra and normalized loop','met','Ω² conditional isometry, positive coarse marginal and finite positive variance'),
         chk('Exact induced diffusion, conditional score variance and shorted form','met','All identities finite-regulator; unbounded block coupling treated at form level'),
         chk('State density and full energy-dependent form uniform along h,R','open','Unknown interacting vacuum and physical-time renormalization')],
        ['SU2','cubic','ground-state','finite','Schur-form'],5)
    add('R-SU2-STATIC-TIME-COUNTER',
        'Exact SU(2) gauge-loop example: identical coarse law, distinct time dynamics',
        'result','finite','P2',
        'A one-vertex/two-loop SU2 gauge graph has the same coarse Haar character law and projected generator as a free coarse rotor, but a nonzero eliminated-sector memory and strictly different positive-time Wilson correlations.',
        'Ground density exp(κχ(A)) with gauge-invariant character potential; the exact memory norm is α²κ² G(κ)/4, G(κ) a positive Bessel-character expression. This is NOT the cubic Wilson action; it falsifies inference from static matching or first-time derivatives to full dynamics.',
        [chk('Finite gauge-invariant two-loop ground state','met','Ωκ=e^(κχ(A)/2)/sqrt(a0κ)'),
         chk('Exact positive memory norm and strict time-correlation inequality','met','SU2 character/Bessel integration; independent finite numerical regression'),
         chk('Extend to physical cubic Wilson ensemble','open','Toy graph is an obstruction to a shortcut, not a 3D result')],
        ['SU2','counterexample','two-time','finite'],4)
    add('W-STATE-SCHUR-UNIFORM',
        'Renormalized interacting marginal and full Schur-form comparison',
        'work','open','P2',
        'Estimate the actual cubic vacuum marginals ρh,R, induced potentials vh,R, conditional logarithmic-score variance and full shorted forms at fixed physical support across h→h/2.',
        'Static marginal or Markovian generator convergence cannot replace interacting long-time control. A valid gap-transfer estimate must include eliminated-sector memory and be uniform in mesh and spatial volume along physical running coupling.',
        [chk('Uniform positivity/nontriviality of normalized physical Wilson variance'),
         chk('State-marginal, logarithmic-score and induced-potential control'),
         chk('Physical-time or energy-dependent full Schur comparison with summable errors'),
         chk('Nontrivial 4D OS continuum reconstruction and dense infrared probes')],
        ['SU2','renormalization','Schur-form','open'],5)
    # Update only subchecks; never alter gate status.
    old=by['W-RENORMALIZED-INFLUENCE'];old['checks'][0]['state']='partial'
    old['checks'][0]['note']='Finite Ω²-weighted gauge-invariant GNS/normalized Wilson candidate constructed; unknown uniform vacuum marginal, scale map and continuum limit.'
    t2=by['T2-OBSERVABLES']
    if t2['checks'][0]['state']=='open':
        t2['checks'][0]['state']='partial'
        t2['checks'][0]['note']='Finite fixed-support interacting Wilson normalization exists; continuum renormalization, density and nontrivial limit remain open.'
    def link(a,b,kind,label,status='open'):
        assert a in by and b in by,(a,b)
        if not any(e['from_id']==a and e['to_id']==b and e['kind']==kind for e in edges):
            edges.append({'from_id':a,'to_id':b,'kind':kind,'label':label,'status':status})
    link('R-TWO-TIME-INFLUENCE','R-VACUUM-WEIGHTED-BLOCK','projection-upgrade','Bare Haar projection replaced by true-vacuum conditional law','finite')
    link('M-CUBIC','R-VACUUM-WEIGHTED-BLOCK','finite-physical-model','Same full Wilson original-link SU2 slab','finite')
    link('R-DYADIC-BARE-MEMORY','R-VACUUM-WEIGHTED-BLOCK','projection-dependence','Bare memory strength is not vacuum-dressed invariant','finite')
    link('R-VACUUM-WEIGHTED-BLOCK','T2-OBSERVABLES','finite-observable-candidate','Local Wilson normalization; continuum still open','finite')
    link('R-VACUUM-WEIGHTED-BLOCK','R-SU2-STATIC-TIME-COUNTER','counterexample','Static marginal and compressed generator do not fix time dynamics','finite')
    link('R-SU2-STATIC-TIME-COUNTER','W-STATE-SCHUR-UNIFORM','necessary-interface','Must bound eliminated-sector time memory','open')
    link('R-VACUUM-WEIGHTED-BLOCK','W-STATE-SCHUR-UNIFORM','required-uniformity','Unknown marginal score and shorted form','open')
    link('W-STATE-SCHUR-UNIFORM','W-RENORMALIZED-INFLUENCE','refines-open-task','Vacuum/physical observable correction to bare influence','open')
    link('W-STATE-SCHUR-UNIFORM','T3-TIME-COMPARE','open-infrared-obligation','Physical long-time scale-uniform exclusion missing','open')
    link('W-STATE-SCHUR-UNIFORM','P2','open-proof-obligation','No uniform interacting weak-coupling estimates','open')
    g['version']='v2.33-draft';g['build_date']='2026-11-06 (UTC)';g['git_branch']=BRANCH
    assert len(nodes)==111 and len(edges)==218,(len(nodes),len(edges))
    assert len([x for x in nodes if x['kind']=='dataset'])==26
    assert all(x['status']=='open' for x in nodes if x['kind'] in ('gate','goal'))
    assert all(e['from_id'] in by and e['to_id'] in by for e in edges)
    p.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
    (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n')
    return g

if __name__=='__main__':
    import argparse
    a=argparse.ArgumentParser();a.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
    g=attach(a.parse_args().root);print('PASS',g['version'],len(g['nodes']),'nodes',len(g['edges']),'links; all continuum gates OPEN')
