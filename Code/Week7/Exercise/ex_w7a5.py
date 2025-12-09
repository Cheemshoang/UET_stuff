arr = list(map(int, input().split()))

nums = {
    'pos': 0,
    'zero': 0,
    'nega': 0
}
for i in arr:
    if i < 0: nums['nega'] += 1
    elif i > 0: nums['pos'] += 1
    else: nums['zero'] += 1
print(nums)