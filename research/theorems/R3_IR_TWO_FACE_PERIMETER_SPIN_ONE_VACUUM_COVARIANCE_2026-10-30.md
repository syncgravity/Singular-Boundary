# Two-face perimeter spin-one identity for the actual physical Wilson vacuum

Date: 2026-10-30. R3-IR-407. Exact finite-volume, original-link, Gauss-invariant ground-state identity. No full-coupling comparison is proved.

Let f be a magnetically deleted face and g its adjacent face, whose magnetic coupling is zero. Assume that their shared original link x appears in no other retained magnetic potential. Every other Wilson face interaction may be at physical strength. On a planar disk the positive normalized unrestricted ground state is Omega_0(x,y)=omega(y); it is Gauss invariant and is the physical vacuum. Denote vacuum expectation by <...>_0.

Choose oriented boundary words W_f=x L(y) and W_g=x^{-1} M(y). Their product in the same base point is W_f W_g=x L x^{-1} M, which is not the perimeter concatenation unless based holonomies are aligned correctly. Instead the cancellation occurs with the conjugated word W_g W_f or by starting the two loops at the endpoints of the shared link: the perimeter word is C=M L (up to cyclic conjugation and orientation reversal). It uses all outer links of the union of f and g, not x. Its character chi_1(C) is gauge invariant because C transforms by conjugation at its base vertex.

For p_g=Tr W_g/2 and a nonnegative central cap k_a(W_f), define a0=int_SU2 k_a(W)dW and a1=int_SU2 k_a(W) chi_1(W)dW. The SU(2) fusion rule p_g²=(1+chi_1(W_g))/4 and Schur integration in the private link x yield the following exact physical vacuum identities:

<k_a(W_f)>_0=a0,
<p_g²>_0=1/4,

<k_a(W_f) p_g²>_0
= a0/4 + a1/12 <chi_1(C)>_0.   (TP-1)

Therefore

Cov_0(k_a(W_f),p_g²)
= (a1/12) <chi_1(C)>_0,        (TP-2)

and, for a0>0,

E_0^{k_a}[p_g²]-E_0[p_g²]
= (a1/(12a0)) <chi_1(C)>_0.   (TP-3)

Proof: integrate the x-Haar factor against the x-independent physical vacuum density omega(y)^2. For each fixed y, set W=xL. Schur orthogonality gives int k_a(W) chi_1(W^{-1}ML)dW = (a1/3)chi_1(ML). Integrating y with omega² yields TP-1; subtract the product of means for TP-2 and divide by a0 for TP-3. All insertions are gauge invariant, so using the unrestricted normalized ground state is identical to physical vacuum expectation.

This identification is more specific than an abstract environmental sign: the troublesome object is the *spin-one character of the two-face outer perimeter Wilson loop*. For an identity-centered small cap a1>0, the short-equal-time cap-neighbor squared-moment sign is EXACTLY the sign of the vacuum perimeter spin-one expectation. Because -1<=chi_1(C)<=3, this gives the unconditional numerical interval
-a1/(12a0) <= E_0^{k_a}[p_g²]-E_0[p_g²] <= a1/(4a0).
No lower bound of nonnegative sign is obtained.

Limits: this is an equal-time ground-state formula **only at zero coupling for the selected neighboring plaquette**. It is NOT a formula for the beta-finite physical trace, not an identity for the integrated path source X, and not a statement about full t=1 coupling. The relation does not prove that <chi_1(C)>_0 is nonnegative or bounded away from negative values uniformly under Penrose refinement. Such a perimeter-loop estimate would be a concrete first gate for a favorable second source-moment comparison; higher-time correlations and full-coupling transport would remain even after that gate.

Dependencies: R3-IR-394 exact private-link factorization, R3-IR-406 conditional SU2 spin-one contrast, R3-IR-400 thermal Gauss-projection caution.
