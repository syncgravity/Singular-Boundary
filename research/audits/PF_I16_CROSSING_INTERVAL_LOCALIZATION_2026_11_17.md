# PF-I16: localization of crossing deleted intervals at the first overcrowded cut

Date: 2026-11-17

## Status

**Proved all orders.** This is a structural lemma for the multivalued-\(\pi\) construction. It narrows, but does not solve, the crossing-interval contribution to blockwise split-demand Hall.

## Proposition

Let \(x=(M,\tau)\in X_k\), where \(k\) is its first overcrowded odd cut, and let \(J=[a,b]\in L_0(\tau)\) be a non-root leaf interval which crosses \(k\):
\[
a\le k<b.
\]
Then:
- if \(k\ge5\), necessarily \(a\in\{k-1,k\}\);
- if \(k=3\), necessarily \(a\in\{1,2,3\}\).

In particular, for every \(k\ge5\), all crossing deleted intervals in the entire source block \(X_k\) belong to only two left-endpoint classes.

## Proof

By definition of the first-overcrowded cut,
\[
m_r(M)=1\qquad\text{for every odd }r<k.
\tag{1}
\]
Suppose \(k\ge5\) and, contrary to the claim, \(a\le k-2\). Since \(a\le k-2<b\), the interval \(J\) crosses the preceding odd cut
\[
r=k-2.
\]

Delete the endpoints of \(J\) and compress the remaining ports. Because \(J\) is a leaf of the interval-overlap tree, deleting it leaves the parent overlap graph connected; hence the parent matching is a connected-overlap matching. The child cut \(r\), which lies strictly between the endpoints of \(J\), becomes parent cut \(r-1\): exactly one deleted endpoint lies to the left of that cut.

Every connected-overlap matching has at least one interval crossing every internal cut. Therefore at least one parent matching interval crosses parent cut \(r-1\). On reinserting \(J\), that interval and \(J\) both cross child cut \(r\), giving
\[
m_r(M)\ge2,
\]
contrary to (1). Thus \(a>k-2\), and integrality together with \(a\le k\) gives \(a=k-1\) or \(a=k\).

For \(k=3\), there is no positive internal parent cut corresponding to the preceding odd cut \(r=1\): deleting an interval that contains port 1 removes the left boundary itself. The only unconditional restriction is \(1\le a\le3\), giving the stated exceptional three classes. \(\square\)

## Consequences for the crossing part of BQH

For a fixed source \(x\in X_k\), at most one matching interval can have any prescribed left endpoint, because matching intervals are pairwise vertex-disjoint. Hence:
- for \(k\ge5\), at most two non-root leaf fibers of \(x\) are crossing fibers;
- for \(k=3\), at most three are crossing fibers.

Under the split-demand convention, the total crossing-fiber demand contributed by one source is therefore at most \(2/d(x)\) for \(k\ge5\), and at most \(3/d(x)\) for \(k=3\), where \(d(x)=|L_0(\tau)|\).

This is a restriction on the **source-side demand**, not yet a Hall bound: different crossing fibers can still have overlapping same-cut target rows. In particular, it does not imply BQH by itself.

## What remains

The crossing part of BQH can now be separated into:
1. the two left-endpoint classes \(a=k-1\) and \(a=k\) for \(k\ge5\);
2. the three exceptional classes \(a=1,2,3\) for \(k=3\);
3. the mixed collisions between these classes and the non-crossing fibers.

The next required estimate is a capacity bound for the union of their parent-canonical same-cut lift rows. Reverse-switch uniqueness controls a fixed \(J\), but not collisions between different allowed left-endpoint classes. The Type-I/Type-II reverse-mark classification is the appropriate target-side tool for that remaining step.

No all-orders BQH, full Hall, weighted one-link inequality, or Yang--Mills mass-gap theorem is claimed.
