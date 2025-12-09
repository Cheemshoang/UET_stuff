tup = tuple(map(int, input().split()))
l = len(tup)
tup_1 = tup[0:1] + tup[l-2:0:-1] + tup[l-1:]
print(tup_1)