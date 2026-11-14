#!/usr/bin/env python3
"""Validate the curated Observatory graph (structure, local source hashes, scope guardrails).
Does NOT certify individual mathematical claims or existence of a mass gap.
Run: python observatory/tools/verify_knowledge_graph.py [--data-dir /uploaded-originals]
"""
import argparse,collections,hashlib,json,sys,re
from pathlib import Path

def sha(path):
 with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def check(cond,reason):
 if not cond:raise AssertionError(reason)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--data-dir',type=Path,help='Optional uploaded original bytes for SHA-256 independent verification')
 args=ap.parse_args()
 # works from local artifact package or checked-in observatory/tools location
 here=Path(__file__).resolve().parent
 if (here/'knowledge-graph.json').exists():root=here
 else:root=here.parent
 g=json.loads((root/'knowledge-graph.json').read_text());m=json.loads((root/'data-manifest.json').read_text() if (root/'data-manifest.json').exists() else (root/'data_manifest.json').read_text())
 check(g['schema']=='singular-boundary.knowledge-graph.v1','graph schema');check(g['canon_status']=='OPEN','canonical status must remain open')
 repo_root=root.parent
 registry=json.loads((repo_root/'docs/research/THEOREM_INDEX_LIVE.json').read_text())
 check(registry.get('schema')=='singular-boundary-theorem-index-v1','source registry schema')
 registry_paths=[x['path'] for x in registry['theorems']]
 actual_paths=sorted(str(p.relative_to(repo_root)) for p in (repo_root/'research/theorems').rglob('*.md'))
 check(registry_paths==actual_paths,'current theorem paths must match source registry')
 check(g['indexed_theorem_paths']==registry['count']==len(registry_paths),'graph theorem count must match source registry')
 check(g['historical_indexed_theorem_paths']==740,'preserve 740 historical source baseline');check(g['complete_theorem_index']=='docs/research/THEOREM_INDEX_LIVE.json','complete source-registry reference');check(g['existing_proof_paths']==78,'do not silently recount previous proof paths')
 n=g['nodes'];e=g['edges'];ids=[x['id'] for x in n];check(len(ids)==len(set(ids)),'duplicate ids');node={x['id']:x for x in n};check(len(g['nodes'])>=70,'node loss');check(len(g['edges'])>=100,'edge loss')
 for a in e:
  check(a['from_id'] in node and a['to_id'] in node,f'dangling edge {a}')
  check(a['from_id']!=a['to_id'],f'self edge {a}')
 check(len([x for x in n if x['kind']=='gate'])==6,'six proof gates required');check(set(x['id'] for x in n if x['kind']=='gate')=={'P0','P1','P2','P3','P4','P5'},'gate ids')
 check(all(x['status']=='open' for x in n if x['kind'] in ('gate','goal')),'FALSELY CLOSED GATE')

 # Canonical P0-P5 scoped-check inventory: exactly 27, status-counted once.
 scoped={x['id']:x for x in n if x['id'] in {'P0','P1','P2','P3','P4','P5'}}
 expected_gate_counts={'P0':6,'P1':4,'P2':4,'P3':4,'P4':4,'P5':5}
 check(set(scoped)==set(expected_gate_counts),'all six canonical scoped gates required')
 for gate,count in expected_gate_counts.items():
  checks=scoped[gate].get('checks',[])
  check(len(checks)==count,f'{gate} scoped-check count changed')
  labels=[x.get('label','').strip() for x in checks]
  check(all(labels) and len(labels)==len(set(labels)),f'{gate} scoped-check labels must be nonempty and unique')
  check(all(x.get('state') in {'met','partial','open','blocked','finite','conditional','exact','obstruction','refuted'} for x in checks),f'{gate} has unknown scoped-check state')
 all_scoped=[x for gate in expected_gate_counts for x in scoped[gate]['checks']]
 state_counts=collections.Counter(x['state'] for x in all_scoped)
 check(len(all_scoped)==27,'canonical P0-P5 scoped-check total must equal 27')
 check(dict(state_counts)=={'partial':6,'open':19,'met':2},'canonical P0-P5 scoped-check state distribution changed; review explicitly')
 if g['version'] in ('v3.05-pf-i16-nilpotent-row-projection','v3.06-pf-i16-product-process-tensor-gap'):
  check(g.get('scoped_checks',{}).get('count')==27,'scoped-check metadata count')
  check(g['scoped_checks'].get('gate_counts')==expected_gate_counts,'scoped-check metadata gate allocation')
  check(g['scoped_checks'].get('state_counts')=={'met':2,'partial':6,'open':19},'scoped-check metadata state allocation')
  check(node['PF-I16-NILPOTENT-ROW-PROJECTION-RESUMMATION']['status']=='candidate','nilpotent resummation must remain candidate')
  check(node['PF-I16-NILPOTENT-ROW-PROJECTION-RESUMMATION']['stage']=='P2','nilpotent resummation remains a P2 analytic candidate')
  if g['version']=='v3.06-pf-i16-product-process-tensor-gap':
   check(node['PF-I16-PRODUCT-PROCESS-TENSOR-GAP-BRIDGE']['status']=='conditional','product-process tensor-gap bridge remains conditional')
   check(node['PF-I16-PRODUCT-PROCESS-TENSOR-GAP-BRIDGE']['stage']=='P2','product-process bridge remains a P2 reference-process result')
   check(any(z['from_id']=='PF-I16-JOINT-SPACETIME-CLUSTER-TREE' and z['to_id']=='PF-I16-PRODUCT-PROCESS-TENSOR-GAP-BRIDGE' and z['status']=='conditional' for z in e),'product-process bridge dependency edge missing')
   check(any(z['from_id']=='PF-I16-PRODUCT-PROCESS-TENSOR-GAP-BRIDGE' and z['to_id']=='PF-I16-QUANTUM-CONNECTED-RESOLVENT-TREE' and z['status']=='open' for z in e),'product-process bridge must not bypass quantum tree gate')
  check(any(z['from_id']=='PF-I16-JOINT-SPACETIME-CLUSTER-TREE' and z['to_id']=='PF-I16-NILPOTENT-ROW-PROJECTION-RESUMMATION' for z in e),'nilpotent resummation route edge missing')
  check(any(z['from_id']=='PF-I16-NILPOTENT-ROW-PROJECTION-RESUMMATION' and z['to_id']=='PF-I16-QUANTUM-CONNECTED-RESOLVENT-TREE' for z in e),'nilpotent candidate must not bypass quantum tree gate')
 check(node['P0']['checks'][0]['label'].startswith('Penrose P3'),'Penrose P0 must be first')
 check(node['P0']['checks'][3]['note'].find('CONTROL ONLY')>=0,'cubic belongs to control certificate')
 check(node['G-GRAV']['status']=='open' and node['THEOREM']['status']=='open','both targets open')
 check('primary-hypothesis' in node['M-PENROSE-2D']['tags'],'Penrose primary marker')
 check('control' in node['M-SQUARE-2D']['tags'],'square is control')
 check(not any(z['from_id'] in ('D-ARCHIVE','D-SWEEPS') and z['to_id']=='M-Z5' for z in e),'mixed archive falsely attributed to Z5')
 check(not any(z['from_id']=='W-LFS' and z['to_id']=='P0' for z in e),'Git LFS cannot block mathematical gate')
 check(len([z for z in e if z['kind']=='experiment-provenance'])==17,'17 geometry-specific source nodes')
 check(node['M-Z5']['status']=='unresolved','Historical Penrose 3D equivalence must remain unresolved')
 check(node['R-MPO']['stage']=='P2','MPO is P2 strip not 3D P0 proof')
 check(any(x['id']=='R-WEAK' and x['status']=='obstruction' for x in n),'weak-coupling mismatch retained')
 check(any(x['from_id']=='P3' and x['to_id']=='P4' and x['status']=='route-specific' for x in e),'Penrose mechanism remains optional')
 check(len(m['files'])==len(set(x['file'] for x in m['files'])),'duplicate original file')
 objects=[x for x in n if x['kind']=='dataset'];check(len(objects)==len(m['files']),'data node coverage')
 byfile={x['asset']['filename']:x for x in objects}
 for f in m['files']:
  check(f['file'] in byfile,'missing file '+f['file']);x=byfile[f['file']]['asset'];check(x['sha256']==f['sha256'] and x['bytes']==f['bytes'],'asset mismatch');check(x['library_path']==f['library_path'],'Library locator mismatch');check(re.fullmatch(r'[0-9a-f]{64}',x['sha256'])is not None,'sha256 shape');check(x['git_lfs_status']=='pending','LFS not configured')
  if args.data_dir:
   p=args.data_dir/f['file'];check(p.is_file(),'missing uploaded source '+str(p));check(p.stat().st_size==f['bytes'],'byte length mismatch');check(sha(p)==f['sha256'],'source SHA mismatch '+str(p))
 # Physics ontology and model-comparison acceptance gates (v2.29 integrated).
 check(g['version'] in ('v2.29','v2.30-draft','v2.31-draft','v2.32-draft','v2.33-draft','v2.34-draft','v2.35-draft','v2.36-draft','v2.37-draft','v2.38-draft','v2.39-draft','v2.40-draft','v2.41-draft','v2.42-research','v2.43-research','v2.44-research','v2.45-research','v2.46-research','v2.47-research','v2.48-concepts','v2.49-ym-proof','v2.69-pf-i16-four-face-c2222','v2.70-pf-i16-dressed-locality','v2.71-pf-i16-refined-rotor','v2.72-pf-i16-pointwise-kato-bochner','v2.73-r3-ir-trace-gradient','v3.04-pf-i16-quasi-factorization-reduction','v3.05-pf-i16-nilpotent-row-projection','v3.06-pf-i16-product-process-tensor-gap'),'unexpected graph version')
 if g['version'] in ('v2.42-research','v2.43-research','v2.44-research','v2.45-research','v2.46-research','v2.47-research','v2.48-concepts','v2.49-ym-proof','v2.69-pf-i16-four-face-c2222','v2.70-pf-i16-dressed-locality','v2.71-pf-i16-refined-rotor','v2.72-pf-i16-pointwise-kato-bochner','v2.73-r3-ir-trace-gradient','v3.04-pf-i16-quasi-factorization-reduction','v3.05-pf-i16-nilpotent-row-projection','v3.06-pf-i16-product-process-tensor-gap'):
  expected={'v2.42-research':(148,342),'v2.43-research':(156,362),'v2.44-research':(159,374),'v2.45-research':(163,388),'v2.46-research':(168,403),'v2.47-research':(172,417),'v2.48-concepts':(188,452),'v2.49-ym-proof':(196,474),'v2.69-pf-i16-four-face-c2222':(278,663),'v2.70-pf-i16-dressed-locality':(282,670),'v2.71-pf-i16-refined-rotor':(283,672),'v2.72-pf-i16-pointwise-kato-bochner':(284,675),'v2.73-r3-ir-trace-gradient':(285,678),'v3.04-pf-i16-quasi-factorization-reduction':(298,703),'v3.05-pf-i16-nilpotent-row-projection':(299,705),'v3.06-pf-i16-product-process-tensor-gap':(300,707)}
  check((len(n),len(e))==expected[g['version']],'curated graph counts by version')
  if g['version'] in ('v2.49-ym-proof','v2.69-pf-i16-four-face-c2222','v2.70-pf-i16-dressed-locality','v2.71-pf-i16-refined-rotor'):
   check(g['ym_proof_interface']['primary_gap_gate']=='YM-UNIFORM-GAUGE-POINCARE','true interacting gauge spectral target')
   check(node['YM-UNIFORM-GAUGE-POINCARE']['status']=='open','uniform physical quantum mass gap OPEN')
   check(node['YM-GROUNDSTATE-DIRICHLET']['status']=='finite','finite true-vacuum identity')
   check(node['YM-CELL-WILSON-LOCALITY']['status']=='finite','finite weighted spatial-flow identity')
   check(node['PF-C5-3D-QUOTIENT-RANK']['status']=='obstruction','quotient rank obstruction')
   check(node['PF-CYCLOTOMIC-DELONE']['status']=='conditional','3D Voronoi source/coupling assumptions retained')
   check(node['PF-VORONOI-HODGE-WEIGHTS']['status']=='open','metric action and Hodge source validation still open')
   check(g['ym_proof_interface'].get('nontrivial_4d_os_constructed') is False,'4D OS continuum remains OPEN')
   check((root/'yang-mills-proof.html').is_file(),'YM proof-map page')
  if g['version'] in ('v2.48-concepts','v2.49-ym-proof'):
   check(len(g.get('conceptual_program',{}).get('concept_ids',[]))==16,'16 conceptual nodes')
   check(g['conceptual_program']['primary_concept']=='CON-2D3D-PROBLEM','historical 2D→3D observation question')
   check(node['CON-34-55-EMERGENCE']['status']=='conditional','synthetic 34:55 not source-certified')
   check(node['CON-3D-OBSERVER']['status']=='open','physical 3D observer OPEN')
   check((root/'conceptual-atlas.html').is_file(),'concept-first atlas exists')
  if g['version'] in ('v2.47-research','v2.48-concepts','v2.49-ym-proof'):
   check(node['PF-ARM-MIRROR-NOGO']['status']=='conditional','no symmetric-patch 34:55 intrinsic selector')
   check(node['PF-J-PROJECTED-ORIENTATION']['status']=='conditional','chosen J is not dynamical selection')
   check(node['PF-OBSERVER-MARKED-GAUGE']['status']=='conditional','marked interacting gauge parity theorem')
   check(node['PF-OBSERVER-SELECTION-LAW']['status']=='open','actual physical handedness selection remains OPEN')
  if g['version'] in ('v2.46-research','v2.47-research','v2.48-concepts','v2.49-ym-proof'):
   check(node['PF-Z5-SLICE-OBSTRUCTION']['status']=='obstruction','strict fixed-sum/basis-edge conflict visible')
   check(node['PF-Z5-QUOTIENT-CANDIDATE']['status']=='conditional','diagonal quotient is a candidate only')
   check(node['PF-DOUBLE-SPIRAL-SOURCE']['status']=='conditional','34:55 dissertation source not physical 3D graph proof')
   check(node['PF-DIHEDRAL-PARITY-NULL']['status']=='conditional','parity conditional null retained')
   check(node['PF-Z5-SOURCE-GENERATOR']['status']=='open','original generator remains OPEN')
  if g['version'] in ('v2.45-research','v2.46-research','v2.47-research','v2.48-concepts','v2.49-ym-proof'):
   check(node['PF-SINGLE-HARMONIC-NOGO']['status']=='obstruction','m10 alone cannot yield chirality')
   check(node['PF-HARMONIC-TRIAD']['status']=='finite','two-harmonic identity finite only')
   check(node['PF-SU2-ROTOR-NULL']['status']=='finite','non-Penrose quantum false-positive recorded')
   check(node['PF-HELICAL-LIFT-FREEDOM']['status']=='obstruction','physical helix not specified by circle')
  if g['version'] in ('v2.44-research','v2.45-research','v2.46-research','v2.47-research','v2.48-concepts','v2.49-ym-proof'):
   check(node['PF-Z13-ALIAS']['status']=='obstruction','sampling alias caveat visible')
   check(node['PF-GAUGE-TWOPOINT']['status']=='conditional','true interacting SU2 two-point scope conditional')
   check(node['PF-CHIRAL-NULL']['status']=='open','chiral falsification still open')
  if g['version'] in ('v2.43-research','v2.44-research','v2.45-research','v2.46-research','v2.47-research','v2.48-concepts','v2.49-ym-proof'):
   check(all('PF-H'+str(i) in node for i in range(7)),'Paper 3 helical observer path missing')
   check(node['PF-H1']['status']=='open' and node['PF-H3']['status']=='conditional','geometry and frequencies properly scoped')
  check(g.get('pf_program',{}).get('stages')==['PF-G0','PF-G1','PF-G2','PF-G3','PF-G4','PF-G5'],'PF route metadata')
  check(all(node['PF-G'+str(i)]['status']=='open' for i in range(6)),'PF source-to-continuum gates open')
  check(node['PF-SCALAR-NOGO']['status']=='obstruction','scalar Laplacian limitation explicit')
  check(node['PF-LORENTZ-OPEN']['status']=='open','spacetime dimensional identity open')
  check(node['M-Z5']['status']=='unresolved' and node['M-CUBIC']['kind']=='model','model/control distinct')
  check(g['pf_program'].get('approved_deployment') is False,'no Pages publication authorization')
  check(all(any(z['from_id']=='PF-G'+str(i) and z['to_id']=='PF-G'+str(i+1) for z in e) for i in range(5)),'PF dependency chain intact')
  check((root/'penrose-program.html').is_file(),'PF primary standalone map')
  check('data-view="pf"' in (root/'graph.html').read_text(),'PF default Atlas lens')
 check(all(x in node for x in ('S-SPECTRAL-DIMENSION','S-CUT-PROJECT-ZETA','S-COMPLEX-STRUCTURE','S-CONFORMAL-SPECTRAL','S-FIBONACCI-CAVITY')),'physics concept nodes')
 if g['version'] in ('v2.70-pf-i16-dressed-locality','v2.71-pf-i16-refined-rotor'):
  check(node['PF-I16-INCIDENCE-UNIFORM-COUNT']['status']=='finite','universal connected-support count recorded as combinatorial only')
  check(node['PF-I16-EXACT-DRESSING-RESIDUAL']['status']=='finite','exact finite dressing identity recorded')
  check(node['PF-I16-THIRD-ORDER-DRESSED-RESOLVENT']['status']=='conditional','third-order analytic bound remains conditional')
  check(node['PF-I16-FOURTH-ORDER-PARTITION-CANCELLATION']['status']=='open','fourth-order cancellation remains open')
  check(any(z['from_id']=='PF-I16-THIRD-ORDER-DRESSED-RESOLVENT' and z['to_id']=='PF-I16-FOURTH-ORDER-PARTITION-CANCELLATION' and z['status']=='open' for z in e),'fourth-order next-step edge missing')
  check(g['pf_i16_dressed_locality']['all_orders_summability'] is False and g['pf_i16_dressed_locality']['continuum_mass_gap'] is False,'no all-orders or continuum gap overclaim')
 if g['version'] in ('v2.71-pf-i16-refined-rotor','v2.72-pf-i16-pointwise-kato-bochner','v2.73-r3-ir-trace-gradient','v3.04-pf-i16-quasi-factorization-reduction'):
  check(node['PF-I16-REFINED-ROTOR-HESSIAN-RESIDUAL-DERIVATIVES']['status']=='conditional','refined rotor estimates remain conditional')
  check(any(z['from_id']=='PF-I16-EXACT-DRESSING-RESIDUAL' and z['to_id']=='PF-I16-REFINED-ROTOR-HESSIAN-RESIDUAL-DERIVATIVES' for z in e),'refined rotor dependency edge missing')
  check(g['pf_i16_dressed_locality']['third_order']['prior_numeric_bound_revalidated'] is False,'prior third-order bound not silently promoted')
 if g['version'] in ('v2.72-pf-i16-pointwise-kato-bochner','v2.73-r3-ir-trace-gradient'):
  check(node['PF-I16-POINTWISE-KATO-BOCHNER-DERIVATIVE-FLOW']['status']=='conditional','pointwise Kato-Bochner derivative flow remains conditional')
  check(any(z['from_id']=='PF-I16-REFINED-ROTOR-HESSIAN-RESIDUAL-DERIVATIVES' and z['to_id']=='PF-I16-POINTWISE-KATO-BOCHNER-DERIVATIVE-FLOW' and z['status']=='conditional' for z in e),'Kato-Bochner dependency edge missing')
  check(any(z['from_id']=='PF-I16-POINTWISE-KATO-BOCHNER-DERIVATIVE-FLOW' and z['to_id']=='PF-I16-THIRD-ORDER-DRESSED-RESOLVENT' and z['status']=='conditional' for z in e),'derivative-flow resolvent edge missing')
  check(g['pf_i16_dressed_locality']['derivative_flow']['pointwise_componentwise_kato_bocher_derived'] is True,'componentwise Kato-Bochner bridge missing')
  check(g['pf_i16_dressed_locality']['all_orders_summability'] is False and g['pf_i16_dressed_locality']['continuum_mass_gap'] is False,'no all-orders or continuum gap overclaim')
 if g['version'] in ('v2.73-r3-ir-trace-gradient','v3.04-pf-i16-quasi-factorization-reduction','v3.05-pf-i16-nilpotent-row-projection','v3.06-pf-i16-product-process-tensor-gap'):
  check(node['R3-IR-TRACE-GRADIENT']['status']=='conditional','R3_IR trace-gradient result remains conditional')
  check(node['R3-IR-TRACE-GRADIENT']['stage']=='P2','R3_IR trace-gradient block remains finite strip P2')
  check(any(x['from_id']=='R3-IR-TRACE-GRADIENT' and x['to_id']=='W-3D-ANALYTIC' and x['status']=='open' for x in e),'3D transfer remains explicitly open')

 if g['version'] in ('v3.04-pf-i16-quasi-factorization-reduction','v3.05-pf-i16-nilpotent-row-projection','v3.06-pf-i16-product-process-tensor-gap'):
  check(node['PF-I16-THIRD-ORDER-DRESSED-RESOLVENT']['status']=='conditional','third-order spatial tree remains conditional')
  check(node['PF-I16-FOURTH-ORDER-PARTITION-CANCELLATION']['status']=='finite','fourth-order exact partition identity finite only')
  check(g['pf_i16_dressed_locality']['third_order']['conditional_spatial_tree_bound'] is True,'conditional third-order Dobrushin tree bound missing')
  check(g['pf_i16_dressed_locality']['fourth_order']['spatial_four_support_tree_status']=='conditional','fourth-order cut-interpolation tree remains conditional')
  check(g['pf_i16_dressed_locality']['all_orders_summability'] is False and g['pf_i16_dressed_locality']['continuum_mass_gap'] is False,'all-orders and continuum gates remain open')
 check('dissertation' not in node['PF-I16-EXACT-SEVEN-CLASS-FOUR-FACE-C2222']['title'].lower() and re.search(r'(?i)\\bpaper\\s*[1-5]\\b',node['PF-I16-EXACT-SEVEN-CLASS-FOUR-FACE-C2222']['title']) is None,'PF-I16 result node must remain result-focused, not a source-document title')
 check(all(x in node and node[x]['status'] in ('open','conditional') for x in ('T0-QC-3D','T1-QC-ACTION','T2-OBSERVABLES','T3-TIME-COMPARE','T4-OS-LIMIT','T5-GAP-TRANSFER')),'unclosed Penrose transfer obligations')
 check(node['R-CUBIC-FINITE-GAP']['status']=='finite','finite strong-coupling theorem scope')
 check(node['I-UV-COUPLING']['status']=='open','missing ultraviolet regime')
 check(node['R-LOW-ENERGY-COUNTER']['status']=='obstruction','spectral counterexample lost')
 check(node['I-QG-SPECTRAL-OP']['status']=='open' and node['G-GRAV']['status']=='open','gravity operator remains open')
 check(not any(x['from_id']=='R-CUBIC-FINITE-GAP' and x['to_id']=='THEOREM' for x in e),'no unlicensed direct finite gap to continuum')
 check(any(x['from_id']=='R-CUBIC-FINITE-GAP' and x['to_id']=='I-UV-COUPLING' for x in e),'strong coupling regime witness missing')
 check((root/'MATHEMATICAL_PHYSICS_GUIDE.md').is_file(),'reader guide missing')
 if g['version'] in ('v2.30-draft','v2.31-draft'):
  check(node['R-CUBIC-3D-SHELL']['status']=='finite','shell must remain finite')
  check(node['W-3D-WILSON-TIME']['status']=='open','full Wilson-time gate must remain open')
  check(any(z['from_id']=='W-3D-WILSON-TIME' and z['to_id']=='P2' and z['status']=='open' for z in e),'no physical-time shortcut')
  check(all(x['status']=='open' for x in n if x['kind'] in ('goal','gate')),'no gate closure')
 if g['version']=='v2.30-draft':
  check(len(n)==103 and len(e)==194,'scoped finite shell graph count')
 if g['version']=='v2.31-draft':
  check(len(n)==105 and len(e)==200,'finite Wilson/time memory graph counts')
  check(node['R-WILSON-EXP-SHELL']['status']=='finite','full Wilson cap scope')
  check(node['R-TEMPORAL-MEMORY']['status']=='finite','finite-time memory scope')
  check(node['W-3D-WILSON-TIME']['checks'][-1]['state']=='open','time RG remains open')
  check(any(a['from_id']=='W-3D-WILSON-TIME' and a['to_id']=='T3-TIME-COMPARE' and a['status']=='open' for a in e),'interacting IR interface must remain open')
 

 if g['version']=='v2.32-draft':
  check(len(n)==108 and len(e)==208,'finite two-scale influence graph count')
  check(node['R-TWO-TIME-INFLUENCE']['status']=='finite','exact finite P/Q influence')
  check(node['R-DYADIC-BARE-MEMORY']['status']=='finite','finite two-scale ratio')
  check(node['W-RENORMALIZED-INFLUENCE']['status']=='open','renormalized influence must remain open')
  check(any(z['from_id']=='W-RENORMALIZED-INFLUENCE' and z['to_id']=='T3-TIME-COMPARE' and z['status']=='open' for z in e),'P2/P4 infrared obligation remains open')
  check(all(x['status']=='open' for x in n if x['kind'] in ('gate','goal')),'continuum gates remain open')
 if g['version'] in ('v2.33-draft','v2.34-draft'):
  check(node['R-VACUUM-WEIGHTED-BLOCK']['status']=='finite','finite true-vacuum scope')
 if g['version']=='v2.33-draft':
  check(len(n)==111 and len(e)==218,'finite true-vacuum graph counts')
  check(node['R-VACUUM-WEIGHTED-BLOCK']['status']=='finite','finite dressed observable checkpoint')
  check(node['R-SU2-STATIC-TIME-COUNTER']['status']=='finite','SU2 gauge-graph temporal counterexample')
  check(node['W-STATE-SCHUR-UNIFORM']['status']=='open','uniform form gap not established')
  check(node['W-RENORMALIZED-INFLUENCE']['checks'][0]['state']=='partial','finite candidate but not uniform')
  check(node['T2-OBSERVABLES']['status']=='open','T2 remains an open continuum interface')
  check(any(x['from_id']=='W-STATE-SCHUR-UNIFORM' and x['to_id']=='T3-TIME-COMPARE' and x['status']=='open' for x in e),'physical-time gap remains open')
  check(all(x['status']=='open' for x in n if x['kind'] in ('gate','goal')),'do not promote continuum')
 if g['version']=='v2.34-draft':
  check(len(n)==115 and len(e)==231,'finite marginal/sum-rule graph count')
  check(node['R-WILSON-MARGINAL-HARNACK']['status']=='finite','true-vacuum Harnack finite only')
  check(node['R-WILSON-FIXED-LOOP-MOMENT']['status']=='finite','physical loop sum rule')
  check(node['I-WILSON-STATIC-TIME-NORM']['status']=='conditional','marginal-time matching unproved')
  check(node['W-LOCAL-MARGINAL-UV']['status']=='open','local uniform UV marginal remains open')
  check(node['W-STATE-SCHUR-UNIFORM']['status']=='open','full physical Schur form remains open')
  check(node['G-GRAV']['status']=='open','quantum gravity open')
  check(all(x['status']=='open' for x in n if x['kind'] in ('gate','goal')),'no continuum gate closure')
  check(any(x['from_id']=='W-LOCAL-MARGINAL-UV' and x['to_id']=='T3-TIME-COMPARE' and x['status']=='open' for x in e),'long-time comparison remains open')
 if g['version']=='v2.35-draft':
  check(len(n)==119 and len(e)==245,'local Wilson Fisher graph counts')
  check(node['R-LOCAL-LINK-ENERGY']['status']=='finite','local no-gap energy certificate scoped')
  check(node['R-LOCAL-WILSON-FISHER']['status']=='finite','volume-independent but not UV-uniform Fisher')
  check(node['R-WILSON-THERMO-SUBSEQ']['status']=='finite','only subsequential fixed-h thermodynamic result')
  check(node['W-UV-UNIFORM-LOCAL-WILSON']['status']=='open','weak-coupling renormalization remains open')
  check(node['W-LOCAL-MARGINAL-UV']['checks'][0]['state']=='partial','local H1 but not uniform pointwise Harnack')
  check(node['T2-OBSERVABLES']['status']=='open','no full T2 continuum closure')
  check(node['I-WILSON-STATIC-TIME-NORM']['status']=='conditional','physical time alignment unproved')
  check(node['G-GRAV']['status']=='open','gravity UV objective not proved')
  check(all(x['status']=='open' for x in n if x['kind'] in ('goal','gate')),'continuum theorem gates remain OPEN')
  check(any(x['from_id']=='W-UV-UNIFORM-LOCAL-WILSON' and x['to_id']=='T3-TIME-COMPARE' and x['status']=='open' for x in e),'all-time uniform influence missing')
 if g['version']=='v2.36-draft':
  check(len(n)==124 and len(e)==260,'spatial Wilson flow graph counts')
  check(node['R-SU2-FISHER-GAP-COUNTER']['status']=='obstruction','Fisher-gap obstruction scoped to class rotor')
  check(node['R-GROUP-HEAT-WILSON-NOGO']['status']=='finite','normalized group heat no-go finite')
  check(node['R-CUBIC-SPATIAL-WILSON-FLOW']['status']=='finite','finite 3D gauge flow only')
  check(node['I-FLOWED-WILSON-DIRICHLET']['status']=='conditional','UV moment criterion conditional')
  check(node['W-PHYSICAL-FLOWED-SCHUR']['status']=='open','physical flow/Schur theorem remains open')
  check(node['R-LOCAL-WILSON-FISHER']['status']=='finite','prior finite local Fisher retained')
  check(node['R-WILSON-THERMO-SUBSEQ']['status']=='finite','prior fixed-h thermodynamic scope')
  check(node['W-UV-UNIFORM-LOCAL-WILSON']['status']=='open','weak-coupling uniformity still open')
  check(node['T2-OBSERVABLES']['status']=='open','renormalized observable T2 still open')
  check(node['T3-TIME-COMPARE']['status']=='open','physical-time T3 still open')
  check(node['G-GRAV']['status']=='open','independent gravitational UV problem still open')
  check(all(x['status']=='open' for x in n if x['kind'] in ('gate','goal')),'no continuum theorem gate promotion')
  check(any(x['from_id']=='W-PHYSICAL-FLOWED-SCHUR' and x['to_id']=='T3-TIME-COMPARE' and x['status']=='open' for x in e),'full physical-time Schur bridge missing')
 if g['version']=='v2.37-draft':
  check(len(n)==128 and len(e)==275,'linearized physical flow graph counts')
  check(node['R-LINEAR-CUBIC-PHYSFLOW']['status']=='finite','linearized finite only')
  check(node['R-PERIODIC-FLOW-FOURIER']['status']=='finite','periodic control only')
  check(node['R-NONLINEAR-PLAQUETTE-FLOW-ESCAPE']['status']=='obstruction','nonlinear Haar counterexample scope')
  check(node['W-NONLINEAR-PHYS-RADIUS']['status']=='open','nonlinear physical flow remains OPEN')
  check(node['R-CUBIC-SPATIAL-WILSON-FLOW']['status']=='finite','prior finite flow remains')
  check(node['W-PHYSICAL-FLOWED-SCHUR']['status']=='open','interacting Schur comparison remains OPEN')
  check(node['T2-OBSERVABLES']['status']=='open','T2 remains OPEN')
  check(node['T3-TIME-COMPARE']['status']=='open','physical-time T3 remains OPEN')
  check(node['G-GRAV']['status']=='open','gravity UV objective remains OPEN')
  check(all(x['status']=='open' for x in n if x['kind'] in ('goal','gate')),'no continuum theorem gate promoted')
  check(any(x['from_id']=='W-NONLINEAR-PHYS-RADIUS' and x['to_id']=='T3-TIME-COMPARE' and x['status']=='open' for x in e),'complete interacting physical-time interface missing')
 if g['version']=='v2.38-draft':
  check(len(n)==132 and len(e)==288,'nonlinear physical energy graph count')
  check(node['R-NONLINEAR-PHYS-ACTION']['status']=='finite','nonlinear classical energy scoped')
  check(node['R-PLAQUETTE-HOLONOMY-ADMISSIBILITY']['status']=='conditional','uniform initial energy hypothesis required')
  check(node['R-CUBIC-CURVATURE-ATOMIC']['status']=='obstruction','curvature concentration at initial time')
  check(node['R-FINITE-FLOWED-VACUUM']['status']=='finite','finite interacting-vacuum variance only')
  check(node['W-NONLINEAR-PHYS-RADIUS']['status']=='open','nonlinear quantum physical-radius still OPEN')
  check(node['W-NONLINEAR-PHYS-RADIUS']['checks'][0]['state']=='partial','classical energy is only a partial certificate')
  check(node['W-PHYSICAL-FLOWED-SCHUR']['status']=='open','full interacting Schur comparisons remain OPEN')
  check(node['T2-OBSERVABLES']['status']=='open','continuum observable still OPEN')
  check(node['T3-TIME-COMPARE']['status']=='open','physical quantum-time bridge still OPEN')
  check(node['G-GRAV']['status']=='open','gravity UV still OPEN')
  check(all(x['status']=='open' for x in n if x['kind'] in ('goal','gate')),'never promote P0-P5')
  check(any(x['from_id']=='R-CUBIC-CURVATURE-ATOMIC' and x['to_id']=='W-NONLINEAR-PHYS-RADIUS' for x in e),'concentration warning is navigable')
 if g['version']=='v2.39-draft':
  check(len(n)==136 and len(e)==302,'Cartan nonlinear smoothing graph counts')
  check(node['R-PLANAR-CARTAN-EMBED']['status']=='finite','Cartan invariant subset only')
  check(node['R-CARTAN-POSITIVE-FLOW-SMOOTH']['status']=='conditional','positive physical time bound conditional only')
  check(node['R-CARTAN-ALLTIME-L2']['status']=='conditional','Cartan nonlinear-to-Maxwell only')
  check(node['W-FULL-NONABELIAN-PHYS-SMOOTHING']['status']=='open','noncommuting SU2 and true vacuum still OPEN')
  check(node['W-NONLINEAR-PHYS-RADIUS']['status']=='open','no full nonlinear quantum continuum claim')
  check(node['T2-OBSERVABLES']['status']=='open','renormalized continuum observable T2 remains open')
  check(node['T3-TIME-COMPARE']['status']=='open','physical quantum-time T3 remains open')
  check(node['G-GRAV']['status']=='open','separate gravity UV objective remains open')
  check(all(x['status']=='open' for x in n if x['kind'] in ('goal','gate')),'no YM continuum gate promoted')
  check(any(x['from_id']=='R-PLANAR-CARTAN-EMBED' and x['to_id']=='W-FULL-NONABELIAN-PHYS-SMOOTHING' and x['status']=='open' for x in e),'Haar-null sector restriction must be explicit')
 if g['version']=='v2.40-draft':
  check(len(n)==139 and len(e)==314,'non-Abelian locality Atlas counts')
  check(node['R-FULL-NONABELIAN-PLAQUETTE-INFLUENCE']['status']=='finite','all-field local estimate finite only')
  check(node['R-FULL-NONABELIAN-MAX-COUNTER']['status']=='obstruction','strict max increase numerical warning')
  check(node['W-FULL-NONABELIAN-SIGNED-COVARIANT-HEAT']['status']=='open','physical-time nonabelian smoothing remains OPEN')
  check(node['W-FULL-NONABELIAN-PHYS-SMOOTHING']['status']=='open','true-vacuum nonabelian bridge remains OPEN')
  check(node['W-NONLINEAR-PHYS-RADIUS']['status']=='open','nonlinear 4D still OPEN')
  check(node['T2-OBSERVABLES']['status']=='open','OS 4D field remains OPEN')
  check(node['T3-TIME-COMPARE']['status']=='open','full Schur remains OPEN')
  check(node['G-GRAV']['status']=='open','gravity UV remains OPEN')
  check(all(x['status']=='open' for x in n if x['kind'] in ('gate','goal')),'no mass-gap gate promotion')
  check(any(x['from_id']=='R-FULL-NONABELIAN-PLAQUETTE-INFLUENCE' and x['to_id']=='W-FULL-NONABELIAN-SIGNED-COVARIANT-HEAT' and x['status']=='open' for x in e),'physical tau/h² blowup visible')
 check(sum(f['kind']=='stage26' for f in m['files'])==8,'compact Stage26 eight');check(sum(f['kind']=='sweep10000' for f in m['files'])==8,'sweeps eight');check(sum(f['kind']=='transcript' for f in m['files'])==7,'transcripts seven');check(sum(f['kind']=='full_archive' for f in m['files'])==1,'full archive one')
 # All bundled runtime assets must be present, and no external script/CSS host is allowed.
 html=(root/'graph.html').read_text();js=(root/'graph-app.js').read_text();css=(root/'graph.css').read_text();script=(root/'knowledge-graph-data.js').read_text()
 for x in ['graph.css','graph-app.js','knowledge-graph-data.js'] :check(x in html,'missing linked asset '+x)
 check(script.startswith('window.SB_KNOWLEDGE_GRAPH='),'data JS prefix')
 check('No personal flag' in html and 'Export review JSON' in html,'editable review workflow missing')
 check('localStorage' in js and 'singular-boundary.review-annotations.v1' in js,'notes import/export missing')
 check('No public deployment' in html,'publication boundary missing');check('data-view="comparison"' in html,'comparison lens missing');check('data-view="bridge"' in html,'cubic-to-quasicrystal lens missing');check('GRAVITY + YM' in html and 'OPEN' in html,'open status omitted');check('No gap claim' in html or 'NO GAP CLAIM' in html,'scope warning absent')
 check('https://cdn.' not in html and 'https://cdn.' not in js,'external code forbidden')
 print(json.dumps({'result':'PASS','nodes':len(n),'edges':len(e),'gates_open':6,'source_files':len(objects),'source_bytes':sum(x['bytes'] for x in m['files']),'verified_original_bytes':bool(args.data_dir),'findings':'Structural+cryptographic checks only; no mathematical theorem certified.'},indent=2))
if __name__=='__main__':
 try:main()
 except Exception as exc:
  print('FAIL:',type(exc).__name__,str(exc),file=sys.stderr);sys.exit(1)
