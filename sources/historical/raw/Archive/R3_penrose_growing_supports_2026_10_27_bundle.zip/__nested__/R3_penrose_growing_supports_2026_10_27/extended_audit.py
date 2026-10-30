#!/usr/bin/env python3
"""Genuine nested Penrose rhombus-prism relative-support audit.
Exact GF(p) ranks, combinatorial nonabelian Bianchi peeling,
conditional Gibbs locality and full-volume geometry provenance.
"""
import json,hashlib,time
import numpy as np
from pathlib import Path
from nested_audit import (build,validate,seed_support,embed_support,complex_3,
  rank_mod_columns,local_rank_audit,cell_boundaries,bianchi_peel,sparse_boundary_projection_rank)
ROOT=Path(__file__).resolve().parent

def canonlink(g,link):
 V,E=len(g.labels),len(g.edges);N=3*E
 if link<N:
  t,e=divmod(link,E);a,b=g.edges[e]
  return ('h',t,tuple(sorted((g.labels[a],g.labels[b]))))
 t,v=divmod(link-N,V);return ('v',t,g.labels[v])
def canonface(g,m):
 typ,t,k=m
 if typ=='s':return ('s',t,tuple(sorted(g.labels[v] for v in g.faces[k])))
 a,b=g.edges[k];return ('t',t,tuple(sorted((g.labels[a],g.labels[b]))))
def hash_canon(vals):return hashlib.sha256(json.dumps(sorted(vals),separators=(',',':')).encode()).hexdigest()

def get_star_seed(g):
 # Four-valent vertex at origin, and a neighboring 5-valent vertex at distance one.
 degree=np.bincount(np.asarray(g.edges).flatten(),minlength=len(g.labels))
 v0=int(np.argmin(np.linalg.norm(g.xy,axis=1)))
 assert degree[v0]==4
 neighbors=sorted(set(y if x==v0 else x for x,y in g.edges if x==v0 or y==v0))
 v1=min((n for n in neighbors if degree[n]>=5),key=lambda n:np.linalg.norm(g.xy[n])); assert degree[v1]>=5
 star0=[tuple(sorted((g.labels[a],g.labels[b]))) for a,b in g.edges if a==v0 or b==v0]
 star1=sorted([tuple(sorted((g.labels[a],g.labels[b]))) for a,b in g.edges if a==v1 or b==v1])[:4]
 return {'v0':g.labels[v0],'v1':g.labels[v1],'t0':star0,'t1':star1,'time0_degree':int(degree[v0])}
def get_star_Q(g,s):
 idx={tuple(sorted((g.labels[a],g.labels[b]))):e for e,(a,b) in enumerate(g.edges)}
 return {(0,idx[e]) for e in s['t0']}|{(1,idx[e]) for e in s['t1']}

