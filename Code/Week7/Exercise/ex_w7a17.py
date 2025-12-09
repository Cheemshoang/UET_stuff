n = int(input())
la = list()
lb = list()

a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: la.append(a[i][j])
        elif i + j == n-1: lb.append(a[i][j])

print(la, lb)