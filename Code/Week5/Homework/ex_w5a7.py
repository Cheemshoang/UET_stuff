def prime(n):
    if n < 2:
        return False
    
    
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    
    
    return True
found = False
n = int(input())
i = n
while i > 2:
    if prime(i) and n%i:
        print(i)
        break
    i = i - 1
