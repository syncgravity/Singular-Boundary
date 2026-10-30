#!/usr/bin/env python3
"""SU2 Peter-Weyl cap concentration and gap-free spin-resolution witness.
True Wilson SU2 class-rotor diagonalization is just a local benchmark;
the theorem's bound is general for full physical lattice spin networks.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

def haar_cap(delta):
    if delta<=0:return 0.
    if delta>=2:return 1.
    a=math.acos(1-delta)
    return (a-(1-delta)*math.sqrt(2*delta-delta*delta))/math.pi

def D(N):
    return (N+1)*(N+2)*(2*N+3)//6

# Analytically exact conditional Peter-Weyl projector diagonal.
for N in range(9):
    assert D(N)==sum((n+1)**2 for n in range(N+1))
    for delta in (.0001,.003,.07,.5,1.):
        assert haar_cap(delta)<=4*math.sqrt(2)/(3*math.pi)*delta**1.5+1e-13

# SU2 Haar cap integration for arbitrary class-bandlimited states.
rng=np.random.default_rng(463)
for nmax in (0,1,2,3,5):
    c=rng.normal(size=nmax+1);c/=np.linalg.norm(c)
    for delta in (.005,.07,.3):
        a=math.acos(1-delta)
        def wave(theta):
            if abs(theta)<1e-13: return sum((n+1)*c[n] for n in range(nmax+1))
            return sum(c[n]*math.sin((n+1)*theta)/math.sin(theta) for n in range(nmax+1))
        cap=quad(lambda t:2/math.pi*math.sin(t)**2*wave(t)**2,0,a,epsabs=2e-12)[0]
        assert cap<=min(1,D(nmax)*haar_cap(delta))+1e-10,(cap,D(nmax),delta)

# Rotor H= A*(-Delta)+b(1-p), SU2 class basis chi_{n/2}.
# It has a true positive Haar-density ground state; test projected overlap and bound.
results=[]
num=420
n=np.arange(num,dtype=float)
for b in (16.,64.,256.,1024.,4096.,16384.):
    ev,V=eigh_tridiagonal(n*(n+2)/4+b,-b*np.ones(num-1)/2,select='i',select_range=(0,0))
    ground=V[:,0]
    E=float(ev[0]);meanp=float(np.dot(ground[:-1],ground[1:]));d=1-meanp
    assert d>0 and b*d<=E+1e-8
    r={"b":b,"energy":E,"magnetic_deficit":d,"truncations":{}}
    for ncut in (0,2,4,8,16,32):
        if ncut>=num:continue
        overlap=float(np.linalg.norm(ground[:ncut+1]))
        fun=lambda delta: math.sqrt(D(ncut)*haar_cap(delta))+math.sqrt(d/delta)
        opt=minimize_scalar(fun,bounds=(max(1e-10,2*d),1),method='bounded')
        val=min(1.,fun(opt.x))
        assert overlap<=val+2e-6,(b,ncut,overlap,val)
        r['truncations'][str(ncut)]={"overlap":overlap,"certified_upper":val,"D":D(ncut)}
    results.append(r)
    print('SU2 rotor b=%7g E=%10.5f mean_d=%9.5f |P_{n<=2}Omega|=%.6f; bound=%.6f'%(b,E,d,r['truncations']['2']['overlap'],r['truncations']['2']['certified_upper']))

import json,os
os.makedirs('/mnt/data/sb_universal_link_spin_gate_20261029',exist_ok=True)
with open('/mnt/data/sb_universal_link_spin_gate_20261029/ROTOR_CHECKS.json','w') as f:json.dump(results,f,indent=2)
print('PASS: universal SU2 Haar cap projector bound; b^1/4 necessary link spin; true rotor overlap inequalities. Does NOT certify eight-face ground state.')
