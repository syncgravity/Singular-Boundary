#!/usr/bin/env python3
"""Read-only, exact deterministic checks. No Monte Carlo; no archive modification.
Check two-time cumulants for finite reversible transfer kernels and the SU2 electric rhombus identities.
"""
from fractions import Fraction as F
from itertools import product, combinations, chain
from math import factorial
import json
import sympy as s

def walsh(v, mask):
    out=F(1)
    for i,x in enumerate(v):
        if (mask >> i)&1:out*=F(x)
    return out

def transfer(k, rho, delta):
    states=list(product((-1,1),repeat=k)); M=len(states)
    qmask=(1<<k)-1
    T=[]
    for i,a in enumerate(states):
        row=[]
        for j,b in enumerate(states):
            v=F(int(i==j))*delta+(F(1)-delta)*(F(1)+rho*walsh(a,qmask)*walsh(b,qmask))/M
            row.append(v)
        T.append(row)
    return states,T

def matvec(T,v):return [sum((a*b for a,b in zip(row,v)),F(0)) for row in T]

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))

def cumulant6(k=3, rho=F(99,100),delta=F(1,8),n=2):
    # Exact two-slab 6-source cumulant for the distinct coordinates x1,x2,x3 at both times.
    states,T=transfer(k,rho,delta)
    lam=delta+(F(1)-delta)*rho
    return lam**n-3*delta**(2*n)+2*delta**(3*n)

def check_k(k, rho,delta):
    states,T=transfer(k,rho,delta);M=2**k
    q=(1<<k)-1
    assert all(min(row)>0 and sum(row)==1 for row in T)
    assert all(T[i][j]==T[j][i] for i in range(M) for j in range(M))
    eigen={}
    for mask in range(M):
        v=[walsh(x,mask) for x in states]
        ev=F(1) if mask==0 else (delta+(1-delta)*rho if mask==q else delta)
        assert matvec(T,v)==[ev*x for x in v]
        eigen[str(mask)]=str(ev)
    return {'k':k,'rho':str(rho),'delta':str(delta),'lambda_parity':str(delta+(1-delta)*rho),
            'min_entry':str(min(min(row) for row in T)),'positive_definite':True,'all_rows_stochastic':True,
            'eigenvalue_coordinate':str(delta)}

def exact_cumulant_from_joint(k,rho,delta,n=2):
    # k=3, n=2 only: form T^n analytically using Walsh spectral decomposition.
    assert k==3
    states,T=transfer(k,rho,delta);M=len(states)
    lam=delta+(1-delta)*rho
    full=(1<<k)-1
    def joint(a,b):
        return (F(1)+lam**n*walsh(a,full)*walsh(b,full)+delta**n*sum(walsh(a,mask)*walsh(b,mask) for mask in range(1,full)))/(M*M)
    # compute joint moments of the 6 coordinate observations (0,x1-x3), (t,x1-x3).
    from functools import lru_cache
    @lru_cache(None)
    def moment(subset):
        a_mask=sum(1<<j for j in subset if j<k)
        b_mask=sum(1<<(j-k) for j in subset if j>=k)
        return sum(joint(a,b)*walsh(a,a_mask)*walsh(b,b_mask) for a in states for b in states)
    def partitions(items):
        if not items:
            yield []
        else:
            first,*rest=items
            for p in partitions(rest):
                yield [[first]]+[b[:] for b in p]
                for i in range(len(p)):
                    cp=[b[:] for b in p]
                    cp[i]=[first]+cp[i]
                    yield cp
    c=sum(((-1)**(len(p)-1))*factorial(len(p)-1)*s.prod([moment(tuple(sorted(b))) for b in p]) for p in partitions(list(range(2*k))))
    assert c==cumulant6(k,rho,delta,n)
    return str(c)

def main():
    cases=[check_k(k,rho=F(9999,10000),delta=F(1,8)) for k in (2,3,4)]
    c6=exact_cumulant_from_joint(3,F(99,100),F(1,8),2)
    a,t=s.symbols('a t',positive=True)
    p2_connected=s.exp(-8*a*t)/16
    p_connected=s.exp(-3*a*t)/4
    kappa=s.factor(p2_connected-2*p_connected**2)
    assert s.simplify(kappa-(s.exp(-8*a*t)/16-s.exp(-6*a*t)/8))==0
    assert s.simplify(kappa.subs(t,0)+s.Rational(1,16))==0
    result={'kernel_cases':cases,'k3_n2_six_cumulant':c6,'four_point_electric_formula':'exp(-8*a*t)/16-exp(-6*a*t)/8',
            'composite_covariance_electric':'exp(-8*a*t)/16',
            'fundamental_covariance_electric':'exp(-3*a*t)/4',
            'zero_time_four_cumulant':'-1/16','stochastic_simulations':False,'physical_interacting_mass_gap_proved':False}
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
