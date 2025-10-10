def distinct(n):
    s = str(n)
    return len(set(s)) == len(s)

def find_square(n):
    ans = []
    i = 0
    while True:
        square = i * i
        if square > n:
            break
        if distinct(square):
            ans.append(square)
            
        i += 1
    return ans

n = int(input())
res = find_square(n);
if not res:
    print("No")

else:
    print(' '.join(map(str, res)))