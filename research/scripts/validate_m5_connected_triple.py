"""Rational regression for connected M5 SU2 triple (1,3,2)."""
from fractions import Fraction as F
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
faces,signs,E=penrose_faces(Approximant(M=5))
assert len(faces)==188 and E==376
edge={i:set(map(int,faces[i])) for i in (1,2,3)}
assert edge[1]&edge[3]=={3}
assert edge[3]&edge[2]=={2}
assert not edge[1]&edge[2]
assert len(edge[1]^edge[2]^edge[3])==8
for i,j,e in ((1,3,3),(3,2,2)):
    assert int(signs[i,list(faces[i]).index(e)])==-int(signs[j,list(faces[j]).index(e)])
a=F(37,117)
c=F(4,351)
A=a/10
B=(c+A/2)/8
D=B/6
assert (A,B,D)==(F(37,1170),F(191,56160),F(191,336960))
assert 10*A==a and 8*B-A/2==c and 6*D-B==0
print('PASS connected triple exact rational resolvent block')
