#!/usr/bin/env python3
"""Build the curated graph from explicit claim-limited records plus hashed uploads.
No simulation binaries or confidential transcript bodies enter the git graph.
"""
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE if (HERE/'data_manifest.json').exists() else HERE.parent
manifest_path=ROOT/'data_manifest.json' if (ROOT/'data_manifest.json').exists() else ROOT/'data-manifest.json'
manifest=json.loads(manifest_path.read_text())
N=[];E=[]
REPO='https://github.com/syncgravity/singular-boundary'
S={
 'dependencies':('docs/research/PROOF_DEPENDENCIES.md','eb258e0e6987ce56d8662695322e3473f77a4539'),
 'p0audit':('docs/research/REPOSITORY_REVIEW_AND_P0_OBJECTIVE_2026-11-04.md','b286ce7008c1407701eeee6fcf02faed422bd0ef'),
 'acceptance':('docs/research/HISTORICAL_RECORD_ACCEPTANCE_GATE_2026-11-01.md','336554fd07a482782757845ee1d468a67b19f40b'),
 'cubegeom':('research/theorems/R3_FIXED_DOMAIN_CUBICAL_CHAIN_REFINEMENT_2026-10-31.md','6cebf700102d575f3272de0eea5c7bf9e72eba71'),
 'cubeham':('research/theorems/R3_CUBICAL_SU2_GAUSS_HAMILTONIAN_REFERENCE_2026-10-31.md','2dd4a29a3135b6e7fa983469200850b18ec26055'),
 'transfer':('research/theorems/R3_CUBICAL_SU2_FINITE_TRANSFER_POSITIVITY_2026-10-31.md','d8c89723c6a4eb5f040b6b4540c146e2aec0a7d4'),
 'prism':('research/theorems/R3_ORIENTED_PRISM_CHAIN_AND_GAUGE_HAMILTONIAN_2026-10-31.md','734dcb8e765359cb86ff90ea19a4a69331488841'),
 'curl':('research/theorems/R3_IR_REPOSITORY_REVIEW_3D_PERIODIC_CURL_SPECTRUM_2026-11-04.md','7aab7b57028365527235b69cf3f5291221e971d8'),
 'regime':('research/theorems/R3_IR_3D_QUANTITATIVE_THRESHOLD_AND_CONTINUUM_SCALING_AUDIT_2026-11-04.md','eb5a0b349ea48970eff8d7e05ac7e798fb9fe787'),
 'history':('research/theorems/R3_IR_LINKED_CLUSTER_SUBTRACTION_PHYSICAL_OBSTRUCTION_2026-11-03.md','843777b2040aed5f1f8b56e6bc3207cbd267799c'),
 'mpo':('research/audits/P2_SOURCE_MPO_RESIDUAL_CYLINDER_DIRICHLET_2026-11-04.md','5adce9a63bc04de02533ca41692caeaa8fbffcd0'),
 'bernstein':('research/audits/P2_BERNSTEIN_SCHATTEN_THERMODYNAMIC_LOCAL_MEASURES_2026-11-04.md','611b9d1370cf73f71fca3c9c623cbb6f0d42491f'),
 'quantum':('research/audits/P2_CENTRAL_BINOMIAL_SCHATTEN_LOCALLY_NORMAL_QUANTUM_2026-11-04.md','fbf5e6dc108d38c41cfaa522c26e4971f9a5b283'),
 'discovery':('observatory/PROOF_PATH_DISCOVERY_2026-11-04.md','60e9137a5dda438662a2bc77db240b6deb5f9e6c'),
 'hktransfer':('research/audits/P0_CUBIC_HEAT_KERNEL_TRANSFER_CERTIFICATE_2026-11-04.md','9aa95ab6ee4110b4b208ad93df55fec9447201f2')
}
REF_LABELS={'dependencies':'P0–P5 proof dependencies','p0audit':'P0 source and acceptance audit','acceptance':'Historical record acceptance gate','cubegeom':'R3-IR-586 · exact cubic refinement','cubeham':'R3-IR-587 · finite cubic Gauss Hamiltonian','transfer':'R3-IR-590 · finite transfer positivity','prism':'R3-IR-562 · oriented Penrose prism candidate','curl':'3D periodic curl and Bianchi spectrum','regime':'3D asymptotic freedom regime audit','history':'Connected-history projection obstruction','mpo':'P-77/P-78 · original-link MPO and Dirichlet','bernstein':'Bernstein Schatten and thermodynamic measures','quantum':'Locally normal thermodynamic quantum state','discovery':'Source-based proof-path discovery','hktransfer':'P0 finite heat-kernel time-action certificate'}
def refs(*keys):
 return [{'title':REF_LABELS.get(k,k),'path':S[k][0],'git_blob_sha':S[k][1],'url':f'{REPO}/blob/{S[k][1]}/{S[k][0]}'} for k in keys]
