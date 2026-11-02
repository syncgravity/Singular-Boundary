# Canonical shared-link orientation reconciliation — 2026-11-01

**Status:** exact quaternion symbolic verification for an adjacent two-face original-link model; global gauge-fixed chain and boundary convention still require audit.

Let A=(a,u), B=(b,v), r=Re(AB)=ab-u·v, and T_i=e_i/2. Define R_A and L_B invariant generators, with the shared-link derivative D_i^−=R_A,i−L_B,i. The flow (A,B)→(A exp(tT_i),exp(−tT_i)B) preserves AB. By contrast D_i^+=R_A,i+L_B,i does not. Normalize the operator as K_±=−3Σ_i L_A,i²−3Σ_i R_B,i²−Σ_i (D_i^±)², so Ka=3a and Kb=3b. With Γ(f,g)=Σ(weighted field derivatives of f times those of g), the independent eight-quaternion-coordinate calculation yields:

| Operator action | D− inverse-paired | D+ same-sign |
|---|---|---|
| Kr | 9r/2 | 15r/2 |
| Γ(a,b) | (r−ab)/4 | (ab−r)/4 |
| K(ab) | (13ab−r)/2 | (11ab+r)/2 |
| Γ(a,r) | 3(b−ar)/4 | 5(b−ar)/4 |
| Γ(b,r) | 3(a−br)/4 | 5(a−br)/4 |

The earlier two-face fourth-order audit matches D− exactly. The later three-face quadratic audit matches D+ exactly. **The discrepancy is explained by different relative shared-link orientations, not by changing Γ's definition alone.** With the D− transformation and r=Re(AB), the exact adjacent quadratic Poisson inverse is

[
\boxed{K_-^{-1}\Gamma_-(a,b)=-ab/26+2r/39.}
]

Its substitution gives K_−(−ab/26+2r/39)=(r−ab)/4. The recently recorded expression ab/22−2r/55 instead belongs to D+ and must not be substituted into a D− recurrence.

The physical chain's based-word orientation, possible inverse face holonomies, link incidence, and boundary embedding remain to be audited before declaring which convention is canonical globally. Historical fourth-order coefficients and score claims are not silently superseded. The present proof checks a local shared-link sector, not the entire three-face gauge-fixed Hamiltonian, all-order cancellation, λ=1 convergence, regulator-uniform gap, or continuum Yang–Mills mass gap.

**Reproducibility:** Complete report, executable direct quaternion differentiator, execution log and checksums are in persistent Library Proof Audits as R3_IR_CANONICAL_SHARED_LINK_RECONCILIATION_2026-11-01.zip.

**Research verdict:** Opposite shared-link derivative orientations explain all conflicts in the mixed quadratic operator tables. The inverse-paired original-link flow preserving AB selects the earlier two-face identities for that coordinate convention; a full physical source and cross-volume embedding check is still outstanding.