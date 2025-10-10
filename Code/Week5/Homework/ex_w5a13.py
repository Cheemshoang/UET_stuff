def sum_div(n):
    sum = 0
    for i in range (1,n):
        if n%i == 0:
            sum += i
            
    return sum
a,b = list(map(int, input().split()))
if sum_div(a) == b and sum_div(b) == a:
    print("True")
else: 
    print("False")