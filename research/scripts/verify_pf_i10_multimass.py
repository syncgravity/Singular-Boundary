#!/usr/bin/env python3
"""PF-I10 multi-mass source-weighted finite-spectral verification.

Stochastic Lanczos quadrature (SLQ) with exact-trace control variates. Supports
full/positive mode means, four Paper4 reference masses, and same-graph uniform
hopping factor. The user-source script is SHA-pinned, private, and not copied.
"""
from __future__ import annotations
import argparse,json,math,time
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.linalg import eigh_tridiagonal
from verify_pf_i10_source_spectral import (source_import,build_sparse,periodic_sparse,
                                         SOURCE_SHA,TAVG)
MASSES=(1e-4,1e-2,1.0,100.0)

def same_graph_uniform(L):
    A=L.copy().tocsr();A.setdiag(0);A.eliminate_zeros()
    A.data[:]=-TAVG
    degree=-np.asarray(A.sum(axis=1)).ravel()
    return sparse.diags(degree)+A

def lanczos_eig_weight(L,v,steps):
    n=L.shape[0]
    q=v.astype(float,copy=True);q/=np.linalg.norm(q)
    old=np.zeros(n);b=0.;aa=[];bb=[]
    for k in range(steps):
        r=L@q
        if k:r-=b*old
        a=float(q@r);r-=a*q
        nb=float(np.linalg.norm(r));aa.append(a)
        if nb<=1e-13:break
        if k<steps-1:bb.append(nb)
        old=q;q=r/nb;b=nb
    ev,vec=eigh_tridiagonal(np.asarray(aa),np.asarray(bb),check_finite=False)
    if ev.min() < -1e-7:raise ArithmeticError('Laplacian unexpectedly non-PSD')
    ev=np.maximum(0.,ev)
    w=vec[0,:]**2
    w/=w.sum()
    return ev,w

def slq_mass(L,seed,steps,probes,masses=MASSES):
    n=L.shape[0];rng=np.random.default_rng(seed)
    mu=float(L.diagonal().sum())/n
    records={str(m2):{k:[] for k in ['sqrt','log','relative_log']} for m2 in masses}
    moments=[];start=time.monotonic()
    for _ in range(probes):
        z=rng.choice(np.array([-1.,1.]),size=n)
        sample_mu=float(z@(L@z))/n
        ev,w=lanczos_eig_weight(L,z,steps)
        moments.append(sample_mu)
        for m2 in masses:
            b=str(m2);shift=ev+m2
            for f in records[b]:
                if f=='sqrt':v=np.sqrt(shift)
                elif f=='log':v=np.log(shift)
                else:v=np.log1p(ev/m2)
                raw=float(w@v)
                if f=='sqrt':slope=1/(2*math.sqrt(mu+m2))
                else:slope=1/(mu+m2)
                records[b][f].append((raw,raw-slope*(sample_mu-mu)))
    out={}
    for m2,props in records.items():
        out[m2]={}
        for f,samples in props.items():
            sam=np.array(samples)
            out[m2][f]={'raw':{'mean':float(sam[:,0].mean()),'se':float(sam[:,0].std(ddof=1)/math.sqrt(probes))},
                        'trace_control':{'mean':float(sam[:,1].mean()),'se':float(sam[:,1].std(ddof=1)/math.sqrt(probes))}}
    return {'masses':out,'probes':probes,'steps':steps,'seed':seed,
            'exact_first_moment':mu,'hutch_first_moment':float(np.mean(moments)),
            'elapsed_sec':time.monotonic()-start,
            'quadrature_truncation_error_certified':False,
            'probe_SE_is_random_sampling_uncertainty_only':True}

