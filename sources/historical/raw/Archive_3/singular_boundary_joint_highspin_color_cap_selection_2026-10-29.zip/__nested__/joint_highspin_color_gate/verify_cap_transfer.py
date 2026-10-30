#!/usr/bin/env python3
"""Exact conditional SU2 target marginals for fixed-norm relative color sector,
and Hilbert-space projection cap transfer. Not the interacting ground state.
"""
from pathlib import Path
import math,csv
import numpy as np
from scipy.special import beta
from scipy.integrate import quad
P=Path(__file__).resolve().parent
PI=math.pi

def central_haar(f,a):
    return 2/PI*quad(lambda t:math.sin(t)**2*f(math.cos(t)),0,a,epsabs=1e-15)[0]

def density_supp(m,p):
    z=(2/PI)*beta(.5,2*m+1.5)
    return (1-p*p)**(2*m)/z

def color_target_T(m):return (4*m+3)/(4*(2*m+2)*(2*m+3))

def P_m(m,a,epsilon=1):
    # normalized mixture with norm fraction epsilon²/(1+epsilon²) in nonclass sector
    def d(p):
        dm=density_supp(m,p)
        return dm*(1+epsilon**2*p*p*(1-p*p)/color_target_T(m))/(1+epsilon**2)
    return central_haar(d,a)

def P_plus(a,epsilon=1):
    # Target factor splus=2sqrt2*p², density 8*p^4 under Haar.
    T=3/16
    return central_haar(lambda p:8*p**4*(1+epsilon**2*p*p*(1-p*p)/T)/(1+epsilon**2),a)

# Normalizations of exact marginal densities on full Haar SU2.
for m in range(0,7):
    assert abs(P_m(m,PI,1)-1)<1e-11,m
assert abs(P_plus(PI,1)-1)<1e-11
assert abs(central_haar(lambda p:p*p*(1-p*p)*8*p**4, PI)-3/16)<1e-12
print('PASS normalized center-even target-color mixtures; nonclass squared-norm fraction = 1/2')

rows=[]
for h in (.25,.1,.03,.01,.001,.0001):
    a=math.acos(1-h)
    haar=(a-math.sin(a)*math.cos(a))/PI
    suppressed=P_m(1,a,1)
    enhanced=P_plus(a,1)
    if h<.01:
        # relative small-cap asymptotic coefficient m=1: 48/35 * h²
        assert abs(suppressed/haar/((48/35)*h*h)-1)<.025
        assert abs(enhanced/haar/4-1)<.025
    print('h',h,'Haar',f'{haar:.8g}','suppressed mixed',f'{suppressed:.8g}',
          'supp/Haar',f'{suppressed/haar:.7g}', 'enhanced mixed/Haar',f'{enhanced/haar:.7g}')
    rows.append((h,haar,suppressed,suppressed/haar,enhanced,enhanced/haar))
with (P/'COLOR_CAPS.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['h','haar','suppressed_center_even_nonclass_50pct','suppressed_over_haar','enhanced_center_even_nonclass_50pct','enhanced_over_haar']);w.writerows(rows)

# Rigorous cap-transfer calculation: P_Omega(B)>= (sqrt(P_Phi(B))-epsilon)^2_+,
# epsilon=||Omega-Phi||; for certified spectral separation d>0 and Ritz
# residual r, epsilon<=sqrt2*r/d, assuming the computed Ritz eigenvector
# corresponds to the isolated ground-state eigenvalue.
for h in (.1,.01,.001,.0001):
    a=math.acos(1-h);haar=(a-math.sin(a)*math.cos(a))/PI
    # demonstrate r/d<=0.1 sqrt(Haar) retains >= 0.737 Haar
    residual_over_gap=.1*math.sqrt(haar)
    lower=(math.sqrt(haar)-math.sqrt(2)*residual_over_gap)**2
    assert lower/haar>.73
print('PASS direct Hilbert-space cap-transfer criterion: sufficient residual/gap o(h^(3/4)) for Haar-order transfer')
print('LIMITATION: no full-Hilbert gap/residual has been certified for the interacting eight-face SU2 Hamiltonian')
