a = list(map(str, input().split()))
d = dict()
for idx, val in enumerate(a):
    if val not in d:
        d[val] = (idx,)
    else:
        d[val] += (idx,)
print(d)
    