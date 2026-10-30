# Physical Gauss-projected Feynman–Kac seam and center-flux cosh identity

2026-10-30. Exact finite-volume operator/kernel audit. Does not prove full-coupling cap survival.

Take a finite collection of original SU(2) edge variables on a planar disk, full link configuration space Q=SU(2)^E with normalized product Haar measure, vertex gauge group G=SU(2)^V with normalized Haar, and physical projector P_G=int_G T_g dg. Let H0=sum_e a_e(-Delta_e)+V0 be a smooth bounded real Wilson potential and O>=0 a bounded gauge-invariant multiplication operator. Let p be the real bounded fundamental Wilson plaquette multiplier, and H(t)=H0+t b(1-p). Assume a unitary link-center involution S commutes with all vertex gauge transformations, preserves H0 and O, and takes p to -p. Such an S was explicitly constructed for ordinary disk boundary conditions in R3-IR-402.

The unrestricted heat operator e^(-beta H0) has a strictly positive continuous integral kernel K0_beta(q,q') by elliptic Feynman–Kac on compact Q. The physical trace is

Z_phys,0=Tr(P_G e^(-beta H0))=int_G dg int_Q dq K0_beta(q,g q).

Likewise the cap-inserted trace is

N_phys,0=Tr(P_G O e^(-beta H0))=int_G dg int_Q dq O(q) K0_beta(q,g q).

The integrands are nonnegative. To interpret the perturbation, use the Brownian-bridge Feynman–Kac kernel with endpoints q and gq, retaining the V0 weight. Define the positive finite-beta physical reference measure by normalizing the joint (g,q,path) weight whose endpoint is gq. Write X=b int_0^beta p(q_s) ds. Then, exactly,

F_beta(t)/F_beta(0)
=E_phys,0^O[exp(tX)]/E_phys,0[exp(tX)]
=E_phys,0^O[cosh(tX)]/E_phys,0[cosh(tX)].

The scalar factor exp(-beta tb) cancels. The center sign map S commutes with the gauge action, hence sends bridge endpoints (q,gq) to (Sq,g Sq), leaves all kernel and insertion weights invariant, and reverses X. Thus the sinh contributions vanish in both physical ensembles. This proves physical positivity and the cosh formula while retaining the **nontrivial gauge seam**; it does not assert a Haar-distributed private link at finite beta.

Importantly, the link-center symmetry S is not in general a vertex gauge transformation: it is an independent unitary on link configurations. The argument needs commutation with vertex gauge actions and preservation of the potential, not identification of S with a physical gauge transformation.

The physical finite-beta baseline F_beta(0)=N_phys,0/Z_phys,0 need not equal its positive-vacuum Haar limit, as demonstrated in R3-IR-400. At each fixed lattice the ratio of cap expectations has a vacuum limit, but the numerator and denominator cosh moments need not separately converge, and no uniform limit in the refinement parameter is established.

The remaining inequality is a nonperturbative lower bound on the physical cap-biased/reference cosh-moment ratio at the final-neighbor coupling; kernel positivity and center parity alone do not order these moments. No uniform cap survival, signed transport estimate or continuum mass gap is inferred.

Proof notes: the gauge group may have a redundant global factor, harmless under normalized Haar averaging. Kernel expressions are up to consistent endpoint conventions for T_g; because g runs over Haar, either q to gq or inverse conventions agree. The trace-class property follows from compact Q and strictly positive elliptic link kinetics; bounded Wilson potentials preserve it.
