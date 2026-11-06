#!/usr/bin/env python3
"""First 3D transverse shell about a 2x2 planar plaquette block.
All cell incidences and GF(2) parity constraints exact; no continuum claim.
"""
from __future__ import annotations
import itertools, json, math
from collections import Counter
import numpy as np
from pathlib import Path
from fractions import Fraction

N=2

def edge(v,a):
    v=tuple(v)
    w=list(v);w[a]+=1
    return (v,tuple(w))

def face(v,a,b):
    v=tuple(v);w=list(v);w[a]+=1;w=tuple(w)
    q=list(v);q[b]+=1;q=tuple(q)
    return ((edge(v,a),1),(edge(w,b),1),(edge(q,a),-1),(edge(v,b),-1))

def slab():
    # Cubical 2x2x1: x,y = 0,1,2; z=0,1
    verts=list(itertools.product(range(3),range(3),range(2)))
    edges=[]
    for v in verts:
        for a,upper in [(0,2),(1,2),(2,1)]:
            if v[a]<upper:edges.append(edge(v,a))
    f=[];labels=[]
    for z in (0,1):
        for x in range(2):
            for y in range(2):
                f.append(face((x,y,z),0,1));labels.append(('xy',x,y,z))
    for y in range(3):
        for x in range(2):
            f.append(face((x,y,0),0,2));labels.append(('xz',x,y,0))
    for x in range(3):
        for y in range(2):
            f.append(face((x,y,0),1,2));labels.append(('yz',x,y,0))
    ee={x:i for i,x in enumerate(edges)}
    bottom=[]
    for i,e in enumerate(edges):
        u,v=e
        if u[2]==v[2]==0 and (u[0]==v[0] and u[0] in (0,2) or u[1]==v[1] and u[1] in (0,2)):
            bottom.append(i)
    facebits=[]
    for fi,faceword in enumerate(f):
        facebits.append(sum(1<<ee[e] for e,sgn in faceword))
    return {'vertices':verts,'edges':edges,'faces':f,'labels':labels,
            'fixed_boundary':set(bottom),'facebits':facebits}

def gf2_nullspace(rows,n):
    mat=list(rows);pivot=[];r=0
    for col in range(n):
        idx=next((i for i in range(r,len(mat)) if (mat[i]>>col)&1),None)
        if idx is None:continue
        mat[r],mat[idx]=mat[idx],mat[r]
        for i in range(len(mat)):
            if i!=r and (mat[i]>>col)&1: mat[i]^=mat[r]
        pivot.append(col);r+=1
    free=[col for col in range(n) if col not in pivot]
    basis=[]
    for j in free:
        vec=1<<j
        for i,col in enumerate(pivot):
            if (mat[i]>>j)&1:vec|=1<<col
        basis.append(vec)
    assert all(not (sum(((vec>>k)&1)*((mask>>k)&1) for k in range(n))%2) for vec in basis for mask in rows)
    return basis,r

