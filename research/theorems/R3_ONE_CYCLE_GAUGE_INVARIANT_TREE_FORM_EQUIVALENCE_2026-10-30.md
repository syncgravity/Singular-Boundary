# R3-IR-534 — Gauge-invariant single-cycle cancellation of rooted-tree principal-form differences (2026-10-30)

**Correction to interpretation of R3-IR-532/533:** Those examples establish different principal coefficients for generic link-coordinate covectors, but their displayed covectors were not gradients of gauge-invariant functions. On a single SU(2) triangle, the apparent transport-tree distinction disappears on ALL smooth gauge-invariant functions.

Let triangle a:0→1, b:1→2, c:2→0, root vertex 0, with W=abc and p=(1/2)Tr(W). Let D_j=Ad(V_j)X_j, with X_j the source-left invariant link derivative (normalization X p=-vector/2). For tree T1={a,b}: V_a=1,V_b=a,V_c=ab. For tree T2={a,c}: V_a=1,V_b=a,V_c=c^-1. For p, direct quaternion differentiation and conjugation invariance give

D_a p=D_b p=D_c p= - (1/2) vec(W)

for **both trees**. The nontrivial c-edge identity follows from the fact that Ad(W^-1) vec(W)=vec(W). Since any smooth gauge-invariant function on a connected graph with first Betti number one is a smooth class function F(W)=f((1/2)Tr W) (with endpoint regularity), all its transported gradients are f'(p) D_j p. Hence the entire real SPD mixed quadratic form Q_T[F]=Σ_(ij) K_ij (D_i F)·(D_j F) is identical for the two trees on the gauge-invariant sector. The same equality extends by form density to gauge-invariant Sobolev states on this finite graph; the restricted Friedrichs forms and operators agree. This is an explicit operator-level **equivalence on the physical one-cycle sector**, not merely a numerical agreement for one observable. The conclusion assumes the same orientation and source derivative convention for both operators, and a fixed real K in their common edge labeling.

Monte Carlo quaternion test: 100 independent seeded SU2 link configurations; gauge invariance under arbitrary three-vertex transformations checked, and the maximum observed |Q_T1-Q_T2| for the Wilson-loop character was below 6e-16 (finite-difference derivatives h=1e-6). This is computational corroboration; the group argument above is the proof.

The graph has just ONE independent cycle. A multi-cycle graph may have distinct rooted-form actions on gauge-invariant Wilson observables; the actual M5 disk has 30-20+1=11 cycles. The result does NOT settle gauge-invariant equivalence there, nor actual refinement scaling, shrinking-center-cap control or continuum Yang-Mills gap. In particular, the generic-covector discrepancy R3-IR-533 must NOT be cited as gauge-invariant physical inequivalence.

Reproducer: research/scripts/validate_tree_gauge_wilson.py.
