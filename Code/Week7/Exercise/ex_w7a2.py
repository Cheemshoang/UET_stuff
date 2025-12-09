from typing import List

ar = list(map(int, input().split()))
def check(arr: List[int]) -> List[int]:
    ttl = []
    sum = 0
    for num in arr:
        sum += num
        ttl.append(sum)
    return ttl

print(check(ar))