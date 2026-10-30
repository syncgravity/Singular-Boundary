"""Stage 16 SU(2) exact temporal-link multihit (conditional mean and heatbath).

For S=sum_p beta_p(1 - 1/2 ReTr U_p), a single oriented link is a unit
quaternion q on S^3 with conditional density exp(q.h), where h_i is obtained
from four independent trial quaternions. The exact local first moment is
E[q|others] = I_2(|h|)/I_1(|h|) * h/|h|.

The Wilson rectangle is multilinear in links on a fixed source temporal line,
and no plaquette contains two temporal links at different time slices at the
same spatial vertex. Thus integrating ALL source-line links exactly is valid,
with each measurement conditioned on all other links. No inner MCMC mixing is
required for those links. Multiple source sites should not be regarded as
jointly integrated unless their supports are independent.
"""
from pathlib import Path
import sys
import numpy as np
from scipy.special import ive
from scipy.stats import vonmises_fisher
from numba import njit
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'ym_stage13'))
from stage13_transport import mat,small_square
from wilson_torus import face_trace_scalar,mul

@njit
def _field(links,fi,sg,beta,adj,degree,eid):
    h=np.zeros(4,np.float64)
    trial=np.zeros(4,np.float64)
    for i in range(4):
        trial[i]=1.
        total=0.
        for j in range(degree[eid]):
            f=adj[eid,j]
            total+=beta[f]*face_trace_scalar(f,links,fi,sg,eid,trial)
        h[i]=total
        trial[i]=0.
    return h

def exact_su2_mean(h):
    h=np.asarray(h,float);k=float(np.linalg.norm(h))
    if k<1e-9:return h/4.  # leading small-k expansion
    return h*(ive(2,k)/ive(1,k))/k

def exact_su2_heatbath(h,rng):
    """Draw from the *exact* one-link conditional Haar-weighted density."""
    h=np.asarray(h,float);k=float(np.linalg.norm(h))
    if k<1e-12:
        q=rng.normal(size=4);return q/np.linalg.norm(q)
    return np.asarray(vonmises_fisher.rvs(h/k,k,random_state=rng)).reshape(4)

@njit
def _direct_batched(links,E,V,nt,idx,sign,lens,sources,targets,t0,lag,means,selected):
    """Wilson rectangles in SU(2) quaternion basis, with cached temporal lines.

    means is a V x lag x 4 array; only source sites with selected[v] true
    replace the source temporal q by its exact conditional expectation.
    """
    n=len(lens);D=np.empty(n,np.float64);M=np.empty(n,np.float64)
    temporal=np.empty((V,4),np.float64)
    source_multi=np.empty((V,4),np.float64)
    for v in range(V):
        T=np.array([1.,0.,0.,0.]);H=T.copy()
        for step in range(lag):
            tt=(t0+step)%nt
            T=mul(T,links[nt*E+tt*V+v])
            if selected[v]:
                H=mul(H,means[v,step])
            else:
                H=mul(H,links[nt*E+tt*V+v])
        temporal[v]=T;source_multi[v]=H
    for i in range(n):
        s0=np.array([1.,0.,0.,0.]);s1=s0.copy()
        for j in range(lens[i]):
            e=idx[i,j]
            q0=links[t0*E+e];q1=links[((t0+lag)%nt)*E+e]
            if sign[i,j]==-1:
                q0=np.array([q0[0],-q0[1],-q0[2],-q0[3]])
                q1=np.array([q1[0],-q1[1],-q1[2],-q1[3]])
            s0=mul(s0,q0);s1=mul(s1,q1)
        s1=np.array([s1[0],-s1[1],-s1[2],-s1[3]])
        A=temporal[sources[i]];Am=source_multi[sources[i]]
        Ad=np.array([A[0],-A[1],-A[2],-A[3]])
        Adm=np.array([Am[0],-Am[1],-Am[2],-Am[3]])
        pre=mul(mul(s0,temporal[targets[i]]),s1)
        D[i]=mul(pre,Ad)[0];M[i]=mul(pre,Adm)[0]
    return D,M