def prs(number,label):return [{'title':label,'url':f'{REPO}/pull/{number}','review_only':True}]
def add(id,title,kind,status,stage=None,summary='',detail='',checks=None,sources=None,tags=None,importance=2,core=False,route=None):
 assert id not in {x['id'] for x in N},id
 N.append(dict(id=id,title=title,kind=kind,status=status,stage=stage,summary=summary,detail=detail,checks=checks or [],sources=sources or [],tags=tags or [],importance=importance,core=core,route=route))
def link(a,b,kind,label='',status='tracked'):
 E.append(dict(from_id=a,to_id=b,kind=kind,label=label,status=status))

def c(label,state,note=''):return {'label':label,'state':state,'note':note}
add('THEOREM','4D SU(2) Yang–Mills existence + positive mass gap','goal','open',summary='Target: a nontrivial OS-reconstructible four-dimensional continuum theory and a strictly positive physical spectral threshold.',detail='Not proved. The graph distinguishes a new finite theorem or algorithm from a result uniform in both spatial volume and genuine 3D refinement.',checks=[c('Certified 3D action and refinement','open'),c('Interacting infinite-volume continuum theory','open'),c('Reconstructed nontrivial physical spectrum','open'),c('A uniform positive mass threshold in physical units','open')],sources=refs('dependencies'),importance=5,core=True)

gates={
'P0':('Regulator & source identity','Source-certified 3D spatial model, refinement and consistent action',[
 c('Genuine 3D geometry, oriented incidence and h→0 on fixed domain','met','R3-IR-586 for the CUBIC benchmark only.'),
 c('Single source-derived electric, magnetic and temporal normalization','partial','A heat-kernel temporal + spatial Wilson finite transfer-action candidate is now source-specified and checked. Isotropic Wilson universality and renormalized continuum compatibility remain open.'),
 c('Gauss-law reducing domains and physical embeddings','partial','Finite cubic operator known; gauge-covariant cross-scale control unresolved.'),
 c('Specified g₀(h), physical units and source renormalization','open'),
 c('Historical coupled-ℤ⁵ ≡ chosen 3D regulator (if claimed)','blocked','Not established; equivalence optional for the separate cubic route.')]),
'P1':('Correct original-link operator','Well-defined physical Gauss-sector Hamiltonian on the chosen P0 family',[
 c('Correct finite original-link spin-network/Gauss algebra','partial','Resolved on specific strips, cubic finite reference available.'),
 c('Same-action 3D electric form, plaquette transport, adjoints','open'),
 c('Self-adjoint physical Hamiltonian and compatible time transfer','partial','Finite constructions only.'),
 c('Scale/volume-compatible operator comparison','open')]),
'P2':('Nonlinear interacting control','Actual physical interacting recurrence or equivalent constructive estimates',[
 c('Finite original-link source and representation','met','P-77 five-state MPO in 1D strip; does not transfer to 3D.'),
 c('Uniform N~m² physical Schatten-1/source response','open'),
 c('Physical 3D all-scale cluster or renormalization construction','open'),
 c('Nonlinear estimates uniform in h and volume along g₀(h)','open')]),
'P3':('Penrose vacuum-current route','Route-specific signed Wilson-current / anti-depletion estimate',[
 c('Finite signed-current/Ward identities in source model','partial'),
 c('3D Penrose cell/action identity and refinement','open'),
 c('Uniform interacting completed-cage or equivalent estimate','open'),
 c('Bridge to physical spectrum at true coupling','open')]),
'P4':('Physical infrared spectrum','Interacting source-visible spectral exclusion below Δ>0',[
 c('Positive-time finite-volume gauge-invariant kernels','partial','P-78 in the corrected 1D strip.'),
 c('All-time common interacting 3D physical dynamics','open'),
 c('Uniform decay at t in physical units, h→0 and R→∞','open'),
 c('Dense-enough physical observable coverage and vacuum isolation','open')]),
'P5':('Continuum & OS reconstruction','Nontrivial four-dimensional limit and physical spectral gap',[
 c('Consistent Schwinger functions / Euclidean measure','open'),
 c('OS positivity, tightness, reconstruction and locality','open'),
 c('Nontriviality / vacuum / physical state density','open'),
 c('Spectral support starts above common M>0','open'),
 c('Independent complete theorem review','open')])}
