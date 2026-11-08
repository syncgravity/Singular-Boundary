#!/usr/bin/env python3
"""PF-I0: conditional diagonal quotient graph / odd-girth / Wilson trace.

This script is NOT a reproduction of Paper 2's generator, Ngrid=25 results,
Fibonacci hopping assignment, or Yang--Mills mass-gap data. All window/cutoff
parameters are illustrative and included in the output.

No external Python packages are required.
"""
from __future__ import annotations
import argparse
import cmath
import itertools
import json
import math
import random
from pathlib import Path

D = 4
E = tuple(tuple(int(i == j) for i in range(D)) for j in range(D)) + ((-1, -1, -1, -1),)
Z = (0, 0, 0, 0)

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def neg(a):
    return tuple(-x for x in a)

def shift(m):
    """C5 cyclic permutation of Z5 representatives, then m4=0 gauge."""
    a, b, c, d = m
    return (-d, a-d, b-d, c-d)

def power_shift(m, n):
    for _ in range(n):
        m = shift(m)
    return m

def z_k(m, k):
    return sum(m[j] * cmath.exp(2j * math.pi * k * j / 5) for j in range(4))

def in_regular_decagon(z, circumradius, orientation=0.0, tolerance=1e-10):
    """Regular decagon; orientation is angle of a vertex, not a source datum."""
    bound = circumradius * math.cos(math.pi / 10)
    for j in range(10):
        normal = cmath.exp(1j*(orientation + (j+.5)*math.pi/5))
        if (z * normal.conjugate()).real > bound+tolerance:
            return False
    return True

def accepted_patch(span, p_radius, w_radius, orientation):
    result = []
    for m in itertools.product(range(-span, span+1), repeat=4):
        if (abs(z_k(m, 1)) <= p_radius + 1e-10
                and in_regular_decagon(z_k(m, 2), w_radius, orientation)):
            result.append(m)
    return tuple(result)

def edges(vertices):
    V = set(vertices)
    return {tuple(sorted((m,add(m,v))))
            for m in vertices for v in E if add(m,v) in V}

def is_bipartite(vertices, edge_set):
    neighbours={v:set() for v in vertices}
    for u,v in edge_set:
        neighbours[u].add(v); neighbours[v].add(u)
    colors={}
    for start in vertices:
        if start in colors: continue
        colors[start]=0
        frontier=[start]
        for v in frontier:
            for u in neighbours[v]:
                if u in colors:
                    if colors[u]==colors[v]: return False
                else:
                    colors[u]=1-colors[v];frontier.append(u)
    return True

def pentagon_cycles(vertices):
    V = set(vertices)
    cycles = set()
    witness = None
    for m in vertices:
        for perm in itertools.permutations(E):
            path = [m]
            for v in perm:
                nxt = add(path[-1], v)
                if nxt not in V:
                    break
                path.append(nxt)
            if len(path)!=6 or path[-1]!=m:
                continue
            p = path[:-1]
            assert len(set(p))==5
            rev = list(reversed(p))
            variants = [tuple(q[k:]+q[:k]) for q in (p,rev) for k in range(5)]
            cycles.add(min(variants))
            if witness is None:
                witness = p
    return cycles, witness

def qmul(x,y):
    a,b,c,d=x; e,f,g,h=y
    return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)

def qinv(x):
    return (x[0],-x[1],-x[2],-x[3])

def qunit(v):
    n = math.sqrt(sum(x*x for x in v))
    return tuple(x/n for x in v)

