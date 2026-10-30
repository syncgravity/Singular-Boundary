"""Reproduce exact 58,024-sector reduction on 901 tenth-order source products."""
from itertools import combinations
from fractions import Fraction as F
from collections import Counter,defaultdict
import io,contextlib,runpy
with contextlib.redirect_stdout(io.StringIO()):
 d=runpy.run_path('research/scripts/ten_proper_forest_exact.py')
S,coeff,canon,edges=d['S'],d['F'],d['canon'],d['edges']
C=frozenset(S);source=defaultdict(F)
for g in S:
 for p,c in coeff[C-{g}].items():source[canon(list(p)+[(g,)])]+=c
assert len(source)==901
counts=Counter()
for p,c in source.items():
 cut=[(a,b) for a,b in edges if not any(a in block and b in block for block in p)]
 assert len(cut)==len(p)
 counts[len(cut)]+=1
 for mask in range(1<<len(cut)):
  assert F(1,15+2*(len(cut)-mask.bit_count()))>0
assert counts=={2:10,3:70,4:185,5:250,6:210,7:120,8:45,9:10,10:1}
assert sum(n*(2**k) for k,n in counts.items())==58024
print('PASS: 901 source terms; 58024 exact spin-sector summands')
