l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
ans = list()
for i in l1:
    if i in l2 and i not in ans:
        ans.append(i)
print(ans)