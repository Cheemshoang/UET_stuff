import math
def check(n):
    sum = 1
    for i in range(2, int(math.sqrt(n))+ 1):
        if n%i == 0:
            sum += i
            if i != n//i:
                sum += n//i
    
    return sum == n
n = int(input())
print(check(n))
