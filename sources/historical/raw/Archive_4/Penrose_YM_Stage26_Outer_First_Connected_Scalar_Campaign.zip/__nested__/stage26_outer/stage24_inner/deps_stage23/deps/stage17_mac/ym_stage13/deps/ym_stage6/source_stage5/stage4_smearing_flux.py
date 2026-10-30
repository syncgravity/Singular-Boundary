"""Stage 4 gauge-covariant APE spatial smearing, scalar spectroscopy and winding flux.

Every transformation is a *measurement* on saved, unchanged Stage-3 SU(2) configurations.
Uniform/area-weighted staple choices are regulator options, not physical improvement claims.
All scalar/torelon fits are fail-closed; a positive signal does not certify a mass.
"""
from __future__ import annotations
from collections import deque
import numpy as np
from numba import njit
from wilson_torus import mul


def staple_structure(sp, weighting='inverse_area'):
    """Produce paths u->v around the other three links of each face.

    APE U'=(1-alpha)U+alpha*sum(w S)/sum(w), projected to SU(2).
    Each staple S transports u->v like edge U, hence local gauge covariance.
    """
    if weighting not in ('inverse_area','uniform'):
        raise ValueError('invalid weighting')
    E=int(sp['E']); fi=np.asarray(sp['face_idx']); fs=np.asarray(sp['face_sign']);areas=np.asarray(sp['face_areas'])
    if not (fi.shape==fs.shape and fi.shape[1]==4):raise ValueError('requires quadrilateral faces')
    st=[[] for _ in range(E)]
    for f in range(len(fi)):
        for j in range(4):
            e=int(fi[f,j]);sg=int(fs[f,j]);rest=[(int(fi[f,(j+k)%4]),int(fs[f,(j+k)%4])) for k in (1,2,3)]
            if sg==1:
                # target u->v; remaining face path is v->u, reverse dagger to u->v
                rest=[(z,-s) for z,s in rest[::-1]]
            # target is v->u: remaining face path is directly u->v
            st[e].append((rest,1/float(areas[f]) if weighting=='inverse_area' else 1.0))
    maxs=max(map(len,st))
    if min(map(len,st))<1 or maxs>2:raise ValueError('invalid spatial face incidence')
    ids=np.full((E,maxs,3),-1,np.int64);sign=np.zeros_like(ids)
    weights=np.zeros((E,maxs),float);n=np.zeros(E,np.int64)
    for e,ss in enumerate(st):
        n[e]=len(ss)
        for k,(rest,w) in enumerate(ss):
            ids[e,k]=[z for z,s in rest]
            sign[e,k]=[s for z,s in rest]
            weights[e,k]=w
    return ids,sign,weights,n

@njit
def _qdagger(q):
    out=q.copy();out[1:]*=-1.
    return out

@njit
def ape_spatial(links, nt, E, staple_ids, staple_signs, weights, nst, alpha, levels):
    """Apply Jacobi-style spatial APE, keeping every temporal link unchanged."""
    if alpha<0 or alpha>=1 or levels<0: raise ValueError('smearing parameters out of range')
    cur=links.copy()
    for level in range(levels):
        nxt=cur.copy()
        for t in range(nt):
            for e in range(E):
                acc=(1-alpha)*cur[t*E+e].copy()
                ws=0.
                for k in range(nst[e]):ws+=weights[e,k]
                for k in range(nst[e]):
                    q=np.array([1.,0.,0.,0.])
                    for j in range(3):
                        z=cur[t*E+staple_ids[e,k,j]]
                        if staple_signs[e,k,j]==-1:z=_qdagger(z)
                        q=mul(q,z)
                    acc+=alpha*(weights[e,k]/ws)*q
                norm=np.sqrt(np.dot(acc,acc))
                if norm<1e-13:raise ValueError('APE projection singular')
                nxt[t*E+e]=acc/norm
        cur=nxt
    return cur


def oriented_windings(sp):
    """Edge deck transformations w(e) from d_e - (x_v - x_u) = P*w(e)."""
    P=np.asarray(sp['periods'],float)
    xy=np.asarray(sp['xy'],float);ends=np.asarray(sp['edges']);D=np.asarray(sp['edge_vectors'])
    real=np.linalg.solve(P,(D-(xy[ends[:,1]]-xy[ends[:,0]])).T).T
    integer=np.rint(real).astype(np.int64)
    residual=float(np.max(np.abs(real-integer)))
    if residual>1e-8:raise ValueError('torus seam displacement inconsistent')
    return integer,residual


