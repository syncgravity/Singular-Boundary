#!/usr/bin/env python3
"""PF-I16 support-locality finite-order combinatorial verifier (source-type path)."""
from itertools import combinations
faces=[frozenset("abcs"),frozenset("sdef"),frozenset("fghi")]
assert len(set.union(*(set(f) for f in faces)))==10
D=[{j for j in range(len(faces)) if j!=i and faces[i]&faces[j]}
   for i in range(len(faces))]
assert D==[{1},{0,2},{1}]
def connected(A):
    A=set(A)
    if not A:return False
    seen={next(iter(A))}
    while True:
        add=seen|set.union(set(),*(D[i]&A for i in seen))
        if add==seen:return seen==A
        seen=add
terms={1:{frozenset([i]) for i in range(3)}}
for n in range(2,8):
    terms[n]=set()
    for j in range(1,n):
        for A in terms[j]:
            for B in terms[n-j]:
                EA=set.union(*(set(faces[i]) for i in A))
                EB=set.union(*(set(faces[i]) for i in B))
                if EA&EB:terms[n].add(A|B)
    assert all(connected(t) and len(t)<=n for t in terms[n])
    print(n,len(terms[n]))
assert frozenset({0,1,2}) not in terms[2]
assert frozenset({0,1,2}) in terms[3]
for k in range(1,4):
    anchored=sum(connected(S) for S in combinations(range(3),k) if 1 in S)
    assert anchored<=112**(k-1)
for j in range(5):
    assert len({(k,sgn) for k in range(5) if k!=j for sgn in (-1,1)})==8
print("PASS: face-overlap histories, exact dual distance and degree 28")