for id,(name,desc,checks) in gates.items():
 add(id,f'{id} · {name}','gate','open',id,summary=desc,detail='No gate is closed. Criterion states refer to precisely identified submodels and evidence—not an overall success percentage.',checks=checks,sources=refs('dependencies','p0audit') if id=='P0' else refs('dependencies'),importance=5,core=True)
 link(id,'THEOREM','required','necessary input')
for a,b in [('P0','P1'),('P0','P2'),('P0','P3'),('P0','P4'),('P0','P5'),('P1','P2'),('P1','P4'),('P2','P4'),('P4','P5')]:link(a,b,'dependency','requires compatible model')
# P3 is an optional route, not necessary to prove YM in every construction.
link('P3','P4','candidate','Penrose-specific possible mechanism','route-specific')

models=[
('M-CUBIC','Cubic 3D benchmark','partial','Genuine dyadic fixed-domain geometric subdivision; finite SU(2) reference. No continuum interacting theorem.',['P0','P1'],refs('cubegeom','cubeham')),
('M-Z5','Historical coupled ℤ⁵ Penrose','unresolved','Dissertation/archives explore coupled ℤ⁵ geometry; a compatible genuine 3D SU(2) regulator family has not been source-certified.',['P0','P3'],refs('p0audit')),
('M-PRISM','Extruded Penrose prism','candidate','Finite oriented 3D candidate is not equivalent to historical coupled ℤ⁵, and small patches are not a directed refinement.',['P0','P3'],refs('prism')),
('M-STRIP','1D face-strip SU(2) laboratory','partial','Corrected original-link interacting Hamiltonian with extensive finite/thermodynamic partial results, not the target 3D spatial regulator.',['P1','P2','P4'],refs('mpo','bernstein'))]
for mid,title,status,summary,st,sr in models:
 add(mid,title,'model',status,st[0],summary=summary,detail='Do not transfer a statement to another regulator without an explicit operator/evidence comparison.',sources=sr,importance=4,core=True,tags=st)
 link(mid,st[0],'candidate','model identity')

