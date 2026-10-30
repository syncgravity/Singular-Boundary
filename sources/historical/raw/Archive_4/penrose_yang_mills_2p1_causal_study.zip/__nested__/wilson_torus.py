"""Local Metropolis SU(2) Wilson simulation for arbitrary orientable quadrangulated tori.
Actions: S=beta sum_f (1 - 1/2 ReTr holonomy_f).
Each link is a norm-one quaternion, and each edge belongs to two faces.
"""
import json, math, time
from pathlib import Path
import numpy as np
from scipy.special import iv
from numba import njit
from penrose_causal_study import Approximant,face_orientation_audit


def penrose_faces(a):
    assert face_orientation_audit(a)['all_opposite']
    fidx=np.empty((len(a.faces),4),np.int64)
    sgn=np.empty((len(a.faces),4),np.int64)
    v=a.Qpar@np.eye(5)
    for f,(u,ua,uab,ub,i,j) in enumerate(a.faces):
        sign=np.linalg.det(v[:,[i,j]])
        if sign>0:
            pairs=[((u,i),1),((ua,j),1),((ub,i),-1),((u,j),-1)]
        else:
            pairs=[((u,j),1),((ub,i),1),((ua,j),-1),((u,i),-1)]
        for k,(key,d) in enumerate(pairs):
            fidx[f,k]=a.edge_lookup[key]
            sgn[f,k]=d
    return fidx,sgn,len(a.edges)


def square_faces(nx,ny):
    F=nx*ny
    fidx=np.empty((F,4),np.int64);sgn=np.array([[1,1,-1,-1]]*F,np.int64)
    for y in range(ny):
        for x in range(nx):
            f=x+nx*y
            h0=x+nx*y
            v1=F+((x+1)%nx)+nx*y
            h2=x+nx*((y+1)%ny)
            v3=F+x+nx*y
            fidx[f,:]=h0,v1,h2,v3
    return fidx,sgn,2*F


def prepare_cellulation(fidx,sgn,E):
    f_of_e=np.full((E,2),-1,np.int64)
    vcount=np.zeros(E,np.int64)
    for f in range(len(fidx)):
        for k in range(4):
            e=fidx[f,k]
            if vcount[e]>=2:raise ValueError(f'edge {e} overincident')
            f_of_e[e,vcount[e]]=f
            vcount[e]+=1
    if not np.all(vcount==2):raise ValueError('Not all edges 2-incident')
    # Orientations should be opposite across each edge.
    for e in range(E):
        fs=f_of_e[e]
        if sum(sgn[f,k] for f in fs for k in range(4) if fidx[f,k]==e):
            raise ValueError('Incorrect orientation')
    return f_of_e


@njit

def mul(q,r):
    a,b,c,d=q
    w,x,y,z=r
    return np.array([a*w-b*x-c*y-d*z,
                     a*x+b*w+c*z-d*y,
                     a*y-b*z+c*w+d*x,
                     a*z+b*y-c*x+d*w])

@njit

def face_trace_scalar(f,links,fidx,sgn,updated=-1,trial=None):
    q=np.array([1.,0.,0.,0.])
    for k in range(4):
        eid=fidx[f,k]
        qq=links[eid] if eid!=updated else trial
        if sgn[f,k]==-1:
            qq=np.array([qq[0],-qq[1],-qq[2],-qq[3]])
        q=mul(q,qq)
    return q[0]


@njit

def random_unit_quat():
    q=np.random.randn(4)
    return q/np.sqrt(np.sum(q*q))


@njit

def metropolis_chain(fidx,sgn,adj,E,beta,seed,burn,measure,angle):
    np.random.seed(seed)
    F=len(fidx)
    links=np.empty((E,4))
    for e in range(E): links[e]=random_unit_quat()
    pf=np.empty(F)
    for f in range(F):pf[f]=face_trace_scalar(f,links,fidx,sgn)
    measurements=np.empty(measure)
    accepted=0
    ca=np.cos(angle)
    sa=np.sin(angle)
    for sweep in range(burn+measure):
        for eid in range(E):
            axis=np.random.randn(3)
            axis=axis/np.sqrt(np.sum(axis*axis))
            alpha=np.random.random()*angle
            qdelta=np.array([np.cos(alpha),np.sin(alpha)*axis[0],np.sin(alpha)*axis[1],np.sin(alpha)*axis[2]])
            trial=mul(qdelta,links[eid])
            fa=adj[eid,0]; fb=adj[eid,1]
            old=pf[fa]+pf[fb]
            af=face_trace_scalar(fa,links,fidx,sgn,eid,trial)
            bf=face_trace_scalar(fb,links,fidx,sgn,eid,trial)
            if np.log(np.random.random())<beta*(af+bf-old):
                links[eid]=trial
                pf[fa]=af;pf[fb]=bf
                if sweep>=burn: accepted+=1
        if sweep>=burn: measurements[sweep-burn]=np.mean(pf)
    # check cached values agree with recomputation
    err=0.
    for f in range(F):
        z=abs(pf[f]-face_trace_scalar(f,links,fidx,sgn))
        if z>err:err=z
    return measurements,accepted/(E*measure),err


def batch_stats(chains,block=25):
    means=[]
    for arr in chains:
        n=len(arr)//block
        means.extend(arr[:n*block].reshape(n,block).mean(axis=1))
    means=np.asarray(means)
    return float(means.mean()),float(means.std(ddof=1)/np.sqrt(len(means))),len(means)


def run_comparison(M=13,nx=34,ny=40,betas=(2.,4.),seeds=(11,29,47),burn=250,measure=750,primitive_periods=False):
    a=Approximant(M,primitive_periods=primitive_periods)
    pen=penrose_faces(a)
    sq=square_faces(nx,ny)
    assert len(pen[0])==len(sq[0])
    result={'geometry':a.stats(),'square':{'nx':nx,'ny':ny,'F':nx*ny},'parameters':{'burn':burn,'measure':measure,'seeds':seeds},'runs':[]}
    for beta in betas:
        run={}
        for name,(fe,si,E) in [('penrose',pen),('square',sq)]:
            adj=prepare_cellulation(fe,si,E)
            ts=time.perf_counter()
            chains=[];rates=[];errs=[]
            for s in seeds:
                samples,rate,err=metropolis_chain(fe,si,adj,E,beta,int(s),burn,measure,angle=1.15)
                chains.append(samples);rates.append(float(rate));errs.append(float(err))
            mean,se,nblocks=batch_stats(chains,block=25)
            run[name]={'mean_plaquette':mean,'se_block_25':se,'n_blocks':nblocks,
                       'acceptance':float(np.mean(rates)),'max_cache_error':max(errs),'seconds':round(time.perf_counter()-ts,2),
                       'per_chain_means':[float(x.mean()) for x in chains]}
        exact=float(iv(2,beta)/iv(1,beta))
        diff=run['penrose']['mean_plaquette']-run['square']['mean_plaquette']
        se=np.hypot(run['penrose']['se_block_25'],run['square']['se_block_25'])
        result['runs'].append({'beta':float(beta),'exact_thermodynamic_plaquette':exact,
                               **run,'penrose_minus_square':float(diff), 'difference_se':float(se),
                               'difference_z':float(diff/se)})
    return result

if __name__=='__main__':
    result=run_comparison()
    with open(Path(__file__).with_name('wilson_comparison_results.json'),'w') as f:json.dump(result,f,indent=2)
    print(json.dumps(result,indent=2))
