a = list(map(int, input().split()))

inc = True   
dec = True   

for i in range(1, len(a)):
    if a[i] <= a[i-1]:
        inc = False
    if a[i] >= a[i-1]:
        dec = False

if inc:
    print("Day tang thuc su")
elif dec:
    print("Day giam thuc su")
else:
    print("Vo danh")
