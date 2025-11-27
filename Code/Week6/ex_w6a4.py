import math
def check(n):
    sum = 0
    for i in range(1, math.sqrt(n)):
        if n%i == 0: sum += i
        if n/i != n: sum += n/i
    
    if sum == n: return True
    return False