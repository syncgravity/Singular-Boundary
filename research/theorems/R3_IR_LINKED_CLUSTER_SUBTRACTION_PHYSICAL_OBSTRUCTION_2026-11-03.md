# Physical overlapping Wilson fusion: linked-channel subtraction and nonlinear quotient obstruction (2026-11-03)

**Exact corrected original-link SU(2) theorem.** The prior exact result for shifted fundamental rectangles F_k=χ1(W_[1,k+1]), G_k=χ1(W_[2,k+2]) is

B(F_k,G_k)=k Ψ00/16 + √3 k(Ψ02+Ψ20)/[16(k+3)] −3k Ψ22/[16(2k+3)],

where B=K^-1 Q Γ_K, the Ψ_cd are four orthonormal *physical Gauss-invariant* original-link spin-network electric eigenstates, and their energies are 6,6+2k,6+2k,6+4k. The dominant Ψ00=H_k is the product of two link-disjoint end-plaquette fundamental Wilson characters; it is **not** a constant and has physical energy 6.

**Uniform remainder:** Define R_k=B(F_k,G_k)−k H_k/16. Orthogonality and the exact four-channel coefficients give

||R_k||_(SN,1)=√3 k/[8(k+3)]+3k/[16(2k+3)] < √3/8+3/32,
||R_k||_2²=3k²/[128(k+3)²]+9k²/[256(2k+3)²] <33/1024.

Both bounds hold for every k≥1 and are sharp as k→∞. They describe one special connected-input overlapping-loop family, not a general all-width nonlinear theorem.

**SUBTRACTION DOES NOT SOLVE THE ORIGINAL POISSON EQUATION:** Since K H_k=6H_k,

K R_k=Q Γ_K(F_k,G_k)−(3k/8)H_k.

The missing source is a nonzero physical spin-network mode; it cannot be removed by constant centering Q. Any linked-cluster subtraction must track an explicit compensation/reconstruction sector.

**NAIVE CONNECTED-SUPPORT QUOTIENT IS NOT NONLINEARLY CLOSED:** Let x=χ1(A), y=χ1(B) be two *original-link disjoint* plaquette fundamental Wilson loops (for example faces 1 and 3), u=χ2(A), and H=xy. Physical electric energies are Kx=3x, Ky=3y, Ku=8u, K(uy)=11uy, with SU(2) character fusion x²=1+u. The carré du champ is Γ_K(H,x)=y Γ_K(x,x)=y(3−u). Consequently the exact physical centered response is

**B(H,x)=y−(1/11)u y.**

Define P_conn on a fixed original-link spin-network eigenbasis to retain *connected minimal nontrivial original-edge support* and discard disconnected support. Then P_conn H=0, P_conn x=x, but **P_conn B(H,x)=y≠0**. So P_conn B(F,G) ≠ P_conn B(P_conn F,P_conn G). The discarded sector is not an ideal of B and can feed connected output channels at the next nonlinear order. Hence simply projecting away disconnected-output spin networks is not a valid autonomous linked-cluster recurrence.

**Correct distinction:** minimal original-edge support (possibly disconnected), connected interaction/hull history (the union of the two input rectangles, width k+2), and cumulants/logarithmic interactions of a specified measure are different notions. A factorized eigenfunction is not automatically a deletable cumulant. An exact decomposition retains both (R_k,kH_k/16) with cross terms and reconstruction, or retains a connected union-hull label and pays for overlap via weights. The particular dominant-channel normalized weight ratio from the archived report is k e^{−(κ+4σ)k} 9^s/[16(2k+5)^{2s}], uniformly bounded for κ+4σ>0; no all-channel weighted closure follows.

**Verification:** independent exact SymPy Q(√3) checks and the previous complete projector/fusion verifier rerun; 7,500 additional exact rational channel assertions for k=1,...,500. The full detailed report, executable verifier, passing log and SHA-256 manifest are archived in The Singular Boundary / Proof Audits.

**Research boundary:** A legitimate cumulant linked-hull calculus and arbitrary-width physical coefficient bound remain open. No interacting λ=1 gap or continuum four-dimensional Yang–Mills mass gap has been proved.