# Authenticated Penrose Q14 word-level incidence and contraction audit

**Source:** `R3_uploaded_gaussian_audit_2026_10_27_bundle.zip`, files `cavity_audit.py`, `verify_bianchi.py`, `construct_surgery.py`, and the original direct Z^5 generator. The canonical face labels are taken from the previously extracted `HISTORICAL_Q14_CANONICAL.json`. This is the ORIGINAL Q14, not an alternative 14-face example.

## Reproduction

`python certificate.py --canonical-Q historical_Q_labels.json` and `python verify_words.py` and `python audit_contraction.py` (NumPy required). All four radii 5, 6.5, 8, 10 reproduce Q=14, H=36, A(H)=62, 54 Bianchi-fill faces, a maximum of 17 factors per peeled inserted word, 84 distinct pair-staple words among the retained face-stars at H, and exact quaternion numerical trace agreement to <5e-16. The original `verify_bianchi.py` independently verifies the weighted coefficient 44. The `certificate.py` field `max_energy_coeff=4` is the **unweighted occurrence multiplicity**, not the energy inequality constant; the latter incorporates squared factor lengths and is 44.

## A crucial correction to the earlier Ward route

The exact original fill set intersects A(H) in **44** faces. There are **10 fill faces outside A(H)**, hence the union has 54+62-44=72 retained faces. Accordingly, the previous statement `A_fill subset A(H)` and derived estimate `lambda E S_fill <=54+lambda sum_{e in H} E m_e` were **invalid** for the original Q14: the nonnegative covering inequality `S_fill <= sum_{e in H} S_e` does not apply. The 54-face energy estimate must cover all 54 faces using additional links, or independently control the 10 exterior fill faces.

The valid universal fractional-cover inequality for any face set F and any set C of links meeting every face, with nonnegative weights w_e satisfying sum_{e in boundary(p) intersect C} w_e >=1, remains:

`lambda E S_F <= (3/2) sum_e w_e + lambda sum_e w_e E m_e`.

## Pair-staple words

For each H link and incident retained face p, the certificate stores `staple_word` with `d(W_p)=1-<U_e,staple>` under SU(2) quaternion conventions. For each pair, it stores a fully free-reduced `loop_word` of the product of the first staple by inverse of the second. The `verify_words.py` script evaluates each word on random SU(2) quaternion links independently and checks the exact equality numerically. This provides a source of explicit noncommutative loop words but does **not** prove any special domination coefficients between these loops and a chosen set of retained faces.

## The elementary B matrix is NOT contractive

For each p in A(H), select an incident e(p) in H with the fewest retained faces at that link, and use the always valid bound `m_e <= S_e = sum_{r incident to e} d(W_r)`. The associated explicit 62x62 nonnegative matrix B is stored in `elementary_B_radius_*.npz` (with face and link order labels). It has B_pp =1 for every p, so rho(B)>=1 by elementary nonnegative-matrix monotonicity. Numerical spectral radii are 4.0 on all four disks. This rules out strict contraction from this naive matrix, **not** from every possible word-level/Bianchi-reduced matrix.

An important additional logical point: `x_p=lambda E d(W_p) <= (3/2) + lambda E m_e` uses the inequality d(W_p)<=S_e and the one-link Ward estimate, valid for e incident to p. The matrix closure needs a genuine deterministic `m_e <= sum_r B_pr d(W_r)` with exterior leakage controlled; the pair-staple word lists alone do not establish it.

## Status

Authenticated geometry, exact word inventory, original Q14 canonical labels, exact 54-face fill and 84 pair words: **recovered and checked**.

Unconditional nontrivial B with rho<1, uniform Gibbs suppression of staple frustration, arbitrary nonstationary R3: **not proved**. The next concrete task is to optimize a fractional cover of the complete 54-fill set on the 72-face union, and derive true nonabelian inequalities for pair-staple loop words that account for the 10 exterior fill faces.
