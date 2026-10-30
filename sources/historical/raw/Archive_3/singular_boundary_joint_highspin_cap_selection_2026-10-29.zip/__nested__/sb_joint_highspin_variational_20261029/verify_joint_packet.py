#!/usr/bin/env python3
"""Independent deterministic checks of exact joint SU(2) finite character packets."""
from pathlib import Path
from scipy.integrate import quad
from scipy.special import beta
import numpy as np

ROOT=Path(__file__).resolve().parent
faces=sorted((x,y) for x in range(3) for y in range(3) if (x,y)!=(0,0))
target=(1,1);retained=[f for f in faces if f!=target]
vertices=sorted({v for x,y in faces for v in [(x,y),(x+1,y),(x+1,y+1),(x,y+1)]})
edges=sorted({tuple(sorted((a,b))) for x,y in faces for a,b in zip([(x,y),(x+1,y),(x+1,y+1),(x,y+1)],[(x+1,y),(x+1,y+1),(x,y+1),(x,y)])})
avec=np.array([.8+.07*(i%6)+.013*(i%3) for i in range(len(edges))]);c=np.array([.78+.09*i for i in range(len(retained))])
def fe(q):
 x,y=q;v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)];return {edges.index(tuple(sorted((v[i],v[(i+1)%4])))) for i in range(4)}
A={q:float(avec[list(fe(q))].sum()) for q in faces}
assert len(edges)==22 and len(vertices)==15 and len(faces)==8

def sine_packet(N):
 n=np.arange(N+1);coeff=np.sqrt(2/(N+2))*np.sin((n+1)*np.pi/(N+2))
 assert abs(coeff@coeff-1)<1e-13
 p=np.zeros((N+2,N+2));
 for i in range(N+1):p[i,i+1]=p[i+1,i]=.5
 nn=np.arange(N+1)
 elec=float(np.sum(coeff**2*nn*(nn+2)/4))
 pexp=float(coeff@(p[:N+1,:N+1]@coeff))
 var=float(1-np.linalg.norm(p[:,:N+1]@coeff)**2)
 assert abs(pexp-np.cos(np.pi/(N+2)))<1e-13
 assert 0<var<1.00001
 return elec,pexp,var

def cap_m(m,delta):
 a=np.arccos(1-delta)
 z=(2/np.pi)*beta(.5,2*m+1.5)
 v=(2/np.pi)/z*quad(lambda theta:np.sin(theta)**(4*m+2),0,a,epsabs=1e-15)[0]
 haar=(a-np.sin(a)*np.cos(a))/np.pi
 return v,haar

def cap_enh(delta):
 a=np.arccos(1-delta)
 # normalized (1+chi1)/sqrt2 = (4p^2)/sqrt2; density 8cos^4 theta
 return 16/np.pi*quad(lambda theta:np.cos(theta)**4*np.sin(theta)**2,0,a,epsabs=1e-15)[0]

# Analytic Beta check for target electric form: m^2/(4m+1)
for m in range(1,9):
 z=(2/np.pi)*beta(.5,2*m+1.5)
 numerator=4*m*m*(2/np.pi)/4 * quad(lambda p:p*p*(1-p*p)**(2*m-.5),-1,1,epsabs=1e-12)[0]
 assert abs(numerator/z-m*m/(4*m+1))<1e-10,(m,numerator/z)
print('PASS exact normalized target SU2 electric Dirichlet identity m=1..8')

