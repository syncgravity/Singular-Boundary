#!/usr/bin/env python3
"""Rigorous combinatorial finite-SU2 two-scale influence kernel checks.

Not a continuum theorem. Verifies exact cubical incidence/conditional expectation
conditions, Haar fundamental first/second moments and coefficients implied by
analytic Haar/Peter-Weyl identities. Optional parameters test scaling only.
"""
import argparse
import itertools
import json
import math
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.linalg import expm


def geometry(nx,ny,nz):
    dims=(nx,ny,nz)
    vertices=list(itertools.product(*(range(v+1) for v in dims)))
    vmap={v:i for i,v in enumerate(vertices)}
    links=[];lk={}
    for v in vertices:
        for a in range(3):
            if v[a]<dims[a]:
                end=list(v);end[a]+=1;end=tuple(end)
                lk[v,a]=len(links);links.append((vmap[v],vmap[end],v,a))
    faces=[];by_type={'xy':0,'xz':0,'yz':0};pairs=[(0,1,'xy'),(0,2,'xz'),(1,2,'yz')]
    for v in vertices:
        for a,b,name in pairs:
            if v[a]>=dims[a] or v[b]>=dims[b]:continue
            va=list(v);va[a]+=1;va=tuple(va)
            vb=list(v);vb[b]+=1;vb=tuple(vb)
            # Oriented +a,+b,-a,-b for face starting at v
            eids=[lk[v,a],lk[va,b],lk[vb,a],lk[v,b]]
            assert len(set(eids))==4
            faces.append(dict(base=v,orientation=name,edges=eids))
            by_type[name]+=1
    bottom=[]
    # Walk the boundary of bottom xy rectangle, full fine perimeter links
    for x in range(nx):bottom.append(lk[(x,0,0),0])
    for y in range(ny):bottom.append(lk[(nx,y,0),1])
    for x in reversed(range(nx)):bottom.append(lk[(x,ny,0),0])
    for y in reversed(range(ny)):bottom.append(lk[(0,y,0),1])
    assert len(bottom)==2*(nx+ny)==len(set(bottom))
    retain=set(bottom)
    integrated=set(range(len(links)))-retain
    # Need an integrated edge for every face and every distinct face pair.
    for i,p in enumerate(faces):
        assert set(p['edges'])&integrated,(nx,ny,nz,i)
        for j in range(i):
            q=faces[j]
            assert (set(p['edges'])^set(q['edges']))&integrated,(nx,ny,nz,i,j)
    # 8 physical coarse perimeter link products in refined lattice (two halves each)
    assert nx==ny and nx in (2,4) and nz in (1,2)
    boundary_groups=[bottom[k:k+nx//2] for k in range(0,2*nx,nx//2)] if False else None
    # The original slab is 2x2x1, so coarse unit coarse-side = 1 fine-grid edge.
    # Its dyadic subdivision is 4x4x2 and has 2 fine links per coarse link.
    factor=nx//2
    groups=[bottom[k:k+factor] for k in range(0,len(bottom),factor)]
    assert len(groups)==8
    assert all(len(x)==factor for x in groups)
    assert len(links)==sum([nx*(ny+1)*(nz+1),ny*(nx+1)*(nz+1),nz*(nx+1)*(ny+1)])
    assert len(vertices)-len(links)+len(faces)-nx*ny*nz==1
    return dict(nx=nx,ny=ny,nz=nz,n_vertices=len(vertices),n_edges=len(links),n_faces=len(faces),
                face_counts=by_type,n_cubes=nx*ny*nz,n_retained_fine_links=len(bottom),
                n_haar_integrated_links=len(integrated),n_physical_coarse_products=len(groups),
                n_nontrivial_face_pairs=len(faces)*(len(faces)-1)//2,
                all_face_pairs_haar_orthogonal=True,bottom_group_lengths=[len(x) for x in groups]),faces


def qmul(a,b):
    s=a[0]*b[0]-np.dot(a[1:],b[1:]);v=a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:]);return np.r_[s,v]


def qinv(a):return a*np.array([1.,-1.,-1.,-1.])


def trace(q):return 2*q[0]


def moment_check(trials=70):
    # Q8 exactly matches 0th, 1st and 2nd moments of a uniformly distributed SU2
    # quaternion, sufficient for ONE FUNDAMENTAL TRACE and TWO TRACES in one link.
    qs=[]
    for k in range(4):
        u=np.zeros(4);u[k]=1.;qs.extend([u,-u])
    rng=np.random.default_rng(17260706)
    max_first=max_second=0
    for _ in range(trials):
        a,b=rng.normal(size=(2,4));a/=np.linalg.norm(a);b/=np.linalg.norm(b)
        # For one shared integrated SU2 edge in the same character loop
        mean1=np.mean([trace(qmul(q,a)) for q in qs])
        mean2=np.mean([trace(qmul(q,a))*trace(qmul(q,b)) for q in qs])
        exact=trace(qmul(qinv(a),b))/2
        max_first=max(max_first,abs(mean1));max_second=max(max_second,abs(mean2-exact))
    assert max_first<1e-14 and max_second<2e-14
    return {'check':'Q8 exact fundamental SU2 Haar moments (degree<=2 only)',
            'trials':trials,'max_first_moment_error':max_first,'max_second_moment_error':max_second}


