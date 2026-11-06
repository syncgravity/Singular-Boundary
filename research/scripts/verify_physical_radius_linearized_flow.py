#!/usr/bin/env python3
"""Finite cubical SU(2) flat-field linearization (three color copies),
physical-scale heat estimates, periodic Fourier control, and a nonlinear
one-plaquette Haar countercheck. No interacting YM continuum claim.
"""
from __future__ import annotations
import argparse, json, math
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply
from scipy.integrate import quad


def cubic(n: int):
    verts=[(i,j,k) for i in range(n+1) for j in range(n+1) for k in range(n+1)]
    vid={v:i for i,v in enumerate(verts)}
    edges=[]; ed={}
    for axis in range(3):
        for v in verts:
            if v[axis]<n:
                ed[(axis,*v)]=len(edges)
                edges.append((axis,v))
    row=[]; col=[]; data=[]
    for idx,(a,v) in enumerate(edges):
        end=list(v);end[a]+=1
        row.extend((idx,idx));col.extend((vid[v],vid[tuple(end)]));data.extend((-1,1))
    d0=coo_matrix((data,(row,col)),shape=(len(edges),len(verts))).tocsr()
    faces=[];row=[];col=[];data=[]
    for a,b in ((0,1),(0,2),(1,2)):
        for v in verts:
            if v[a]<n and v[b]<n:
                ip=len(faces);faces.append((a,b,v))
                va=list(v);va[a]+=1
                vb=list(v);vb[b]+=1
                # oriented square: +a at v, +b at v+e_a, -a at v+e_b, -b at v
                for axis,z,sign in ((a,v,1),(b,tuple(va),1),(a,tuple(vb),-1),(b,v,-1)):
                    row.append(ip);col.append(ed[(axis,*z)]);data.append(sign)
    d1=coo_matrix((data,(row,col)),shape=(len(faces),len(edges))).tocsr()
    assert (d1@d0).nnz==0 or np.max(abs((d1@d0).data))<1e-14
    assert len(verts)==(n+1)**3 and len(edges)==3*n*(n+1)**2 and len(faces)==3*n*n*(n+1)
    assert len(verts)-len(edges)+len(faces)-n**3==1
    return verts, edges, faces, d0, d1


def norms(x,h): return math.sqrt(h**3 * float(x@x))


def open_cube_test(n:int,tau:float):
    verts,edges,faces,d0,d1=cubic(n);h=1/n
    def A(axis,pos):
        x,y,z=(np.array(pos,dtype=float)+0)/n
        if axis==0:x+=h/2
        if axis==1:y+=h/2
        if axis==2:z+=h/2
        return (math.sin(math.pi*y)*math.cos(math.pi*z),
                math.sin(math.pi*z)*math.cos(math.pi*x),
                math.sin(math.pi*x)*math.cos(math.pi*y))[axis]
    a=np.array([h*A(axis,v) for axis,v in edges]); b0=(d1@a)/(h*h)
    edge_op=(d1.T@d1).tocsr()
    face_op=(d1@d1.T).tocsr()
    # flat-SU2 linearized gradient flow: a'(s) = -(1/4) d* d a, s=tau/h^2
    a1=expm_multiply((-tau/(4*h*h))*edge_op,a)
    b1=expm_multiply((-tau/(4*h*h))*face_op,b0)
    commutation=norms((d1@a1)/(h*h)-b1,h)
    assert commutation<5e-11,(n,commutation)
    phi=np.array([math.sin(1+2*math.pi*x/(n+1))*math.cos(2*math.pi*y/(n+1)) for x,y,z in verts]);
    shifted=expm_multiply((-tau/(4*h*h))*edge_op,a+d0@phi)
    gauge=norms(shifted-(a1+d0@phi),h)
    assert gauge<2e-11,(n,gauge)
    contraction=norms(b1,h)/norms(b0,h)
    grad=math.sqrt(h**3 * float(b1@(face_op@b1)))/h
    lap=norms(face_op@b1,h)/(h*h)
    grad_bound=math.sqrt(2/(math.e*tau))*norms(b0,h)
    lap_bound=(4/(math.e*tau))*norms(b0,h)
    assert norms(b0,h)>0.1
    assert contraction<=1+2e-12
    assert grad<=grad_bound+1e-11 and lap<=lap_bound+1e-11,(n,grad,grad_bound,lap,lap_bound)
    return {'n':n,'h':h,'V':len(verts),'E':len(edges),'F':len(faces),'tau':tau,
      'initial_curvature_norm':norms(b0,h),'flow_curvature_norm':norms(b1,h),
      'curvature_contraction':contraction,'commutation_L2_error':commutation,'linearized_gauge_shift_error':gauge,
      'physical_gradient_norm':grad,'gradient_bound':grad_bound,
      'physical_laplacian_norm':lap,'laplacian_bound':lap_bound}


