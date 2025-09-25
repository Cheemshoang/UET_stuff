import math as m
a,b,c = map(float, input().split())
if a + b > c and b + c > a and c + a > b:
    s = (a + b + c)/2
    area = m.sqrt(s * (s - a) * (s - b) * (s - c))
    print(round(area, 1))
else:
    print("Khong phai 3 canh cua tam giac")
    