def ratios(a,b,qa,pa,masses=MASSES):
    nc,pc=a['n'],b['n'];cq,cp=a['components'],b['components']
    ans={}
    for m2 in masses:
        key=str(m2);ans[key]={}
        for f in ['sqrt','log','relative_log']:
            zer={'sqrt':math.sqrt(m2),'log':math.log(m2),'relative_log':0.}[f]
            c={}
            for mode in ['raw','trace_control']:
                ma=qa['masses'][key][f][mode];mb=pa['masses'][key][f][mode]
                fa,fb=ma['mean'],mb['mean'];ea,eb=ma['se'],mb['se']
                va=(nc*fa-cq*zer)/(nc-cq);vb=(pc*fb-cp*zer)/(pc-cp)
                c[mode]={'full':fa/fb,'positive':va/vb,
                    'positive_SE_independent':abs(va/vb)*math.hypot((nc*ea/(nc-cq))/va,(pc*eb/(pc-cp))/vb)}
            ans[key][f]=c
    return ans

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-script',type=Path,required=True)
    ap.add_argument('--cache',type=Path,required=True)
    ap.add_argument('--ngrids',nargs='+',type=int,default=[7,10,12,15,18,20,23,25])
    ap.add_argument('--probes',type=int,default=256)
    ap.add_argument('--steps',type=int,default=180)
    ap.add_argument('--seed',type=int,default=112609)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();source=source_import(args.source_script)
    rows=[]
    for ngrid in args.ngrids:
        p=args.cache/f'PF_I10_source_{ngrid}.npz'
        if p.exists():
            r=np.load(p,allow_pickle=False)
            L=sparse.csr_matrix((r['data'],r['indices'],r['indptr']),shape=tuple(r['shape']))
            qc=json.loads(str(r['meta'].item()))
            if qc['source_sha256']!=SOURCE_SHA:raise ValueError('bad cache source')
        else:
            L,qc,_=build_sparse(source,ngrid)
        P,per=periodic_sparse(qc['n'])
        U=same_graph_uniform(L)
        uniform={'n':qc['n'],'components':qc['components'],
                 'trace_over_n':float(U.diagonal().mean()),'same_qc_basis_edges':True}
        source_spectrum=slq_mass(L,args.seed+ngrid*100,args.steps,args.probes)
        per_spectrum=slq_mass(P,args.seed+ngrid*100+1,args.steps,args.probes)
        uniform_spectrum=slq_mass(U,args.seed+ngrid*100,args.steps,args.probes)
        total=ratios(qc,per,source_spectrum,per_spectrum)
        fib_uni=ratios(qc,uniform,source_spectrum,uniform_spectrum)
        uni_per=ratios(uniform,per,uniform_spectrum,per_spectrum)
        # Factorization of POINT ESTIMATES, though independent probes for
        # periodic and QC; the uniform QC uses the same probes and graph size.
        for m in [str(x) for x in MASSES]:
            for f in ['sqrt','log','relative_log']:
                for flavor in ['full','positive']:
                    for mode in ['raw','trace_control']:
                        prod=fib_uni[m][f][mode][flavor]*uni_per[m][f][mode][flavor]
                        assert abs(prod-total[m][f][mode][flavor])<1e-9
        row={'Ngrid':ngrid,'QC':qc,'periodic':per,'uniform_same_graph':uniform,
             'ratios':total,'fib_over_same_graph_uniform':fib_uni,
             'same_graph_uniform_over_periodic':uni_per,
             'source_slq':source_spectrum,'periodic_slq':per_spectrum,'uniform_slq':uniform_spectrum}
        rows.append(row)
        # checkpoint after every row; discard timing/CPU from reproducible evidence
        args.output.write_text(json.dumps({'status':'source-faithful finite scalar spectral SLQ, no YM gap',
            'source_sha256':SOURCE_SHA,'steps':args.steps,'probes':args.probes,
            'seed':args.seed,'rows':rows},indent=2,sort_keys=True)+'\n')
        print(json.dumps({'ngrid':ngrid,'n':qc['n'],
            'sqrt':total['0.0001']['sqrt']['trace_control']['positive'],
            'sqrt_se':total['0.0001']['sqrt']['trace_control']['positive_SE_independent'],
            'zeta_prime_ratio':total['0.0001']['log']['trace_control']['positive'],
            'mass_flow':[total[str(m)]['relative_log']['trace_control']['positive'] for m in MASSES]}),flush=True)
if __name__=='__main__':main()
