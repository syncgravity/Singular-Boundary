#!/usr/bin/env python3
"""Nonabelian relative Tietze elimination for 14-face affected retained patch.
58/59 pivots possible? audit residual frozen-exterior relators and word growth.
"""
import json
from pathlib import Path
from collections import Counter
from direct_cut_project import build
from construct_surgery import product_collar
from cavity_audit import seed_support,Q_from_seed
from classify_modes import analyze,link_key
P=Path(__file__).resolve().parent

def reduce(w,cyclic=True):
    stack=[]
    for x in w:
        if stack and stack[-1]==-x:stack.pop()
        else:stack.append(x)
    if cyclic:
        while len(stack)>1 and stack[0]==-stack[-1]:stack=stack[1:-1]
    return stack

def inverse(w):return [-x for x in reversed(w)]

def solve(joint=True, optimized=False, radius=5.):
    g,_=build(radius,0);words,meta=product_collar(g);Q=Q_from_seed(g,seed_support(g));R=set(range(len(words)))-Q
    H={e for f in Q for e,s in words[f]}; A=sorted(p for p in R if any(e in H for e,s in words[p]));outside=([next(e for e in range(3*(len(g.labels)+len(g.edges))) if link_key(g,e)==key) for key in json.loads((P/'optimized_basis.json').read_text())['best_basis_z5_labels']] if optimized else analyze(g)[0]['chosen_exterior_link_ids'])
    local={e+1 for e in H| (set(outside) if joint else set())}
    rel={f:reduce([s*(e+1) for e,s in words[f]]) for f in A}
    # Avoid change of relator by cyclic conjugation every time? cyclic relators equivalent as group relations.
    ops=[]
    for iteration in range(90):
        count=Counter(abs(x) for w in rel.values() for x in w if abs(x) in local)
        candidates=[]
        for f,w in rel.items():
            seen=Counter(abs(x) for x in w)
            for j,x in enumerate(w):
                if abs(x) in local and seen[abs(x)]==1:
                    c=(len(w)-1)*max(count[abs(x)]-1,0)
                    candidates.append((c,len(w),f,j))
        if not candidates:break
        cost,ll,f,j=min(candidates);w=rel.pop(f);x=w[j];rest=w[j+1:]+w[:j]
        val=inverse(rest) if x>0 else rest;rep={abs(x):val,-abs(x):inverse(val)}
        for ff,ww in list(rel.items()):
            next_w=[]
            for z in ww:next_w.extend(rep[z] if abs(z)==abs(x) else [z])
            rel[ff]=reduce(next_w)
        local.remove(abs(x));ops.append({'face':f,'edge':abs(x)-1,'word_length':len(w),'replacement_len':len(val),'replacement_word':val, 'max_remaining_len':max(map(len,rel.values()),default=0)})
        if max((len(w) for w in rel.values()),default=0)>50000:break
    nonempty=[(f,w) for f,w in rel.items() if w]
    report={'joint':joint,'optimized':optimized,'radius':radius,'faces':len(A),'Hlinks':len(H),'outside_links':len(outside) if joint else 0,'solved_count':len(ops), 'active_left':len(local),'nonempty_relators':len(nonempty),'max_nonempty_length':max((len(w) for f,w in nonempty),default=0), 'max_substitution_length':max((a['replacement_len'] for a in ops),default=0), 'operations':ops, 'residual':{str(f):w[:200] for f,w in nonempty[:15]},'residual_frozen_only_count':sum(not any(abs(t) in local for t in w) for f,w in nonempty)}
    (P/(('relative_words_joint_optimized.json' if optimized else 'relative_words_joint.json') if joint else 'relative_words_initial.json')).write_text(json.dumps(report,indent=2)) if radius==5. else None
    print('joint',joint,'solved',len(ops),'left active',len(local),'nonempty',len(nonempty),'max rest',report['max_nonempty_length'],'max substitution',report['max_substitution_length'],flush=True)
    return report
if __name__=='__main__':solve(False);solve(True)
