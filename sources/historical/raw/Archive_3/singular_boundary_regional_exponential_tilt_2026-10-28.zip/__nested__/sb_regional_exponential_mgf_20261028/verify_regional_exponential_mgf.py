#!/usr/bin/env python3
"""Deterministic symbolic and SU(2) Jacobi tests for RT-1 to RT-18.

Exact proofs are the ground-state form inequalities in PROOF_REPORT.md.
Finite character-basis diagonalizations are checks, NOT proofs of their infinite-h
asymptotics or of the connected Penrose vacuum. No Monte Carlo.
"""
import json
import math
from itertools import combinations
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal

p,a,b=sp.symbols('p a b',real=True,positive=True)
D={2:-a*(1-p*p),1:3*a*p}
C={1:2*a*(1-p*p),0:-3*a*p}

def composition(A,B):
    out={}
    for i,f in A.items():
        for j,g in B.items():
            for k in range(i+1):
                n=i+j-k
                out[n]=out.get(n,0)+f*sp.binomial(i,k)*sp.diff(g,p,k)
    return {n:sp.factor(z) for n,z in out.items() if sp.simplify(z)!=0}

def commutator(A,B):
    first=composition(A,B); second=composition(B,A)
    return {i:sp.factor(first.get(i,0)-second.get(i,0)) for i in set(first)|set(second) if sp.simplify(first.get(i,0)-second.get(i,0))!=0}

TC=commutator(D,C)
CTC=commutator(C,TC)
assert CTC[0]==-6*a**3*(5*p*p+1)
assert sp.simplify(CTC[2]-8*a**3*(1-p**4))==0
rho_log_deriv=-p/(1-p*p)
assert sp.simplify(CTC[1]-(sp.diff(CTC[2],p)+rho_log_deriv*CTC[2]))==0
V={0:b*(1-p)}
CVC=commutator(C,commutator(V,C))
assert sp.simplify(CVC[0]+8*a*a*b*p*(1-p*p))==0
# Casimir convention for the four-link physical class function.
assert sp.simplify((1-p*p)/4-(1-p)/2+(1-p)**2/4)==0
assert sp.simplify(a*(1-p*p)/(4*(1-p))-a*(1+p)/4)==0

beta,amax,h,lam,R,delta=sp.symbols('beta amax h lam R delta',positive=True)
k=sp.sqrt(amax/beta)
rate=lam*(R+delta)-R/k*sp.atanh(k*lam)
assert sp.simplify(sp.diff(rate,lam).subs(lam,0)-delta)==0
assert sp.simplify(sp.limit(rate/lam,lam,0)-delta)==0
# Exact derivation of tilt scaling and recurrence.
Delta=sp.symbols('Delta',positive=True)
base=Delta/sp.sqrt(amax*(beta/h**2))*sp.atanh((lam/h)*sp.sqrt(amax/(beta/h**2)))
assert sp.simplify(base-Delta*h/sp.sqrt(amax*beta)*sp.atanh(k*lam))==0
assert sp.simplify((h**3*Delta/beta)/(h**2)*sp.sqrt(beta/amax)*sp.atanh(k*lam)-base)==0
# One-plaquette moment hierarchy constants.
Cs=[1,3*math.sqrt(2)]
for j in range(1,6):
    Cs.append(3*math.sqrt(2)*Cs[-1]+(j*j/2)*Cs[-2])
assert abs(Cs[2]-18.5)<1e-12

# Actual three-face Penrose Z5 *spatial* incidence fixture.
faces0=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(face):
    return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(t-u) for t,u in zip(x,y))==1}
faces=[edges(f) for f in faces0]
edge_set=set.union(*faces)
assert len(edge_set)==10 and max(sum(e in f for f in faces) for e in edge_set)==2

# Ground state of exact gauge-invariant SU(2) one-face magnetic rotor,
# solved by deterministic character Jacobi truncation.
rows=[]
for mesh in (0.2,0.1,0.05,0.025):
    A=1.; B=4./mesh**2; N=120
    j=np.arange(N,dtype=float)
    diag=A*j*(j+2)+B
    off=np.full(N-1,-B/2)
    eig, v=eigh_tridiagonal(diag,off,select='i',select_range=(0,0))
    omega=v[:,0]; E0=eig[0]
    P=np.diag(np.full(N-1,.5),1)+np.diag(np.full(N-1,.5),-1)
    dmat=np.eye(N)-P
    md=float(omega@dmat@omega)
    md2=float(omega@dmat@dmat@omega)
    var=md2-md*md
    K=np.diag(diag-E0)+np.diag(off,1)+np.diag(off,-1)
    source=(dmat-md*np.eye(N))@omega
    m1=float(source@K@source)
    m2=float(source@K@K@source)
    m3=float(source@K@K@K@source)
    # First moment equals exact Haar SU2 character/Casimir identity.
    assert abs(m1-A*float(omega@(np.eye(N)-P@P)@omega))<1e-9
    # Local score kinetic is E0-b E[d], since the source state is exact.
    kinetic=E0-B*md
    assert kinetic>=-1e-9 and abs(kinetic/A)<100/mesh
    # Explicit exact conservative inequalities.
    assert md <=3*math.sqrt(2*A/B)+1e-8
    assert md2 <=18.5*A/B+1e-8
    assert m2 <=626*A*A+1e-7
    if B>=72*A:
        assert (3/(16*math.sqrt(2)))*A**1.5/B**.5 <=m1+1e-9
        assert m1<=6*math.sqrt(2)*A**1.5/B**.5+1e-8
        assert (9/(512*626))*A/B <=var+1e-12
    assert m3>=-1e-8 and m3<=18*A**3+16*A*A*E0+1e-6
    # Genuine independent-component SU2 Wilson example at fixed total area.
    F=int(1/mesh**2)
    rows.append({'h':mesh,'b':B,'E0_h':E0*mesh,'Ed_over_h':md/mesh,
                 'var_d_over_h2':var/mesh**2,
                 'm1_d_over_h':m1/mesh,'m2_d':m2,
                 'm3_d_times_h':m3*mesh,
                 'component_count':F,
                 'normalized_source_variance_over_h':F*var,
                 'normalized_source_first_moment':mesh*F*m1,
                 'normalized_source_second_moment_times_h':mesh**2*F*m2,
                 'normalized_source_third_moment_times_h2':mesh**3*F*m3})

out={'checks':['exact SU2 commutators and Haar divergence form',
               'fixed area regional exponential tilt scale and sharp tail rate',
               'exact one-plaquette hierarchy and finite h upper/lower certificates',
               'actual spatial three-rhombus Penrose 10-edge incidence',
               'nonlinear one-face character basis deterministic evaluation'],
     'nonlinear_rotor_values':rows,
     'scope':'One-face nonlinear SU2 and separate disjoint product comparison; not connected Penrose quantum vacuum',
     'status':'All algebraic assertions checked; proofs are in PROOF_REPORT.md; no stochastic simulations'}
Path(__file__).with_name('verification_output.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact Casimir/third commutator and sharp regional exponential tilt; nonlinear physical rotor checks')
for row in rows: print('h=%7.4f Var(A)/h=%9.6f m1(A)=%9.6f h*m2(A)=%9.6f h²*m3(A)=%9.6f'%(
    row['h'],row['normalized_source_variance_over_h'],row['normalized_source_first_moment'],row['normalized_source_second_moment_times_h'],row['normalized_source_third_moment_times_h2']))
