#!/usr/bin/env python3
"""Exact rational/Bessel identities and deterministic asymptotic sanity checks.
No Monte Carlo; no historical observations or field configurations generated.
"""
import sympy as s
import mpmath as mp
import json

k=s.symbols('k',positive=True)
Z=s.besseli(1,2*k)/k
r=s.besseli(0,2*k)/s.besseli(1,2*k)-1/k
assert s.simplify(s.diff(Z,k)-2*r*Z)==0
# Haar E[p^2] = (Z'' / 4Z), Var[p]=(log Z)''/4 = r'/2.
var=s.diff(r,k)/2
assert s.simplify(s.diff(Z,k,2)/(4*Z)-r*r-var)==0

h,c1,c2,I,eps=s.symbols('h c1 c2 I eps',positive=True)
# At k_i=c_i/h, r_i=1-3h/(4c_i)+O(h^2).
# A_i=h^1/2 Q r_i with Q~I/h^2, difference order h^-1/2.
diff_mean=(s.Rational(3,4)*I*(1/c2-1/c1))/s.sqrt(h)
rare_var=s.expand(eps*(1-eps)*diff_mean**2)
assert s.simplify((rare_var.subs(eps,h)).subs({c1:1,c2:2,I:1}) - s.Rational(9,64)*(1-h))==0
assert s.simplify((rare_var.subs(eps,s.Rational(1,2))).subs({c1:1,c2:2,I:1}) - s.Rational(9,256)/h)==0
# Overlap per face from Z(k)~e^(2k)/(sqrt(4pi) k^(3/2))
theta=(2*s.sqrt(c1*c2)/(c1+c2))**s.Rational(3,2)
assert s.simplify(theta.subs({c1:1,c2:2})-(2*s.sqrt(2)/3)**s.Rational(3,2))==0
assert float(theta.subs({c1:1,c2:2}))<1
# Agmon: mgf bound via core and tail, theta_h=h times X and L=cL/h.
C,beta,amax,lam,th,L=s.symbols('C beta amax lam th L',positive=True)
weighted=64*amax*h*h/(beta*L)
tail_mgf=s.exp(2*th*h*L)*weighted/(2*L)
assert s.simplify(tail_mgf.subs(L,C/h)-32*amax*s.exp(2*th*C)*h**4/(beta*C**2))==0
# Branch Chernoff relative entropy exponent for macroscopic fraction rho of F:
# t=gamma/h, log mgf per face -> (3/2)log[c/(c-gamma/2)].
co,ga,rho=s.symbols('co ga rho',positive=True)
chernoff=-ga*rho/h+s.Rational(3,2)*s.log(co/(co-ga/2))
assert s.limit(h*chernoff,h,0)==-ga*rho
# Deterministic Bessel evaluation of overlap and sample variance (no sampling).
mp.mp.dps=60
out=[]
for H in ['0.1','0.05','0.025']:
    hh=mp.mpf(H); k1=1/hh;k2=2/hh; mid=(k1+k2)/2
    def logZ(kk):return mp.log(mp.besseli(1,2*kk))-mp.log(kk)
    def rr(kk):return mp.besseli(0,2*kk)/mp.besseli(1,2*kk)-1/kk
    def vv(kk):return mp.mpf('0.25')*(mp.diff(logZ,kk,2))
    F=round(1/float(hh)**2); qtotal=F; w=hh
    r1=rr(k1);r2=rr(k2);rm=rr(mid)
    s0=mp.exp(F*(logZ(mid)-mp.mpf('.5')*(logZ(k1)+logZ(k2))))
    m1=mp.sqrt(hh)*qtotal*r1; m2=mp.sqrt(hh)*qtotal*r2; mm=mp.sqrt(hh)*qtotal*rm
    v1=hh*F*vv(k1);v2=hh*F*vv(k2);vm=hh*F*vv(mid)
    N=1+2*mp.sqrt(w*(1-w))*s0
    mean=((1-w)*m1+w*m2+2*mp.sqrt(w*(1-w))*s0*mm)/N
    second=((1-w)*(m1*m1+v1)+w*(m2*m2+v2)+2*mp.sqrt(w*(1-w))*s0*(mm*mm+vm))/N
    variance=second-mean*mean
    assert variance>0
    out.append({'h':H,'faces':F,'overlap_log':str(mp.log(s0))[:20], 'variance_eps_h':str(variance)[:24]})
print(json.dumps({'exact_checks':True,'asymptotic_rare_variance_limit':'9/64 for c1=1,c2=2,I=1','half_mixture_divergence':'9/(256*h)','agmon_true_vacuum_tail_mgf':'O(h^4) for fixed theta','deterministic_bessel_evaluations':out,'nonlinear_ground_state_variance_proved':False,'monte_carlo':False},indent=2))
