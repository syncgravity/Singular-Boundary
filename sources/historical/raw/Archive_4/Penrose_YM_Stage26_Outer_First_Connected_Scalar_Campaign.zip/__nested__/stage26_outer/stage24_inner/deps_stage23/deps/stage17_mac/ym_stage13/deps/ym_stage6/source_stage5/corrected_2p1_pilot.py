"""Corrected Penrose open-patch SU(2) Wilson 2+1D measurement pilot.

S = beta * sum_{spatial and temporal plaquettes} (1 - 0.5*ReTr U_p).
This uses *uniform* plaquette beta on an open spatial disk (periodic time).
Uniform beta is a demonstrator only, NOT a calibrated irregular-mesh
continuum gauge action. Nothing herein is a continuum glueball/string-tension
estimator. Inputs copied from the two archived studies and imported as modules.

Run: PYTHONPATH=source_phase3/Phase_III_CutProject_Recomputation:source_2p1 \
     python corrected_2p1_pilot.py --pilot
"""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import defaultdict, deque
from pathlib import Path
import numpy as np
from numba import njit
from direct_cut_project import build as build_direct, validate as validate_direct
from wilson_torus import mul, face_trace_scalar

ROOT = Path(__file__).resolve().parent


def geometry(radius=3.5, offset=0):
    g, gamma = build_direct(radius, offset)
    stats = validate_direct(g, gamma)
    edge_ids = {e: i for i, e in enumerate(g.edges)}
    fidx = np.empty((len(g.faces), 4), np.int64)
    signs = np.empty_like(fidx)
    face_areas = np.empty(len(g.faces))
    for i, face in enumerate(g.faces):
        x = g.xy[np.asarray(face)]
        face_areas[i] = abs(np.linalg.det(np.stack((x[1]-x[0], x[3]-x[0]))))
        for j in range(4):
            a,b = face[j], face[(j+1)%4]
            fidx[i,j] = edge_ids[(min(a,b),max(a,b))]
            signs[i,j] = 1 if a < b else -1
    edges = np.asarray(g.edges, dtype=np.int64)
    graph_hash = hashlib.sha256(json.dumps({'labels':g.labels,'faces':g.faces, 'edges':g.edges},
                                          sort_keys=True).encode()).hexdigest()
    return dict(V=len(g.labels),E=len(g.edges),F=len(g.faces),xy=g.xy,edges=edges,
                face_idx=fidx,face_sign=signs,face_areas=face_areas,
                graph_hash=graph_hash,stats=stats,g=g)


def extrude_open(sp, nt, beta):
    """Correct open spatial edges have 3 incident plaquettes (vs 4 interior)."""
    if nt < 4: raise ValueError('nt must be >=4')
    V,E,F = (sp[k] for k in ('V','E','F'))
    L, P = nt*(E+V), nt*(E+F)
    fi = np.empty((P,4),dtype=np.int64)
    sg = np.empty((P,4),dtype=np.int64)
    for t in range(nt):
        for f in range(F):
            p=t*(F+E)+f
            fi[p]=t*E+sp['face_idx'][f]
            sg[p]=sp['face_sign'][f]
        for e,(u,v) in enumerate(sp['edges']):
            p=t*(F+E)+F+e
            fi[p]=[t*E+e,nt*E+t*V+v,((t+1)%nt)*E+e,nt*E+t*V+u]
            sg[p]=[1,1,-1,-1]
    inc=[[] for _ in range(L)]
    for f, row in enumerate(fi):
        for eid in row:inc[int(eid)].append(f)
    degree=np.array([len(x) for x in inc],dtype=np.int64)
    if np.min(degree) < 2:raise AssertionError('orphan or under-connected link')
    boundary_edges=0
    face_use=np.bincount(sp['face_idx'].ravel(),minlength=E)
    for t in range(nt):
        for e in range(E):
            expected=2+face_use[e]
            assert degree[t*E+e]==expected
            if face_use[e]==1:boundary_edges+=1
    vdeg=np.bincount(sp['edges'].flatten(),minlength=V)
    for t in range(nt):
        np.testing.assert_array_equal(degree[nt*E+t*V:nt*E+(t+1)*V],vdeg)
    ai=np.full((L,max(degree)),-1,np.int64)
    for i,faces in enumerate(inc):ai[i,:len(faces)]=faces
    end=np.empty((L,2),dtype=np.int64)
    for t in range(nt):
        for e,(u,v) in enumerate(sp['edges']):end[t*E+e]=(t*V+u,t*V+v)
        for u in range(V):end[nt*E+t*V+u]=(t*V+u,((t+1)%nt)*V+u)
    for row,sgrow in zip(fi,sg):
        start=np.where(sgrow==1,end[row,0],end[row,1])
        stop=np.where(sgrow==1,end[row,1],end[row,0])
        if not np.array_equal(stop,np.roll(start,-1)):
            raise AssertionError('3D plaquette boundary does not close')
    return dict(fi=fi,sg=sg,beta=np.full(P,float(beta)),adj=ai,degree=degree,
                ends=end,nt=nt,V=V,E=E,F=F,L=L,P=P,
                boundary_spatial_links=boundary_edges)


