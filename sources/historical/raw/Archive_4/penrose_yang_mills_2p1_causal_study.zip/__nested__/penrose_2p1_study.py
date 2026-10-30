"""Experimental SU(2) Wilson theory in 2+1 Euclidean dimensions on extruded
periodic Penrose rhombus and square cellulations.

The diagonal geometric Hodge weights are a discretization *choice*, not a
proved geometry-independent continuum regularization. No gauge fixing.
"""
from __future__ import annotations
import json, math, time
from dataclasses import dataclass
import numpy as np
from numba import njit
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces, square_faces, mul, random_unit_quat, face_trace_scalar


def spatial_penrose(M):
    a=Approximant(M)
    fidx, fsgn, E=penrose_faces(a)
    edges=np.array([(u,v) for u,v,j in a.edges],dtype=np.int64)
    V=len(a.nodes);F=len(a.faces)
    v=a.Qpar@np.eye(5)
    face_areas=np.array([abs(np.linalg.det(v[:,[i,j]])) for u,ua,uab,ub,i,j in a.faces],dtype=float)
    edge_lengths=np.array([np.linalg.norm(v[:,j]) for u,w,j in a.edges],dtype=float)
    fundamental=a.Qpar@np.stack([a.t1,a.t2],axis=1)
    area=abs(np.linalg.det(fundamental))
    assert abs(sum(face_areas)-area)/area < 1e-9
    return dict(kind='penrose',V=V,E=E,F=F,face_idx=fidx,face_sign=fsgn,
                edges=edges,face_areas=face_areas,edge_lengths=edge_lengths,
                area=area,periods=fundamental,model_scale=M)


def spatial_square(nx,ny,area):
    fs,sg,E=square_faces(nx,ny)
    F=nx*ny;V=F
    asq=np.sqrt(area/F)
    edges=np.empty((E,2),dtype=np.int64)
    for y in range(ny):
        for x in range(nx):
            u=x+nx*y
            edges[u]=u,((x+1)%nx)+nx*y
            edges[F+u]=u,x+nx*((y+1)%ny)
    return dict(kind='square',V=V,E=E,F=F,face_idx=fs,face_sign=sg,
                edges=edges,face_areas=np.full(F,asq*asq),edge_lengths=np.full(E,asq),
                area=area,periods=np.diag([nx*asq,ny*asq]),model_scale=None)


def paired_spatial(M):
    p=spatial_penrose(M)
    # near-square control with closest spatial cell count, ignoring F equality
    k=round(np.sqrt(p['F']))
    choices=[(x,y) for x in range(max(3,k-4),k+5) for y in range(max(3,k-4),k+5)]
    target=abs(p['periods'][0,0]*p['periods'][1,1]-p['periods'][0,1]*p['periods'][1,0])
    target_ratio=np.linalg.svd(p['periods'],compute_uv=False)
    aspect=max(target_ratio)/min(target_ratio)
    def score(pair):
        x,y=pair
        density=abs(x*y/p['F']-1)
        ratio=max(x/y,y/x)
        return density + 0.12*abs(math.log(ratio/aspect))
    nx,ny=min(choices,key=score)
    sq=spatial_square(nx,ny,p['area'])
    return p,sq


def geometric_weights(spatial,beta_ref,a_ref,dt):
    farea=spatial['face_areas'];l=spatial['edge_lengths']
    incidence=[[] for _ in range(spatial['E'])]
    for f in range(spatial['F']):
        for e in spatial['face_idx'][f]:
            incidence[e].append(f)
    if any(len(faces)!=2 for faces in incidence):raise ValueError('not a closed quadrangulation')
    # In isotropic Cartesian square geometry of spacing a_ref, both weights beta_ref.
    # Spatial face weights (space-time cell volume / spatial face area squared)
    bs=beta_ref*a_ref*dt/farea
    # Temporal face weights (dual width / edge length) times temporal anisotropy.
    wt=np.array([(farea[fs[0]]+farea[fs[1]])/(2*l[e]**2)
                 for e,fs in enumerate(incidence)])
    bt=beta_ref*a_ref/dt*wt
    return bs,bt


