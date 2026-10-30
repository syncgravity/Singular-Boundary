import json, numpy as np
from pathlib import Path
from direct_cut_project import build
from construct_surgery import product_collar,shell
from cavity_audit import seed_support,Q_from_seed
ROOT=Path(__file__).resolve().parent
g,_=build(5.,0); words,meta=product_collar(g);Q=Q_from_seed(g,seed_support(g));R=set(range(len(words)))-Q
H={e for q in Q for e,s in words[q]};K=shell(H,words,R);A={p for p in R if any(e in H for e,s in words[p])}

def red(w,cyclic=True):
 st=[]
 for x in w:
  if st and st[-1]==-x:st.pop()
  else:st.append(x)
 if cyclic:
  while len(st)>=2 and st[0]==-st[-1]:st=st[1:-1]
 return tuple(st)
def inv(w):return tuple(-x for x in reversed(w))

def eliminate(exterior):
 free=set(e+1 for e in H);released=exterior+1
 rel={f:red([s*(e+1) for e,s in words[f] if e in H or e==exterior]) for f in A}
 areas={f:{f:1} for f in A}
 ops=[]
 for it in range(70):
  opts=[]
  for f,w in rel.items():
   for j,x in enumerate(w):
    if abs(x) in free and sum(abs(y)==abs(x) for y in w)==1:
     freq=sum(sum(abs(z)==abs(x) for z in ww) for ww in rel.values())
     opts.append(((len(w)-1)*(freq-1),len(w),f,j))
  if not opts:break
  _,__,f,j=min(opts);w=rel.pop(f);elim_area=areas.pop(f);x=w[j];a=abs(x);rest=w[j+1:]+w[:j]
  subst=inv(rest) if x>0 else rest;mp={a:subst,-a:inv(subst)}
  for ff,ww in list(rel.items()):
   z=[];cnt=0
   for v in ww:
    if abs(v)==a:z.extend(mp[v]);cnt+=1
    else:z.append(v)
   rel[ff]=red(z)
   for f0,number in elim_area.items():areas[ff][f0]=areas[ff].get(f0,0)+cnt*number
  free.remove(a);ops.append({'face':int(f),'eliminated_edge':int(a-1),'replacement_length':len(subst)})
  if max((len(w) for w in rel.values()),default=0)>100000:break
 exterior_words=[(f,tuple(int(x//abs(x)) for x in w)) for f,w in rel.items() if w and set(abs(x) for x in w)=={released}]
 return {'e':int(exterior),'H_pivots':len(ops),'H_remaining':len(free),'maximum_residual_word_length':max((len(w) for w in rel.values()),default=0),
         'pure_exterior_relators':[(int(f),list(w)) for f,w in exterior_words],
         'pure_exterior_relator_area':{str(f): {str(k):int(v) for k,v in sorted(areas[f].items())} for f,w in exterior_words},
         'pure_exterior_relator_factor_upper':{str(f):int(sum(areas[f].values())) for f,w in exterior_words},'operations':ops,
         'unresolved_relators_count':sum(bool(w) for w in rel.values())}

def rank_mod(mat,prime):
 x=np.array(mat,dtype=np.int64)%prime; r=0
 for c in range(x.shape[1]):
  if r>=x.shape[0]:break
  valid=np.flatnonzero(x[r:,c]);
  if len(valid)==0:continue
  i=r+int(valid[0]);x[[r,i]]=x[[i,r]]
  x[r]=(x[r]*pow(int(x[r,c]),-1,prime))%prime
  for ii in range(r+1,x.shape[0]):
   if x[ii,c]:x[ii]=(x[ii]-x[ii,c]*x[r])%prime
  r+=1
 return r

def main():
 D=np.zeros((len(A),len(H)),dtype=np.int64);Hlist=sorted(H);Alist=sorted(A)
 for i,f in enumerate(Alist):
  for j,e in enumerate(Hlist):
   D[i,j]=next((s for ee,s in words[f] if e==ee),0)
 rr=rank_mod(D,1000003);assert rr==rank_mod(D,1000033)==35,rr
 witness=[]
 for e in sorted(K-H):
  vec=np.array([next((s for ee,s in words[f] if e==ee),0) for f in Alist],dtype=np.float64)
  if rank_mod(np.column_stack((D,vec)).astype(np.int64),1000003)>rr and rank_mod(np.column_stack((D,vec)).astype(np.int64),1000033)>rr:
   r=eliminate(e)
   witness.append({'edge':int(e),'pure_exterior_relators':r['pure_exterior_relators'],'H_pivots':r['H_pivots'], 'H_remaining':r['H_remaining'], 'max_residual':r['maximum_residual_word_length']})
   print('candidate',e,'pure relators',r['pure_exterior_relators'][:2],'eliminations',r['H_pivots'], 'remaining',r['H_remaining'],flush=True)
   if r['pure_exterior_relators']:
    (ROOT/'nonabelian_single_link_witness.json').write_text(json.dumps({'summary':witness,'selected_witness':r},indent=2));break
 (ROOT/'nonabelian_candidates.json').write_text(json.dumps(witness,indent=2))
if __name__=='__main__':main()