def catalog_square(sp,nanchors=16,lengths=(1,2,3,4)):
    """Many physical-length-controlled x/y paths, including periodic seams."""
    E,V=sp['E'],sp['V']; edges=np.asarray(sp['edges']);dv=np.asarray(sp['edge_vectors'])
    # Root anchors sampled deterministically across the torus; for 8x8,
    # sampled indices 0,4,8,... provide both axes and sublattice coverage.
    roots=np.unique(np.linspace(0,V-1,nanchors,dtype=int))
    table={}
    for e,(a,b) in enumerate(edges):
        table.setdefault(int(a),[]).append((e,+1,int(b),dv[e]))
        table.setdefault(int(b),[]).append((e,-1,int(a),-dv[e]))
    items=[]
    for origin in roots:
        for axis in (0,1):
            cur=int(origin);ids=[];sg=[];disp=np.zeros(2)
            for length in range(1,max(lengths)+1):
                opts=[v for v in table[cur] if np.allclose(v[3],np.eye(2)[axis],atol=1e-8)]
                if len(opts)!=1:raise ValueError(f'no unique straight edge at {cur} along {axis}: {opts}')
                e,s,nxt,step=opts[0];ids.append(e);sg.append(s);cur=nxt;disp=disp+step
                if length in lengths:
                    items.append((list(ids),list(sg),int(origin),cur,disp.copy()))
    maxlen=max(map(lambda z:len(z[0]),items))
    idx=np.full((len(items),maxlen),-1,np.int64);sign=np.zeros_like(idx);lens=[];src=[];dst=[];dx=[]
    for i,(ii,ss,u,v,d) in enumerate(items):
        idx[i,:len(ii)]=ii;sign[i,:len(ss)]=ss;lens.append(len(ii));src.append(u);dst.append(v);dx.append(d)
    return {'idx':idx,'sign':sign,'length':np.asarray(lens,np.int64),'u':np.asarray(src,np.int64),'v':np.asarray(dst,np.int64), 'dx':np.asarray(dx,float),'r':np.linalg.norm(dx,axis=1)}

def multihit_batched(links,lat,sp,paths,t0=0,lag=10):
    E,V,nt=sp['E'],sp['V'],lat['nt']
    if t0<0 or lag<=0 or lag>=nt:raise ValueError('rectangle must have distinct temporal endpoints')
    sources=np.unique(paths['u'])
    means=np.zeros((V,lag,4),float)
    selected=np.zeros(V,np.bool_);selected[sources]=True
    for v in sources:
        for step in range(lag):
            eid=nt*E+((t0+step)%nt)*V+v
            h=_field(links,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],eid)
            means[v,step]=exact_su2_mean(h)
    D,M=_direct_batched(links,E,V,nt,paths['idx'],paths['sign'],paths['length'],paths['u'],paths['v'],t0,lag,means,selected)
    return D,M

def action_delta_field(links,lat,eid,q):
    """Independent Wilson-action difference evaluated by recomputing affected faces."""
    old=links[eid].copy()
    x=links.copy();x[eid]=q
    js=lat['adj'][eid,:lat['degree'][eid]]
    return float(sum(lat['beta'][f]*(face_trace_scalar(f,x,lat['fi'],lat['sg'])-face_trace_scalar(f,links,lat['fi'],lat['sg'])) for f in js))

def heatbath_source_line(links,lat,sp,source,t0=0,lag=10,seed=1):
    """Exact conditional heatbath resampling of one complete temporal source line.

    Given all other links frozen, these selected same-site/different-time links
    do not share any plaquette, so their joint conditional distribution is the
    PRODUCT of local von Mises-Fisher distributions. One pass yields exact
    conditional equilibrium for that line, not for the whole gauge field.
    """
    E,V,nt=sp['E'],sp['V'],lat['nt']
    if source<0 or source>=V or t0<0 or not 0<lag<nt:raise ValueError('invalid temporal line')
    out=links.copy();rng=np.random.default_rng(seed)
    for step in range(lag):
        eid=nt*E+((t0+step)%nt)*V+source
        h=_field(links,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],eid)
        out[eid]=exact_su2_heatbath(h,rng)
    return out
