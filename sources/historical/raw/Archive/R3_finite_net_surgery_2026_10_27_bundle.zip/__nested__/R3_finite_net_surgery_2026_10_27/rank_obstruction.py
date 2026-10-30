#!/usr/bin/env python3
"""Independent exact GF(p) relative exterior curvature constraints for nested Q14 collars."""
import json
from pathlib import Path
from construct_surgery import product_collar,shell
from direct_cut_project import build
from cavity_audit import seed_support,Q_from_seed
ROOT=Path(__file__).resolve().parent

def sparse_rank(columns, allow=None, prime=1000003):
    allowed=None if allow is None else set(allow);basis={}
    for word in columns:
        v={e:(sgn%prime) for e,sgn in word if allowed is None or e in allowed}
        while v:
            pivot=min(v)
            if pivot not in basis:
                scale=pow(v[pivot],-1,prime)
                basis[pivot]={e:(a*scale)%prime for e,a in v.items()}
                break
            t=v[pivot]
            for e,a in basis[pivot].items():
                val=(v.get(e,0)-t*a)%prime
                if val:v[e]=val
                else:v.pop(e,None)
    return len(basis)

def main():
    seed=seed_support(build(5.,0)[0]);rows=[]
    for radius in (5.,6.5,8.,10.):
        g,_=build(radius,0);faces,_=product_collar(g);Q=Q_from_seed(g,seed);R=set(range(len(faces)))-Q
        H={e for p in Q for e,s in faces[p]}
        for j in range(3):
            A={p for p in R if any(e in H for e,s in faces[p])}
            columns=[faces[p] for p in sorted(A)]
            result=[]
            for mod in [1000003,1000033]:
                r_all=sparse_rank(columns,None,mod)
                r_local=sparse_rank(columns,H,mod)
                result.append((r_all,r_local))
            assert result[0]==result[1]
            allrank,localrank=result[0]
            rows.append({'radius':radius,'shell':j,'adjustable_links':len(H),'affected_retained_faces':len(A),
                         'full_incidence_rank':allrank,'local_incidence_rank':localrank,
                         'relative_exterior_rank':allrank-localrank})
            H=shell(H,faces,R)
    (ROOT/'rank_certificate.json').write_text(json.dumps({'source':'Direct Z5 Penrose spacetime exact signed face-to-link incidence, Q14 retained cavity','method':'independent modular elimination with two primes','rows':rows,'interpretation':'positive exterior rank precludes universal flat completion with every outside link fixed; does not preclude averaged Gibbs suppression'},indent=2))
    for r in rows:print(r['radius'],r['shell'],r['adjustable_links'],r['relative_exterior_rank'])
if __name__=='__main__':main()
