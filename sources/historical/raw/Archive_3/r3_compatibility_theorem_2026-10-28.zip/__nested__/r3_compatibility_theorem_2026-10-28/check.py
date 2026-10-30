import json
import numpy as np
from scipy.special import ive
from scipy.integrate import quad
from pathlib import Path

def z(lam):
    # normalized SU2 Wilson integral z=lambda -> e^-lambda 2 I1(lambda)/lambda
    return 2*ive(1,lam)/lam

def hb(eps):
    return (eps-np.sin(eps)*np.cos(eps))/np.pi

out=[]
for lam in [1,2,5,10,20,50,100]:
    aligned=z(2*lam)/z(lam)
    anti=np.exp(-2*lam)/z(lam)
    # for single link cavity+insertion: m=1,n=q=1,L=1.
    bound=(8/(3*np.pi**3))*lam**(-1.5)*np.exp(-1)
    vol=hb(1/np.sqrt(lam))
    out.append({'lambda':lam,'aligned_ratio':aligned,'frustrated_ratio':anti,'theorem_lower_bound':bound,'bound_verified':bool(aligned>=bound),'haar_ball_volume':vol,'haar_lower_bound':(8/(3*np.pi**3))*lam**(-1.5)})
assert all(r['bound_verified'] for r in out)
assert all(r['haar_ball_volume']>=r['haar_lower_bound']-1e-14 for r in out)
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2))
print('PASS 7 aligned and frustrated examples; compatible theorem bound and Haar volume')