results=[
('R-CUBE','R3-IR-586 · exact cubical chain refinement','finite','P0','Oriented ∂∂=0, chain maps, h→0 for dyadic cube on [0,1]³; geometric-only.',refs('cubegeom'),'M-CUBIC'),
('R-CUBE-H','R3-IR-587 · cubic Gauss Hamiltonian','finite','P1','Finite Gauss-invariant Kogut–Susskind model; no renormalized continuum.',refs('cubeham'),'M-CUBIC'),
('R-TRANSFER','R3-IR-590 · finite transfer positivity','finite','P5','Positive symmetric finite-graph time transfer; not continuum OS.',refs('transfer'),'M-CUBIC'),
('R-CURL','3D periodic discrete curl spectrum','finite','P0','Exact periodic curl, cohomology and long-wavelength soft modes; quadratic tangent model.',refs('curl'),'M-CUBIC'),
('R-PRISM','R3-IR-562 · prism chain & rooted candidate','candidate','P0','Finite oriented prism ∂∂=0 and rooted gauge form; not historical ℤ⁵ derivation.',refs('prism'),'M-PRISM'),
('R-STRIP-THERMO','P-53/55 · strip thermodynamic states','finite','P2','Infinite-row energy density, locally normal subsequential states; no full common interacting dynamics.',refs('bernstein','quantum'),'M-STRIP'),
('R-MPO','P-77 · physical five-state MPO','finite','P2','Polynomial-bond approximation existence; trace-norm asymptotics and efficiency not obtained.',refs('mpo'),'M-STRIP'),
('R-DIRICHLET','P-78 · positive-energy Dirichlet form','conditional','P4','Gauge-invariant finite local cylinder first moments; nonzero first moment ≠ mass gap.',refs('mpo'),'M-STRIP'),
('R-OBSTRUCT','Disconnected physical history cannot be discarded','obstruction','P2','Exact connected-support projection fails in specified physical score; keep history.',refs('history'),'M-STRIP'),
('R-WEAK','Weak magnetic gap fails continuum coupling trajectory','obstruction','P4','Electric-dominated stability regime does not contain asymptotic freedom g₀(h)→0.',refs('regime'),'M-CUBIC'),
('R-NONINTERTWINE','Naive dyadic Hamiltonian intertwining fails','obstruction','P0','Exact electric Wilson witness and magnetic internal-curvature counterexample in separate draft audit.',prs(56,'P0 quantum non-intertwining audit'),'M-CUBIC'),
('R-FSUM','Quantitative local f-sum spectral response','conditional','P4','Positive first moment and positive mass above threshold in strip; cannot exclude near-zero excitation.',prs(55,'f-sum audit')+prs(56,'P4 spectral-weight continuation'),'M-STRIP'),
('R-OSBRIDGE','Conditional OS spectral-support lemma','conditional','P5','A common dense-family e^{-Mt} bound would exclude energies below M; its hypotheses remain open.',prs(57,'uniform theorem bridge'),'M-CUBIC'),
('R-INDEX','740 theorem paths in frozen Observatory catalog','indexed','P0','Discovery index only; most theorem bodies were not independently audited. No automatic mathematical edges inferred.',refs('discovery','acceptance'),'M-CUBIC')]
for id,title,status,stage,summary,src,model in results:
 add(id,title,'result',status,stage,summary=summary,detail='Evidence statement is restricted to the exact cited model, domain and quantifiers. A source-linked record is not a review-board certification.',sources=src,importance=3,core=id not in ('R-INDEX','R-CURL','R-PRISM'))
 link(model,id,'study','result on model')
 link(id,stage,'supports','scope-limited',status)

