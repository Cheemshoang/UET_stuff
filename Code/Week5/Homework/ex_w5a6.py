def prime(n):
    if n < 2:
        return False
    
    
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    
    
    return True


a, b = list(map(int, input().split()))
sum = 0
for i in range (a, b+1):
    if prime(i):
        sum += i
        
print(sum)