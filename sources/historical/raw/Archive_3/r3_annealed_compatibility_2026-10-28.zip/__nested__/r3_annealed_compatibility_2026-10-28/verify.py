import numpy as np, json
from scipy.special import ive
from scipy.integrate import quad
from pathlib import Path
out=[]
def a(l):return 2*ive(1,l)/l
for lam in [1.,2.,5.,10.,20.,50.,100.,1000.]:
    # Z inserted / Z cavity from exact Haar integration of U,K
    ratio=a(2*lam)/a(lam)
    # probability of near-flat insertion face U in cavity, Q deficit <=1/(2lam)
    cutoff=np.arccos(1-1/(2*lam))
    numerator=quad(lambda t: (2/np.pi)*np.sin(t)**2 * np.exp(-lam*(1-np.cos(t))),0,cutoff,epsabs=1e-13)[0]
    prob=numerator/a(lam)
    out.append({'lambda':lam,'ratio_exact':ratio,'near_flat_probability':prob,'a_lambda':a(lam)})
# high precision standard quadrature one test
l=5
z=quad(lambda t: (2/np.pi)*np.sin(t)**2*np.exp(-l*(1-np.cos(t))),0,np.pi,epsabs=1e-14)[0]
assert abs(z-a(l))<2e-13
assert all(p['near_flat_probability']>0.01 for p in out)
assert all(p['ratio_exact']>0.35 for p in out)
result={'geometry':'abstract two-plaquette two-link SU(2) complex: cavity faces U, U K; inserted face U','proof_status':'exact identities; not demonstrated as a Penrose R3 subcomplex','numeric_check':out,'quadrature_error_a5':abs(z-a(l)),'limit_ratio':2**(-1.5)}
Path(__file__).with_name('certificate.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
