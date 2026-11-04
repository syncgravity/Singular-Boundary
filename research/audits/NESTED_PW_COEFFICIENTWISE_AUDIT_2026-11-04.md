# Independent nested original-link SU(2) Peter–Weyl regression — 2026-11-04

**Status: exact shared-link two-face finite calculation. The arbitrary-spin coefficientwise local-first tame theorem remains unverified.** This is new independent testing of that theorem's smallest genuinely nested original-link case, not a mass-gap proof.

## Correct physical model

Two adjacent square plaquettes of an open straight strip have face holonomies A,B∈SU(2) and corrected original-link electric generator K=4(C_A+C_B)+2D, D=∑_a R_{A,a}L_{B,a}, C=-∑R_a². Original-link differential generators are T_a=iσ_a/2. This is the model and sign convention of research/theorems/R3_IR_EXACT_ALL_LENGTH_PETER_WEYL_SPECTRUM_2026-11-01.md. Do **not** replace K with the separate-face rotor operator.

Take physical (gauge-invariant) observables x=χ₁(A), y=χ₁(B), u=χ₂(A)=x²−1. Let F=xy carry outer connected history [1,2] and G=x carry inner history [1]. Their plaquette loops share an original physical edge. With Γ_K(F,G)=(F KG+G KF−K(FG))/2 and B=K⁻¹QΓ_K, put T=D(uy).

Quaternion derivatives on SU(2) give the exact identities
- D(xy)=\vec A·\vec B and T=D(uy)=4A₀(\vec A·\vec B).
- Kx=3x, Ky=3y, K(uy)=11uy+2T, K(T)=uy+10T.
- Γ_K(xy,x)=(3−u)y−T/2; all source terms have zero Haar constant.

In the {uy,T} basis the positive electric K matrix is [[11,1],[2,10]], determinant 108. Thus the exact response is

**B(xy,x)=y−(19/216)u y−(7/216)T.**

The output y, which depends only on B, is a genuine physical mode with energy 3 and **must not be discarded** by a connected-minimal-support quotient.

## Independent coupled-spin coefficientwise calculation

The output (n_A,n_B)=(2,1) representation contains spins 1 and 1/2. For D=J₁·J₁/₂, eigenvalues are −1 (multiplicity 2) and 1/2 (multiplicity 4); K eigenvalues 9 and 12 as expected from the exact all-length spectrum. The matrix Peter–Weyl coefficient is C₂,₁=−(19/216)I₆−(7/216)D with eigenvalues −1/18 (multiplicity 2) and −5/48 (multiplicity 4), hence **||C₂,₁||_{S₁}=19/36**. The (0,1) y block has coefficient I₂, nuclear norm 2.

With face-degree PW projective norm Pσ(f)=∑_n d_n exp(σ|n|)||A_n||_{S₁}, d_n=∏(n_i+1), the exact norms are

- Pσ(x)=4e^σ, Pσ(xy)=16e^{2σ}.
- **Pσ(B(xy,x))=4e^σ+(19/6)e^{3σ}.**
- Corresponding unweighted-history local-first output L¹ equals **8e^σ+(19/2)e^{3σ}**; input F has L¹=32e^{2σ}, inner G has L²=16e^σ.
- Including outer history weight e^{2κ} and inner e^κ, the exact tame input/output ratio is **e^{-κ}(8e^{-2σ}+19/2)/512**, bounded for κ>0,σ≥0.

This verifies for this one **nontrivial shared-edge** physical pair the differential source, its exact coupled electric inversion, coefficientwise PW block decomposition, nuclear sums and nested history label. It is not an all-spin or arbitrary-width operator inequality.

## Reproducibility

The committed independent SymPy verifier computes exact quaternion left/right fields, reduces only by the two SU(2) unit-sphere relations, verifies nine polynomial identities, and separately constructs the spin-1 ⊗ spin-1/2 6×6 block. All checks passed. Original local script SHA-256: 8290324da39f56bb023ee3ed48f97af5b971b7bd1ca132759fa78c50fa58597b.

## Decision

**PASS** one genuine nested two-face original-link regression. **OPEN** the inherited coefficientwise arbitrary-spin, arbitrary-width Peter–Weyl tame estimate and its exceptional-Casimir counting. The November 4 local-first Borel-disk consequence remains **conditional**. Next test the family χ_n(A)χ₁(B) against χ₁(A) at unrestricted n, then a genuinely three-face nested channel; retain all physically nonconstant disconnected-support outputs. Do not transfer these straight-strip results to a 3D Penrose or cubic regulator without P0 model certification.

No positive-coupling convergence, interacting physical spectral gap or 4D continuum mass-gap proof is claimed.
