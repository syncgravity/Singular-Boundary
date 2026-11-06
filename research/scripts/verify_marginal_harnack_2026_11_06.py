#!/usr/bin/env python3
"""Finite SU(2) Wilson vacuum marginal/heat-kernel Harnack and physical-loop UV-sum-rule checks.
No continuum or YM mass-gap result. Independent finite-dimensional response check is NOT an SU(2) model.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from scipy.integrate import quad


def delta_upper(s: float) -> float:
    # SU2 heat eigenvalue n(n+2)/4, n>=1.  For n>=2, n(n+2)/4>=n.
    q=math.exp(-s)
    return 4.0*math.exp(-3*s/4) + ((1+q)/(1-q)**3 -1 -4*q)


def cubic(n: int, g_squared: float, s: float=8.0):
    E=3*n*(n+1)**2
    F=3*n*n*(n+1)
    h=1.0/n
    alpha=g_squared/(2*h)
    beta=2/(g_squared*h)
    assert E - F + n**3 - (n+1)**3==-1  # Euler V-E+F-C =1
    d=delta_upper(s)
    assert 0 < d < .01
    heat_logratio=math.log((1+d)/(1-d))
    Lambda=(2*s*beta*F/alpha)+E*heat_logratio
    assert abs((2*s*beta*F/alpha) - 8*s*F/(g_squared*g_squared)) <1e-8*max(1,Lambda)
    L_loop=4*n  # unit square boundary in the fixed [0,1]^3 physical box: length 4
    first_Haar=0.75*alpha*L_loop
    return dict(n=n,E=E,F=F,vertices=(n+1)**3,cubes=n**3,h=h,g_squared=g_squared,
                alpha=alpha,beta=beta,Lambda=Lambda,loop_edge_count=L_loop,
                first_moment_Haar=first_Haar,heat_kernel_delta_upper=d,
                log_density_ratio_bound=2*Lambda)


def random_su2_quaternion(rng, count):
    a=rng.normal(size=(count,4));a/=np.linalg.norm(a,axis=1)[:,None];return a

def qmultiply(a,b):
    # a=(a0,a_vec); b similarly. Implement batch quaternion product.
    av=a[:,1:];bv=b[:,1:]
    return np.column_stack((a[:,0]*b[:,0]-np.einsum('ij,ij->i',av,bv),
           a[:,0,None]*bv+b[:,0,None]*av+np.cross(av,bv)))


def haar_regression():
    rng=np.random.default_rng(20261106)
    rows=[];N=140000
    for L in (1,2,4,8,16):
        u=np.zeros((N,4));u[:,0]=1
        for _ in range(L):u=qmultiply(u,random_su2_quaternion(rng,N))
        W=2*u[:,0]
        m=float(W.mean());v=float(W.var());grad=float(np.mean(1-W*W/4))
        assert abs(m)<.012 and abs(v-1)<.022 and abs(grad-.75)<.01,(L,m,v,grad)
        rows.append(dict(links=L,mean_W=m,var_W=v,avg_su2_grad_squared=grad,haar_expected_first_moment_factor=.75))
    return rows


def finite_response_regression():
    # A 4-state positivity-improving finite analogue checks the universal spectral
    # susceptibility contraction. This is NOT numerical lattice SU(2).
    edges=((0,1),(0,2),(1,3),(2,3),(0,3))
    K=np.zeros((4,4))
    for i,j in edges:
        K[i,i]+=1;K[j,j]+=1;K[i,j]-=1;K[j,i]-=1
    source=np.diag([0.0,1.1,2.0,0.6])
    def get(theta):
        vals,vecs=eigh(K+theta*source)
        Om=vecs[:,0]
        if Om.sum()<0: Om=-Om
        assert np.min(Om)>0
        rho=np.array([sum(Om[:2]**2),sum(Om[2:]**2)])
        return vals,Om,np.sqrt(rho)
    out=[]
    for theta in (0., .2,1.0,3.0):
        vals,Om,r=get(theta);eps=1.e-5
        speed=np.linalg.norm((get(theta+eps)[2]-get(theta-eps)[2])/(2*eps))
        avg=float(Om@source@Om)
        sd=math.sqrt(float(Om@source@source@Om)-avg*avg)
        gap=float(vals[1]-vals[0]);bound=sd/gap
        assert speed<bound+1e-5,(theta,speed,bound)
        out.append(dict(theta=theta,coarse_hellinger_speed=float(speed),spectral_susceptibility_bound=bound,
                        finite_gap=gap,source_standard_deviation=sd))
    return out


def relative_marginal_transfer():
    # These are admissible positive SU2 class densities, not claimed to be
    # exact ground-state marginals of any 3D cubic Wilson Hamiltonian.
    from scipy.special import iv
    results=[]
    for kappa in (0.0,0.05,0.2,0.5,1.0):
        a0=float(iv(0,2*kappa)-iv(2,2*kappa))
        def moment(power):
            def integrand(theta):
                W=2*math.cos(theta)
                return (2/math.pi)*math.sin(theta)**2*math.exp(kappa*W)/a0*W**power
            return quad(integrand,0,math.pi,epsabs=1e-12)[0]
        mu=moment(1); m2=moment(2); variance=m2-mu*mu
        G=1-m2/4; q=G/variance
        delta=2*abs(kappa)+abs(math.log(a0))
        k=4.0 # g_f^2/g_c^2 =1 with two-link dyadic spatial refinement
        ratio=k*(q/.75)
        lo=k*math.exp(-2*delta);hi=k*math.exp(2*delta)
        assert lo-1e-10<=ratio<=hi+1e-10,(kappa,ratio,lo,hi)
        if kappa==0.:assert abs(ratio-4)<1e-10
        results.append(dict(kappa=kappa,log_density_ratio_sup=delta,normalized_loop_q=q,
            moment_ratio_two_scales=ratio,rigorous_ratio_interval=[lo,hi]))
    return results


def counterexample():
    M=1.0
    rows=[]
    for h in (.5,.25,.125,.0625):
        high=h**(-3)
        first=(1-h)*M+h*high
        assert high>=M and first>=M and first>(1-h)*M
        rows.append(dict(h=h,gap=M,high_energy=high,high_energy_weight=h,
                         first_moment=first,correlation_at_t1=(1-h)*math.exp(-M)+h*math.exp(-high)))
    return rows


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path('verification.json'));a=ap.parse_args()
    d=delta_upper(8)
    rows=[cubic(n,1.0) for n in (1,2,4,8,16)]
    stats={'scope':'finite SU2 Wilson/vacuum Harnack and exact Wilson first-moment formula; NOT interacting continuum',
       'status':'PASS','heat_kernel_time_s':8,'delta_8_upper':d,'delta_8_less_than_one_hundredth':d<.01,
       'clean_heat_kernel_ratio_upper':'101/99',
       'Harnack_log_bound':'Lambda=64F/g0^4 + E log(101/99), for g_squared=g0^2',
       'marginal_pointwise_bounds':'exp(-2 Lambda) <= rho_X <= exp(2 Lambda)',
       'Wilson_variance_bounds':'exp(-2 Lambda) <= Var_rho(W) <= exp(2 Lambda)',
       'first_moment_bounds':'(3/4) alpha L exp(-4 Lambda) <= -C_f_prime(0) <= (3/4) alpha L exp(4 Lambda)',
       'first_moment_exact':'alpha L E_rho(1-W^2/4) / Var_rho(W)',
       'conditional_two_scale_transfer':'If |log(rho_f/rho_c)|<=delta on the same fixed loop, then k exp(-2delta)<=m1_f/m1_c<=k exp(2delta), k=4 g_f^2/g_c^2',
       'necessary_marginal_mismatch':'If |log(m1_f/m1_c)|<=epsilon, then delta>=max(0,(abs(log(k))-epsilon)/2), k=4 g_f^2/g_c^2',
       'cubic_meshes':rows,'haar_quaternion_regression':haar_regression(),
       'four_state_response_regression_non_SU2':finite_response_regression(),
       'relative_positive_SU2_class_marginal_regression':relative_marginal_transfer(),
       'high_energy_spectral_counterexample':counterexample(),
       'response_inequality':'||partial_theta sqrt(rho_theta)||_2 <= sqrt(Var_nu(F)) / Delta_theta <= n_faces / Delta_theta, source derivative at fixed kinetic alpha',
       'limitations':['Explicit Harnack bound grows with number of links/faces and inverse g0^4; it gives no volume/UV uniform comparison.',
       'Large normalized Wilson first moment is an ultraviolet diagnostic, not evidence of zero infrared mass gap.',
       'The relative-marginal test uses admissible class densities, not solved interacting cubic Wilson vacua.',
       'Finite source-response estimate uses inverse of finite spectral gap: using it to infer a uniform gap would be circular.',
       'Four-state matrix regression is not an SU2 gauge field and is used only to test the general perturbation inequality.',
       'No actual finite 3D interacting ground state Omega has been numerically solved.']}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(stats,indent=2)+'\n')
    print('PASS: SU2 heat Harnack; 5 physical loop UV sum rules; 140000×5 Haar quaternions; four-state response; relative-marginal transfer; positive spectral counterexample')
    print('delta8 upper',d,'mesh first Haar moments',[(x['n'],x['first_moment_Haar']) for x in rows])

if __name__=='__main__':main()
