# Four-prism loop: exact four-port incidence and fundamental Fourier audit

27 October 2026. Scope: constructed combinatorial 2x2 quadrilateral extrusion, not an authenticated Penrose patch.

## 1. Cellular structure and retained action

The saved incidence file gives 18 vertices, 33 links, 20 faces, 4 prisms. The four deleted/interfacing temporal faces are indexed Q=(3,4,10,13), leaving 16 retained faces. Exact integer identities B1 B2=0, B2 B3=0 are inherited from the previously checked construction. The retained face boundary matrix has rank 15, while the full face matrix has rank 16. Exactly one link, e=10 (central vertical edge), is absent from every retained face and occurs once in each of the four interface faces, with signs (+,-,+,-).

Thus the actual cavity action S0 depends on the other 32 links but not U_e. Its cavity distribution has **exact conditional Haar** for this link, without any approximation and with all 16 retained spatial/temporal Wilson interactions present.

Orient the four interface face words so this common link occurs with exponent +1 (invert the negatively oriented face words). For each frozen exterior v, W_i = A_i(v) U_e B_i(v). All A_i,B_i are SU(2) words in exterior links. No independent one-port factorization follows.

## 2. Interface effective kernel: exact but not evaluated at positive coupling

The union of four interface squares has 13 edges and 10 vertices, hence first Betti number 4. A spanning-tree coordinate change introduces four independent oriented port holonomies h=(h1,...,h4) and 9 tree variables, preserving product Haar. The remaining 20 links are noninterface links. Gauge invariance allows a tree gauge for the 9 interface-tree edges. The **exact** reduced kernel (for fixed corresponding gauge convention) is

    F_beta(h) = ∫_{SU(2)^20} exp[-Σ_{p∉Q} β_p d(W_p(h,v))] dv.

The actual interface measure is proportional to F_beta(h) dh on SU(2)^4; inserted interface faces multiply by Π_i exp[-γ_i d(h_i)]. Under residual diagonal gauge conjugation, F_beta transforms invariantly. A full Fourier coefficient at irreducible multiport index (j1,...,j4) is the matrix

    Fhat_beta(j1,...,j4) = ∫_{SU(2)^4} F_beta(h) ⊗_i D_{ji}(h_i)^* dh.

These are exact finite-dimensional group integrals. At β_p=0 for all retained faces, F_beta(h)=1 exactly; hence only the all-trivial sector is nonzero. At β_p>0, **the full 20-link contraction has not been evaluated**. The conditional computation below must not be mistaken for a proof about Fhat_beta.

## 3. Exactly computed conditional four-port spin-1/2 intertwiner

For a fixed exterior configuration with A_i=B_i=I (after choosing the inverted orientations), h_i=U_e. The fundamental four-port matrix coefficient has the Haar integral

    P = ∫_{SU(2)} D_1/2(U)^{⊗4} dU.

This is the orthogonal projector onto Inv((C²)^{⊗4}). The singlet-pairing tensors ε_{12}ε_{34}, ε_{13}ε_{24}, ε_{14}ε_{23} span the 2D invariant subspace. If S is the 16×3 matrix of these vectors, P=S S^+ (Moore-Penrose pseudoinverse). The verified 16×16 matrix is real symmetric, P²=P and has eigenvalues 1 (multiplicity 2), 0 (multiplicity 14).

For an exterior choice with h_1=-U_e and h_{2,3,4}=U_e, possible by a central -I holonomy on one fixed exterior segment, the corresponding four-port matrix becomes **-P**, with eigenvalues -1 (multiplicity 2), 0 (multiplicity 14). This proves conditional multiport positivity can fail. Other frozen exteriors produce left/right unitary transforms of P, in general not Hermitian. It does **not** show the fully exterior-integrated Fhat_beta is negative. Note that positive semidefiniteness of covariance/moment Gram matrices is a distinct and generally automatic property, unlike positive-definiteness of a function on a product group.

## 4. Support-local single insertion but unresolved joint insertion

Because U_e is conditionally Haar, inserting **one** of the four face weights, with the others absent, gives exactly Z_1/Z_0=q(γ) for arbitrary β on all 16 retained faces. This is cutoff-uniform and independent of surrounding Wilson coupling. Simultaneously inserting all four faces yields the conditional integral

    A_gamma(v)=∫_{SU(2)} Π_{i=1}^4 exp[-γ_i d(A_i(v) U B_i(v))] dU,

and unconditional ratio E_{exterior cavity}[A_gamma(v)]. Fixed exterior choices can make A_gamma exponentially small in γ. Controlling its exterior average requires a new joint correlation comparison; the conditional intertwiner computation does not supply it.

## 5. Reproducibility and scope

`verify.py` reads the saved signed boundary matrices, confirms the interface-only link, reconstructs singlet pairings and computes P and -P by exact finite-dimensional linear algebra (floating-point implementation with 1e-12 verification). `fundamental_blocks.npz` contains both 16×16 matrices and 16×3 spanning vectors; `certificate.json` records checks.

This is a **partial**, noncircular multiport computation. No full positive-coupling Fourier matrix, uniform positivity correction, arbitrary Penrose-support insertion theorem, or continuum mass gap is claimed.
