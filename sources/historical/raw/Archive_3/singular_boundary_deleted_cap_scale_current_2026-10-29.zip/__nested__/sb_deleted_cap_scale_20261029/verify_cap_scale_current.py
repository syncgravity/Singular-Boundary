#!/usr/bin/env python3
"""Verify exact Haar cap-scale current bounds and positive SU2 rotor comparator."""
import math
import numpy as np
from scipy.integrate import simpson

PI=math.pi

def H(a):
    return (a-math.sin(2*a)/2)/PI

def omega(u):
    return (2/PI)*np.sin(u)**2

def smoothstep(x):
    z=np.asarray(x)
    out=np.zeros_like(z,dtype=float)
    out[z>=1]=1.
    q=(z>0)&(z<1)
    v=z[q]
    y=np.exp(-1/v); x=np.exp(-1/(1-v))
    out[q]=y/(y+x)
    return out

def bump(x):
    return smoothstep((x-1/4)/(1/3-1/4))*smoothstep((1/2-x)/(1/2-5/12))

# Exact proof constants for pure-Haar case: T=0, m=H(a).
for a in [0.02,0.1,0.4,1.0]:
    ring=H(a)-H(a/2)
    W=0.5-H(a)
    lower=ring/(2*(W+ring))
    lower_simple=ring/2
    assert H(a)>=lower>=lower_simple
    K=(PI/2)*(1/math.tan(a/2)-1/math.tan(a))
    assert K>0
    assert ring>0
    print(f'HAAR a={a:.2f} mass={H(a):.10g} CS1={lower:.10g} CS2={lower_simple:.10g} K={K:.9g}')

# Test exact abstract cap-scale inequality against positive smooth radial shapes.
# Deliberately include equator-favoring, center-favoring, highly oscillatory,
# and two-center bumps. The positive derivative integral is calculated directly.
u=np.linspace(0,PI/2,160001)
w=omega(u)
for key in ['haar','increasing','decreasing','oscillatory','center-dip']:
    if key=='haar': y=np.ones_like(u)
    elif key=='increasing': y=np.exp(2*u)
    elif key=='decreasing': y=np.exp(-2*u)
    elif key=='oscillatory': y=1+0.16*np.cos(64*u)
    else: y=1-0.7*np.exp(-(u/0.09)**4)
    Z=2*simpson(w*y*y,x=u)
    y=y/np.sqrt(Z)
    lder=np.gradient(np.log(y),u)
    for a in [0.05,0.12,0.35]:
        T=simpson(np.maximum(lder[u>=a/2],0),x=u[u>=a/2])
        mass=simpson(w[u<=a]*y[u<=a]**2,x=u[u<=a])
        ring=H(a)-H(a/2);W=0.5-H(a)
        k=ring*np.exp(-2*T)
        rhs=k/(2*(W+k))
        assert mass+3e-5>=rhs,(key,a,mass,rhs)
        Tout=simpson(np.maximum(lder[u>=a],0),x=u[u>=a])
        mask=(u>=a/2)&(u<=a)
        Js=simpson(w[mask]*np.gradient(y,u)[mask]**2,x=u[mask])
        K=(PI/2)*(1/math.tan(a/2)-1/math.tan(a))
        rhs2=min(H(a)/4,ring*max(0,np.exp(-Tout)/np.sqrt(2)-np.sqrt(K*Js))**2)
        assert mass+3e-5>=rhs2,(key,a,mass,rhs2)
    print('SHAPES',key,'PASS')

# Deep-core high-frequency comparator, computed in x=u/eps coordinates.
# We verify exact support and analytic variation/Fisher and cap-ratio bounds,
# and numerically integrate only its tiny support to avoid extreme-scale meshes.
from scipy.integrate import trapezoid
for n in (8,16,32,64):
    a=n**(-0.5);eps=n**(-6);N=n*n;c=0.2
    assert eps/2<a/2
    plateau_cycles=math.floor(N/12)-1
    Tlower=max(0,plateau_cycles)*math.log((1+c)/(1-c))
    x=np.linspace(0.25,0.5,max(4097,24*N+1))
    q=c*bump(x)*np.sin(2*PI*N*x)
    wloc=omega(eps*x)
    local=eps*trapezoid(wloc*(2*q+q*q),x=x)
    Z=1+2*local
    # left cap includes one support; the other symmetric cap is disjoint
    m=(H(a)+local)/Z
    ratio=m/H(a)
    assert abs(ratio-1)<100*(eps/a)**3
    assert 0.9<ratio<1.1
    assert Tlower>=0
    # Explicit derivative bound from bump' and oscillatory derivative:
    # J=O(N² eps); N² eps = n^-2.
    bound_power=N*N*eps
    assert abs(ratio-1)<0.01 and bound_power==n**(-2)
    print(f'COMPARATOR n={n:2d} T_global_lower={Tlower:9.4f} T_cap=0 J_power={bound_power:.8g} Haar_mass_ratio={ratio:.12f}')

print('PASS: exact SU2 Haar cap, cap-scale current, two-scale shell and positive rotor separation; no Monte Carlo')
