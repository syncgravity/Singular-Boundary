# Low-energy source spectral distribution criterion and positivity limitation
Date: 2026-10-30
Status: PROVED finite-regulator spectral estimate; the required connected Penrose uniform spectral distribution bound remains OPEN.

Setting. On the physical gauge invariant Hilbert space let K=H_f^--E_f^->=0, P the canonical conditional Haar projector over the deleted based face and Q=I-P. On Ran Q let A=QKQ be the positive Friedrichs compression, with strictly positive lower spectral bound at each finite regulator (not uniformly). For p=P Omega, q=Q Omega, and L2 source s=-QTPp, assume the exact equation Aq=s, so ||q||²=int_(0,infty) lambda^-2 dmu_s(lambda), mu_s(B)=||1_B(A)s||².

THEOREM (spectral-distribution inequality). Let F(lambda)=mu_s((0,lambda]), and choose Lambda>0, alpha>0 and M>=0 with F(lambda)<=M lambda^(2+alpha) for all 0<lambda<=Lambda. Then
||q||² <=(1+2/alpha) M Lambda^alpha + ||s||²/Lambda².
Proof: split the negative-second moment at Lambda. The high part is <=Lambda^-2 ||s||². Stieltjes integration by parts on (0,Lambda] gives integral lambda^-2 dF = Lambda^-2 F(Lambda)+2 int_0^Lambda lambda^-3 F(lambda)d lambda (the lower endpoint vanishes under alpha>0). The hypothesis bounds this by (1+2/alpha) M Lambda^alpha. QED.

If the RHS is o(h^(3/2)) uniformly for bulk faces f and suitable Lambda_h, the existing OT-4 cap inequality yields Haar-order identity cap probability at delta~h, and the independently proved exponential-tilt trial yields logarithmic deletion scaling. The needed Penrose bound on F(lambda) and ||s|| is not established. This is a sufficient criterion rather than a new dynamical estimate.

SEMIGROUP POSITIVITY CAUTION. Although <s,e^-tA s>>=0 for every t>=0 by the spectral theorem, e^-tA on Ran Q is not generally positivity preserving in the pointwise order of functions. Q is conditional mean-zero fiber projection; a nonnegative function in Ran Q must vanish almost everywhere. Nor is e^-t QKQ interchangeable with Qe^-tKQ when [K,Q] !=0. Thus standard positivity-improving heat kernel/Harnack bounds for e^-tK cannot be inserted into the compressed source autocorrelation without additional arguments.

NO-GO FOR UNWEIGHTED SOURCE. In scalar spectral toy A=epsilon and s=epsilon, with epsilon->0, one has ||s||->0 but ||A^-1 s||=1, and integral_0^infty t<s,e^-tA s>dt=1. Therefore source-norm smallness alone cannot control the low energy inverse-square moment. This toy is not the Penrose Hamiltonian.

Outstanding: a model-specific estimate for F_{f,h}(lambda) with sufficient refinement dependence, or a direct relative center-cap comparison that avoids the global Q-norm criterion. No magnetic deletion bulk theorem or continuum mass gap is proved.
