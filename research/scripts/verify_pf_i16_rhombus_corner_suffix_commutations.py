#!/usr/bin/env python3
"""Test whether the common P-edge pair restriction can be moved to a suffix.

Adjacent swaps are accepted only when both orders are valid elementary collapses
and yield exactly the same residual cell inventory.
"""
from __future__ import annotations
import argparse,gzip,hashlib,itertools,json,zipfile
from collections import Counter
from pathlib import Path
EXPECTED={
 "collapse":"d0d96755ceaa556759f6d5a2d0f60d0df1cd5f9805b12e5461c6d1747f6f8141",
 "diagrams":"aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba",
 "inventory":"("5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f", "3e50240bf1b037f3de8dd4e4c4ab94d4523533c25ceeab4000410c641cf07b77")"}
def load(path,expected):
 raw=path.read_bytes()
 if zipfile.is_zipfile(path):
  with zipfile.ZipFile(path) as z:
   names=z.namelist();assert len(names)==1,names;raw=z.read(names[0])
 if path.suffix=='.gz' or raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
 h=hashlib.sha256(raw).hexdigest();assert (h in expected if isinstance(expected,(tuple,list,set)) else h==expected),(path,h,expected)
 return json.loads(raw),h
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def edge(a,b):return tuple(sorted((tuple(a),tuple(b))))
def face_vertices(r):
 m=tuple(r['lower']);j,k=r['directions'];ej=tuple(int(i==j) for i in range(5));ek=tuple(int(i==k) for i in range(5));return {m,add(m,ej),add(add(m,ej),ek),add(m,ek)}
def face_edges(r):
 v=sorted(face_vertices(r));return {edge(a,b) for a,b in itertools.combinations(v,2) if sum(abs(x-y) for x,y in zip(a,b))==1}
def union(face_ids,fv,fe):
 F=set(face_ids);E=set().union(*(fe[i] for i in F));V=set().union(*(fv[i] for i in F));return {'F':F,'E':E,'V':V}
def sequence(path):
 out=[]
 for st in ('first_relative_collapse','second_relative_collapse'):
  for x in path[st]['face_edge_pairs']:out.append(('FE',edge(*x['free_edge']),int(x['removed_face'])))
  for x in path[st]['edge_vertex_pairs']:out.append(('EV',tuple(x['free_vertex']),edge(*x['removed_edge'])))
 return out
def apply(state,p,target,fv,fe):
 F=set(state['F']);E=set(state['E']);V=set(state['V'])
 if p[0]=='FE':
  _,e,f=p;inc={q for q in F if e in fe[q]}
  if e not in E or f not in F or e in target['E'] or f in target['F'] or inc!={f}:return None
  F.remove(f);E.remove(e)
 else:
  _,v,e=p;incE={q for q in E if v in q};incF={q for q in F if v in fv[q]}
  if v not in V or e not in E or v in target['V'] or e in target['E'] or incE!={e} or incF:return None
  E.remove(e);V.remove(v)
 return {'F':F,'E':E,'V':V}
def replay(seq,start,target,fv,fe):
 s={k:set(v) for k,v in start.items()}
 for p in seq:
  s=apply(s,p,target,fv,fe)
  if s is None:return None
 return s
