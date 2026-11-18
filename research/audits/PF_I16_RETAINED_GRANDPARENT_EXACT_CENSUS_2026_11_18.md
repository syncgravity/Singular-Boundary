# PF-I16: exact retained-grandparent sibling census — test specification

Date: 2026-11-18

## Status

**Corrected finite test prepared; no numerical conclusion yet.** The previous fixed-parent n=12 diagnostic is not evidence: its final retained-route check used a permissive inverse helper without the no-reinsertion guard, it excluded p=q, and it did not verify that the selected parent sources actually reconstruct one common child source. Its run was later marked cancelled.

The corrected verifier is
\`research/verification/verify_pf_i16_retained_grandparent_exact_census.py\`.
It is staged on branch
\`research/pf-i16-retained-grandparent-exact-2026-11-18\`.
The workflow will be submitted only after the exact verifier and this specification are read back and checked.

## 1. Correct theorem target

For a source \(r=(M,\tau)\), the retained multivalued-\(\pi\) neighborhood is
\[
N_\pi(r)=
\bigcup_{L\in L_0(\tau)}
\{U:\ L\text{ is a valid guarded reverse mark of }U,\ 
P_L(U)\in C_{\rm can}(\pi_L(r))\}.
\tag{RG}
\]
This is not the condition \(U\in C_{\rm can}(r)\). The two-step canonical-suffix characterization is
\[
U\in N_\pi(r)
\iff
\text{some valid construction history ends in }(K,L),
\quad K=\operatorname{canleaf}(\pi_L(r)).
\tag{2S}
\]

For a common parent with four matching intervals, deleting either of its non-root leaves leaves a three-interval parent. Its canonical neighborhood can be strict, so the low-order theorem \(N_\pi(r)=C(r)\) no longer settles the question.

## 2. Why this fixed parent is the right first test

The first n=8 universal-coverage miss has common parent
\[
R=\left(
((1,4),(2,5),(3,7),(6,8)),
((0,1),(0,2),(2,3))
\right).
\]
Its non-root leaves are
\[
A=(2,5),\qquad B=(6,8),
\]
with A the canonical leaf.

For this rooted overlap tree:
- deleting A leaves a rooted path whose canonical non-root leaf is the surviving B;
- deleting B leaves a rooted star whose canonical non-root leaf is A.

Consequently, the two-step suffix test for this R reduces to checking the two possible ordered reverse pairs:
- reverse A, then reverse B in the projected parent;
- reverse B, then reverse A in the projected parent.

At this order the twice-projected source has two matching intervals and its canonical parent target is the unique base target. The verifier nevertheless checks the projected target against the actual canonical output set rather than relying on that simplification.

This is a sibling-specific question. It does not assert universal \(N_\pi(R)=C(R)\), which is already false.

## 3. Previous results and rejected shortcuts

### Low-order retained-grandparent theorem

The durable audit \`PF_I16_RETAINED_GRANDPARENT_COMPATIBILITY_2026_11_18.md\` proves
\[
N_\pi(r)=C(r)
\]
for sources with at most three matching intervals. Therefore every ten-port sibling-source diamond has its common double inverse retained at the six-port common parent, regardless of p=q. This closes the first nontrivial order, but not four-interval common parents.

### Universal coverage failure at eight ports

Workflow [44366065661](https://github.com/syncgravity/Singular-Boundary/actions/runs/44366065661) completed successfully. Its log reports:
- n=6: 22 sources, 241 ordinary and 241 retained source-target incidences;
- n=8: 608 sources, 43,991 ordinary and 38,208 retained source-target incidences;
- 197 of 608 n=8 sources have strict retained subsets.

The first miss is exactly R above, with target
\[
((1,2),(2,3),(2,4),(3,5),(3,6),(6,7),(6,8)).
\]
The only ordinary final-leaf route for that target projects to a noncanonical parent target. This is a counterexample to universal ordinary-to-retained coverage, not to the sibling-specific claim.

### Canonical third-mark claims already disproved

The n=10 unrestricted canonical source-diamond census found 320,655 canonical-parent failures among 3,600,244 mutually surviving common-target incidences. The distinct-parent census separately found 286,440 failures among 765,852 incidences. Thus neither unrestricted nor p!=q canonical-third-mark implication is available. These results do not refute (RG), which is weaker.

### Hall reductions that remain open

The fixed-parent/fixed-Q selector, integer selector, and simultaneous reverse-mark lift reductions have documented obstructions or overloads. Fractional allocation is not an integer selector. The mixed-fiber Hall inequality remains an arbitrary-family union/capacity problem. The all-orders cut-local lemmas control noncrossing source and target blocks and localize crossing leaves, but do not control collisions between different fibers. No rowwise expansion estimate may be summed as if different fibers had disjoint targets.

## 4. Corrections made to the earlier n=12 diagnostic

The previous script \`verify_pf_i16_fixed_n8_miss_sibling_diamond.py\` had three independent scope/validity problems:

1. Its final \`retained_routes\` call imported \`inverse_last_switch\` from the leaf-peeling diagnostic. That helper checks a local pattern but omits the exact no-reinsertion guard. A positive route count could therefore be false.
2. It skipped p=q, although the retained-grandparent statement has no distinct-parent hypothesis.
3. It paired p and q merely because their canonical deletions gave R and their inserted marks were disjoint. It did not reconstruct a common child matching and overlap tree, so not every counted pair was necessarily a genuine sibling-source diamond.

The replacement fixes all three:
- It uses \`local_records\`, \`inverse\`, and \`relabel_tree\` from the exact reverse-mark census, enforcing induced pattern, full endpoint incidence, overlap, and no-reinsertion.
- It includes p=q.
- It lifts both parent sources to the same twelve-port labels, requires identical child matchings, unions their lifted overlap-tree edges, checks that the union is a tree with J and K as non-root leaves, and verifies exactly
  \[
  \pi_J(x)=p,\qquad \pi_K(x)=q.
  \]
Only then is a pair counted as a sibling-source diamond.

The target-side fiber neighborhoods and both inverse projections continue to use the existing exact \`fiber_neighborhood\`, \`project_once\`, and \`second_inverse\` routines.

## 5. Verifier controls

Before the full census, the script checks:
1. The known six-port rooted-star example that is not in \(C_{\rm can}(R)\) is nevertheless retained through the other leaf.
2. The first eight-port universal-coverage miss has no retained route.
3. All 241 ordinary source-target incidences at six ports pass the exact retained-route test, matching the proved low-order theorem.

These controls are intended to catch precisely the distinction between ordinary, canonical, and retained neighborhoods and the earlier inverse-guard defect.

## 6. Interpretation of the forthcoming census

The workflow fixes R and enumerates every twelve-port sibling-source diamond whose two ten-port parents delete canonically to R. It records p=q and p!=q separately, intersects the exact retained fiber neighborhoods, and for every mutually surviving common target computes the common double inverse U.

- **Any unretained U** is a finite counterexample to the proposed sibling-specific retained-grandparent rerouting at this first four-interval parent. It would rule out this proof primitive in its present form.
- **No unretained U** is only finite evidence for this R at twelve ports. It does not prove the sibling-specific statement for all four-interval parents, much less all orders.
- Either result leaves the all-orders mixed-fiber Hall theorem and weighted one-link inequality open.

No workflow result is asserted in this specification.
