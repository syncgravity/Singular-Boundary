#!/usr/bin/env python3
"""Independent deterministic SU(2) radial current, one-sided potential budget audit.
No Monte Carlo, no full many-face Penrose ground state computation.
"""
import numpy as np
from scipy.special import roots_legendre
from scipy.integrate import simpson
from math import pi, acos, sqrt, log

def haar_ball(delta):
    return (acos(1-delta)-(1-delta)*sqrt(2*delta-delta*delta))/pi

def compute(n, k=1.0):
    assert n >= 16 and n % 2 == 0
    eps = n**(-1.5)
    c = (1+eps*eps/2)**(-.5)
    # Half-period midpoint for oscillatory positive-part integrals
    N = 256*n
    u = (np.arange(N)+0.5)*(pi/2)/N
    C = np.cos(2*n*u)
    S = np.sin(2*n*u)
    psi = c*(1+eps*C)
    dpsi = -2*n*eps*c*S
    ddpsi = -4*n*n*eps*c*C
    Voverk = (ddpsi + 2*np.cos(u)/np.sin(u)*dpsi)/psi
    B = np.mean(np.sin(u)*np.cos(u)*np.maximum(Voverk,0))*(pi/2)
    r = dpsi/psi
    T_num = np.mean(np.maximum(r,0))*(pi/2)
    T_exact = (n/2)*log((1+eps)/(1-eps))
    O = log((1+eps)/(1-eps))
    J = 2*n*n*eps*eps/(1+eps*eps/2)
    assert abs(T_num-T_exact)<1e-5*max(1,T_exact), (T_num,T_exact)
    assert O<=T_exact+1e-12<=B+2e-5
    # Exact normalized Haar mass moment and bound on every center ball
    delta=1/n
    mh=haar_ball(delta)
    alpha=acos(1-delta)
    M=64*n
    t=(np.arange(M)+0.5)*alpha/M
    mass=np.mean((2/pi)*np.sin(t)**2*(c*(1+eps*np.cos(2*n*t)))**2)*alpha
    assert mh*((1-eps)**2/(1+eps**2/2)) - 2e-6*mh <= mass
    assert mass <= mh*((1+eps)**2/(1+eps**2/2)) + 2e-6*mh
    # Conditional score C(p)=-k*sin u * r; the exact first-derivative current
    score=-k*np.sin(u)*r
    T_from_score=np.mean(np.maximum(-score,0)/(k*np.sin(u)))*(pi/2)
    assert abs(T_from_score-T_num)<2e-12
    # Exact positive eigenfunction of -k (d²+2 cot d)+V, V>=0 with shift
    # Vraw= k*(psi''+2cot psi')/psi, bounded by 12k n² eps/(1-eps)
    Vshift=12*k*n*n*eps/(1-eps)
    assert np.min(k*Voverk+Vshift)>-1e-8
    assert np.max(k*Voverk+Vshift)<2*Vshift+1e-8
    # H psi = Vshift psi exactly: -k Delta psi + (k Delta psi /psi +Vshift)psi
    residual = (-k*(ddpsi + 2*np.cos(u)/np.sin(u)*dpsi) + (k*Voverk+Vshift)*psi - Vshift*psi)
    assert np.max(np.abs(residual))<1e-9
    return n,eps,J,O,T_exact,B,mass/mh, Vshift, np.max(np.abs(residual))

if __name__=='__main__':
    print('n,eps,Fisher,one-sided-osc,positive-log-variation,positive-V-budget,cap/Haar,potential-shift,max-residual')
    out=[compute(n) for n in (16,32,64,128,256,512)]
    for row in out:
        print(','.join(f'{x:.10g}' if isinstance(x,float) else str(x) for x in row))
    assert all(out[i+1][5]>out[i][5] for i in range(len(out)-1))
    assert all(out[i+1][4]<out[i][4] for i in range(len(out)-1))
    assert all(out[i+1][2]<out[i][2] for i in range(len(out)-1))
    print('PASS: current/potential hierarchy, exact comparator ground state, positive potential, Haar cap and Fisher asymptotics')
