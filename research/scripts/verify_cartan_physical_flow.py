#!/usr/bin/env python3
"""Exact invariant Cartan-planar SU(2) cubic Wilson flow, mesh-uniform nonlinear estimates.
No claim about positive-probability events in the interacting SU(2) vacuum or a gap.
"""
from __future__ import annotations
import json, math, argparse
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply
from scipy.integrate import solve_ivp


def planar(n):
    """Oriented open 2D cell complex; B2: faces x edges, L = B2 B2*."""
    edges = [((i,j),axis) for i in range(n+1) for j in range(n+1) for axis in (0,1) if (i if axis==0 else j)<n]
    idx={e:i for i,e in enumerate(edges)}
    rows=[];cols=[];vals=[]
    for i in range(n):
        for j in range(n):
            f=i*n+j
            terms=[(((i,j),0),1),(((i+1,j),1),1),(((i,j+1),0),-1),(((i,j),1),-1)]
            for term,sgn in terms:
                rows.append(f);cols.append(idx[term]);vals.append(sgn)
    B=coo_matrix((vals,(rows,cols)),shape=(n*n,len(edges)),dtype=float).tocsr()
    L=(B@B.T).tocsr()
    assert np.max(np.abs(L.diagonal()-4))<1e-15
    assert np.max(np.abs(L).sum(axis=1))<=8+1e-12
    return B,L,edges


def smooth_angles(n,edges):
    h=1/n
    a=[]
    for (i,j),axis in edges:
        if axis==0:
            a.append(h*0.17*math.cos(2*math.pi*j/n)*math.sin(math.pi*(i+.5)/n))
        else:
            a.append(h*0.31*math.sin(2*math.pi*i/n)*math.sin(math.pi*(j+.5)/n))
    return np.array(a,dtype=float)


def evolve(n,tau,init_scale=1.):
    B,L,edges=planar(n)
    h=1/n
    theta=smooth_angles(n,edges)*init_scale
    F0=(B@theta)/h**2
    M=float(np.max(np.abs(F0)))
    delta=h**2*M/2
    assert delta<math.pi/2
    H0=.5*h*h*float(F0@F0)
    Bt=B.T.tocsr()
    def rhs(t,y):
        F=y[:-2]
        u=np.sin(.5*h*h*F)
        Fdot=-(L@u)/(2*h**4)
        gF=Bt@F; gu=Bt@u
        dissip=float(gF@gu)/(2*h*h)
        int_grad=float(gF@gF)
        return np.r_[Fdot,dissip,int_grad]
    z0=np.r_[F0,0.,0.]
    sol=solve_ivp(rhs,(0,tau),z0,method='DOP853',rtol=7e-11,atol=2e-12)
    assert sol.success,sol.message
    F=sol.y[:-2,-1]
    D,gradtime=map(float,sol.y[-2:,-1])
    H=.5*h*h*float(F@F)
    lin=expm_multiply((-tau/(4*h*h))*L,F0,traceA=(-tau/(4*h*h))*float(L.diagonal().sum()))
    err=float(np.max(np.abs(F-lin)))
    err2=h*float(np.linalg.norm(F-lin))
    eta=1-math.cos(delta); kappa=math.cos(delta)
    unconditional_l2_bound=eta/math.sqrt(2*kappa)*(h*float(np.linalg.norm(F0)))
    theoretical=tau*h*h*M**3/12
    max_final=float(np.max(np.abs(F)))
    assert max_final<=M+2e-9
    assert D>=-1e-11 and H<=H0+1e-9
    assert abs(H0-H-D)<1e-7,(H0,H,D)
    assert err<=theoretical+2e-9,(n,tau,err,theoretical)
    assert err2<=unconditional_l2_bound+2e-9,(n,tau,err2,unconditional_l2_bound)
    assert H+math.cos(delta)/4*gradtime<=H0+1e-7
    return dict(n=n,h=h,tau=tau,initial_F_sup=M,initial_q_sup=delta,final_F_sup=max_final,
                initial_physical_F_L2_energy=H0,final_physical_F_L2_energy=H,
                integrated_nonlinear_dissipation=D,integrated_face_gradient_sq=gradtime,
                nonlinear_linear_sup_error=err,rigorous_sup_error_bound=theoretical,
                nonlinear_linear_L2h_error=err2,rigorous_alltime_L2h_bound=unconditional_l2_bound,
                normalized_error_vs_h2=err/h**2,
                identity_error=abs(H0-H-D),evals=sol.nfev)


