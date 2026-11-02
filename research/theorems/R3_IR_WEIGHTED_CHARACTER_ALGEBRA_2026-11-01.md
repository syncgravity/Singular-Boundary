# R3-IR — Weighted SU(2) character algebra and bilinear Poisson operator

**Date:** 2026-11-01. **Status:** Proved for one-link central functions, not the full multi-link gauge-invariant chain.

Let χ_n be the SU(2) characters, λ_n=n(n+2)/4, and define ||Σ f_nχ_n||_{Aρ}=Σ|f_n|(n+1)e^{ρn}. Define B=K⁻¹P₀Γ_K, K=−ΣX_k², Γ_K(f,g)=Σ(X_kf)(X_kg).

**Algebra:** χ_mχ_n=Σ_{j=0}^{min(m,n)}χ_{m+n−2j}. The corresponding dimensions sum to (m+1)(n+1), so ||fg||_{Aρ}≤||f||_{Aρ}||g||_{Aρ} for every ρ≥0.

**Bilinear Poisson closure at ρ>0:** B(χ_m,χ_n)=Σ_{j:l=m+n−2j≥1}[(λ_m+λ_n−λ_l)/(2λ_l)]χ_l. The normalized weighted coefficient sum is
C_{m,n}(ρ)=Σ_{j:l≥1}|(λ_m+λ_n−λ_l)/(2λ_l)|[(l+1)/((m+1)(n+1))]e^{−2ρj}.
This is uniformly bounded for any fixed ρ>0: assume m≥n. If m≥2n, then l≥m/2 and the eigenvalue ratio is O(1); the CG-weighted sum ≤1. If n≤m<2n, split j≤n/2 (l≥m, ratio O(1)) and j>n/2 (ratio O(n²), dimension ratio O(1/n), and the geometric tail is O(e^{−ρn}/(1−e^{−2ρ}))). Thus B:Aρ×Aρ→Aρ is bounded for fixed ρ>0.

**Failure at ρ=0:** For m=n=N, output χ_{2k}, 1≤k≤N/4, has coefficient λ_N/λ_{2k}−1/2≳N²/k². Weighted by (2k+1)/(N+1)², these contribute ≳1/k. Consequently C_{N,N}(0)≳log N→∞: B is unbounded A₀×A₀→A₀, although A₀ is a multiplication algebra.

**Verification:** Exact finite character sums were tested for m,n<100, ρ∈{0,0.01,0.05,0.1,0.5}, multiplication checks for m,n<70, and diagonal n through 2048. Local verifier, log and SHA256 manifest are archived in Library.

**Scope:** The class-function algebra does not extend automatically to shared-link multi-face functions or full matrix coefficients. No all-orders connected convergence, λ=1 interacting gap, or continuum mass gap is proved. Next task: construct full matrix-coefficient weights with controlled Clebsch–Gordan multiplicities and shared-link derivatives.