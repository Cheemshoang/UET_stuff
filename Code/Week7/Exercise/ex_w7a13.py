from typing import Dict
parts = input().split()
d = {}

for p in parts:
    k, v = p.split(":")
    d[k] = int(v)

def rev(d1: Dict) -> Dict:
    d2 = {}
    for k,v in d1.items():
        d2[v] = k
    return d2
print(rev(d))