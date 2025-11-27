def max_of_two(a,b) -> int:
    if a >= b:
        return a
    else:
        return b

a,b = list(map(int, input().split()))

print(max_of_two(a,b))