# PF-I16 — Revised hierarchy: L6c coarse support naturality

Date: 18 November 2026  
Branch: research/pf-i16-z5-incidence-lift-2026-11-18  
Scope: Ngrid=7 PF-I16 original-source replay and PF-I11 completed-window core; all n=6 Hall sources and all eligible marks; their n=4 parents.

## 1. Revised hierarchy

The old L6 demanded equality of the retained port-to-edge labels after parent deletion. That condition fails for the frozen rank-indexed edge assignment, including the explicit two-mark/same-parent obstruction.

We retain L1-L5 and replace that strong L6 with L6c:

- L1: port injectivity.
- L2: each child matched pair is still represented by one actual signed elementary basis edge.
- L3: strict accepted-vertex and accepted-face realization.
- L4: connected face-supported interval supports with ordered lower-to-upper child trace.
- L5: exact full interval-overlap incidence, with explicit typed witnesses and disjoint supports for non-overlapping pairs.
- L6c: parent naturality of the retained support diagram up to simple-homotopy equivalence, not equality of individual matched-edge labels.
- L7: global port-order and interval-boundary-order compatibility remains separate.
- L8: construction independence and all-orders formulation remain separate.

The relaxation is deliberately narrow: it forgets the identity and dimension of a particular shared cell, but preserves which intersections are empty or nonempty, and requires every nonempty intersection and every retained support to be contractible in the tested finite case.

For a retained interval family indexed by R, define its intersection diagram by all subfamily intersections
K_S = intersection over i in S of K_i, for nonempty S subset R, recording emptiness and simple-homotopy type. L6c requires the child restricted diagram and parent diagram to agree in this coarse category. The union must also have the same simple-homotopy type. For the present n=6 to n=4 test there are two retained intervals, so singleton supports, their pair intersection, and their union exhaust the diagram.

Deletion compatibility is relative: the child union must collapse onto the union of the retained child supports by elementary free-face pairs, without deleting any cell belonging to a retained support. Shared cells are retained, not deleted with the marked interval.

Parent coherence is checked for every parent source reached through multiple marked projections. All incoming child restrictions must have the same coarse diagram class as the parent, rather than receiving arbitrary mark-dependent parent assignments.

## 2. Finite test protocol

The child support assignments are exactly those frozen by the L4-L5 verifier. The target-side face labels are not changed. For each of the 30 eligible order-six marked projections:

1. Restrict the child's support family by deleting the marked interval index.
2. Compute the full cellular subcomplex of each retained support and every intersection.
3. Verify each retained support collapses to an edge.
4. Verify every required nonempty pair intersection collapses to a vertex; non-overlapping pairs remain empty.
5. Verify the retained union collapses to a vertex.
6. Compute the parent support family from the parent full-overlap graph, and compare the coarse intersection-diagram signatures.
7. Collapse the full child union onto the retained child union using only free face-edge and free edge-vertex pairs.
8. Group all marked projections by exact parent matching/tree structure and check coherence across every incoming projection.

No Hall demand, deficiency, flow, congestion, matching output, or observer phase is used.

## 3. Results

Both target domains give the same result:

| Test | PF-I16 source replay | PF-I11 completed core |
|---|---:|---:|
| Eligible marked projections | 30/30 | 30/30 |
| Relative deletion collapses | 30/30 | 30/30 |
| Coarse child-parent diagram comparisons | 30/30 | 30/30 |
| Parent coherence groups | 2/2 | 2/2 |

There are two distinct parent matching/tree structures, each reached by 15 marked projections. Within each parent group, every incoming child restriction has the same coarse diagram signature as the parent.

The retained pair intersections have the following cell-level witnesses before forgetting their exact type:

| Intersection type | Marked projections |
|---|---:|
| Shared face | 26 |
| Shared edge/path | 2 |
| Shared vertex | 2 |

All 30 are nonempty and contractible, as is the parent intersection. The witness dimension is therefore not invariant under deletion; the intersection's coarse homotopy type is.

Relative deletion collapses use the following total elementary pairs:

- 34 face-edge pairs;
- 46 edge-vertex pairs;
- 80 pairs total across 30 marked projections.

The per-projection collapse-length histogram is:

| Elementary pairs | Projections |
|---:|---:|
| 2 | 24 |
| 3 | 2 |
| 6 | 2 |
| 7 | 2 |

No retained cell is removed. The maximum relative collapse length is seven pairs.

## 4. Explicit two-mark coherence witness

Use the six-port source

M = {[1,4], [2,5], [3,6]}, with tree {I1-I2, I1-I3}.

Deleting I2 gives the same four-port parent matching {[1,3], [2,4]} and tree with one edge. The retained child supports are:

- retained I1: faces (m;0,2) and (m;0,4);
- retained I3: faces (m;0,2) and (m;2,3).

Deleting I3 gives exactly the same parent matching/tree. The retained child supports are:

- retained I1: faces (m;0,2) and (m;0,4);
- retained I2: faces (m;0,4) and (m;3,4).

Here m=(0,1,0,0,0). In both cases, the two retained supports are collapsible disks and their intersection is one accepted rhombus. The parent support diagram is also two collapsible disks intersecting in one accepted rhombus.

Thus the two projections disagree on which specific target rhombus is shared, but agree on the coarse support diagram. This is precisely the distinction L6c is intended to preserve.

## 5. Interpretation and limitations

**Finite L6c verdict: pass** for all 30 eligible n=6 marked projections in both Ngrid=7 target domains.

This result is stronger than merely checking that the retained overlap graph is unchanged: it includes explicit relative free-cell collapses of the child union onto the retained child union, contractibility of each retained support and each nonempty intersection, comparison with the parent support diagram, and coherence across both parent structures.

The result does not establish a literal cellular map that preserves every original face label. It intentionally does not preserve individual matched-edge identities across deletion. It also does not yet establish L6c for parent orders above n=4, or for larger interval families with nontrivial triple and higher intersections.

The verifier is research/scripts/verify_pf_i16_hall_l6c_coarse_support_naturality.py. It imports the frozen L4-L5 support constructor and the two target builders, and includes exact relative-collapse certificates in its output.

Execution provenance: the finite n=6 source enumeration, support-diagram checks, and relative-collapse calculations were independently executed in the analysis environment in this session. The new repository verifier has been committed and inspected, but has not been executed from a cloned repository checkout here. The repository script is a reproducible replay artifact, not a claimed checkout-run.

## 6. Next step

Proceed to L7 without changing the frozen L1-L5 data or the L6c support equivalence. Test global port-order and interval-boundary-order compatibility separately in each target domain. Any proposed relaxation must be stated before the test; do not silently permute port labels, reverse an oriented child trace, or fit observer phases to repair an ordering failure.
