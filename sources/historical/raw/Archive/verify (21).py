#!/usr/bin/env python3
"""Exact support-local SU2 Haar-pivot and heatbath-excess certificates.
For two occupied temporal intervals t=0,1 of a three-step Penrose prism.
Does NOT prove ambient-uniform local plaquette energy or full R3.
"""
from pathlib import Path
import csv, json, numpy as np
from scipy.special import ive
from run_supports import growth, spatial_edge_sets, bc
from nested_audit import build,validate,complex_3
ROOT=Path(__file__).resolve().parent
rng=np.random.default_rng(20261027)

def qm(a,b):
    a0=a[0];b0=b[0]
    return np.r_[a0*b0-np.dot(a[1:],b[1:]), a0*b[1:]+b0*a[1:]+np.cross(a[1:],b[1:])]
def inv(a): return np.r_[a[0],-a[1:]]
def haar(n):
    z=rng.normal(size=(n,4));return z/np.linalg.norm(z,axis=1)[:,None]
def prod_word(config,word):
    z=np.array([1.,0.,0.,0.]);
    for edge,sign in word.items():
        z=qm(z,config[edge] if sign==1 else inv(config[edge]))
    return z

def theta(Q,g,ns=3):
    V,E,F=len(g.labels),len(g.edges),len(g.faces)
    Qkeys={(int(t),int(e)) for t,e in Q}
    piv={ (t,e): (0*E+e if t==0 else 2*E+e) for t,e in Qkeys}
    assert all(t in (0,1) for t,e in Qkeys) and len(set(piv.values()))==len(piv)
    return piv

