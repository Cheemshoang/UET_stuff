arr = list(map(int, input().split()))
mp = {}
for i in arr:
    if i not in mp:
        mp[i] = 1
    else:
        mp[i] += 1
best_num = 1e9
best_cnt = -1
for num, count in mp.items():
    if count > best_cnt:
        best_cnt = count
        best_num = num
    elif count == best_cnt:
        if num < best_num:
            best_num = num