@njit
def run_chain(fi,sg,coupling,adj,degree,L,seed,burn,steps,thin,angle):
    """Saved snapshots permit post-hoc correlators/paths; includes cache check."""
    np.random.seed(seed)
    from_scratch=np.empty((L,4),np.float64)
    for e in range(L):
        q=np.random.randn(4)
        from_scratch[e]=q/np.sqrt(np.sum(q*q))
    pf=np.empty(len(fi))
    for f in range(len(fi)):pf[f]=face_trace_scalar(f,from_scratch,fi,sg)
    nsave=steps//thin
    save=np.empty((nsave,L,4),np.float64)
    action=np.empty(nsave,np.float64)
    accepted=0
    proposals=np.empty(adj.shape[1],np.float64)
    for sweep in range(burn+steps):
        for eid in range(L):
            axis=np.random.randn(3)
            axis/=np.sqrt(np.sum(axis*axis))
            alpha=np.random.random()*angle
            delta=np.array([np.cos(alpha),np.sin(alpha)*axis[0],np.sin(alpha)*axis[1],np.sin(alpha)*axis[2]])
            trial=mul(delta,from_scratch[eid]); ds=0.
            for j in range(degree[eid]):
                f=adj[eid,j]
                proposals[j]=face_trace_scalar(f,from_scratch,fi,sg,eid,trial)
                ds += coupling[f]*(proposals[j]-pf[f])
            if np.log(np.random.random()) < ds:
                from_scratch[eid]=trial
                for j in range(degree[eid]):pf[adj[eid,j]]=proposals[j]
                if sweep>=burn:accepted+=1
        if sweep>=burn and (sweep-burn+1)%thin==0:
            m=(sweep-burn+1)//thin-1
            save[m]=from_scratch
            action[m]=np.sum(coupling*(1-pf))
    maxerror=0.
    for f in range(len(fi)):
        er=abs(pf[f]-face_trace_scalar(f,from_scratch,fi,sg))
        if er>maxerror:maxerror=er
    return save,action,accepted/(steps*L),maxerror


def face_cluster_loops(sp):
    """Construct gauge-invariant thick/thin rhombi and 2-face boundary loops."""
    areas=sp['face_areas'];cut=np.median(areas)
    # Equal-area numerical degeneracies will leave one category empty, which is rejected.
    amin,amax=areas.min(),areas.max()
    cut=(amin+amax)/2
    labs=[];loops=[];counts=defaultdict(int)
    for f in range(sp['F']):
        typ='thick' if areas[f]>cut else 'thin'
        loops.append((sp['face_idx'][f].tolist(),sp['face_sign'][f].tolist()))
        labs.append(typ);counts[typ]+=1
    # Adjacent face pairs: remove shared edge then order oriented 6-edge polygon.
    incident=defaultdict(list)
    for f in range(sp['F']):
        for e in sp['face_idx'][f]:incident[int(e)].append(f)
    for e,fs in sorted(incident.items()):
        if len(fs)!=2:continue
        pairs=[]
        for f in fs:
            for eid,s in zip(sp['face_idx'][f],sp['face_sign'][f]):
                if int(eid)!=e:
                    a,b=sp['edges'][eid]
                    pairs.append((int(a),int(b),int(eid),int(s)) if s==1
                                 else (int(b),int(a),int(eid),int(s)))
        if len(pairs)!=6:raise AssertionError('double loop must have six edges')
        a0=pairs[0]; path=[a0];other=pairs[1:]
        while other:
            choices=[p for p in other if p[0]==path[-1][1]]
            if len(choices)!=1:raise AssertionError('adjacent double face boundary invalid')
            path.append(choices[0]);other.remove(choices[0])
        assert path[-1][1]==path[0][0]
        loops.append(([p[2] for p in path],[p[3] for p in path]))
        labs.append('double');counts['double']+=1
    if any(counts[k]==0 for k in ('thin','thick','double')):
        raise ValueError('operator basis incomplete')
    lengths=np.array([len(e) for e,s in loops],np.int64)
    li=np.full((len(loops),max(lengths)),-1,np.int64)
    sg=np.zeros_like(li)
    for i,(es,ss) in enumerate(loops):li[i,:len(es)]=es;sg[i,:len(ss)]=ss
    typeidx=np.array([('thin','thick','double').index(l) for l in labs],np.int64)
    return dict(idx=li,sign=sg,length=lengths,kind=typeidx,counts=dict(counts))


