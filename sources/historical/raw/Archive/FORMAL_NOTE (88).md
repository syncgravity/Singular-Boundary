# R3 three-step two-defect coefficient in the spatial gauge-invariant spin-network basis
Date: 2026-10-27

## Scope and important non-result
Verified calculation for the assembled nine-vertex, twelve-edge, four-plaquette spatial disk; its three-step periodic extrusion has 27 vertices, 63 edges, 48 faces and 12 prisms. Exact positive one-plaquette spin-network sector calculated, but **the complete two-defect mixed coefficient is not computed** and its positivity remains open. The spatial disk is not a provenance-certified Penrose patch.

## Exact expression for the full coefficient
Let H=L²(SU(2)^E)^G be the gauge-invariant spatial Hilbert space (normalized Haar). Use orthonormal spin-network functions Ψ_α, with Ψ_0=1. Spatial Wilson multiplication F=M_f for f(U)=prod_{a=1}^4 exp[-κ d(W_a(U))] (equal spatial coupling). The normalized temporal operator for a time step with edge couplings t_e is the tensor product of SU2 Wilson convolutions, restricted to H. A spin-network basis diagonalizes it: K_t Ψ_α=k_α(t) Ψ_α, k_α(t)=prod_e I_{2j_e(α)+1}(t_e)/I_1(t_e). At t_e=0 interpret eigenvalue as 1 for j_e=0 and 0 for j_e>0. For the special baseline of *all temporal faces absent* K_0=|0><0|. With nonuniform temporal edge supports S_1,S_2 in steps 1 and 2 and no temporal faces in step 3, K_1=K_0+D_1, K_2=K_0+D_2, D_i>=0, and

T_new = Tr(F K_1 F K_2 F K_0), T_old = F_00³,
T_new-T_old = sum_{α≠0} (x_α+y_α) |F_{0α}|² F_00 + M,
M = sum_{α,β ≠0} x_α y_β F_{0α} F_{αβ} F_{β0},
where x_α=k_α(S_1), y_β=k_β(S_2), F_{αβ}=∫ f conj(Ψ_α) Ψ_β dU. (The first linear term weights x for first interval and y for second; Hermiticity makes the coefficients equal.) All sums are absolutely convergent at finite coupling, subject to ordinary trace-class regularity. **The sign of M is not determined by PSD of F**, because F_{αβ} need not be entrywise nonnegative in the spin-network basis.

## Exact one-plaquette fundamental principal block
On the simply-connected four-face spatial disk, there is a gauge-fixed change of variables from links to four independent plaquette holonomies h_a with product Haar measure. Define Ψ_a=χ_{1/2}(h_a) for a=1,...,4. These four functions and Ψ_0=1 are orthonormal in the FULL spatial Haar gauge-invariant Hilbert space (they are not a complete basis). Each Ψ_a is a spin-network eigenfunction of temporal convolution, with spin 1/2 on its four perimeter links and 0 elsewhere. Define
q=q(κ)=2e^{-κ}I_1(κ)/κ,
r=I_2(κ)/I_1(κ), s=I_3(κ)/I_1(κ), m=2r, b=1+3s.
The **exact full-spatial-integral** principal matrix on span{Ψ_0,Ψ_1,...,Ψ_4} is
F_{00}=q⁴, F_{0a}=q⁴ m, F_{aa}=q⁴ b, F_{ab}=q⁴ m² for a≠b.
Every entry is nonnegative. Consequently the contribution to M from α,β among the four one-face spin networks is nonnegative, and explicitly
M_one-face = q¹² m² [m² (Σ_a x_a)(Σ_b y_b) +(b-m²) Σ_a x_a y_a],
where x_a=prod_{e∈∂a}I_2(t_e^(1))/I_1(t_e^(1)) (zero if an edge has t_e=0) and similarly y_a. (Equivalently directly sum F_{0a} F_{ab} F_{b0}; formula applies with b-m² potentially positive, which follows from positivity of variance of χ under Wilson distribution.) This is a *sector contribution*, not an independently defined positive Gibbs probability, and other spin-network sectors can cancel it.

At κ=2, q=0.21526928924893768, m=0.8662548534446234, b=1.4012354396661293. Summing all four indices with x_a=y_a=1 gives 1.085720210181893e-7 (unweighted sector contraction); the true Wilson coefficients multiply by small nonnegative x,y.

## Rigorous but ambient-size finite-volume bound
The full three-step product complex has 63 links, 27 vertices and hence 37 gauge-fixed independent links. With every face coupling at most c_+ λ, a product of 37 SU2 Haar balls of radius O(λ^-1/2) around the flat identity gives Z_full>= exp(-C) c^37 λ^(-3*37/2), while Z_cavity<=1. Hence for λ>=1, the insertion free energy obeys
0<=F_Q<= (111/2)log λ+C(37,c_+, incidence).
This is large-λ logarithmic on the *fixed assembled complex*, but **NOT** the target uniform C|Q| log λ in arbitrary Penrose cavities. The global small-ball bound pays for all physical links.

## Conclusions
1. Derived exact full spin-network mixed coefficient formula; verified a strictly nonnegative fundamental single-plaquette 5x5 principal block.
2. No cancellation theorem or coupling-uniform support-local lower bound for the **complete** mixed coefficient follows.
3. The uncomputed part is the spin networks with multiple loops and nontrivial intertwiners plus all their cross terms with the one-face sector. Negative gauge-fixed multiport Fourier blocks from the earlier isolated four-prism problem do not alone determine the sign of F_{αβ} here.
4. Next credible computation: finite spin cutoff on each of twelve spatial links, exact edge-Haar intertwiner contractions for F_{αβ}, and certified truncation errors **relative to the desired insertion lower bound**. The existing absolute character-tail control is not sufficient at λ→∞ for fixed cutoff.
