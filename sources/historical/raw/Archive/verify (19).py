#!/usr/bin/env python3
"""Exact integer relative-rank test and finite Gaussian determinant comparison.
All geometry from the three-step periodic quadrilateral-prism incidence file.
"""
from pathlib import Path
import numpy as np, json, math
from scipy.linalg import null_space
ROOT=Path(__file__).resolve().parent
src=Path('/mnt/data/R3_local_conditional_2026_10_27/incidence.npz')
z=np.load(src);D=z['d2'].astype(float);Qgood=z['Q'].astype(int)
Qbad=np.array([13,18,22,25,26,29,32,37],dtype=int)

def modular_rank(A,p=1000003):
    a=np.asarray(A,dtype=np.int64).copy()%p
    rr=0
    for j in range(a.shape[1]):
        hits=np.flatnonzero(a[rr:,j]);
        if hits.size==0:continue
        k=int(hits[0])+rr
        if k!=rr:a[[rr,k]]=a[[k,rr]]
        a[rr,:]=a[rr,:]*pow(int(a[rr,j]),-1,p)%p
        for i in range(rr+1,a.shape[0]):
            if a[i,j]:a[i,:]=(a[i,:]-a[i,j]*a[rr,:])%p
        rr+=1
        if rr==min(a.shape):break
    return rr

def get_forms(Q):
    L=np.flatnonzero((D[:,Q]!=0).any(axis=1)); E=np.setdiff1d(np.arange(D.shape[0]),L);R=np.setdiff1d(np.arange(D.shape[1]),Q)
    infos={}
    for name,S in [('retained',R),('inserted',np.arange(D.shape[1]))]:
        AA=D[np.ix_(L,S)].T;BB=D[np.ix_(E,S)].T
        ns=null_space(AA.T,rcond=1e-11)
        W=ns.T@BB;C=W.T@W;C=(C+C.T)/2
        eig=np.linalg.eigvalsh(C);r=int(np.sum(eig>1e-8))
        rankD=modular_rank(D[:,S]);rankLocal=modular_rank(D[np.ix_(L,S)])
        assert r==rankD-rankLocal,(name,r,rankD,rankLocal)
        infos[name]={'rank':r,'rankD':rankD,'rankLocal':rankLocal,'C':C,'eigpos':eig[eig>1e-8]}
    C0=infos['retained']['C'];C1=infos['inserted']['C'];
    delta=C1-C0;delta=(delta+delta.T)/2
    assert np.linalg.eigvalsh(delta).min()>-1e-8
    eig0,V0=np.linalg.eigh(C0);kernel=V0[:,eig0<1e-8]
    W=kernel.T@C1@kernel;v,V=np.linalg.eigh((W+W.T)/2)
    j=np.argmax(v);xi=kernel@V[:,j];
    violation={'max_exterior_energy_at_retained_zero':float(v[j]),'retained_energy':float(xi@C0@xi),'inserted_energy':float(xi@C1@xi)}
    if infos['retained']['rank']==infos['inserted']['rank']:
        H=V0[:,eig0>1e-8];s=np.sqrt(eig0[eig0>1e-8]);G=(H.T@C1@H)/s[:,None]/s[None,:];g=np.linalg.eigvalsh(G)
        assert np.linalg.norm(C1-H@H.T@C1)<1e-8
        M=float(max(g));r_eff=int(np.sum(g>1+1e-6));
    else:G=None;g=[];M=None;r_eff=None
    eta=1.
    curve={}
    for ll in (1,3,10,30,100,300,1000,10000,100000):
        # stable direct eig logdet with zeros replaced by eta
        e0=np.linalg.eigvalsh(C0);e1=np.linalg.eigvalsh(C1);
        ldet1=sum(np.log1p(ll*t/eta) for t in e1 if t>1e-8)
        ldet0=sum(np.log1p(ll*t/eta) for t in e0 if t>1e-8)
        curve[str(ll)]=float(1.5*(ldet1-ldet0))
    return {'Q':Q.tolist(),'local_links':len(L),'exterior_links':len(E),'retained_face_rank':infos['retained']['rankD'],'retained_local_rank':infos['retained']['rankLocal'],'retained_exterior_rank':infos['retained']['rank'],'inserted_face_rank':infos['inserted']['rankD'],'inserted_local_rank':infos['inserted']['rankLocal'],'inserted_exterior_rank':infos['inserted']['rank'],'new_exterior_modes':infos['inserted']['rank']-infos['retained']['rank'],'delta_rank':int(np.sum(np.linalg.eigvalsh(delta)>1e-8)),'max_generalized_eigenvalue':M,'generalized_eigenvalues':list(map(float,g)),'spectral_changed_modes':r_eff,'null_witness':violation,'regularized_gaussian_H':curve},(C0,C1,xi,L,E)

good,gm=get_forms(Qgood);bad,bm=get_forms(Qbad)
assert good['new_exterior_modes']==0 and bad['new_exterior_modes']==1
assert bad['null_witness']['retained_energy']<1e-9 and bad['null_witness']['inserted_energy']>1e-4
assert good['max_generalized_eigenvalue']<1.44
# asymptotic slope numerically
slope=(bad['regularized_gaussian_H']['100000']-bad['regularized_gaussian_H']['10000'])/np.log(10)
assert abs(slope-1.5)<0.002,slope
certificate={'geometry':'four-quadrilateral spatial disk × three-edge periodic time circle; NOT a Penrose tile extraction','good_fourteen_face_support':good,'rank_obstructed_eight_face_support':bad,'bad_asymptotic_log_slope':float(slope),'analytic_gaussian_rank_asymptotic_slope':1.5,'regularization':'Gaussian exterior reference eta=1 isotropic quadratic penalty, added as a model assumption; compact nonlinear SU2 measure not evaluated','scope':'rank and Gaussian statements only; does not establish nonlinear or arbitrary-volume bound'}
(ROOT/'certificate.json').write_text(json.dumps(certificate,indent=2))
np.savez_compressed(ROOT/'effective_forms.npz',good_C0=gm[0],good_C1=gm[1],bad_C0=bm[0],bad_C1=bm[1],bad_exterior_null_witness=bm[2],good_Q=Qgood,bad_Q=Qbad)
print(json.dumps({name:{k:x[k] for k in ['Q','local_links','exterior_links','retained_exterior_rank','inserted_exterior_rank','new_exterior_modes','max_generalized_eigenvalue','null_witness']} for name,x in [('good',good),('bad',bad)]},indent=2))
print('Gaussian high-coupling H: good',good['regularized_gaussian_H']['100000'],'bad',bad['regularized_gaussian_H']['100000'],'bad slope',slope)
