def factorial(n):
    prod = 1
    for i in range (1,n+1):
        prod *= i
    return prod
n = int(input())
print(factorial(n))