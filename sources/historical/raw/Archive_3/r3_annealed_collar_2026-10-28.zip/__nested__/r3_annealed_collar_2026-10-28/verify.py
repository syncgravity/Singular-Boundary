import numpy as np
from scipy.special import i1e
from scipy.integrate import quad
from pathlib import Path
import json
L=[0.1,1.,2.,5.,10.,30.,100.]
rows=[]
for l in L:
    log_a=np.log(2)+np.log(i1e(l))-np.log(l) # exp(-lambda) I1(lambda)*2/l
    quad_a=2/np.pi*quad(lambda t: np.exp(l*(np.cos(t)-1))*np.sin(t)**2,0,np.pi,epsabs=1e-14)[0]
    analytic=float(np.exp(log_a))
    rel=float(abs(analytic-quad_a)/analytic)
    rows.append(dict(lam=l,log_a=float(log_a),a=analytic,quad=quad_a,relative_error=rel))
assert max(x['relative_error'] for x in rows)<2e-10
out={'description':'Haar normalized single-plaquette Wilson insertion; independent free edge / annealed holonomy','formula':'a(lambda)=exp(-lambda)*2*I1(lambda)/lambda','rows':rows,'max_rel_error':max(x['relative_error'] for x in rows)}
Path('/mnt/data/r3_annealed_collar_2026-10-28/numerical_certificate.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
