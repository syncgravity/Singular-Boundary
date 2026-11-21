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

## Verified results

Workflow run: https://github.com/syncgravity/Singular-Boundary/actions/runs/44189404066
Checked-out commit: d79cf5d346f7d572c4e1430a15067e24b0dc55f7
Conclusion: success.

| Ports | First crowded cut | Fibers | Targets | Exact split demand | Scaled demand | Max flow | Deficit |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 3 | 220 | 1,244 | 1,052/3 | 4,208 | 4,208 | 0 |
| 8 | 5 | 24 | 102 | 28 | 336 | 336 | 0 |
| 10 | 3 | 8,512 | 78,334 | 42,424/3 | 169,696 | 169,696 | 0 |
| 10 | 5 | 440 | 3,732 | 1,700/3 | 6,800 | 6,800 | 0 |
| 10 | 7 | 48 | 306 | 45 | 540 | 540 | 0 |

At 8 ports there are 244 crossing fibers in total, with 12,665 raw leaf-last incidences and 10,221 retained same-cut, parent-canonical incidences. At 10 ports there are 9,000 crossing fibers, with 3,702,225 raw incidences and 2,543,659 retained incidences.

A saturated flow proves the split-demand quotient Hall inequality for every subfamily of crossing fibers in each displayed finite cut block. The two lower-endpoint classes were included in the same network for each cut, so their mutual target collisions are included.

## Interpretation and limitation

This is finite evidence for crossing fibers only. It does not prove the mixed crossing/non-crossing quotient Hall inequality, does not establish any all-orders expansion bound, and is not a source-level counterexample if a future quotient route fails.

Even if all crossing-only flows saturate, the full blockwise quotient still requires mixed families containing both crossing and non-crossing fibers. No all-orders conclusion follows from these finite runs.

## Reproducibility

Verifier: research/verification/verify_pf_i16_crossing_fiber_split_hall.py

Workflow: .github/workflows/pf-i16-crossing-fiber-split-hall.yml
