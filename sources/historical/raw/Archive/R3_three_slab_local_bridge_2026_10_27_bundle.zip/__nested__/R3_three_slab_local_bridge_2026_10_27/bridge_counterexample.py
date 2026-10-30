"""Exact rational 2-state positive-kernel counterexample to three-factor Loewner monotonicity.
Not a SU(2) Wilson counterexample. Shows positive kernels plus positive-definite
convolution difference do not suffice for a 3-slab replacement argument.
"""
import sympy as s
from pathlib import Path
import json
C=s.Matrix([[1,s.Rational(7,10)],[s.Rational(7,10),1]])
V0=s.diag(1,2); V2=s.diag(2,1)
A0=V0*C*V0; A2=V2*C*V2
P=s.ones(2,2)/2; z=s.Rational(17,10)
D=C-z*P
B1=P
A1=C
v=s.Matrix([1,-1]);
assert D==s.Rational(3,20)*v*v.T
assert A0.det()>0 and A2.det()>0 and A0[0,1]>0 and A2[0,1]>0
assert (A0*D*A2).trace()<0
Z_A=(A0*A1*A2).trace(); Z_B=(A0*B1*A2).trace();gap=s.simplify(Z_A-z*Z_B)
print('Z_A',Z_A,'Z_B',Z_B,'z',z,'Z_A-z Z_B',gap)
assert gap<0
out={'group':'Z2 toy, NOT SU2','positive_convolution_kernel':[[str(y) for y in row] for row in C.tolist()], 'positive_outer_A0':[[str(y) for y in row] for row in A0.tolist()], 'positive_outer_A2':[[str(y) for y in row] for row in A2.tolist()], 'Loewner_positive_convolution_difference':[[str(y) for y in row] for row in D.tolist()], 'z':str(z),'completed_trace':str(Z_A),'cavity_trace':str(Z_B),'monotonicity_defect':str(gap),'meaning':'Strictly positive integral kernels and positive convolution spectrum do not alone guarantee a 3-factor trace monotonicity. This does not rule out extra SU2 gauge structure.'}
Path(__file__).with_name('counterexample_certificate.json').write_text(json.dumps(out,indent=2))
