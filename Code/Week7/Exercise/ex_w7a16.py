n, m = map(int, input().split())
#moi dong la mot list
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    # mỗi phần tử in width=4, căn phải
    print(''.join(f"{x:4d}" for x in a[i]))