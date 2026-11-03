# SU(2) class-function ℓ¹ same-radius Poisson algebra and adjacent shared-link obstruction — 2026-11-02

## Definitions
On one SU(2) face, let χ_j be normalized Haar-orthogonal SU(2) characters, Lχ_j=λ_jχ_j with λ_j=j(j+2)/4, L=−Δ, and Q Haar centering. Let Γ(f,g)=<∇f,∇g>. Define A_σ on class functions f=Σ_j c_jχ_j by ||f||_(A_σ)=Σ_j e^(σj)|c_j|, σ>0.

## Exact positive-radius theorem
The Clebsch–Gordan product χ_jχ_k=Σ_{ℓ=|j−k|, ℓ≡j+k mod 2}^{j+k} χ_ℓ and L(fg)=fLg+gLf−2Γ(f,g) yield, for ℓ≥1,
[χ_ℓ]L^(-1)QΓ(χ_j,χ_k)=(λ_j+λ_k−λ_ℓ)/(2λ_ℓ).
Write m=j+k, ℓ=m−2r. Because λ_j+λ_k≤λ_m and λ_m/λ_ℓ≤(1+2r)²,
|[χ_ℓ]L^(-1)QΓ(χ_j,χ_k)| ≤1+2r+2r².
Let z=exp(−2σ). Since e^(σℓ)=e^(σ(j+k))z^r, coefficient ℓ¹ summation gives
**||L^(-1)QΓ(f,g)||_(A_σ) ≤ [(1+z)²/(1−z)³] ||f||_(A_σ)||g||_(A_σ)**.
This is a bounded bilinear same-radius map for all σ>0, including at unchanged analytic radius. Character multiplication itself satisfies ||fg||_(A_σ)≤(1−z)^(-1)||f||_(A_σ)||g||_(A_σ). Small-σ bound diverges like (2σ³)^(-1). In the archived original-link one-face convention K=4L, Γ_K=4Γ_L, this is precisely K^(-1)QΓ_K.

## Sharp qualitative boundary at σ=0
||χ_N||_(A_0)=1 whereas the χ_2 output coefficient of L^(-1)QΓ(χ_N,χ_N) is N(N+2)/8−1/2→∞. Thus the unweighted character ℓ¹ algebra fails for the quadratic Poisson map.

## Adjacent-face obstruction
For adjacent face holonomies A,B with a=Re A, b=Re B, the corrected original-link identity is Γ(a,b)=(ab−Re(AB))/4. Choosing A=i and B=i,j,−i holds a=b=0 but yields Γ=1/4,0,−1/4. Therefore the algebra of independent face characters is NOT closed under shared-link gradients: coupled invariants Re(AB) or full matrix-coefficient data are mandatory. The one-face theorem does not establish multi-face polymer closure, a λ=1 interacting spectral gap, nor a continuum Yang–Mills mass gap.

## Verification
Exact-rational checker verifies 255,255 contributing character coefficients for j,k≤90, 100 generating-function coefficients, zero-radius divergence, and shared-link quaternion example. A full proof, checker, passing log, SHA256 checksum are stored under /The Singular Boundary/Proof Audits/.