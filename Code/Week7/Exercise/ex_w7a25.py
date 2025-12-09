N = int(input())
a = list(map(int, input().split()))
seen = [False]*10

for x in a:
    seen[x] = True
ans = []
for d in range(10):
    if not seen[d]:
        ans.append(d)

print(ans)