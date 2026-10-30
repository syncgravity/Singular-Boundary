from fractions import Fraction as Q
from contextlib import redirect_stdout
from collections import defaultdict
import runpy,io
with redirect_stdout(io.StringIO()): d=runpy.run_path('research/scripts/ten_proper_forest_exact.py')
S,F,canon=d['S'],d['F'],d['canon'];C=frozenset(S);src=defaultdict(Q)
for g in S:
 for p,c in F[C-{g}].items():src[canon(list(p)+[(g,)])]+=c
assert len(src)==901
bound=sum((c*Q(len(p),15*(15+2*len(p))) for p,c in src.items()),Q())
assert bound==Q(5293486920929863227916486611931874506772464379,462348425729977179195166851391654980002803430400000)
print('PASS exact full-projection upper bound:',float(bound))
