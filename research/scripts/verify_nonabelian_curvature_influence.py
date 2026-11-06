#!/usr/bin/env python3
"""Original-link finite noncommuting SU(2) cubical Wilson flow: exact amplitude influence.

Independent finite 3D quaternion experiment, not a quantum continuum simulator.
"""
import argparse,json,math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp


def qm(a,b):
    a=np.asarray(a);b=np.asarray(b)
    return np.concatenate(((a[...,0]*b[...,0]-np.sum(a[...,1:]*b[...,1:],axis=-1))[...,None],a[...,0,None]*b[...,1:]+b[...,0,None]*a[...,1:]+np.cross(a[...,1:],b[...,1:])),axis=-1)

def qi(a):
    b=np.array(a,copy=True);b[...,1:]*=-1;return b

def qe(v):
    t=np.linalg.norm(v,axis=-1)
    k=np.where(t<1e-9,.5-t*t/48,np.sin(t/2)/np.maximum(t,1e-300))
    return np.concatenate((np.cos(t/2)[...,None],k[...,None]*v),axis=-1)

def cubical(n):
    V=[(i,j,k) for i in range(n+1) for j in range(n+1) for k in range(n+1)]
    E=[(v,d) for v in V for d in range(3) if v[d]<n]; lookup={e:i for i,e in enumerate(E)}
    f=[]
    for v in V:
        for a,b in ((0,1),(0,2),(1,2)):
            if v[a]==n or v[b]==n:continue
            va=list(v);va[a]+=1;vb=list(v);vb[b]+=1
            f.append([(lookup[v,a],1),(lookup[tuple(va),b],1),(lookup[tuple(vb),a],-1),(lookup[v,b],-1)])
    ids=np.array([[e for e,s in face] for face in f],int)
    signs=np.array([[s for e,s in face] for face in f],int)
    N=np.zeros((len(f),len(f)),int)
    inv={}
    for p,ff in enumerate(f):
        for e,s in ff:inv.setdefault(e,[]).append(p)
    for s in inv.values():
        for p in s:
            for r in s:N[p,r]+=1
    assert len(E)==3*n*(n+1)**2 and len(f)==3*n*n*(n+1)
    assert np.array_equal(N.diagonal(),4*np.ones(len(f),int))
    assert int((N-np.diag(N.diagonal())).sum(axis=1).max())<=12
    return E,ids,signs,N

def face_data(q,ids,signs):
    parts=np.where((signs<0)[...,None],qi(q[ids]),q[ids]);nf=len(ids)
    ones=np.zeros((nf,4));ones[:,0]=1.
    pref=[ones]
    for i in range(4):pref.append(qm(pref[-1],parts[:,i]))
    suff=[None]*5;suff[4]=ones
    for i in range(3,-1,-1):suff[i]=qm(parts[:,i],suff[i+1])
    grad=np.empty((nf,4,3))
    for i in range(4):
        left=qm(qm(parts[:,i],suff[i+1]),pref[i]);right=qm(qm(suff[i+1],pref[i]),parts[:,i]);
        grad[:,i,:]=np.where((signs[:,i]>0)[:,None],left[:,1:],-right[:,1:])*.5
    S=1-pref[4][:,0]
    return S,grad

def derivatives(q,ids,signs):
    ell,gf=face_data(q,ids,signs)
    grad=np.zeros((len(q),3));
    for i in range(4):np.add.at(grad,ids[:,i],gf[:,i,:])
    ell_dot=-np.sum(gf*grad[ids],axis=(1,2))
    return ell,gf,grad,ell_dot

