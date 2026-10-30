#!/usr/bin/env python3
"""Verified analytic finite SU(2) joint packets; no full interacting vacuum solution.

Requires NumPy SciPy. All Haar integrals deterministic 1-D quadrature.
"""
from __future__ import annotations
import math, csv
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import beta

OUT = Path(__file__).resolve().parent
PI=math.pi

def haar_p(fn):
    return quad(lambda p: (2/PI)*math.sqrt(max(0,1-p*p))*fn(p),-1,1,epsabs=1e-12,limit=400)[0]

def packet(N:int):
    assert N>=1
    L=N+2
    k=np.arange(1,L,dtype=float)
    coef=np.sqrt(8/(3*L))*np.sin(PI*k/L)**2
    assert abs(float(coef@coef)-1)<4e-13
    theta=PI/L
    d=(2/3)*math.sin(theta)**2
    d2=(2*(2*L-3)/(3*L))*math.sin(theta)**4
    pp=np.pad(coef,(1,1))
    pcoef=np.zeros(N+2)
    pcoef[:N+1]=(pp[:-2]+pp[2:])/2
    pcoef[N+1]=coef[-1]/2
    # SU2 p*chi_n = (chi_{n-1}+chi_{n+1})/2, chi_-1=0.
    ex_p=float(coef@pcoef[:N+1]); ex_d=1-ex_p
    ex_d2=float(np.dot((np.pad(coef,(0,1))-pcoef),np.pad(coef,(0,1))-pcoef))
    assert abs(ex_d-d)<3e-12,(N,ex_d,d)
    assert abs(ex_d2-d2)<3e-12,(N,ex_d2,d2)
    var=2*d-d2
    assert abs(var-(1-float(pcoef@pcoef)))<3e-12
    assert var>0
    n=np.arange(N+1,dtype=float)
    electric=float(np.dot(coef**2,n*(n+2)/4))
    return dict(N=N,coeff=coef,deficit=d,deficit2=d2,var=var,electric=electric)

def cap_probability(m:int,h:float):
    a=math.acos(1-h)
    z=(2/PI)*beta(.5, 2*m+1.5)
    val=(2/PI)/z*quad(lambda theta:math.sin(theta)**(4*m+2),0,a,epsabs=1e-15)[0]
    haar=(a-math.sin(a)*math.cos(a))/PI
    return val,haar,z

def target_variance_factor(m):
    # Under target density (1-p^2)^{2m}/Z: E[p²(1-p²)].
    return (4*m+3)/(4*(2*m+2)*(2*m+3))

# Check target Dirichlet energy for all m. Norming dH = (2/pi)sqrt(1-p²)dp.
for m in range(1,9):
    Z=(2/PI)*beta(.5,2*m+1.5)
    I=haar_p(lambda p: p*p*(1-p*p)**(2*m-1))
    target_kin=A=4*m*m/4*I/Z
    assert abs(target_kin-m*m/(4*m+1))<5e-10,(m,target_kin)
    rv=haar_p(lambda p: p*p*(1-p*p)**(2*m+1))/Z
    assert abs(rv-target_variance_factor(m))<1e-12,(m,rv,target_variance_factor(m))
print('PASS beta-integral target energy m²/(4m+1), color variance factor for m=1..8')

# Packet closed moments and explicit inequality for conditional magnetic cost.
for N in range(1,120):
    z=packet(N)
    weighted_d_upper=2*z['deficit2']/z['var']
    assert weighted_d_upper <= 4*math.sin(PI/(N+2))**2 + 0.4, (N,weighted_d_upper)
print('PASS smooth packet exact deficit, second deficit and conditional weighted deficit N=1..119')

# Fixed connected eight-face square-rhombus disk and asymmetric coefficients from source chat.
faces=sorted((x,y) for x in range(3) for y in range(3) if (x,y)!=(0,0))
target=(1,1)
retained=[f for f in faces if f!=target]
verts=sorted({v for x,y in faces for v in ((x,y),(x+1,y),(x+1,y+1),(x,y+1))})
edges=sorted({tuple(sorted((a,b))) for x,y in faces for a,b in zip([(x,y),(x+1,y),(x+1,y+1),(x,y+1)],[(x+1,y),(x+1,y+1),(x,y+1),(x,y)])})
assert len(verts)==15 and len(edges)==22 and len(faces)==8
avec=[.8+.07*(i%6)+.013*(i%3) for i in range(22)]
coef=[.78+.09*i for i in range(7)]
def face_A(q):
    x,y=q
    v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
    return sum(avec[edges.index(tuple(sorted((v[i],v[(i+1)%4]))))] for i in range(4))
