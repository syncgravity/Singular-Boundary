# PF-I16 global alternating-path rerouting diagnostic

Date: 2026-11-16

## Purpose

The same-parent-fiber admissible-exchange graph is disconnected at n=8, so a
collision cannot generally be repaired by a sequence of single-edge exchanges
that stays inside one parent source's output neighborhood.

This verifier instead uses the full leaf-last child-source -> port-tree
relation. Fix a deterministic source-saturating matching. Contract each
occupied target to its current owner. For every source x, an edge to a target
currently owned by y becomes a directed alternating arc x -> y. A target not
used by the matching is a free endpoint.

For a shared child target T and a pair of child sources in one parent fiber,
let y be the current owner of T. If y has an alternating path
y=y_0 -> y_1 -> ... -> y_r to a source y_r with a free candidate target F,
then shifting y_i to the target formerly assigned to y_{i+1}, and y_r to F,
frees T. One of the colliding child sources can then be assigned T. This is a
valid local reassignment of the finite matching; it does not by itself give a
simultaneous all-collisions or all-orders construction.

## Exact finite results

Verifier:
`research/verification/verify_pf_i16_global_alternating_cycles.py`

CI workflow:
`.github/workflows/pf-i16-global-alternating-cycles.yml`

Successful GitHub Actions run: 43982033946
Run URL: https://github.com/syncgravity/Singular-Boundary/actions/runs/43982033946
Verifier commit: b297266c0489c7e5fcf904c177bff85e1a62605d

| Ports n | Sources | Target union | Matching | Same-fiber collision pairs | Distinct-projection pairs | Reroutable pairs | Reroutes whose path meets another parent fiber |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 3 | 2/2 | 2 | 0 | 0 | 0 |
| 6 | 22 | 43 | 22/22 | 223 | 48 | 48 | 16 |
| 8 | 608 | 1,493 | 608/608 | 41,848 | 9,943 | 9,943 | 6,199 |

Additional n=8 diagnostics:
- All 608 sources can reach a free target by an alternating path in the
  selected matching.
- Maximum shortest reroute path length is 2 source-to-source arcs.
- 6,587 of the 9,943 distinct-projection collision pairs have their shared
  target currently owned by a source outside the colliding pair.
- A concrete cross-fiber example is printed by the verifier, including the
  colliding parent source, shared target, source pair, alternating source
  path, and parent fibers along that path.

At n=6, all 48 distinct-projection collision pairs are reroutable; 16 use a
path meeting another parent fiber. At n=8, all 9,943 are reroutable in the
chosen finite matching; 6,199 use another parent fiber.

## Interpretation and limitations

This is evidence that the failed within-fiber connectivity condition was too
restrictive. The full child relation has enough alternating-path flexibility
to reroute every tested distinct-projection collision pair, and most n=8
reroutes use a source outside the colliding parent fiber.

However:
1. The matching is a finite, deterministic Hopcroft-Karp matching, not a
   recursively defined assignment valid for arbitrary n.
2. Pairwise reroutability does not prove that all collisions can be repaired
   simultaneously while preserving previously imposed assignments or a
   prescribed parent-target capacity profile.
3. The finite results do not establish the coordinatewise down-set Hall
   inequalities for arbitrary n.
4. No all-orders weighted one-link inequality or Yang-Mills mass-gap theorem
   is claimed.

The next proof obligation is a global exchange theorem with a monotone
potential or a capacitated flow invariant that makes successive alternating
reroutes compatible. In particular, it must control how often a parent
projection (parent source, parent target) may be used, rather than forbidding
repeated parent projections.
