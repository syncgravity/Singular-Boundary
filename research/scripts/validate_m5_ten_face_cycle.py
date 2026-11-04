"""Verify indexed M5 unicyclic branch-connecting ring."""
from collections import defaultdict, deque
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
fi,sg,E=penrose_faces(Approximant(M=5))
ef=defaultdict(list)
for f,word in enumerate(fi):
    for e in word:ef[int(e)].append(f)
adj={f:set() for f in range(len(fi))}
for e,faces in ef.items():
    assert len(faces)==2
    a,b=faces;adj[a].add(b);adj[b].add(a)
core={1,2,3,4,7,8,10}
ban={0,1,2,3,7,8}
queue=deque([(4,(4,))]);seen=ban|{4}
while queue:
    u,path=queue.popleft()
    if u==10:break
    for v in sorted(adj[u]):
        if v not in seen:seen.add(v);queue.append((v,path+(v,)))
assert path==(4,154,150,11,10),path
s=core|{154,150,11}
induced={(min(a,b),max(a,b)) for a in s for b in adj[a]&s}
assert len(s)==10 and len(induced)==10
cycle=(1,3,2,4,154,150,11,10,7,8,1)
ed=[]
for a,b in zip(cycle,cycle[1:]):
    shared=set(map(int,fi[a]))&set(map(int,fi[b]))
    assert len(shared)==1
    e=next(iter(shared))
    ai=list(map(int,fi[a])).index(e);bi=list(map(int,fi[b])).index(e)
    assert int(sg[a][ai])==-int(sg[b][bi])
    ed.append(e)
assert ed==[3,2,5,19,296,17,18,12,8,14]
assert {(min(a,b),max(a,b)) for a,b in zip(cycle,cycle[1:])}==induced
print("PASS M5 10-face induced unicycle; path",path,"edges",ed)
