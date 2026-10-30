"""Locally portable replica of the prespecified Phase III admission metrics."""
from collections import Counter,deque
from pathlib import Path
import numpy as np
def ball(g,n):
 a=adj(g)
 if len(g.xy): root=int(np.argmin(np.sum((g.xy-np.mean(g.xy,axis=0))**2,axis=1)))
 else:root=0
 seen={root};q=deque([root]);order=[]
 while q and len(order)<n:
  u=q.popleft();order.append(u)
  for v in sorted(a[u]):
   if v not in seen:seen.add(v);q.append(v)
 return sorted(order)
OUT=Path(__file__).parent

def adj(g):
 a=[set() for _ in g.labels]
 for u,v in g.edges:a[u].add(v);a[v].add(u)
 return a

def tv(c,d):
 n=sum(c.values());m=sum(d.values())
 return .5*sum(abs(c[k]/n-d[k]/m) for k in c.keys()|d.keys())

def profile(g,S):
 a=adj(g);sel=set(S); full={v:len(a[v]) for v in S}; inside={v:len(a[v]&sel) for v in S}
 # rooted neighborhoods of selected induced graph; boundary distance restricted to a full two-hop ball before comparing
 lab0={v:(inside[v],) for v in S}
 lab1={v:(inside[v], tuple(sorted(inside[w] for w in a[v]&sel))) for v in S}
 # WL-style r2 rooted signature using shared r1 labels, with deterministic tuple ordering
 lab2={v:(lab1[v],tuple(sorted(lab1[w] for w in a[v]&sel))) for v in S}
 faces=[f for f in g.faces if all(v in sel for v in f)]
 fc=Counter(v for f in faces for v in f)
 faceedge=Counter(tuple(sorted((u,v))) for f in faces for u,v in zip(f,f[1:]+f[:1]))
 cuts=sum(full[v]-inside[v] for v in S)
 return dict(N=len(S),degree=Counter(inside.values()),root1=Counter(lab1.values()),root2=Counter(lab2.values()),faceinc=Counter(fc.get(v,0) for v in S),cut=cuts,faces=len(faces),faceedge=Counter(faceedge.values()),m2=sum(inside[v]**2+inside[v] for v in S)/len(S),mean_degree=np.mean(list(inside.values())))

def cmp(a,b):
 return {'degree_tv':tv(a['degree'],b['degree']),'radius1_tv':tv(a['root1'],b['root1']),'radius2_tv':tv(a['root2'],b['root2']),'face_incidence_tv':tv(a['faceinc'],b['faceinc']),'boundary_cut_relative_delta':abs(a['cut']-b['cut'])/max(1,(a['cut']+b['cut'])/2),'second_moment_delta':a['m2']-b['m2'],'penrose_cut':a['cut'],'periodic_cut':b['cut'],'penrose_faces':a['faces'],'periodic_faces':b['faces']}

# Predeclared strict thresholds: all must pass. No after-the-fact relaxed selection.
THRESHOLDS={'degree_tv':.05,'radius1_tv':.10,'radius2_tv':.15,'face_incidence_tv':.10,'boundary_cut_relative_delta':.10,'second_moment_delta_abs':.2}
def admitted(r):return all(abs(r[k])<=v if k=='second_moment_delta_abs' else r[k]<=v for k,v in THRESHOLDS.items() if k!='second_moment_delta_abs') and abs(r['second_moment_delta'])<=THRESHOLDS['second_moment_delta_abs']

