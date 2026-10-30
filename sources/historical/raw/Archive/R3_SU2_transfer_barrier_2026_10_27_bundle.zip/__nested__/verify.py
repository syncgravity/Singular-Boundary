"""Numerical sanity checks for exact SU(2) spectral/trace inequalities.

These checks supplement, but do not replace, the analytic proofs in FORMAL_NOTE.md.
"""
import json
import numpy as np
from scipy.special import ive
from scipy.linalg import sqrtm

rng=np.random.default_rng(20261027)


def z(beta):
    if beta == 0: return 1.0
    return 2*ive(1,beta)/beta


def eigen(beta,j):
    if beta == 0: return float(j==0)
    return 2*ive(int(2*j+1),beta)/beta


def psd(n):
    a=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    return a.conj().T@a/n


results={"bessel":[],"noncommutative_holder":[],"constants":{}}
for beta in [0,0.1,1,2.5,3.5,10,100,1000]:
    zz=z(beta)
    bound=np.exp(-.5)/(6*np.pi)*(1+beta)**(-1.5)
    assert zz>=bound*(1-1e-12)
    ev=[eigen(beta,j/2) for j in range(16)]
    assert min(ev)>=0
    assert abs(ev[0]-zz)<1e-13
    results['bessel'].append({'beta':beta,'z':zz,'lower_bound':bound,'min_first16_eigenvalues':min(ev)})

for n in [2,3,5]:
    for N in [2,3,5]:
        t=psd(n)+.25*np.eye(n)
        rt=np.asarray(sqrtm(t),dtype=complex)
        q=rng.integers(0,4,size=N)
        zz=z(3.5)
        ops=[]
        for qi in q:
            b=psd(n)
            b=b/(np.linalg.eigvalsh(b).max()+.1)
            ops.append(zz**(-int(qi))*(rt@b@rt))
        product=np.eye(n,dtype=complex)
        for op in ops: product=product@op
        cavity=np.trace(product).real
        complete=np.trace(np.linalg.matrix_power(t,N)).real
        bound=complete*zz**(-int(sum(q)))
        assert cavity>=-1e-8 and cavity<=bound*(1+1e-9)
        results['noncommutative_holder'].append({'matrix_size':n,'slabs':N,'q_total':int(sum(q)),'cavity':float(cavity),'holder_upper':float(bound),'ratio':float(cavity/bound)})

k,q,nu=36,14,7
C=1+k*np.log(6*np.pi)+(3*k/2)*np.log(2*nu*k)+q*(np.log(6*np.pi)+.5)
results['constants']={'k':k,'q':q,'nu':nu,'log_lambda_coefficient':1.5*(k+q),'explicit_additive_constant':float(C),'general_k_le_4q_coefficient_per_q':7.5}
with open('audit.json','w') as f: json.dump(results,f,indent=2)
print(json.dumps({'n_bessel_checks':len(results['bessel']),'n_holder_checks':len(results['noncommutative_holder']),'constants':results['constants']},indent=2))
