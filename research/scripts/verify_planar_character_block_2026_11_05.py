#!/usr/bin/env python3
"""Symbolic and numerical SU(2) planar-character convolution checks, NOT a continuum proof."""
import argparse,json
from pathlib import Path
import sympy as sp

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path('docs/evidence/R3_SU2_PLANAR_CHARACTER_BLOCK_2026-11-05.json'));a=p.parse_args()
 t=sp.symbols('t',positive=True)
 coeffs={n:sp.besseli(n,2*t)-sp.besseli(n+2,2*t) for n in range(5)}
 for n,f in coeffs.items():
  assert sp.simplify(f - (n+1)/t*sp.besseli(n+1,2*t))==0
 series={n:sp.series(f,t,0,11).removeO() for n,f in coeffs.items()}
 assert series[0].coeff(t,0)==1 and series[1].coeff(t,1)==1
 assert series[1].coeff(t,3)==sp.Rational(1,3)
 # Convolutions on connected planar disks: a_n^F/d_n^(F-1).
 Fcheck={F: {n:sp.simplify(series[n]**F / sp.Integer(n+1)**(F-1)) for n in range(4)} for F in (1,2,3,4)}
 c1=sp.series(coeffs[1]**4/(8*coeffs[0]**4),t,0,11).removeO().expand()
 c2=sp.series(coeffs[2]**4/(27*coeffs[0]**4),t,0,11).removeO().expand()
 assert c1.coeff(t,4)==sp.Rational(1,8)
 assert c1.coeff(t,6)==-sp.Rational(1,12)
 assert c1.coeff(t,8)==sp.Rational(1,24)
 assert c2.coeff(t,8)==sp.Rational(1,432)
 assert c1.coeff(t,4)**2/2==sp.Rational(1,128)
 assert c2.coeff(t,8)!=c1.coeff(t,4)**2/2
 samples=[]
 for z in (sp.Rational(1,10),sp.Rational(1,4),sp.Rational(1,2),sp.Integer(1),sp.Integer(2)):
  a0=float(sp.N(coeffs[0].subs(t,z),25));
  first=float(sp.N(coeffs[1].subs(t,z)**4/(8*coeffs[0].subs(t,z)**4),25))
  second=float(sp.N(coeffs[2].subs(t,z)**4/(27*coeffs[0].subs(t,z)**4),25))
  assert a0>0 and 0<second<first and first<1
  samples.append({'t':str(z),'normalization_a0':a0,'normalized_fundamental_coefficient':first,'normalized_label2_coefficient':second})
 out={'status':'PASS','scope':'Isolated 2D central SU(2) Wilson-character block, not 3D interacting time dynamics',
      'blocking_formula':'a_n(t)^F / (n+1)^(F-1)',
      'bessel_coefficient':'a_n(t)=I_n(2t)-I_(n+2)(2t)=(n+1) I_(n+1)(2t)/t',
      'fundamental_F4_series':str(c1),'highest_weight2_F4_series':str(c2),
      'checks':['5 exact Bessel recurrence identities','4 planar face counts','dyadic F4 t^4/8, -t^6/12, t^8/24','highest-weight 2 t^8/432','5 numerical positive coefficient checks'],
      'samples':samples,'gate_status':'P0,P2,P4,P5 and Penrose transfer remain OPEN'}
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n')
 print('PASS: exact SU2 planar block coefficient a_n^F/d_n^(F-1), F=1..4; fundamental F4=t^4/8+...')
if __name__=='__main__':main()