def extrude(spatial,nt,beta_ref,a_ref,dt,mean_targets=None,weight_mode="geometric"):
    V=spatial['V'];E=spatial['E'];F=spatial['F']
    L=nt*(E+V);P=nt*(F+E)
    fi=np.empty((P,4),np.int64);sg=np.empty((P,4),np.int64)
    bs,bt=geometric_weights(spatial,beta_ref,a_ref,dt)
    if mean_targets is not None:
        bs=bs*(mean_targets[0]/bs.mean())
        bt=bt*(mean_targets[1]/bt.mean())
    if weight_mode=='uniform':
        bs=np.full(F,float(bs.mean()))
        bt=np.full(E,float(bt.mean()))
    elif weight_mode=='shuffled':
        rng=np.random.default_rng(4051)
        bs=bs[rng.permutation(F)]
        bt=bt[rng.permutation(E)]
    elif weight_mode!='geometric':raise ValueError('unknown weight_mode')
    couplings=np.empty(P);kinds=np.empty(P,np.int8)
    for t in range(nt):
        ofs=t*E;ofsnext=((t+1)%nt)*E
        tlink=nt*E+t*V
        for f in range(F):
            p=t*(F+E)+f
            fi[p]=ofs+spatial['face_idx'][f]
            sg[p]=spatial['face_sign'][f]
            couplings[p]=bs[f];kinds[p]=0
        for e,(u,v) in enumerate(spatial['edges']):
            p=t*(F+E)+F+e
            fi[p]=ofs+e,tlink+v,ofsnext+e,tlink+u
            sg[p]=1,1,-1,-1
            couplings[p]=bt[e];kinds[p]=1
    # General 3D link-face incidence, variable edge degree (3-7 temporal links)
    adj=[[] for _ in range(L)]
    orient=[[] for _ in range(L)]
    for f in range(P):
        for k in range(4):
            eid=int(fi[f,k]);adj[eid].append(f);orient[eid].append(int(sg[f,k]))
    if any(len(x)==0 for x in adj):raise ValueError('orphan link')
    # 3D edges have mixed plaquette orientations; an unsigned sum of
    # face-boundary signs is NOT required to vanish around each edge.
    for e in range(nt*E):
        if len(adj[e]) != 4: raise ValueError('spatial link must meet four plaquettes')
    for e in range(nt*E,L):
        if len(adj[e]) < 3: raise ValueError('temporal link must meet at least three ribbons')
    maxdeg=max(map(len,adj));ai=np.full((L,maxdeg),-1,np.int64)
    an=np.empty(L,np.int64)
    for e,ff in enumerate(adj):
        an[e]=len(ff);ai[e,:len(ff)]=ff
    return dict(fi=fi,sg=sg,beta=couplings,kinds=kinds,adj=ai,degree=an,
                nt=nt,L=L,P=P,F=F,E=E,V=V,bs=bs,bt=bt,
                space=spatial)


@njit
def rect_trace(links,nt,E,V,edges,e,t,lag):
    """Gauge-invariant rectangular temporal Wilson loop, spacing = one edge."""
    u=edges[e,0];v=edges[e,1]
    q=links[(t%nt)*E+e].copy()
    for k in range(lag):
        qt=links[nt*E+((t+k)%nt)*V+v]
        q=mul(q,qt)
    qs=links[((t+lag)%nt)*E+e].copy()
    qs[1:]*=-1
    q=mul(q,qs)
    for k in range(lag-1,-1,-1):
        qt=links[nt*E+((t+k)%nt)*V+u].copy()
        qt[1:]*=-1
        q=mul(q,qt)
    return q[0]