def make_paths(sp, max_steps=3, per_size=12):
    """Shortest interior spatial paths with accurate endpoint physical distances."""
    E,V=sp['E'],sp['V'];adj=[[] for _ in range(V)]
    face_uses=np.bincount(sp['face_idx'].ravel(),minlength=E)
    boundary=set(sp['edges'][face_uses==1].flatten().tolist())
    for e,(u,v) in enumerate(sp['edges']):
        if face_uses[e]!=2: continue  # exclude boundary edges from static-source paths
        adj[int(u)].append((int(v),e,1));adj[int(v)].append((int(u),e,-1))
    paths=defaultdict(list)
    for origin in range(V):
        if origin in boundary:continue
        q=deque([origin]);best={origin:[]}
        while q:
            u=q.popleft()
            if len(best[u])>=max_steps:continue
            for v,e,s in sorted(adj[u]):
                if v in best:continue
                seq=best[u]+[(e,s)]
                best[v]=seq;q.append(v)
                if v<=origin or v in boundary:continue
                n=len(seq)
                r=float(np.linalg.norm(sp['xy'][origin]-sp['xy'][v]))
                # Exclude tight bent paths that return close to the origin.
                if r>=0.58*n:
                    paths[n].append((r,origin,v,seq))
    chosen=[]
    for n in range(1,max_steps+1):
        candidates=sorted(paths[n],key=lambda a:(a[0],a[1],a[2]))
        if not candidates:continue
        ix=np.unique(np.round(np.linspace(0,len(candidates)-1,min(per_size,len(candidates)))).astype(int))
        chosen.extend((n,*candidates[i]) for i in ix)
    maxlen=max((x[0] for x in chosen),default=0)
    outi=np.full((len(chosen),maxlen),-1,np.int64)
    outs=np.zeros_like(outi)
    meta=[]
    for j,(n,r,u,v,seq) in enumerate(chosen):
        for k,(eid,s) in enumerate(seq):outi[j,k]=eid;outs[j,k]=s
        meta.append({'path_id':j,'edges':n,'physical_r':r,'u':int(u),'v':int(v)})
    return dict(idx=outi,sign=outs,length=np.array([x['edges'] for x in meta],np.int64),
                u=np.array([x['u'] for x in meta],np.int64),v=np.array([x['v'] for x in meta],np.int64),
                meta=meta)


@njit
def trace_closed_path(links, nt,E,t,ids,sgns,n):
    h=np.array([1.,0.,0.,0.])
    for k in range(n):
        q=links[t*E+ids[k]].copy()
        if sgns[k]==-1:q[1:]*=-1
        h=mul(h,q)
    return h[0]


@njit
def loop_scalar_obs(links,nt,E,lo_idx,lo_sign,lo_len,lo_typ):
    obs=np.zeros((nt,3),np.float64)
    count=np.zeros(3,np.float64)
    for j in range(len(lo_len)):count[lo_typ[j]]+=1
    for t in range(nt):
        for j in range(len(lo_len)):
            obs[t,lo_typ[j]]+=1.-trace_closed_path(links,nt,E,t,lo_idx[j],lo_sign[j],lo_len[j])
        for k in range(3):obs[t,k]/=count[k]
    return obs


