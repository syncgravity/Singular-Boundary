"""Exact finite-disk tenth-order Q_f response scalar, using repository forest solver."""
from fractions import Fraction as Q
from collections import defaultdict,Counter
from math import comb,sqrt
from contextlib import redirect_stdout
import io,runpy
with redirect_stdout(io.StringIO()):
 d=runpy.run_path('research/scripts/ten_proper_forest_exact.py')
S,F,canon=d['S'],d['F'],d['canon']
C=frozenset(S);source=defaultdict(Q)
for g in S:
 for p,c in F[C-{g}].items():source[canon(list(p)+[(g,)])]+=c
assert len(source)==901 and all(c>0 for c in source.values())
assert Counter(len(p) for p in source)=={2:10,3:70,4:185,5:250,6:210,7:120,8:45,9:10,10:1}
alpha={k:sum((Q((-1)**j*comb(k,j),15+2*j) for j in range(k+1)),Q()) for k in range(2,11)}
assert all(v>0 for v in alpha.values())
kappa=sum((c*alpha[len(p)]/4**(len(p)-1) for p,c in source.items()),Q())
expected=Q(2376252926673252101321919045001703951557,3082322838199847861301112342611033200018689536000000)
assert kappa==expected
print('PASS exact coefficient',kappa)
print('projected L2 norm',float(kappa)*sqrt(3)/8)
