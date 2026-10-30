"""Reproducible prototype: rational-slope Z^5 Penrose model-set approximants
and gauge-theory cellulation diagnostics. Not an implementation of earlier
unavailable Monte Carlo source code.
"""
import itertools, json, math
from collections import deque, Counter
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull

EYE = np.eye(5, dtype=np.int64)
PHASE0 = np.array([0.1371, -0.0813, 0.0472, 0.0967, -0.0649])
PHASE = PHASE0 - np.mean(PHASE0)  # fix A4 slice, four canonical pentagonal windows


def saturation_index(t1, t2):
    minors=[int(t1[i]*t2[j]-t1[j]*t2[i]) for i in range(5) for j in range(i+1,5)]
    return math.gcd(*minors)


def saturated_periods(t1, t2):
    """Basis of integer points in the rational 2-plane, not an arbitrary supercell."""
    a=t1.copy();b=t2.copy()
    while (idx:=saturation_index(a,b))>1:
        prime=next(p for p in range(2,idx+1) if idx%p==0 and all(p%i for i in range(2,math.isqrt(p)+1)))
        if np.all(a%prime==0):
            a=a//prime
        elif np.all(b%prime==0):
            b=b//prime
        else:
            lam=next((j for j in range(1,prime) if np.all((b-j*a)%prime==0)),None)
            if lam is None: raise ValueError('Unable to saturate rational-period lattice')
            b=(b-lam*a)//prime
    return a,b


def periods(M):
    th=2*np.pi*np.arange(5)/5
    t1=np.rint(M*np.cos(th)).astype(np.int64)
    t2=np.rint(M*np.sin(th)).astype(np.int64)
    t1[0] = -int(np.sum(t1[1:]))  # preserve C5 physical plane sum-zero
    # Symmetric rounding ensures sum zero for selected M; check explicitly.
    if np.sum(t1) or np.sum(t2):
        raise ValueError(f'Period rounding failed for M={M}, {t1}, {t2}')
    return t1,t2


