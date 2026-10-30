"""Phase II experimental extensions. Explicit finite-volume SU(2) lattice-gauge benchmarks.

All Metropolis updates target exp[-beta sum_f(1-ReTr(W_f)/2)] product Haar(dU).
Proposal is an isotropic, symmetric SU(2) increment; metropolis is exact for that target.
"""
from __future__ import annotations
import argparse, json, time, platform
from collections import Counter
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
from phase2 import Complex, penrose, square, links, random_su2, oriented, holonomies

def torus(nx,ny):
    if min(nx,ny)<3: raise ValueError('torus dimensions must be >=3')
    labels=[(i,j) for j in range(ny) for i in range(nx)]
    vid=lambda i,j:(j%ny)*nx+(i%nx)
    faces=[(vid(i,j),vid(i+1,j),vid(i+1,j+1),vid(i,j+1)) for j in range(ny) for i in range(nx)]
    edges=sorted({tuple(sorted((f[k],f[(k+1)%4]))) for f in faces for k in range(4)})
    return Complex(labels,np.array(labels,float),faces,edges)

def incidence_report(g,penrose_labels=False,expected_euler=None):
    counts=Counter(tuple(sorted((f[k],f[(k+1)%4]))) for f in g.faces for k in range(4))
    adj=[set() for _ in g.labels]
    for a,b in g.edges: adj[a].add(b);adj[b].add(a)
    visited=set(); components=0
    for start in range(len(adj)):
        if start in visited: continue
        components+=1; todo=[start];visited.add(start)
        while todo:
            for v in adj[todo.pop()]:
                if v not in visited:visited.add(v);todo.append(v)
    faces_valid=all(len(f)==4 and len(set(f))==4 for f in g.faces)
    edge_valid=(set(counts)==set(g.edges) and all(1<=v<=2 for v in counts.values()))
    step_valid=(not penrose_labels or all(np.sum(np.abs(np.array(g.labels[a])-np.array(g.labels[b])))==1 for a,b in g.edges))
    chi=len(g.labels)-len(g.edges)+len(g.faces)
    passed=(faces_valid and edge_valid and step_valid and components==1 and
            (expected_euler is None or chi==expected_euler))
    return dict(passed=passed,vertices=len(g.labels),edges=len(g.edges),faces=len(g.faces),
      euler=chi,components=components,boundary_edges=sum(c==1 for c in counts.values()),
      boundary_per_vertex=sum(c==1 for c in counts.values())/len(g.labels),
      degree_histogram=dict(sorted(Counter(map(len,adj)).items())),
      face_valid=faces_valid,edge_valid=edge_valid,unit_z5_steps=step_valid)

def sparse_laplacian(g,U):
    row=[];col=[];val=[];diag=np.zeros(len(g.labels),dtype=int)
    for a,b in g.edges:
        diag[a]+=1;diag[b]+=1
        T=U[a,b]
        for i in range(2):
            for j in range(2):
                row.extend((2*a+i,2*b+j));col.extend((2*b+j,2*a+i))
                val.extend((-T[i,j],-np.conj(T[i,j])))
    for v,d in enumerate(diag):
        for i in range(2):row.append(2*v+i);col.append(2*v+i);val.append(complex(d))
    return coo_matrix((val,(row,col)),shape=(2*len(g.labels),)*2).tocsr()

def low_spectrum(g,U,k=10,tol=1e-9):
    H=sparse_laplacian(g,U)
    t=time.perf_counter()
    if H.shape[0]<=k+1: vals=np.linalg.eigvalsh(H.toarray())[:k]
    else: vals=np.sort(eigsh(H,k=k,which='SA',tol=tol,return_eigenvectors=False,maxiter=20000))
    elapsed=time.perf_counter()-t
    return dict(eigenvalues=vals.tolist(),elapsed_seconds=elapsed,
                heat_trace_low_mode_lower_bound={str(q):float(np.exp(-q*vals).sum()/(2*len(g.labels))) for q in (0.25,1,4)},
                note='heat_trace_low_mode_lower_bound is not the full heat trace')

def face_adjacencies(g):
    lookup={e:[] for e in g.edges}
    for i,face in enumerate(g.faces):
        for a,b in zip(face,face[1:]+face[:1]):lookup[tuple(sorted((a,b)))].append(i)
    return lookup

def action(g,U,beta):return float(beta*np.sum(1-holonomies(g,U)))