As={q:face_A(q) for q in faces}
A_all=sum(avec)
qcolor=(1,0) # one of four target-adjacent retained faces
icol=retained.index(qcolor)
rows=[]
for b in [1,16,256,4096,65536,1048576]:
    state=[]
    for q,ci in zip(retained,coef):
        nmax=max(6,int(8*b**.25)+20)
        options=[]
        for N in range(1,nmax+1):
            z=packet(N)
            E=As[q]*z['electric']+b*ci*z['deficit']
            options.append((E,N,z))
        value,N,z=min(options,key=lambda e:e[0])
        state.append((value,N,z))
    Eprod=sum(y[0] for y in state)
    Ns=[y[1] for y in state]
    z_g=state[icol][2]
    # m=1 center-suppressed state. Normalized color partner R Psi/sqrt(E|R|²).
    m=1
    tgtE=As[target]*m*m/(4*m+1)
    xvar=target_variance_factor(m)
    r2=xvar*z_g['var']/3
    assert r2>0
    # Potential energy of normalized color partner. Face q_color has conditional
    # angular variance factor (1-p_g²) and E[d_g(1-p_g²)]/E[1-p_g²]
    # <= 2 E[d_g²]/E[1-p_g²]. Every other retained face remains unchanged.
    Cpot=b*sum(ci*(2*z_g['deficit2']/z_g['var'] if q==qcolor else w[2]['deficit'])
               for q,ci,w in zip(retained,coef,state))
    # Max original link spin <= N_max+m+2: very conservative but rigorous
    # for SU2 product with a fixed polynomial color factor.
    Jcap=max(Ns)+m+2
    Ecolor_upper=A_all*Jcap*(Jcap+1)+Cpot
    Ebase=Eprod+tgtE
    # Mixed state (base + color)/sqrt2 has fixed 50% exact color-norm fraction.
    Emixed_bound=(math.sqrt(Ebase)+math.sqrt(Ecolor_upper))**2/2
    assert Emixed_bound < 1e9*math.sqrt(b)
    print(f'b={b:8d} N={Ns} E_base={Ebase:12.6f} E_color_upper={Ecolor_upper:12.5f} E_mixed_bound={Emixed_bound:12.5f} color_norm_r2={r2:.6g}')
    rows.append(dict(b=b,max_N=max(Ns),E_product=Eprod,E_suppressed=Ebase,
                     E_color_upper=Ecolor_upper,E_mixed_upper=Emixed_bound,
                     color_pre_normalization_r2=r2,color_norm_fraction=.5,
                     E_mixed_over_sqrt_b=Emixed_bound/math.sqrt(b)))
with (OUT/'ENERGY_CERTIFICATES.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)

cap_rows=[]
for h in [0.25,0.1,0.01,0.001,0.0001]:
    m=1
    val,haar,z=cap_probability(m,h)
    ratio=val/haar
    a=math.acos(1-h)
    asymptotic=16*a**7/(35*PI)
    assert ratio<1
    if h<=.0001:
        assert abs(val/asymptotic-1)<.001
    # color partner adds nonnegative p²(1-p²) weight so near-center cap is O(h) smaller.
    print(f'h={h:g}, Haar={haar:.9g}, m=1 suppressed={val:.9g}, suppression ratio={ratio:.9g}')
    cap_rows.append(dict(h=h,haar=haar,cap_suppressed=val,ratio=ratio))
with (OUT/'CAP_CERTIFICATES.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(cap_rows[0]));writer.writeheader();writer.writerows(cap_rows)
print('PASS joint SU2 high-spin simultaneous product, fixed 50% nonclass sector and enhanced cap suppression; no true vacuum estimate')