class Approximant:
    def __init__(self, M, phase=PHASE, primitive_periods=False):
        self.M=M
        self.t1, self.t2=periods(M)
        self.primitive_periods=bool(primitive_periods)
        if self.primitive_periods:
            self.t1,self.t2=saturated_periods(self.t1,self.t2)
        P=np.stack([self.t1,self.t2],axis=1).astype(float)
        U,S,Vt=np.linalg.svd(P.T,full_matrices=True)
        self.Qpar=Vt[:2,:]
        self.Qperp=Vt[2:,:]
        self.phase=np.asarray(phase, dtype=float)
        cube=np.array(list(itertools.product([0., 1.],repeat=5)),dtype=float)
        self.window_verts=(cube@self.Qperp.T)
        self.hull=ConvexHull(self.window_verts)
        self.normals=self.hull.equations[:,:3]
        self.offsets=self.hull.equations[:,3]
        self.hnorm=np.linalg.norm(self.normals,axis=1)
        self.gram11=int(self.t1@self.t1)
        self.gram12=int(self.t1@self.t2)
        self.gram22=int(self.t2@self.t2)
        self.det=self.gram11*self.gram22-self.gram12**2
        assert self.det>0
        self._members={}
        self._build()

    def canon(self,n):
        n=np.asarray(n,dtype=np.int64)
        dot1=int(self.t1@n)
        dot2=int(self.t2@n)
        c1=(self.gram22*dot1-self.gram12*dot2)//self.det
        c2=(self.gram11*dot2-self.gram12*dot1)//self.det
        return tuple((n-c1*self.t1-c2*self.t2).tolist())

    def inside(self,n):
        n=np.asarray(n,dtype=float)
        w=self.Qperp@(n-self.phase)
        return bool(np.max(self.normals@w+self.offsets) < -1e-9)

    def signed_margin(self,n):
        w=self.Qperp@(np.asarray(n,dtype=float)-self.phase)
        return float(np.min(-(self.normals@w+self.offsets)/self.hnorm))

    def _build(self):
        start = None
        for vv in itertools.product(range(-1,3), repeat=5):
            if 1 <= sum(vv) <= 4 and self.inside(vv):
                start = self.canon(vv)
                break
        assert start is not None
        Q=deque([start]); visited={start}
        while Q:
            n=Q.popleft()
            for e in EYE:
                for sign in (-1,1):
                    z=self.canon(np.asarray(n)+sign*e)
                    if z not in visited and self.inside(z):
                        visited.add(z);Q.append(z)
        self.nodes=sorted(visited)
        self.index={p:i for i,p in enumerate(self.nodes)}
        self.neighbors=[]
        for n in self.nodes:
            nb=[]
            for j,e in enumerate(EYE):
                z=self.canon(np.asarray(n)+e)
                nb.append(self.index.get(z,-1))
            self.neighbors.append(nb)
        self.neighbors=np.array(self.neighbors,dtype=np.int64)
        self.edges=[]
        for i,nb in enumerate(self.neighbors):
            for j,z in enumerate(nb):
                if z>=0:
                    self.edges.append((i,int(z),j))
        self.edge_lookup={(i,j):eid for eid,(i,z,j) in enumerate(self.edges)}
        self.faces=[]
        for i in range(len(self.nodes)):
            for a in range(5):
                ia=self.neighbors[i,a]
                if ia<0: continue
                for b in range(a+1,5):
                    ib=self.neighbors[i,b]
                    if ib<0: continue
                    iab=self.neighbors[ia,b]
                    if iab>=0 and self.neighbors[ib,a]==iab:
                        self.faces.append((i,ia,iab,ib,a,b))
        incidence=np.zeros(len(self.edges), dtype=np.int64)
        for i,ia,iab,ib,a,b in self.faces:
            for key in ((i,a),(ia,b),(ib,a),(i,b)):
                eid=self.edge_lookup.get(key)
                if eid is None:
                    raise RuntimeError('face edge not present')
                incidence[eid]+=1
        self.incidence=incidence
        self.margins=np.array([self.signed_margin(n) for n in self.nodes])
        self.degrees=np.zeros(len(self.nodes),dtype=int)
        for a,b,j in self.edges:
            self.degrees[a]+=1;self.degrees[b]+=1

    def stats(self):
        V=len(self.nodes);E=len(self.edges);F=len(self.faces)
        # compare rational plane to true exact Penrose physical space via projector
        angles=np.arange(5)*2*np.pi/5
        Qref=np.vstack([np.cos(angles),np.sin(angles)])/np.sqrt(2.5)
        subspace_err=np.linalg.norm(self.Qpar.T@self.Qpar-Qref.T@Qref,ord=2)
        vs=self.Qpar@EYE.T
        actual=np.array([abs(np.linalg.det(vs[:,[a,b]])) for a in range(5) for b in range(a+1,5)])
        return {
            'M':self.M,'periods':[self.t1.tolist(),self.t2.tolist()],
            'primitive_periods':self.primitive_periods,
            'period_supercell_index':saturation_index(self.t1,self.t2),
            'vertices':V,'edges':E,'faces':F,'euler_torus':V-E+F,
            'edge_face_incidence':dict(sorted(Counter(self.incidence.tolist()).items())),
            'degree_histogram':dict(sorted(Counter(self.degrees.tolist()).items())),
            'minimum_window_margin':float(np.min(self.margins)),
            'relative_subspace_error':float(subspace_err),
            'face_area_min':float(min(actual)),'face_area_max':float(max(actual)),
            'connected':True,
            'window_hull_vertices':len(self.hull.vertices),
        }


def main():
    for M in (3,5,8,13):
        a=Approximant(M)
        print(json.dumps(a.stats()))

if __name__=='__main__':main()

# Supplemental independent checks appended here, used by the study driver.

def exact_penrose_window(phase=PHASE):
    from scipy.linalg import null_space
    theta=np.arange(5)*2*np.pi/5
    Qpar=np.stack((np.cos(theta),np.sin(theta)),axis=0)/np.sqrt(2.5)
    Qperp=null_space(Qpar).T
    vertices=np.array(list(itertools.product([0.,1.],repeat=5)),dtype=float)
    hull=ConvexHull(vertices@Qperp.T)
    return Qpar,Qperp,hull


def inside_3d_window(n, Qperp, hull, phase=PHASE):
    w=Qperp@(np.asarray(n,dtype=float)-phase)
    return bool(np.max(hull.equations[:,:3]@w+hull.equations[:,3]) < -1e-9)


