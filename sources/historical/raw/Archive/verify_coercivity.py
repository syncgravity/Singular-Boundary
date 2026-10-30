#!/usr/bin/env python3
"""Test exact gauge-covariant near-pure-gauge collar coercivity, nonabelian
Q14 exterior obstruction, and an unconditional one-link Peierls center flip.
Proven statements are in FORMAL_NOTE.md; random quaternion checks are audits.
"""
import json, math
from pathlib import Path
import numpy as np
from direct_cut_project import build
from construct_surgery import product_collar,shell,qmul,qinv,character_word,unit_random
from cavity_audit import seed_support,Q_from_seed
ROOT=Path(__file__).resolve().parent
rng=np.random.default_rng(20261027)
seed=seed_support(build(5.,0)[0]);g0,_=build(5.,0)
E0=len(g0.edges);special_key=tuple(sorted((g0.labels[g0.edges[19][0]],g0.labels[g0.edges[19][1]])))
other_key=tuple(sorted((g0.labels[g0.edges[54][0]],g0.labels[g0.edges[54][1]])))
I=np.array([1.,0.,0.,0.])
def dist(q,target): return float(math.acos(float(np.clip(np.dot(q,target),-1,1))))
def random_small(delta):
 v=rng.normal(size=3);v/=np.linalg.norm(v);theta=rng.random()*delta
 return np.r_[math.cos(theta),math.sin(theta)*v]
def endpoints(g):
 V,E=len(g.labels),len(g.edges)
 res=[]
 for t in range(3):
  for e,(a,b) in enumerate(g.edges):res.append(((t,a),(t,b)))
 for t in range(3):
  for v in range(V):res.append(((t,v),((t+1)%3,v)))
 return res

