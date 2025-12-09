a = list(map(int, input().split()))
max = -1e9
for i in a:
    if i > max:
        max = i
print(max)