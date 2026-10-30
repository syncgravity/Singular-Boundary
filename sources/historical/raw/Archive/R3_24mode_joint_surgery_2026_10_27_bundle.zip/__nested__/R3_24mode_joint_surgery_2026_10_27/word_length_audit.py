"""Exact group-word lengths for 59-pivot flat gluing after full expansion."""
import json
from pathlib import Path
P=Path(__file__).resolve().parent

def inv(w):return tuple(-x for x in reversed(w))
def red(w):
    z=[]
    for a in w:
        if z and z[-1]==-a:z.pop()
        else:z.append(a)
    return tuple(z)
for kind in ['joint','joint_optimized']:
 dat=json.loads((P/('relative_words_'+kind+'.json')).read_text());ops=dat['operations'];rep={}
 records=[]
 for op in reversed(ops):
  x=op['edge']+1
  # Expand signed relator substitutions in reverse order by literal group words.
  new=[]
  for a in op['replacement_word']:
   w=rep[abs(a)] if abs(a) in rep else (abs(a),)
   new.extend(w if a>0 else inv(w))
  rep[x]=red(new)
  records.append((int(op['edge']),len(rep[x])))
 from collections import Counter
 occurrences=Counter(x for w in rep.values() for x in map(abs,w))
 maxword=max(l for e,l in records)
 print(kind,'max expanded word',maxword,'sum lengths',sum(l for e,l in records),'worst',sorted(records,key=lambda x:-x[1])[:8])
 (P/('word_lengths_'+kind+'.json')).write_text(json.dumps({'max_expanded_link_word_length':maxword,'sum_expanded_lengths':sum(l for e,l in records),'max_frozen_or_free_symbol_overlap':max(occurrences.values()),'symbols_in_expanded_words':len(occurrences),'lengths_by_link':{str(e):l for e,l in sorted(records)}, 'symbol_occurrence_counts':{str(k):v for k,v in sorted(occurrences.items())}},indent=2))
