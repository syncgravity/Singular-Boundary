"""Algebraic Haar-ball estimate for active links in finite SU(2) Wilson systems."""
import json,math
from pathlib import Path
import numpy as np
from nested_audit import build,complex_3
c0=2*math.sin(1.0)**2/(3*math.pi)
a=0.25
B=8*a*a+4*math.log(1/(c0*a**3))
result={'haar_small_ball_c0':c0,'radius_coefficient':a,'energy_upper_bound':f'(lambda / count retained faces) * E(sum retained Wilson deficit) <= 6 log(lambda)+{B:.12f}, lambda>=1','constant':B,'verified_geometry':[]}
for r in [5.,6.5,8.,10.]:
 g,_=build(r,0);cols,meta=complex_3(g)
 num_active=len(set().union(*(set(c) for c in cols)))
 assert num_active<=4*len(cols)
 N=len(g.edges)*3+len(g.labels)*3
 assert N==num_active
 result['verified_geometry'].append({'radius':r,'faces':len(cols),'active_links':num_active,'active_links_le_4_faces':True})
Path(__file__).with_name('energy_bound_certificate.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
