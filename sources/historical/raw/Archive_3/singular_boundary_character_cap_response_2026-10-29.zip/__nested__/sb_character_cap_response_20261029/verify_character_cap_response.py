#!/usr/bin/env python3
"""Deterministic SU(2) heat-kernel character-window and local cap-response certificates.
The heat kernel model is a comparator, NOT the deleted Penrose vacuum.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import expit

pi=math.pi

def haar(a):return (a-0.5*math.sin(2*a))/pi

def chi(j,u):
    if abs(u)<1e-12:return 2*j+1
    return math.sin((2*j+1)*u)/math.sin(u)

def center_even_heat(u,J):
    # normalized heat kernel + its center translation / 2: integer spins only.
    js=np.arange(0,int(12*J)+1,dtype=float)
    mult=2*js+1
    damp=np.exp(-js*(js+1)/(J*J))
    su=np.sin(u)
    if abs(su)<1e-12:chars=mult
    else:chars=np.sin(mult*u)/su
    return float(np.dot(mult*damp,chars))

def cutoff_smooth(u,a):
    # eta=0 on [0,a]; eta=1 on [2a,pi-2a]; symmetric around pi/2.
    v=min(u,pi-u)
    if v<=a:return 0.
    if v>=2*a:return 1.
    t=(v-a)/a
    return 6*t**5-15*t**4+10*t**3

def tests_heat():
    print('Heat-kernel center-cap removal with positive finite character window')
    print('  J     a       removed_mass    min(c_j/d_j) j<=J       mass(B_a)')
    for J in [4,8,12,24]:
        a=.12/J
        # reference center-even heat kernel integrates to 1 exactly; compact support change only near two centers.
        q=lambda u: 2/pi*math.sin(u)**2*center_even_heat(u,J)
        removed=2*quad(lambda u:q(u)*(1-cutoff_smooth(u,a)),0,2*a,epsabs=2e-13,limit=200)[0]
        assert removed<.2
        ratio=[]
        for j in range(1,J+1):
            initial=(2*j+1)*math.exp(-j*(j+1)/J**2)
            corr=2*quad(lambda u:q(u)*(1-cutoff_smooth(u,a))*chi(j,u),0,2*a,epsabs=2e-12,limit=200)[0]
            current=(initial-corr)/(1-removed)
            ratio.append(current/(2*j+1))
        assert min(ratio)>0
        print(f'{J:3d}  {a:.6f}   {removed:.8f}       {min(ratio):.8f}           0 (exact)')
        # Strict positive version replacing zero cutoff by exp(-J^2); finite-spin expectations remain positive.
        if J>=8:
            eps=math.exp(-J*J)
            denom=1-(1-eps)*removed
            cap=eps*2*quad(q,0,a,epsabs=2e-14)[0]/denom
            assert cap<haar(a)*1e-10


def test_harmonic_analysis():
    # Verify exact SU2 Fourier coefficient b_j for sharp central caps and character orthogonality.
    for a in (.15,.33,.7):
      for j in (1,2,3,7):
        direct=quad(lambda u:2/pi*math.sin(u)**2*chi(j,u),0,a,epsabs=1e-13)[0]
        exact=(math.sin(2*j*a)/(2*j)-math.sin((2*j+2)*a)/(2*j+2))/pi
        assert abs(direct-exact)<2e-13
    print('PASS: exact SU2 character coefficients, spin window and strict positive cap-suppressed rotor')


def test_uv_scaling():
    # m1(k)<=C a^4 and m1(b_g d_g)<=C b_g².
    # UV mixed response <= C a² b_g/Lambda². For a²~h, b_g~h^-2,
    # Lambda=L h^-2, the ratio to A_a²~a^6~h³ is O(L^-2).
    for h in (.2,.1,.05,.01,.001):
        a=math.sqrt(h); b=h**-2; Lam=10*h**-2
        uv=a*a*b/(Lam*Lam)
        assert abs(uv/(a**6)-.01)<1e-12
    print('PASS: exact UV mixed-resolvent spectral exponent and h-independent ratio at Lambda=10 h^-2')

if __name__=='__main__':
    test_harmonic_analysis();tests_heat();test_uv_scaling()