@njit
def chain_3d(fi,sg,betas,adj,degree,nt,F,E,V,edges,seed,burn,steps,thin,angle):
    np.random.seed(seed)
    L=len(adj);P=len(fi)
    links=np.empty((L,4),np.float64)
    for e in range(L):links[e]=random_unit_quat()
    plaquette=np.empty(P,np.float64)
    for f in range(P):plaquette[f]=face_trace_scalar(f,links,fi,sg)
    nsave=steps//thin
    # Spatial action density: mean_f [(Amean/Af) (1 - plaquette_f)]
    # Caller can weight time-slice output and calculate connected correlators.
    spatial_series=np.empty((nsave,nt,F),np.float32)
    mean_spatial=np.empty(nsave,np.float64)
    mean_temporal=np.empty(nsave,np.float64)
    mean_action=np.empty(nsave,np.float64)
    rectangle=np.empty((nsave,nt//2),np.float64)
    accept=0
    new_pf=np.empty(adj.shape[1],np.float64)
    for sweep in range(burn+steps):
        for eid in range(L):
            axis=np.random.randn(3)
            axis=axis/np.sqrt(np.sum(axis*axis))
            alpha=np.random.random()*angle
            qd=np.array([np.cos(alpha),np.sin(alpha)*axis[0],np.sin(alpha)*axis[1],np.sin(alpha)*axis[2]])
            trial=mul(qd,links[eid])
            ds=0.
            for j in range(degree[eid]):
                f=adj[eid,j]
                val=face_trace_scalar(f,links,fi,sg,eid,trial)
                new_pf[j]=val
                ds+=betas[f]*(val-plaquette[f])
            if np.log(np.random.random())<ds:
                links[eid]=trial
                for j in range(degree[eid]):
                    f=adj[eid,j]
                    plaquette[f]=new_pf[j]
                if sweep>=burn:accept+=1
        if sweep>=burn and (sweep-burn+1)%thin==0:
            j=(sweep-burn+1)//thin-1
            tot_s=0.;tot_t=0.;tots=0.
            for t in range(nt):
                for f in range(F):
                    p=t*(F+E)+f
                    v=plaquette[p]
                    spatial_series[j,t,f]=v
                    tot_s+=v
                    tots+=betas[p]*(1-v)
                for e in range(E):
                    p=t*(F+E)+F+e
                    v=plaquette[p]
                    tot_t+=v
                    tots+=betas[p]*(1-v)
            mean_spatial[j]=tot_s/(nt*F)
            mean_temporal[j]=tot_t/(nt*E)
            mean_action[j]=tots/P
            for lag in range(1,nt//2+1):
                qsum=0.
                for tt in range(nt):
                    for ee in range(E):
                        qsum+=rect_trace(links,nt,E,V,edges,ee,tt,lag)
                rectangle[j,lag-1]=qsum/(nt*E)
    err=0.
    for f in range(P):
        zz=abs(plaquette[f]-face_trace_scalar(f,links,fi,sg))
        if zz>err:err=zz
    return spatial_series,mean_spatial,mean_temporal,mean_action,rectangle,accept/(L*steps),err


def correlator_moments(series,area_weights):
    # series: Nsav x Nt x F. Spatial gauge-invariant scalar integrated action density.
    # subtract constants after forming ensemble moment (do NOT subtract each slice mean).
    obs=np.einsum('stf,f->st',1-series,area_weights)/np.sum(area_weights)
    nt=obs.shape[1];maxlag=nt//2
    q=np.stack([(obs*np.roll(obs,-lag,axis=1)).mean(axis=1)
                for lag in range(maxlag+1)],axis=1)
    return obs.mean(axis=1),q


def stationary_block_stats(one,q,block=15):
    # moving-free blocks, estimating between-block standard errors using jackknife.
    n=len(one)//block
    if n<5:raise ValueError('need at least five independent-ish blocks')
    m1=one[:n*block].reshape(n,block).mean(axis=1)
    m2=q[:n*block].reshape(n,block,q.shape[1]).mean(axis=1)
    mu=m1.mean();mom=m2.mean(axis=0)
    conn=mom-mu**2
    jk=[]
    for i in range(n):
        lm=(np.sum(m1)-m1[i])/(n-1)
        qq=(np.sum(m2,axis=0)-m2[i])/(n-1)
        jk.append(qq-lm*lm)
    jk=np.asarray(jk)
    se=np.sqrt((n-1)/n*np.sum((jk-jk.mean(axis=0))**2,axis=0))
    return conn,se,n


def autocorr_diagnostic(x,lagcap=30):
    x=np.asarray(x,float)
    x=x-np.mean(x)
    var=np.mean(x*x)
    if var==0:return {'tau_int_saved_samples':None,'rho_1':None}
    ac=np.array([np.mean(x[:-k]*x[k:])/var for k in range(1,min(lagcap+1,len(x)//4))])
    tau=0.5
    for a in ac:
        if a<=0:break
        tau+=a
    return {'tau_int_saved_samples':float(tau),'rho_1':float(ac[0]) if len(ac) else None}


def rectangle_energy_jackknife(rect,dt,block):
    n=len(rect)//block
    b=rect[:n*block].reshape(n,block,rect.shape[1]).mean(axis=1)
    avg=b.mean(axis=0)
    en=[]
    for i in range(len(avg)-1):
        if min(avg[i],avg[i+1])<=0:
            en.append([None,None]);continue
        e=-np.log(avg[i+1]/avg[i])/dt
        vals=[]
        for k in range(n):
            ww=(n*avg-b[k])/(n-1)
            if min(ww[i],ww[i+1])>0:
                vals.append(-np.log(ww[i+1]/ww[i])/dt)
        if len(vals)!=n:en.append([float(e),None]);continue
        vals=np.asarray(vals)
        se=np.sqrt((n-1)/n*np.sum((vals-np.mean(vals))**2))
        en.append([float(e),float(se)])
    return en


def run_once(spatial,nt,beta_ref,seed,burn,steps,thin,block,dt,a_ref,angle=0.95,mean_targets=None,weight_mode="geometric"):
    lat=extrude(spatial,nt,beta_ref,a_ref,dt,mean_targets=mean_targets,weight_mode=weight_mode)
    t0=time.perf_counter()
    vals,s,t,action,rect,acc,err=chain_3d(lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],nt,lat['F'],lat['E'],lat['V'],spatial['edges'],seed,burn,steps,thin,angle)
    weights=a_ref*a_ref/spatial['face_areas']
    mu,mom=correlator_moments(vals,weights)
    corr,sec,nblocks=stationary_block_stats(mu,mom,block=block)
    def sample_stats(arr):
        arr=arr[:len(arr)//block*block].reshape(-1,block).mean(axis=1)
        return float(arr.mean()),float(arr.std(ddof=1)/np.sqrt(len(arr)))
    return {'geometry':spatial['kind'],'nt':nt,'seed':seed,'beta_ref':beta_ref,
            'burn':burn,'steps':steps,'thin':thin,'blocks':nblocks,'block_configurations':block,
            'spatial_plaquette':sample_stats(s),'temporal_plaquette':sample_stats(t),
            'action_per_plaquette':sample_stats(action),
            'rectangular_wilson_loops':[sample_stats(rect[:,k]) for k in range(rect.shape[1])],
            'rectangle_effective_static_energies':rectangle_energy_jackknife(rect,dt,block),
            'autocorrelation':{'spatial':autocorr_diagnostic(s),'temporal':autocorr_diagnostic(t),
                               'rectangle_tau2':autocorr_diagnostic(rect[:,1])},
            'correlator':corr.tolist(),'correlator_se_jackknife':sec.tolist(),
            'acceptance':float(acc),'max_cache_error':float(err),
            'seconds':time.perf_counter()-t0,
            'spatial_coupling_mean':float(np.mean(lat['bs'])),
            'temporal_coupling_mean':float(np.mean(lat['bt'])),
            'spatial_coupling_range':[float(np.min(lat['bs'])),float(np.max(lat['bs']))],
            'temporal_coupling_range':[float(np.min(lat['bt'])),float(np.max(lat['bt']))]}


def run_study(M=5,betas=(2.5,),nt=10,seeds=(109,211),burn=160,steps=600,thin=3,block=10,normalize_means=True,weight_mode="geometric"):
    pp,ss=paired_spatial(M)
    area=pp['area'];a_ref=np.sqrt(area/pp['F']);dt=a_ref
    meta={'M':M,'nt':nt,'physical_area':float(area),'time_spacing':float(dt),
          'time_extent':float(nt*dt),'reference_spatial_spacing':float(a_ref),'normalize_mean_couplings':bool(normalize_means),
          'weight_mode':weight_mode,
          'geometry':{g['kind']:{'V':g['V'],'E':g['E'],'F':g['F'],
                  'periods':g['periods'].tolist(),'face_area_range':[float(x) for x in (min(g['face_areas']),max(g['face_areas']))],
                  'spatial_length_range':[float(x) for x in (min(g['edge_lengths']),max(g['edge_lengths']))]}
                      for g in (pp,ss)},'results':[]}
    for beta in betas:
        for geom in (pp,ss):
            for seed in seeds:
                means=(beta*a_ref*dt/(area/ss['F']),beta*a_ref/dt) if normalize_means else None
                result=run_once(geom,nt,beta,seed,burn,steps,thin,block,dt,a_ref,mean_targets=means,weight_mode=weight_mode)
                meta['results'].append(result)
                print(json.dumps({'M':M,'beta':beta,'geom':geom['kind'],'seed':seed,'sp':result['spatial_plaquette'],
                                'tm':result['temporal_plaquette'],'R2':result['rectangular_wilson_loops'][1],
                                'C1':result['correlator'][1],
                                'seC1':result['correlator_se_jackknife'][1],
                                'elapsed_s':round(result['seconds'],2)}),flush=True)
    return meta

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument('--M',type=int,default=5)
    ap.add_argument('--betas',nargs='+',type=float,default=[2.5])
    ap.add_argument('--nt',type=int,default=10)
    ap.add_argument('--seeds',nargs='+',type=int,default=[109,211])
    ap.add_argument('--burn',type=int,default=160)
    ap.add_argument('--steps',type=int,default=600)
    ap.add_argument('--thin',type=int,default=3)
    ap.add_argument('--block',type=int,default=10)
    ap.add_argument('--raw-geometric',action='store_true')
    ap.add_argument('--weight-mode',choices=['geometric','uniform','shuffled'],default='geometric')
    ap.add_argument('--out',type=str,default='study_2p1_results.json')
    args=ap.parse_args()
    out=run_study(M=args.M,betas=args.betas,nt=args.nt,seeds=args.seeds,
                  burn=args.burn,steps=args.steps,thin=args.thin,block=args.block,normalize_means=not args.raw_geometric,weight_mode=args.weight_mode)
    with open(args.out,'w') as f:json.dump(out,f,indent=2)
