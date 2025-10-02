a, b= list(map(int, input().split()))
if a == 0:
    if b == 0:
        print("vo so nghiem")
    else:
        print("vo nhgiem")
else:
    print(round(-b/a), 2)