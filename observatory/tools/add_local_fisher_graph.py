#!/usr/bin/env python3
"""Idempotent v2.35 scope overlay: volume-independent finite-coupling SU2 local Fisher lemma.
Do NOT promote any continuum YM or quantum gravity gate. Requires earlier v2.34 overlay.
"""
from pathlib import Path
import argparse, json

SOURCE_PATH='research/theorems/R3_LOCAL_INTERACTING_SU2_FISHER_AND_THERMODYNAMIC_SUBSEQUENCE_2026-11-06.md'
SOURCE_SHA='b6e7fc69c8f8f48fd74efaf95d1662bf73168a02'
BRANCH='audit/2026-11-06-local-wilson-fisher-thermodynamic'


def attach(root: Path):
    root=Path(root);p=root/'knowledge-graph.json';g=json.loads(p.read_text())
    if g['version']=='v2.35-draft':return g
    assert g['version']=='v2.34-draft',g['version']
    n=g['nodes'];e=g['edges'];by={x['id']:x for x in n}
    assert len(n)==115 and len(e)==231
    source={'title':'Gap-independent local Wilson vacuum Fisher and fixed-spacing thermodynamic subsequence',
            'path':SOURCE_PATH,'git_blob_sha':SOURCE_SHA,
            'url':f'https://github.com/syncgravity/singular-boundary/blob/{SOURCE_SHA}/{SOURCE_PATH}'}
    def ck(label,state='open',note=''):return {'label':label,'state':state,'note':note}
    def add(id,title,kind,status,stage,summary,detail,checks,tags,importance=4):
        assert id not in by,id
        x={'id':id,'title':title,'kind':kind,'status':status,'stage':stage,
           'summary':summary,'detail':detail,'checks':checks,'sources':[source],
           'tags':tags,'importance':importance,'core':False,'route':None}
        n.append(x);by[id]=x
    def edge(a,b,kind,label,status='open'):
        assert a in by and b in by,(a,b)
        assert not any(z['from_id']==a and z['to_id']==b and z['kind']==kind for z in e)
        e.append({'from_id':a,'to_id':b,'kind':kind,'label':label,'status':status})
    add('R-LOCAL-LINK-ENERGY','Gap-independent local SU(2) link kinetic energy bound',
        'result','finite','P2',
        'For every finite original-link cubic SU(2) Wilson vacuum, alpha Σ_{e in S}∫|∇eΩ|²≤beta·#plaquettes touching S; one link has degree ≤4 independent of the box.',
        'Exact variational one-link excision/partial Haar trial. No source response or spectral gap used. The estimate is volume-independent at fixed g0, but beta/alpha=4/g0^4 grows in the weak-coupling ultraviolet.',
        [ck('Open 3D cubic boundary incidence degree ≤4','met'),
         ck('Haar-link removal variational identity for the full interacting vacuum','met'),
         ck('Uniform control as g0(h)→0','open','Upper bound scales as g0^-4')],
        ['SU2','cubic','finite','local-energy','gap-free'],5)
    add('R-LOCAL-WILSON-FISHER','Volume-independent interacting Wilson-holonomy Fisher bound',
        'result','finite','P2',
        'For any simple physical Wilson loop, ∫SU2 |∇sqrtρ_C|²≤16/g0^4 and Fisher(ρ_C)≤64/g0^4, independent of total volume and elementary contour length. Positive trace variance ≥π²/[64 CS³(1+16/g0^4)³].',
        'The conditional Haar disintegration permits selecting any one original loop edge; its holonomy map is a bi-invariant SU2 isometry. Sobolev on fixed SU2 and exact Haar trace semicircle law give volume-uniform anti-concentration. No pointwise local Harnack or uniform weak-g0 limit is proved.',
        [ck('True interacting-vacuum loop marginal H1/Fisher estimate','met','Volume-independent for each fixed g0'),
         ck('Quantified trace variance lower bound from SU2 Sobolev','met','Fixed SU2 geometric constant CS'),
         ck('Weak-bare-coupling pointwise marginal ratio bound','open','H1 does not imply L∞ pointwise control on SU2')],
        ['SU2','cubic','finite','Fisher','local-variance'],5)
    add('R-WILSON-THERMO-SUBSEQ','Local Wilson state and spectral-measure subsequences at fixed mesh',
        'result','finite','P2',
        'At fixed h,g0 and fixed physical loop, interacting Wilson marginals have L1-convergent subsequences as box size tends to infinity, and normalized local spectral measures are tight with finite first moment.',
        'Rellich compactness of sqrtρ in H1(SU2), volume-independent positive Wilson variance, and a uniform first-spectral-moment bound imply subsequential nontrivial local states and correlations. This does not prove unique thermodynamic vacuum, positive IR gap or h→0 existence.',
        [ck('Thermodynamic subsequence of fixed-h Wilson marginal','met','Strong L1 from compact embedding'),
         ck('Volume-uniform fixed-h local spectral first moment and tightness','met','High-energy tail ≤M_h,C/S'),
         ck('Unique infinite-volume vacuum and uniform h→0 physical gap','open','Requires interacting scale-volume limits')],
        ['SU2','cubic','finite','thermodynamic-subsequence'],4)
    add('W-UV-UNIFORM-LOCAL-WILSON','Weak-coupling uniform local Wilson and Schur-form renormalization',
        'work','open','P2',
        'Turn the fixed-coupling volume-independent H1/Fisher bounds into renormalized estimates uniform along g0(h)→0, with stable gauge-invariant smeared observables and the entire interacting time-dependent Schur complement.',
        'Locality removes the global E/F factor, but the proven g0^-4 Fisher bound and its variance consequence degrade in the asymptotically free regime; no physical IR spectral exclusion or Penrose action follows.',
        [ck('Source-derived physical smearing or renormalization of fixed-size Wilson observable'),
         ck('Scale-uniform interacting local marginal/score control without assuming a gap'),
         ck('Complete interacting Schur/connected-time bound in physical units'),
         ck('Nontrivial 4D OS reconstruction and dense physical spectral probes')],
        ['SU2','cubic','renormalization','open'],5)

    work=by['W-LOCAL-MARGINAL-UV']
    assert work['status']=='open'
    work['summary']='A genuine volume-independent, gap-free SU2 Wilson H1/Fisher and trace-variance bound is now proved at fixed bare coupling; pointwise local Harnack, UV-uniform renormalized states and full physical-time Schur comparison remain OPEN.'
    work['checks'][0]['state']='partial'
    work['checks'][0]['note']='The finite true-vacuum local Fisher and trace-variance estimates are independent of volume, but do not prove a uniform pointwise Harnack, adjacent-scale marginal ratio or g0→0 bound.'
    work['detail']='A new source-qualified variational link-excision lemma removes all-volume E/F dependence at fixed g0 and supplies subsequential fixed-h local vacuum/spectral compactness. The bound still grows like g0^-4 and does not compare the complete time-dependent effective operator.'

    edge('M-CUBIC','R-LOCAL-LINK-ENERGY','source-model','full original-link cubical SU2 Wilson regulator','finite')
    edge('R-VACUUM-WEIGHTED-BLOCK','R-LOCAL-LINK-ENERGY','true-vacuum-input','uses actual interacting positive ground state','finite')
    edge('R-LOCAL-LINK-ENERGY','R-LOCAL-WILSON-FISHER','conditional-isometry','one local link controls whole physical-loop marginal','finite')
    edge('R-WILSON-MARGINAL-HARNACK','R-LOCAL-WILSON-FISHER','local-improvement','replaces global volume-dependent bound by local H1, not local pointwise Harnack','finite')
    edge('R-LOCAL-WILSON-FISHER','R-WILSON-THERMO-SUBSEQ','compactness','fixed-h Rellich and uniform variance','finite')
    edge('R-WILSON-FIXED-LOOP-MOMENT','R-WILSON-THERMO-SUBSEQ','short-time-bound','uniform first moment at fixed h and physical contour','finite')
    edge('R-LOCAL-WILSON-FISHER','T2-OBSERVABLES','finite-physical-observable','local marginal not a continuum renormalized field','finite')
    edge('R-WILSON-THERMO-SUBSEQ','T3-TIME-COMPARE','insufficient-for-ir','fixed-h subsequential spectral tightness excludes no soft energy','open')
    edge('R-LOCAL-WILSON-FISHER','W-UV-UNIFORM-LOCAL-WILSON','weak-coupling-limit','Fisher bound degrades as g0^-4','open')
    edge('W-UV-UNIFORM-LOCAL-WILSON','P2','critical-interacting-obligation','scale-uniform renormalization missing','open')
    edge('W-UV-UNIFORM-LOCAL-WILSON','W-LOCAL-MARGINAL-UV','refines-source','local bound exists but UV control open','open')
    edge('W-UV-UNIFORM-LOCAL-WILSON','T3-TIME-COMPARE','open-physical-time','complete Schur influence and decay missing','open')
    edge('R-WILSON-THERMO-SUBSEQ','T4-OS-LIMIT','fixed-mesh-not-4d','thermodynamic subsequence not a 4D continuum OS reconstruction','open')
    edge('R-LOCAL-WILSON-FISHER','I-UV-COUPLING','bare-g0-degradation','bound scales as g0^-4 as g0→0','open')

    g.update(version='v2.35-draft',git_branch=BRANCH,build_date='2026-11-06 (UTC)',
             scope='Exact finite-volume-independent local Wilson Fisher and fixed-h thermodynamic subsequence; UV-uniform interacting Yang–Mills gap and gravity remain OPEN.')
    assert len(n)==119 and len(e)==245 and len({x['id'] for x in n})==119
    assert len([x for x in n if x['kind']=='dataset'])==26
    assert all(x['status']=='open' for x in n if x['kind'] in ('goal','gate'))
    p.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
    (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n')
    return g


if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
    g=attach(a.parse_args().root)
    print('PASS local Fisher source overlay',len(g['nodes']),'nodes',len(g['edges']),'edges, all continuum gates OPEN')
