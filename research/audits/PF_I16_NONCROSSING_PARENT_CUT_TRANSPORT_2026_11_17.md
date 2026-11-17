# PF-I16: parent crowded-cut transport for non-crossing leaf fibers

Date: 2026-11-17

## Theorem (exact source-cut transport)

Let x=(M,tau) lie in X_k, where k is the first overcrowded odd cut: the matching load m_r(M) is 1 for every odd r<k and m_k(M)>=3. Let J=[a,b] be a non-root leaf interval and let p=pi_J(x) be obtained by deleting the two endpoints of J and compressing the remaining ordered ports.

If J does not cross k, then the first overcrowded odd cut of the parent matching is determined exactly:

- **J left of or ending at k:** if b<=k, the parent first overcrowded odd cut is k-2;
- **J right of k:** if a>k, the parent first overcrowded odd cut is k.

The assertion is understood only when the indicated parent cut exists; for k=3, the left case maps to parent cut 1.

## Proof

For any parent cut q, its corresponding child cut is obtained by restoring the deleted endpoints. The number of restored endpoints to the left of the parent cut is exactly the shift in cut index.

If b<=k, both deleted endpoints lie at or left of child cut k. Thus child cut k corresponds to parent cut k-2. Since J itself does not cross k, deleting J leaves the crossing count at this cut unchanged, so the parent load at k-2 is at least 3.

Now take any odd parent cut q<k-2. If q lies before J, its corresponding child cut is q; if it lies after J, its corresponding child cut is q+2. In either case the corresponding child cut is odd and strictly less than k. The child matching load there is exactly 1. Deleting J cannot increase that load, and J does not cross the parent cut under consideration. Hence every earlier odd parent cut has load 1. The first parent crowded cut is k-2.

If a>k, neither deleted endpoint lies to the left of any child cut q<=k. Parent odd cuts q<k correspond to the same child cuts q, and so have load 1. Parent cut k corresponds to child cut k; J does not cross it, so its load remains at least 3. The first parent crowded cut is k.

This proves both cases.

## Crossing versus non-crossing parent strata

For a fixed child block X_k, the leaf fibers therefore split into three geometrically different recursive strata:

1. **Left non-crossing:** b<=k; parent source lies in block X_{k-2}.
2. **Right non-crossing:** a>k; parent source lies in block X_k.
3. **Crossing:** a<=k<b; for k>=5 the localization theorem forces a in {k-1,k}; for k=3 it forces a in {1,2,3}. The parent cut corresponding to child cut k is k-1, which is even, so the parent first-overcrowded odd-cut label is not determined by this argument.

This is a genuine recursive block decomposition for all non-crossing fibers. It sharpens the mixed-family problem: left and right non-crossing fibers recurse into known source-cut strata, while only crossing fibers pass through an even parent cut and require the separate reverse-mark analysis.

## Consequence for the quotient Hall problem

For a fiber family S in child block k, split it as S_L union S_R union S_C according to the three classes above. The exact demand is additive:

\[
\sum_{F\in S}\delta(F)=\sum_{F\in S_L}\delta(F)+\sum_{F\in S_R}\delta(F)+\sum_{F\in S_C}\delta(F).
\]

But target neighborhoods need not be disjoint across these strata. Therefore the source-cut recursion alone does not imply

\[
|N(S)|\ge\sum_{F\in S}\delta(F).
\]

The remaining structural task is to control overlaps between the left-parent, right-parent, and crossing target rows, not merely to prove Hall separately inside each stratum.

## Finite mixed-family evidence

The exact all-fiber multivalued-pi max-flow certificate already includes all three strata simultaneously, with the parent-canonical and same-target-cut restrictions in force:

| Ports | Fibers | Scaled demand | Max flow | Deficit |
|---:|---:|---:|---:|---:|
| 6 | 18 | 44 | 44 | 0 |
| 8 | 440 | 3,648 | 3,648 | 0 |
| 10 | 21,280 | 380,928 | 380,928 | 0 |

The exact workflow log is run 44177680653. These are finite certificates, not an all-orders theorem.

## Status and next target

The non-crossing parent-block label is now proved. The next proof target is a **three-stratum overlap inequality**: bound the common target neighborhood of an arbitrary mixture of left-parent, right-parent, and crossing fibers. A useful first reduction is to group left/right fibers by their parent first-crowded block and compare their inverse parent targets before adding the crossing reverse-mark contributions. No Hall conclusion is claimed here.
