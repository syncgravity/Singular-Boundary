# The Singular Boundary — Rare-event sparse-defect source theorem and soft-mode alternative

**Research date:** 2026-10-28. **Classification:** exact finite interacting SU(2) Wilson vacuum theorem conditional on the *previously proved* uniform regional exponential moment, with an explicitly conditional continuum soft-mode alternative. **Not proved:** that a single defect somewhere becomes rare, that the source has nonvanishing limiting variance, the regulator-uniform physical gap, full continuum reconstruction or Stage7/26 source identity. No Monte Carlo.

## 1. Geometry and actual physical vacuum

Let \(H_h=\sum_e a_e(-\Delta_e)+\sum_f b_fd_f\) on a finite simply connected face-complete SU(2) rhombus disk, with Gauss invariance at every vertex, \(d_f=1-p_f\in[0,2]\), \(p_f=\tfrac12\operatorname{ReTr}W_f\), \(0<a_e\le a_*\), four links per face, at most two incident faces per link. On a fixed physical-area interior face set \(D\) with complete collar and \(b_f\ge\beta h^{-2}\), the earlier regional ground-state comparison and nonlinear exponential-tilt theorem yield **an actual interacting vacuum exponential moment**:

\[
Z_h=h\sum_{f\in D}d_f,\quad \nu_h=\Omega_h^2dU,\quad \exists\ t_0>0,M<\infty:\ \sup_{h\le h_0}\mathbb E_{\nu_h}e^{t_0 Z_h}\le M.\tag{RE-1}
\]

Indeed use the exact regional Laplace bound on \(X=Z_h/h\) with parameter \(s=t_0 h\); with \(b_*\ge\beta h^{-2}\) and \(\Delta_D\le C_Eh^{-3}\), the log Laplace bound is \(O(t_0)\) uniformly for sufficiently small \(h\). The unique positive full-space ground state is gauge-invariant, so all following energies and projections act inside the physical Gauss sector.

