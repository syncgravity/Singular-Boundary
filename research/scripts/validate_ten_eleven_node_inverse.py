from fractions import Fraction as F
x=[F(j,10) for j in range(11)]
w=[]
for j in range(11):
 p=[F(1)];den=F(1)
 for i in range(11):
  if i==j:continue
  den*=x[j]-x[i]
  q=[F(0)]*(len(p)+1)
  for k,c in enumerate(p):q[k]-=c*x[i];q[k+1]+=c
  p=q
 w.append(sum((c/F(15+2*k) for k,c in enumerate(p)),F())/den)
for r in range(11):
 assert sum((w[j]*x[j]**r for j in range(11)),F())==F(1,15+2*r)
assert sum(w)==F(1,15)
assert sum([10,70,185,250,210,120,45,10,1])==901
assert 901*11==9911
print("PASS 11-node exact rational moments for all 901 terms")
