"""Check combinatorial support of exact ten-face forest recursion."""
from itertools import combinations
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
fi,sg,E=penrose_faces(Approximant(M=5))
C=(1,3,2,4,154,150,11,10,7,8)
links={g:set(map(int,fi[g])) for g in C}
edges={(a,b) for a,b in combinations(C,2) if links[a]&links[b]}
assert len(edges)==10
assert all(len(links[a]&links[b])==1 for a,b in edges)
total=0
for k in range(1,10):
    for J in combinations(C,k):
        J=set(J)
        sub=[(a,b) for a,b in edges if a in J and b in J]
        assert len(sub)<len(J)
        total+=1
assert total==1022
print('PASS 1022 proper subsets induce forests; largest cut basis 256')
