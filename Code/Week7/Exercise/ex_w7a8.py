arr = list(map(str, input().spilt()))
dick = dict()
for i in arr:
    if i not in dick:
        dick[i] = 1
    else:
        dick[i] += 1
print(dick)