def check_roundtrip(g,cols,meta,Q,pivs):
    V,E,F=len(g.labels),len(g.edges),len(g.faces)
    x=haar(3*(E+V));orig=x.copy()
    # Store independent inserted holonomies in the new coordinates
    y={k: prod_word(orig,cols[3*F+k[0]*E+k[1]]) for k in pivs}
    rec=orig.copy()
    for (t,e),Y in y.items():
        a,b=g.edges[e];U1=orig[E+e];Tv0=orig[3*E+0*V+b];Tu0=orig[3*E+0*V+a];
        if t==0:
            # W0 = U0 Tv0 U1^-1 Tu0^-1 => U0=W0 Tu0 U1 Tv0^-1
            rec[0*E+e]=qm(qm(qm(Y,Tu0),U1),inv(Tv0))
        else:
            # W1 = U1 Tv1 U2^-1 Tu1^-1 => U2=Tu1^-1 W1^-1 U1 Tv1
            Tv1=orig[3*E+V+b];Tu1=orig[3*E+V+a]
            rec[2*E+e]=qm(qm(qm(inv(Tu1),inv(Y)),U1),Tv1)
    err=float(np.max(np.abs(rec-orig)))
    err_y=max(float(np.linalg.norm(prod_word(rec,cols[3*F+t*E+e])-Y)) for (t,e),Y in y.items())
    assert err<1e-12 and err_y<1e-12,(err,err_y)
    # Arbitrary replacement of one inserted Haar coordinate only changes one pivot link
    key=sorted(pivs)[len(pivs)//2];p=pivs[key]
    new=rec.copy(); t,e=key;a,b=g.edges[e];Yn=haar(1)[0];U1=orig[E+e]
    if t==0:
        new[p]=qm(qm(qm(Yn,orig[3*E+a]),U1),inv(orig[3*E+b]))
    else:
        new[p]=qm(qm(qm(inv(orig[3*E+V+a]),inv(Yn)),U1),orig[3*E+V+b])
    face_near={i for i,col in enumerate(cols) if p in col}
    # all exterior face words strictly invariant outside local incidence
    err_far=max((np.linalg.norm(prod_word(rec,col)-prod_word(new,col)) for i,col in enumerate(cols) if i not in face_near),default=0.)
    err_new=float(np.linalg.norm(prod_word(new,cols[3*F+t*E+e])-Yn))
    assert err_far<1e-12 and err_new<1e-12,(err_far,err_new)
    return dict(roundtrip_error=err,inserted_word_error=err_y,far_face_invariance_error=err_far,new_Haar_word_error=err_new)

def compute_entry(g,cols,meta,order,family,radius):
    E,F,V=len(g.edges),len(g.faces),len(g.labels)
    Qkeys=bc(g,order);Q={3*F+t*E+e for t,e in Qkeys}
    P=theta(Qkeys,g)
    allL={link for q in Q for link in cols[q]}
    near_all={i for i,col in enumerate(cols) if i not in Q and any(link in allL for link in col)}
    near_pivot={i for i,col in enumerate(cols) if i not in Q and any(p in col for p in P.values())}
    influence={i for i,col in enumerate(cols) if any(p in col for p in P.values())}
    incident={p:sum(p in col for i,col in enumerate(cols) if i not in Q) for p in P.values()}
    assert max(incident.values())<=3,incident
    assert len(P)==len(Q)
    assert len(near_pivot)<=3*len(P)
    assert len(allL)<=4*len(Q)
    ex_near={link for i in near_all for link in cols[i] if link not in allL}
    # unchanged boundaries even when patch grows and ambient Q is same
    status={
      'radius':float(radius),'family':family,'spatial_selected_faces':len(order),
      'Q_temporal_faces':len(Q),'independent_exact_Haar_pivots':len(P),
      'local_all_insertion_links':len(allL),'retained_faces_touched_by_pivots':len(near_pivot),
      'retained_faces_touched_by_all_Q_links':len(near_all),
      'boundary_links_of_all_Q_region':len(ex_near),
      'max_retained_face_occurrence_per_pivot':max(incident.values()),
      'max_retained_face_occurrence_per_all_local_link':max(sum(k in col for i,col in enumerate(cols) if i not in Q) for k in allL),
      'all_Q_face_words_length':4,
      'max_number_Q_pivots_per_retained_face':max((sum(p in col for p in P.values()) for i,col in enumerate(cols) if i not in Q),default=0),
      'max_transformed_retained_face_word_length_upper_bound':4+3*max((sum(p in col for p in P.values()) for i,col in enumerate(cols) if i not in Q),default=0),
      'collar_for_exact_product_Haar_pivots':0,
      'ratio_local_pivot_faces_per_Q':len(near_pivot)/len(Q),
    }
    return status,Q,P

def staple_check():
    # For one link, conditional Boltzmann factor exp[t*n dot U]; von Mises on SU(2).
    # t=lam*|sum staple quaternions|. Conditional excess = |h|(1-I2(t)/I1(t)).
    grid=np.geomspace(1e-6,1e5,10000)
    r=ive(2,grid)/ive(1,grid)
    bound=grid*(1-r)
    assert bound.max() < 1.5001,float(bound.max())
    # Explicit fully frustrated boundary: two opposite staples (h=0),
    # so both incident faces carry expectation 1 regardless of lambda.
    return {'checked_grid_min_t':float(grid[0]),'checked_grid_max_t':float(grid[-1]),
       'max_t_times_mean_excess_on_grid':float(bound.max()),'universal_bound_analytic':1.5,
       'two_opposite_staples_conditional_frustration':2.,
       'two_opposite_staples_conditional_mean_total_energy':2.,
       'note':'No per-plaquette raw energy bound without controlling expected staple frustration.'}

def main():
    rows=[]; audits=[]
    for radius in (5.,8.,10.):
        g,_=build(radius,0)
        cols,meta=complex_3(g)
        seq,seed=growth(g)
        sizes=([1,3,6,16] if radius==5 else [1,3,6,16,40,80] if radius==8 else [1,3,6,16,40,80,160])
        for family in ('compact','filament'):
            for k in sizes:
                if k>len(seq[family]) or (family=='filament' and k>10):continue
                rec,Q,P=compute_entry(g,cols,meta,seq[family][:k],family,radius)
                rows.append(rec)
                if (radius==5 and k==6 and family=='compact') or (radius==10 and k==160 and family=='compact'):
                    test=check_roundtrip(g,cols,meta,Q,P)
                    audits.append({'radius':radius,'family':family,'n':k,'Q':len(Q),**test})
                print('radius',radius,'family',family,'n',k,'Q',rec['Q_temporal_faces'],'pivot',len(P),'influenced',rec['retained_faces_touched_by_pivots'],flush=True)
    columns=list(rows[0]);
    with (ROOT/'relative_haar_audit.csv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=columns);wr.writeheader();wr.writerows(rows)
    cert={'geometry':'verified direct-Z5 Penrose rhombus disks x 3-step periodic time',
      'support_class':'arbitrary selected temporal faces at steps 0,1; none selected at step 2',
      'analytical_normal_form':'Y_0e=U_e(0) T_v(0) U_e(1)^-1 T_u(0)^-1, Y_1e=U_e(1) T_v(1) U_e(2)^-1 T_u(1)^-1',
      'claim':'The |Q| distinct pivot links can be replaced by the |Q| Wilson-holonomy variables with exact product-Haar measure, fixing all other link coordinates. Each change affects at most 3 retained face words, bounded face length 4.',
      'raw_n':len(rows),'rows':rows,'quaternion_tests':audits,'staple_heatbath':staple_check(),
      'scope_limit':'Does not bound the exterior Gibbs marginal or lambda times expected minimum staple frustration. No arbitrary all-three-step pivot theorem or uniform R3 proof.'}
    (ROOT/'certificate.json').write_text(json.dumps(cert,indent=2))
    print('PASSED',len(rows),'genuine Penrose supports',len(audits),'quaternion audits; staple',cert['staple_heatbath']['max_t_times_mean_excess_on_grid'])
if __name__=='__main__':main()
