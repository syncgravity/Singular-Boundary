#!/usr/bin/env python3
"""Finite SU(2) P0 heat-kernel/temporal gauge action regression.
Scientific scope: exact finite-model identities only. No continuum limit or gap.
"""
import json
import math
from pathlib import Path
import numpy as np
from scipy.special import roots_jacobi, eval_chebyu

rng=np.random.default_rng(20261104)

def haar(n=1):
    q=rng.normal(size=(n,4))
    return q/np.linalg.norm(q,axis=1)[:,None]

def mul(a,b):
    a=np.asarray(a);b=np.asarray(b)
    a0,aa=a[...,0],a[...,1:]
    b0,bb=b[...,0],b[...,1:]
    return np.concatenate([((a0*b0)-(aa*bb).sum(axis=-1))[...,None],
                           a0[...,None]*bb+b0[...,None]*aa+np.cross(aa,bb)],axis=-1)

def inv(a):
    t=np.array(a,copy=True);t[...,1:]*=-1;return t

def kh(t,cos_theta,nmax=64):
    """SU(2) central heat kernel with Haar normalized to 1 and Casimir j(j+1)."""
    x=np.clip(cos_theta,-1,1)
    val=np.zeros_like(x,dtype=float)
    for n in range(nmax+1):
        c=n*(n+2)/4
        val+=(n+1)*np.exp(-t*c)*eval_chebyu(n,x)
    return val

def cube(n):
    vertices=list(np.ndindex(n+1,n+1,n+1));idx={v:i for i,v in enumerate(vertices)}
    edges=[];dic={}
    for v in vertices:
        for a in range(3):
            if v[a]<n:
                w=list(v);w[a]+=1;w=tuple(w)
                dic[v,a]=len(edges);edges.append((idx[v],idx[w]))
    faces=[]
    for v in vertices:
        for a,b in ((0,1),(1,2),(2,0)):
            if v[a]>=n or v[b]>=n:continue
            va=list(v);va[a]+=1;va=tuple(va)
            vb=list(v);vb[b]+=1;vb=tuple(vb)
            faces.append([(dic[v,a],+1),(dic[va,b],+1),(dic[vb,a],-1),(dic[v,b],-1)])
    return edges,faces

def gauge_links(U,edges,h):
    return np.array([mul(mul(h[s],u),inv(h[t])) for (s,t),u in zip(edges,U)])

def face_holonomy(U,word):
    z=np.array([1.,0.,0.,0.]);
    for i,sgn in word:z=mul(z,U[i] if sgn>0 else inv(U[i]))
    return z

def temporal_factors(U0,U1,edges,g):
    # k_t(U1_e [g_source U0_e g_target^-1]^-1)
    return np.array([mul(u1,inv(mul(mul(g[s],u0),inv(g[t])))) for (s,t),u0,u1 in zip(edges,U0,U1)])

def finite_gauge_check(n,trials=15):
    edges,faces=cube(n);NV=max(max(a,b) for a,b in edges)+1
    max_spatial=0;max_temporal=0;min_k=float('inf')
    t_heat=0.6
    for _ in range(trials):
        U0=haar(len(edges));U1=haar(len(edges));g=haar(NV)
        h0=haar(NV);h1=haar(NV)
        U0g=gauge_links(U0,edges,h0);U1g=gauge_links(U1,edges,h1)
        gg=np.array([mul(mul(b,gv),inv(a)) for a,b,gv in zip(h0,h1,g)])
        b0=np.array([face_holonomy(U0,f)[0] for f in faces])
        b1=np.array([face_holonomy(U0g,f)[0] for f in faces])
        max_spatial=max(max_spatial,float(np.max(np.abs(b0-b1))))
        x=np.array([q[0] for q in temporal_factors(U0,U1,edges,g)])
        xg=np.array([q[0] for q in temporal_factors(U0g,U1g,edges,gg)])
        max_temporal=max(max_temporal,float(np.max(np.abs(x-xg))))
        min_k=min(min_k,float(np.min(kh(t_heat,x))))
        assert np.min(kh(t_heat,x))>0
    assert max_spatial<2e-13,(n,max_spatial)
    assert max_temporal<2e-13,(n,max_temporal)
    return dict(n=n,vertices=NV,edges=len(edges),faces=len(faces),trials=trials,max_spatial_residual=max_spatial,max_temporal_residual=max_temporal,min_sampled_heat_kernel=min_k)

def character_fourier_check():
    # normalized Haar radial: (2/pi)*sqrt(1-x^2) dx; Jacobi alpha=beta=.5
    xs,weights=roots_jacobi(120,.5,.5)
    rows=[];worst=0
    for t in (.35,.7,1.1):
        k=kh(t,xs,64)
        assert np.min(k)>0,(t,np.min(k))
        z=(2/math.pi)*np.dot(weights,k)
        assert abs(z-1)<2e-12
        for n in range(0,11):
            moment=(2/math.pi)*np.dot(weights,k*eval_chebyu(n,xs))/(n+1)
            desired=math.exp(-t*n*(n+2)/4)
            err=abs(moment-desired)
            worst=max(worst,err)
            assert err < 2e-12,(t,n,moment,desired)
        rows.append(dict(heat_time=t,haar_integral=z,min_radial_density=float(np.min(k)),max_character_eigenvalue_error=max(abs((2/math.pi)*np.dot(weights,k*eval_chebyu(n,xs))/(n+1)-math.exp(-t*n*(n+2)/4)) for n in range(11))))
    # Convolution semigroup is exact from the Peter-Weyl diagonal identity.
    return dict(checks=rows,worst_absolute_eigenvalue_error=worst)

def loop_scaling_witness():
    # 4 fine links vs 8 after dyadic split: each fundamental spin has Casimir 3/4.
    coarse=4*3/4;fine=8*3/4
    assert coarse==3 and fine==6
    # exact kinetic match only if alpha_h = 2 alpha_(h/2)
    return dict(coarse_casimir=coarse,refined_casimir=fine,required_alpha_ratio=2,requires_g2_half_equals_g2_quarter=True)

if __name__=='__main__':
    out={'scope':'Finite SU2 heat-kernel and gauge action. Not a continuum YM theorem.',
         'gauge_checks':[finite_gauge_check(n) for n in (1,2)],
         'heat_fourier':character_fourier_check(),
         'holonomy_refinement_obstruction':loop_scaling_witness(),
         'analytic_justification':'Peter-Weyl spectrum c_j=j(j+1), positive Haar heat kernel, central gauge covariance and symmetric Trotter convergence at fixed graph.'}
    Path(__file__).with_name('verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
