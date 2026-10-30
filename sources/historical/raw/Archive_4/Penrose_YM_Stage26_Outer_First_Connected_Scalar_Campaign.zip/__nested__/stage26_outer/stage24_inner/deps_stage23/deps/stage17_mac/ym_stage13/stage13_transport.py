"""Stage 13: exact SU(2) temporal transporter algebra and conditional-slab estimator.

Validation-sized square torus only, not production or a continuum extraction.
State index: spatial links t*E+e; temporal links nt*E+t*V+v.
"""
import numpy as np
from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'deps/ym_stage6/source_stage5'))
sys.path.insert(0,str(HERE/'deps/ym_stage6'))
from stage6_multilevel import slab_partition,assert_slab_factorization,condition_sweeps,update_sweeps_inplace,plaquettes
from stage3_periodic_pilot import square_torus
from stage2_ym_calibration import assemble

def mat(q):
    w,x,y,z=q
    return np.array([[w+1j*z,y+1j*x],[-y+1j*x,w-1j*z]],complex)

def time_line(links,nt,E,V,vertex,t0,steps):
    T=np.eye(2,dtype=complex)
    for k in range(steps):
        T=T@mat(links[nt*E+((t0+k)%nt)*V+vertex])
    return T

def spatial_holonomy(links,E,spatial_edges,signs,t):
    H=np.eye(2,dtype=complex)
    for e,s in zip(spatial_edges,signs):
        U=mat(links[t*E+e]);H=H@(U if s==1 else U.conj().T)
    return H

def paired_matrix(B,A):
    """Pairs destination and source temporal transporters retaining both color lines."""
    return np.kron(B,np.conj(A))

def contract_paired(S0,P,S1):
    """Exact normalized SU(2) Wilson rectangle from paired temporal transporter."""
    return float(np.einsum('pi,ipjk,kj->',S0,P.reshape(2,2,2,2),S1.conj()).real/2)

def direct_rectangle(links,nt,E,V,u,v,path,sg,t0,lag):
    S0=spatial_holonomy(links,E,path,sg,t0)
    S1=spatial_holonomy(links,E,path,sg,(t0+lag)%nt)
    A=time_line(links,nt,E,V,u,t0,lag)
    B=time_line(links,nt,E,V,v,t0,lag)
    return float(np.trace(S0@B@S1.conj().T@A.conj().T).real/2)

def paired_rectangle(links,nt,E,V,u,v,path,sg,t0,slab):
    if t0%slab or nt%slab:raise ValueError('rectangle must begin at a frozen boundary')
    lag=slab*2
    P=np.eye(4,dtype=complex)
    for start in (t0,t0+slab):
        A=time_line(links,nt,E,V,u,start,slab)
        B=time_line(links,nt,E,V,v,start,slab)
        P=P@paired_matrix(B,A)
    S0=spatial_holonomy(links,E,path,sg,t0)
    S1=spatial_holonomy(links,E,path,sg,(t0+lag)%nt)
    return contract_paired(S0,P,S1)

def conditioned_rectangle(outer,lat,sp,u,v,path,sg,slab=5,inner=12,warm=12,spacing=2,seed=11):
    nt=lat['nt'];E=sp['E'];V=sp['V']
    if nt<3*slab or nt%slab:raise ValueError('need at least three slabs, including a distinct upper boundary')
    locked,allowed,group,boundaries=slab_partition(nt,E,V,slab)
    assert_slab_factorization(lat,group,locked,nt,E,V,slab)
    original=outer[locked].copy()
    state,_,err=condition_sweeps(outer,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],allowed,warm,.95,seed)
    pf=plaquettes(state,lat['fi'],lat['sg'])
    Ts=[np.zeros((4,4),complex) for _ in range(2)]
    samples=[]
    for j in range(inner):
        update_sweeps_inplace(state,pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],allowed,spacing,.95)
        Ps=[]
        for idx,start in enumerate((0,slab)):
            A=time_line(state,nt,E,V,u,start,slab)
            B=time_line(state,nt,E,V,v,start,slab)
            Q=paired_matrix(B,A)
            Ts[idx]+=Q/inner
            Ps.append(Q)
        S0=spatial_holonomy(outer,E,path,sg,0)
        S1=spatial_holonomy(outer,E,path,sg,2*slab)
        samples.append(contract_paired(S0,Ps[0]@Ps[1],S1))
    if not np.array_equal(original,state[locked]):raise AssertionError('frozen links modified')
    residual=float(np.max(np.abs(plaquettes(state,lat['fi'],lat['sg'])-pf)))
    if max(err,residual)>1e-9:raise AssertionError('plaquette cache')
    S=spatial_holonomy(outer,E,path,sg,0)
    Stop=spatial_holonomy(outer,E,path,sg,2*slab)
    return {'conditional':contract_paired(S,Ts[0]@Ts[1],Stop),
            'inner_direct_mean':float(np.mean(samples)),
            'initial_direct':paired_rectangle(outer,nt,E,V,u,v,path,sg,0,slab),
            'cache_error':residual,'frozen_exact':True,'inner':inner}

def small_square(nt=15,nx=5,ny=5,beta=3.5):
    sp=square_torus(nx,ny,float(nx*ny))
    lat,cal=assemble(sp,nt,beta,1.,1.)
    return sp,lat

def identity_field(lat):
    u=np.zeros((lat['L'],4),float);u[:,0]=1.
    return u