def norm_residuals(q,ids,signs,N):
    ell,gf,g,dell=derivatives(q,ids,signs)
    amp=np.sqrt(np.maximum(ell,0))
    localnorm=np.linalg.norm(gf,axis=-1)
    normbound=np.sqrt(ell[:,None]/2)
    rb=float(np.max(localnorm-normbound))
    exact_norm_residual=float(np.max(np.abs(localnorm**2-(ell*(2-ell)/4)[:,None])))
    cov=np.einsum('pij,pij->p',gf,g[ids])
    assert np.max(abs(cov+dell))<1e-10
    # local _upper_ differential inequality for amplitudes at ell>0:
    # (d/ds) sqrt ell <= (N@amp)/4. Valid with or without diagonal
    # (a slightly stronger bound subtracts the negative diagonal contribution).
    mask=amp>1e-8
    actual=dell[mask]/(2*amp[mask]); upper=(N@amp)[mask]/4
    ratio=np.max(actual-upper) if len(actual) else 0
    # exactly: |d sqrt ell / ds| <= (N@amp)/4
    absratio=np.max(np.abs(actual)-upper) if len(actual) else 0
    nonlinear_upper=(N@amp)[mask]/4 - amp[mask] - .5*amp[mask]*(2-ell[mask])
    # offdiag adjacency/4 minus the exact self-face square-gradient loss.
    sharpened_upper=((N@amp)[mask]-4*amp[mask])/4 - amp[mask]*(2-ell[mask])/2
    sharp_violation=float(np.max(actual-sharpened_upper)) if len(actual) else 0.
    return dict(max_gradient_exact_identity_error=exact_norm_residual,max_gradient_minus_upper=rb,max_diff_amp_minus_upper=float(ratio),max_abs_diff_amp_minus_upper=float(absratio),max_diff_amp_minus_sharp_upper=sharp_violation,
                max_curvature=float(np.max(ell)),max_amp_rate=float(np.max(actual)),
                n_positive=int(mask.sum()),dS_ds=float(-np.sum(g*g)))

def random_q(len_edges,scale,rng):return qe(rng.normal(0,scale,size=(len_edges,3)))

def gauge_q(q,E,n,rng):
    V=[(i,j,k) for i in range(n+1) for j in range(n+1) for k in range(n+1)];lookup={v:i for i,v in enumerate(V)}
    G=qe(rng.normal(size=(len(V),3)))
    return np.array([qm(qm(G[lookup[v]],q[e]),qi(G[lookup[tuple(vv)]])) for e,(v,d) in enumerate(E) for vv in [tuple(v[j]+(j==d) for j in range(3))]])

