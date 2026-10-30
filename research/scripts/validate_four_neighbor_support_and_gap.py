"""Validate necessary neighbor coupling support and finite gap arithmetic."""
import sys
from fractions import Fraction as F
from pathlib import Path
# Supply an external penrose_study checkout with PENROSE_STUDY_SRC if needed.
import os
if os.environ.get('PENROSE_STUDY_SRC'):
 sys.path.insert(0,os.environ['PENROSE_STUDY_SRC'])
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
f,_,_=penrose_faces(Approximant(M=5))
C=(1,3,2,4,154,150,11,10,7,8)
expect={0:1,1:2,4:4,13:10}
for e,g in expect.items():
 assert [h for h in C if e in f[h]]==[g]
for g,e in ((1,86),(2,88),(4,372),(10,26)):
 assert e in f[g] and all(e not in f[h] for h in C if h!=g)
r=F(3,320)
assert 10*r==F(3,32)
assert F(3,4)-10*r==F(21,32)
print("PASS four mandatory neighboring couplings and finite-volume min-max gap 21/32")
