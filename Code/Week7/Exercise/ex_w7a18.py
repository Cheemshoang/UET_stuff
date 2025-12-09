n, m, k = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
sum = 0
for i in range(n):
    sum += a[i][k-1]
print(sum)