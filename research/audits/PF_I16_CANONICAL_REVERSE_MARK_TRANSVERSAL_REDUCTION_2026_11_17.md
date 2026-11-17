# PF-I16: canonical reverse-mark transversal reduction (corrected)

Date: 2026-11-17

> **Correction.** The earlier version conflated a fractional transport with
> a selector. A fractional submeasure can split one target's capacity among
> rows carrying different reverse marks; a selector m(T) cannot. Also,
> delta(p,J) was not proved to be at most one. The earlier sentence claiming
> that a row's demand is automatically at most one is withdrawn. The exact
> selector criterion and its proof are now recorded in
> PF_I16_CANONICAL_REVERSE_MARK_SELECTOR_HALL_CRITERION_2026_11_17.md.

## 1. Target-side classification

A valid reverse mark J={a,b} in a child target T is only:

- Type I: adjacent endpoints of degrees (1,3) or (2,2);
- Type II: distance-two endpoints, one leaf and one degree-two vertex,
  with one of the two ordered path orientations.

The distance-three leaf/leaf path is invalid because the restored old edge
is already present in the induced local tree.

## 2. Fixed-parent row construction

Fix an injective matching Q from parent sources p to canonical parent targets
Q(p). A row is r=(p,J), with split demand
[
  delta(p,J)=\sum_{x\in X(p,J)}1/d(x).
]
Its candidate target set E_r consists of child targets obtained by inserting
J last into Q(p) through a guarded local switch.

Every T in E_r has J as a valid reverse mark and inverse parent target
Q(p). If two rows with the same mark J contain T, reverse inversion gives
Q(p)=Q(p'); injectivity of Q gives p=p'. Thus same-mark collisions are
separated. Different marks remain in competition for a target.

## 3. Exact selector criterion

A selector assigns each target to at most one row/mark. Because a target has
capacity one, row r must receive at least q_r=ceil(delta(p,J)) distinct
targets. By cloning row r q_r times and applying Hall's marriage theorem,
such a selector assignment exists if and only if
[
 |\bigcup_{r\in R}E_r|\ge\sum_{r\in R}\lceil delta_r\rceil
 \quad\text{for every row family R}.
]
The proof and the precise distinction from fractional flow are in the
selector Hall-criterion audit linked above.

This integer Hall condition is stronger than the split-demand inequality
with sum delta_r. The latter can be satisfied by splitting a target between
different marks and therefore does not produce a selector.

## 4. Demand is not automatically at most one

If the parent tree tau has L non-root leaves, attaching the new leaf J to
one of those L leaves gives child leaf count L; attaching J to any other
parent vertex gives child leaf count L+1. Thus, if a fixed (p,J)-fiber has
a such leaf attachments and b other attachments,
[
 delta(p,J)=a/L+b/(L+1).
]
No general argument currently bounds this by one. The selector quota is
ceil(delta), and it must be computed from the actual allowed attachment
vertices.

## 5. Status

The parent-source separation implication is rigorous, conditional on an
injective parent matching Q. The exact selector existence problem is
reduced to the integer Hall condition above. Neither that condition nor an
all-orders canonical-mark selector has been proved. The finite split-demand
max-flow certificates do not establish it: they use all canonical parent
targets and fractional demands, not one fixed representative Q(p) and
rounded row quotas.

The all-orders mixed lift expansion, global cross-fiber Hall inequality,
and weighted one-link inequality remain open.