def full_3d_cartan_test(n):
    from verify_nonlinear_energy_flow import cubical,qexp,action_gradient,ode_rhs
    geom=cubical(n); B,L,plane_edges=planar(n)
    h=1/n
    angles=smooth_angles(n,plane_edges)
    edge_angle=dict(zip(plane_edges,angles))
    a=np.array([edge_angle.get(((i,j),axis),0.) if axis in (0,1) else 0. for (i,j,k),axis in geom['edges']])
    q0=qexp(np.column_stack([np.zeros(len(a)),np.zeros(len(a)),a]))
    S,gradient,defects=action_gradient(q0,geom)
    # Direct oriented 3D edge/face incidence B3.
    id4=geom['ids'];sign4=geom['signs'];r=np.repeat(np.arange(len(id4)),4)
    mat=coo_matrix((sign4.flatten(),(r,id4.flatten())),shape=(len(id4),len(a))).tocsr()
    b3=mat@a
    pred=.5*(mat.T@np.sin(b3/2))
    err=float(np.max(np.abs(gradient[:,2]-pred)))
    transverse=float(np.max(np.abs(gradient[:,:2])))
    zforce=float(np.max(np.abs(gradient[[i for i,e in enumerate(geom['edges']) if e[1]==2],:])))
    assert err<1e-12 and transverse<1e-12 and zforce<1e-12,(err,transverse,zforce)
    assert np.count_nonzero(np.abs(b3)>1e-12)<=n*n*(n+1)
    tau=.025
    sol=solve_ivp(lambda s,y:ode_rhs(s,y,geom),(0,tau/h**2),q0.flatten(),method='DOP853',rtol=2e-10,atol=4e-12)
    assert sol.success,sol.message
    qfin=sol.y[:,-1].reshape(-1,4)
    # Since all links stay in the same Cartan subgroup and identical across z,
    # compare bottom XY face flux with the exact scalar nonlinear ODE.
    # Compare face values by coordinates using each layer: use matrix b3 at initial
    # and reconstruct scalar via the exact planar B map.
    theta=smooth_angles(n,plane_edges)
    f0=B@theta/h**2
    def rhsF(t,y):return -(L@np.sin(.5*h*h*y))/(2*h**4)
    small=solve_ivp(rhsF,(0,tau),f0,method='DOP853',rtol=2e-11,atol=5e-12)
    assert small.success
    f=small.y[:,-1]
    # final 3D plaquette group angles follow the independent full SU2 quaternion integration.
    full_b=[];full_coords=[]
    from verify_nonlinear_energy_flow import quats_and_parts
    P=quats_and_parts(qfin,geom)[1][-1]
    for idx,face in enumerate(geom['ids']):
        dirs=[geom['edges'][e][1] for e in face]
        if set(dirs)=={0,1}:
            v=2*math.atan2(P[idx,3],P[idx,0])/h**2
            (i,j,k),_=geom['edges'][face[0]]
            full_b.append(v)
            full_coords.append((i,j,k))
    mismatch=0.
    for v,(i,j,k) in zip(full_b,full_coords):
        mismatch=max(mismatch,abs(v-f[i*n+j]))
    uniterr=float(np.max(abs(np.linalg.norm(qfin,axis=1)-1)))
    noncartan=float(np.max(np.abs(qfin[:,1:3])))
    assert mismatch<4e-8,(n,mismatch)
    assert noncartan<3e-10 and uniterr<2e-10
    return dict(n=n,vertices=len(geom['verts']),links=len(geom['edges']),faces=len(geom['ids']),
                force_reduction_error=err,noncartan_force=transverse,vertical_link_force=zforce,
                full_su2_vs_scalar_flux_error=mismatch,postflow_noncartan_quat=noncartan,
                unit_norm_error=uniterr)



