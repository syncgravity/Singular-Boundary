# PF-I16 four-interval support inventory

Date: 2026-11-19  
Branch: `research/pf-i16-four-interval-diamond-2026-11-19`  
Pull request: #119 (draft)

## Scope

This is a target-only inventory for the four-interval extension of the PF-I16 Hall incidence lift. It is run on the Ngrid=12 PF-I11 completed-window core, which is a face subcomplex of the independently replayed Ngrid=12 PF-I16 original-source complex.

The inventory enumerates every eligible matched edge with exactly two accepted incident rhombi and every connected face-supported support of one, two, or three accepted rhombi containing exactly one of those two incident rhombi, subject to the union having one simple boundary cycle. Face connectivity includes meeting at a vertex as well as at an edge; pinched or multiple-cycle boundaries are rejected. All selected vertices and faces are checked against strict PF-I16 acceptance inequalities.

No Hall source records, demands, loads, deficiencies, matchings, or flow outcomes are read in selecting target edges or support families.

## Reproducible run

GitHub Actions run: `44569289813`  
Run head: `599264fbcbf85c8153e45cef9b30b4631e52a507`  
Artifact: `pf-i16-four-interval-support-inventory`  
Artifact SHA-256: `3eec052f72f3f0b64963df737957b795ac923e16698628a60d9bc932a350ae1a`

The inventory step and artifact upload succeeded. The subsequent commit-to-branch step initially failed because Actions checked out a detached HEAD and the workflow attempted a bare `git push`. The workflow has since been corrected to check out the PR head ref and push explicitly to that branch. The corrected push path has not yet been independently verified by a subsequent Actions run.

## Counts

| Quantity | Count |
|---|---:|
| Completed-core vertices | 4,294 |
| Completed-core edges | 8,382 |
| Completed-core accepted rhombi | 4,089 |
| Original-source control vertices | 4,324 |
| Original-source control edges | 8,468 |
| Original-source control accepted rhombi | 4,145 |
| Eligible matched edges with exactly two accepted incident rhombi | 8,026 |
| Eligible edges vertex-disjoint from the frozen three-edge motif | 8,004 |
| Distinct accepted face keys appearing in enumerated supports | 4,089 |
| Total support options over all eligible matched edges | 214,108 |
| Maximum support size | 3 rhombi |

Minimum strict acceptance margins over enumerated supports:

- Vertex-window margin: 0.003609455403427164
- Face-triangle margin: 0.003609455403427164

Support-option counts per edge range from 9 to 28. The histogram is in the machine-generated artifact.

## Four-interval source graph context

An independent reconstruction of the ordered-port source enumerator gives 608 order-eight sources, 1,050 eligible reverse-leaf projections, and 13 distinct four-interval overlap graphs. Restricting to actual eligible reverse-leaf deletions, the retained three-interval parent graphs are the two-edge star, two-edge path, and triangle patterns already covered by the demand-independent alternative triple. There are 490 unordered pairs of eligible deletions in the same source, hence 490 source deletion diamonds to test.

## What this inventory does not establish

This inventory is not a four-interval compatibility result. It does not select a fourth edge, assign one support to each of four intervals, or check the exact four-vertex intersection graph. It does not perform the full L6c intersection-diagram comparison, relative deletion collapse, or L7b ordered multi-footprint boundary-word test. It establishes neither L8 construction independence nor an all-orders incidence lift.

## Next gate

For each of the 13 overlap graphs, fix the first three interval supports from the matching star/path/triangle restriction and search the 8,004 vertex-disjoint candidate edges with their full one-to-three-rhombus support families. A candidate must realize the exact four-interval intersection graph and satisfy every eligible one-interval deletion restriction. Then check all 490 source deletion diamonds by comparing both deletion paths in the complete L6c intersection diagram and L7b ordered boundary signature. No conclusion should be drawn from an inventory count alone.
