import json, itertools, collections, numpy as np
from pathlib import Path
from direct_cut_project import build
from construct_surgery import product_collar
from solve_cover import ROOT

def inverse(w):return [(e,-s) for e,s in reversed(w)]
def reduce_word(w):
 z=[]
 for e,s in w:
  if z and z[-1]==(e,-s):z.pop()
  else:z.append((e,s))
 return z

def staples(W,e,faces):
 res={}
 for f in faces:
  pos=next(i for i,(x,_) in enumerate(W[f]) if x==e)
  word=W[f];sign=word[pos][1];tail=word[pos+1:]+word[:pos]
  res[f]=inverse(tail) if sign==1 else tail
 return res

def main():
 report=[]
 for radius in [5.,6.5,8.,10.]:
  suffix=str(radius).replace('.','_');c=json.loads((ROOT/f'cover_radius_{suffix}.json').read_text())
  g,_=build(radius,0);W,_=product_collar(g)
  entries=[];edges=c['selected_cover_edges']; paircount=0;length_hist=collections.Counter();nstar=collections.Counter();maxw=0
  R=set(range(len(W)))-set(c['Q']);
  for e in edges:
   faces=c['selected_cover_star_faces'][str(e)]; st=staples(W,e,faces);n=len(faces);nstar[n]+=1
   combos=[]
   for f,h in itertools.combinations(faces,2):
    word=reduce_word(list(st[f])+inverse(st[h]));length_hist[len(word)]+=1;maxw=max(maxw,len(word))
    combos.append({'face_a':f,'face_b':h,'loop_word':[[int(x),int(s)] for x,s in word], 'loop_length':len(word)})
   paircount+=len(combos)
   entries.append({'link':e,'n_star':n,'incident_retained_faces':faces,'pairs':combos})
  cert={'radius':radius,'selected_cover_link_count':len(edges),'total_pair_staple_loops':paircount, 'max_free_reduced_loop_length':maxw,'length_histogram':dict(length_hist),'star_degree_histogram':dict(nstar),'entries':entries,
  'analytic_SU2_bounds':{'exact':'m_e=2 sum_{i<j} d(a_i a_j^-1)/(n_e+R_e), R_e=norm(sum a_i)','pair_triangle':'d(a_i a_j^-1) <= 2(d(W_i)+d(W_j))','frustration_pair_bound':'m_e <= 2/n_e sum_{i<j}d(a_i a_j^-1)','small_curvature_improvement':'if sum_i d(W_i)<=delta then R_e>=n_e-delta and m_e<=2/(2n_e-delta) sum_{i<j} d(a_i a_j^-1), for 0<=delta<n_e'}}
  (ROOT/f'pair_staple_radius_{suffix}.json').write_text(json.dumps(cert,separators=(',',':')))
  report.append({'radius':radius,'loops':paircount,'max_reduced_word_length':maxw,'star_degree_histogram':dict(nstar),'word_lengths':dict(length_hist)})
  print(report[-1],flush=True)
 (ROOT/'pair_summary.json').write_text(json.dumps(report,indent=2))
if __name__=='__main__':main()
