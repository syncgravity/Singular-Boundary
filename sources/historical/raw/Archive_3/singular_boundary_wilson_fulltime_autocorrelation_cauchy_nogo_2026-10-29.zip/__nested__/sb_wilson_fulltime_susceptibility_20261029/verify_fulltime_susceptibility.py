#!/usr/bin/env python3
"""Rigorous-identity deterministic diagnostics for SU2 Wilson auto-responses.

NOT a simulation of a connected asymmetric Penrose deleted vacuum.
SU2 character Fourier checks are exact free-Haar calculations. The rotor is
an exactly diagonalized one-face class-sector comparator for the full-time
neighbor driver, with four equal incident kinetic coefficients A_g=4.
"""
import math
import numpy as np
from scipy.integrate import simpson
from scipy.special import roots_legendre
from scipy.linalg import eigh_tridiagonal


def bump_phi(theta, a):
    z = 2 * theta / a
    return np.where(z < 1, np.maximum(1-z*z, 0)**8, 0.)

def cap_diagnostics(a, N=2401):
    theta = np.linspace(0,a/2,N)
    phi = bump_phi(theta,a)
    weight = (2 / math.pi) * np.sin(theta)**2 * phi
    alpha = simpson(weight, x=theta)
    # Integer representations only; this is the center-even cap source.
    J = math.ceil(28/a)
    js = np.arange(J+1, dtype=float)
    # Stable normalized SU2 character, with continuous extension at theta zero.
    chars = (2*js[:,None]+1) * np.sinc((2*js[:,None]+1)*theta[None,:]/math.pi) / np.sinc(theta[None,:]/math.pi)
    betas = simpson(chars * weight[None,:], x=theta, axis=1)
    gammas = betas**2/(2*js+1)
    levels = js[1:] * (js[1:] + 1)
    var = np.sum(gammas[1:]**2)
    kinetic = np.sum(levels * gammas[1:]**2) # A=1
    inv = np.sum(gammas[1:]**2 / levels)  # A=1
    assert abs(gammas[0]-alpha*alpha)/alpha**2<1e-10
    assert inv * kinetic >= var**2 * (1-1e-10)
    assert 0<var and 0<inv and 0<kinetic
    print(f'cap a={a:.6g} alpha={alpha:.8e} F={alpha**2:.8e} var={var:.8e} m1/A={kinetic:.8e} chi*A={inv:.8e} (chi/F)/a^5*A={inv/(alpha**2 * a**5):.8g} Jensen ratio={inv*kinetic/var**2:.6g} Jmax={J}')
    return alpha, var, kinetic, inv

for a in (.5,.25,.125,.0625): cap_diagnostics(a)

n=np.arange(144,dtype=float)
A=4.
node,wt=roots_legendre(108)
u=(node+1)/2
ws=wt/2
for b in (4.,25.,100.,400.):
    diag0=n*(n+2)
    off=-b/2*np.ones(len(n)-1)
    eigen_end,vec_end=eigh_tridiagonal(diag0+b,off,select='i',select_range=(0,0))
    g=vec_end[:,0]
    p_end=float(np.dot(g[:-1],g[1:]))
    S_integral=0.
    for t,w in zip(u,ws):
        vals,V=eigh_tridiagonal(diag0+t*b, -t*b/2*np.ones(len(n)-1))
        ground=V[:,0]
        pg=np.zeros_like(ground)
        pg[:-1]+=.5*ground[1:]
        pg[1:]+=.5*ground[:-1]
        wsource=-b*pg
        coeffs=V.T@wsource
        chi=float(np.sum(coeffs[1:]**2/(vals[1:]-vals[0])))
        S_integral+=w*chi
    exact=b*p_end/2
    private=(3/(2*math.sqrt(2)))*math.sqrt(A*b)
    lower=max(0,b/2-private/2)
    assert abs(S_integral-exact) < 1e-4*max(1,exact), (b,S_integral,exact)
    assert lower-1e-8 <= exact <= b/2+1e-8
    print(f'neighbor b={b:.0f} <p>_1={p_end:.9f} int_chi={S_integral:.9f} exact_identity={exact:.9f} min_bound={lower:.9f} max_bound={b/2:.9f} chi/b={S_integral/b:.9f}')
print('PASS: full-time Wilson driver susceptibility identity, two-sided bounds, exact Haar cap self H^-1 scale, Jensen lower bound; no Penrose gap claim')
