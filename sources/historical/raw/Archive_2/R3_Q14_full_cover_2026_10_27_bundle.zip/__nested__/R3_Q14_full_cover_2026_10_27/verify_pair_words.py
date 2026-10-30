import numpy as np,json
from pathlib import Path
from direct_cut_project import build
from construct_surgery import product_collar
from pair_bounds import staples, inverse,ROOT

def mul(a,b):return np.r_[a[0]*b[0]-np.dot(a[1:],b[1:]),a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:])]
def conj(a):return a*np.array([1.,-1.,-1.,-1.])
def evalword(word,U):
 ans=np.array([1.,0.,0.,0.])
 for e,s in word:ans=mul(ans,U[e] if s==1 else conj(U[e]))
 return ans
rng=np.random.default_rng(67183);results=[]
for radius in [5.,6.5,8.,10.]:
 key=str(radius).replace('.','_');g,_=build(radius,0);W,_=product_collar(g)
 j=json.loads((ROOT/f'pair_staple_radius_{key}.json').read_text())
 n=max(e for w in W for e,s in w)+1;U=rng.standard_normal((n,4));U/=np.linalg.norm(U,axis=1)[:,None]
 largest=0.;gapmin=100.;ncheck=0
 for entry in j['entries']:
  e=entry['link'];st=staples(W,e,entry['incident_retained_faces']);
  for f,s in st.items():
   actual=evalword(W[f],U)[0];a=evalword(s,U)
   largest=max(largest,abs(actual-np.dot(U[e],a)))
  for item in entry['pairs']:
   i,h=item['face_a'],item['face_b'];left=mul(evalword(st[i],U),conj(evalword(st[h],U)))
   right=evalword(item['loop_word'],U)
   largest=max(largest,float(np.max(np.abs(left-right))))
   pi=1-evalword(W[i],U)[0];pj=1-evalword(W[h],U)[0];pair=1-right[0]
   gapmin=min(gapmin,2*(pi+pj)-pair);ncheck+=1
 assert largest<1e-12 and gapmin>-1e-10
 results.append({'radius':radius,'pairs_checked':ncheck,'largest_word_error':largest,'minimum_triangle_slack':gapmin})
print(results)
(ROOT/'pair_verification.json').write_text(json.dumps(results,indent=2))
