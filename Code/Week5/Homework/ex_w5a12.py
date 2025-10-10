x, n = list(map(int, input().split()))

for i in range (n):
    x = x * 1.07
    
print(round(x))