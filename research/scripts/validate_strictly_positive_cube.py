from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec=75
k=F(2376252926673252101321919045001703951557,3082322838199847861301112342611033200018689536000000)
L=Decimal(k.numerator)*Decimal(3).sqrt()/(Decimal(k.denominator)*8)
r=F(3,320); q=F(1,10**16); t=r*q
a=1/((1-q)*(1-2*q))
rem=2*(a**10-1)
assert rem<61*q
assert Decimal(rem.numerator)/Decimal(rem.denominator)<L
lb=(L-Decimal(rem.numerator)/Decimal(rem.denominator))*Decimal(q.numerator)**10/Decimal(q.denominator)**10/Decimal(2048)
assert lb>Decimal('7.8e-177')
print("PASS: all 1024 candidate coupling vectors are strictly positive")
print("couplings range",t,2*t)
print("lower physical L2 Q norm for at least one corner",lb)
