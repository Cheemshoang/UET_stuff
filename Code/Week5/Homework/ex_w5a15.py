m, n = list(map(int, input().split()))

y = (n - 2*m)/2
x = m - y
if isinstance(x, int) and isinstance(y, int):
    print(f"Ga: {x}, Cho: {y}")
else:
    print("Invalid")