@njit
def rect_path(links,nt,E,V,path_idx,path_sign,pathlen,u,v,t,lag):
    h=np.array([1.,0.,0.,0.])
    # spatial path u -> v at t
    for k in range(pathlen):
        q=links[t*E+path_idx[k]].copy()
        if path_sign[k]==-1:q[1:]*=-1
        h=mul(h,q)
    # temporal v forward
    for k in range(lag):h=mul(h,links[nt*E+((t+k)%nt)*V+v])
    # spatial path reversed v -> u at t+lag
    for k in range(pathlen-1,-1,-1):
        q=links[((t+lag)%nt)*E+path_idx[k]].copy()
        if path_sign[k]==1:q[1:]*=-1
        h=mul(h,q)
    # temporal u backwards
    for k in range(lag-1,-1,-1):
        q=links[nt*E+((t+k)%nt)*V+u].copy();q[1:]*=-1
        h=mul(h,q)
    return h[0]


@njit
def measure_wilson_paths(links,nt,E,V,paths_idx,paths_sign,paths_len,paths_u,paths_v,maxlag):
    vals=np.empty((len(paths_len),maxlag),np.float64)
    for j in range(len(paths_len)):
        for lag in range(1,maxlag+1):
            s=0.
            for t in range(nt):
                s+=rect_path(links,nt,E,V,paths_idx[j],paths_sign[j],paths_len[j],paths_u[j],paths_v[j],t,lag)
            vals[j,lag-1]=s/nt
    return vals


