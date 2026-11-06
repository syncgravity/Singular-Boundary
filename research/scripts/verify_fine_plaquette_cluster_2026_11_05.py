#!/usr/bin/env python3
"""Exact Q8 Schur-orthogonality checks of SU(2) 2D face-block character identity.

Q8 has an irreducible 2D defining representation, so its first matrix moment
and U tensor U^{-1} orthogonality match normalized SU(2) Haar. Each internal
edge occurs once in each of its two adjacent plaquette characters. Finite
Q8 enumeration is therefore an EXACT cross-check of that Haar integration,
NOT a simulation of interacting Yang--Mills or a proof by finite sampling.
"""
from __future__ import annotations
import argparse,itertools,json
from fractions import Fraction
from pathlib import Path

I=(1,0,0,0)
Q8=[tuple(s*int(i==j) for i in range(4)) for j in range(4) for s in (-1,1)]

def mul(a,b):
 a0,x,y,z=a;b0,u,v,w=b
 return (a0*b0-x*u-y*v-z*w,
         a0*u+x*b0+y*w-z*v,
         a0*v-x*w+y*b0+z*u,
         a0*w+x*v-y*u+z*b0)

def inv(a):return (a[0],-a[1],-a[2],-a[3])

def product(factors):
 out=I
 for x in factors:out=mul(out,x)
 return out

def face_holonomy(e,x,y):
 return product([e['h',x,y],e['v',x+1,y],inv(e['h',x,y+1]),inv(e['v',x,y])])

def boundary_holonomy(e,nx,ny):
 return product([e['h',x,0] for x in range(nx)]
                +[e['v',nx,y] for y in range(ny)]
                +[inv(e['h',x,ny]) for x in range(nx-1,-1,-1)]
                +[inv(e['v',0,y]) for y in range(ny-1,-1,-1)])

def audit(nx,ny,case):
 F=nx*ny
 edges={('h',x,y) for x in range(nx) for y in range(ny+1)}|{('v',x,y) for x in range(nx+1) for y in range(ny)}
 internal=sorted([e for e in edges if (e[0]=='h' and 0<e[2]<ny) or (e[0]=='v' and 0<e[1]<nx)])
 boundary=sorted(edges-set(internal))
 assert len(internal)==(ny-1)*nx+(nx-1)*ny
 config={e:I for e in boundary}
 # Different nontrivial boundary values test orientation and gauge covariance.
 if case=='negative':config[boundary[0]]=(-1,0,0,0)
 if case=='traceless':config[boundary[0]]=(0,1,0,0)
 if case=='noncommuting':
  config[boundary[0]]=(0,1,0,0)
  config[boundary[-1]]=(0,0,1,0)
 if case=='conjugate':
  for k,e in enumerate(boundary):config[e]=Q8[(3*k+1)%8]
 expectation=Fraction(2*boundary_holonomy(config,nx,ny)[0],2**(F-1))
 total=8**len(internal)
 sums=[0]*(1<<F)
 if total>5000:raise ValueError('Exact enumeration cap for regression; theorem is for all disks')
 for vals in itertools.product(Q8,repeat=len(internal)):
  e=dict(config);e.update(zip(internal,vals))
  chis=[2*face_holonomy(e,x,y)[0] for x in range(nx) for y in range(ny)]
  # Exhaust all squarefree monomials; any proper nonempty subset has an exposed interior edge.
  monomials=[1]
  for mask in range(1,1<<F):
   j=(mask & -mask).bit_length()-1
   monomials.append(monomials[mask^(1<<j)]*chis[j])
  for mask,v in enumerate(monomials):sums[mask]+=v
 actual=Fraction(sums[-1],total)
 assert actual==expectation,(nx,ny,case,actual,expectation)
 assert all(sums[mask]==0 for mask in range(1,(1<<F)-1)),(nx,ny,case,'proper subset fails')
 assert sums[0]==total
 return dict(nx=nx,ny=ny,F=F,case=case,internal_edges=len(internal),Q8_assignments=total,
             coarse_boundary_character=2*boundary_holonomy(config,nx,ny)[0],
             expected_full_product=str(expectation),actual_full_product=str(actual),
             nonempty_proper_subsets_checked=(1<<F)-2,status='PASS')

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path('docs/evidence/R3_CUBIC_FACE_BLOCK_HAAR_2026-11-05.json'));a=p.parse_args()
 cases=['identity','negative','traceless','noncommuting','conjugate']
 rows=[]
 for nx,ny in [(1,2),(1,3),(2,2)]:
  for case in cases:rows.append(audit(nx,ny,case))
 result={'status':'PASS','identity':'For a simply connected rectangular fine face block with F elementary faces and boundary holonomy W, Haar average of the product of all F fundamental face characters over internal fine edges equals 2^(1-F) chi_1(W). For any proper nonempty subset of the faces, average is zero.',
 'mathematical_input':'SU(2) Schur orthogonality of fundamental matrix elements, plus Euler disk incidence V_int-E_int=1-F. Exact Q8 averaging is a representation-theoretically valid regression for the internal-edge moments.',
 'caveats':['Q8 finite verification is not the analytic proof for every finite disk.', 'This is kinematic Haar conditional expectation, NOT an interacting effective action or physical-time correlation.', 'Only un-repeated squarefree products of selected elementary plaquette characters are addressed in the vanishing statement.', 'The full-block term is quartic only at a single dyadic refinement; no interacting multiscale uniform estimate is proved.'], 'rows':rows}
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS: ',len(rows),'exact Q8-orthogonality cases; 2x2 block coefficient 1/8; all nonempty proper subsets vanish')

if __name__=='__main__':main()
