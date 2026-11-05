#!/usr/bin/env python3
"""Public-facing mathematical-physics ontology and explicit cubic-to-quasicrystal bridges.
Run AFTER source-faithful hierarchy. Stable original Library asset IDs/sha256 remain intact.
Not a proof of a continuum mass gap.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

def blob_sha(content: bytes)->str:
    return hashlib.sha1(f'blob {len(content)}\0'.encode()+content).hexdigest()

def extend(root: Path):
    root=Path(root);path=root/'knowledge-graph.json';g=json.loads(path.read_text())
    if g['version']=='v2.29': return g
    assert g['version']=='v2.28-draft',g['version']
    nodes=g['nodes'];edges=g['edges'];by={n['id']:n for n in nodes}
    rename={'D-DISS':'D-SPECTRAL-SOURCES','PUB-DISS':'PUB-THEOREM-REVIEW',
            'PAPER-1':'S-SPECTRAL-DIMENSION','PAPER-2':'S-CUT-PROJECT-ZETA',
            'PAPER-3':'S-COMPLEX-STRUCTURE','PAPER-4':'S-CONFORMAL-SPECTRAL',
            'PAPER-5':'S-FIBONACCI-CAVITY'}
    for n in nodes:
        if n['id'] in rename:n['id']=rename[n['id']]
    for e in edges:
        e['from_id']=rename.get(e['from_id'],e['from_id']);e['to_id']=rename.get(e['to_id'],e['to_id'])
    by={n['id']:n for n in nodes}
    # Titles are physics concepts, with source PDF identity retained only as provenance.
    topics={
      'S-SPECTRAL-DIMENSION':('Spectral dimension flow on Fibonacci and Penrose graphs',
        'Study heat-kernel return probabilities, local spectral measures and scale-dependent effective dimension on aperiodic graphs.',
        'The graph Laplacian is not yet a demonstrated gravitational fluctuation operator. Computed spectral flow is finite-model evidence only.'),
      'S-CUT-PROJECT-ZETA':('Cut-and-project geometry, spectral zeta and complex dimensions',
        'Compare spectral zeta functions of explicitly defined quasiperiodic and periodic operators; distinguish finite regularized ratios from ultraviolet finiteness.',
        'An approximately 16.7% reported regularized contrast is not derived from the 2+1D SU(2) Stage26 correlators and does not prove gravitational finiteness.'),
      'S-COMPLEX-STRUCTURE':('Almost-complex structure J and complementary geometry',
        'Investigate J²=−I and real/imaginary decompositions of cut-and-project spaces as mathematically precise kinematic structures.',
        'A decomposition or complex structure by itself supplies no interacting Lorentz-covariant dynamics.'),
      'S-CONFORMAL-SPECTRAL':('Conformal boundary, spectral regularization and vacuum energy',
        'Test boundary geometry, spectral-triple regularization and cutoff dependence of quantum effective actions.',
        'Finite zeta-regularized quantities do not imply finite gravitational path-integral measures or UV-complete dynamics.'),
      'S-FIBONACCI-CAVITY':('Fibonacci quasiperiodic cavity and field-response model',
        'Source material proposes an additional quasiperiodic cavity/field-response mechanism; operator and physical scope require independent verification.',
        'Indexed background, not a source-certified interacting gauge or gravitational theorem.')}
    for id,(title,summary,detail) in topics.items():
        n=by[id];n.update(title=title,summary=summary,detail=detail,tags=['spectral-physics','hypothesis','source-archive'])
        # Existing v2.28 generator unintentionally aliased source lists, appending Stage26 runner to all PDF nodes.
        # Keep only audit source for these conceptual topic records; runtime sources remain on Stage26 interface.
        n['sources']=[x for x in n['sources'] if 'P0_MODEL_HIERARCHY' in x.get('path','')]
    by['D-SPECTRAL-SOURCES'].update(title='Foundational aperiodic spectral-geometry sources',
        summary='Archived source studies: graph spectral dimension, zeta functions, complex structure, boundary regularization and quasiperiodic response.',
        detail='The original source archive is cryptographically identified in the evidence manifest. Titles here name mathematical objects, not chapters or authors.')
    by['PUB-THEOREM-REVIEW'].update(title='Independent mathematical theorem synthesis',kind='work',status='open',
        summary='Integrate source-verified lemmas into a referee-checkable mathematical proof with each model and limit declared.',
        detail='Publication readiness is an independent audit obligation, not a prerequisite inferred from the number of indexed source files.')
    by['G-GRAV'].update(title='Quasicrystalline ultraviolet quantum-gravity problem',
        summary='Does a physically correct cut-and-project spectral/gravitational operator yield a controlled ultraviolet interacting quantum-gravity theory?',
        detail='Finite graph spectral measures or regularized zeta ratios cannot by themselves establish a gravitational functional integral or quantum dynamics.',
        tags=['penrose','quasiperiodic','quantum-gravity'])
    by['M-Z5'].update(title='Coupled ℤ⁵ · proposed three-spatial-dimensional geometry',
        summary='A five-integer-coordinate cut-and-project structure with a compact/complementary direction is proposed; no authenticated refining 3D SU(2) spatial model is yet established.')
    by['M-PENROSE-2D'].update(title='Penrose P3 quasicrystalline spatial graph',
        detail='Compare the graph Laplacian, spectral-zeta operator, physical SU(2) Wilson action and proposed gravity fluctuation operator as distinct operators until explicit identification is proved.')
    by['M-SQUARE-2D'].update(summary='Area-matched periodic 2D spatial control: 151×151 square torus against the scale-55 Penrose model-set torus in 2+1D SU(2) Monte Carlo.',
        detail='Total physical area was matched in the generator; graph spectra, local operators, independent random streams and continuum limits were not automatically matched.')
    by['P0'].update(summary='Model-indexed P0 geometry and source identity: Penrose physical hypothesis, square/cubic controls and explicit action/observable comparison certificates.',
        detail='No cubic finite result closes the quasicrystalline 3D regulator interface. Neither the YM nor quantum-gravity continuum objective is proved.')
    by['P0']['checks'][0]['note']='Different spectral operators were proposed on Penrose geometry; exact source- and operator-equivalence is still open.'
    by['P0']['checks'][2]['note']='A compact complementary coordinate is only a proposed kinematic interpretation, not a genuine 3D refining gauge complex.'
    by['I-PENROSE-SQUARE'].update(summary='Define the same physical observable and appropriately matched normalization on Penrose and square 2+1D SU(2) ensembles; separately compare graph spectral-zeta operators.',
        detail='The reported zeta-ratio contrast belongs to a graph spectral calculation, not the Stage26 scalar Monte Carlo. Both require their own controls and uncertainty treatment.')
    by['I-PENROSE-SQUARE']['checks'][1]['label']='Distinguish graph spectral-zeta from 2+1D Wilson-loop/scalar operators'
    by['W-ORIGINAL-SOURCES'].update(summary='Authenticate the Stage26 SU(2) generator/dependency stack and independently identify the graph Laplacian and zeta-function calculation.',
        detail='Archived Stage26 code is located; its source_sha256 is the input checkpoint checksum, not a code hash. The spectral-zeta and Yang–Mills observables are different.')
    by['FILE-19'].update(title='Primary aperiodic spectral-geometry source archive',
        summary='Five archived technical studies and supplementary research material, SHA-256 verified.',
        detail='Original filename and immutable SHA-256 remain in asset metadata; this node is provenance rather than a theorem.',tags=['spectral-source','archive'])
    for n in nodes:
        if n['kind']=='dataset' and n['asset']['kind']=='transcript':
            i=n['id'].split('-')[-1]
            n['title']=f'Research correspondence and corrections · source {int(i)-19}'
            n['summary']='Archived research-context record; no theorem follows without independent proposition-level proof.'
            n['detail']='Original filename, byte length, checksum and Library location are available as provenance metadata.'
    for n in nodes:
        if n['id']=='R-P0-HK':n['summary']='Fixed-grid cubic SU(2) temporal heat-kernel/spatial Wilson transfer; does not give a 4D continuum vacuum or universality theorem.'
    report_path='docs/research/YM_CUBIC_PENROSE_TRANSFER_AND_INFRARED_GATES_2026-11-05.md'
    check_path='docs/evidence/YM_CUBIC_PENROSE_GATE_CHECKS_2026-11-05.json'
    rep_path=root.parent/report_path
    if not rep_path.is_file():raise FileNotFoundError(rep_path)
    docsha=blob_sha(rep_path.read_bytes())
    repo='https://github.com/syncgravity/singular-boundary/blob/'
    source_report=[dict(title='Cubic–quasicrystal operator and gap-transfer contract',path=report_path,git_blob_sha=docsha,url=repo+docsha+'/'+report_path)]
    def chk(label,state='open',note=''):return {'label':label,'state':state,'note':note}
    def add(id,title,kind,status,stage=None,summary='',detail='',checks=None,tags=None,importance=3,core=False,sources=None):
        assert id not in by,id
        row=dict(id=id,title=title,kind=kind,status=status,stage=stage,summary=summary,detail=detail,
                 checks=checks or [],sources=sources or source_report,tags=tags or [],importance=importance,core=core,route=None)
        by[id]=row;nodes.append(row)
    def edge(a,b,kind,label='',status='open'):
        assert a in by and b in by,(a,b)
        if not any(x['from_id']==a and x['to_id']==b and x['kind']==kind for x in edges):
            edges.append(dict(from_id=a,to_id=b,kind=kind,label=label,status=status))
    # Existing exact finite theorem, explicitly not a UV/continuum theorem.
    exact_path='research/theorems/R3_CUBICAL_SU2_FULL_PHYSICAL_STRONG_COUPLING_GAP_2026-10-31.md'
    cubic_sha='44d749965dd28521697b8779de2743e3bcdbcf5d'
    add('R-CUBIC-FINITE-GAP','Finite cubic SU(2) Gauss-invariant strong-coupling gap', 'result','finite','P4',
        summary='Complete finite physical Hilbert-space min–max gap certificate: Δ≥(3g₀²/2−2F/g₀²)/h; sufficient condition g₀⁴>4F/3.',
        detail='F=3n²(n+1) on the open n³ box. The sufficient threshold demands g₀ grow with n and does not reach the asymptotically free g₀(h)→0 continuum regime.',
        checks=[chk('Exact finite Gauss-invariant electric minimum 3','met','R3-IR-589'),
                chk('Uniform positive physical gap along g₀(h)→0','open','NOT implied by finite min–max bound')],
        tags=['cubic','finite','minmax'],sources=[{'title':'R3-IR-589 full finite cubic Gauss gap','path':exact_path,'git_blob_sha':cubic_sha,'url':repo+cubic_sha+'/'+exact_path}]+source_report,importance=4,core=True)
    add('I-UV-COUPLING','Weak-bare-coupling ultraviolet regime mismatch', 'interface','open','P2',
        summary='Known cubic finite/weak-interaction gap certificates require electric-dominated parameters, while asymptotic freedom approaches g₀(h)→0 and z=4/g₀⁴→∞.',
        detail='Resolve with a new constructive large-z/renormalization mechanism. Failure of a sufficient strong-coupling estimate is NOT a no-gap theorem.',
        checks=[chk('Nonperturbative physical coupling trajectory g₀(h)','open'),
                chk('Uniform interacting estimates along that trajectory','open'),
                chk('Independent limits h→0, box size→∞ and physical t','open')],importance=5,core=True,tags=['renormalization','coupling'])
    add('T0-QC-3D','T0 · Genuine refining quasicrystalline three-space','interface','open','P0',
        summary='Construct a 3D quasicrystalline cell family with ∂∂=0, fixed physical domain, h→0 and controlled geometry, explicitly related to the chosen cut-and-project model.',
        checks=[chk('Oriented locally finite 3D incidence and topological modes'),chk('Nested or directed h→0 refinement with geometric control'),chk('Source geometry and compact-coordinate identity demonstrated')],
        tags=['Penrose','geometry'],importance=5,core=True)
    add('T1-QC-ACTION','T1 · Quasicrystalline Gauss-invariant SU(2) action','interface','open','P1',
        summary='On the T0 geometry, derive electric and magnetic forms plus reflection-positive time transfer from one physically normalized lattice gauge action.',
        checks=[chk('Gauge-covariant original-link electric form and domains'),chk('Magnetic face coefficients and Bianchi/topological modes'),chk('Positive time transfer and physical normalization')],
        tags=['Penrose','action'],importance=5,core=True)
    add('T2-OBSERVABLES','T2 · Renormalized gauge-invariant observable dictionary','interface','open','P2',
        summary='Identify a dense common family of physically supported observables and matched cube/quasicrystal regulator representatives, including renormalization and vacuum centering.',
        checks=[chk('Physical test support and renormalization definition'),chk('Model-to-model observable map with units and symmetry'),chk('Nontriviality/density conditions for continuum fields')],importance=5,core=True)
    add('T3-TIME-COMPARE','T3 · Interacting physical-time correlation comparison','interface','open','P4',
        summary='Require an interacting correlation bound with a common exponential rate e^{−Mt}, uniform in h and volume; short-time or unweighted similarity does not preserve the gap.',
        checks=[chk('Cubic interacting decay bound at true g₀(h)'),chk('Quasicrystal/cube correlation difference ≤B_F e^{−Mt}'),chk('Independence of h and spatial volume in physical units')],importance=5,core=True)
    add('T4-OS-LIMIT','T4 · Nontrivial 4D OS reconstruction on both models','interface','open','P5',
        summary='Construct nontrivial reflection-positive continuum Schwinger functions and a common physical-time interpretation; prove density of gauge-invariant created states.',
        checks=[chk('Convergence of renormalized Schwinger distributions'),chk('OS positivity, covariance, clustering and locality'),chk('Nontrivial vacuum sector and dense physical probes')],importance=5,core=True)
    add('T5-GAP-TRANSFER','T5 · Physical spectral-gap transfer to quasicrystal','interface','conditional','P5',
        summary='If T0–T4 and a common positive physical-time decay rate hold, the spectral-measure Laplace lemma gives a quasicrystalline SU(2) mass-gap lower bound.',
        detail='Conditional implication only; exponential weighted comparison is among the missing hard hypotheses. The gravitational ultraviolet problem remains independent.',
        checks=[chk('Complete T0–T4 hypotheses','open'),chk('Common M>0 for a dense OS observable family','open')],importance=5,core=True)
    add('R-LOW-ENERGY-COUNTER','Small correlation error can hide lower spectral energies','result','obstruction','P4',
        summary='C_cube(t)=e^{−Mt} and C_qc(t)=(1−η)e^{−Mt}+ηe^{−mt} differ by at most η, yet C_qc has spectral weight at m<M.',
        detail='Positive Laplace measures give an exact counterexample to transferring an infrared gap from tiny unweighted correlation error. This is a model-independent toy measure, not a Penrose gauge vacuum.',
        tags=['counterexample','infrared'],importance=4,core=True)
    add('I-QG-SPECTRAL-OP','Graph spectral zeta → physical gravitational operator','interface','open',None,
        summary='Identify the quantum gravitational fluctuation operator and measure whose ultraviolet traces are claimed to be controlled by Penrose spectral geometry.',
        checks=[chk('Prove relation of graph Laplacian and physical fluctuation operator'),chk('Specify renormalized determinant/measure and cutoff'),chk('Establish the exact UV integrability or finiteness claim')],tags=['quantum-gravity'],importance=5,core=True)
    edge('M-CUBIC','R-CUBIC-FINITE-GAP','proves-in-model','finite sufficient inequality','finite')
    edge('R-CUBIC-FINITE-GAP','I-UV-COUPLING','regime-mismatch','g₀⁴>4F/3 incompatible with g₀→0')
    edge('R-WEAK','I-UV-COUPLING','regime-mismatch','small z does not approach z→∞')
    edge('I-UV-COUPLING','W-3D-ANALYTIC','required-work','constructive large-z multiscale method')
    edge('I-UV-COUPLING','P2','blocks','uniform interacting control not established')
    edge('M-Z5','T0-QC-3D','needs-construction','genuine source-faithful 3D family')
    edge('M-PENROSE-2D','T0-QC-3D','does-not-imply','2D tiling not 3D spatial refinement')
    edge('R-CUBE','T0-QC-3D','comparison-not-identity','cubic cell refinement is a geometric control')
    edge('T0-QC-3D','T1-QC-ACTION','prerequisite','requires physical 3D cell model')
    edge('R-CUBE-H','T1-QC-ACTION','control-only','not a Penrose Hamiltonian')
    edge('R-P0-HK','T1-QC-ACTION','control-only','finite cubic transfer does not prove quasicrystal action')
    edge('T1-QC-ACTION','T2-OBSERVABLES','prerequisite','correct gauge-invariant operator algebra')
    edge('I-PENROSE-SQUARE','T2-OBSERVABLES','source-calibration','2+1D same-observable comparison is a separate test')
    edge('T2-OBSERVABLES','T3-TIME-COMPARE','prerequisite','common renormalized probes')
    edge('I-UV-COUPLING','T3-TIME-COMPARE','blocks','cubic physical decay itself unproved')
    edge('T3-TIME-COMPARE','T4-OS-LIMIT','required-not-sufficient','OS and nontriviality independent')
    edge('T4-OS-LIMIT','T5-GAP-TRANSFER','required','Hilbert space and dense probe family')
    edge('T3-TIME-COMPARE','T5-GAP-TRANSFER','conditional','common physical decay')
    edge('R-OSBRIDGE','T5-GAP-TRANSFER','lemma','spectral support from Laplace decay','conditional')
    edge('R-LOW-ENERGY-COUNTER','T3-TIME-COMPARE','warns','unweighted correlation closeness insufficient','obstruction')
    edge('T5-GAP-TRANSFER','THEOREM','would-imply','quasicrystal YM mass gap if nontrivial 4D construction exists','conditional')
    edge('S-SPECTRAL-DIMENSION','I-QG-SPECTRAL-OP','model-hypothesis','graph dimension is not physical gravity operator')
    edge('S-CUT-PROJECT-ZETA','I-QG-SPECTRAL-OP','candidate','finite regularized zeta ≠ gravitational UV finiteness')
    edge('I-QG-SPECTRAL-OP','G-GRAV','blocks','physical gravitational path-integral bridge open')
    edge('T0-QC-3D','G-GRAV','possible-input','geometry alone not gravity dynamics')
    edge('T5-GAP-TRANSFER','G-GRAV','distinct-objectives','YM gap never establishes gravity UV finiteness')
    # Clear status for the viewer. No implied full gate closure.
    assert all(n['status']=='open' for n in nodes if n['kind'] in ('goal','gate'))
    for n in nodes:
        # Replace chapter/paper-centered descriptors in *navigable* node text only.
        for k in ('title','summary','detail'):
            if isinstance(n.get(k),str):
                n[k]=re.sub(r'(?i)\bdissertation\b','source program',n[k])
                n[k]=re.sub(r'(?i)\bPaper\s*([1-5])\b',lambda m:'spectral source study '+m.group(1),n[k])
        for v in n.get('checks',[]):
            for k in ('label','note'):
                if isinstance(v.get(k),str):
                    v[k]=re.sub(r'(?i)\bdissertation\b','source program',v[k]);v[k]=re.sub(r'(?i)\bPaper\s*([1-5])\b',lambda m:'spectral source study '+m.group(1),v[k])
        n['tags']=[x for x in n.get('tags',[]) if x.lower() not in ('dissertation','paper')]
    # Keep original file name EXACT in asset and manifest for provenance integrity.
    g.update(version='v2.29',build_date='2026-11-05',git_branch='main',
             scope='Mathematical physics atlas: cubic SU(2) finite results, open continuum infrared gates, explicit quasicrystal transfer conditions, and distinct ultraviolet gravity questions. No gap theorem.',
             bridge_contract='T0–T5',user_facing_labels='physics concepts; source document identity restricted to provenance metadata')
    assert len(nodes)==len({x['id'] for x in nodes})
    assert all(e['from_id'] in by and e['to_id'] in by for e in edges)
    assert all(n['status']=='open' for n in nodes if n['kind'] in ('goal','gate'))
    assert all('dissertation' not in (n['title']+' '+n.get('summary','')+' '+n.get('detail','')).lower() for n in nodes)
    path.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
    (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n')
    return g

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent);a=ap.parse_args();j=extend(a.root)
    print('PASS',len(j['nodes']),'physics nodes;',len(j['edges']),'typed edges; all six YM gates OPEN')
