"""Validate the exact link-spin upper bound and shifted-resolvent threshold."""
from fractions import Fraction
from collections import Counter
from math import sqrt
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
from collections import defaultdict
a=Approximant(M=5)
faces,signs,E=penrose_faces(a)
B=(3,2,4,154,150,11,10,7,8)
counts=Counter(int(e) for f in B for e in faces[f])
boundary={e for e,n in counts.items() if n==1}
A=set(int(e) for e in faces[1])
assert len(boundary)==20 and len(A)==4 and len(A&boundary)==2
support=Counter({e:1 for e in boundary})
support.update(A)
assert sum(m==1 for m in support.values())==20
assert sum(m==2 for m in support.values())==2
L=Fraction(20)*Fraction(3,4)+Fraction(2)*Fraction(2)
assert L==19
threshold=722/sqrt(3)
z=Fraction(500)
from math import sqrt
lower=sqrt(3)/(8*float(z*z))-361/(4*float(z*z*z))
assert float(z)>threshold and lower>0
print("PASS 20 single, 2 double; electric max 19; z=500 lower",lower)
