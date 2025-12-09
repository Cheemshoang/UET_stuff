l1 = list(map(int, input().split()))
k = int(input())
ans = list()
seen = set()
for x in l1:
    if k-x in seen:
        ans.append((k-x,x))
    seen.add(x)
    
ans.sort(key = lambda t: t[0])
print(ans)