work=[
('W-SOURCE','Identify one canonical 3D source/action','P0','urgent','Freeze geometry, operator, topology, and model provenance in one acceptance record.','A same-action specification validated against source code and historical model identity.'),
('W-SCALING','Derive anisotropic g₀(h) and physical normalization','P0','urgent','Derive E/B/temporal factors, coupling trajectory and renormalized source from one action.','A checkable scale family and regulator transfer/OS normalization.'),
('W-EMBED','Gauge-equivariant scale comparisons','P0','urgent','Replace naive Hamiltonian intertwining with a justified renormalized comparison.','A theorem with explicit h, volume, domains, and counterterms.'),
('W-Z5','Reconstruct genuine coupled-ℤ⁵ 3D geometry','P0','research','Source qualify any historical Penrose spatial interpretation without calling the prism equivalent.','Explicit infinite 3D nested cells, ∂ maps, non-Abelian action, and authentic generator tests.'),
('W-OPERATOR','3D physical operator-domain and time test','P1','urgent','Derive closed positive gauge-reduced form and temporal transfer on the same P0 action.','Domains, Gauss covariance, adjoints, transfer kernel, and normalizations reproducibly coincide.'),
('W-SCHATTEN','Joint N≈m² physical Schatten response','P2','research','Tighten the actual Gauss-twirled full-inverse nuclear estimates beyond representational MPO bounds.','Nontrivial high-spin, large-width trace-class bound or explicit rigorous obstruction.'),
('W-3D-ANALYTIC','3D interacting renormalization / cluster construction','P2','urgent','Transfer or replace the strip technology on 3D original links along g₀(h).','Uniform physical Schwinger/dynamics estimates across volume, h and coupling.'),
('W-BOREL','Signed positive-axis physical Borel reconstruction','P2','research','Prove genuine sign-sensitive Borel summability or use another nonperturbative construction.','Interacting state/dynamics; formal germ alone is not a solution.'),
('W-PENROSE-CURRENT','Interacting Penrose signed-current inequality','P3','research','Establish a genuine 3D Wilson-current anti-depletion bound under a certified source-model action.','Uniform physical-volume/mesh signed-current estimate.'),
('W-IR','Uniform low-frequency spectral exclusion','P4','urgent','Prove a common M>0 in physical units for interacting gauge-invariant observables.','Spectral measures vanish on (0,M), uniformly before limits.'),
('W-DYNAMICS','Common infinite-volume interacting time evolution','P4','urgent','Construct state/dynamics and a dense physical local observable family.','Joint reflection-positive temporal correlations with strong enough limits.'),
('W-OS','Nontrivial 4D Osterwalder–Schrader limit','P5','urgent','Show OS axioms, locality, vacuum, nontriviality and physical Hilbert reconstruction.','A fully specified QFT and independently verified OS hypotheses.'),
('W-REVIEW','Independent theorem and provenance review','P5','review','Audit all hypotheses, immutable source hashes, falsification tests, and final publication claims.','Independent referee-grade review and canonical acceptance gate satisfied.'),
('W-LFS','Git LFS custody migration','P0','infrastructure','Move binary originals from Library into configured Git LFS once enabled; preserve exact hashes.','Every LFS pointer rechecked against current sha256 manifest; no claim status changes.')]
for id,title,stage,prio,summary,done in work:
 add(id,title,'work','open',stage,summary=summary,detail='Acceptance test: '+done,checks=[c(done,'open')],sources=refs('p0audit') if stage=='P0' else refs('dependencies'),importance=3 if prio=='urgent' else 2,core=prio=='urgent',tags=[prio])
 link(id,stage,'blocks','required work', 'open')
# Interfaces are explicit, not theorem conclusions.
interfaces=[
('I-01','Model → physical quantum operator','P0','P1','One action must induce the physical electric/magnetic/time operators and Gauss sector.'),
('I-12','Gauss operator → nonlinear analytic bound','P1','P2','Same exact operator and source need nonperturbative control with correct domains.'),
('I-24','Interacting construction → low-energy spectrum','P2','P4','The constructed state/dynamics must produce physical finite-time spectral measures.'),
('I-34','Penrose Wilson current → infrared mechanism','P3','P4','Route-specific inequality must imply source-visible low-frequency exclusion.'),
('I-45','Physical infrared → 4D reconstructed spectrum','P4','P5','Positive threshold must survive both limits and be dense in OS Hilbert space.')]
for id,title,a,b,summary in interfaces:
 add(id,title,'interface','open',b,summary=summary,detail='A planned theorem interface. Compatible hypotheses, model tags, units and quantifiers must be checked at both endpoints.',sources=refs('dependencies'),core=False)
 link(a,id,'bridge','input');link(id,b,'bridge','output')

# Data families and leaf files have immutable per-byte digest and explicit Library paths, never binary payloads.
families={
 'stage26':'D-ARCHIVE','sweep10000':'D-SWEEPS','full_archive':'D-FULL', 'whitney':'D-WHITNEY','dissertation':'D-DISS','transcript':'D-CONVO'
}
family_titles={
'D-ARCHIVE':('Stage 26 · 800 compact checkpoints','Integrity-checked ZIP members only: four Penrose and four square seeds 101/211/307/419.'),
'D-SWEEPS':('Eight sweep-10,000 multihit NPZs','Planar two-component displacement observables, not a certified 3D SU(2) regulator.'),
'D-FULL':('Full Penrose seed-101 archive','Full source archive preserved in Library; the compact checkpoints are distinct artifacts.'),
'D-WHITNEY':('Global Whitney 11-face data','One original local geometric mass-data file; not a continuum refinement by itself.'),
'D-DISS':('Dissertation v10.7 source bundle','March 2026 scholarly and experiment materials; historical source, not November corrected theorem.'),
'D-CONVO':('Seven research transcript sources','Historical reasoning and correction trail; transcripts are not theorem certification.')}
for fid,(title,summary) in family_titles.items():
 add(fid,title,'data_family','archived','P0',summary=summary,detail='Every original file is available in Library; click a leaf to inspect SHA-256 and exact Library locator.',sources=refs('p0audit'),importance=2,core=fid in ('D-ARCHIVE','D-SWEEPS','D-DISS'))
 link(fid,'P0','provenance','source evidence')
