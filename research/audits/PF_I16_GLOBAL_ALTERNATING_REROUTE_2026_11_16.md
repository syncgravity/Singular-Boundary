# PF-I16 global alternating-path rerouting diagnostic

Date: 2026-11-16

## Motivation

The source-constrained parent-exchange graph is disconnected at eight ports:
5,156 collision pairs have projections in different components. The next
test therefore uses the full child-source to final-tree bipartite graph,
allowing alternating paths to pass through multiple parent fibers.

## Exact test

For each child source, enumerate its complete leaf-last output neighborhood.
Compute a deterministic maximum bipartite matching. It must saturate all
child sources. For each final tree shared by multiple child sources, and
each challenger other than the tree's currently matched owner, search for
an alternating path

```
shared tree -> its matched source -> an alternative tree
             -> that tree's matched source -> ... -> free tree.
```

If such a path exists, the challenger can be assigned the shared tree while
the currently matched owner is shifted along the path. This certifies that
the individual collision can be rerouted without losing left saturation.

The verifier also records how many parent fibers occur among sources on
the alternating path. It verifies each child-to-parent projection lies in
the corresponding parent source's exact guarded output neighborhood.

This is a diagnostic of individual collision repair. It does not prove that
many collisions can be repaired simultaneously, nor does it prove the
all-orders Hall inequality.

## Reproducibility

Verifier: `research/verification/verify_pf_i16_global_alternating_reroute.py`

Workflow: `.github/workflows/pf-i16-global-alternating-reroute.yml`

The workflow is deliberately strict: it exits nonzero if any challenger
cannot be rerouted. A failure is an obstruction to this particular
single-collision rerouting proposal, not a counterexample to full Hall.

## Interpretation

A pass would show that every individual shared-target collision can be
resolved in the full graph by an alternating path, potentially traversing
multiple parent fibers. A failure would identify a collision target whose
matched owner cannot be moved to a free target under the selected matching.
Even a pass is weaker than the required simultaneous exchange theorem:
the rerouting paths may overlap and compete for the same matched sources or
free targets.
