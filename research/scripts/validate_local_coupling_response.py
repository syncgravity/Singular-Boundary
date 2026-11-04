import math
for a in (0.01,1.0,100.0):
 b,s=1.0,0.2
 E=lambda t:a+t-math.hypot(a,t)
 response=1-b/math.hypot(a,b)
 secant=(E(b)-E(b-s))/s
 assert 0<=response<=secant<=2
 print('background',a,'local response',response,'backward secant',secant)
print('PASS concave local energy response comparison')
