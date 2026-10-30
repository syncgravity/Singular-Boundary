# R3-IR-504: Strong-magnetic SU(2) rotor Harnack obstruction

Take p(U)=Tr(U)/2, -Delta p=(3/4)p, and H=a(-Delta)+b(1-p). Haar x=(1+p)/2 has Beta(3/2,3/2) law. The trial psi_n=(1+p)^n has squared-density Beta(2n+3/2,3/2) and exact energy quotient E_trial=3 a n²/[4(4n+1)]+3b/(2n+3). With n nearest sqrt(8b/a), E0/b=O(sqrt(a/b)). The ground-state identity b E_Omega(1-p)<=E0 therefore forces E_Omega(1-p)->0 as b/a grows.

The smooth strictly positive ground-state density rho=Omega² has logarithmic oscillation A=osc(log rho). The pointwise density comparison implies E_rho(1-p)>=e^-A E_Haar(1-p)=e^-A, thus A>=log(b/E0)>=(1/2)log(b/a)-O(1). A uniform SU2-wide log-density oscillation bound cannot follow solely from fixed positive electric ellipticity in the strong-magnetic regime. Exact rational beta integrals validated for b/a=1,10,100,10000,100000000; script research/scripts/validate_su2_rotor_harnack_obstruction.py.

IMPORTANT: the desired Penrose quantity is the UNION of center caps near +I and -I. Localization near +I does NOT invalidate that target, and this rotor test is not a proof about the interacting Penrose model. It specifically invalidates uniform full-group Harnack control as an automatic strategy; a targeted center-cap estimate might still work. No refinement-uniform result or continuum mass gap has been proved.