def isP(p,P):return (p[1] if p[0]=='FE' else p[2]) in P
def move_suffix(seq,start,target,P,fv,fe):
 seq=list(seq);swaps=0
 for right in range(len(seq)-1,0,-1):
  for j in range(right):
   if isP(seq[j],P) and not isP(seq[j+1],P):
    a,b=seq[j],seq[j+1];s0=replay(seq[:j],start,target,fv,fe)
    if s0 is None:return None,swaps,('prefix-invalid',j)
    ab=apply(s0,a,target,fv,fe);ab=apply(ab,b,target,fv,fe) if ab is not None else None
    ba=apply(s0,b,target,fv,fe);ba=apply(ba,a,target,fv,fe) if ba is not None else None
    if ab is None or ba is None or ab!=ba:return None,swaps,(j,a,b,ab is not None,ba is not None)
    seq[j],seq[j+1]=b,a;swaps+=1
 end=replay(seq,start,target,fv,fe)
 if end is None:return None,swaps,('replay-invalid',)
 return seq,swaps,None
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--collapse',type=Path,required=True);ap.add_argument('--diagrams',type=Path,required=True);ap.add_argument('--inventory',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
 col,ch=load(a.collapse,EXPECTED['collapse']);dia,dh=load(a.diagrams,EXPECTED['diagrams']);inv,ih=load(a.inventory,EXPECTED['inventory'])
 fv=[face_vertices(x) for x in inv['face_key_table']];fe=[face_edges(x) for x in inv['face_key_table']]
 lookup={(pi,wi):w for pi,pair in enumerate(dia['per_pair']) for wi,w in enumerate(pair['graph5_witnesses'])}
 counts=Counter();type_counts=Counter();rows=[];distinct=set();n=0
 for w in col['families']['graph5']['witness_results']:
  pi,wi=w['pair_index'],w['witness_index'];dw=lookup[(pi,wi)];supports=dw['support_face_indices']
  for pm in w['permutation_results']:
   pmap=pm['source_to_support_isomorphism']
   for cert in pm['diamond_certificates']:
    if cert['same_elementary_pair_set'] or cert['source_mark_pair']!=[1,2]:continue
    L=sequence(cert['path_delete_m_then_n']);R=sequence(cert['path_delete_n_then_m']);D=set(L)^set(R)
    F={x[2] for x in D if x[0]=='FE'};E={x[1] if x[0]=='FE' else x[2] for x in D};V={x[1] for x in D if x[0]=='EV'}
    if (len(F),len(E),len(V),len(D))!=(1,2,1,4):continue
    P=fe[next(iter(F))]-E;assert len(P)==2
    removed={pmap[i] for i in cert['source_mark_pair']};remain=[i for i in range(4) if i not in removed]
    A=union(set().union(*(set(supports[i]) for i in remain)),fv,fe);X=union(set().union(*(set(supports[i]) for i in range(4))),fv,fe)
    outputs=[]
    for label,seq in [('left',L),('right',R)]:
     assert replay(seq,X,A,fv,fe)==A,(pi,wi,label,'original replay failed')
     moved,swaps,block=move_suffix(seq,X,A,P,fv,fe);ok=block is None
     if ok:
      ids=[i for i,p in enumerate(moved) if isP(p,P)];assert ids==[len(moved)-2,len(moved)-1]
      suffix=moved[-2:]
     else:suffix=None
     outputs.append({'path':label,'movable_to_suffix_by_valid_adjacent_swaps':ok,'valid_swaps':swaps,'first_blocker':block,'suffix':suffix})
    both=all(x['movable_to_suffix_by_valid_adjacent_swaps'] for x in outputs)
    counts['both_suffix' if both else 'blocked']+=1
    if not both:
     b1=outputs[0]['first_blocker'];b2=outputs[1]['first_blocker'];same=(b1[1:3]==b2[1:3])
     counts['same_first_blocker' if same else 'different_first_blocker']+=1
     if same:type_counts[(b1[1][0],b1[2][0])]+=1
     assert same,(pi,wi,b1,b2)
    else:assert outputs[0]['suffix']==outputs[1]['suffix'],(pi,wi,outputs)
    n+=1;distinct.add(w['witness_id'])
    rows.append({'pair_index':pi,'witness_index':wi,'root_preserving_map':pmap,'paths':outputs,'both_paths_share_suffix_after_valid_swaps':both})
 assert n==64 and len(distinct)==32
 assert counts['both_suffix']==16 and counts['blocked']==48 and counts['same_first_blocker']==48
 result={'schema':'PF-I16-RHOMBUS-CORNER-SUFFIX-COMMUTATION-AUDIT-v1','inputs':{'collapse_payload_sha256':ch,'diagrams_payload_sha256':dh,'inventory_payload_sha256':ih},'scope':'64 graph-5 Ngrid=12 minimal four-cell certificates; source marks [1,2]; both root-preserving maps','counts':{'certificates':n,'distinct_geometric_witnesses':len(distinct),'both_paths_suffix_movable_by_valid_adjacent_swaps':counts['both_suffix'],'blocked_in_both_paths':counts['blocked'],'blocked_cases_with_identical_first_blocker_in_both_paths':counts['same_first_blocker'],'first_blocker_pair_type_histogram':[{'P_pair':k[0],'interfering_pair':k[1],'count':v} for k,v in sorted(type_counts.items())]},'conclusions':{'16_cases_have_a_common_P_edge_pair_suffix_after_valid_adjacent_swaps':True,'48_cases_do_not_admit_that_naive_suffix_move':True,'in_all_48_blocked_cases_the_first_interfering_pair_is_identical_in_both_paths':True,'the_blocker_may_be_part_of_a_larger_common_local_block':True,'no_claim_that_the_larger_block_has_been_reordered_or_certified':True,'global_restriction_naturality_not_proved':True,'geometric_L8_closed':False},'rows':rows}
 a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result['counts'],sort_keys=True))
if __name__=='__main__':main()