def corr_operators(obs):
    """Translation averaged connected C_ij(t), with ensemble VEV subtraction."""
    mu=np.mean(obs,axis=(0,1));Nt=obs.shape[1]
    out=np.empty((Nt//2+1,3,3))
    for lag in range(Nt//2+1):
        raw=np.einsum('sti,stj->ij',obs,np.roll(obs,-lag,axis=1))/(obs.shape[0]*Nt)
        out[lag]=raw-np.outer(mu,mu)
    return out


def summarize(snapshot_dict,nt,E,V,loop_basis,paths,B=160):
    """Simple chain-aware bootstrap by blocking within each Markov trajectory."""
    raws=[];rws=[]
    for data in snapshot_dict.values():
        for links in data:
            raws.append(loop_scalar_obs(links,nt,E,loop_basis['idx'],loop_basis['sign'],
                                        loop_basis['length'],loop_basis['kind']))
            rws.append(measure_wilson_paths(links,nt,E,V,paths['idx'],paths['sign'],
                                           paths['length'],paths['u'],paths['v'],min(3,nt//2-1)))
    raw=np.array(raws);rw=np.array(rws)
    # chain resampling of non-overlapping, 3-configuration blocks
    nper=min(len(x) for x in snapshot_dict.values())
    block=max(1,min(3,nper//3))
    blocks=[];s=0
    for values in snapshot_dict.values():
        for i in range(0,len(values)-block+1,block):
            blocks.append(np.arange(s+i,s+i+block))
        s+=len(values)
    C=corr_operators(raw)
    rng=np.random.default_rng(11027)
    cb=[]; wb=[]
    for _ in range(B):
        ind=np.concatenate([blocks[j] for j in rng.integers(0,len(blocks),len(blocks))])
        cb.append(corr_operators(raw[ind]))
        wb.append(rw[ind].mean(axis=0))
    cb=np.asarray(cb);wb=np.asarray(wb)
    c_cov=np.cov(cb.reshape(B,-1),rowvar=False)
    path_means=rw.mean(axis=0)
    binned=[]
    for n in sorted(set(paths['length'].tolist())):
        inds=np.where(paths['length']==n)[0]
        m=path_means[inds].mean(axis=0)
        bt=wb[:,inds,:].mean(axis=1)
        binned.append({'path_edges':int(n),'n_paths':len(inds),
                       'mean_physical_r':float(np.mean([paths['meta'][i]['physical_r'] for i in inds])),
                       'wilson_W_t':m.tolist(), 'bootstrap_se':bt.std(axis=0,ddof=1).tolist()})
    return dict(n_configs=int(len(raw)),block=int(block),n_blocks=int(len(blocks)),
                scalar_operator_names=['thin','thick','double'],
                scalar_C=C.tolist(),scalar_C_bootstrap_se=cb.std(axis=0,ddof=1).tolist(),
                scalar_diag_signal_to_noise_t2=(np.diag(C[2])/np.maximum(1e-30,np.diag(cb.std(axis=0,ddof=1)[2]))).tolist(),
                wilson_by_path_size=binned)


def run_pilot(radius=3.5, offset=0, nt=8, beta=2., seeds=(101,211), burn=24,steps=48,thin=4):
    sp=geometry(radius,offset)
    lat=extrude_open(sp,nt,beta)
    lo=face_cluster_loops(sp)
    paths=make_paths(sp)
    if not len(paths['length']):raise ValueError('no bulk paths')
    snapshots={};chain_stats={}
    for seed in seeds:
        saved, actions, acc, err=run_chain(lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],lat['L'],
                                          int(seed),burn,steps,thin,0.95)
        if err>1e-10:raise ValueError('plaquette cache error')
        snapshots[str(seed)]=saved
        chain_stats[str(seed)]={'acceptance':float(acc),'action_mean':float(actions.mean()),
                                'plaquette_mean':float(1-actions.mean()/(beta*lat['P'])),
                                'max_plaquette_cache_error':float(err)}
    measure=summarize(snapshots,nt,sp['E'],sp['V'],lo,paths)
    # Deliberate no-fit gate: fewer than 3 significant nonzero time lags,
    # insufficient MCMC for validated mass and no large-R/T static potential.
    meta={'status':'smoke-test / exploratory; no continuum extraction',
          'extraction_gates':{'scalar_0pp_mass':'not admitted: no stable three-time-slice plateau or production chain diagnostics',
                              'string_tension':'not admitted: only short path lengths and no large-distance potential plateau',
                              'continuum':'not admitted: no physical tuning or lattice-spacing series'},
          'geometry':{'radius':radius,'offset':offset,'fingerprint':sp['graph_hash'],**sp['stats']},
          'lattice':{'spatial_boundary':'open','time':'periodic','nt':nt,'beta_uniform':beta,
                     'L':lat['L'],'P':lat['P'],'boundary_spatial_links_over_time':lat['boundary_spatial_links']},
          'sampling':{'seeds':list(seeds),'burn':burn,'steps':steps,'thin':thin,'n_snapshots_per_chain':steps//thin},
          'loop_basis_counts':lo['counts'],'n_path_groups':len(set(paths['length'].tolist())),
          'chains':chain_stats,'measurement':measure,
          'limitations':['open finite patch is not toroidal Penrose approximant',
                         'uniform beta on rhombi is not a calibrated isotropic continuum action',
                         'short Markov chains do not establish thermalized production ensemble',
                         'scalar 0++ mass not fit; no reliable plateau',
                         'short small-source loops do not determine string tension',
                         'no continuum trajectory or matched periodic comparator']}
    return meta,snapshots,sp,lat,paths


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--pilot',action='store_true')
    p.add_argument('--radius',type=float,default=3.5)
    p.add_argument('--offset',type=int,default=0)
    p.add_argument('--nt',type=int,default=8)
    p.add_argument('--beta',type=float,default=2.)
    p.add_argument('--burn',type=int,default=24)
    p.add_argument('--steps',type=int,default=48)
    p.add_argument('--thin',type=int,default=4)
    p.add_argument('--outdir',default=str(ROOT/'outputs'))
    a=p.parse_args()
    if not a.pilot: p.error('must explicitly specify --pilot (not continuum production)')
    outdir=Path(a.outdir);outdir.mkdir(parents=True,exist_ok=True)
    report,saves,sp,lat,paths=run_pilot(radius=a.radius,offset=a.offset,nt=a.nt,beta=a.beta,burn=a.burn,steps=a.steps,thin=a.thin)
    (outdir/'pilot_summary.json').write_text(json.dumps(report,indent=2))
    np.savez_compressed(outdir/'pilot_configs.npz',**{'chain_'+k:v for k,v in saves.items()})
    (outdir/'path_metadata.json').write_text(json.dumps(paths['meta'],indent=2))
    print(json.dumps({'geometry':report['geometry'],'lattice':report['lattice'],
                      'chains':report['chains'],'n_configs':report['measurement']['n_configs'],
                      'scalar_C_t2_SNR':report['measurement']['scalar_diag_signal_to_noise_t2'],
                      'wilson':report['measurement']['wilson_by_path_size']},indent=2))

if __name__=='__main__':main()
