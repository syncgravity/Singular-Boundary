# PF-I16 canonical insertion-order matching audit — 2026-11-16

## Purpose

The connected-tree witness lemma gives at least two guarded local choices at
each insertion for any parent-before-child order. The next question was whether
one or a small fixed family of canonical orders suffices to give an injective
source-to-tree assignment, avoiding the full all-orders neighborhood.

This audit tests that restricted proposal. It does not alter the full guarded
switch relation or the full coordinatewise relation.

## Restricted constructions tested

For each source \(x=(M,\tau)\):

1. Root \(\tau\) at the interval containing port 1.
2. Choose one of a fixed family of parent-before-child insertion orders.
3. At each insertion, take the first eligible edge on the connected-tree
   witness path (excluding an edge contained strictly inside the new interval).
4. Branch over all guarded local patterns for that selected edge.
5. Encode the resulting port trees and run a deterministic lexicographic
   augmenting-path assignment over the source neighborhoods.

The eight tested order templates are BFS ascending, BFS descending, DFS
ascending, DFS descending, and four Kahn topological orders prioritized by
interval endpoints or interval length. Every generated edge replacement is
guarded, and every resulting tree has cut load bounded by its source.

## Exact results

| Ports | Sources | Candidate target union | Source degree range | Matched | Result |
|---:|---:|---:|---:|---:|---|
| 4 | 2 | 3 | 2–3 | 2 | saturated |
| 6 | 22 | 32 | 4–12 | 22 | saturated |
| 8 | 608 | 679 | 8–54 | 525 | Hall deficit 83 |

At eight ports, alternating reachability from the unmatched sources gives an
explicit Hall-deficient set \(S\):
\[
|S|=342,\qquad |N(S)|=259,\qquad |S|-|N(S)|=83.
\]
A source in the witness set is
\[
M=((1,4),(2,6),(3,7),(5,8)),\quad
\tau=((0,1),(0,2),(1,3)),
\]
using the verifier's zero-based interval indices for \(\tau\).

For comparison, the single BFS-ascending order matched only 493 of 608
sources. The first three templates improved this to 522, and the eight
templates improved it to 525, but neither is sufficient.

## Interpretation

This is a genuine Hall obstruction for the tested *restricted subrelation*.
It is **not** a Hall obstruction for the full guarded switch relation:
the separate exact full-neighborhood verifier still finds a source-saturating
matching at eight ports (608 of 608).

The result rules out the proposed shortcut “choose one of these fixed
canonical insertion orders, then only use the witness edge at each step.”
It does not rule out:
- a source-dependent or matching-dependent insertion order;
- choosing among several eligible witness-path edges;
- alternating-path reassignment that can move a source between different
  insertion histories;
- an all-orders structural induction.

The local two-choice witness lemma is therefore only a per-source branching
bound. It does not provide the cross-source Hall expansion needed for an
injective assignment.

## Scope

The ten-port source-object count is 31,744, but the ten-port candidate
neighborhood/matching test was not run: the eight-port restricted relation
already fails. No ten-port result is claimed here.

No all-orders weighted one-link inequality or Yang–Mills mass-gap conclusion
follows from these finite tests.

## Reproduction

Verifier:
`research/verification/verify_pf_i16_fixed_order_inductive_candidate.py`

The GitHub Actions run completed successfully with the Hall deficit reported as
an expected diagnostic (rather than causing CI to fail):
- Run: https://github.com/syncgravity/Singular-Boundary/actions/runs/43972795747
- Commit: `15a437a3889ec79d74ad85bbd083fdde368896d5`
- Full guarded-neighborhood enumeration and full-relation injective assignment
  also passed in the same run at n=4,6,8.

The eight-order verifier's final exact output at n=8 was 525 matched of 608,
with alternating Hall witness sizes 342 and 259 (deficit 83).