def audit_support(g,cols,meta,cells,qs,localtag):
 Q=sorted(i for i,m in enumerate(meta) if m[0]=='t' and (m[1],m[2]) in qs)
 assert len(Q)==len(qs)
 Qset=set(Q);Ret=[c for f,c in enumerate(cols) if f not in Qset]
 L=set(e for f in Q for e in cols[f]);C=set(L);ranks=[];rad0_L=L.copy()
 for rad in range(3):
  ranks.append({'radius':rad,'adjustable_links':len(C),'rank_retained_local':rank_mod_columns(Ret,C),'rank_full_local':rank_mod_columns(cols,C)})
  if rad<2:C|={e for col in cols if C.intersection(col) for e in col}
 rankR=rank_mod_columns(Ret)
 rankF=3*len(g.edges)
 for d in ranks:
  d['rank_retained_exterior']=rankR-d['rank_retained_local'];d['rank_full_exterior']=rankF-d['rank_full_local']
  d['exterior_rank_increase']=d['rank_full_exterior']-d['rank_retained_exterior']
 # all faces that touch local links, including Q; defines exact conditional integral
 influenced=[f for f,col in enumerate(cols) if L.intersection(col)];boundary=set()
 for f in influenced:boundary.update(set(cols[f])-L)
 locality={'local_links':len(L),'affected_retained_faces':len(set(influenced)-Qset),
           'local_interacting_faces_including_Q':len(influenced),
           'boundary_exterior_links':len(boundary),
           'local_link_hash':hash_canon([canonlink(g,e) for e in L]),
           'local_face_hash':hash_canon([canonface(g,meta[f]) for f in influenced]),
           'boundary_link_hash':hash_canon([canonlink(g,e) for e in boundary]),
           'max_incident_face_count_per_link':max(sum(e in col for col in cols) for e in L)}
 # exact nonabelian cell Bianchi peeling certificates
 peel,left,exp=bianchi_peel(cols,cells,Q)
 assert all(not set(e)&Qset for e in exp.values())  # if fully peeled
 for q,v in exp.items():
  # direct integer signed incidence check D_q=sum h D_r
  target=cols[q];reconstructed={}
  for f,coef in v.items():
   for e,a in cols[f].items():reconstructed[e]=reconstructed.get(e,0)+coef*a
  assert all(reconstructed.get(e,0)==target.get(e,0) for e in set(target)|set(reconstructed))
 bianchi={'q_projection_rank':sparse_boundary_projection_rank(cells,Q),
         'peelable_Q_count':len(peel),'unpeeled_Q_count':len(left),
         'elimination_max_expanded_face_count':max((sum(map(abs,v.values())) for v in exp.values()),default=0),
         'distinct_elimination_cells':len({x['cell'] for x in peel}),
         'selected_cell_fingerprints':hash_canon([('c',f//len(g.faces),tuple(sorted(g.labels[v] for v in g.faces[f%len(g.faces)]))) for f in [x['cell'] for x in peel]]),
         'nonabelian_word_meaning':'products of transported plaquette words via six-face cell boundaries; bound counts face factors, not transport-link length'}
 if not left:
  nonlinear={}
  for q,expr in exp.items():
   ell=sum(map(abs,expr.values()))
   for face,co in expr.items():nonlinear[face]=nonlinear.get(face,0)+ell*abs(co)
  bianchi['retained_faces_in_expanded_repair']=len(nonlinear)
  bianchi['pointwise_nonlinear_energy_coefficient']=max(nonlinear.values())
  bianchi['max_retained_face_multiplicity']=max(sum(abs(exp[q].get(face,0)) for q in exp) for face in nonlinear)
  # Noncommutative Bianchi words do not permit cancellation merely because the signed
  # abelian face coefficients cancel: track each transported factor with multiplicity.
  from collections import Counter
  occurrences={}
  for op in peel:
   q=op['face']; terms=Counter()
   for face in cells[op['cell']]:
    if face==q:continue
    terms.update(occurrences[face] if face in occurrences else {face:1})
   occurrences[q]=terms
  weight=Counter()
  for terms in occurrences.values():
   length=sum(terms.values())
   weight.update({face:length*count for face,count in terms.items()})
  bianchi['max_nonabelian_face_factor_count']=max(sum(terms.values()) for terms in occurrences.values())
  bianchi['nonlinear_curvature_coefficient_certified']=max(weight.values())
  bianchi['nonabelian_retained_face_support_count']=len(weight)
 if localtag=='star8':
  # Temporal link of four-valent central spatial vertex only appears in four inserted faces at t=0.
  v0=int(np.argmin(np.linalg.norm(g.xy,axis=1)));free_edge=3*len(g.edges)+v0
  incoming=[i for i,col in enumerate(cols) if free_edge in col]
  assert set(incoming).issubset(Qset) and len(incoming)==4
  bianchi['released_link_exact_Haar_coordinate']={'canonical_key':canonlink(g,free_edge),'incident_faces':len(incoming),'incident_retained_faces':0,'interpretation':'one ordinary temporal SU(2) link has exactly normalized Haar law under the retained cavity'}
 if left:
  bianchi['unpeeled_face_fingerprints']=[canonface(g,meta[q]) for q in sorted(left)]
 return {'tag':localtag,'Q_face_count':len(Q),'Q_face_fingerprints':[canonface(g,meta[q]) for q in Q],
  'global_rank_retained':rankR,'global_rank_full':rankF,
  'additional_global_rank':rankF-rankR,'collar':ranks,'conditional_locality':locality,'bianchi':bianchi}

def main():
 g5,_=build(5,0);seed=seed_support(g5);star=get_star_seed(g5)
 out=[];prev_geo=None
 for r in [5.,6.5,8.,10.]:
  t0=time.time();g,gamma=build(r,0);report=validate(g,gamma)
  if prev_geo:
   assert prev_geo['v'].issubset(set(g.labels)) and prev_geo['f'].issubset({tuple(sorted(g.labels[i] for i in f)) for f in g.faces})
  prev_geo={'v':set(g.labels),'f':{tuple(sorted(g.labels[i] for i in f)) for f in g.faces}}
  cols,meta=complex_3(g);cells=cell_boundaries(g)
  # independent chain d2*d3=0 without constructing dense matrices
  for cc in cells:
   vec={}
   for f,x in cc.items():
    for e,a in cols[f].items():vec[e]=vec.get(e,0)+x*a
   assert not any(vec.values())
  ids,support14=embed_support(seed,g)
  support8=get_star_Q(g,star)
  one={'radius':r,'geometry':report,'links_3d':3*(report['vertices']+report['edges']),
       'faces_3d':3*(report['faces']+report['edges']),'cells_3d':3*report['faces'],
       'supports':{'overlapping14':audit_support(g,cols,meta,cells,support14,'overlapping14'),
                   'star8':audit_support(g,cols,meta,cells,support8,'star8')},
       'seconds':round(time.time()-t0,3)}
  out.append(one)
  print('R',r,'spatial',report['faces'],'Q outcomes',
       {k:(v['additional_global_rank'],[(x['adjustable_links'],x['exterior_rank_increase']) for x in v['collar']],v['bianchi']['peelable_Q_count']) for k,v in one['supports'].items()},'time',one['seconds'],flush=True)
 # exact ambient-invariance checks on conditional local functions: same canonical local link/face/neighbor data
 for key in ('overlapping14','star8'):
  h=out[0]['supports'][key]['conditional_locality']
  for x in out[1:]:
   H=x['supports'][key]['conditional_locality']
   for c in ['local_links','affected_retained_faces','local_interacting_faces_including_Q','boundary_exterior_links','local_link_hash','local_face_hash','boundary_link_hash']:
    assert H[c]==h[c],(key,x['radius'],c,h[c],H[c])
   assert x['supports'][key]['bianchi']['elimination_max_expanded_face_count']==out[0]['supports'][key]['bianchi']['elimination_max_expanded_face_count']
 cert={'description':'actual nested regular Z5 Penrose disks with three-step periodic prism extrusion; exact modulo-prime ranks; six-face nonabelian peeling and conditional Gibbs locality','source':'unchanged direct_cut_project.py from verified uploaded Phase III bundle','offset':0,'radii':[5.,6.5,8.,10.],
  'fixed_spatial_labels':{'overlapping14_faces':[list(map(list,face)) for face in seed['face_labels']],
                          'star8_vertex_0':list(star['v0']),'star8_vertex_1':list(star['v1']),
                          'star8_t0_links':[list(map(list,x)) for x in star['t0']],
                          'star8_t1_links':[list(map(list,x)) for x in star['t1']]},
  'results':out,'limits':'No sampled exterior Gibbs marginals, nonlinear curved-config repair transport, or all-support theorem; conditional locality of the function is not a uniform lower bound on its expectation.'}
 (ROOT/'certificate.json').write_text(json.dumps(cert,indent=2,default=lambda x:list(x) if isinstance(x,tuple) else int(x)))
 print('PASS: all checks, hashes and ranks',flush=True)
if __name__=='__main__':main()
