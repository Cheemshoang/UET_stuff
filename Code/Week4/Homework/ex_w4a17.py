a, b, c, d = list(map(int, input().split()))
if b%a == 0:
    k = b/a
    if b*k == c and c*k == d:
        print("Yes")
    else:
        print("No")
else:
    print("No")