def test_wilson_cycle(path):
    """A reproducible noncommuting SU2 gauge transform on a 5-link loop."""
    rng = random.Random(131017)
    g = {v: qunit(tuple(rng.uniform(-1,1) for _ in range(4))) for v in path}
    u = {tuple(sorted((path[j], path[(j+1)%5]))):
         qunit(tuple(rng.uniform(-1,1) for _ in range(4))) for j in range(5)}
    def oriented(a,b):
        v = u[tuple(sorted((a,b)))]
        return v if a<b else qinv(v)
    hol = (1.0,0.0,0.0,0.0)
    hol_new = (1.0,0.0,0.0,0.0)
    for j in range(5):
        a=path[j]; b=path[(j+1)%5]
        orig=oriented(a,b)
        transformed=qmul(qmul(g[a],orig),qinv(g[b]))
        hol=qmul(hol,orig)
        hol_new=qmul(hol_new,transformed)
    gauge_invariant=abs(hol[0]-hol_new[0])
    assert gauge_invariant < 2e-12
    assert abs(math.sqrt(sum(x*x for x in hol))-1)<2e-12
    return gauge_invariant, hol[0]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--span',type=int,default=6)
    parser.add_argument('--physical-radius',type=float,default=5.0)
    parser.add_argument('--window-radius',type=float,default=1.65)
    parser.add_argument('--window-orientation',type=float,default=0.0)
    parser.add_argument('--output',type=Path)
    a=parser.parse_args()
    assert a.span>=1 and a.physical_radius>0 and a.window_radius>0
    checks=0
    # Exact integer algebra and C5 representation. These do not depend on W.
    assert add(add(add(add(E[0],E[1]),E[2]),E[3]),E[4])==Z; checks+=1
    for m in itertools.product(range(-2,3),repeat=4):
        assert power_shift(m,5)==m; checks+=1
    for i,v in enumerate(E):
        assert shift(v)==E[(i+1)%5]; checks+=1
    # Exhaustive signed walks of lengths 1,3 (odd <5) in the full Cayley graph.
    S=E+tuple(neg(v) for v in E)
    for n in (1,3):
        for path in itertools.product(S, repeat=n):
            m=Z
            for v in path:m=add(m,v)
            assert m!=Z; checks+=1
    # All length-five closed walks must traverse the five directions once,
    # with one common sign. Test exact count of sequences: 2 * 5!.
    five_closed=0
    for word in itertools.product(range(10), repeat=5):
        m=Z
        for j in word:m=add(m,S[j])
        if m==Z:
            five_closed+=1
            assert set(word)==set(range(5)) or set(word)==set(range(5,10))
    assert five_closed==2*math.factorial(5); checks+=1
    # Cyclic action on unnormalized source Fourier coordinates.
    w=cmath.exp(2j*math.pi/5)
    for m in itertools.product(range(-1,2),repeat=4):
        assert abs(z_k(shift(m),1)-w*z_k(m,1))<1e-12
        assert abs(z_k(shift(m),2)-w*w*z_k(m,2))<1e-12
        checks+=2
    # Illustrative cut and its finite graph (NOT source parameter recovery).
    V=accepted_patch(a.span,a.physical_radius,a.window_radius,a.window_orientation)
    VV=set(V); e=edges(V)
    assert len(VV)==len(V);checks+=1
    assert all(shift(m) in VV for m in V);checks+=len(V)
    assert all(tuple(sorted((shift(u),shift(v)))) in e for u,v in e);checks+=len(e)
    cycles,witness=pentagon_cycles(V)
    assert witness is not None
    assert not is_bipartite(V,e);checks+=1
    for cyc in cycles:
        assert all(tuple(sorted((cyc[j],cyc[(j+1)%5]))) in e for j in range(5))
        checks+=1
    # Trace/U(1)-independent SU2 holonomy test on one genuinely 5-sided loop.
    gauge_error,wilson_halftrace=test_wilson_cycle(witness);checks+=2
    # C5-invariant geometry is not enough for C5-invariant family-only hopping.
    # Choose one edge of family 0. Rotation creates a family 1 edge.
    v0=E[0]; candidate=next((m for m in V if add(m,v0) in VV),None)
    assert candidate is not None
    rotated=shift(candidate)
    assert add(rotated,E[1]) in VV
    t0=(1+math.sqrt(5))/2
    t0=t0*t0
    t1=1.0
    assert t0!=t1;checks+=1
    # Weighted graph Laplacian identity L=D-A, exact by edge pairing.
    f={m:math.sin(sum((j+1)*m[j] for j in range(4))) for m in V}
    quadratic=sum((f[u]-f[v])**2 for u,v in e)
    direct=sum(f[m]*sum(f[m]-f[n] for j in range(5)
                          for s in (1,-1)
                          for n in [add(m,tuple(s*x for x in E[j]))] if n in VV) for m in V)
    assert abs(quadratic-direct)<1e-9;checks+=1
    report={
      'scope':'conditional quotient test; illustrative regular decagon, NOT Paper 2 source generator',
      'parameters':{'span':a.span,'physical_radius':a.physical_radius,
                    'window_radius':a.window_radius,'window_orientation_radians':a.window_orientation},
      'exact_invariants':{'quotient_rank':4,'relation':'sum(v_0,...,v_4)=0',
                          'shortest_possible_odd_cycle_length':5,
                          'five_step_closed_signed_words':five_closed,
                          'c5_order':5},
      'illustrative_graph':{'vertices':len(V),'edges':len(e),
                             'mean_degree':2*len(e)/len(V),'five_cycles':len(cycles),'bipartite':False,
                             'five_cycle_witness':[list(q) for q in witness]},
      'gauge_test':{'max_halftrace_difference':gauge_error,
                    'original_wilson_halftrace':wilson_halftrace},
      'hopping_test':{'family_0_weight':t0,'family_1_weight':t1,
                      'rotational_invariance_of_family_only_nonconstant_weights':False},
      'checks_passed':checks,
      'source_parameters_authenticated':False,
      'mass_gap_certified':False}
    doc=json.dumps(report,sort_keys=True,indent=2)+'\n'
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(doc)
    print(doc)

if __name__=='__main__':
    main()