def run():
 rows=[]
 for rad in [5.,6.5,8.,10.]:
  g,_=build(rad,0);W,meta=product_collar(g);V,E=len(g.labels),len(g.edges)
  Q=Q_from_seed(g,seed);R=set(range(len(W)))-Q
  H={e for f in Q for e,s in W[f]};K=shell(H,W,R)
  A={f for f in R if any(e in K for e,s in W[f])}
  halo={e for f in A for e,s in W[f] if e not in K}
  keymap={tuple(sorted((g.labels[a],g.labels[b]))):e for e,(a,b) in enumerate(g.edges)}
  e=keymap[special_key];e2=keymap[other_key]
  p=3*len(g.faces)+e; p2=3*len(g.faces)+e2
  assert p in R and p2 in R and e in K-H
  h_p={ed for ed,s in W[p] if ed in H};h_p2={ed for ed,s in W[p2] if ed in H}
  assert h_p==h_p2 and len(h_p)==1
  incident=[f for f in R if e in {ed for ed,s in W[f]}]
  assert len(incident)==4
  around={ed for f in incident for ed,s in W[f]};assert len(around)==13
  pair_external={ed for f in (p,p2) for ed,s in W[f] if ed not in H}
  assert len(pair_external)==6 and e in pair_external
  # random configurations on the entire lattice. Gauge-pure halo with small perturbations,
  # while K variables are left hot/Haar. Test by assigning pure gauge values on K.
  ends=endpoints(g);lam_vals=[1.,4.,30.,100.]
  tested=0;max_energy_ratio=0.;max_error=0.
  for lam in lam_vals:
   for it in range(3):
    pure_vert=unit_random(rng,3*V)
    gauge=np.array([qmul(pure_vert[3*0+u[0]*V+u[1]],qinv(pure_vert[v[0]*V+v[1]])) for u,v in ends])
    U=unit_random(rng,len(ends))
    eps=.25
    for f in halo:U[f]=qmul(random_small(eps/math.sqrt(lam)),gauge[f])
    Vtrial=U.copy()
    for f in K:Vtrial[f]=gauge[f]
    Sk=sum(1.-character_word(Vtrial,W[f]) for f in A)
    limit=8*eps*eps*len(A)/lam
    assert Sk<=limit+1e-8,('sK inequality violated',rad,lam,Sk,limit)
    max_energy_ratio=max(max_energy_ratio,Sk/limit)
    tested+=1
  # severe local defect: all links identity except the special exterior e=-I.
  U=np.tile(I,(3*(V+E),1));U[e]=-I
  f1=1.-character_word(U,W[p]);f2=1.-character_word(U,W[p2]);assert f1+f2==2.
  # Opposite staple argument proves S_H >=2 for EVERY change to the shared H link.
  # Directly audit full-action center flip: the only four incident plaquettes go flat.
  action_before=sum(1.-character_word(U,W[f]) for f in incident)
  Uflip=U.copy();Uflip[e]*=-1
  action_after=sum(1.-character_word(Uflip,W[f]) for f in incident)
  assert abs(action_before-8)<1e-10 and abs(action_after)<1e-10
  # Robust near -I defect with radius delta; all 12 other incident links near I.
  delta=.05;min_total=100.;min_flip=100.
  for it in range(80):
   U=np.tile(I,(3*(V+E),1))
   for f in around-{e}:U[f]=random_small(delta)
   U[e]=-random_small(delta)
   # center flip: full retained action decrease exact -2 sum cos
   cos=np.array([character_word(U,W[f]) for f in incident]);decrease=-2*cos.sum()
   assert decrease>=8*math.cos(4*delta)-1e-8
   min_flip=min(min_flip,decrease)
   # Pair energy lower bound with arbitrary shared H link; numerically sample it.
   hh=next(iter(h_p));old=U[hh].copy()
   for hval in unit_random(rng,30):
    U[hh]=hval
    total=(1.-character_word(U,W[p]))+(1.-character_word(U,W[p2]))
    assert total>=2-6*delta-1e-9,(rad,total)
    min_total=min(min_total,total)
   U[hh]=old
  rows.append({'radius':rad,'Q':len(Q),'H_links':len(H),'K_links':len(K),'A_K_faces':len(A),'halo_links':len(halo),
    'special_exterior_link_id':e,'special_z5_endpoints':[list(x) for x in special_key],
    'two_retained_temporal_face_ids':[p,p2],'shared_only_H_link':next(iter(h_p)),'pair_exterior_link_count':len(pair_external),
    'incident_retained_face_count':len(incident),'local_defect_link_neighborhood_count':len(around),
    'exact_center_defect_s_H_lower':2.0,'all_links_identity_except_e_center_flip_action_drop':action_before-action_after,
    'nearflat_epsilon':.25,'eta_per_Q':8*(.25**2)*len(A)/len(Q),
    'lambda_sK_bound':8*(.25**2)*len(A),'center_flip_delta':delta,
    'center_flip_gibbs_suppression_exponent':2*len(incident)*math.cos(4*delta),
    'certified_bad_class_sH_lower':2-6*delta,
    'max_observed_sK_over_bound':max_energy_ratio,'min_observed_center_flip_decrease':min_flip,
    'min_observed_retained_temporal_pair_energy':min_total,'checked_random_gauge_and_exterior_samples':tested})
  print('rad',rad,'H/K',len(H),len(K),'halo',len(halo),'pair',p,p2,'drop',action_before-action_after,'sK_fraction',max_energy_ratio,flush=True)
 assert all(x['H_links']==36 and x['K_links']==125 and x['A_K_faces']==175 and x['halo_links']==133 for x in rows)
 (ROOT/'certificate.json').write_text(json.dumps({'proof_scope':'gauge-covariant near-pure-gauge exterior halo condition on fixed 14-face Penrose support; unconditional exponential suppression for a specified 13-link obstruction event, NOT full s_H tail','geometry':rows,'analytical_joint_tail':'P(lambda s_H >=t and halo_good) <= min(1,exp(-t+8 epsilon^2 |A(K)|+|K|(1.5log(lambda)+log(4097)+2nu)))','full_probability_tail_obstruction':'P(lambda s_H>=t) <= joint_bound + P(halo_bad); halo_bad probability not controlled by these arguments'},indent=2))
if __name__=='__main__':run()
