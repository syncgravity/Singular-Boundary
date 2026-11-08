from pathlib import Path
import ast,hashlib,json,zipfile,re
P=Path('/mnt/data/early_papers_source_audit')
Z=Path('/mnt/data/Archive(1).zip')
TITLES={
 'paper1.pdf':'Spectral Dimension Flow and Gravitational Finiteness on the Fibonacci Lattice',
 'paper2.pdf':'Spectral Dimension Flow on the Penrose Tiling: From Two-Dimensional Quasicrystalline Structure to the Kaluza-Klein Bridge',
 'paper3.pdf':'The Gravitational Path Integral on the Penrose Lattice: From Z5 to Minkowski’s World via Lapidus Complex Dimensions',
 'paper4.pdf':'The Complex Structure of Quasicrystalline Spacetime: The J-Operator and the Hidden Domain',
 'paper5.pdf':'Spectral Identity on the Penrose Lattice: The Heat Kernel as Locational Observable and the Constitutive Hypothesis of Position',
 'paper5_appendix.pdf':'Appendix to Paper 5: Experimental Design for Detection of Quasicrystalline Spectral Signatures',
 'paper6.pdf':'The Conformal Boundary of Quasicrystalline Spacetime: Λ as a Function on Perpendicular Space',
 'paper7.pdf':'The Analytic Structure of Spectral Suppression on the Penrose Lattice: Failure Bands, the Complementary Pair Identity, and the Cosmological Constant',
 'paper8.pdf':'The Walker’s Path: Neural Coherence, Synchronicity, and Failure Correction on the Quasicrystalline Lattice',
}
ROLES={
 'paper1_compute.py':'Fibonacci-chain Hamiltonian and regular/Fibonacci Laplacians; heat-kernel spectral-flow diagnostics',
 'paper2_computation.py':'Robinson-triangle subdivision, Delaunay/filter graph and spectral computation (one implementation)',
 'paper2_compute.py':'de Bruijn pentagrid P3 tiles, Fibonacci hopping, Conway-worm and spectral-dimension calculations (distinct implementation)',
 'paper3_compute.py':'P3 integer labels, scalar Laplacian and Z5 coordinate/compact-direction and spectral-zeta diagnostics',
 'paper3_coupled_compute.py':'P3 indexed vertices and all accepted original-basis nearest neighbors; coupled-named scalar Laplacian, comparator and zeta ratios',
 'paper5_compute.py':'position-resolved heat kernel/identity/phason and spectral-temperature computations',
 'paper6_convergence_compute.py':'finite P3/basis incidence, scalar zeta and conformal/gradient diagnostics across cutoffs',
 'paper6_figures.py':'finite-graph observables, corrected mass-relative log determinant and figures',
 'zeta_prime_validation.py':'zeta-prime/relative determinant validation and comparison of multiple finite model operators',
}
with zipfile.ZipFile(Z) as z:
 contents={Path(n).name:z.read(n) for n in z.namelist() if not n.startswith('__MACOSX/') and not n.endswith('/')}
 assert all(contents[x].startswith(b'%PDF') for x in TITLES)
 assert all(x in contents for x in ROLES)
 manuscripts=[]
 for file,title in TITLES.items():
  manuscripts.append({'archival_filename':file,'content_title':title,'sha256':hashlib.sha256(contents[file]).hexdigest(),'archival_number_is_order':False,'matches_titlepage_text':True})
 programs=[]
 for file,role in ROLES.items():
  source=contents[file].decode('utf-8')
  node=ast.parse(source,filename=file)
  func=[x.name for x in node.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))]
  programs.append({'archival_filename':file,'sha256':hashlib.sha256(contents[file]).hexdigest(),'code_role_by_inspection':role,'defined_functions':func,'self_reported_header':(ast.get_docstring(node) or '').strip().splitlines()[:7], 'archival_number_is_order':False,'matching_number_implies_manuscript_dependency':False})
 data={'provenance':'User supplied Archive(1).zip','zip_sha256':hashlib.sha256(Z.read_bytes()).hexdigest(),'method':'content-title and parsed-function source crosswalk, NO chronological or causal inference from filenames','manuscripts':manuscripts,'programs':programs,'interpretation_rules':['Manuscript archival file numbers are storage identifiers only; do not infer order, revision, or substantive dependence from their suffixes.','Script filename numbers are likewise not proof of manuscript ownership, execution order, or model consistency.','Where a source file itself documents reliance on another dataset or code version, record that as source-reported only, then verify import, invocation or input provenance.','Geometry and numerical equivalence must be validated from mathematical definitions, inputs, actual integer vertex/edge/operator arrays, and output hashes.','The reported finite PF-I6 matched central window checks are about their recorded functions and inputs, independent of any paper-name order.','Any printed in-text references such as Paper N are historical text and must not substitute for source-content identity.']}
 path=P/'PF_I6_TITLE_FIRST_SOURCE_CROSSWALK_2026_11_07.json'
 path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
 lines=['# PF-I6 source-identity erratum — manuscript titles, not file numbers','', '**Date:** 2026-11-07 · **User correction:** disregard numbering in paper archive filenames.', '', 'The source analysis below is indexed by **printed title, SHA-256, implemented algorithm, and verified inputs/outputs**. Number-like filename suffixes are preserved solely to locate raw archive members. They are **not** evidence of chronology, a revision chain, or one-to-one script↔manuscript ownership.', '', '## Manuscripts identified by content', '', '| Content title | Raw archive member (locator only) | SHA-256 prefix |', '|---|---|---|']
 for o in manuscripts:
  lines.append(f"| {o['content_title']} | `{o['archival_filename']}` | `{o['sha256'][:16]}` |")
 lines+=['','## Executables identified by code behavior','','| Code behavior or outputs | Raw archive member (locator only) | SHA-256 prefix |','|---|---|---|']
 for o in programs:
  lines.append(f"| {o['code_role_by_inspection']} | `{o['archival_filename']}` | `{o['sha256'][:16]}` |")
 lines+=['','## Corrected research interpretation','', 'The finite PF-I6 test compared **two specific algorithms and their actual integer-labeled vertex/edge sets**, not successive numbered papers. A de Bruijn grid-intersection P3 constructor and an independent accepted-window cut-and-project constructor matched on four central disks **when their offsets, selection and crop were matched**. Two named Laplacians (tile-edge enumeration and all accepted-basis-neighbor enumeration) differed at some larger *finite* grid cutoffs because the tile enumerator omitted ordinary boundary rhombi; that difference is verified at the level of the concrete source functions. These facts do **not** establish chronology, an independent second physical dimension, the source identity of the merged-final dissertation, or the quantum mass gap.', '', 'The old PF-I6 report is preserved with a visible addendum pointing here. The Observatory must not use filename numbering to infer computational dependencies or research lineage. Dependencies are asserted only when an actual code import, function call, data read, explicit source claim, or mathematical equality supports them. Where an input is absent, mark that dependency **unverified**.', '', '**Verification boundary:** Nine script files AST-parsed, nine manuscript/appendix titles read from extracted title pages, all file hashes independently calculated from original ZIP members. This is not a claim to have independently executed every script end-to-end or recovered the large eigenspectrum input arrays.', '']
 (P/'PF_I6_TITLE_FIRST_SOURCE_CROSSWALK_2026_11_07.md').write_text('\n'.join(lines))
 print('wrote',len(manuscripts),'title records,',len(programs),'script records, original ZIP SHA',data['zip_sha256'])
