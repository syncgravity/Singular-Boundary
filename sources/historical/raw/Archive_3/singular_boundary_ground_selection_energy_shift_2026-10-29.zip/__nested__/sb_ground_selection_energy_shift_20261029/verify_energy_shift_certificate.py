#!/usr/bin/env python3
"""SU(2) center-even cap energy-shift certificate and exact radial rotor check.
No assumptions about the spectral gap of an interacting eight-face Wilson system.
"""
from pathlib import Path
from math import pi, sin, cos, acos, sqrt
import csv
import numpy as np
from scipy.linalg import eigh
ROOT=Path(__file__).resolve().parent

def haar_angle(a):
    return (a-sin(2*a)/2)/pi

def lower_2x2(a,q,r2):
    # Numerically stable smaller eigenvalue: det/lambda_max
    disc=sqrt((a-q)**2+4*r2)
    return 2*(a*q-r2)/(a+q+disc)

def symcap_class_matrix(a,N):
    # exact SU(2) center-even character basis chi_j for j = 0,...,N
    # K = 1_{theta<=a or theta>=pi-a}; Haar density = 2/pi sin² theta.
    K=np.empty((N+1,N+1))
    for j in range(N+1):
        k=2*j+1
        for l in range(N+1):
            n=2*l+1
            if k==n:
                integ=a/2-sin(2*k*a)/(4*k)
            else:
                integ=sin((k-n)*a)/(2*(k-n))-sin((k+n)*a)/(2*(k+n))
            K[j,l]=4/pi*integ
    return .5*(K+K.T)

# A*(-Delta) chi_j = A*j(j+1)*chi_j, first nonconstant
# target-center-even j=1 mode has energy M=2*A.
A=1.;M=2*A;lam=M/4
rows=[]
for h in (0.25,0.1,0.03,0.01,0.003,0.001,0.0001):
    a=acos(1-h)
    m=haar_angle(a)
    mu=2*m
    assert 0<mu<1
    energy_ritz=lam*mu
    off2=lam*lam*mu*(1-mu)
    L=lower_2x2(energy_ritz,M,off2)
    schur=energy_ritz-off2/(M-energy_ritz)
    simple_ratio=(M-lam)/(M-lam*mu)
    assert 0<=schur<=L<=energy_ritz+1e-13
    assert schur/(lam*mu)>=simple_ratio-1e-10
    assert L/(2*lam*m)>.74
    # exact projected SU2 even rotor, no quadrature / Monte Carlo
    K=symcap_class_matrix(a,45)
    assert abs(K[0,0]-mu)<2e-14
    assert np.linalg.eigvalsh(K)[0]>-1e-11
    H=np.diag(A*np.arange(46)*(np.arange(46)+1))+lam*K
    energy_numeric=float(eigh(H,subset_by_index=[0,0],check_finite=False)[0][0])
    assert L<=energy_numeric+1e-10, (h,L,energy_numeric)
    assert energy_numeric<=energy_ritz+1e-10
    ratio=L/(2*lam*m)
    rows.append((h,m,mu,energy_ritz,L,energy_numeric,ratio))
    print(f'BINARY h={h:.5g} Haar+={m:.9g} E_Ritz={energy_ritz:.9g} '
          f'E_lower={L:.9g} E_even45={energy_numeric:.9g} certified_cap_over_Haar={ratio:.8f}')
with (ROOT/'INDICATOR_CAP_CERTIFICATES.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['h','haar_one_cap','mu_symmetric','rank1_Ritz_energy',
                                'rigorous_full_rotor_energy_lower','46_character_Ritz_energy',
                                'certified_single_cap_over_Haar']);w.writerows(rows)

# Soft, compactly supported convolution: phi=indicator_{theta<=a/2},
# k=phi*phi^vee, k>=0, support theta<=a, nu=k(I)=alpha; F=alpha².
# k^+=(k(U)+k(-U))/2 is center-even. For a<pi/2, ||k^+||<=alpha/2.
soft=[]
for h in (0.25,0.1,0.01,0.001,0.0001):
    a=acos(1-h)
    alpha=haar_angle(a/2)
    mu=alpha*alpha
    kappa=alpha/2
    trial=lam*mu
    r2_upper=lam*lam*kappa*mu
    schur=trial-r2_upper/(M-trial)
    assert schur>0
    # k(U)<=alpha*1_{theta<=a}, and expectation of k equals expectation of k^+.
    cap_lower=schur/(lam*alpha)
    ratio=cap_lower/haar_angle(a)
    assert ratio>0
    soft.append((h,alpha,mu,cap_lower,ratio))
    print(f'SOFT h={h:.5g} alpha={alpha:.9g} mu={mu:.9g} '
          f'certified_cap_over_Haar={ratio:.8f}')
with (ROOT/'SOFT_CAP_CERTIFICATES.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['h','alpha_half_cap_Haar','convolution_Haar_mean',
                                'certified_one_cap_probability_lower','certified_one_cap_over_Haar']);w.writerows(soft)
assert abs(soft[-1][-1]-.125)<.002
print('PASS exact SU2 source-energy certification, center-even SU2 rotor, rank-one Schur bounds and small-cap convolution lower limit 1/8')
print('LIMIT: free target rotor, not connected eight-face Wilson ground state')