for f in manifest['files']:
 name=f['file']; family=families[f['kind']]
 ident='FILE-'+str(manifest['files'].index(f)+1).zfill(2)
 detail=f"{f['bytes']:,} bytes · sha256 {f['sha256']}. Stored at {f['library_path']}. Cryptographic identity does not certify numerical physics."
 add(ident,name,'dataset','archived','P0',summary=f"{f['kind'].replace('_',' ')} • {f['bytes']:,} bytes",detail=detail,tags=[f['kind']],importance=1,core=False)
 N[-1]['asset']={'filename':name,'bytes':f['bytes'],'sha256':f['sha256'],'library_path':f['library_path'],'kind':f['kind'],'upload_verified':True,'git_lfs_status':'pending'}
 link(ident,family,'member','hashed source file')
 if f['kind'] in ['stage26','sweep10000','full_archive']:
  link(family,'M-Z5','evidence','historical simulations; non-3D') if (family,'M-Z5') not in {(e['from_id'],e['to_id']) for e in E} else None
 if f['kind']=='whitney':link(family,'M-PRISM','evidence','candidate geometry')
add('D-MANIFEST','SHA-256 + Library custody manifest','manifest','archived','P0',summary='Git-tracked text contains 26 immutable file digests; original payloads remain in Library pending LFS.',sources=[{'title':'Repository manifest','path':'observatory/data-manifest.json','branch':'audit/2026-11-04-knowledge-graph'}],core=False)
link('D-MANIFEST','D-ARCHIVE','indexes');link('D-MANIFEST','D-SWEEPS','indexes');link('D-MANIFEST','D-FULL','indexes');link('D-MANIFEST','D-CONVO','indexes')

add('PUB-DISS','Dissertation → audited research monograph','publication','open','P5',summary='Evolve v10.7 with source separation, corrected operator results, explicit unproved chapters and independently publishable finite contributions.',sources=prs(57,'Dissertation evolution plan'),importance=2,core=True)
link('D-DISS','PUB-DISS','provenance');link('P5','PUB-DISS','publication','final outcome only if proved')
link('W-REVIEW','PUB-DISS','required');link('R-INDEX','PUB-DISS','discovery')

# New finite P0 action candidate and quantified bridge from review (no continuum closure).
add('R-P0-HK','Finite cubic heat-kernel transfer action','result','finite','P0',
    summary='Explicit time-discrete temporal SU(2) heat kernels plus spatial Wilson weights induce the cubic Gauss-invariant Kogut–Susskind Hamiltonian at fixed spatial regulator.',
    detail='Finite positive symmetric transfer, central heat kernel, original-link gauge covariance and fixed-h temporal Trotter limit; same-action finite candidate only. NOT isotropic Wilson universality, h→0 interacting OS reconstruction, or uniform gap.',
    checks=[c('Finite temporal heat-kernel/spatial Wilson kernel and matching K+V','partial','Source-reproducible construction, independent review pending'),c('Uniform refinement h→0 and correct 4D continuum universality','open')],
    sources=refs('hktransfer','cubeham','transfer'),importance=4,core=False,tags=['cubic','heat-kernel','finite'])
link('M-CUBIC','R-P0-HK','source-model','same cubic original links')
link('R-P0-HK','P0','scoped-evidence','finite temporal action, not a closed gate')
link('R-P0-HK','W-SCALING','remaining-work','3D action/physical continuum universality still open','open')
add('I-SCALE-TELESCOPE','Conditional renormalized-correlation telescope','interface','conditional','P4',
    summary='A common physical M>0 and summably small exponentially weighted one-step interaction errors would preserve a volume- and h-uniform spectral decay rate.',
    detail='Requires a volume-uniform coarse-scale interacting decay bound, renormalized same-model F_h, and a summable error sup_R sup_t exp(Mt)|C_{j+1,R}(t)-C_{j,R}(t)|. This is a conditional triangle-inequality lemma; neither premise is proved and the estimate may be as difficult as the main gap problem.',
    checks=[c('Base-scale gap uniformly in physical volume','open'),c('Summable gauge-invariant weighted one-step RG errors','open'),c('Dense nontrivial continuum OS observable family','open')],sources=refs('hktransfer','dependencies'),importance=4,core=True)
