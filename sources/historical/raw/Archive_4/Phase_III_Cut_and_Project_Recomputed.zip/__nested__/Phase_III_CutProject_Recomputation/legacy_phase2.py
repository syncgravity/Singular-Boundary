"""Reproducible rhombic Penrose pentagrid and square comparison with SU(2) links.
Dependencies: numpy, scipy. Python >=3.10. All observables finite-volume.
"""
import argparse, json
from dataclasses import dataclass
from itertools import combinations
import numpy as np
from scipy.sparse import lil_matrix
from scipy.linalg import eigvalsh

@dataclass
class Complex:
    labels: list
    xy: np.ndarray
    faces: list
    edges: list


def build_edges(faces):
    return sorted({tuple(sorted((f[i], f[(i+1)%len(f)]))) for f in faces for i in range(len(f))})


def penrose(radius=3.8, line_range=9, gamma=(0.07, 0.19, 0.31, 0.43, 0.61)):
    """Generic 5-grid dual rhombic patch, from pairs of grid-line crossings.
    Distinct gamma offsets avoid triple crossings; neighboring grid cells differ by a basis vector.
    """
    theta=2*np.pi*np.arange(5)/5
    normals=np.column_stack((np.cos(theta),np.sin(theta)))
    gamma=np.asarray(gamma, dtype=float)
    label_to_id={}; labels=[]; faces=[]; seen=set()
    def add(key):
        if key not in label_to_id:
            label_to_id[key]=len(labels); labels.append(key)
        return label_to_id[key]
    for i,j in combinations(range(5),2):
        A=np.stack([normals[i],normals[j]])
        inv=np.linalg.inv(A)
        for p in range(-line_range,line_range+1):
            for q in range(-line_range,line_range+1):
                x=inv@np.array([p+gamma[i],q+gamma[j]])
                if np.linalg.norm(x)>radius: continue
                # Exact four neighboring 5-grid cells at a two-line crossing.
                base=np.floor(normals@x-gamma+1e-10).astype(int)
                # The coordinates on active grid lines are exactly integers.
                base[i]=p-1; base[j]=q-1
                local=[]
                for di,dj in [(0,0),(1,0),(1,1),(0,1)]:
                    k=base.copy(); k[i]+=di; k[j]+=dj
                    local.append(add(tuple(int(t) for t in k)))
                key=tuple(sorted(local))
                if key not in seen: faces.append(tuple(local)); seen.add(key)
    xy=np.array([np.array(v)@normals for v in labels])
    return Complex(labels,xy,faces,build_edges(faces))


def square(nx=9,ny=9):
    labels=[(i,j) for j in range(ny) for i in range(nx)]
    xy=np.array(labels,float)
    vid=lambda i,j:j*nx+i
    faces=[(vid(i,j),vid(i+1,j),vid(i+1,j+1),vid(i,j+1)) for j in range(ny-1) for i in range(nx-1)]
    return Complex(labels,xy,faces,build_edges(faces))


def dagger(a): return a.conj().T

def random_su2(rng, amplitude=0.3):
    v=rng.normal(size=3); v/=np.linalg.norm(v)
    t=rng.normal(scale=amplitude)
    a,b,c=v*np.sin(t)
    return np.array([[np.cos(t)+1j*c, b+1j*a],[-b+1j*a,np.cos(t)-1j*c]])


def links(graph,seed=1,amplitude=0.3):
    rng=np.random.default_rng(seed)
    return {e:random_su2(rng,amplitude) for e in graph.edges}


def oriented(U,u,v):
    return U[(u,v)] if u<v else dagger(U[(v,u)])


def laplacian(graph,U):
    n=len(graph.labels); H=np.zeros((2*n,2*n),dtype=complex)
    for a,b in graph.edges:
        T=U[(a,b)]
        ia=slice(2*a,2*a+2); ib=slice(2*b,2*b+2)
        H[ia,ia]+=np.eye(2); H[ib,ib]+=np.eye(2)
        H[ia,ib]-=T; H[ib,ia]-=dagger(T)
    return H


def holonomies(graph,U):
    out=[]
    for face in graph.faces:
        M=np.eye(2,dtype=complex)
        for a,b in zip(face,face[1:]+face[:1]): M=M@oriented(U,a,b)
        out.append(float(np.real(np.trace(M))/2))
    return np.asarray(out)


def transform(graph,U,seed=42):
    rng=np.random.default_rng(seed)
    gs=[random_su2(rng,1.0) for _ in graph.labels]
    Ut={(a,b):gs[a]@T@dagger(gs[b]) for (a,b),T in U.items()}
    return Ut,gs


def verify(graph,U):
    H=laplacian(graph,U)
    Ut,gs=transform(graph,U)
    Ht=laplacian(graph,Ut)
    G=np.zeros_like(H)
    for i,g in enumerate(gs): G[2*i:2*i+2,2*i:2*i+2]=g
    w=eigvalsh(H)
    return dict(n_vertices=len(graph.labels),n_edges=len(graph.edges),n_faces=len(graph.faces),
      euler_characteristic=len(graph.labels)-len(graph.edges)+len(graph.faces),
      hermiticity_error=float(np.linalg.norm(H-dagger(H))),
      gauge_covariance_error=float(np.linalg.norm(Ht-G@H@dagger(G))),
      min_eigenvalue=float(w[0]),
      spectral_gauge_error=float(np.max(np.abs(w-eigvalsh(Ht)))),
      wilson_gauge_error=float(np.max(np.abs(holonomies(graph,U)-holonomies(graph,Ut)))),
      low_eigenvalues=[float(v) for v in w[:min(12,len(w))]],
      mean_plaquette=float(np.mean(holonomies(graph,U))))


def main():
    p=argparse.ArgumentParser(); p.add_argument('--radius',type=float,default=3.2)
    p.add_argument('--square-size',type=int,default=9); p.add_argument('--seed',type=int,default=2026)
    p.add_argument('--amplitude',type=float,default=0.3);p.add_argument('--output',default='results.json')
    a=p.parse_args()
    graphs={'penrose':penrose(radius=a.radius),'square':square(a.square_size,a.square_size)}
    data={name:verify(g,links(g,a.seed,a.amplitude)) for name,g in graphs.items()}
    with open(a.output,'w') as f:json.dump({'parameters':vars(a),'results':data},f,indent=2)
    print(json.dumps(data,indent=2))
if __name__=='__main__':main()
