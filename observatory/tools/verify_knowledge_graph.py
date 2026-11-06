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
 check(g['schema']=='singular-boundary.knowledge-graph.v1','graph schema');check(g['canon_status']=='OPEN','canonical status must remain open');check(g['indexed_theorem_paths']==740,'preserve source index snapshot');check(g['existing_proof_paths']==78,'do not silently recount previous proof paths')
 n=g['nodes'];e=g['edges'];ids=[x['id'] for x in n];check(len(ids)==len(set(ids)),'duplicate ids');node={x['id']:x for x in n};check(len(g['nodes'])>=70,'node loss');check(len(g['edges'])>=100,'edge loss')
 for a in e:
  check(a['from_id'] in node and a['to_id'] in node,f'dangling edge {a}')
  check(a['from_id']!=a['to_id'],f'self edge {a}')
 check(len([x for x in n if x['kind']=='gate'])==6,'six proof gates required');check(set(x['id'] for x in n if x['kind']=='gate')=={'P0','P1','P2','P3','P4','P5'},'gate ids')
 check(all(x['status']=='open' for x in n if x['kind'] in ('gate','goal')),'FALSELY CLOSED GATE')
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
 check(g['version'] in ('v2.29','v2.30-draft','v2.31-draft','v2.32-draft','v2.33-draft','v2.34-draft','v2.35-draft','v2.36-draft'),'unexpected graph version')
 check(all(x in node for x in ('S-SPECTRAL-DIMENSION','S-CUT-PROJECT-ZETA','S-COMPLEX-STRUCTURE','S-CONFORMAL-SPECTRAL','S-FIBONACCI-CAVITY')),'physics concept nodes')
 check(not any('dissertation' in x['title'].lower() or re.search(r'(?i)\bpaper\s*[1-5]\b',x['title']) for x in n),'source-document titles exposed as graph concept nodes')
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
