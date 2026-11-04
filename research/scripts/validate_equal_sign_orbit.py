from fractions import Fraction as F
from decimal import Decimal,localcontext
import os,sys
if os.environ.get("PENROSE_STUDY_SRC"):
 sys.path.insert(0,os.environ["PENROSE_STUDY_SRC"])
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
fi,sg,_=penrose_faces(Approximant(M=5))
S=(1,3,2,4,154,150,11,10,7,8)
private={}
for g in S:
 other={int(e) for h in S if h!=g for e in fi[h]}
 target={int(e) for e in fi[0]}
 eligible=sorted(set(map(int,fi[g]))-other-target)
 assert eligible,(g,eligible)
 private[g]=eligible[0]
assert private=={1:86,3:87,2:88,4:372,154:297,150:291,11:16,10:26,7:7,8:9}
K=F(2376252926673252101321919045001703951557,3082322838199847861301112342611033200018689536000000)
q=F(1,10**8);t=q*F(3,320)
rem=2*((1-q*q)**(-10)-1)
with localcontext() as ctx:
 ctx.prec=90
 L=Decimal(K.numerator)/Decimal(K.denominator)*Decimal(3).sqrt()/8
 R=Decimal(rem.numerator)/Decimal(rem.denominator)
 bound=(L-R)/Decimal(2*10**80)
 assert L>R and bound>Decimal("8.24e-94")
print("PASS ten independent outer-edge center flips, exact remainder, positive equal-coupling bound",t,bound)
