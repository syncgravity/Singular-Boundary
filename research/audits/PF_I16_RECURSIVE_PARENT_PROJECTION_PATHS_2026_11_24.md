# PF-I16 recursive parent-projection paths for residual collisions

Date: 2026-11-24 UTC  
Branch: \`research/pf-i16-parent-fiber-exchange-2026-11-23\`  
Workflow: [45364715606](https://github.com/syncgravity/Singular-Boundary/actions/runs/45364715606), conclusion **SUCCESS**  
Artifact: [14906366335](https://github.com/syncgravity/Singular-Boundary/actions/runs/45364715606/artifacts/14906366335)  
Artifact ZIP SHA-256: \`c4e2548f6a7ec89d9bf580fca8b91ceacf6ed9a7b4b63b4eaa192a85c6f96f70\`  
Decoded JSON SHA-256: \`a5306758bb324bdc78031fa8ef982cc065cb3737f14ba1516cc6abe04c7afd3f\`

**Status:** all 4,881 residual \(n=8\) non-diamond collision pairs from the S/C/D census have connected canonical parent projections in the order-six S/C/D graph. This is a parent-level connectivity result only; it is not a path-lifting theorem.

## 1. Input residual class

The preceding cross-source audit found 4,881 \(n=8\) shared-target collision pairs whose block endpoints remain in different components after:
- fixed-\((p,J,P)\) sibling-lift \(S\)-moves;
- same-source deletion-diamond \(D\)-moves with the ordinary common-parent witness;
- cross-source common-parent/same-parent-target \(C\)-incidences.

These are precisely the residual pairs for which either the parent source or the parent target changes across the two incidences.

## 2. Canonical parent projection

For each \(n=8\) endpoint \((x,J,P,T)\), the verifier takes its exact parent source \(p=\pi_J(x)\) and parent target \(P=P_J(T)\).

It then:
1. Locates \(p\) in the complete \(n=6\) source enumeration.
2. Selects the canonical non-root leaf \(L(p)\) of \(p\).
3. Computes the exact guarded inverse of \(P\) at \(L(p)\).
4. Compresses that inverse to the canonical parent target \(U\).
5. Maps \((p,P)\) to the unique \(n=6\) block \((r,L(p),U)\), verifying that \(p\) is a child source in that block and \(P\) is one of its retained child targets.

No \(\mathbb Z^5\) displacement or helical phase is introduced. This is a purely combinatorial parent projection.

## 3. Exact path census

| Quantity | Result |
|---|---:|
| Order-six blocks | 45 |
| Order-six C-incidence witnesses | 82 |
| Order-six S/C/D components | 1 |
| Order-eight blocks | 3,980 |
| Order-eight C-incidence witnesses | 5,786 |
| Residual order-eight non-diamond collision pairs | 4,881 |
| Distinct order-six parent-block endpoint pairs | 155 |
| Residual pairs with disconnected order-six parent projections | 0 |
| Maximum shortest-path length in the order-six block graph | 6 |

Shortest path lengths, weighted by the number of \(n=8\) collision pairs:

| Order-six path length | Residual \(n=8\) collision pairs |
|---:|---:|
| 0 | 126 |
| 1 | 914 |
| 2 | 1,053 |
| 3 | 903 |
| 4 | 733 |
| 5 | 686 |
| 6 | 466 |
| **Total** | **4,881** |

Thus every residual \(n=8\) collision pair projects to a connected order-six parent-block pair, with a shortest path of at most six \(C/D\) edges after the \(S\)-blocks are contracted.

## 4. Explicit parent path for a residual collision

One residual \(n=8\) collision has common child target
\[
T=\{(1,2),(2,3),(2,5),(3,4),(3,6),(6,7),(6,8)\}.
\]

Its left endpoint has parent source intervals \((1,3),(2,5),(4,6)\), parent tree \((0,1),(1,2)\), parent target
\[
P=\{(1,2),(2,3),(2,4),(4,5),(4,6)\},
\]
and deleted mark \((2,5)\).

Its right endpoint has parent source intervals \((1,4),(2,5),(3,6)\), parent tree \((0,1),(1,2)\), parent target
\[
Q=\{(1,2),(2,3),(2,5),(3,4),(3,6)\},
\]
and deleted mark \((6,8)\).

The two canonical parent projections are order-six block IDs 1 and 6. A shortest order-six path is
\[
1\to13\to14\to12\to17\to5\to6,
\]
with edge types
\[
C,\ D,\ D,\ C,\ C,\ D.
\]

This records the parent-level route that a future lifting lemma would have to realize. The current order-eight S/C/D graph does not contain a path between the original residual endpoints.

## 5. Interpretation and open lifting obligation

The finite result supports a recursive strategy: the remaining order-eight collisions are not separated at the canonical parent level. Their parent projections can be connected by a short order-six path.

The gap is the **lifting of each parent-level edge**. An order-six \(D\)-edge is witnessed by one parent source with two eligible marks and an ordinary common-parent target. To lift it to order eight, one must exhibit a child source extension and a child target that preserve the exact outer mark, both inner guarded inverses, and the ordinary common-parent witness. An order-six \(C\)-edge similarly requires two distinct child-source extensions with a common lifted target and compatible parent projection. Connectivity of the parent graph does not guarantee either lift.

The next verifier should classify the six edge steps in each shortest parent path by liftability, retaining:
- the exact order-six source and target witness;
- all order-eight child-source extensions of that parent source;
- the outer mark and parent-target projection;
- the child target(s) that lift the parent edge;
- exact guarded inverse and ordinary common-parent \(U\) certificates;
- whether consecutive lifted edges can be joined at the same order-eight state.

A failed edge lift is a precise obstruction to the proposed recursive parent-fiber exchange lemma. A successful path lift for all 4,881 cases would be a stronger finite theorem, but would still require an all-orders lifting argument.

No all-orders PFEL, split-demand Hall, multivalued-\(\pi\) Hall, or weighted one-link inequality follows.

## 6. Reproduction

Verifier: \`research/verification/verify_pf_i16_recursive_parent_projection_paths.py\`  
Workflow: \`.github/workflows/pf-i16-recursive-parent-projection-paths.yml\`  
Verifier blob SHA: \`718b2614c84a1df48ab97f26202259816c023b7e\`  
Workflow blob SHA: \`29846f7a484ee38c8d86631a272b2642bfc9938f\`  
Successful run: [45364715606](https://github.com/syncgravity/Singular-Boundary/actions/runs/45364715606)
