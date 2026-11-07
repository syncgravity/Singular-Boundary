#!/usr/bin/env python3
"""13-phase Paper 3 harmonic-triad, decagon null and lift checks.
Source-independent finite controls; not a coupled-Z5 interacting SU2 simulation.
Full 10,108 assertion verifier in the Library reproducibility archive.
"""
import math
import numpy as np
N=13
j=np.arange(N)
rng=np.random.default_rng(20261107)
def T(f,a):
    return np.mean(f*np.roll(f,-a)*np.roll(f,-3*a))
def Delta(f):
    return T(f,5)-T(f,8)
def mode(m,amp,phi):
    return amp*np.cos(2*np.pi*m*j/N+phi)
s=2*np.pi*10*5/N
K=.5*(np.sin(s)+np.sin(4*s)-np.sin(5*s))
assert abs(K+0.5762850408754576)<1e-12
checks=1
for _ in range(1000):
    mu=rng.uniform(.25,1.75);A=rng.uniform(0,.2);phi=rng.uniform(-np.pi,np.pi)
    f=mu+mode(10,A,phi)
    assert abs(Delta(f))<1e-12
    checks+=1
for _ in range(1000):
    mu=rng.uniform(.7,1.3)
    A=rng.uniform(.01,.25);B=rng.uniform(.01,.2)
    phi=rng.uniform(-np.pi,np.pi);psi=rng.uniform(-np.pi,np.pi)
    f=mu+mode(10,A,phi)+mode(20,B,psi)
    assert abs(Delta(f)-K*A*A*B*np.sin(psi-2*phi))<2e-12
    assert 0<f.min() and f.max()<2
    checks+=2
for _ in range(100):
    mu=1.;A=.2;B=.1;phi=rng.uniform(-np.pi,np.pi)
    psi=rng.uniform(-np.pi,np.pi);chi=rng.uniform(-np.pi,np.pi)
    original=mu+mode(10,A,phi)+mode(20,B,psi)
    rotated=mu+mode(10,A,phi+10*chi)+mode(20,B,psi+20*chi)
    assert abs(Delta(original)-Delta(rotated))<1e-12
    checks+=1
normals=2*np.pi*np.arange(10)/10
def decagon(p):
    theta=2*np.pi*j/N+p
    return (np.cos(np.pi/10)-.73*np.max(np.cos(theta[:,None]-normals),axis=1))**2
assert abs(Delta(decagon(0)))<1e-12
checks+=1
for _ in range(300):
    p=rng.uniform(-np.pi,np.pi)
    assert abs(Delta(decagon(p))+Delta(decagon(-p)))<1e-12
    checks+=1
A=.7;omega=2*np.pi*8/13
def geometry(v):
    den=A*A*omega*omega+v*v
    return A*omega*omega/den,v*omega/den
assert abs(geometry(0)[1])<1e-14
for v in np.geomspace(.01,10,100):
    k,t=geometry(v)
    assert k>0 and t>0 and abs(t/k-v/(A*omega))<1e-12
    checks+=1
print("PASS",checks,"source-limited harmonic, D10 mirror and helical lift checks")
print("K",K,"non-Penrose mixed harmonic Delta",Delta(1+mode(10,.4,0)+mode(20,.25,.8)))
