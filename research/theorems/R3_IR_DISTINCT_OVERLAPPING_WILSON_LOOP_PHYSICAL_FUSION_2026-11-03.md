# Exact physical fusion of distinct overlapping SU(2) Wilson loops — November 3, 2026

**Theorem, finite original-link SU(2) square ladder and theta graphs.** The previously archived same-loop Wilson-character fusion theorem extends to distinct simple loops sharing one or two original-edge paths. These statements use the physical original-link electric generator, not the invalidated nearest-neighbor face ansatz. The complete 206-line proof and independent exact-rational verifier are archived in The Singular Boundary / Proof Audits.

Let C_n=n(n+2)/4 and B(f,g)=K^-1Q Γ_K(f,g). For physical normalized eigenfunctions f,g (energies E_f,E_g) and a normalized output eigenfunction Ψ of positive energy E, the **exact multiplier** is

    <Ψ,B(f,g)> = (E_f+E_g-E)/(2E) <Ψ,f g>.

**One shared contiguous path / theta graph.** The two loop boundaries have an opposite-oriented common path of s>=1 edges and exclusive paths of x,y>=1 edges. For SU(2) characters χ_a and χ_b, the possible common-edge output labels c=|a−b|,|a−b|+2,...,a+b have **orthonormal fusion-channel amplitudes**

    α_c = sqrt((c+1)/((a+1)(b+1))).

Their exact electric energies and Poisson coefficients are

    E_c = x C_a + y C_b + s C_c,
    B_c = α_c s(C_a+C_b−C_c)/(2 E_c).

There are exactly min(a,b)+1 channels independent of perimeter. The explicit coefficient-l1 bound is ||B||_SN1 <= (1/2) max(s/min(x,y),1) sqrt(min(a,b)+1). For adjacent nonoverlapping rectangles of p and q faces, s=1, x=2p+1, y=2q+1. At p=q=1 and a=b=1 this returns the independently validated **B=+Ψ_0/12−sqrt(3) Ψ_2/52** (the Ψ_0 channel is a nonconstant six-link outer Wilson loop, not the vacuum).

For a=b=m, the common singlet coefficient is **s/[(m+1)(x+y)]**. Hence arbitrarily long shared paths with fixed exclusive lengths cause real linear growth on general theta graphs, even though the same-loop perimeter cancels exactly.

**Two disjoint shared paths / partially overlapping rectangles.** Suppose shared path lengths are s1,s2>=1, both traversed with the same orientation, with independent nonempty exclusive pieces of total lengths x,y. On each shared path, SU(2) Clebsch–Gordan labels c,d run over |a−b|,...,a+b in increments of two. The normalized channel amplitudes, electric energies and complete physical Poisson coefficients are

    α_cd = sqrt((c+1)(d+1))/((a+1)(b+1)),
    E_cd = x C_a + y C_b + s1 C_c + s2 C_d,
    B_cd = α_cd [s1(C_a+C_b−C_c)+s2(C_a+C_b−C_d)]/(2 E_cd).

There are exactly (min(a,b)+1)^2 orthogonal channels, independent of total perimeter and shared-path lengths. The corresponding explicit coarse bound is ||B||_SN1 <= (1/2) max((s1+s2)/min(x,y),1)(min(a,b)+1). These amplitudes follow analytically from orthogonal Clebsch–Gordan projectors on each shared path plus Schur orthogonality on four independent exclusive segments; the Haar norm squared is (c+1)(d+1)/[(a+1)(b+1)]².

Rectangles enclosing p and q faces with k partially overlapping faces (1<=k<min(p,q), neither contained in the other) share top and bottom paths with s1=s2=k and have exclusive lengths x=2(p+1−k), y=2(q+1−k).

For the 3-face configuration [1,2] and [2,3] at fundamental spin, channels (00,02,20,22) have electric energies (6,8,8,10) and the **exact response**

    B = Ψ_00/16 + sqrt(3)(Ψ_02+Ψ_20)/64 − 3 Ψ_22/80.

Its canonical coefficient-l1 norm is 1/10+sqrt(3)/32 and physical Hilbert norm squared is 347/51200.

**All-width physical counterexample on connected input loops.** Put F_k=χ_1(W_[1,k+1]) and G_k=χ_1(W_[2,k+2]), k>=1. They are normalized physical spin networks with energies 3(k+2)/2 each, and share two separate original-link paths of length k. Here x=y=4. The exact four-channel response is

    B(F_k,G_k) = (k/16)Ψ_00
      +[sqrt(3)k/(16(k+3))](Ψ_02+Ψ_20)
      −[3k/(16(2k+3))]Ψ_22.

Ψ_00 is the normalized product of the *two separated end-plaquette fundamental Wilson characters* and has electric energy 6. Its coefficient k/16 is independently established without relying on full recoupling: letting P=A_1, U=A_2...A_(k+1), Q=A_(k+2), the physical product Haar orthogonality identities give <χ_1(PU)χ_1(UQ),χ_1(P)χ_1(Q)>=1/4. The multiplier [3(k+2)−6]/(2*6)=k/4 gives k/16. Therefore **||B(F_k,G_k)||_L2 >= k/16** and **||B(F_k,G_k)||_SN1 >= k/16**. This is a genuine fixed-spin, all-width obstruction to any unweighted volume-uniform bilinear algebra on these connected Wilson-loop inputs. The growing output channel has disconnected *actual* support and must be treated carefully in linked-cluster/cumulant conventions.

**Weighted regularity qualification:** Assign both inputs connected hull width k+1 and the output the union hull width k+2. With face-hull exponent κ, per-original-edge total degree exponent σ, and polynomial degree moment s, the exact normalized Ψ_00 channel ratio is

    (k/16) exp(−κ k−4σ k) * 9^s/(2k+5)^(2s).

At κ=σ=0 this channel prevents a same-grade estimate for s<1/2; a positive κ or σ suppresses it. This does NOT establish sufficiency for any weighting or a nonlinear fixed point. It neither proves the interacting λ=1 lattice gap nor the continuum four-dimensional Yang–Mills mass gap.

**Verification:** Exact independent spin-Casimir/projector checks, rational fusion identities and full shifted-rectangle formula through k=500, plus a separate binary-tetrahedral SU(2) 24-element exact Haar quadrature of the crucial projection 1/4. **87,009 tests passed.** Complete proof, executable checker, log and SHA256 manifest are in The Singular Boundary / Proof Audits.