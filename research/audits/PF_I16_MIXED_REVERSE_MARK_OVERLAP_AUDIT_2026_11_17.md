# PF-I16: mixed reverse-mark overlap audit and continuation checkpoint

Date: 2026-11-17

Branch: `research/pf-i16-admissible-exchange-2026-11-16`

Parent branch head checked immediately before this write:
`c80f4c67e94b4039f78ca0ae4b414419f6475401`.

Status: **research checkpoint; no new Hall theorem proved**.

## 1. Purpose and source-of-truth rule

This record preserves the continuation work on mixed Type I/Type II reverse-mark collisions. It is deliberately an audit/checkpoint rather than a theorem claim. The all-orders Hall condition for the multivalued-π relation remains open. The weighted one-link inequality remains conditional on that all-orders Hall theorem.

Use the exact guarded-switch semantics in:

- `research/audits/PF_I16_GUARDED_SWITCH_REVALIDATION_2026_11_16.md`;
- `research/audits/PF_I16_REVERSE_SWITCH_TARGET_CONGESTION_2026_11_17.md`;
- `research/audits/PF_I16_MULTIVALUED_PI_ALL_ORDERS_PROOF_PROGRAM_2026_11_16.md`.

Do not import an informal mark-type label unless its marked pair is checked against the ordered four-endpoint pattern and the no-reinsertion guard in the first record.

## 2. Established framework retained

For a fiber (F=(p,J)), its demand is
[
delta_F=sum_{xin F}rac{1}{d(x)}.
]
For a target (T), let (mathcal R(T)) be its eligible reverse marks/fibers, with eligibility requiring the exact parent-canonical condition (P_J(T)in C_{m can}(p)).

The mixed-fiber Hall condition has the exact weighted dual form
[
sum_Fdelta_F z_F
le
sum_Tmax_{Finmathcal R(T)}z_F
qquad(z_Fge0).
	ag{MR}
]
For a Type I/Type II partition, set
[
A_T=max_{Finmathcal R_I(T)}z_F,qquad
B_T=max_{Finmathcal R_{II}(T)}z_F,
]
with empty maxima zero, and
[
S_I=sum_TA_T-sum_{Fin I}delta_Fz_F,qquad
S_{II}=sum_TB_T-sum_{Fin II}delta_Fz_F.
]
Then (MR) is equivalent to
[
sum_Tmin(A_T,B_T)le S_I+S_{II}.
	ag{MO}
]
This is an exact reformulation, not a structural proof. In particular, the maximum is over all eligible parent centers at the target; parent-source multiplicity must not be discarded.

The exact target-side congestion decomposition in
`PF_I16_REVERSE_SWITCH_TARGET_CONGESTION_2026_11_17.md`
also remains controlling: for fixed ((T,J)), the inverse parent target (P_J(T)) is unique, but distinct marks (J) and distinct parent sources can still collide at the target. The desired target congestion estimate (TC) remains open.

## 3. Configurations examined in the conversation

Two local overlap shapes were examined as potential exceptions to a proposed third-mark repair.

### A. Five-vertex path

The target shape was
[
ell-u-b-c-v
]
with displayed mixed marks (J_I={b,c}) and (J_{II}={ell,b}). Their four-vertex supports overlap in ({u,b,c}), and both marks contain (b).

### B. Branching five-vertex tree

The target shape had edges
[
ell b,quad bc,quad be,quad cv,
]
with displayed mixed marks (J_I={ell,b}) and (J_{II}={ell,c}). Their supports overlap in ({ell,b,c}), and both marks contain (ell).

The conversation then asserted candidate complete lists of locally valid marks and concluded that no third mark survives either inverse. **Those complete-list assertions are not yet certified and must not be cited as lemmas.** The exact ordered endpoint condition is easy to misapply: in the guarded forward move, the inserted interval endpoints and the old-edge endpoints alternate, so the marked pair must be one of the two alternating pairs in the sorted four-endpoint set. The informal Type I/II table used in the conversation has not yet been replayed against the exact three guarded local trees (S_0,S_1,S_2), the no-reinsertion guard, and the inverse incidence test.

