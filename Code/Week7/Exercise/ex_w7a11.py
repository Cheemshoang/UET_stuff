tup = tuple(map(int, input().split()))
tup_1 = list()
tup_2 = list()
for i in tup:
    if i%2 == 0:
        tup_1.append(i)
    else: 
        tup_2.append(i)
print(tuple(tup_1))
print(tuple(tup_2))
