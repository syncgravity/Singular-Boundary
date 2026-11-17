# PF-I16 crossing-fiber split-demand Hall test

Date: 2026-11-17

## Purpose

This verifier isolates the crossing-leaf fibers in each first-overcrowded source block X_k, retaining the complete multivalued-pi parent-canonical restriction and the same-target-block restriction Y_k.

For each source x=(M,tau) in X_k, it retains only non-root leaves J=[a,b] with a<=k<b. For each fiber F=(p,J,k), it:
1. enumerates the common forced-leaf-last child row;
2. reverses the final switch at J;
3. retains the child target only if its compressed parent target belongs to C_can(p);
4. retains only targets in Y_k;
5. assigns exact split demand delta(F)=sum_{x in F}1/d(x).

It then builds an integer-capacity bipartite flow network with target capacity 12, clearing all denominators at n=8,10. For each cut k, all crossing fibers from both lower-endpoint classes are placed in the same network. Thus the test includes collisions between a=k-1 and a=k, rather than testing those classes independently.

## Structural assertions

The verifier asserts the all-orders crossing-localization restriction:
- a in {k-1,k} when k>=5;
- a in {1,2,3} when k=3.

It also reports the number of fibers by (k,a), raw and retained incidence counts, and exact max-flow/min-cut data.

## Interpretation

A saturated flow proves the split-demand quotient Hall inequality for every subfamily of crossing fibers in that finite cut block. A deficient cut disproves only this crossing-fiber quotient route; it is not automatically a source-level Hall counterexample.

Even if all crossing-only flows saturate, the full blockwise quotient still requires mixed families containing both crossing and non-crossing fibers. No all-orders conclusion follows from finite runs.

## Reproducibility

Verifier: research/verification/verify_pf_i16_crossing_fiber_split_hall.py

Workflow: .github/workflows/pf-i16-crossing-fiber-split-hall.yml

Initial workflow run: https://github.com/syncgravity/Singular-Boundary/actions/runs/44189404066

Checked-out commit: d79cf5d346f7d572c4e1430a15067e24b0dc55f7

At audit creation the run was queued; no flow result is asserted here. Update this audit only after inspecting the completed job log.