def main():
    a=argparse.ArgumentParser();a.add_argument('--out',type=Path,required=True);args=a.parse_args()
    rng=np.random.default_rng(361218)
    tests=[];counter=None
    for n in (2,3):
        E,ids,signs,N=cubical(n)
        for scale in (.04,.28,.8):
            for sample in range(24):
                q=random_q(len(E),scale,rng)
                res=norm_residuals(q,ids,signs,N)
                assert res['max_gradient_minus_upper']<1e-10,res
                assert res['max_gradient_exact_identity_error']<1e-10,res
                assert res['max_abs_diff_amp_minus_upper']<1e-10,res
                assert res['max_diff_amp_minus_sharp_upper']<1e-10,res
                # gauge covariance: face trace stable under arbitrary vertex rotations.
                if sample==0:
                    # Verify every original-link cross-face Cauchy-Schwarz identity.
                    edge_to_face={}
                    for p,ee in enumerate(ids):
                        for k,e in enumerate(ee):edge_to_face.setdefault(int(e),[]).append((p,k))
                    max_cross_violation=0.
                    for neighbors in edge_to_face.values():
                        for i,(p,k) in enumerate(neighbors):
                            for r,l in neighbors[i+1:]:
                                prod=abs(np.dot(face_data(q,ids,signs)[1][p,k],face_data(q,ids,signs)[1][r,l]))
                                err=prod-(.5*np.sqrt(max(0.,face_data(q,ids,signs)[0][p]*face_data(q,ids,signs)[0][r])))
                                max_cross_violation=max(max_cross_violation,err)
                    assert max_cross_violation<1e-10
                    res['max_cross_gamma_violation']=max_cross_violation
                    q2=gauge_q(q,E,n,rng)
                    x=face_data(q,ids,signs)[0];y=face_data(q2,ids,signs)[0]
                    res['gauge_action_error']=float(np.max(np.abs(x-y)))
                    assert res['gauge_action_error']<1e-12
                if sample==0 or sample==23:tests.append(dict(n=n,scale=scale,sample=sample,**res))
                # strict increase of a maximal plaquette amplitude means a naive max principle fails.
                ell,_,_,dell=derivatives(q,ids,signs)
                imax=int(np.argmax(ell))
                if counter is None and dell[imax]>1e-8:
                    second=float(np.partition(ell,-2)[-2])
                    counter=dict(n=n,scale=scale,sample=sample,max_face=imax,max_ell=float(ell[imax]),second_largest_ell=second,strict_max_margin=float(ell[imax]-second),max_ell_derivative=float(dell[imax]),total_action_derivative=float(-np.sum(derivatives(q,ids,signs)[2]**2)),random_seed=361218)
                    counter['q_vectors']=q.tolist()
                    cross=np.cross(q[0,1:],q[1,1:])
                    counter['noncommuting_link_cross_norm']=float(np.linalg.norm(cross))
                    assert counter['strict_max_margin']>0 and counter['noncommuting_link_cross_norm']>1e-8 and counter['total_action_derivative']<0
    # Gauge-covariant full nonlinear ODE integration checks one true noncommuting sample.
    flow=[]
    for n in (2,3):
        E,ids,signs,N=cubical(n);q0=random_q(len(E),.32,rng);h=1/n;tau=.02
        def rhs(s,y):
            q=y.reshape(-1,4);ell,_,grad,_=derivatives(q,ids,signs)
            return qm(np.column_stack((np.zeros(len(E)),-.5*grad)),q).ravel()
        sol=solve_ivp(rhs,(0,tau/h**2),q0.ravel(),rtol=2e-10,atol=5e-12,method='DOP853')
        assert sol.success
        final=sol.y[:,-1].reshape(-1,4)
        e0,_,g0,_=derivatives(q0,ids,signs);ef,_,gf,_=derivatives(final,ids,signs)
        assert ef.sum()<=e0.sum()+1e-10
        assert np.max(abs(np.linalg.norm(final,axis=1)-1))<1e-9
        flow.append(dict(n=n,tau=tau,initial_total_action=float(e0.sum()),final_total_action=float(ef.sum()),
                         initial_max_face_defect=float(e0.max()),final_max_face_defect=float(ef.max()),
                         max_link_norm_error=float(np.max(abs(np.linalg.norm(final,axis=1)-1)))))
    out=dict(status='PASS',scope='Exact noncommuting finite 3D SU2 Wilson link gradient-flow local defect influence bound; not h-uniform positive-physical-time smoothing',
             tests=tests,flows=flow,maximum_counterexample=counter,random_noncommuting_checks=144,
             theorem={'edge_gradient':'|grad_e ell_p|² = ell_p(2-ell_p)/4 <= ell_p/2',
                      'amplitude':'a_p=sqrt(ell_p), D^+_s a_p <= (1/4) sum_q N_pq a_q, N_pq=# shared original links',
                      'sharp_local_amplitude':'D^+_s a_p <= (1/4) sum_{q ne p} N_pq a_q - a_p(2-ell_p)/2',
                      'matrix_comparison':'a(s) <= exp(s N_off/4) a(0) elementwise; N_off=N-4I, max_p a_p(s) <= exp(3s) max_p a_p(0)',
                      'finite_graph_influence':'If support of a(0) is graph distance d away from p, a_p(s) <= ||a0||infty exp(3s)(3s)^d/d!',
                      'physical_time':'s=tau/h² yields exp(3 tau/h²), NOT uniform in h',
                      'nonabelian_scope':'applies to all finite SU2 link configurations, with no commuting or near-flat assumption'},
             remaining=['No non-Abelian mesh-independent positive-flow-time curvature smoothing from this comparison',
                        'Need covariant cancellations and noncommutative Bianchi rather than absolute-value path majorants',
                        'Actual interacting vacuum covariance and physical Schur/OS/mass-gap remain open'])
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',cases=len(tests),flows=flow,counterexample=counter is not None,
        max_grad_violation=max(t['max_gradient_minus_upper'] for t in tests),
        max_amp_bound_violation=max(t['max_abs_diff_amp_minus_upper'] for t in tests),
        max_sharp_bound_violation=max(t['max_diff_amp_minus_sharp_upper'] for t in tests)),indent=2))
if __name__=='__main__':main()
