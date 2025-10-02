a, b, c = list(map(int, input().split()))
if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print("Tam giac deu")
    elif a == b or b == c or c == a:
        print("Tam giac can")
    else:
        print("Tam giac thuong")
else:
    print("Khong phai tam giac")