def periodic_mode(n:int,k:tuple[int,int,int],tau:float):
    h=1/n
    assert all(abs(i)<=n//2 for i in k),('alias',n,k)
    lam=4/h**2*sum(math.sin(math.pi*ki*h)**2 for ki in k)
    continuum=4*math.pi**2*sum(ki**2 for ki in k)
    discrepancy=continuum-lam
    spectral_bound=4*math.pi**4*h**2/3 *sum(ki**4 for ki in k)
    heat=math.exp(-tau*lam/4)
    heat_cont=math.exp(-tau*continuum/4)
    heat_err=abs(heat-heat_cont)
    heat_bound=tau*math.pi**4*h**2/3*sum(ki**4 for ki in k)
    assert discrepancy>=-1e-11 and discrepancy<=spectral_bound+1e-11
    assert heat_err<=heat_bound+1e-11
    return {'n':n,'mode':list(k),'tau':tau,'physical_curl_laplacian_eigenvalue':lam,
            'continuum_eigenvalue':continuum,'eigenvalue_discrepancy':discrepancy,
            'rigorous_eigenvalue_error_bound':spectral_bound,
            'flow_multiplier':heat,'continuum_multiplier':heat_cont,
            'multiplier_error':heat_err,'rigorous_mult_error_bound':heat_bound}


def oneplaquette(eps:float):
    # a=tanh(s), eps=1-a: s = atanh(1-eps).
    a=1-eps; s=math.atanh(a)
    def p(t): return (2/math.pi)*math.sqrt(max(0,t*(2-t)))
    def d(t): return eps*(2-t)/(eps+(1-eps)*t)
    def dp(t): return eps*(2-eps)/(eps+(1-eps)*t)**2
    # SU2 metric |grad x|²=(1-x²)/4 = t(2-t)/4
    marks=sorted(set([0,eps,10*eps,100*eps,0.5,1,2]));marks=[t for t in marks if t<=2]
    def integ(f): return sum(quad(f,marks[i],marks[i+1],epsabs=2e-12,epsrel=2e-11,limit=160)[0] for i in range(len(marks)-1))
    mean_d=integ(lambda t:p(t)*d(t))
    second=integ(lambda t:p(t)*d(t)**2)
    var=second-mean_d**2
    dirichlet=integ(lambda t:p(t)*t*(2-t)/4*dp(t)**2)
    assert var>0
    return {'epsilon':eps,'flow_s':s,'haar_mean_of_one_minus_xflow':mean_d,'variance_xflow':var,
            'curvature_fundamental_Haar_dirichlet':dirichlet,
            'normalized_four_link_electric_moment_over_alpha':4*dirichlet/var,
            'asymptotic_mean_coeff_check':mean_d/(3*eps),
            'asymptotic_variance_coeff_check':var/(4*math.sqrt(2)*eps**1.5),
            'asymptotic_dirichlet_coeff_check':dirichlet/(math.sqrt(2)/4*math.sqrt(eps)),
            'asymptotic_electric_moment_coeff_check':4*dirichlet/var*4*eps}


def nonlinear_plaquette_temporal_correlation(s:float, t:float, N:int=2048, modes:int=120):
    """Free electric four-link reference, NOT interacting Wilson vacuum.
    SU2 Haar Gauss-Chebyshev quadrature; characters chi_n=U_n(x), Casimir n(n+2)/4.
    """
    k=np.arange(1,N+1,dtype=float)
    theta=np.pi*k/(N+1)
    x=np.cos(theta)
    weight=2/(N+1)*np.sin(theta)**2
    assert abs(weight.sum()-1)<3e-14
    a=math.tanh(s)
    xf=(x+a)/(1+a*x)
    mean=float(weight@xf)
    variance=float(weight@((xf-mean)**2))
    f=(xf-mean)/math.sqrt(variance)
    u0=np.ones_like(x);u1=2*x
    coeff=[]
    for n in range(modes+1):
        if n==0:un=u0
        elif n==1:un=u1
        else:
            un=2*x*u1-u0
            u0,u1=u1,un
        coeff.append(float(weight@(f*un)))
    # eliminate n=0 (vacuum); 4-link electric generator gives e^{-t*n(n+2)}
    cs=float(sum(coeff[n]**2*math.exp(-t*n*(n+2)) for n in range(1,modes+1)))
    parsed=float(sum(v*v for v in coeff[1:]))
    assert abs(coeff[0])<2e-10
    assert 0<=cs<=1+1e-8
    return {'s':s,'physical_quantum_time_t_in_alpha_units':t,'N_haar_nodes':N,
      'n_character_modes':modes,'connected_correlation':cs,
      'character_parseval_partial':parsed,
      'free_electric_4_link_Haar_reference_only':True}


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',default='docs/evidence/R3_PHYSICAL_RADIUS_LINEARIZED_FLOW_2026-11-05.json');a=p.parse_args()
    cases=[open_cube_test(n,tau) for n in (2,3,4,6) for tau in (0.025,0.1)]
    fourier=[periodic_mode(n,k,.1) for k in [(1,0,0),(1,1,0)] for n in (4,8,16,32,64)]
    plaquettes=[oneplaquette(e) for e in (0.1,0.03,0.01,0.003,0.001,0.0003,0.00003)]
    correlations=[nonlinear_plaquette_temporal_correlation(s,.2) for s in (0.,.4,.8,1.5,2.5,3.5,4.5,5.5,6.5)]
    assert correlations[-1]['connected_correlation']<correlations[0]['connected_correlation']
    assert abs(correlations[0]['connected_correlation']-math.exp(-.6))<2e-12
    # Nonlinear rare-event mode agrees with predicted power laws at smaller epsilon.
    last=plaquettes[-1]
    assert abs(last['asymptotic_variance_coeff_check']-1)<.08,last
    assert abs(last['asymptotic_dirichlet_coeff_check']-1)<.08,last
    assert abs(last['asymptotic_electric_moment_coeff_check']-1)<.08,last
    result={'status':'PASS','scope':'linearized flat SU2 cubic spatial Wilson flow only; periodized Fourier control; isolated plaquette nonlinear Haar reference; no interacting vacuum continuum or gap',
            'linearization':'A_s=-(d1.T d1)/4 A; physical tau=h² s; curvature F_h=d1 A /h²',
            'open_cube':cases,'periodic_fourier':fourier,'nonlinear_isolated_plaquette':plaquettes,'four_link_free_electric_temporal_correlations':correlations,
            'uniform_bound':'||((dd*)/h²)^(k/2) F_h(tau)|| <= (2k/(e tau))^(k/2) ||F_h(0)||, k=1,2',
            'Fourier_O_h2':'0<=4pi²|k|²-lambda_h<=4pi⁴h² sum(k_i⁴)/3; exp multiplier <=tau*pi⁴*h² sum(k_i⁴)/3',
            'nonlinear_isolated_plaquette_limit':'variance(x_s) ~4sqrt(2)*epsilon^(3/2), Haar Dirichlet ~sqrt(2)/4*epsilon^(1/2), normalized four-link first moment /alpha ~ 1/(4epsilon), epsilon=1-tanh(s)',
            'required_next':'Nonlinear physical-radius bound and nonzero interacting covariance, complete Schur/IR positive-time comparison, 4D OS, Penrose model-specific geometry'}
    import pathlib
    out=pathlib.Path(a.out);out.parent.mkdir(exist_ok=True,parents=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(cases),'open cubic heat cases;',len(fourier),'periodic Fourier controls;',len(plaquettes),'nonlinear Haar plaquettes;',len(correlations),'temporal reference controls')
    print('Worst commutation error',max(x['commutation_L2_error'] for x in cases))
    print('Nonlinear last coefficients',last['asymptotic_variance_coeff_check'],last['asymptotic_dirichlet_coeff_check'],last['asymptotic_electric_moment_coeff_check'])

if __name__=='__main__':main()
