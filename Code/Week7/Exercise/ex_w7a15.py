from typing import Dict
parts = input().split()
d = {}

for p in parts:
    k, v = p.split(":")
    d[k] = int(v)

ks = int(input())
ans = {}
for k,v in d.items():
    if v > ks:
        ans[k] = v
print(ans)