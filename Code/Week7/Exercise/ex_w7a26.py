a = list(map(int, input().split()))
sum = 0

for i in range(1, len(a) - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        sum += a[i]

print(sum)