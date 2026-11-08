#!/usr/bin/env python3
"""PF-I1: exact arithmetic audit of the Paper-2 perpendicular-space quotient.

Uses the cyclotomic integer ring Z[X]/(1+X+X^2+X^3+X^4),
representing a+b*zeta+c*zeta^2+d*zeta^3 by 4 integer coordinates.
No arbitrary acceptance window or external dependencies are used.

Passing this script checks arithmetic identities and finite Fibonacci witnesses.
Density and torus-topology conclusions are *proved in the accompanying report*;
a finite numerical or symbolic script alone does not certify topological density.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
from itertools import product
from pathlib import Path

Z = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
X = (0, 1, 0, 0)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def scale(k, a):
    return tuple(k*x for x in a)


def multiply(a, b):
    # Modulo X^4 = -(1+X+X^2+X^3).
    c = [0] * 7
    for i in range(4):
        for j in range(4):
            c[i+j] += a[i]*b[j]
    for d in range(6, 3, -1):
        t=c[d]
        for j in range(1, 5):
            c[d-j]-=t
        c[d]=0
    return tuple(c[:4])


def power(a, n):
    out=ONE
    for _ in range(n):
        out=multiply(out,a)
    return out


def det_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    n=len(A)
    result=Fraction(1)
    for col in range(n):
        piv=next((r for r in range(col,n) if A[r][col]),None)
        if piv is None: return Fraction(0)
        if piv!=col:
            A[col],A[piv]=A[piv],A[col]
            result=-result
        val=A[col][col]
        result*=val
        for r in range(col+1,n):
            f=A[r][col]/val
            for j in range(col,n):
                A[r][j]-=f*A[col][j]
    return result


def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a


def source_projection(m, zeta_powers):
    # Fourier projection z_k(m) = sum_j m_j zeta^(k*j).
    out=Z
    for j,coefficient in enumerate(m):
        out=add(out,scale(coefficient,zeta_powers[j%5]))
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    p.add_argument('--paper2',type=Path,help='Optional PDF to hash for source integrity')
    args=p.parse_args()
    checks=0
    zeta=[power(X,k) for k in range(5)]
    assert power(X,5)==ONE;checks+=1
    assert sum((zeta[j][0] for j in range(5)))==0
    assert all(sum(zeta[j][i] for j in range(5))==0 for i in range(4));checks+=4
    assert zeta[4]==(-1,-1,-1,-1);checks+=1
    phi=neg(add(zeta[2],zeta[3]))
    assert multiply(phi,phi)==add(phi,ONE);checks+=1
    assert add(zeta[1],zeta[4])==add(phi,neg(ONE));checks+=1
    eta=zeta[2]
    eta_phi=multiply(eta,phi)
    assert eta_phi==neg(add(ONE,zeta[4]));checks+=1
    assert phi!=Z and eta!=Z and eta_phi!=Z;checks+=1

    # Exact Fibonacci best-approximation witnesses: epsilon_n=F_{n+1}-phi*F_n=(-1)^n phi^{-n}.
    fib=[]
    with localcontext() as ctx:
        ctx.prec=90
        PHI=(Decimal(1)+Decimal(5).sqrt())/2
        for n in range(1,41):
            f0,f1=fibonacci(n),fibonacci(n+1)
            eps=add(scale(f1,ONE),neg(scale(f0,phi)))
            assert multiply(eps,power(phi,n))==scale((-1)**n,ONE);checks+=1
            m=(f1,f0,0,0,f0)
            z2=source_projection(m,[zeta[(2*j)%5] for j in range(5)])
            assert z2==eps;checks+=1
            z1=source_projection(m,zeta)
            assert z1==add(scale(f1,ONE),scale(f0,add(phi,neg(ONE))));checks+=1
            eps_float=Decimal(f1)-PHI*Decimal(f0)
            assert abs(eps_float-Decimal((-1)**n)/(PHI**n))<Decimal('1e-55');checks+=1
            if n in (1,2,5,10,15,20,25,30,35,40):
                fib.append({'n':n,'F_n':f0,'F_n_plus_1':f1,'internal_real_displacement':str(eps_float),
                            'absolute_internal':str(abs(eps_float)),
                            'physical_real_displacement':str(Decimal(f1)+(PHI-1)*Decimal(f0))})

    # Fixed-sum slice (A4) still has dense internal image: 5 H subset projection(A4).
    # Pointwise arithmetic test of n = 5m - (sum m_j)*(1,1,1,1,1).
    p2=[zeta[(2*j)%5] for j in range(5)]
    for m in product(range(-2,3), repeat=5):
        S=sum(m)
        n=tuple(5*x-S for x in m)
        assert sum(n)==0;checks+=1
        assert source_projection(n,p2)==scale(5,source_projection(m,p2));checks+=1

    # The joint 4-dimensional Fourier image is a full-rank lattice: Gram of four generators.
    # G_ij = cos(2*pi(i-j)/5)+cos(4*pi(i-j)/5) = 2 if i=j else -1/2.
    Gram=[[Fraction(2) if i==j else Fraction(-1,2) for j in range(4)] for i in range(4)]
    gram_det=det_fraction(Gram)
    assert gram_det==Fraction(125,16);checks+=1
    # Principal minors >0 prove Gram positive definite; hence rank 4 and discrete.
    minors=[]
    for k in range(1,5):
        v=det_fraction([row[:k] for row in Gram[:k]])
        assert v>0;checks+=1
        minors.append(str(v))
    # The additive internal image has rank 4, not a discrete rank 2 lattice.
    # Proof from irrationality and 1,phi,eta,phi*eta in Z[zeta] is in report.
    report={
      'date':'2026-11-07',
      'scope':'source topology PF-I1, exact cyclotomic arithmetic; not Paper 2 spectral replication',
      'source':'Sharpe Paper 2 section 3 equation (9) and sections 2.1-2.2',
      'internal_image':'Z[zeta_5] as an additive subgroup of C, dense (proved in report)',
      'internal_quotient':'C / image has indiscrete quotient topology; NOT topological T2',
      'fixed_sum_zero_image':'dense because 5*image(Z5) lies in image(A4)',
      'joint_quotient':'C^2 / Lambda_F is a compact topological real 4-torus',
      'integer_kernel':'Z*(1,1,1,1,1)',
      'gram_4d':[[str(x) for x in row] for row in Gram],
      'gram_principal_minors':minors,
      'gram_determinant':str(gram_det),
      'joint_lattice_covolume_exact':'5*sqrt(5)/4',
      'fibonacci_convergent_witnesses':fib,
      'finite_checks_passed':checks,
      'acceptance_window_authenticated':False,
      'original_generator_authenticated':False,
      'spectral_zeta_reproduced':False,
      'physical_dimension_derived':False,
      'mass_gap_proved':False,
    }
    if args.paper2:
        report['paper2_sha256']=hashlib.sha256(args.paper2.read_bytes()).hexdigest()
    s=json.dumps(report,sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(s)
    print(s)

if __name__=='__main__':
    main()
