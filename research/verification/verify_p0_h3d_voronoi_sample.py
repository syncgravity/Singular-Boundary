#!/usr/bin/env python3
"""Finite Voronoi diagnostic for the alternative 3D Z5 cut-and-project set.

Requires NumPy and SciPy. The coefficient-buffer inequality is exact;
Voronoi coordinates, radii and volumes are floating-point diagnostics.
"""
from collections import Counter
from itertools import product
from math import pi, sqrt
import numpy as np
import scipy
from scipy.spatial import ConvexHull, Delaunay, Voronoi, cKDTree

PHI=(1+sqrt(5))/2
OMEGA=np.exp(2j*pi/5)
SCALE=sqrt(2/5)
OUTER=12
CORE=8
TOL=1e-10

def enumerate_model_set():
    points=[]; labels=[]; core_indices=[]
    for a,b,c,d in product(range(-OUTER,OUTER+1),repeat=4):
        e=-(a+b+c+d)
        if abs(e)>OUTER: continue
        m=(a,b,c,d,e)
        z1=sum(m[j]*OMEGA**j for j in range(5))
        z2=sum(m[j]*OMEGA**(2*j) for j in range(5))
        if abs(z2.imag)<=PHI+TOL:
            idx=len(points)
            points.append((SCALE*z1.real,SCALE*z1.imag,SCALE*z2.real))
            labels.append(m)
            if max(map(abs,m))<=CORE: core_indices.append(idx)
    return np.asarray(points),labels,np.asarray(core_indices,dtype=int)

def main():
    points,labels,core=enumerate_model_set()
    assert len(points)==23525 and len(core)==7383
    assert len(np.unique(np.round(points,12),axis=0))==len(points)
    distances,_=cKDTree(points).query(points[core],k=2)
    nearest=distances[:,1]
    vor=Voronoi(points)
    face_count=np.zeros(len(points),dtype=int)
    for i,j in vor.ridge_points:
        face_count[i]+=1; face_count[j]+=1
    rows=[]
    for i,nn in zip(core,nearest):
        region=vor.regions[vor.point_region[i]]
        assert region and -1 not in region
        vertices=vor.vertices[region]
        radius=float(np.linalg.norm(vertices-points[i],axis=1).max())
        inradius=float(nn/2)
        volume=float(ConvexHull(vertices).volume)
        rows.append((radius,inradius,int(face_count[i]),len(region),volume))
    data=np.asarray(rows)
    radii,inradii=data[:,0],data[:,1]
    faces=Counter(data[:,2].astype(int))
    vertices=Counter(data[:,3].astype(int))
    max_radius=float(radii.max())
    max_aspect=float((radii/inradii).max())

    # Exact buffer: omitted n differs from core m by at least 5 in one
    # integer coordinate. Internal window width is 2*phi; use Parseval.
    omitted=sqrt((2/5)*(25-4*PHI**2))
    assert omitted>2*max_radius
    assert abs(max_radius-0.800870278041345)<1e-8
    assert abs(nearest.min()-0.459505841094721)<1e-8
    assert abs(nearest.max()-1.026053801951947)<1e-8
    assert faces==Counter({12:5396,14:1363,8:624}),faces
    assert vertices==Counter({18:4695,22:1038,20:1026,12:624}),vertices
    assert data[:,4].min()>0

    # Delaunay degeneracy of the core point set; Voronoi remains polyhedral.
    simplices=points[core][Delaunay(points[core]).simplices]
    volumes=np.abs(np.linalg.det(simplices[:,1:]-simplices[:,:1]))/6
    zero=int(np.count_nonzero(volumes<1e-10))
    assert len(volumes)==43220 and zero==2277

    print("P0-H3D finite Voronoi diagnostic: PASS")
    print(f"numpy={np.__version__}; scipy={scipy.__version__}")
    print(f"buffered points={len(points)}; exact-buffer core cells={len(core)}")
    print(f"nearest-neighbour=[{nearest.min():.12f},{nearest.max():.12f}]")
    print(f"Voronoi circumradius=[{radii.min():.12f},{radii.max():.12f}]")
    print(f"Voronoi inradius=[{inradii.min():.12f},{inradii.max():.12f}]")
    print(f"max aspect ratio={max_aspect:.12f}")
    print(f"face histogram={dict(sorted(faces.items()))}")
    print(f"vertex histogram={dict(sorted(vertices.items()))}")
    print(f"volume=[{data[:,4].min():.12f},{data[:,4].max():.12f}]")
    print(f"Delaunay tetrahedra={len(volumes)}; zero-volume={zero}")
    print(f"omitted-point lower bound={omitted:.12f}; twice circumradius={2*max_radius:.12f}")
    print("PASS: buffer excludes omitted points from all core Voronoi cells")
    print("SCOPE: finite candidate geometry only; no gauge Hamiltonian or mass gap")

if __name__=="__main__":
    main()
