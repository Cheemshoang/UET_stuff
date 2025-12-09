a = list(map(int, input().split()))
k = int(input())
found = False
for idx, val in enumerate(a):
    if val == k:
        print(idx+1)
        found = True
        break

if not found: print(-1)
    