Define \(Q_f=\tfrac12(\arccos p_f)^2\), \(r_f=Q_f-d_f\ge0\). Let \(\chi\in C^1\) be one on \([0,1]\), zero on \([2,\infty)\), with \(\|\chi'\|_\infty\le C_\chi\), and \(\delta_h=h^{3/4}\). For signed \(|q_f|\le q_*\), put

\[
S_h=\sqrt h\sum_{f\in D}q_f r_f[1-\chi(d_f/\delta_h)],\quad
G_h=\sqrt h\sum_{f\in D}q_fr_f\chi(d_f/\delta_h),\quad R_h=S_h+G_h.
\tag{RE-2}
\]

The earlier fixed-support theorem gives \(\|(G_h-\nu_hG_h)\Omega_h\|\le\epsilon_h\le C_Gh^{1/4}\). Let \(\mathcal E_h=\{\max_{f\in D}d_f>\delta_h\}\), \(P_h=\nu_h(\mathcal E_h)\in[0,1]\). *This means at least one bad face,* not a positive bad-area fraction. Existing bad-area results do not prove \(P_h\to0\).

The prior exact SU(2) derivative estimate gives

\[
\Gamma(S_h)\le C_\Gamma Z_h,\quad C_\Gamma=32a_*q_*^2(\sqrt{\pi^6/1152}+\sqrt2 C_\chi\pi^4/96)^2.\tag{RE-3}
\]

Because each cutoff factor and its derivative vanish when \(d_f\le\delta_h\), all source gradients vanish on \(\mathcal E_h^c\). Thus the **strictly stronger support-localized estimate** is

\[
\boxed{\Gamma(S_h)\le C_\Gamma Z_h\mathbf1_{\mathcal E_h}.}\tag{RE-4}
\]

Also \(0\le r_f\le c_0d_f\), \(c_0=\pi^2/4-1\), so for *signed* q

\[
\boxed{|S_h|\le c_0q_*h^{-1/2}Z_h\mathbf1_{\mathcal E_h}.}\tag{RE-5}
\]

Both are pointwise configuration-space inequalities, independent of a vacuum approximation.

## 2. Exponential integrability and rare-event moment lemma

For any nonnegative random variable \(Z\) with \(\mathbb E e^{tZ}\le M\), any measurable event \(\mathcal E\) of probability \(P>0\), and \(L=\log(M/P)\ge0\), conditional Jensen gives

\[
\boxed{\mathbb E[Z\mathbf1_{\mathcal E}]\le (P/t)L.}\tag{RE-6}
\]

For a second moment choose \(r=(L+2)/t\), which is \(\ge2/t\). Split \(\mathbb E[Z^2\mathbf1_{\mathcal E}]\) at \(Z=r\). For \(Z\le r\) the expectation is at most \(Pr^2\). For \(Z>r\), the function \(z^2e^{-tz}\) is decreasing, so

\[
\mathbb E[Z^2\mathbf1_{Z>r}]\le r^2e^{-tr}\mathbb E e^{tZ}\le e^{-2}Pr^2.
\]

Consequently

\[
\boxed{\mathbb E[Z^2\mathbf1_{\mathcal E}]\le(1+e^{-2})\frac P{t^2}(L+2)^2.}\tag{RE-7}
\]

The formulas hold uniformly for \(P=1\) as well; if \(P=0\) all event-supported quantities vanish. Unlike ordinary Hölder estimates, the logarithmic bounds retain the useful near-linear dependence on rare-event probability.

## 3. True-vacuum rare-event Dirichlet and variance theorem

The exact interacting ground-state transform in the physical sector yields

\[
J_h:=\langle S_h\Omega_h,K_hS_h\Omega_h\rangle=\mathbb E_{\nu_h}\Gamma(S_h)
\le\frac{C_\Gamma}{t_0}P_h\log\frac M{P_h}.\tag{RE-8}
\]

The uncentered L² bound implies the **unconditional at each regulator** estimate

\[
\boxed{\operatorname{Var}_{\nu_h}(S_h)\le\frac{c_0^2q_*^2(1+e^{-2})}{t_0^2h}
P_h\left(2+\log\frac M{P_h}\right)^2.}\tag{RE-9}
\]

No gap, Gaussian comparison or independent-face assumption enters. Combining with \(\epsilon_h\) gives the full remainder bound

\[
\boxed{\sqrt{\operatorname{Var}_{\nu_h}(R_h)}\le\epsilon_h+
\frac{c_0q_*\sqrt{1+e^{-2}}}{t_0\sqrt h}\sqrt{P_h}\left(2+\log\frac M{P_h}\right).}\tag{RE-10}
\]

In particular, if \(P_h\log^2(M/P_h)=o(h)\), then the *entire fixed-support nonlinear Wilson–angle centered remainder* converges to zero in vacuum norm. A simple sufficient rate is \(P_h=o(h/\log^2(1/h))\), provided this is checked with the corresponding logarithmic factor. The existing regional bad-area theorem does **not** supply such a bound on \(P_h\).

Conversely, if \(\liminf_h\operatorname{Var}_{\nu_h}(R_h)\ge v_0>0\), then for all sufficiently small \(h\)

\[
P_h\left(2+\log\frac M{P_h}\right)^2\ge c(v_0,t_0,q_*,C_\chi)\,h.\tag{RE-11}
\]

In particular \(P_h\) cannot decay superpolynomially; it must satisfy a lower envelope of order \(h/\log^2(1/h)\) up to constants. This is a quantitative **necessary frequency of at least one high-defect face**, not a claim that it occurs in the true vacuum.

## 4. No thin-neck assumption: a rare-event/soft-physical-mode alternative

Assume \(P_h\to0\) and \(\liminf_h\operatorname{Var}_{\nu_h}(R_h)\ge v_0>0\). Then RE-8 gives \(J_h\to0\) without needing two bands or any bottleneck in the distribution of \(S_h\). Centered source vectors \(s_h=(S_h-\nu_hS_h)\Omega_h\) and \(r_h=(R_h-\nu_hR_h)\Omega_h\) obey \(\|r_h-s_h\|\le\epsilon_h\). For all small h take \(\epsilon_h\le\sqrt{v_0}/4\); then \(\|s_h\|^2\ge9v_0/16\). Define

\[
\Lambda_h:=\frac{8J_h}{v_0},\quad \Pi_h=\mathbf1_{(0,\Lambda_h]}(K_h)\ \text{in the physical sector}.\tag{RE-12}
\]

The high-energy spectral tail satisfies \(\|(1-\Pi_h)s_h\|^2\le J_h/\Lambda_h=v_0/8\); hence \(\|\Pi_hs_h\|^2\ge7v_0/16\). Transferring through the good component gives the **source-visible soft-mode theorem**

\[
\boxed{\mu_{R_h}((0,\Lambda_h])\ge \frac{(\sqrt7-1)^2}{16}v_0.}\tag{RE-13}
\]

Since \(J_h=O(P_h\log(M/P_h))\to0\), one has \(\Lambda_h\to0\). The physical Euclidean two-point function therefore obeys, for every \(\tau\ge0\),

\[
\boxed{C_{R_h}(\tau)\ge e^{-\tau\Lambda_h}\frac{(\sqrt7-1)^2}{16}v_0.}\tag{RE-14}
\]

The full physical gap satisfies \(\Delta_h^{\mathrm{phys}}\le\Lambda_h\to0\). This result is stronger than the previous two-band spectral-neck alternative: *mere rarity of any defect*, together with nonvanishing remainder variance, forces source-visible infrared softening. The assumption \(P_h\to0\) has **not** been proved for connected nonlinear Penrose vacua.

## 5. Conditional uniform-gap bound and exact unresolved question

If a positive regulator-uniform physical gap \(\Delta_h^{\mathrm{phys}}\ge\Delta_*>0\) were proved independently, the source-specific Poincaré inequality and RE-8 would imply

\[
\boxed{\sqrt{\operatorname{Var}_{\nu_h}(R_h)}\le\epsilon_h+
\sqrt{\frac{C_\Gamma}{t_0\Delta_*}P_h\log(M/P_h)}.}\tag{RE-15}
\]

Thus **under a proven uniform gap**, \(P_h\to0\) suffices for the centered remainder to vanish, without the stronger \(P_h=o(h/\log^2h)\) requirement. No gap is assumed in the unconditional RE-8–RE-10 theorem, and no gap is established here.

**Remaining noncircular obligation:** Estimate the actual nonlinear Wilson vacuum extreme-event probability \(P_h=\nu_h(\max_{f\in D}d_f>h^{3/4})\), or derive direct source-projected dynamical control. The existing bad-area concentration only bounds \(h^2N_{bad}\), and does not bound the event that *at least one* bad face exists. The original Stage7/26 temporal Q14 and full continuum mass gap remain independently open.

## 6. Verification and provenance

The companion `verify_rare_event_soft_mode.py` checks the global SU(2) class-angle inequalities, support-localized gradient bound, entropy moment lemma, physical spectral cutoff algebra on genuine interacting one-plaquette character-basis vacua at several magnetic strengths, and the logical source-projection constants. The canonical original three-rhombus, ten-edge **spatial** Penrose seed is checked, but the historical temporal action identity is not certified. All checks are deterministic, with no Monte Carlo or modification of the uploaded data archives.
