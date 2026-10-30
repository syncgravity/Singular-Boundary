"""Numerical SU(2) Haar heat-bath thermal mgf versus rigorous Gamma(3/2,1) bound."""
import json
from scipy.integrate import quad
from math import exp,log
results=[]
for t in [0.0,0.01,0.1,1.0,10.0,100.0]:
 for s in [0.1,0.5,0.8]:
  def integ(rate):
   return quad(lambda y:(y*(2-y))**.5*exp(-rate*t*y),0,2,epsabs=1e-12,epsrel=1e-12)[0]
  ratio=integ(1-s)/integ(1) if t else 1.0
  gamma=(1-s)**(-1.5)
  assert ratio <= gamma+1e-8
  results.append(dict(t=t,s=s,mgf=ratio,gamma_bound=gamma,ratio_to_gamma=ratio/gamma))
with open(__file__.replace('verify_mgf.py','mgf_verification.json'),'w') as f:json.dump(results,f,indent=2)
print('PASS',len(results),'single-link mgf comparisons')
