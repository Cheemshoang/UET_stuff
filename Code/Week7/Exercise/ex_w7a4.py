arr = input().split()
res = dict()

for i in arr:
    k,v = i.split(':')
    
    if k not in res: res[k] = []
    res[k].append(v)
print(res)