def k_ball(seed, inside, k):
    front={tuple(seed)};nodes=set(front)
    for _ in range(k):
        next_front=set()
        for n in front:
            for e in EYE:
                for s in (-1,1):
                    z=tuple((np.asarray(n)+s*e).tolist())
                    if z not in nodes and inside(z):next_front.add(z)
        nodes.update(next_front);front=next_front
    return nodes


def local_agreements(a, max_k=7):
    _,Qr,hull=exact_penrose_window()
    ref=lambda n: inside_3d_window(n,Qr,hull)
    seed=next((t for t in itertools.product([0,1],repeat=5)
               if sum(t) in (2,3) and ref(t) and a.inside(t)),None)
    if seed is None: raise RuntimeError('No seed common to planes')
    out={}
    for k in range(1,max_k+1):
        r=k_ball(seed,ref,k);p=k_ball(seed,a.inside,k)
        out[k]={'match':r==p,'reference_vertices':len(r),'approximant_vertices':len(p),
                'symmetric_difference':len(r.symmetric_difference(p))}
    return {'seed':seed,'balls':out}


def face_orientation_audit(a):
    edge_signs=[[] for _ in a.edges]
    cross=np.empty((5,5),dtype=float)
    vec=a.Qpar@EYE.T
    for i in range(5):
        for j in range(5): cross[i,j]=np.linalg.det(vec[:,[i,j]])
    for u,ua,uab,ub,aa,bb in a.faces:
        s=1 if cross[aa,bb]>0 else -1
        # positive face around u -> ua -> uab -> ub -> u
        for key,direction in (((u,aa),1),((ua,bb),1),((ub,aa),-1),((u,bb),-1)):
            edge_signs[a.edge_lookup[key]].append(direction*s)
    ok=sum(sorted(ss)==[-1,1] for ss in edge_signs)
    return {'oppositely_oriented_edges':ok,'total_edges':len(a.edges),
            'all_opposite':ok==len(a.edges)}


def pentagon_window_audit(a):
    # At each sum(n)=k section of [0,1]^5, all extreme points have k entries equal to 1.
    # These correspond to four polygonal windows (k=1..4) in the 2D star complement.
    # Get perpendicular 2D coordinates orthogonal to the 5-vector of ones.
    basis=a.Qperp.copy()
    h=basis@np.ones(5)
    u=h/np.linalg.norm(h)
    _,_,vh=np.linalg.svd(u.reshape(1,-1),full_matrices=True)
    twod=vh[1:,:]@basis
    counts={}
    for k in range(1,5):
        verts=np.array([vv for vv in itertools.product([0.,1.],repeat=5) if sum(vv)==k])
        v2=verts@twod.T
        hull=ConvexHull(v2)
        counts[k]=int(len(hull.vertices))
    return counts


def independent_window_membership_audit(a):
    """Cross-check 3D zonotope inclusion using independent 2D pentagon halfspaces.
    Compare every accepted vertex and every excluded one-step neighbor.
    """
    basis=a.Qperp
    h=basis@np.ones(5)
    _,_,vh=np.linalg.svd((h/np.linalg.norm(h)).reshape(1,-1),full_matrices=True)
    perpendicular2=vh[1:,:]@basis
    sections={}
    for k in (1,2,3,4):
        binary=np.array([v for v in itertools.product([0.,1.],repeat=5) if sum(v)==k])
        sections[k]=ConvexHull(binary@perpendicular2.T).equations
    candidates=set(a.nodes)
    for n in a.nodes:
        for e in EYE:
            for s in (-1,1):candidates.add(a.canon(np.asarray(n)+s*e))
    matches=0
    for n in candidates:
        k=sum(n)
        if k in sections:
            x=perpendicular2@(np.asarray(n,dtype=float)-a.phase)
            pentagon_inside=bool(np.max(sections[k][:,:2]@x+sections[k][:,2]) < -1e-9)
        else:
            pentagon_inside=False
        if pentagon_inside!=a.inside(n):raise AssertionError(f'window disagreement: {n}, k={k}')
        matches+=1
    return {'checked_vertices_and_neighbors':matches,'all_agree':True}
