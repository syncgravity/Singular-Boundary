# PF-I16 — L7b oriented boundary-order test

Date: 18 November 2026  
Branch: research/pf-i16-z5-incidence-lift-2026-11-18  
Scope: frozen L1-L5 support family; PF-I16 original-source replay and PF-I11 completed-window core at Ngrid=7; all 22 order-six Hall sources and all 30 eligible marked projections to order-four parents.

## 1. Test definition

L7b asks whether the cyclic order of retained overlap footprints on each interval's oriented support boundary is compatible with parent deletion.

No target-wide linear order is introduced. Each support boundary is oriented from its distinguished lower-port image to its upper-port image. Its directed matched edge is the marked edge of the boundary circle.

For each retained interval, the test records the pairwise support-intersection footprint on that interval's boundary. It compares the footprint's relative position to the distinguished directed edge before and after deletion.

The necessary relative-position classes are:

- `contains_marked_edge`;
- `both_endpoints_without_marked_edge`;
- `tail_endpoint_only`;
- `head_endpoint_only`;
- `open_complementary_arc`;
- `empty`.

These classes are invariant under orientation-preserving boundary equivalence that preserves the distinguished directed edge and its ordered endpoints. Subdivision and collapse may change the number of boundary edges and the dimension of the shared footprint, but cannot move a footprint across the marked edge or change whether it contains the marked edge or one of its endpoints.

This is deliberately a **necessary-condition test**. A mismatch disproves L7b for the frozen support family under the adopted relative convention. A match does not by itself prove complete ordered boundary-word equivalence.

## 2. Results

Both target domains give identical results:

| Test | PF-I16 original-source replay | PF-I11 completed-window core |
|---|---:|---:|
| Eligible marked projections checked | 30 | 30 |
| Retained-interval comparisons | 60 | 60 |
| Relative-position mismatches | 28 | 28 |
| Projections failing the necessary test | 14 | 14 |
| Projections passing the necessary test | 16 | 16 |
| Parent coherence groups | 2 | 2 |

The 14 failing projections split as follows:

| Child full-overlap graph | Deleted interval index (zero-based) | Failing projections |
|---|---:|---:|
| Path: (0,1),(1,2) | — | 0 |
| Star: (0,1),(0,2) | 1 | 2 |
| Triangle: (0,1),(0,2),(1,2) | 1 | 12 |

All failures occur when the middle sorted interval I2 is deleted from a star or triangle full-overlap graph. Deleting I3 in those same graph patterns passes this necessary test. The path cases pass.

The two parent structures each have 15 incoming marked projections. In each group, the parent ordered-position word is fixed, while the child-restricted words have three distinct forms; seven of the 15 incoming restrictions disagree with the parent word. Thus parent coherence also fails under L7b.

## 3. First explicit obstruction

Take the source matching M = {[1,4], [2,5], [3,6]} and tree edges {(I1,I2), (I1,I3)}. The full overlap graph is a triangle. Delete I2 = [2,5]. The parent is {[1,3], [2,4]}, with retained child intervals I1 and I3 mapping in order to parent intervals 1 and 2.

Write m = (0,1,0,0,0). The child supports are:

- child I1: (m;0,2), (m;0,4);
- child I3: (m;0,2), (m;2,3).

The parent supports are:

- parent interval 1: (m;0,2), (m;0,4);
- parent interval 2: (m;0,4), (m;3,4).

The retained child supports intersect in face (m;0,2); the parent supports intersect in face (m;0,4). This is permitted by L6c, which forgets the identity of the shared face. L7b detects where those faces lie relative to the marked boundary edge.

### Retained interval 1

Its oriented boundary cycle, starting with its distinguished directed edge, is:

`01000 -> 01001 -> 11001 -> 11000 -> 11100 -> 01100 -> 01000`

Each five-digit string denotes its five coordinates.

- Child restriction: shared face (m;0,2) meets boundary edges at positions {3,4,5}, and boundary vertices at positions {0,3,4,5}. It touches the tail endpoint only; it does **not** contain the distinguished edge.
- Parent: shared face (m;0,4) meets boundary edges at positions {0,1,2}, and vertices at positions {0,1,2,3}. It contains the distinguished directed edge and both endpoints.

Thus the relative classes are `tail_endpoint_only` versus `contains_marked_edge`.

### Retained child interval 3, becoming parent interval 2

- Child restriction: boundary-edge positions {3,4,5}, vertices {0,3,4,5}; it touches the tail endpoint only.
- Parent restriction: boundary-edge positions {2,3,4}, vertices {2,3,4,5}; it lies in the open complementary arc and touches neither endpoint.

Thus the relative classes are `tail_endpoint_only` versus `open_complementary_arc`.

Neither mismatch can be repaired by an orientation-preserving subdivision or collapse that preserves the distinguished directed matched edge and its ordered endpoints. Doing so would require moving the footprint across the marked edge or changing its incidence with a marked endpoint.

This is not the old strict-L6 edge-label obstruction: L6c remains satisfied. It is a separate ordering obstruction.

## 4. Interpretation

**L7b necessary-condition verdict: fail for the frozen L4-L5 support family.**

The failure is not a counterexample to Hall's theorem, and it does not prove that no alternative support assignment can satisfy L7b. It shows that the current lexicographically selected support family cannot be extended to a parent-natural oriented boundary lift while preserving the marked lower-to-upper edge in the stated sense.

The 16 projections that pass the necessary position test remain unproved at the full boundary-word level. They should not be described as L7b passes.

Both target domains produce the same boundary cycles and footprint positions because the supports used in the test lie in the common accepted face population. The target complexes remain separate: PF-I16 has 1,550 vertices, 3,017 edges, and 1,468 faces; PF-I11 has 1,432 vertices, 2,761 edges, and 1,330 faces.

## 5. Reproducibility and provenance

Verifier: `research/scripts/verify_pf_i16_hall_l7b_boundary_order.py`.

It imports the frozen L4-L5 support constructor, the two target builders, and the Hall source exporter. It checks all 30 marked projections in each target, emits the oriented boundary cycles and footprint positions, compares target-domain outputs, and records parent-group coherence.

Execution provenance: the 30-projection boundary-cycle and relative-position calculations were independently executed in the analysis environment in this session using the exact frozen support assignments and the source-record enumeration. The repository verifier has been committed and inspected but has not been run from a cloned repository checkout in this session. Do not represent it as a checkout-run.

## 6. Consequence and next step

Do not weaken L7b after seeing this failure, and do not repair it by reversing a trace, permuting interval indices, or fitting a target axis.

The next mathematically legitimate step is to search the already-defined finite L4-L5 support candidate sets for a **single globally coherent alternative support assignment** that satisfies all 30 L6c parent projections and the L7b relative boundary-order condition simultaneously. The search objective and admissibility conditions must be fixed before selection; no Hall demands, flows, or deficiencies may be used to choose the supports.

If no assignment exists in the bounded one-/two-rhombus candidate family, record that as a bounded-lift impossibility result, not as a Hall counterexample. If one exists, freeze it and rerun L4, L5, L6c, and L7b in both target domains.
