x = int(input())
a = list(map(int, input().split()))
ans = []
for idx, val in enumerate(a):
    if val < x:
        ans.append(idx+1)
if not ans:
    print(-1)
else: 
    print(ans)