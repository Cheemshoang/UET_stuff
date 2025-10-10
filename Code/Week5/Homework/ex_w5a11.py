n = int(input())
cnt = 0
for i in range (1,n+1):
    if n%i == 0 and i%2 == 0:
        cnt += 1
print(cnt)