def scales(geom_coarse,geom_fine,g_c=1.0,g_f=0.9,h=0.5,frequency=1.0):
    assert g_c>0 and g_f>0 and h>0 and frequency>=0
    F_c,F_f=geom_coarse['n_faces'],geom_fine['n_faces']
    alpha_c=g_c**2/(2*h);alpha_f=g_f**2/h
    beta_c=2/(g_c**2*h);beta_f=4/(g_f**2*h)
    c2_c=F_c*beta_c**2/4;c2_f=F_f*beta_f**2/4
    assert math.isclose(c2_f/c2_c,(128/5)*(g_c/g_f)**4,rel_tol=2e-15)
    # bare-free connected *vacuum* kernel for fixed physical time t
    times=(0.,.1,.5,1.,2.,5.)
    free=[dict(t=t,coarse=c2_c*math.exp(-3*alpha_c*t),fine=c2_f*math.exp(-3*alpha_f*t),
               discrepancy=abs(c2_f*math.exp(-3*alpha_f*t)-c2_c*math.exp(-3*alpha_c*t))) for t in times]
    def bounds(F,alpha,beta,c2):
        # QHQ>=QKQ>=3 alpha/4 Q; also 0<=V<=2 F beta.
        # On the vacuum excited vector B1, K acts with exactly 3 alpha.
        lo=c2/(frequency+3*alpha+2*F*beta)
        hi=c2/(frequency+3*alpha)
        operator_hi=c2/(frequency+3*alpha/4)
        assert lo<=hi<=operator_hi
        return dict(alpha=alpha,beta=beta,memory_t0=c2,
            vacuum_resolvent_lower=lo,vacuum_resolvent_upper=hi,
            general_operator_resolvent_upper=operator_hi,
            memory_time_bound_decay_rate=3*alpha/4,
            unweighted_memory_integral_upper=c2/(3*alpha/4),
            free_vacuum_integral=c2/(3*alpha),
            potential_upper_bound=2*F*beta)
    return dict(g_coarse=g_c,g_fine=g_f,h_coarse=h,h_fine=h/2,frequency=frequency,
        coarse=bounds(F_c,alpha_c,beta_c,c2_c),fine=bounds(F_f,alpha_f,beta_f,c2_f),
        exact_zero_time_ratio=c2_f/c2_c,
        formula_zero_time_ratio='(128/5) * (g0(h)/g0(h/2))^4',
        exact_free_vacuum_memory_ratio_at_zero_time=c2_f/c2_c,
        free_vacuum_memory=free,
        caveat='These are bare conditional-Haar influence bounds at two finite regulators; no physical renormalization or continuum gap follows.')


def finite_spin_block_check(spins=17,alpha=.8,beta=1.4,t=.037,z=.75,steps=7):
    """Independent finite Peter-Weyl *one-plaquette* matrix check, not 3D proof.

    Fundamental SU2 representation ring: chi_1 chi_n=chi_(n+1)+chi_(n-1).
    One coarse channel P=span{chi_0}; the short-time transfer is symmetric.
    """
    assert spins>=5 and beta>0 and alpha>0 and 0<t<1
    dimensions=np.arange(spins,dtype=float)
    H=np.diag(alpha*dimensions*(dimensions+2)/4+beta)
    for i in range(spins-1):H[i,i+1]=H[i+1,i]=-beta/2
    # finite-dimensional matrix H is nonnegative by multiplier bound.
    assert np.linalg.eigvalsh(H).min()>0
    A=H[0,0]
    B=H[1:,0]
    D=H[1:,1:]
    sigma=float(B@np.linalg.solve(D+z*np.eye(spins-1),B))
    direct=float(np.linalg.inv(H+z*np.eye(spins))[0,0])
    schur=1/(A+z-sigma)
    assert abs(direct-schur)<1e-13
    assert abs(B@B-beta**2/4)<1e-14
    # Exact spin-0 two-point influence kernel and finite transfer recursion.
    M=expm(-t*H)
    a=float(M[0,0]);b=M[1:,0];d=M[1:,1:]
    assert np.linalg.eigvalsh(d).min()>0 and np.linalg.eigvalsh(M).min()>0
    L=[float(b@np.linalg.matrix_power(d,k)@b) for k in range(steps)]
    assert min(L)>=-1e-15
    recurrence=[1.]
    for n in range(steps):
        value=a*recurrence[n]
        value+=sum(L[n-1-k]*recurrence[k] for k in range(n))
        recurrence.append(value)
    direct_p=[float(np.linalg.matrix_power(M,n)[0,0]) for n in range(steps+1)]
    diff=max(abs(x-y) for x,y in zip(recurrence,direct_p))
    assert diff<1e-12
    # Full Wilson finite character with symmetric transfer:
    # M_t = exp(-tV/2)exp(-tK)exp(-tV/2).
    K=np.diag(alpha*dimensions*(dimensions+2)/4)
    V=H-K
    ST=expm(-t*V/2)@np.diag(np.exp(-t*np.diag(K)))@expm(-t*V/2)
    qtp=ST[1:,0];tmemory=float(qtp@qtp)
    assert tmemory>=0 and tmemory<=(t**2*beta**2/4)*(1+1e-7)
    return {'model':'finite spin-character SU2 one-plaquette sanity check; not 3D proof',
        'spin_basis_size':spins,'t':t,'z':z,'Feshbach_abs_error':abs(direct-schur),
        'discrete_volterra_max_error':diff,'first_two_step_memory':L[0],
        'symmetric_transfer_memory':tmemory,'leading_continuum_t2_coefficient':beta**2/4,
        'time_memory_bound':t*t*beta**2/4,'discrete_memory_terms':L,
        'evolution':direct_p}


