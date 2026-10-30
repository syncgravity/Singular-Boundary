#!/usr/bin/env python3
"""Three-step cycle-breaking temporal support: group-valued Haar forest coordinates."""
from pathlib import Path
import json,numpy as np
from nested_audit import build,complex_3
from verify import haar,qm,inv,prod_word
R=Path(__file__).resolve().parent
# Choose a pivot spatial-time endpoint which occurs in exactly one selected temporal face
# for each spatial edge. This requires at least one of the three intervals to be retained.
CHOICES={
  (0,):{0:0}, (1,):{1:2}, (2,):{2:2},
  (0,1):{0:0,1:2}, (0,2):{0:1,2:2}, (1,2):{1:1,2:0},
}
def pivots_for(Qkeys,E):
    by_edge={}
    for t,e in Qkeys:by_edge.setdefault(e,set()).add(t)
    out={}
    for e,ss in by_edge.items():
        typ=tuple(sorted(ss)); assert typ in CHOICES,('full temporal cycle not covered',e,typ)
        for t,j in CHOICES[typ].items():out[(t,e)]=j*E+e
    assert len(out)==len(Qkeys)==len(set(out.values()))
    # Ensure every selected face contains its pivot but NO other selected pivot.
    for (t,e),p in out.items():
        for (s,f),q in out.items():
            if f==e and s!=t:
                assert q not in {t*E+e,((t+1)%3)*E+e}
    return out

def test(g,cols,keys,seed):
    V,E,F=len(g.labels),len(g.edges),len(g.faces)
    ps=pivots_for(keys,E)
    original=haar(3*(V+E));ys={key:prod_word(original,cols[3*F+key[0]*E+key[1]]) for key in ps}
    rec=original.copy()
    for (t,e),pivot in ps.items():
        u,v=g.edges[e];t1=(t+1)%3
        Tu=original[3*E+t*V+u];Tv=original[3*E+t*V+v];Y=ys[(t,e)]
        if pivot==t*E+e:
            rec[pivot]=qm(qm(qm(Y,Tu),original[t1*E+e]),inv(Tv))
        else:
            assert pivot==t1*E+e
            rec[pivot]=qm(qm(qm(inv(Tu),inv(Y)),original[t*E+e]),Tv)
    err=float(np.max(np.abs(rec-original)))
    yerr=max(float(np.linalg.norm(prod_word(rec,cols[3*F+t*E+e])-ys[t,e])) for t,e in keys)
    assert err<1e-12 and yerr<1e-12,(err,yerr)
    # A change in an individual inserted face coordinate modifies only its one spatial pivot.
    e0=sorted(ps)[len(ps)//2];pp=ps[e0]
    new=rec.copy();t,e=e0;u,v=g.edges[e];t1=(t+1)%3
    Tu=rec[3*E+t*V+u];Tv=rec[3*E+t*V+v];newY=haar(1)[0]
    if pp==t*E+e:new[pp]=qm(qm(qm(newY,Tu),rec[t1*E+e]),inv(Tv))
    else:new[pp]=qm(qm(qm(inv(Tu),inv(newY)),rec[t*E+e]),Tv)
    face_near={i for i,col in enumerate(cols) if pp in col}
    farerr=max((np.linalg.norm(prod_word(rec,col)-prod_word(new,col)) for i,col in enumerate(cols) if i not in face_near),default=0.)
    nexterr=float(np.linalg.norm(prod_word(new,cols[3*F+t*E+e])-newY))
    assert farerr<1e-12 and nexterr<1e-12,(farerr,nexterr)
    # Each spatial pivot belongs to <=2 retained spatial faces and <=1 retained temporal face.
    Qid={3*F+t*E+e for t,e in keys}
    retained_counts=[sum((pp in col) for i,col in enumerate(cols) if i not in Qid) for pp in ps.values()]
    assert max(retained_counts)<=3
    return {'support_size':len(keys),'distinct_pivots':len(ps),'max_retained_faces_per_pivot':max(retained_counts),'roundtrip_max_error':err,'holonomy_max_error':yerr,'far_face_change_error':float(farerr),'changed_holonomy_error':nexterr}

def main():
    out=[]
    for radius in (5.,8.,10.):
        g,_=build(radius,0);cols,meta=complex_3(g);E=len(g.edges)
        # Deterministic pseudo-random 2-of-3 and 1-of-3 choices, anchored in central edges.
        mid=np.argsort([np.linalg.norm((g.xy[u]+g.xy[v])/2) for u,v in g.edges])
        for k in [8,24,50,100] if radius==5. else [8,24,50,100,200]:
            keys=set()
            patterns=[(0,2),(1,2),(0,1),(0,),(1,),(2,)]
            for i,e in enumerate(mid[:k]):
                for t in patterns[i%6]:keys.add((t,int(e)))
            res=test(g,cols,keys,0);res.update({'radius':radius,'spatial_edges_selected':k})
            out.append(res)
    (R/'forest_certificate.json').write_text(json.dumps({'title':'General three-interval cycle-breaking Haar chart','restriction':'For each spatial edge e at least one of t=0,1,2 temporal faces must remain retained. No result for all-three temporal insertion cycle.', 'proof':'Each selected temporal face chooses a spatial-link leaf pivot belonging to no other selected face on that spatial edge. Change of variables is independent Haar translation or inversion. The table CHOICES provides a constructive certificate.', 'verified':out},indent=2))
    print('PASS',len(out),'three-step cycle-breaking supports; largest Q',max(x['support_size'] for x in out))
if __name__=='__main__':main()
