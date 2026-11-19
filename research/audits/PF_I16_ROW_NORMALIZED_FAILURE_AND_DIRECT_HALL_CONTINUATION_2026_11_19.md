# PF-I16: row-normalized allocation failures and direct Hall continuation

Date: 2026-11-19

## Scope

This audit records the completed exact-rational diagnostics of the two row-normalized sufficient allocations. It does not change the multivalued-\(\pi\) relation, the split-demand Hall obligation, or the weighted one-link theorem statement.

The exact blockwise Hall target remains
\[
\left|\bigcup_{F\in S}N_k(F)\right|\ge\sum_{F\in S}\delta(F)
\quad\text{for every fiber family }S\subseteq\mathcal F_k.
\tag{BQH_k}
\]
Equivalently, for every nonnegative weight vector \(z\),
\[
\sum_F\delta(F)z_F
\le
\sum_{T\in Y_k}\max_{F:T\in N_k(F)}z_F.
\tag{MR_k}
\]
This is the direct mixed-fiber dual. The all-orders proof must establish it without assigning more than unit capacity to any target.

## Completed run 44440991439: blockwise row normalization

Workflow: https://github.com/syncgravity/Singular-Boundary/actions/runs/44440991439

The verifier computes, within each first-crowded-cut block,
\[
L_k(T)=\sum_{F:T\in N_k(F)}\frac{\delta(F)}{|N_k(F)|}.
\]
The job completed successfully as a diagnostic process and reported OVERALL_RNL_BLOCKWISE=FAIL. The script's FAIL is the mathematical test result, not a workflow failure.

Exact results:

| Order | Cut | Fibers | Targets | Positive incidences | Overloaded targets |
|---:|---:|---:|---:|---:|---:|
| 6 | 3 | 12 | 34 | 111 | 8 |
| 8 | 3 | 382 | 1,356 | 17,100 | 131 |
| 8 | 5 | 42 | 102 | 1,047 | 6 |
| 10 | 3 | 19,792 | 90,751 | 6,243,410 | positive |
| 10 | 5 | 1,328 | 4,068 | 181,674 | positive |
| 10 | 7 | 120 | 306 | 8,343 | 0 |

At n=6 the exact maximum target load in the k=3 block is
\[
\frac{17}{14}>1,
\]
at target
\[
((1,2),(2,3),(2,6),(3,4),(3,5)).
\]
The six incident positive row contributions are:
- two fibers with deleted interval (2,6), each demand 3/2 and row sizes 4 and 6;
- two fibers with deleted interval (3,4), each demand 3/2 and row sizes 8 and 14;
- two fibers with deleted interval (3,5), each demand 3/2 and row sizes 8 and 14.

The complete incident list and exact rational loads are in the workflow log. There are no empty same-block rows at n=6,8,10. The n=8 k=3 maximum is
\[
\frac{58911088562633}{19982847094056}>1,
\]
and the n=8 k=5 maximum is
\[
\frac{19129}{18144}>1.
\]
At n=10 the k=7 block passes this sufficient load test, but the k=3 and k=5 blocks do not.

**Conclusion:** blockwise row normalization fails already at n=6. This does not produce a Hall-deficient fiber family; it rejects only the allocation \(\delta(F)/|N_k(F)|\).

## Completed run 44440846425: global full-row normalization

Workflow: https://github.com/syncgravity/Singular-Boundary/actions/runs/44440846425

This verifier uses the full retained row \(N(F)\), not its same-cut restriction, and tests
\[
L(T)=\sum_{F:T\in N(F)}\frac{\delta(F)}{|N(F)|}.
\]

| Order | Sources | Fibers | Targets reached | Fiber-target incidences | Overloaded targets |
|---:|---:|---:|---:|---:|---:|
| 8 | 608 | 440 | 1,493 | 19,154 | 138 |
| 10 | 31,744 | 21,280 | 95,864 | 6,598,466 | 6,428 |

At n=8 the exact maximum load is
\[
\frac{56478563159950721}{20150147805387600}>1.
\]
The worst target has 40 incident fibers. At n=10 the worst target has 388 incident fibers and the maximum load is strictly greater than one (see the exact run log / uploaded artifact for the full rational and complete incident-fiber witness).

**Conclusion:** global full-row normalization also fails. Its failure is logically distinct from blockwise failure, but neither refutes split-demand Hall or the original source-level Hall theorem.

## What survives

1. The exact fiber demand identity
   \[
   \delta(p,J)=\frac{a(p,J)}{d(p)}+\frac{b(p,J)}{d(p)+1}
   \]
   remains valid.
2. The all-orders single-fiber cap \(\delta(F)\le s/2\) remains valid.
3. Fixed-(parent, deleted-interval) fibers still have strong local expansion and individually satisfy Hall.
4. Exact nonuniform split-demand flows still saturate all demand at n=6,8,10. In particular, the independently replayed n=10 certificate has scaled demand and flow both 380,928 at scale 12, with maximum target load exactly 12/12.
5. Thus the present failure is a failure of a particular uniform-in-row allocation, not evidence of a deficient set.

## Mathematical diagnosis

The equal-row rule erases the internal structure of a fiber's row. In particular, it treats all retained child targets in \(N_k(F)\) as interchangeable, although each target is reached through a specific reverse mark \(J\), a specific projected parent target \(P_J(T)\), and a specific guarded local switch. The overloads show that these target-side incidences are not sufficiently regular for equal row spreading.

The next proof step must preserve that reverse-mark / parent-target structure. A valid proof can take either of two forms:

- construct an explicit nonuniform transport \(\lambda(F,T)\ge0\), supported on \(T\in N_k(F)\), with
  \[
  \sum_T\lambda(F,T)=\delta(F),\qquad
  \sum_F\lambda(F,T)\le1;
  \]
- prove the weighted dual \((MR_k)\) directly for arbitrary \(z_F\ge0\), without first fixing a transport.

A candidate transport should depend on the reverse-mark geometry and parent overlap data, not merely on \(|N_k(F)|\) or on the reciprocal number of fibers incident to a target. The already-tested equal reciprocal reverse-degree split also fails at n=8 and n=10.

## Proof boundary

No Hall-deficient family has been found by these tests. No all-orders mixed-Hall proof has been established. The weighted one-link inequality remains conditional on all-orders multivalued-\(\pi\) Hall. No Yang--Mills mass-gap conclusion follows.