def concentrated(n,tau):
    """True planar Cartan links realizing one localized face q=h, E_3D->4."""
    from scipy.sparse.linalg import spsolve
    B,L,_=planar(n)
    h=1/n
    q0=np.zeros(n*n)
    q0[(n//2)*n+(n//2)]=h
    # B has full row rank on an open disk, so b=2q is realizable
    # by actual link angles theta=B* L^-1 (2q), not independent face guesses.
    theta=B.T@spsolve(L,2*q0)
    assert np.max(np.abs(B@theta-2*q0))<1e-10
    ephys=8*(n+1)/h*(1-math.cos(h))
    M=math.sqrt(2*(.5*h*h*np.dot(2*q0/h**2,2*q0/h**2)))
    F0=2*q0/h**2
    def rhs(t,F):return -(L@np.sin(.5*h*h*F))/(2*h**4)
    sol=solve_ivp(rhs,(0,tau),F0,method='DOP853',rtol=4e-10,atol=1e-10)
    assert sol.success
    F=sol.y[:,-1]
    linear=expm_multiply((-tau/(4*h*h))*L,F0,traceA=(-tau/(4*h*h))*float(L.diagonal().sum()))
    eta=1-math.cos(h); kappa=math.cos(h)
    l2err=h*np.linalg.norm(F-linear)
    bound=eta/math.sqrt(2*kappa)*(h*np.linalg.norm(F0))
    assert l2err<=bound+2e-9,(n,tau,l2err,bound)
    assert np.max(np.abs(F))<=np.max(np.abs(F0))+1e-8
    # Any universal lattice Nash constant C_N>=1 suffices numerically here.
    diagnostic=math.sqrt(tau)*np.max(np.abs(F))/math.sqrt(ephys)
    return dict(n=n,h=h,tau=tau,exact_link_flux_residual=float(np.max(np.abs(B@theta-2*q0))),
        initial_physical_3d_energy=ephys,initial_max_physical_curvature=float(np.max(np.abs(F0))),
        final_max_physical_curvature=float(np.max(np.abs(F))),
        dimensionless_positive_time_smoothing_ratio=diagnostic,
        nonlinear_linear_L2h_error=float(l2err),rigorous_alltime_L2h_bound=float(bound),
        initial_curvature_L2_2D=float(M))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    results=[evolve(n,tau) for n in (6,10,16,24,32) for tau in (.018,.075)]
    geometry=[full_3d_cartan_test(n) for n in (2,3)]
    local_defects=[concentrated(n,tau) for n in (8,16,32) for tau in (.02,.05)]
    out=dict(status='PASS',model='Exact nonlinear SU2 Cartan-planar embedded invariant sector in 3D open cubic Wilson gradient flow',
             scope='Classical two-dimensional spatial curvature sector; measure zero under finite true SU2 Wilson vacuum. No full non-Abelian 3D / 4D quantum statement.',
             cubic_embedding_checks=geometry,nonlinear_curvature_checks=results,localized_realizable_energy_cases=local_defects,
             analytic_certificates={'F_sup':'||F_h(tau)||_infty <= ||F_h(0)||_infty provided ||h² F_h(0)/2||_infty<pi/2',
                'nonlinear_minus_linear':'||F_h(tau)-exp(-tau L/(4h²))F_h(0)||_infty <= tau h² ||F_h(0)||_infty³/12',
                'energy':'H(tau)+cos(delta)/4 int_0^tau ||B*F||² dt <= H(0), H=h²||F||²/2',
                'nonlinear_positive_time_nash':'||F(tau)||_infty <= sqrt(2 C_N/(kappa tau)) ||F(0)||_(2,h); kappa=cos(delta), C_N is universal discrete 2D Dirichlet Nash constant',
                'alltime_nonlinear_linear_L2':'||F_nonlinear(tau)-F_linear(tau)||_(2,h) <= (1-cos(delta))/sqrt(2cos(delta)) ||F0||_(2,h), all tau>=0'},
             open=['No genuinely non-Abelian commutator control on full SU2 configuration ensemble',
                   'No true interacting vacuum mass or nonvanishing continuum covariance',
                   'No 4D OS reconstruction or full Schur mass-gap estimate',
                   'No 3D Penrose/quasicrystal regulator or gravitational UV theorem'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','mesh_count':len(results),'embedding_count':len(geometry),
      'max_reduced_force_err':max(x['force_reduction_error'] for x in geometry),
      'max_reduced_dynamics_err':max(x['full_su2_vs_scalar_flux_error'] for x in geometry),
      'max_energy_err':max(x['identity_error'] for x in results),
      'largest_vs_bound':max(x['nonlinear_linear_sup_error']/x['rigorous_sup_error_bound'] for x in results),
      'max_localized_positive_time_ratio':max(x['dimensionless_positive_time_smoothing_ratio'] for x in local_defects),
      'worst_alltime_L2_ratio':max([x['nonlinear_linear_L2h_error']/x['rigorous_alltime_L2h_bound'] for x in results+local_defects])},indent=2))
if __name__=='__main__':main()