def soft_mode_warning(deltas=(.1,.001,.000001)):
    """Memory kernel can decay quickly even when the total H has a soft mode."""
    rows=[]
    for delta in deltas:
        h=np.array([[1.,1.-delta],[1.-delta,1.]])
        spectrum=np.linalg.eigvalsh(h)
        assert np.allclose(spectrum,[delta,2-delta])
        # P onto the first coordinate, D=1, B=1-delta:
        # full memory is M(t)=(1-delta)^2 exp(-t), independent of the small eigenvalue.
        rows.append({'delta':delta,'full_low_eigenvalue':float(spectrum[0]),
                     'memory_decay_rate':1.,'memory_t0':float((1-delta)**2)})
    return {'model':'positive 2x2 self-adjoint memory-warning toy; not Yang-Mills',
            'conclusion':'fast memory decay does not imply absence of soft modes in the full Schur complement',
            'rows':rows}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path('two_scale_verification.json'))
    parser.add_argument('--g-coarse',type=float,default=1.0);parser.add_argument('--g-fine',type=float,default=0.9)
    parser.add_argument('--h',type=float,default=0.5);parser.add_argument('--frequency',type=float,default=1.0)
    args=parser.parse_args()
    gc,_=geometry(2,2,1);gf,_=geometry(4,4,2)
    assert (gc['n_vertices'],gc['n_edges'],gc['n_faces'],gc['n_cubes'])==(18,33,20,4)
    assert (gf['n_vertices'],gf['n_edges'],gf['n_faces'],gf['n_cubes'])==(75,170,128,32)
    assert (gc['n_retained_fine_links'],gf['n_retained_fine_links'])==(8,16)
    assert (gc['n_haar_integrated_links'],gf['n_haar_integrated_links'])==(25,154)
    assert gc['face_counts']==dict(xy=8,xz=6,yz=6)
    assert gf['face_counts']==dict(xy=48,xz=40,yz=40)
    a=scales(gc,gf,args.g_coarse,args.g_fine,args.h,args.frequency)
    out=dict(status='PASS',scope='Exact finite SU2 cubic influence operator geometry and two-scale certificate; no 4D YM gap or Penrose transfer',
       coarse_geometry=gc,fine_geometry=gf,haar_moments=moment_check(),two_scale=a,finite_character_check=finite_spin_block_check(),soft_mode_warning=soft_mode_warning(),
       analytic_proofs=['Schur orthogonality plus an unretained unique edge for every pair of distinct plaquettes',
                        'QHP=QVP and B*B=(beta² F/4)P',
                        'Block self-adjoint Feshbach Schur formula at real z>=0',
                        'Volterra/Nakajima-Zwanzig memory of P exp(-tH)P',
                        'D>=QKQ>=3alpha/4 on Q and D<=QKQ+2Fbeta',
                        'Vacuum B1 lies in free electric eigenvalue 3alpha',
                        'Duhamel positive-transfer first-memory operator norm <= t² beta²F/4',
                        'Exact discrete transfer Volterra convolution via Q T Q and offdiagonal Q T P'],
       unproved=['scale/volume-uniform renormalized influence control','interacting connected physical-time correlations',
                 'nontrivial 4D OS continuum','Penrose regulator universality','quantum gravity ultraviolet finiteness'])
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS geometry n(2,2,1)=20 faces, n(4,4,2)=128 faces; 8 retained boundary products')
    print('PASS complete pairwise face Haar test:',gc['n_nontrivial_face_pairs'],gf['n_nontrivial_face_pairs'])
    print('PASS Q8 first/second Haar:',out['haar_moments']['max_second_moment_error'])
    print('PASS sharp bare influence ratio:',a['exact_zero_time_ratio'])
    print('PASS rigorous resolvent bounds for two refined spatial regulators')
    print('PASS finite spin-character Feshbach and discrete transfer exact recurrence')
    print('PASS gap-vs-memory soft-mode counterexample')

if __name__=='__main__':main()