def compute():
    G=slab();f=G['facebits'];E=len(G['edges']);F=len(f);assert (len(G['vertices']),E,F)==(18,33,20)
    # Homogeneous interior-link parity and boundary parity on the eight retained edges.
    rows=[]
    for k in range(E):
        if k not in G['fixed_boundary']:
            rows.append(sum((1<<i) for i,v in enumerate(f) if v>>k&1))
    basis,rank=gf2_nullspace(rows,F)
    assert len(basis)==5,(len(basis),rank)
    buckets={'vacuum':[], 'loop':[]}
    bottommask=sum(1<<k for k in G['fixed_boundary'])
    by_area={}
    for subset in range(1<<len(basis)):
        faceset=0
        for j,b in enumerate(basis):
            if subset>>j&1:faceset^=b
        bound=0
        for i,x in enumerate(f):
            if faceset>>i&1:bound^=x
        assert bound&~bottommask==0,(faceset,bound)
        assert bound in (0,bottommask),('mixed boundary',faceset,bound)
        kind='loop' if bound else 'vacuum'
        row={'bits':faceset,'indices':[i for i in range(F) if faceset>>i&1], 'area':faceset.bit_count()}
        buckets[kind].append(row)
    assert {k:len(v) for k,v in buckets.items()}=={'loop':16,'vacuum':16}
    for kind,rs in buckets.items():
        by_area[kind]=dict(sorted(Counter(x['area'] for x in rs).items()))
    # Independent full enumeration over every one of the 2^20 squarefree face subsets.
    # This does not assume a priori that the four-cube boundaries generate every cycle.
    index=np.arange(1<<F,dtype=np.uint32)
    parity=np.zeros(1<<F,dtype=np.uint64)
    for i,mask in enumerate(f):
        parity^=np.where((index>>i)&1,np.uint64(mask),np.uint64(0))
    retained=np.uint64((1<<E)-1-sum(1<<k for k in G['fixed_boundary']))
    good=(parity&retained)==0
    full_solutions=set(int(v) for v in index[good]);small_solutions=set(x['bits'] for l in buckets.values() for x in l)
    assert full_solutions==small_solutions and len(full_solutions)==32
    assert {int(i) for i in np.unique(parity[good])}=={0,bottommask}
    print('Area histograms',by_area)
    loop4=[a for a in buckets['loop'] if a['area']==4]
    loop8=[a for a in buckets['loop'] if a['area']==8]
    vacuum6=[a for a in buckets['vacuum'] if a['area']==6]
    vacuum10=[a for a in buckets['vacuum'] if a['area']==10]
    loop10=[a for a in buckets['loop'] if a['area']==10]
    outer_sphere=[a for a in buckets['vacuum'] if a['area']==16]
    assert len(loop4)==1 and len(loop8)==4 and len(vacuum6)==4
    assert len(vacuum10)==len(loop10)==4 and len(outer_sphere)==1
    assert by_area=={'vacuum':{0:1,6:4,10:4,12:2,14:4,16:1},'loop':{4:1,8:4,10:4,12:7}},by_area
    assert loop4[0]['indices']==list(range(4))
    # Count contracted internal edges and cell vertices on each embedded surface.
    coeffs={}
    for name,sets,expected in [('planar',loop4,4),('bulge',loop8,8),('bubble',vacuum6,6),('double_adjacent_bulge',loop10,10),('double_adjacent_bubble',vacuum10,10)]:
        data=[]
        for a in sets:
            freq=Counter(k for i in a['indices'] for k,_ in G['faces'][i])
            assert all(v==1 or v==2 for v in freq.values()),(name,a)
            internal=sum(v==2 for v in freq.values())
            boundary=sum(v==1 for v in freq.values())
            vertices=set(k for x in freq for k in x)
            # Euler characteristic of surface built from selected faces (disk 1 or sphere 2).
            euler=len(vertices)-len(freq)+expected
            assert euler==(2 if name in ('bubble','double_adjacent_bubble') else 1),(name,a,euler)
            # Edge-Haar factors 1/2 on each internal edge, remaining vertex index loops.
            if name in ('bubble','double_adjacent_bubble'):
                # Sphere: all twelve edges have two incident faces, eight vertices
                assert boundary==0 and internal==2*expected and len(vertices)==expected+2
                factor=2**(2-expected)
            else:
                # Disk: one boundary fundamental trace; E_int = F - 1 + V_int
                assert boundary==8,(name,boundary)
                v_int=len(vertices)-8
                assert internal==expected-1+v_int,(name,internal,v_int)
                factor=2**(v_int-internal)
            assert abs(factor-(2**((2 if name in ('bubble','double_adjacent_bubble') else 1)-expected)))<1e-12
            data.append({'face_labels':[G['labels'][i] for i in a['indices']], 'area':expected,'internal_edges':internal,'boundary_edges':boundary,'surface_vertices':len(vertices),'euler':euler,'haar_coefficient':factor})
        coeffs[name]=data
    # The unique 16-face full outer sphere has four basal faces and a 12-face lid.
    # They meet only on the retained bottom 8-cycle, so the Haar integral factors
    # as (2^-3 chi_f(U))*(2^-11 chi_f(U^-1))=2^-14(chi_0+chi_2).
    exterior=outer_sphere[0]
    assert set(range(4)).issubset(exterior['indices'])
    assert len(exterior['indices'])==16
    for k in G['fixed_boundary']:
        assert sum(k in [G['edges'].index(edge) for edge,_ in G['faces'][i]] for i in exterior['indices'])==2
    # A nontrivial adjoint character requires two fundamental factors on EACH
    # retained boundary link; no other squarefree surface has that support.
    double_perimeter=[]
    for a in buckets['vacuum']:
        if all(sum(k in [G['edges'].index(edge) for edge,_ in G['faces'][i]] for i in a['indices'])==2 for k in G['fixed_boundary']):double_perimeter.append(a)
    assert len(double_perimeter)==1 and double_perimeter[0]==exterior
    # These bounds use only |tr_fund(U)|<=2 and the parity-enumerated face supports;
    # they apply to the positive truncated Wilson-character weight 1+lambda*tr(U),
    # for |lambda|<1/2, not to a claimed 4D Yang--Mills transfer operator.
    bounds=[]
    for lam in (0.001,0.01,0.025,0.05,0.1,0.2):
        q=2*abs(lam)
        rest12=sum(n*q**k for k,n in [(12,9),(14,4),(16,1)])
        den=(1-2*abs(lam))**20
        assert den>0
        p0=1+lam**6/4+lam**10/64
        p1=lam**4/8+lam**8/32+lam**10/128
        b=(2*rest12*(1+abs(p1)/p0))/den
        bounds.append({'lambda':lam,'crude_tail_from_degree_12':rest12,'vacuum_lower_bound':den,
                       'normalized_effective_weight_remainder_upper_bound':b,
                       'effective_normalized_fundamental_rational_approximation':p1/p0,
                       'leading_shell_fundamental_increment':lam**8/32,
                       'adjoint_exact_unscaled_coefficient':lam**16/16384})
    # Exact defining SU(2) matrix Schur orthogonality for the quaternion subgroup.
    eye=np.eye(2,dtype=np.complex128)
    su2_generators=[1j*np.array([[0,1],[1,0]]),1j*np.array([[0,-1j],[1j,0]]),1j*np.array([[1,0],[0,-1]])]
    q8=[sign*a for a in [eye]+su2_generators for sign in (1,-1)]
    for a,b,c,d in itertools.product(range(2),repeat=4):
        avg=sum((u[a,b]*np.conj(u[c,d]) for u in q8))/8
        target=(0.5 if (a==c and b==d) else 0.)
        assert abs(avg-target)<1e-14,(a,b,c,d,avg,target)
    return {'volume':'2x2x1 open 3D cubical slab','vertices':18,'edges':E,'faces':F,'integrated_edges':E-8,'fixed_coarse_boundary_edges':8,
      'nullspace_rank':rank,'nullspace_dimension':len(basis),'allowed_2chains':{k:len(v) for k,v in buckets.items()},
      'area_histograms':by_area,'leading_embedded_surfaces':coeffs,
      'strong_coupling_coefficients':{'vacuum_degree_6':'1/4','fundamental_degree_4':'1/8','fundamental_transverse_degree_8':'1/32', 'fundamental_degree_10_adjacent_bulges':'1/128','vacuum_degree_10_adjacent_bubbles':'1/64','adjoint_degree_16_full_sphere':'1/16384'},
      'normalized_effective_weight':'Z(U;lambda) / integral_SU2 Z(U;lambda) dU',
      'certified_truncation':'P0(lambda)+P1(lambda)*chi_1(U)+R_12(U;lambda), P0=1+lambda^6/4+lambda^10/64, P1=lambda^4/8+lambda^8/32+lambda^10/128',
      'remainder_r12_uniform_bound':'9*(2*abs(lambda))^12+4*(2*abs(lambda))^14+(2*abs(lambda))^16',
      'all_2power20_subsets_checked':True,'positive_action_for_abs_lambda_less_than':0.5,
      'explicit_normalized_remainder_bound':bounds,
      'proof_scope':'Exact 2x2x1 finite 3D spatial SU(2) Haar block with positive truncated plaquette weight; no physical-time transfer, no refinement-uniform claim.'}

if __name__=='__main__':
    data=compute()
    out=Path(__file__).with_name('slab_verification.json');out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k not in ('leading_embedded_surfaces','area_histograms')},indent=2))
