n = int(input())
cnt = 0

while n > 0:
    cnt += 1
    n = n// 10
    
print(cnt)