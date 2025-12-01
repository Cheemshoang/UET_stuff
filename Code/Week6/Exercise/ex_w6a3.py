a = int(input())

def check(a) -> bool:
    if a == 0 or a == 1: return False
    
    i = 2
    while(i**2 <= a):
        if a%i == 0: return False
        i += 1
    
    return True
        
print(check(a))
