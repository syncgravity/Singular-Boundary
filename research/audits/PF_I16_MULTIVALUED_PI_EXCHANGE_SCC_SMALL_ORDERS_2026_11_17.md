# PF-I16 multivalued-pi exchange SCC census: n=4,6,8

Date: 2026-11-17

Verifier: `research/verification/verify_pf_i16_multivalued_pi_exchange_scc_small.py`

Workflow: [44049609042](https://github.com/syncgravity/Singular-Boundary/actions/runs/44049609042)

## Exact results

The verifier reconstructs the multivalued-pi relation (all non-root leaves per source, canonical leaf-last parent neighborhood), computes a left-saturating matching, and runs an exact matching-relative SCC census.

| n | sources | distinct parent sources | incidences | targets | matching | SCCs | sink SCCs | sink size | free neighbors of sink |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 1 | 5 | 3 | 2/2 | 1 | 1 | 2 | 1 |
| 6 | 22 | 2 | 241 | 43 | 22/22 | 2 | 1 | 4 | 5 |
| 8 | 608 | 22 | 38,208 | 1,493 | 608/608 | 4 | 1 | 8 | 19 |

No zero-free sink SCC occurs at any tested order. By the exact matching-relative slack identity, these finite graphs have strict Hall expansion:
[
|N(A)|ge |A|+1
qquad	ext{for every nonempty source set }A.
]
In particular every individual incidence is exchangeable into some left-saturating matching.

The condensation data are:
- n=4: one SCC of size 2, already the unique sink.
- n=6: SCC sizes 18 and 4, with the size-18 component pointing to the size-4 sink.
- n=8: SCC sizes 528, 36, 36, and 8; the size-528 component points to all three smaller components, and each size-36 component points to the size-8 sink.

The unique sink SCC sizes 2,4,8 suggest the conjectural pattern (2^{s-1}) for n=2s. This is only a pattern in three finite cases; no proof or n=10 result is claimed by this audit.

## What this does and does not establish

The result is stronger than a saturating matching alone: it certifies positive Hall slack for every nonempty subset in each finite graph. It is not an all-orders theorem. The n=10 multivalued-pi SCC job is still computing separately.

A plausible inductive target is to identify a canonical terminal exchange class (K_n) of size (2^{s-1}), prove:
1. (K_n) is strongly connected under matching-relative exchanges;
2. it is the unique sink SCC;
3. it has at least one free child target neighbor;
4. every other SCC has a directed path into (K_n).

The difficult point is that the matching itself is currently obtained by a finite maximum-matching computation. A genuine all-orders proof must construct or characterize a compatible matching recursively, rather than assume an arbitrary matching has the desired condensation.

The strict Hall conclusion is matching-independent even though its SCC certificate is computed relative to one chosen matching. The proof task is therefore to find a recursive matching whose exchange condensation can be controlled under all leaf deletions and insertions.

No Yang--Mills mass-gap conclusion is claimed.