lines=['b,spin_n_max,product_energy,target_suppressed_energy,target_enhanced_energy,spin1_neighbour_variance,nonclass_norm2_epsilon_half,semiclassical_ratio']
for b in [1,4,16,64,256,1024,4096,65536]:
 # choose exact optimal finite packet size by evaluating the complete 1-face Rayleigh quotient
 Ns=[];terms=[];gvars=[]
 for q,ci in zip(retained,c):
  choices=[]
  for N in range(1,101):
   ee,pp,v=sine_packet(N)
   choices.append((A[q]*ee+b*ci*(1-pp),N,v))
  value,N,v=min(choices)
  Ns.append(N);terms.append(value);gvars.append(v)
 energy=sum(terms)
 # m=1 target: exact electric shift A_f/5; enhanced: shift A_f
 # R=p_f D_fg, source g=first cardinal retained (1,0)
 gi=retained.index((1,0))
 target_var=(4*1+3)/(4*(2*1+2)*(2*1+3)) # E_target[p^2(1-p^2)] = 7/80
 norm2=1+0.25/3*target_var*gvars[gi]
 lines.append(f'{b},{max(Ns)},{energy:.12f},{energy+A[target]/5:.12f},{energy+A[target]:.12f},{gvars[gi]:.12g},{norm2:.12f},{energy/np.sqrt(b):.12f}')
 print('b',b,'N',Ns,'Eprod',round(energy,6),'E_plus_m1',round(energy+A[target]/5,6),'E_plus_enh',round(energy+A[target],6),'nonclass norm2',round(norm2,10))
(ROOT/'JOINT_VARIATIONAL_DATA.csv').write_text('\n'.join(lines)+'\n')

print('h,haar_cap,suppressed_m1,ratio_m1_over_haar,enhanced_cap,ratio_enh_over_haar')
caplines=['h,haar_cap,suppressed_m1,ratio_m1_over_haar,enhanced_cap,ratio_enh_over_haar']
for h in [0.25,0.1,0.05,0.01,0.001]:
 v,haar=cap_m(1,h);enh=cap_enh(h)
 print(h,'%.9g'%haar,'%.9g'%v,'%.9g'%(v/haar),'%.9g'%enh,'%.9g'%(enh/haar))
 caplines.append(f'{h},{haar:.15g},{v:.15g},{v/haar:.15g},{enh:.15g},{enh/haar:.15g}')
(ROOT/'CAP_DATA.csv').write_text('\n'.join(caplines)+'\n')
# closed m=1 near-cap small-angle coefficient, as checked by ratio
for a in [1e-2,5e-3]:
 h=1-np.cos(a);v,haar=cap_m(1,h)
 assert abs(v/((16/(35*np.pi))*a**7)-1)<5e-4
 assert abs((v/haar)/((24/35)*a**4)-1)<5e-4
print('PASS m=1 cap asymptotics 16a^7/(35pi), ratio (24/35)a^4')
# Color norm: conditional SU2 Haar quaternion directions give 1/3 variance
for m in [0,1,2,4]:
 e_p=(4*m+3)/(4*(2*m+2)*(2*m+3))
 z=(2/np.pi)*beta(.5,2*m+1.5)
 x=(2/np.pi)/z*quad(lambda p:p*p*(1-p*p)**(2*m+1.5),-1,1)[0]
 assert abs(e_p-x)<1e-10
print('PASS conditional nonabelian color R^2 factor for m=0,1,2,4')
# Independent exact SU2 relative-angle integration: D=-sin(theta_f)sin(theta_g)t,
# with t uniformly distributed on [-1,1] for two independently Haar axes.
from numpy.polynomial.legendre import leggauss
nodes,weights=leggauss(8)
for pf,pg in [(0.12,-0.55),(0.8,0.25),(-0.4,-0.9)]:
 D=-np.sqrt(1-pf*pf)*np.sqrt(1-pg*pg)*nodes
 assert abs((weights@D)/2)<1e-15
 exact=(1-pf*pf)*(1-pg*pg)/3
 assert abs(weights@(D*D)/2-exact)<1e-14
print('PASS independent 8-node SU2 relative-color angular contraction')
# Independent verification of the closed sine packet angular variance, including
# the omitted last-Jacobi-channel contribution.
for N in [1,2,3,4,8,16,32,64]:
 _,_,V=sine_packet(N)
 th=np.pi/(N+2)
 assert abs(V-np.sin(th)**2*(1-1/(2*(N+2))))<2e-13
print('PASS exact off-class source norm via sine-packet omitted-character identity')
print('ALL PASSED')
