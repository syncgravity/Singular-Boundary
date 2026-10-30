# R3-IR-424 — Higher-spin four-neighbor insertion threshold and exact mixed reconstruction

2026-10-30. Finite original-link SU(2) Wilson disk with free boundary. Exact representation selection, not a uniform cap bound.

Let f be a deleted magnetic target rhombus, with four distinct neighboring faces g_i sharing separate links x_i (each shared link appears in no other face magnetic term). The four-neighbor family is H(t)=H_e + V_rest + sum_i b_i(1-t_i p_{g_i}) on the Gauss-invariant Hilbert space, with each t_i real. Let C_j(t)=<Omega_t,chi_j(W_f)Omega_t>, j a positive INTEGER spin. The finite-volume positive ground state is unique, gauge invariant, and real analytic in the coupling parameters locally.

THEOREM (HS-1). For any i, and every fixed choice of other t_k, all derivatives in t_i of C_j at t_i=0 of orders n<2j vanish:
partial_i^n C_j(t_1,...,t_i=0,...,t_4)=0, n=0,...,2j-1.

Proof. At t_i=0 the shared x_i is magnetically private; H(0)=a_i(-Delta_{x_i})+H_{rest,i}, with the exact positive vacuum independent of x_i. Each perturbative insertion of p_{g_i} is a fundamental (spin 1/2) matrix coefficient in x_i. The electric generator and the rest of H preserve x_i Peter-Weyl spin. In an nth derivative of the normalized vacuum density Omega_t^2, every summand has a total of at most n fundamental insertions across its bra and ket expansions. Tensor-product spin addition implies no coefficient of x_i spin greater than n/2. Meanwhile chi_j(W_f) as a function of x_i, with all remaining links fixed, is pure x_i spin j. Orthogonality gives zero for n<2j. Normalization derivatives do not increase the spin-insertion count; the constant scalar potential b_i similarly cannot. This statement holds while all other neighboring couplings are arbitrary, since none activates x_i when t_i=0.

COROLLARY (HS-2). Iterated Taylor-with-integral-remainder in each t_i gives, for nonnegative t_i,

C_j(t)=int_0^{t1}...int_0^{t4}
 [prod_i (t_i-u_i)^(2j-1)/(2j-1)!]
 (partial_1^(2j) partial_2^(2j) partial_3^(2j) partial_4^(2j) C_j)(u)
 du_1...du_4.

At physical full neighbor coupling t_i=1,

C_j(1,1,1,1)=int_[0,1]^4
 [prod_i (1-u_i)^(2j-1)/(2j-1)!]
 D_(8j) C_j(u) d^4u. (HS-2)

The weight is nonnegative, and its total integral is [1/(2j)!]^4. For j=1 this recovers the 8-fold two-derivative-in-each-variable reconstruction from R3-IR-418. For j=2 the leading per-neighbor derivative order is four and total mixed order sixteen, etc.

This selection rule is a genuine original-link Wilson constraint absent from arbitrary center-symmetric probability densities such as R3-IR-423. It makes the high-integer-spin content required for an identity cap an increasingly high coupling-response order near the fully decoupled boundary.

LIMITATIONS. This does NOT bound the high derivatives themselves, their signs, or their variation under physical strong magnetic coupling. The positive integral weight can be defeated by large mixed derivatives and is not a regulator-uniform suppression estimate. No lower bound for the complete cap, Wilson spectral gap, or continuum Yang-Mills mass gap is proved.
