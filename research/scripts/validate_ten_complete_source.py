"""Assemble tenth-order source exactly from validated proper-subset solver."""
from collections import defaultdict,Counter
from fractions import Fraction as Q
from contextlib import redirect_stdout
import io,runpy
with redirect_stdout(io.StringIO()):
 d=runpy.run_path('research/scripts/ten_proper_forest_exact.py')
S,F,canon=d['S'],d['F'],d['canon']
C=frozenset(S)
source=defaultdict(Q)
for g in S:
 for p,c in F[C-{g}].items():
  source[canon(list(p)+[(g,)])]+=c
assert len(source)==901 and all(c>0 for c in source.values())
assert Counter(len(p) for p in source)=={2:10,3:70,4:185,5:250,6:210,7:120,8:45,9:10,10:1}
for g in S:
 key=canon([(g,),tuple(sorted(C-{g}))])
 assert source[key]==Q(8483727237120608689933065034371083,652118084602408946310490345836847605350400000)
assert sum(source.values(),Q())==Q(40813079394342586463066870229231664727111,65211808460240894631049034583684760535040000)
print('PASS 2560 source contributions consolidated into 901 exact rational products')
