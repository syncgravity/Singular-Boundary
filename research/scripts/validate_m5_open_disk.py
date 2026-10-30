"""Extract and validate an eleven-face free-boundary disk from M5 incidence."""
from collections import Counter, defaultdict, deque
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
A=Approximant(M=5); words,signs,_=penrose_faces(A)
face_ids=(0,1,3,2,4,154,150,11,10,7,8)
counts=Counter(int(e) for f in face_ids for e in words[f])
verts=set();boundary=defaultdict(set);adj={f:set() for f in face_ids}
for e,n in counts.items():
    u,v,_=A.edges[e];u=int(u);v=int(v);verts.update((u,v))
    incident=[(f,int(signs[f][list(words[f]).index(e)])) for f in face_ids if e in words[f]]
    if n==1:boundary[u].add(v);boundary[v].add(u)
    else:
        assert n==2 and incident[0][1]==-incident[1][1]
        a,b=incident[0][0],incident[1][0];adj[a].add(b);adj[b].add(a)
assert (len(verts),len(counts),len(face_ids))==(20,30,11)
assert len(verts)-len(counts)+len(face_ids)==1
assert len(boundary)==16 and all(len(x)==2 for x in boundary.values())
def connected(graph,seed):
    seen=set();q=deque([seed])
    while q:
        u=q.popleft()
        if u not in seen:seen.add(u);q.extend(graph[u]-seen)
    return seen
assert connected(boundary,next(iter(boundary)))==set(boundary)
assert connected(adj,0)==set(face_ids)
assert sum(n==1 for n in counts.values())==16
assert sum(n==2 for n in counts.values())==14
assert all(counts[int(e)]==2 for e in words[0])
assert len(counts)-len(verts)+1==len(face_ids)
print("PASS: open disk 11 faces, 30 edges, 20 vertices, Euler +1")
print("PASS: 16-edge simple boundary; deleted face interior; 11 independent face variables")
