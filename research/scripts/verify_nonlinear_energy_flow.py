#!/usr/bin/env python3
"""Independent exact finite SU(2) nonlinear spatial Wilson-flow energy audit.

This tests a classical finite gauge-field ODE. It does NOT sample the quantum
interacting Yang--Mills vacuum or construct a continuum mass gap.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp


def qmul(a, b):
    a=np.asarray(a);b=np.asarray(b)
    return np.concatenate([(a[...,0]*b[...,0]-np.sum(a[...,1:]*b[...,1:],axis=-1))[...,None],
                           a[...,0,None]*b[...,1:]+b[...,0,None]*a[...,1:]+np.cross(a[...,1:],b[...,1:])],axis=-1)

def qinv(a):
    r=np.array(a,copy=True);r[...,1:]*=-1;return r

def qexp(a):
    a=np.asarray(a); theta=np.linalg.norm(a,axis=-1);half=theta/2
    sn=np.where(theta<1e-10,0.5-theta**2/48+theta**4/3840,np.sin(half)/np.maximum(theta,1e-300))
    return np.concatenate([np.cos(half)[...,None],sn[...,None]*a],axis=-1)

def unit(a):return a/np.linalg.norm(a,axis=-1,keepdims=True)

def cubical(n):
    v=[(i,j,k) for i in range(n+1) for j in range(n+1) for k in range(n+1)]
    edges=[(x,d) for x in v for d in range(3) if x[d]<n]
    idx={e:i for i,e in enumerate(edges)}
    faces=[]
    face_centers=[]
    for x in v:
        for a,b in [(0,1),(0,2),(1,2)]:
            if x[a]==n or x[b]==n:continue
            y=list(x);y[a]+=1
            z=list(x);z[b]+=1
            faces.append([(idx[x,a],1),(idx[tuple(y),b],1),
                          (idx[tuple(z),a],-1),(idx[x,b],-1)])
            center=np.array(x,dtype=float);center[a]+=0.5;center[b]+=0.5
            face_centers.append(center/n)
    ids=np.array([[e for e,s in f] for f in faces],dtype=int)
    signs=np.array([[s for e,s in f] for f in faces],dtype=int)
    deg=np.bincount(ids.ravel(),minlength=len(edges))
    assert len(v)==(n+1)**3 and len(edges)==3*n*(n+1)**2
    assert len(faces)==3*n*n*(n+1) and deg.max()<=4
    return {'n':n,'h':1/n,'verts':v,'edges':edges,'ids':ids,'signs':signs,'degree':deg,'face_centers':np.array(face_centers)}

def quats_and_parts(q, geom):
    ids,sgn=geom['ids'],geom['signs']
    parts=np.where((sgn<0)[...,None],qinv(q[ids]),q[ids])
    pref=[np.broadcast_to(np.array([1.,0.,0.,0.]),(len(ids),4)).copy()]
    for i in range(4):pref.append(qmul(pref[-1],parts[:,i,:]))
    suff=[None]*5;suff[4]=pref[0]
    for i in range(3,-1,-1):suff[i]=qmul(parts[:,i,:],suff[i+1])
    return parts,pref,suff

def action_gradient(q, geom):
    parts,pref,suff=quats_and_parts(q,geom)
    P=pref[4];defects=1-P[:,0]
    grad=np.zeros((len(q),3),dtype=float)
    for k in range(4):
        # Left Lie derivative of 1-Re(product) along exp(t i sigma/2) on link k.
        cyc=qmul(qmul(parts[:,k,:],suff[k+1]),pref[k])
        alt=qmul(qmul(suff[k+1],pref[k]),parts[:,k,:])
        # Both cyc and alt have the same SU(2) real/imaginary trace cyclic value
        # for + links we need U_k * suffix * prefix, for - links suffix * prefix * U_k^{-1}.
        piece=np.where((geom['signs'][:,k]>0)[:,None],cyc[:,1:],-alt[:,1:])*0.5
        np.add.at(grad,geom['ids'][:,k],piece)
    return float(defects.sum()),grad,defects

def smooth_links(geom):
    h=geom['h']; a=[]
    for (i,j,k),d in geom['edges']:
        x=(i+0.5*(d==0))*h;y=(j+0.5*(d==1))*h;z=(k+0.5*(d==2))*h
        if d==0: val=[0.22*math.sin(2*math.pi*y),0.,0.13*math.cos(2*math.pi*z)]
        elif d==1:val=[0.,0.15*math.sin(2*math.pi*x),0.]
        else:val=[0.17*math.cos(2*math.pi*x),0.,0.12*math.sin(2*math.pi*y)]
        a.append(h*np.array(val))
    return qexp(np.array(a))

def gauge_transformation(q,geom,rng):
    gg=unit(rng.normal(size=(len(geom['verts']),4)));vi={v:i for i,v in enumerate(geom['verts'])}
    sources=[];targets=[]
    for v,d in geom['edges']:
        w=list(v);w[d]+=1
        sources.append(vi[v]);targets.append(vi[tuple(w)])
    return qmul(qmul(gg[sources],q),qinv(gg[targets])),gg,np.array(sources),np.array(targets)

def ode_rhs(t,y,geom):
    q=y.reshape(-1,4)
    _,grad,_=action_gradient(q,geom)
    v=np.column_stack([np.zeros(len(q)),-0.5*grad])
    return qmul(v,q).ravel()

def local_force_test(n=2,seed=1709):
    geom=cubical(n); rng=np.random.default_rng(seed)
    q0=unit(rng.normal(size=(len(geom['edges']),4)))
    s,g,_=action_gradient(q0,geom)
    h=geom['h'];u=0.8
    # Direct scalar derivatives for one coordinate in SU(2) Lie units
    delta=2.e-6
    targets=[]
    for e,j in [(0,0),(1,2),(min(5,len(q0)-1),1)]:
        v=np.zeros((len(q0),3));v[e,j]=1.
        qp=qmul(qexp(delta*v),q0);qm=qmul(qexp(-delta*v),q0)
        sp=action_gradient(qp,geom)[0];sm=action_gradient(qm,geom)[0]
        targets.append(abs((sp-sm)/(2*delta)-g[e,j]))
    qt,gg,sources,dests=gauge_transformation(q0,geom,rng)
    st,gt,_=action_gradient(qt,geom)
    gquat=np.column_stack([np.zeros(len(g)),g]); expected=qmul(qmul(gg[sources],gquat),qinv(gg[sources]))[:,1:]
    return dict(gradient_errors=targets,action_gauge_error=abs(st-s),gradient_gauge_error=float(np.linalg.norm(gt-expected,axis=1).max()),
                action=s,force_square=float((g*g).sum()),force_upper=8*s,max_degree=int(max(geom['degree'])))

def integrate_flow(n,tau=0.015):
    geom=cubical(n);q0=smooth_links(geom);h=geom['h'];init,_,_=action_gradient(q0,geom)
    # Record exact energy identity by simultaneously integrating physical dissipation.
    # Solve dimensionless time s=tau/h². J'(s)=8||grad S||²/h.
    def rhs(s,z):
        q=z[:-1].reshape(-1,4)
        a,g,_=action_gradient(q,geom)
        dy=ode_rhs(s,z[:-1],geom)
        return np.r_[dy,(8/h)*float(np.sum(g*g))]
    s_end=tau/h**2
    y0=np.r_[q0.ravel(),0.]
    res=solve_ivp(rhs,(0,s_end),y0,method='DOP853',rtol=5.e-10,atol=3.e-11,max_step=min(0.04,s_end/4))
    if not res.success:raise RuntimeError(res.message)
    qf=res.y[:-1,-1].reshape(-1,4);sf,grad,defects=action_gradient(qf,geom)
    E0=8*init/h;Ef=8*sf/h;D=res.y[-1,-1]
    return {'n':n,'h':h,'s_lattice':s_end,'tau_physical':tau,'E_initial':E0,'E_final':Ef,
            'integrated_physical_dissipation':float(D),'identity_error':abs(E0-Ef-D),
            'initial_S':init,'final_S':sf,'max_plaquette_defect':float(defects.max()),
            'max_plaquette_bound':E0*h/8,'max_quaternion_norm_error':float(np.max(np.abs(np.linalg.norm(qf,axis=1)-1))),
            'evaluations':res.nfev,'force_upper_pointwise':8*sf,'force_squared_final':float((grad*grad).sum())}

def smooth_energy(n):
    g=cubical(n);q=smooth_links(g);S,_,ds=action_gradient(q,g)
    return {'n':n,'h':1/n,'E':8*n*S,'S':S,'face_defect_max':float(np.max(ds)),'F':len(ds)}

def isolated_link_defect(n):
    geom=cubical(n);q=np.tile([1.,0.,0.,0.],(len(geom['edges']),1))
    # Interior link at midpoint in physical cube, always available for n >= 3.
    center=tuple([n//2]*3)
    e=next(i for i,(v,d) in enumerate(geom['edges']) if v==center and d==0)
    h=geom['h'];angle=math.sqrt(h)
    q[e]=qexp(np.array([0,0,angle]))
    S,grad,ds=action_gradient(q,geom);deg=int(geom['degree'][e])
    expected=deg*(1-math.cos(angle/2))
    masses=(8/h)*ds
    centroid=np.einsum("p,pj->j",masses,geom["face_centers"])/max(np.sum(masses),1e-100)
    atom_sq_radius=float(np.dot(masses,np.sum((geom["face_centers"]-0.5)**2,axis=1)))
    return dict(n=n,h=h,edge_index=e,degree=deg,action=S,analytic_action=expected,E_physical=8*S/h,
                max_plaquette_defect=float(ds.max()),max_curvature_angle_per_h2=angle/h**2,
                scaled_angle_h_three_halves=angle*h**1.5/h**2,physical_action_upper=deg,
                energy_measure_centroid=centroid.tolist(),energy_measure_atom_squared_radius=atom_sq_radius,
                force_bound_holds=float((grad*grad).sum())<=8*S+1e-12)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    grad=local_force_test();assert max(grad['gradient_errors'])<3.e-8,grad
    assert grad['gradient_gauge_error']<1.e-12,grad
    assert grad['action_gauge_error']<1.e-12,grad
    assert grad['force_square']<=grad['force_upper']+1.e-10
    smooth=[smooth_energy(n) for n in (2,3,4,5,6,8,10)]
    flows=[integrate_flow(n) for n in (2,3,4)]
    for f in flows:
        assert f['identity_error']<2e-7,f
        assert f['E_final']<=f['E_initial']+2e-9
        assert f['max_plaquette_defect']<=f['max_plaquette_bound']+1e-10
        assert f['force_squared_final']<=f['force_upper_pointwise']+1e-8
        assert f['max_quaternion_norm_error']<1e-7
    defects=[isolated_link_defect(n) for n in (3,4,6,8,12)]
    for d in defects:
        assert abs(d['action']-d['analytic_action'])<1e-10,d
        assert d['E_physical']<=d['physical_action_upper']+1e-10,d
        assert abs(d['scaled_angle_h_three_halves']-1)<1e-14
        assert d['energy_measure_atom_squared_radius']<2*d['h']**2*d['E_physical']
    output={'status':'PASS','scope':'Classical nonlinear 3D cubic SU(2) gradient flow with physical time scaling; no quantum interacting-vacuum claim',
            'conventions':{'S':'sum_p [1-Re holonomy quaternion]','physical_energy':'8 S / h',
                'flow':'dU/ds=-grad S; tau=h²s','physical_dissipation':'d E/d tau= -8/h³ sum_e |grad_e S|²'},
            'gradient_covariance':grad,'smooth_sample_energy':smooth,'nonlinear_flow_integral':flows,'concentrated_defect':defects,
            'scientific_gates':{g:'OPEN' for g in ['P0','P1','P2','P3','P4','P5','T0','T1','T2','T3','T4','T5','4D_YM_gap','quantum_gravity_UV']},
            'limits':['Finite nonlinear gauge flow and energy balance; does not bound positive-time interacting quantum correlations',
              'E(0) uniform requires smooth/admissible classical initial configurations, not proved for Wilson vacuum',
              'Energy and integrated force alone do not imply instantaneous h-uniform curvature derivatives or a 4D continuum',
              'Concentrated one-link defects with E=O(1) have physical curvature angles/h²~h^-3/2',
              'Nonvanishing true-vacuum flowed Wilson covariance, Schur comparison, OS and gap remain open']}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'status':'PASS','max_flow_energy_identity_error':max(x['identity_error'] for x in flows),
                      'max_gradient_fd_error':max(grad['gradient_errors']),
                      'max_gauge_gradient_error':grad['gradient_gauge_error'],
                      'smooth_energy_last':smooth[-1]['E'],'max_defect_ratio':max(d['max_curvature_angle_per_h2'] for d in defects)},indent=2))
if __name__=='__main__':main()
