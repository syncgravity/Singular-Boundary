#!/usr/bin/env python3
"""Read-only, exact rational SU(2) Wilson-source identity fixtures.
No simulation, random data, gauge-field sampling, or historical result regeneration.
Trace formula uses U(q)=q0 I + i(qx sigma_x+qy sigma_y+qz sigma_z).
"""
from fractions import Fraction as Q
from itertools import combinations, product
import json

zero=Q(0)
def vdot(u,v):return sum((a*b for a,b in zip(u,v)),zero)
def cross(u,v):return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def qmul(q,r):
    a,u=q[0],q[1:];b,v=r[0],r[1:];c=cross(u,v)
    return (a*b-vdot(u,v),)*(1)+tuple(a*y+b*x-z for x,y,z in zip(u,v,c))
def inv(q):return (q[0],)+tuple(-x for x in q[1:])
def trace(q):return 2*q[0]
def gram3(qs):
    s=[q[0] for q in qs]
    d={(i,j):vdot(qs[i][1:],qs[j][1:]) for i,j in combinations(range(len(qs)),2)}
    t={(i,j,k):vdot(cross(qs[i][1:],qs[j][1:]),qs[k][1:]) for i,j,k in combinations(range(len(qs)),3)}
    return s,d,t

def main():
    I=(Q(1),zero,zero,zero)
    X=(zero,Q(1),zero,zero)
    Y=(zero,zero,Q(1),zero)
    Z=(zero,zero,zero,Q(1))
    MZ=inv(Z)
    H=(Q(3,5),Q(4,5),zero,zero)
    K=(Q(5,13),zero,Q(12,13),zero)
    S=[I,X,Y,Z,MZ,H,K,inv(H)]
    assert all(sum(x*x for x in q)==1 for q in S)
    n=0
    for a,b in product(S,repeat=2):
        assert trace(a)*trace(b)==trace(qmul(a,b))+trace(qmul(a,inv(b)))
        assert qmul(a,inv(a))==I
        n+=1
    t=0
    for a,b,c in product(S,repeat=3):
        si,sj,sk=a[0],b[0],c[0]
        u,v,w=a[1:],b[1:],c[1:]
        formula=2*(si*sj*sk-si*vdot(v,w)-sj*vdot(u,w)-sk*vdot(u,v)+vdot(cross(u,v),w))
        assert trace(qmul(qmul(a,b),c))==formula
        t+=1
    # Pair traces fail to determine orientation of three adjoint vectors
    S1=[X,Y,Z];S2=[X,Y,MZ]
    one1,two1,tri1=gram3(S1);one2,two2,tri2=gram3(S2)
    assert one1==one2 and two1==two2 and tri1!=tri2
    assert trace(qmul(qmul(X,Y),Z))==2
    assert trace(qmul(qmul(X,Y),MZ))==-2
    # Elementary face-only traces miss a mixed closed path
    assert trace(Z)==trace(X)==0
    assert trace(qmul(Z,Z))==-2 and trace(qmul(Z,X))==0
    # Graph fixture: two square faces sharing an edge -> cyclomatic rank 2
    v,e=6,7;r=e-v+1
    assert r==2
    n3=r + r*(r-1)//2 + r*(r-1)*(r-2)//6
    result={'suite':'exact rational SU(2) quaternion traces',
        'pair_trace_product_identity_cases':n,
        'triple_trace_formula_cases':t,
        'handedness_witness_traces':[str(trace(qmul(qmul(X,Y),Z))),str(trace(qmul(qmul(X,Y),MZ)))],
        'two_face_mixed_word_witness_traces':[str(trace(qmul(Z,Z))),str(trace(qmul(Z,X)))],
        'two_face_cycle_rank':r,'two_face_generating_trace_coordinates':n3,
        'checks_passed':True,'simulations_run':False,'full_interacting_gap_proved':False}
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
