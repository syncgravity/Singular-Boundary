# Three-move fractional transport: incidence/degree reduction (2026-11-16)

## Exact transport quantity

For each left source x=(M,\tau), let C(x) be the set of distinct three-move local-switch output trees. The uniform transport column at a right tree T is
\[
W(T)=\sum_{x:T\in C(x)}\frac1{|C(x)|}.
\]
The desired finite-coupling statement is \(W(T)\le1\) for every T.

Define the unweighted source incidence
\[
I(T)=|\{x:T\in C(x)\}|,\qquad
d_* = \min_x |C(x)|.
\]
Then the elementary bound
\[
W(T)\le \frac{I(T)}{d_*}
\]
shows that the uniform transport theorem would follow from the pair of estimates
\[
\boxed{d_*\ge 3^{s-1},\qquad I(T)\le3^{s-1}\text{ for every }T,}
\tag{ID}
\]
where n=2s. This separates the source-expansion problem from the target-incidence problem and removes the varying denominators from the column estimate.

## Finite evidence and new instrumentation

The existing exact uniform-column regression found minimum source degrees
\[
d_*=3,9,27
\]
at n=4,6,8 respectively, matching \(3^{s-1}\). The existing exact maximum column loads are 2/3, 4/5, and approximately 0.976422959218.

The verifier `research/verification/verify_pf_i16_local_switch_fractional_transport.py` now also counts, for every output tree, the number of distinct source objects incident to it. It reports the maximum incidence and compares it with \(3^{s-1}\), alongside the exact rational column maximum. This is diagnostic instrumentation: the incidence maxima have not yet been established in this audit, and no assertion of (ID) is made.

## Why this is a useful next target

If the observed source-degree floor is structural, it may follow by showing that every one of the s-1 interval insertions contributes at least three distinguishable continuations, despite possible mergers between histories. That distinctness issue must be proved; merely counting three local replacement shapes at each step is not enough because different histories can in principle merge.

The target-incidence bound is a separate inverse problem: for a fixed port tree T, count how many pairs (M,\tau) admit at least one legal insertion history and local-switch sequence ending at T. A direct reverse-switch encoding may bound this number by \(3^{s-1}\), or reveal the correct larger bound and a compensating stronger source-degree estimate.

## Proof boundary

The implication (ID) => (FC) is immediate, but neither all-orders estimate in (ID) is proved. The n=4,6,8 exact fractional transport results remain finite computations. No n=10 result or all-orders local-switch column bound is claimed. The weighted one-link inequality and Yang--Mills mass gap remain open.