Accordingly, the only safe facts to retain from this exploration are the displayed tree shapes and the displayed candidate marks. Whether they are valid reverse marks of the stated types, whether the lists are exhaustive, and whether a third mark is blocked must be checked mechanically and then proved from the local pattern table.

## 4. What the local exploration does and does not imply

Even if a target has two valid mixed reverse marks and no third compatible local inverse, that is only a target-local statement. It does not imply a Hall deficiency. The two corresponding fibers may have additional targets elsewhere in their common canonical neighborhoods.

For an eligible pair (F_I,F_{II}) colliding at (T), define
[
E(F_I,F_{II};T)=
igl(N(F_I)cup N(F_{II})igr)setminus{T}.
]
A pairwise Hall check requires
[
delta_{F_I}+delta_{F_{II}}
le 1+|E(F_I,F_{II};T)|.
]
For larger families, the full weighted union condition is required; pairwise checks alone do not establish it.

A valid nonlocal compensation lemma must retain:

1. exact reverse-mark validity under the guarded-switch inverse;
2. parent-canonical eligibility (P_J(T)in C_{m can}(p));
3. distinct parent centers (p), including repeated parent-target incidences;
4. split demands (delta_F), not unweighted mark counts;
5. target capacity one, including collisions from different marks at the same target.

A third locally valid mark is neither necessary nor sufficient for the required expansion.

## 5. Required next audit before further lemma claims

1. Implement or extract a target-side reverse-mark enumerator directly from the guarded-switch code. For each target (T), enumerate every candidate interval (J), reconstruct (P_J(T)), and check the full inverse conditions, including the no-reinsertion guard.
2. Apply that enumerator to configurations A and B with explicit ordered port labels. Report the complete valid-mark list and the Type I/II signature of each mark. Do not infer a mark type from a drawn tree without checking the sorted endpoint pattern.
3. For each valid mark, compute its actual parent source(s) and test (P_J(T)in C_{m can}(p)). Keep local validity and canonical eligibility as separate predicates.
4. Only after steps 1–3, test whether any other mark remains valid after a first inverse. Distinguish local validity after inversion from membership in the canonical neighborhood of the twice-reduced source.
5. If no local repair exists, test nonlocal expansion in the exact fiber neighborhoods. A finite computation is diagnostic only; a proof must establish a demand-sensitive bound for arbitrary fiber families or an equivalent target-capacity allocation.

## 6. Dependencies and proof boundary

The following existing records remain the relevant dependencies:

- `PF_I16_MULTIVALUED_PI_ALL_ORDERS_PROOF_PROGRAM_2026_11_16.md`: exact multivalued-π relation and global capacity-sensitive lifting obligation.
- `PF_I16_CUT_CLASS_LOCAL_HALL_THEOREM_2026_11_17.md`: same-first-overcrowded-cut individual/fixed-fiber expansion; does not prove Hall for unions of fibers.
- `PF_I16_BLOCKWISE_SPLIT_DEMAND_HALL_REDUCTION_2026_11_17.md`: sufficient blockwise split-demand quotient Hall reduction; all-orders condition remains open.
- `PF_I16_CROSSING_FIBER_SPLIT_HALL_TEST_2026_11_17.md`: finite crossing-fiber flows only.
- `PF_I16_REVERSE_SWITCH_TARGET_CONGESTION_2026_11_17.md`: exact reverse-mark congestion decomposition and open target-capacity criterion.
- `PF_I16_MATCHING_RELATIVE_EXCHANGE_CRITERION_2026_11_17.md`: finite matching-relative strict-Hall diagnostic; not an all-orders construction.

The finite n=8/n=10 flows and the n=10 matching certificate remain finite evidence. They do not prove all-orders Hall. No unconditional weighted one-link inequality is claimed. No Yang--Mills mass-gap conclusion follows.

## 7. Disposition

This checkpoint records the two candidate local overlap configurations and the precise verification work needed to validate or reject the proposed blocking-core observation. It intentionally does **not** promote the conversation's unverified complete-mark lists or no-third-mark conclusions to repository theorem status.

Next mathematical target: after the local reverse-mark census is verified, establish a nonlocal, demand-sensitive expansion/capacity estimate for the eligible neighborhoods of mixed Type I/Type II fibers.
