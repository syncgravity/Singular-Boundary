# R3-IR-529 — Direct deleted-face cap via protected non-tree shared link (2026-10-30)

**Finite-model theorem, conditional on R3-IR-528's Hilbert-fiber diamagnetic gap proof.** In the actual extracted 11-face M5 open disk, face 0 is deleted and the retained faces are 1,3,2,4,154,150,11,10,7,8. Using the deterministic root-0 BFS tree from R3-IR-527, link **13 is non-tree**. It is contained in face 0 and exactly one retained plaquette, **face 10**. It does not occur in any rooted transport coefficient. Turning off only b_10 makes the magnetic potential independent of U_13, so P_13 reduces H0 and its unique positive ground state is Haar-constant along U_13, even for arbitrarily large couplings on the OTHER nine retained plaquettes. Since face 0 holonomy contains U_13 once, its conditional law at b_10=0 is EXACT SU2 Haar.

The protected local gap theorem R3-IR-528, if accepted with its specified scalar positive divergence-form root-tree operator, supplies R_13(H0-E0)R_13 >= gamma_13 R_13 with gamma_13=3 g2_squared/(8 M_13,13), R_13=I-P_13. For H_b=H0-b_10 p_10, b_10<gamma_13, P_13 p_10 P_13=0; min-max E_b<=E0 and projecting the ground eigen-equation gives ||R_13 Omega_b||<=b_10/(gamma_13-b_10). The normalized P_13 component has exactly Haar-distributed deleted face-0 holonomy. Pure-state measurement contraction yields

**Prob_Omega_b(C_{face0,delta}) >= max(0,c_delta-b_10/(gamma_13-b_10))**,

c_delta=(2/pi)[acos(1-delta)-(1-delta)sqrt(2delta-delta²)].

The bound is **independent of all other nine magnetic couplings**, but applies only for sufficiently weak SELECTED b_10. It is ADDITIVE; at fixed b_10>0 it does not yield a positive relative c_delta bound as delta->0. It also does not persist automatically under physical h-refinement b_10/gamma_13 increasing. The root-tree transport prescription is a model choice, not independently derived as uniquely physical.

Archived M5 numerical geometry: M_13,13=0.7778590280946629, gamma_13=0.4820924954982508 when g2_squared=1. b_10=3/32000 gives eps=0.00019450258092080497. For delta=.1,.2,.3, the Haar masses c_delta are .037386073468498655, .10408803866182784, .1881204043741874; corresponding lower bounds .03719157088757785,.10389353608090703,.1879259017932666. These values are double precision, not interval certified. Actual geometry/incidence, path independence and Schur arithmetic were checked by executing /mnt/data/validate_m5_deleted_face_protected_link.py; repository script reproduces checks with the archived mounted modules.

**Substantial caveat**: The gap step depends on the Hilbert-valued diamagnetic comparison, currently given as an analytic argument in R3-IR-528 but not independently formalized for arbitrary noncommuting SU2 root-transport generators. A gap-proof audit and actual gauge-covariant operator-domain treatment remain necessary before upgrading this conditional result to an unconditional published theorem. No continuum Yang-Mills mass gap or refinement-uniform shrinking cap is established.