def shortest_winding(sp,origin,wind,dw,max_steps=80,box=2):
    """BFS in lifted graph states (vertex, integer winding pair)."""
    V=int(sp['V']);adj=[[] for _ in range(V)]
    for e,(u,v) in enumerate(sp['edges']):
        q=dw[e];adj[int(u)].append((int(v),int(e),1,int(q[0]),int(q[1])))
        adj[int(v)].append((int(u),int(e),-1,-int(q[0]),-int(q[1])))
    goal=(int(origin),int(wind[0]),int(wind[1]));start=(int(origin),0,0)
    que=deque([start]);parent={start:None};depth={start:0}
    while que:
        z=que.popleft()
        if z==goal:break
        if depth[z]>=max_steps:continue
        for v,e,s,wx,wy in adj[z[0]]:
            w0=z[1]+wx;w1=z[2]+wy
            if abs(w0)>box or abs(w1)>box:continue
            nxt=(v,w0,w1)
            if nxt not in parent:
                parent[nxt]=(z,e,s);depth[nxt]=depth[z]+1;que.append(nxt)
    if goal not in parent:raise ValueError('no winding cycle found')
    seq=[];z=goal
    while z!=start:
        prev,e,s=parent[z];seq.append((e,s));z=prev
    return seq[::-1]


def winding_paths(sp, nanchors=6, max_steps=80):
    """Closed graph paths winding once around the two primitive torus periods."""
    dw,res=oriented_windings(sp)
    V=sp['V']; anchors=np.unique(np.linspace(0,V-1,nanchors,dtype=int))
    out=[]
    for direction in range(2):
        wind=(1,0) if direction==0 else (0,1)
        for u in anchors:
            seq=shortest_winding(sp,int(u),wind,dw,max_steps=max_steps)
            dis=sum((sp['edge_vectors'][e]*s for e,s in seq),np.zeros(2))
            expected=np.asarray(sp['periods'])[:,direction]
            if np.max(np.abs(dis-expected))>1e-8:raise AssertionError('winding physical displacement mismatch')
            out.append({'anchor':int(u),'direction':direction,'winding':list(wind),
                        'edges':len(seq),'length':float(np.linalg.norm(dis)),
                        'ids':[int(e) for e,s in seq],'signs':[int(s) for e,s in seq]})
    longest=max(len(q['ids']) for q in out)
    idx=np.full((len(out),longest),-1,np.int64);sg=np.zeros_like(idx);ll=np.zeros(len(out),np.int64)
    dirs=np.zeros(len(out),np.int64)
    for j,p in enumerate(out):
        ll[j]=len(p['ids']);idx[j,:ll[j]]=p['ids'];sg[j,:ll[j]]=p['signs'];dirs[j]=p['direction']
    return dict(idx=idx,sign=sg,length=ll,direction=dirs,meta=out,deck_residual=res)

@njit
def trace_spatial_path(links,nt,E,t,ids,sgns,n):
    h=np.array([1.,0.,0.,0.])
    for j in range(n):
        q=links[t*E+ids[j]]
        if sgns[j]==-1:q=_qdagger(q)
        h=mul(h,q)
    return h[0]

@njit
def measure_winding(links,nt,E,idx,sign,length,direction):
    result=np.zeros((nt,2),np.float64);count=np.zeros(2,np.float64)
    for j in range(len(length)):count[direction[j]]+=1
    for t in range(nt):
        for j in range(len(length)):
            result[t,direction[j]]+=trace_spatial_path(links,nt,E,t,idx[j],sign[j],length[j])
        for k in range(2):result[t,k]/=count[k]
    return result

@njit
def measure_scalar_groups(links,nt,E,idx,sign,length,kind,nkind=3):
    result=np.zeros((nt,nkind),float);cnt=np.zeros(nkind,float)
    for j in range(len(length)):cnt[kind[j]]+=1
    for t in range(nt):
        for j in range(len(length)):
            result[t,kind[j]]+=1.-trace_spatial_path(links,nt,E,t,idx[j],sign[j],length[j])
        for k in range(nkind):
            if cnt[k]>0:result[t,k]/=cnt[k]
    return result


