a,b = map(int, input().split())
if(b < a):
    for i in range(b,a):
        b += 1
        a -= 1
elif(b > a):
    for i in range(a,b):
        a += 1
        b -= 1
else:
    print(a,b)
        
print(a,b)
        