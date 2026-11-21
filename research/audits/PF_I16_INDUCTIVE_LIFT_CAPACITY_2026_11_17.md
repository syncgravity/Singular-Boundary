# PF-I16: Inductive lift structure and simultaneous extension tests

Date: 2026-11-17

## 1. Leaf-peeling setup

For a child source x=(M,tau), choose its canonical non-root leaf interval J(x), delete J and its endpoints, and compress labels. This defines a parent source p(x) on n-2 ports. Write F_p={x:p(x)=p} for the children of a fixed parent source p.

For each child x, the leaf-last output neighborhood C_leaf(x) has a deterministic inverse projection
  pi_x : C_leaf(x) -> C_leaf(p(x)).
The inverse is recovered from the final leaf endpoints a,b by
  {u,v} = (N_T(a) union N_T(b)) minus {a,b},
then replacing the local three edges by uv, deleting a,b, and compressing.

## 2. Why ordinary parent matching is insufficient

A child matching chooses one distinct child target T_x for every child source x. Its projection induces, for each parent p, a multiplicity vector
  r_p(U) = #{x in F_p : pi_x(T_x)=U}.
In general r_p(U) is not bounded by one: several children of the same parent can project to the same parent target. At n=8, the previously verified global child matching used up to 18 copies of a single (parent source, parent target) pair.

Also, child targets are globally exclusive: the same labeled tree T can be a candidate for sources in different parent fibers. Therefore it is not enough to choose a separate parent matching in each fiber, nor to treat each parent target as a unit-capacity slot.

The natural inductive object is a capacity-labelled parent lift system: parent-target multiplicities r_p(U), together with a global collision constraint on the lifted labeled child trees. The exchange operation must reroute these multiplicities across parent fibers while preserving distinct child targets.

## 3. Exact extension criterion

Let G=(X,Y,E) be the child-source/child-tree bipartite graph. For a set F of prescribed disjoint edges (x_i,T_i), a left-saturating matching containing F exists if and only if the residual graph
  G_F = G[ X minus {x_i}, Y minus {T_i} ]
has a matching saturating all remaining left vertices.

This criterion is tested directly by maximum bipartite matching. It is stronger and more transparent than attempting to compose individual alternating reroutes: separate reroutes may consume the same intermediate source or target.

## 4. Two-edge finite result

The exact residual criterion was applied to every admissible pair of individually flexible challenger edges at n=4 and n=6, and to 4,079 deterministic-spread pairs at n=8.

- n=4: 2/2 compatible
- n=6: 14,426/14,426 compatible
- n=8: 4,079/4,079 sampled compatible

CI run: https://github.com/syncgravity/Singular-Boundary/actions/runs/43984128568

The n=8 pair universe contains 449,925,003 pairs; the sample is not exhaustive.

## 5. Three-edge test

Verifier: `research/verification/verify_pf_i16_simultaneous_three_edge_flexibility.py`
Workflow: `.github/workflows/pf-i16-simultaneous-three-edge.yml`

For each tested triple of individually flexible challenger edges with pairwise distinct sources and pairwise distinct targets, the verifier deletes all six endpoints and computes an exact maximum matching on the residual graph. The n=4 universe is exhaustive; n=6 and n=8 use deterministic-spread samples. Results are pending at the time this note was written and must be appended only after the workflow finishes.

## 6. What an all-orders induction would still need

A finite k-edge extension property, even for k=3, is not the induction theorem. A sufficient route would be a structural lemma that, for every n and every finite set F of pairwise disjoint admissible child assignments, guarantees Hall's condition in G_F. Equivalently, the residual child graph must satisfy
  |N_F(A)| >= |A| for every A subset of X minus sources(F),
where N_F(A) excludes the already-used target trees.

A useful stronger invariant is a quantitative residual expansion bound uniform in F, not merely existence of one matching or one-edge flexibility. Such a bound would be stable under the deletion of forced child assignments and could potentially be propagated through leaf peeling.

No all-orders residual expansion bound, all-orders Hall theorem, weighted one-link inequality, or Yang-Mills mass-gap conclusion is claimed here.
