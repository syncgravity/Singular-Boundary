"""Verify M5 face-cycle annulus boundary incidence."""
from collections import Counter
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces

fi,sg,E=penrose_faces(Approximant(M=5))
C=[1,3,2,4,154,150,11,10,7,8]
B=[f for f in C if f!=1]
def boundary(faces):
    cnt=Counter(int(e) for f in faces for e in fi[f])
    assert set(cnt.values()) <= {1,2}
    return set(e for e,n in cnt.items() if n==1),set(e for e,n in cnt.items() if n==2)
nine,nine_internal=boundary(B)
ten,ten_internal=boundary(C)
inner=set(map(int,fi[0]))
outer=ten-inner
assert len(nine)==20 and len(nine_internal)==8
assert len(ten)==20 and len(ten_internal)==10
assert len(inner)==4 and inner <= ten and len(outer)==16
assert sorted(inner)==[0,1,4,13]
assert sorted(outer)==[7,9,11,16,25,26,34,86,87,88,89,291,295,297,300,372]
assert set(map(int,fi[1])) & set(e for f in B for e in fi[f])=={3,14}
print("PASS M5 nine-face disk boundary: 20 links")
print("PASS M5 ten-face annulus: inner 4 links, outer 16 links")