def metropolis_sweep(g,U,beta,rng,step=0.35,adj=None):
    if adj is None:adj=face_adjacencies(g)
    shuffled=list(g.edges);rng.shuffle(shuffled);accepted=0
    # Cache plaquettes so each proposal only recomputes its incident faces.
    p=holonomies(g,U)
    for e in shuffled:
        proposal=random_su2(rng,step)@U[e]
        old=U[e];U[e]=proposal
        touched=adj[e]
        new=np.array([np.real(np.trace(_face_matrix(g.faces[j],U)))/2 for j in touched])
        ds=beta*float(np.sum(p[touched]-new))
        if np.log(rng.random()) < -ds:
            accepted+=1
            p[touched]=new
        else:U[e]=old
    return accepted/len(g.edges)

def _face_matrix(face,U):
    W=np.eye(2,dtype=complex)
    for a,b in zip(face,face[1:]+face[:1]):W=W@oriented(U,a,b)
    return W

def mcmc(g,beta,seed,burn=30,thin=5,samples=12,step=0.4,k=8):
    rng=np.random.default_rng(seed);U={e:random_su2(rng,1.0) for e in g.edges}
    adj=face_adjacencies(g); acceptance=[]; data=[]
    for sweep in range(burn+thin*samples):
        acceptance.append(metropolis_sweep(g,U,beta,rng,step,adj))
        if sweep>=burn and (sweep-burn+1)%thin==0:
            obs=low_spectrum(g,U,k=k)
            data.append(dict(plaquette=float(np.mean(holonomies(g,U))),
                   ground_eigenvalue=float(obs['eigenvalues'][0]),
                   low_spectrum=obs['eigenvalues'],solver_seconds=obs['elapsed_seconds']))
    x=np.array([d['plaquette'] for d in data]);
    lag1=float(np.corrcoef(x[:-1],x[1:])[0,1]) if len(x)>3 and np.std(x)>1e-12 else None
    ess_rough=(len(x)*(1-lag1)/(1+lag1) if lag1 is not None and -0.99<lag1<0.99 else None)
    return dict(beta=beta,seed=seed,burn=burn,thin=thin,samples=samples,step=step,
       acceptance=float(np.mean(acceptance)),plaquette_lag1=lag1,
       plaquette_ess_ar1_approx=ess_rough,measurements=data,
       warning='ESS is an AR(1) heuristic only; short chains are not evidence of equilibration.')

def matched_square(p):
    n=max(3,round(np.sqrt(len(p.labels))))
    return square(n,n)

def run_pilot(radii=(1.8,2.4,3.0,3.6),seeds=range(20),amplitude=0.3,k=6):
    raw=[]
    for radius in radii:
        pg=penrose(radius=radius)
        sg=matched_square(pg)
        for name,g in [('penrose',pg),('square_open',sg)]:
            inc=incidence_report(g,penrose_labels=name=='penrose',expected_euler=1)
            if not inc['passed']:raise AssertionError(f'incidence invalid: {name} radius {radius}: {inc}')
            for seed in seeds:
                r=low_spectrum(g,links(g,seed=seed,amplitude=amplitude),k=k)
                raw.append(dict(radius=radius,graph=name,seed=seed,incidence=inc,
                                eigenvalues=r['eigenvalues'],elapsed_seconds=r['elapsed_seconds']))
    return dict(protocol='independent small-angle random links: NOT Wilson Gibbs ensemble',
       parameters=dict(radii=list(radii),seeds=list(seeds),amplitude=amplitude,k=k),raw=raw)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--mode',choices=['pilot','mcmc','incidence'],default='pilot')
    p.add_argument('--radii',type=float,nargs='+',default=[1.8,2.4,3.0,3.6])
    p.add_argument('--seeds',type=int,default=20)
    p.add_argument('--radius',type=float,default=2.4)
    p.add_argument('--beta',type=float,default=1.0)
    p.add_argument('--burn',type=int,default=30)
    p.add_argument('--thin',type=int,default=5)
    p.add_argument('--samples',type=int,default=12)
    p.add_argument('--seed',type=int,default=2026)
    p.add_argument('--output',default='phase2_extended_results.json')
    a=p.parse_args()
    if a.mode=='pilot':result=run_pilot(a.radii,range(a.seeds))
    elif a.mode=='mcmc':
        g=penrose(a.radius);s=matched_square(g)
        result={name:dict(incidence=incidence_report(graph, name=='penrose'),
             chain=mcmc(graph,a.beta,a.seed,a.burn,a.thin,a.samples)) for name,graph in [('penrose',g),('square_open',s)]}
    else:
        g=penrose(a.radius);s=matched_square(g)
        result={name:incidence_report(graph,name=='penrose',1 if name!='square_torus' else 0) for name,graph in [('penrose',g),('square_open',s),('square_torus',torus(8,8))]}
    out={'environment':dict(python=platform.python_version(),numpy=np.__version__), 'results':result}
    Path(a.output).write_text(json.dumps(out,indent=2))
    print('Wrote',a.output)
if __name__=='__main__': main()
