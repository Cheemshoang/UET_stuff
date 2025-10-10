def collatz(n):
    cnt = 0
    serie = []
    serie.append(n)
    while n > 1:
        if n%2 == 0:
            n = n//2
            cnt += 1
            serie.append(n)
        else:
            n = 3*n +1
            cnt += 1
            serie.append(n)
    
    return cnt, serie 
    
n = int(input())
cnt_max = 0
serie_max = []
i_max = 0
for i in range(1, n+1):
    cnt_i, serie_i = collatz(i)
    if cnt_i > cnt_max:
        i_max = i
        cnt_max = cnt_i
        serie_max = serie_i
    elif cnt_i == cnt_max:
        if i < i_max:
            i_max = i
            serie_max = serie_i
        
print(f"number{i_max}, step{cnt_max}, list{serie_max}")
    
            