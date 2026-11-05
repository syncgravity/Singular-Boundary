#!/usr/bin/env python3
"""Idempotent source-faithful reclassification of the Proof Atlas.
Must run after build_knowledge_graph.py; does not change original binary data.
"""
import argparse, json
from pathlib import Path

def reconcile(root: Path):
 root=Path(root); out_path=root/'knowledge-graph.json'; g=json.loads(out_path.read_text(encoding='utf8'))
 # Build from the pinned v2.27 source; repeat runs are safe.
 if g['version']=='v2.28-draft':return g
 assert g['version']=='v2.27-draft',g['version']
 n=g['nodes'];e=g['edges']; lookup={x['id']:x for x in n}
 def chk(label,state='open',note=''):return {'label':label,'state':state,'note':note}
 def add(id,title,kind,status,stage=None,summary='',detail='',checks=None,tags=None,core=True,importance=4,sources=None):
  assert id not in lookup,id
  row={'id':id,'title':title,'kind':kind,'status':status,'stage':stage,'summary':summary,'detail':detail,'checks':checks or [],'sources':sources or [],'tags':tags or [],'importance':importance,'core':core,'route':None}
  n.append(row);lookup[id]=row
 def edge(a,b,kind,label='',status='tracked'):
  assert a in lookup and b in lookup,(a,b)
  if not any(z['from_id']==a and z['to_id']==b and z['kind']==kind for z in e):e.append({'from_id':a,'to_id':b,'kind':kind,'label':label,'status':status})

 # Retain the historical YM target, but do not misidentify it as the sole purpose of the dissertation.
 lookup['THEOREM']['title']='YM goal · Nontrivial 4D SU(2) theory and mass gap'
 lookup['THEOREM']['summary']='Separate Clay-style Yang–Mills existence and mass-gap objective; not established by Penrose spectral suppression.'
 add('G-GRAV','Primary dissertation goal · Quasicrystalline spectral quantum gravity','goal','open',summary='Determine whether Fibonacci/Penrose and coupled ℤ⁵ spectral geometry yield a physically justified ultraviolet gravitational theory and consistent quantum dynamics.',detail='Original dissertation aim. Neither finite spectral-zeta changes nor Stage26 planar correlations prove interacting gravity finiteness. Distinct from Yang–Mills mass gap.',checks=[chk('Reproduce spectral geometry and original periodic control under comparable operators'),chk('Specify physically correct gravitational quantum operator and relevant measure'),chk('Certify 3D spatial / 3+1D source geometry and dynamics'),chk('Prove the claimed ultraviolet finiteness or precisely delimited renormalized result'),chk('Demonstrate physical continuum consistency, not only a kinematic identification')],tags=['penrose','quantum-gravity','dissertation'],importance=5)
 lookup['PUB-DISS']['summary']='Original Fibonacci/Penrose/coupled-ℤ⁵ quantum-gravity papers remain central; independent SU(2) continuum mass-gap research is a separate proof objective.'
 edge('G-GRAV','PUB-DISS','primary-objective','source-faithful publication program')

 # Distinguish the source program from two different controls and an unproved 3D extension.
 add('M-PENROSE-2D','Penrose P3 · original quasicrystalline spatial model','model','partial','P0',summary='Two-dimensional Penrose graph/tiling and spectral-hypothesis model. Exact 3D interacting regulator remains unproved.',detail='Source Papers 1–4 and simulation archives do not automatically define the same operator. Distinguish graph Laplacian from gravitational fluctuation operator and from original-link SU(2) Hamiltonian.',tags=['primary-hypothesis','2D','penrose'],importance=5)
 add('M-SQUARE-2D','Square lattice · area-matched periodic control','model','finite','P0',summary='Area-matched 2D periodic spatial control (square_torus 151×151 vs model-set torus scale 55) in the 2+1D Stage7/26 SU(2) campaign; NOT the primary dissertation theory.',detail='Recovered Stage7 geometry code matches TOTAL PHYSICAL AREA; SU(2) couplings use calibrated anisotropic weights at reference beta 3.5. Identical sites, physical spectral operators and Monte Carlo uncertainty are NOT implied; Stage26 is not Paper 2 spectral zeta.',tags=['control','2D','square'],importance=5)
 lookup['M-CUBIC']['title']='Cubic 3D · quantum reference/control extension'
 lookup['M-CUBIC']['summary']='Genuine dyadic cubic 3D refinement and finite SU(2) transfer results; an independent control/reference, not a substitute for Penrose or a proved continuum equivalent.'
 lookup['M-Z5']['title']='Coupled ℤ⁵ · proposed (3+1)D Penrose extension'
 lookup['M-Z5']['summary']='Paper 2 proposes two extended Penrose spatial coordinates, compact third coordinate and imaginary-time interpretation. Source-certified interacting 3D refinement and dynamics remain OPEN.'
 lookup['M-PRISM']['title']='Extruded prism · distinct candidate, not coupled ℤ⁵'
 lookup['P0']['title']='P0 · Source-faithful model and controls'
 lookup['P0']['summary']='Two distinct mathematical tracks: Penrose spectral-gravity hypothesis and square/cubic control models, with explicit bridges required before transferring claims.'
 lookup['P0']['checks']=[
  chk('Penrose P3 2D graph and spectral-observable provenance','partial','Historical Papers 1–4 define proposed operators; the Stage26 operator is not yet shown equivalent to Paper 2 spectral-zeta operator.'),
  chk('Square control paired on the SAME observable and normalization','partial','Stage7 source constructs an area-matched square control; 8 matched-label sweeps use lags [4,6,8,10] and 600 planar pairs/seed. Source_sha256 identifies Stage9 checkpoints, not Python code; full runtime/uncertainty remain open.'),
  chk('Penrose coupled-ℤ⁵ genuine 3D oriented refinement and physical action','open','Paper 2 compact-third-coordinate identification is a proposal, not a source-certified interacting 3D mesh.'),
  chk('Cubic 3D reference geometry and finite gauge transfer','met','R3-IR-586/587/590 and later heat-kernel audit, CONTROL ONLY; no Penrose model identity or continuum mass gap.'),
  chk('Verified cross-model spectral/measure/operator comparison','open','No Penrose↔square/cubic equivalence, universality, or spectral-measure theorem from data matching alone.'),
  chk('Physically correct gravitational operator and separate YM continuum targets','open','One-loop spectral-zeta ratios, a regularized spectral-triple value, and an interacting gravity/YM theorem are different obligations.')]
 lookup['P0']['detail']='Cubic subcriteria cannot complete the Penrose P0. Model-indexed closure records are required; six YM gates and the separate quantum-gravity objective remain OPEN.'

 # Prevent misattribution of generic data families (half periodic controls) to coupled Z5.
 e[:]=[z for z in e if not ((z['from_id'] in ('D-ARCHIVE','D-SWEEPS') and z['to_id']=='M-Z5') or (z['from_id']=='M-CUBIC' and z['to_id']=='R-INDEX') or (z['from_id']=='W-LFS' and z['to_id']=='P0'))]
 lookup['W-LFS']['stage']=None
 lookup['W-LFS']['detail']='Data-custody infrastructure only: Git LFS migration is NOT a mathematical P0 acceptance condition.'
 edge('W-LFS','D-MANIFEST','custody-only','archive migration does not block proof')
 edge('M-PENROSE-2D','M-Z5','proposed-extension','Paper 2 kinematic construction, no interacting equivalence','open')
 edge('M-SQUARE-2D','M-CUBIC','control-extension','2D periodic control → independent 3D cubic benchmark, not model equivalence','open')
 edge('M-PENROSE-2D','P0','primary-model','2D source geometry still requires 3D and operator bridge','open')
 edge('M-SQUARE-2D','P0','control','not the target model')
 edge('M-PENROSE-2D','G-GRAV','primary-hypothesis','original spectral-geometry inquiry','open')
 edge('M-Z5','G-GRAV','proposed-physics','dynamics and UV operator not certified','open')
 edge('D-DISS','G-GRAV','historical-source','the original objective')
 edge('R-INDEX','PUB-DISS','catalog','theorem file counts do not certify claims')
 # Correct Stage26 leaf attribution with geometry-specific actual filenames.
 count={'penrose':0,'square':0}
 for x in n:
  if x['kind']=='dataset' and (x['asset']['kind'] in ('stage26','sweep10000','full_archive')):
   name=x['asset']['filename'];target=('M-PENROSE-2D' if name.startswith('penrose_') else 'M-SQUARE-2D' if name.startswith('square_') else None)
   assert target,(x['id'],name)
   count['penrose' if target=='M-PENROSE-2D' else 'square']+=1
   edge(x['id'],target,'experiment-provenance','2D source data; not a 3D action')
 assert count=={'penrose':9,'square':8},count

 audit_path='docs/research/P0_MODEL_HIERARCHY_PENROSE_CONTROL_AUDIT_2026-11-05.md'
 src=[{'title':'2026-11-05 independent model-identity audit','path':audit_path,'url':'https://github.com/syncgravity/singular-boundary/blob/audit/2026-11-05-penrose-primary-control/'+audit_path,'review_only':True}]
 paper_file=root.parent/'docs/evidence/P0_PENROSE_SQUARE_PAIRING_2026-11-05.json'
 if not paper_file.is_file():paper_file=root.parent/'pairing_audit.json'
 paperinfo=json.loads(paper_file.read_text())['paper_sources'] if paper_file.is_file() else None
 if paperinfo is None:
  raise RuntimeError('pairing_audit.json needed to pin authentic embedded dissertation paper PDFs')
 for i,p in enumerate(paperinfo,1):
  add('PAPER-'+str(i),f'Original dissertation Paper {i} · PDF in v10.7', 'result','indexed','P0',
      summary='Original historical source; read and verify its mathematical hypotheses before incorporating physical claims.',detail='Tar member: '+p['archive_member']+'; original SHA-256 '+p['sha256']+'; Library: /The Singular Boundary/Data/Original Uploads/Sharpe_dissertation_v10.7.tar.gz. Paper-level result is not a certified 4D theorem.',
      tags=['original-source','paper'],core=i<=4,importance=3,sources=src)
  edge('D-DISS','PAPER-'+str(i),'contains','PDF archived inside source tarball')
  edge('PAPER-'+str(i),'M-PENROSE-2D','source-context','historical theory proposal, not identical Stage26 operator')

 add('I-PENROSE-SQUARE','Penrose ↔ square · same-observable comparison gate','interface','open','P0',
     summary='Source-qualify the recovered Stage26 SU(2) 2+1D scalar observable versus the separate Paper 2 graph/spectral-zeta calculation, then compare Penrose/square control with correctly matched physics and independent error model.',
     detail='Paper 2 spectral-zeta suppression (~16.7%) is not a result from the Stage26 sweep-10,000 multihit files. Four same-label seeds and 600 pairs are descriptive; independent uncertainty and spectral-operator identity remain open.',
     checks=[chk('Audit recovered Stage26 runner and nested modules against complete run inputs'),chk('Source-qualify Paper 2 vs Stage26 operator/observable'),chk('Match physical units, scale/volume, coupling and boundaries'),chk('Establish sound sampling uncertainty and a falsifiable null comparison'),chk('Only then test claimed universal spectral differences')],sources=src,importance=5)
 edge('M-PENROSE-2D','I-PENROSE-SQUARE','compare','primary geometry');edge('M-SQUARE-2D','I-PENROSE-SQUARE','compare','periodic control')
 edge('I-PENROSE-SQUARE','P0','required-comparison','no spectral theorem inferred yet','open')
 add('W-ORIGINAL-SOURCES','Recover original generators and exact spectral operators','work','open','P0',summary='Stage26 runner/README have been located and read in historical Git archive. Next authenticate full dependencies/restart inputs, and separately recover Paper 1/2 graph spectral-zeta generators.',
     detail='Stage26 source located: stage26_outer.py Git blob 95423cfc83ba4774e160ac1e3dadc1fa964eca25. Its source_sha256 is Stage9 input checkpoint hash, NOT code SHA. Archived run dependencies and Paper 1/2 spectral-zeta generator must be independently authenticated.',checks=[chk('Authenticate recovered runner with original Stage9 checkpoint hashes, dependency stack, estimator and replay')],sources=src,importance=5)
 add('W-GRAV-OP','Gravitational fluctuation operator and UV finiteness bridge','work','open','P0',summary='Relate the quasicrystalline graph spectral object to a physically justified quantum gravitational operator and a precisely defined UV claim.',detail='An observed finite lattice zeta ratio or finite spectral-triple regularized quantity is not a nonperturbative gravitational path-integral finiteness theorem.',checks=[chk('Construct physically justified interacting gravitational operator and domains'),chk('Prove the correct continuum/cutoff claim in that operator')],sources=src,importance=5)
 edge('W-ORIGINAL-SOURCES','I-PENROSE-SQUARE','blocks','generator and operator provenance missing','open')
 edge('W-ORIGINAL-SOURCES','P0','blocks','authentic source linkage pending','open')
 edge('W-GRAV-OP','G-GRAV','blocks','physical UV operator required','open')
 edge('I-PENROSE-SQUARE','G-GRAV','conditional-evidence','spectral contrast alone does not prove gravitational finiteness','open')
 edge('G-GRAV','THEOREM','distinct-objectives','no logical implication without theorem','open')

 stage26_base='sources/historical/raw/Archive_4/Penrose_YM_Stage26_Outer_First_Connected_Scalar_Campaign.zip/__nested__/stage26_outer/'
 stage26_sources=[('stage26_outer.py','95423cfc83ba4774e160ac1e3dadc1fa964eca25'),('README_STAGE26.md','b552b9b42024a0a4dd4d577afc7d4a53a4b2b120'),('stage24_inner/deps_stage23/deps/stage17_mac/stage7_large_torus.py','c747ae3584148cc0f6e8907e529e6e742962194e')]
 for name,digest in stage26_sources:
  ref={'title':'Recovered Stage26 '+name+' (Git blob)','path':stage26_base+name,'git_blob_sha':digest,'url':'https://github.com/syncgravity/singular-boundary/blob/'+digest+'/'+stage26_base+name}
  lookup['I-PENROSE-SQUARE']['sources'].append(ref)
  lookup['W-ORIGINAL-SOURCES']['sources'].append(ref)
 g['sources_verified']['stage26runner']={'path':stage26_base+'stage26_outer.py','blob_sha':stage26_sources[0][1]}
 g['version']='v2.28-draft';g['build_date']='2026-11-05 (America/Denver)';g['git_branch']='audit/2026-11-05-penrose-primary-control'
 g['scope']='Two separate goals: original Penrose quantum-gravity hypothesis and SU(2) mass-gap objective. Square/cubic periodic controls are distinct; no model equivalence or continuum gap established.'
 g['primary_hypothesis']='Penrose/Fibonacci/coupled Z5';g['control_models']=['square 2D','cubic 3D'];g['dual_open_goals']=['G-GRAV','THEOREM']
 assert all(x['status']=='open' for x in n if x['kind'] in ('goal','gate'))
 assert len({x['id'] for x in n})==len(n)
 assert all(x['from_id'] in lookup and x['to_id'] in lookup for x in e)
 out_path.write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 (root/'knowledge-graph-data.js').write_text('window.SB_KNOWLEDGE_GRAPH='+json.dumps(g,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf8')
 return g

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent);cfg=a.parse_args();g=reconcile(cfg.root);print('PASS Penrose primary / controls separated:',len(g['nodes']),'nodes',len(g['edges']),'edges')
