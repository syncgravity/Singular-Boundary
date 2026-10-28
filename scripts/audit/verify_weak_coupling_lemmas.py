#!/usr/bin/env python3
"""Deterministic rational audit of the R3-IR local Penrose reduction.

Only coefficient/graph accounting is computed; SU(2) Haar orthogonality
and spectral statements are proved in the accompanying mathematical note.
No Monte Carlo, mass fitting, or replacement historical outputs.
"""
from collections import Counter
from fractions import Fraction as Q
import json

def verify(faces, electric, magnetic, a_star):
    assert faces and all(len(f)==4 and len(set(f))==4 for f in faces)
    edges=set(electric)
    assert edges==set().union(*(set(f) for f in faces))
    assert len(magnetic)==len(faces) and all(b>=0 for b in magnetic)
    assert all(a>=a_star>0 for a in electric.values())
    d=Counter(e for f in faces for e in f)
    assert all(1<=d[e]<=2 for e in edges)
    # Exactly split each electric edge among its incident plaquettes.
    h=[{e:electric[e]/d[e] for e in f} for f in faces]
    for e in edges:
        assert sum((hf.get(e,Q(0)) for hf in h),Q(0))==electric[e]
    local=[Q(3,4)*min(hf.values()) for hf in h]
    assert min(local)>=Q(3,8)*a_star
    adjacency=[sum(bool(set(f)&set(g)) for j,g in enumerate(faces) if i!=j)
               for i,f in enumerate(faces)]
    assert max(adjacency)<=4
    kappas=[Q(3,4)*sum(electric[e] for e in f) for f in faces]
    # First two exactly known coefficients from the SU(2) Haar theorem.
    eprime=sum(magnetic,Q(0))
    e2=-sum((b*b/(4*k) for b,k in zip(magnetic,kappas)),Q(0))
    tangent=sum((b*b/(4*k*k) for b,k in zip(magnetic,kappas)),Q(0))
    return dict(edges=len(edges),faces=len(faces),max_neighbor_degree=max(adjacency),
                edge_degrees=dict(sorted(d.items())),
                local_gap_bound=str(min(local)),
                full_electric_gap_bound=str(Q(3,4)*min(electric.values())),
                kappa=[str(k) for k in kappas], E_first=str(eprime),
                E_second_coefficient=str(e2),vacuum_tangent_norm2=str(tangent))

if __name__=="__main__":
    # A formal two-plaquette shared-link incidence fixture, NOT a historical
    # reconstruction or a simulation.
    faces=[("e0","e1","e2","e3"),("e3","e4","e5","e6")]
    a={f"e{i}":Q(1) for i in range(7)}
    out=verify(faces,a,[Q(1),Q(1)],Q(1))
    assert out["local_gap_bound"]=="3/8"
    assert out["full_electric_gap_bound"]=="3/4"
    assert out["E_first"]=="2"
    assert out["E_second_coefficient"]=="-1/6"
    assert out["vacuum_tangent_norm2"]=="1/18"
    assert out["kappa"]==["3","3"]
    print(json.dumps({"result":out,
          "activity_bound":"||T_I(t)|| <= (2e t beta)^|I| if t beta <= 1",
          "beta_bound":"(16/3)(b_star/a_star)",
          "uniform_interacting_gap_proved":False},indent=2))
