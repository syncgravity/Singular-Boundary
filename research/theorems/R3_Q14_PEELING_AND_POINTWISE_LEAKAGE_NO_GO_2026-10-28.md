# Q14: exact private-edge core and unavoidable exterior-star leakage

**2026-10-28. New finite-incidence theorem and a pointwise SU(2) center counterexample; not a uniform Gibbs or spectral-gap theorem.** This audit uses original archived Q14 word certificates and full-cover rational witnesses at Penrose disk radii 5, 6.5, 8, 10. No Monte Carlo or historical source regeneration.

## Sources and integrity

Original words: \`R3_historical_wordlevel_2026_10_27_bundle.zip\`, original source/labels: \`R3_recovered_original_2026_10_27_bundle.zip\`, exact rational covers/pair words: \`R3_Q14_full_cover_2026_10_27_bundle.zip\`. The detailed theorem, read-only deterministic audit script, certificate and per-file hashes are in \`singular_boundary_q14_peeling_leakage_2026_10_28.zip\`, SHA-256 \`fb83fd866eaf33fa1eb61ef2684161ce6ac78bfc8ff42ac986bf456190fc0821\`.

Let Q be the original 14 inserted temporal faces, R all other retained faces, F the 54 Bianchi-fill faces. **All links are integrated in this original finite-disk retained partition.** This is not the separately described 12-prism/37-link fixed-boundary object. For edge e, \`st_R(e)\` denotes all retained faces incident to e; define \`S_F = sum_(p in F) (1 - ReTr(W_p)/2)\`.

## Theorem A: exactly six valid private-edge integrations

At all four radii exactly six fill faces have links incident to no other face of the **full retained action**. Sequential deletion of these six leaves a 48-face fill core with no additional private-edge deletions. The six are inside A(H); all ten Bianchi-fill faces outside A(H) remain.

Radius-5 (face,edge): \`(269,507), (276,510), (325,537), (427,597), (439,603), (484,627)\`.

With \`R'=R\P\`, \`F'=F\P\` and \`z(lambda)=2 exp(-lambda) I_1(lambda)/lambda\`:
\[
Z_R=z(\lambda)^6 Z_{R'},\quad
\mathbb E_{R,\lambda}S_F=6\left[1-\frac{I_2(\lambda)}{I_1(\lambda)}\right]+\mathbb E_{R',\lambda}S_{F'},
\quad 0\le\lambda\left[1-I_2/I_1\right]\le3/2.
\]
**This is not a factorization of the inserted numerator** \`Z_(R+Q)\`, because eliminated private edges may occur in Q.

## Theorem B: LP optimum remains 22

The four original 54x101 cover LPs have exact rational primal/dual witnesses of equal objective 22. Every peeled face has **zero dual weight**; every positive-weight primal edge still touches F'. The original primal restricted to 48 constraints and the original dual restricted to 48 coordinates remain feasible and both objective 22. Thus the residual 48-face fractional-cover optimum remains **22**, without resolving a new LP.

On the archived 40 chosen weighted links, the 225 original pair-staple words reduce to **190** after the six deletions: **58** F'-F', **108** F'-external, **24** external-external. **49** distinct exterior star-leakage faces remain. The cover Ward constant is still \`(3/2)*22=33\`; peeling separately contributes at most 9. No unsuppressed staple-frustration bound follows.

## Theorem C: a universal pointwise no-go for nonnegative one-link covers

Of the 101 fill-incident edges, **23** have full retained star in F and **78** leak to R\F. Only **26** fill faces meet a star-closed edge, leaving **28 exposed fill faces** whose four edges all leak. For each of the 78 leaking edges e, the saved words certify a retained exterior-star face g with an edge a not belonging to any fill face; all four disks have this property.

Let arbitrary \`w_e>=0\` satisfy \`sum_(e in ∂p) w_e>=1\` for each p in F. Choose an exposed face p; one of its four edges e has \`w_e>=1/4\`. Choose its certified exterior-star face g with a fresh edge a outside E(F). Set the SU(2) center link \`U_a=-I\` and **every other link to I**. Then \`S_F=0\`, but the star of e has at least one +I and one -I face holonomy. In terms of the exact conditional one-link staple minimum \`m_e = |st_R(e)| - |sum_(r∈st_R(e)) quaternion_staple_(r,e)|\`, one has \`m_e>=2\`. Therefore:
\[
\boxed{S_F=0,\quad \sum_e w_e m_e \ge 1/2.}
\]
Hence **no** finite C yields \`sum_e w_e m_e<=C S_F\` pointwise on all SU(2) configurations for **any** nonnegative one-link fractional cover. Nor can \`C S_F + D/lambda\` uniformly dominate for fixed C,D as lambda grows.

Radius-5 stronger concrete witness: archived optimal cover link \`e=42\`, \`w_42=1/2\`, star faces \`(20,22,252,570)\`; set \`U_52=-I\`. Face 22 is the single -I member, \`m_42=2\`, giving \`sum w m >=1\` while S_F=0.

**Scope:** this is a deterministic no-go for **fill-only pointwise Ward absorption**, not a no-go for correlated **Gibbs-averaged** estimates. The flipped exterior face has nonzero Wilson action; its contribution may be exponentially suppressed under the retained Gibbs law. Nothing here proves a physical mass gap, proves a uniform conditional cavity bound, or establishes equivalence to the older 12-prism object.

## Next proof gate

A useful next step must use exterior-action cost or a joint, nonabelian correlated integration (and boundary conditions stated precisely), rather than reusing a pointwise fill-only cover. The historical **59-pivot finite-net repair source + inputs and certificate**, or the original **12-prism/37-link cavity C,Q boundary partition**, would be precise records worth recovering if available. No Stage 19–26 numerical reruns are requested.