def connected_corr(obs):
    """Symmetric connected C_{ij}(tau) with exact time-translation average."""
    obs=np.asarray(obs,float)
    if obs.ndim!=3:raise ValueError('expected (config,time,operator)')
    nt=obs.shape[1];centered=obs-obs.mean(axis=(0,1))[None,None,:]
    out=np.empty((nt//2+1,obs.shape[2],obs.shape[2]))
    for k in range(len(out)):
        z=np.einsum('cti,ctj->ij',centered,np.roll(centered,-k,axis=1))/(len(obs)*nt)
        out[k]=(z+z.T)/2
    return out


def centered_flux_corr(obs):
    c=connected_corr(obs)
    return np.diagonal(c,axis1=1,axis2=2)


def gevp_diagnostics(C,t0=1,t=2,ridge=1e-8):
    """Diagnostic only; whitening rejects indefinite source metric, no mass fitting."""
    from scipy.linalg import eigh
    A=(C[t0]+C[t0].T)/2;B=(C[t]+C[t].T)/2
    eva=np.linalg.eigvalsh(A);evb=np.linalg.eigvalsh(B)
    msg={'t0':t0,'t':t,'rank':len(eva), 'C_t0_min_eigen':float(eva.min()),
         'C_t_min_eigen':float(evb.min()), 'metric_positive':bool(eva.min()>ridge),
         'principal_correlators':None,'admit_mass':False}
    if eva.min()>ridge:
        msg['principal_correlators']=[float(v) for v in eigh(B,A,eigvals_only=True)]
    return msg


def square_scalar_basis(sp):
    """Translationally and quarter-turn averaged square-torus scalar loop basis.

    1x1 faces; all 1x2 and 2x1 two-face outlines; all 2x2 four-face outlines.
    Unlike a checkerboard partition, these operators do not explicitly select
    one sublattice of the periodic reference.
    """
    if sp.get('spatial_kind')!='square_torus':raise ValueError('square torus required')
    nfaces=sp['F'];P=np.asarray(sp['periods']);a=float(np.sqrt(sp['face_areas'][0]))
    nx=int(np.rint(np.linalg.norm(P[:,0])/a));ny=int(np.rint(np.linalg.norm(P[:,1])/a))
    if nx*ny!=nfaces or min(nx,ny)<5:raise ValueError('square torus dimensions invalid')
    face=lambda i,j:(j%ny)*nx+(i%nx)
    groups=[[],[],[]]
    groups[0]=[[f] for f in range(nfaces)]
    for j in range(ny):
        for i in range(nx):
            groups[1].append([face(i,j),face(i+1,j)])
            groups[1].append([face(i,j),face(i,j+1)])
            groups[2].append([face(i,j),face(i+1,j),face(i,j+1),face(i+1,j+1)])
    loops=[];kinds=[]
    for typ,grp in enumerate(groups):
        for faces in grp:
            oriented={}
            for f in faces:
                for e,s in zip(sp['face_idx'][f],sp['face_sign'][f]):
                    e=int(e);s=int(s)
                    if e in oriented:
                        if oriented[e]!=-s:raise ValueError('inconsistent orientation')
                        del oriented[e]
                    else:oriented[e]=s
            arcs=[]
            for e,s in oriented.items():
                u,v=sp['edges'][e]
                if s<0:u,v=v,u
                arcs.append((int(u),int(v),e,s))
            if not arcs:raise AssertionError('empty face-cluster perimeter')
            start=arcs[0];path=[start];left=arcs[1:]
            while left:
                cand=[p for p in left if p[0]==path[-1][1]]
                if len(cand)!=1:raise ValueError('face-cluster perimeter not a single simple cycle')
                step=cand[0];path.append(step);left.remove(step)
            if path[-1][1]!=path[0][0]:raise ValueError('perimeter does not close')
            loops.append(path);kinds.append(typ)
    maxlen=max(len(p) for p in loops)
    ids=np.full((len(loops),maxlen),-1,np.int64);sign=np.zeros_like(ids);ll=np.zeros(len(loops),np.int64)
    for i,p in enumerate(loops):
        ll[i]=len(p);ids[i,:ll[i]]=[a[2] for a in p];sign[i,:ll[i]]=[a[3] for a in p]
    return dict(idx=ids,sign=sign,length=ll,kind=np.array(kinds,np.int64),counts={
        'plaquette':len(groups[0]),'rectangle_1x2':len(groups[1]),'square_2x2':len(groups[2])})