link('W-EMBED','I-SCALE-TELESCOPE','proposed-bridge','test one-step gauge-invariant interacting correlations','open')
link('I-SCALE-TELESCOPE','P4','conditional','would preserve common physical-time decay if hypotheses proved','conditional')
link('I-SCALE-TELESCOPE','W-OS','requires','OS and nontriviality remain independent','open')

# Structural guards (source-qualified model, no gate closed by editing review notes)
ids={n['id'] for n in N}
assert all(e['from_id'] in ids and e['to_id'] in ids for e in E)
assert len({n['id'] for n in N})==len(N)
assert all(n['status']=='open' for n in N if n['kind']=='gate')
assert sum(n['kind']=='dataset' for n in N)==len(manifest['files'])
# Specific model-only claim guards
assert next(n for n in N if n['id']=='R-MPO')['stage']=='P2'
assert next(n for n in N if n['id']=='M-Z5')['status']=='unresolved'
obj={'schema':'singular-boundary.knowledge-graph.v1','build_date':'2026-11-04 (America/Denver)', 'version':'v2.27-draft','scope':'Curated source-linked, research-status graph, NOT 740 independently reviewed proofs. Closure labels only for exact subresults and never gate completion.', 'canon_status':'OPEN','catalog_baseline':'fd1c1c1c8db078f8ec9d591d182059bd1635b164','indexed_theorem_paths':740,'existing_proof_paths':78,'git_branch':'audit/2026-11-04-p0-heat-kernel-transfer', 'status_legend':{'open':'Not closed: missing mathematical/evidence conditions','finite':'Recorded finite-model result only; no continuum transfer','conditional':'Implication uses hypotheses not presently proved for the continuum theory','obstruction':'Demonstrated failure of a specified proposed shortcut','partial':'Some strictly scoped evidence but missing gate certificate','candidate':'Model or route proposed; identity/derivation incomplete','archived':'Original source files archived; integrity not mathematical validation','indexed':'Discovered/indexed only','unresolved':'Source-model identity unresolved'}, 'nodes':N,'edges':E,'sources_verified':{k:{'path':v[0],'blob_sha':v[1]} for k,v in S.items()},'library_manifest':'observatory/data-manifest.json'}
(ROOT/'knowledge-graph.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(ROOT/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(obj,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf8')
print('nodes',len(N),'edges',len(E),'by-kind', {k:sum(n['kind']==k for n in N) for k in sorted(set(n['kind'] for n in N))})

# Source-faithful Penrose-vs-square hierarchy is a non-destructive postbuild layer.
from reconcile_penrose_control import reconcile
reconcile(ROOT)

from add_mathematical_physics_bridge import extend
extend(ROOT)

# Scoped three-dimensional finite magnetic shell: no theorem gate promotion.
from add_transverse_shell_graph import attach
attach(ROOT)

# Full Wilson-exponential shell and positive two-time-memory finite model.
from add_wilson_time_graph import attach as attach_wilson_time
attach_wilson_time(ROOT)

# Matched finite cubic dyadic meshes: exact all-time P/Q influence plus spectral resolvent bounds.
from add_two_scale_influence_graph import attach as attach_two_scale_influence
attach_two_scale_influence(ROOT)

# True interacting-vacuum SU2 conditional blocking, finite Schur form and open scale target.
from add_vacuum_weighted_block_graph import attach as attach_vacuum_rg
attach_vacuum_rg(ROOT)

# Quantitative finite Wilson marginal Harnack, fixed-loop sum rule and conditional dyadic time normalization.
from add_marginal_harnack_graph import attach as attach_marginal_harnack
attach_marginal_harnack(ROOT)
