# PF-I16 n=10: full-neighborhood sample and expansion program

Date: 2026-11-17

## Exact source count

The n=10 source set has exactly 31,744 objects (M,tau), over 706 perfect matchings. The overlap-tree count per matching ranges from 1 to 125. Source-count CI: https://github.com/syncgravity/Singular-Boundary/actions/runs/43990555456

## Why the canonical subgraph is insufficient

A deterministic one-witness-edge subrelation, even when enlarged to four parent-before-child traversal orders, has only 20,854 targets for 31,744 sources and maximum matching 16,212. This is a restricted-subgraph obstruction, not a failure of the full leaf-last relation. Details: `research/audits/PF_I16_N10_FIXED_WITNESS_SUBGRAPH_OBSTRUCTION_2026_11_17.md`.

## Spread sample of the complete leaf-last neighborhoods

The complete `candidate_outputs(..., forced_last=leaf)` generator includes all parent-before-child insertion orders and all guarded overlapping edges. A deterministic spread sample of 203 sources (stride 157 through the exact 31,744-source ordering) produced:

- minimum distinct target degree: 16;
- maximum distinct target degree: 1,947;
- mean distinct target degree: 422.650.

This indicates that the full relation is substantially richer than the one-witness subgraph. It is a sample only; it is not an estimate with a proved error bound and it does not establish Hall.

Verifier: `research/verification/sample_pf_i16_full_leaf_last_n10.py`.

CI: https://github.com/syncgravity/Singular-Boundary/actions/runs/43991395574

## Full exact n=10 graph computation

The next job enumerates the complete leaf-last neighborhood for every one of the 31,744 sources, encodes each ten-port tree as a 45-bit edge mask, and computes a maximum bipartite matching. This is the first full-relation n=10 matching attempt.

- Verifier: `research/verification/verify_pf_i16_full_leaf_last_graph_n10.py`
- Workflow: `.github/workflows/pf-i16-full-leaf-last-graph-n10.yml`
- Run: https://github.com/syncgravity/Singular-Boundary/actions/runs/43991584609

At audit time this run is still in progress; no n=10 matching or expansion conclusion is claimed.

## Next proof bottleneck

If the full n=10 graph has a left-saturating matching, the next step is to exploit the matching-relative identity

  |N(A)|-|A| = |B_D(A)| + |F(A)|

and focus only on sources with at most two free-target neighbors. If every source has at least three free neighbors, the expansion bound follows immediately. Otherwise, the low-free-degree source set may be much smaller than all 31,744 sources and could support a restricted exact cut census.

No n=10 uniform expansion theorem, all-orders Hall theorem, weighted one-link inequality, or Yang-Mills mass gap is established by the current sample.
